init python:
    Event(**{
    "name": "morgan_hottub_sex_male",
    "label": "morgan_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(morgan,
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
    "name": "fuck_morgan",
    "display_name": "Fuck",
    "label": "morgan_fuck_ROOM",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            ),
        PersonTarget(morgan,
            IsActive(),
            MinStat("love", 140),
            MinStat("sub", 40),
            MinStat("sexperience", 3),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })


label morgan_hottub_sex_male:
    $ CONDOM = False
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ game.active_date.clothes = "swimsuit"
    scene bg pool with fade
    "This is one of those occasions when everyone knows that there's something else going on."
    "Sure, I invited Morgan over so that we could take a dip in the hot-tub together."
    "That's what she agreed to and neither of us has added anything more to that since."
    "But I can tell from the look she gives me the moment that she arrives at my place."
    "We both know that we have the place to ourselves, so there's no chance of being caught."
    "And we both know that the real reason we're doing this is so that we can have sex in the tub."
    mike.say "Take your time, Morgan."
    mike.say "I'll just be waiting for you in the tub, okay?"
    show morgan swimsuit at left with easeinleft
    "No sooner have I said this and started to lower myself into the water, Morgan emerges from the house."
    show morgan swimsuit at center with ease
    "She doesn't even take the time to stop and let me get a look at her swimsuit."
    hide morgan
    show hottub morgan
    with fade
    "She just hurries towards the tub and clambers in as quickly as she can."
    if morgan.male <= 33:
        morgan.say "Ooh, I love the bubbles, [hero.name]!"
    elif morgan.male <= 66:
        morgan.say "Ah, I needed this, [hero.name]!"
    else:
        morgan.say "Oh yeah, nice and hot - just the way I like it, [hero.name]!"
    "I don't offer an answer to what Morgan has to say straight away."
    "Instead I find myself staring at the sight of her in that swimsuit."
    "It leaves nothing whatsoever to the imagination."
    "Which means my own imagination is free to think of all the things we could get up to!"
    morgan.say "Hey!"
    if morgan.male <= 33:
        morgan.say "What do you think you're looking at, [hero.name]?"
    elif morgan.male <= 66:
        morgan.say "You think I don't know what that look means, [hero.name]?"
    else:
        morgan.say "You like what you see, huh, [hero.name]?"
    "I can't help chuckling at this and shaking my head."
    mike.say "Wow, Morgan..."
    mike.say "I can't help it."
    mike.say "You look so good in that swimsuit!"
    "Morgan leans back against the edge of the tub, beginning to smile too."
    if morgan.male <= 33:
        morgan.say "Aww, that's sweet of you to say!"
    elif morgan.male <= 66:
        morgan.say "I thought so too!"
    else:
        morgan.say "You don't look too bad yourself!"
    morgan.say "Why don't you come over here and take closer look?"
    "I nod eagerly as I close in on Morgan, still grinning like a fool."
    "She licks her lips as I do so and slips down the straps of her swimsuit."
    "This action frees up her perfect, petite little breasts."
    "But more importantly, it makes my cock stiffen with alarming speed!"
    "I'm hard as diamond by the time I make it over to Morgan's side of the tub."
    "And she can't help but see it sticking out before me as I come to her."
    if morgan.male <= 33:
        morgan.say "Oh my!"
    elif morgan.male <= 66:
        morgan.say "Someone's ready to get down to business!"
    else:
        morgan.say "Yeah, that's right - bring it on!"
    "I stop Morgan's mouth with a deep and passionate kiss."
    "Not because I want to shut her up."
    "But rather because I can't resit her lips."
    "She doesn't offer any resistance of her own."
    "And kisses me back with an equal amount of desire on her part too."
    "I can feel Morgan's nipples stiffening as they rub against my chest."
    "At the same time she's yanking down my trunks to get at my cock."
    show hottub sex male morgan outside with fade
    "Soon enough she has them down and begins to take hold of it."
    call morgan_dick_reactions from _call_morgan_dick_reactions_1
    "I don't interfere, letting Morgan guide me home all on her own."
    "Only when I feel the slick sensation of her lips do I take any action."
    show hottub sex male morgan inside
    "Taking Morgan a little by surprise, I thrust forwards."
    "She yelps as the head of my cock pressed against the folds of her pussy."
    "And then she lets out a low moan as it pushes inside of her."
    if morgan.male <= 33:
        morgan.say "Oh...oh, [hero.name]!"
    elif morgan.male <= 66:
        morgan.say "Mmm...oh shit!"
    else:
        morgan.say "Oh yeah...that's what I'm talking about!"
    "I lift one of Morgan's legs out of the water and sling it over my shoulder."
    "This means that her muscles are stretched and I can sink deeper still."
    "And then I start to thrust in and out, using all of my leverage as I do so."
    "By now, Morgan seems to have lost the power of speech."
    "Instead she keep on making sounds that are almost animal in nature."
    "And I'm no different, grunting and sighing as I keep up the pace."
    "Morgan is still leaning back against the edge of the tub."
    "Her hands are hanging at her sides, her arms seemingly lifeless."
    "I can't help wondering if the only thing holding her up is my cock!"
    "I can certainly see that Morgan's in the process of zoning out."
    "Her mouth is starting to hang open and her eyes are rolling back into her head!"
    "For my own part, I'm finding the whole thing almost hypnotic too."
    "I can't tear my eyes away from her breasts as they move before me."
    "Small as they are, they're still jiggling in time with my thrusts!"
    "I reach out, taking hold of one in the palm of my hand."
    "And then I squeeze it, caressing the nipple between my finger and thumb."
    "At this, Morgan lets out a deeper moan than ever before."
    "I swear that I feel her tighten around the shaft of my cock."
    "It's like she's squeezing me back in return."
    "But I can't take the sensation of it."
    "And I start to cum..."
    menu:
        "Cum inside":
            "I could easily pull out of Morgan before it's too late."
            "But I'm still worried that she might tumble backwards."
            "And so I keep as tight a hold on her as I can until the end."
            show hottub sex male cumshot with vpunch
            $ morgan.love += 1
            "This means that I shoot my load inside of her."
            with vpunch
            "And the effect is quite something to see!"
            show hottub sex male ahegao with vpunch
            "Morgan squeezes her eyes closed and wails as I cum."
            "She reaches out, digging her fingers into my arms as she holds on for dear life!"
        "Pull out":
            "I make sure that I have a tight hold on Morgan as I make to pull out."
            "The last thing that I want is for her to go toppling over backwards and fall out of the tub!"
            show sexinserts chest morgan zorder 1 at center, zoomAt(1, (-140, 940))
            "She moans at the sensation of my cock sliding out of her."
            show sexinserts chest morgan cum
            show hottub sex male outside cumshot
            with vpunch
            $ morgan.sub += 1
            "But then I shoot my load up and onto her exposed chest."
            with vpunch
            "And the feeling of cum raining down on her skin is more than enough to distract her!"
            show hottub sex male outside -cumshot
            "Morgan makes little sounds that are more like growls than human cries."
            "And she holds onto me for dear life the whole time."
    hide hottub
    hide sexinserts
    show hottub morgan
    with fade
    "Afterwards, neither of us feels the need to speak as we sink down in the water."
    "Morgan rests her head on my chest, letting out a satisfied sigh as she does so."
    "I stroke her blue hair, twirling strands of it between my fingers."
    "And I'm feeling so relaxed that it's a battle to keep my eyes from closing."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ morgan.sexperience += 1
    $ game.active_date.clothes = None
    return

label morgan_fuck_date_nightclub:
label morgan_fuck_vip:
label morgan_fuck_restroom:
label morgan_fuck_nightclub:
    show morgan
    if renpy.seen_image("morgan cunnilingus restroom"):
        "The music in the nightclub is seriously doing it for me tonight."
        "The DJ's playing stuff from back when Morgan and I were in our teens."
        "And I can see it's having the same effect on her too."
        "Or it could also have something to do with how much we've both drunk."
        "Either way, we're having a pretty good time on the dance-floor."
        "Morgan can't seem to keep her hands off me for a second."
        "And the last thing I want is to let go of her too!"
        show morgan surprised
        morgan.say "Oh god..."
        morgan.say "I remember this song!"
        mike.say "Me too, Morgan."
        mike.say "It was everywhere that summer, yeah?"
        show morgan normal
        "Morgan nods her head at this."
        morgan.say "Oh man..."
        morgan.say "I used to..."
        show morgan blush
        "Suddenly I see Morgan's expression change."
        "She stops talking and her cheeks flush red."
        "All of which just makes me more interested in what she just remembered."
        mike.say "What is it, Morgan?"
        mike.say "What did you used to do?"
        "Morgan looks like she's not going to tell me what I want to know."
        "But then she turns to look me in the eye."
        "And I see a certain glint in there."
        if morgan.male >= 66:
            morgan.say "Ah..."
            morgan.say "What the hell!"
        elif morgan.male >= 33:
            morgan.say "I suppose I should tell you."
            morgan.say "Things are different between us now."
        else:
            morgan.say "Okay..."
            morgan.say "I'll tell you."
            morgan.say "But you have to be nice to me!"
        show morgan close
        "Morgan leans in close before she spills the beans."
        "Which obviously means she doesn't want anyone overhearing her."
        morgan.say "Back in the day..."
        morgan.say "I used to listen to this song when..."
        morgan.say "When I was...thinking about you!"
        morgan.say "I used to...touch myself!"
        show morgan -close
        "I stand back once Morgan's done."
        "And all I can do is blink in amazement."
        mike.say "Whoa..."
        mike.say "I'll never be able to hear this song without thinking about that again!"
        "Morgan's still blushing as I say this."
        "And she lets out a nervous giggle."
        show morgan blushhappy
        morgan.say "I..."
        morgan.say "I used to imagine it was you too."
        morgan.say "Imagine that it was you doing things to me!"
        "I let out a sigh, realising that my head's spinning a little."
        "The mere thought of Morgan doing something like that is SO hot!"
        show morgan blush
        morgan.say "Are..."
        morgan.say "Are you okay, [hero.name]?"
        mike.say "Yeah, Morgan..."
        mike.say "I'm just..."
        mike.say "Well...I'm just a little turned-on right now!"
        show morgan surprised
        "Morgan looks surprised by the admission."
        "But then she reaches out and takes hold of my hand."
        show morgan blushhappy
    morgan.say "You want to do something for me, [hero.name]?"
    morgan.say "You want to make one of my fantasies come true?"
    "Nodding eagerly, I let Morgan lead me off the dance-floor."
    "And I don't resist when I see her making for the bathroom either."
    scene bg restroom
    show morgan
    with fade
    "Once inside, she hustles me into one of the empty cubicles."
    "Then she slams the door and locks it tight."
    if renpy.seen_image("morgan cunnilingus restroom"):
        mike.say "Erm..."
        mike.say "Okay, Morgan..."
        mike.say "What exactly is it that you wanted me to do?"
        "By way of answer, Morgan smiles as she slips past me."
        "Then she stands in front of the toilet, hands on her waistband."
    show morgan bottomless with dissolve
    "Morgan boldly pulls down her panties, exposing herself."
    "Then she sits down on the lid, spreading her legs."
    if morgan.male >= 66:
        show morgan blushhappy
        morgan.say "I want you to lick me out, yeah?"
        morgan.say "I want your tongue down here!"
    elif morgan.male >= 33:
        morgan.say "I...I want you to give me oral, [hero.name]!"
        morgan.say "Right here and now!"
    else:
        show morgan blush
        morgan.say "C...can you use your tongue, [hero.name]?"
        morgan.say "You know...like, on me?"
    "I'm nodding even before Morgan's finished asking the question."
    "Of course I'm going to go down on her right now."
    if renpy.seen_image("morgan cunnilingus restroom"):
        "After what she just confessed to me, how could I say no?"
        "I mean, it'd be rude not to!"
        mike.say "I know it's too late now, Morgan."
        mike.say "But I SO wish I'd been able to do this back in the day."
        mike.say "So sit back, and let me make up for lost time, okay?"
        show bg restroom at zoomAt(2.5, (640, 720))
        show morgan a at zoomAt(2.5, (640, 720))
        "I'm down on my knees as I'm saying all of this."
        "And I'm looking up at Morgan as the same time."
        "She nods, biting her lip with anticipation in her eyes."
        "And I get the distinct impression she wants me to get on with it!"
    scene bg restroom at blur(16), dark with dissolve
    "So I lean in and close my eyes."
    "That done my other senses take over."
    "My nose fills with the musky scent of Morgan's pussy."
    "It tells me that she's already pretty excited."
    show morgan cunnilingus restroom bottomless embarrassed blush with dissolve
    "Something that's confirmed when I place my lips against hers."
    "The tip of my tongue touches them a moment later."
    "And I can taste the juices flowing down there."
    "This spurs me on, making me stick out my tongue."
    "I hear Morgan begin to whimper as I do so."
    "And that only serves to make me even bolder."
    show morgan cunnilingus mikemid closed -blush
    pause .4
    show morgan cunnilingus mikeup
    pause .4
    show morgan cunnilingus mikedown
    pause .4
    show morgan cunnilingus mikemid
    pause .4
    show morgan cunnilingus mikeup
    "My tongue begins to explore the folds around the edges."
    "I go around the whole thing, not skimping in any spot."
    show morgan cunnilingus mikedown pleasure
    pause .4
    show morgan cunnilingus mikemid
    pause .4
    show morgan cunnilingus mikeup
    pause .4
    show morgan cunnilingus mikedown
    pause .4
    show morgan cunnilingus mikemid
    pause .4
    show morgan cunnilingus mikeup
    "The whole time I can feel the effect this is having."
    "Morgan is twitching and twisting as she sits there."
    "And I hear the sound of her bracing herself against the sides of the cubicle."
    "All I can do is hope that nobody hears the sound."
    "Or that they just assume someone's having a serious session on the toilet in here!"
    "Already aware of how precarious our situation is, I push on hard."
    show morgan cunnilingus mikedown blush
    pause .4
    show morgan cunnilingus mikemid
    pause .4
    show morgan cunnilingus mikeup
    pause .4
    show morgan cunnilingus mikedown
    pause .4
    show morgan cunnilingus mikemid
    pause .4
    show morgan cunnilingus mikeup
    "Even so I don't let that affect the quality of my performance."
    "But I do start pushing my tongue deeper into Morgan's pussy."
    "Turning my head to get further in, I hear Morgan react."
    show morgan cunnilingus opened smile
    if morgan.male >= 66:
        morgan.say "Oh fuck yeah!"
        morgan.say "Lick me out - just like that!"
    elif morgan.male >= 33:
        morgan.say "Oh, [hero.name]..."
        morgan.say "I dreamed about this!"
    else:
        morgan.say "Ah..."
        morgan.say "Ah, [hero.name]..."
        morgan.say "You're so wicked!"
    "My mouth curls into a grin at the praise."
    "But I don't stop for even a moment."
    show morgan cunnilingus mikedown closed pleasure
    pause .2
    show morgan cunnilingus mikemid
    pause .2
    show morgan cunnilingus mikeup
    pause .2
    show morgan cunnilingus mikedown
    pause .2
    show morgan cunnilingus mikemid
    pause .2
    show morgan cunnilingus mikeup
    pause .2
    show morgan cunnilingus mikedown
    pause .2
    show morgan cunnilingus mikemid
    pause .2
    show morgan cunnilingus mikeup
    pause .2
    show morgan cunnilingus mikedown
    pause .2
    show morgan cunnilingus mikemid
    pause .2
    show morgan cunnilingus mikeup
    "Pushing my tongue deeper still, I bury myself between Morgan's thighs."
    "Her legs lifted up off the ground to let me get right in there."
    "I can feel her entire body beginning to quake and quiver."
    "And there's a distinct sense of relief that she's about to cum."
    $ morgan.love += 4
    if game.active_date:
        $ game.active_date.score += 20
    show morgan cunnilingus opened squirt mikedown
    "Morgan lets out a muffled wail of pleasure when it finally happens."
    "She has to bite down on her own hand, but it's still pretty damn loud!"
    "And I sit up, gasping for air as she does so."
    scene bg restroom
    show morgan
    with fade
    "As soon as she's able, Morgan grabs for her panties."
    "She pulls them on and stands up on wobbly legs."
    "Then we hurry out of the bathroom, trying to look innocent."
    "I just hope nobody really looks too closely at Morgan's smile."
    "Because it's a picture of erotic satisfaction right now!"
    return

label morgan_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg house
    show morgan
    with fade


    call morgan_fuck_date_intro_male (location) from _call_morgan_fuck_date_intro_male


    call morgan_dick_reactions from _call_morgan_dick_reactions


    call morgan_fuck_date_foreplay_male from _call_morgan_fuck_date_foreplay_male

    call handle_npc_leaving (morgan, _return, from_foreplay=True) from _call_handle_npc_leaving_16
    if _return:
        return




    call morgan_fuck_date_choices_male from _call_morgan_fuck_date_choices_male


    call handle_npc_leaving (morgan, _return) from _call_handle_npc_leaving_17
    if _return:
        return


    hide morgan
    call morgan_sleep_date_fuck (location) from _call_morgan_sleep_date_fuck
    return

