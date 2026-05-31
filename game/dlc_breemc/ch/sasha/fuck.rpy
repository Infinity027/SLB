init python:
    Event(**{
    "name": "sasha_hottub_sex_female",
    "label": "sasha_hottub_sex_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(sasha,
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
    "name": "fuck_sasha_female",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            HasStamina(),
            ),
        IsHour(20, 0),
        PersonTarget(sasha,
            IsActive(),
            Not(HasCheated()),
            MinStat("love", 150),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

label sasha_hottub_sex_female:
    $ game.active_date.clothes = "swimsuit"
    scene bg pool
    sasha.say "Hey, [hero.name]..."
    sasha.say "You out here yet?"
    sasha.say "Because I'm ready for a soak in the tub!"
    sasha.say "I...WHOA!"
    "I turn around as soon as I hear the sound of Sasha's voice."
    show sasha swimsuit stuned with fade
    "And it's kind of flattering, the way that she's forced to stop and stare."
    "I know that it's kind of not fair to spring a surprise like this on her."
    "But it does feel pretty good being able to leave her almost speechless!"
    bree.say "Ta da!"
    bree.say "Pretty nice, huh?"
    hide sasha
    show hottub sasha mcalone valentine
    with fade
    "I gesture around myself, showing off the work I've put in to get ready for this."
    "The lighting around the hot-tub is subdued and atmospheric."
    "There are rose petals strewn around the edge and on the water."
    "Candles are burning in carefully chosen spots."
    "And I have a bottle of wine in one hand."
    "Along with two glasses in the other."
    sasha.say "Ah..."
    scene bg pool
    show sasha swimsuit happy
    with fade
    sasha.say "Yeah, [hero.name]!"
    sasha.say "And here I was thinking we were just taking a dip in the tub!"
    show sasha normal
    "I put what I hope is a confident smile on my face as I walk over to Sasha."
    "And I'm hoping that the fact I'm pouring the wine at the same time will help too."
    "Handing one of the glasses over to Sasha, I sit on the edge of the tub."
    bree.say "Well..."
    bree.say "We could do something like that, Sasha."
    bree.say "But I was thinking about it..."
    bree.say "And I wondered if you wanted to so something more?"
    "Sasha doesn't say anything for a moment, she just sips her wine."
    show sasha normal
    "I can feel the nerves starting to take hold of me."
    "Was this a mistake after all?"
    "Did I totally misjudge the situation?"
    show sasha at center, zoomAt(1.5, (640, 1040)) with dissolve
    "But then Sasha takes a few steps forwards, approaching the tub."
    "What I feel in the moment is the strangest combination of relief and fear."
    "Relief that she's coming closer, that she's not simply walking away from me."
    "But also fear that I don't know where this is going."
    "Or maybe it's actually fear that I have a good idea where it's going!"
    hide sasha
    show hottub sasha valentine
    with fade
    "Sasha sits down on the other side of the tub."
    "And she keeps her eyes on me the whole time."
    sasha.say "I always wondered how you felt about me, [hero.name]."
    sasha.say "About how I can swing both ways."
    sasha.say "And I wondered about you too."
    sasha.say "Like, are you into girls as well as guys?"
    "I nod slowly, unconsciously moving towards Sasha as I do so."
    "She makes no effort to pull back of move away."
    "So I keep on going, inching closer until we're sitting side by side."
    bree.say "I think it depends, Sasha."
    bree.say "Like, if it's the right girl..."
    bree.say "Then I'd definitely be tempted."
    "Sasha raises an eyebrow."
    "And she regards me with interest."
    sasha.say "And I'm the right girl, huh?"
    bree.say "Oh no, Sasha..."
    bree.say "I think you're totally the wrong girl!"
    bree.say "And that's why you scare me a little."
    bree.say "As well as turning me on..."
    "Sasha bursts out laughing at this."
    "But I can tell from her tone that it's not mocking laughter."
    "In fact, there's a warmth in it that excites me."
    "And that excitement seems to have a strange effect on my confidence."
    "Because a moment later, I lean forward and plant my lips on Sasha's."
    "She freezes for a moment, the sheer spontaneity seeming to catch her out."
    "But then Sasha recovers herself, and I wonder what she's going to do."
    "Will she pull away from me?"
    "Or will she go with it?"
    "The answer comes a moment later when I hear the sound of her glass being put down."
    show hottub sex female sasha valentine with fade
    "And then, her hands free, Sasha wraps them around me, pulling me close against her."
    "I should really have revelled in those few seconds of being in total control more."
    "Because now I can feel the momentum swinging in Sasha's direction."
    "Not only does she return the kiss with equal passion."
    "But she goes further still, tilting her head and parting her lips."
    "Sasha's tongue darts into my mouth, meeting no resistance."
    "I feel her taking my glass from my hand, freeing me to embrace her."
    "With nothing else to hold us back, Sasha and I roll in the water."
    "I can feel her hands exploring my body as we do so."
    "They slide over me, pausing here and there to stroke and squeeze."
    "This means that I never know where the next sensation is going to come from or when."
    "I do the best I can to match what Sasha's doing to me."
    "But at every turn I feel like she's just a little ahead."
    "It's like she's leading me on, urging me to chase after her."
    "How is it that I was the one who plucked up the courage to kiss her."
    "And yet the moment things start to heat up between us, she's back in charge!"
    "I can feel a frustration building in me, right alongside my desire."
    "I want this more than anything right now."
    "But I want to be Sasha's equal in it too."
    "I can't let her lead me by the nose."
    "I can't let her dominate me, no matter how incredible that would feel."
    "So the next time I find myself on top, I summon up all of my strength."
    "And I press myself down atop Sasha in the water."
    "I'm not trying to hurt her or throw her around."
    "Just to assert myself and take control."
    "At first, Sasha struggles a little, trying to turn me over again."
    "But then she seems to read the intent in my eyes."
    sasha.say "Oh..."
    sasha.say "I see how it is, [hero.name]..."
    sasha.say "You want to be the one on top!"
    "Instead of nodding or offering any kind of an answer, I choose action."
    "I thrust one hand under the water, sliding it up the inside of Sasha's thigh."
    "And then I slip it quickly under her swimsuit."
    sasha.say "Oooh..."
    sasha.say "Oh, [hero.name]..."
    sasha.say "You little slut!"
    "Sasha says all of this as I begin to stroke between her thighs."
    "The tips of my fingers dance over the folds of her pussy."
    "And then I start to push them deeper still, exploring Sasha's lips."
    "Underwater it's hard to tell just how much this is arousing her."
    "So I have to listen carefully to the sounds coming from her other lips."
    "And based on the moaning and gasping that I'm hearing, this is working just fine."
    "Soon enough I can feel Sasha opening up like a flower down there."
    "And as soon as she does, my fingers slip slowly inside of her."
    "My other hand is on Sasha's belly as all of this happens."
    "But now it begins to travel upwards, reaching her chest."
    "There I use it to caress her breasts through the material of her swimsuit."
    "The sight of her nipples stiffening only adds to my pleasure."
    "But then I move my hand higher still, touching Sasha's cheek."
    "She turns her head at my touch, opening her mouth."
    "At first I think she's going to bite in the throes of passion."
    "But instead she takes my fingers into her mouth."
    "And then she sucks on them, licking desperately as if it'll bring her release."
    "That moment of release isn't long coming either."
    with vpunch
    "Sasha begins to quiver and shake, making waves in the water."
    "And now she does bite down on my fingers."
    "Which makes me yelp, more in surprise than actual pain."
    with vpunch
    "At the same time I can feel the muscles of her pussy squeezing my other hand too."
    with vpunch
    "All I can do is hold Sasha up in the water as she cums."
    "That and watch the effects of my attentions on her body."
    "It seems amazing to me that I did all of that to her."
    "Just me, using only my two hands."
    "Well, my tongue too, I guess!"
    "Holding Sasha with one hand, I use the other to retrieve my glass of wine."
    "Because I think I deserve a drink as a reward for all the work I just put in!"
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ sasha.sexperience += 1
    $ game.active_date.clothes = None
    scene bg black with dissolve
    return

label sasha_fuck_bathroom_female:
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ sasha.sexperience += 1
    if Room.has_tag(mike.room, 'home') and not mike.hidden and mike.sexperience >= 3:
        "Should [mike.name] join in?"
        menu:
            "Yes":
                call home_harem_bree_sasha_shower_female from _call_shower_ffm_female_1
                return
            "No":
                $ mike.love -= 2
                hide mike
    show sasha naked
    bree.say "Were you that dirty that you just couldn't wait your turn for the shower?"
    "I chuckle weakly at my lame attempt to relieve the tension between us with humour."
    "But Sasha almost totally ignores my words."
    "I can positively feel the progress of her eyes as they pass over my wet, naked body."
    show sasha blush
    sasha.say "Oh, I'm dirty alright...I'm feeling positively filthy right now, [hero.name]!"
    sasha.say "Only it's the kind of filthy that no shower's going to help me with..."
    show sasha shy
    "I can already feel my cheeks flushing, and not just from the awkwardness of my housemate joining me in the shower."
    "The look on Sasha's face tells me that she's not going to simply have a wash and then leave."
    "Oh no, she wants much more from me than that."
    "And it's this visible desire for me that's already making me feel hot in turn."
    "I'd be lying if I said that I didn't like to have people look at my body like this, guys and girls alike."
    "Having Sasha do the same is so flattering that I can't help but be turned on by her attention."
    "A part of me wants to rise to the challenge, to meet her on a level and show that I'm not afraid to embrace this element of my sexuality."
    "But another is enjoying the feeling of being eyed-up, quaking a little at the prospect of someone so hungry for me pressing their affections further."
    "What can I say - even a thoroughly modern, sexually-liberated woman likes to play the part of an innocent, blushing little maid once in a while..."
    show shower breesasha with fade
    "And so I resolve to keep my back pressed against the wall, enjoying the sensation of having Sasha come to me."
    "And come on she does, perhaps sensing that I will do nothing to stop her advances, even being turned on by that realisation than ever."
    "As she closes the space between us, Sasha reaches out with one hand, caressing the inside of my thighs in the most suggestive manner possible."
    "Her other hand clasps the side of my neck, stroking my jaw with her thumb."
    "She holds my eye the entire time that her fingers a coming ever closer to the top of my thighs."
    "But even before I feel them brush the outermost folds of my pussy, I can sense it becoming hopelessly slick in anticipation and excitement."
    "It positively tingles with a static charge by the time the tips of Sasha's fingers finally slide along the length of its lips."
    "I meet this contact with a sharp intake of breath at how intense the feeling is, drawing a quizzical and amused look from Sasha in return."
    "She cocks her head to one side, as if to ask if I like what she's doing to me, and all I can do is close my eyes and nod frantically."
    "Encouraged by this, she goes further, stroking more deeply into my folds and pressing harder as she does so."
    "Now I can't help beginning to sigh and pant at the sensations spreading outwards from my groin and into every extremity of my body."
    "But as I do so, Sasha pulls my mouth towards her own and almost tries to swallow my gasps of pleasure whole."
    "At first she kisses me with a fiery aggression that forces me into utter submission, just as she's massaging me into a state of helpless arousal."
    "This changes though, as I feel the urge to push my tongue into Sasha's mouth, almost as a mirror of the way her fingers are now starting to slip inside of me."
    "We succeed in feeding the fire inside of each other now, her attentions making mine all the more intense and vice versa."
    "My hands wrap around the small of Sasha's back, pulling her so close to me that her hand is almost pressed as hard against her pussy as it is against my own."
    "I can feel out chests being forced together, my larger breasts slipping over her more petite pair."
    "Where our nipples brush past each other for the smallest of instances, I feel a new jolt of arousal that only adds to my pleasure."
    "But now that Sasha's hand is rubbing against her own pussy with almost as much effect as my own, I can feel her beginning to gasp as well."
    "Suddenly, she breaks the kiss and pulls away from me just enough to relieve herself before it's too late to keep from cumming."
    "I can't hide the surprise and disappointment on my face, but Sasha shakes her head and wags a playful finger in my face at this."



    "She's the one that needs to be in charge, and if anyone's going to cum, it has to be who she chooses and when."
    "Not that I mind that in the least, as I'm now resigned to being the passive partner in this encounter."
    "And damn, but she's good at this!"




    "Right now I know full well that Sasha's pleasing me the exact same way that she'd like to be pleasured herself."
    "And it's so good that it's simply exquisite."

    "Then I shudder, groan and feel the cascade of my orgasm coming over me with the inevitability of an incoming tide."
    "Still shaking, I slide down the last few feet of the wall until I end up curled in the bottom of the shower."
    "Sasha lies at my side, panting and exhausted from her own exertions at the same time."
    "Neither of us speaks as much as a word, because there doesn't seem to be any need for them."
    "We simply sit there in silence, while the water washes us clean once more and the evidence is carried away down the swirling drain."
    return

label sasha_fuck_date_female(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ game.room = "bedroom4"
    scene bg bedroom4
    if not sasha.sexperience:
        show sasha
        "If I was nervous about going out on a date with Sasha, I'm even more so about taking it to the next level."
        "I know that I shouldn't be - this is the twenty-first century, for god's sake!"
        "And I'm not some religious nut or moral conservative either...but the alcohol certainly helps to ease my nerves as I let Sasha lead me into my bedroom."


        "She begins to strip off her clothes, starting from the top and working her way down."
        show sasha underwear
        "But she stops when she's down to her bra and panties, noting my own hesitation."
        show sasha shout
        sasha.say "What's up - you feeling like you're about to be eaten up by the Big Bad Wolf-Bitch?"
        show sasha normal
        bree.say "I'm sorry...I guess I'm just a little scared, that's all."
        show sasha shout
        sasha.say "Hey, there's no need to be."
        sasha.say "It's just like sex with a guy, only there's no dicks involved!"
        show sasha normal
        "I chuckle at the implied joke, beginning to feel more relaxed as Sasha's humour defuses the awkward moment."
        show sasha shout
        sasha.say "Would it help if I took the lead here?"
        show sasha normal
        "I nod silently, suddenly aware of how close she's standing to me and the fact that she's almost naked."
        show sasha shout
        sasha.say "Okay, just relax and trust me - you're going to love this."
        show sasha normal
        "With that, Sasha reaches out and begins to undress me."
        "I'm only wearing a pair of shorts and a sweater, but somehow she makes peeling them off of me feel like an intense and prolonged ritual of seduction."
        "Stepping out of my shorts as she pulls them down, Sasha wastes no time in unhooking my bra and then tugging at my own panties."
        "Completely naked now, I realise that she's enjoying being in a position of power over me."
        "The notion causes my cheeks to flush with colour, something that only serves to make Sasha's grin become wicked with intent."
        sasha.say "Up on the bed with you, come on."
        "Still blushing, I obey without saying a word."
    else:
        call sasha_fuck_date_female_oral_intro from _call_sasha_fuck_date_female_oral_intro
        call sasha_fuck_date_female_oral from _call_sasha_fuck_date_female_oral

    menu:
        "Doggy":
            call sasha_fuck_date_female_doggy () from _call_sasha_fuck_date_female_doggy

    $ sasha.sexperience += 1
    call sasha_sleep_date_fuck_female (location) from _call_sasha_sleep_date_fuck_female
    return

label sasha_sleep_date_fuck_female(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene expression f"bg {game.room}"
        show sasha strapon
        sasha.say "Sweet dreams, [hero.name]..."
        bree.say "You too, Sasha..."
        $ sasha.love += 3
        $ game.room = "bedroom4"
        call sleep ("sasha") from _call_sleep_90
    return

label sasha_fuck_date_female_oral_intro:
    if randint(0, 1) == 0:
        "I tried the best I could not to be nervous while I was out on a date with Sasha tonight."
        "And I don't know if I managed to hide my nerves from for even as much as a moment."
        "But I did seem to end up drinking more than a little as a result."
        "The result of that was me giggling and blushing at almost everything Sasha said."
        "I know it makes me look silly, like some kind of drunken bimbo."
        "But Sasha can be so funny, and she's so savage with it!"
        "I could never be that confident!"
        "I think things went well though."
        "Because Sasha's still talking to me as we walk into the house."
        "She's even smiling as I hear the door swing closed behind me."
        "But it's only now that I realise it's the door to my bedroom!"
        "Oh my - I don't think Sasha's ready to call it a night just yet!"
        show sasha shout
        sasha.say "Hey, [hero.name]..."
        sasha.say "Are you feeling okay?"
        sasha.say "You look a little peaky."
        sasha.say "And you were hitting the booze pretty hard back there!"
        show sasha normal
        "I shake my head, struggling to look more together than I feel."
        "I may be nervous, but the last thing I want is to actually admit as much."
        bree.say "What...me?!?"
        bree.say "What are you talking about, Sasha?"
        bree.say "I'm fine - why wouldn't I be fine?"
        "Realising that I'm beginning to babble, I clamp my mouth shut."
        "Amazingly, this seems to be more than enough to convince Sasha."
        show sasha happy
        sasha.say "Whatever you say, [hero.name]."
        sasha.say "And I'm glad you're okay."
        sasha.say "Because the night's not over yet!"
        show sasha normal
        bree.say "It's not?"
        show sasha shout
        sasha.say "No way!"
        show sasha normal
        "Without stopping to explain herself, Sasha jumps onto my bed."
        "I watch in amazement as she crawls over the mattress."
        "And then begins to tug at her clothes, eagerly pulling them off."
        "All I can do is stand there and watch in a stunned silence."
        "Sasha's stripping off on my bed!"
        show sasha naked
        "One of the hottest girls I know is getting naked right in front of me!"
        sasha.say "Erm, [hero.name]..."
        show sasha flirt
        sasha.say "Are you gonna come over here or what?!?"
        show sasha normal
        "I almost jump at the realisation of what Sasha means."
        "Not only is she getting naked, but she wants me to join her too!"
        bree.say "Oh..."
        bree.say "Oh yeah...of course I am, Sasha!"
        bree.say "I'm coming, okay?"
        show sasha happy
        "Sasha laughs and shakes her head as I rush to follow her lead."
        "I have most of my own clothes off before I reach the bed."
        "And I'm so eager to do this that I almost trip and fall in the act!"
        "But when I finally make it and pull off the last of my clothes, I stop and stare."
    else:
        "Sasha and I have been chatting all the way back home from our date."
        "You know how it is, right?"
        "You're having a great time, talking about everything and nothing all at once."
        "You and your date have just clicked on such a basic level that the night flows naturally."
        "Then the next thing you know, you're back at your place."
        "Not only that, you're taking it to the next level too!"
        "Don't get me wrong - I'm totally up for that."
        "It's just I'm not used to being the one to bring a hot girl back to my room!"
        bree.say "So, Sasha..."
        bree.say "Here we are..."
        show sasha shout
        sasha.say "Erm, yeah, [hero.name]."
        show sasha normal
        bree.say "Just you and me..."
        show sasha shout
        sasha.say "Certainly looks that way."
        show sasha normal
        bree.say "All alone in my bedroom..."
        show sasha shout
        sasha.say "Unless you've got somebody stashed away in the closet!"
        show sasha normal
        "I let out an anxious burst of laughter at Sasha's joke."
        "And as I do so, I just know that my nerves are totally obvious."
        "There's no way Sasha doesn't know I'm crapping myself right now!"
        bree.say "So what are we going to do now?"
        sasha.say "Hmm..."
        show sasha shout
        sasha.say "Well..."
        sasha.say "I was kinda thinking of something like this..."
        hide sasha
        show sasha kiss
        with fade
        $ sasha.flags.kiss += 1
        "Without any warning, Sasha leans in and kisses me."
        "It's full on the mouth and delivered with genuine passion."
        "My eyes pop open in surprise, as wide as saucers."
        "But then I feel myself giving in to the sensations of the kiss."
        "And I feel my eyes begin to close as I surrender to it completely."
        "Before I know what's happening, Sasha and I are wrapped in each others arms."
        "The kiss becomes deeper and more intense with every second that it lasts."
        "Sasha has her tongue in my mouth, and I have mine in hers."
        "I can feel myself beginning to come alive down there too."
        "Sasha's getting me so excited."
        "Making me feel so damn horny!"
        "In fact, she's got me in such a tangle I can't think of anything else."
        "Which is why I don't notice that she's already started to undress me!"
        "I feel the sensation of Sasha touching my naked chest before I see it."
        "And only then do my eyes pop open again."
        "In fact, I'm so surprised that I accidentally break off the kiss."
        hide sasha kiss
        show sasha
        with fade
        bree.say "Wha..."
        bree.say "Oh god..."
        show sasha shout
        sasha.say "What's the matter, [hero.name]?"
        sasha.say "Am I going too fast for you?"
        show sasha normal
        "I can feel myself blushing at the mere thought this is too much for me."
        "At the thought that Sasha might think I'm some kind of prude that can't handle it."
        "And one thing I know is that's not how I want to come across to her."
        bree.say "N...no, Sasha..."
        bree.say "No way..."
        bree.say "It's just so...so exciting when you touch me!"
        bree.say "Please don't stop!"
        show sasha happy
        "Sasha smiles at my pleas, and I smile in return."
        "But there's something almost wolfish in her expression."
        "Something that frightens me, but turns me on far more!"
        show sasha shout
        sasha.say "Don't worry, [hero.name]."
        sasha.say "I won't stop touching you."
        sasha.say "Not until you can't stand to be touched anymore!"
        show sasha normal
        "The promises that Sasha makes to me, every word she speaks."
        "It's like I can feel them between my thighs!"
        "She's talking me into getting wet for her!"
        "I stand still as a statue, letting Sasha remove the last of my clothes."
        show sasha naked with dissolve
        "That done, she hastily pulls off her own so that we're both naked."
        "And then she takes me by the hand, leading me over to the bed."
        "I follow meekly, trying not to seem like Sasha's the one in control."
        "But inside, I can't deny the fact that I'm enjoying all of this."
        "It feels strangely liberating to let her take charge."
        "Like whatever happens next is out of my control."
        "Sasha's free to do with me as she pleases!"
    return

label sasha_fuck_date_female_oral:
    menu:
        "Lick Sasha's pussy":
            "There's Sasha, lying on her back in the middle of my bed."
            "And she's naked - completely naked!"
            "Of course she notices my reaction to the sight."
            "And the smile on her face only serves to make her that much more beautiful."
            sasha.say "I take it you like what you see, huh?"
            "I can't summon the words to answer the question."
            "So I just nod dumbly, almost staggering forwards."
            "Sasha laughs again and opens her arms out to me."
            "I half climb and half fall onto the bed."
            "But luckily for me I kind of land on top of her."
            "Sasha wriggles under me, wrapping her arms and legs around my body."
            "Her skin feels electric against mine, like she's making me tingle."
            "But the sensation becomes more intense a moment later."
            hide sasha
            show sasha kiss naked
            with fade
            $ sasha.flags.kiss += 1
            "Because that's when she finds my lips and kisses me."
            "I can feel my entire body come alive as Sasha does so."
            "Every inch of me feels it, but it touches me most between my thighs."
            "As Sasha slides her tongue into my mouth, I start to feel it down there."
            "My cheeks must be as red as ripe tomatoes by now."
            "Because I desperately wish she was using her tongue somewhere else!"
            "Without warning, Sasha breaks of the kiss a moment later."
            hide sasha kiss
            show sasha naked flirt
            with fade
            "I can't help looking up, confusion and disappointment in my eyes."
            "But she doesn't spare as much as a second to comfort me."
            "Instead, Sasha pushes me firmly downwards."
            "This sends me slithering backwards down her body."
            hide sasha
            show sasha cunnilingus
            with fade
            "It's now, as I look back up at her, that I see her earrings."
            "I must have noticed the fact that they're pentagrams before now."
            "But in the heat of the moment, it strikes me like never before."
            "Is Sasha actually some kind of magician - even a witch?"
            "Maybe that's why I simply can't resist her will!"
            "Maybe she slipped something into my drink - or cast a spell on me!"
            sasha.say "That's it..."
            sasha.say "That's right, [hero.name]..."
            sasha.say "You get to work down there, like a good girl!"
            "I feel Sasha reach out and put her hand atop my head."
            "And then she pushes me down, over her breasts and belly."
            "Then I'm sinking between her thighs, only just able to see her face."
            show sasha cunnilingus middle
            "I catch the scent of Sasha's pussy before I feel it."
            "The smell is musky and sweet, almost too complex to describe."
            "And to me it's like the most potent pheromone I can imagine."
            show sasha cunnilingus up
            "I can only see the very top of Sasha's head by now."
            "She's nodding, urging me onwards - well, downwards, I guess!"
            "But it's not like I need to be told what's expected of me."
            show sasha cunnilingus middle
            "I part my lips and push out my tongue, almost holding my breath as I do so..."
            "And then I feel the tip touch the folds of Sasha's pussy!"
            "If the sensation of my skin touching hers was electric, this is so much more!"
            show sasha cunnilingus down
            "I imagine this is the sensation that you feel the moment before a lightning strike!"
            "The taste of Sasha is bitter and moreish all at once, instantly addictive."
            "I don't need her hand to push me deeper in or to keep me there."
            "In fact, Sasha couldn't pull me back now if she tried!"
            show sasha cunnilingus middle
            "It's not that my tongue suddenly has a life of it's own."
            "More like it's the part of me that takes the lead."
            "The rest of me follows, simply helping to push it onwards."
            "I barely hear the sounds that Sasha's making as I work on her."
            show sasha cunnilingus up
            "The movements of her body around me don't even seem to exist to me."
            "All I can feel are my tongue, my lips and her pussy."
            "Well, that's not really the truth..."
            show sasha cunnilingus middle
            "Because I can still feel my own pussy too."
            "Every time I lick and probe Sasha's, I feel myself twitch and twinge in sympathy."
            "Oh fuck...I wish someone was doing the same thing to me right now!"
            "That's the only way this could be any better than it already is!"
            show sasha cunnilingus down
            "I have no idea how long I've been down here."
            "No idea how long I've been going down on Sasha."
            "I feel like I'm in some kind of trance."
            "All I can think about is keeping on licking and lapping."
            show sasha cunnilingus middle pleasure
            sasha.say "[hero.name]..."
            sasha.say "[hero.name]...st...stop..."
            sasha.say "I...I'm cumming..."
            "I hear Sasha's words, but they don't seem to mean anything to me."
            "It's like she's talking to somebody else in the room with us."
            show sasha cunnilingus up
            "Part of me won't let any distraction get in the way of what I'm doing."
            "I barely feel it when Sasha wraps her legs around me, like she's holding on for dear life!"
            show sasha cunnilingus middle ahegao
            sasha.say "[hero.name]..."
            sasha.say "Oh fuck...[hero.name]..."
            sasha.say "Please...you already did it..."
            sasha.say "You made me cum...you made me cum..."
            sasha.say "You can stop now!"
            show sasha cunnilingus down
            "I look up, my thoughts confused and my vision swimming."
            "Everything slowly begins to come back into focus."
            "And when it does, I can't help staring at Sasha in amazement."
            show sasha cunnilingus notongue
            "She's not reclining on the bed like before, looking like she's in control."
            "Instead the bedclothes are tangled around her as if there's been a struggle."
            "Her hair is dishevelled and her cheeks are flushed, the eyes above them wide."
            bree.say "S...Sasha?"
            bree.say "Are you okay?"
            bree.say "I...I hope I did okay!"
            "Sasha lets out a gasp that turns into a helpless burst of laughter."
            sasha.say "Erm...yeah, [hero.name]..."
            sasha.say "I'd say you did better than okay!"
            sasha.say "Nobody's made me cum like that in quite a while!"
            "I can feel myself blushing at Sasha's frank admission."
            "But I can also feel a genuine sense of pride growing inside of me too."
            "Maybe I'm not as hopeless at this kind of thing as I thought I'd be."
            $ sasha.love += 4
        "Make Sasha eat my pussy" if sasha.sub >= 25:
            "And the first thing she does with that power is lie me down on the bed."
            "Of course I do nothing to resist, letting her get me into the position she desires."
            "Curiosity and desire are more than enough to render me totally submissive."
            "Once Sasha has me laid down on my back, she crawls onto the bed below me."
            "I prop myself up on my elbows, watching as she parts my legs."
            scene bg black
            show bree cunnilingus sasha
            with fade
            "Sasha crawls between them, pushing my thighs down as she gets closer."
            "I almost yelp with anticipation as she licks her lips."
            "Sasha holds my eye as she reaches the top of my legs."
            "And I can't tear my gaze away as her head begins to sink downwards."
            "As soon as her eyes sink below the range of my vision, I hold my breath."
            "It's like I daren't breath until I know that she's really going to do it."
            show bree cunnilingus sasha down
            "Like some perverse part of my mind thinks this could all be a weird joke."
            bree.say "Gha..."
            bree.say "Mmm..."
            bree.say "Oh...on shit!"
            "It's not a joke."
            "Holy fuck, it's not a joke!"
            show bree cunnilingus sasha middle
            "I can feel Sasha exploring the edges of my pussy with her tongue."
            "The same tongue that was in my mouth a couple of minutes ago!"
            "Back then it was what she was doing to my mouth making me wet down there."
            "But now the roles are reversed, and my lips part to gasp at the sensation."
            show bree cunnilingus sasha up
            "I've gone down on my fair share of willing partners."
            "And I know what I like when I'm on the receiving end too."
            "But Sasha doesn't seem to want or need any advice from me right now."
            show bree cunnilingus sasha middle
            "It's like she's on a mission and nothing's going to stop her."
            "I know I'm certainly not capable of doing that, even if I wanted to."
            "I can feel her working her way around and inwards."
            show bree cunnilingus sasha down
            "I imagine Sasha spiralling slowly towards the inside of me."
            "Every tiny step she takes seems to ramp up the intensity of the experience for me."
            "And when that tongue of hers finally dips into my pussy..."
            show bree cunnilingus sasha middle pleasure
            bree.say "Sasha..."
            bree.say "Don't stop..."
            bree.say "Don't stop now..."
            "There's no way that I should be able to hear a thing Sasha says."
            show bree cunnilingus sasha up
            "And I'm sure that she's so tied up in the moment she can't hear me either."
            "But somehow I'm convinced that my outburst reaches her down there."
            show bree cunnilingus sasha middle
            "I hear what sounds like laughter, a wicked giggle of delight."
            "That sound is soon lost beneath my own desperate panting."
            show bree cunnilingus sasha down
            "I want to grab hold of Sasha's head and push her deeper."
            "I want to squeeze at my breasts and nipples to give myself some relief."
            "But it's all I can do to hold myself up and keep from collapsing onto my back!"
            show bree cunnilingus sasha middle
            bree.say "S...Sasha!"
            bree.say "I'm gonna..."
            bree.say "I'm gonna cum!"
            show bree cunnilingus sasha up ahegao
            "Only now do I actually feel my head falling backwards."
            "It hits the bedclothes as Sasha tips me over the edge."
            "My orgasm is every bit as intense as all that came before it."
            show bree cunnilingus sasha middle
            "And it leaves me in a state of utterly helpless confusion."
            "All I can do is lie there, a heap of limp, sweaty limbs."
            "Sasha props herself up on one elbow, licking her lips like a satisfied cat."
            show bree cunnilingus sasha notongue
            sasha.say "Told you I wouldn't stop."
            sasha.say "Not until you'd had enough."
            sasha.say "And right now, you look more than satisfied!"
            bree.say "I..."
            bree.say "Ye..."
            bree.say "Whoo..."
            "Sasha laughs again and leans in closer, kissing me on the forehead."
            sasha.say "Losing the power of speech is perfectly normal!"
            sasha.say "You should be back to normal in a little while."
            sasha.say "But I gotta warn you - this kind of thing's addictive!"
            $ sasha.love += 2
            $ sasha.sub += 1
    return

label sasha_fuck_date_female_doggy():
    sasha.say "I want you on all fours...that's right, good girl!"
    show bree doggy noone
    with fade
    "I keep looking forwards, unable to see what Sasha is doing."
    "I think that I can hear her rummaging under the bed."
    "But there's also the sound of something else, almost like she's pulling on a belt or harness of some kind."
    sasha.say "Like I already said - one of the best things about doing it with another girl is that you get to decide whether or not there's a dick involved."
    sasha.say "But you can also choose who gets to use it as well!"
    "I can feel something brushing the cheeks of my ass, threatening to nudge itself between them."
    show bree doggy sasha
    "A glance over my shoulder makes me gasp in surprise at what I see there."
    "Kneeling on the bed behind me, Sasha is wearing one of the most impressive dildos that I've ever seen."
    "It glistens with lube in the subdued lighting of her bedroom, swaying slightly as she leans forwards to put it to use."
    "To put it to use on me!"
    "I can feel a strange mixture of arousal and fear making my pussy almost quiver in anticipation."
    "Half of me wants to cower away from the approaching dildo and the other half perversely can't wait to discover what it'll feel like."
    "But Sasha's not going to let the former happen, I know that much."
    "I feel her hands take a gentle but firm hold of my ass, pulling me towards her even as she thrusts forwards."
    "My pussy is a little tight at first, reflecting my trepidation."
    "But Sasha presses on regardless, using the dildo with the skill of a pro to stroke and tease my lips until I can't help sighing in genuine pleasure."
    "Now all I can feel is my resistance melting away, more with each second that passes and each new stroke at my pussy."
    "Instinctively I lower myself just a little, spreading my legs at the same time."
    "Now the tip of the dildo is literally pressing against the lips of my pussy, threatening to push in at any moment."
    "Sasha took the liberty of lubing it up beforehand, and now with my own body responding and things down there stretched apart, it's not a challenge to go further."
    "I'm no stranger to a man's dick inside of me, or using a dildo for my own pleasure."
    "But this somehow like both and yet neither."
    "Sasha is obviously getting a kick out of this, but she's not obsessed with getting herself off like a guy would be right now."
    "Likewise it's a totally different feeling to have someone else use a dildo on me rather than doing it myself."
    "As the head goes as far in as possible and the shaft rubs back and forth inside of me, I can't help but gasp in amazement at the sensations it creates."
    "But a large part of my pleasure is coming from the fact that I'm being brought off by Sasha's efforts alone."
    "My cheeks begin to burn anew as I realise how much I'm getting off on being treated like some glorified toy for her gratification."
    "All too soon I can feel the sensations becoming too much for me, and I begin to spill over into an orgasm."
    show bree doggy sasha ahegao
    "Cumming whilst on the end of Sasha's strap-on makes me redden all the more, but it also makes the whole experience that much more exciting too."
    return

label shower_ffm_female:
label home_harem_bree_sasha_shower_female:
    $ renpy.sound.play("sd/shower.ogg", loop=True)
    $ sasha.sexperience += 1
    $ mike.sexperience += 1
    scene bg bathroom
    show sasha naked at left
    show mike naked at right
    "Neither of us as much as touch him to begin with, instead making a show of stripping each other off as he watched."
    "He was still too surprised to have done anything all the same, and so he just stood there, eyes following every piece of clothing that we removed."
    "But even if he was not making any conscious moves, I couldn't help smiling at the sight of his cock beginning to stir the whole time."
    "Once we're all naked, Sasha skips ahead of me, stepping into the shower and beckoning for us both to follow."
    "I can't help smiling as I reach out and take hold of [mike.name] by his now well and truly erect cock, using it to lead him into the cubicle."
    "Even when we get into the shower, he still seems to be hesitant, not making any move to assert himself."
    hide mike
    hide sasha
    show shower breesasha
    with fade
    "Reasoning that he needs some more motivation in order to shake off his inaction, I lean against one of the tiled walls and pull Sasha into a close embrace."
    "As my hands begin to explore her smooth skin, made slippery by the water raining down from above, I can already feel Sasha returning the favour with equal enthusiasm."
    "I feel her weight lean into me perhaps a second before her questing lips find my own, her tongue immediately seeking a way between them and finding it with ease."
    "Sasha's breasts brush roughly against me as she presses herself atop me, slipping over my chest and making it hard to tell where one pair ends and the other begins."
    "Already I want to reach down between my legs, fingers anticipating the feeling of my pussy."
    "But still [mike.name] seems to be holding back, not ready to commit himself to what we're doing together."
    "I'm certain that he's not reticent because of shyness, and so that can only mean that we've been giving him too good of a show to tear himself away from."
    "Reluctantly I break the kiss with Sasha, leading her to fall to kissing and almost biting at my neck as I do so."
    "Making sure that I have [mike.name]'s attention, I begin to run my hands up and down the small of Sasha's back, massaging and kneading at her buttocks."
    "Sasha herself can't help moaning at the pleasure that this gives her, bending down and stretching her backside towards him as she does so."
    "Though I can't see her from [mike.name]'s point of view, I know enough about my own anatomy to be sure that he must have a rather inviting view from that angle."
    "I see him lick his lips, and then he's snared, stepping forwards to close the small distance between them."
    "He doesn't take time for teasing or foreplay of any kind, instead just taking hold of Sasha's left buttock in one hand and using the other to guide himself home."
    hide shower breesasha
    show shower threesome breesasha
    "I have no idea whether he's chosen to push his way into Sasha's pussy or take her up the ass, but the effect is still quite something from where I'm standing."
    "Sasha doesn't protest or object in the slightest, only letting out a muffled moan as begins to kiss me again in earnest."
    "[mike.name] pushes in as far as he can possibly go, holding himself there for a lingering moment."
    "In response she probes just as deeply into my mouth with her tongue, almost too deep for me to handle."
    "But thankfully, as [mike.name] begins to lessen the degree to which he's pressed into her, starting to move back and forth, Sasha too settles into a more tolerable rhythm."
    "Though she's the one that's actually getting fucked, I feel strangely as though Sasha's becoming nothing but a bridge between [mike.name] and myself."
    "I open my eyes as Sasha kisses me, and see that he's looking straight at me, rather than down at her as she takes his cock from behind."
    "It's almost like I can feel every thrust of his dick inside of her, as it translates into the way in which she kisses me."
    "As it writhes and twists in my mouth, Sasha's tongue feels like nothing more than an extension of [mike.name]'s cock."
    "Before I know it, my fingers are sliding between my legs and stroking the outer lips of my pussy."
    "Wet as I may be from the water of the shower, I know the difference between it and the slick sensation of my own body."
    "Stroking in the right places in just the right way means that I can't help but come alive to the pleasure of what we're doing all over again."
    "Sure, [mike.name] might be inside of Sasha right now, but what she's doing to me is thanks to what he's doing to her."
    "And what I'm doing to myself is likewise the end of a sensual chain that started when his cock entered her body."
    "I can already sense that I'm zoning out thanks to the sensations that I'm feeling and the heat in the shower cubicle."
    "How close Sasha and [mike.name] are to cumming I have no idea, but I can feel mine coming over me right then and there."
    "Breaking Sasha's kiss for the second time, I lean my head against the wall and can't keep from letting out a strained cry as I cum."
    "Perhaps it's the sight of this that spurs him on, but for a second, it looks like [mike.name] is about to cum too, and while he's deep inside of Sasha."
    show shower bj breesasha bree sasha
    "Don't ask me how, but [mike.name] actually manages to hold it in, pulling out before it's too late and urgently forcing the both of us to kneel in the bottom of the shower before him."
    "I can't help wondering if his desperation to pull out was because he was doing Sasha in the pussy, but there's no time to contemplate such things right now."
    show shower bj breesasha bree sasha shoot
    "Instead we sit on our haunches, looking up at him in obvious anticipation as he strokes his cock in the last moments before his climax finally takes him."
    "Sasha and I jostle and push playfully for the best position, and I find that I have to keep myself from actually pushing her aside for real."
    "There's still a part of me that's unreasonably jealous that she was the one to get [mike.name]'s cock inside of her, and wants to claim the largest portion of his cum as compensation."
    show shower bj breesasha bree sasha shoot facial
    "The point becomes moot only a second later, when he finally cums and gives us a shower inside of a shower."
    "I can't hope to tell just which one of us actually gets the most of it, but I feel the warm cum streak my forehead and cheeks, as well as landing inside of my wide-open mouth."
    "Swallowing what I managed to catch and then licking greedily with my lips for whatever else I can find on my face, I'm too satisfied to be jealous of Sasha any longer."
    "All I have the will and energy to do is sit there, as the continued pattering of the water washes the three of us clean."
    stop sound
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
