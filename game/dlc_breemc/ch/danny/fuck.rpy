init python:
    Event(**{
    "name": "danny_hottub_sex_female",
    "label": "danny_hottub_sex_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(danny,
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

label danny_hottub_sex_female:
    scene bg livingroom with dissolve
    "For all that I'm trying to be cool and confident, I'm actually pretty nervous right now."
    "And that's because I've finally decided to invite Danny over for a dip in the hot-tub."
    "Any other guy and I would have done it almost without hesitation, without even thinking."
    "But Danny's not like other guys, you know?"
    "He's kind of from the wrong side of the tracks."
    "He's a rebel and a renegade, he does his own thing."
    "And yeah, I know - he's kind of a bad dude too."
    "But I'm sure that's more like a kind of persona he puts on to survive in his natural habitat."
    "Underneath there's probably a pretty nice guy waiting for the chance to come out and shine."
    "Or maybe I'm just fooling myself, and I kinda like the thrill of dating a real bad boy for a change."
    "Either way it doesn't matter."
    "Danny's here how and I'm committed to making this thing work."
    "I've made sure that I'm wearing a cute swimsuit when Danny arrives."
    scene bg pool with fade
    show danny at left with easeinleft
    "And as I lead him out into the back yard, he seems to appreciate the effort on my part."
    show danny at center with ease
    danny.say "Ouch!"
    danny.say "You are looking fine tonight, girl!"
    danny.say "You should wear less clothes more often!"
    "Okay, okay...I know that I should be offended by him speaking to me like that."
    "But somehow I can't bring myself to tell Danny off."
    "In fact I find myself giggling and blushing at his words."
    "He's just such an obviously macho jerk, it's kind of a turn-on!"
    "And no, I have no idea how he's able to have that effect on me."
    "I guess it's just some kind of animal magnetism he has."
    bree.say "Oh, thank you, Danny!"
    bree.say "This is my favourite swimsuit, you know?"
    danny.say "Well, as of right now, [hero.name]..."
    danny.say "It's my favourite too!"
    "As he says this, Danny walks up behind me."
    "And I feel him touching my ass."
    "He doesn't slap it or squeeze the buttock."
    "Just passes his hand over it in a suggestive manner."
    "As he does so, I feel a tingle of excitement pass through me."
    "Like I know it's wrong for a guy to just feel he can touch me."
    "But I so desperately want to know what he's going to do next!"
    "Trying as best I can to shake off the effect, I gesture to the hot-tub."
    bree.say "What do you think, Danny?"
    bree.say "I tried to make it look nice for you!"
    if game.calendar.get_time_of_day() == "evening":
        $ renpy.show(f"hottub_bg_night_left")
    else:
        $ renpy.show(f"hottub_bg_{game.calendar.season_name}_left")
    $ renpy.show("hottub_fg_valentine_left", tag="romantic")
    with fade
    "I've turned down all the lighting except for the underwater lights in the tub."
    "And I've also gone to the trouble of scattering rose petals on the steaming water."
    "There's a bottle of wine and two glasses perched on the rim of the tub too."
    "Danny takes it all in, nodding in what I assume is approval."
    scene bg pool
    show danny
    with fade
    danny.say "Yeah, [hero.name]..."
    danny.say "This is all pretty fancy."
    danny.say "Far more fancy than I'm used to!"
    "I turn to pour us a glass of wine."
    "But when I do so, I can't help noticing that Danny starts to strip-off."
    $ game.active_date.clothes = "swimsuit"
    show danny swimsuit with dissolve
    "I do the best I can to watch as I pour the wine."
    "And pretty soon I'm more interested in him than the task at hand."
    "Under his vest and T-shirt, Danny's body is thin, but wiry with muscle."
    "And the multiple tattoos and scars only serve to add to my fascination."
    "I can't help wondering what the stories behind them all are."
    "In the end I almost spill the wine as I'm giving him all my attention."
    bree.say "H...here you go, Danny!"
    danny.say "Ah, thanks, [hero.name]."
    danny.say "This is pretty fancy too."
    danny.say "Imagine me drinking wine!"
    danny.say "Normally I only drink beer or bourbon!"
    "I do the best I can to tear my gaze away from the bulge in Danny's trunks."
    "And I have to force myself to look him straight in the eye instead."
    bree.say "It can be a lot of fun, Danny."
    bree.say "You know, trying new things?"
    show danny at center, zoomAt(1.5, (640, 1040))
    "Danny nods and then smiles as I reach out and take hold of his hand."
    "As if he's intrigued by what I have in mind, he lets me lead him over to the tub."
    "I step into the water, slowly lowering myself down until I'm sitting."
    "And Danny follows my lead, sitting down more slowly than I did before him."
    show hottub danny valentine with fade
    danny.say "WHOA!"
    danny.say "What did I just sit on?"
    danny.say "Some kind of fountain?!?"
    "I can't help giggling at Danny's apparent alarm."
    bree.say "No, Danny..."
    bree.say "You just sat on one of the water jets, that's all!"
    bree.say "They're the things that make all the bubbles, see?"
    "Danny finds a safer spot to sit in, and looks around."
    "Slowly his expression softens and he seems to calm down."
    danny.say "Oh yeah, I see that now..."
    danny.say "Hey, this is kinda nice!"
    "Now that he's gotten over the initial shock, Danny seems to relax."
    "And I can tell that from the ways he starts giving me a certain look."
    danny.say "But what'd be even nicer..."
    danny.say "Is if you scooted over here, [hero.name]."
    danny.say "Maybe come sit on my water jet a while?"
    "Maybe it's the wine going to my head."
    "But I find myself giggling again, and nodding too."
    "I do as Danny says, sliding over to him with my glass in hand."
    "He gives me a pirate's grin, putting down his own glass."
    "And I only realise as I make it to him why."
    "It's so he can wrap his arms around my waist and pull me onto his lap!"
    show hottub sex female danny with fade
    bree.say "Whoo..."
    bree.say "Danny!"
    bree.say "You almost made me spill my wine!"
    danny.say "Heh, heh, heh..."
    danny.say "You ain't going to hold onto it long, [hero.name]."
    danny.say "Not with what I got planned for you..."
    "As Danny says all of this, I feel his hand on my thigh."
    "And when I look down, I see him sliding it upwards."
    "I watch as Danny pushes his fingers under the crotch."
    "Then I gasp as he starts to play with me down there."
    bree.say "Mmm..."
    bree.say "Oh..."
    bree.say "Oh, Danny!"
    danny.say "Oh, so you like that?"
    danny.say "Huh, [hero.name]?"
    "All I can manage in response is a desperate nod of the head."
    danny.say "You don't want me to stop?"
    danny.say "You want some more?"
    "This time he gets an equally desperate nod."
    "Danny lets out another of those filthy chuckles of his."
    "And the sound, as well as what it signifies, turns me on almost as much as his touch!"
    "Danny's not taking his time about what he's doing either."
    "I can feel his fingers stroking the folds of my pussy."
    "But at the same time he's already probing between the lips."
    "Doing all that he can to get the tips of his fingers in there."
    "Normally I like a guy to take his time about things like this."
    "You know, put in the work to get me in the mood and ready for him?"
    "But somehow none of that seems to matter with Danny."
    "I guess I was expecting him to be rough and ready."
    "The kind of guy that sees what he wants and just takes it!"
    "Maybe that explains why my response isn't to call him a jerk or demand that he take his time."
    "Instead it's to make a desperate grab for the waistband of his trunks."
    "And then to grab what I find inside of them!"
    danny.say "Whoa..."
    danny.say "Looks like you know exactly what you want, [hero.name]!"
    danny.say "I like that in a woman!"
    "I don't know if I manage to nod in response or not."
    "All I know is that the moment I see Danny's cock, I forget everything else."
    "I'm rubbing my hands up and down his shaft like crazy."
    "And it's getting bigger all the time I'm doing that!"
    "Oh shit..."
    "How is he doing this to me?"
    "I'm a pretty intelligent girl, right?"
    "A modern woman that should me immune to this kind of macho bullshit!"
    "But all I know right now is that I want that thing inside of me!"
    "Danny seems to read my mind as he pulls his fingers out of my pussy."
    "And he can almost sit back then, watching me struggle to mount his cock."
    "I push it hard against the lips of my pussy, panting in desperation."
    "All the time hoping that none of my housemates see me doing all of this."
    "I don't know if I could face the shame of that..."
    "But once again, all thought of anything else fades a moment later."
    "And that's because I feel myself sinking down onto Danny's cock."
    "I mumble and moan incoherently as I feel him filling me."
    "My cheeks are flushed and I can feel my heart beating faster."
    "That's when Danny steps in and takes control."
    "Throwing my arm around his neck, he lifts up my leg."
    "His other hand holds my waist, putting me totally in his power."
    "And then he takes full advantage of that fact, thrusting into me from below."
    "I didn't think this could get any better, but I was wrong."
    "Danny fucks me hard and without hesitation."
    "Not once does he stop to ask if I'm okay with it."
    "And every moment is fucking glorious!"
    "I'm so not used to being treated like this."
    "Most modern guys are scared shitless of not pleasing a girl."
    "Or else they're afraid of being in charge and getting called a brute."
    "But Danny's already most of those things by nature."
    "And even better, he's like a goddamn machine!"
    "Maybe this isn't what I want to be treated like every time I make love."
    "But as a one-off thing it's thrilling beyond belief."
    "All I can do is lie back and let Danny have his way with me."
    "His cock thrusts in and out of me like a piston."
    "Every time he fills me, I feel myself losing it a little more."
    "Oh god...this isn't going to last long at all."
    "But when I ends, it's going to be quite something!"
    bree.say "Oh fuck..."
    bree.say "Harder, Danny..."
    bree.say "Fuck me harder!"
    danny.say "Dammit, woman!"
    danny.say "Are you trying to kill me?"
    "Despite his complaints, Danny does as he's told."
    "I feel him go even harder than before."
    "And it's enough to finish me off."
    with vpunch
    "I cling to him as I cum, burying my head in his shoulder."
    with vpunch
    "Danny loses it a few moments later, shooting his load into me."
    $ danny.impregnate()
    with vpunch
    "That makes me cum again, thrashing helplessly in the water."
    "Afterwards I slide off Danny's cock, exhausted and helpless."
    "He grins at me as he helps himself to more wine."
    "And all I can do is cling to the edge of the tub, my limbs feeling like jelly."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ danny.sexperience += 1
    $ game.active_date.clothes = None
    scene bg black with dissolve
    return

label give_danny_lapdance:
    "Oh man, this is going to be a tough one!"
    "Yeah, I know, I know - there's no such thing as an easy lap-dance."
    "And I did have a choice whether to take the job or not."
    "But at least normally I have the advantage of not knowing the guy."
    "Something that makes a huge difference, believe me."
    "One peak through the curtains lets me know that it's Danny waiting for me tonight."
    "No mistaking that face for anyone else - let alone the leering grin!"
    "He's like every sleazy extra from every bar in every action movie rolled into one!"
    "Urgh..."
    "This would have been so much easier if it were a guy like [mike.name]."
    "Someone that's sucker for having tits and ass shaken at him, for sure."
    "But not a genuinely intimidating guy the likes of Danny."
    "No, this guy would make [mike.name] run for the hills."
    "Come on, [hero.name]...pull yourself together!"
    "You knew there'd be times like this when you took the job."
    "If you can't walk in there and perform for this guy, then you should just up and quit!"
    "Plus, if I can do this kind of thing in front of Danny..."
    "Then I should be able to do it in front of anyone."
    "I nod, waving a hand in front of my face for the sake of the breeze it creates."
    "Then I do the best I can to let that little pep-talk sink in."
    "A nod to the left sees my music start up."
    "I take a moment to shake all of the kinks out."
    "And then I take a deep breath, stepping through the curtains."
    scene danny lapdance
    show danny lapdance nomc
    with fade
    "This is supposed to be the moment that the guy sees me for the first time."
    "The few seconds in which I have to dazzle him and take control of the encounter."
    "But right from the off, I'm still being thrown by Danny's intimidating presence."
    "At the sight of me, he leans forward in his chair."
    "There's a leering expression on his face, one that's hungry too."
    "And he claps his hands together loudly."
    "Not in applause, but in anticipation."
    show danny lapdance nomc at center, zoomAt(1.5, (420, 1040))
    danny.say "Oh yeah!"
    danny.say "Now this is what I'm taking about!"
    danny.say "Hey there, sweet-cheeks..."
    danny.say "How are you doing?"
    scene bg black
    show danny lapdance worried
    with fade
    "I'm already dancing as all of this happens."
    "Making sure to keep moving the whole time."
    "While also trying as best I can to keep out of Danny's reach."
    "Because if he's entranced, I figure he'll be easier to dodge."
    bree.say "I...I'm fine, Danny..."
    bree.say "In fact...I'm better than fine!"
    danny.say "Good to hear it, [hero.name]."
    danny.say "That means you're good to dance for me."
    danny.say "To get my motor running, yeah?"
    bree.say "Of course, Danny..."
    show danny lapdance normal
    bree.say "That's what I'm paid for!"
    "This seems to please Danny no end, and he leans back in his chair."
    "It's a relief to see him do so, giving me more room to work."
    "And it also means that there's less chance of him grabbing hold of me too!"
    "But then I remember that he's not sitting back in order to relax."
    "He's doing it to get a better view of the performance."
    "This realisation wakes me up and gets me moving."
    "It makes me start to really put the effort in and pull out all the stops."
    "I remember all the moves I can pull from my memory."
    "And I feel them flow together into a coherent routine."
    "Whereas before I was just playing for time, now I'm moving like I mean it."
    "I do the best I can to forget all about who Danny is."
    "What I need to do is think of him as being like any other customer."
    "To do this I stop myself from looking him in the face."
    "And instead I concentrate on moving in time to the music."
    "This seems to work, as I can feel the tension begin to drain out of me."
    "Soon I'm focused on the task at hand, leaving my worries behind."
    "My efforts seem to be having a positive effect on Danny too."
    "Because I can hear him clapping again."
    "But this time there's something different about the sound."
    "It takes me a moment to figure out just what that is."
    "And then I realise that he really is applauding me now!"
    show danny lapdance at center, zoomAt(1.5, (420, 1040))
    danny.say "Bravo, [hero.name], bravo!"
    danny.say "You're doing great!"
    danny.say "You really got this thing by the balls!"
    scene danny lapdance with fade
    "I know that I shouldn't be reacting like this."
    "And the modern feminist inside of me is cringing."
    "But Danny's words are already making a smile spread across my face."
    "There's just something so flattering about being praised in that way."
    "Especially when it comes from a guy the likes of him."
    "Maybe it's just a throwback to the days of men being in charge."
    "But it still gives me a little thrill, knowing I'm pleasing him!"
    "Then again, maybe it's just because Danny's such a bad-boy."
    "I can't help wondering what he'd do to me."
    "You know, if he were allowed to put his hands on my body..."
    "Part of me wonders just what he would do to me."
    "And how it would feel the whole time he was doing it!"
    "No...stop it, [hero.name]!"
    "Focus on the task at hand."
    "Plenty of time for day-dreaming when you're off duty."
    "The smile still on my face, I begin to move closer to Danny."
    "Of course his eyes are on me the whole time."
    "And he has a huge grin on his face too."
    "For a moment my eyes wander downwards, below his waist."
    "And that's when I see just how hard he is right now!"
    "I'm not shocked our outraged, you understand."
    "Just surprised by the sheer size of it!"
    "Of course, Danny notices my interest."
    danny.say "Oh, oh!"
    danny.say "Like what you see, huh?"
    "For a moment I feel like he's putting me on the spot."
    "And I can sense that I'm beginning to blush."
    "But then I remember where I am and what we're doing."
    "It takes a lot of willpower, but I push down the urge to blush."
    "And I do the best I can to forget all about the instinct to be embarrassed."
    bree.say "Oh, Danny..."
    bree.say "You bet I do!"
    bree.say "With some of the monsters that we get in here..."
    bree.say "It's a relief to see something so small!"
    "It takes a moment for what I just said to sink in."
    "But when it does, Danny frowns at me."
    danny.say "H...hey!"
    danny.say "What the hell's that supposed to mean?"
    danny.say "I'm a paying customer, dammit!"
    danny.say "You're supposed to be nice to me!"
    "Now it's my turn to laugh, long and as dirty as I can make it."
    "All the time I keep right on dancing too, teasing Danny."
    "And soon enough I see the heat in him begin to fuel his desire."
    "Instead of seething over my insult, he's watching me more intently."
    "And so I up my game accordingly."
    "I'm now shaking my ass in his face."
    "And then I switch around to do the same with my chest."
    "He's nodding, silently urging me on."
    "But what makes me so sure that I have him is what he's doing with his hand."
    "I can see Danny's arm moving, and then I glance down towards his wrist."
    show danny lapdance worried
    "And I notice that he has one of his hands inside his pants!"
    "I try not to laugh at the idea of him whacking off in front of me."
    "Instead I keep my attention focused on the dance."
    "Pretty soon Danny's self-stimulation is reaching its peak."
    "And I swear that his eyes are starting to glaze over too!"
    danny.say "Oh yeah..."
    danny.say "Oh yeah, [hero.name]..."
    danny.say "Just like that..."
    danny.say "Just like...uurgh..."
    "I take the guttural sound he just made as a sign he's lost it."
    "That and the fact that he's sitting there with his eyes crossed!"
    show danny lapdance normal
    "I stop dancing and bend over Danny, trying to see if he's okay."
    "Part of me is still worried that he'll turn out to be faking it."
    "And he'll jump on me the moment I'm withing reach."
    bree.say "Erm..."
    bree.say "Danny?"
    bree.say "Can you hear me?"
    "The only response I get from Danny is incoherent burbling."
    "But he's breathing and I'm pretty sure he won't swallow his tongue."
    "Plus I think I know what the wet patch spreading over his groin is."
    "So I pause just long enough to give him a nod."
    "And then I slip out between the curtains."
    "Already reflecting on what I think is a job well done."
    scene bg black with dissolve
    return

label danny_fuck_date_female(location="hero"):
    $ game.room = "bedroom4"
    call danny_fuck_date_intro_female (location) from _call_danny_fuck_date_intro_female
    if hero.skills.mouth.value >= 5:
        menu:
            "Offer a blowjob":
                call danny_fuck_date_blowjob from _call_danny_fuck_date_blowjob
            "Proceed to the main course":
                pass
    menu:
        "Standing":
            call danny_fuck_date_standing (0) from _call_danny_fuck_date_standing
        "Doggy" if hero.sexperience >= 5:
            call danny_fuck_date_doggy (5) from _call_danny_fuck_date_doggy

    if _return == "leave_without_gain":
        return
    $ danny.sexperience += 1
    if _return == "leave_with_gain":
        return
    hide danny
    call danny_sleep_date_fuck (location) from _call_danny_sleep_date_fuck
    return

label danny_fuck_date_intro_female(location="hero"):
    $ renpy.dynamic("result")
    $ result = game.days_played % 3
    if result == 0:
        scene bg house
        show danny
        with fade
        "I've been dreading the moment that I had to take Danny back to my place ever since we started dating."
        "Not because I'm worried that he might do something criminal, like steal out TV or anything like that."
        "No, it's more that I'm sure he'll spoil his manners if he bumps into [mike.name] or Sasha while he's there."
        "But right now we're on our way back from a date that's gone really well, and I don't want it to end yet."
        "So I'm gambling on the fact that it's going to be late enough for everyone else to be in bed right now."
        "Which makes us meeting either of my housemates between the front door and my bedroom highly unlikely."
        "Of course Danny seems delighted at the prospect of coming back to my place."
        "And he doesn't make any effort to hide his glee at what lies ahead as we walk up the path."
        show danny joke
        danny.say "Oh yeah..."
        danny.say "I've been waiting for this all night, [hero.name]..."
        danny.say "I hope your bed's got some heavy-duty springs inside of it!"
        show danny smile
        "Danny comes out with all of this as we're stepping onto the porch."
        "And as usual, he's not even trying to keep his voice down."
        if hero.morality >= 25:
            bree.say "Ooh..."
            bree.say "You have to be quieter, Danny..."
            bree.say "Otherwise you'll wake Sasha and [mike.name], who won't want you inside the house!"
        elif hero.morality <= -25:
            bree.say "Fuck sake, Danny..."
            bree.say "I wanna shag as much as you do, okay?"
            bree.say "But if [mike.name] and Sasha hear us, they'll totally kill my libido!"
        else:
            bree.say "Geez, Danny..."
            bree.say "Turn down the volume a little, yeah?"
            bree.say "If [mike.name] and Sasha hear us, you'll blow it!"
        "At first Danny tries to look all tough and unconcerned by my warning."
        show danny upset
        "But when I mention [mike.name] and Sasha ruining our fun, he seems to take things more seriously."
        "And his answer to me comes in the form of a low hiss."
        show danny angry
        danny.say "What?"
        danny.say "They'd really do that?!?"
        show danny upset
        "The truth is that I have no idea what [mike.name] and Sasha would do at the sight of Danny."
        "Seeing him creeping around the house in the middle of the night would probably freak them out."
        "Maybe even result in someone calling the police."
        "But if the threat of it means that I can make Danny behave, then I'm going to use it."
        "So I make sure to look serious as I unlock the door, nodding my head and holding a finger to my lips."
        scene bg livingroom
        show danny
        with fade
        "And I'm relieved to see Danny nod as he hurries after me, almost stepping on my heels."
        "Once we're inside the house, he seems to be trying hard to keep his mouth shut."
        "This makes me all the more determined to take full advantage."
        scene bg secondfloor
        show danny
        with fade
        "I pull Danny after me down the hall and then up the stairs, heading straight for my room."
        "Once there, I open the door and practically shove him in ahead of me."
        "Then I close the door behind us again, turning the lock to secure us some privacy."
        scene bg bedroom4 with fade
        "When I turn around, I'm expecting Danny to be already leering over me."
        "Practically drooling at the prospect of us getting it on."
        "But instead I find him standing in the middle of the room."
        show danny surprised with fade
        "His eyes are wide open, almost like he's stunned into silence by something."
        "I hurry over to him, concerned that there's something really wrong."
        "Well, that and out of the fear I might not be getting any tonight!"
        bree.say "Danny..."
        bree.say "What's wrong?"
        bree.say "Are you feeling okay?"
        "Danny slowly nods his head, blinking as she glances around the room."
        show danny shout
        danny.say "Ah..."
        danny.say "Yeah, [hero.name]..."
        danny.say "It's just...I never saw so much pink in one place before!"
        danny.say "It's kinda tripping me out..."
        show danny normal
        "I frown at Danny, not understanding what he means."
        "Sure, the walls, ceiling and floor are all pink."
        "And so are most of the plushies on my shelves, as well as my bedclothes."
        "But there are at least some things in here that aren't really pink at all!"
        if hero.morality >= 25:
            bree.say "Hey..."
            bree.say "You leave my choice in décor alone, you big meanie!"
            bree.say "Or else you can get out and go home."
        elif hero.morality <= -25:
            bree.say "Are you serious, Danny?"
            bree.say "You'd rather take the piss out of my décor then actually fuck?!?"
        else:
            bree.say "Come on, Danny..."
            bree.say "Snap out of it already!"
            bree.say "We're here to have fun, not critique my décor!"
        "For the second time tonight, my laying it on the line seems to work."
        "I watch as Danny shakes his head, like he's shaking off the funk was in."
        "And when he's done, I see his old self emerge once more."
        show danny shout
        danny.say "You're right, [hero.name]..."
        show danny joke
        danny.say "I dunno what came over me!"
        show danny normal
        "Danny chuckles as he begins to peel off his clothes and toss them aside."
        "And I turn my back on him to do the same."
        hide danny with dissolve
        "Not because I don't want him to see me getting naked."
        "But simply so that I can throw my own clothes into the laundry hamper."
        "As I'm doing this, I can almost feel Danny's eyes running up and down my body."
        "It's like I know that he's going to be treating himself the whole time."
        show danny normal naked with dissolve
        "When I turn back around I see that I'm right."
        "Danny's standing there, looking pleased with himself."
        "Perhaps because his cock is already hard and standing to attention."
        if hero.morality >= 25:
            "I do the best I can not to be intimidated by the sight of it."
            "But it's just so big that I can't help staring straight at it!"
        elif hero.morality <= -25:
            "My eyes go wide the moment I see it, and a smile spreads across my face."
            "Because the sight of it makes me remember just why I put up with Danny's bullshit."
            "It's so that I can get my hands on that magnificent monster between his legs!"
        else:
            "I want to do something to burst Danny's bubble."
            "But he's so goofy in his cockiness that I can't help giving him a lop-sided grin."
        show danny joke
        danny.say "Yeah, [hero.name]..."
        danny.say "You know you love the sight of it!"
        danny.say "Now get over here, and let's do this thing, yeah?"
        show danny normal
        "Trying to keep my true feelings off my face, I walk over to where Danny's standing."
        "But it's really no good, as I can't deny the way that he's able to get under my skin."
        "I know that I should be turned off by all of his bad qualities, like daddy always told me."
        "It's just there's that cute, goofy side to him that always makes me come running back for more."
    elif result == 1:
        scene bg house
        show danny
        with fade
        "As soon as the taxi drops us off outside the house, I lead Danny to the front door."
        scene bg livingroom
        show danny
        with fade
        "And then I open it as fast as I can manage, almost shoving him into the hallway."
        scene bg secondfloor
        show danny
        with fade
        "From there we hurry up the stairs and across the landing to my bedroom door."
        "Or to be more accurate, I do the best I can to drag Danny after me the whole time."
        "He seems to be more comfortable following at his own pace, chuckling all the way."
        if hero.morality >= 25:
            bree.say "Shh!"
            bree.say "Danny, be quiet..."
            bree.say "I don't want my housemates to know you're here!"
        elif hero.morality <= -25:
            bree.say "Shut up and hurry up, Danny!"
            bree.say "I've waited all night to get some."
            bree.say "And I'm not waiting any longer!"
        else:
            bree.say "Will you stop laughing, Danny?"
            bree.say "If you wake my housemates, we'll have to deal with the fallout."
            bree.say "And that's really going to kill the mood!"
        "Danny holds up his hands as I open the door and hurry inside."
        scene bg bedroom4
        show danny angry
        with fade
        danny.say "Geez..."
        show danny shout
        danny.say "Settle down, [hero.name]..."
        danny.say "We're here and we're gonna have some fun."
        danny.say "There's nothing more to it than that!"
        show danny smile
        "I'm still not totally convinced by Danny's attempts to reassure me."
        "So I end up almost slamming the door as I close it behind us."
        "But when I turn around a moment later, I feel all of my frustration vanish."
        "It's weird and I really can't explain it, suddenly none of it seems to matter."
        "All I'm seeing in front of me is the familiar sight of my own bedroom."
        "That and Danny standing in the middle of it, halfway through peeling off his shirt."
        "Pulling it over his head to reveal those hard, sinewy muscles of his."
        "Not to mention the tattoos and all that scar-tissue too!"
        show danny joke
        danny.say "Heh..."
        danny.say "You like what you see, huh?"
        show danny smile
        "As soon as Danny calls me out on the way I'm looking at him, the bubble bursts."
        "All of a sudden I'm right there in the room with him, not just a casual observer."
        if hero.morality >= 25:
            bree.say "I..."
            bree.say "I guess that I do, Danny!"
        elif hero.morality <= -25:
            bree.say "Oh, you know I do, Danny..."
            bree.say "But I'm really looking forward to the other half coming off!"
        else:
            bree.say "You know that I do, Danny..."
            bree.say "We wouldn't be here otherwise!"
        "Danny shakes his head and chuckles, already unbuckling his belt."
        "Then he lets his pants fall to his ankles, taking his shorts with them."
        show danny joke
        danny.say "Looks like you need to catch up, [hero.name]."
        danny.say "I'm already damn near naked."
        danny.say "And you're still got all of your clothes on!"
        show danny smile
        "I realise that he's right."
        show danny normal naked
        "Danny's kicking off his pants and socks."
        "But I'm still as much dressed as I was during our date!"
        "Quick as a flash I begin unbuttoning, unzipping and otherwise removing everything."
        "Which means that, rather than a sexy strip-tease, Danny's treated to an awkward display."
        "All four of my limbs are flailing around, flinging clothes away on all sides."
        "And by the time I'm finally naked too, my head is spinning from the effort of it all."
        show danny joke
        danny.say "Now that's what I'm takin' about!"
        show danny smile
        "Danny strides over to where I'm standing."
    else:
        scene bg house
        show danny
        with fade
        "I'm kind of walking on air as Danny and I make it back to my place."
        "And that's because we just had the best time yet on our date tonight."
        "I don't know what it was, but something just seemed to click for us."
        scene bg livingroom
        show danny
        with fade
        "Danny was funny and charming, with the slightest reminder of his being a bad boy."
        "He dropped in just enough of the latter to make sure that things were exciting."
        "But not so much that it spoiled the former and ruined the night for me."
        scene bg secondfloor
        show danny
        with fade
        if hero.morality >= 25:
            "So I decided to be brave and invite him back to the house."
        elif hero.morality <= -25:
            "So I was totally desperate to get him back to the house."
        else:
            "So it was a no-brainer to invite him back to the house."
        "And as we're walking into my room, I'm just hoping I made the right decision."
        scene bg bedroom4
        show danny angry
        with fade
        danny.say "Geez, [hero.name]..."
        danny.say "I can't remember the last time I saw this much pink!"
        danny.say "Or so many stuffed animals!"
        show danny upset
        "I feel myself blushing a little as Danny comments on the décor of my bedroom."
        "Because it's making me painfully aware of just how different our worlds are."
        bree.say "Oh, come on, Danny..."
        bree.say "It's not weird to have some soft toys around the place!"
        bree.say "Don't act like you never saw them before."
        "Danny picks up the nearest soft toy and shakes it."
        "Then he shakes his head as he puts it down again."
        show danny shout
        danny.say "Sure I've seen them before, [hero.name]."
        danny.say "But the ones I'm used to are usually packed full of drugs and shit!"
        show danny normal
        "In a desperate attempt to change the subject, I walk over to the bed."
        "Then I sit on the edge of the mattress and pat the space beside me."
        "This seems to do the trick, as Danny instantly follows my lead."
        "And a moment later the bed creaks as he sits down in the spot I showed him."
        show danny joke
        danny.say "So..."
        danny.say "I'm thinking you didn't invite me back here to talk about teddy-bears."
        danny.say "Am I right?"
        show danny smile
        if hero.morality >= 25:
            "Having Danny so close to me is a pretty intimidating thing."
            "But I'm determined to show him that I'm not afraid."
        elif hero.morality <= -25:
            "It's all I can do to keep from throwing myself at Danny right now."
            "Because his bad boy charm is already making me melt between my thighs!"
        else:
            "Danny can be pretty intimidating close up."
            "But I'm sure he's more interested in charming me than scaring me."
        bree.say "Of course not, Danny!"
        "I say this while holding his eye."
        "But at the same time I'm beginning to peel off my top."
        "Danny's eyes widen as he watches me, and his head nods slowly."
        "I swear that his gaze never moves from me once in the whole time it takes."
        "He watches intently as I remove every single piece of my clothing."
        "But that doesn't mean Danny stays still while he does so."
        "Because I see him begin to follow my lead, stripping off his own clothes."
        "So that by the time I finally kick off my panties, he's naked too!"
        show danny naked shout with dissolve
        danny.say "Heh..."
        danny.say "I like what I see, [hero.name]!"
        show danny joke
        danny.say "How about you?"
        show danny naked normal
        "My eyes can't help going wider than before as I look Danny up and down."
        "He's got one of those muscular bodies that you just know didn't come from the gym."
        "Plus he's got his fair share of tattoos and scars as well."
        "All of which combines to make a whole capable of leaving me weak at the knees!"
        if hero.morality >= 25:
            bree.say "Y...yeah, Danny..."
            bree.say "You have such a big...skull tattooed on your chest!"
        elif hero.morality <= -25:
            bree.say "Oh yeah, Danny!"
            bree.say "I love it - and it's totally turning me on too!"
        else:
            bree.say "I do, Danny..."
            bree.say "I don't think I ever saw so many tattoos in one place!"
            bree.say "It's like you're a walking work of art."
        "Danny nods and smiles, clearly pleased with my comments."
        show danny joke
        danny.say "If you like it so much..."
        danny.say "Then why don't you prove it to me?"
        show danny smile
        "Danny follows up the suggestion by sticking out his tongue."
        "Then he mimes licking at something in a totally suggestive manner."
        "As if I really needed him to make what he wants so obvious!"
        if hero.morality >= 25:
            bree.say "S...sure thing, Danny!"
        elif hero.morality <= -25:
            bree.say "You try and stop me, Danny!"
        else:
            bree.say "Okay, Danny - let's see what I can do!"
    return


label danny_fuck_date_blowjob:
    $ renpy.dynamic("result")
    $ result = game.days_played % 2
    if result == 0:
        "Without any warning, I get down on my knees."
        scene bg black
        show danny blowjob bedroom naked limp
        with fade
        "I can hear Danny chuckling to himself as I set to work."
        "And I can imagine the look on his face, picture him nodding in approval."
        "He's only half-way hard to begin with, a little limp in my hands."
        "But at the touch of my fingers I can feel him begin to stir."
        show danny blowjob hard
        "Soon enough his cock is rising up in front of my face."
        "And by the time I open my lips to kiss the tip, it's good and hard."
        show danny blowjob closed suck
        "I close my eyes and part my lips, taking him straight into my mouth."
        "Another time I might have put more effort into other stuff first."
        "So I kind of feel justified in cutting to the chase."
        "Not that Danny seems to mind me dispensing with the fancy stuff."
        show danny blowjob opened
        "From the moment I'm licking and caressing, he can't keep quiet."
        "I can hear him moaning and groaning with pleasure as my head moves back and forth."
        show danny blowjob deepthroat
        "And I quicken my pace as a result."
        "Luckily for me, Danny's too distracted to realise I'm doing this."
        "Hell, if he notices any change he probably just thinks I'm trying harder to please him!"
        show danny blowjob closed suck
        pause 0.2
        show danny blowjob deepthroat
        pause 0.2
        show danny blowjob suck
        pause 0.2
        show danny blowjob deepthroat
        pause 0.2
        show danny blowjob suck
        pause 0.2
        show danny blowjob deepthroat
        "By now I'm going as fast and hard as I dare."
        "Taking him ever deeper into my mouth to make things more intense."
        show danny blowjob opened
        "I can't help flinching as Danny slams his hands against the walls of the bedroom."
        "I know that he's only bracing himself so that he can keep on his feet."
        show danny blowjob closed suck
        pause 0.2
        show danny blowjob deepthroat
        pause 0.2
        show danny blowjob suck
        pause 0.2
        show danny blowjob deepthroat
        pause 0.2
        show danny blowjob suck
        pause 0.2
        show danny blowjob deepthroat
        "But it puts me on edge again, making me want to through this without being interrupted."
        "To that end, I reach down and take hold of Danny's balls."
        "And then I begin to squeeze them pretty hard."
        "That seems to do the trick, to be enough to push him over the edge."
        show danny blowjob suck opened
        pause 0.2
        show danny blowjob deepthroat
        pause 0.2
        show danny blowjob suck
        pause 0.2
        show danny blowjob deepthroat
        pause 0.2
        show danny blowjob suck
        pause 0.2
        show danny blowjob deepthroat
        "I know for certain that he's going to cum in the next few seconds."
        "And I just have enough time left to decide how I'm going to finish this."
        menu:
            "Swallow":
                show danny blowjob suck
                "I let Danny's cock slip a little way back."
                "Just enough to give me the space I'm going to need."
                "And then I wait for it to happen."
                show danny blowjob cum closed with vpunch
                "As soon as he looses it, I start to swallow."
                with vpunch
                "The fact that I'm prepared means it goes without a hitch."
                show danny blowjob lick pullout with vpunch
                "I'm able to handle everything Danny can throw at me with relative ease."
                show danny blowjob licking hard opened bodycum -cum
                "So things come to a smooth and satisfying end."
            "Pull his cock out":
                show danny blowjob lick pullout
                "I let Danny's cock slide all the way out of my mouth."
                "And then I wait patiently as it bobs in front of my face."
                show danny blowjob closed hard licking
                "Closing my eyes, I don't see the it as it happens."
                show danny blowjob cum with vpunch
                "Instead I feel the spattering of cum on my face."
                with vpunch
                "It's warm and sticky, covering my nose and cheeks."
                show danny blowjob facecum bodycum opened -cum with vpunch
                "Some of it even lands on my lips, letting me taste it too."
    else:
        "Sliding off the bed, I turn so that I'm facing Danny."
        "Then I kneel down in front of him, on level with his groin."
        "I swear that a few seconds ago, his cock was hidden between his legs."
        "But now, when I look down, it's standing to attention an inch from my face!"
        scene bg black
        show danny blowjob bedroom naked hard
        with fade
        bree.say "Aaargh!"
        bree.say "Where'd that come from?!?"
        danny.say "Heh..."
        danny.say "What can I say, [hero.name]?"
        danny.say "You have that kind of effect on a guy!"
        "Doing the best I can to play down my surprise, I put a smile on my face."
        "Then I lean in closer, wondering how best to get things started."
        "It's about then I notice Danny's eyes zeroing in on my breasts."
        "They're almost resting on his thighs, and they seem to be fascinating him."
        "So rather than going straight in with my mouth, I decide to take a different approach."
        "Lifting one breast with each hand, I separate them."
        "And then I lean forwards, trapping Danny's cock between them."
        "A quick glace upwards shows me the look of surprise and delight on his face."
        "Which is all the encouragement I need to throw myself into it."
        "Pushing my breasts together, I begin to massage the shaft of his cock."
        "I'm sure to keep it almost totally smothered at first."
        "But then I allow a little more to rise up at a time."
        "Soon enough this means that the tip emerges from my cleavage."
        "Then it's followed by the rest of the head, rising slowly below it."
        "I make sire to put a look of mock surprise on my face as it pops up."
        "Like it was the last thing I expected to see there."
        "And almost instantly I can hear Danny chuckling."
        danny.say "Heh..."
        danny.say "You like what you see, huh?"
        danny.say "Yeah, you know you do!"
        "I don't stop massaging him with my breasts for a moment."
        show danny blowjob speed
        "But now that he's so close to my face, I can start using my mouth too."
        "So I lean forwards and plant a kiss on the very tip."
        show danny blowjob suck
        "I repeat the action a couple of times."
        "Just enough for Danny to be lulled into a false sense of security."
        "Then I open my mouth wide, and I almost pounce on him."
        "I must have Danny's cock halfway into my mouth before he realises what's going on."
        "And when he does, I feel his entire body quiver in surprise."
        danny.say "Huh..."
        danny.say "Wha..."
        danny.say "What gives?!?"
        "Ignoring Danny's demand for an explanation, I press on with my plan."
        "Because I figure a physical demonstration will be a far better way of answering him."
        show danny blowjob deepthroat -speed
        "Taking him deep into my mouth, I begin to bob my head up and down."
        "This means that I can use my lips, tongue and teeth at the same time."
        show danny blowjob suck
        pause 0.2
        show danny blowjob deepthroat
        pause 0.2
        show danny blowjob suck
        pause 0.2
        show danny blowjob deepthroat
        pause 0.2
        show danny blowjob suck
        pause 0.2
        show danny blowjob deepthroat
        "Plus I can begin to get him ever deeper inside too."
        "Pretty soon there's no sign of objection from Danny."
        "Only the sound of him gasping and moaning as I go to work on him."
        "Making sure to relax the muscles in my throat, I prepare myself."
        show danny blowjob closed suck
        pause 0.2
        show danny blowjob deepthroat
        pause 0.2
        show danny blowjob suck
        pause 0.2
        show danny blowjob deepthroat
        pause 0.2
        show danny blowjob suck
        pause 0.2
        show danny blowjob deepthroat
        "And then I start to ease him down deeper than ever before."
        "I have no idea if Danny actually knows I'm deep-throating him right now."
        "But there's obviously no way that I can stop and check either."
        "So instead I just press on, doing everything I can to make it memorable."
        show danny blowjob suck opened speed
        pause 0.2
        show danny blowjob deepthroat
        pause 0.2
        show danny blowjob suck
        pause 0.2
        show danny blowjob deepthroat
        pause 0.2
        show danny blowjob suck
        pause 0.2
        show danny blowjob deepthroat
        "Pretty soon I can feel the effects that my efforts are having on Danny too."
        "He's beginning to twitch and spasm, like he's about to lose it."
        "Which means I'm going to have to make a decision before he does so."
        menu:
            "Pull his cock out":
                show danny blowjob lick pullout -speed
                "I make sure that I slide Danny's cock out of my mouth before the end."
                "Then I allow it to sink down just a little, still holding it between my breasts."
                show danny blowjob closed hard licking
                "I manage this just in time for the moment when he loses it."
                show danny blowjob cum with vpunch
                "All of which means I take the shot square in the face."
                "I smile as he stripes my face with his load."
                show danny blowjob facecum bodycum opened -cum with vpunch
                "And once he's done, Danny collapses backwards onto the bed."
                "Which I guess means that he's well and truly spent!"
            "Swallow":
                show danny blowjob suck -speed
                "All I need to do is dial things back a little before it happens."
                "Just ease Danny's cock a way up and out of my throat."
                "I manage to get it done a mere few seconds before it's too late."
                show danny blowjob cum closed with vpunch
                "Which means that I can swallow the load he fires into my mouth with ease."
                "Every drop passes down my throat without incident."
                show danny blowjob lick pullout with vpunch
                "And once he's done, Danny collapses backwards onto the bed."
                show danny blowjob licking hard opened bodycum -cum
                "Which I guess means that he's well and truly spent!"

    $ hero.skills.mouth.value += 1
    $ danny.love += 2
    return

label danny_fuck_date_standing(sexperience_min):
    "I'm fully expecting Danny to grab me and try to pull me onto the bed."
    "So when I feel his hands taking hold of me, I don't resist for a moment."
    "But then I find myself gasping in surprise as he neatly spins me around."
    "I put out my hands to keep myself from falling over, placing them flat against the wall."
    scene danny stand
    show danny stand bedroom
    with fade
    "And this seems to play right into what Danny has in mind for me."
    "Quick as a flash, he slides his hand left hand under my left knee."
    "Then he uses it to hoist my whole leg into the air."
    "This spreads my thighs wide apart, leaving what's between them exposed."
    "And I can already feel the presence of his manhood as it comes ever closer!"
    danny.say "So what's it gonna be?"
    danny.say "You want it in the front or the back door, [hero.name]?"
    menu:
        "Use the front door":
            if hero.morality >= 10:
                $ hero.morality -= 1
            if hero.morality >= 25:
                bree.say "Not the back door, Danny..."
                bree.say "That sounds scary!"
            elif hero.morality <= -25:
                bree.say "Put it in my pussy, Danny..."
                bree.say "And make sure you fill it up too!"
            else:
                bree.say "Don't get ahead of yourself, Danny..."
                bree.say "Put it in the front door!"
            "Danny let's out a wicked chuckle as I tell him what I want."
            danny.say "Okay, [hero.name]..."
            danny.say "What the lady wants, the lady gets!"
            call check_condom_usage (danny) from _call_check_condom_usage_140
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show danny stand condom
            "The first time Danny slides the head of his cock over my lips, I can't help quivering."
            "I feel like I've been waiting for this all night, every moment building up to this one."
            "The way it slithers and slides tells me that my body and mind are on the exact same page too."
            "Every pass Danny makes see the resistance down there weaken just a little."
            "Each time it brings him a little closer to being able to break down the barriers in his way."
            "This seems to go on for a long while, relief almost coming and then being snatched away."
            "Soon enough the feeling of frustration building inside of me is too much for me to handle."
            "So without warning, I reach down and take a firm hold of Danny's cock."
            danny.say "Urgh..."
            danny.say "[hero.name]..."
            danny.say "What are you doing?!?"
            "By way of an answer, I push the head of his member hard against the lips of my pussy."
            "Danny groans as I grind myself against him at the same time, moving back and forth."
            "I'm soon groaning too, feeling the effects of what I'm doing."
            "And then it happens, the lips of my pussy finally begin to give way."
            "Danny doesn't need to be told what he should do next."
            show danny stand vaginal eyes_closed mouth_pleasure
            "As soon as he's half an inch inside of me, instinct kicks in."
            "And I can feel him beginning to take control back from me again."
            show danny stand at stepback(speed=0.1, h=-10, v=0)
            "Danny's entire body begins to move back and forth, driving his cock deep into me."
            "Then he pulls all the way back, to the point where I'm sure he's going to slide out."
            show danny stand eyes_dazed at stepback(speed=0.1, h=-10, v=0)
            "But then he goes forwards again, as deep as before and with the same effect on me."
            show danny stand at stepback(speed=0.1, h=-10, v=0)
            "That's what I feel from then on, the rough motion of Danny fucking me."
            show danny stand at stepback(speed=0.1, h=-10, v=0)
            "Every muscle in his body devoted to the act and working as hard as it possibly can."
            "But I still need more!"
            bree.say "Danny..."
            bree.say "Harder..."
            bree.say "Fuck me harder!"
            show danny stand eyes_closed mouth_hurt
            "Danny doesn't say a word in response, making me think he didn't hear me."
            "But then I feel the sensation of him twining his hands into my hair."
            "And I gasp as he tightens his grip and pulls backwards."
            show danny stand mouth_pleasure
            "The additional leverage he gets from this seems to double the pleasure I'm feeling."
            "So much so that I'd be nodding my head and urging him on right now."
            "You know, if it wasn't for the fact he's yanking on my hair?"
            if hero.morality <= -10:
                menu:
                    "Enjoy yourself":
                        danny.say "Oh yeah..."
                        danny.say "Oh fuck yeah!"
                        show danny stand at stepback(speed=0.1, h=-10, v=0)
                        "Danny's really going for it by now, shouting and slapping my ass hard."
                        show danny stand at stepback(speed=0.1, h=-10, v=0)
                        "And we're rattling everything we touch around us at the same time."
                        show danny stand at stepback(speed=0.1, h=-10, v=0)
                        "Also, it's kind of hard for me to keep quiet through all of this too!"
                        show danny stand eyes_dazed mouth_dazed at stepback(speed=0.1, h=-10, v=0)
                        if hero.morality >= 25:
                            bree.say "Oh...Oh..."
                            bree.say "Oh, Danny...you bad boy!"
                        elif hero.morality <= -25:
                            bree.say "Uh...uh...uh..."
                            bree.say "Fuck me...harder, Danny...harder!"
                        else:
                            bree.say "Holy shit..."
                            bree.say "That's...that's so good!"
                        play sound door_banging
                        "Suddenly there's the sound of hammering at my bedroom door."
                        "And then a familiar voice on the other side."
                        mike.say "[hero.name]..."
                        mike.say "Keep it down in there, will you?"
                        mike.say "Some of us are trying to sleep!"
                        $ mike.love -= 4
                        show danny stand eyes_scared mouth_hurt
                        bree.say "Uh..."
                        bree.say "Okay...okay, [mike.name]..."
                        bree.say "I'll do...my best!"
                        "Danny and I are still as statues, waiting for [mike.name] to leave."
                        "Then we hear the sound of footsteps walking away and a door slamming."
                        danny.say "Don't worry, [hero.name]..."
                        danny.say "He's gone - and now, back to the fucking!"
                    "Keep it quiet":
                        danny.say "Oh yeah..."
                        danny.say "Oh fuck yeah!"
                        show danny stand eyes_scared mouth_dazed
                        bree.say "Shhh!"
                        bree.say "Keep it down a little, Danny!"
                        "Danny seems surprised by me telling him off."
                        "But he nods all the same and seems to take my warning to heart."
                        "For my part, I'm just relieved not to have gotten a visit from [mike.name] or Sasha."
                        "And I really want to keep it that way too."
            else:
                danny.say "Oh yeah..."
                danny.say "Oh fuck yeah!"
                show danny stand eyes_scared mouth_dazed
                bree.say "Shhh!"
                bree.say "Keep it down a little, Danny!"
                "Danny seems surprised by me telling him off."
                "But he nods all the same and seems to take my warning to heart."
                "For my part, I'm just relieved not to have gotten a visit from [mike.name] or Sasha."
                "And I really want to keep it that way too."
            "I have to give it to Danny, he's got some real stamina in that body of his."
            show danny stand eyes_dazed mouth_pleasure
            "Every time I glance over my shoulder, I'm treated to the sight of it moving and thrusting."
            "Those sinewy muscles of his aren't the kind you get by working out in the gym."
            "They're the kind a guy gets by living on the edge, by being a real life outlaw."
            "And the very thought of what he did to get them sends a shiver of excitement through my body!"
            "Danny seems to sense the shiver as it happens and take it for a side-effect of his physical attentions."
            show danny stand eyes_closed mouth_pleasure at stepback(speed=0.1, h=-10, v=0)
            "Because I hear him let out a filthy chuckle, and then he starts to move even faster and harder then before!"
            "This catches me totally off-guard, because it's the last thing I expected him to do."
            show danny stand at stepback(speed=0.1, h=-10, v=0)
            "I was sure he couldn't do more than we was doing, so I'd decided to let my guard down."
            "But now I can't do anything other than hold on for dear life as he pushes me further still."
            show danny stand at stepback(speed=0.1, h=-10, v=0)
            "Danny keeps on chuckling as he starts to see the effect that he's having on me."
            "Delighting in the sight and sensation of my own body made helpless by his own."
            "I know that I can't keep this pace up for much longer."
            show danny stand at stepback(speed=0.1, h=-10, v=0)
            "Danny's already starting to twitch and buck inside of me."
            "Now I have to decide exactly how I want this thing to end."
            call cum_reaction (danny, 'vaginal', sexperience_min) from _call_cum_reaction_265
            if _return == "vaginal_outside":
                bree.say "Danny..."
                bree.say "Get out of there..."
                bree.say "Right now!"
                "Normally I'd expect Danny to defy me, even just for the sake of it."
                show danny stand out
                "But this time he jumps to do as he's told, yanking his cock straight out of me."
                "The sensation pushes me over the edge, making me succumb to my own climax."
                show danny stand out cum with hpunch
                "And a moment later, Danny shoots his load all over my ass."
                show danny stand eyes_ahegao mouth_pleasure squirt with hpunch
                "Meanwhile my orgasm is in full effect, the sensation making my limbs go weak."
                "And in the end, the only thing holding me us is the grip Danny has on my body."
                $ danny.sub += 1
            else:
                bree.say "Danny..."
                bree.say "You stay right there..."
                bree.say "You hear me?!?"
                "There's no time for Danny to answer the question with words."
                "Instead I feel him stiffen, and then it happens."
                if not CONDOM:
                    show danny stand cum
                with hpunch
                "Danny explodes, shooting his load into me."
                with hpunch
                "He's as deep as he can be at that moment."
                with hpunch
                "So I feel everything, the sensation making my limbs go weak."
                show danny stand eyes_ahegao mouth_pleasure squirt
                "And in the end, the only thing holding me us is the grip Danny has on my body."
                if not CONDOM:
                    $ danny.impregnate()
                $ danny.love += 2
            $ hero.skills.pussy.value += 1
        "Use my back door" if hero.sexperience >= (sexperience_min + 5):
            if hero.morality >= -10:
                $ hero.morality -= 1
            if hero.morality >= 25:
                bree.say "ooh the back door, Danny..."
                bree.say "That sounds so exciting!"
            elif hero.morality <= -25:
                bree.say "Put it in my ass, Danny..."
                bree.say "And make sure you fill it up too!"
            else:
                bree.say "Why don't you treat yourself, Danny..."
                bree.say "Go ahead and use the back door!"
            "Danny let's out a wicked chuckle as I tell him what I want."
            danny.say "Okay, [hero.name]..."
            danny.say "What the lady wants, the lady gets!"
            "The first time Danny slides the head of his cock between my buttocks, I can't help quivering."
            "I feel like I've been waiting for this all night, every moment building up to this one."
            "The way it slithers and slides tells me that my body and mind are on the exact same page too."
            "Every pass Danny makes see the resistance down there weaken just a little."
            "Each time it brings him a little closer to being able to break down the barriers in his way."
            "This seems to go on for a long while, relief almost coming and then being snatched away."
            "Soon enough the feeling of frustration building inside of me is too much for me to handle."
            "So without warning, I reach down and take a firm hold of Danny's cock."
            danny.say "Urgh..."
            danny.say "[hero.name]..."
            danny.say "What are you doing?!?"
            "By way of an answer, I push the head of his member hard against my hole."
            "Danny groans as I grind myself against him at the same time, moving back and forth."
            "I'm soon groaning too, feeling the effects of what I'm doing."
            "And then it happens, the muscles of my ass finally begin to give way."
            "Danny doesn't need to be told what he should do next."
            show danny stand anal eyes_closed mouth_pleasure
            "As soon as he's half an inch inside of me, instinct kicks in."
            "And I can feel him beginning to take control back from me again."
            show danny stand at stepback(speed=0.1, h=-10, v=0)
            "Danny's entire body begins to move back and forth, driving his cock deep into me."
            "Then he pulls all the way back, to the point where I'm sure he's going to slide out."
            show danny stand eyes_dazed at stepback(speed=0.1, h=-10, v=0)
            "But then he goes forwards again, as deep as before and with the same effect on me."
            show danny stand at stepback(speed=0.1, h=-10, v=0)
            "That's what I feel from then on, the rough motion of Danny fucking me."
            show danny stand at stepback(speed=0.1, h=-10, v=0)
            "Every muscle in his body devoted to the act and working as hard as it possibly can."
            "But I still need more!"
            bree.say "Danny..."
            bree.say "Harder..."
            bree.say "Fuck me harder!"
            show danny stand eyes_closed mouth_hurt
            "Danny doesn't say a word in response, making me think he didn't hear me."
            "But then I feel the sensation of him twining his hands into my hair."
            "And I gasp as he tightens his grip and pulls backwards."
            show danny stand mouth_pleasure
            "The additional leverage he gets from this seems to double the pleasure I'm feeling."
            "So much so that I'd be nodding my head and urging him on right now."
            "You know, if it wasn't for the fact he's yanking on my hair?"
            if hero.morality <= -10:
                menu:
                    "Enjoy yourself":
                        danny.say "Oh yeah..."
                        danny.say "Oh fuck yeah!"
                        show danny stand at stepback(speed=0.1, h=-10, v=0)
                        "Danny's really going for it by now, shouting and slapping my ass hard."
                        show danny stand at stepback(speed=0.1, h=-10, v=0)
                        "And we're rattling everything we touch around us at the same time."
                        show danny stand at stepback(speed=0.1, h=-10, v=0)
                        "Also, it's kind of hard for me to keep quiet through all of this too!"
                        show danny stand eyes_dazed mouth_dazed at stepback(speed=0.1, h=-10, v=0)
                        if hero.morality >= 25:
                            bree.say "Oh...Oh..."
                            bree.say "Oh, Danny...you bad boy!"
                        elif hero.morality <= -25:
                            bree.say "Uh...uh...uh..."
                            bree.say "Fuck me...harder, Danny...harder!"
                        else:
                            bree.say "Holy shit..."
                            bree.say "That's...that's so good!"
                        play sound door_banging
                        "Suddenly there's the sound of hammering at my bedroom door."
                        "And then a familiar voice on the other side."
                        mike.say "[hero.name]..."
                        mike.say "Keep it down in there, will you?"
                        mike.say "Some of us are trying to sleep!"
                        $ mike.love -= 4
                        show danny stand eyes_scared mouth_hurt
                        bree.say "Uh..."
                        bree.say "Okay...okay, [mike.name]..."
                        bree.say "I'll do...my best!"
                        "Danny and I are still as statues, waiting for [mike.name] to leave."
                        "Then we hear the sound of footsteps walking away and a door slamming."
                        danny.say "Don't worry, [hero.name]..."
                        danny.say "He's gone - and now, back to the fucking!"
                    "Keep it quiet":
                        danny.say "Oh yeah..."
                        danny.say "Oh fuck yeah!"
                        show danny stand eyes_scared mouth_dazed at stepback(speed=0.1, h=-10, v=0)
                        bree.say "Shhh!"
                        bree.say "Keep it down a little, Danny!"
                        "Danny seems surprised by me telling him off."
                        "But he nods all the same and seems to take my warning to heart."
                        "For my part, I'm just relieved not to have gotten a visit from [mike.name] or Sasha."
                        "And I really want to keep it that way too."
            else:
                danny.say "Oh yeah..."
                danny.say "Oh fuck yeah!"
                show danny stand eyes_scared mouth_dazed at stepback(speed=0.1, h=-10, v=0)
                bree.say "Shhh!"
                bree.say "Keep it down a little, Danny!"
                "Danny seems surprised by me telling him off."
                "But he nods all the same and seems to take my warning to heart."
                "For my part, I'm just relieved not to have gotten a visit from [mike.name] or Sasha."
                "And I really want to keep it that way too."
            "I have to give it to Danny, he's got some real stamina in that body of his."
            show danny stand eyes_dazed mouth_pleasure
            "Every time I glance over my shoulder, I'm treated to the sight of it moving and thrusting."
            "Those sinewy muscles of his aren't the kind you get by working out in the gym."
            "They're the kind a guy gets by living on the edge, by being a real life outlaw."
            "And the very thought of what he did to get them sends a shiver of excitement through my body!"
            "Danny seems to sense the shiver as it happens and take it for a side-effect of his physical attentions."
            show danny stand eyes_closed mouth_pleasure at stepback(speed=0.1, h=-10, v=0)
            "Because I hear him let out a filthy chuckle, and then he starts to move even faster and harder then before!"
            "This catches me totally off-guard, because it's the last thing I expected him to do."
            show danny stand at stepback(speed=0.1, h=-10, v=0)
            "I was sure he couldn't do more than we was doing, so I'd decided to let my guard down."
            show danny stand at stepback(speed=0.1, h=-10, v=0)
            "But now I can't do anything other than hold on for dear life as he pushes me further still."
            "Danny keeps on chuckling as he starts to see the effect that he's having on me."
            "Delighting in the sight and sensation of my own body made helpless by his own."
            "I know that I can't keep this pace up for much longer."
            show danny stand at stepback(speed=0.1, h=-10, v=0)
            "Danny's already starting to twitch and buck inside of me."
            "Now I have to decide exactly how I want this thing to end."
            call cum_reaction (danny, 'anal', sexperience_min) from _call_cum_reaction_266
            if _return == 'anal_outside':
                bree.say "Danny..."
                bree.say "Get out of there..."
                bree.say "Right now!"
                "Normally I'd expect Danny to defy me, even just for the sake of it."
                show danny stand out
                "But this time he jumps to do as he's told, yanking his cock straight out of me."
                with hpunch
                "The sensation pushes me over the edge, making me succumb to my own climax."
                show danny stand out cum with hpunch
                "And a moment later, Danny shoots his load all over my ass."
                show danny stand eyes_ahegao mouth_pleasure squirt with hpunch
                "Meanwhile my orgasm is in full effect, the sensation making my limbs go weak."
                "And in the end, the only thing holding me us is the grip Danny has on my body."
                $ danny.sub += 2
                $ danny.love += 1
            elif _return == 'anal_inside':
                bree.say "Danny..."
                bree.say "You stay right there..."
                bree.say "You hear me?!?"
                "There's no time for Danny to answer the question with words."
                "Instead I feel him stiffen, and then it happens."
                show danny stand cum with hpunch
                "Danny explodes, shooting his load into me."
                with hpunch
                "He's as deep as he can be at that moment."
                with hpunch
                "So I feel everything, the sensation making my limbs go weak."
                show danny stand eyes_ahegao mouth_pleasure squirt
                "And in the end, the only thing holding me us is the grip Danny has on my body."
                $ danny.sub += 1
                $ danny.love += 2
            $ danny.flags.anal += 1
            $ hero.skills.ass.value += 1
    "Once we're both spent, Danny and I hold each other up as we stagger to my bed."
    "Danny collapses onto the mattress first, then I land right by his side."
    "And I have no idea which of us falls asleep first, just that I soon black out."
    "All I need right now is to rest, to recharge my batteries and wake up refreshed."
    return

label danny_fuck_date_doggy(sexperience_min):
    $ renpy.dynamic("result")
    $ result = game.days_played % 2
    if result == 0:
        "The whole time I can feel Danny's eyes on me."
        "He's staring in silence, eyes getting wider the whole time."
        "I slowly crawls on the floor on all fours, taking my time."
        scene danny doggy
        show danny doggy nonpc pleasure
        with fade
        "And I look back over my shoulder at him."
        bree.say "What about it, Danny?"
        bree.say "You wanna help me be bad?"
        danny.say "Urgh..."
        danny.say "Ah shit, [hero.name]..."
        danny.say "Wadda ya trying to do to me?!?"
        "Even as he's saying all of this, he's closing the short distance between us too."
        show danny doggy -nonpc with fade
        "And by the time he reaches the bed, he's more than ready to go."
        "I only catch a brief glimpse of his cock as he leaps up behind me."
        "But like the rest of him, it looks excited, hard and ready for business!"
        "I can't help letting out a little yelp as I feel him grab hold of me."
        "Danny's hands are large and rough, taking a firm grip."
        "But I keep telling myself that this is what I wanted."
        "This is what I was trying to goad him into doing."
        "I just hope that I can handle what I'm asking for!"
        danny.say "So what's it gonna be?"
        danny.say "You want it in the front or the back door, [hero.name]?"
        menu:
            "Use the front door":
                if hero.morality >= 10:
                    $ hero.morality -= 1
                if hero.morality >= 25:
                    bree.say "Not the back door, Danny..."
                    bree.say "That sounds scary!"
                elif hero.morality <= -25:
                    bree.say "Put it in my pussy, Danny..."
                    bree.say "And make sure you fill it up too!"
                else:
                    bree.say "Don't get ahead of yourself, Danny..."
                    bree.say "Put it in the front door!"
                "Danny let's out a wicked chuckle as I tell him what I want."
                danny.say "Okay, [hero.name]..."
                danny.say "What the lady wants, the lady gets!"
                call check_condom_usage (danny) from _call_check_condom_usage_141
                if _return == False:
                    return "leave_without_gain"
                if CONDOM:
                    show danny doggy condom
                "Suddenly there doesn't seem to be room for thinking anymore."
                "Because I feel the sensation of something between my legs."
                "At first I think it must be Danny's cock."
                "But then I feel myself being touched in more than one place."
                "It's one of his hands!"
                "I shudder as Danny strokes and caresses me down there."
                "His fingertips trace the lines of my lips, exploring the folds."
                "And every movement makes me looser and wetter than the last."
                "My head nods without any conscious thought."
                "Because he seems to know exactly what he's doing down there."
                "In what feels like no time at all, I know that my body's surrendering to him."
                "Part of me expects Danny to push further, to put his fingers inside of me."
                show danny doggy hurt rolled vaginal
                "But then my head comes up and my eyes pop open."
                "Because instead he chooses that moment to get his cock involved."
                show danny doggy pleasure
                "I gasp as I feel him pushing into me."
                "He's not taking it slowly either."
                "Danny thrusts himself into me in one go."
                "He doesn't pause or hesitate, just keeps right on going."
                show danny doggy normal
                "I can feel every inch of him entering me, parting the walls of my pussy."
                "For a moment I actually think that he might never stop."
                "But eventually he does, stopping only when he can't go any further."
                danny.say "How's that feel, [hero.name]?"
                danny.say "You like that, huh?"
                bree.say "Y...yeah..."
                bree.say "I...I like it..."
                "My panting and gasping for breath is only in part from what I'm feeling right now."
                "A lot of it is actually because of the anticipation I have for what's coming next."
                danny.say "Then let's see how you like this!"
                show danny doggy hurt rolled speed with hpunch
                "That's the only warning I get before Danny leaps into action."
                "And before I know what's happening, he's moving inside of me."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "There's no slow build, no chance for me to get up to speed."
                "Instead Danny just kicks into high gear goes for it."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "I can hear someone moaning and crying out in the room."
                "But it takes me a few moments to realise that it's me!"
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "Sure, Danny's grunting with the effort as he pounds away."
                "But those other sounds can only be coming from me."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "I don't remember the last time I got fucked like this."
                "Or maybe I've never had it this hard and rough before."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "With all that Danny's doing to me, it's hard to be sure."
                "I guess this is what I wanted."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "To be made love to like he would with the girl that lives here."
                "If you could really call what we're doing making love, that is."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "It kinda feels more like being humped in a mating frenzy!"
                "But the fact is that I'm taking all he can give me."
                "And I know that I want more!"
                show danny doggy down hurt with hpunch
                "Danny might be thrusting into me for all he's worth."
                "But I'm pushing back into him at the same time."
                "Arching my back to make sure the angle is just right."
                show danny doggy speed with hpunch
                pause 0.2
                show danny doggy -speed
                "I can feel the roughness of his hands."
                "And the way that his coiled muscles are working so hard."
                show danny doggy speed with hpunch
                pause 0.2
                show danny doggy -speed
                "Those aren't the kind that you get from working out at the gym either."
                "Just thinking about the fights and chases with the cops that must have built them."
                show danny doggy speed pleasure with hpunch
                pause 0.2
                show danny doggy -speed
                "Oh god..."
                "The simple thought of it sends a shudder of excitement through my entire body!"
                "I never really faced the danger that Danny embodies this honestly before now."
                show danny doggy speed with hpunch
                pause 0.2
                show danny doggy -speed
                "He's no pretend bad boy either - he's the genuine article!"
                show danny doggy speed with hpunch
                pause 0.2
                show danny doggy -speed
                bree.say "Danny..."
                bree.say "Oh fuck..."
                bree.say "I'm...I'm gonna cum!"
                danny.say "Sh...shit..."
                danny.say "I can feel it..."
                call cum_reaction (danny, 'vaginal', sexperience_min) from _call_cum_reaction_267
                if _return == "vaginal_outside":
                    bree.say "Get out of there..."
                    bree.say "Right now!"
                    "The muscles in my pussy begin to clench and squeeze."
                    "And I can hear Danny groaning as they clamp down on him."
                    "He's going so fast and hard that there's no way he can pace himself."
                    show danny doggy up out -vaginal with hpunch
                    "In an unexpected move, he manage to pull his cock out."
                    "And he begins to cum a moment later too."
                    show danny doggy ahegao rolled with hpunch
                    "All the same we both keep right on going until the end."
                    "Keeping up the pace we've set and making the climax that much more intense."
                    show danny doggy squirt cum cumshot -speed with hpunch
                    "I feel Danny's cum on my back."
                    show danny doggy down rolled
                    "And then everything seems to go dark as I slump onto the bed."
                    $ danny.sub += 1
                else:
                    bree.say "You stay right there..."
                    bree.say "You hear me?!?"
                    "The muscles in my pussy begin to clench and squeeze."
                    "And I can hear Danny groaning as they clamp down on him."
                    "He's going so fast and hard that there's no way he can pace himself."
                    show danny doggy up with hpunch
                    "And he begins to cum a moment later too."
                    show danny doggy ahegao rolled with hpunch
                    "All the same we both keep right on going until the end."
                    "Keeping up the pace we've set and making the climax that much more intense."
                    show danny doggy squirt creampie -speed with hpunch
                    "I feel Danny explode inside of me."
                    show danny doggy down rolled
                    "And then everything seems to go dark as I slump onto the bed."
                    if not CONDOM:
                        $ danny.impregnate()
                    $ danny.love += 2
                $ hero.skills.pussy.value += 1
            "Use my back door" if hero.sexperience >= (sexperience_min + 5):
                if hero.morality >= -10:
                    $ hero.morality -= 1
                if hero.morality >= 25:
                    bree.say "ooh the back door, Danny..."
                    bree.say "That sounds so exciting!"
                elif hero.morality <= -25:
                    bree.say "Put it in my ass, Danny..."
                    bree.say "And make sure you fill it up too!"
                else:
                    bree.say "Why don't you treat yourself, Danny..."
                    bree.say "Go ahead and use the back door!"
                "Danny let's out a wicked chuckle as I tell him what I want."
                danny.say "Okay, [hero.name]..."
                danny.say "What the lady wants, the lady gets!"
                "Suddenly there doesn't seem to be room for thinking anymore."
                "Because I feel the sensation of something between my legs."
                "At first I think it must be Danny's cock."
                "But then I feel myself being touched in more than one place."
                "It's one of his hands!"
                "I shudder as Danny strokes and caresses me down there."
                "His fingertips trace the lines of my lips, exploring the folds."
                "And every movement makes me looser and wetter than the last."
                "My head nods without any conscious thought."
                "Because he seems to know exactly what he's doing down there."
                "In what feels like no time at all, I know that my body's surrendering to him."
                "Part of me expects Danny to push further, to put his fingers inside of me."
                show danny doggy hurt rolled anal
                "But then my head comes up and my eyes pop open."
                "Because instead he chooses that moment to get his cock involved."
                show danny doggy pleasure
                "I gasp as I feel him pushing into me."
                "He's not taking it slowly either."
                "Danny thrusts himself into me in one go."
                "He doesn't pause or hesitate, just keeps right on going."
                show danny doggy normal
                "I can feel every inch of him entering me, parting the walls of my ass."
                "For a moment I actually think that he might never stop."
                "But eventually he does, stopping only when he can't go any further."
                danny.say "How's that feel, [hero.name]?"
                danny.say "You like that, huh?"
                bree.say "Y...yeah..."
                bree.say "I...I like it..."
                "My panting and gasping for breath is only in part from what I'm feeling right now."
                "A lot of it is actually because of the anticipation I have for what's coming next."
                danny.say "Then let's see how you like this!"
                show danny doggy hurt rolled speed with hpunch
                "That's the only warning I get before Danny leaps into action."
                "And before I know what's happening, he's moving inside of me."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "There's no slow build, no chance for me to get up to speed."
                "Instead Danny just kicks into high gear goes for it."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "I can hear someone moaning and crying out in the room."
                "But it takes me a few moments to realise that it's me!"
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "Sure, Danny's grunting with the effort as he pounds away."
                "But those other sounds can only be coming from me."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "I don't remember the last time I got fucked like this."
                "Or maybe I've never had it this hard and rough before."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "With all that Danny's doing to me, it's hard to be sure."
                "I guess this is what I wanted."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "To be made love to like he would with the girl that lives here."
                "If you could really call what we're doing making love, that is."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "It kinda feels more like being humped in a mating frenzy!"
                "But the fact is that I'm taking all he can give me."
                "And I know that I want more!"
                show danny doggy down hurt with hpunch
                "Danny might be thrusting into me for all he's worth."
                "But I'm pushing back into him at the same time."
                "Arching my back to make sure the angle is just right."
                show danny doggy speed with hpunch
                pause 0.2
                show danny doggy -speed
                "I can feel the roughness of his hands."
                "And the way that his coiled muscles are working so hard."
                show danny doggy speed with hpunch
                pause 0.2
                show danny doggy -speed
                "Those aren't the kind that you get from working out at the gym either."
                "Just thinking about the fights and chases with the cops that must have built them."
                show danny doggy speed pleasure with hpunch
                pause 0.2
                show danny doggy -speed
                "Oh god..."
                "The simple thought of it sends a shudder of excitement through my entire body!"
                "I never really faced the danger that Danny embodies this honestly before now."
                show danny doggy speed with hpunch
                pause 0.2
                show danny doggy -speed
                "He's no pretend bad boy either - he's the genuine article!"
                show danny doggy speed with hpunch
                pause 0.2
                show danny doggy -speed
                bree.say "Danny..."
                bree.say "Oh fuck..."
                bree.say "I'm...I'm gonna cum!"
                danny.say "Sh...shit..."
                danny.say "I can feel it..."
                call cum_reaction (danny, 'anal', sexperience_min) from _call_cum_reaction_268
                if _return == "anal_outside":
                    bree.say "Get out of there..."
                    bree.say "Right now!"
                    "My muscles begin to clench and squeeze."
                    "And I can hear Danny groaning as they clamp down on him."
                    "He's going so fast and hard that there's no way he can pace himself."
                    show danny doggy up out -anal with hpunch
                    "In an unexpected move, he manage to pull his cock out."
                    "And he begins to cum a moment later too."
                    show danny doggy ahegao rolled with hpunch
                    "All the same we both keep right on going until the end."
                    "Keeping up the pace we've set and making the climax that much more intense."
                    show danny doggy squirt cum cumshot -speed with hpunch
                    "I feel Danny's cum on my back."
                    show danny doggy down rolled
                    "And then everything seems to go dark as I slump onto the bed."
                    $ danny.sub += 1
                else:
                    bree.say "You stay right there..."
                    bree.say "You hear me?!?"
                    "My muscles begin to clench and squeeze."
                    "And I can hear Danny groaning as they clamp down on him."
                    "He's going so fast and hard that there's no way he can pace himself."
                    show danny doggy up with hpunch
                    "And he begins to cum a moment later too."
                    show danny doggy ahegao rolled with hpunch
                    "All the same we both keep right on going until the end."
                    "Keeping up the pace we've set and making the climax that much more intense."
                    show danny doggy squirt creampie -speed with hpunch
                    "I feel Danny explode inside of me."
                    show danny doggy down rolled
                    "And then everything seems to go dark as I slump onto the bed."
                    $ danny.sub += 1
                    $ danny.love += 2
                $ danny.flags.anal += 1
                $ hero.skills.ass.value += 1
    else:
        "I try to maintain eye-contact, but he walks around behind me."
        "And then he literally claps his hands onto my haunches!"
        "This stops me from turning to follow him."
        "But it also makes a loud cracking sound, causing me to jump in surprise."
        bree.say "Aargh!"
        danny.say "Don't worry, [hero.name]..."
        danny.say "I got you."
        "I can feel Danny pulling me downwards, and I'm powerless to resist."
        scene danny doggy
        show danny doggy nonpc pleasure
        with fade
        "Following his lead, I allow myself to be guided down until I'm on all-fours."
        "And all the time it's happening, I can feel my heart starting to race."
        if hero.morality >= 25:
            bree.say "P...promise me you'll be gentle?"
        elif hero.morality <= -25:
            bree.say "I'm going as fast as I can, okay?"
            bree.say "And you'd better make this worth my while too!"
        else:
            bree.say "Okay, Danny..."
            bree.say "I know that we both want the same thing!"
        "I can hardly wait for Danny to get started, for what's coming next."
        "In fact I'm almost biting my lip in anticipation."
        "But then I realise that he's not making his move."
        show danny doggy -nonpc with fade
        danny.say "Ah, [hero.name]..."
        danny.say "Where'd you actually want it?"
        "Part of me can't believe that Danny's actually stopped to ask me that question."
        "But another is kind of touched that he's capable of thinking of me at a time like this."
        menu:
            "Fuck my pussy":
                if hero.morality >= 10:
                    $ hero.morality -= 1
                if hero.morality >= 25:
                    bree.say "Erm..."
                    bree.say "Could you maybe use the front-door?"
                elif hero.morality <= -25:
                    bree.say "What are you waiting for, Danny?"
                    bree.say "Stick it in my pussy already!"
                else:
                    bree.say "Hmm..."
                    bree.say "I think I fancy it in the front tonight."
                "I feel Danny's grip on me tighten as soon as I'm done speaking."
                "And I can sense that this time he's all ready to go."
                call check_condom_usage (danny) from _call_check_condom_usage_144
                if _return == False:
                    return "leave_without_gain"
                if CONDOM:
                    show danny doggy condom
                "It's at times like this I'm reminded of just how strong Danny really is."
                "And by that I don't mean the kind of strength that comes from working out at the gym."
                "Because as Danny's grip tightens on me, I can feel that his strength comes from the way he lives his life."
                "The way he's a guy that lives on the edge and survives by his wits, that's what makes him so strong."
                "It also translates into the way that he makes love too, filling him with an eagerness and a passion."
                "I guess when you're living so dangerously, everything you can experience is deadly important."
                "Because you never know when fate is going to catch up to you, when the pleasure you're feeling might be your last."
                "Maybe that's why I feel myself shiver with anticipation when his cock slides between my thighs."
                "And it might also go a long way towards explaining what happens when he rubs the head against my pussy too."
                "Normally I'd expect there to be at least a small measure of natural resistance before my body allowed him inside."
                "Even the smallest token to make him put in the effort."
                show danny doggy pleasure vaginal

                "But to my surprise, I feel the lips down there begin to part almost immediately."
                if hero.morality >= 25:
                    bree.say "Oh..."
                    bree.say "Oh my goodness!"
                elif hero.morality <= -25:
                    bree.say "Aah..."
                    bree.say "Oh fuck yeah!"
                else:
                    bree.say "Mmm..."
                    bree.say "Oh my god!"
                "Danny seems to take my words as encouragement, and begins to push harder as well as faster."
                "Which is more than okay with me, as it means that I get to feel him inching all the way into me."
                show danny doggy hurt rolled vaginal
                "I can't begin to describe the way that it feels as anything other than amazing and overwhelming."
                "But when he really begins to move a moment later, I feel like he's totally blowing my mind."
                "Before I was keen on keeping myself involved in dictating what's going on between us."
                "Yet now all I can do is lower my head and bite my lip, surrendering myself to the experience."
                "Each time Danny thrusts forwards, I feel like a jolt of electricity passes through my body."
                show danny doggy normal
                "Looking down I can see my arms shaking from the force of it, and my breasts swinging too."
                "Danny's fingers are digging into the soft flesh of my waist s he grips me tighter."
                "Even though I feel like I've lost the ability to speak, I'm silently urging him on."
                "And much to my delight, it feels as though Danny can sense what I'm thinking."
                "Because he somehow manages to suddenly kick things up another gear."
                "Before I was keeping quiet and just enjoying the feeling of being fucked."
                show danny doggy hurt rolled speed with hpunch
                "But now there's nothing I can do to keep myself from starting to cry out."
                "Pretty soon I'm moaning whenever Danny thrusts himself into me."
                "And then I'm left helplessly whimpering when he goes the other way."
                "All the time I'm doing everything I can to make him go harder and deeper."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "I spread my legs, lower myself down and push backwards for all I'm worth."
                "Anything to add even a little more effect to what Danny's making me feel."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                danny.say "Urgh..."
                danny.say "You better be ready, [hero.name]..."
                danny.say "Cos I'm gonna cum!"
                "At the mere mention of Danny shooting his load, my eyes snap open."
                "Then my head shoots up as I come back to life, determined to take back control."
                call cum_reaction (danny, 'vaginal', sexperience_min) from _call_cum_reaction_273
                if _return == "vaginal_outside":
                    if hero.morality >= 25:
                        bree.say "Mmm..."
                        bree.say "D...Danny..."
                        bree.say "Pull out...please!"
                    elif hero.morality <= -25:
                        bree.say "D...don't you...dare cum in me..."
                        bree.say "You pull out of there...before...you...cum!"
                    else:
                        bree.say "P...pull out..."
                        bree.say "Don't...don't cum in me!"
                    show danny doggy up out -vaginal with hpunch
                    "My pleas seem to have the desired effect on Danny, as I feel him begin to pull out."
                    show danny doggy ahegao rolled with hpunch
                    "And he only just manages to do so before he loses it, shooting his load into the air."
                    "As his cock is bobbing over my ass when it happens, he showers my buttocks with the stuff."
                    show danny doggy squirt cum cumshot -speed with hpunch
                    "But even though he's pulled out, it's not like I stop feeling anything at all."
                    "In fact the sensation of him sliding out of me almost blows my mind."
                    show danny doggy down rolled
                    "My limbs go weak, and I sink down onto the floor, totally helpless."
                    $ danny.sub += 1
                else:
                    if hero.morality >= 25:
                        bree.say "Mmm..."
                        bree.say "D...Danny..."
                        bree.say "Don't pull out...please!"
                    elif hero.morality <= -25:
                        bree.say "D...don't you...dare pull out..."
                        bree.say "You stay in there...until...you...cum!"
                    else:
                        bree.say "K...keep going..."
                        bree.say "Don't...don't stop now!"
                    show danny doggy up with hpunch
                    "My pleas seem to have the desired effect on Danny, as I feel no change in his pace."
                    "He keeps right on going, ploughing into me with the same level of intensity and force."
                    show danny doggy ahegao rolled with hpunch
                    "And he doesn't stop until the very moment that he loses it."
                    "But when he does, it's not like I stop feeling anything at all."
                    show danny doggy squirt creampie -speed with hpunch
                    "In fact the sensation of him exploding inside of me almost blows my mind."
                    show danny doggy down rolled
                    "My limbs go weak, and I sink down onto the floor, totally helpless."
                    if not CONDOM:
                        $ danny.impregnate()
                    $ danny.love += 2
                $ hero.skills.pussy.value += 1
            "Fuck my ass" if hero.sexperience >= (sexperience_min + 5):
                if hero.morality >= -10:
                    $ hero.morality -= 1
                if hero.morality >= 25:
                    bree.say "Erm..."
                    bree.say "Could you maybe use the back-door?"
                elif hero.morality <= -25:
                    bree.say "What are you waiting for, Danny?"
                    bree.say "Stick it in my ass already!"
                else:
                    bree.say "Hmm..."
                    bree.say "I think I fancy it round the back tonight."
                "I feel Danny's grip on me tighten as soon as I'm done speaking."
                "And I can sense that this time he's all ready to go."
                "It's at times like this I'm reminded of just how strong Danny really is."
                "And by that I don't mean the kind of strength that comes from working out at the gym."
                "Because as Danny's grip tightens on me, I can feel that his strength comes from the way he lives his life."
                "The way he's a guy that lives on the edge and survives by his wits, that's what makes him so strong."
                "It also translates into the way that he makes love too, filling him with an eagerness and a passion."
                "I guess when you're living so dangerously, everything you can experience is deadly important."
                "Because you never know when fate is going to catch up to you, when the pleasure you're feeling might be your last."
                "Maybe that's why I feel myself shiver with anticipation when his cock slides between my thighs."
                "And it might also go a long way towards explaining what happens when he rubs the head between my buttocks too."
                "Normally I'd expect there to be at least a small measure of natural resistance before my body allowed him inside."
                "Even the smallest token to make him put in the effort."
                show danny doggy anal
                "But to my surprise, I feel the muscles down there begin to relax almost immediately."
                if hero.morality >= 25:
                    bree.say "Oh..."
                    bree.say "Oh my goodness!"
                elif hero.morality <= -25:
                    bree.say "Aah..."
                    bree.say "Oh fuck yeah!"
                else:
                    bree.say "Mmm..."
                    bree.say "Oh my god!"
                "Danny seems to take my words as encouragement, and begins to push harder as well as faster."
                "Which is more than okay with me, as it means that I get to feel him inching all the way into me."
                "I can't begin to describe the way that it feels as anything other than amazing and overwhelming."
                show danny doggy hurt rolled
                "But when he really begins to move a moment later, I feel like he's totally blowing my mind."
                "Before I was keen on keeping myself involved in dictating what's going on between us."
                "Yet now all I can do is lower my head and bite my lip, surrendering myself to the experience."
                "Each time Danny thrusts forwards, I feel like a jolt of electricity passes through my body."
                show danny doggy hurt rolled speed with hpunch
                "Looking down I can see my arms shaking from the force of it, and my breasts swinging too."
                "Danny's fingers are digging into the soft flesh of my waist s he grips me tighter."
                "Even though I feel like I've lost the ability to speak, I'm silently urging him on."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "And much to my delight, it feels as though Danny can sense what I'm thinking."
                "Because he somehow manages to suddenly kick things up another gear."
                "Before I was keeping quiet and just enjoying the feeling of being fucked."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "But now there's nothing I can do to keep myself from starting to cry out."
                "Pretty soon I'm moaning whenever Danny thrusts himself into me."
                "And then I'm left helplessly whimpering when he goes the other way."
                "All the time I'm doing everything I can to make him go harder and deeper."
                show danny doggy speed at startle(0.05,-10)
                pause 0.2
                show danny doggy -speed
                "I spread my legs, lower myself down and push backwards for all I'm worth."
                "Anything to add even a little more effect to what Danny's making me feel."
                danny.say "Urgh..."
                danny.say "You better be ready, [hero.name]..."
                danny.say "Cos I'm gonna cum!"
                "At the mere mention of Danny shooting his load, my eyes snap open."
                "Then my head shoots up as I come back to life, determined to take back control."
                call cum_reaction (danny, 'anal', sexperience_min) from _call_cum_reaction_274
                if _return == "anal_outside":
                    if hero.morality >= 25:
                        bree.say "Mmm..."
                        bree.say "D...Danny..."
                        bree.say "Pull out...please!"
                    elif hero.morality <= -25:
                        bree.say "D...don't you...dare cum in me..."
                        bree.say "You pull out of there...before...you...cum!"
                    else:
                        bree.say "P...pull out..."
                        bree.say "Don't...don't cum in me!"
                    show danny doggy up out -anal with hpunch
                    "My pleas seem to have the desired effect on Danny, as I feel him begin to pull out."
                    show danny doggy ahegao rolled with hpunch
                    "And he only just manages to do so before he loses it, shooting his load into the air."
                    show danny doggy squirt cum cumshot -speed with hpunch
                    "As his cock is bobbing over my ass when it happens, he showers my buttocks with the stuff."
                    "But even though he's pulled out, it's not like I stop feeling anything at all."
                    "In fact the sensation of him sliding out of me almost blows my mind."
                    show danny doggy down rolled
                    "My limbs go weak, and I sink down onto the floor, totally helpless."
                    $ danny.sub += 1
                else:
                    if hero.morality >= 25:
                        bree.say "Mmm..."
                        bree.say "D...Danny..."
                        bree.say "Don't pull out...please!"
                    elif hero.morality <= -25:
                        bree.say "D...don't you...dare pull out..."
                        bree.say "You stay in there...until...you...cum!"
                    else:
                        bree.say "K...keep going..."
                        bree.say "Don't...don't stop now!"
                    show danny doggy up with hpunch
                    "My pleas seem to have the desired effect on Danny, as I feel no change in his pace."
                    "He keeps right on going, ploughing into me with the same level of intensity and force."
                    show danny doggy ahegao rolled with hpunch
                    "And he doesn't stop until the very moment that he loses it."
                    show danny doggy squirt creampie -speed with hpunch
                    "But when he does, it's not like I stop feeling anything at all."
                    "In fact the sensation of him exploding inside of me almost blows my mind."
                    show danny doggy down rolled
                    "My limbs go weak, and I sink down onto the floor, totally helpless."
                    $ danny.sub += 1
                    $ danny.love += 2
                $ danny.flags.anal += 1
                $ hero.skills.ass.value += 1
    return

label danny_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom4
        show danny naked
        with fade
        menu:
            "You should leave":
                bree.say "I am done with you and I have to get up early tomorrow, you should leave."
                "The sex was beyond incredible."
                "Frowning a little, Danny straightens and shrugs, then goes to collect his clothes from where he'd let it fall earlier."
                hide danny with easeoutright
                "He then heads up the stairs."
                $ danny.love -= 1
                $ danny.sub += 1
                call sleep from _call_sleep_103
            "You should sleep here":
                bree.say "You can stay and sleep here."
                "I say, my voice a little shaky."
                "We curl up spooning together in bed, drifting toward sleep."
                $ danny.love += 1
                call sleep ("danny") from _call_sleep_104
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