label morgan_fuck_date_intro_male(location="hero"):
    if not morgan.sexperience:
        show morgan at center, zoomAt(1.0, (640, 720))
        "I'm still reeling from the series of revelations that have come from Morgan's unexpectedly walking back into my life all of a sudden."
        "Not so long ago, Morgan was a guy that I'd lost touch with, then all of a sudden he turned out to be a she."
        "As if that wasn't enough, I discovered that this female friend I never knew I had, always carried a torch for me."
        "The next thing I know, we're out on a date together, and things are going amazingly well."
        "So well, in fact, that we've already decided to skip the formalities and take it to another level."
        "I suppose that if I ever wanted proof positive that I was wrong about Morgan being a guy, this is the point where I get it!"
        "All of this seems so crazy, like one of those weird dreams that you're convinced are reality, for a while even after you wake up."
        "The counterpoint to the craziness is the fact that this new version of Morgan I'm getting to meet for the very first time is something else."
        "The Morgan I remember was a slight, awkward-looking guy that never seemed the least bit comfortable in his...I mean her, skin."
        show morgan b sadsmile
        "By way of contrast, the Morgan that I'm getting to know now is petite, elfin and moves with a grace that finally makes sense of her body."
        show morgan a flirt at center, traveling(1.5, 5.0, (640, 1040))
        "She's so cute and sexy that I honestly keep forgetting the person that I used to think she was."
        "I suppose tonight must have been pretty weird for her too."
        "I mean, she not only found out that I used to think she was a guy, but she's supposedly always had a thing for me too."
        "If I've felt the strain of wanting to discover the real her and also trying not to fall short of her expectations - imagine the pressure on her too!"
        "But in a way, maybe the two things have kind of balanced the whole thing out a bit?"
        "Maybe there being something making this a little weird for both of us means that we're trying that little bit harder?"
        hide morgan
        show morgan kiss
        with fade
        $ morgan.flags.kiss += 1
        "Either way, when we're standing on my doorstep and I invite her in, she's the one that pulls me in for a kiss."
        "The fact that I have to almost stoop down to kiss her back just makes it all the more spontaneous and exciting."
        "It's the first time I've been this close to Morgan, this intimate."
    else:
        hide morgan
        show morgan kiss
        with fade
        $ morgan.flags.kiss += 1
        "When we're standing on my doorstep and I invite her in, she's the one that pulls me in for a kiss."
        "The fact that I have to almost stoop down to kiss her back just makes it all the more spontaneous and exciting."
    if game.week_day % 3 == 0:
        "It's times like this when I really do have to take a couple of seconds out to pinch myself."
        hide morgan kiss
        show morgan at center, zoomAt(1.25, (640, 880))
        show bg livingroom
        with fade
        "Because I can't actually believe that I'm hurrying into the house and to my bedroom with Morgan."
        show bg bedroom1 with fade
        $ game.room = "bedroom1"
        "As if the revelation that my old friend was actually a majorly hot girl wasn't enough."
        "And on top of that the fact she'd always held a torch for me, even after so many years."
        "The thing that tops it all off is how I now get to date her and do all the other great stuff that comes along with it!"
        "All of which means I can't stop staring at Morgan with a big, dumb smile on my face."
        show morgan talkative
        if morgan.male >= 75:
            morgan.say "Whoa..."
            morgan.say "What the fuck's up?"
        elif morgan.male >= 25:
            morgan.say "Hey, [hero.name]…"
            morgan.say "What's up with you?"
        else:
            morgan.say "Oh, [hero.name]..."
            morgan.say "Are you feeling okay?"
        show morgan normal
        "I'm just closing my bedroom door behind us as Morgan asks the question."
        "And she kind of catches me by surprise, leaving me speechless for a moment."
        mike.say "Wha..."
        mike.say "What do you mean?"
        show morgan talkative
        if morgan.male >= 75:
            morgan.say "You've got a dumb look on your face."
            morgan.say "That's what I'm talking about!"
        elif morgan.male >= 25:
            morgan.say "That look on your face..."
            morgan.say "The one that makes you look like a big, dumb puppy."
            morgan.say "What's up with that?"
        else:
            morgan.say "You have a funny look on your face!"
        show morgan normal
        "I think about trying to play it cool and deny everything."
        "But then I remember how long it took for me to find out the truth about Morgan."
        "And I realise that I don't want to make the mistake of keeping things from her."
        "Juts in case it leads me back down the same kind of path as before."
        mike.say "It's being with you, Morgan."
        mike.say "That's what does it."
        mike.say "Sometimes I just can't believe all of this is happening."
        mike.say "That I'm getting to be with you like this, you know?"
        show morgan sadsmile
        "Morgan looks down at her feet for a moment."
        "And I can see that she's biting her lip."
        show morgan blush
        "Then she looks up at me, those big eyes full of genuine emotion."
        show morgan blushhappy
        if morgan.male >= 75:
            morgan.say "Ah..."
            morgan.say "I'm not good at all this mushy shit!"
            morgan.say "Let's just say...me too, and leave it at there."
        elif morgan.male >= 25:
            morgan.say "Y...you don't know how it feels, [hero.name]…"
            morgan.say "To hear you saying things like that about me."
            morgan.say "After all this time, I can't believe it either!"
        else:
            morgan.say "This is kind of scary..."
            morgan.say "When you talk about me like that..."
            morgan.say "I can hardly believe it either!"
        show morgan flirt
        "Neither of us seems to need to say another word."
        "Because the very next second we step close together."
        "Then we're wrapped in each other's arms."
        hide morgan
        show morgan kiss
        with fade
        $ morgan.flags.kiss += 1
        "And our lips are pressed together in a passionate kiss."
        "I don't know which one of us starts to undress the other first."
        "Or maybe we both start to do it at the same time."
        "But either way one item of clothing after another gets torn off."
        show morgan kiss naked with dissolve
        "And it doesn't take long before Morgan and I are both totally naked."
        "The sensation of her petite body pressed against mine was hot enough."
        "But now that I can feel the heat of her naked form against mine..."
        "Well, let's just say that nature is going to take it's course!"
        "Little by little I start to take move, walking Morgan towards the bed."
        "She seems to be going along with me, right up until we're a foot away from it."
        "It's then that I feel her twist in my arms, turning herself around."
        hide morgan kiss
        show morgan naked blush
        show bg bedroom1
        with fade
        "And the next thing I know, the kiss is broken."
    else:
        "The kiss is electric, thanks to the trepidation that we're both feeling at this moment in time."
        "And the sensation of her body against mine is something else."
        "Morgan's as slender as she is petite, her body almost all firm lines and slight curves."
        "I don't think there's a spare ounce of weight on her frame."
        "Breaking the kiss is next to impossible, but I so desperately want to peel off her clothes and see what lies beneath."
        hide morgan kiss
        show morgan
        show bg livingroom
        with fade
        "I hurriedly open the door and lead her into the living room."
        "We race down the stairs, neither of us speaking."
        show bg bedroom1 with fade
        $ game.room = "bedroom1"
        "Almost as soon as the door to my bedroom shuts behind us, I can't help myself."
        show morgan naked blush at center, zoomAt(1.5, (640, 1040)) with vpunch
        "Morgan yelps and laughs in surprise as I instantly begin to strip her clothes from her."
        "She does nothing to stop me, but I can see that she wasn't expecting me to be so bold."
        "I can't read her mind, only interpret her feelings from her expression and body-language."
        "But I hope that she's thrilled to be able to inspire such hopeless desire in me, especially after hiding that crush for so many years."
        "For my part, I simply can't wait to see her naked."
        "It's not that I still doubt her femininity, more that I've been so turned on by her that I want to see it as the culmination of my desire."
        hide morgan
        show morgan naked blush
        "Finally I step back a little and see what I've been longing to see."
        "Morgan stands before me, utterly naked now."
        show morgan naked flirt
        "She knows that she's on show, and she bites her lip in bashful amusement at the feeling."
        "All I can think is that she makes sense to me now, she makes so much sense where before she only caused me awkward confusion."
        "Her skin is smooth and pale, her limbs slender and yet feminine, breasts petite and in perfect scale."
    if not morgan.sexperience:
        mike.say "Morgan...you're...you're beautiful."
        mike.say "I feel like I know you...for the first time ever."
        "I feel like I'm babbling, just talking pure crap."
        "But she smiles up at me, stepping forward to begin pulling off my own clothes."
        morgan.say "Don't stop now - there's a whole lot more of me still to get to know!"
    return

label morgan_fuck_date_foreplay_male:
    if morgan.sub >= 50 or hero.sexperience >= 30:
        menu:
            "Have her suck you off" if morgan.sub >= 50:
                call morgan_fuck_date_blowjob from _call_morgan_fuck_date_blowjob
            "Give her some oral attention" if hero.sexperience >= 30:
                call morgan_fuck_date_cunnilingus from _call_morgan_fuck_date_cunnilingus
            "Fuck her":
                return
    call stop_all_sfx from _call_stop_all_sfx_29

    return _return

label morgan_fuck_date_choices_male:
    menu:
        "Standing" if hero.sexperience >= 15:
            call morgan_fuck_date_standing (15) from _call_morgan_fuck_date_standing
        "Doggy" if hero.sexperience >= 5:
            call morgan_fuck_date_doggy (5) from _call_morgan_fuck_date_doggy
        "Cowgirl" if hero.sexperience >= 10:
            call morgan_fuck_date_cowgirl (10) from _call_morgan_fuck_date_cowgirl
        "Missionary":
            call morgan_fuck_date_missionary (0) from _call_morgan_fuck_date_missionary
    call stop_all_sfx from _call_stop_all_sfx_30

    return _return

label morgan_fuck_date_blowjob:
    if game.week_day % 2 == 0:
        "Once she has me naked to the waist and begins to undo the front of my pants, Morgan slows her pace a little."
        "I can see her casting me fleeting glances as her hand pauses to massage my cock through the fabric."
        show morgan bj with fade
        "Quick as a flash, she's down on her knees before me, not even asking permission."
        "A moment later, Morgan has my rousing cock in one hand and is yanking down my pants with the other."
        if morgan.male >= 75:
            morgan.say "I...I like a cock, [hero.name]."
            morgan.say "I...I like to know how they taste before I put one inside of me."
            show morgan bj suck closed
            "Without any further explanation, Morgan wraps her lips around the head of my dick and begins to suck."
            "She's forceful, aggressive, and treats me to a blowjob the intensity of which I can't compare to anything I've experienced before."
            "Her fine cheekbones are standing out even more than normal as she takes yet more of me into her mouth."
            "I really want to savour this moment, but Morgan's so intense and focused that I fear, at this rate, I'll cum in a matter of mere seconds."
            mike.say "Morgan...oh god!"
            "My hands clasp the sides of her head."
            "But I don't know if it's to stop her or keep this from ending."
        elif morgan.male >= 25:
            morgan.say "I always dreamed about this moment, [hero.name]."
            morgan.say "The day that I'd finally get to put your cock in my mouth."
            show morgan bj suck
            "She goes slowly from there, drawing me into her mouth gently and carefully, as though she wants to linger over the moment."
            "This means that, for me too, it's slow and deliberate, every moment more enjoyable than the one before."
            show morgan bj closed
            "Though she's taking her time, I can soon feel just how good at this Morgan actually is."
            "I could cum at any moment, and looking down to see her huge blue eyes gazing back up at me only serves to make that all the more likely."
            "My hands are suddenly cupping Morgan's head, caressing her cheeks."
            "I'm running my fingers through her electric blue hair, almost still unable to believe that this is actually happening."
        else:
            morgan.say "Maybe I talk too much, huh?"
            morgan.say "Maybe this is what I should really use my mouth for!"
            show morgan bj suck closed
            "And with that, she slides her lips over the tip of my dick and proceeds to give me a truly amazing experience."
            "Morgan takes me in as deep as she can, showing an enthusiasm that takes me completely by surprise."
            "This side of her personality, seems to exist only to give me pleasure."
            "At times I swear that she can't be able to breathe even enough to keep from feeling discomfort, let alone the depth to which she's swallowed by cock."
            "But it's not like I have the time or space to worry about her, as I'm totally absorbed by the effects she's having on me."
            "A moment later I have Morgan's head held in my hands, enjoying the feel of her movements."
            "My hold is gentle, but I fear that it would become firm and forceful were she to show signs of ending this before I'm satisfied."
        "Suddenly I feel that I've reached the point where I need to either let myself go or else hold on for dear life."
        show morgan bj opened
        "I sense Morgan knows this as well as I do, as she catches my eye and seems to ask the question with no more than a raised eyebrow."
        menu:
            "Cum in her mouth":
                "I want to hold back and give her more, god knows that I do."
                "But the weight of all the revelations and fantastic things that I've discovered about Morgan are just too much for me."
                "I could never have imagined that we'd be here, together like this."
                "And she's already blown my mind, so should I really be surprised that she's blown me like this too?"
                show morgan bj creampie with vpunch
                "There's not even time to warn her that I'm cumming, but Morgan seems to understand simply from reading my face."
                show morgan bj closed with vpunch
                "She rides every moment of my climax, keeping everything that I have neatly concealed in her mouth."
                show morgan bj -creampie tongueout cum chub
                show sexinserts head morgan cum zorder 1
                "Slowly she allows my cock to slide out from between her slick lips, forming them into a smile as it slips away."
                "Morgan makes no effort to spit out what she's caught in her mouth, instead swallowing it smoothly."
                show sexinserts head morgan -cum zorder 1
                show morgan bj opened
                "All the time she looks at me with a satisfied, almost sleepy expression."
                if hero.fitness < 50:
                    $ morgan.love -= 10
                    return "leave_with_gain"
            "Don't cum in her mouth" if hero.fitness >= 50:
                "I have no idea just how I keep from cumming, right there and then in Morgan's mouth."
                "But somehow I manage to dig down deep and find the will to hold back."
                show morgan bj hard tongueout
                "She senses the fact that I've pulled myself back from the brink at the last moment, and releases me gently."
                "Morgan literally clambers backwards and onto the bed, spreading herself out so that she can take me as I climb after her."
    else:
        "I can tell from the moment we're fully naked that Morgan's on a mission."
        "She hardly seems to pause before she's dragging me towards the bed."
        "Her grip on my wrist is like iron and I can feel her tugging and pulling on my arm."
        "At one point I even think that she might get carried away and dislocate my shoulder!"
        "Any resistance that I put up doesn't appear to have an effect."
        "And so I resort to words instead of actions in the hope of getting Morgan's attention."
        mike.say "Whoa...whoa!"
        mike.say "Settle down, Morgan."
        mike.say "We're in the room where the magic happens."
        mike.say "There's no need to rush things, you know?"
        mike.say "You've got to let the magician show you his tricks!"
        "I know how corny that sounds even as it's coming out of my mouth."
        "It's all that I can think of in the heat of the moment."
        "But it seems to have the desired effect, as Morgan stops and looks back over her shoulder."
        morgan.say "Good thing I'm not lactose intolerant."
        show morgan annoyed
        morgan.say "Because that was one cheesy line!"
        "I almost open my mouth and point out that hers was just as bad."
        "But then I stop myself before I can squander the chance I've given myself."
        mike.say "I'm just wondering what's with the hurry, Morgan?"
        mike.say "Not that I'm against where it's going..."
        if morgan.male >= 70:
            "A filthy grin spreads across Morgan's face at the question."
            "And she surprises me by suddenly grabbing the front of my pants."
            morgan.say "I'll tell you what, [hero.name]."
            show morgan normal
            morgan.say "I want to suck your cock - that's what!"
            morgan.say "Unless you've got a problem with that?"
        elif morgan.male < 30:
            "Morgan blushes a little, cocking her head on one side."
            "She flutters her eyelids at me, looking suspiciously innocent."
            morgan.say "I just wondered if..."
            show morgan blush
            morgan.say "If your cock was feeling sore?"
            morgan.say "And if you wanted me to kiss it better?"
        else:
            "Morgan looks a little nervous at the question."
            "It's almost as if I've put her on the spot."
            "But she recovers pretty quickly, looking coy as she explains herself."
            morgan.say "I've been thinking about something all night."
            show morgan blush
            morgan.say "I...I'd like to suck your cock!"
            morgan.say "If that's okay with you?"
        "It takes a moment for what she's saying to actually sink in."
        "And then I find myself nodding eagerly and fumbling with my flies."
        mike.say "S...sure, Morgan!"
        mike.say "Sure thing - whatever you want!"
        "Morgan can't help smiling at the way I'm suddenly falling over myself."
        "But can you really blame me?"
        "She was trying to be spontaneous and here I am giving her the third degree!"
        "Of course I want her to go down on me - it'd be a dream come true."
        "Morgan reaches out to take my hand for a second time."
        "But now she doesn't have to pull me after her."
        "I lay down on the bed, flat on my back."
        "And in less than a minute, Morgan is laid on top of me."
        show morgan bj with fade
        "It's not like she needs to do much more than reach out and take hold of it."
        "My cock was already getting hard the moment she told me what she wanted!"
        "So by now it's as stiff as a board and pointing straight at her."
        "Morgan wastes no time in getting started, stroking the shaft with her hand."
        "She holds my eye as she leans in to begin kissing the base, just above my balls."
        "The look in that gaze is almost as much of a turn on as the feel of her lips."
        "I swear I can see all of the feelings that Morgan has for me in it."
        "All the time that I failed to see her for who she really was."
        "All of those years she waited in frustrated silence for me to realise my mistake."
        "I guess there's no way she's going to let me forget who she truly is now!"
        "Morgan traces a line up the underside of my cock with the tip of her tongue."
        show morgan bj hard tongueout
        "Her touch is so delicate and light that I can hardly feel it."
        "But the second that she reaches the head, it's like she pounces on me!"
        "It's inside of her mouth before I know it, she moves that fast."
        show morgan bj suck
        "And now her eyes are closed as she loses herself in the experience."
        "I hear myself gasping as the sensation of what she's doing overtakes me."
        "Morgan's head bobs up and down with ever more speed."
        "Which means that the intensity of the treatment she's giving me rises at the same time."
        "As I reach down and take hold of her head, my fingers twine in her hair."
        "Is she always this eager when it comes to using her mouth?"
        "Or is Morgan actually trying to make up for all the lost time between us?"
        "Either way she's making her point and putting me totally at her mercy."
        "And all I can think in the middle of it all is how long it took us to get here."
        "It was almost worth waiting for, the feeling is that good."
        "But part of me can't help thinking about all that I've missed out on."
        "The whole time that I was dumb enough to think Morgan was a guy."
        "There she was, holding in a desire for me that could inspire her to do this!"
        "Not for the first time, I feel like kicking myself."
        "I try ignore those thoughts and instead focus on the sensations I'm feeling."
        "And soon all that's on my mind is how Morgan's tongue and lips feel."
        "They're wrapped around my cock, working away like things possessed."
        "It's almost too much for me to take."
        "And I can already feel myself cumming..."
        menu:
            "Cum in her mouth":
                "I can't pull my cock out of Morgan's mouth before I shoot my load."
                show morgan bj closed
                "It's just so deep in there I'd only make it half way at best."
                "And so I let go, hoping that she's ready for it!"
                show morgan bj creampie with vpunch
                "Morgan's eyes pop open the moment that I do so."
                show morgan bj opened with vpunch
                "She makes a choking sound that I think is the first sign of things to come."
                with vpunch
                "But then she begins to swallow desperately, almost recovering her poise."
                show morgan bj -creampie tongueout cum chub
                show sexinserts head morgan cum zorder 1
                "Soon enough, she's back in control and enjoying the sensation."
                "Which means I can relax and watch as Morgan finishes the job."
                "She sucks and licks until the very last moment."
                show morgan bj -creampie tongueout -cum chub
                show sexinserts head morgan -cum zorder 1
                "And every drop she catches is gulped down almost greedily!"
            "Don't cum in her mouth":
                "I'm about to shoot my load in Morgan's mouth when a totally different urge overtakes me."
                "For some reason, I'm instantly taken with the idea of cumming in her face instead."
                "I can't say where the notion comes from, just that I'm intent on doing it."
                "Morgan gasps in surprise as I pull my cock out of her mouth with no warning."
                show morgan bj hard tongueout
                "But she has no more than a few seconds to look puzzled before I lose myself."
                with vpunch
                "The cum spatters straight into Morgan's face, striping her cheeks."
                with vpunch
                if morgan.male >= 70:
                    show sexinserts head morgan zorder 1
                    "She opens her mouth wide, trying to catch as much as possible."
                    show sexinserts head morgan cum zorder 1
                    "And I can see that she's laughing the whole time!"
                elif morgan.male < 30:
                    "Morgan lets out a yelp of surprise, shaking her head from side to side."
                    "But then she starts to giggle helplessly, as it runs down her face!"
                else:
                    show sexinserts head morgan zorder 1
                    "Though she seems shocked at first, Morgan soon recovers."
                    show sexinserts head morgan cum zorder 1
                    "And she even catches some of it in her mouth, licking her lips as she swallows it!"
    hide sexinserts
    return

