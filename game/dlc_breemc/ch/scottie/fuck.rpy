init python:
    Event(**{
    "name": "scottie_hottub_sex_female",
    "label": "scottie_hottub_sex_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(scottie,
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
    "name": "fuck_scottie_beach",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM_female",
    "conditions": [
        IsHour(14, 18),
        HeroTarget(
            IsGender("female"),
            IsRoom("beach", "date_beach", "date_nudistbeach"),
            HasStamina(),
            ),
        PersonTarget(scottie,
            IsActive(),
            MinStat("love", 120),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    InteractActivity(**{
    "name": "fuck_scottie_park",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsRoom("date_park"),
            HasStamina(),
            ),
        PersonTarget(scottie,
            OnDate(),
            MinStat("love", 120),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    Event(**{
    "name": "scottie_fuck_pub",
    "label": "scottie_fuck_pub_female",
    "conditions": [
        HeroTarget(IsGender("female"),
            IsActivity("work_pub_female"),
            ),
        PersonTarget(scottie,
            Not(IsHidden()),
            Not(IsFlag("delay")),
            MinStat("love", 120),
            ),
        ],
    "do_once": False,
    "once_month": True,
    "quit": False,
    })

label scottie_hottub_sex_female:
    scene bg pool with fade
    scottie.say "Hey!"
    scottie.say "Yo, [hero.name]!"
    scottie.say "I'm here already - where are you?!?"
    "I almost jump at the sound of Scottie's voice."
    "He's not supposed to be here yet."
    "I haven't finished the final touches to the hot-tub!"
    "I need to sort out those little things that'll make it perfect!"
    bree.say "Erm..."
    bree.say "Okay, Scottie..."
    bree.say "I'll be there in a few seconds, okay?"
    "Either Scottie doesn't pick up on the hint in my tone."
    "Or else he's just too dense to pick up on it at all."
    "Because the sound of my voice attracts him bee to a flower."
    "And he comes ambling around the corner of the house a moment later."
    show scottie casual with easeinleft
    scottie.say "Oh..."
    scottie.say "There you are, [hero.name]!"
    scottie.say "Lucky I found you back here."
    scottie.say "Otherwise I'd have thought you were standing me up!"
    "I just manage to throw the last of my preparations together that very second."
    "Then I turn round to face Scottie, gesturing to all of my hard work."
    bree.say "Ta da!"
    bree.say "What do you think, Scottie?"
    "I've made sure the lighting is low and seductive in the yard."
    "I've lined the side of the tub with candles."
    "I've put out a nice bottle of wine and two glasses."
    "Hell, I've even scattered rose petals all over the place!"
    "Scottie looks around, scratching the back of his head."
    scottie.say "Ooh..."
    scottie.say "What's with the candles?"
    show scottie sad
    scottie.say "Did you not pay your electricity bill?"
    "I open my mouth to put Scottie right."
    "But it's then that he notices the petals."
    show scottie normal
    scottie.say "And you might want to sweep this up, [hero.name]."
    scottie.say "Like, get a gardener in to tidy the place!"
    "I can feel my blood beginning to boil as Scottie goes on."
    "Is he going to be so clueless and rude about all of my efforts?"
    show scottie at startle
    "Apparently not, because his eyes light up when he spots the wine."
    scottie.say "Oh, great - booze!"
    scottie.say "Let's have some of that, [hero.name]..."
    show scottie at right5 with ease
    "As he hurries over to snatch up the bottle, I try to calm myself down."
    "After all, I knew that Scottie was a bit of an ape before I asked him over."
    "What did I expect to happen?"
    "That a few thoughtful bits of decor would turn him into a gentleman?"
    "A moment later my thoughts are interrupted."
    show scottie at center, zoomAt(1.5, (640, 1040)) with dissolve
    "As Scottie walks over and hands me a glass of wine."
    scottie.say "Here you go, [hero.name]."
    show scottie angry
    scottie.say "Took me a while to open it."
    scottie.say "Because some asshole went and stuck a cork in the bottle!"
    show scottie normal
    "I try not to laugh as I take the glass from Scottie."
    "He can be such a dumbass sometimes!"
    "But that's one of the things that I kind of like about him."
    "It means that he's far less complicated than most guys I've dated."
    "In fact, I think I've met dogs smarter than Scottie!"
    bree.say "Don't worry about that, Scottie."
    bree.say "Let's get in the tub, okay?"
    hide scottie
    show scottie casual
    with dissolve
    "Scottie nods in agreement, peeling off his top."
    $ game.active_date.clothes = "swimsuit"
    show scottie swimsuit with dissolve
    "Then he kicks off his pants, revealing his trunks underneath."
    "And that's when I remember the other thing that I like about him."
    "That seriously hot body!"
    "Scottie's so crazily ripped!"
    "Part of me wants to reach out and touch him right now."
    "But I manage to fight the urge and wait a little longer."
    show hottub scottie valentine with fade
    "As I settle down in the water, I take a sip of my wine."
    "And much to my delight, I see Scottie checking out the view too."
    scottie.say "Wow, [hero.name]..."
    scottie.say "You're looking good tonight!"
    bree.say "Aw..."
    bree.say "Thank you, Scottie!"
    bree.say "You're looking...excited!"
    "I say this as I'm looking down at Scottie's crotch."
    "And I can see that he wasn't kidding about liking how I look."
    "He's getting bigger down there by the second!"
    "Scottie follows my gaze down and then laughs."
    scottie.say "Oh..."
    scottie.say "Looks like little Scottie wants to say hi!"
    scottie.say "I guess that means we should fuck, huh?"
    "I can't help smiling at Scottie's frankness."
    "Another guy might be embarrassed in the same situation."
    "Or they'd at least try to seem a little less obvious."
    "But not Scottie, he never thinks anything he doesn't say!"
    bree.say "You know what, Scottie..."
    bree.say "I think I could go for that right now!"
    "Scottie's face lights up at my enthusiasm."
    "He nods as he puts his glass down on the edge of the tub."
    scottie.say "Wow, [hero.name]..."
    scottie.say "We're so on the same book right now!"
    bree.say "Page, Scottie..."
    bree.say "It's on the same page!"
    "I don't know if Scottie even hears what I just said."
    "But in the end, does it really matter?"
    "He's gliding through the water towards me."
    "So perhaps I should be focussing on that, rather than correcting him."
    "I turn to put my own glass on the edge of the tub too."
    "But Scottie gets to me before I'm done and can turn back around."
    "I feel his hands grab hold of my waist."
    "Then he pulls me backwards and towards him."
    scottie.say "Got ya, [hero.name]!"
    scottie.say "Now you can't escape!"
    "He's so obvious and straight up with what he wants."
    "Which is great when we both want the exact same thing!"
    bree.say "Do I look like I want to get away, Scottie?"
    show hottub sex female scottie with fade
    "I make my point by pushing myself backwards too."
    "And the moment I do, I feel his ripped body against mine."
    "Even better, I can feel his cock pressed against my ass too!"
    "Scottie lets out a dumb laugh of testosterone fuelled delight."
    "And as he does so, I feel him fumbling around with my swimsuit."
    "Looking back over my shoulder, I see what the problem is."
    "Scottie's trying to pull his cock out with one hand."
    "And at the same time he's also trying to yank aside the crotch of my swimsuit."
    "I'm really not sure he's capable of doing two things at once."
    "So I step in to help, pulling the material of my swimsuit aside for him."
    "Scottie gasps in relief, glad of my help."
    "And a moment later, his cock pops out of his trunks."
    "I stare at it for a moment, feeling my hunger for it rise."
    "Then I turn my head back, biting my lip in anticipation."
    "Scottie doesn't keep me waiting long either."
    "I feel the head of his cock push between my thighs."
    "And then it's rubbing against the lips of my pussy."
    "Scottie doesn't waste any time getting down to business."
    "By that I don't mean that he starts pounding away like a brute."
    "He's just super eager to get it on."
    "And luckily for me, I'm in the exact same mood."
    "I can feel my pussy getting wetter by the second."
    "So as Scottie rubs the head of his cock against it, the inevitable happens."
    "Muscles slacken, the lips relax, and he begins to inch his way inside."
    "I brace myself by holding onto the edge of the tub."
    "But aside from that, all I can do is relax and go with it."
    "Scottie, on the other hand, is working harder by the second."
    "And I'm feeling all of the benefits from the word go!"
    "You might have guessed that Scottie's not a small guy down there."
    "So there's no problems when it comes to him filling me up."
    "And he's rock-hard too, which means he feels amazing inside of me."
    "As he starts to thrust in and out, the pleasure only builds."
    "I find myself nodding in approval and in the hope of more."
    "But I have no idea if Scottie can see me doing it."
    "Luckily for me, it seems that he has the exact same thing in mind."
    "He starts to fuck me harder and faster, making me gasp and moan."
    "But there doesn't seem to be any sign of him slowing down at all."
    "Scottie just keeps on going faster and harder."
    "And that means I feel the pleasure mounting inside of me too."
    "My moans are slowly turning into cries and then almost into screams."
    "I try as best I can to bite my lip and keep the noise down."
    "Because I'm afraid of someone hearing the sounds that I'm making."
    "Either a neighbour peeking from behind a curtain."
    "Or worse, one of my housemates coming to see what all the commotion is about!"
    "But I daren't open my mouth and try to plead with Scottie."
    "Because I'm sure that'll just end in me screaming even louder."
    "So I just bite my lip and do the best I can to keep quiet."
    scottie.say "Unh..."
    scottie.say "[hero.name]..."
    scottie.say "You're so...fucking hot!"
    scottie.say "I'm gonna...gonna cum!"
    with hpunch
    "True to his word, Scottie shoots his load almost as soon as he's finished talking."
    with hpunch
    "And the moment it happens, all of my hard work to stay silent is undone."
    with hpunch
    "The last thrust as he fills me up is too much, and I can't hold back any more."
    bree.say "Ah..."
    bree.say "Fuck..."
    bree.say "Scottie..."
    bree.say "You're making me...making me cum too!"
    with hpunch
    "I squeal and cry out as my orgasm takes hold."
    "And I'm glad for Scottie holding me up while it happens too."
    "Because otherwise I'd have been helpless to keep myself from sinking."
    "He holds onto me the whole time, then lets me sink back against him."
    "Totally spent, I lie back in Scottie's arms, happy just to be held."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ scottie.sexperience += 1
    $ game.active_date.clothes = None
    scene bg black with dissolve
    return

label scottie_fuck_date_female(location="hero"):
    $ game.room = "bedroom4"
    call scottie_fuck_date_intro_female (location) from _call_scottie_fuck_date_intro_female
    menu:
        "Missionary":
            call scottie_fuck_date_missionary (0) from _call_scottie_fuck_date_missionary
        "Spoon" if hero.sexperience >= 5:
            call scottie_fuck_date_spoon (5) from _call_scottie_fuck_date_spoon
        "Doggy" if hero.sexperience >= 10:
            call scottie_fuck_date_doggy (10) from _call_scottie_fuck_date_doggy
        "Cowgirl" if hero.sexperience >= 15:
            call scottie_fuck_date_cowgirl (15) from _call_scottie_fuck_date_cowgirl

    hide bree
    hide scottie
    with fade
    "Scottie and I lie on the bed, exhausted and covered in sweat that's quickly cooling."
    "I make to say something, some small talk."
    "But I can already hear his snoring, loud as a chainsaw, in my ear."
    "I guess now the only decision left is to either kick him out, or else let him sleep it off here."
    $ scottie.sexperience += 1
    call scottie_sleep_date_fuck_female (location) from _call_scottie_sleep_date_fuck_female
    return

label scottie_sleep_date_fuck_female(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom4
        show scottie naked
        with fade
        menu:
            "You should leave":
                bree.say "I am done with you and I have to get up early tomorrow, you should leave."
                "The sex was beyond incredible."
                "Frowning a little, Scottie straightens and shrugs, then goes to collect his clothes from where he'd let it fall earlier."
                "He then heads up the stairs."
                $ scottie.love -= 1
                $ scottie.sub += 1
                call sleep from _call_sleep_91
            "You should sleep here":
                bree.say "You can stay and sleep here."
                "I say, my voice a little shaky."
                "We curl up spooning together in bed, drifting toward sleep."
                $ scottie.love += 1
                call sleep ("scottie") from _call_sleep_92
    return

label scottie_fuck_date_intro_female(location="hero"):
    $ result = game.days_played % 4
    if result == 0:
        scene bg bedroom4
        "Once we're back at my place, we spill into my room without even thinking about anything else."
        show scottie with dissolve
        "After all, I'm not exactly taking Scottie out on a date for the sake of his non-existent conversation skills."
        show scottie b at center, zoomAt(1.5, (640, 1040))
        "Luckily for me then that he's as eager as can be and doesn't need to be led by the hand."
        hide scottie
        show scottie kiss
        with fade
        $ scottie.flags.kiss += 1
        "Scottie wastes no time in beginning to kiss me aggressively once the door is closed behind us and almost yanking off my clothes."
        "After so many modern guys that are all gentleness and manners, it's kind of thrilling to be treated in that way."
        "Offer no resistance, returning his kisses and enjoying being roughly stripped."
        "Liking in particular when an item of clothing holds me bound for a few moments at a time."
        "Once I'm finally naked, I return the favour."
        "Scottie begins to kiss my neck and then my breasts as I struggle to pull off his clothes."
        "His body is more impressive than I thought, and I find myself wondering why Sasha ever gave all of this up."
        scottie.say "Yeah, baby - strip it all off of me!"
        scottie.say "You know it's making you crazy!"
        show scottie kiss naked
        "Oh yeah, I remember now what it was - he's mentally mired in adolescence."
        "But, like I said, we're not here to talk."
        hide scottie
        show scottie naked b at center, zoomAt(1.5, (640, 1040))
    elif result == 1:
        show bg street
        show scottie at center, zoomAt(1.5, (640, 1040))
        with fade
        "Scottie's been quiet the whole of the taxi ride back to my place."
        "But that doesn't mean he's been in a world of his own my any means."
        "He keeps on shooting me a certain kind of look and grinning the whole time."
        "And I have to admit that we've just been on a really fun date together."
        "One of those nights when Scottie's dumb sense of humour just kind of worked."
        "So much so that I think he deserves a reward as soon as we get back to my place."
        "Scottie seems to be aware of what's going through my head too."
        "Whether it's just dumb luck on his part."
        "Or some kind of instinctive animal insight, I have no idea."
        show bg livingroom with fade
        "But he doesn't need to be told to follow me into the house."
        "And he's right on my heels as I lead the way upstairs to my bedroom too."
        show bg bedroom4
        show scottie joke
        with fade
        "As soon as we're inside and the door is closed behind us, Scottie gives me a wink."
        scottie.say "So, [hero.name]..."
        scottie.say "You lured me back here to your lair."
        scottie.say "That must mean you want some of this!"
        show scottie naked with dissolve
        "Scottie underlines his point by pulling off his top."
        "Then he tosses it aside and pulls a little pose for my benefit."
        "And I have to admit, the sight of his naked torso is pretty impressive."
        "I mean, Scottie does take good care of himself in that department."
        "But there's just something so cheesy and dumb about the way he goes about it."
        "I can't help chuckling and shaking my head."
        show scottie embarrassed
        scottie.say "Hey!"
        scottie.say "What's so funny?"
        scottie.say "Girls usually go crazy for me when I do that!"
        "Suddenly I feel like a complete jerk for laughing at Scottie."
        "He's such a typical jock most of the time, you know?"
        "That makes it easy to forget he's actually pretty sensitive."
        show scottie at center, zoomAt(1.75, (640, 1190))
        "I hurry over to where he's standing, and throw my arms around him."
        bree.say "I'm sorry, Scottie."
        bree.say "Your muscles are very nice!"
        bree.say "I think I maybe had just a little too much to drink."
        show scottie normal
        "This seems to be more than enough to mollify Scottie."
        "And they way I'm stroking his chest restores his fragile ego too."
        scottie.say "You bet they're nice, babe."
        scottie.say "But not as nice as what you got under your clothes!"
        bree.say "Oh, really?"
        bree.say "So you want to see, do you?"
        show scottie happy
        "Scottie nods, a wide grin spreading across his face."
        scottie.say "You bet I do!"
        show scottie at center, zoomAt(1.5, (640, 1040))
        "I nod and slip out of his arms."
        "Then I walk over to the side of the bed."
        "And I start to take off my clothes, slowly and seductively."
        show scottie perv
        "As Scottie watches me, I'm reminded of how simple he is at heart."
        "All he really wants to do is have fun and indulge his animal appetites."
        "And there are so many ways that I can use that to indulge myself at the same time."
        "That's why I make sure to smile at him, wink and shake my ass a hell of a lot."
        "Because I can see the effect that all of it is having on him."
        "And it's all going to make what I get out of this that much better too."
        "As I get down to my underwear, I make sure to look Scottie in the eye."
        "He's staring intently as I take off my bra and drop it onto the floor."
        "And his eyes almost pop out of their sockets as I pull down my panties!"
        "I can see that he's having to fight to keep himself still."
        "All of his instincts must be telling him to run straight over here."
        "But somehow he's managing to keep a lid on it and wait for permission."
        "I swear I can see that muscles of his body twitching with anticipation."
        "So when I beckon him over with a single finger, I'm excited to see what happens."
        bree.say "What are you waiting for, Scottie?"
        bree.say "Come on over here!"
        "My words seem to release something deep down in Scottie."
    elif result == 2:
        scene bg secondfloor
        show scottie
        with fade
        "Scottie follows me into the house and up the stairs to my bedroom without a single word."
        "But then why would a guy like him even stop to question what's apparently on the cards?"
        "He's so cocky and full of confidence that I must just take it for granted he's in luck."
        "I mean, he is tonight, because I want the same thing too."
        "But I can't help looking at him sideways and wondering just how gullible Scottie really is."
        "I open the door to my room and gesture for him to step inside, a plan forming in my mind."
        scene bg bedroom4
        show scottie
        with fade
        "Then I close the door behind us, leaning on it as if to bar any chance of escape."
        bree.say "Well, well..."
        bree.say "Now that I've lured you back to my lair..."
        bree.say "It's time that I revealed my true intentions."
        show scottie embarrassed
        scottie.say "Erm..."
        scottie.say "What are you talking about, [hero.name]?"
        bree.say "I didn't bring you back here to make love to you, Scottie!"
        show scottie surprised at startle
        scottie.say "Wait...you didn't?!?"
        bree.say "No, Scottie - I brought you back here to end you!"
        bree.say "To end you and sell your organs on the dark web!"
        scottie.say "No, [hero.name]!"
        show scottie sad
        scottie.say "Please don't do it...I've got so much more to give!"
        "The look of horror on Scottie's face looks so genuine that I can't keep it up."
        "And so I laugh and shake my head."
        bree.say "Kidding, Scottie...I was kidding."
        bree.say "God, you are SO gullible."
        show scottie shy
        "The look of relief on Scottie's face is plain to see."
        show scottie embarrassed
        "Though he does all he can to cover it up with fake bravado."
        scottie.say "Uh..."
        scottie.say "Of course I knew you were kidding, babe!"
        show scottie normal
        scottie.say "I was just...just playing along, yeah?"
        "I walk over to the bed and sit down on the mattress."
        "Then I pat the spot right at my side."
        bree.say "Actually, Scottie..."
        bree.say "I am interested in one of your organs."
        bree.say "And I was wondering if you'd mind donating it to me tonight?"
        bree.say "We could call it a short-term loan, if you like?"
        show scottie surprised
        "Scottie looks puzzled for a moment, trying to figure out what I mean."
        show scottie annoyed
        "But then he notices me staring straight at his groin."
        show scottie happy
        "And a knowing smile spreads across his face."
        scottie.say "Oh..."
        scottie.say "I get it, [hero.name]."
        scottie.say "Sure thing - you can have as much of it as you want!"
        "I watch as Scottie makes his intentions clear by starting to strip-off."
        "And then I begin to remove my own clothes as I watch him."
        "I'm sure to go much more slowly than he does, and the effect is clear."
        "Scottie's trying to watch me at the same time as I watch him."
        show scottie perv
        "But the difference is that he's still standing up."
        "Which means that he starts to sway as he's trying to step out of his pants."
        show scottie naked with dissolve
        "Then he topples and almost falls flat on his face."
        "At the last minute, Scottie somehow manages to turn leap forwards and onto the bed."
        "And when he lands beside me, he's also pulled off the last of his clothes too."
        "I let out a yelp of surprise as he reaches for me."
        "But I don't make any effort to escape his grasp."
        scottie.say "Hey, [hero.name]..."
        scottie.say "Let me help you with that..."
        "Scottie keeps a hold of me while he pulls off the last of my clothes."
        "And then I find myself held in his embrace, skin to skin."
        "This is one of the few positions in which I feel like we're equal."
        "Scottie's no genius, but in bed, he's a kind of savant."
        "Because here his most basic, animal instincts serve him well."
    else:
        show bg street
        show scottie at center, zoomAt(1.25, (640, 920))
        with fade
        "I don't know what's happened tonight to change things up."
        "But Scottie's been totally hitting it out of the park."
        "Our date's gone super amazingly well, really the best ever."
        "And he's been making me split my sides laughing all night too."
        "I mean, yeah...I have had a little bit to drink."
        "Maybe even more than I'm used to having on a date."
        "But I don't think I'm that drunk!"
        "Just seeing the better side of Scottie for a change."
        show bg house
        show scottie at center, zoomAt(1.25, (640, 920))
        with fade
        "It's just a coincidence that I struggle to fit my key into the lock."
        "And I'm a little distracted."
        "Which is why I almost fall into the hallway when it opens."
        scene bg livingroom with fade
        show scottie at center, zoomAt(1.25, (940, 920)) with easeinright
        "Scottie does me a solid by closing the door behind us."
        play sound door_slam
        pause 0.5
        with vpunch
        "But he slams it so hard that I swear I hear the whole house shake."
        bree.say "SSSSHHH!"
        bree.say "Be quiet, Scottie!"
        bree.say "We don't wanna wake up Masha or Sike..."
        show scottie surprised at center, zoomAt(1.25, (640, 920)) with ease
        scottie.say "Huh?"
        scottie.say "What did you just say?"
        bree.say "I said we don't wanna wake Sasha and [mike.name]!"
        show scottie happy at startle
        scottie.say "Uh-uh..."
        show scottie joke
        scottie.say "You said Masha and Sike!"
        scottie.say "You're drunk as hell!"
        "I frown at Scottie's accusation, crossing my arms over my chest."
        bree.say "Oh really?"
        bree.say "I'll show you who's drunk!"
        show scottie at center, zoomAt(1.5, (640, 1040))
        "Without asking, I grab hold of Scottie's hand."
        "And then I start to drag him up the stairs."
        show bg secondfloor
        show scottie shy at center, zoomAt(1.5, (640, 1040))
        with fade
        scottie.say "Erm..."
        scottie.say "[hero.name]..."
        scottie.say "I kinda wanted to go upstairs with you anyway."
        scottie.say "So there's no need to..."
        "I turn and lean into Scottie's face as we're halfway up the stairs."
        bree.say "Did I ask for your opinion, Scottie?"
        show scottie embarrassed
        scottie.say "Ah..."
        bree.say "Well, did I?!?"
        scottie.say "I guess not, [hero.name]!"
        bree.say "Then shut the hell up and let's get to my bedroom already!"
        "My words seem to have the desired effect."
        show scottie perv
        "Scottie nods furiously and begins to follow on my heels."
        "This means that within mere seconds we're at the door to my room."
        play sound door_slam
        show bg bedroom4
        show scottie
        with fade
        "I throw it open and we rush inside, slamming it closed behind us."
        "Neither of us pauses even for as much as the blink of an eye."
        show scottie naked with dissolve
        "Instead we instantly begin to tear off our clothes as we make for the bed."
    return

label scottie_fuck_date_missionary(sexperience_min):
    "I'm not in the mood to be subtle about anything tonight."
    hide scottie
    show scottie missionary nonpc
    with fade
    "So as soon as I'm naked, I throw myself backwards onto the bed."
    "And then I hold out my arms to Scottie."
    bree.say "Come on, big boy..."
    bree.say "Come and get some!"
    "Scottie claps his hands together and a broad smile creeps onto his face."
    "Then he interlaces his fingers and turns them inside out."
    "The cracking sound this makes is so loud that it actually makes we wince."
    "But then I'm distracted by the fact that he jumps into the bed."
    show scottie missionary pain -nonpc with vpunch
    "Scottie lands on his knees, right between my legs."
    "I feel the bed creak under his weight."
    "And I'm a little afraid that it might break."
    show scottie missionary -pain
    "But luckily for us, it seems able to take the strain."
    scottie.say "Now then..."
    scottie.say "Where to begin?"
    menu:
        "Ask for some foreplay before":
            show scottie missionary down
            bree.say "I dunno, Scottie..."
            bree.say "Maybe with a little foreplay?"
            bree.say "You know, something to get me in the mood?"
            scottie.say "Don't worry, [hero.name]..."
            scottie.say "I got just the thing!"
            show scottie missionary nonpc
            "Scottie leans over me, running his hands up my legs."
            "I can't help biting my lip in anticipation as I watch him."
            "Because I just can't wait to see what he's about to do to me."
            "Once his hands reach the top of my thighs, they don't go any higher."
            show scottie missionary pleasure finger
            "Instead they slide down the inside of my legs, making me gasp with surprise."
            "Okay, okay...I kind of knew that he was going to make a beeline for my pussy."
            "But give a girl a break, yeah?"
            show scottie missionary -pleasure
            "At least let me tell it in a way that makes things sound romantic and exciting!"
            "The truth is that I'm not really sure what to expect from this."
            "I know that Scottie's a sporty kind of guy and he works out a lot."
            "You don't get to be as ripped as he is by sitting around eating donuts all day!"
            "But that does mean his hands are pretty hardy and weathered as a result."
            "Part of me is worried that his fingers are going to be clumsy on account of this."
            "I'm still biting my lip, but now a little of it is from nerves too."
            show scottie missionary pleasure
            "But as I feel him begin to stroke at the edges of my pussy, I get a surprise."
            "And it's not one of the unpleasant kind either."
            "Because I find that Scottie's touch is as strong as I'd expected."
            "Yet it's also subtle and oddly gentle too."
            "Scottie starts by tracing the outline of my pussy."
            "He uses two fingers, stroking them around and inwards."
            "This way, little by little, he works towards the inner folds."
            "I'm feeling a mixture of rising pleasure and intense expectation."
            "And every fraction of an inch that he moves inwards cranks up the sensations."
            "I can also feel that the reaction of my own body is making things easier for Scottie too."
            "Every passing second makes me slicker to the touch."
            "And it makes the muscles down there relax as well."
            "So when the time finally comes for the tips of his fingers to venture inside..."
            "Well, let's just say that Scottie doesn't have any trouble exploring."
            "But for me the sensations that it causes are far more dramatic."
            "I find myself gasping and crying out with the pleasure I'm feeling."
            show scottie missionary ahegao
            "My back arches on the bed, and I throw my head backwards."
            "It must be a strange sight to behold."
            "One person's entire body moving, wriggling and writhing."
            "And all on account of another simply moving the fingers of one hand!"
            "Sure, Scottie can't get his fingers as deep into me as he could his manhood."
            "But then his manhood could never move in the same way once in there."
            "And, of course, he only has one of those!"
            "They wander here and there, exploring the soft space inside of me."
            "Every spot they touch as tender and intimate as it's possible to be."
            "I know that I can't stand much more of this."
            "So it comes as a genuine relief when I feel myself beginning to cum."
            bree.say "Ah..."
            show scottie missionary pleasure
            bree.say "Scottie..."
            "I don't see what the look on his face is as I say this."
            "Because I close my eyes tightly as my orgasm takes hold."
            "My hands grip the bedclothes as I hold on for dear life."
            show scottie missionary -finger
            "And only when he sees what's happening to me does Scottie finally stop."
            show scottie missionary -nonpc
        "Fuck now" if hero.morality < -25:
            pass
    "Scottie puts one hand under each of my thighs."
    show scottie missionary normal pose3 down
    "Then he jerks me forwards so that my groin connects with his."
    scottie.say "So, [hero.name]..."
    scottie.say "Where'd you want it?"
    scottie.say "Front-door or back-door?"
    menu:
        "Ask for vaginal sex":
            "Normally I'd be more than a little pissed off at that kind of question."
            "I'm not a prude, but it's still way too on the nose!"
            "But somehow it doesn't seem to bother me tonight."
            "I guess I must simply be in a more tolerant mood than usual."
            bree.say "Mmm..."
            bree.say "Front-door, Scottie..."
            bree.say "I want you in my pussy!"
            "Scottie gives me a wink and a smile."
            scottie.say "You got it, babe!"
            call check_condom_usage (scottie) from _call_check_condom_usage_132
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show scottie missionary condom
            "Scottie doesn't waste any time once he knows what I want of him."
            "He simply lowers himself down atop me and gets down to business."
            "It's not the kind of subtle seduction a modern girl's used to."
            "But sometimes it's fun to just thrown down and do it."
            show scottie missionary pose2
            "And that notion becomes a reality a moment later, when I feel his cock between my legs."
            "It's a lot like Scottie himself, big, hard and thick."
            show scottie missionary pose1
            "Sticking it's head into whatever happens to be in front of it."
            "Right now that just so happens to be my pussy."
            "And it's more than ready for what he's going to do to it!"
            "There's the usual token show of resistance."
            "The lips doing the best they can to keep him out."
            "But they're the one part of my body that's still fighting back."
            "And they soon decide that surrender is the only option."
            show scottie missionary vaginal pleasure
            scottie.say "Ha ha..."
            scottie.say "Here I come, [hero.name]!"
            bree.say "Ah..."
            show scottie missionary pose2 pain
            bree.say "Oh fuck..."
            "All of a sudden the resistance is gone, and there's nothing holding him back."
            "But Scottie's still thrusting forwards with all of his might."
            show scottie missionary pose3 pleasure
            "And now that effort sees him sink deep into me without stopping."
            "The only thing that halts his advance is the act of filling me completely."
            "But it's not like I know all of this is happening in the moment."
            "Instead my senses are overloaded by the sensation of having him inside of me."
            "Like I already said, Scottie's a big boy, and he's almost more than I can take."
            "Even before he regains his composure and starts to move, I'm all but overwhelmed."
            "And when he does, it only takes a couple of seconds for me to be rendered helpless."
            show scottie missionary pain pose2
            pause 0.15
            show scottie missionary pose1
            pause 0.35
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3
            pause 0.25
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose1
            pause 0.35
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3
            pause 0.25
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose1
            pause 0.35
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 at startle(0.05,-10)
            "All Scottie's doing is thrusting back and forth, going in and out."
            "But it feels like he's somehow reaching every part of me as he does so."
            "I'm laid there under him, feeling like I'm pinned to the bed."
            "And the crazy thing is that I just want him to go harder and faster still."
            bree.say "S...Scottie..."
            bree.say "M...more..."
            bree.say "I...I need more!"
            "Scottie looks down at me with a smile on his face."
            "And he nods like what I'm asking him is nothing at all."
            scottie.say "Oh..."
            scottie.say "Okay, babe..."
            scottie.say "I was just...gonna take it slow!"
            "At first I think Scottie's just bragging."
            "That he's trying to talk himself up."
            "But then I feel a renewed surge of energy as his body begins to move even faster than before."
            show scottie missionary pleasure pose2
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            "I asked for it, and now I'm getting it in spades."
            "And I can safely say that Scottie wasn't bragging."
            "Once he gets up to speed, the guy's like a fucking machine!"
            show scottie missionary pleasure pose2
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            "If I was overwhelmed before, then I'm totally helpless now."
            "I can't do a thing but lie back and let it happen to me."
            "Scottie's pushing me harder by the second."
            show scottie missionary pleasure pose2
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            "And I know that I won't be able to hold on much longer."
            "So when I feel myself starting to cum, it's almost a relief."
            "Because the change in my body seems to be enough to affect Scottie too."
            scottie.say "Whoa!"
            scottie.say "Get ready, babe..."
            scottie.say "I'm gonna lose it - big time!"
            call cum_reaction (scottie, 'vaginal', sexperience_min) from _call_cum_reaction_243
            if _return == "vaginal_outside":
                show scottie missionary pain
                "I recall at the last possible second that we chose not to use a condom."
                "That means I have to pull out of Scottie as I feel him start to cum."
                "I want him out of me when it happens, and that's what I get."
                show scottie missionary pose2
                pause 0.1
                show scottie missionary pose1
                pause 0.275
                show scottie missionary pose2 speed
                pause 0.1
                show scottie missionary pose3 at startle(0.05,-10)
                pause 0.175
                show scottie missionary pose2 -speed
                pause 0.1
                show scottie missionary pose1 outside
                pause 0.275
                show scottie missionary pose2
                pause 0.1
                show scottie missionary pose3 ahegao cumshot with hpunch
                $ scottie.sub += 1
                "Like every part of this that's gone before, it's incredible, even explosive."
                with hpunch
                "Even though it's only the sensation of his cock popping out of me."
                with hpunch
                "I can feel the warmth of Scottie's cum as it rains down on me from above."
                "And it's totally overwhelming me too, making me want to close my eyes and black-out."
                "Or maybe I'm just finally falling asleep after all of this exertion."
                show scottie missionary pleasure
                "Either way I can feel my eyes starting to close as I sink into unconsciousness."
            else:
                "I recall at the last possible second that we remembered to use a condom."
                "That means I have no problem grabbing hold of Scottie as I feel him start to cum."
                "I want him as deep inside of me as possible when it happens, and that's what I get."
                show scottie missionary pose2
                pause 0.1
                show scottie missionary pose1
                pause 0.275
                show scottie missionary pose2 speed
                pause 0.1
                show scottie missionary pose3 at startle(0.05,-10)
                pause 0.175
                show scottie missionary pose2 -speed
                pause 0.1
                show scottie missionary pose1
                pause 0.275
                show scottie missionary pose2
                pause 0.1
                show scottie missionary pose3 ahegao creampie with hpunch
                $ scottie.love += 2
                if not CONDOM and hero.morality > 0:
                    $ hero.morality -= 4
                "Like every part of this that's gone before, it's incredible, even explosive."
                with hpunch
                "I feel like Scottie's orgasm is feeding my own, becoming a part of it."
                with hpunch
                "And it's totally overwhelming me too, making me want to close my eyes and black-out."
                "Or maybe I'm just finally falling asleep after all of this exertion."
                show scottie missionary pleasure
                "Either way I can feel my eyes starting to close as I sink into unconsciousness."
        "Ask for anal sex" if hero.sexperience >= (sexperience_min + 5):
            "Normally I'd be more than a little pissed off at that kind of question."
            "I'm not a prude, but it's still way too on the nose!"
            "But somehow it doesn't seem to bother me tonight."
            "I guess I must simply be in a more tolerant mood than usual."
            bree.say "Mmm..."
            if hero.morality > 0:
                $ hero.morality -= 2
            bree.say "Back-door, Scottie..."
            bree.say "I want you in my ass!"
            "Scottie gives me a wink and a smile."
            scottie.say "Ooh..."
            scottie.say "Feeling a little extra spicy tonight, huh?"
            scottie.say "You got it, babe!"
            "Scottie doesn't waste any time once he knows what I want of him."
            "He simply lowers himself down atop me and gets down to business."
            "It's not the kind of subtle seduction a modern girl's used to."
            "But sometimes it's fun to just thrown down and do it."
            show scottie missionary pose2
            "And that notion becomes a reality a moment later, when I feel his cock between my buttocks."
            "It's a lot like Scottie himself, big, hard and thick."
            show scottie missionary pose1
            "Sticking it's head into whatever happens to be in front of it."
            "Right now that just so happens to be my ass."
            "And it's more than ready for what he's going to do to it!"
            "There's the usual token show of resistance."
            "The muscles doing the best they can to keep him out."
            "But they're the one part of my body that's still fighting back."
            "And they soon decide that surrender is the only option."
            show scottie missionary anal pleasure
            scottie.say "Ha ha..."
            scottie.say "Here I come, [hero.name]!"
            bree.say "Ah..."
            show scottie missionary pose2 pain
            bree.say "Oh fuck..."
            "All of a sudden the resistance is gone, and there's nothing holding him back."
            "But Scottie's still thrusting forwards with all of his might."
            show scottie missionary pose3 pleasure
            "And now that effort sees him sink deep into me without stopping."
            "The only thing that halts his advance is the act of filling me completely."
            "But it's not like I know all of this is happening in the moment."
            "Instead my senses are overloaded by the sensation of having him inside of me."
            "Like I already said, Scottie's a big boy, and he's almost more than I can take."
            "Even before he regains his composure and starts to move, I'm all but overwhelmed."
            "And when he does, it only takes a couple of seconds for me to be rendered helpless."
            show scottie missionary pain pose2
            pause 0.15
            show scottie missionary pose1
            pause 0.35
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3
            pause 0.25
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose1
            pause 0.35
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3
            pause 0.25
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose1
            pause 0.35
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3
            "All Scottie's doing is thrusting back and forth, going in and out."
            "But it feels like he's somehow reaching every part of me as he does so."
            "I'm laid there under him, feeling like I'm pinned to the bed."
            "And the crazy thing is that I just want him to go harder and faster still."
            bree.say "S...Scottie..."
            bree.say "M...more..."
            bree.say "I...I need more!"
            "Scottie looks down at me with a smile on his face."
            "And he nods like what I'm asking him is nothing at all."
            scottie.say "Oh..."
            scottie.say "Okay, babe..."
            scottie.say "I was just...gonna take it slow!"
            "At first I think Scottie's just bragging."
            "That he's trying to talk himself up."
            "But then I feel a renewed surge of energy as his body begins to move even faster than before."
            show scottie missionary pleasure pose2
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            "I asked for it, and now I'm getting it in spades."
            "And I can safely say that Scottie wasn't bragging."
            "Once he gets up to speed, the guy's like a fucking machine!"
            show scottie missionary pleasure pose2
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            "If I was overwhelmed before, then I'm totally helpless now."
            "I can't do a thing but lie back and let it happen to me."
            "Scottie's pushing me harder by the second."
            show scottie missionary pleasure pose2
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2 speed
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            pause 0.175
            show scottie missionary pose2 -speed
            pause 0.1
            show scottie missionary pose1
            pause 0.275
            show scottie missionary pose2
            pause 0.1
            show scottie missionary pose3 at startle(0.05,-10)
            "And I know that I won't be able to hold on much longer."
            "So when I feel myself starting to cum, it's almost a relief."
            "Because the change in my body seems to be enough to affect Scottie too."
            scottie.say "Whoa!"
            scottie.say "Get ready, babe..."
            scottie.say "I'm gonna lose it - big time!"
            call cum_reaction (scottie, 'anal', sexperience_min) from _call_cum_reaction_244
            if _return == "anal_outside":
                show scottie missionary pain
                "I remember at the last possible second that I wanted Scottie to pull out."
                "That means I have to act fast as I feel him start to cum."
                "I want him out of me when it happens, and that's what I get."
                show scottie missionary pose2
                pause 0.1
                show scottie missionary pose1
                pause 0.275
                show scottie missionary pose2 speed
                pause 0.1
                show scottie missionary pose3 at startle(0.05,-10)
                pause 0.175
                show scottie missionary pose2 -speed
                pause 0.1
                show scottie missionary pose1 outside
                pause 0.275
                show scottie missionary pose2
                pause 0.1
                show scottie missionary pose3 ahegao cumshot with hpunch
                $ scottie.sub += 1
                "Like every part of this that's gone before, it's incredible, even explosive."
                with hpunch
                "Even though it's only the sensation of his cock popping out of me."
                with hpunch
                "I can feel the warmth of Scottie's cum as it rains down on me from above."
                "And it's totally overwhelming me too, making me want to close my eyes and black-out."
                "Or maybe I'm just finally falling asleep after all of this exertion."
                show scottie missionary pleasure
                "Either way I can feel my eyes starting to close as I sink into unconsciousness."
            else:
                "I remember at the last possible second that we chose to use the back-door."
                "That means I have no problem grabbing hold of Scottie as I feel him start to cum."
                "I want him as deep inside of me as possible when it happens, and that's what I get."
                show scottie missionary pose2
                pause 0.1
                show scottie missionary pose1
                pause 0.275
                show scottie missionary pose2 speed
                pause 0.1
                show scottie missionary pose3 at startle(0.05,-10)
                pause 0.175
                show scottie missionary pose2 -speed
                pause 0.1
                show scottie missionary pose1
                pause 0.275
                show scottie missionary pose2
                pause 0.1
                show scottie missionary pose3 ahegao creampie with hpunch
                $ scottie.love += 2
                "Like every part of this that's gone before, it's incredible, even explosive."
                with hpunch
                "I feel like Scottie's orgasm is feeding my own, becoming a part of it."
                with hpunch
                "And it's totally overwhelming me too, making me want to close my eyes and black-out."
                "Or maybe I'm just finally falling asleep after all of this exertion."
                show scottie missionary pleasure
                "Either way I can feel my eyes starting to close as I sink into unconsciousness."
    return

label scottie_fuck_date_spoon(sexperience_min):
    if scottie.sub < 75:
        scottie.say "What are you waiting for?"
        scottie.say "Get your ass on that bed, girl."
        "I clamber to obey, eager to see what Scottie has in store for me next."
        if randint(1, 100) <= 10 + scottie.flags.anal * 10:
            "Scottie guides me down onto the bed so that I'm on all fours, and then begins to gently probe my ass with one finger."
            "I've never had too much experience with anal before, and I've already seen that Scottie's not a little guy in that department."
            "Luckily for me there's a bottle of lube on the bedside table, and I hear him pumping some onto the palm of his hand."
            hide scottie
            show breemc scottie spoon bedroom2 anal
            with fade
            scottie.say "Open wide, [hero.name] - here it comes!"
            "At first I don't think my ass can take the size of him, but then he pushes harder, and he's inside of me."
            "I moan, deep and low, as he slides further in, the width of him forcing my muscles to make room for him."
            if game.flags.analSkill < 5:
                $ posi = "v"
                if scottie.flags.anal:
                    $ scottie.flags.anal -= 1
                "While my ass is stretching to take all of him in, Scottie's dick is also starting to really hurt me more with every new thrust he makes."
                bree.say "Oh...oh, Scottie...it hurts!"
                scottie.say "What...really?"
                bree.say "Yeah...you're...you're just much too big for my ass!"
                bree.say "Please...take it out and put it in my pussy...please?!?"
                hide bree
                show breemc scottie spoon bedroom2 out
                with fade
                "Disappointed to have to pull out, but his ego undoubtedly stroked at the same time, Scottie does as I ask."
                "I can already feel the weight of his dick as it sways against my back and the inside of my thighs."
                "I can also feel my pussy stirring in anticipation as it comes ever closer with each pass."
                scottie.say "Little [hero.name], little [hero.name]...let me in!"
                if scottie.love + randint(1, 100) <= 150:
                    $ posi += "c"
                    "Scottie pauses in the middle of making for my pussy, my playing along with his game distracting him from the annoyance of stopping for a moment."
                    "He hastily fumbles for a condom from the bedside table and rolls it on."


                    show breemc scottie spoon bedroom2 vaginal
                    "And then he's finally on me and in me, sliding inside and not stopping until all of him is buried in me."
                    "I've been with guys so terrified of screwing this up that they did just that."
                    "But Scottie's too simple to be that preoccupied, and he simply sets about pleasing himself in the most immediate way possible."
                    "Part of me feels like I'm just along for the ride."
                    "But all the same - what a ride!"
                    bree.say "Don't stop now, I want to feel it all."
                    show breemc scottie spoon bedroom2 vaginal cum eyes_ahegao mouth_ahegao with hpunch
                    "I don't know if Scottie was planning to pull out or not, but he won't if I have anything to do with it."
                    with hpunch
                    "I can feel his pace quicken even as I begin to succumb to my own climax, and he cums within seconds of me."
                else:
                    bree.say "What time is it, Mr Wolf?"
                    scottie.say "Time I was balls deep inside of you!"
                    "I ask you, with wit like that, how can a girl hope to resist?"
                    show breemc scottie spoon bedroom2 vaginal
                    "Scottie makes good on his promise a moment later, and I feel the sensation of him filling me completely."
                    "I wrap my legs around his, almost desperately and in fear of losing an inch of him."
                    "But I needn't have feared, as he pushes as deeply into me as he's able, forcing me down onto the bed and pinning me there."
                    "There's no more words now, only the sound of him almost growling as he rides me and my own mounting cries of fast approaching climax."
                    if scottie.love + randint(1, 100) >= 200:
                        show breemc scottie spoon bedroom2 vaginal cum eyes_ahegao mouth_ahegao with hpunch
                        "I start to buck and twitch as my orgasm takes me."
                        with hpunch
                        "Scottie responds in kind, holding me firmly in place as he cums."
                        with hpunch
                        "I can feel him spreading inside of me like a slow-motion firework."
                        with hpunch
                        "He pushes me onwards into a second climax, prolonging my ecstasy still further."
                    else:
                        show breemc scottie spoon bedroom2 out eyes_closed mouth_ahegao cum with hpunch
                        "Almost the same moment that I climax, Scottie pulls out of me."
                        with hpunch
                        "The sudden and unexpected void makes my orgasm somehow less, more hollow in nature."
                        with hpunch
                        "He cums a few seconds later, spreading his load across my buttocks and lower back."
            else:
                $ posi = "a"
                $ scottie.flags.anal += 1
                if game.flags.analSkill < 10:
                    $ game.flags.analVirginity = 1
                    "My ass feels like something back there is going to tear or brake at any moment, but at the same time, the sensation is phenomenal."
                    bree.say "Scottie, keep it up...break me if you have to!"
                    "I can feel the instant effect that my words have on Scottie, driving him to fuck me even harder than before."
                    scottie.say "You like that, huh?"
                    bree.say "Oh yes, Scottie...god...I feel like my ass was made for your dick!"
                    "I can feel him quicken yet again, raising the sensations from my ass almost to the level of making me want to scream."
                else:
                    if not game.flags.analVirginity:
                        "I've never really had someone fuck me up the ass before now."
                        "Sure, I've messed around back there with fingers and toys, but never with a guy's dick!"
                        "At first I wonder if it'll be at all like being fucked in the pussy, but as soon as Scottie's cock is between by buttocks, I know that's not going to be the case."
                        $ game.flags.analVirginity = 1
                    "He's hard enough to make the muscles of my ass part for him, and they resist so much that every in of him feels incredible as he pushes his way into me."
                    "At the same time as I'm moaning in reaction to Scottie, I can hear him groaning from the effort and the clenching of my muscles around his dick."
                    show breemc scottie spoon bedroom2 anal eyes_closed mouth_ahegao
                    bree.say "Fuck my ass harder, Scottie...please!"
                    "He struggles to oblige, the more pressure he puts on my already taut ass, the better it feels."
                    "Just when I think that something is about to break and I'm screaming in pain, I realise it's actually that I'm right on the brink of cumming."
                show breemc scottie spoon bedroom2 anal eyes_ahegao mouth_ahegao cum with hpunch
                "I start to buck and twitch as my orgasm takes me."
                with hpunch
                "Scottie responds in kind, holding me firmly in place as he cums."
                with hpunch
                "I can feel him spreading inside my ass like a slow-motion firework."
                with hpunch
                "The feeling pushes me onwards into a second climax, prolonging my ecstasy still further."
        else:
            $ posi = "v"
            if scottie.flags.anal:
                $ scottie.flags.anal -= 1
            "Scottie pushes me suddenly backwards so that I collapse onto the bed, and almost pounces on my back."
            "He's not careful about where his weight ends up, but the feeling is like being ravished by something a little bit wild and out of control."
            show breemc scottie spoon bedroom2 out with fade
            "I can already feel the weight of his dick as it sways against my back and the inside of my thighs."
            "I can also feel my pussy stirring in anticipation as it comes ever closer with each pass."
            scottie.say "Little [hero.name], little [hero.name]...let me in!"
            if scottie.love + randint(1, 100) <= 150:
                $ posi += "c"
                "Scottie pauses in the middle of making for my pussy, my playing along with his game distracting him from the annoyance of stopping for a moment."
                "He hastily fumbles for a condom from the bedside table and rolls it on."
                show breemc scottie spoon bedroom2 vaginal condom
                "And then he's finally on me and in me, sliding inside and not stopping until all of him is buried in me."
                "I've been with guys so terrified of screwing this up that they did just that."
                "But Scottie's too simple to be that preoccupied, and he simply sets about pleasing himself in the most immediate way possible."
                "Part of me feels like I'm just along for the ride."
                "But all the same - what a ride!"
                bree.say "Don't stop now, I want to feel it all."
                show breemc scottie spoon bedroom2 vaginal cum eyes_ahegao mouth_ahegao with hpunch
                "I don't know if Scottie was planning to pull out or not, but he won't if I have anything to do with it."
                with hpunch
                "I can feel his pace quicken even as I begin to succumb to my own climax, and he cums within seconds of me."
            else:
                bree.say "What time is it, Mr Wolf?"
                scottie.say "Time I was balls deep inside of you!"
                "I ask you, with wit like that, how can a girl hope to resist?"
                show breemc scottie spoon bedroom2 vaginal
                "Scottie makes good on his promise a moment later, and I feel the sensation of him filling me completely."
                "I wrap my legs around his, almost desperately and in fear of losing an inch of him."
                "But I needn't have feared, as he pushes as deeply into me as he's able, forcing me down onto the bed and pinning me there."
                "There's no more words now, only the sound of him almost growling as he rides me and my own mounting cries of fast approaching climax."
                if scottie.love + randint(1, 100) >= 200:
                    show breemc scottie spoon bedroom2 vaginal cum eyes_ahegao mouth_ahegao with hpunch
                    "I start to buck and twitch as my orgasm takes me."
                    with hpunch
                    "Scottie responds in kind, holding me firmly in place as he cums."
                    with hpunch
                    "I can feel him spreading inside of me like a slow-motion firework."
                    with hpunch
                    "He pushes me onwards into a second climax, prolonging my ecstasy still further."
                    $ scottie.impregnate()
                    $ scottie.love += 1
                else:
                    show breemc scottie spoon bedroom2 out eyes_closed mouth_ahegao cum with hpunch
                    "Almost the same moment that I climax, Scottie pulls out of me."
                    with hpunch
                    "The sudden and unexpected void makes my orgasm somehow less, more hollow in nature."
                    with hpunch
                    "He cums a few seconds later, spreading his load across my buttocks and lower back."
        hide bree
        show scottie naked b at center, zoomAt(1.5, (640, 1040))
        with fade
        scottie.say "Don't just lie there panting - get cleaning me up, you lazy bitch!"
        if "c" in posi:
            scottie.say "Shame to see this stuff go to waste!"
            "Scottie peels the condom off of his dick and squeezes it so that the end holding his cum bulges."
            scottie.say "Open wide, [hero.name]!"
            "I stick out my tongue and allow Scottie to pour the contents of the condom onto it."
            "It's already cold, and I can feel it slithering over my tongue and down my throat."
        elif "v" in posi:
            menu:
                "Do it" if hero.morality < 0:
                    "Scottie's dick is already drooping, but there's still a considerable amount of ground to cover."
                    "I begin to lick him clean from the base of his cock and then work my way upwards, circling the shaft as I go."
                    scottie.say "Don't skimp on the clean up, [hero.name] - make sure you get into all the nooks and crannies!"
                    "I try my best to oblige, being sure to pay particular attention to the head and tip before I'm done."
                "Don't do it":
                    bree.say "Eww, Scottie - I'm up for this whole kinky thing, but there's a fucking limit!"
                    scottie.say "Don't talk back, bitch - do as I say, now!"
                    bree.say "Seriously, Scottie...go wash that thing in the bathroom or something."
                    bree.say "Just stop waving it in my face!"
                    "Scottie's face falls as he realises that I'm deadly serious."
                    scottie.say "Erm...oh, okay..."
        else:
            "Scottie proffers his soiled dick, fully expecting me to indulge his wishes."
            "He's already drooping by now, and the scent of him is something quite pungent."
            menu:
                "Do it" if -75 > hero.morality < -25:
                    "I try as best I can to breathe through my mouth while I perform the unappealing task."
                    "But it's not easy to do so when the vast majority of it requires the use of your lips and tongue."
                    "For the most part I manage to progress with gulps of air captured at opportune moments."
                    "Though once or twice I mess up and either catch the full aroma of Scottie and my own body commingled, or else taste the same on the back of my throat."
                    $ hero.morality -= 1
                    $ scottie.sub -= 1
                "Do it" if hero.morality <= -75:
                    "I try to clear my mind and focus on nothing but the task at hand, shutting everything else out."
                    "But the smell and sensation of it are just too much for that to work, and I can already feel myself beginning to gag."
                    "This is possibly the single most degrading thing that I have ever agreed to do in my life."
                    "A part of me still can't understand just why I'm doing it, but another is strangely turned on by the thought that I've sunk so low."
                    "No one could possibly imagine that I'd even be capable of this if they met me under normal circumstances."
                    "But somehow, allowing myself to literally clean the filth from my own ass off of Scottie's dick after he's fucked me up it is oddly liberating."
                    "If I have the courage to do this, then surely I can do anything...or have anything done to me?"
                "Don't do it":
                    bree.say "Eww, Scottie - I'm up for this whole kinky thing, but there's a fucking limit!"
                    scottie.say "Don't talk back, bitch - do as I say, now!"
                    bree.say "Seriously, Scottie...go wash that thing in the bathroom or something."
                    bree.say "Just stop waving it in my face!"
                    "Scottie's face falls as he realises that I'm deadly serious."
                    scottie.say "Erm...oh, okay..."
                    $ scottie.sub += 1
    else:
        bree.say "Now you listen very closely to me, dumbass!"
        bree.say "I want everything that you've got in you, and I want it now!"
        "Scottie's face registers a mixture of trepidation and sheer excitement as we climb onto the bed together."
        menu:
            "Tell him to fuck you in the ass":
                "I turn my back on Scottie and then get down on all fours, stalking a foot or so away from him like a haughty cat."
                "Glancing back over my shoulder, I make sure he can see that I've already spread my legs in anticipation of what's to come next."
                bree.say "What do you want, a written invitation?"
                bree.say "Lube yourself up and fuck me in the ass...NOW!"
                "Scottie's cock is fully erect even before he can get a drop of lube onto it."
                "Ready to go, he practically leaps atop me and fumbles eagerly for my ass with his dick."
                show breemc scottie spoon bedroom2 anal
                "Eager as he is, he still sinks in slowly, forcing the reluctant muscles of my ass to make way for him."
                if game.flags.analSkill < 5:
                    $ posi = "v"
                    "It doesn't take me long to realise that most of what I'm feeling is actually just pain."
                    "Game as Scottie is, he's hurting me more with every moment that passes."
                    bree.say "Stop it, fuckwit!"
                    bree.say "That freakshow cock of yours is too damn big for my ass!"
                    show breemc scottie spoon bedroom2 out
                    "Scottie stops suddenly and starts to pull himself out of me, looking confused and disappointed."
                    bree.say "Who the fuck said you could stop?"
                    bree.say "Stick it in my pussy, moron!"
                    menu:
                        "Tell him to wear a condom":
                            $ posi += "c"
                            bree.say "Uhh, uh...not until you put something on it!"
                            "Scottie looks visibly panicked until I point to the condoms on the bedside table and he dives hastily for them."
                            "It only takes him a moment to slip one on and lube himself up, and then he's back on me like a lion on its prey."
                            show breemc scottie spoon bedroom2 vaginal condom
                            "For all that he's a hopeless idiot elsewhere, Scottie really delivers where it matters."
                            "His dick is of a very nice size, and he knows exactly how to put it to good use."
                            "I want to keep on putting him in his place, enjoying the act so much."
                            "But he feels so good inside of me that I can't keep from moaning and panting like a bitch in heat."
                        "Don't":
                            "Part of me knows that I should stop Scottie and make him use protection, but the sight of his looming cock makes me desperate to get on with business."
                            show breemc scottie spoon bedroom2 out
                            "So much so that I make no protest as he covers me and I feel the head of his dick slipping between my buttocks and hunting out my already welcoming pussy."
                            show breemc scottie spoon bedroom2 vaginal
                            "He sinks into me, slowly at first and then with more urgency as he reaches the limits of his length."
                            "Scottie doesn't move for a few moments, and the feeling of his dick inside of me is almost enough to make me crazy."
                            "And then he begins to pull back and thrust forwards, gaining speed with each repetition."
                            "As I start to sigh and moan, I again find myself wondering why Sasha dumped the guy, rather than simply breaking him in properly."
                            menu:
                                "Let him cum inside":
                                    bree.say "Don't stop now, I want to feel it all."
                                    show breemc scottie spoon bedroom2 vaginal cum eyes_ahegao mouth_ahegao with hpunch
                                    "I don't know if Scottie was planning to pull out or not, but he won't if I have anything to do with it."
                                    with hpunch
                                    "I can feel his pace quicken even as I begin to succumb to my own climax, and he cums within seconds of me."
                                "Tell him to pull out":
                                    bree.say "Get your elephant prick out of me, asshole!"
                                    bree.say "Right NOW!"
                                    show breemc scottie spoon bedroom2 out eyes_closed mouth_ahegao with hpunch
                                    "Scottie struggles to do as he's told, whipping his dick out a second before I cum."
                                    with hpunch
                                    "The sudden void only serves to intensify the sensations of orgasm, almost sending me into a fit of pleasure."
                                    show breemc scottie spoon bedroom2 out eyes_closed mouth_ahegao cum with hpunch
                                    "So much so that I hardly feel Scotties own cum raining down on my ass until it starts to cool and run down my thighs."
                else:
                    $ posi += "a"
                    $ scottie.flags.anal += 1
                    $ game.flags.analVirginity = 1
                    "Scottie's enthusiasm translates almost instantly into a sensation that makes me shake with delight."
                    show breemc scottie spoon bedroom2 anal eyes_closed mouth_ahegao
                    "I'm no enthusiast when it comes to anal sex, but when it's done right, I simply love it."
                    "Each time he thrusts into me, I can feel the muscles inside of my ass pull and protest."
                    "The pleasure and pain are almost impossible to tell apart, and I find both pushing me dangerously closer to coming with each thrust."
                    bree.say "Good boy, keep it up...make me feel like you're still in there a week after you're done!"
                    show breemc scottie spoon bedroom2 anal eyes_ahegao mouth_ahegao with hpunch
                    "As Scottie struggles to obey, I hear myself begin to yelp, almost like a dog, as my orgasm comes over me."
                    with hpunch
                    bree.say "Don't stop now, I want to feel it all."
                    show breemc scottie spoon bedroom2 anal eyes_ahegao mouth_ahegao cum with hpunch
                    "I can feel his pace quicken even as I begin to succumb to my own climax, and he cums within seconds of me."
            "Tell him to fuck your pussy":
                $ posi = "v"
                "I lay down on my side, making sure that he has a grand view of all my curves."
                "Scottie watches intently as I stroke a hand up and down my thigh and squeeze one breast with the other."
                bree.say "Well, what are you waiting for?"
                bree.say "Are you going to put that donkey dick of yours to good use, or what?"
                "As if I'm talking to his cock rather then Scottie himself, I see him becoming visibly more erect with each moment that passes."
                "So I figure - why not do just that?"
                bree.say "Here, boy...come on, that's right!"
                bree.say "I've got something so nice and so juicy, just waiting for you right here!"
                menu:
                    "Tell him to wear a condom":
                        $ posi += "c"
                        bree.say "Uhh, uh...not until you put something on it!"
                        "Scottie looks visibly panicked until I point to the condoms on the bedside table and he dives hastily for them."
                        "It only takes him a moment to slip one on and lube himself up, and then he's back on me like a lion on its prey."
                        show breemc scottie spoon bedroom2 vaginal condom
                        "For all that he's a hopeless idiot elsewhere, Scottie really delivers where it matters."
                        "His dick is of a very nice size, and he knows exactly how to put it to good use."
                        "I want to keep on putting him in his place, enjoying the act so much."
                        "But he feels so good inside of me that I can't keep from moaning and panting like a bitch in heat."
                    "Don't":
                        "Part of me knows that I should stop Scottie and make him use protection, but the sight of his looming cock makes me desperate to get on with business."
                        show breemc scottie spoon bedroom2 out
                        "So much so that I make no protest as he covers me and I feel the head of his dick slipping between my buttocks and hunting out my already welcoming pussy."
                        show breemc scottie spoon bedroom2 vaginal
                        "He sinks into me, slowly at first and then with more urgency as he reaches the limits of his length."
                        "Scottie doesn't move for a few moments, and the feeling of his dick inside of me is almost enough to make me crazy."
                        "And then he begins to pull back and thrust forwards, gaining speed with each repetition."
                        "As I start to sigh and moan, I again find myself wondering why Sasha dumped the guy, rather than simply breaking him in properly."
                        menu:
                            "Let him cum inside":
                                bree.say "Don't stop now, I want to feel it all."
                                show breemc scottie spoon bedroom2 vaginal cum eyes_ahegao mouth_ahegao with hpunch
                                "I don't know if Scottie was planning to pull out or not, but he won't if I have anything to do with it."
                                with hpunch
                                "I can feel his pace quicken even as I begin to succumb to my own climax, and he cums within seconds of me."
                                $ scottie.impregnate()
                                $ scottie.love += 2
                            "Tell him to pull out":
                                bree.say "Get your elephant prick out of me, asshole!"
                                bree.say "Right NOW!"
                                show breemc scottie spoon bedroom2 out eyes_closed mouth_ahegao with hpunch
                                "Scottie struggles to do as he's told, whipping his dick out a second before I cum."
                                with hpunch
                                "The sudden void only serves to intensify the sensations of orgasm, almost sending me into a fit of pleasure."
                                show breemc scottie spoon bedroom2 out eyes_closed mouth_ahegao cum with hpunch
                                "So much so that I hardly feel Scotties own cum raining down on my ass until it starts to cool and run down my thighs."
                                $ scottie.love += 1
                                $ scottie.sub += 1
        if not "c" in posi:
            bree.say "No time for lounging around yet, asshole - you made a mess, so now clean it up!"
            if "v" in posi and scottie.sub < 50:
                "Scottie eagerly plucks up his underwear and begins to mop up between my thighs."
                "It's not the most erotic or romantic of gestures, but he seems to be trying to make a decent job of it all the same."
                "He works diligently, avoiding eye-contact until he feels that he's done."
                "And even then he waits patiently for me to inspect his works and nod in approval."
            elif "v" in posi:
                "Scottie doesn't need telling twice as he obliges me by lowering his head between my thighs."
                "He proceeds to clean me up by licking away at every accumulation of bodily fluids that he can find, and all without complaint."
                "All there is for me to do is lean back and allow him to do his thing."
                "Technically it might not be as hygienic as a shower, but it's certainly more enjoyable."
            elif "a" in posi and scottie.sub < 80:
                "Grabbing his discarded underwear, Scottie begins to dab away at my buttocks, rather like an inexperienced maid cleaning a valuable, yet fragile antique."
                "I've had more enjoyable post-sex experiences, but it's amusing to see a guy with that much swagger brought firmly to heel."
                bree.say "Make sure you do a good job back there - I want it so clean you could eat your dinner off of it!"
                "At that, Scottie redoubles his efforts, and I have to chuckle at the fact that he doesn't seem to have gotten the joke."
            elif "a" in posi:
                "Scottie is quick to crouch down and begin literally licking my ass clean."
                "He shows no shame whatsoever in using his tongue on my buttocks, persisting until there's no trace of cum to be found."
                "I don't think for a moment that he'll go deeper, but then I feel him gently part my cheeks and begin to probe between them too."
                "Scottie doesn't skimp either, exploring every inch until satisfied that he's done as he was told."
    return

label scottie_fuck_date_doggy(sexperience_min):
    scene scottie doggy
    show scottie doggy nonpc
    "I can barely climb onto the bed before he makes it across the room."
    "I'm also amazed that he manages to take off his pants and shorts too!"
    "Like an animal unleashed, he leaps onto the bed."
    "His hands reach out and grab me around the waist too."
    show scottie doggy -nonpc
    "I'm not expecting it, so I can't help crying out in surprise."
    bree.say "Whoa!"
    "But that only seems to make Scottie all the more determined."
    "Then I feel the first hits of his manhood back there too."
    "And it's like the sensation flips a switch inside of my head."
    "Suddenly I feel every bit as animalistic as Scottie seems to be acting."
    "I'm not thinking about seduction or who's in charge any longer."
    "All I can think of is getting that thing inside of me."
    "And how it's going to feel once I do!"
    menu:
        "Guide him to my pussy":
            scottie.say "So, [hero.name]..."
            scottie.say "Where do you want it?"
            "Part of me is a little surprised to hear the question."
            "I was expecting that Scottie would just take over from here."
            "But all the same, I don't hesitate to give him an answer."
            bree.say "The pussy, Scottie..."
            bree.say "That's where I want it!"
            "I hear Scottie chuckle."
            "And I can picture him nodding with a lascivious grin too."
            scottie.say "What the lady wants..."
            scottie.say "The lady gets!"
            call check_condom_usage (scottie) from _call_check_condom_usage_122
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show scottie doggy condom
            scottie.say "Ready or not, [hero.name]..."
            scottie.say "Here I come!"
            "I can't help biting my lip with anticipation."
            "And almost instantly, the wait proves worth it."
            "Scottie pushes his cock between my thighs."
            "And all at once I'm reminded of just how impressive it is!"
            "The head slides along the length of my pussy, form one end to the other."
            "The sensation makes me shudder, and I can almost feel myself beginning to open up."
            "Scottie repeats the movement, again and again without mercy."
            "And every time he makes a pass, I expect that to be the moment it happens."
            "That he's going to choose that second to take it to the next level."
            "In fact he makes so many passes that I start to become complacent."
            "And that's just what he seems to be waiting for me to do."
            "Because without warning, I feel him kick it up a level."
            "Scottie pulls me roughly backwards without warning."
            "At the same time he thrusts himself forwards."
            "There's a moment of resistance, where we both hold our breath."
            "And then it happens."
            "The lips of my pussy part and Scottie starts to slide into me."
            show scottie doggy vaginal
            "Even though I can feel the strength he's using, it's still slow."
            "That makes the sensation all the more incredible."
            "Everything feels stretched out and turned into an extreme."
            "At first Scottie seems to be totally in thrall to that sensation."
            "I can feel him moving slowly and deliberately inside of me."
            "Closing my eyes, I resign myself to going at this pace."
            show scottie doggy pleasure
            "And I even start to match my breathing to the speed too."
            play sound spank
            with hpunch
            "But suddenly I hear a sound like the cracking of a whip."
            "And my backside jumps from something hitting it really hard."
            show scottie doggy pain mark1
            bree.say "Ouch!"
            bree.say "What the..."
            show scottie doggy pleasure
            "Before I can get the words out, it happens again."
            play sound spank
            with hpunch
            "But this time I realise what's going on."
            show scottie doggy normal
            "Scottie's slapping my ass!"
            scottie.say "Oh yeah!"
            scottie.say "How'd you like that, huh?"
            scottie.say "You want some more?"
            scottie.say "Because that's what you're gonna get!"
            "I was looking back over my shoulder when Scottie started slapping my ass."
            show scottie doggy mark2 pain
            play sound spank
            with hpunch
            "But the more he does it, the harder he starts to fuck me at the same time."
            show scottie doggy pleasure
            "This means that pretty soon I can't help being overwhelmed by the sensations."
            "Little by little I'm forced to turn my head back around."
            "It's almost like the spanking I'm getting is clouding my thoughts."
            show scottie doggy mark3 pain
            play sound spank
            with hpunch
            "Like it's turning me, by degrees, into a creature of base sensations."
            show scottie doggy pleasure
            "I feel at once both humiliated and aroused, which is a confusing thing."
            "And I know that the cheeks of my face must be as red as those of my ass too."
            "Part of me feels like I should be telling Scottie off right now."
            show scottie doggy mark4 pain
            play sound spank
            with hpunch
            "Demanding that he stop what he's doing and show me more respect."
            show scottie doggy pleasure
            "But the other part of me is the one that's winning out."
            "And that's the one that's finding a strange enjoyment in my situation."
            show scottie doggy mark5 pain
            play sound spank
            with hpunch
            "I don't know how or why, but I'm getting off on what Scottie's doing to me!"
            "In fact, I can already feel myself starting to lose it!"
            show scottie doggy pleasure
            bree.say "Mmm..."
            bree.say "Scottie..."
            bree.say "You're making me..."
            bree.say "Making me cum!"
            call cum_reaction (scottie, 'vaginal', sexperience_min) from _call_cum_reaction_219
            if _return == "vaginal_outside":
                if not CONDOM:
                    "I remember that we didn't use a condom."
                    "So I have a to act before it's too late."
                "Moving forwards, I make sure that Scottie slides out of me."
                show scottie doggy -vaginal
                "The sensation is more than enough to push me over the edge."
                "And it seems like the same is true for him too."
                show scottie doggy ahegao with hpunch
                "I collapse onto the bed, overtaken by my own orgasm."
                "At the same time I hear Scottie gasping."
                show scottie doggy cumshot with hpunch
                $ scottie.love += 2
                "And I feel him shooting his load over my buttocks too."
            else:
                if CONDOM:
                    "Remembering that we used a condom, I make a decision."
                "I don't want Scottie to pull out before the end."
                "So I push myself backwards, hard against him."
                show scottie doggy ahegao with hpunch
                "This seems to be more than enough to do the job."
                with hpunch
                "And a moment later I feel him begin to cum too."
                show scottie doggy creampie with hpunch
                if not CONDOM:
                    $ scottie.impregnate()
                $ scottie.love += 5
                "But after that, I don't remember much at all."
                "Only the overwhelming sensation of my own orgasm."
        "Guide him to my ass" if hero.sexperience >= (sexperience_min + 5):
            scottie.say "So, [hero.name]..."
            scottie.say "Where do you want it?"
            "Part of me is a little surprised to hear the question."
            "I was expecting that Scottie would just take over from here."
            "But all the same, I don't hesitate to give him an answer."
            bree.say "The ass, Scottie..."
            bree.say "That's where I want it!"
            "I hear Scottie chuckle."
            "And I can picture him nodding with a lascivious grin too."
            scottie.say "What the lady wants..."
            scottie.say "The lady gets!"
            scottie.say "Ready or not, [hero.name]..."
            scottie.say "Here I come!"
            "I can't help biting my lip with anticipation."
            "And almost instantly, the wait proves worth it."
            "Scottie pushes his cock between my thighs."
            "And all at once I'm reminded of just how impressive it is!"
            "The head slides around the hole of my ass."
            "The sensation makes me shudder, and I can almost feel myself beginning to open up."
            "Scottie repeats the movement, again and again without mercy."
            "And every time he makes a pass, I expect that to be the moment it happens."
            "That he's going to choose that second to take it to the next level."
            "In fact he makes so many passes that I start to become complacent."
            "And that's just what he seems to be waiting for me to do."
            "Because without warning, I feel him kick it up a level."
            "Scottie pulls me roughly backwards without warning."
            "At the same time he thrusts himself forwards."
            "There's a moment of resistance, where we both hold our breath."
            "And then it happens."
            "The muscles of my ass begin to relax and Scottie starts to slide into me."
            show scottie doggy anal
            "Even though I can feel the strength he's using, it's still slow."
            "That makes the sensation all the more incredible."
            "Everything feels stretched out and turned into an extreme."
            "At first Scottie seems to be totally in thrall to that sensation."
            "I can feel him moving slowly and deliberately inside of me."
            "Closing my eyes, I resign myself to going at this pace."
            show scottie doggy pleasure
            "And I even start to match my breathing to the speed too."
            play sound spank
            with hpunch
            "But suddenly I hear a sound like the cracking of a whip."
            "And my backside jumps from something hitting it really hard."
            show scottie doggy pain mark1
            bree.say "Ouch!"
            show scottie doggy pleasure
            bree.say "What the..."
            "Before I can get the words out, it happens again."
            play sound spank
            with hpunch
            "But this time I realise what's going on."
            show scottie doggy normal
            "Scottie's slapping my ass!"
            scottie.say "Oh yeah!"
            scottie.say "How'd you like that, huh?"
            scottie.say "You want some more?"
            scottie.say "Because that's what you're gonna get!"
            "I was looking back over my shoulder when Scottie started slapping my ass."
            show scottie doggy mark2 pain
            play sound spank
            with hpunch
            "But the more he does it, the harder he starts to fuck me at the same time."
            show scottie doggy pleasure
            "This means that pretty soon I can't help being overwhelmed by the sensations."
            "Little by little I'm forced to turn my head back around."
            "It's almost like the spanking I'm getting is clouding my thoughts."
            show scottie doggy mark3 pain
            play sound spank
            with hpunch
            "Like it's turning me, by degrees, into a creature of base sensations."
            show scottie doggy pleasure
            "I feel at once both humiliated and aroused, which is a confusing thing."
            "And I know that the cheeks of my face must be as red as those of my ass too."
            "Part of me feels like I should be telling Scottie off right now."
            show scottie doggy mark4 pain
            play sound spank
            with hpunch
            "Demanding that he stop what he's doing and show me more respect."
            show scottie doggy pleasure
            "But the other part of me is the one that's winning out."
            "And that's the one that's finding a strange enjoyment in my situation."
            show scottie doggy mark5 pain
            play sound spank
            with hpunch
            "I don't know how or why, but I'm getting off on what Scottie's doing to me!"
            "In fact, I can already feel myself starting to lose it!"
            show scottie doggy pleasure
            bree.say "Mmm..."
            bree.say "Scottie..."
            bree.say "You're making me..."
            bree.say "Making me cum!"
            call cum_reaction (scottie, 'anal', sexperience_min) from _call_cum_reaction_220
            if _return == "anal_outside":
                "I decide that I don't want Scottie to cum in my ass."
                "So I have a to act before it's too late."
                "Moving forwards, I make sure that Scottie slides out of me."
                show scottie doggy -anal
                "The sensation is more than enough to push me over the edge."
                show scottie doggy ahegao with hpunch
                "And it seems like the same is true for him too."
                with hpunch
                "I collapse onto the bed, overtaken by my own orgasm."
                show scottie doggy cumshot with hpunch
                $ scottie.sub += 1
                "At the same time I hear Scottie gasping."
                "And I feel him shooting his load over my buttocks too."
            else:
                "Remembering that he's doing me up the ass, I make a decision."
                "I don't want Scottie to pull out before the end."
                "So I push myself backwards, hard against him."
                show scottie doggy ahegao with hpunch
                "This seems to be more than enough to do the job."
                with hpunch
                "And a moment later I feel him begin to cum too."
                show scottie doggy creampie with hpunch
                $ scottie.love += 2
                "But after that, I don't remember much at all."
                "Only the overwhelming sensation of my own orgasm."
    return


label scottie_fuck_beach_female:
label scottie_fuck_nudistbeach_female:
label scottie_fuck_date_nudistbeach_female:
label scottie_fuck_date_beach_female:
    $ CONDOM = False
    scene bg beach
    "The weather report was right for once, today's nothing but clear skies and red-hot sun."
    "Which makes me glad that we chose to trust it and spend some time at the beach."
    "All I want to do now is lie back and soak up the rays so I can get a natural tan."
    show scottie
    "But Scottie seems to have very different ideas, none of which involve sun-bathing."
    "I can tell that there's something bugging him as soon as we choose a spot and lie down."
    "Anyone else and I'd have said they had something on their mind."
    "But I still can't be sure that Scottie actually has one of his own."
    "Though he's getting on my nerves."
    "As he won't stop looking back to the more crowded part of the beach."
    scottie.say "Wow..."
    scottie.say "How far away do you think those girls over there are?"
    "I sit up and frown as Scottie points down the beach."
    bree.say "What are you talking about, Scottie?"
    scottie.say "Those girls over there, [hero.name]..."
    scottie.say "I can see them for sure."
    scottie.say "But do you think they can see me too?"
    bree.say "What does it matter if they can or can't?"
    bree.say "Surely they're just enjoying the beach."
    bree.say "You know, like I'm trying to right now?"
    "Scottie doesn't seem to get the unsubtle hint that I don't care."
    "And he certainly doesn't notice the irritable tone of my voice either."
    scottie.say "I bet they can, [hero.name]..."
    scottie.say "I bet they can see everything we're doing over here!"
    "Seeing that Scottie's not going to let it drop, I let out a grunt of annoyance."
    "And I haul myself up to look in the same direction as he is."
    "I squint at the girls he must mean, and then I shake my head."
    bree.say "You're wrong, Scottie."
    bree.say "There's no way they can see us from over there."
    scottie.say "You're sure?"
    show scottie happy
    scottie.say "That's great news, [hero.name]!"
    bree.say "It is?"
    scottie.say "Of course it is."
    show scottie perv
    scottie.say "It means we can do stuff without them seeing us!"
    "From the look on Scottie's face, I can see where this is going."
    "Now that he's got the answer he wanted, he can't hide it any longer."
    "And I can read him like book!"
    bree.say "Not now, Scottie..."
    bree.say "I'm not in the mood, okay?"
    show scottie surprised at startle
    scottie.say "WHAT?!?"
    show scottie annoyed
    scottie.say "Oh come on, [hero.name]."
    scottie.say "You've been teasing me since we got here!"
    scottie.say "How is that fair?"
    bree.say "What are you talking about, Scottie?"
    bree.say "I haven't been teasing you at all."
    if not game.room == 'date_nudistbeach':
        bree.say "All I've done is lie here in my swimsuit!"
    else:
        bree.say "All I've done is lie here!"
    show scottie embarrassed
    scottie.say "But, [hero.name]..."
    show scottie surprised
    scottie.say "That IS teasing me!"
    scottie.say "I can see every inch of your body - and I'm only human!"
    "I shake my head as I lie back down."
    bree.say "Sounds like you need to cool down, Scottie."
    bree.say "Why not go take a swim in the sea of something?"
    show scottie annoyed
    scottie.say "Urgh..."
    scottie.say "It was never this boring when I came here with Sasha!"
    "The moment I hear the mention of my housemate's name, my eyes snap open."
    show scottie surprised at center, zoomAt(1.5, (640, 1140))
    with vpunch
    "And a second later I'm sat up, one hand grabbing Scottie by the jaw."
    "With a strength that surprises me, I turn his entire head to face me."
    bree.say "What did you just say?"
    scottie.say "Ouch..."
    show scottie embarrassed
    scottie.say "[hero.name]..."
    scottie.say "You're hurting me!"
    with hpunch
    "This earns Scottie an even harder squeeze."
    bree.say "I asked you a question!"
    scottie.say "Okay, okay..."
    scottie.say "I said it was never this boring with Sasha!"
    scottie.say "She's do stuff with me..."
    scottie.say "Fun stuff..."
    scottie.say "Naughty stuff too!"
    "I already know what he's trying to do."
    "And I know that I shouldn't rise to it either."
    "But the mere thought of Scottie comparing me to Sasha..."
    "Well, it makes me feel more than a little crazy!"
    "I know that it's an emotion that I shouldn't be feeling."
    "And it's not like I feel jealous of Sasha in any other way."
    "It's just that when Scottie uses her against me, it totally sets me off."
    "Like I can't stand to be compared to the last girl he dated in any way, shape or form!"
    "I push Scottie down onto the sand, where he lands with gasp."
    "Then I swing a leg over him so that I can straddle his thighs."
    bree.say "So..."
    bree.say "Sasha's more fun than me, is she?!?"
    scottie.say "I..."
    show scottie blush
    scottie.say "I didn't mean it like that, [hero.name]!"
    bree.say "Oh no?"
    bree.say "Because that's how it sounded to me!"
    bree.say "And I think that means you need to be educated."
    bree.say "Educated about how I'm every bit as exciting as Sasha!"
    "I'm already pulling down his trunks as I say this."
    "And as soon as they're off him, I do the same with my swimsuit too."
    scene scottie cowgirl
    show scottie cowgirl beach
    with fade
    "Then I grab Scottie's cock and begin to rub him to life."
    scottie.say "[hero.name[0]]...[hero.name]..."
    scottie.say "Please...be gentle?"
    bree.say "I'm not making any promises, Scottie!"
    menu:
        "Guide him to my pussy":
            "It doesn't take long for me to get Scottie good and hard."
            "I might not know if it's more from arousal or fear."
            "But that's not something I choose to dwell upon for too long."
            "Instead I push the head of his cock hard against the lips of my pussy."
            bree.say "How's that feel, Scottie?"
            show scottie cowgirl vaginal
            bree.say "Is that what you want, huh?"
            "Scottie's nodding his head as I say all of this."
            "His eyes as wide as saucers the whole time."
            scottie.say "Y...yeah, [hero.name]..."
            scottie.say "That's it!"
            scottie.say "Can...can I have some more?"
            "I feel a wicked smile creeping onto my face as he says this."
            "Like he's in my power and can't escape."
            "So I do as he asks, rubbing the head of his cock along my lips."
            "Scottie's already panting and gasping from the pleasure he's feeling."
            "But the truth is that I'm fighting from one second to the next."
            "Fighting not to let on that I'm feeling the same way too."
            "Sure, I'm enjoying the feeling of holding power over him."
            "But the sensation of his cock, warm and hard in the palm of my hand..."
            "It's filling me with desire at the same time."
            "The effort only becomes that much harder when the inevitable happens too."
            "As I feel my own body surrender to desire, I have to bite my lip."
            show scottie cowgirl down pain
            "And as Scottie's cock begins to inch into me, I taste the copper tang of blood."
            "With every tiny degree that he creeps inside, I lose a little more ground."
            "Until I feel that he can't go any further."
            "And in that moment I see no point in keeping up the charade any longer."
            bree.say "S...Scottie..."
            show scottie cowgirl normal
            bree.say "Fuck me..."
            bree.say "Please?!?"
            "Scottie stares up at me for a moment, as if he suspects a trick."
            "But then he seems to realise that I'm being totally sincere."
            show scottie cowgirl up
            pause 0.45
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.45
            show scottie cowgirl up
            pause 0.45
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.45
            show scottie cowgirl up
            pause 0.45
            show scottie cowgirl down at startle(0.05,-10)
            "And this makes him leap into action a few seconds later."
            "Before I know what's happening, all of that pent up energy is released."
            show scottie cowgirl up
            pause 0.45
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.45
            show scottie cowgirl up
            pause 0.45
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.45
            show scottie cowgirl up
            pause 0.45
            show scottie cowgirl down at startle(0.05,-10)
            "All of the frustration that was building up in Scotties body flows out."
            "And it's instantly turned into frantic energy that he uses to satisfy my desires."
            show scottie cowgirl up speed
            pause 0.35
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.35
            show scottie cowgirl up
            pause 0.35
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.35
            show scottie cowgirl up
            pause 0.35
            show scottie cowgirl down -speed at startle(0.05,-10)
            "The change in our positions is instant and dramatic."
            "Where before I was the one dominating him, now I'm being taken in hand."
            show scottie cowgirl up speed pleasure
            pause 0.35
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.35
            show scottie cowgirl up
            pause 0.35
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.35
            show scottie cowgirl up
            pause 0.35
            show scottie cowgirl down -speed at startle(0.05,-10)
            "And it feels incredible, beyond the ability of words to describe."
            "Scottie doesn't hold anything back, he gives me everything all at once."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down -speed at startle(0.05,-10)
            "My head falls back and I moan for mercy."
            "But the only way this can end is when one of finally succumbs."
            "I want that to be me, as much as I'm enjoying what's being done to me."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down -speed at startle(0.05,-10)
            "Yet for some reason, I cling stubbornly on as Scottie pounds away."
            "Only when he kicks it up another gear do I feel myself beginning to give in."
            "It's like the long, slow climb to the top of a roller-coaster."
            show scottie cowgirl up speed
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down -speed at startle(0.05,-10)
            "And when I get there, I teeter on the brink for a moment."
            "Then I tumble over the edge!"
            call cum_reaction (scottie, 'vaginal', 5) from _call_cum_reaction_221
            if _return == "vaginal_outside":
                "I pull myself off Scottie as it happens."
                show scottie cowgirl up speed
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down -speed at startle(0.05,-10)
                pause 0.5
                show scottie cowgirl up -vaginal
                "And the sensation takes him with it too."
                show scottie cowgirl cumshot with vpunch
                "I feel him shoot his load over me."
                show scottie cowgirl ahegao with vpunch
                "Then the whole thing overwhelms my senses."
                with vpunch
                $ scottie.love += 2
                "And I fall insensible into the sand."
            else:
                "Scottie's deep inside me when it happens."
                show scottie cowgirl up speed
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down -speed at startle(0.05,-10)
                "And the sensation takes him with it too."
                show scottie cowgirl up speed
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down -speed at startle(0.05,-10)
                "I feel him shoot his load into me."
                show scottie cowgirl up ahegao
                pause 0.35
                show scottie cowgirl down creampie with vpunch
                pause 0.35
                show scottie cowgirl up
                pause 0.5
                show scottie cowgirl down with vpunch
                pause 0.5
                show scottie cowgirl up
                pause 0.75
                show scottie cowgirl down -speed with vpunch
                "Then the whole thing overwhelms my senses."
                $ scottie.love += 3
                "And I fall insensible into the sand."
        "Guide him to my ass" if hero.sexperience >= 10:
            "It doesn't take long for me to get Scottie good and hard."
            "I might not know if it's more from arousal or fear."
            "But that's not something I choose to dwell upon for too long."
            "Instead I push the head of his cock hard between the cheeks of my ass."
            bree.say "How's that feel, Scottie?"
            show scottie cowgirl anal
            bree.say "Is that what you want, huh?"
            "Scottie's nodding his head as I say all of this."
            "His eyes as wide as saucers the whole time."
            scottie.say "Y...yeah, [hero.name]..."
            scottie.say "That's it!"
            scottie.say "Can...can I have some more?"
            "I feel a wicked smile creeping onto my face as he says this."
            "Like he's in my power and can't escape."
            "So I do as he asks, rubbing the head of his cock around my hole."
            "Scottie's already panting and gasping from the pleasure he's feeling."
            "But the truth is that I'm fighting from one second to the next."
            "Fighting not to let on that I'm feeling the same way too."
            "Sure, I'm enjoying the feeling of holding power over him."
            "But the sensation of his cock, warm and hard in the palm of my hand..."
            "It's filling me with desire at the same time."
            "The effort only becomes that much harder when the inevitable happens too."
            "As I feel my own body surrender to desire, I have to bite my lip."
            show scottie cowgirl down pain
            "And as Scottie's cock begins to inch into me, I taste the copper tang of blood."
            "With every tiny degree that he creeps inside, I lose a little more ground."
            "Until I feel that he can't go any further."
            "And in that moment I see no point in keeping up the charade any longer."
            bree.say "S...Scottie..."
            show scottie cowgirl normal
            bree.say "Fuck me..."
            bree.say "Please?!?"
            "Scottie stares up at me for a moment, as if he suspects a trick."
            "But then he seems to realise that I'm being totally sincere."
            show scottie cowgirl up
            pause 0.45
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.45
            show scottie cowgirl up
            pause 0.45
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.45
            show scottie cowgirl up
            pause 0.45
            show scottie cowgirl down at startle(0.05,-10)
            "And this makes him leap into action a few seconds later."
            "Before I know what's happening, all of that pent up energy is released."
            show scottie cowgirl up
            pause 0.45
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.45
            show scottie cowgirl up
            pause 0.45
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.45
            show scottie cowgirl up
            pause 0.45
            show scottie cowgirl down at startle(0.05,-10)
            "All of the frustration that was building up in Scotties body flows out."
            "And it's instantly turned into frantic energy that he uses to satisfy my desires."
            show scottie cowgirl up speed
            pause 0.35
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.35
            show scottie cowgirl up
            pause 0.35
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.35
            show scottie cowgirl up
            pause 0.35
            show scottie cowgirl down -speed at startle(0.05,-10)
            "The change in our positions is instant and dramatic."
            "Where before I was the one dominating him, now I'm being taken in hand."
            show scottie cowgirl up speed pleasure
            pause 0.35
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.35
            show scottie cowgirl up
            pause 0.35
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.35
            show scottie cowgirl up
            pause 0.35
            show scottie cowgirl down -speed at startle(0.05,-10)
            "And it feels incredible, beyond the ability of words to describe."
            "Scottie doesn't hold anything back, he gives me everything all at once."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down -speed at startle(0.05,-10)
            "My head falls back and I moan for mercy."
            "But the only way this can end is when one of finally succumbs."
            "I want that to be me, as much as I'm enjoying what's being done to me."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down -speed at startle(0.05,-10)
            "Yet for some reason, I cling stubbornly on as Scottie pounds away."
            "Only when he kicks it up another gear do I feel myself beginning to give in."
            "It's like the long, slow climb to the top of a roller-coaster."
            show scottie cowgirl up speed
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down -speed at startle(0.05,-10)
            "And when I get there, I teeter on the brink for a moment."
            "Then I tumble over the edge!"
            call cum_reaction (scottie, 'anal', 5) from _call_cum_reaction_222
            if _return == 'anal_outside':
                "I pull myself off Scottie as it happens."
                show scottie cowgirl up speed
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down -speed at startle(0.05,-10)
                pause 0.5
                show scottie cowgirl up -anal
                "And the sensation takes him with it too."
                show scottie cowgirl cumshot with vpunch
                "I feel him shoot his load over me."
                show scottie cowgirl ahegao with vpunch
                "Then the whole thing overwhelms my senses."
                $ scottie.sub += 1
                "And I fall insensible into the sand."
            else:
                "Scottie's deep inside me when it happens."
                show scottie cowgirl up speed
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down -speed at startle(0.05,-10)
                "And the sensation takes him with it too."
                "I feel him shoot his load into me."
                show scottie cowgirl up ahegao
                pause 0.35
                show scottie cowgirl down creampie with vpunch
                pause 0.35
                show scottie cowgirl up
                pause 0.5
                show scottie cowgirl down with vpunch
                pause 0.5
                show scottie cowgirl up
                pause 0.75
                show scottie cowgirl down -speed with vpunch
                "Then the whole thing overwhelms my senses."
                $ scottie.love += 2
                "And I fall insensible into the sand."
    $ game.active_date.score += 20
    $ scottie.sexperience += 1
    return

label scottie_fuck_park_female:
label scottie_fuck_date_park_female:
    scene bg park
    "It's turned out to be a pretty nice day, the sun shining in a clear blue sky."
    "And it's warm too, enough to be out and about in summer clothes."
    "But still with a cooling breeze blowing on occasion to keep it from being too much."
    "So it seemed like the perfect day to visit the park in the company of a charming date."
    "But I don't have one of those."
    show scottie casual happy with dissolve
    "So I'll just have to make do with Scottie instead."
    scottie.say "Look, [hero.name]!"
    scottie.say "Over there!"
    "I turn to glance in the direction Scottie's head is bobbing in."
    "And I squint my eyes, trying to make out what he's seen this time."
    bree.say "Wild guess, Scottie..."
    bree.say "Is it another squirrel?"
    "Scottie shakes his head, but doesn't look away from the object of his interest."
    scottie.say "No, [hero.name]..."
    show scottie normal
    scottie.say "It's those guys over there."
    scottie.say "The one's playing catch with a ball!"
    "I can just make out the people that Scottie must be talking about."
    "And he must have pretty good eyesight, as they're a long way off."
    bree.say "Yeah, I see them."
    bree.say "But what am I looking at exactly?"
    "Scottie doesn't seem to hear my question."
    "Or if he does, the answer he gives me misses the point."
    scottie.say "Oh boy..."
    show scottie happy
    scottie.say "That looks like do much fun!"
    show scottie normal
    scottie.say "I wonder if they'd let me join in too?"
    bree.say "Erm..."
    bree.say "We're kind of on a date right now, Scottie."
    bree.say "You remember that, yeah?"
    "Scottie looks disappointed as I remind him of that fact."
    show scottie annoyed
    "He tears his eyes away from the people playing with a ball."
    "And then we get back to walking together along the path."
    scottie.say "Harumph..."
    show scottie normal
    scottie.say "I wish we had a ball, [hero.name]."
    scottie.say "Then you could throw it for me and I could bring it back to you."
    scottie.say "Doesn't that sound like a good time?"
    "I try to ignore the feeling that Scottie gives me at times like this."
    "Namely that I should be walking with him on the other end of a collar and lead."
    "Maybe if I change the subject he'll remember he's supposed to walk on two legs, not four."
    bree.say "I've wanted to show you the paths in the woods for ages, Scottie."
    bree.say "They're really peaceful and very beautiful too."
    bree.say "In fact, they're my favourite part of the park."
    scottie.say "I guess so, [hero.name]."
    scottie.say "If you like them, then that's fine by me!"
    show scottie at center, zoomAt(1.5, (640, 1040))
    "I smile and wrap myself around Scottie's arm."
    "It's at times like this that I remember he might be as dumb as a box of rocks."
    "But he's also capable of being seriously sweet too."
    bree.say "It's usually pretty quiet and deserted too."
    bree.say "So we can have a nice walk together, just you and me."
    "Even as I'm saying this, I can't help looking this way and that."
    "Because there's something unusual about the path we're walking down."
    "Something that makes it seem different to the way I remember it."
    "I'm trying to figure out just what it could be."
    "But it's hard to think with all these people passing us."
    "And what's odd is that they're all wearing raincoats."
    "Even though the weather is fine today."
    scottie.say "Uh, [hero.name]..."
    show scottie annoyed
    scottie.say "What are all these guys doing around here?"
    scottie.say "Don't those types usually hang around the porno theatre in the seedy part of town?"
    "Suddenly I look around and it's like seeing them for the first time."
    "Scottie's right, there are a whole bunch of creepy-looking guys in the woods!"
    show scottie surprised with hpunch
    "I take hold of Scottie's hand and hurry on down the path."
    "Maybe if we got deeper into the woods we can lose them."
    "That way we can enjoy some private time together."
    scene bg forest at center, zoomAt(1.5, (640, 1040))
    show scottie normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "Pretty soon I'm satisfied that we're away from the strange guys."
    "And we're walking off the path into one of the really nice clearings."
    show scottie surprised
    scottie.say "Whoa!"
    show scottie surprised
    scottie.say "This place sure is green!"
    scottie.say "You ever wonder how many shades of green there are?"
    show scottie normal
    scottie.say "I mean like, there's grass green, leaf green and..."
    bree.say "Scottie..."
    bree.say "Shut the fuck up and kiss me, okay?"
    show scottie surprised
    "Scottie's eyes go wide as I drape my arms around his neck."
    hide scottie
    show scottie kiss mc_sport
    with fade
    $ scottie.flags.kiss += 1
    "But then his reliable animal instinct seems to kick in."
    "And he pulls me close, kissing me with a sudden passion."
    "Thank fuck that he does too!"
    "I can feel every muscle in my body relax at the sensation."
    "There must be all kinds of endorphins and stuff flooding my body too."
    "That's one of the best things about Scottie."
    "He's so refreshingly simplistic that he kind of takes you back to nature."
    "In a matter of mere seconds we're tearing off each other's clothes."
    hide scottie kiss
    scene scottie doggy
    show scottie doggy park down mc_sport
    with fade
    "And then we're tumbling down onto the ground together."
    "I end up on all fours in front of Scottie."
    "He's behind me, already making a grab for my ass."
    bree.say "That's it, Scottie..."
    bree.say "Give me what I really need!"
    "Scottie shows no sign of having heard me."
    "But I can see that his cock is getting harder by the second."
    "And I can already feel my pussy twitching at the sight!"
    "I feel Scottie take a firm hold of me."
    "Then he pulls back, getting ready to do it."
    "It's at that very moment I hear a rustling in the bushes."
    "And I catch a glimpse of someone hiding in there."
    "No, scratch that - multiple someone's in there!"
    bree.say "Scottie..."
    bree.say "There..."
    bree.say "In the..."
    bree.say "Mmm...oh god!"
    menu:
        "Guide him to my pussy":
            "I don't have time to say anything more, as Scottie gets straight to work."
            "At once I feel both the head of his cock and the tips of his fingers down there."
            "He's using them all to stroke the lips of my pussy without pause or mercy."
            "And he seems to have the magic touch too."
            "Because I can already feel myself beginning to surrender!"
            "All the time I'm still looking straight ahead."
            "And I can see the exact same things that I could before he started to work on me."
            "But now it's clearer than ever that there's more than one person out there."
            "I can see and hear multiple shapes moving closer through the bushes."
            "And pretty soon I can see them for certain, squatting there as they watch us."
            "It has to be the same bunch of weirdos we saw back on the path."
            "They must have followed use here, guessing what we were going to do."
            "And now they've got an unhindered view of the whole proceedings!"
            "I open my mouth for a second time, trying to warn Scottie."
            "But that's the very moment that my pussy chooses to give up the fight."
            scottie.say "Oh man..."
            scottie.say "Oh yeah..."
            scottie.say "Here I come!"
            show scottie doggy vaginal pleasure
            "I can only gasp at the sensation as Scottie's cock slides into me."
            "It's as long and large as I remember, and it fills me completely."
            "My mouth hangs open as I begin to pant and gasp."
            "Believe me, there's nothing else that I can hope to do right now."
            "Scottie's already getting up to speed as he thrusts in and out of me."
            "And I don't know what's causing the flush I can feel on my cheeks."
            "Whether it's the way that he's making me pant and sweat."
            "Or the knowledge that I'm probably being watched by perverts!"
            play sound spank
            with hpunch
            "Suddenly there's the sound of skin against skin."
            "But way too loud to be his thighs slapping into my butt."
            show scottie doggy park pain mark1
            "And I can't help yelping in surprise."
            "Scottie's slapping my ass!"
            bree.say "Ow!"
            show scottie doggy pleasure
            scottie.say "Oh yeah!"
            scottie.say "You like that, huh?"
            show scottie doggy mark2 pain
            play sound spank
            with hpunch
            "Scottie slaps my ass again and again, not holding back for a second."
            "And soon enough I have two more red cheeks to contend with!"
            show scottie doggy pleasure
            "Now the humiliation is mounting by the second."
            "Not only am I naked on my hands and knees while being pounded."
            show scottie doggy mark3 pain
            play sound spank
            with hpunch
            "Scottie's also playing my buttocks like a pair of damn bongos!"
            "All while an audience is no doubt pleasuring themselves in the bushes."
            "The only space I have in my head as Scottie fucks me is totally occupied."
            "And it's full of thoughts around how I'm being watched this whole time."
            "I feel put on show, humiliated and robbed of my dignity."
            "But what puzzles me is the fact that I don't feel the urge to cry out."
            "Like, I could shout for Scottie to stop at any moment."
            "And I know that he'd do it too."
            "But I don't."
            show scottie doggy mark4 pain
            play sound spank
            with hpunch
            pause 0.35
            show scottie doggy mark5 pain
            play sound spank
            with hpunch
            "I just let him keep on going while the feeling of shame builds inside of me."
            show scottie doggy pleasure
            "Is it possible that...that I like it?"
            "The revelation feels like it's too much for me."
            "Like it pushes me over the edge."
            scottie.say "Ungh..."
            scottie.say "[hero.name]..."
            with hpunch
            scottie.say "You're cumming!"
            show scottie doggy ahegao with hpunch
            "I keep my eyes wide open and stare into the bushes the whole time."
            show scottie doggy creampie with hpunch
            "As my own orgasm takes hold and Scottie follows along afterwards, I look straight ahead."
            "Not once do I tear my eyes away from our silent, hidden watchers."
            $ scottie.love += 4
        "Guide him to my ass" if hero.sexperience >= 10:
            "I don't have time to say anything more, as Scottie gets straight to work."
            "At once I feel both the head of his cock and the tips of his fingers down there."
            "He's using them all to probe the hole in my ass without pause or mercy."
            "And he seems to have the magic touch too."
            "Because I can already feel myself beginning to surrender!"
            "All the time I'm still looking straight ahead."
            "And I can see the exact same things that I could before he started to work on me."
            "But now it's clearer than ever that there's more than one person out there."
            "I can see and hear multiple shapes moving closer through the bushes."
            "And pretty soon I can see them for certain, squatting there as they watch us."
            "It has to be the same bunch of weirdos we saw back on the path."
            "They must have followed use here, guessing what we were going to do."
            "And now they've got an unhindered view of the whole proceedings!"
            "I open my mouth for a second time, trying to warn Scottie."
            "But that's the very moment that my ass chooses to give up the fight."
            scottie.say "Oh man..."
            scottie.say "Oh yeah..."
            scottie.say "Here I come!"
            show scottie doggy anal pleasure
            "I can only gasp at the sensation as Scottie's cock slides into me."
            "It's as long and large as I remember, and it fills me completely."
            "My mouth hangs open as I begin to pant and gasp."
            "Believe me, there's nothing else that I can hope to do right now."
            "Scottie's already getting up to speed as he thrusts in and out of me."
            "And I don't know what's causing the flush I can feel on my cheeks."
            "Whether it's the way that he's making me pant and sweat."
            "Or the knowledge that I'm probably being watched by perverts!"
            play sound spank
            with hpunch
            "Suddenly there's the sound of skin against skin."
            "But way too loud to be his thighs slapping into my butt."
            show scottie doggy park pain mark1
            "And I can't help yelping in surprise."
            "Scottie's slapping my ass!"
            bree.say "Ow!"
            show scottie doggy pleasure
            scottie.say "Oh yeah!"
            scottie.say "You like that, huh?"
            show scottie doggy mark2 pain
            play sound spank
            with hpunch
            "Scottie slaps my ass again and again, not holding back for a second."
            "And soon enough I have two more red cheeks to contend with!"
            show scottie doggy pleasure
            "Now the humiliation is mounting by the second."
            "Not only am I naked on my hands and knees while being pounded."
            show scottie doggy mark3 pain
            play sound spank
            with hpunch
            "Scottie's also playing my buttocks like a pair of damn bongos!"
            show scottie doggy pleasure
            "All while an audience is no doubt pleasuring themselves in the bushes."
            "The only space I have in my head as Scottie fucks me is totally occupied."
            "And it's full of thoughts around how I'm being watched this whole time."
            "I feel put on show, humiliated and robbed of my dignity."
            "But what puzzles me is the fact that I don't feel the urge to cry out."
            "Like, I could shout for Scottie to stop at any moment."
            "And I know that he'd do it too."
            "But I don't."
            show scottie doggy mark4 pain
            play sound spank
            with hpunch
            pause 0.35
            show scottie doggy mark5 pain
            play sound spank
            with hpunch
            "I just let him keep on going while the feeling of shame builds inside of me."
            show scottie doggy pleasure
            "Is it possible that...that I like it?"
            "The revelation feels like it's too much for me."
            "Like it pushes me over the edge."
            scottie.say "Ungh..."
            scottie.say "[hero.name]..."
            with hpunch
            scottie.say "You're cumming!"
            show scottie doggy ahegao with hpunch
            "I keep my eyes wide open and stare into the bushes the whole time."
            show scottie doggy creampie with hpunch
            "As my own orgasm takes hold and Scottie follows along afterwards, I look straight ahead."
            "Not once do I tear my eyes away from our silent, hidden watchers."
            $ scottie.love += 2
            $ scottie.sub += 1
    scene bg forest at center, zoomAt(1.5, (640, 1040))
    show scottie casual embarrassed at center, zoomAt(1.5, (640, 1040))
    with fade
    "Afterwards I think about mentioning the fact we were watched to Scottie."
    "But as we get dressed, the urge to do so fades away more quickly than I can explain."
    "Somehow the thought of having that secret knowledge thrills me enough to make it happen."
    "And so I keep it to myself as he begins to prattle away again."
    "The watchers in the bushes has long since slunk away, leaving us alone."
    scene bg park
    show scottie casual happy at center, zoomAt(1.5, (640, 1040))
    with fade
    "So I guess I'll be keeping this as my own little secret."
    "Though I don't quite know what any of it says about me."
    "The feelings while I was being watched."
    "And the urge to keep it a secret alike."
    return

label scottie_fuck_pub_female:
    $ CONDOM = False
    "It's been one of those long shifts behind the bar at the Winchester."
    "And I couldn't be happier that I finally made it through to closing time."
    "All of the customers are filing out of the doors as I wait to lock them."
    show scottie at center, zoomAt(1.25, (340, 900)) with dissolve
    "And Scottie's amongst them too, though we agreed to meet up after I finished work."
    scottie.say "Uhm..."
    scottie.say "Are you gonna be long, [hero.name]?"
    scottie.say "Because I can wait for you out here, yeah?"
    "I smile and shake my head at this idea."
    "And instead I nod towards the bar."
    bree.say "There's no need for that, Scottie."
    bree.say "You can wait for me over by the bar if you like."
    show scottie surprised
    "Scottie seems surprised by the offer."
    show scottie happy
    "But he nods eagerly at it all the same."
    scottie.say "Are you sure?"
    show scottie normal
    scottie.say "Like, you won't get into trouble or anything?"
    bree.say "Of course not."
    bree.say "Just so long as you behave yourself!"
    hide scottie
    show scottie
    "Scottie nods and hurries over to the bar."
    "And I lock the doors, then get busy tidying the place up."
    "There's not all that much to do, just the usual cleaning and tidying."
    "Which means that I can easily chat to Scottie while I handle it."
    "For his part, Scottie seems to be finding it odd to be in the pub after closing."
    show scottie shy
    "He keeps glancing about the place like everything is strange and new."
    bree.say "You okay, Scottie?"
    bree.say "It's just...you look a little uneasy."
    scottie.say "Oh..."
    scottie.say "Well...yeah, [hero.name]."
    scottie.say "I've never been in here without there being people!"
    scottie.say "The place looks so different, you know?"
    bree.say "Ah, it's not so strange."
    bree.say "You get used to it pretty quickly."
    "Scottie nods at this."
    "But he's still looking around like he's not quite convinced."
    "I notice also that he's not moving from the spot he's standing on."
    bree.say "You really going to stand there like a statue?"
    bree.say "I have to go check the restrooms in a minute."
    bree.say "And you're welcome to come along."
    "Scottie takes a look around the pub and shakes his head."
    scottie.say "I dunno, [hero.name]..."
    show scottie normal
    scottie.say "What if someone sees me on the CCTV cameras or something?"
    scottie.say "They might think I'm a burglar!"
    "I chuckle and shake my head at Scottie."
    bree.say "No chance of that, Scottie."
    bree.say "This place is really old-school."
    bree.say "The only cameras in the building are the ones in our phones!"
    show scottie joke
    "At this I see a sudden change in Scottie's demeanour."
    show scottie at center, zoomAt(1.5, (640, 1040))
    "His face breaks into a smile and he hurries over to me."
    scottie.say "You're serious?"
    show scottie happy
    scottie.say "Then we can do whatever we like!"
    bree.say "Scottie..."
    bree.say "I'm not letting you behind the bar!"
    show scottie surprised
    scottie.say "No, [hero.name]..."
    show scottie normal
    scottie.say "That's not what I mean."
    show scottie shy
    scottie.say "I was thinking of more...you know, naughty stuff!"
    "Suddenly I catch on to what Scottie's trying to say."
    "And I'm surprised to find that I'm not in the least bit dismissive of it."
    "In fact, the idea of doing something rebellious right here sounds kind of good!"
    bree.say "Well..."
    bree.say "Now that you mention it..."
    bree.say "I had always wondered..."
    show scottie perv
    "Scottie's suddenly hanging on my every word."
    "He's nodding as he urges me on to say it."
    scottie.say "Yeah, [hero.name], yeah?"
    scottie.say "You always wondered what?!?"
    bree.say "Okay, Scottie..."
    bree.say "I always wondered what it'd be like to do it..."
    bree.say "On the pool table!"
    "Scottie's head is nodding even faster now."
    "And he's already walking over to the aforementioned pool table."
    scottie.say "Okay, [hero.name]..."
    show scottie happy
    scottie.say "Your wish is my command!"
    show scottie underwear with dissolve
    "I watch in stunned amazement as Scottie pulls off his shirt."
    "And as he starts to undo his pants, I find myself hurrying over."
    bree.say "Scottie!"
    bree.say "What are you doing?!?"
    show scottie surprised
    "Scottie looks at me with a puzzled expression on his face."
    scottie.say "What does it look like, [hero.name]?"
    show scottie happy
    scottie.say "I'm making your fantasy into a reality!"
    "I'm already fumbling with Scottie's clothes."
    "Trying to put them back on him even as he's taking them off."
    "But then he starts taking mine off at the same time too!"
    bree.say "You're crazy, Scottie!"
    bree.say "We can't do this."
    scottie.say "Why not, [hero.name]?"
    show scottie normal
    scottie.say "You locked the doors."
    scottie.say "There are no cameras."
    scottie.say "And we're the only ones in here."
    scottie.say "So who's gonna know?"
    "I stop trying to put Scotties clothes back on as his words sink in."
    "He's right - there really is no way anyone could ever find out."
    "So why am I being such a prude?"
    "In the time it's taken me to come to my senses, Scottie hasn't been idle."
    "And now I see that he's almost managed to strip me to the waist!"
    "There's a pause in his progress though, as he stops to stare at my chest."
    show scottie happy
    scottie.say "Whoa!"
    show scottie perv
    scottie.say "Boobies!"
    "I roll my eyes and start to climb backwards onto the pool table."
    bree.say "You have such a way with words, Scottie!"
    scene scottie missionary
    show scottie missionary pub nonpc down
    with fade
    bree.say "Now if we're going to do this, you'd better make it count."
    bree.say "And you'd better make it quick too!"
    "I watch as Scottie nods and pulls down his pants."
    "And I find myself hoping that I've made the right decision."
    "The first thing that Scottie does is grab hold of my thighs."
    "Then he pulls me towards him at the edge of the pool table."
    "I can't help yelping in surprise as the felt chafes my ass a little."
    show scottie missionary pain -nonpc
    bree.say "Ouch!"
    scottie.say "Huh?"
    scottie.say "Are you okay, [hero.name]?"
    show scottie missionary normal
    bree.say "Yeah, Scottie..."
    bree.say "I'll be fine."
    bree.say "Just don't stop!"
    show scottie missionary hold
    "Scottie nods, grabbing hold of my thighs again."
    "This time, when he pulls me close, it's only his thighs I can feel."
    "And the contact between skin and skin is a lot easier to handle."
    scottie.say "Okay, [hero.name]..."
    scottie.say "Where do you want it?"
    "For a moment I think about leaving the decision up to Scottie."
    "But then I remember who I'm dealing with."
    "And I decide to keep that little measure of power in my own hands."
    menu:
        "Guide him to my pussy":
            bree.say "Pussy, Scottie..."
            bree.say "Fuck my pussy, yeah?"
            bree.say "And don't beat around the bush..."
            bree.say "Or my bush...or whatever!"
            "Scottie almost gives me a salute as he leaps into action."
            show scottie missionary vaginal
            "I can already feel the head of his cock pressing against me."
            "And the thrill of doing it in a place like this..."
            "On the spur of the moment..."
            "Well, let's just say that I'm more than ready for it!"
            "Scottie doesn't have to work too hard to get things started."
            "He must stroke it along the lips of my pussy maybe half a dozen times."
            "And the very next moment, they start to part."
            show scottie missionary pose2 -hold
            "Slowly but surely I can feel him inching his way inside of me."
            "For a moment I'm sure that he's forgotten what I told him."
            "That he's forgotten we needed to make this fun but also fast."
            "And I'm about to open my mouth and urge him on."
            "But then Scottie seems to leap into action."
            show scottie missionary pose3
            "He pushes all the way into me."
            show scottie missionary pose2
            pause 0.35
            show scottie missionary pose1
            pause 0.35
            show scottie missionary pose2
            pause 0.35
            show scottie missionary pose3
            "And then he starts to thrust in and out in almost desperate earnest."
            "The words I was about to say die on my lips."
            show scottie missionary pose2
            pause 0.35
            show scottie missionary pose1
            pause 0.35
            show scottie missionary pose2
            pause 0.35
            show scottie missionary pose3
            "They're replaced with a gasp that soon becomes a deep moan."
            "And from that moment on, all I can do is hang on for dear life."
            show scottie missionary pose2
            pause 0.35
            show scottie missionary pose1
            pause 0.35
            show scottie missionary pose2
            pause 0.35
            show scottie missionary pose3
            "Scottie seems to be on autopilot, his brain focused on one thing alone."
            "Luckily for me, that happens to be just what I asked of him."
            show scottie missionary pose2 pleasure
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            "Scottie can keep on banging away at the same pace easily."
            "And that's because he has the edge of the pool table to stop him."
            show scottie missionary pose2
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            "But all I can do is spread out my arms and hope for the best."
            "There's no way my hands can get any purchase on the felt of the table."
            show scottie missionary pose2
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            "And I'm afraid of tearing it if I try to use my nails too."
            "This means that I'm rocking back and forth the whole time."
            show scottie missionary pose2
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            "My entire body moves in sympathy with Scottie's motions."
            "And all of it is translated into motion within me."
            show scottie missionary pose2
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            "Even if I could manage to speak, it'd do me no good."
            "Because all I'd be able to do would be to beg him for more!"
            show scottie missionary pose2
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            pause 0.25
            show scottie missionary pose2
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            "But as that thought passes through my mind, I feel a change in Scottie."
            "And it's not that he's slowing down either."
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            pause 0.15
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            "Almost like he's able to read my mind, I feel him begin to go faster still."
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            pause 0.15
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            "I didn't think it was possible, but he actually kicks it up a gear."
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            pause 0.15
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            "And once that happens, there's no way I can hope to hold on."
            bree.say "Oh..."
            show scottie missionary pose2 ahegao up
            bree.say "Scottie..."
            bree.say "I'm...gonna...cum!"
            "Scottie's head nods frantically as I say this."
            "Though I don't know if that means he's telling me he knows."
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            pause 0.15
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            "Or if he's trying to let me know that he's cumming too!"
            call cum_reaction (scottie, 'vaginal', 5) from _call_cum_reaction_223
            if _return == "vaginal_outside":
                "I get my answer a moment later as I feel Scottie pull out of me."
                show scottie missionary outside cumshot hold with hpunch
                "He shoots his load a second later, and it rains down on my belly."
                show scottie missionary onbody with hpunch
                "All I can do is lie there and stare up at the ceiling as my body shakes."
                show scottie missionary -cumshot down with hpunch
                "I seem to forget where I am, almost drifting away from myself."
                $ scottie.love += 2
                "And for a brief few seconds I enjoy not having a care in the world."
            else:
                "I get my answer a moment later as I feel Scottie let go."
                show scottie missionary pose3 creampie with hpunch
                "He shoots his load deep inside me, and I lose it the moment he does."
                with hpunch
                "All I can do is lie there and stare up at the ceiling as my body shakes."
                show scottie missionary down with hpunch
                $ scottie.love += 3
                "I seem to forget where I am, almost drifting away from myself."
                "And for a brief few seconds I enjoy not having a care in the world."

        "Guide him to my ass" if hero.sexperience >= 10:
            bree.say "Ass, Scottie..."
            bree.say "Fuck my ass, yeah?"
            bree.say "And don't beat around the bush..."
            bree.say "Or hole...or whatever!"
            "Scottie almost gives me a salute as he leaps into action."
            show scottie missionary anal
            "I can already feel the head of his cock pressing against me."
            "And the thrill of doing it in a place like this..."
            "On the spur of the moment..."
            "Well, let's just say that I'm more than ready for it!"
            "Scottie doesn't have to work too hard to get things started."
            "He must stroke it around my hole maybe half a dozen times."
            "And the very next moment, the muscles start to relax."
            show scottie missionary pose2 -hold
            "Slowly but surely I can feel him inching his way inside of me."
            "For a moment I'm sure that he's forgotten what I told him."
            "That he's forgotten we needed to make this fun but also fast."
            "And I'm about to open my mouth and urge him on."
            "But then Scottie seems to leap into action."
            show scottie missionary pose3
            "He pushes all the way into me."
            show scottie missionary pose2
            pause 0.35
            show scottie missionary pose1
            pause 0.35
            show scottie missionary pose2
            pause 0.35
            show scottie missionary pose3
            "And then he starts to thrust in and out in almost desperate earnest."
            "The words I was about to say die on my lips."
            show scottie missionary pose2
            pause 0.35
            show scottie missionary pose1
            pause 0.35
            show scottie missionary pose2
            pause 0.35
            show scottie missionary pose3
            "They're replaced with a gasp that soon becomes a deep moan."
            "And from that moment on, all I can do is hang on for dear life."
            show scottie missionary pose2
            pause 0.35
            show scottie missionary pose1
            pause 0.35
            show scottie missionary pose2
            pause 0.35
            show scottie missionary pose3
            "Scottie seems to be on autopilot, his brain focused on one thing alone."
            "Luckily for me, that happens to be just what I asked of him."
            show scottie missionary pose2 pleasure
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            "Scottie can keep on banging away at the same pace easily."
            "And that's because he has the edge of the pool table to stop him."
            show scottie missionary pose2
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            "But all I can do is spread out my arms and hope for the best."
            "There's no way my hands can get any purchase on the felt of the table."
            show scottie missionary pose2
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            "And I'm afraid of tearing it if I try to use my nails too."
            "This means that I'm rocking back and forth the whole time."
            show scottie missionary pose2
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            "My entire body moves in sympathy with Scottie's motions."
            "And all of it is translated into motion within me."
            show scottie missionary pose2
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            "Even if I could manage to speak, it'd do me no good."
            "Because all I'd be able to do would be to beg him for more!"
            show scottie missionary pose2
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            pause 0.25
            show scottie missionary pose2
            pause 0.25
            show scottie missionary pose3 speed with hpunch
            pause 0.25
            show scottie missionary pose3 -speed
            "But as that thought passes through my mind, I feel a change in Scottie."
            "And it's not that he's slowing down either."
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            pause 0.15
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            "Almost like he's able to read my mind, I feel him begin to go faster still."
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            pause 0.15
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            "I didn't think it was possible, but he actually kicks it up a gear."
            show scottie missionary pose1
            "And once that happens, there's no way I can hope to hold on."
            bree.say "Oh..."
            show scottie missionary pose2 ahegao up
            bree.say "Scottie..."
            bree.say "I'm...gonna...cum!"
            "Scottie's head nods frantically as I say this."
            "Though I don't know if that means he's telling me he knows."
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            pause 0.15
            show scottie missionary pose2
            pause 0.15
            show scottie missionary pose3 speed with hpunch
            pause 0.15
            show scottie missionary pose3 -speed
            "Or if he's trying to let me know that he's cumming too!"
            call cum_reaction (scottie, 'anal', 5) from _call_cum_reaction_224
            if _return == 'anal_outside':
                "I get my answer a moment later as I feel Scottie pull out of me."
                show scottie missionary outside cumshot hold with hpunch
                "He shoots his load a second later, and it rains down on my belly."
                show scottie missionary onbody with hpunch
                "All I can do is lie there and stare up at the ceiling as my body shakes."
                show scottie missionary -cumshot down with hpunch
                "I seem to forget where I am, almost drifting away from myself."
                $ scottie.love += 2
                "And for a brief few seconds I enjoy not having a care in the world."
            else:
                "I get my answer a moment later as I feel Scottie let go."
                show scottie missionary pose3 creampie with hpunch
                "He shoots his load deep inside me, and I lose it the moment he does."
                with hpunch
                "All I can do is lie there and stare up at the ceiling as my body shakes."
                show scottie missionary down with hpunch
                $ scottie.love += 3
                "I seem to forget where I am, almost drifting away from myself."
                "And for a brief few seconds I enjoy not having a care in the world."
    $ hero.replace_activity()
    $ game.pass_time(4)
    return

label scottie_fuck_date_cowgirl(sexperience_min):
    scottie.say "You want top or bottom, babe?"
    bree.say "Hmm..."
    bree.say "I think I want top."
    "Scottie nods as he rolls over and I come up on top."
    scene scottie cowgirl with fade
    "But something of his comes up with me."
    "Of course it's his cock, standing to attention in front of me."
    "And the sight of it makes me want to get things started all the more!"
    menu:
        "Guide him to my pussy":
            "I can't keep a smile off my face as I reach out for Scottie's cock."
            "And as soon as I take hold of it, I know exactly where it's going."
            "I start to rub my hand up and down the shaft as I get myself into position."
            call check_condom_usage (scottie) from _call_check_condom_usage_123
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show scottie cowgirl condom
            "As soon as I feel the head of Scottie's cock against my pussy, I kind of lose it."
            "I've been waiting for this moment, trying to be as patient as I can possibly be."
            "But now I'm on the verge of getting what I want, and it's becoming impossible to hold back."
            "That's why I don't waste any time in getting down to it, pushing it hard against my lips."
            show scottie cowgirl vaginal
            "I'm already beginning to pant as I try to push it between them."
            "And I feel like cursing the way that my own body tries to resist the effort."
            "Scottie's panting too, almost like he's doing it in sympathy with me."
            "But I know that the reality is he's anticipating what's going to come next."
            "I have no idea which one of use actually feels it happening first."
            "Even though it's a change that's coming over my body, rather than his."
            show scottie cowgirl pain
            "But little by little, I can sense that resistance drain away."
            "And just as slowly, Scottie starts to inch his way inside of me."
            "I lower myself down as it happens, always wanting to go faster than I'm able."
            "Scottie nods the whole time, encouraging me to go faster."
            "I find myself almost squatting over him like a giant frog!"
            show scottie cowgirl down normal
            "And once I know that he can't go any deeper, I take the impression a step further."
            show scottie cowgirl up
            pause 0.35
            show scottie cowgirl down
            "Because I start to raise and lower myself, going up and down atop him."
            "If Scottie even notices the froggy likeness, he keeps it to himself."
            "All of his attention instead seems to be focused on the upper half of my body."
            show scottie cowgirl up
            pause 0.35
            show scottie cowgirl down
            "Or to be more specific, he can't help staring at my breasts right now."
            "And for once, I can't honestly say that I blame him."
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down
            "The fact is that I'm moving faster with each second that passes."
            "Motion that's being translated into every part of my body moving in sympathy."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "And that means my breasts are swaying back and forth like crazy."
            "Hell, I can hardly see Scottie for them myself!"
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "But I certainly feel it when he reaches up and grabs hold of them."
            bree.say "Ooh..."
            show scottie cowgirl down pleasure
            bree.say "Ah..."
            bree.say "Oh yeah, Scottie..."
            bree.say "Squeeze me, good and hard!"
            "Scottie nods and seems to act on my demands almost as soon as I voice them."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "But the truth is that I have no way of knowing if he even heard me at all."
            "Luckily for me, he's totally focused on handling my breasts."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "Scottie doesn't just squeeze them, he actually manages to mix it up."
            "He presses them together and massages them against my chest."
            "And then he begins to pinch my nipples, rubbing them between his fingers."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "This is the thing that starts to send surges of pleasure running through me."
            "Every time Scottie presses my nipples between his fingers, I literally quiver."
            "Part of me feels that I'm being overwhelmed and wants to tell him to stop."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "But another, the part of me that wins out, wants him to do even more."
            "By now my body is practically on auto-pilot."
            "At the same time my mind is becoming totally fogged with pleasure."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "I feel like I could go on like this forever, my head reeling."
            "But then something changes, and at first I don't know what it is."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "Looking down I realise that Scottie's let go of my breasts."
            "Instead of playing with them, his hands are grasping me around the waist."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "And before I can figure out why, his next move gives me the answer."
            "Suddenly Scottie thrusts his groin upwards."
            "He puts all of his strength into it too."
            show scottie cowgirl up speed
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "Which means that I feel him surge upwards inside of me."
            "Before I was the one riding Scottie as he lay back and left me to it."
            show scottie cowgirl up speed
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "But now he's thrusting into me so hard and so fast..."
            "There's nothing I can do to resist as I'm swept along."
            show scottie cowgirl up speed
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "And a moment later he blurts out an explanation for what's happening."
            scottie.say "Hold on, [hero.name]..."
            scottie.say "Here I come!"
            call cum_reaction (scottie, 'vaginal', sexperience_min) from _call_cum_reaction_225
            if _return == "vaginal_outside":
                "I know that I don't want Scottie to cum inside of me."
                "So I take action before it's too late."
                show scottie cowgirl up speed
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down with vpunch
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down with vpunch
                pause 0.15
                show scottie cowgirl up -vaginal -speed
                "Lifting myself upwards, I don't stop until he slides out of me."
                "Scottie lets out a groan as he shoots his load a moment later."
                show scottie cowgirl cumshot with hpunch
                $ scottie.love += 2
                "But the motion of pulling him out of me is almost too much."
                show scottie cowgirl ahegao with vpunch
                "I can feel myself starting to cum too, even as Scottie covers my belly in cum."
                "Nothing I've felt this far even comes close, as it sweeps me away."
                "And even when it's all over, I can still feel the echoes of it all over my body."
            else:
                "I'm not worried for even a moment, because I remember that we used a condom."
                "Now all that I have to do is hold on for dear life and enjoy the experience."
                "And it's a pretty intense one, I have to say!"
                show scottie cowgirl up speed
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down with vpunch
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down with vpunch
                pause 0.1
                show scottie cowgirl down -speed
                if not CONDOM:
                    show scottie cowgirl creampie with vpunch
                    $ scottie.impregnate()
                $ scottie.love += 3
                "Scottie arches his body as he cums, burying himself deep inside of me."
                with vpunch
                "And the second that it hits me, I can feel myself starting to cum too."
                show scottie cowgirl ahegao with vpunch
                "Nothing I've felt this far even comes close, as it sweeps me away."
                "And even when it's all over, I can still feel the echoes of it all over my body."
        "Guide him to my ass" if hero.sexperience >= (sexperience_min + 5):
            "I can't keep a smile off my face as I reach out for Scottie's cock."
            "And as soon as I take hold of it, I know exactly where it's going."
            "I start to rub my hand up and down the shaft as I get myself into position."
            "As soon as I feel the head of Scottie's cock between my buttocks, I kind of lose it."
            "I've been waiting for this moment, trying to be as patient as I can possibly be."
            "But now I'm on the verge of getting what I want, and it's becoming impossible to hold back."
            "That's why I don't waste any time in getting down to it, pushing it hard against my ass."
            show scottie cowgirl anal
            "I'm already beginning to pant as I try to push it home."
            "And I feel like cursing the way that my own body tries to resist the effort."
            "Scottie's panting too, almost like he's doing it in sympathy with me."
            "But I know that the reality is he's anticipating what's going to come next."
            "I have no idea which one of use actually feels it happening first."
            "Even though it's a change that's coming over my body, rather than his."
            show scottie cowgirl pain
            "But little by little, I can sense that resistance drain away."
            "And just as slowly, Scottie starts to inch his way inside of me."
            "I lower myself down as it happens, always wanting to go faster than I'm able."
            "Scottie nods the whole time, encouraging me to go faster."
            "I find myself almost squatting over him like a giant frog!"
            show scottie cowgirl down normal
            "And once I know that he can't go any deeper, I take the impression a step further."
            show scottie cowgirl up
            pause 0.35
            show scottie cowgirl down
            "Because I start to raise and lower myself, going up and down atop him."
            "If Scottie even notices the froggy likeness, he keeps it to himself."
            "All of his attention instead seems to be focused on the upper half of my body."
            show scottie cowgirl up
            pause 0.35
            show scottie cowgirl down
            "Or to be more specific, he can't help staring at my breasts right now."
            "And for once, I can't honestly say that I blame him."
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down
            "The fact is that I'm moving faster with each second that passes."
            "Motion that's being translated into every part of my body moving in sympathy."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "And that means my breasts are swaying back and forth like crazy."
            "Hell, I can hardly see Scottie for them myself!"
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "But I certainly feel it when he reaches up and grabs hold of them."
            bree.say "Ooh..."
            show scottie cowgirl down pleasure
            bree.say "Ah..."
            bree.say "Oh yeah, Scottie..."
            bree.say "Squeeze me, good and hard!"
            "Scottie nods and seems to act on my demands almost as soon as I voice them."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "But the truth is that I have no way of knowing if he even heard me at all."
            "Luckily for me, he's totally focused on handling my breasts."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "Scottie doesn't just squeeze them, he actually manages to mix it up."
            "He presses them together and massages them against my chest."
            "And then he begins to pinch my nipples, rubbing them between his fingers."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "This is the thing that starts to send surges of pleasure running through me."
            "Every time Scottie presses my nipples between his fingers, I literally quiver."
            "Part of me feels that I'm being overwhelmed and wants to tell him to stop."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "But another, the part of me that wins out, wants him to do even more."
            "By now my body is practically on auto-pilot."
            "At the same time my mind is becoming totally fogged with pleasure."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "I feel like I could go on like this forever, my head reeling."
            "But then something changes, and at first I don't know what it is."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "Looking down I realise that Scottie's let go of my breasts."
            "Instead of playing with them, his hands are grasping me around the waist."
            show scottie cowgirl up speed
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.25
            show scottie cowgirl up
            pause 0.25
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "And before I can figure out why, his next move gives me the answer."
            "Suddenly Scottie thrusts his groin upwards."
            "He puts all of his strength into it too."
            show scottie cowgirl up speed
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "Which means that I feel him surge upwards inside of me."
            "Before I was the one riding Scottie as he lay back and left me to it."
            show scottie cowgirl up speed
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "But now he's thrusting into me so hard and so fast..."
            "There's nothing I can do to resist as I'm swept along."
            show scottie cowgirl up speed
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.15
            show scottie cowgirl up
            pause 0.15
            show scottie cowgirl down at startle(0.05,-10)
            pause 0.1
            show scottie cowgirl down -speed
            "And a moment later he blurts out an explanation for what's happening."
            scottie.say "Hold on, [hero.name]..."
            scottie.say "Here I come!"
            call cum_reaction (scottie, 'anal', sexperience_min) from _call_cum_reaction_226
            if _return == "anal_outside":
                "I know that I don't want Scottie to cum inside of me."
                "So I take action before it's too late."
                show scottie cowgirl up speed
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down with vpunch
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down with vpunch
                pause 0.15
                show scottie cowgirl up -anal -speed
                "Lifting myself upwards, I don't stop until he slides out of me."
                "Scottie lets out a groan as he shoots his load a moment later."
                show scottie cowgirl cumshot with hpunch
                $ scottie.sub += 1
                "But the motion of pulling him out of me is almost too much."
                show scottie cowgirl ahegao with vpunch
                "I can feel myself starting to cum too, even as Scottie covers my belly in cum."
                "Nothing I've felt this far even comes close, as it sweeps me away."
                "And even when it's all over, I can still feel the echoes of it all over my body."
            else:
                "I'm not worried for even a moment, because we're using the back door this time."
                "Now all that I have to do is hold on for dear life and enjoy the experience."
                "And it's a pretty intense one, I have to say!"
                show scottie cowgirl up speed
                pause 0.15
                show scottie cowgirl down at startle(0.05,-10)
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down with vpunch
                pause 0.15
                show scottie cowgirl up
                pause 0.15
                show scottie cowgirl down with vpunch
                pause 0.1
                show scottie cowgirl down creampie -speed with vpunch
                $ scottie.love += 2
                "Scottie arches his body as he cums, burying himself deep inside of me."
                with vpunch
                "And the second that it hits me, I can feel myself starting to cum too."
                show scottie cowgirl ahegao with vpunch
                "Nothing I've felt this far even comes close, as it sweeps me away."
                "And even when it's all over, I can still feel the echoes of it all over my body."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
