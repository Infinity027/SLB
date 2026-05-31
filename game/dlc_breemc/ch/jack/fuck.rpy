init python:
    Event(**{
    "name": "jack_hottub_sex_female",
    "label": "jack_hottub_sex_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(jack,
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

    Activity(**{
    "name": "jack_fuck_date_vip_doggy_female",
    "label": "jack_fuck_date_vip_doggy_female",
    "display_name": "Fuck",
    "duration": 1,
    "conditions": [
        IsDone("jack_nightclub_date_female"),
        HeroTarget(
            IsGender("female"),
            IsRoom("date_nightclub")
            ),
        PersonTarget(jack,
            OnDate(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": False,
    "once_day": True,
    "icon": "fuck",
    })

    Activity(**{
    "name": "jack_fuck_date_beach_female",
    "label": "jack_fuck_date_beach_female",
    "display_name": "Fuck",
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsRoom("date_beach"),
            ),
        PersonTarget(jack,
            OnDate(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": False,
    "once_day": True,
    "icon": "fuck",
    })


label jack_hottub_sex_female:
    scene bg pool
    if game.calendar.get_time_of_day() == "evening":
        $ renpy.show(f"hottub_bg_night_left")
    else:
        $ renpy.show(f"hottub_bg_{game.calendar.season_name}_left")
    $ renpy.show("hottub_fg_valentine_left", tag="romantic")
    with fade
    "I've been preparing the hot-tub for when Jack gets here, making sure everything is just so."
    "I feel like I have to make sure it's perfect for us taking a dip amongst the bubbles together."
    "Part of me isn't sure why the preparations are so important to me."
    "I mean, Jack literally jumped at the chance to come over and join me in the tub."
    "It was almost like he couldn't believe I made the offer."
    "Like he'd won the lottery or something crazy!"
    "Oh...maybe that's it?"
    "Jack's not like most guys, you know?"
    "The kind that swagger about trying to impress you with the size of their manhood."
    "It almost makes me chuckle to think of it, but Jack's more your typical geek!"
    "And I don't mean that in a bad way either."
    "It means he's passionate and enthusiastic."
    "In fact, it's kind of hot that he's so geeky!"
    "So maybe that's why I'm so keen for this to turn out well."
    "The problem is that I don't know how to make a dip in the hot-tub geeky!"
    "So I've just had to go for the classics, yeah?"
    "Subdued lighting, candles, wine and scattering rose petals around the place."
    "I just hope Jack can handle something so straight-up and mainstream..."
    jack.say "Hey, [hero.name]!"
    jack.say "Sorry if I'm a little late."
    jack.say "I....WHOA!"
    scene bg pool
    show jack smile at left5
    with fade
    "I turn around to see Jack standing a little way off from the hot-tub."
    "He's looking around with what seems to be amazement on his face."
    bree.say "Oh..."
    bree.say "Hey, Jack!"
    bree.say "Are you okay?"
    show jack normal at center with ease
    "Jack shakes his head and makes himself look me in the eye."
    "It's almost like he's stunned by the way the place looks."
    jack.say "Ah...no..."
    show jack happy
    jack.say "I'm fine, [hero.name]!"
    show jack blush
    jack.say "But we did say tonight, didn't we?"
    jack.say "To take a dip in your hot-tub?"
    bree.say "Yeah, Jack."
    "I gesture to everything that I've been rushing to put together."
    bree.say "Why'd you think I went to all this trouble?"
    show jack normal
    "Jack blinks at me for a moment."
    "Then he looks a little sheepish."
    jack.say "I...I kinda thought it must be for someone else, [hero.name]."
    jack.say "I mean...people don't usually do stuff like this for me."
    jack.say "Definitely not girls!"
    "There it is again, that endearing quality that he has."
    "Most guys would be puffing out their chests right now."
    "Full of themselves at getting a girl to go all out for them."
    "But not Jack - he's so humble he assumes it's for someone else!"
    show jack at center, zoomAt(2.0, (640, 1340))
    "I walk over to where he's standing and plant a kiss on his lips."
    show jack blush at center, zoomAt(1.5, (640, 1040))
    bree.say "Well this girl did, Jack."
    bree.say "So are we doing this thing, or what?"
    "Jack still looks more than a little stunned."
    "But he nods his head and pulls off his shirt."
    hide jack
    $ game.active_date.clothes = "swimsuit"
    show jack swimsuit
    with dissolve
    "Then he pulls off his pants to reveal his swimsuit."
    "Jack lets me lead him over to the tub, and we step down into the water."
    "While he gets comfortable, I pour us both a glass of wine."
    show hottub jack valentine with fade
    "Handing one to Jack, I lie back in the water, letting the bubbles do their work."
    bree.say "So, Jack..."
    bree.say "How do you like it?"
    "Jack nods eagerly as he takes a sip of his wine."
    jack.say "This is great, [hero.name]!"
    jack.say "All we have at my place is a shower."
    jack.say "And sometimes that doesn't even work!"
    "I can't help laughing at Jack as he says this."
    bree.say "Oh, Jack!"
    bree.say "We're not in here to get clean."
    bree.say "In fact, I wondered if you wanted to get a little dirty?"
    "I give Jack a wink and stretch out my leg towards him."
    "And I see the look of surprise on his face as I rub my foot against his own leg too."
    jack.say "Whoa..."
    jack.say "I...I mean, yeah, [hero.name]!"
    jack.say "That sounds great!"
    jack.say "You know that I'm cool with that kind of thing."
    play sound "<from 1.4 to 2.6>sd/SFX/humans/finger_snap.ogg"
    "Jack clicks his fingers and tries to make himself look cool."
    "But the result is pretty comical, making me chuckle again."
    "Oh boy - how is this guy's dorkiness turning me on so much?"
    "Shaking it off, I put down my glass."
    "And then I slide through the water to where Jack is sitting."
    "Once I'm there, I drape my arms around his neck."
    "And then I lower myself down onto him."
    bree.say "Let's not get confused here, Jack."
    bree.say "When I say get dirty, you know what I mean, right?"
    bree.say "You know that I want you to fuck me?"
    "I hear Jack swallow as I ask him the question."
    "And his eyes are wide as he nods to show me he understands."
    "But I'm not too worried about the expression on Jack's face."
    "Because right now another part of him is speaking to me as well."
    "And it's using a language that's a lot easier to understand."
    "Of course it's his manhood, which I can feel as I straddle his thighs."
    "Even if Jack's head is all aflutter, his cock is sure of what it wants!"
    "Not wasting any time, I reach down with one hand."
    "And I slide it into his trunks, my fingers searching for it."
    "When they close around the shaft, I give Jack's cock a quick squeeze."
    "It's not too hard or harsh, but it's enough to snap him out of it."
    "And he seems to come round a second later, his attention fixed on me."
    jack.say "Oh, [hero.name]!"
    jack.say "That feels really good!"
    bree.say "Not as good as it's going to in a little while, Jack!"
    "I ease his cock out of his trunks as I say this."
    "And at the same time I pull aside the crotch of my own swimsuit."
    "Jack watches in complete fascination as I guide his cock home."
    show hottub sex female jack with fade
    "Even more so as I rub the tip against the folds of my pussy."
    "My skin might be wet from the water."
    "But that part of me is wet for an entirely different reason."
    "And soon enough, nature takes it's course."
    jack.say "[hero.name[0]]...[hero.name]..."
    jack.say "Oh god..."
    jack.say "That's even better!"
    "I nod and smile, biting my lip as I feel Jack sliding into me."
    "It's slow going, every fraction of an inch adding to the sensation."
    "And the look of amazement on his face only makes it feel better."
    "Once he's deep enough inside, I take my hand away."
    "Then I use both of them to take hold of his wrists."
    "Jack doesn't resist as I lift his arms up and place his hands on me waist."
    "In fact, he looks like he's waiting for me to tell him what to do next."
    bree.say "Jack..."
    jack.say "Y...yeah, [hero.name]?"
    bree.say "Listen to me very carefully, okay?"
    jack.say "Sure thing!"
    bree.say "I want you to fuck me, Jack."
    bree.say "And I want you to fuck me hard, okay?"
    bree.say "Can you do that for me, Jack?"
    "Jacks eyes look like they're about to pop right out of his head."
    "But he's nodding all the same, a determined look on his face."
    bree.say "And I want your hands all over me too."
    bree.say "I want you to grab by ass and squeeze my breasts, yeah?"
    "To make my point, I start grinding myself against Jack as I say all of this."
    "Wriggling so that his cock is worked against the walls of my pussy."
    "It's about then that I feel the first hints of Jack coming to life."
    "His groin twitches, pushing his cock deeper into me."
    "Then I feel his grip on me tightening, his fingers pressing into my thighs."
    "I can't help moaning, nodding as I ask for more."
    "That seems to be all that Jack needs to know what I want."
    "Because the next thrust he makes sends a jolt through my entire body."
    "He notes the effect, because it's soon followed by another and another."
    "As each wave of pleasure hits me, it gets harder to stay focused."
    "Jack's love-making is like a snowball rolling downhill."
    "It starts out slow and small, but just keeps getting bigger and picking up speed!"
    "He seems to have taken my words to heart as well."
    "As I can feel his hands all over my body."
    "I'm gasping and panting as Jack explores every inch of me."
    "But I make sure to keep on nodding as he does so."
    "Because I don't want him to even think of stopping."
    "I'm almost laid atop Jack in the water by now."
    "Pushing him down into the water as he thrusts up into me from below."
    "Sure, he's doing most of the work."
    "But that doesn't stop my ass from going up and down too."
    "My muscles are straining to let him fill me to the very limit."
    "And part of me feels like I want to swallow him whole down there!"
    bree.say "Mmm..."
    bree.say "Oh, Jack..."
    bree.say "Don't stop..."
    bree.say "Not until you cum in me - please!"
    jack.say "[hero.name]..."
    jack.say "I...I think I'm going to..."
    with vpunch
    "Jack shoots his load a moment later, his entire body stiffening as he does so."
    with vpunch
    "This means that he's as deep inside of me as he can possibly go."
    with vpunch
    "And that I take the whole thing without any chance of escaping."
    "Not that I want to do that, not for a second."
    $ jack.impregnate()
    with vpunch
    "Instead I cling to Jack as tightly as I can, feeling myself start to cum too."
    "I want to make this last as long as possible, to ride Jack until the very end."
    "Only when we're totally spent do we start to loosen our hold on each other."
    "And even then we remain wrapped in each others arms."
    "After all, there's still wine and the water's warm."
    "There's nowhere else I'd rather be in all the world right now."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ jack.sexperience += 1
    $ game.active_date.clothes = None
    scene bg black with dissolve
    return

label jack_fuck_date_female(location="hero"):
    $ game.room = "bedroom4"
    call jack_fuck_date_intro_female (location) from _call_jack_fuck_date_intro_female
    menu:
        "Missionary":
            call jack_fuck_date_missionary (0) from _call_jack_fuck_date_missionary
        "Reverse cowgirl" if hero.sexperience >= 5:
            call jack_fuck_date_reverse_cowgirl (5) from _call_jack_fuck_date_reverse_cowgirl
        "Doggy" if hero.sexperience >= 10:
            call jack_fuck_date_doggy (10) from _call_jack_fuck_date_doggy
    if _return == "leave_without_gain":
        return
    $ jack.sexperience += 1
    if _return == "leave_with_gain":
        return
    call sleep ("jack") from _call_sleep_120
    hide jack
    return

label jack_fuck_date_intro_female(location="hero"):
    if game.week_day % 3 == 0:
        scene bg livingroom
        show jack normal
        with fade
        "I can tell that Jack's more than a little nervous about coming back to my place."
        "And it's kind of making me feel confused as to just why that should be."
        "Because we just had a date that seemed to go well, maybe even great."
        "Yet as we walk in through the front-door, he's glancing over his shoulder."
        bree.say "Jack..."
        bree.say "What's the matter with you?"
        bree.say "I don't live with my parents."
        bree.say "My dad's not about to appear out of the shadows!"
        "Mentioning my dad makes an image of him flash into my mind."
        "And I push it away with a shudder of trepidation and concern for Jack."
        "I know that he's nowhere near ready for that introduction just yet!"
        show jack smile
        jack.say "I know that, [hero.name]."
        jack.say "It's not your folks that I'm worried about."
        show jack sad
        jack.say "It's [mike.name]!"
        "I stare at Jack for a moment, amazed at what he just said."
        bree.say "Huh?"
        bree.say "What's [mike.name] got to do with it?"
        show jack normal
        jack.say "Well..."
        jack.say "He is my friend, [hero.name]."
        jack.say "And you're his smoking hot housemate."
        show jack blush
        jack.say "He might be jealous of us...you know, doing stuff together!"
        "I let out a snort of laughter and shake my head."
        bree.say "[mike.name] doesn't tell me what to do, Jack."
        bree.say "And if he's a real friend, he won't resent you getting some action either."
        bree.say "And if he does, then he can go piss up a rope!"
        jack.say "Shh!"
        show jack normal
        jack.say "What if he hears you?"
        show jack at center, zoomAt(1.5, (640, 1040))
        "I shake my head and grab Jack by the hand."
        show jack at center, zoomAt(1.5, (940, 1040)) with ease
        "And then I pull him up the stairs after me."
        "As we're climbing them, I make sure to shout out."
        bree.say "Hey, [mike.name]..."
        bree.say "I'm taking Jack to my bedroom now."
        bree.say "And I'm going to have him fuck my brains out, okay?"
        show bg secondfloor
        show jack surprised at center, zoomAt(1.5, (640, 1040))
        with fade
        bree.say "So I don't want to be disturbed."
        bree.say "Oh, and that goes for you too, Sasha!"
        "At first Jack looks like he's going to have a genuine heart attack."
        "But as we get to the landing and make it to my room, his mood slowly changes."
        scene bg bedroom4
        show jack blush
        with fade
        "Once he sees that there's nobody shouting back, he seems to relax."
        show jack smile
        "And when I close the door to my room behind us, he's smiling again."
        jack.say "Wow, [hero.name]..."
        show jack normal
        jack.say "Do you really not care what your housemates think?"
        bree.say "Nah, Jack, I don't!"
        "I mean, it does help that I know [mike.name] and Sasha are both out tonight."
        "But what Jack doesn't know won't hurt him."
        "Plus I can see that he's already getting off on thinking I'm a bad girl."
        "Which promises good things for him and me alike!"
        "Keen to keep up the image, I start to strip-off my clothes."
        show jack surprised
        "Which makes Jack's eyes almost pop out of their sockets."
        jack.say "Are...are we going to start straight away?"
        jack.say "I always thought that girls wanted a guy to do stuff first."
        show jack blush
        jack.say "You know...like talk and stare longingly into their eyes?"
        bree.say "Nah, Jack..."
        bree.say "Not tonight."
        bree.say "Tonight I just want to fuck!"
        "Jack can't seem to believe his ears."
        show jack surprised
        "And his eyes must be causing him similar issues too."
        "Because he goggles as I crawl backwards onto the bed, totally naked."
        show jack perv
        "Then he nearly chokes as I part my legs and give him a view of what's between them."
        "I don't even need to tell him what to do next."
        "Instead Jack starts to pull of his clothes in an almost desperate manner."
        "I watch in amusement as he tosses them aside and then approaches the bed."
        show jack naked at center, zoomAt(1.5, (640, 1040)) with fade
        "By now Jack's pretty much sinking down onto his knees as he comes closer."
        "Like the sight of my pussy is somehow hypnotising him."
    elif game.week_day % 3 == 1:
        scene bg street
        show jack smile
        with fade
        "Tonight's been one of those dates when everything just seems to right."
        "The place where Jack and I spent the evening was perfect, buzzing with atmosphere."
        show jack happy
        "And we were getting on better than ever, talking and laughing all night long."
        scene bg taxi
        show bg taxi car
        with fade
        "So much so that I almost feel like something's changed between us because of it."
        "Like we've moved on to a new stage in our relationship."
        "Though I'm not sure of just what's changed just yet."
        "But suffice to say that neither of us is going home alone tonight!"
        "So when the taxi pulls up at my place, I haul Jack out with me."
        jack.say "Whoa..."
        jack.say "This is you, [hero.name]."
        jack.say "I live miles away from here!"
        bree.say "You're not going home tonight, Jack..."
        bree.say "You're staying over here - with me!"
        "For perhaps the first time since we started dating, Jack just gets it."
        "He understands what I'm saying to him without needing to have it explained."
        "And he nods eagerly, taking hold of my hand as he does so."
        scene bg house
        show jack normal
        with fade
        "Then he lets me lead him up the path to the front door."
        "Letting us in, I gesture for him to follow me and be quiet."
        scene bg livingroom
        show jack normal
        with fade
        "Because the last thing I want is for [mike.name] or Sasha to see us."
        "I don't want a sarcastic comment from her."
        "Or for him to spot one of his oldest friends."
        "Either would be painfully awkward right now."
        scene bg bedroom4
        show jack normal at center, zoomAt (1.5, (640, 1040))
        with fade
        "Thankfully we make it to my bedroom door without incident."
        "And I waste no time in hustling Jack inside, then closing it behind us."
        "As soon as I'm sure we're alone, I start to pull off my clothes."
        "But when I look up from tossing some of them aside, I see Jack's staring at me."
        "And what's more puzzling is that he's not getting undressed himself."
        bree.say "Jack..."
        bree.say "What's the problem?"
        bree.say "Why aren't you getting undressed too?"
        "Jack stares at me in silence for a moment."
        "Then he kind of shakes his head and blinks at me."
        jack.say "S...sure, [hero.name]..."
        show jack smile
        jack.say "Of course..."
        show jack normal
        jack.say "It's just that..."
        "Jack trails off before he finishes what he was going to say."
        "Almost like he's embarrassed by the mere thought of it."
        bree.say "It's okay, Jack..."
        bree.say "You can say what you were about to say."
        bree.say "It's important that we're honest with each other."
        show jack blush
        "Jack smiles and I see he's blushing a little too."
        jack.say "I'm sorry, [hero.name]..."
        jack.say "I'm still not used to this kind of thing."
        jack.say "To a hot girl wanting to do stuff with me, you know?"
        "It's times like this when I remember how innocent Jack can be."
        "And how sweet it is to know that he's so stoked to be in a relationship with me."
        "So many guys are arrogant assholes, and they think I should be grateful to be with them."
        "It's such a novelty to be with a guy that worships me the way Jack does."
        "And I try the best I can not to let that go to my head as well."
        hide jack
        show jack kiss
        with fade
        $ jack.flags.kiss += 1
        "Walking over to where Jack's standing, I lean in and kiss him on the lips."
        "Then I begin to gently pull off his clothes, helping him to undress."
        hide jack kiss
        show jack naked at center, zoomAt(1.5, (640, 1040))
        with fade
    else:
        scene bg street with fade
        "Normally I like to have a guy be all manly and masterful when I take him home after a date."
        "That's not always the way that I feel and it's not like I want to be dominated all the time either."
        "But it's just one of those habits that I've fallen into."
        "You know, something I kind of like?"
        "But with Jack, it's a totally different story."
        "I mean, there's no way that you could call the guy a confident, alpha male type."
        "He's more of a typical nerd, into comic-books, cartoons and roleplaying games!"
        "But that means he's kind of a big kid, someone I can really have fun with."
        "And if you manage to get things right, that's as great as being with any man's man."
        scene bg house
        show jack normal
        with fade
        "Like right now, we're walking up to the front-door of my place."
        "We just got back from a date that went really well."
        "In fact, it was a genuine riot!"
        "Jack's had me in stitches all night, laughing till tears ran down my cheeks."
        "And now we're sneaking inside the house, trying to be quiet."
        "Like a couple of naughty kids that have stayed out way past curfew."
        "Before, Jack was pretty worried about [mike.name] spotting us coming home like this."
        "But now he's kind of over it, and the whole thing's more like a joke to him."
        scene bg livingroom with fade
        show jack at right with easeinright
        "As I open the door and he follows me inside, Jack holds a finger up to his lips."
        jack.say "Shh!"
        jack.say "We have to be extra quiet, [hero.name]..."
        show jack at center with ease
        jack.say "Nobody can know that we're even here!"
        "I have to cover my mouth to keep from bursting out laughing."
        "Sure, that line might not sound too funny to you."
        "But we've had a couple of drinks tonight."
        "And I'm totally on Jack's wavelength right now."
        "So to me it's simply hilarious."
        bree.say "I am being quiet, Jack!"
        bree.say "Can't you hear that I'm whispering?"
        bree.say "Ooh..."
        bree.say "I think I can hear [mike.name] and Sasha snoring too!"
        show jack smile
        "Now it's Jack's turn to stifle his laughter."
        "I take advantage of this by grabbing hold of his hand."
        "And then I lead him straight up the stairs and to my bedroom door."
        "Taking one last look around, I open it and push him inside."
        scene bg bedroom4
        show jack blush
        with fade
        "Jack seems to be taken by surprise by the shove."
        "Because he stumbles into the room, almost falling on his face."
        "But somehow he manages to save himself, turning as he goes."
        "This means that he staggers backwards into the edge of my bed."
        "And then he sits down hard, the frame and mattress creaking under his weight."
        "Closing the door, I hurry over to where he's sitting."
        "Jack makes to get up, but I shake my head and push him back down."
        bree.say "Uh-uh..."
        bree.say "Nope..."
        bree.say "You sit right there, Jack..."
        bree.say "Because I'm going to give you a super sexy, strip-tease!"
        "In my own mind I sound like a complete sex-kitten."
        "I wink at Jack to underline my intentions."
        "But part of me is worried that I look like a drunken mess instead."
        "Though none of that seems to bother Jack in the slightest."
        show jack perv
        "Instead he nods and watches me with wide eyes, eager to see what I have in mind."
        "I do the best I can to make it sensual and sexy."
        "Though my balance doesn't seem to be holding up."
        "And more than once it takes multiple attempts for me to get certain things off."
        "But finally I manage to escape my bra and push down my panties."
        "Then I raise my hands in the air and take a deep bow."
        bree.say "Ta-da!"
        "When I stand up, I feel more than a little dizzy."
        "But I see that Jack's staring at me."
        "And he looks like he has amazement in his eyes!"
        bree.say "Wha...what's the matter?"
        bree.say "Did I miss something out?"
        "I start staring at myself, looking to see if I'm actually naked."
        show jack blush
        jack.say "Whoa, [hero.name]..."
        jack.say "You look SO amazing!"
        jack.say "It just...just hits me sometimes, you know?"
        jack.say "That I'm actually going out with the hottest girl in the world!"
        "Oh man, that gets me right in the feels!"
        "I know Jack's not a lady-killer, far from it."
        "But that also means that he's honest about his feelings."
        "And that compliment just lit a fire inside of me!"
        show jack at center, zoomAt(1.5, (640, 1040)) with hpunch
        "Without saying a word, I hurry over to where Jack's sitting."
        "And I start to pull off his clothes like my life depends on it!"
        jack.say "Wha..."
        jack.say "What's the matter, [hero.name]?"
        jack.say "Could you..."
        jack.say "Could you maybe...slow down?"
        "I hear what Jack's saying loud and clear."
        "But I just shake my head and keep on going."
        bree.say "No way, Jack..."
        bree.say "Not until I get what I want!"
        "Pretty soon I've got jack stripped down to his shorts."
        show jack naked
        "And these are proving the hardest thing to get off of him."
        "I'm tugging away at them for all I'm worth, straining with the effort."
        "So when I finally get them off, they fly away like something shot out of a catapult!"
        "That done, I stand back to admire my handiwork."
        "And Jack looks up at me with a nervous smile on his face."
        jack.say "Erm..."
        jack.say "[hero.name]..."
        jack.say "That way you're looking at me right now..."
        jack.say "It's kind of making me nervous!"
        "I offer Jack what I hope is a reassuring smile."
        "And at the same time I reach down between his legs."
        "Because what I'm really interested in is right there."
    return

label jack_fuck_date_missionary(sexperience_min):
    scene jack missionary
    show jack missionary mcalone
    with fade
    jack.say "Whoa..."
    jack.say "What should I do now, [hero.name]?"
    jack.say "I'll do anything you tell me to!"
    menu:
        "Make him eat my pussy":
            "I can't help wondering if Jack means what he's saying."
            "But then a good way to find out occurs to me."
            "So I lean back on my elbows and point to my pussy."
            bree.say "Okay, Jack..."
            bree.say "I want you to eat my pussy."
            bree.say "Really go to town on me, yeah?"
            "For a moment I think that Jack's going to go back on his word."
            show jack missionary lick -mcalone
            "Then he surprises me by simply nodding and leaning down between my thighs."
            "I have to admit that I'm not prepared for this in the slightest."
            "I'd been expecting to have to coax Jack into going down on me."
            "So now I find myself caught on the hop as he gets straight to work."
            "And the very second that I feel his lips touch mine, I feel a jolt of pleasure."
            "It's weird, because I can tell straight away that Jack's not a veteran at this."
            show jack missionary pain
            "Yet there's something about the way I can feel him exploring down there."
            "He's not taking anything for granted or skipping ahead."
            "Instead I'm treated to an intimate experience like no other."
            show jack missionary normal
            "Jack takes his time, lips and now tongue getting in on the act."
            "At first it feels like nothing more than gentle kisses around the edge."
            "But then he seems to turn his head sideways."
            "This means that his tongue is able to slide neatly into my pussy."
            "From this point on, Jack doesn't hold back."
            "My hands grab hold of the bedclothes beneath me."
            show jack missionary pleasure
            "And my back starts to bend, raising my groin up from the bed."
            "Jack follows every move I make, holding onto my thighs as he does so."
            "He doesn't let up for a second, even as I bend like a bow."
            "The further back I lean the more effort Jack seems to put into it."
            "And this goes on until my head is actually touching the mattress."
            bree.say "Oh..."
            show jack missionary shaking at startle(0.05,-10)
            bree.say "Oh god..."
            bree.say "Jack!"
            show jack missionary ahegao squirt with vpunch
            "I teeter over the edge and into an orgasm as Jack's still going at it."
            "In fact I'm not sure he even notices it's happening."
            "That is until my body goes limp, like a puppet with severed strings."
            "And I collapse into a heap on the bed before him."
        "Guide him to my pussy":
            "I take a moment to get my mind focused on what I want."
            "And once I do, there's no question as to just what that is."
            bree.say "My pussy, Jack..."
            bree.say "I want you in my pussy!"
            "Jack nods eagerly, clearly delighted with my request."
            show jack missionary -mcalone
            "And he starts to make for the objective I just gave him."
            call check_condom_usage (jack) from _call_check_condom_usage_119
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show jack missionary condom
            "Jack's so keen to get on with the job that he doesn't give me time to prepare."
            "In fact I can't even get myself into a comfortable position before he gets started."
            "I end up getting pushed backwards as he hurries to grab hold of my thighs."
            "This means that I'm almost bent over backwards, but he doesn't seem to notice."
            "Instead he's focused solely on giving me what he thinks I want."
            bree.say "Jack..."
            show jack missionary pain
            bree.say "W...wait a second..."
            show jack missionary normal
            bree.say "I'm not ready...to go!"
            jack.say "What was that, [hero.name]?"
            jack.say "Did you just tell me to go?"
            jack.say "Okay, whatever you say!"
            "Before I can say another word, Jack thrusts himself forwards."
            "And I feel the head of his cock make contact with my pussy."
            "I had no idea I was as ready for what he's wanting to give me."
            show jack missionary vaginal pleasure
            "The moment we touch, I pretty much lose the power of speech."
            "This means I can't tell Jack to slow down or let me get comfortable."
            show jack missionary normal
            "His first thrust just slides along the lips of my pussy."
            "His second follows a moment later, and I can already feel my resistance fading."
            show jack missionary pain
            "The third see my pussy open a little, enough for him to push further."
            "But the fourth one sees my lips part like an opening flower."
            "This time Jack pushes for all he's worth, and then he's inside of me."
            show jack missionary pleasure
            "He keeps on moving, not stopping until he's totally filled me."
            "From the sounds he's making, I'm sure Jack's enjoying himself."
            show jack missionary normal
            "But it's impossible for me to look up and check the expression on his face."
            "By now I'm bending over backwards, my head and feet on the mattress."
            "But almost no other part of me is even in contact with it."
            "Jack's holding me up, and at the same time he's folding me in half."
            "And I can already feel him starting to move inside of me."
            "I couldn't tell Jack to stop even if I wanted to."
            "And the possibility of me wanting him to stop becomes more remote with each passing second."
            "The reason for that is how Jack's throwing himself into making love to me."
            "He seems determined to show me just what he's capable of between the sheets."
            show jack missionary speed with hpunch
            "Which also means that he's picking up speed all the time."
            "And that same determination is already leaving me helpless."
            "Other guys might be sure of themselves, cocky and full of confidence."
            "But Jack's far too much of a nerd to think he's a god-level lover."
            "That means he's putting every ounce of effort he can muster into it."
            show jack missionary pleasure
            "I mean, he is good in bed - really good!"
            "But the fact he doesn't know that means I'm reaping the benefits."
            "He's so good that I can feel my senses being overwhelmed."
            "And I start to lose track of how long we've been doing this."
            "One part of my mind is sure that we've been at it for hours."
            "But another thinks that we just started a couple of seconds ago."
            "Either way, I know that I can't keep up this pace forever."
            "Already I can feel the sensation of an orgasm building in me."
            "It starts deep down, in the very core of my body."
            show jack missionary shaking insert with hpunch
            "Then suddenly it pulses outwards, taking over my senses."
            "I have no idea if Jack knows that it's happening or not."
            "But I can certainly sense the effect that it's having on him."
            "The most pressing of those effects being that he's about to cum too!"
            call cum_reaction (jack, 'vaginal', sexperience_min) from _call_cum_reaction_213
            if _return == "vaginal_outside":
                "Using the very last of my energy, I desperately wriggle and squirm."
                "It's all in an effort to free myself before it's too late."
                "And at the very last moment possible, I succeed."
                show jack missionary -vaginal at startle(0.05,-10)
                "Jack's cock pops out of me and I hear him gasp from the sensation."
                show jack missionary cumshot with hpunch
                "A second later my own orgasm hits too."
                show jack missionary ahegao with hpunch
                $ jack.love += 1
                "And it hits me like a tidal wave, sweeping me along in it's wake."
                "Finally the strength in my muscles gives out."
                "And I collapse onto the mattress, motionless and spent."
            elif _return == "vaginal_condom":
                "Right now I'm glad that we decided to use a condom."
                "Because I don't know if I could move a muscle to stop what's happening."
                show jack missionary ahegao with hpunch
                "Jack shoots his load into me when he's as deep as he can get."
                $ jack.love += 2
                with hpunch
                "And it hits me like a tidal wave, sweeping me along in it's wake."
                "Finally the strength in my muscles gives out."
                "And I collapse onto the mattress, motionless and spent."
            else:
                "Right now I can't move a muscle to stop what's happening."
                with hpunch
                "Jack shoots his load into me when he's as deep as he can get."
                show jack missionary creampie ahegao with hpunch
                "And it hits me like a tidal wave, sweeping me along in it's wake."
                $ jack.love += 5
                $ jack.impregnate()
                "Finally the strength in my muscles gives out."
                "And I collapse onto the mattress, motionless and spent."
        "Guide him to my ass" if hero.sexperience >= (sexperience_min + 5):
            "I take a moment to get my mind focused on what I want."
            "And once I do, there's no question as to just what that is."
            bree.say "My ass, Jack..."
            bree.say "I want you in my ass!"
            "Jack nods eagerly, clearly delighted with my request."
            show jack missionary -mcalone
            "And he starts to make for the objective I just gave him."
            "In fact, Jack's so keen to get on with the job that he doesn't give me time to prepare."
            "In fact I can't even get myself into a comfortable position before he gets started."
            "I end up getting pushed backwards as he hurries to grab hold of my thighs."
            "This means that I'm almost bent over backwards, but he doesn't seem to notice."
            "Instead he's focused solely on giving me what he thinks I want."
            bree.say "Jack..."
            show jack missionary pain
            bree.say "W...wait a second..."
            show jack missionary normal
            bree.say "I'm not ready...to go!"
            jack.say "What was that, [hero.name]?"
            jack.say "Did you just tell me to go?"
            jack.say "Okay, whatever you say!"
            "Before I can say another word, Jack thrusts himself forwards."
            "And I feel the head of his cock make contact with my hole."
            "I had no idea I was as ready for what he's wanting to give me."
            show jack missionary anal pleasure
            "The moment we touch, I pretty much lose the power of speech."
            "This means I can't tell Jack to slow down or let me get comfortable."
            show jack missionary normal
            "His first thrust just slides around the ring of my ass."
            "His second follows a moment later, and I can already feel my resistance fading."
            show jack missionary pain
            "The third see my ass open a little, enough for him to push further."
            "But the fourth one sees my muscles relax like an opening flower."
            "This time Jack pushes for all he's worth, and then he's inside of me."
            show jack missionary pleasure
            "He keeps on moving, not stopping until he's totally filled me."
            "From the sounds he's making, I'm sure Jack's enjoying himself."
            show jack missionary normal
            "But it's impossible for me to look up and check the expression on his face."
            "By now I'm bending over backwards, my head and feet on the mattress."
            "But almost no other part of me is even in contact with it."
            "Jack's holding me up, and at the same time he's folding me in half."
            "And I can already feel him starting to move inside of me."
            "I couldn't tell Jack to stop even if I wanted to."
            "And the possibility of me wanting him to stop becomes more remote with each passing second."
            "The reason for that is how Jack's throwing himself into making love to me."
            "He seems determined to show me just what he's capable of between the sheets."
            show jack missionary speed with hpunch
            "Which also means that he's picking up speed all the time."
            "And that same determination is already leaving me helpless."
            "Other guys might be sure of themselves, cocky and full of confidence."
            "But Jack's far too much of a nerd to think he's a god-level lover."
            "That means he's putting every ounce of effort he can muster into it."
            show jack missionary pleasure
            "I mean, he is good in bed - really good!"
            "But the fact he doesn't know that means I'm reaping the benefits."
            "He's so good that I can feel my senses being overwhelmed."
            "And I start to lose track of how long we've been doing this."
            "One part of my mind is sure that we've been at it for hours."
            "But another thinks that we just started a couple of seconds ago."
            "Either way, I know that I can't keep up this pace forever."
            "Already I can feel the sensation of an orgasm building in me."
            "It starts deep down, in the very core of my body."
            show jack missionary shaking insert with hpunch
            "Then suddenly it pulses outwards, taking over my senses."
            "I have no idea if Jack knows that it's happening or not."
            "But I can certainly sense the effect that it's having on him."
            "The most pressing of those effects being that he's about to cum too!"
            call cum_reaction (jack, 'anal', sexperience_min) from _call_cum_reaction_214
            if _return == "anal_inside":
                "Right now I'm glad that we decided to go with the ass."
                "Because I don't know if I could move a muscle to stop what's happening."
                with hpunch
                "Jack shoots his load into me when he's as deep as he can get."
                show jack missionary creampie ahegao with hpunch
                $ jack.love += 2
                "And it hits me like a tidal wave, sweeping me along in it's wake."
                "Finally the strength in my muscles gives out."
                "And I collapse onto the mattress, motionless and spent."
            else:
                "Using the very last of my energy, I desperately wriggle and squirm."
                "It's all in an effort to free myself before it's too late."
                "And at the very last moment possible, I succeed."
                show jack missionary -anal
                "Jack's cock pops out of me and I hear him gasp from the sensation."
                show jack missionary cumshot with hpunch
                "A second later my own orgasm hits too."
                show jack missionary ahegao with hpunch
                $ jack.sub += 1
                "And it hits me like a tidal wave, sweeping me along in it's wake."
                "Finally the strength in my muscles gives out."
                "And I collapse onto the mattress, motionless and spent."
    return

label jack_fuck_date_reverse_cowgirl(sexperience_min=0):
    hide jack
    show jack reverse cowgirl
    with fade
    "Jack gasps as I take hold of his cock and start to stroke it."
    "It had already begun to stir, starting to rise upwards."
    "But now that process is speeding up dramatically!"
    bree.say "Don't worry, Jack..."
    bree.say "I promise to be gentle!"
    jack.say "I..."
    jack.say "I don't know if I believe you, [hero.name]!"
    jack.say "But...don't let that stop you!"
    "I nod, still trying to reassure Jack that he's in good hands."
    "Then I turn my back on him and lower myself onto his lap."
    menu:
        "Guide him to my pussy":
            "I look back over my shoulder at Jack."
            "He hurries meets my eye."
            "And I see that his are as wide as saucers right now!"
            bree.say "Mmm..."
            bree.say "Okay, Jack..."
            bree.say "You're going in through the front-door, okay?"
            "Jack nods eagerly, desperate to show that he's game."
            "But before he can say a word, I turn my head back again."
            call check_condom_usage (jack) from _call_check_condom_usage_129
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show jack reverse cowgirl condom
            "I wonder if I need to be more specific with Jack."
            "You know, tell him exactly what I want him to do and how?"
            "After all, he's not the most confident or experienced of guys!"
            "I could always..."
            show jack reverse cowgirl blush
            bree.say "Whoa..."
            bree.say "Wait...what?"
            "Before I have time to react, I feel Jack's hands taking hold of me."
            "And from that point on, the roles are pretty much switched."
            "Before, I was the one handing out the orders, the one in charge."
            "But now I can feel myself being taken in hand as Jack asserts himself."
            "His cock is already moving beneath me, pushing between my thighs."
            "Then I feel it pressing against my pussy, and the sensation leaves me helpless."
            bree.say "Oh..."
            bree.say "Oh, Jack!"
            show jack reverse cowgirl vaginal
            "No matter what I say, Jack's not stopping to listen."
            "Instead he pulls me downwards, firmly and without hesitation."
            "Of course my body tries as best it can to resist."
            "Muscles down there struggle to keep him out, despite what I want."
            "I'm willing them to surrender with each and every thought."
            "But the very act of resistance makes everything so much more intense."
            "So when the inevitable happens and they start to weaken..."
            "What I feel all but explodes inside of me."
            show jack reverse cowgirl pleasure
            "I'm sinking down slowly, a fraction of an inch at a time."
            "Each one means that Jack fills me just a little more."
            "And each time I feel like it can't get any more overwhelming."
            "Yet each time that's exactly what happens."
            "By the time Jack can't go deeper, I'm leaning back on him."
            "My head's almost resting on his shoulder, so I can see his face."
            "I'm expecting to see an expression of triumph on it."
            "The look of a guy that knows he's got a girl right in the palm of his hand."
            "But instead I'm greeted with that same goofy grin."
            "The one Jack has on his face when he's thrilled with something and just can't hide it."
            "I can't help smiling back, because I know what it means."
            "It means that what Jack's doing to me is on account of his genuine affection."
            "He's not the kind of guy that wants to dominate me, just to have a real good time."
            show jack reverse cowgirl at startle(0.05,-10)
            "Jack's nodding as he starts to move inside of me."
            "And it doesn't take long for me to lose the ability to think so deeply."
            show jack reverse cowgirl at startle(0.05,-10)
            "Because all I can do is lie there and let Jack have his way with me."
            show jack reverse cowgirl at startle(0.05,-10)
            "I never knew he had this much strength and stamina in him."
            show jack reverse cowgirl at startle(0.05,-10)
            "His entire body seems to be moving under me."
            show jack reverse cowgirl at startle(0.05,-10)
            "Which is ironic, as I feel like it's rendered me immobile!"
            show jack reverse cowgirl at startle(0.05,-10)
            "Jack must be doing most of it with his lower body too."
            "Because I can feel his hands roaming all over me."
            show jack reverse cowgirl at startle(0.05,-10)
            "They stroke, tickle and squeeze wherever they go."
            "All of which only makes what I'm feeling more intense."
            "And when Jack's hands inevitably settle on my breasts, all doubles again."
            "With one in each hand, he massages them over and over."
            "My nipples were hard before he found his way to them."
            "And now, as he pinches and pulls at them, they feel harder still."
            "I can hear myself starting to gasp and wail."
            bree.say "J...Jack..."
            show jack reverse cowgirl pain
            bree.say "You're..."
            bree.say "You're going to make me..."
            bree.say "Make me cum!"
            "As soon as the words leave my mouth, they seem to affect Jack."
            "The admission acts like some kind of magic spell."
            show jack reverse cowgirl at startle(0.05,-10)
            "I can feel him twitching and bucking inside of me."
            show jack reverse cowgirl at startle(0.05,-10)
            "At first I can't make sense of it."
            show jack reverse cowgirl at startle(0.05,-10)
            "But then it dawns on me - Jack's about to cum too!"
            call cum_reaction (jack, 'vaginal', sexperience_min) from _call_cum_reaction_237
            if _return == "vaginal_outside":
                "I have just enough time to make the move."
                "Pulling myself upwards and off Jack the moment before it happens."
                show jack reverse cowgirl -vaginal cumshot
                "The both of us gasp as his cock slides out of me."
                with vpunch
                "With one final push, Jack lets go."
                $ jack.love += 1
                show jack reverse cowgirl ahegao cumshot with vpunch
                "And then he shoots his load into the air from between my thighs."
                with vpunch
                "A surge so intense that we both collapse onto the bed once it's done."
            else:
                "There's scarcely time for me to think."
                "Let alone time to actually move a muscle."
                "All I can do is hang on for dear life as it happens."
                "With one final push, Jack lets go."
                show jack reverse cowgirl ahegao creampie with vpunch
                $ jack.love += 5
                $ jack.impregnate()
                "And then he shoots his load into me in one huge surge."
                with vpunch
                "A surge so intense that we both collapse onto the bed once it's done."

        "Guide him to my ass" if hero.sexperience >= (sexperience_min + 5):
            "I look back over my shoulder at Jack."
            "He hurries meets my eye."
            "And I see that his are as wide as saucers right now!"
            show jack reverse cowgirl blush
            bree.say "Mmm..."
            bree.say "Okay, Jack..."
            bree.say "You're going in through the back-door, okay?"
            "Jack nods eagerly, desperate to show that he's game."
            "But before he can say a word, I turn my head back again."
            "I wonder if I need to be more specific with Jack."
            "You know, tell him exactly what I want him to do and how?"
            "After all, he's not the most confident or experienced of guys!"
            "I could always..."
            show jack reverse cowgirl pain
            bree.say "Whoa..."
            bree.say "Wait...what?"
            "Before I have time to react, I feel Jack's hands taking hold of me."
            "And from that point on, the roles are pretty much switched."
            "Before, I was the one handing out the orders, the one in charge."
            "But now I can feel myself being taken in hand as Jack asserts himself."
            "His cock is already moving beneath me, pushing between my thighs."
            "Then I feel it pressing between my buttocks, and the sensation leaves me helpless."
            show jack reverse cowgirl anal
            bree.say "Oh..."
            bree.say "Oh, Jack!"
            "No matter what I say, Jack's not stopping to listen."
            "Instead he pulls me downwards, firmly and without hesitation."
            "Of course my body tries as best it can to resist."
            "Muscles down there struggle to keep him out, despite what I want."
            "I'm willing them to surrender with each and every thought."
            "But the very act of resistance makes everything so much more intense."
            "So when the inevitable happens and they start to weaken..."
            show jack reverse cowgirl pleasure
            "What I feel all but explodes inside of me."
            "I'm sinking down slowly, a fraction of an inch at a time."
            "Each one means that Jack fills me just a little more."
            "And each time I feel like it can't get any more overwhelming."
            "Yet each time that's exactly what happens."
            "By the time Jack can't go deeper, I'm leaning back on him."
            "My head's almost resting on his shoulder, so I can see his face."
            "I'm expecting to see an expression of triumph on it."
            "The look of a guy that knows he's got a girl right in the palm of his hand."
            "But instead I'm greeted with that same goofy grin."
            "The one Jack has on his face when he's thrilled with something and just can't hide it."
            "I can't help smiling back, because I know what it means."
            "It means that what Jack's doing to me is on account of his genuine affection."
            "He's not the kind of guy that wants to dominate me, just to have a real good time."
            show jack reverse cowgirl at startle(0.05,-10)
            "Jack's nodding as he starts to move inside of me."
            show jack reverse cowgirl at startle(0.05,-10)
            "And it doesn't take long for me to lose the ability to think so deeply."
            show jack reverse cowgirl at startle(0.05,-10)
            "Because all I can do is lie there and let Jack have his way with me."
            show jack reverse cowgirl at startle(0.05,-10)
            "I never knew he had this much strength and stamina in him."
            show jack reverse cowgirl at startle(0.05,-10)
            "His entire body seems to be moving under me."
            show jack reverse cowgirl at startle(0.05,-10)
            "Which is ironic, as I feel like it's rendered me immobile!"
            show jack reverse cowgirl at startle(0.05,-10)
            "Jack must be doing most of it with his lower body too."
            "Because I can feel his hands roaming all over me."
            "They stroke, tickle and squeeze wherever they go."
            show jack reverse cowgirl at startle(0.05,-10)
            "All of which only makes what I'm feeling more intense."
            "And when Jack's hands inevitably settle on my breasts, all doubles again."
            "With one in each hand, he massages them over and over."
            "My nipples were hard before he found his way to them."
            "And now, as he pinches and pulls at them, they feel harder still."
            show jack reverse cowgirl at startle(0.05,-10)
            "I can hear myself starting to gasp and wail."
            bree.say "J...Jack..."
            bree.say "You're..."
            show jack reverse cowgirl pain
            bree.say "You're going to make me..."
            bree.say "Make me cum!"
            "As soon as the words leave my mouth, they seem to affect Jack."
            show jack reverse cowgirl at startle(0.05,-10)
            "The admission acts like some kind of magic spell."
            show jack reverse cowgirl at startle(0.05,-10)
            "I can feel him twitching and bucking inside of me."
            "At first I can't make sense of it."
            show jack reverse cowgirl at startle(0.05,-10)
            "But then it dawns on me - Jack's about to cum too!"
            call cum_reaction (jack, 'anal', sexperience_min) from _call_cum_reaction_238
            if _return == "anal_inside":
                "There's scarcely time for me to think."
                "Let alone time to actually move a muscle."
                "All I can do is hang on for dear life as it happens."
                with vpunch
                "With one final push, Jack lets go."
                show jack reverse cowgirl creampie ahegao with vpunch
                "And then he shoots his load into me in one huge surge."
                with vpunch
                $ jack.love += 2
                "A surge so intense that we both collapse onto the bed once it's done."
            else:
                "I have just enough time to make the move."
                "Pulling myself upwards and off Jack the moment before it happens."
                "The both of us gasp as his cock slides out of me."
                show jack reverse cowgirl -anal cumshot with vpunch
                "With one final push, Jack lets go."
                show jack reverse cowgirl ahegao with vpunch
                "And then he shoots his load into the air from between my thighs."
                $ jack.sub += 1
                with vpunch
                "A surge so intense that we both collapse onto the bed once it's done."
    return

label jack_fuck_date_doggy(sexperience_min=0):
    show jack naked
    menu:
        "Use collar":
            "Once we're both naked, I walk over to the bedside table and open the drawer."
            "Reaching inside, I pull out the collar and leash that I always keep in there."
            "And turning to face Jack, I strap the collar around my neck."
            show jack at center, zoomAt(1.5, (640, 1040))
            "Then I walk back over to where he's standing and hand the leash to him."
            "Jack looks down at the leash in his hand, then up at me."
            bree.say "It's okay, Jack..."
            bree.say "I trust you more than anyone else in the world."
            bree.say "That's why I'm putting my leash in your hands."
            "Jack seems to understand what I'm saying, as he nods."
            "Then he pulls the leash a little, as if testing it out."
            "And I know that he understands what all of this means."
            scene jack doggy
            show jack doggy grasp mc_collar
            with fade
        "Ask for a spanking":
            "Once we're both naked, I walk over to the bed and kneel down beside it."
            scene jack doggy
            show jack doggy mcalone
            with fade
            "I make sure that my ass is held high in the air as I do so."
            "And then I look back over my shoulder at Jack."
            show jack doggy climax
            bree.say "This girl doesn't just want you, Jack..."
            bree.say "She wants you to spank her too!"
            show jack doggy normal
            "Jack's eyes go wide with surprise."
            "And he takes half a step back too."
            jack.say "You..."
            jack.say "You can't be serious?!?"
            show jack doggy climax
            bree.say "I'm totally serious."
            bree.say "I want you to come over here and spank me."
            bree.say "Come spank this big, round ass of mine!"
            show jack doggy normal
            "Once more shake is all that it takes."
            "And Jack comes sprinting across the room."
            show jack doggy -mcalone spankup with dissolve
            "He kneels behind me, drawing back his hand."
            play sound spank
            show jack doggy spankdown surprised hurt
            with hpunch
            "Then I look the other way as he brings it down on my buttocks."
            "The sound is like the clapping of hands."
            show jack doggy spankdown pain climax
            "And it sends a thrill through my body that almost drowns out the pain."
            "But the pain is tolerable, and gone in the blink of an eye."
            "Whereas the pleasure that it creates in me lingers far longer."
            show jack doggy spankup
            pause 0.3
            show jack doggy spankdown surprised hurt
            play sound spank
            with hpunch
            "Jack seems to be really getting into the swing of it too."
            show jack doggy spankdown pain climax
            "His previous reluctance being replaced by an eagerness to please."
            show jack doggy spankup
            pause 0.3
            show jack doggy spankdown surprised hurt
            play sound spank
            with hpunch
            "And, I suspect, not a small amount of enjoyment on his part too."
            show jack doggy spankdown pain climax
            "In fact I have to be the one to put an end to it."
            show jack doggy spankup
            pause 0.3
            show jack doggy spankdown surprised hurt
            play sound spank
            with hpunch
            "Calling him off before it's too late."
            show jack doggy spankdown pain climax
            bree.say "Jack..."
            bree.say "Ah..."
            bree.say "That's enough..."
            bree.say "Ah..."
            bree.say "Stop before...I cum!"
            show jack doggy spankdown back normal
            "Much to my relief, Jack does as I ask."
            "And as soon as the spanking stops, I climb up and onto the bed."
            "With my buttocks still tingling from the effects of the spanking."
            "But wanting other parts of my body to now become the centre of attention instead."
        "Use dildo":
            "Once we're both naked, I walk over to the bedside table and open the drawer."
            "I pull something out and turn around, holding it up for Jack to see."
            show jack surprised
            jack.say "O...M...G!"
            jack.say "That thing's massive!"
            "I chuckle at Jack's response."
            "And I wave the dildo in my hand around for effect."
            bree.say "What, this?"
            bree.say "This is just my little friend, Jack."
            bree.say "The one that keeps me company when you're not around!"
            scene jack doggy
            show jack doggy mcalone
            with fade
            "I hand it to him and then lean on the edge of the bed."
            "Then I look back over my shoulder at him."
            bree.say "Come on, Jack..."
            bree.say "Get using that thing on me already!"
            "Jack almost jumps out of his skin."
            show jack doggy -mcalone with dissolve
            "But then I see him nod and lean in closer."
            "I take this as my chance to turn my head around."
            show jack doggy closed
            "And I close my eyes, waiting for the fun to begin."
            "At first, Jack seems reluctant, like he's scared he might hurt me."
            "But it doesn't take long for the familiar sensation of the dildo to effect me."
            "I can feel my pussy slowly waking up to what's happening, becoming wet and slick."
            "Jack also seems to notice this, taking advantage and moving faster."
            "And when the inevitable happens, he doesn't hesitate."
            show jack doggy dildo
            "That's when I feel the dildo sink into me, going all the way."
            "After that, Jack's manner becomes more forceful."
            show jack doggy climax pain
            "Before too long I'm panting and moaning, feeling like I'm on the brink."
            "And that's what makes me call an end to the proceedings."
            bree.say "Jack..."
            bree.say "Jack, stop..."
            bree.say "I want you to...to make me cum."
            bree.say "Not the toy!"
            show jack doggy back normal
            "Jack does as he's told, releasing me on the very edge of an orgasm."
        "Ask for a fingering":
            "Once we're both naked, I walk over to the bed and kneel down beside it."
            scene jack doggy
            show jack doggy mcalone
            with fade
            "I make sure that my ass is held high in the air as I do so."
            "And then I look back over my shoulder at Jack."
            show jack doggy climax
            bree.say "This girl doesn't just want you, Jack..."
            bree.say "She wants you to finger her too!"
            show jack doggy normal
            "Jack's eyes go wide with surprise."
            "And he takes half a step back too."
            jack.say "You..."
            jack.say "You can't be serious?!?"
            show jack doggy climax
            bree.say "I'm totally serious."
            bree.say "I want you to come over here and finger me."
            show jack doggy normal
            "Once more shake is all that it takes."
            "And Jack comes sprinting across the room."
            show jack doggy -mcalone with dissolve
            "He kneels behind me, reaching forwards with one hand."
            "At first, Jack seems reluctant, like he's scared he might hurt me."
            "But it doesn't take long for the sensation of his touch to effect me."
            show jack doggy closed
            "I can feel my pussy slowly waking up to what's happening, becoming wet and slick."
            "Jack also seems to notice this, taking advantage and moving faster."
            "And when the inevitable happens, he doesn't hesitate."
            "That's when I feel his finger sink into me, going all the way."
            "After that, Jack's manner becomes more forceful."
            "Before too long I'm panting and moaning, feeling like I'm on the brink."
            "And that's what makes me call an end to the proceedings."
            show jack doggy climax
            bree.say "Jack..."
            bree.say "Jack, stop..."
            bree.say "I want you to...to make me cum."
            bree.say "Not with your finger...with your cock!"
            show jack doggy back normal
            "Jack does as he's told, releasing me on the very edge of an orgasm."
        "Fuck right now":
            "Once we're both naked, I take hold of Jack's hand."
            "And I give it a reassuring squeeze."
            bree.say "It's okay, Jack..."
            bree.say "I trust you more than anyone else in the world."
            bree.say "Now let's have some fun, okay?"
            "Jack seems to understand what I'm saying, as he nods."
            "And I know that he understands what all of this means."
            scene jack doggy
            show jack doggy mcalone
            with fade
    "Once I'm on the bed, Jack doesn't seem to need any more instructions."
    show jack doggy back normal
    "I'm on all fours, and he climbs up behind me, already clapping his hands on my butt."
    "But just as I think he's about to take control for the first time, I hear him speak."
    jack.say "Okay, [hero.name]..."
    jack.say "Where do you want me?"
    "I shrug and set my mind to answering the question."
    "Because I guess I can let that one go."
    menu:
        "Fuck my pussy!":
            show jack doggy climax
            bree.say "Let's keep things simple tonight, Jack..."
            bree.say "You stick that thing right between my thighs, okay?"
            bree.say "And by that, I mean my pussy!"
            show jack doggy normal
            jack.say "Sure thing, [hero.name]..."
            jack.say "You got it!"
            "I can feel Jack moving around on the bed behind me."
            "Getting ready to kick things off, and I can hardly wait."
            call check_condom_usage (jack) from _call_check_condom_usage_130
            if _return == False:
                return "leave_without_gain"
            show jack doggy fuck -grasp -dildo with fade
            "As soon as I feel Jack's weight settling behind me, I know that I'm ready."
            "All of that infectious energy that he possesses is about to be put to good use."
            "And it seems like he's not wasting any time either, as I feel him start to push forwards."
            show jack doggy fuck closed
            "I've already made things as easy as I can for him back there, and he quickly takes advantage."
            "I feel his cock between my thighs, and the sensation sends a shudder through my entire body."
            "Luckily for me, Jack either doesn't notice or else just reads this as a sign of my excitement."
            "With a sensitive guy like him, it could easily be mistaken for unease or reluctance."
            "And the last thing I want right now is for him to break stride and ruin the mood."
            "So it comes as a genuine relief when the tip of his cock brushes against my pussy."
            "The sigh that I can't help letting out is half arousal and half that same sense of relief."
            "Again, Jack does the right thing by taking it as appreciation of his efforts."
            "In fact he starts to stroke it up and down my lower lips."
            "And that makes the sensation so much better in an instant."
            show jack doggy pain climax
            bree.say "Oh yeah..."
            bree.say "Just like that, Jack..."
            bree.say "Keep doing what you're doing!"
            show jack doggy normal
            "My words seem to have the desired effect on Jack, as he redoubles his efforts."
            show jack doggy hurt
            "And there's just no way that my pussy, stubborn as it is, can hope to resist."
            "Slowly it begins to open up, my lips parting a little at a time."
            "And that's exactly how I feel jack sinking into me."
            "Every fraction of an inch seems to increase the pleasure."
            "To make everything feel even better than before."
            "It takes me a moment to realise that Jack's gone as far as he can."
            "That he's all the way inside of me and pausing in that position."
            show jack doggy surprised climax fuck
            "I open my mouth to say something, maybe give more encouragement."
            show jack doggy surprised fuck pleasure fx at startle(0.05,-10)
            "But I don't have the chance to get even the first word out."
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            "Not before Jack begins to move, thrusting back and forth."
            "The change in him is so quick and unexpected."
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck climax at startle(0.05,-10)
            "It catches me totally off-guard and throws me into a state of confusion."
            "And the sounds that comes out instead is a long, low moan of helpless pleasure."
            "But even that isn't enough to break Jack's stride."
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            "Because now he's fucking me with a single-minded dedication."
            "The same kind that he'd normally be devoting to his many nerdy hobbies!"
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            "Which is why I know what it's like to be the very centre of Jack's attentions and passion."
            "All I can do is dig my fingers into the bedclothes and hold on tight."
            show jack doggy fuck closed hurt at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            "I don't want Jack to stop for a moment, and I'm not even sure I could make him."
            "This is one of those times when the only thing to do is ride it out."
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            "That and keep on hoping that I don't pass out of something crazy like that!"
            jack.say "Urgh..."
            jack.say "[hero.name]..."
            jack.say "I think I'm gonna..."
            jack.say "Gonna cum!"
            call cum_reaction (jack, 'vaginal', sexperience_min) from _call_cum_reaction_239
            if _return == "vaginal_outside":
                show jack doggy climax pleasure fuck fx
                bree.say "Quick, Jack..."
                bree.say "Pull out!"
                "Those are the last words I manage to get out before it happens."
                show jack doggy fuck tongueout ahegao fx with vpunch
                "The moment before Jack cums, I sense myself losing it too."
                show jack doggy fuck -fx with vpunch
                "It's so intense that I almost don't feel Jack pulling out."
                show jack doggy fuck tongue -fx with vpunch
                "And I only know that it's happened when he shoot his load over me."
                "Feeling hot, sticky cum spattering down on my butt."
            elif _return == "vaginal_condom":
                "Neither of us need to say another word, because we took precautions."
                show jack doggy fuck tongue fx with vpunch
                "And the moment before Jack cums, I sense myself losing it too."
                show jack doggy fuck tongueout ahegao -fx with vpunch
                "It's so intense that I almost don't feel him lose it inside of me."
                with vpunch
                "The sensation of it mingles with that of my own orgasm."
                "And there's no way to separate the two."
            else:
                show jack doggy climax pleasure fuck fx
                bree.say "Keep going..."
                bree.say "Don't stop now!"
                "Those are the last words I manage to get out before it happens."
                "Jack seems to hear me, doing exactly as he's told."
                show jack doggy fuck tongue fx with vpunch
                "And the moment before he cums, I sense myself losing it too."
                show jack doggy fuck tongueout ahegao -fx with vpunch
                "It's so intense that I almost don't feel him lose it inside of me."
                with vpunch
                "The sensation of it mingles with that of my own orgasm."
                "And there's no way to separate the two."
        "Fuck my ass!" if hero.sexperience >= (sexperience_min + 5):
            show jack doggy climax
            bree.say "Let's mix it up a little tonight, Jack..."
            bree.say "You stick that thing right in the backdoor, okay?"
            bree.say "And by that, I mean my ass!"
            show jack doggy normal
            jack.say "Are...are you serious?!?"
            show jack doggy climax
            bree.say "One hundred percent serious."
            show jack doggy normal
            jack.say "S...sure thing, [hero.name]..."
            jack.say "You got it!"
            "I can feel Jack moving around on the bed behind me."
            "Getting ready to kick things off, and I can hardly wait."
            show jack doggy fuck -grasp -dildo
            "As soon as I feel Jack's weight settling behind me, I know that I'm ready."
            "All of that infectious energy that he possesses is about to be put to good use."
            "And it seems like he's not wasting any time either, as I feel him start to push forwards."
            show jack doggy fuck closed
            "I've already made things as easy as I can for him back there, and he quickly takes advantage."
            "I feel his cock between my thighs, and the sensation sends a shudder through my entire body."
            "Luckily for me, Jack either doesn't notice or else just reads this as a sign of my excitement."
            "With a sensitive guy like him, it could easily be mistaken for unease or reluctance."
            "And the last thing I want right now is for him to break stride and ruin the mood."
            "So it comes as a genuine relief when the tip of his cock brushes against my ass."
            "The sigh that I can't help letting out is half arousal and half that same sense of relief."
            "Again, Jack does the right thing by taking it as appreciation of his efforts."
            "In fact he starts to stroke it up and down between my buttocks."
            "And that makes the sensation so much better in an instant."
            show jack doggy pain climax
            bree.say "Oh yeah..."
            bree.say "Just like that, Jack..."
            bree.say "Keep doing what you're doing!"
            show jack doggy closed normal
            "My words seem to have the desired effect on Jack, as he redoubles his efforts."
            show jack doggy hurt
            "And there's just no way that my ass, stubborn as it is, can hope to resist."
            "Slowly it begins to open up, my muscles relaxing a little at a time."
            "And that's exactly how I feel jack sinking into me."
            "Every fraction of an inch seems to increase the pleasure."
            "To make everything feel even better than before."
            "It takes me a moment to realise that Jack's gone as far as he can."
            "That he's all the way inside of me and pausing in that position."
            show jack doggy surprised climax fuck
            "I open my mouth to say something, maybe give more encouragement."
            show jack doggy surprised fuck pleasure fx at startle(0.05,-10)
            "But I don't have the chance to get even the first word out."
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            "Not before Jack begins to move, thrusting back and forth."
            "The change in him is so quick and unexpected."
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            "It catches me totally off-guard and throws me into a state of confusion."
            "And the sounds that comes out instead is a long, low moan of helpless pleasure."
            "But even that isn't enough to break Jack's stride."
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            "Because now he's fucking me with a single-minded dedication."
            "The same kind that he'd normally be devoting to his many nerdy hobbies!"
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            "Which is why I know what it's like to be the very centre of Jack's attentions and passion."
            "All I can do is dig my fingers into the bedclothes and hold on tight."
            show jack doggy fuck closed hurt at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            "I don't want Jack to stop for a moment, and I'm not even sure I could make him."
            "This is one of those times when the only thing to do is ride it out."
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            pause 0.2
            show jack doggy fuck at startle(0.05,-10)
            "That and keep on hoping that I don't pass out of something crazy like that!"
            jack.say "Urgh..."
            jack.say "[hero.name]..."
            jack.say "I think I'm gonna..."
            jack.say "Gonna cum!"
            call cum_reaction (jack, 'anal', sexperience_min) from _call_cum_reaction_240
            if _return == "anal_inside":
                show jack doggy climax pleasure fuck fx
                bree.say "Keep going..."
                bree.say "Don't stop now!"
                "Those are the last words I manage to get out before it happens."
                "Jack seems to hear me, doing exactly as he's told."
                show jack doggy fuck tongue fx with vpunch
                "And the moment before he cums, I sense myself losing it too."
                show jack doggy fuck tongueout ahegao -fx with vpunch
                "It's so intense that I almost don't feel him lose it inside of me."
                with vpunch
                "The sensation of it mingles with that of my own orgasm."
                "And there's no way to separate the two."
            else:
                show jack doggy climax pleasure fuck fx
                bree.say "Quick, Jack..."
                bree.say "Pull out!"
                "Those are the last words I manage to get out before it happens."
                show jack doggy fuck tongueout ahegao -fx with vpunch
                "The moment before Jack cums, I sense myself losing it too."
                with vpunch
                "It's so intense that I almost don't feel Jack pulling out."
                show jack doggy fuck tongue with vpunch
                "And I only know that it's happened when she shoot his load over me."
                "Feeling hot, sticky cum spattering down on my butt."
    $ jack.love += 2
    return

label jack_fuck_date_vip_doggy_female(sexperience_min=0):
    "I'm thinking that I'm going to have to coax Jack into getting intimate with me."
    "That he's going to need to be lead by the hand the whole way."
    "But Jack takes me by surprise a moment later."
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene drink_room_club as bg zorder 1
    show jack kiss date zorder 2
    show drink_room_fg_club as fg zorder 3
    with hpunch
    $ jack.flags.kiss += 1
    "Because he all but pounces on me!"
    "I'm overwhelmed at first, unable to respond."
    "But then I remember that this is exactly what I wanted him to do."
    "And so I just lean into it, letting things run their natural course."
    "Before I know it, we're locked in a passionate embrace."
    "Kissing like our lives depend on it and tearing off each other's clothes."
    show jack kiss naked zorder 2 with dissolve
    "Somehow I manage to get naked first, which means I have the upper hand."
    "And for some reason I can't fathom, I want to see Jack assert himself."
    "Maybe it's a desire to have him drop the wide-eyed and innocent act."
    "Or maybe I just want to be fucked like a bitch in heat right now."
    scene jack doggy
    show jack doggy mcalone nightclub
    with fade
    "Whatever the reason, I get down on all fours in front of Jack."
    "And then I shake my ass at him, just to make my desires clear."
    show jack doggy climax mcalone nightclub
    bree.say "Come on, Jack..."
    bree.say "What are you waiting for?"
    show jack doggy normal -mcalone nightclub with dissolve
    jack.say "Okay, [hero.name], okay..."
    jack.say "I'm on it!"
    jack.say "But where do you want me?"
    menu:
        "Guide him to my pussy":
            show jack doggy climax nightclub
            bree.say "Where do you think, Jack?"
            bree.say "On top of me, now!"
            bree.say "And while you're at it, use the front door too!"
            show jack doggy normal nightclub
            "Looking back over my shoulder, I see Jack nodding eagerly."
            show jack doggy fuck happy nightclub
            "And then he lowers himself down and onto my back."
            "It's all I can do to keep from shivering as I feel him touch me."
            "Because the familiar feel and weight of his body is already exciting me."
            "I know that cute belly of his is really a fuel tank."
            "One that belongs to a genuine love-making machine!"
            "My instinct is to keep looking back over my shoulder."
            "But I somehow manage to fight it, leaving Jack to his allotted task."
            "And pretty soon my reward is to feel his hands on my haunches."
            "He's neither hesitant nor too forceful in the way he holds me."
            "Getting things just right and making me feel safe in his hands."
            "Though a moment later I feel the first brush of his cock against my thighs."
            show jack doggy pain fuck nightclub
            "And I find it hard to keep my head clear and my thoughts in order."
            "As Jack begins to push his way between my legs, it only gets worse."
            show jack doggy closed fuck nightclub
            "Part of me knows that I should keep myself under control."
            "That I should maintain my dignity while he's on me."
            show jack doggy pain fuck nightclub
            "But another part of me has already surrendered to the idea of being fucked."
            "The purely animal part of me that wants gratification at any cost."
            "The battle between the two is settled as soon as Jack makes his next move."
            show jack doggy closed climax fuck nightclub
            "When I feel the head of his cock pressing against my pussy, I'm sold."
            "All I want is for him to get inside of me and down to business."
            "But no matter what my head wants, my body is more stubborn."
            "There's no way that my pussy's going to just open up to him."
            "And so I feel Jack begin to stroke and tease down there."
            show jack doggy pain climax nightclub
            "All of which only serves to add to the pleasure I'm experiencing."
            "It's a sensation that I could stand for a very long time."
            "Yet after showing such reluctance to begin with, my body soon seems to change it's mind."
            "Because I can feel the lips down there starting to part."
            show jack doggy surprised climax fuck nightclub
            "And little by little, Jack's cock begins to sink into me."
            "Though there's nothing little about it!"
            "He goes slowly at first, probably as overwhelmed as I am."
            show jack doggy normal back fuck nightclub
            "But the deeper he goes, the more his confidence seems to grow."
            "So by the time he can't get any deeper, I'm in the palm of his hand."
            "And from that point on, Jack doesn't look back once."
            "Before I know it, he's thrusting away at me."
            "The feeling of him building up until it's overwhelming my senses."
            "I thought I was going to be the one giving the orders here."
            show jack doggy surprised fuck pleasure nightclub fx at startle(0.05,-10)
            "But now Jack's firmly in charge, and I'm reaping the benefits."
            "Every time he sinks into me, my entire body shakes."
            "And when he pulls back again, it only gets more intense."
            "My head is bowed, down below my shoulders, swaying from side to side."
            "I don't know how long I can keep this up before Jack makes me cum."
            "But I'm determined to make every second until then count."
            "And of course there's no way anyone will walk in on us."
            "Is there?"
            "I was so confident when I told Jack that, I kind of convinced myself."
            "But the reality is that the privacy we're enjoying could end any moment."
            "And it's the danger of that happening which makes the difference in the end."
            "The mixture of excitement and fear pushes me over the edge."
            show jack doggy climax pleasure fuck nightclub fx
            bree.say "Mmmm..."
            bree.say "Jack..."
            show jack doggy surprised climax pleasure fuck nightclub fx
            bree.say "I'm going to cum!"
            bree.say "Right now!"
            "Jack doesn't say anything in response."
            "But I feel him tense, and I know he's losing it too."
            menu:
                "Cum in my pussy!":
                    show jack doggy climax pleasure fuck nightclub fx
                    bree.say "Jack..."
                    bree.say "Don't you dare pull out!"
                    "Again Jack doesn't speak."
                    show jack doggy fuck tongue nightclub fx with hpunch
                    "He just does as he's told, shooting his load into me."
                    with hpunch
                    "I thought that I was already having an orgasm."
                    show jack doggy fuck tongueout ahegao nightclub with hpunch
                    "But the sensation of it redoubles all that I'm feeling."
                    "Jack keeps on going, still thrusting in and out."
                    "Though I'm too far gone to be able to do anything at all."
                "Pull out of my pussy!":
                    show jack doggy climax pleasure fuck nightclub fx
                    bree.say "Jack..."
                    bree.say "Pull out...NOW!"
                    "Again Jack doesn't speak."
                    "He just does as he's told, pulling his cock out of me."
                    with hpunch
                    "I thought that I was already having an orgasm."
                    show jack doggy fuck tongueout ahegao nightclub with hpunch
                    "But the sensation of it redoubles all that I'm feeling."
                    show jack doggy fuck tongue nightclub -fx with hpunch
                    "Jack groans as he shoots his load over my exposed buttocks."
                    "Though I'm too far gone to be able to do anything at all."
        "Guide him to my ass" if hero.sexperience >= (sexperience_min + 5):
            show jack doggy climax nightclub
            bree.say "Where do you think, Jack?"
            bree.say "On top of me, now!"
            bree.say "And while you're at it, use the back door too!"
            show jack doggy normal nightclub
            "Looking back over my shoulder, I see Jack nodding eagerly."
            "And then he lowers himself down and onto my back."
            jack.say "Really?!?"
            jack.say "Okay, [hero.name]..."
            jack.say "Whatever you say!"
            "It's all I can do to keep from shivering as I feel him touch me."
            show jack doggy fuck happy nightclub
            "Because the familiar feel and weight of his body is already exciting me."
            "I know that cute belly of his is really a fuel tank."
            "One that belongs to a genuine love-making machine!"
            "My instinct is to keep looking back over my shoulder."
            "But I somehow manage to fight it, leaving Jack to his allotted task."
            "And pretty soon my reward is to feel his hands on my haunches."
            "He's neither hesitant nor too forceful in the way he holds me."
            "Getting things just right and making me feel safe in his hands."
            "Though a moment later I feel the first brush of his cock against my thighs."
            show jack doggy pain fuck nightclub
            "And I find it hard to keep my head clear and my thoughts in order."
            "As Jack begins to push his way between my butt cheeks, it only gets worse."
            show jack doggy closed fuck nightclub
            "Part of me knows that I should keep myself under control."
            "That I should maintain my dignity while he's on me."
            show jack doggy pain fuck nightclub
            "But another part of me has already surrendered to the idea of being fucked."
            "The purely animal part of me that wants gratification at any cost."
            "The battle between the two is settled as soon as Jack makes his next move."
            show jack doggy surprised hurt fuck nightclub
            "When I feel the head of his cock pressing against my ass, I'm sold."
            "All I want is for him to get inside of me and down to business."
            "But no matter what my head wants, my body is more stubborn."
            "There's no way that my ass is going to just open up to him."
            "And so I feel Jack begin to stroke and tease down there."
            show jack doggy pain hurt fuck nightclub
            "All of which only serves to add to the pleasure I'm experiencing."
            "It's a sensation that I could stand for a very long time."
            show jack doggy pain climax fuck nightclub
            "Yet after showing such reluctance to begin with, my body soon seems to change it's mind."
            show jack doggy surprised climax fuck nightclub
            "Because I can feel the muscles down there starting to relax."
            "And little by little, Jack's cock begins to sink into me."
            "Though there's nothing little about it!"
            show jack doggy normal back fuck nightclub
            "He goes slowly at first, probably as overwhelmed as I am."
            "But the deeper he goes, the more his confidence seems to grow."
            "So by the time he can't get any deeper, I'm in the palm of his hand."
            "And from that point on, Jack doesn't look back once."
            "Before I know it, he's thrusting away at me."
            "The feeling of him building up until it's overwhelming my senses."
            "I thought I was going to be the one giving the orders here."
            show jack doggy surprised fuck pleasure nightclub fx at startle(0.05,-10)
            "But now Jack's firmly in charge, and I'm reaping the benefits."
            "Every time he sinks into me, my entire body shakes."
            "And when he pulls back again, it only gets more intense."
            "My head is bowed, down below my shoulders, swaying from side to side."
            "I don't know how long I can keep this up before Jack makes me cum."
            "But I'm determined to make every second until then count."
            "And of course there's no way anyone will walk in on us."
            "Is there?"
            "I was so confident when I told Jack that, I kind of convinced myself."
            "But the reality is that the privacy we're enjoying could end any moment."
            "And it's the danger of that happening which makes the difference in the end."
            "The mixture of excitement and fear pushes me over the edge."
            show jack doggy climax pleasure fuck nightclub fx
            bree.say "Mmmm..."
            bree.say "Jack..."
            show jack doggy surprised climax pleasure fuck nightclub fx
            bree.say "I'm going to cum!"
            bree.say "Right now!"
            show jack doggy hurt pleasure fuck nightclub fx
            "Jack doesn't say anything in response."
            "But I feel him tense, and I know he's losing it too."
            menu:
                "Cum in my ass!":
                    show jack doggy climax pleasure fuck nightclub fx
                    bree.say "Jack..."
                    bree.say "Don't you dare pull out!"
                    "Again Jack doesn't speak."
                    show jack doggy fuck tongue nightclub fx with hpunch
                    "He just does as he's told, shooting his load into me."
                    with hpunch
                    "I thought that I was already having an orgasm."
                    show jack doggy fuck tongueout ahegao nightclub with hpunch
                    "But the sensation of it redoubles all that I'm feeling."
                    "Jack keeps on going, still thrusting in and out."
                    "Though I'm too far gone to be able to do anything at all."
                "Pull out of my ass!":
                    show jack doggy climax pleasure fuck nightclub fx
                    bree.say "Jack..."
                    bree.say "Pull out...NOW!"
                    "Again Jack doesn't speak."
                    "He just does as he's told, pulling his cock out of me."
                    with hpunch
                    "I thought that I was already having an orgasm."
                    show jack doggy fuck tongueout ahegao nightclub with hpunch
                    "But the sensation of it redoubles all that I'm feeling."
                    show jack doggy fuck tongue nightclub -fx with hpunch
                    "Jack groans as he shoots his load over my exposed buttocks."
                    "Though I'm too far gone to be able to do anything at all."
    show jack doggy mcalone closed nightclub -fx with fade
    "It takes me a while to recover and regain my senses."
    show jack doggy mcalone back nightclub
    "And when I do, I find Jack dressed and looking worried."
    "He thrusts my clothes towards me, urging me to take them."
    jack.say "Come on, [hero.name]..."
    jack.say "Get dressed, quickly!"
    bree.say "Okay, okay..."
    bree.say "I'm going as fast as I can."
    $ jack.love += 2
    $ jack.sexperience += 1
    hide jack doggy
    return

label jack_fuck_date_beach_female:
    scene bg beach
    "It's a perfect day to be hitting the beach - hot sun, blue skies and not a cloud for miles around."
    "And when I remembered that I was supposed to be spending time with Jack today, it seemed a no-brainer."
    "I mean, what guy wouldn't want to be here right now, soaking up the rays and strolling along the shore?"
    "And at first I think that I was totally on the money in asking Jack to come along with me."
    "But as I walk along the sand, looking for a place to claim as our own, he's nowhere to be seen."
    bree.say "Huh?"
    bree.say "That's weird..."
    bree.say "Jack, where are you?"
    show jack with dissolve
    "It's only when I look straight behind me that I see him Jack."
    "And he's lingering back there, like he doesn't want to be seen."
    jack.say "Erm..."
    jack.say "I'm right here, [hero.name]."
    jack.say "Where else would I be?"
    show jack sad at center, zoomAt(1.5, (640, 1040))
    "I walk back to where Jack's standing."
    "And I make a point of taking his hand."
    bree.say "I dunno, Jack..."
    bree.say "Maybe walking right by my side?"
    bree.say "You know, helping me pick the perfect spot?"
    "I'm surprised to see that Jack looks nervous as say all of this."
    "He's glancing this way and that, like he's afraid of being seen."
    show fx drop
    jack.say "Erm..."
    jack.say "How about one where nobody's going to see us?"
    jack.say "How does that sound?"
    hide fx
    "I can already feel a smile spreading across my face."
    "And that's because I didn't think Jack was that kind of guy."
    "At least not one as forward as that!"
    bree.say "Okay, Jack..."
    bree.say "If that's what you want."
    bree.say "As soon as we get out of sight, we can start fooling around!"
    show jack blush
    "Jack's eyes go wide at this."
    "Like he's excited and yet conflicted at the same time."
    "All the same he lets me pull him towards a particularly secluded part of the beach."
    scene bg black with dissolve
    pause 0.2
    scene bg beach
    show jack sad at center, zoomAt(1.5, (640, 1040))
    with dissolve
    "Once we get there, I can't wait to start pulling at my swimsuit."
    "Look, don't judge me, okay?"
    "I just know what I want when I want it!"
    "But much to my own surprise, Jack doesn't follow my example."
    bree.say "What's the matter, Jack?"
    bree.say "I thought you wanted to get out of sight?"
    bree.say "So that we could...you know...do stuff?"
    "Jack swallows hard."
    jack.say "Oh...right..."
    jack.say "I thought you wanted to keep people from seeing me!"
    bree.say "Seeing you?"
    bree.say "What do you mean?"
    jack.say "Well..."
    jack.say "I don't exactly have what you'd call a beach-bod, do I?"
    "Now it's all starting to make sense."
    "Jack's on edge because he's self-conscious!"
    "I shake my head and walk over to where Jack's standing."
    "Then I reach up and push his hands away from the buttons of his shirt."
    "Once that's done, I start to unbutton it myself."
    bree.say "Oh, Jack!"
    bree.say "Why'd you think I asked you to the beach in the first place?"
    bree.say "It's because this is the bod that I want to be seen with!"
    show jack sad at center, zoomAt(1.75, (640, 1190))
    "I wrap my arms around Jack, pulling him close to me."
    show jack normal
    "It takes a moment for him to respond, but then he returns the hug."
    "And I'm reminded of just how reassuring and safe being held in his arms can feel."
    bree.say "And anyway, who cares if you have a mighty belly, Jack."
    bree.say "All that means is you have a big appetite."
    bree.say "Big enough to eat me..."
    show jack blush
    "I start to slip out of my swimsuit as I'm saying this."
    "Letting it drop to the sand so that I'm left naked."
    "Then I take hold of Jack's hand, guiding it between my thighs."
    "And I feel my heart begin to flutter as his fingers move down there."
    bree.say "So how about it, Jack?"
    bree.say "Are you feeling hungry right now?"
    "Jack's eyes are as wide as saucers as he looks at me."
    "And I can see that he's already forgetting about everything else."
    "All of his self-consciousness seems to be draining away before my eyes."
    "And it's quickly being replaced by genuine, naked arousal."
    show jack perv
    jack.say "Y...you really mean that?"
    jack.say "You like the way that I look?"
    jack.say "And...you want me to..."
    hide jack
    show jack missionary beach mcalone
    with fade
    "I take a step backwards and start to lower myself onto the sand."
    "It's been a while since I tried to pull off a move like this."
    "And I'm kind of banking on being able to do it like I did back when I was a teenager."
    "For a moment I think that my back's going to call me out and dump me on my ass."
    "But then I feel the old knack for it, and I literally bend over backwards."
    "My toes sink into the sand and my arms support the other end of my body."
    "I did it!"
    "I pulled off a crab in front of Jack."
    "And not just any old crab, but a naked one!"
    "Jack looks amazed, spellbound almost."
    "But that doesn't stop him following me down onto the sand."
    "In fact, he really does look like he's under a spell right now."
    "Like he can't help being drawn after my pussy!"
    "Jack pulls down his shorts and tosses them aside."
    "Not actually essential for what I want of him right now."
    "But I guess he's just getting into the spirit by following my example."
    "As soon as he's on his knees, Jack gets down to business."
    show jack missionary lick pain -mcalone
    "His arms reach between my legs and them underneath my thighs."
    "Jack's hands grip me around the waist, helping to hold me up."
    show jack missionary pleasure
    "Then he leans in closer and I lose sight of his face altogether."
    "But then it hardly matters, because my eyes close a moment later."
    "And from then on, everything becomes about sensations instead."
    "Jack begins to tentatively lick and kiss around the edges."
    "Skirting the outer parts of my pussy like he's afraid to go in closer."
    "Or maybe I'm wrong to judge him so harshly."
    "Maybe this is a delicate form of foreplay."
    "Because the caution and subtlety that Jack's showing is having an effect."
    "He gives a little at a time, careful never to over-commit himself."
    "And so he feeds my desires a little at a time."
    "Always offering a tiny bit more, but never allowing me to be satisfied."
    "There's no hope of me being able to keep quiet as this is happening."
    "And I'm sure that I keep on crying out, moaning in helpless pleasure."
    "But the sound of my cries doesn't seem to daunt Jack in the slightest."
    "If anything, it seems to have the opposite effect."
    "Because now I can feel him finally beginning to move inwards."
    "It could be a rise in his confidence that does it."
    "Or else a mere compulsion to push onwards down a logical path."
    "Either way the result for me is the same."
    "The further inwards Jack's lips and tongue go, the more intense my sensations become."
    "And when I finally feel the tip of his tongue actually pushing inside..."
    "Well, there's no holding back after that."
    show jack missionary shaking pain
    "I can feel my fingers and toes clenching in the sand."
    "Every muscle in my body seems to clench and release at the same time."
    "All of it in sympathy with what's happening between my thighs."
    "The entirety of my body is moving now, quivering with anticipation."
    "Just waiting for what's already starting to happen."
    show jack missionary ahegao squirt mcalone at center, zoomAt(1.5, (480, 1020)) with hpunch
    "And when it finally comes over me, my climax sweeps in like a wave."
    "Jack seems to sense that it's happening too."
    "But rather than stopping, he keeps on going as it takes me."
    show jack missionary at center, traveling(1.5, 1.0, (780, 820))
    "There's a few seconds when I think my back's going to give out again."
    "That I'm going to end up a quivering mess on the sand."
    show jack missionary pleasure -squirt
    "I think the only thing that keeps it from happening is Jack holding me up."
    "I can feel his hands clutching me and his arms supporting my weight."
    "But even as the waves of my orgasm are gripping me, I know it's not enough."
    "So I use all of my willpower to raise my head and speak four words."
    show jack missionary -shaking
    bree.say "Jack..."
    bree.say "I need...more!"
    "I see him looking down on me with an intense expression on his face."
    "And without pause or hesitation, he nods."
    scene jack missionary
    show jack missionary outside pleasure beach
    with fade
    "Jack straightens up, and then he thrusts himself forwards."
    "But all I can do is hold on for dear life!"
    menu:
        "Guide him to my pussy":
            "I'm already in a state of extreme arousal and coming down off my first orgasm."
            "That means that my head's in a state of total disarray, my thoughts confused."
            "But it also means that my body doesn't need to be coaxed into life a second time."
            "I have no idea if Jack's aware of that fact, or if he's just running on instinct too."
            "Either way the result is the same."
            show jack missionary normal
            "Instead of his lips and tongue, this time I feel the head of his cock down there."
            "I don't need to see the thing to know just how hard it is right now."
            "And that's because I can already feel it pressing against the lips of my pussy."
            "Like I already said, I'm more than ready for this."
            show jack missionary pain vaginal shaking
            "So it comes as no surprise when he only needs to apply the smallest amount of pressure."
            "Normally I'd be savouring the resistance before my body surrendered to the inevitable."
            "Loving the way that it added spice to the whole experience."
            "The way it heightened the intensity once he found his way inside."
            "But this time, Jack all but slides straight into me."
            "The motion is smooth and steady, filling me more with each second that passes."
            show jack missionary normal -shaking
            "Once he's as deep as he can go, Jack pauses for a moment."
            "I guess that he's enjoying the sensation for himself."
            "And at the same time I'm reminded of just how good his cock feels inside of me."
            "But it's not like I have a long time to contemplate the feeling."
            show jack missionary pain speed at startle(0.05,-10)
            "Because Jack begins to move in earnest a few seconds later."
            "And once he does that, it's clear he's not holding back."
            "I must have been able to get Jack pretty worked up before we started."
            "Because now the energy that he's putting into his thrusts is insane!"
            "I thought that I was being pushed to the limit when he was going down on me."
            "But what he's doing now makes that pale in comparison."
            "I feel like I'm being bent in half, like my spine might snap at any second."
            "And yet there's no way I'm going to ask him to stop."
            "No way that I'd ever let him stop either."
            "All the time that this is going on, I'm surprising myself too."
            "I thought that what Jack did to be beforehand was a lot."
            "I thought that it'd have left me drained, exhausted and spent."
            "But somehow the pleasure that he's making me feel is keeping me going."
            "It's like my body is somehow able to transform it into a new burst of energy and stamina."
            show jack missionary pleasure at startle(0.05,-10)
            "I feel my muscles tense and my body stay rigid when I expected it to become limp and lifeless."
            "Even more amazing is the fact that I can already feel a second climax starting to build."
            "And before it's even begun, I know that it's going to be bigger than the last."
            "Already I can feel the muscles down there starting to clench and squeeze."
            "Jack groans as my pussy clutches his cock like a fist."
            "But he keeps right on going regardless."
            show jack missionary ahegao shaking at startle(0.05,-10)
            "And a few seconds later I start to cum again."
            "I can already feel that I'm taking Jack with me."
            "He doesn't need to say a word, I just know that he's about to lose it too."
            menu:
                "Cum in my pussy!":
                    "Jack's still got a pretty good hold on me as it's all happening."
                    "And that's fine by me, as I'm not planning on going anywhere."
                    with hpunch
                    "I was sure my orgasm couldn't get any more intense than it already is."
                    show jack missionary creampie with hpunch
                    $ jack.love += 4
                    "But the moment Jack lets go, I feel like it doubles instantly."
                    with hpunch
                    "It's all that I can do to hold onto him until everything subsides."
                    show jack missionary pleasure
                    "Then I finally fall helpless and motionless onto the sand."
                "Pull out of my pussy!":
                    "I'm afraid that Jack's going to drop me onto the sand any moment."
                    "But I still do all that I can to wriggle free of him before it happens."
                    "Just in time he seems to realise that I'm trying to do."
                    show jack missionary pleasure outside
                    "And he releases me, lowering me gently onto the ground."
                    show jack missionary pleasure cumshot with hpunch
                    $ jack.sub += 2
                    "He lets go a moment later, shooting his load onto my exposed belly."
                    with hpunch
                    "And all I can do is lie there motionless, in the grip of my own orgasm."
        "Guide him to my ass":
            "I'm already in a state of extreme arousal and coming down off my first orgasm."
            "That means that my head's in a state of total disarray, my thoughts confused."
            "But it also means that my body doesn't need to be coaxed into life a second time."
            "I have no idea if Jack's aware of that fact, or if he's just running on instinct too."
            "Either way the result is the same."
            show jack missionary normal
            "Instead of his lips and tongue, this time I feel the head of his cock down there."
            "I don't need to see the thing to know just how hard it is right now."
            "And I know that I need to act now too, if I want to get my own way."
            "Reaching down I grab hold of Jack's cock, making him grunt at the sensation."
            "Then I position it firmly between my butt cheeks."
            "Like I already said, I'm more than ready for this."
            "And Jack seems to understand exactly what I want too."
            show jack missionary pain anal shaking
            "So it comes as no surprise when he only needs to apply the smallest amount of pressure."
            "Normally I'd be savouring the resistance before my body surrendered to the inevitable."
            "Loving the way that it added spice to the whole experience."
            "The way it heightened the intensity once he found his way inside."
            "But this time, Jack all but slides straight into me."
            "The motion is smooth and steady, filling my ass more with each second that passes."
            show jack missionary normal -shaking
            "Once he's as deep as he can go, Jack pauses for a moment."
            "I guess that he's enjoying the sensation for himself."
            "And at the same time I'm reminded of just how good his cock feels inside of me."
            "But it's not like I have a long time to contemplate the feeling."
            show jack missionary pain speed at startle(0.05,-10)
            "Because Jack begins to move in earnest a few seconds later."
            "And once he does that, it's clear he's not holding back."
            "I must have been able to get Jack pretty worked up before we started."
            "Because now the energy that he's putting into his thrusts is insane!"
            "I thought that I was being pushed to the limit when he was going down on me."
            "But what he's doing now makes that pale in comparison."
            "I feel like I'm being bent in half, like my spine might snap at any second."
            "And yet there's no way I'm going to ask him to stop."
            "No way that I'd ever let him stop either."
            "All the time that this is going on, I'm surprising myself too."
            "I thought that what Jack did to be beforehand was a lot."
            "I thought that it'd have left me drained, exhausted and spent."
            "But somehow the pleasure that he's making me feel is keeping me going."
            "It's like my body is somehow able to transform it into a new burst of energy and stamina."
            "I feel my muscles tense and my body stay rigid when I expected it to become limp and lifeless."
            show jack missionary pleasure at startle(0.05,-10)
            "Even more amazing is the fact that I can already feel a second climax starting to build."
            "And before it's even begun, I know that it's going to be bigger than the last."
            "Already I can feel the muscles down there starting to clench and squeeze."
            "Jack groans as my ass clutches his cock like a fist."
            "But he keeps right on going regardless."
            show jack missionary ahegao shaking at startle(0.05,-10)
            "And a few seconds later I start to cum again."
            "I can already feel that I'm taking Jack with me."
            "He doesn't need to say a word, I just know that he's about to lose it too."
            menu:
                "Cum in my ass!":
                    "Jack's still got a pretty good hold on me as it's all happening."
                    "And that's fine by me, as I'm not planning on going anywhere."
                    with hpunch
                    "I was sure my orgasm couldn't get any more intense than it already is."
                    show jack missionary creampie with hpunch
                    $ jack.love += 2
                    $ jack.sub += 2
                    "But the moment Jack lets go, I feel like it doubles instantly."
                    with hpunch
                    "It's all that I can do to hold onto him until everything subsides."
                    show jack missionary pleasure
                    "Then I finally fall helpless and motionless onto the sand."
                "Pull out of my ass!":
                    "I'm afraid that Jack's going to drop me onto the sand any moment."
                    "But I still do all that I can to wriggle free of him before it happens."
                    "Just in time he seems to realise that I'm trying to do."
                    show jack missionary pleasure outside
                    "And he releases me, lowering me gently onto the ground."
                    show jack missionary pleasure cumshot with hpunch
                    $ jack.love += 4
                    $ jack.sub += 1
                    "He lets go a moment later, shooting his load onto my exposed belly."
                    with hpunch
                    "And all I can do is lie there motionless, in the grip of my own orgasm."
    return


label jack_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom4
        show jack naked
        with fade
        menu:
            "You should leave":
                bree.say "I am done with you and I have to get up early tomorrow, you should leave."
                "The sex was beyond incredible."
                "Frowning a little, Jack straightens and shrugs, then goes to collect his clothes from where he'd let it fall earlier."
                "He then heads up the stairs."
                $ jack.love -= 1
                $ jack.sub += 1
                call sleep from _call_sleep_107
            "You should sleep here":
                bree.say "You can stay and sleep here."
                "I say, my voice a little shaky."
                "We curl up spooning together in bed, drifting toward sleep."
                $ jack.love += 1
                call sleep ("jack") from _call_sleep_108
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