label morgan_fuck_date_cunnilingus:
    if game.week_day % 2 == 0:
        "Now that Morgan's body is laid bare to me, I can't help being instantly drawn towards her pussy."
        "I know that's not exactly a rare thing for anyone presented with the naked body of a willing female partner."
        "But for me, Morgan's pussy is something that's assumed almost mythical proportions since the revelation that she was a girl."
        "It's the centre of her mystery and something that I want to explore as intimately as possible."
        "I push her down gently onto the bed, spreading her legs and lowering my head towards her exposed lips."
        "Morgan props herself up on her elbows, seemingly taken by surprise by my enthusiasm to go down upon her."
        if morgan.male >= 75:
            show morgan cunnilingus naked with fade
            morgan.say "Oh [hero.name]...yes please!"
            morgan.say "I...I mean...I like a man that gets straight to the point!"
            morgan.say "Make me scream, baby!"
            "I don't quite know what to make of the oddly raucous way that Morgan urges me on."
            "But it doesn't do anything to deter my efforts - quite the opposite in fact."
            show morgan cunnilingus pleasure mikemid
            "I use my thumbs to stroke the outer folds of her pussy, parting them yet further to allow my tongue to probe inside."
            "The familiar sour taste begins to hit my senses, and I feel the urge to push deeper into her almost immediately."
            show morgan cunnilingus closed
            "I might have taken more time and care over the whole thing if Morgan herself were not so forceful in her reactions."
            "But she's already crying out and gripping handfuls of the bedclothes in response to my attentions."
            show morgan cunnilingus opened blush mikeup
            "Suddenly I feel Morgan's legs wrap around me, as if she's trying to pull me up and onto her."
            morgan.say "That's enough teasing, [hero.name]."
            morgan.say "H...how about you fuck me for real, huh?"
        elif morgan.male >= 25:
            show morgan cunnilingus closed pleasure naked with fade
            morgan.say "Ahh...yes...please, [hero.name]!"
            "Morgan's pleas are not desperate as I go down on her, more that she's eager to be touched in this new and intimate manner."
            "Her pussy is small and perfectly neat, shaven smooth and so inviting to the eye I can hardly wait to begin."
            show morgan cunnilingus mikemid opened
            "I start by gently licking the outline of her tight folds, exploring them with the tip of my tongue."
            "Licking a pussy always reminded me of licking a battery and getting a little shock."
            show morgan cunnilingus closed
            "And Morgan is no exception, as I almost shudder at the sensation of her as I begin to go further inwards."
            "She's shuddering too, enjoying the feeling of my tongue travelling towards the centre of her pussy."
            "I'm trying as best I can to use every trick that I can think of to get her off."
            show morgan cunnilingus mikeup
            "I roll my tongue, turning it from a tube to a point and making sure that it's constantly moving."
            "At times it feels as though the tip must be something like a good two inches into Morgan's pussy."
            show morgan cunnilingus blush
            "My lips are pressed against the outer folds, and I can feel the beginnings of stubble upon her skin."
            morgan.say "[hero.name]...you're gonna...make me...cum!"
            morgan.say "Please...put it inside!"
        else:
            show morgan cunnilingus embarrassed naked with fade
            "Morgan giggles in a seductive and disarming manner."
            morgan.say "[hero.name]...are you really gonna lick my pussy?!?"
            "I look at Morgan with a quizzically raised eyebrow as I go down on her."
            show morgan cunnilingus mikemid
            "Experimentally, I lick her pussy from back to front, not probing deeply at first."
            morgan.say "Mmm...[hero.name], that feels so good!"
            "She continues to giggle and squirm as I get into the swing of things, and I can't say what she's doing isn't a turn on."
            show morgan cunnilingus closed pleasure
            "Soon her squeals and yelps are interspersed with genuine gasps and moans of pleasure."
            "I don't keep a mental record of my performances when it comes to giving oral, but this can't rank amongst my best efforts."
            "All the same, it doesn't seem to matter that much to Morgan, who by now is writhing and panting at my attentions."
            show morgan cunnilingus blush mikeup
            morgan.say "Oh, [hero.name]...oh, god!"
            morgan.say "I can feel your tongue inside of me!"
            morgan.say "Oh...oh, wow!"
            "I clamber atop of Morgan with the intention of fucking her in that moment."
            "Eager to see what the effect of putting something more substantial inside of her will be."
    else:
        show morgan blush
        "Although Morgan doesn't say anything at first, I know what her look means."
        "It's one of the loaded kind that a girl gives a guy when she has something to ask him."
        "Specifically when she has something to ask him that's more than a little awkward..."
        mike.say "Uhm..."
        mike.say "What's up, Morgan?"
        if morgan.male >= 75:
            morgan.say "Well..."
            show morgan normal
            morgan.say "I kinda want you to do something for me."
            morgan.say "I want you to go down on me."
        elif morgan.male >= 25:
            morgan.say "Oh, this is kind of embarrassing..."
            morgan.say "But would you...well..."
            morgan.say "Would you go down on me?"
        else:
            morgan.say "I...well...I..."
            morgan.say "Ah, hell - would you go down on me tonight?"
        "For a moment I'm not sure what to say."
        "Of course I don't have any issue going down on Morgan."
        "It'd be a pleasure to please her like that."
        "But then I remember the long and winding path that got us here."
        "Morgan must have spent years hung up on me while I thought she was a guy."
        "The least I can do for her now is to be sensitive to her needs as a way of making it up to her."
        mike.say "Sure thing, Morgan."
        mike.say "It's no big deal."
        mike.say "In fact, I'd love to!"
        "I see Morgan's cheeks flush red as she realises that I'm up for it."
        "And the sight makes me all the more eager to go through with my promise."
        morgan.say "It was..."
        show morgan normal
        morgan.say "Well, it was one of the things that I used to think about."
        morgan.say "Something I imagined when I was touching myself..."
        "Whoa..."
        "Wait a minute!"
        "Did she just admit that she used to masturbate over me?!?"
        "Now I can't wait to get down to it!"
        mike.say "Don't worry, Morgan."
        mike.say "I'll do my best."
        mike.say "I just hope I can live up to your imagination!"
        "Morgan says nothing in response, just biting her lip and waiting for my next move."
        "And so I take the initiative for the first time tonight, guiding her down onto the bed."
        "Once she's laid out before me, I lower myself atop her and gently part her thighs."
        show morgan cunnilingus naked with fade
        "I know that Morgan's watching my every move, and I can hear her breathing heavily."
        "In fact, part of me is sure that I can actually hear the sound of her heart, pounding in her chest!"
        "So that's why I start out slowly, just brushing the edges of Morgan's pussy."
        show morgan cunnilingus pleasure mikemid
        "All the same, she twitches and moans the second I do so."
        "Knowing that I could blow it by going at her too hard, I keep on with my plan."
        "Using just the tip of my tongue, I trace the lines of her folds."
        show morgan cunnilingus closed
        "It's not like I have to force myself either."
        "Morgan's pussy is like a work of art, neat and tight."
        show morgan cunnilingus opened blush mikeup
        "It practically begs to be explored with care and intimate attention."
        "And then there's the fact that she rewards my efforts too."
        show morgan cunnilingus mikemid closed -blush
        pause .4
        show morgan cunnilingus mikeup
        pause .4
        show morgan cunnilingus mikedown
        pause .4
        show morgan cunnilingus mikemid
        pause .4
        show morgan cunnilingus mikeup
        "Morgan moves slowly, with a languid motion as I begin to go deeper."
        "She never shifts enough to impede my progress, just writhing in pleasure."
        show morgan cunnilingus mikemid
        pause .4
        show morgan cunnilingus mikeup
        pause .4
        show morgan cunnilingus mikedown
        pause .4
        show morgan cunnilingus mikemid
        pause .4
        show morgan cunnilingus mikeup
        "And all that does is make me want to press on further, to give her even more."
        "When the moment comes for me to actually push my tongue inside, Morgan finally moves."
        show morgan cunnilingus mikemid closed
        pause .4
        show morgan cunnilingus mikeup
        pause .4
        show morgan cunnilingus mikedown
        pause .4
        show morgan cunnilingus mikemid
        pause .4
        show morgan cunnilingus mikeup
        "But even then, she simply succumbs to her urges and pushes her pussy into my face."
        "Luckily she only succeeds in pushing my tongue deeper, rather than smothering me!"
        show morgan cunnilingus mikedown closed pleasure
        pause .2
        show morgan cunnilingus mikemid
        pause .2
        show morgan cunnilingus mikeup
        pause .2
        show morgan cunnilingus mikedown
        pause .2
        show morgan cunnilingus mikemid
        pause .2
        show morgan cunnilingus mikeup
        pause .2
        show morgan cunnilingus mikedown
        pause .2
        show morgan cunnilingus mikemid
        pause .2
        show morgan cunnilingus mikeup
        pause .2
        show morgan cunnilingus mikedown
        pause .2
        show morgan cunnilingus mikemid
        pause .2
        show morgan cunnilingus mikeup
        "Never one to argue with a gift pussy in the mouth, I take full advantage."
        "Of course, this only serves to make Morgan all the more excited and animated."
        show morgan cunnilingus mikedown
        "By now it's all I can do to keep her down on the mattress as I struggle to keep going."
        "Every stroke of my tongue seems to make her buck and writhe all the more!"
        show morgan cunnilingus mikedown
        pause .2
        show morgan cunnilingus mikemid
        pause .2
        show morgan cunnilingus mikeup
        pause .2
        show morgan cunnilingus mikedown
        pause .2
        show morgan cunnilingus mikemid
        pause .2
        show morgan cunnilingus mikeup
        pause .2
        show morgan cunnilingus mikedown
        pause .2
        show morgan cunnilingus mikemid
        pause .2
        show morgan cunnilingus mikeup
        pause .2
        show morgan cunnilingus mikedown
        pause .2
        show morgan cunnilingus mikemid
        pause .2
        show morgan cunnilingus mikeup with vpunch
        "All it takes is one last push from me, reaching parts that I haven't touched before."
        "And then I can hear Morgan start to groan as the first throes of her orgasm take hold."
        show morgan cunnilingus mikedown
        pause .2
        show morgan cunnilingus mikemid
        pause .2
        show morgan cunnilingus mikeup
        pause .2
        show morgan cunnilingus mikedown
        pause .2
        show morgan cunnilingus mikemid
        pause .2
        show morgan cunnilingus mikeup
        pause .2
        show morgan cunnilingus mikedown
        pause .2
        show morgan cunnilingus mikemid
        pause .2
        show morgan cunnilingus mikeup
        pause .2
        show morgan cunnilingus mikedown
        pause .2
        show morgan cunnilingus mikemid
        pause .2
        show morgan cunnilingus mikeup with vpunch
        "But even now there's no chance to ease off with what I'm doing."
        "I need to keep right on, to make sure that Morgan reaches her peak."
        show morgan cunnilingus mikemid squirt with vpunch
        "Only when she's practically thrashing around do I take it that she's there."
        "Which means that I can start to slow down and guide her through the aftershocks."


































































































        "Afterwards I take the time to catch my breath and let Morgan recover."
        "She's still panting a little when she props herself up on her elbow."
        "And her normally pale cheeks are flushed with colour too."
        mike.say "Well?"
        mike.say "Did I live up to what you imagined?"
        morgan.say "No way - you were better!"
        if morgan.male >= 75:
            morgan.say "My imagination never made me cum that hard!"
        elif morgan.male >= 25:
            morgan.say "You're like a dream come true!"
        else:
            morgan.say "I could never have imagined how good you really are!"
        "I can't help smiling at her praise, blushing a little too."
        "I couldn't have imagined Morgan being better than she actually is either."
        $ morgan.love += 2
    return

