init python:
    Event(**{
    "name": "reona_hottub_sex_male",
    "label": "reona_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            IsActivity("date_hot_tub_home")),
        PersonTarget(reona,
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

label reona_hottub_sex_male:
    $ CONDOM = False
    scene bg pool
    "I've spent most of the day getting everything ready for Reona coming over."
    "The space around the hot-tub has never been cleaner or more pristine."
    "I've scrubbed out the tub and filled it with fresh, crystal-clear water."
    "I also found the time to make sure the mood-lighting is working too."
    "Then I raided the house for all the candles that I could find to bring out here."
    "I just have to hope that [bree.name] and Sasha don't miss them before Reona's been and gone!"
    "Finally I bought the perfect bottle of wine and scattered flower-petals all over the place."
    "So when I stand back and take a look at the result, I can't help being impressed."
    "Because it looks like I got this whole romantic thing nailed!"
    "I'm still admiring my handiwork when I hear the sound of approaching footsteps."
    "That could well be Reona, as it's about the time I asked her to come over."
    "And when I also hear the sound of her voice, all doubt is banished."
    reona.say "Hey, [hero.name]..."
    reona.say "Where the hell are you?"
    reona.say "Nobody answered the door..."
    reona.say "So you gotta be back here, right?"
    show reona at left with easeinleft
    "I turn around just in time to see Reona walk round the corner of the house."
    "And as she does so, I can't help a smile spreading across my face."
    show reona at center with ease
    "Because she looks just as good as I hoped she would!"
    "As usual, Reona's wearing as little as she can possibly get away with."
    "And I'm assuming that she has her swimming costume on under it too."
    "Which must also mean that it's got to be microscopic!"
    mike.say "Oh..."
    mike.say "Hi, Reona..."
    mike.say "Yeah...I'm just getting things ready."
    mike.say "Making sure everything's perfect, you know?"
    show reona interested
    "Reona gives me a lop-sided glance."
    show reona happy at startle
    "And then she lets out a snort of laughter."
    reona.say "Ha!"
    reona.say "Someone's been reading cheesy romance novels!"
    reona.say "Subdued lighting, candles...and rose petals!"
    reona.say "I thought it was only girls that fell for all that stuff?!?"
    "I can't help feeling more than a little surprised at what I'm hearing."
    "And I guess that it must show on my face too, as Reona shakes her head."
    show reona surprised
    reona.say "Oh shit..."
    reona.say "You're not kidding, are you?"
    reona.say "You've really bought into all of this!"
    show reona embarrassed
    mike.say "Yeah..."
    mike.say "No..."
    mike.say "I mean..."
    mike.say "I was just trying to make it romantic, that's all!"
    show reona annoyed
    "Reona rolls her eyes at this."
    reona.say "Then why didn't you say so?"
    show reona normal
    reona.say "When someone says come over and jump in the hot-tub..."
    reona.say "I'm always gonna think they mean come over and fuck in the hot-tub!"
    "I find myself staring at Reona in amazement."
    mike.say "R...really?!?"
    mike.say "I mean we can do that..."
    mike.say "Obviously I was hoping we would..."
    show reona devious
    reona.say "Okay, okay..."
    reona.say "Slow down, Mister Romance!"
    reona.say "You went to the trouble of buying wine."
    reona.say "So let's have some of that first!"
    "I nod and hurry to grab the bottle and two glasses."
    "Then I fill them both and turn to hand one to Reona."
    "But I stop, frozen to the spot as I see what she's doing."
    $ game.active_date.clothes = "swimsuit"
    show reona swimsuit with dissolve
    "And that's tearing off the last of her clothes and tossing them aside."
    "Which reveals the swimsuit Reona's wearing in all its glory."
    "Honestly, I don't think I've ever seen clothing that made someone look so naked!"
    show reona happy
    reona.say "So, you like what you see, huh?"
    "I nod slowly as Reona grabs one of the glasses from me."
    "And I watch as she downs the contents in one swallow."
    reona.say "Meh..."
    reona.say "This stuff is okay, I guess."
    reona.say "Usually I like something way stronger."
    "The next thing I know, Reona's taken hold of my hand."
    show hottub reona with fade
    show hottub reona swimsuit
    "And she's leading me to the edge of the hot-tub."
    "She takes a step into the water, turning to pull me in too."
    "As we sink into the warm, bubbling liquid, Reona wraps her arms around my neck."
    reona.say "You know..."
    reona.say "This romantic crap is all well and good."
    reona.say "But the thing is, it just means I have to wait."
    reona.say "It's something else between me and what I want."
    reona.say "And I hate to have to wait for what I want!"
    "At this point she's looking straight into my eyes."
    "And the effect of that is pretty hypnotic."
    "So much so that I hardly notice she's pulled my trunks halfway off already!"
    "Sure, I could protest."
    "I could demand that she stop and enjoy the romantic ambiance I spent so long creating."
    "But who am I trying to kid?"
    "If a girl as hot as Reona wants to pull off my trunks, then I'm going to let her!"
    "Reona's hand emerges from the water a moment later, clutching my trunks."
    "And she wastes no time in tossing them over her shoulder."
    "This seems to act as a signal for me, a subliminal cue."
    "Because the next thing I know, I'm tearing at Reona's swimming costume."
    "My hands are all over her as I desperately try to pull it off."
    "But my clumsy efforts don't seem to bother her in the slightest."
    "In fact, they seem to do quite the opposite."
    "As Reona is happy to let me keep going until I finally succeed."
    "But as soon as she's naked, she makes a play to take back control."
    "I reach for Reona, desperate to take hold of her body."
    "But she twists and turns in the water, leaving me empty-handed."
    mike.say "Huh..."
    mike.say "What the..."
    mike.say "Where's you go?"
    "Reona chuckles as she easily evades me."
    "She slips through the water with ease, always out of reach."
    "By comparison, I splash around as I flounder in her wake."
    "I can't make sense of what she's doing or why."
    "A moment ago she was demanding that I fuck her."
    "But now she's doing everything she can to avoid me!"
    "Eventually, by some minor miracle, I finally manage to catch Reona."
    "And once I do, there's only one thing on my mind."
    "Wrapping my arms around her, I press my belly against her back."
    "To my surprise, she doesn't try to wriggle free or resist in any way."
    show hottub sex male reona outside with fade
    "In fact she leans backwards, pushing her ass against my groin."
    "It's only when I hear the sound of her filthy giggles that I realise what's going on."
    "I thought I was the one trying to catch Reona."
    "But the truth is she was leading me on the whole time."
    "Teasing me to the point where I couldn't control myself."
    "And now she's got me right where she wants me."
    "The realisation doesn't make me want to stop."
    "Instead it makes me all the more determined to press on."
    "To show Reona just what I'm capable of under pressure!"
    "What takes over in my now is pure base instinct."
    "The simple desire have my way with Reona."
    "And in doing so find a release from the pressure she's built up in me."
    "My cock is as hard as it's possible to get."
    "But my hold on Reona's waist is almost as hard too."
    "And when I pull her backwards and onto me, I feel the state she's in too."
    show hottub sex male reona inside
    "The lips of Reona's pussy are hot and slick, slippery to the touch."
    "There's only the slightest moment of resistance before the inevitable happens."
    "All it takes is one more thrust, and she opens to me like a flower to the light."
    show hottub sex male at startle(0.05,-10)
    "I keep on pulling her back and pushing myself forwards."
    "And soon enough I'm sinking all the way in."
    "I don't stop until there's no room to go further."
    show hottub sex male at startle(0.05,-10)
    "And then I begin to move in and out in earnest."
    "Up to now, Reona's been quiet, almost like she was unable to make a sound."
    show hottub sex male at startle(0.05,-10)
    "But all of that changes as I begin to pick up speed."
    "Within seconds I can hear the sound of her panting."
    "Then she starts to moan."
    show hottub sex male at startle(0.05,-10)
    "Finally the sounds she's making turn into cries."
    "And it's clear they're cries of sheer and helpless pleasure."
    "Reona bounces up and down in my lap, breasts bouncing as buttocks slapping."
    show hottub sex male at startle(0.05,-10)
    "Her hands clench into fists, nails digging into her palms."
    "And then they begin to roam over her body."
    "I see them pinching and squeezing as they go."
    show hottub sex male at startle(0.05,-10)
    "As if she's trying to find a way to release the pleasure she's feeling."
    "Reona does look like it's steadily building up inside of her."
    "Like it won't be long before she can't take any more."
    show hottub sex male at startle(0.05,-10)
    "I know this from the sounds that Reona's making."
    "But also from the way that she's holding onto me tighter than ever."
    "And by that I don't just mean the grip of her hands."
    show hottub sex male at startle(0.05,-10)
    "I can already feel the muscles of her pussy clenching like a fist."
    "The sensation is enough to speed up the arrival of my own climax too."
    show hottub sex male ahegao at startle(0.05,-10)
    "So when Reona finally succumbs to her orgasm, I follow on her heels."
    show hottub cumshot inside with vpunch
    $ reona.impregnate()
    $ reona.sub += 1
    "Letting go, I shoot everything that I have into her."
    with vpunch
    "And only then to I feel her body go limp."
    with vpunch
    "Once it's over, neither of us seems to be able to move a muscle."
    "We simply float in the water, still gripped by the afterglow."
    "But Reona's the first one to regain the power of speech."
    show hottub sex male -ahegao
    "She chuckles and makes a deep groan of satisfaction."
    reona.say "Now, we can enjoy all the romantic shit, [hero.name]..."
    reona.say "Now we've earned it!"
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ reona.sexperience += 1
    $ game.active_date.clothes = None
    return

label reona_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg street
    show reona


    call reona_fuck_date_intro_male (location) from _call_reona_fuck_date_intro


    call reona_dick_reactions from _call_reona_dick_reactions


    call reona_fuck_date_foreplay_male from _call_reona_fuck_date_foreplay_male


    call reona_fuck_date_choices_male from _call_reona_fuck_date_choices_male


    call handle_npc_leaving (reona, _return) from _call_handle_npc_leaving_29
    if _return:
        return


    hide reona
    call reona_fuck_date_sleep (location="hero") from _call_reona_fuck_date_sleep
    return

label reona_fuck_date_intro_male(location="hero"):
    $ rand_intro = game.days_played % 5
    if rand_intro == 0:
        scene bg house
        show reona happy
        with fade
        "As soon as Reona and I arrive back on the doorstep of my place, I know exactly how I want this to go."
        "I make a point of unlocking the door and throwing it open, then gesturing for her to hurry inside."
        "But the effect is kind of ruined by the way I flinch when the door slams loudly against the wall."
        mike.say "This way, madame..."
        scene bg livingroom
        show reona happy
        with fade
        pause 1
        show reona surprised
        mike.say "WHOA!"
        mike.say "Erm...maybe that was a little loud..."
        show reona normal
        "Reona doesn't seem to be in the least bit annoyed with either the noise or my cringing from it."
        "Instead she strides straight into the hallway, already laughing at my efforts to impress her."
        reona.say "Oh, [hero.name]…"
        show reona flirt
        reona.say "If you think that's loud, wait until we get to your bedroom."
        reona.say "Because I promise you we're gonna make enough noise to raise the dead!"
        "I have to say that all of this leaves me feeling more than a little conflicted."
        "On the one hand I'm eager to see just what Reona means by that."
        "And so my instinct is to follow at her heels like an obedient hound."
        "But then I remember that I did have an agenda for tonight."
        "I wanted to show Reona that I'm capable of amazing her."
        "That I can do things in the bedroom that'll make her swoon too."
        "So once I have the door locked behind us, I scurry in front of Reona again."
        mike.say "My thoughts exactly, Reona!"
        mike.say "So let's not beat about the bush, yeah?"
        mike.say "My room's right this way."
        show reona happy
        "Much to my delight, Reona nods and smiles."
        "In fact, she seems more than happy to let me take the lead."
        "She holds out her hand for me to take, and then lets me guide her to our ultimate destination."
        "This makes me all the more keen to hurry her along, constantly glancing back over my shoulder."
        show reona normal
        "And every time I do this, Reona's amusement seems to increase."
        "By the time we make it to the door, she's laughing out loud."
        "But I have to let go of her hand in order to close the door behind us."
        "I do this as hastily as I possibly can, hurrying to follow Reona."
        scene bg bedroom1
        show reona flirt
        with fade
        "Yet when I turn around, I see that she hasn't bothered to wait for me."
        "Instead Reona's used the few seconds I was distracted to make it to my bed."
        "And now she's leaning back against the pillows, pulling up her skirt!"
        "For a moment I feel like I'm frozen in place, unable to move a muscle."
        "Reona must realise this, because her smile becomes even more wicked than before."
        "On top of that, she stops hiking up her skirt."
        "And instead she begins to pull down her panties instead."
        show reona happy
        reona.say "You know what, [hero.name]…"
        reona.say "I get the feeling that you've got something you want to show me."
        reona.say "Maybe something that you feel like you've got to prove to me."
        reona.say "Which is all well and good."
        show reona normal
        reona.say "But I've got something I want to show you first."
        reona.say "Something to motivate you..."
        "It's only when I can finally see what's between Reona's legs that the spell is broken."
        show reona flirt bottomless with dissolve
        "As soon as she pulls her panties down far enough and reveals her pussy for the first time."
        "That's the exact moment when I regain control of my body, when I feel myself able to move again."
        "And once I feel like I can do that, I don't hesitate to take full advantage."
    elif rand_intro == 1:
        scene bg house
        show reona
        with fade
        "I'm kind of on a high when Reona and I make it back to my place tonight."
        "The date we've just been on went way better than I could have hoped."
        "And I keep picking up what I think are super-positive vibes from her too."
        "But I'm always trying to be that kind of modern guy who's no way a creep."
        "So I do my best not to let it show that I'm hoping to get some action tonight."
        "Which is pretty hard when you're dating a girl as hot and flirtatious as Reona."
        scene bg livingroom
        show reona happy
        with fade
        reona.say "So..."
        reona.say "Here we are..."
        reona.say "You and me, at your place..."
        "Reona and I just stepped in the door and started walking towards my room."
        "I can hear the innuendo and mischief in her voice as easily as the words themselves."
        "And even without the need to look in her direction, Reona's already starting to turn me on!"
        mike.say "My room's just over here, Reona."
        mike.say "We can go in there and just chill, you know?"
        mike.say "See how the mood takes us?"
        "By now I'm opening the door to my room."
        "And I'm about to stand aside and let Reona go in first."
        scene bg livingroom with hpunch
        scene bg bedroom1
        "But that's when I feel a sudden shove from behind."
        "It catches me totally off-guard and sends me tumbling into my room."
        "I almost fall flat on my face, but somehow I manage to turn as I stumble."
        "And I end up on my ass, staring upwards in genuine surprise." with vpunch
        show reona embarrassed
        reona.say "Chill out?"
        reona.say "See how it goes?"
        show reona devious
        reona.say "Ha!"
        reona.say "Reona craves not these things!"
        "I watch as Reona closes the door behind her."
        "Then she turns and walks over to where I'm sitting on the floor."
        "I'd have gotten up already, but as Reona approaches me, she starts to strip-off."
        "And that means I'm entranced, left totally unable to move as I watch her."
        show reona underwear with dissolve
        "Almost unconsciously, I find myself following her example."
        "I'm pulling off my own clothes and tossing them aside without the need to be asked!"
        show reona naked with dissolve
        "By the time Reona reaches me, she's totally naked."
        "And I'm on my knees before her, looking up in silent amazement."
        show reona pensive
        "Reona cocks her head on one side as she looks down at me."
        reona.say "What are you doing down there, [hero.name]?"
        reona.say "You'd better get up if you want to put it in me."
        show reona devious
        reona.say "And believe me, you REALLY want to put it in me!"
        "That's all it takes for Reona to get me struggling to my feet."
        "And I'm nodding the whole time that I'm getting up too."
        mike.say "Sure thing, Reona..."
        mike.say "Just let me..."
        mike.say "Just let me get up!"
        show reona happy
        "Reona chuckles to herself as she watches my efforts to do as I'm told."
        "And I can see from the smile on her face that she approves of my enthusiasm too."
        reona.say "Mmm..."
        reona.say "Looks like you're ready for me after all!"
        reona.say "Now then..."
        reona.say "Just let me get myself into position!"
    elif rand_intro == 2:
        scene bg house
        show reona flirt
        with fade
        "I've been eager to get back to my place almost since the date Reona and I have been on started."
        "And that's not because of anything she's said or done."
        "Oh no, it's all on account of the way she's been looking at me."
        "I mean, you know that Reona's a pretty sensual kind of girl."
        "The kind that's full of a passion that she's not afraid of sharing."
        "A passion that she likes to show in a very physical way too."
        "Well I never knew that she could channel all of that passion into a single look!"
        "But that's precisely what she's been doing all night."
        "Every time I look up and catch Reona staring at me, she looks hungry as hell."
        "And I can tell that she's not hungering for anything other than me!"
        "Another girl might do the best she can to hide it, embarrassed at her desires."
        "But not Reona, oh no."
        "She might as well have the word 'horny' written on her forehead right now."
        "And as we get out of the taxi and walk up to the house, it all seems to come to a head."
        "Reona practically pushes me up the path and onto the porch."
        "Then she jostles me as I pull out my keys and try to open the door."
        show reona interested
        reona.say "Come on, come on..."
        reona.say "What's taking so long?!?"
        mike.say "Whoa..."
        mike.say "Hey, Reona..."
        mike.say "I'm going as fast as I can!"
        show reona annoyed
        reona.say "Well it's not fast enough!"
        "The very moment I have the door open, Reona pushes me inside."
        scene bg livingroom
        show reona interested
        with hpunch
        "I'm totally not expecting the shove she gives me, and so I stagger forwards."
        "And I believe that I would have landed on my face in the middle of the hallway."
        "That is if she hadn't been there to take me by the hand."
        reona.say "Your room's down there, right?"
        reona.say "Right?!?"
        mike.say "Y...yeah..."
        mike.say "Right down there..."
        "Reona doesn't dignify this with an answer."
        "Instead she begins dragging me towards my bedroom door."
        "I do the best I can to keep up with the pace she's setting."
        "But all the same, I end up almost falling more than once."
        "As soon as she reaches the door, Reona pushes it open."
        "Then she all but flings me inside as she slams it behind us."
        scene bg bedroom1
        show reona normal
        with fade
        "I turn and open my mouth to say something."
        "But Reona holds up a hand, cutting me off."
        "And even as she's doing this, I see that her clothes are already coming off."
        reona.say "No time for chit-chat, [hero.name]…"
        show reona flirt
        reona.say "You've got something I want."
        reona.say "Nah, scrub that - you've got something I need!"
        "I'm nodding like a fool the whole time Reona's saying all of this to me."
        "But for some reason I don't seem to be able to move a muscle."
        mike.say "You mean that..."
        mike.say "You want me to..."
        show reona pensive
        mike.say "So I should..."
        reona.say "Just take your clothes off and fuck me already!"
        show reona annoyed
        reona.say "Urgh..."
        reona.say "Why is that so hard for you to understand?!?"
        "Reona's frustrated words are what finally break the spell."
        "They see me begin to move, and I start tearing at my clothes."
        "All the time I'm nodding eagerly, trying to make up for my previous inaction."
        show reona underwear normal with dissolve
        "This also has the effect of mollifying Reona."
        "Not totally, but just enough so that I feel safer approaching her."
        show reona naked flirt with dissolve
        "Sure that she won't actually kill me once she gets her hands on me."
    elif rand_intro == 3:
        scene bg house
        show reona happy
        with fade
        "Reona already knows her way around my house from all the times she's been over here to study with me."
        "But I'm more than happy to say that by now our relationship has gone way beyond that stage."
        "And now she's using that knowledge to lead me to my bedroom door, and not for the purpose of hitting the books!"
        scene bg livingroom
        show reona happy at center, zoomAt(1.5, (640, 1040))
        with fade
        "All the way through the date we've just been on, Reona's been flirting heavily."
        "Well, I guess what she was doing counts as flirting for her."
        "For myself and almost any other girl, you'd probably call it offering herself up as a living sacrifice!"
        "But just to be clear, I have no problem with that at all, and I'm not resisting her efforts to lead me."
        "I'm eagerly following on Reona's heels, wanting to see just what she has in store for me."
        "In fact, I might be following a little too close."
        show reona surprised with hpunch
        reona.say "Ouch!"
        show reona sad
        reona.say "Hey, you just trod on my foot!"
        mike.say "Oops..."
        mike.say "Sorry, Reona."
        mike.say "I guess I'm just kind of excited, that's all."
        show reona devious
        "At the mention of my excitement, Reona seems to forget all about the pain in her foot."
        "Because I see a knowing smile spread across her face, and she nods at me."
        reona.say "And so you should be, [hero.name]."
        show reona normal
        reona.say "Time alone with me is always exciting."
        reona.say "Thrilling to - kind of like being on a roller-coaster!"
        "I'm nodding at every word coming out of Reona's mouth."
        "My head bobbing up and down the whole time."
        "So much so that I don't even realise we've reached the door to my bedroom."
        "Which means it comes as a surprise when she leads me in there and over to the bed."
        scene bg bedroom1
        show reona flirt
        with fade
        pause 1
        show reona underwear with dissolve
        "I stand there in silence, watching as Reona starts to strip off her clothes."
        "And I'd probably have remained like that without being given any more orders."
        "But it looks like Reona already has something else in mind for me."
        show reona annoyed
        reona.say "Don't just stand there staring, [hero.name]…"
        reona.say "Start getting undressed already!"
        mike.say "Oh..."
        mike.say "Okay!"
        show reona normal
        "I hurry to do as I'm told, tugging awkwardly at my clothes."
        "But all the time I'm still watching Reona as intently as before."
        show reona naked flirt with dissolve
        "By the time Reona's done and begins to walk over to the bed, I'm almost panting in anticipation."
    else:
        scene bg livingroom
        show reona happy
        with fade
        "I hold the door to my room open for Reona, and then watch as she strides in like she owns the place."
        "Not that I mind one bit, not after the good time we've just had on our date tonight."
        "And especially when it looks like there's more good things to come before it's over."
        scene bg bedroom1
        show reona underwear
        with fade
        "I say that because Reona doesn't waste any time once she's inside of my bedroom."
        "In fact she's already stripping off her clothes before I've even been able to close the door!"
        "Hastily slamming it behind me, I shake my head at Reona."
        mike.say "What are you doing, Reona?!?"
        mike.say "At least let me close the door first."
        "Reona looks back over her shoulder at me, already more than half-way undressed."
        "And from the look on her face, I can tell that she's not in the least bit concerned."
        show reona happy
        reona.say "Why would I wait for that, [hero.name]?"
        reona.say "What's the point in wasting valuable time?"
        mike.say "Because one of my housemates might have been walking past."
        mike.say "That's the point!"
        "Reona lets out a chuckle and shakes her head at this."
        reona.say "What's the matter, [hero.name]?"
        reona.say "Are you embarrassed to be seen with me?"
        mike.say "What?"
        mike.say "No...of course not!"
        show reona normal
        reona.say "Then maybe you're worried they might like what they see too?"
        show reona naked with dissolve
        "By this time, Reona's finished taking off her clothes."
        "And, of course, that means she's standing in front of me totally naked."
        "Only up until now, she's had her back turned to me, somewhat muting the effect."
        "But all of that changes the moment that Reona turns around to face me."
        "Now I'm hit by the sight of her all at once, and it literally stops me in my tracks."
        "Reona obviously knows exactly what she's doing, already giving me a knowing smile."
        show reona happy
        reona.say "You're right, [hero.name], I know that face."
        reona.say "And it's certainly not the one you pull when you're embarrassed!"
        "All I can do is stand there and nod, still robbed of the power of speech."
        "Reona walks over to the side of my bed and sits on the edge of the mattress."
        "She pats the spot beside her with one hand, while beckoning me closer with the other."
        show reona flirt
        reona.say "Why don't you come over here and sit beside me?"
        reona.say "You think that you can manage that?"
        "There's something about Reona's tone that snaps me out of my trance-like state."
        "I don't know if it's the slightly mocking way that she asks the question."
        "Or if it's more to do with the invitation to get close to her while she's naked."
        "But either way I find myself leaping into action the very second after she asks it."
        "One second I'm standing still, unable to move a muscle."
        "And the next I'm literally tearing at my clothes to get them off."
        "That and hurrying across the room and towards the bed."
        "I'm just about naked by the time I make it to Reona's side."
        "And I can't keep from throwing myself down on the bed next to her."
        show reona pensive
        "Which, of course, causes her to bounce upwards as I do so."
        reona.say "Whoa..."
        reona.say "Full marks for the enthusiasm, tiger!"
        show reona flirt
        reona.say "But there's no need to throw yourself around like that."
        mike.say "Huh?"
        mike.say "There isn't?"
        show reona happy
        reona.say "No, [hero.name]."
        reona.say "I'm going to be totally gentle with you tonight."
        mike.say "You are?"
        "Reona smiles at me as it's now my turn to be asking the questions."
        "At first she looks innocent and totally harmless."
        show reona devious
        "But then I watch as the smile on her face changes suddenly."
        "Specifically it goes from sweet to impish in mere seconds."
        reona.say "Nah..."
        reona.say "I was only kidding!"
    $ game.room = "bedroom1"
    return

label reona_fuck_date_foreplay_male:

    menu:
        "Eat her pussy":
            call reona_fuck_date_cunnilingus from _call_reona_fuck_date_cunnilingus
        "Demand a blowjob" if hero.sexperience >= 30:
            call reona_fuck_date_blowjob from _call_reona_fuck_date_blowjob
        "Fuck her right now":
            pass
    call stop_all_sfx from _call_stop_all_sfx_47

    return _return

label reona_fuck_date_choices_male:
    menu:
        "Missionary":
            call reona_fuck_date_missionary (0) from _call_reona_fuck_date_missionary
        "Cowgirl" if hero.sexperience >= 40:
            call reona_fuck_date_cowgirl (40) from _call_reona_fuck_date_cowgirl
        "Reverse cowgirl" if hero.sexperience >= 50:
            call reona_fuck_date_reverse_cowgirl (50) from _call_reona_fuck_date_reverse_cowgirl
        "Doggy" if hero.sexperience >= 60:
            call reona_fuck_date_doggy (60) from _call_reona_fuck_date_doggy
    call stop_all_sfx from _call_stop_all_sfx_48

    return _return

label reona_fuck_date_sleep(location="hero"):
    scene bg bedroom1
    if game.hour > 19 or game.hour < 6:
        show reona naked
        if reona.is_sex_slave:
            reona.say "May I share your bed tonight, Master?"
        else:
            reona.say "Mmm...you cool with me spending the night here?"
        menu:
            "No":
                mike.say "No...I have to be up really early in the morning."
                "The sex was beyond incredible, but now I want to be alone."
                "Reona frowns in disappointment, clearly trying to shrug off the sense of rejection."
                reona.say "Alright [hero.name], sleep well then."
                "She shakes her head as she collects her things and leaves my bedroom."
                $ reona.sub += 1
                call sleep from _call_sleep_99
            "Yes":
                mike.say "YES...I mean, yes...if you want to!"
                "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                show cuddle reona
                "Reona curling up against me beneath the covers is as good as the sex."
                reona.say "Mmmph... 'nn nigh... 'weet dre'ms..."
                mike.say "You too, Reona..."
                $ reona.love += 3
                call sleep ("reona") from _call_sleep_100
    return

label reona_fuck_date_cunnilingus:
    scene bg black
    show reona cunnilingus eyes_close finger naked
    with fade
    "All at once I find myself hurrying across the room towards Reona."
    "At the same time I'm pulling off my clothes too, just tossing them aside."
    "And when I make it to the bed, I don't stop to climb onto it."
    "Instead I launch myself into the air, landing right between Reona's legs."
    "Normally I'd be scared of breaking my bed by doing something like that."
    "But right now I hardly even notice the sound of it creaking under my weight."
    "That's because all of my attention is focussed on Reona."
    "Well, maybe it would be more accurate to say it's divided between two parts of her."
    "The first is obviously the prize that's positioned between her legs."
    "And the second is the look on her face, which is at once both amazed and excited."
    show reona cunnilingus deep
    pause 0.3
    show reona cunnilingus tip
    pause 0.3
    show reona cunnilingus deep
    pause 0.3
    show reona cunnilingus tip
    pause 0.3
    show reona cunnilingus deep
    pause 0.3
    show reona cunnilingus tip
    "I can't describe the thrill that Reona's expression is making me feel."
    "The knowledge that I'm the one thrilling and exciting her is intoxicating."
    "And it makes me all the more determined to press on with what I'm doing."
    show reona cunnilingus eyes_open
    mike.say "Just lie back and leave this to me, Reona."
    mike.say "I know what I'm doing."
    show reona cunnilingus -finger
    "I make the point of looking up at Reona one last time."
    "And I see that she still has the same look on her face as before."
    "But now she's also nodding eagerly, wanting to see what I have in mind."
    "That's more than enough to make me sure of what I'm going to do."
    "So I take a deep breath."
    "I put my hands on Reona's thighs."
    "Then I lower my head between them."
    show reona cunnilingus eyes_close mouth_pleasure mike
    "I think about closing my eyes as I do all of this."
    "Because the scent of Reona's pussy is already filling my senses."
    "It's like a perfect perfume, once that captures the essence of her sensuality."
    "I could have found my way to her pussy without the need to see a thing."
    "But instead I keep them open, using my vision to guide the tip of my tongue."
    "At first I don't even let it touch the fist folds of the very edge."
    "I simply use it to trace the outline of Reona's pussy."
    "Keeping my touch as light as I can, I tease her the whole time."
    show reona cunnilingus up mouth_normal
    "And as soon as my tongue as much as brushes against the outer edge, I know it's working."
    "Because Reona's reaction is to gasp and moan, almost sobbing at the threat of me touching it."
    "I can imagine the way she's anticipating the moment I actually start in on her pussy."
    "I can all but feel the way that her body is becoming ever more desperate for the sensation."
    "But still I hold on, teetering on the edge of giving her what she wants."
    "All of which means that the moment I do indulge her, the effect is sudden and impressive."
    show reona cunnilingus eyes_open mouth_pleasure
    "The very second the tip of my tongue slides into the first folds, Reona lets out a gasp."
    "It's deep, almost desperate in nature, embodying all of her desire and frustration."
    "I imagine she's casting her head about too, trying to release some of the tension she's feeling."
    "But there's no need for her to worry about that."
    "Because I'm determined to take care of that for her!"
    show reona cunnilingus eyes_ahegao mouth_normal
    "It's not that I speed up to any great degree now that I'm actually licking away at her pussy."
    "If anything, I feel like I slow down, but at the same time I redouble the intensity of what I'm doing."
    "I try as best I can to apply the same discipline to this as I have to tutoring Reona."
    "I'm being thorough, covering all the angles and making sure to leave nothing out."
    "And the result of that is plain to see."
    "Or to be more specific, for me it's plain to feel and hear."
    show reona cunnilingus eyes_close mouth_hurt
    "As my tongue delves ever deeper into Reona's pussy, her entire body quivers."
    "And I can hear the moans and cries that she's letting out at the same time."
    "It's almost as it she's moving in time with the motions of my tongue."
    "By now I've circled Reona's pussy many times, working my way inwards too."
    "I can feel it sinking deeper as well, beginning to probe inside."
    "And the deeper it gets, the more extreme her reactions become."
    show reona cunnilingus down mouth_ahegao
    "Rather than gasping, Reona now seems to be panting instead."
    "My tongue is starting to feel a little numb, the muscles threatening to cramp."
    "But still I do all that I can to ignore the sensation and push onwards."
    "My instincts tell me that Reona can't be too far from reaching her limit."
    "That she can't hold out much longer before the end comes."
    "And just as I feel pain beginning to spread through my tongue, it starts to happen."
    show reona cunnilingus eyes_open mouth_hurt
    "Reona's body tenses, her thighs clamping down on me in an effort to keep me in place."
    "But she needn't have worried, because I'm focussed on one thing and one thing alone."
    "Which is making sure that she comes, and in as spectacular a fashion as possible!"
    show reona cunnilingus eyes_close
    reona.say "Mmm..."
    reona.say "Argh..."
    show reona cunnilingus eyes_ahegao
    reona.say "Oh...oh fuck!"
    reona.say "What...what are you doing to me?!?"
    "I can't express how it feels to hear words like that coming out of Reona."
    "She's always seemed to be the one with all the sexual experience."
    "The one that knows just how to wrap me around her finger."
    "But now here she is, in the palm of my hand!"
    show reona cunnilingus up mouth_ahegao squirt
    "I push my tongue as deep as I can while Reona rides out her orgasm."
    "Trying as best I can to squeeze even more pleasure out of it for her."
    "And once I feel her body go limp, I finally let up and raise my head."
    show reona cunnilingus eyes_close mouth_pleasure -mike -squirt
    mike.say "Urgh..."
    mike.say "I think my tongue went to sleep!"
    mike.say "How are you doing, Reona?"
    mike.say "Erm..."
    mike.say "Reona, are you okay?"
    "I say this because I can now see that Reona's collapsed into the pillows at the head of the bed."
    "And as I lean in closer, I can see that she's staring into space, her eyes totally blank!"
    reona.say "Urr…"
    show reona cunnilingus eyes_open
    reona.say "Can you stop the room spinning, please?"
    reona.say "I think I want to get off now!"
    return

label reona_fuck_date_blowjob:
    scene bg black
    show reona bj finger squeeze mouth_lick
    with fade
    "I watch as Reona begins to lower herself down in front of me."
    "In reality, all she's doing is getting down on the floor."
    "But as usual with Reona, everything she does is oozing with sexual overtones."
    "And I'm totally entranced by the way that her naked body is moving."
    "Once Reona's head is level with my groin, she leans forwards."
    "Then she gives me a knowing look from below."
    show reona bj mike
    with fade
    reona.say "You'd better hold on, [hero.name]."
    reona.say "Because I guarantee you've never had a BJ like this!"
    "All I can do is nod in eagerness and anticipation."
    "Because I already know that Reona has a reputation for being wild."
    "So it stands to reason that she's probably not bragging without cause."
    "The first indication I get that my hunch is correct comes pretty much instantly."
    "Because a change seems to come over Reona."
    "Even before her lips make contact with my cock, her demeanour changes."
    show reona bj handjob -finger
    "Where before she was flirtatious and funny, now she becomes focussed."
    "It's not that she loses any of the passion that she was showing before."
    "More like it's channelled into what she's doing instead."
    "Reona massages my cock at the base, gripping it firmly."
    "So much so that I can't help letting out a gasp of pain."
    mike.say "Ouch!"
    show reona bj mouth_open
    reona.say "Don't worry, [hero.name]..."
    reona.say "You'll get used to it!"
    "As Reona says this, her lips are perhaps a fraction of an inch from my cock."
    show reona bj suck eyes_close finger squeeze -handjob
    "And I swear that I can feel the last breath of her words as she finally swallows the tip."
    "To begin with, Reona uses her mouth in the gentlest ways imaginable."
    "The touch of her tongue and lips is soft, with only a hint of her teeth in the mix."



    show reona bj -squeeze
    "I can feel my heart beginning to beat faster as she does all of this."

    "In fact I'm so distracted that I don't even notice what Reona's doing with her other hand."
    "The first thing I know about it is the sensation of her grabbing hold of my ass."
    "Her fingers sink into one of my buttocks, almost like she's clamping on."

    show reona bj eyes_open -finger
    "Then I feel the other hand seize my previously untouched butt-cheek!"
    "Reona starts to really go for it after that, squeezing them both."
    "And for a moment I think that's all she's going to do."
    "That she's so into my tight buns that she's just going to keep massaging them."
    "Which would have been fine as far as I'm concerned."
    "But then I realise that what she's doing is nothing but a distraction."
    "Because all of a sudden, the restraint she's shown seems to vanish."
    show reona bj eyes_close
    "Where before Reona was going slowly inside of her mouth, she now throws caution to the wind."
    "Her head begins to bob back and forth, picking up speed with every passing second."
    "And my cock is thrust ever deeper into her mouth as all of this is happening."
    "Now I realise that Reona's not gripping my ass just for the sake of how it feels."
    "She's holding onto it to keep my cock right where she wants it!"
    "It's only now that I get to feel the true extent of her powers too."
    "Before this was an exquisite and yet sedate experience for me."
    "But with every passing second I feel more like I'm strapped into a roller-coaster."
    "The feelings that are spreading through me are impossible to resist."
    "And I can even begin to feel the muscles of my legs twinging."
    "My knees starting to become weak from the things Reona's doing to me."
    "I risk a glance down, wondering what kind of a sight will greet me."
    show reona bj eyes_open
    "But I get as far as catching her eye, as she glances up at me."
    "And the knowing look in it is almost too much for me to handle."
    "Now I understand all of the hype that Reona gave herself before we began."
    "None of it was just for the sake of bragging."
    "All of it was the honest truth!"
    "As if that look conveyed even more between us than I suspected, Reona changes gear."
    show reona bj eyes_close
    "Before now, I wouldn't have thought that was possible, that she could pull it off."
    "But she must have been holding back until now, keeping the best for last."
    "Because I finally feel my cock pushing deep into Reona's throat."
    show reona bj eyes_open
    "She looks up at me, almost the entire length of it inside her mouth."
    "By now my eyes must be as wide as saucers, about to pop out of their sockets."
    "I can feel myself nodding too, trying to communicate what I'm feeling."
    "It's a wonder I can even manage to get the words out before it's too late."
    mike.say "Reona..."
    mike.say "I'm gonna..."
    mike.say "I'm gonna cum!"
    "Reona gives me what I think is a nod of the head."
    "Which I take to mean she's ready for what I decide to do next."
    "And that's a good thing, because I know exactly how I want this to end!"
    menu:
        "Make her swallow your thick juice":
            "My cock's so deep inside of Reona's mouth that I'm worried she might choke."
            "But she's been so masterful at every stage of the affair that I trust her to handle it."
            "And so I make no effort to pull out as I feel myself losing it."
            show reona bj eyes_close cum with vpunch
            $ reona.love += 2
            "This means that I shoot my load deep into Reona's mouth, practically straight down her throat!"
            with vpunch
            "For a moment her eyes seem to bulge, but then just as quickly Reona regains control."
            show reona bj finger squeeze eyes_open tongueout mouthcum -mike -suck
            "And I watch in amazement as she swallows every last drop."
        "Cover her face with your milk":
            "My cock's so deep inside of Reona's mouth that I'm worried she might choke."
            show reona bj tongueout finger squeeze -suck
            "So instead of keeping on going, I pull myself out of there before it's too late."
            "Reona seems to take this in her stride, recovering in an instant."
            "Which is a relief, because I can't hold on any longer!"
            show reona bj eyes_close cum with vpunch
            $ reona.sub += 1
            "I have to let it all go, shooting my entire load straight into her face."
            with vpunch
            "Reona closes her eyes and opens her mouth, not flinching as it hits her."
            show reona bj down mouth_lick facecum -mike -cum
            "Then she licks her lips, as if savouring the sensation as well as the taste."
    "Once it's all over, my body finally gives up the fight."
    "And I find myself collapsing onto the floor, landing pretty hard on my ass."
    show reona bj down eyes_open mouth_lick rightpeace leftpeace
    "Reona remains kneeling in front of me, making no move to clean herself up."
    "Instead she gives me one of those knowing smiles that she does so well."
    reona.say "You see?"
    reona.say "I told you it was the best you'd ever get!"
    "I have no idea of that's the truth of the matter or not."
    "Because right now, Reona seems to have rendered me incapable of thinking straight."
    "So there's no way I can compare her to all the other girls I've had a BJ from."
    "But for the sake of harmony and because it's all I can manage, I nod in agreement."
    "And part of me is pretty sure that once I recover my senses, she'll be proven right."
    "Even if not, one thing's for sure."
    "That was an experience that I'm never going to forget!"
    return

label reona_fuck_date_missionary(sexperience_min):
    scene bg black
    show reona missionary
    with fade
    "She lays on her back and raises her legs into the air."
    reona.say "You see, [hero.name]?"
    reona.say "There's nothing weird about this."
    show reona missionary mouth_hurt left_peace right_peace
    reona.say "Just a girl and a guy about to fuck like rabbits!"
    "I wish there was some clever line that I could respond with."
    "But the truth is that Reona's got me so worked up right now."
    "All I can do is nod like a moron, eager to get things going."
    show reona missionary mike mouth_normal left_hold right_hold
    "My eyes wide with anticipation as I decide where to start."
    menu:
        "Fuck her pussy":
            "I feel like this is the kind of situation where it'd be easy to overthink things."
            "So I do the best I can to clear my mind of all superfluous thoughts."
            "Then I look down and allow myself to be drawn in by the first thing I see."
            "And the moment that I set eyes on Reona's pussy, my mind's made up."
            call check_condom_usage (reona) from _call_check_condom_usage_10
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show reona missionary condom
            show reona missionary mouth_orgasm
            reona.say "Come on, [hero.name]..."
            reona.say "What are you waiting for?"
            reona.say "A fucking written invitation?!?"
            show reona missionary mouth_normal
            reona.say "Get your cock inside of me already!"
            "It's not like I was taking my time to begin with."
            "But Reona's demand still serves to make me jump to it."
            $ used_toy = False
            if reona.flags.buttplug:
                menu:
                    "Use butt-plug":
                        $ used_toy = True
                        "But then I remember some of the stuff I have hidden under the bed."
                        show reona missionary mouth_pleasure -mike
                        "So I reach down and feel around until I find what I'm looking for."
                        "A butt-plug, which should help to spice things up a little."
                        show reona missionary eyes_surprised mouth_orgasm buttplug
                        "Without warning, I slide it between Reona's buttocks."
                        "And then I plunge it into her unprepared hole!"
                        reona.say "Wha..."
                        show reona missionary mouth_pleasure eyes_close
                        reona.say "Oh fuck..."
                        "Reona begins to moan and gasp as the plug sinks into her."
                    "Don't use toys":
                        "For a moment I think about hunting around under the bed for a toy to use."
                        "But the I remember how eager Reona sounded when she asked me to get on with it."
                        "So I forget about the idea and resolve to do the job myself."
            "Luckily for me, there's not too much work needed to actually get things moving."
            show reona missionary mouth_orgasm eyes_open vaginal mike
            "Almost as soon as the head of my cock touches Reona's pussy, I can feel it's ready for me."
            "Her lips are already slick and I swear I can feel actual heat from down there too!"
            "Plus the second she feels me against her lips, Reona grabs hold of me and pulls downwards."
            show reona missionary eyes_close mouth_pleasure forth
            "This means that I almost slide straight into her without any resistance at all."
            "If anything, Reona's pussy holds out for mere seconds before it opens to me."
            "And when it does, I find myself sinking all the way in, right up to my balls!"
            "At the same time, both of us are feeling all of the sensations this creates."
            "Reona's nodding and gasping, trying to pull me further into her."
            "And I'm beginning to lose the ability to think straight."
            "That's because the things she's making me feel are totally clouding my brain."
            "Before I was worried about my ability to please her."
            "But now there's just a base, almost animalistic desire to take her."
            "Not that the urges flowing through me seem to bother Reona at all."
            show reona missionary back
            pause 0.5
            show reona missionary forth eyes_hurt with hpunch
            pause 0.35
            show reona missionary back
            pause 0.2
            show reona missionary forth with hpunch
            pause 0.35
            show reona missionary back
            pause 0.2
            show reona missionary forth with hpunch
            "As I begin to move atop her, my speed picks up straight away."
            "And I'm not being subtle with my attentions either."
            "Straight away I'm thrusting with all of my strength."
            show reona missionary back
            pause 0.25
            show reona missionary forth mouth_orgasm with hpunch
            pause 0.15
            show reona missionary back
            pause 0.25
            show reona missionary forth with hpunch
            pause 0.15
            show reona missionary back eyes_close
            pause 0.25
            show reona missionary forth with hpunch
            pause 0.15
            show reona missionary back
            pause 0.25
            show reona missionary forth with hpunch
            "Yet Reona seems to be more than able to take what I'm dishing out."
            show reona missionary eyes_hurt
            "She clings on to me, soaking it all up while nodding away."
            "Which I guess means that she's liking it and wants more of the same."
            show reona missionary mouth_normal right_peace
            "Hell, I even look up to see that she's giving me the peace sign!"
            "And that surely means Reona's loving what I'm doing to her."
            "That's right about the time I start to wonder if I can keep this up."
            "I'm doing all I can to push Reona to her limit."
            "But she seems to be able to absorb it all and beg for more."
            "So maybe it's time for me to play the ace I have up my metaphorical sleeve?"
            if used_toy:
                show reona missionary back mouth_orgasm
                pause 0.5
                show reona missionary mouth_pleasure right_hold out -mike
                "Reaching down, I find the end of the butt-plug sticking out of Reona."
                "Then I take hold of it, and with one firm tug, pull it out of her ass."
                show reona missionary eyes_surprised mouth_orgasm analgape -buttplug with hpunch
                pause 0.25
                show reona missionary eyes_ahegao mouth_ahegao
                $ reona.sub += 1
                "The effect is instant and pretty impressive, as she gasps at the sensation."
                "And just as I'd hoped, it pushes her over the edge and starts her cumming."
                show reona missionary mike vaginal
            else:
                "It might have looked and felt like I was putting everything into fucking Reona."
                "But all this time, I've been careful to hold back the last of my strength."
                "And now I make use of it in one final push to get the job done."
                show reona missionary back right_hold
                pause 0.75
                show reona missionary forth mouth_orgasm eyes_surprised with hpunch
                pause 0.4
                show reona missionary mouth_ahegao eyes_ahegao with hpunch
                $ reona.love += 1
                "The effect is instant and pretty impressive, as she gasps at the sensation."
                "And just as I'd hoped, it pushes her over the edge and starts her cumming."
            "With Reona losing it, there's not much I can do to hang on myself."
            "So I'm going to have to decide how I want this thing to end."
            call cum_reaction (reona, 'vaginal', sexperience_min) from _call_cum_reaction_251
            if _return == "vaginal_outside":
                "We might have chosen not to use protection, but that doesn't mean I'm not being careful."
                show reona missionary out eyes_hurt mouth_orgasm
                "I make sure that I pull out of Reona before the inevitable happens."
                if not CONDOM:
                    show reona missionary forth
                    pause 0.3
                    show reona missionary back
                    pause 0.4
                    show reona missionary forth
                    pause 0.4
                    show reona missionary back
                    pause 0.6
                    show reona missionary forth eyes_close cum with hpunch
                    $ reona.love += 2
                    "Lines of hot, white cum spatter across Reona's exposed belly."
                    with hpunch
                    "And then they start to run down and onto the bed beneath her."
                else:
                    show reona missionary mouth_normal cum with hpunch
                    "Almost the same second that I'm all the way out, I shoot my load."
            elif _return == "vaginal_condom":
                "The fact we thought ahead and used a condom means there's nothing to worry about."
                "So I can simply go with the flow, letting the urge to cum sweep me along with it."
                "At the same time I make one last effort to push as deep into Reona as possible."
                show reona missionary back
                pause 0.3
                show reona missionary forth eyes_close mouth_orgasm with hpunch
                pause 0.3
                show reona missionary back
                pause 0.4
                show reona missionary forth with hpunch
                pause 0.4
                show reona missionary back
                pause 0.6
                show reona missionary forth eyes_hurt with hpunch
                $ reona.love += 1
                "This means that when I shoot my load, she takes it all, with nothing held back."
                "And I might be flattering myself here, but it does seem to make her cum all over again!"
            elif _return == "vaginal_inside_pill":
                show reona missionary eyes_hurt mouth_orgasm
                reona.say "Keep...going..."
                reona.say "I'm on...the pill!"
                "I silently thank Reona for the timely reminder because it means there's nothing to worry about."
                "So I can simply go with the flow, letting the urge to cum sweep me along with it."
                "At the same time I make one last effort to push as deep into Reona as possible."
                show reona missionary back
                pause 0.3
                show reona missionary forth eyes_close with hpunch
                pause 0.3
                show reona missionary back
                pause 0.4
                show reona missionary forth with hpunch
                pause 0.4
                show reona missionary back
                pause 0.6
                show reona missionary forth mouth_ahegao cum with hpunch
                $ reona.love += 3
                "This means that when I shoot my load, she takes it all, with nothing held back."
                "And I might be flattering myself here, but it does seem to make her cum all over again!"
            elif _return == "vaginal_inside_pregnant":
                "I'm not going to forget that Reona's pregnant, and that it means there's nothing to worry about."
                "So I can simply go with the flow, letting the urge to cum sweep me along with it."
                "At the same time I make one last effort to push as deep into Reona as possible."
                show reona missionary back
                pause 0.3
                show reona missionary forth eyes_close mouth_hurt with hpunch
                pause 0.3
                show reona missionary back
                pause 0.4
                show reona missionary forth with hpunch
                pause 0.4
                show reona missionary back
                pause 0.6
                show reona missionary forth mouth_ahegao cum with hpunch
                $ reona.love += 3
                "This means that when I shoot my load, she takes it all, with nothing held back."
                "And I might be flattering myself here, but it does seem to make her cum all over again!"
            elif _return == "vaginal_inside_happy":
                "We might have chosen not to use protection, but that doesn't mean I'm not being careful."
                "So I make to pull out of Reona before it's too late."
                show reona missionary eyes_hurt mouth_orgasm back with hpunch
                "But that's when I realise she's clinging onto me!"
                reona.say "No..."
                reona.say "No..."
                reona.say "Don't pull out!"
                "I'm still trying my best to do just that, but Reona's not letting go."
                show reona missionary eyes_close mouth_pleasure cum with hpunch
                $ reona.impregnate()
                $ reona.love += 5
                "And I'm still struggling when I shoot my load into her too."
                show reona missionary eyes_open mouth_normal vaginaldrip out -mike with hpunch
                "As this happens, she falls back onto the bed, a look of triumph on her face."
                "Which leaves me totally confused and already beginning to panic."
            elif _return == "vaginal_inside_mad":
                show reona missionary eyes_hurt mouth_pleasure
                reona.say "No..."
                reona.say "No..."
                reona.say "You have to pull out!"
                "Reona's panicked tones snap me back to reality, breaking the spell in an instant."
                "We didn't use any protection, so she's right - I have to pull out!"
                "But even as I start trying to do just that, the inevitable happens."
                show reona missionary eyes_surprised mouth_orgasm cum with hpunch
                $ reona.impregnate()
                $ reona.love -= 5
                "And I'm still struggling when I shoot my load into her too."
                show reona missionary eyes_close mouth_hurt back out vaginaldrip -cum with hpunch
                "As this happens, she falls back onto the bed, a look of horror on her face."
                "Which matches mine, as I'm totally confused and already beginning to panic."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "I feel like this is the kind of situation where it'd be easy to overthink things."
            "So I do the best I can to clear my mind of all superfluous thoughts."
            "Then I look down and allow myself to be drawn in by the first thing I see."
            "Just as I do so, Reona shifts a little, letting me see more of her butt."
            "And the moment that I set eyes on Reona's neat little hole, my mind's made up."
            show reona missionary mouth_orgasm
            reona.say "Come on, [hero.name]..."
            reona.say "What are you waiting for?"
            reona.say "A fucking written invitation?!?"
            show reona missionary mouth_normal
            reona.say "Get your cock inside of me already!"
            "It's not like I was taking my time to begin with."
            "But Reona's demand still serves to make me jump to it."
            $ used_toy = False
            if hero.has_item("anal_beads"):
                menu:
                    "Use pleasure beads":
                        $ used_toy = True
                        "But then I remember some of the stuff I have hidden under the bed."
                        show reona missionary mouth_pleasure -mike
                        "So I reach down and feel around until I find what I'm looking for."
                        "A string of pleasure beads, which should help to spice things up a little."
                        show reona missionary eyes_surprised mouth_orgasm beads
                        "Without warning, I slide the first bead between Reona's lips."
                        "And then I plunge it into her unprepared pussy!"
                        reona.say "Wha..."
                        show reona missionary mouth_pleasure eyes_close
                        reona.say "Oh fuck..."
                        "Reona begins to moan and gasp as the bead sinks into her."
                    "Do not use toys":
                        "For a moment I think about hunting around under the bed for a toy to use."
                        "But the I remember how eager Reona sounded when she asked me to get on with it."
                        "So I forget about the idea and resolve to do the job myself."
            "Luckily for me, there's not too much work needed to actually get things moving."
            show reona missionary mouth_orgasm eyes_open anal mike
            "Almost as soon as the head of my cock touches Reona's hole, I can feel it's ready for me."
            "Her muscles are already relaxed and I swear I can feel actual heat from down there too!"
            "Plus the second she feels me against her hole, Reona grabs hold of me and pulls downwards."
            show reona missionary eyes_close mouth_pleasure forth
            "This means that I almost slide straight into her without any resistance at all."
            "If anything, Reona's muscles hold out for mere seconds before it opens to me."
            "And when it does, I find myself sinking all the way in, right up to my balls!"
            "At the same time, both of us are feeling all of the sensations this creates."
            "Reona's nodding and gasping, trying to pull me further into her."
            "And I'm beginning to lose the ability to think straight."
            "That's because the things she's making me feel are totally clouding my brain."
            "Before I was worried about my ability to please her."
            "But now there's just a base, almost animalistic desire to take her."
            "Not that the urges flowing through me seem to bother Reona at all."
            show reona missionary back
            pause 0.5
            show reona missionary forth eyes_hurt with hpunch
            pause 0.35
            show reona missionary back
            pause 0.2
            show reona missionary forth with hpunch
            pause 0.35
            show reona missionary back
            pause 0.2
            show reona missionary forth with hpunch
            "As I begin to move atop her, my speed picks up straight away."
            "And I'm not being subtle with my attentions either."
            "Straight away I'm thrusting with all of my strength."
            show reona missionary back
            pause 0.25
            show reona missionary forth mouth_orgasm with hpunch
            pause 0.15
            show reona missionary back
            pause 0.25
            show reona missionary forth with hpunch
            pause 0.15
            show reona missionary back eyes_close
            pause 0.25
            show reona missionary forth with hpunch
            pause 0.15
            show reona missionary back
            pause 0.25
            show reona missionary forth with hpunch
            "Yet Reona seems to be more than able to take what I'm dishing out."
            show reona missionary eyes_hurt
            "She clings on to me, soaking it all up while nodding away."
            "Which I guess means that she's liking it and wants more of the same."
            show reona missionary mouth_normal left_peace
            "Hell, I even look up to see that she's giving me the peace sign!"
            "And that surely means Reona's loving what I'm doing to her."
            "That's right about the time I start to wonder if I can keep this up."
            "I'm doing all I can to push Reona to her limit."
            "But she seems to be able to absorb it all and beg for more."
            "So maybe it's time for me to play the ace I have up my metaphorical sleeve?"
            if used_toy:
                show reona missionary back mouth_pleasure standby left_hold
                "Reaching down, I find the string pleasure beads, the end sticking out of Reona."
                "Then I take hold of it, and with one firm tug, pull them out of her pussy."
                show reona missionary mouth_orgasm eyes_surprised pulled with vpunch
                pause 0.25
                show reona missionary mouth_ahegao eyes_ahegao normal vaginalgape -beads
                $ reona.love += 1
                "The effect is instant and pretty impressive, as she gasps at the sensation of each bead popping out."
                "And just as I'd hoped, it pushes her over the edge and starts her cuming."
            else:
                "It might have looked and felt like I was putting everything into fucking Reona."
                "But all this time, I've been careful to hold back the last of my strength."
                "And now I make use of it in one final push to get the job done."
                show reona missionary back left_hold
                pause 0.75
                show reona missionary forth mouth_orgasm eyes_surprised with hpunch
                pause 0.4
                show reona missionary mouth_ahegao eyes_ahegao with hpunch
                $ reona.sub += 1
                "The effect is instant and pretty impressive, as she gasps at the sensation."
                "And just as I'd hoped, it pushes her over the edge and starts her cuming."
            "With Reona losing it, there's not much I can do to hang on myself."
            "So I'm going to have to decide how I want this thing to end."
            call cum_reaction (reona, 'anal', sexperience_min) from _call_cum_reaction_252
            if _return == 'anal_outside':
                show reona missionary out eyes_hurt mouth_orgasm
                "I make sure that I pull out of Reona before the inevitable happens, and I'm just in time too."
                show reona missionary forth
                pause 0.3
                show reona missionary back
                pause 0.4
                show reona missionary forth
                pause 0.4
                show reona missionary back
                pause 0.6
                show reona missionary forth eyes_close cum with hpunch
                $ reona.sub += 1
                "Lines of hot, white cum spatter across Reona's exposed belly."
                "And then they start to run down and onto the bed beneath her."
            elif _return == 'anal_inside':
                "The fact that I chose to take Reona up the ass means there's nothing to worry about."
                "So I can simply go with the flow, letting the urge to cum sweep me along with it."
                "At the same time I make one last effort to push as deep into Reona as possible."
                show reona missionary back
                pause 0.3
                show reona missionary forth eyes_close with hpunch
                pause 0.3
                show reona missionary back
                pause 0.4
                show reona missionary forth with hpunch
                pause 0.4
                show reona missionary back
                pause 0.6
                show reona missionary forth mouth_ahegao cum with hpunch
                $ reona.sub += 2
                "This means that when I shoot my load, she takes it all, with nothing held back."
                "And I might be flattering myself here, but it does seem to make her cum all over again!"
    return

label reona_fuck_date_cowgirl(sexperience_min):
    scene bg black
    show reona cowgirl
    with fade
    reona.say "Hmm..."
    reona.say "Looks like someone's ready for me!"
    reona.say "So what do you say?"
    reona.say "Shall we get this party started?"
    "All I can do in way of a response is nod my head."
    "And thankfully that seems to be enough, as Reona returns the gesture."
    reona.say "I'm going to ride you like one of those guys at a rodeo."
    "Suddenly Reona leans in closer, as if to emphasise her point."
    reona.say "And just like them, I'm going to break you too!"
    menu:
        "Fuck her pussy":
            "The moment that those words come out of Reona's mouth, I know I'm in for a real ride here."
            "She's kind of issuing a challenge to me, boldly proclaiming that she's not going to be holding back."
            "And I feel the urge to rise to that same challenge growing within me even as she's saying it."
            "So I make a silent declaration to myself, deciding what my mission is going to be here."
            call check_condom_usage (reona) from _call_check_condom_usage_136
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show reona cowgirl condom
            "I can already feel how hot and wet she is down there, how slippery her pussy is."
            "And now she's being pulled downwards by gravity, while my cock is positioned beneath it."
            "Reona begins to wriggle and writhe as more pressure is put on her lips."
            "I can feel the natural resistance that's still keeping me out of there."
            "But with every second that passes, the forces acting against it are getting more intense."
            show reona cowgirl eyes_close mouth_open
            "Suddenly, Reona shuts her eyes tight, and throws back her head."
            reona.say "Ah..."
            reona.say "Mmm..."
            reona.say "Oh..."
            show reona cowgirl vaginal eyes_lookdown mouth_pleasure
            $ reona.love += 1
            "All of this happens as the head of my cock finally starts to sink into her."
            "A little at a time, her pussy relaxes, and when it does, I go deeper still."
            "She's gripping my hands tightly, using them to hold herself upright."
            "But there's nothing she can do to keep from inching her way down and onto me."
            "When I'm sure there's no chance of me slipping out of her, I make my move."
            show reona cowgirl eyes_close
            "Slowly at first, I begin to move up and down, sliding my cock in and out of her."
            "Each thrust sees me gain a little more speed and a little more force."
            "To begin with, the change is hardly noticeable."
            "And nothing in Reona's reaction seems to change either."
            show reona cowgirl mouth_open at startle(0.05,-10)
            "But it doesn't take long for me to pick up speed."
            "And by the time I have, Reona's more than reacted to it."
            show reona cowgirl at startle(0.05,-10)
            "Now she's bobbing up and down in sympathy with my own movements."
            "This means that she's effectively riding my cock, enhancing what I'm doing to her."
            show reona cowgirl at startle(0.05,-10)
            "Reona's head bobs up and down on her shoulders."
            show reona cowgirl at startle(0.05,-10)
            "And perhaps more noticeably, her breasts are bouncing like crazy!"
            show reona cowgirl at startle(0.05,-10)
            "They jiggle up and down, often hiding her face from view."
            show reona cowgirl at startle(0.05,-10)
            "And I can see that her nipples are standing proud and erect, as hard as they can be."
            show reona cowgirl eyes_open mouth_pleasure at startle(0.05,-10)
            "Reona keeps trying to lower herself down onto me, to get her knees onto the bed."
            show reona cowgirl at startle(0.05,-10)
            "But the motion of my thrusting upwards seems to keep her from doing it."
            "This means that she's held in a position where all of her weight is pressing down."
            "And not to put too fine of a point on it, what it's pressing down on is my cock?"
            show reona cowgirl mouth_ahegao eyes_close
            "I can feel every muscle of her body, straining to keep her from collapse."
            "And the effect it's having on me is pretty intense, to say the least."
            "When I do manage to see past Reona's breasts, I study the look on her face."
            "Her mouth is hanging open thanks to her jaw being slack."
            show reona cowgirl mouth_hurt eyes_open at startle(0.05,-10)
            "So it comes as no surprise when I feel her pussy starting to twitch a moment later."
            show reona cowgirl at startle(0.05,-10)
            "Looks like Reona's had all that she can take, and now she's about to cum!"
            show reona cowgirl at startle(0.05,-10)
            "Which means I need to decide how I'm going to end this, and fast."
            call cum_reaction (reona, 'vaginal', sexperience_min) from _call_cum_reaction_253
            if _return == "vaginal_outside":
                if not CONDOM:
                    "The fact we chose not to use a condom means that I only have one choice."
                    "And I'm sure to pull out of Reona before it's too late."
                else:
                    "I'm sure to pull out of Reona before it's too late."
                with vpunch
                "But the sensation of doing so only seems to make her orgasm more intense."
                show reona cowgirl out cum mouth_open with vpunch
                $ reona.sub += 1
                "Reona gasps and shakes as I shoot my load over her belly."
                "Then she topples sideways onto the bed."
            elif _return == "vaginal_condom":
                "It's times like this when remembering to use a condom really pays off."
                "Because all I have to do is lie back and watch the fireworks!"
                with vpunch
                "As Reona succumbs to her orgasm, she pulls me along with her."
                with vpunch
                "While I'm as deep inside of her as possible, I lose it."
                show reona cowgirl eyes_close mouth_ahegao with vpunch
                $ reona.love += 1
                "And she rides out the last moments of pleasure as I shoot my load into her."
                "Then she topples sideways onto the bed."
            elif _return == "vaginal_inside_pill":
                "I remember in good time that Reona's on the pill."
                "And that's good news for me."
                "Because all I have to do is lie back and watch the fireworks!"
                with vpunch
                "As Reona succumbs to her orgasm, she pulls me along with her."
                with vpunch
                "While I'm as deep inside of her as possible, I lose it."
                show reona cowgirl eyes_ahegao mouth_ahegao cum with vpunch
                $ reona.love += 3
                "And she rides out the last moments of pleasure as I shoot my load into her."
                "Then she topples sideways onto the bed."
            elif _return == "vaginal_inside_pregnant":
                "Right now the fact that Reona's pregnant really pays off."
                "Because all I have to do is lie back and watch the fireworks!"
                with vpunch
                "As Reona succumbs to her orgasm, she pulls me along with her."
                with vpunch
                "While I'm as deep inside of her as possible, I lose it."
                show reona cowgirl eyes_ahegao mouth_ahegao cum with vpunch
                $ reona.love += 3
                "And she rides out the last moments of pleasure as I shoot my load into her."
                "Then she topples sideways onto the bed."
            elif _return == "vaginal_inside_happy":
                "The fact we chose not to use a condom means that I only have one choice."
                "And I make to pull out of Reona before it's too late."
                show reona cowgirl mouth_normal with vpunch
                "But the moment that I do, she pushes down on me with all her might."
                "This takes me by total surprise, meaning that I have no time to react."
                with vpunch
                "While I'm as deep inside of her as possible, I lose it."
                show reona cowgirl eyes_ahegao mouth_pleasure cum with vpunch
                $ reona.impregnate()
                $ reona.love += 5
                "And she rides out the last moments of pleasure as I shoot my load into her."
                "Then she topples sideways onto the bed."
                "But I'm already asking myself what the hell just happened, and why!"
            elif _return == "vaginal_inside_mad":
                show reona cowgirl eyes_surprised mouth_open
                reona.say "What are you doing?!?"
                reona.say "You gotta pull out!"
                "Reona's words snap me back to reality."
                "I remember that we didn't use a condom."
                "So she's right - I have to pull out, before..."
                with vpunch
                "But by now, it's too late."
                with vpunch
                "While I'm as deep inside of her as possible, I lose it."
                show reona cowgirl eyes_ahegao mouth_hurt cum with vpunch
                $ reona.impregnate()
                $ reona.love -= 5
                "Reona tries to get off as I shoot my load into her."
                "But from the look on her face, she already knows it's done."
                "And I'm already asking myself how I could have let this happen."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "The moment that those words come out of Reona's mouth, I know I'm in for a real ride here."
            "She's kind of issuing a challenge to me, boldly proclaiming that she's not going to be holding back."
            "And I feel the urge to rise to that same challenge growing within me even as she's saying it."
            "So I make a silent declaration to myself, deciding what my mission is going to be here."
            "I can already feel how hot and wet she is back there, how slippery her hole is."
            "And now she's being pulled downwards by gravity, while my cock is positioned beneath it."
            "Reona begins to wriggle and writhe as more pressure is put on her hole."
            "I can feel the natural resistance that's still keeping me out of there."
            "But with every second that passes, the forces acting against it are getting more intense."
            show reona cowgirl eyes_close mouth_open
            "Suddenly, Reona shuts her eyes tight, and throws back her head."
            reona.say "Ah..."
            reona.say "Mmm..."
            reona.say "Oh..."
            show reona cowgirl anal eyes_lookdown mouth_pleasure
            $ reona.sub += 1
            "All of this happens as the head of my cock finally starts to sink into her."
            "A little at a time, her muscles relax, and when it does, I go deeper still."
            "She's gripping my hands tightly, using them to hold herself upright."
            "But there's nothing she can do to keep from inching her way down and onto me."
            "When I'm sure there's no chance of me slipping out of her, I make my move."
            show reona cowgirl eyes_close
            "Slowly at first, I begin to move up and down, sliding my cock in and out of her."
            "Each thrust sees me gain a little more speed and a little more force."
            "To begin with, the change is hardly noticeable."
            "And nothing in Reona's reaction seems to change either."
            show reona cowgirl mouth_open at startle(0.05,-10)
            "But it doesn't take long for me to pick up speed."
            "And by the time I have, Reona's more than reacted to it."
            show reona cowgirl at startle(0.05,-10)
            "Now she's bobbing up and down in sympathy with my own movements."
            "This means that she's effectively riding my cock, enhancing what I'm doing to her."
            show reona cowgirl at startle(0.05,-10)
            "Reona's head bobs up and down on her shoulders."
            show reona cowgirl at startle(0.05,-10)
            "And perhaps more noticeably, her breasts are bouncing like crazy!"
            show reona cowgirl at startle(0.05,-10)
            "They jiggle up and down, often hiding her face from view."
            show reona cowgirl at startle(0.05,-10)
            "And I can see that her nipples are standing proud and erect, as hard as they can be."
            show reona cowgirl eyes_open mouth_pleasure at startle(0.05,-10)
            "Reona keeps trying to lower herself down onto me, to get her knees onto the bed."
            show reona cowgirl at startle(0.05,-10)
            "But the motion of my thrusting upwards seems to keep her from doing it."
            "This means that she's held in a position where all of her weight is pressing down."
            "And not to put too fine of a point on it, what it's pressing down on is my cock?"
            show reona cowgirl mouth_ahegao eyes_close
            "I can feel every muscle of her body, straining to keep her from collapse."
            "And the effect it's having on me is pretty intense, to say the least."
            "When I do manage to see past Reona's breasts, I study the look on her face."
            "Her mouth is hanging open thanks to her jaw being slack."
            show reona cowgirl mouth_hurt eyes_open at startle(0.05,-10)
            "So it comes as no surprise when I feel her ass starting to twitch a moment later."
            show reona cowgirl at startle(0.05,-10)
            "Looks like Reona's had all that she can take, and now she's about to cum!"
            show reona cowgirl at startle(0.05,-10)
            "Which means I need to decide how I'm going to end this, and fast."
            call cum_reaction (reona, 'anal', sexperience_min) from _call_cum_reaction_254
            if _return == 'anal_outside':
                "Just because I chose to use the back passage doesn't mean I have to stay in there."
                "Because a guy might want to make a little show out of losing it."
                "And I'm sure to pull out of Reona before it's too late."
                with vpunch
                "But the sensation of doing so only seems to make her orgasm more intense."
                show reona cowgirl out cum mouth_open with vpunch
                $ reona.sub += 1
                "Reona gasps and shakes as I shoot my load over her belly."
                "Then she topples sideways onto the bed."
            elif _return == 'anal_inside':
                "It's times like this when using the back passage really pays off."
                "Because all I have to do is lie back and watch the fireworks!"
                with vpunch
                "As Reona succumbs to her orgasm, she pulls me along with her."
                with vpunch
                "While I'm as deep inside of her as possible, I lose it."
                show reona cowgirl eyes_ahegao mouth_ahegao cum with vpunch
                $ reona.sub += 2
                "And she rides out the last moments of pleasure as I shoot my load into her."
                "Then she topples sideways onto the bed."
    return

label reona_fuck_date_reverse_cowgirl(sexperience_min):
    scene bg black
    show reona reverse cowgirl bedroom
    with fade
    "Reona leaps onto my lap."
    "She lands right on my thighs, pinning me to the bed."
    show reona reverse cowgirl handjob
    "And just to make sure that she keeps me where she wants me, she grabs hold of my cock too!"
    mike.say "Oof..."
    mike.say "What the..."
    mike.say "Ouch!"
    reona.say "Oh don't be such a wimp, [hero.name]."
    reona.say "I only gave it a tug to make sure you were really awake!"
    "Again, it's the tone of voice Reona's using that really gets me going."
    "I don't know if she's being so dismissive just to get a rise out of me."
    "But whatever the case, now I am fully awake and ready to leap into action."
    mike.say "Don't you worry, Reona..."
    mike.say "I'm totally awake."
    mike.say "And I know just how to prove it to you!"
    "As I'm saying this, I reach around with both hands."
    "And I take a firm hold of Reona's breasts."
    "Without giving her the chance to react, I begin to squeeze and squash them."
    "I also make sure to pinch the nipples with my fingertips and rub their mass in the palms of my hands."
    "Reona's reaction is instant and dramatic, as she seems to begin melting in my grasp."
    "I feel her lean her weight against me, almost like her muscles are going slack."
    "But the one part of her that doesn't loosen up is the hand still holding my cock."
    "If anything, Reona starts gripping this even tighter than before."
    reona.say "Oh fuck..."
    reona.say "Oh fuck yeah!"
    reona.say "You'd better be able to keep that up, [hero.name]!"
    "Reona underlines her point by beginning to stroke her hand up and down the shaft."
    "This seems to be as much a peace-offering as an attempt at foreplay."
    "And I'm more than willing to take it as such, whatever her intentions might be."
    "That done, my thoughts start turning towards just what I'm going to do next."
    "Because I think I'm going to need to make my move as quickly as possible."
    menu:
        "Fuck her pussy":




            call check_condom_usage (reona) from _call_check_condom_usage_137
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show reona reverse cowgirl condom
            show reona reverse cowgirl out
            "At first Reona seems reluctant to release her grip on my cock."
            "But it doesn't take her long to see that she's standing in the way of what she wants."
            "And as soon as she relents and lets me go, I lift her a little way into the air."
            "At the same time I pull my own groin back, just enough to give me the space I need."
            "Then I lower her down and onto me, allowing gravity to do most of the work."
            show reona reverse cowgirl eyes_close
            "As soon as the head of my cock touches her lips, Reona begins to wriggle and squirm."
            "But this only makes me tighten my grip on her and pull down harder than before."
            "And that's because I know full well that she's not trying to escape from my clutches."
            "I can tell without needing to ask that Reona's efforts are to get me inside of her."
            "She's doing all that she can to work the head against herself."
            "To encourage the lips of her pussy to begin opening and allow me to enter."
            "At first we both seem to be making little progress in that respect."
            "But the sensation of my cock rubbing against her pussy is more than a little thrilling."
            "So at least we can console ourselves with the feelings of pleasure that it's creating."
            "In fact I'm becoming so used to it that I almost forget the ultimate goal here."
            "Which means that, when we finally have a breakthrough, it takes me by surprise."
            "All of a sudden something changes as Reona's body starts to surrender to the inevitable."
            show reona reverse cowgirl eyes_surprised vaginal
            "The head of my cock jerks, and then it sinks into her."
            "Not even half an inch at first, but enough to see me stop struggling in vain."
            show reona reverse cowgirl eyes_open
            "Reona and I seem to respond to this on a totally unconscious level."
            "Suddenly we're no longer circling aimlessly, but pushing for a common goal."
            reona.say "Oh god..."
            reona.say "Don't stop now!"
            reona.say "Please...don't stop!"
            "I would have gone on without the need for Reona to beg me."
            "But the sound of her voice makes me all the more determined to do so."
            "In fact it inspires me to make a renewed effort."
            show reona reverse cowgirl eyes_close
            "One more pull and thrust is all that it takes for things to happen."
            "All of Reona's resistance seems to vanish in a single moment."
            "And I feel her sink down onto me in one smooth motion."
            "At the same time she begins to moan with pure, unadulterated pleasure."
            "I don't stop until I'm all the way inside of Reona, unable to go any deeper."
            "And I mean to stay there for a moment, just to savour the feeling of it."
            show reona reverse cowgirl eyes_open at startle(0.05,-10)
            "But Reona has different ideas, instantly starting to bounce up and down."
            show reona reverse cowgirl at startle(0.05,-10)
            "It seems like if I don't go along with what she wants, then she'll just do it herself!"
            "Not wanting to be left out of the action, I do the best I can to match her movements."
            show reona reverse cowgirl eyes_close at startle(0.05,-10)
            "And that means pretty soon I'm thrusting up from below, and using all my strength to do so."
            show reona reverse cowgirl at startle(0.05,-10)
            "Reona's bouncing up and down on my lap, every thrust burying my cock deep inside of her."
            "And from the sounds that she's making, this is exactly what she wants."






            show reona reverse cowgirl at startle(0.05,-10)
            "Judging by the gasps of pleasure escaping her lips, I wonder how much more she can take."
            show reona reverse cowgirl eyes_open
            "I get an answer to that question a few moments later."
            show reona reverse cowgirl at startle(0.05,-10)
            "Because that's when I start to feel Reona's muscles squeezing my cock."
            "The same force seems to be spreading out across her body too."
            show reona reverse cowgirl at startle(0.05,-10)
            "Which can only means she's on the verge of reaching her climax."
            show reona reverse cowgirl at startle(0.05,-10)
            "So I need to decide how I want to end things, before it's too late!"
            call cum_reaction (reona, 'vaginal', sexperience_min) from _call_cum_reaction_255
            if _return == "vaginal_outside":
                if not CONDOM:
                    "I'm conscious of the fact that we chose not to use any protection."
                    "So my primary concern is making sure that I pull out in time."
                else:
                    "My primary concern is making sure that I pull out in time."
                "But the upside of that is the sensation it causes when I do so."
                "All I need to do is make sure that I have a tight hold on Reona."
                show reona reverse cowgirl out cum eyes_close with vpunch
                $ reona.sub += 1
                "Then I just do it, shooting my load in front of her."
                with vpunch
                "The vision of it redoubles her own orgasm, sending her almost into a frenzy of pleasure."
                with vpunch
                "One that I'm more than happy to ride out with her."
            elif _return == "vaginal_condom":
                "I've not forgotten the fact that we chose to use protection."
                "And secure in that knowledge, I push right on without stopping."
                "All I need to do is make sure that I have a tight hold on Reona."
                show reona reverse cowgirl eyes_close with vpunch
                $ reona.love += 1
                "Then I just let go, shooting my load into her without holding a thing back."
                with vpunch
                "This redoubles her own orgasm, sending her almost into a frenzy of pleasure."
                with vpunch
                "One that I'm more than happy to ride out with her."
            elif _return == "vaginal_inside_pill":
                reona.say "Don't pull out..."
                reona.say "I'm...on the...pill!"
                "I silently thank Reona for the timely reminder of that fact."
                "And secure in that same knowledge, I push right on without stopping."
                "All I need to do is make sure that I have a tight hold on Reona."
                show reona reverse cowgirl eyes_ahegao cum with vpunch
                $ reona.love += 3
                "Then I just let go, shooting my load into her without holding a thing back."
                with vpunch
                "This redoubles her own orgasm, sending her almost into a frenzy of pleasure."
                with vpunch
                "One that I'm more than happy to ride out with her."
            elif _return == "vaginal_inside_pregnant":
                "It's impossible to forget the fact that Reona's pregnant."
                "And secure in that knowledge, I push right on without stopping."
                "All I need to do is make sure that I have a tight hold on Reona."
                show reona reverse cowgirl eyes_ahegao cum with vpunch
                $ reona.love += 3
                "Then I just let go, shooting my load into her without holding a thing back."
                with vpunch
                "This redoubles her own orgasm, sending her almost into a frenzy of pleasure."
                with vpunch
                "One that I'm more than happy to ride out with her."
            elif _return == "vaginal_inside_happy":
                "I'm conscious of the fact that we chose not to use any protection."
                "So my primary concern is making sure that I pull out in time."
                show reona reverse cowgirl eyes_lookdown
                "But as soon as I try to make that happen, Reona resists with all her strength."
                reona.say "Oh no..."
                reona.say "No you don't!"
                mike.say "Reona..."
                mike.say "What are you doing?!?"
                "But by the time I manage to ask the question, it's already too late."
                show reona reverse cowgirl eyes_close cum with vpunch
                $ reona.impregnate()
                $ reona.love += 5
                "I can't stop myself from shooting my load into her without holding a thing back."
                with vpunch
                "This redoubles her own orgasm, sending her almost into a frenzy of pleasure."
                with vpunch
                "One that I'm more forced to ride out with her."
                "Even as I'm wondering what in the hell just happened."
            elif _return == "vaginal_inside_mad":
                show reona reverse cowgirl eyes_lookdown
                reona.say "Oh no..."
                reona.say "No you don't!"
                mike.say "Reona..."
                mike.say "What the..."
                "But by the time I manage to ask the question, it's already too late."
                show reona reverse cowgirl eyes_ahegao with vpunch
                $ reona.impregnate()
                $ reona.love -= 5
                "I can't stop myself from shooting my load into her without holding a thing back."
                with vpunch
                "Even as we scramble to part, we both know that it's not going to change things."
                "We just screwed up badly, and now we're going to have to deal with the fallout."
        "Fuck her ass":




            show reona reverse cowgirl out
            "At first Reona seems reluctant to release her grip on my cock."
            "But it doesn't take her long to see that she's standing in the way of what she wants."
            "And as soon as she relents and lets me go, I lift her a little way into the air."
            "At the same time I pull my own groin back, just enough to give me the space I need."
            "Then I lower her down and onto me, allowing gravity to do most of the work."
            show reona reverse cowgirl eyes_close
            "As soon as the head of my cock slides between her buttocks, Reona begins to wriggle and squirm."
            "But this only makes me tighten my grip on her and pull down harder than before."
            "And that's because I know full well that she's not trying to escape from my clutches."
            "I can tell without needing to ask that Reona's efforts are to get me inside of her."
            "She's doing all that she can to work the head against herself."
            "To encourage the muscles of her ass to begin opening and allow me to enter."
            "At first we both seem to be making little progress in that respect."
            "But the sensation of my cock rubbing against her hole is more than a little thrilling."
            "So at least we can console ourselves with the feelings of pleasure that it's creating."
            "In fact I'm becoming so used to it that I almost forget the ultimate goal here."
            "Which means that, when we finally have a breakthrough, it takes me by surprise."
            "All of a sudden something changes as Reona's body starts to surrender to the inevitable."
            show reona reverse cowgirl eyes_surprised anal
            "The head of my cock jerks, and then it sinks into her."
            "Not even half an inch at first, but enough to see me stop struggling in vain."
            show reona reverse cowgirl eyes_open
            "Reona and I seem to respond to this on a totally unconscious level."
            "Suddenly we're no longer circling aimlessly, but pushing for a common goal."
            reona.say "Oh god..."
            reona.say "Don't stop now!"
            reona.say "Please...don't stop!"
            "I would have gone on without the need for Reona to beg me."
            "But the sound of her voice makes me all the more determined to do so."
            "In fact it inspires me to make a renewed effort."
            show reona reverse cowgirl eyes_close
            "One more pull and thrust is all that it takes for things to happen."
            "All of Reona's resistance seems to vanish in a single moment."
            "And I feel her sink down onto me in one smooth motion."
            "At the same time she begins to moan with pure, unadulterated pleasure."
            "I don't stop until I'm all the way inside of Reona, unable to go any deeper."
            "And I mean to stay there for a moment, just to savour the feeling of it."
            show reona reverse cowgirl eyes_open at startle(0.05,-10)
            "But Reona has different ideas, instantly starting to bounce up and down."
            show reona reverse cowgirl at startle(0.05,-10)
            "It seems like if I don't go along with what she wants, then she'll just do it herself!"
            "Not wanting to be left out of the action, I do the best I can to match her movements."
            show reona reverse cowgirl eyes_close at startle(0.05,-10)
            "And that means pretty soon I'm thrusting up from below, and using all my strength to do so."
            show reona reverse cowgirl at startle(0.05,-10)
            "Reona's bouncing up and down on my lap, every thrust burying my cock deep inside of her."
            "And from the sounds that she's making, this is exactly what she wants."






            show reona reverse cowgirl at startle(0.05,-10)
            "Judging by the gasps of pleasure escaping her lips, I wonder how much more she can take."
            show reona reverse cowgirl eyes_open
            "I get an answer to that question a few moments later."
            show reona reverse cowgirl at startle(0.05,-10)
            "Because that's when I start to feel Reona's muscles squeezing my cock."
            "The same force seems to be spreading out across her body too."
            show reona reverse cowgirl at startle(0.05,-10)
            "Which can only means she's on the verge of reaching her climax."
            show reona reverse cowgirl at startle(0.05,-10)
            "So I need to decide how I want to end things, before it's too late!"
            call cum_reaction (reona, 'anal', sexperience_min) from _call_cum_reaction_256
            if _return == 'anal_outside':
                "Even though I chose to use the back entrance, I don't want to lose it inside of Reona."
                "I don't know why, but I want to make a little show of it instead."
                "So my primary concern is making sure that I pull out in time."
                "But the upside of that is the sensation it causes when I do so."
                "All I need to do is make sure that I have a tight hold on Reona."
                show reona reverse cowgirl out cum eyes_close with vpunch
                $ reona.sub += 1
                "Then I just do it, shooting my load in front of her."
                with vpunch
                "The vision of it redoubles her own orgasm, sending her almost into a frenzy of pleasure."
                with vpunch
                "One that I'm more than happy to ride out with her."
            elif _return == 'anal_inside':
                "There's always an extra benefit to using the back entrance."
                "The simple fact that it means there's no chance of an unwanted accident."
                "And secure in that knowledge, I push right on without stopping."
                "All I need to do is make sure that I have a tight hold on Reona."
                show reona reverse cowgirl eyes_ahegao cum with vpunch
                $ reona.sub += 2
                "Then I just let go, shooting my load into her without holding a thing back."
                with vpunch
                "This redoubles her own orgasm, sending her almost into a frenzy of pleasure."
                with vpunch
                "One that I'm more than happy to ride out with her."
    return

label reona_fuck_date_doggy(sexperience_min):
    scene bg black
    show reona doggy naked
    with fade
    "Her hands braced against the wall, Reona spreads her legs apart."
    "Then she looks back over her shoulder at me."
    "And now I can see that she's beginning to smile."
    "Most likely because I'm almost naked too."
    "And she can clearly see the effect that the view is having on me."
    reona.say "Like what you see, huh?"
    reona.say "My pussy making you get good and hard?"
    reona.say "Then you'd better get over here and show me what you're gonna do with it!"
    "I'm nodding like a fool as I walk over to where Reona's waiting for me."
    show reona doggy mike
    mike.say "You bet, Reona..."
    mike.say "I'm coming, yeah..."
    mike.say "I'm coming as fast as I can!"
    reona.say "Just make sure you don't cum too quickly, okay?"
    reona.say "I've got one hell of an itch for you to scratch down there!"
    "I feel the need to show Reona that I'm serious."
    "To send the message that I know what I'm doing here."
    "And that means she's going to be in for the ride of her life!"
    play sound spank
    show reona doggy spank eyes_pleasure with hpunch
    "With that in mind, I clasp my hands onto her bare buttocks."
    "The sound of them making contact produces a loud crack."
    "Loud enough to make Reona squeal in surprise."
    reona.say "Yah!"
    show reona doggy eyes_normal mouth_pleasure -spank
    reona.say "What the..."
    "Though I suspect it's more due to the sound than the force of the impact."
    "By now I'm so close to her that my cock is already between her thighs."
    "And I know that I have to work hard and fast if I want to be able to satisfy her."
    "So I only have a couple of seconds to decide where I'm going to actually put it!"
    menu:
        "Fuck her pussy":
            "If I wasn't under so much pressure, I might have been inspired to experiment."
            "But the urgency I'm feeling means that I want to get straight down to business."
            "And that's why I choose to focus my attention on Reona's pussy."
            "It's warm, slick and more than inviting right now."
            "So I line myself up and take aim..."
            show reona doggy mouth_normal
            call check_condom_usage (reona) from _call_check_condom_usage_138
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show reona doggy condom
            reona.say "Come on, [hero.name]…"
            reona.say "Get your cock inside me already!"
            "I'd been feeling more than a little sure I was the one in charge."
            "That by grabbing hold of Reona with confidence, I'd asserted myself."
            "But her commands are more than enough to disabuse me of that notion."
            "And I find myself leaping to do as she says."
            show reona doggy vaginal eyes_closed
            "Luckily for me, it's not as though there's much work needs to be done."
            "Almost the same moment that the head of my cock touches her pussy, Reona starts to melt."
            "I honestly mean to spend some time teasing her before trying to push my way inside."
            "To linger around the edges of her pussy and work her into even more of a state."
            "But she's already so slippery down there I begin to lose control."
            "And the folds of her pussy conspire to steer my cock towards its centre."
            "Sure, there's a token amount of resistance, just enough to keep me out."
            "Yet that too is struggling against the fact that Reona's desperate to be fucked."
            "I can almost feel the last of her unconscious resistance falling away."
            "That is until I get the more immediate feeling of her grabbing my cock!"
            show reona doggy eyes_normal
            reona.say "Fuck the foreplay, [hero.name]…"
            reona.say "I already told you..."
            show reona doggy mouth_pleasure
            reona.say "I need cock!"
            "I'm gently pushing forwards as Reona says all of this."
            "And her words leave me stunned, yet still in motion."
            "She's also pushing the head of my cock hard against her lips at the same time."
            "Together these two things serve to give her exactly what she wants."
            show reona doggy smash eyes_closed mouth_normal
            "Reona's pussy parts, and I feel myself sinking straight into her."
            "Before now I was consciously trying to take my time."
            "To be sure that I gave her everything I had and missed nothing out."
            "But the sensation of being inside her seems to kind of blow my mind."
            "Reona just feels so good as she wraps around the length of my cock."
            "And then there's the sounds she's making too."
            "Every inch that slides into Reona makes her pant and gasp all the more."
            "Her head is nodding up and down, thanking me for what I'm doing to her."
            reona.say "Mmm..."
            reona.say "Oh...oh yeah..."
            reona.say "So good...so good..."
            show reona doggy eyes_normal
            reona.say "More...please?"
            "Without thinking, I leap into action, determined to give Reona what she wants."
            "Gripping her tighter than ever, I start to thrust in and out of her."
            show reona doggy -smash
            pause 0.35
            show reona doggy smash eyes_closed mouth_pleasure with hpunch
            pause 0.1
            show reona doggy bounce
            pause 0.15
            show reona doggy rest
            pause 0.35
            show reona doggy -smash
            pause 0.35
            show reona doggy smash with hpunch
            pause 0.1
            show reona doggy bounce
            pause 0.15
            show reona doggy rest
            "My movements are so fast and so sudden that she's almost flattened against the wall."
            show reona doggy eyes_normal
            "Somehow she manages to brace her arms against it, glancing back over her shoulder."
            "I can see that Reona's eyes are already starting to glaze over."
            "And the smile on her face looks like that of a gratified animal."
            "In fact, she looks so animalistic that I feel the urge to tame her."
            show reona doggy pulled eyes_closed
            "Reaching out with one hand, I twine my fingers in her hair."
            "Then I pull Reona's head backwards."
            "Not enough to hurt her, just enough to feel like I'm in control."
            "In response, Reona begins to gasp anew."
            show reona doggy eyes_normal
            "And I can see that the light has returned to her eyes."
            "Because now she's looking back at me with fevered interest in them."
            show reona doggy -smash
            pause 0.35
            show reona doggy smash mouth_teeth with hpunch
            pause 0.1
            show reona doggy bounce
            pause 0.15
            show reona doggy rest
            pause 0.35
            show reona doggy -smash
            pause 0.35
            show reona doggy smash with hpunch
            pause 0.1
            show reona doggy bounce
            pause 0.15
            show reona doggy rest
            "The sound of my legs slapping into Reona's thighs is getting ever louder."
            "And I can see her breasts swaying in sympathy too."
            "In fact her entire body is jiggling and bouncing."
            "Man, it's like fucking a hot, sexy inflatable!"
            show reona doggy -smash
            pause 0.25
            show reona doggy smash with hpunch
            pause 0.1
            show reona doggy bounce
            pause 0.15
            show reona doggy rest
            pause 0.25
            show reona doggy -smash
            pause 0.25
            show reona doggy smash eyes_ahegao with hpunch
            pause 0.1
            show reona doggy bounce
            pause 0.15
            show reona doggy rest
            "Suddenly I feel the sensation of Reona's pussy squeezing me hard."
            "All of her muscles are twitching, and her eyes are rolling back into her head."
            "Unless I'm very much mistaken, she's already starting to cum!"
            call cum_reaction (reona, 'vaginal', sexperience_min) from _call_cum_reaction_257
            if _return == "vaginal_outside":
                "I keep firm control of myself as I ride out Reona's orgasm."
                "And when I feel her pushing me towards my own, I make my move."
                show reona doggy out eyes_normal mouth_pleasure -smash
                "This amounts to me pulling out of her in one smooth motion."
                if not CONDOM:
                    show reona doggy cum
                    $ reona.love += 2
                with hpunch
                "Then I hold on tight as I shoot my load over her exposed back."
                with hpunch
                "By now I'm almost holding Reona up, pressing her against the wall."
                show reona doggy eyes_closed mouth_normal -pulled -cum
                "But when I shower her with cum, she finally flops forwards."
                "And I have to catch her before she falls."
            elif _return == "vaginal_condom":
                "Right now I'm more than glad that we chose to use a condom."
                "Because it means that I don't have to worry about a thing."
                "I can keep right on going, enjoying the feeling of Reona's orgasm."
                "And when mine comes close on its heels, I just go with it."
                show reona doggy -smash
                pause 0.15
                show reona doggy smash with hpunch
                pause 0.1
                show reona doggy bounce
                pause 0.15
                show reona doggy rest
                pause 0.15
                show reona doggy -smash
                pause 0.15
                show reona doggy smash eyes_closed mouth_ahegao with hpunch
                pause 0.1
                show reona doggy bounce
                pause 0.15
                show reona doggy rest
                "By now I'm almost holding Reona up, pressing her against the wall."
                show reona doggy mouth_pleasure -smash -pulled
                $ reona.love += 2
                "But when I lose it inside of her, she finally flops forwards."
                "And I have to catch her before she falls."
            elif _return == "vaginal_inside_pill":
                "Right now I'm more than glad that Reona remembered to tell me she was on the pill."
                "Because it means that I don't have to worry about a thing."
                "I can keep right on going, enjoying the feeling of Reona's orgasm."
                "And when mine comes close on its heels, I just go with it."
                show reona doggy -smash
                pause 0.15
                show reona doggy smash with hpunch
                pause 0.1
                show reona doggy bounce
                pause 0.15
                show reona doggy rest
                pause 0.15
                show reona doggy -smash
                pause 0.15
                show reona doggy smash mouth_ahegao with hpunch
                pause 0.1
                show reona doggy bounce
                pause 0.15
                show reona doggy rest
                "By now I'm almost holding Reona up, pressing her against the wall."
                show reona doggy eyes_closed -smash -pulled
                $ reona.love += 5
                "But when I lose it inside of her, she finally flops forwards."
                "And I have to catch her before she falls."
            elif _return == "vaginal_inside_pregnant":
                "The fact that Reona's pregnant does have some fringe benefits."
                "Like right now, it means that I don't have to worry about a thing."
                "I can keep right on going, enjoying the feeling of Reona's orgasm."
                "And when mine comes close on its heels, I just go with it."
                show reona doggy -smash
                pause 0.15
                show reona doggy smash with hpunch
                pause 0.1
                show reona doggy bounce
                pause 0.15
                show reona doggy rest
                pause 0.15
                show reona doggy -smash
                pause 0.15
                show reona doggy smash mouth_ahegao with hpunch
                pause 0.1
                show reona doggy bounce
                pause 0.15
                show reona doggy rest
                "By now I'm almost holding Reona up, pressing her against the wall."
                show reona doggy eyes_closed -smash -pulled
                $ reona.love += 3
                "But when I lose it inside of her, she finally flops forwards."
                "And I have to catch her before she falls."
            elif _return == "vaginal_inside_happy":
                "I keep firm control of myself as I ride out Reona's orgasm."
                "So when I feel myself coming I'm confident that I'll manage to pull out of Reona."
                "But that's when I realise she's tightening onto me!"
                reona.say "No..."
                reona.say "I'm not letting you go!"
                "I'm trying my best to escape her grip before it's too late but its only making the pleasure more intense."
                show reona doggy -smash
                pause 0.15
                show reona doggy smash with hpunch
                pause 0.1
                show reona doggy bounce
                pause 0.15
                show reona doggy rest
                pause 0.15
                show reona doggy -smash
                pause 0.15
                show reona doggy smash mouth_ahegao with hpunch
                $ reona.impregnate()
                pause 0.1
                show reona doggy bounce
                pause 0.15
                show reona doggy rest
                "By now I'm almost holding Reona up, pressing her against the wall."
                show reona doggy eyes_closed -smash -pulled
                $ reona.love += 5
                "But when I lose it inside of her, she finally flops forwards."
                "And I have to catch her before she falls."
            else:
                "I keep firm control of myself as I ride out Reona's orgasm."
                "And as I do so, my mind begins to wander..."
                reona.say "NO!"
                reona.say "Don't do it!"
                reona.say "Don't you dare cum in me!"
                "I freeze before I can pull out of Reona's pussy."
                "More from shock than any refusal to do as she says."
                show reona doggy -smash
                pause 0.15
                show reona doggy smash with hpunch
                pause 0.1
                show reona doggy bounce
                pause 0.15
                show reona doggy rest
                pause 0.15
                show reona doggy -smash
                pause 0.15
                show reona doggy smash eyes_pleasure mouth_teeth with hpunch
                $ reona.impregnate()
                pause 0.1
                show reona doggy bounce
                pause 0.15
                show reona doggy rest
                "By now I'm almost holding Reona up, pressing her against the wall."
                show reona doggy eyes_closed -smash -pulled
                $ reona.love -= 5
                "But when I lose it inside of her, she finally flops forwards."
                "And I have to catch her before she falls."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "If I wasn't under so much pressure, I might have been inspired to experiment."
            "But the urgency I'm feeling means that I want to get straight down to business."
            "And that's why I choose to focus my attention on Reona's pussy."
            "It's warm, slick and more than inviting right now."
            "So I line myself up and take aim..."
            show reona doggy mouth_normal
            reona.say "Come on, [hero.name]…"
            reona.say "Get your cock inside me already!"
            "I'd been feeling more than a little sure I was the one in charge."
            "That by grabbing hold of Reona with confidence, I'd asserted myself."
            "But her commands are more than enough to disabuse me of that notion."
            "And I find myself leaping to do as she says."
            show reona doggy vaginal eyes_closed
            "The only problem is that she makes me jump."
            "And that means my cock is out of position when I get down to it."
            "The head is pushed right between Reona's buttocks."
            "So when I push forwards, it's jammed hard against her tight little hole."
            "But she's already so slippery down there I begin to lose control."
            "And the pressing of her buttocks conspires to steer my cock towards its centre."
            "Sure, there's a token amount of resistance, just enough to keep me out."
            "Yet that too is struggling against the fact that Reona's desperate to be fucked."
            "I can almost feel the last of her unconscious resistance falling away."
            "That is until I get the more immediate feeling of her grabbing my cock!"
            show reona doggy eyes_normal
            reona.say "Fuck the foreplay, [hero.name]…"
            reona.say "I already told you..."
            show reona doggy mouth_pleasure
            reona.say "I need cock!"
            "I'm gently pushing forwards as Reona says all of this."
            "And her words leave me stunned, yet still in motion."
            "She's also pushing the head of my cock hard against her ass at the same time."
            "Together these two things serve to give her exactly what she wants."
            show reona doggy smash eyes_closed mouth_normal
            "Reona's ass opens up, and I feel myself sinking straight into her."
            "Before now I was consciously trying to take my time."
            "To be sure that I gave her everything I had and missed nothing out."
            "But the sensation of being inside her seems to kind of blow my mind."
            "Reona just feels so good as she wraps around the length of my cock."
            "And then there's the sounds she's making too."
            "Because now she's realising where I'm headed!"
            reona.say "Oh..."
            reona.say "Oh fuck...."
            reona.say "My ass!"
            "Every inch that slides into Reona makes her pant and gasp all the more."
            "Her head is nodding up and down, thanking me for what I'm doing to her."
            reona.say "Mmm..."
            reona.say "Oh...oh yeah..."
            reona.say "So good...so good..."
            show reona doggy eyes_normal
            reona.say "More...please?"
            "Without thinking, I leap into action, determined to give Reona what she wants."
            "Gripping her tighter than ever, I start to thrust in and out of her."
            show reona doggy -smash
            pause 0.35
            show reona doggy smash eyes_closed mouth_pleasure with hpunch
            pause 0.1
            show reona doggy bounce
            pause 0.15
            show reona doggy rest
            pause 0.35
            show reona doggy -smash
            pause 0.35
            show reona doggy smash with hpunch
            pause 0.1
            show reona doggy bounce
            pause 0.15
            show reona doggy rest
            "My movements are so fast and so sudden that she's almost flattened against the wall."
            show reona doggy eyes_normal
            "Somehow she manages to brace her arms against it, glancing back over her shoulder."
            "I can see that Reona's eyes are already starting to glaze over."
            "And the smile on her face looks like that of a gratified animal."
            "In fact, she looks so animalistic that I feel the urge to tame her."
            show reona doggy pulled eyes_closed
            "Reaching out with one hand, I twine my fingers in her hair."
            "Then I pull Reona's head backwards."
            "Not enough to hurt her, just enough to feel like I'm in control."
            "In response, Reona begins to gasp anew."
            show reona doggy eyes_normal
            "And I can see that the light has returned to her eyes."
            "Because now she's looking back at me with fevered interest in them."
            show reona doggy -smash
            pause 0.35
            show reona doggy smash mouth_teeth with hpunch
            pause 0.1
            show reona doggy bounce
            pause 0.15
            show reona doggy rest
            pause 0.35
            show reona doggy -smash
            pause 0.35
            show reona doggy smash with hpunch
            pause 0.1
            show reona doggy bounce
            pause 0.15
            show reona doggy rest
            "The sound of my legs slapping into Reona's thighs is getting ever louder."
            "And I can see her breasts swaying in sympathy too."
            "In fact her entire body is jiggling and bouncing."
            "Man, it's like fucking a hot, sexy inflatable!"
            show reona doggy -smash
            pause 0.25
            show reona doggy smash with hpunch
            pause 0.1
            show reona doggy bounce
            pause 0.15
            show reona doggy rest
            pause 0.25
            show reona doggy -smash
            pause 0.25
            show reona doggy smash eyes_ahegao with hpunch
            pause 0.1
            show reona doggy bounce
            pause 0.15
            show reona doggy rest
            "Suddenly I feel the sensation of Reona's ass squeezing me hard."
            "All of her muscles are twitching, and her eyes are rolling back into her head."
            "Unless I'm very much mistaken, she's already starting to cum!"
            call cum_reaction (reona, 'anal', sexperience_min) from _call_cum_reaction_258
            if _return == 'anal_outside':
                "I keep firm control of myself as I ride out Reona's orgasm."
                "And when I feel her pushing me towards my own, I make my move."
                show reona doggy out eyes_normal mouth_pleasure -smash
                "This amounts to me pulling out of her in one smooth motion."
                show reona doggy cum with hpunch
                $ reona.sub += 1
                "Then I hold on tight as I shoot my load over her exposed back."
                with hpunch
                "By now I'm almost holding Reona up, pressing her against the wall."
                show reona doggy eyes_closed mouth_normal -pulled -cum
                "But when I shower her with cum, she finally flops forwards."
                "And I have to catch her before she falls."
            elif _return == 'anal_inside':
                "Right now I'm more than glad that I kept on taking Reona up the ass."
                "Because it means that I don't have to worry about a thing."
                "I can keep right on going, enjoying the feeling of Reona's orgasm."
                "And when mine comes close on its heels, I just go with it."
                show reona doggy -smash
                pause 0.15
                show reona doggy smash with hpunch
                pause 0.1
                show reona doggy bounce
                pause 0.15
                show reona doggy rest
                pause 0.15
                show reona doggy -smash
                pause 0.15
                show reona doggy smash mouth_ahegao with hpunch
                pause 0.1
                show reona doggy bounce
                pause 0.15
                show reona doggy rest
                "By now I'm almost holding Reona up, pressing her against the wall."
                show reona doggy eyes_closed -smash -pulled
                $ reona.sub += 2
                "But when I lose it inside of her, she finally flops forwards."
                "And I have to catch her before she falls."
    return

label whore_harem_beach_fuck_intro(appointment=None):
    "I pack my things and head to the beach."
    scene bg beach with fade
    "Once I get there, it doesn't take me long to spot Reona and Lexi"
    mike.say "Hey, girls..."
    mike.say "I got here as soon as I could!"
    show reona swimsuit zorder 2 with dissolve
    show lexi a smile swimsuit nophone zorder 1 with dissolve
    pause 0.3
    show reona at left4
    show lexi a at right4
    with ease
    "Lexi waves and gives me a smile."
    show lexi a smile
    show reona happy
    lexi.say "Hi, [hero.name]…"
    reona.say "Hi, [hero.name]…"
    "We start to walk down to the beach."

    call whore_harem_beach_fuck from _call_whore_harem_beach_fuck_1

    $ lexi.sexperience += 1
    $ reona.sexperience += 1
    $ game.pass_time(4)
    scene bg black with dissolve
    return

label whore_harem_beach_fuck:
    $ reona.set_room("beach")
    $ lexi.set_room("beach")
    scene bg black
    show whore handjob sign nomc
    with fade
    "But as soon as we get there, I'm presented with my first real challenge."
    "Which is a mass of naked bodies, spread out over the length of the sand."
    mike.say "Erm..."
    mike.say "Do we strip off now?"
    reona.say "Of course not, silly!"
    lexi.say "We find a spot first."
    "Reona and Lexi seem to know what they're doing."
    scene bg beach with fade
    "So I just follow their lead, allowing them to pick the spot."
    "And then I watch as they begin to take off their swimming costumes."
    "I reckon I have about thirty seconds grace before someone notices I'm not getting naked."
    "So I use that time to steel myself, remembering that everyone's naked here already."
    "Then I take a deep breath and put both hands on the waistband of my trunks."
    "Without pausing, I pull them all the way down and step out of them."
    "And as soon as I do so, I have to admit that it doesn't feel too bad."
    "Nobody seems to be staring at me, they're just acting perfectly normal."
    "Well, as normal as things can be when everyone in sight is totally naked!"
    mike.say "Okay..."
    mike.say "This is good."
    mike.say "This is really..."
    show whore handjob nomc naked holding sign with fade
    mike.say "Whoa!"
    "I'm really thinking that I can handle this, until I turn around."
    "Because that's when I see Lexi and Reona for the first time."
    "I mean, I've seen girls naked before, of course I have."
    "But there's just something about seeing the pair of them like this."
    "They're standing there on the sand, smiling and waving at me."
    "And I guess it just somehow blows a part of my mind."
    show whore handjob down
    lexi.say "Oh, look, Reona..."
    lexi.say "I think someone likes what he sees!"
    reona.say "Yeah, Lexi..."
    reona.say "He's certainly saluting us!"
    "Their eyes wander downwards, settling on my groin."
    "And as soon as I follow them down, I see what they're talking about."
    "My cock is totally beginning to rise from the sight of them!"
    "Feeling my cheeks flush, I sit down on the sand."
    "And then I do the best I can to hide my erection from sight."
    "But of course I'm not going to get any mercy from Lexi and Reona."
    "They stride right over to where I'm sitting, in all of their nakedness."
    "And I swear they're making their bodies jiggle and sway more than normal too!"
    lexi.say "Aww..."
    lexi.say "Did the big, bad boobies scare you?"
    reona.say "Don't worry, [hero.name]…"
    reona.say "We won't bite!"
    reona.say "Well...not too hard..."
    show whore handjob -nomc limp still with fade
    "Before I know what's happening, Lexi and Reona are all over me."
    "First one of them is kissing me, then the other."
    show whore handjob -nomc hj
    "And their hands are roaming over my body at the same time too."
    "At first the feeling is so intense that I hardly notice the sounds."
    show whore handjob speed at startle(0.05,-10)
    "But as things get more intense, they become ever louder too."
    "So much so that when I have the chance to speak, I have to ask."
    mike.say "Wha..."
    mike.say "What's all the noise?"
    reona.say "Oh, just ignore that, [hero.name]..."
    reona.say "It's only the other people on the beach."
    lexi.say "They're watching the show..."
    lexi.say "Hoping that we put on a good performance!"
    "Looking around, I can see that they're right."
    "Almost everyone that can is looking in our direction."
    "And they seem to be studying us with interest too!"
    "Part of me wants to say that this is all wrong."
    "That we really shouldn't be getting intimate in front of these people."
    "But it's getting drowned out by the part of me that just wants to have fun."
    "The part of me that really doesn't care who sees me get my hands on Lexi and Reona."
    "And you can guess which part of me wins out in the end."
    "Because a moment later, I reach out and grab hold of one of the girls."
    menu:
        "Fuck Lexi":
            show whore doggy onlexi with fade
            "I clap my hands onto Lexi's haunches, meaning to pull her straight onto me."
            "But rather than simply letting me have my way, she scuttles out of reach."
            with hpunch
            "Which in turn forces me to get onto my hands and knees to chase her across the sand."
            mike.say "Hey..."
            mike.say "Get back here!"
            lexi.say "You think I'm gonna make this easy for you?"
            lexi.say "You gotta catch me first!"
            "For all of Lexi's defiance, it doesn't take me long to do just that."
            "I catch her no more than a few feet away, pulling her backwards and against me."
            "It's only when I look down that I realise Lexi's been clambering over Reona."
            "And the second before I managed to catch her, they'd pressed their lips together."
            "That's when I hear some of the watchers on the beach laughing and cheering."
            show whore doggy down
            pause 0.2
            show whore doggy up
            pause 0.2
            show whore doggy down
            pause 0.2
            show whore doggy up
            pause 0.2
            show whore doggy down
            "Hell, some of them are even clapping my efforts!"
            "Well of course they are - they're getting to see the girls make out."
            "And then there's the added attraction of me fucking Lexi at the same time!"
            "Rather than being embarrassed, I feel encouraged."
            "And so I waste no time in thrusting myself between Lexi's thighs."
            menu:
                "Fuck her pussy":
                    show whore doggy onlexi
                    "I know that I'm more than ready for the task at hand, that I can't get any harder."
                    "But as soon as the head of my cock slides against Lexi's pussy, I know she is too."
                    "They're warm, soft and totally slick, already feeling like they're melting against me."
                    "And that's all the encouragement I need to begin moving myself back and forth."
                    "Lexi starts to moan almost as soon as I get going, pushing herself backwards."
                    "This means that she's grinding against me as I'm pushing forwards."
                    show whore doggy vaginal
                    "So it's not long before the inevitable happens, as her lips begin to part."
                    "I can feel myself sinking into Lexi, deeper with every passing second."
                    "And I know that she's feeling it too."
                    "Because she's not exactly keeping quiet!"
                    "It's now that she breaks away from kissing Reona."
                    "And instead she begins to urge me on in my efforts."
                    lexi.say "Uh..."
                    lexi.say "Oh yeah..."
                    lexi.say "Oh fuck yeah..."
                    lexi.say "Give it to me!"
                    "But it's not like I need the encouragement."
                    show whore doggy vaginal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "As soon as my cock's all the way inside of Lexi, nothing's going to hold me back."
                    "With a firm hold on her haunches, I launch myself into the task of fucking her."
                    show whore doggy vaginal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "My body moves faster with each passing second, my thrusts getting harder too."
                    "Lexi doesn't seem to be able to keep up the demands that she was making any more."
                    show whore doggy vaginal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "Instead her words quickly turn into unintelligible moans of almost animal pleasure."
                    "But the sound isn't something I have to put up with for too long."
                    show whore doggy vaginal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "As Reona seems to be feeding on the sight of the other girl getting pumped."
                    show whore doggy ahegao
                    "And she soon plants her lips on Lexi's again, jamming her tongue between them."
                    "All of this only serves to make me all the more determined in what I'm doing."
                    "With Lexi totally occupied, she's at my mercy, totally helpless to resist."
                    show whore doggy vaginal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "Every time I push myself into her, I feel like that might be the last time."
                    "That I'm going to feel myself losing it and shoot my load into Lexi."
                    show whore doggy vaginal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "But somehow I manage to keep going, prolonging the experience just a little longer."
                    "And it's not just Lexi and I that seem to appreciate that fact either."
                    show whore doggy vaginal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "I can hear the cheering still coming from the other people on the beach."
                    "Hell, I swear I even catch sight of some pleasuring themselves at the sight!"
                    show whore doggy vaginal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "The whole thing makes me feel like I'm an athlete in some weird erotic competition."
                    "Like they'll start holding up score-cards once it's all over or something."
                    show whore doggy vaginal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "In which case, they'd better get ready to grade my performance."
                    "Because I can feel myself getting ready to cum!"
                    menu:
                        "Cum inside":
                            with hpunch
                            "Reona keeps right on kissing Lexi as I thrust into her."
                            show whore doggy vaginal creampie with hpunch
                            "And she doesn't stop even as I let go and fill up her pussy."
                            show whore doggy closed with hpunch
                            "All that Lexi can manage is a muffled moan of pleasure."
                            "Which comes out of her as I hold her firmly in place."
                            "And while cum starts to ooze out around my cock."
                        "Pull out":
                            "Reona keeps right on kissing Lexi as I pull out of her."
                            show whore doggy out down
                            pause 0.2
                            show whore doggy up
                            pause 0.2
                            show whore doggy down
                            pause 0.2
                            show whore doggy up
                            pause 0.2
                            show whore doggy down cumshot with hpunch
                            "And she doesn't stop even as I lose it and shoot my load over her ass."
                            show whore doggy out up -cumshot
                            pause 0.2
                            show whore doggy down
                            pause 0.2
                            show whore doggy up
                            pause 0.2
                            show whore doggy down cumshot cum onbody with hpunch
                            "All that Lexi can manage is a muffled moan of pleasure."
                            show whore doggy up -cumshot
                            pause 0.2
                            show whore doggy down cumshot cum onbody with hpunch
                            "Which comes out of her as I hold her firmly in place."
                            show whore doggy -cumshot
                            "And while cum spatters over her back and buttocks."
                "Fuck her ass":
                    show whore doggy onlexi
                    "I know that I'm more than ready for the task at hand, that I can't get any harder."
                    "But as soon as the head of my cock slides between Lexi's buttocks, I know she is too."
                    "They're warm, soft and totally welcoming, already feeling like they're melting against me."
                    "And that's all the encouragement I need to begin moving myself back and forth."
                    "Lexi starts to moan almost as soon as I get going, pushing herself backwards."
                    "This means that she's grinding against me as I'm pushing forwards."
                    show whore doggy anal
                    "So it's not long before the inevitable happens, as her muscles begin to relax."
                    "I can feel myself sinking into Lexi, deeper with every passing second."
                    "And I know that she's feeling it too."
                    "Because she's not exactly keeping quiet!"
                    "It's now that she breaks away from kissing Reona."
                    "And instead she begins to urge me on in my efforts."
                    lexi.say "Uh..."
                    lexi.say "Oh yeah..."
                    lexi.say "Oh fuck yeah..."
                    lexi.say "Give it to me!"
                    "But it's not like I need the encouragement."
                    show whore doggy anal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "As soon as my cock's all the way inside of Lexi, nothing's going to hold me back."
                    "With a firm hold on her haunches, I launch myself into the task of fucking her."
                    show whore doggy anal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "My body moves faster with each passing second, my thrusts getting harder too."
                    "Lexi doesn't seem to be able to keep up the demands that she was making any more."
                    show whore doggy anal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "Instead her words quickly turn into unintelligible moans of almost animal pleasure."
                    "But the sound isn't something I have to put up with for too long."
                    show whore doggy anal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "As Reona seems to be feeding on the sight of the other girl getting pumped."
                    show whore doggy ahegao
                    "And she soon plants her lips on Lexi's again, jamming her tongue between them."
                    "All of this only serves to make me all the more determined in what I'm doing."
                    "With Lexi totally occupied, she's at my mercy, totally helpless to resist."
                    show whore doggy anal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "Every time I push myself into her, I feel like that might be the last time."
                    "That I'm going to feel myself losing it and shoot my load into Lexi."
                    show whore doggy anal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "But somehow I manage to keep going, prolonging the experience just a little longer."
                    "And it's not just Lexi and I that seem to appreciate that fact either."
                    show whore doggy anal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "I can hear the cheering still coming from the other people on the beach."
                    "Hell, I swear I even catch sight of some pleasuring themselves at the sight!"
                    show whore doggy anal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "The whole thing makes me feel like I'm an athlete in some weird erotic competition."
                    "Like they'll start holding up score-cards once it's all over or something."
                    show whore doggy anal onlexi at stepback(speed=0.1, h=-10, v=-5)
                    "In which case, they'd better get ready to grade my performance."
                    "Because I can feel myself getting ready to cum!"
                    menu:
                        "Cum inside":
                            with hpunch
                            "Reona keeps right on kissing Lexi as I thrust into her."
                            show whore doggy anal creampie with hpunch
                            "And she doesn't stop even as I let go and fill up her pussy."
                            show whore doggy closed with hpunch
                            "All that Lexi can manage is a muffled moan of pleasure."
                            "Which comes out of her as I hold her firmly in place."
                            "And while cum starts to ooze out around my cock."
                        "Pull out":
                            "Reona keeps right on kissing Lexi as I pull out of her."
                            show whore doggy out down
                            pause 0.2
                            show whore doggy up
                            pause 0.2
                            show whore doggy down
                            pause 0.2
                            show whore doggy up
                            pause 0.2
                            show whore doggy down cumshot with hpunch
                            "And she doesn't stop even as I lose it and shoot my load over her ass."
                            show whore doggy out up -cumshot
                            pause 0.2
                            show whore doggy down
                            pause 0.2
                            show whore doggy up
                            pause 0.2
                            show whore doggy down cumshot cum onbody with hpunch
                            "All that Lexi can manage is a muffled moan of pleasure."
                            show whore doggy up -cumshot
                            pause 0.2
                            show whore doggy down cumshot cum onbody with hpunch
                            "Which comes out of her as I hold her firmly in place."
                            show whore doggy -cumshot
                            "And while cum spatters over her back and buttocks."
        "Fuck Reona":
            "I make a grab for Reona, meaning to pull her towards me."
            "But she wriggles and squirms, giggling as she slips away."
            "I make to follow, but the effort of reaching for her throws me off balance."
            with vpunch
            "And instead of getting hold of Reona, I end up falling flat on my back."
            reona.say "Oh no..."
            reona.say "You fell down!"
            reona.say "Be a shame if someone were to..."
            reona.say "Take advantage of you!"
            show whore reverse cowgirl raising up with vpunch
            "As she's saying this, Reona turns around and pounces on me."
            "She lands on my legs with her back turned, pinning me to the sand."
            "And then she straddles my thighs, pushing her ass backwards."
            mike.say "Huh..."
            mike.say "What are you..."
            "Reona waggles her ass in front of me, keeping it just out of reach."
            "And it doesn't take me long to figure out that she's teasing me with it."
            "So I make to sit up and grab hold of her again."
            lexi.say "Oh no you don't!"
            "No sooner have my shoulders lifted off the sand than they're pushed back down again."
            "And I turn my head to see Lexi, chuckling as she uses all of her weight to pin me down."
            mike.say "Hey!"
            mike.say "What are you..."
            mike.say "Stop that!"
            "Lexi and Reona don't seem to be in any hurry to do as I ask."
            "Instead they keep on holding me down and teasing me."
            "And I can already hear laughter coming from further away too."
            "Which makes me think the other people on the beach are enjoying the show."
            "And if that's the case, then I'm not going to be the comedy relief."
            "I want to be the star attraction!"
            menu:
                "Fuck her pussy":
                    "Summoning a sudden and unexpected burst of strength, I make to sit up."
                    "And luckily for me, Lexi seems to have taken her eyes off the prize."
                    "Because I manage to take her completely by surprise, throwing her off."
                    lexi.say "Whoa..."
                    "At the sound of Lexi's cry, Reona turns her head to see what's happening."
                    reona.say "Huh?"
                    "But that's all she gets the chance to say."
                    "As I'm already taking hold of her."
                    "With a hand on either side of Reona's waist, I pull her firmly downwards."
                    show whore reverse cowgirl vaginal up
                    "An action that introduces her to the head of my cock, waiting below."
                    "Reona can do nothing but moan as she sits down on it."
                    "And as she does so, the inevitable begins to happen."
                    "Her pussy manages to hold out for perhaps thirty seconds."
                    "But the state of arousal that she's in combines with the force of gravity."
                    show whore reverse cowgirl lying vaginal down with vpunch
                    "And there's nothing she can do to keep herself from beginning to sink downwards."
                    "I'm nodding and smiling as I feel Reona's pussy open up to me."
                    "On the one hand because it's a pretty amazing sensation from my point of view."
                    "And on the other because it means that I'm now the one in control."
                    "Before the people watching us were laughing and joking."
                    "But now they're being treated to an intense display of passionate love-making."
                    "One that's being masterfully delivered, even if I do say so myself!"
                    mike.say "How's that feel, Reona?"
                    mike.say "Are you liking it, huh?"
                    mike.say "You want some more?"
                    "I know that Reona can hear every word I'm saying."
                    "Because at first she nods her head eagerly."
                    "And then she turns it to look back over her shoulder at me."
                    show whore reverse cowgirl raising
                    reona.say "Y...yeah..."
                    show whore reverse cowgirl raising down
                    reona.say "I want it..."
                    show whore reverse cowgirl raising up
                    reona.say "I want it so badly!"
                    show whore reverse cowgirl raising down
                    "I can't help the smile that creeps across my face at the admission."
                    "Feeling like I'm finally the one in the driving seat, the one in control!"
                    show whore reverse cowgirl raising up
                    pause 0.2
                    show whore reverse cowgirl raising down at startle(0.05,-10)
                    pause 0.2
                    show whore reverse cowgirl raising up
                    pause 0.2
                    show whore reverse cowgirl raising down at startle(0.05,-10)
                    "So I launch myself into fucking Reona, not caring about anything else."
                    "Which I guess is why I'm not prepared for that happens next."
                    lexi.say "Hey, [hero.name]..."
                    lexi.say "Did you miss me?"
                    "Lexi seems to pop up out of nowhere, pushing me down with both hands."
                    "There's no way I can respond, so I end up on my back again."
                    "But this time Lexi's not about to let me turn the tables on her."
                    "Before I can regain my balance, she straddles my chest."
                    "And then she lowers herself onto my face!"
                    mike.say "What the..."
                    mike.say "Mmmph..."
                    "Even in my current state of confusion, it's pretty obvious what's happening."
                    "Lexi's getting in on the action and making me use my mouth for other things."
                    "And the only way out of this situation is going to be by pleasuring her like crazy."
                    "So that's exactly what I do, probing and licking with my tongue."
                    show whore reverse cowgirl raising up ahegao
                    pause 0.2
                    show whore reverse cowgirl raising down at startle(0.05,-10)
                    pause 0.2
                    show whore reverse cowgirl raising up
                    pause 0.2
                    show whore reverse cowgirl raising down at startle(0.05,-10)
                    "The results seem to be instant too, as Lexi squirms almost as much as Reona."
                    "But at the same time I can feel that something else is about to happen too."
                    "I'm going to cum, and I need to decide where I want to be when I lose it!"
                    menu:
                        "Cum inside":
                            "Still pleasuring Lexi for all I'm worth, I decide to let nature take it's course."
                            show whore reverse cowgirl raising up
                            pause 0.2
                            show whore reverse cowgirl raising down at startle(0.05,-10)
                            pause 0.2
                            show whore reverse cowgirl raising up cum
                            pause 0.2
                            show whore reverse cowgirl lying down -cum with vpunch
                            "Which means lying back and shooting my load deep into Reona at the same time."
                            show whore reverse cowgirl lying up cum
                            pause 0.2
                            show whore reverse cowgirl lying down -cum at startle(0.05,-10)
                            pause 0.2
                            show whore reverse cowgirl lying up cum
                            pause 0.2
                            show whore reverse cowgirl lying down -cum with vpunch
                            "I can feel every moment of the process as it happens, and the effect it's having."
                            show whore reverse cowgirl close with vpunch
                            "But there's no way I can hear the sounds that Reona's making."
                            "Or the reaction of everyone watching us."
                        "Pull out":
                            "There's no way that I can get out from under Lexi in order to do anything."
                            show whore reverse cowgirl raising up
                            pause 0.2
                            show whore reverse cowgirl raising down at startle(0.05,-10)
                            pause 0.2
                            show whore reverse cowgirl raising up
                            pause 0.2
                            show whore reverse cowgirl lying down at startle(0.05,-10)
                            "But I want to pull out of Reona before I shoot my load."
                            "So I have to shake my entire body, rocking from side to side."
                            show whore reverse cowgirl raising up
                            pause 0.2
                            show whore reverse cowgirl raising down at startle(0.05,-10)
                            pause 0.2
                            show whore reverse cowgirl raising up
                            pause 0.2
                            show whore reverse cowgirl lying down at startle(0.05,-10)
                            "The motion isn't enough to dislodge Reona, but it's sufficient to free something else."
                            show whore reverse cowgirl -vaginal with vpunch
                            "At the last moment, I feel my cock break free popping out of her."
                            show whore reverse cowgirl cumshot with vpunch
                            "A moment later it happens, and I shoot warm, sticky cum up Reona's back."
                "Fuck her ass":
                    "Summoning a sudden and unexpected burst of strength, I make to sit up."
                    "And luckily for me, Lexi seems to have taken her eyes off the prize."
                    "Because I manage to take her completely by surprise, throwing her off."
                    lexi.say "Whoa..."
                    "At the sound of Lexi's cry, Reona turns her head to see what's happening."
                    reona.say "Huh?"
                    "But that's all she gets the chance to say."
                    "As I'm already taking hold of her."
                    "With a hand on either side of Reona's waist, I pull her firmly downwards."
                    "An action that introduces her to the head of my cock, waiting below."
                    show whore reverse cowgirl anal up
                    "Reona can do nothing but moan as she sits down on it."
                    "And as she does so, the inevitable begins to happen."
                    "Her ass manages to hold out for perhaps thirty seconds."
                    "But the state of arousal that she's in combines with the force of gravity."
                    show whore reverse cowgirl lying anal down with vpunch
                    "And there's nothing she can do to keep herself from beginning to sink downwards."
                    "I'm nodding and smiling as I feel Reona's ass open up to me."
                    "On the one hand because it's a pretty amazing sensation from my point of view."
                    "And on the other because it means that I'm now the one in control."
                    "Before the people watching us were laughing and joking."
                    "But now they're being treated to an intense display of passionate love-making."
                    "One that's being masterfully delivered, even if I do say so myself!"
                    mike.say "How's that feel, Reona?"
                    mike.say "Are you liking it, huh?"
                    mike.say "You want some more?"
                    "I know that Reona can hear every word I'm saying."
                    "Because at first she nods her head eagerly."
                    "And then she turns it to look back over her shoulder at me."
                    show whore reverse cowgirl raising
                    reona.say "Y...yeah..."
                    show whore reverse cowgirl raising down
                    reona.say "I want it..."
                    show whore reverse cowgirl raising up
                    reona.say "I want it so badly!"
                    show whore reverse cowgirl raising down
                    "I can't help the smile that creeps across my face at the admission."
                    "Feeling like I'm finally the one in the driving seat, the one in control!"
                    show whore reverse cowgirl raising up
                    pause 0.2
                    show whore reverse cowgirl raising down at startle(0.05,-10)
                    pause 0.2
                    show whore reverse cowgirl raising up
                    pause 0.2
                    show whore reverse cowgirl raising down at startle(0.05,-10)
                    "So I launch myself into fucking Reona, not caring about anything else."
                    "Which I guess is why I'm not prepared for that happens next."
                    lexi.say "Hey, [hero.name]..."
                    lexi.say "Did you miss me?"
                    "Lexi seems to pop up out of nowhere, pushing me down with both hands."
                    "There's no way I can respond, so I end up on my back again."
                    "But this time Lexi's not about to let me turn the tables on her."
                    "Before I can regain my balance, she straddles my chest."
                    "And then she lowers herself onto my face!"
                    mike.say "What the..."
                    mike.say "Mmmph..."
                    "Even in my current state of confusion, it's pretty obvious what's happening."
                    "Lexi's getting in on the action and making me use my mouth for other things."
                    "And the only way out of this situation is going to be by pleasuring her like crazy."
                    "So that's exactly what I do, probing and licking with my tongue."
                    show whore reverse cowgirl raising up ahegao
                    pause 0.2
                    show whore reverse cowgirl raising down at startle(0.05,-10)
                    pause 0.2
                    show whore reverse cowgirl raising up
                    pause 0.2
                    show whore reverse cowgirl raising down at startle(0.05,-10)
                    "The results seem to be instant too, as Lexi squirms almost as much as Reona."
                    "But at the same time I can feel that something else is about to happen too."
                    "I'm going to cum, and I need to decide where I want to be when I lose it!"
                    menu:
                        "Cum inside":
                            "Still pleasuring Lexi for all I'm worth, I decide to let nature take it's course."
                            show whore reverse cowgirl raising up
                            pause 0.2
                            show whore reverse cowgirl raising down at startle(0.05,-10)
                            pause 0.2
                            show whore reverse cowgirl raising up cum
                            pause 0.2
                            show whore reverse cowgirl lying down -cum with vpunch
                            "Which means lying back and shooting my load deep into Reona at the same time."
                            show whore reverse cowgirl lying up cum
                            pause 0.2
                            show whore reverse cowgirl lying down -cum at startle(0.05,-10)
                            pause 0.2
                            show whore reverse cowgirl lying up cum
                            pause 0.2
                            show whore reverse cowgirl lying down -cum with vpunch
                            "I can feel every moment of the process as it happens, and the effect it's having."
                            show whore reverse cowgirl close with vpunch
                            "But there's no way I can hear the sounds that Reona's making."
                            "Or the reaction of everyone watching us."
                        "Pull out":
                            "There's no way that I can get out from under Lexi in order to do anything."
                            show whore reverse cowgirl raising up
                            pause 0.2
                            show whore reverse cowgirl raising down at startle(0.05,-10)
                            pause 0.2
                            show whore reverse cowgirl raising up
                            pause 0.2
                            show whore reverse cowgirl lying down at startle(0.05,-10)
                            "But I want to pull out of Reona before I shoot my load."
                            "So I have to shake my entire body, rocking from side to side."
                            show whore reverse cowgirl raising up
                            pause 0.2
                            show whore reverse cowgirl raising down at startle(0.05,-10)
                            pause 0.2
                            show whore reverse cowgirl raising up
                            pause 0.2
                            show whore reverse cowgirl lying down at startle(0.05,-10)
                            "The motion isn't enough to dislodge Reona, but it's sufficient to free something else."
                            show whore reverse cowgirl -anal with vpunch
                            "At the last moment, I feel my cock break free popping out of her."
                            show whore reverse cowgirl cumshot with vpunch
                            "A moment later it happens, and I shoot warm, sticky cum up Reona's back."
        "Ask Lexi for a blowjob":
            show whore lexiblowjob with fade
            "Just when I feel like I'm about to shoot my load, Lexi makes her move."
            "She all but dives for my cock, her mouth open to show that she means business."
            show whore lexiblowjob blowjob
            "And a second later she's clamped on, unwilling to let go for even a moment."
            "Somehow the shock of the change seems to have an instant effect on me."
            "It stops me from shooting my load straight away, and I find myself holding on."
            "All the while, Lexi's working away at me with frantic speed and intent."
            "Her head bobs up and down, picking up speed as she gets into it."
            "But not to be outdone, Reona takes advantage of Lexi's distraction."
            "I watch as she all but pounces on the other girl's pussy."
            show whore lexiblowjob up
            pause 0.2
            show whore lexiblowjob mid
            pause 0.2
            show whore lexiblowjob down
            pause 0.2
            show whore lexiblowjob mid
            pause 0.1
            show whore lexiblowjob up
            "And then she goes down on Lexi just like she's going down on me!"
            show whore lexiblowjob up
            pause 0.2
            show whore lexiblowjob mid
            pause 0.2
            show whore lexiblowjob down
            pause 0.2
            show whore lexiblowjob mid
            pause 0.1
            show whore lexiblowjob up
            "Reona's attentions don't stop anything, not even for an instant."
            show whore lexiblowjob up
            pause 0.2
            show whore lexiblowjob mid
            pause 0.2
            show whore lexiblowjob down
            pause 0.2
            show whore lexiblowjob mid
            pause 0.1
            show whore lexiblowjob up
            "Instead they make the whole thing that much more intense."
            show whore lexiblowjob up
            pause 0.2
            show whore lexiblowjob mid
            pause 0.2
            show whore lexiblowjob down
            pause 0.2
            show whore lexiblowjob mid
            pause 0.1
            show whore lexiblowjob up
            "Lexi redoubles her efforts, soon pushing me back to the point of orgasm."
            show whore lexiblowjob up
            pause 0.2
            show whore lexiblowjob mid
            pause 0.2
            show whore lexiblowjob down
            pause 0.2
            show whore lexiblowjob mid
            pause 0.1
            show whore lexiblowjob up
            "And so now I have to decide where it's going to go!"
            menu:
                "Cum inside":
                    "Lexi doesn't seem to have a problem with my cock being almost down her throat."
                    "So I decide to leave it there as I feel myself start to cum."
                    show whore lexiblowjob cum with hpunch
                    "And true to form, she handles it like a pro, not gagging once."
                    show whore lexiblowjob closed with hpunch
                    "Lexi swallows every last drop, even sucking the last at the very end."
                "Pull out":
                    "I make to pull my cock out of Lexi's mouth, and she instantly gets what I'm doing."
                    "This means that she smoothly pulls her head back and releases me without hesitation."
                    show whore lexiblowjob lick -blowjob
                    "And once my cock is out, bobbing in front of her eyes, she waits patiently."
                    show whore lexiblowjob cumshot with hpunch
                    "No more than a second later it happens, and I shoot my load right into her face."
                    with hpunch
                    "But Lexi doesn't flinch even once, smiling as I paint her cheeks with cum."
        "Ask Reona for a blowjob":
            "I feel like I'm about to blow, when everything gets turned upside down."
            "Suddenly Lexi's clambering around on top of me, almost like she's looking for something."
            hide whore
            show whore reonablowjob
            with fade
            "But then I see Reona dart behind her, and then I feel her take hold of my cock!"
            lexi.say "Hey..."
            lexi.say "What are you..."
            show whore reonablowjob blowjob
            "By the time Lexi manages to get her words out, Reona's already got the head in her mouth."
            "And she doesn't waste any time in beginning to give me head as soon as she does either."
            "Luckily for me, Lexi seems to take this as a sign that she's been beaten to the punch."
            "Which is a relief, as I don't want them arguing over my manhood."
            "As well as the fact that what Reona's doing feels incredibly good!"
            show whore reonablowjob hand close moan
            "Somehow the shock of the change seems to have an instant effect on me."
            "It stops me from shooting my load straight away, and I find myself holding on."
            "All the while, Reona's working away at me with frantic speed and intent."
            "Her head bobs up and down, picking up speed as she gets into it."
            "This is the kind of thing that I'd like to last as long as humanly possible."
            "But even before Reona got started I was on the verge of losing it."
            show whore reonablowjob handjob
            "And so she's soon pushing me back to the point of orgasm."
            "So now I have to decide where it's going to go!"
            menu:
                "Cum inside":
                    "Reona doesn't seem to have a problem with my cock being almost down her throat."
                    "So I decide to leave it there as I feel myself start to cum."
                    show whore reonablowjob cum with vpunch
                    "And true to form, she handles it like a pro, not gagging once."
                    with vpunch
                    "Lexi swallows every last drop, even sucking the last at the very end."
                "Pull out":
                    "I make to pull my cock out of Reona's mouth, and she instantly gets what I'm doing."
                    "This means that she smoothly pulls her head back and releases me without hesitation."
                    show whore reonablowjob lick
                    "And once my cock is out, bobbing in front of her eyes, she waits patiently."
                    show whore reonablowjob cumshot with vpunch
                    "No more than a second later it happens, and I shoot my load right into her face."
                    with vpunch
                    "But Reona doesn't flinch even once, smiling as I paint her cheeks with cum."
        "Ask both of them for a blowjob":
            "Just as I feel like I'm about to shoot my load, Lexi and Reona start to move."
            "Without a word to me about what they're doing, they haul me up into a sitting position."
            hide whore
            show whore blowjob
            with fade
            "And just like that, they both start working on my cock!"
            show whore blowjob lexiblow
            "Somehow the shock of the change seems to have an instant effect on me."
            "It stops me from shooting my load straight away, and I find myself holding on."
            "That's how I find myself watching as Lexi and Reona stroke the shaft."
            show whore blowjob reonablow
            "And then they start to lean in closer, kissing and licking too."
            "So it looks like I'm getting a full-on double blow-job to finish off!"
            "All I have to do is sit back and leave the girls to it."
            show whore blowjob lexiblow
            "Well, that and enjoy myself while it lasts!"
            "I can see that there are a lot of people watching with interest too."
            "As though this is a fitting ending to the show that we've been putting on."
            show whore blowjob reonablow
            "All the while I'm looking around, Lexi and Reona are working away with frantic speed and intent."
            "Their heads bob up and down, picking up speed as they get into it."
            "This is the kind of thing that I'd like to last as long as humanly possible."
            show whore blowjob lexiblow
            "But even before Lexi and Reona got started I was on the verge of losing it."
            "And so they're soon pushing me back to the point of orgasm."
            "So now I have no choice but to let nature take it's course."
            "Sensing what's about to happen, they both release me."
            show whore blowjob -lexiblow lexilick reonalick
            "And once my cock is out, bobbing in front of their eyes, they wait patiently."
            show whore blowjob cumshot lexiwink reonawink with vpunch
            "No more than a second later it happens, and I shoot my load right into their faces."
            show whore blowjob dickcum onface -cumshot lexismile reonasmile with vpunch
            "But Lexi and Reona don't flinch even once, smiling as I paint their cheeks with cum."
    return

label missed_whore_harem_date:
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