label morgan_fuck_date_doggy(sexperience_min):
    "Clasping her hands together beneath her chin, she grins at my own approving smile."
    morgan.say "Okay, [hero.name] - how would you like me?"
    "For all that she's happy to let me call the shots, Morgan can still leave me almost speechless."
    "I reach up to tug at my collar, but then realise that I'm not even wearing one right now!"
    mike.say "Ah...on the bed, Morgan...on the bed."
    mike.say "On your hands and knees too!"
    "Morgan nods obediently as she turns towards the bed and starts to climb onto it."
    "She's following my instructions to the letter, doing exactly as she's been told."
    "And yet somehow, she still manages to make me feel like I'm the one being led by the nose!"
    "All I can do is follow in the wake of her pert little ass as it clambers up and waves from side to side before me."
    if morgan.male >= 70:
        "Even though she's the one that's being told what to do, I can still see the glimmer in Morgan's eyes."
        "She watches me with a smile as I climb onto the bed after her."
        "Looking like she's a little nervous, but determined to enjoy this every bit as much as I am."
        morgan.say "You...you better do me real hard, [hero.name]!"
        morgan.say "Doggy style means I want to be fucked...like...like a bitch!"
        "I respond to this in the only way that I makes sense to me."
        scene morgan doggy with fade
        "And that's to grab Morgan by the haunches, and pull her roughly backwards."
        "Morgan yelps in surprise and looks back over her shoulder at me."
        "Now her eyes are showing me an almost perfect cocktail of shock and anticipation."
        mike.say "Shut your mouth, unless you're going to use it to get me off!"
        mike.say "Who do you think you are?"
        mike.say "You're the one that's about to be fucked, not the one doing the fucking!"
        "I see Morgan quickly turn her head away to keep me from seeing her giggling."
        "She's almost licking her lips with the desire to see me make good on my threats."
        "And I hardly need any more motivation to press right on with them."
        "I squeeze her buttocks as though they were a pair of ripe fruits."
        "And then I slap them, one after the other, making Morgan squeal in genuine surprise."
        "By now I can feel that she's almost quaking with anticipation."
        "When my already stiff cock brushes between her buttocks, I can feel that she's more than ready."
        "All I need to do now is make my move, and there's nothing that she can do to resist me!"
        "Now that my cock is between Morgan's thighs, I face the first real dilemma of the night."
        "As she's demurely following my every order, it's down to me to decide where I go from here."
        "Both options are tempting, but in the end I know which one I want almost the second I really think about it..."
        menu:
            "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                "It's not every day that you find yourself in bed with a girl that's this willing to please."
                "And so in those exceptional circumstances, surely it'd be a waste of an opportunity to play it safe?"
                "The first thing that Morgan knows about my intentions is the feeling of something probing between her cheeks."
                "But the difference is that this time it's not teasing or trying to make her jump."
                show morgan doggy anal pleasure
                if persistent.xray:
                    show morgan doggy xray
                "No, this time I'm totally serious about wanting to take her up the ass!"
                morgan.say "Oh, my asshole!"
                morgan.say "I can feel it in my asshole!"
                "Morgan sounds surprised, but not alarmed or revolted by the sensation."
                "And the thought that she might actually be liking what I'm doing to her only spurs me on."
                "With a sudden thrust, I force the head of my cock past the ring of her sphincter."
                "I hear Morgan moan, and feel the intense grip of her muscles as they instinctively clamp down on me."
                "But for all of her unconscious efforts to close the way forward, it only makes me more determined."
                "I begin to move with a more regular pace and rhythm to my thrusts in and out of her."
                "At first all that happens is the clutching of her muscles becomes ever more intense."
                "But my cock has the whole of my body behind it, which is that much stronger than Morgan's ass alone."
                "Soon enough I can feel her muscles reaching their limits, and then they melt away in the fatigue of surrender."
                "As if they were a measure of her entire being, Morgan too seems to wilt and lose the will to fight."
                "Instead she becomes ever more placid and consumed by the sensations she's feeling with each second that passes."
                "By now, her ass is as unresisting and pliable as she is herself, and feels incredible around my cock."
                show morgan doggy tongueout
                "All I can hear from Morgan is the occasional sound of her moaning as she's used."
                "And all I can feel of her moving are the twitches that come from the conquered muscles of her ass."
                "I feel that, were I not making an effort to hold her up, she might collapse like a boneless jelly."
                "And so I keep on pushing myself into her with a more gentle rhythm."
                "Making sure that she feels everything until the very moment that I cum."
                call cum_reaction (morgan, 'anal', sexperience_min) from _call_cum_reaction_132
                if _return == 'anal_inside':
                    "Morgan's taken everything that I had to give her right up to this point."
                    "And so it seems unfair to pull out on her now and deny her that last sensation."
                    "So I keep right on letting her have everything that I have to give."
                    show morgan doggy creampie ahegao with hpunch
                    $ morgan.love += 1
                    "Morgan cries out, louder than ever before, the moment that I lose myself inside of her."
                    "And when I do loosen my grip on her afterwards, she takes mere seconds to drop to the bed, panting and gasping."
                elif _return == 'anal_outside':
                    "Call me evil if you like, but I'm curious as to just how far gone Morgan is right now."
                    "It feels like my cock and I are the only things holding her up at all."
                    "And so just before I actually cum, I decide to test this theory by pulling out."
                    show morgan doggy -anal normal
                    "My hunch proves to be right on the money, as she instantly collapses into a heap on the bed."
                    show morgan doggy cumshot with hpunch
                    "Morgan makes almost desperate panting and gasping sounds as I lose myself over her."
                    show morgan doggy -cumshot dickcum cum onbody pleasure
                    $ morgan.sub += 5
                    "Streamers of warm semen streak her back, buttocks and thighs."
                    "But if she feels it at all, she shows no outward sign."
                $ morgan.flags.anal += 1
            "Fuck her pussy":
                call check_condom_usage (morgan) from _call_check_condom_usage_87
                if _return == False:
                    return
                "I push the head of my cock a little further between Morgan's cheeks."
                "She jumps a little, squealing again in that very pleasant manner."
                "And with that sound still fresh in my ears, I get ready to make good on all of my threats."
                "There's no question that I want to be inside of Morgan's tight little pussy right now."
                show morgan doggy vaginal pleasure
                if persistent.xray:
                    show morgan doggy xray
                if CONDOM:
                    show morgan doggy condom
                "So I don't hesitate to pull her backwards and push the head of my cock against her slick lips."
                "Though she makes a couple of almost desperate yelping sounds at the sudden sensation, there's no sign of a fight."
                "Morgan's pussy betrays her true feelings too, letting me slip inside with only a token show of resistance."
                "In almost one smooth motion, I'm into her and as deep as I can possibly go."
                "I see Morgan look back over her shoulder at me, her mouth opening as if she's about to speak."
                "An impulse takes hold of me at that moment, and I suddenly thrust myself deeper into her again."
                "Instantly the words that Morgan was trying to form are turned into an almost animal groan."
                "She looks at me with a helplessness that only serves to make the sensation of thrusting all the more enjoyable."
                "Of course, this makes me wait for her to recover, and to try to speak for a second time."
                "Another thrust into her produces almost the exact same result, and renews the thrill that I feel from it too."
                "And from then on, it becomes almost like a game to me."
                "Whenever Morgan seems to be making an effort to speak or express herself in any way, I thrust as deep into her as possible."
                "I find myself taking an ever more perverse delight in forcing her to remain mute."
                "It feels like I'm almost making her behave like an animal, rather than a human being."
                "Indeed, Morgan herself seems to be taking on more of an animalistic air as time goes on."
                show morgan doggy tongueout
                "Soon she stops trying to speak at all, and satisfies herself with sounds of pleasure."
                "I can see her grabbing handfuls of the bedclothes at the same time, gripping on as if for dear life."
                "She tosses her head, making her electric blue hair fly around like the plumage of some exotic creature."
                "By now I'm beginning to feel as though I'm becoming more animal than man myself."
                "It's getting harder and harder to think of anything but being inside Morgan and how it feels."
                "The game I've been playing at her expense seems to have consumed me too."
                "And soon I can't hold back from giving all that I can, and that means going all the way!"
                call cum_reaction (morgan, 'vaginal', sexperience_min) from _call_cum_reaction_133
                if _return == "vaginal_outside":
                    "At the very last moment possible, my sex-addled brain suddenly recalls how to remember important shit."
                    "Almost without a conscious thought as to what's at stake, I push Morgan forwards."
                    show morgan doggy -vaginal normal
                    "In the same movement, I also drag my cock out of her in one go."
                    with hpunch
                    "Without me to support her, Morgan instantly collapses onto the bed in a heap of limbs."
                    show morgan doggy cumshot pleasure with hpunch
                    "I land on my ass just behind her, cumming at the same time."
                    show morgan doggy -cumshot dickcum cum onbody with hpunch
                    $ morgan.sub += 1
                    "Streamers of warm semen streak her back, buttocks and thighs."
                    "But if she feels it at all, she shows no outward sign."
                elif _return == "vaginal_condom":
                    "It's right about now that I'm very much thankful to have worn a condom."
                    "I don't know if I could have dragged my head back into being able to think straight."
                    "But as it is, I can just keep right on going until the very end."
                    show morgan doggy creampie with hpunch
                    $ morgan.love += 1
                    "I lose myself and turn that sensation into one final push."
                    with hpunch
                    "And the sound that Morgan makes in response is the most animalistic yet."
                    with hpunch
                    "Almost as soon as I'm done, she slides off of my cock and onto the bed before me."
                elif _return == "vaginal_inside_pill":
                    "We may be fucking like a couple of animals right now, but part of my brain is still awake."
                    "And somehow it manages to make me vaguely aware of the fact that Morgan's on the pill right now."
                    "Silently thanking the still human part of me for this information, I keep on going to the end."
                    show morgan doggy creampie ahegao with hpunch
                    $ morgan.love += 2
                    "I cum a moment later in one final push."
                    with hpunch
                    "The sound Morgan makes is the most animalistic yet."
                    with hpunch
                    "And as soon as I'm done, she slides off of me and onto the bed in exhausted silence."
                elif _return == "vaginal_inside_pregnant":
                    "I'd like to think that the reason I keep right on going until I lose myself inside Morgan is obvious enough."
                    "All the while we've been having sex, I've felt the weight of her belly in each and every thrust."
                    "But the truth is that I'm too far gone to be sure that I'm not just caught up in the moment!"
                    show morgan doggy creampie ahegao with hpunch
                    $ morgan.love += 2
                    "Either way, I fill Morgan when I'm at the deepest point I can reach inside of her."
                    with hpunch
                    "She sags as if stunned by the sensation, lowing almost like a cow."
                    with hpunch
                    "I hold her as she folds up and sinks onto the bed, supporting the weight of her belly the whole time."
                elif _return == "vaginal_inside_mad":
                    "If I'm really the one getting to make all of the choices tonight, then that's just what I'll do!"
                    "I'm having far too good of a time to even think about stopping now."
                    "And Morgan gave up her right to say no when she put me in the driving seat."
                    show morgan doggy creampie with hpunch
                    $ morgan.impregnate()
                    $ morgan.love -= 5
                    "Taking full advantage of just how out of it she is, I lose myself deep inside of her."
                    with hpunch
                    "It's only as she's coming down and beginning to regain her senses afterwards that Morgan realises what's happened."
                    "She doesn't say anything, but all the same, I can still hear her base, animal moans turning into the sound of human sobbing..."
                elif _return == "vaginal_inside_happy":
                    "At the very last moment possible, my sex-addled brain suddenly recalls how to remember important shit."
                    "Almost without a conscious thought as to what's at stake, I try to pull out of Morgan."
                    "But then I feel her grab my wrist and hold on with an almost preternatural strength."
                    "She makes sounds then, almost incoherent grunts that vaguely sound like someone pleading against the action I'm trying to take."
                    show morgan doggy creampie ahegao with hpunch
                    $ morgan.impregnate()
                    $ morgan.love += 5
                    "More thrown and confused than moved to do as she asks, I lose myself a moment later."
                    with hpunch
                    "She sags as if stunned by the sensation, lowing almost like a cow."
                    with hpunch
                    "And then she collapses onto the bed, making deep, satisfied sounds that could never be mistaken for actual words."
    elif morgan.male < 30:
        "Morgan practically scuttles onto the bed, looking back over her shoulder as she goes."
        "On her face is an expression of mixed anticipation and actual trepidation."
        "But still she does as she's told and makes no move to disobey a single word that I've said."
        "As I climb up behind her, I can see that she's biting her lip as she waits in silence."
        "Of course, this only serves to make me all the more wolfish as I climb up behind her."
        "And I begin to make low, almost growling noises as I get close enough to touch her."
        "Morgan keeps stealing furtive glances back at me, her head then quickly turning away."
        "The whole thing begins to feel a hell of a lot like a game of cat and mouse."
        "Her waiting with baited breath, and me trying to pick the exact moment to pounce."
        "When I do finally make my move, it's only to clap my hands upon Morgan's thighs."
        "But she's gotten herself so tense by now that she yelps out loud and leaps forwards a whole foot!"
        scene morgan doggy with fade
        "Not wanting to let her get away, I follow her, tightening my grip on her haunches at the same time."
        "Morgan makes a little wailing sound as I drag her backwards, but doesn't try to resist."
        "By the time I have her where I want her, I can hear her panting."
        "Her heart must be pounding in her chest by now, and the thought makes me want her all the more."
        "Going more slowly now, so as to savour the moment, I pull Morgan back."
        "This time I don't stop until her buttocks are pressed firmly against my groin."
        "Morgan tries to leap forward again almost as soon as she feels my cock between her legs."
        "But this time I have a firm hold of her, and she's going nowhere but where I let her!"
        "She realises this soon enough, and any sign of her struggling ceases."
        "It seems that she's accepted the fact that I'm the one in charge here."
        "And that I'm free to do with her as I like..."
        "It's not lost on me that I could probably get away with doing pretty much anything to her right now."
        "So do I go with my gut and take her in a way that I know I'll enjoy?"
        "Or should I go with something more adventurous, as I don't know when I'll have a chance like this again?"
        menu:
            "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                "But then how can I look myself in the face if I pass up this opportunity?"
                "And what does it say to Morgan if I don't?"
                "What does it say if I put her in her place and then just do her like any other time?"
                "No, I started this one way and I need to finish it up in the same manner too."
                "That's why I reach down and part Morgan's buttocks, exposing her tight, pink asshole."
                show morgan doggy anal
                if persistent.xray:
                    show morgan doggy xray
                morgan.say "Oooh, [hero.name]!"
                morgan.say "What are you doing?"
                morgan.say "You know that's my ass, right?!?"
                "I don't even dignify that with an answer, or pause for a moment."
                "Instead I slowly push the head of my cock into her sphincter."
                show morgan doggy pleasure
                morgan.say "Ahhh..."
                "I can feel the muscles of Morgan's ass as they instinctively try to push me out."
                "But I keep right on going, not stopping until I have at least half of my cock inside of her."
                morgan.say "Mmmm..."
                morgan.say "Ahhh...[hero.name]!"
                "The sound of Morgan taking my cock up her ass and the sensations of it set each other off to perfection."
                "She does nothing but take what I have to give her without protest."
                "As if the surrender of her muscles in her ass makes the rest of her body do the same."
                show morgan doggy tongueout
                "Right now I feel like I'm the unquestioned master of Morgan's mind and body alike!"
                "She only seems to move in response to me as I thrust in and out of her."
                "And the only sounds that she makes are those inspired by the feel of my cock inside her."
                "I keep on, pounding away at Morgan's ass for as long as I can manage."
                "And I enjoy every single moment of it, right up until I can feel myself cumming..."
                call cum_reaction (morgan, 'anal', sexperience_min) from _call_cum_reaction_134
                if _return == 'anal_inside':
                    "As I'm the one running this show, I don't see any reason to ask for Morgan's permission."
                    "And likewise, there's no real consequences for doing it either."
                    show morgan doggy creampie ahegao with hpunch
                    $ morgan.love += 2
                    "So that's why I decide to keep on thrusting into her ass as I cum."
                    with hpunch
                    "The volume of her cries increases as I fill her."
                    with hpunch
                    "And I can feel the muscles of her ass quivering around my cock."
                    "Once it's over and I'm spent, Morgan buries her head in the pillows and keels over sideways."
                elif _return == 'anal_outside':
                    "There's no sense of mercy in my deciding to pull out of Morgan's ass the moment before I cum."
                    "It's more that I want to feel the sensation of whipping it free and see her reaction to the same."
                    show morgan doggy -anal normal
                    "And she doesn't disappoint me in that, as I feel my cock squeezed and feel her quake from it leaving her body."
                    show morgan doggy cumshot with hpunch
                    "Morgan gasps as it pops out of her ass, and then yelps as I cum all over her naked back."
                    show morgan doggy -cumshot dickcum cum onbody pleasure with hpunch
                    $ morgan.sub += 2
                    "Strings of warm semen stripe her buttocks too, running down her thighs and dripping onto the sheets."
                    with hpunch
                    "I watch all of this as I collapse onto my own ass, panting and gasping almost as much as Morgan herself."
                $ morgan.flags.anal += 1
            "Fuck her pussy":
                call check_condom_usage (morgan) from _call_check_condom_usage_88
                if _return == False:
                    return
                show morgan doggy
                if CONDOM:
                    show morgan doggy condom
                "Just because I have Morgan completely at my mercy right now, that doesn't mean I have to go crazy."
                "I mean, I want to enjoy this as well as getting off on the fact I'm in charge, don't I?"
                "And so that's why I resist the all too real temptation to take her up the ass."
                "Instead I pull Morgan firmly onto my cock, feeling the sensation of her slick lips against the tip."
                morgan.say "Oooh...you feel so BIG!"
                morgan.say "I hope there's room inside of me for that..."
                show morgan doggy vaginal pleasure
                if persistent.xray:
                    show morgan doggy xray
                morgan.say "Ahhh..."
                "Morgan's words are cut off as I suddenly thrust myself inside her pussy."
                "Already wet in anticipation of this very moment, she yields without much of a struggle."
                "With the second push, I'm all the way into her and enjoying the feeling of her around my cock."
                "By now, all that Morgan can hope to use her mouth for is to make moans and groans."
                "The fine mixture of pain and pleasure in those sounds is more than enough to spur me on."
                "But combined with the way she feels, it makes me want to dominate her all the more."
                show morgan doggy tongueout
                "That's why I keep a tight hold on Morgan, holding her up while I pound away."
                "I fear that if I were to loosen my grip on her just a little, she might actually collapse!"
                "But if she wants to pass out, then she can do that on her own time."
                "And she can at least wait until I've managed to cum!"
                "All the same, I can feel Morgan's limbs starting to shake."
                "If she's getting that weak from taking all I have to give her, I might just end up supporting her anyway!"
                "Not knowing if I have the strength for that myself, I make one final effort to push on to the end."
                "I'm not going to be denied the chance to cum if I can help it."
                "And maybe I'll be able to drag Morgan along with me into the bargain."
                call cum_reaction (morgan, 'vaginal', sexperience_min) from _call_cum_reaction_135
                if _return == "vaginal_outside":
                    "I can't hold Morgan up any longer, and I can't cum inside of her either."
                    "So the only course of action open to me is pulling myself out before it's too late."
                    show morgan doggy -vaginal normal
                    "We both gasp as I do this, and I feel as dizzy as she looks once I'm free."
                    show morgan doggy cumshot with hpunch
                    "Morgan only manages to stay upright for as long as it takes me to cum over her trembling back."
                    show morgan doggy -cumshot dickcum cum onbody pleasure with hpunch
                    $ morgan.sub += 1
                    "And as soon as the semen spatters down on her exposed skin, her legs and arms buckle all at once."
                    with hpunch
                    "With nothing to support her any longer, she collapses into a heap on the bed."
                elif _return == "vaginal_condom":
                    "Even as I'm losing myself, I can already feel Morgan going limp in my hands."
                    show morgan doggy creampie with hpunch
                    $ morgan.love += 1
                    "I struggle to hold her up, cumming at the same time."
                    with hpunch
                    "The combination of my climax and taking almost all of her weight makes me gasp with the effort."
                    with hpunch
                    "I can feel my head becoming light and dizziness setting in."
                    "But the sensation of it all makes the struggle worthwhile."
                    "Only after I've let it all go inside of her do I finally let go of Morgan."
                    "With nothing to support her any longer, she collapses into a heap on the bed."
                elif _return == "vaginal_inside_pill":
                    "Just as I'm wondering whether I should keep going or pull out, I remember something important."
                    "I can just keep on going, as Morgan's on the pill right now!"
                    "Using the last of my energy, I push into her one last time."
                    show morgan doggy creampie ahegao with hpunch
                    $ morgan.love += 2
                    "And then I lose myself, filling her in the same act."
                    with hpunch
                    "Only after I've let it all go inside of her do I finally let go of Morgan."
                    with hpunch
                    "With nothing to support her any longer, she collapses into a heap on the bed."
                elif _return == "vaginal_inside_pregnant":
                    "I don't have to worry for a moment about pulling out of Morgan before I cum."
                    "Not when her pregnant belly is as visibly swollen as it is right now!"
                    "The weight of it adds to the sensation of every thrust that I make into her."
                    "And I can't help wondering if it's all that's keeping her upright too!"
                    show morgan doggy creampie ahegao with hpunch
                    $ morgan.love += 2
                    "But then I lose myself, and fill Morgan a second later."
                    with hpunch
                    "My job done, I can finally let go and allow her to collapse onto the bed."
                    with hpunch
                    "Morgan rolls onto her side before me, cradling her belly with both arms."
                elif _return == "vaginal_inside_mad":
                    "When I feel Morgan trying to wriggle off of me before I cum, I can't help smiling at the sensation."
                    mike.say "Oh no, you're not going anywhere."
                    mike.say "Not without my saying so!"
                    "I grab a handful of Morgan's electric blue hair, yanking her head backwards as I do so."
                    show morgan doggy creampie with hpunch
                    $ morgan.impregnate()
                    $ morgan.love -= 5
                    "She lets out a pathetic little wail with every thrust I make into her as I cum."
                    with hpunch
                    "And afterwards, when I let go of her hair and she collapses onto the bed, she begins to sob quietly to herself."
                elif _return == "vaginal_inside_happy":
                    "As much as I like being the one in charge, I can't justify cumming inside of Morgan without protection."
                    "But as I make to pull out, I see her looking back over her shoulder, desperately shaking her head."
                    morgan.say "No...please...[hero.name]."
                    morgan.say "Cum...in...me!"
                    "I've been calling the shots up to this point, but somehow she manages to turn it around, right there and then."
                    "This means that she's called probably the most important shot of the night."
                    show morgan doggy creampie ahegao with hpunch
                    $ morgan.impregnate()
                    $ morgan.love += 5
                    "And so it goes off right inside of her!"
                    with hpunch
                    "I lose it mere seconds later, filling Morgan with all that I have left in me."
                    with hpunch
                    "Completely spent, I let go of her and she slumps onto the bed."
                    "Morgan rolls onto her side before me, smiling as she rolls into a ball, protectively clutching her belly."
    else:
        "Morgan all but hops onto the bed at my command, landing on all fours and prancing like a cat."
        "While she adopts the position I told her to, she's sure to shake her backside and pout her lips as she does so."
        "What she's doing is not so much a show of defiance."
        "But more a reminder that she's more than up for what I have in mind to do to her!"
        "All of this means that I end up jumping onto the bed after her."
        "And then jumping onto Morgan in turn, hearing the bedframe creak under my weight."
        "Morgan laughs approvingly as she feels me grabbing hold of her from behind."
        "She makes no effort to stop me, accepting without question that I'm the one in charge here."
        "But the enthusiasm that she's showing me is far more of a turn-on than any faked resistance could hope to be."
        "And just how playful she's being makes me want to do the same in return."
        scene morgan doggy with fade
        "Teasing her with the head of my cock, I start to push it between her open thighs."
        "But I'm still careful to keep it from actually sneaking inside of her before I'm ready."
        "I hear Morgan gasp in surprise as she feels me stroking the lips of her pussy."
        "And the she giggles infectiously as I rub myself between her buttocks a second later."
        morgan.say "You wanna come in?"
        morgan.say "Then you're gonna have to make up your mind!"
        morgan.say "Which hole is it gonna be, huh?"
        "I try not to chuckle at Morgan's baiting of me with her words."
        "I really want to laugh out loud, but that would ruin the image of me being the one calling the shots."
        "So instead I take a firmer hold of her and make my presence felt with a little more force than before."
        mike.say "I'll make my choice when I'm good and ready."
        mike.say "And that's the first you'll know about it!"
        "But all the same, she has got a point."
        "She's kneeling there, ready and willing to go."
        "And here I am, still dithering over where I want to stick it!"
        "Now I honestly feel like I'm the one in charge around here."
        "Morgan's laid wide open and at the mercy of anything that I choose to do to her."
        "I take a quick look at the choices before me, and I know exactly what I want from her..."
        menu:
            "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                "Smiling to myself, I suddenly think of the perfect way to pay Morgan back for her impudence."
                show morgan doggy anal pleasure
                if persistent.xray:
                    show morgan doggy xray
                "And so, parting her buttocks, I push the head of my cock a little way into her exposed asshole."
                morgan.say "Aaah..."
                morgan.say "What are you..."
                "Her words melt away into mere sound as I push myself slowly into her."
                "Though Morgan's sphincter naturally tries to resist, I press on and enter her all the same."
                "Almost instantly I can feel that the effort was worth it."
                "The muscles of her ass clamp down on the shaft of my cock instantly."
                "And the sensation is like the best hand-job that I can imagine and the tightest pussy, all rolled into one."
                "I hold myself still once I'm in as far as I can go, feeling her muscles strain and then surrender."
                "And from there it feels simply amazing, as I begin to move in and out of her."
                "Morgan's ass seems to quiver and quake with every movement that I make."
                "But the rest of her body soon picks up on this, and she starts to move in sympathy."
                "It's as though her ass has taken over from her brain, and everything follows its lead."
                show morgan doggy tongueout
                "Morgan glances back over her shoulder at me, her eyes wide and her mouth hanging open."
                "There's almost a look of disbelief on her face as she does so."
                "As though she simply can't believe I'm taking her up the ass."
                "And on top of that, she can't believe how much she's panting and squirming from it either!"
                "Any hint of the cheekiness and mischief that were in her before now are well and truly gone."
                "Behind the surprise on her face is a deeper expression, one that all but admits utter defeat."
                "Whatever defiance was left inside of Morgan has been well and truly extinguished."
                "The feeling of my cock in her ass, almost pinning her to the bed has seen to that."
                "All she can do now is stay right there on her hands and knees and take it."
                "And from the feeling that's rising inside of me right now, she's not going to have to wait all that long!"
                call cum_reaction (morgan, 'anal', sexperience_min) from _call_cum_reaction_136
                if _return == 'anal_inside':
                    show morgan doggy creampie with hpunch
                    $ morgan.love += 1
                    "When I lose myself, buried deep in Morgan's ass, she stays as still as a statue."
                    "The subtle trembling of her body is all that betrays that she's alive and awake."
                    "She takes everything that I have to give, as deep as I can get it."
                    "Morgan doesn't cry out once, just bites her lip and endures."
                    "Afterwards she flops down onto the bed, slithering off of my now slack cock."
                    "But still she doesn't say a thing, only lays there, panting and exhausted."
                elif _return == 'anal_outside':
                    "Call me a little cruel if you like, but I want to see just how far gone Morgan is right now."
                    show morgan doggy -anal cumshot with hpunch
                    "And so I pull my cock out of her ass moments before I cum."
                    show morgan doggy -cumshot dickcum cum onbody with hpunch
                    $ morgan.sub += 3
                    "Morgan moans in protest, and then lowers her head as strings of white semen streak her back."
                    with hpunch
                    "She manages to stay upright, shaking and quivering, until I've shot my entire load over her."
                    "When I'm done she flops down onto the bed, my cum dripping off of her."
                    "She doesn't say a thing the whole time, only lays there in silence, panting and exhausted."
                $ morgan.flags.anal += 1
            "Fuck her pussy":
                call check_condom_usage (morgan) from _call_check_condom_usage_89
                if _return == False:
                    return
                show morgan doggy
                if CONDOM:
                    show morgan doggy condom
                "Sometimes the best course of action is the most familiar."
                show morgan doggy vaginal pleasure
                if persistent.xray:
                    show morgan doggy xray
                "That's why I take a firm hold of Morgan and push myself straight into her pussy."
                "I think she was expecting something more unusual or complicated from me."
                "As she makes a yelping sound that I'd have thought more in keeping with being taken up the ass."
                "But all the same, it doesn't take long for her initial surprise to subside."
                "And when it does, I'm already well into my stride and enjoying the sensation of fucking her."
                "I think it's in Japan that they say 'sometimes the soul just wants Udon'."
                "Well, sometimes the cock just wants pussy!"
                "And from the way she begins to moan and sigh as I thrust in and out of her."
                "I'd definitely say that Morgan's pussy just wants cock right now too!"
                "And it proves to be hungry for all that I can give it too."
                "At one point, I even begin to wonder if I might have over faced myself here."
                show morgan doggy tongueout
                "No matter how much effort I put into it, Morgan takes all I can give and still seems to want more."
                "But rather than admit defeat, I put all that I have left into redoubling my efforts."
                "Ever so slowly, a little at a time, I feel myself catching up to her."
                "Soon I'm keeping a better pace with Morgan, no longer afraid of her leaving me behind."
                "Now I want to reign her in, remind her of just who's in charge."
                "Maybe even punish her a little for her disobedience just now..."
                "I push into her a bit harder than before, enjoying the way it makes her moan."
                "Another push earns me another moan, and makes me keep on going."
                "And it's these sudden, almost violent thrusts that see me through to the end."
                "Each one making Morgan cry out just a little louder and me come a little closer to losing it."
                "I think she actually starts to cum a second before me, taking me with her as she goes..."
                call cum_reaction (morgan, 'vaginal', sexperience_min) from _call_cum_reaction_137
                if _return == "vaginal_outside":
                    show morgan doggy -vaginal normal
                    "I don't know how I manage to pull my cock out of Morgan in time to avoid an accident taking place."
                    "Perhaps some unconscious instinct or fear of becoming a parent just asserts itself and takes over."
                    "But whatever the reason, I hear Morgan moan in disappointment as she feels my cock pulled out of her."
                    show morgan doggy cumshot with hpunch
                    "She has almost no time to complain, however, as I cum in the next second."
                    show morgan doggy -cumshot dickcum cum onbody pleasure with hpunch
                    $ morgan.sub += 1
                    "Ribbons of warm semen stripe her back and buttocks, running down her sides and thighs."
                    with hpunch
                    "I see all of this as I land on my backside, panting and sighing with exhaustion."
                elif _return == "vaginal_condom":
                    show morgan doggy creampie with hpunch
                    $ morgan.love += 1
                    "It's all I can do to remember that I wore a condom as I lose myself inside of Morgan."
                    with hpunch
                    "She rides every moment of my orgasm, as if trying to absorb as much as she possibly can."
                    with hpunch
                    "All I can do is hang on for dear life and enjoy the sensations that are flooding me."
                    "Afterwards, we both collapse onto the bed, no one able to move, let alone speak."
                    "All I can do is lie there, waiting for my heart to stop pounding in my ears and the room to stop spinning above me."
                elif _return == "vaginal_inside_pill":
                    "Morgan shakes her head at the very first sign of me trying to pull out."
                    morgan.say "Don't stop..."
                    morgan.say "Pill...remember?!?"
                    "I don't have time to nod, as I cum almost as soon as she says this."
                    show morgan doggy creampie ahegao with hpunch
                    $ morgan.love += 2
                    "I lose myself deep inside of Morgan, hearing her gasp in delight."
                    with hpunch
                    "After it's all over and done with, we topple over onto the bed, neither of us able to move or speak."
                elif _return == "vaginal_inside_pregnant":
                    "How could I forget that Morgan's carrying our baby?"
                    "Especially when I've been feeling the weight of her belly this whole time!"
                    "It adds to the sensations that I experience when making love to her."
                    show morgan doggy creampie ahegao with hpunch
                    $ morgan.love += 2
                    "And it anchors me as I lose myself inside of her too."
                    with hpunch
                    "When Morgan collapses onto the bed, I support her the entire way."
                    "And then we lie together, exhausted as I stroke it lazily."
                elif _return == "vaginal_inside_mad":
                    show morgan doggy creampie normal -tongueout with hpunch
                    $ morgan.impregnate()
                    $ morgan.love -= 25
                    "Morgan feels the full and unadulterated force of my orgasm as I lose myself inside of her."
                    "There'll be consequences later, but for the moment we're both lost in it and nothing else matters."
                    "All that I can hear is my own hoarse panting for breath and the sound of Morgan moaning as she cums in turn."
                    hide morgan
                    show bg bedroom1
                    show morgan naked angry
                    with hpunch
                    morgan.say "Ah...ah...aaah, fuck!"
                    with hpunch
                    "Morgan's words are almost indistinguishable from the gasps she makes as I thrust into her."
                    morgan.say "You...you came in me...you stupid bastard!"
                    morgan.say "You came inside of me without a damn rubber!"
                elif _return == "vaginal_inside_happy":
                    "Almost as soon as I try to pull out, I feel Morgan trying to wriggle backward to stop me."
                    morgan.say "No...please..."
                    morgan.say "Don't stop..."
                    "I have no time to ask what Morgan means or why she wants me to do that."
                    show morgan doggy creampie ahegao with hpunch
                    $ morgan.impregnate()
                    $ morgan.love += 5
                    "I cum mere moments after she speaks, filling her with all that I have."
                    with hpunch
                    "We collapse together afterwards, into a mess of sweaty limbs."
                    "But while Morgan has a smile on her face, I still can't make sense of what just happened."
    return

label morgan_fuck_date_cowgirl(sexperience_min):
    "Morgan scrambles onto the bed backwards, beckoning for me to come to her with an urgent wave of her hands."
    "But then it's not like I need a whole lot of encouragement to do just that!"
    if morgan.male >= 70:
        "By the moment that I land next to her, thinking to climb straight on top, she catches me by complete surprise."
        "I don't know how she does it, but somehow Morgan uses my weight and momentum against me as I land."
        "One second she's under me, and then she's managed to flip me over so that I land on my back, gasping and disoriented."
        scene morgan reverse cowgirl
        with fade
        "I wonder where she could have gone, but then I feel her climbing atop me and almost pinning me down to the bed as she looks back over her shoulder at me."
        morgan.say "Not so fast, [hero.name]."
        morgan.say "I...I call going on top!"
        "Still more than a little stunned at her speed and aggression, I nod hastily in response."
        mike.say "S...sure...sure thing, Morgan."
        mike.say "If that's what you want..."
        "I'd like to think that a lot of my confusion is also thanks to her sitting atop me right now."
        "That and the fact that she's been stroking my quickly stiffening cock the whole time too..."
        morgan.say "Good - because it is, yeah it is."
        morgan.say "I want you to fuck me, good and hard...yeah?"
        morgan.say "Can you do that for me, [hero.name]?"
        "I nod hastily, my cock feeling painfully erect by now and making me gasp as she suddenly squeezes the shaft."
        morgan.say "Then what are you waiting for, huh?"
        morgan.say "Are you going to fuck me, or what?"
        mike.say "Yeah...okay...gimmie a chance already!"
        "Morgan laughs at my flustered tones, showing me that she's playing around."
        "Which is at least something of a relief as I struggle to do as I'm told."
        "Truth is I'm more turned-on by what she's doing than riled up."
        "And I want to get down to business almost as much as she does!"
        "By now I can feel the hot, moist sensation that's been building between Morgan's legs this whole time."
        "I guess that I have no more than a couple of seconds in which to decide just where this is going."
        "And I'm guessing that the fact she's not already made that clear to me, means Morgan's happy to leave that decision up to me..."
        menu:
            "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                "I'm not normally one to beat a path straight to a girl's ass in a situation like this."
                "But there's just something about how forwards and aggressive Morgan's being tonight."
                "It's not like I'm annoyed or that she's challenging my masculinity - I'm not that pathetic, I hope!"
                "More like she's throwing down the gauntlet and I'm just bending down to pick it up."
                "That's why I don't feel the need to ask for permission, and just go for it."
                show morgan reverse cowgirl anal pleasure
                $ morgan.sub += 1
                "Making sure my dick's at just the right angle for entry, I pull Morgan down onto me."
                "As the muscles of her sphincter instinctively tighten, she lets out a sudden yelp of surprise and shock."
                morgan.say "H...hey..."
                morgan.say "Wha..what are you doing to me?!?"
                "That said, I notice that she's making no serious effort to move her ass out of the way or get off of me."
                "So I choose to interpret her words more as a challenge than an instruction to stop."
                mike.say "You said you wanted me to fuck you, Morgan."
                mike.say "You didn't say how!"
                "I give her another firm yank downwards, burying the head of my cock in her ass."
                "From there I don't stop again until it's almost halfway buried inside of her."
                "Morgan casts her head back and let's out a deep, throaty moan as gravity takes over."
                "And then she sinks down the rest of the way, surrendering to the sensations that are coursing through her body."
                "She stops making any effort to struggle, her resistance melting away as she sit there on my cock."
                "Slowly and steadily, I begin to move inside of her."
                "Morgan doesn't show any sign of feeling it at first, remaining still and silent."
                show morgan reverse cowgirl pleasure
                "But then her moaning begins again, and she leans back onto my chest to support herself."
                "Its weird to watch her go from her usual assertive self to this quiet, almost passive state."
                "Morgan rides my thighs slowly and with what looks like infinite feeling."
                "Her eyes are closed the entire time, and I don't think I've ever seen her look more beautiful."
                "In the end, I guess she must have managed to cast a spell over me too."
                "As I feel myself getting close to cumming without warning or hope of stopping!"
                call cum_reaction (morgan, 'anal', sexperience_min) from _call_cum_reaction_138
                if _return == 'anal_inside':
                    show morgan reverse cowgirl cum with vpunch
                    "I don't want to break that spell either, and as there's no danger to it, I keep right on going."
                    with vpunch
                    "This means that Morgan's got me as deep inside of her as possible at the moment I cum."
                    with vpunch
                    "Only now do her eyes finally open and sounds start to come from her lips again."
                    morgan.say "Oh shit...I can feel you!"
                    morgan.say "Feel you...cumming in my ass!"
                    "Morgan rides me until the very last, before collapsing across me and slithering over my sweat-soaked body."
                    $ morgan.love += 1
                elif _return == 'anal_outside':
                    show morgan cowgirl -anal
                    "It takes almost all of my remaining strength to do it."
                    "But somehow I manage to pull my cock out of Morgan's ass in time."
                    "It emerges with an almost comical popping sound, bobbing up before her."
                    show sexinserts chest morgan zorder 1
                    show sexinserts belly morgan as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    show morgan reverse cowgirl cum
                    with vpunch
                    "She has only a couple of seconds to look surprised before I cum."
                    show sexinserts chest morgan cum zorder 1
                    show sexinserts belly morgan cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    with vpunch
                    "And the streamers of hot semen are instantly spattered up over her stomach and breasts."
                    "I lie back, gasping in exhaustion and watching the cum run down over Morgan's body."
                    $ morgan.sub += 5
                $ morgan.flags.anal += 1
            "Fuck her pussy":
                call check_condom_usage (morgan) from _call_check_condom_usage_90
                if _return == False:
                    return
                "I can already feel just how slick the lips of Morgan's pussy have gotten with every move my cock makes."
                "So it seems a no-brainer to just push a little harder and angle myself a little higher, until..."
                morgan.say "Oh, hello down there!"
                morgan.say "Looks like someone wants to come inside..."
                show morgan reverse cowgirl vaginal



                "Her words trail off as she actually feels my cock pushing it's way into the folds of her pussy."
                "She might be in the mood for playful banter of that kind, sure enough."
                "But right now, my cock is all business!"
                "Soon the only sounds that are coming out of Morgan's mouth are moans and sighs, almost grunts too."
                "I don't stop pushing into her until I can feel my balls pressing against her buttocks."
                "While I hold myself there, she keeps on groaning, leaning back against my chest for support."
                "My own hands are by now clamped firmly upon her waist, holding her in place."
                "At the same time I begin to thrust upwards, making her ride me so that she sways in sympathy to my movements."
                show morgan reverse cowgirl vaginal pleasure
                "And soon Morgan starts to react to this more intense and overwhelming pace herself."
                "Each and every thrust seems to shake a little more of the smug amusement from her face as she looks back over her shoulder at me."
                "In the end she can't keep from throwing her head back and almost yelping like a scalded dog."
                "But my redoubled efforts haven't only taken their toll on Morgan."
                "And suddenly I can feel the irresistible urge to cum rising inside of me too..."
                call cum_reaction (morgan, 'vaginal', sexperience_min) from _call_cum_reaction_139
                if _return == "vaginal_outside":
                    "My hurry to get my cock inside of Morgan is coming back to haunt me right now."
                    "It means that I have to be even quicker to pull it out of her before the end comes!"
                    "Serves me right for giving in and going for instant gratification, I guess."
                    "Morgan herself seems far too wrapped up in the moment to have even remembered."
                    "This means that I have to use my grip on her waist to half lift her off of me and then squirm out from underneath."
                    show sexinserts belly morgan zorder 1 at center, zoomAt(1, (-140, 970))
                    show morgan reverse cowgirl -vaginal
                    "Her surprise means that she hinders, rather than helps, delaying me by a vital couple of seconds."
                    show sexinserts belly morgan cum zorder 1 at center, zoomAt(1, (-140, 970))
                    show morgan reverse cowgirl cum
                    with vpunch
                    "The upshot of this is that she literally gets an shot over her stomach as I finally cum."
                    with vpunch
                    "Eyes and mouth all wide open in shock, Morgan feels the warm cum running down the length of her belly."
                    $ morgan.sub += 1
                elif _return == "vaginal_condom":
                    "It's now that I'm really thankful that I chose to wear the condom."
                    "As it means that I can just keep on going, not break my stride and ruin the moment for the both of us."
                    with vpunch
                    "Morgan takes every last ounce of effort that I can put into it when I cum."
                    with vpunch
                    "I can see and feel her arms quiver and quake as she follows me a moment later."
                    "Her head hangs down, forwards and away from me, her blue hair obscuring most of her face."
                    "All I can see is her lips, as they shape silent gasps and grimaces."
                    "And then, still silent, it's all over."
                    $ morgan.love += 1
                elif _return == "vaginal_inside_pill":
                    "I can feel myself beginning to panic as I realise I'm not wearing a condom."
                    "Morgan, on the other hand, seems blissfully unaware of the approaching danger."
                    "I'm about to warn her and try to pull out, but she beats me to the punch."
                    morgan.say "What's the matter, dummy - you forget I'm on the pill?"
                    "Of course she is - how could I forget a thing like that?!?"
                    show morgan reverse cowgirl cum with vpunch
                    "Unfortunately, this brainwave has used up all the time I had left, and I cum a mere moment later."
                    with vpunch
                    "The intensity of the orgasm takes me by surprise, and I keep hold of Morgan like I'm clinging on for dear life."
                    with vpunch
                    "More prepared for the tumult, she rides it out like a pro."
                    "When we're both finished, she's panting, but I sound like I'm close to death!"
                    $ morgan.love += 2
                elif _return == "vaginal_inside_pregnant":
                    "I don't need to be reminded of the fact that it's okay to keep right on going to the end."
                    "After all, I've had Morgan's swollen little belly pressed against my thighs the whole time."
                    "It stands out so much against her otherwise petite frame, making her look almost ready to burst."
                    "Truth be told, I love the feeling of its weight and it makes me want her all the more whenever I see it."
                    show morgan reverse cowgirl cum with vpunch
                    "And though Morgan doesn't burst just yet, I do a moment later, filling her as I cum."
                    with vpunch
                    "She lowers herself onto me backwards as she begins to shake from her own orgasm which follows."
                    "Her increased weight feels oddly comforting as she lays atop me back to stomach, still quivering with the aftershocks of her climax."
                    $ morgan.love += 2
                elif _return == "vaginal_inside_mad":
                    show morgan reverse cowgirl cum with vpunch
                    "I can feel myself letting go and filling Morgan in almost the same moment that I remember I'm not wearing a condom."
                    with vpunch
                    "Morgan herself starts to try to get free a second later, but by then it's too late!"
                    morgan.say "[hero.name]...what are you..."
                    morgan.say "Get it out of me, you stupid bastard!"
                    morgan.say "I'm serious - you can't..."
                    $ morgan.impregnate()
                    "Her hands are balled into fists and I'm sure that she's actually going to hit me."
                    "But then I can see in her eyes that she's noted the horror in mine."
                    "Morgan lowers her fists, but still keeps on swearing and cursing under her breath."
                    "Thankfully, I think it's dawned on her that we both just screwed up, and not just me!"
                    $ morgan.love -= 10
                elif _return == "vaginal_inside_happy":
                    "Remembering that I'm not wearing a condom, I begin to make an effort to pull out in good time."
                    "But the very moment that I do, Morgan pins my legs to the bed with her hands, shaking her head."
                    morgan.say "Oh no, you're not cutting out on me this late into the game!"
                    mike.say "But, Morgan - I'm not wearing a..."
                    "She cuts me off before I have the chance to say the actual word."
                    morgan.say "Like I care!"
                    morgan.say "I want it all, [hero.name] - start to finish!"
                    show morgan reverse cowgirl cum ahegao with vpunch
                    "Before I can say another word, I lose it, filling her with everything that I have to give."
                    with vpunch
                    "Morgan's face lights up as she pushes all of her weight down on me, making sure I'm in her as deep as possible."
                    $ morgan.impregnate()
                    with vpunch
                    "She offers me no sane explanation as to just why she wants me to cum inside of her like this."
                    "But she seems delighted with the fact that I have!"
                    $ morgan.love += 5
    elif morgan.male < 30:
        "Morgan quails a little, showing that she's more nervous than she wants to let on."
        "But she doesn't try to clamber off of the bed and run."
        "I'm pretty sure she's not actually afraid of what I want to do to her."
        "But all the same she has that deer in the headlights look on her face right now."
        "Which isn't really an issue, as I'd gladly eat venison knowing it used to be Bambie!"
        "I practically grapple Morgan once I'm on the bed, rolling her over as I grab her."
        scene morgan reverse cowgirl
        with fade
        "She squeals in alarm, and sways wildly as she comes up on top of me from the tussle and with her back to me."
        morgan.say "Oooh, [hero.name]..."
        morgan.say "You made my head spin!"
        "I can't help smiling at Morgan as she tries to shake her brains back into some semblance of order."
        "Another girl might be complaining at the way I just manhandled her."
        "But she just seems to take it in her stride."
        mike.say "Just you wait, Morgan."
        mike.say "It's gonna be spinning a whole lot more before I'm done with you!"
        "Morgan's eyes go wide at this statement, and she begins to giggle uncontrollably."
        morgan.say "Naughty!"
        "I'm rewarded for my impudence with a gentle slap on the thigh."
        "That and the sight of Morgan blushing at the thought of what I have in store for her."
        "But then her face shows genuine surprise and almost shock as she feels my cock pressing against her for the first time."
        "I see Morgan bite her lip, for all of her girly innocence, as she imagines what's coming next."
        "Which in turn reminds me that I haven't exactly decided what's next either!"
        "I guess this is it - decision time!"
        "Morgan's never going to be more ready than she is right now."
        "And I'm pretty sure that she's also completely at my mercy too..."
        menu:
            "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                "I kind of feel guilty about taking advantage of how much Morgan seems to be letting me take the lead here."
                "But a wicked little part of me just can't help wanting to show her where being so passive can land her."
                "And that's why I pull her down onto me while angling my dick in just such a way..."
                show morgan reverse cowgirl anal pleasure
                morgan.say "Oooh...oh shit!"
                morgan.say "[hero.name]...you missed!"
                morgan.say "Isn't that the wrong hole?"
                "She wriggles and writhes as she sinks down onto my cock."
                "And all this does is quicken the process."
                morgan.say "Aah...aah!"
                morgan.say "I can feel it inside of me!"
                "Putting on my best attempt at innocence and concern, I pretend to come to her aid."
                mike.say "Geez, Morgan - I'm sorry."
                mike.say "I don't know how it could have happened!"
                "I clap my hands on Morgan's thighs, trying to look like I want to pull out of her ass."
                "But in reality, all I'm actually doing is holding her down while I push even deeper into her than before."
                morgan.say "Wha...what...what are you doing?!?"
                morgan.say "That's just making it worse!"
                mike.say "I'm sorry...it won't..."
                mike.say "Oh no, you don't think it's, I don't know...stuck up there, do you?"
                morgan.say "Well, now I do!"
                show morgan reverse cowgirl pleasure
                "As insensitive as it sounds, I have to try pretty hard to keep from cumming."
                "She continues to moan and struggle while I'm fucking her."
                "Her enthusiasm growing with each moment that passes."
                morgan.say "Oooh...what's happening now?"
                morgan.say "[hero.name], are you about to cum?!?"
                call cum_reaction (morgan, 'anal', sexperience_min) from _call_cum_reaction_140
                if _return == 'anal_inside':
                    "Oh, so now she notices what's going on down there!"
                    "And my guess is that she's going to feel this too..."
                    show morgan reverse cowgirl cum with vpunch
                    "A second later I can feel myself losing it, shooting my load into Morgan."
                    "By now I've dropped any pretence of trying to get her off of my cock."
                    with vpunch
                    "My hands are firmly holding her in place as my hips thrust as deep as possible into her."
                    show morgan reverse cowgirl cum ahegao with vpunch
                    "Morgan responds by crying out, eyes wide in genuine surprise at the sensation."
                    "It's lucky for me that she's too wrapped up what's happening to get mad about it too!"
                    $ morgan.love += 3
                elif _return == 'anal_outside':
                    show morgan cowgirl -anal
                    show sexinserts chest morgan zorder 1
                    show sexinserts belly morgan as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    "Deciding to keep up the pretence that my cock ended up in Morgan's ass by sheer accident, I make to pull out of her."
                    "All the time, she's waving her hands, urging me to hurry up and extricate myself from her back-passage."
                    "I'm not all that concerned about the fact I'm doing so, as I seem to have thought one step ahead of Morgan here."
                    "I don't know just what she thought was going to happen the moment that I whipped my dick out of her."
                    show morgan reverse cowgirl cum with vpunch
                    "But the wailing she makes and the way she desperately tries to shield her face a moment later tells me it wasn't to have me basically cum in her face."
                    show sexinserts chest morgan cum zorder 1
                    with vpunch
                    "Ribbons of warm semen shoot upwards, spattering Morgan's breasts, as well as the side of her face where it's not protected."
                    show sexinserts belly morgan cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    with vpunch
                    "She makes constant sounds of disgust as she tries to shakes the sticky mess off of her."
                    "And call me cruel, but I can't help laughing out loud at her predicament."
                    $ morgan.sub += 2
                $ morgan.flags.anal += 1
            "Fuck her pussy":
                call check_condom_usage (morgan) from _call_check_condom_usage_91
                if _return == False:
                    return
                "Morgan's basically putting her fate in my hands right now."
                "And that means I can't take advantage of her without it playing on my conscience."
                show morgan reverse cowgirl
                "Which means that I choose to pull her gently down and onto my cock pretty much where she's already pressing against me."
                show morgan reverse cowgirl vaginal pleasure



                "Morgan moans a little as the lips of her pussy are forced apart and the head of my dick enters her."
                "I deliberately take it slow, enjoying the way that what she's feeling is written all over her face."
                "Morgan has her hands pressed flat against my thighs, still fending off the last of her apparent dizziness."
                "But now she suddenly takes a firm hold of them, as if afraid of being pulled away from me."
                show morgan reverse cowgirl pleasure
                morgan.say "Oh, [hero.name] - you were telling the truth."
                morgan.say "You really are making my head spin!"
                "Morgan smiles sweetly over her shoulder, pouting her lips each and every time I push into her from below."
                "I keep my pace gentle to begin with, enjoying the sight of what it's doing to her."
                "But as Morgan starts to show ever more signs of her pleasure intensifying, I slowly start to speed up."
                morgan.say "Mmm...that feels amazing."
                morgan.say "How do you know to make it feel just like I wanted it to?"
                morgan.say "It's so good - I feel like I'm melting inside!"
                "I don't know if Morgan's being genuine, or just trying to give my ego a rub."
                "But either way, the effect that her words have on me is the same."
                "And soon I'm doing all that I can to make sure she keeps on telling me how much she's loving it."
                "All the time, her face is a picture of ecstasy, eyes closed and lips pouting as she gasps for breath."
                morgan.say "You feel so good inside of me, [hero.name]."
                morgan.say "So good that I wish we could do this forever!"
                "I can't even begin to argue with Morgan on that particular point."
                "Right now I'd probably make the same wish myself."
                "But the reality is that I can already feel that I'm about to cum..."
                call cum_reaction (morgan, 'vaginal', sexperience_min) from _call_cum_reaction_141
                if _return == "vaginal_outside":
                    "Judging by the state that she's worked herself into, I doubt if Morgan even recalls I'm not wearing a condom."
                    "That means it falls to me to make sure I don't get caught out and cause an accident that we'll both regret!"
                    "But when I try to pull out, Morgan fights me for a moment, proving that she has forgotten after all."
                    "I hate to have to do it, but what choice do I really have?"
                    show morgan reverse cowgirl -vaginal
                    show sexinserts chest morgan zorder 1
                    show sexinserts belly morgan as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    with vpunch
                    "Using the strong grip that I still have on her waist, I pull myself out from under Morgan."
                    "And it's just in time, as I cum almost the same moment that my cock is free."
                    show sexinserts chest morgan cum zorder 1
                    show sexinserts belly morgan cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    show morgan reverse cowgirl cum
                    with vpunch
                    "Morgan looks over her shoulder, shocked and disappointed as I cum over her."
                    with vpunch
                    "But I'm sure that, in the long run, she'd actually prefer this to the alternative."
                    $ morgan.sub += 1
                elif _return == "vaginal_condom":
                    "I have no idea if Morgan even remembers that I took the time to wear a condom."
                    "And this means that her oblivious sighs and moans could be thanks to a good memory or sheer ignorance."
                    with vpunch
                    "But whatever the case might be, I keep right on thrusting into her until the very moment I cum."
                    with vpunch
                    "Morgan cums a moment after me, making it look like she's been schooled in the Hollywood interpretation of the female orgasm."
                    with vpunch
                    "Whether she's faking it or not, I hardly have the time to care."
                    "I cum like my life depends on it, groaning and panting almost as much as Morgan is herself."
                    $ morgan.love += 1
                elif _return == "vaginal_inside_pill":
                    "Morgan seems to sense that I'm on the brink, and shakes her head desperately."
                    morgan.say "It's...okay...[hero.name]."
                    morgan.say "I'm...on...the pill."
                    morgan.say "Cum in me...if you want..."
                    "I wouldn't have needed any more invitation than those very words from her lips."
                    show morgan reverse cowgirl cum with vpunch
                    "But I was pretty much cumming at the same moment she said it!"
                    with vpunch
                    "I cum like my life depends on it, groaning and panting almost as much as Morgan is herself."
                    $ morgan.love += 2
                elif _return == "vaginal_inside_pregnant":
                    "Neither Morgan nor I need to be reminded of just why it's safe for me to keep on going right now."
                    "I can feel the weight of her swollen belly pressing down on mine from above all too well."
                    "But the weight is in no way an impediment or something that I need to ignore."
                    "In fact it makes me all the more intense in my need to please Morgan, to show her how much I desire her."
                    "It's something that we've created together, a living symbol of our love for each other."
                    show morgan reverse cowgirl cum ahegao with vpunch
                    "I cradle Morgan's weight as I fill her, feeling her lay ever more of it back onto me as she cums herself."
                    with vpunch
                    "She ends panting and soaked in sweat, laid backwards onto me as best she can with her belly sticking up on top."
                    $ morgan.love += 2
                elif _return == "vaginal_inside_mad":
                    morgan.say "[hero.name]...[hero.name]!"
                    morgan.say "You have to get it out of me - RIGHT NOW!"
                    "Morgan's panicked words shake me back to reality, making me aware I'm not wearing protection."
                    with vpunch
                    "I try desperately to do as she says, but it's just too late."
                    show morgan reverse cowgirl cum with vpunch
                    "I cum a second later, losing everything that I have inside of Morgan all at once."
                    $ morgan.impregnate()
                    with vpunch
                    "I stare up at Morgan, my eyes wide with shock."
                    "And she looks back over her shoulder at me, the exact same look on her face too."
                    $ morgan.love -= 10
                elif _return == "vaginal_inside_happy":
                    "I remember that I'm not wearing protection in those dangerous moments just before I'm about to cum."
                    "But as I scrabble to pull myself out of Morgan in time, I feel her wrap her legs around me and grab my thighs with her hands."
                    mike.say "Morgan...what are you..."
                    morgan.say "Please, [hero.name], please don't!"
                    morgan.say "I...I want this - please!"
                    "I don't honestly know if I could have managed to extricate myself from her before I came, now that she's holding me down."
                    show morgan reverse cowgirl cum ahegao with vpunch
                    "But in the few seconds that I have to make up my mind about what Morgan's saying, it's too late anyway."
                    with vpunch
                    "I cum with an urgency that surprises me, filling her while she clings on in desperation."
                    $ morgan.impregnate()
                    with vpunch
                    "Morgan takes all that I have to give her, and then collapses backwards onto me, moaning in satiated satisfaction."
                    $ morgan.love += 5
    else:
        "Morgan's ready for me as I leap on top of her, and we end up as a frenetic ball of limbs and libido."
        "We roll on the bed together, with it looking like I'll come out on top one moment and her the next."
        "Morgan finally hoists herself up and over me, turning so she has her back to me and scrambling to pin me to the bed despite her smaller size."
        "And that's when I decide to yield to her, save for making a token gesture of resistance and pushing back a little."
        "Sure, some guys might feel like it'd hurt their manhood to admit defeat and let Morgan come out on top like that."
        scene morgan reverse cowgirl
        with fade
        "But from the view I have as she looks down over me right now, I think they'd be the ones losing out!"
        "Morgan leans in close, smiling as she teases me with the sight of her naked body."
        "At the same time, I can feel her rubbing her slick lips against the shaft of my now very much erect cock."
        morgan.say "I came out on top."
        morgan.say "I say that means I get to choose where it goes!"
        mike.say "Bullshit, Morgan!"
        mike.say "I let you get on top, and stay there too."
        mike.say "Plus, it's MY cock!"
        morgan.say "Phsaw - like that matters!"
        morgan.say "You wanna stick it in one of MY holes, don't you?"
        "Rather than answering her with more words, I take a tight hold of Morgan around the waist, pulling her closer."
        "She yelps in surprise, but she doesn't object, and the smile never fades from her face for even a moment."
        mike.say "Keep firing off that dirty little mouth of yours, Morgan."
        mike.say "And I might just stick it in there to shut you up!"
        morgan.say "You do, and I'll bite it off!"
        "With that, we start to wrestle again."
        "And I'm having such a good time doing so, that so long as my cock ends up in Morgan, I don't honestly care where it actually is!"
        menu:
            "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                "The moment that I feel the head of my cock pass Morgan's pussy and press between her buttocks, my mind's made up."
                "That mischievous part of me that loves to tease her knows exactly what I'm going to do next."
                show morgan reverse cowgirl anal pleasure
                "Instead of pulling back and aiming for her pussy, I keep right on going and aim for her ass."
                "As soon as she feels it pressing against her anus, Morgan's face registers her shock, and then her amusement."
                morgan.say "Whoa...hey!"
                morgan.say "Where'd you think you're going, huh?"
                "I give her a sly smile in response, not stopping for a moment."
                morgan.say "Who said you could put that thing up there?"
                morgan.say "And how long have you been eyeing up my ass?"
                "By now I have my cock almost half way up her, feeling the muscles of her sphincter clutching at the shaft."
                "I'm refusing to answer any of her questions and keeping on going for one sole reason."
                "And that's the fact that, for all of her chatter, Morgan hasn't actually objected even once."
                "In fact, as she sinks down as far as she can onto my cock, she slowly stops talking altogether."
                "Instead she begins to moan and sigh at the sensations that she's feeling."
                "I can almost read what I'm feeling in her face looking at me over her shoulder, as her muscles finally accept what's going on."
                "All trace of her formerly joking and flirty demeanour is soon gone."
                "And in it's place is a near silent and almost sensual version of Morgan that's very different."
                "She presses her hands flat against my chest, rocking in time to my thrusts."
                "This means that she can take as much of my cock inside of her as physically possible with each thrust."
                show morgan reverse cowgirl pleasure
                "All I can do is lay back and watch Morgan's face over her shoulder, hypnotised by the expressions passing over it."
                "While it's the squeezing and caressing of her muscles that make me cum in the physical sense."
                "I swear that I could have done the same by simply studying the pleasure that's showing on her face the whole time too..."
                call cum_reaction (morgan, 'anal', sexperience_min) from _call_cum_reaction_142
                if _return == 'anal_inside':
                    "There's no danger in keeping right on going until the end."
                    "And Morgan's not exactly clambering to get off of my cock either."
                    show morgan reverse cowgirl ahegao
                    "But just the same as each and every thrust being reflected on her face, she shows climax in the exact same way."
                    show morgan reverse cowgirl cum with vpunch
                    "She takes all that I have to give her, gasping for breath as she leans over me."
                    with vpunch
                    "All I can manage to do myself is gasp from breath in the same way."
                    with vpunch
                    "And a moment later, Morgan's arms give out, making her fall back onto my chest."
                elif _return == 'anal_outside':
                    "I don't need to pull out of Morgan's ass to avoid an accident."
                    "But for some reason I feel compelled to do so all the same."
                    show sexinserts chest morgan zorder 1
                    show sexinserts belly morgan as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    show morgan reverse cowgirl -anal
                    "Maybe it's the way that Morgan's face twists into an expression of disappointment as I do so?"
                    "Or maybe it's the feeling of her muscles desperately twitching around my cock as it withdraws?"
                    show morgan reverse cowgirl cum with vpunch
                    "Either way, I cum the very moment that it slithers out of Morgan's ass."
                    show sexinserts chest morgan cum zorder 1
                    show sexinserts belly morgan cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    with vpunch
                    "This means that she's instantly spattered with a rope of warm semen."
                    with vpunch
                    "It hits her on her delicate breasts, making her squeal, and then runs down her belly and onto her thighs below."
                $ morgan.flags.anal += 1
            "Fuck her pussy":
                call check_condom_usage (morgan) from _call_check_condom_usage_92
                if _return == False:
                    return
                "I can practically feel the lips of Morgan's already slick pussy pulling me in."
                "And why go all the way round to knock on the back door when the front's already wide open?"
                mike.say "Knock, knock - can I come in?"
                morgan.say "Depends what the hell you want!"
                mike.say "Urgent delivery - live organ donation!"
                mike.say "The patient needs it inside of her, and pronto!"
                "I see Morgan's mouth curl as she tries to keep from laughing at the corny nature of the joke."
                "At the same time, she lowers herself down and onto me."
                morgan.say "Well, you'd better come in then!"
                show morgan reverse cowgirl vaginal pleasure



                "I can't help but gasp as Morgan takes a firm hold of my cock and guides it into her."
                "She holds my eye the entire time, clearly enjoying the way the sensation shows on my face."
                morgan.say "Mmmm...I think I found where your delivery belongs."
                morgan.say "Fits pretty much perfect, right about...there!"
                "And with that, she sits down on my cock, not stopping until it's in as deep as it can go."
                "I can hear Morgan sighing and moaning as she sinks down, losing the will to speak another word."
                "And she seems to become ever more engrossed in the moment as she starts to move atop me too."
                "Pretty soon all of the playful joking has faded away to nothing."
                "In its place there's only the sound of us both panting and gasping in time to our movements."
                "Yet we only seem to move below the waist, Morgan's hands holding onto my thighs and mine gripping at her waist."
                "All she looks back over her shoulder, holding my eye, as if unable to tear them away from staring into their depths."
                show morgan reverse cowgirl pleasure
                "I honestly can't say how long we're locked in this embrace, minutes or even as much as an hour."
                "But the spell is broken by the undeniable sensation of my being about to cum."
                "I feel my hands tighten around Morgan's waist and know that the inevitable climax is close enough to touch..."
                call cum_reaction (morgan, 'vaginal', sexperience_min) from _call_cum_reaction_143
                if _return == "vaginal_outside":
                    "As much as I desperately want to keep right on going, I can't risk cumming inside of Morgan."
                    "So summoning up all of my will-power, I pull myself out from under her as best I can."
                    show morgan reverse cowgirl -vaginal
                    show sexinserts chest morgan zorder 1
                    show sexinserts belly morgan as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    "The surprise and disappointment is instantly visible on her face, and she moans at the sensation."
                    show morgan reverse cowgirl cum with vpunch
                    "But that expression only lasts as long as it takes me to finally cum."
                    show sexinserts chest morgan cum zorder 1
                    show sexinserts belly morgan cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    with vpunch
                    "Freed as it has been from her pussy, my cock shoots its load straight onto Morgan's naked body."
                    with vpunch
                    "I watch, panting and exhausted as it spatters across her belly and runs down her thighs."
                    $ morgan.sub += 1
                elif _return == "vaginal_condom":
                    "Those few seconds that it took to put on the condom are paying off right now."
                    "It means that I can just devote myself to making sure that things end as smoothly as possible."
                    "I concentrate on maintaining my rhythm, and Morgan seems not to notice a thing."
                    with vpunch
                    "That is until the very moment of my climax, when her eyes almost pop open."
                    with vpunch
                    "She arches atop me, her body expressing every second of my orgasm like a dancing puppet."
                    with vpunch
                    "Once it's over, Morgan collapses backwards onto me, the pair of us totally and utterly spent."
                    $ morgan.love += 1
                elif _return == "vaginal_inside_pill":
                    morgan.say "No...don't stop now."
                    morgan.say "Pill...remember?!?"
                    "Morgan speaks up just in time to keep me from trying to pull out of her."
                    "I miss maybe a couple of beats as my brain struggles to process her words."
                    show morgan reverse cowgirl cum with vpunch
                    "But then I'm right back at it again, thrusting into her as I finally cum."
                    with vpunch
                    "Morgan clings to me tighter than ever, riding out every last second."
                    with vpunch
                    "Once it's over, Morgan collapses backwards onto me, the pair of us totally and utterly spent."
                    $ morgan.love += 2
                elif _return == "vaginal_inside_pregnant":
                    "I've been able to feel the heavy, reassuring weight of Morgan's swollen belly atop me this whole time."
                    "As if I need anything else to remind me of the fact that it's okay to cum inside of her!"
                    "It's pressed between us as she presses her weight down upon me, trying to get as close as possible."
                    "All the same, I try to support it as best I can, keen to protect what's already growing inside of her."
                    show morgan reverse cowgirl cum with vpunch
                    "Morgan clings to me tighter than ever, riding out every last second."
                    with vpunch
                    "Once it's over, Morgan collapses backwards onto me, the pair of us totally and utterly spent."
                    $ morgan.love += 2
                elif _return == "vaginal_inside_mad":
                    morgan.say "[hero.name] - you're gonna cum inside of me!"
                    mike.say "Wha...what?!?"
                    "But by the time I've shaken the cobwebs out of my head, it's already too late."
                    show morgan reverse cowgirl cum with vpunch
                    "I can't keep myself from cumming, and Morgan can't get off of my cock in time."
                    with vpunch
                    "She finally manages to clamber off of me a few seconds later."
                    "But a tendril of cum already dripping out of her betrays the fact that we were both of us too late."
                    $ morgan.impregnate()
                    "In the silence that follows, Morgan and I exchange shocked glances and helpless shrugs."
                    "Neither of us can explain what happened, but we're both too guilty to even think of blaming the other too."
                    $ morgan.love -= 10
                elif _return == "vaginal_inside_happy":
                    "At the very last moment possible, I remember that I'm not wearing a condom."
                    "But almost as soon as I try to pull out of Morgan, I feel her tense her muscles and resist my efforts."
                    mike.say "Morgan...what are you..."
                    morgan.say "Oh no, you're not going anywhere!"
                    mike.say "But...I'm not wearing..."
                    morgan.say "I know, I know...I just...want this."
                    morgan.say "I want it too bad to let you go!"
                    show morgan reverse cowgirl cum ahegao with vpunch
                    "Before I can say another word, I feel myself cumming."
                    $ morgan.impregnate()
                    with vpunch
                    "Morgan smiles down at me as I fill her, a look of satisfaction on her face."
                    $ morgan.love += 5
    hide bellycum
    hide sexinserts
    return

label morgan_fuck_date_missionary(sexperience_min):
    scene morgan missionary
    "With Morgan pinned to the bed and myself firmly atop her, I'm eager to take things to the next logical step."
    "Beneath me, Morgan looks flushed and more than willing to let me have my way with her."
    call check_condom_usage (morgan) from _call_check_condom_usage_93
    if _return == False:
        return
    "Here goes - this is it."
    "Not only have I had the revelations of rediscovering an old friend and then being told that he was a she all along."
    "She's also on the brink of becoming something far more to me than a face newly returned from the past."
    if morgan.male >= 75:
        "If I was in any doubt as to what Morgan wanted of me, she makes it clear by pulling me towards her."
        "One hand grips me around the neck, while the other fumbles around below, guiding me into her."
        "All the time she thrusts her groin towards me, as if desperate to feel me slip inside."
        show morgan missionary vaginal
        if CONDOM:
            show morgan missionary vaginal condom
        "When I make it and finally sink into her, Morgan feels incredible - tight and yet welcoming."
        morgan.say "Oh, shit...that's it...give it to me!"
        "I'm already deep inside of Morgan and more than committed to the act when she makes this demand of me."
        "But still I do my best to oblige, setting a quick rhythm and enjoying the immediate rewards in terms of sensation."
        "I'm used to being the one that makes most of the groans and grunts during sex, but Morgan soon puts me to shame in this respect."
        "Every thrust into her is met with a satisfied noise that makes me think that she's about to begin growling and clawing at any moment."
        "Indeed, I can feel her nails as she runs them down my back and scratches me in the throes of her passion."
        "My only answer to this is to become even more forceful myself, making Morgan's entire body shudder as I fuck her with all I have to give."
        "Her petite breasts are literally bouncing up and down by now, and she's slick with sweat."
        morgan.say "Hmmm...I don't care if you have to break me in half, [hero.name]."
        morgan.say "Just keep fucking me like this 'til I cum!"
        "I sincerely hope that won't be something that takes too long to happen."
        "My stamina's not the problem here, it's more the almost savage way that Morgan seems to like to make love."
        "She's driving me to such a degree that I can't keep going for much longer without cumming myself."
    elif morgan.male >= 25:
        "For all that my journey towards discovering the truth about Morgan felt strange and challenging, this moment is the complete opposite."
        "We seem to come together without a second of hesitation or the need for one person to show the other the way."
        "In that moment, everything just feels right."
        show morgan missionary vaginal
        if CONDOM:
            show morgan missionary vaginal condom
        "I feel myself brush against the lips of Morgan's pussy, and then I'm inside of her."
        "Just like that we come together and there's nothing between us."
        morgan.say "Oh, [hero.name]...I never thought...that I'd have this..."
        morgan.say "It feels...so good."
        "I lean in and kiss Morgan passionately then, wanting to be as close to her as I can manage to be."
        "Before now, I don't think that I'd fully understood what being with me meant to her."
        "Sure, I've been the guy that's longed for a girl so badly, but I've never had someone want me for so long as Morgan has."
        "The intensity of her passion and the way it's inflaming her desire is almost intoxicating to me."
        "For all that her body is making me come alive with my own pleasure, I feel the need to give her as much as I can in return."
        "My kisses have spilled onto her neck by this time, and I can't keep from nipping and biting on occasion too."
        "It feels like in the same way that Morgan has become almost an entirely new person to me now, I want the same for myself."
        "I want to live up to the image that she's carried of me for all those years, to be the man that she wants me to be in her fantasies."
        "My body reflects this same desire, as I continue to push myself into Morgan with every ounce of stamina that I still possess."
        morgan.say "[hero.name]...I'm going to cum!"
        "I almost fail to hear Morgan's breathless words, as I feel myself succumbing to the very same thing."
    else:
        morgan.say "Wow, [hero.name]...you're so big!"
        morgan.say "You're going to fill me up nicely!"
        "Morgan's chuckles and giggles are becoming less frequent now, replaced instead with panting and sighing instead."
        "She wraps her hands around my neck and seems to hold on for dear life as I lower myself down atop her."
        show morgan missionary vaginal
        if CONDOM:
            show morgan missionary vaginal condom
        "Though I feel my cock pushing into her without too much resistance, still Morgan rolls her eyes and moans intensely all the same."
        "I begin to move inside of her, and she seems happy to abandon herself to my attentions, simply letting me have my way with her."
        "But that's not any kind of problem, as the feeling of having her entire body laid open to my attentions is something quite irresistible."
        "Morgan writhes beneath me, responding with all of her being to the pleasure that she takes from my taking my own from her."
        "It's as though the years that she must have spent nursing her affections for me have rendered her helpless now that she has her heart's desire."
        "All that she wants to do is lie back and let me use her like a living doll, like a human sex-toy."
        "And I'm more than happy to oblige her in that particular desire."
        "Her petite form is almost folded in half beneath me now, and I can feel her small breasts rubbing against my chest, her nipples stiff and erect."
        "I can't remember a single thing about the person that I once thought Morgan to be."
        "His memory is almost gone from my mind, erased in favour of the woman that I'm making love to right now."
        "Like Morgan's sentiments about my cock entering her pussy - there's simply no room for him inside of my head."
        "And I feel like the moment that I cum, his memory will be washed away forever."
    "This is it, I can't hold on for a moment longer."
    call cum_reaction (morgan, 'vaginal', sexperience_min) from _call_cum_reaction_144
    if _return == "vaginal_outside":
        show sexinserts belly morgan zorder 1 at center, zoomAt(1, (640, 770)) with hpunch
        "I have all the proof I need to believe that Morgan is and always has been a girl."
        "I don't need to get her pregnant to prove it beyond any shadow of a doubt."
        show sexinserts belly morgan cum zorder 1 at center, zoomAt(1, (640, 770))
        show morgan missionary out cum
        with hpunch
        "At the last second, I pull out of Morgan and send my load showering over her stomach and already slick thighs."
        with hpunch
        "She can't help but groan in disappointment, but she'll thank me for it once the dust has settled and her heart has stopped hammering in her chest."
        $ morgan.love += 1
    elif _return == "vaginal_condom":
        with hpunch
        "As I feel my climax taking over, I begin to thrust more deeply into Morgan than I thought was possible."
        with hpunch
        "Even though she can't feel everything, there's still no way that she can fail to be effected by this doubling of intensity."
        with hpunch
        "Her head thrashes from side to side as she's pulled into her own orgasm a few seconds later."
        $ morgan.love += 1
    elif _return == "vaginal_inside_pill":
        show morgan missionary vaginal cum with hpunch
        "Gasping at the sensations racking her body, Morgan barely manages to gasp out as I reach my end."
        with hpunch
        morgan.say "I...on...pill....fuck!"
        $ morgan.love += 2
    elif _return == "vaginal_inside_pregnant":
        show morgan missionary vaginal cum with hpunch
        "Gasping at the sensations racking her body, Morgan barely manages to gasp out as I reach my end."
        with hpunch
        morgan.say "I...pregnant....fuck!"
        $ morgan.love += 2
    elif _return == "vaginal_inside_mad":
        show morgan missionary vaginal cum with hpunch
        "Morgan feels the full and unadulterated force of my orgasm as I lose myself inside of her."
        show morgan missionary vaginal cum orgasm with hpunch
        "There'll be consequences later, but for the moment we're both lost in it and nothing else matters."
        with hpunch
        "All that I can hear is my own hoarse panting for breath and the sound of Morgan moaning as she cums in turn."
        $ morgan.impregnate()
        hide morgan
        show bg bedroom1
        show morgan naked angry
        with hpunch
        if morgan.male >= 50:
            morgan.say "Ah...ah...aaah, fuck!"
            "Morgan's words are almost indistinguishable from the gasps she makes as I thrust into her."
            morgan.say "You...you came in me...you stupid bastard!"
            morgan.say "You came inside of me without a damn rubber!"
        else:
            morgan.say "Oh god, oh god, oh god...you came in me!"
            "I can feel her beginning to shudder from something other than the sensation of my cock inside of her."
            "At the same time, she starts to let out little sobs that are barely even audible."
            morgan.say "In me...with no condom!"
        $ morgan.love -= 25
    elif _return == "vaginal_inside_happy":
        show morgan missionary vaginal cum with hpunch
        "Morgan feels the full and unadulterated force of my orgasm as I lose myself inside of her."
        show morgan missionary vaginal cum orgasm with hpunch
        $ morgan.impregnate()
        "There'll be consequences later, but for the moment we're both lost in it and nothing else matters."
        with hpunch
        "All that I can hear is my own hoarse panting for breath and the sound of Morgan moaning as she cums in turn."
        $ morgan.love += 5
    return

label morgan_fuck_date_standing(sexperience_min):
    scene bg black
    show morgan standing half nomc
    with fade
    "This makes me open my eyes, just in time to see what Morgan's doing."
    "Morgan is bending over and thrusting her ass hard against me!"
    "She looks back over her shoulder as she does so too."
    "And I can see that there's a wicked grin on her face."
    if morgan.male >= 66:
        morgan.say "Screw the bed..."
        morgan.say "Just fuck me here!"
    elif morgan.male >= 33:
        morgan.say "Not on the bed, [hero.name]…"
        morgan.say "I want you to do me right here, yeah?"
        morgan.say "Bend me over and do me from behind!"
    else:
        morgan.say "You don't have to use the bed, [hero.name]..."
        morgan.say "You can do me here...if you want!"
    "My eyes are almost popping out of my head by the time Morgan asks the question."
    "Already I can feel myself getting painfully hard from the sight of her in that position."
    "And the mere thought of the possibilities is enough to set my head spinning."
    mike.say "Y...yeah, Morgan..."
    mike.say "You got it..."
    mike.say "Wherever you want it!"
    menu:
        "Fuck her pussy":
            "From where I'm standing I have a pretty good view of Morgan below the waist."
            "And as if she senses my gaze travelling in that direction, she spreads her legs."
            "The action means that now I can see absolutely everything down there."
            "But the moment that my eyes settle on her neat, perfect little pussy..."
            show morgan standing -nomc
            "Well, there's nothing else that I want more in this world!"
            call check_condom_usage (morgan) from _call_check_condom_usage_142
            if CONDOM:
                show morgan standing condom
            if _return == False:
                return
            play sound spank
            show morgan standing spank closed pleasure with hpunch
            "I reach out and clap my hands onto Morgan's haunches."
            "They make a smacking sound as they grip her."
            "And the yelp that she lets out is pretty satisfying to hear too."
            morgan.say "Argh..."
            show morgan standing half pinch
            morgan.say "Ooh..."
            morgan.say "I love it when you take charge!"
            "Morgan underlines the point by wriggling in my grasp."
            "That and pushing her ass hard against me too."
            mike.say "Whoa..."
            mike.say "Okay, Morgan, okay..."
            show morgan standing -spank
            mike.say "I'm on it!"
            "I do the best I can to ignore the pressure that Morgan's putting me under."
            "But I'm still wanting to make this as memorable as I can for her."
            "So I set my mind racing to find a solution."





























            show morgan standing pullout
            "By the time I have the head of my cock between her legs, Morgan is already totally aroused."
            "I know this because the head slithers here and there, sliding on her natural wetness."
            "But that doesn't mean her pussy is just going to open up and let me straight in there."
            "Instead I feel the muscles still trying their best to keep her lips tightly together."
            "That doesn't bother me though, as I can already hear the way that Morgan's panting."
            "And her body quivers whenever my cock brushes her pussy, letting me know she's desperate too."
            "This means I have all the encouragement I need to push my way inside of her."
            "Pressing myself as close as possible, I make one pass after another."
            "And each time I think that she's going to open to me, only to be denied."
            "Yet every pass sees Morgan gasping and quaking with greater intensity."
            "Finally there's not a hint of resistance left in her body."
            show morgan standing vaginal closed pleasure
            "The muscles down there surrender and her lips part."
            "But that doesn't mean I'm going to respond with the same subtlety."
            "Instead I throw all of my weight behind the next thrust."
            show morgan standing half
            "Which means that I push my way into Morgan in one smooth motion."
            "Rather than being allowed to prepare itself, her body is invaded all at once."
            "And as I fill her, I can feel it being forced to stretch in order to take me."
            show morgan standing closed pinch
            morgan.say "Urgh..."
            morgan.say "Mmm..."
            show morgan standing half
            morgan.say "P...please..."
            morgan.say "F...fuck me..."
            morgan.say "Fuck me hard?"
            "It's not like Morgan had to beg me to do that."
            "But the fact she put it into words makes me leap to obey her."
            "I don't pause to savour the sensation of being inside her."
            show morgan standing spank closed pleasure at stepback(speed=0.1, h=-10, v=-20)
            pause 0.3
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "Instead I instantly begin to thrust in and out for all I'm worth."
            "The effect is pretty dramatic too, as Morgan starts to almost wail."
            "But the fact she's nodding the whole time tells me this is what she wants."
            "Which is lucky, because it's what I want too."
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            pause 0.3
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "And I don't know if I could stop now even if I wanted to!"
            "My fingers are digging into Morgan's waist, holding on desperately."
            show morgan standing down at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "Every thrust I make seems to send jolts of pleasure through her body."
            "I know this because I can see how motions are making her breasts jiggle."
            "But she's also writhing and wriggling on her own too."
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "Motions that have to be an expression of what she's feeling right now."
            "All I know for myself is that this feels so right."
            "It feels like something that's supposed to be."
            "Something that I never want to end."
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "But the problem is that I've chosen intensity over longevity."
            "And so I can already feel my reserve of stamina coming to an end."
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "I'm going to have to end it soon."
            "So I'd better do something to make it memorable."













            show morgan standing up at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "And the effect on Morgan is instant, as well as dramatic."
            "Because I can feel her pussy clenching around my cock."
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "Which means I've managed to make her cum at the same time as me!"
            call cum_reaction (morgan, 'vaginal', sexperience_min) from _call_cum_reaction_269
            if _return == "vaginal_outside":
                if CONDOM:
                    "I need to pull out."
                else:
                    "I want to stay right where I am, but we didn't use protection, so I need to pull out."
                "And that's just what I do, keeping up the same speed and intensity until the very last moment."
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing pinch out cumshot -spank -vaginal with hpunch
                if CONDOM:
                    "Then I yank myself straight out of Morgan."
                else:
                    "Then I yank myself straight out of Morgan, and within seconds I shoot my load over her back."
                "She's already starting to cum herself, and the sensation seems to push her along faster."
                show morgan standing half
                if not CONDOM:
                    show morgan standing cum -cumshot
                    $ morgan.love += 1
                    $ morgan.sub += 1
                with hpunch
                "So much so that I feel the need to hold on tighter, to keep her from toppling over!"
            elif _return == "vaginal_condom":
                "Remembering that we chose to use a condom, I feel confident ploughing straight on."
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                "And that's just what I do, keeping up the same speed and intensity until the very last moment."
                show morgan standing pinch at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing with hpunch
                "Then I just let go, allowing myself to lose it as deep inside Morgan as I can go."
                with hpunch
                "She's already starting to cum herself, and the sensation seems to push her along faster."
                show morgan standing half with hpunch
                $ morgan.love += 1
                "So much so that I feel the need to hold on tighter, to keep her from toppling over!"
            elif _return == "vaginal_inside_pill":
                show morgan standing half pinch
                morgan.say "It's...okay..."
                morgan.say "I'm on...the...pill!"
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                "I silently thank Morgan for the timely reminder, because with it I feel confident ploughing straight on."
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                "And that's just what I do, keeping up the same speed and intensity until the very last moment."
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing pleasure closed cumshot shaking with hpunch
                "Then I just let go, allowing myself to lose it as deep inside Morgan as I can go."
                with hpunch
                "She's already starting to cum herself, and the sensation seems to push her along faster."
                show morgan standing half pinch pullout cum -shaking -vaginal with hpunch
                $ morgan.love += 2
                "So much so that I feel the need to hold on tighter, to keep her from toppling over!"
            elif _return == "vaginal_inside_pregnant":
                show morgan standing half pinch
                morgan.say "It's...okay..."
                morgan.say "I'm pregnant...remember?"
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                "I silently thank Morgan for the timely reminder, because with it I feel confident ploughing straight on."
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                "And that's just what I do, keeping up the same speed and intensity until the very last moment."
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing pleasure closed cumshot shaking with hpunch
                "Then I just let go, allowing myself to lose it as deep inside Morgan as I can go."
                with hpunch
                "She's already starting to cum herself, and the sensation seems to push her along faster."
                show morgan standing half pinch pullout cum -shaking -vaginal
                $ morgan.love += 2
                "So much so that I feel the need to hold on tighter, to keep her from toppling over!"
            elif _return == "vaginal_inside_mad":
                show morgan standing wide pleasure
                morgan.say "Pull...out..."
                morgan.say "Quickly!"
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                "Morgan's warning catches me totally off-guard, and I'm unable to respond."
                "I know that I should be doing as she says, but for some reason I'm frozen."
                show morgan standing closed cumshot with hpunch
                "Then I just let go, allowing myself to lose it as deep inside Morgan as I can go."
                with hpunch
                "She's already starting to cum herself, and the sensation seems to push her along faster."
                "So much so that I feel the need to hold on tighter, to keep her from toppling over!"
                show morgan standing wide
                $ morgan.love -= 25
                "But all the time she's looking back over her shoulder at me, a horrified expression on her face."
            elif _return == "vaginal_inside_happy":
                "I want to stay right where I am, but we didn't use protection, so I need to pull out."
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                "And that's just what I do, keeping up the same speed and intensity until the very last moment."
                "Then I make to yank myself out before it's too late, but I find something stopping me."
                show morgan standing wide pleasure
                "Morgan's pushing herself backwards, using her weight to keep me in there!"
                morgan.say "No..."
                morgan.say "No way..."
                morgan.say "I want you to...cum in me!"
                "If I'd had more time to react, then I maybe could have pulled out in time."
                "But the state of confusion that I'm in means that everything happens too fast."
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing closed cumshot shaking with hpunch
                "I have no choice but top let go, allowing myself to lose it as deep inside Morgan as I can go."
                with hpunch
                "She's already starting to cum herself, and the sensation seems to push her along faster."
                show morgan standing half pinch -shaking
                $ morgan.love += 5
                "So much so that I feel the need to hold on tighter, to keep her from toppling over!"
                "But all the time she's looking back over her shoulder at me, a delighted expression on her face."
        "Fuck her ass":
            "From where I'm standing I have a pretty good view of Morgan below the waist."
            "And as if she senses my gaze travelling in that direction, she spreads her legs."
            "The action means that now I can see absolutely everything down there."
            "But the moment that my eyes settle on her neat, perfect little hole..."
            show morgan standing -nomc
            "Well, there's nothing else that I want more in this world!"
            play sound spank
            show morgan standing spank closed pleasure with hpunch
            "I reach out and clap my hands onto Morgan's haunches."
            "They make a smacking sound as they grip her."
            "And the yelp that she lets out is pretty satisfying to hear too."
            morgan.say "Argh..."
            show morgan standing half pinch
            morgan.say "Ooh..."
            morgan.say "I love it when you take charge!"
            "Morgan underlines the point by wriggling in my grasp."
            "That and pushing her ass hard against me too."
            mike.say "Whoa..."
            mike.say "Okay, Morgan, okay..."
            show morgan standing -spank
            mike.say "I'm on it!"
            "I do the best I can to ignore the pressure that Morgan's putting me under."
            "But I'm still wanting to make this as memorable as I can for her."
            "So I set my mind racing to find a solution."





























            show morgan standing pullout
            "By the time I have the head of my cock between her buttocks, Morgan is already totally aroused."
            "I know this because the head slithers here and there, sliding on her natural wetness."
            "But that doesn't mean her ass is just going to open up and let me straight in there."
            "Instead I feel the muscles still trying their best to keep her hole tightly closed."
            "That doesn't bother me though, as I can already hear the way that Morgan's panting."
            "And her body quivers whenever my cock brushes her hole, letting me know she's desperate too."
            "This means I have all the encouragement I need to push my way inside of her."
            "Pressing myself as close as possible, I make one pass after another."
            "And each time I think that she's going to open to me, only to be denied."
            "Yet every pass sees Morgan gasping and quaking with greater intensity."
            "Finally there's not a hint of resistance left in her body."
            show morgan standing anal closed pleasure
            "The muscles down there surrender and her hole relaxes."
            "But that doesn't mean I'm going to respond with the same subtlety."
            "Instead I throw all of my weight behind the next thrust."
            show morgan standing half
            "Which means that I push my way into Morgan in one smooth motion."
            "Rather than being allowed to prepare itself, her body is invaded all at once."
            "And as I fill her, I can feel it being forced to stretch in order to take me."
            show morgan standing closed pinch
            morgan.say "Urgh..."
            morgan.say "Mmm..."
            show morgan standing half
            morgan.say "P...please..."
            morgan.say "F...fuck me..."
            morgan.say "Fuck me hard?"
            "It's not like Morgan had to beg me to do that."
            "But the fact she put it into words makes me leap to obey her."
            "I don't pause to savour the sensation of being inside her."
            show morgan standing spank closed pleasure at stepback(speed=0.1, h=-10, v=-20)
            pause 0.3
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "Instead I instantly begin to thrust in and out for all I'm worth."
            "The effect is pretty dramatic too, as Morgan starts to almost wail."
            "But the fact she's nodding the whole time tells me this is what she wants."
            "Which is lucky, because it's what I want too."
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            pause 0.3
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "And I don't know if I could stop now even if I wanted to!"
            "My fingers are digging into Morgan's waist, holding on desperately."
            show morgan standing down at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "Every thrust I make seems to send jolts of pleasure through her body."
            "I know this because I can see how motions are making her breasts jiggle."
            "But she's also writhing and wriggling on her own too."
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "Motions that have to be an expression of what she's feeling right now."
            "All I know for myself is that this feels so right."
            "It feels like something that's supposed to be."
            "Something that I never want to end."
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "But the problem is that I've chosen intensity over longevity."
            "And so I can already feel my reserve of stamina coming to an end."
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "I'm going to have to end it soon."
            "So I'd better do something to make it memorable."













            show morgan standing up at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "And the effect on Morgan is instant, as well as dramatic."
            "Because I can feel her ass clenching around my cock."
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show morgan standing at stepback(speed=0.1, h=-10, v=-20)
            "Which means I've managed to make her cum at the same time as me!"
            call cum_reaction (morgan, 'anal', sexperience_min) from _call_cum_reaction_270
            if _return == 'anal_inside':
                "Now that I've hit my ideal pace, I feel confident ploughing straight on."
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                "And that's just what I do, keeping up the same speed and intensity until the very last moment."
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing pleasure closed cumshot shaking with hpunch
                "Then I just let go, allowing myself to lose it as deep inside Morgan as I can go."
                with hpunch
                "She's already starting to cum herself, and the sensation seems to push her along faster."
                show morgan standing half pinch -shaking with hpunch
                $ morgan.sub += 3
                show morgan standing down
                "So much so that I feel the need to hold on tighter, to keep her from toppling over!"
            elif _return == 'anal_outside':
                "I could stay right where I am, but for some reason I feel the urge to pull out before the end."
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                "And that's just what I do, keeping up the same speed and intensity until the very last moment."
                show morgan standing at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show morgan standing out pinch cumshot -spank -anal with hpunch
                "Then I yank myself straight out of Morgan, and within seconds I shoot my load over her back."
                with hpunch
                "She's already starting to cum herself, and the sensation seems to push her along faster."
                show morgan standing half cum -cumshot with hpunch
                $ morgan.love += 1
                $ morgan.sub += 1
                show morgan standing down
                "So much so that I feel the need to hold on tighter, to keep her from toppling over!"
            $ morgan.flags.anal += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
