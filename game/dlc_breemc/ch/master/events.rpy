init python:
    
    Event(**{
        "name": "meet_the_master_female",
        "label": "meet_the_master_female",
        "duration": 1,
        "conditions": [
            IsDayOfWeek("246"),
            IsHour(10, 16),
            HeroTarget(
                IsGender("female"),
                IsRoom("beach"),
                ),
            ],
        "chances": 50,
        "do_once": True
        })
    
    Event(**{
        "name": "master_female_meet_event_01",
        "label": "master_female_meet_event_01",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("meet_the_master_female"),
            IsHour(10, 16),
            HeroTarget(
                IsGender("female"),
                IsRoom("beach"),
                MaxStat("morality", 0),
                ),
            PersonTarget("master",
                IsFlag("delay", 0),
                ),
            ],
        "do_once": True
        })
    
    Event(**{
        "name": "master_female_meet_event_02",
        "label": "master_female_meet_event_02",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("master_female_meet_event_01"),
            IsHour(10, 16),
            HeroTarget(
                IsGender("female"),
                IsRoom("beach"),
                MaxStat("morality", 0),
                ),
            PersonTarget("master",
                IsFlag("delay", 0),
                ),
            ],
        "do_once": True
        })
    
    Event(**{
        "name": "master_missed_training",
        "label": "master_missed_training",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsHour(10, 16),
            HeroTarget(
                IsGender("female"),
                IsRoom("beach"),
                MaxStat("morality", 0),
                IsFlag("master_training"),
                IsFlag("missed_training"),
                ),
            PersonTarget("master",
                IsFlag("delay", 0),
                ),
            ],
        "do_once": False,
        "once_hour": False,
        })
    
    Activity(**{
        "name": "master_female_money_favour",
        "label": "master_female_money_favour",
        "rooms": "beach",
        "conditions": [
            IsDone("meet_the_master_female"),
            IsHour(10, 16),
            HeroTarget(
                IsGender("female"),
                MinStat("energy", 3),
                MinStat("hunger", 3),
                MinStat("grooming", 3),
                MinStat("fun", 3),
                MaxStat("morality", -25),
                ),
            ],
        "display_name": "Help the old man",
        "icon": "master",
        })
    
    Event(**{
        "name": "master_preg_talk",
        "label": "master_preg_talk",
        "conditions": [
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                IsFlag("pregnancy_father", "master"),
                Or(
                    MinCounter("pregnant", 60),
                    IsFlag("foundpreg"),
                    ),
                ),
            PersonTarget(master,
                IsPresent(),
                Not(IsHidden()),
                IsFlag("toldpreg", False),
                MinStat("sexperience", 1),
                ),
            ],
        "do_once": False,
        })
    
    Event(**{
        "name": "master_find_out_pregnancy",
        "label": "master_find_out_pregnancy",
        "conditions": [
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                MinCounter("pregnant", 30),
                CounterChanceChecker("pregnant", 50)
                ),
            PersonTarget(master,
                IsPresent(),
                Not(IsHidden()),
                IsFlag("toldpreg", False),
                MinStat("sexperience", 1),
                ),
            ],

        "do_once": False,
        })
    
    Event(**{
        "name": "master_kiss_me_female",
        "label": "master_kiss_me_female",
        "max_girls": 1,
        "conditions": [
            HeroTarget(IsGender("female")),
            PersonTarget(master,
                Not(IsHidden()),
                IsPresent(),
                MinFlag("kiss", 1),
                MinStat("love", 150),
                ),
            ],
        "chances": 20,
        "once_day": True,
        "do_once": False,
        "quit": False,
        })
    
    Event(**{
        "name": "master_female_event_01",
        "label": "master_female_event_01",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("master_training_female_event_06"),
            IsHour(10, 16),
            ValidRooms("beach"),
            HeroTarget(
                IsGender("female"),
                Not(IsActivity()),
                ),
            PersonTarget("master",
                IsFlag("delay", 0),
                ),
            ],
        "do_once": True
        })
    
    Event(**{
        "name": "master_female_event_02",
        "label": "master_female_event_02",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("master_female_event_01"),
            IsHour(10, 16),
            ValidRooms("beach"),
            HeroTarget(
                IsGender("female"),
                Not(IsActivity()),
                ),
            PersonTarget("master",
                IsFlag("delay", 0),
                MinStat("love", 20)
                ),
            ],
        "do_once": True
        })
    
    Event(**{
        "name": "master_female_event_03",
        "label": "master_female_event_03",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("master_training_female_event_02"),
            IsHour(10, 16),
            ValidRooms("street"),
            HeroTarget(
                IsGender("female"),
                Not(IsActivity()),
                ),
            PersonTarget("master",
                IsFlag("delay", 0),
                MinStat("love", 40)
                ),
            ],
        "do_once": True
        })
    
    Event(**{
        "name": "master_female_event_04",
        "label": "master_female_event_04",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("master_female_event_03"),
            IsHour(10, 16),
            ValidRooms("beach"),
            HeroTarget(
                IsGender("female"),
                Not(IsActivity()),
                ),
            PersonTarget("master",
                IsFlag("delay", 0),
                MinStat("love", 60)
                ),
            ],
        "do_once": True
        })
    
    Event(**{
        "name": "master_female_event_05",
        "label": "master_female_event_05",
        "priority": 500,
        "duration": 1,
        "conditions": [
            IsDone("master_female_event_04"),
            IsHour(18, 23),
            ValidRooms("beach"),
            HeroTarget(
                IsGender("female"),
                Not(IsActivity()),
                ),
            PersonTarget("master",
                IsFlag("delay", 0),
                MinStat("love", 80)
                ),
            ],
        "do_once": True
        })
    
    
    InteractActivity(**{
        "name": "master_birthday_date_female",
        "label": "master_birthday_date_female",
        "duration": 2,
        "conditions": [
            HeroTarget(
                IsGender("female"),
                ),
            PersonTarget(master,
                IsActive(),
                Not(OnDate()),
                Not(IsHidden()),
                IsBirthday(),
                MinStat("love", 100),
                ),
            ],
        "display_name": "Date with Master",
        "icon": "date",
        "do_once": True,
        })

label master_female_money_favour:
    scene bg beach
    show master normal
    bree.say "Hey, old man!"
    master.say "Oh Hi!"
    bree.say "Want me to help you out?"
    menu:
        "Offer a handjob" if hero.morality <= -25:
            show master happy at startle
            "He nods eagerly and points to a secluded spot all the way behind the beach-huts, urging me to follow him."
            hide master with easeoutright
            "I tell myself that this isn't so bad - I only have to touch one part of him, and he doesn't get to touch me at all."
            scene bg beach at center, zoomAt(2.5, (0, 1440))
            show master at center, zoomAt(1.65, (640, 1140))
            with fade
            "Again, the old guy drops his shorts, which I understand the need for."
            "And then takes off his shirt, which I don't."
            "His muscular body once again surprise me on such an old man."
            scene master bj with fade
            show master bj far
            "I get down on my knees in front of him, my eyes on his cock and not his face."
            "Even just the promise of what I'm about to do and my kneeling in front of him is enough to set his cock to stirring."
            "I oblige by cupping his balls in one hand and taking his shaft in the other, rubbing it up and down roughly."
            show master bj close lick handjob
            "Normally I'd be careful to build up to being this forceful with a guy's cock."
            "But I figure that he doesn't really deserve to be pampered, based on what he's paying for and his unpleasant pass-time here at the beach."
            show master bj handjob up
            "All the same, my harsh treatment of his cock seems to be having the desired effect."
            "He's as big as he's going to get without surgery, and the head is already throbbing and red."
            "I try not to look up at his face, which is mostly obscured by his beard anyway, instead listening to him gasp for breath."
            show master bj handjob down closed
            "My hand starts to move up and down his shaft faster still now, and I begin to squeeze at his balls too."
            "I don't know if it's because I'm simply that good at this kind of thing or the fact that he's so old."
            "But he's already starting to twitch and twinge, gasping as I push him ever closer to cumming with each second that passes."
            show master bj handjob up with hpunch
            "I make the mistake of thinking that I still have enough time to get out of the way before I bring him off."
            show master bj far cumshot -up -lick -handjob -close with vpunch
            "And I'm proven spectacularly wrong a couple of seconds later when he shoots his load straight into my unsuspecting face."
            "I have to give it to him, it splatters all over my face like I'd have expected of a man half his age."
            show master bj cum onface -cumshot with vpunch
            "As I wipe the cum out of my eyes, squinting the whole time, he offers me a helpless grin and hands over a surprisingly pristine handkerchief to speed up the process."
            "He offers to let me keep the handkerchief, and I smile condescendingly, tossing it aside as soon as I'm all cleaned up and a safe distance away."
            "I'm much more satisfied with being able to keep the wad of money he hands over at the same time anyway."
            $ hero.money += 25
            if hero.morality > -50:
                $ hero.morality -= 1
            $ game.flags.master_handjob = True
        "Offer a blowjob" if hero.morality <= -50:
            $ game.flags.MasterStory = 1
            bree.say "Tell you what, I'm feeling particularly generous today."
            bree.say "I'll let you blow your load in my mouth."
            bree.say "How does that sound, hmm?"
            show master happy at startle
            "His eyes light up at this, or at least from what his bushy eyebrows are doing above his sunglasses, I assume they do."
            "Without as much as a single word, he shoves the entire wad of notes into my hand, nodding vigorously the entire time."
            "Don't judge me, okay?"
            "He might be an old perv, but he looks like he keeps himself clean and he's not even tried to put a hand on me before this."
            "And who knows - if he got more attention of this kind, then maybe he'd be less inclined to hang about the beach, letching on sunbathing girls?"
            hide master with easeoutright
            "He nods eagerly and points to a secluded spot all the way behind the beach-huts, urging me to follow him."
            scene bg beach at center, zoomAt(2.5, (0, 1440))
            show master at center, zoomAt(1.65, (640, 1140))
            with fade
            "Again the old guy drops his shorts, which I understand the need for."
            "And then takes off his shirt, which I don't."
            scene master bj with fade
            show master bj far
            "I kneel down in front of him and give his already twitching cock a few playful strokes."
            "I lick my lips at the same time, letting him get the impression that I'm looking forward to getting my lips around it."
            "Call it insincere if you like, but I just want him to feel like he's getting value for his money."
            show master bj close lick
            show mouth_insert bree zorder 1 at zoomAt(1, (840, 160))
            "I tickle his balls with one hand while guiding the tip of his cock into my mouth with the other."
            "Not taking it straight in, I kiss and lick at the head for a short while, building his anticipation for what's to come next."
            "And then, when he's already panting and biting his lip, I take him in further and begin to suck away with some gusto."
            "I don't intend to make this either particularly long or complicated, just give him a thrill and make him cum in short order."
            show master bj suck
            "After all, he's paying for a blowjob, not a six-year relationship."
            "And I don't know if his old man's body could take much more without him having a stroke or something similar."
            "I'm going at him pretty hard now, taking him almost as far in as I can manage and giving his balls a good, hard squeezing."
            "He's gasping with what I assume to be orgasmic pleasure, and not the first flushes of a heart attack, and so I redouble my efforts."
            with hpunch
            "Jerking and staying up only because he has the wall for support, he loses himself a couple of seconds later."
            show master bj suck cum inmouth
            show mouth_insert bree cum
            with hpunch
            "True to my word, I keep him in my mouth the whole time, not letting one drop of cum leak out of my mouth."
            with hpunch
            "I'm swallowing even as his cock slithers out of my mouth and he slowly slides down the wall to end up sitting in an exhausted heap before me."
            hide mouth_insert
            "As he looks to be in no condition to say a word, and as I already have his money, I get to my feet and give him a little wave goodbye."
            "Walking back to my towel and the bottle of water I brought with me, I really don't spare a thought for his fate should anyone discover him in such a state."
            "I took care of my part of the bargain, and now all I have to worry about is soaking up the sun for what's left of the day."
            $ hero.money += 50
            if hero.morality > -75:
                $ hero.morality -= 1
            $ game.flags.master_blowjob = True
    return
label meet_the_master_female:
    scene bg beach
    "It's not often that I get to spend any serious time down at the beach these days, what with work and my studies and everything else in a modern girl's life."
    "So when I do, I'm not one of those people who likes to spend all of their time messing around in the more crowded spots with the casual beach-goers."
    "I have a couple of more out-of-the-way spots that I always make a bee-line for, places where it's quiet and yet good for whatever particular pass-time I have in mind."
    "Today, that's sun-bathing, so I make my way straight to a familiar path that leads behind the sand-dunes for about a half-mile or so."
    "If I take the right turn off and onto the beach itself, I'll find myself on a pristine spot of sand that catches the rays for the best part of the day."
    "There's usually no one else back here at this time of day, save for the really rare dog-walker."
    show master normal at right with dissolve
    "And so when I see someone up ahead that's just standing sideways on to me and looking out over the beach beyond the dunes, it comes as somewhat of a surprise."
    "Maybe it's because I wasn't expecting to see anyone at all that I seem to find him instantly intriguing."
    "But then there's also the fact that he's a pretty memorable character to consider as well."
    "As I get closer, I can see that he's an older guy, his pate bare from baldness rather than being shaved."
    "In fact, apart from his bushy white eyebrows, the only other hair on his head is a long, bushy goatee beard and moustaches that almost completely cover his mouth."
    "He has on pretty typical beach clothes, a blue shirt and tan shorts, as well as sandals."
    "It's when I take a look at his sunglasses that I realise he's actually craning his neck to see something on the other side of the dunes."
    show master perv at center, zoomAt(1.25, (740, 900))
    "I can't make it out myself, but as I get closer, I see that his mouth is hanging open and his breathing is loud and heavy."
    "Shrugging it off, I guess that he must have been jogging, or at least walking at a pace and then stopped when something caught his eye."
    "By the time I get level with the old man, I glance over in the hope of seeing what's got him so entranced."
    "Over his shoulder, I see that there's a slight gap in the dunes."
    "Not enough to see the entirety of the beach - but more than enough to see the couple of dozen young girls sunbathing in their bikinis!"
    "That's when it dawns on me that the dirty old geezer is actually watching the rows of unsuspecting girls."
    "Which would account for both his intense interest and heavy breathing."
    menu:
        "Do nothing":
            "The last thing that I want to do today is surprise a geriatric pervert in the middle of indulging himself like that."
            hide master with fade
            "So I simply turn my attention back to the path in front of me and quicken my pace as much as I dare without it looking obvious."
            "Pretty soon I leave the old man behind, and once he's out of sight, I feel that I can slow down again."
            "I make it to the spot where I was hoping to sunbathe soon afterwards, and spread my towel out on the sand."
            "But almost the same moment that I'm finished rubbing the sunscreen into my body, a thought occurs to me."
            "If the old perv's in the habit of sneaking around behind the dunes at the beach, he might well know about this spot too!"
            "Suddenly I can't shake the feeling that he could be lurking somewhere right now, leering at my glistening limbs, flat belly and perky chest."
            "I glance around as my paranoia takes hold, but there's no sign of anyone, nor any sunlight glinting off of a bald head either."
            "Laying down on my towel, I still don't feel entirely happy with the situation."
            "I resolve to put up with the inconvenience of tan-lines for the sake of the knowledge that didn't give the creep a free eyeful too."
            "In the end I don't stay as long as I would otherwise have done, and instead scuttle off home via another route perhaps an hour later."
            $ hero.cancel_event()
        "Scold him" if hero.morality >= 25:
            $ hero.morality += 1
            "The fact that I could so easily have been one of those poor, unsuspecting girls on the beach right now makes my blood boil."
            "And a guy as old as that one should really know better - I mean, most of those girls are young enough to be his granddaughters."
            "Oh my god - what if one of them IS his granddaughter and he's perving over her without knowing it?!?"
            "I can't just walk on by, I have to do something about it!"
            bree.say "Hey, just what do you think you're doing, buddy?"
            show master surprised at center, zoomAt(1.0, (740, 900)), vshake
            "At the sound of my voice, the old man literally jumps a couple of feet in the air."
            "Which is quite an impressive feat for a man of his evidently advanced years."
            "His head shoots to the left and then the right as he searches for the source of the scolding."
            show master sad at center, zoomAt(1.25, (640, 900)) with ease
            "And then, painfully slowly, he turns around to regard me with the guilty expression of a man that's been well and truly caught in the act."
            show master normal
            "Old pervert" "Ah...erm...were you talking to me, young lady?"
            "At the audible attempt at charm in his tone, I instantly cross my arms over my chest and fix him with a stern, disapproving look."
            "The old man clocks this immediately, and looks suitably sheepish in response."
            bree.say "Don't you 'young lady' me, you filthy old goat!"
            bree.say "You know exactly what you were doing just now - and so do I!"
            show master at startle
            "He bobs up and down on the spot a little, and then casts a glance over his shoulder, as if seeing the view of the nubile young sunbather for the first time."
            "Old pervert" "Oh...oh...I see...I see what the source of your confusion is now!"
            show master happy at startle
            "He lets out a nervous laugh as he rubs the back of his head and gives me what he clearly thinks is an innocent smile."
            bree.say "The only person confused here is you, if you think I don't know you were perving on those poor, unsuspecting girls over there!"
            "At this, the old man waves both of his hands at me in a desperate attempt to dismiss my accusations."
            show master talkative at startle(0.1, 5)
            "Old pervert" "No, no, no - that's not it at all!"
            show master perv
            "Old pervert" "While it might look like I was staring at those young ladies in their skimpy little bikinis..."
            "At the mention of bikinis, he seems to lose track of what he was saying for a moment, and has to actually shake his head to get back on track again."
            show master talkative at startle(0.1, 5)
            "Old pervert" "As I was saying - while it might look like I was staring at those young ladies, I was really doing nothing of the sort."
            show master normal
            "All I can offer in way of an answer is a derisive snort."
            show master talkative at startle(0.1, 5)
            "Old pervert" "No, really - you see I am a martial artist of some considerable skill and notoriety."
            "Old pervert" "And it's become my habit to come to this deserted part of the beach and train the muscles of my eyes by staring out to sea for hours on end!"
            show master normal
            "I shake my head in disbelief, scarcely able to credit the bullshit story he's spinning for me."
            bree.say "Martial artist, I don't think so - piss artist, more like!"
            bree.say "I'll give you two choices, granddad - either bugger off now, or else I call the police and see what they have to say about your crazy excuses!"
            show master sad
            "For all his claims of being a martial artist, the old man gulps and begins to sweat pretty quickly at the mention of my calling the police."
            "He glances this way and that for a moment, as if not sure of what to do, and then darts into the deeper dunes at the back of the path and disappears."
            hide master with easeoutright
            "Left alone, I'm not sure that I want to go on to the spot I'd picked for sunbathing now after all."
            "The thought that he might still be hanging around somewhere is creeping me out, and so I decide to turn around and retrace my steps instead."
            $ hero.cancel_event()
        "Flirt with him" if hero.morality <= -25:
            $ hero.morality -= 1
            "While I'm contemplating whether to tear a strip off of the old pervert or else just walk on by, a strange notion suddenly occurs to me."
            "The old man seems pretty harmless, he's well-dressed and quite well-groomed too, and it's not like he's exposing himself or anything like that."
            "In fact, if I'd passed him in the street, I wouldn't have been freaked out by him in the slightest."
            "Maybe he just innocently stopped to look out over the sea and happened to be struck by how beautiful the sunbathers looked?"
            "I mean, it'd be patronising to think that such an old person shouldn't be turned on by the sight of young, hot flesh on show, wouldn't it?"
            "In fact, I can't help feeling a little jealous of those girls on the beach in an odd kind of way."
            "They could be responsible for stirring so many glorious memories in the bosom of this sweet, innocent old man, reminding him of his past glories."
            "When you look at it like that, it's almost poetic!"
            "And anyway, I'm willing to bet that I could stir more wonderful memories in the old coot than those air-headed little bimbos anyway!"
            bree.say "Well hello there!"
            show master surprised at center, zoomAt(1.0, (740, 900)), vshake
            "At the sound of my voice, the old man literally jumps a couple of feet in the air."
            "Which is quite an impressive feat for a man of his evidently advanced years."
            "His head shoots to the left and then the right as he searches for the source of the voice."
            show master sad at center, zoomAt(1.25, (640, 900)) with ease
            "And then, painfully slowly, he turns around to regard me with the guilty expression of a man that's been well and truly caught in the act."
            show master talkative at startle(0.1, 5)
            "Old pervert" "Ah...erm...were you talking to me, young lady?"
            show master normal
            "I smile broadly, trying to assure him that he's not being raked over the coals."
            bree.say "Well, I don't see anyone else around here - do you?"
            show master perv
            "The old man rubs the back of his head and licks his lips as he properly looks me over for the first time."
            "I can't honestly say that I blame him for the way that he swallows slowly."
            scene bg beach at center, zoomAt(2.0, (0, 1340)), dark
            show bree a sexyswimsuit at center, zoomAt(1.25, (640, 900))
            with fade
            "After all, I have got on my skimpiest white bikini, the one with the top that's mostly strap and the bottoms that's all but a thong."
            "Crossing my arms over my chest, I make sure to squeeze my breasts tightly as I do so, making them bulge visibly."
            scene bg beach
            show master perv at center, zoomAt(1.25, (640, 900))
            with fade
            "Though I can't see them, I'm sure the old man's eyes are doing the same thing behind his sunglasses too."
            "His adam's apple bobs up and down in silent appreciation of what he's seeing and the fact that it's up close."
            show master surprised blush at startle(0.1, 5)
            "Old pervert" "This...this isn't what it looks like!"
            "I raise a quizzical eyebrow at this, as if I'm not fully convinced."
            bree.say "Okay - what is it that this should look like?"
            show master sad
            "The old man gulps again, and glances around one last time before he tries to explain himself."
            "Old pervert" "Well...you see...I happen to be a martial artist, one of some considerable skill and notoriety."
            "This is sounding better by the moment!"
            show master talkative at startle(0.1, 5)
            "Old pervert" "And I need to train the muscles of my eyeballs like any others in my body."
            "Old pervert" "So I've taken to coming here and staring out to sea for that very purpose."
            show master normal
            "Aww, it's so cute that he thinks he needs to cook up such a crazy excuse for just looking at some young girls at the beach!"
            bree.say "But you need to train them to look at stuff close up too, don't you?"
            "The old man looks totally nonplussed by the question, until I squeeze my chest just a little tighter for his benefit."
            show master talkative at startle(0.1, 5)
            "Old pervert" "Oh...yes, yes - that's exactly so, and you're such a perceptive young lady to realise that fact too!"
            show master normal
            bree.say "And you'd need to see something pretty intricate to watch, yeah?"
            "At this, he nods eagerly."
            bree.say "Say, something like a girl putting on sunscreen, maybe?"
            "By now, his head is bobbing up and down like a jack-in-the-box."
            bree.say "So if I were to, say...put my own sunscreen on right here, rather than when I get to my favourite spot on the beach..."
            bree.say "I'd actually be doing you a favour, right?"
            show master happy at startle(0.1, 5)
            "Old pervert" "I..I'd be greatly obliged to you, young lady!"
            show master normal
            bree.say "Well, when you put it like that - do I really have a choice?"
            "Smiling to myself, I put down my bag and pull out the bottle of sunscreen inside."
            "I squeeze a generous amount into the palm of one hand, and then get to work."
            show master perv -blush
            "Starting from my feet, I smooth the white cream into each leg, drawing my hands upwards in long, smooth motions."
            "Upon reaching my backside, I make a point of kneading each buttock as I work the sunscreen in."
            "I do my belly next, and then stroke the sides of my body until I reach my breasts."
            "Here, I turn my back on the old man so that I can undo my bikini top."
            "I look back over my shoulder as I slide my hands under the top and work the cream into my breasts."
            "The sight of him almost turned to stone as he strains to see as much as possible makes me grin with genuine amusement."
            "I can also see a bulge in his shorts that seems to suggest he's in pretty good shape as far as that department's concerned."
            "There's only my arms and neck to take care of now, and I wrap these up nice and quick."
            "I think he's had all the little treats he deserves for now anyway."
            "Fastening the back of my bikini top, I offer the old man a little wave before I shoulder my bag and set off on my way."
            bree.say "Hope that helped?"
            "The old man nods with almost crazed enthusiasm as he watches me go."
            bree.say "Oh, I'm so glad to hear that - maybe I'll see you around here again some time?"
            hide master
            hide bree
            with fade
            "His nodding continues as I walk away down the path and he slowly disappears from sight."
    "Honestly, some of the people that you meet on an innocent trip to the beach!"
    "You really couldn't make this shit up."
    $ master.flags.delay = TemporaryFlag(True, 1)
    return

label master_female_meet_event_01:
    scene bg beach
    "From the weather being fine and there being just enough free time in my schedule for the day, everything fell into line to give me a golden opportunity to slip away to the beach for some much needed me time."
    "And never being the kind of girl to look a gift horse in the mouth, that meant I was feeling the warm sand under my feet as soon as I could make it out of the house and down to the dunes."
    "The fact that it's not the weekend means that the beach is far quieter than I'm used to seeing it, with only a small number of people soaking up the sun or taking a swim in the sea."
    "This means that I can take my pick when it comes to choosing the spot where I dump my stuff and prepare to lie down, taking time to truly appreciate the nicer specimens of the human anatomy on show as I do so."
    "I feel flattered to note that this admiration isn't just a one-sided thing, as several of those that I check out are quick to return the gesture, and with similar sentiments."
    "Though I'm only here to do some relaxing, I make a mental note that the bikini I chose to wear today is one that's worth keeping at the top of the list when I want to make an impression."
    "Pretty soon I'm laid on my towel, sunglasses protecting me against the glaze of the intense rays and allowing the sound of the lapping waves to lull me almost to sleep."
    "At first I try to ignore the funny feeling that keeps nagging at the back of my mind, the strange sensation of being watched."
    "The last thing that I want right now is to be distracted, and so I assume that it's just the admiring eyes that I attracted earlier, still lingering after seeing something they like."
    "But no matter how hard I try, thinking about other things and even trying some mediation exercises that I can remember learning, I can't seem to shake the feeling."
    "It's bugging me like hell, and there's just no way that I'm going to be able to relax properly until I do something about it."
    "Sitting up, I take in all of the beach that I can see from where I'm lying, at first not seeing a single thing that could explain the weird sensation."
    "Turning my head through three hundred and sixty degrees, all I find are perfectly innocent people doing perfectly inoffensive stuff."
    "But then, as I take a second look at the row of beach-huts that back onto the dunes, something moves enough to catch my eye."
    "Lifting my sunglasses and putting them on top of my head, I scrutinise the spot closely for almost a minute before I see anything at all."
    "What I do see is the sun glinting off of something smooth and shiny, something that seems to be bobbing around behind the beach-huts."
    show master normal at right with dissolve
    "A moment later I catch a glimpse of a face below it as well, and I instantly know that I'm actually looking at a bald head."
    "And from where I'm seeing it in relation to the beach and my own recollection of the last time I was here, I think that I can guess exactly who it belongs to as well!"
    "I could just let it go and try to ignore the fact that I know there's a dirty old pervert lurking around back there."
    "But something inside of me seems to just snap, making me suddenly and majorly annoyed that he's ruining my much needed chill-out time with his lecherous antics."
    "Getting up from my towel, I march straight over to where the beach-huts stand and then around the back of them."
    show master perv at center, zoomAt(1.25, (740, 900)) with fade
    "There's no way he can't have seen me coming, and I see that he has on account of the fact that he's already managed to scuttle perhaps twenty feet into the tall grass when I get there."
    show master sad at center, zoomAt(1.25, (1040, 900)) with ease
    "He can't possibly think that he's fooling me, as it's plain to see the grass shaking and parting as he goes."
    "Planting my hands firmly on my hips, I decide to call the filthy old geezer's bluff."
    bree.say "Hey, you!"
    show master surprised at vshake
    "Almost immediately I see his progress through the grass come to an abrupt halt."
    bree.say "Yeah, I know it's you."
    bree.say "Get back here, right now - before I scream so loud they'll hear it in the next county!"
    "There's a momentary pause, probably as he mulls over his chances of escape and measures them against the sincerity he can hear in my voice."
    show master sad at center, zoomAt(1.25, (640, 900)) with ease
    "And then the rustling in the grass begins again, only coming towards me this time and noticeably slower than before."
    "Soon enough the grass at the start of the dunes parts, and the shameless old peeping-Tom emerges into the open."
    "For all of his boldness when actually snooping, he's now looking down at the ground, even kicking at the sand with his feet."
    "He looks like nothing more than a kid that's been caught in the act of misbehaving and how has to face the music."
    bree.say "Well - what have you got to say for yourself this time, hey?"
    "In way of response he mutters something in a tone that's almost too low for me to make out."
    bree.say "What was that - speak up!"
    show master talkative at startle(0.1, 5)
    master.say "I said I was only looking..."
    show master normal
    bree.say "Yeah, I bet you were."
    bree.say "It's a miracle that I didn't catch you with it out and in your goddamn hand!"
    "He keeps on shuffling his feet and avoiding my eye, and it occurs to me that now I've caught him bang to rights, I have no idea what to do next."
    "I cross my arms over my chest and shake my head as he finally musters up the courage to look me in the face for the first time."
    show master talkative at startle(0.1, 5)
    master.say "You know I only do this because I'm frustrated, full of pent up energy?"
    master.say "I'd pay you..."
    show master normal
    bree.say "You'd what?"
    show master talkative at startle(0.1, 5)
    master.say "Pay you...if you were to help me out..."
    show master normal
    "I raise an eyebrow and regard him with a knowing smirk."
    bree.say "And how would you want me to do that - let me guess!"
    bree.say "No, before you even think of asking - I'm not going to fuck you for money!"
    show master talkative at startle(0.1, 5)
    master.say "Well...maybe there's something else you could bring yourself to do...for money?"
    show master normal
    menu:
        "Get the fuck lost!" if hero.morality >= -75:
            bree.say "Eww, gross - get the hell away from me, you creepy old bastard!"
            bree.say "I don't want your filthy money - it makes my skin crawl just to look at you!"
            hide master
            show master sad
            "My reaction is so extreme and intense that the old geezer actually leaps away from me a good metre or so."
            bree.say "I thought I made it plain to you the last time I had to tell you off?"
            bree.say "Stop spying on girls around here, or I'll call the cops on you!"
            "He capers in a circle at this, waving his arms as if trying to either get me to calm down or else starting to have some kind of twitching fit."
            show master surprised at startle(0.1, 5)
            master.say "Okay, okay - I get it!"
            master.say "No cops, no cops...I'll stop watching you, I promise?!?"
            hide master with easeoutright
            "It's only when he's crawled off back into the long grass that I realise he only ever vowed to stop spying on me, rather than all of the other girls on the beach at any given time."
            "As I start to make my way back to where I left my blanket, I can't help shaking my head in grudging admiration of the old geezer's slyness."
            $ hero.cancel_event()
        "Offer a handjob" if hero.morality <= -25:
            bree.say "Well, I dunno - just how much are we talking about here?"
            "Sensing that I might not be opposed to what he's suggesting, the old codger suddenly perks up."
            "He reaches into the pocket of his shorts and pulls out a wad of notes, nodding and grinning as he does so."
            "I try to guess how much is wrapped up in there, thinking the whole time that I could really use the money."
            bree.say "That'll buy you a hand-job, old man - no mouth and no touching me, okay?"
            show master happy at startle
            "He nods eagerly and points to a secluded spot all the way behind the beach-huts, urging me to follow him."
            hide master with easeoutright
            "I tell myself that this isn't so bad - I only have to touch one part of him, and he doesn't get to touch me at all."
            scene bg beach at center, zoomAt(2.5, (0, 1440))
            show master at center, zoomAt(1.65, (640, 1140))
            with fade
            "The old guy drops his shorts, which I understand the need for."
            "And then takes off his shirt, which I don't."
            "But it does reveal that his body is in pretty good shape for an old-timer."
            "Maybe he wasn't so full of shit as I thought when he claimed he was some kind of martial artist?"
            "Plus, his cock is quite a relief when I finally see it - not a monster, but pretty decent for the junk of an old man."
            "Maybe if I can forget about the rest of him and just concentrate on that, this won't be that bad after all..."
            "I show willing by getting down on my knees in front of him, my eyes on his cock and not his face."
            "He's not getting the full treatment of flirting and teasing, no matter what he's prepared to pay me."
            "And anyway, I know that the old goat is getting a premium view of my cleavage from up there, so he can make do with that."
            "Even just the promise of what I'm about to do and my kneeling in front of him is enough to set his cock to stirring."
            hide master
            show master bj far mc_swimsuit
            with fade
            "I oblige by cupping his balls in one hand and taking his shaft in the other, rubbing it up and down roughly."
            show master bj close lick handjob
            "Normally I'd be careful to build up to being this forceful with a guy's cock."
            "But I figure that he doesn't really deserve to be pampered, based on what he's paying for and his unpleasant pass-time here at the beach."
            show master bj handjob up
            "All the same, my harsh treatment of his cock seems to be having the desired effect."
            "He's as big as he's going to get without surgery, and the head is already throbbing and red."
            "I try not to look up at his face, which is mostly obscured by his beard anyway, instead listening to him gasp for breath."
            show master bj handjob down closed
            "My hand starts to move up and down his shaft faster still now, and I begin to squeeze at his balls too."
            "I don't know if it's because I'm simply that good at this kind of thing or the fact that he's so old."
            "But he's already starting to twitch and twinge, gasping as I push him ever closer to cumming with each second that passes."
            show master bj handjob up with hpunch
            "I make the mistake of thinking that I still have enough time to get out of the way before I bring him off."
            show master bj far cumshot -up -lick -handjob -close with vpunch
            "And I'm proven spectacularly wrong a couple of seconds later when he shoots his load straight into my unsuspecting face."
            "I have to give it to him, it splatters all over my face like I'd have expected of a man half his age."
            show master bj cum onface -cumshot with vpunch
            "As I wipe the cum out of my eyes, squinting the whole time, he offers me a helpless grin and hands over a surprisingly pristine handkerchief to speed up the process."
            "He offers to let me keep the handkerchief, and I smile condescendingly, tossing it aside as soon as I'm all cleaned up and a safe distance away."
            "I'm much more satisfied with being able to keep the wad of money he hands over at the same time anyway."
            $ hero.money += 50
            if hero.morality > -50:
                $ hero.morality -= 1
        "Offer a blowjob" if hero.morality <= -50:
            bree.say "Well, I dunno - just how much are we talking about here?"
            "Sensing that I might not be opposed to what he's suggesting, the old codger suddenly perks up."
            "He reaches into the pocket of his shorts and pulls out a wad of notes, nodding and grinning as he does so."
            "I try to guess how much is wrapped up in there, thinking the whole time that I could really use the money."
            bree.say "Tell you what, I'm feeling particularly generous today."
            bree.say "Hand over the whole wad, and I'll let you blow yours in my mouth."
            bree.say "How does that sound, hmm?"
            show master happy at startle
            "His eyes light up at this, or at least from what his bushy eyebrows are doing above his sunglasses, I assume they do."
            "Without as much as a single word, he shoves the entire wad of notes into my hand, nodding vigorously the entire time."
            "Don't judge me, okay?"
            "He might be an old perv, but he looks like he keeps himself clean and he's not even tried to put a hand on me before this."
            "And who knows - if he got more attention of this kind, then maybe he'd be less inclined to hang about the beach, letching on sunbathing girls?"
            hide master with easeoutright
            "He nods eagerly and points to a secluded spot all the way behind the beach-huts, urging me to follow him."
            "I tell myself that this isn't so bad - I only have to touch one part of him, and he doesn't get to touch me at all."
            scene bg beach at center, zoomAt(2.5, (0, 1440))
            show master at center, zoomAt(1.65, (640, 1140))
            with fade
            "The old guy drops his shorts, which I understand the need for."
            "And then takes off his shirt, which I don't."
            "But it does reveal that his body is in pretty good shape for an old-timer."
            "Maybe he wasn't so full of shit as I thought when he claimed he was some kind of martial artist?"
            "Plus, his cock is quite a relief when I finally see it - not a monster, but pretty decent for the junk of an old man."
            "There's a story worth telling - the one about the time I blew a martial arts master off on the beach!"
            "Of course when I do tell it, he'll look more like Bruce Lee, and maybe the money will be his winnings from a lethal tournament of death..."
            scene master bj with fade
            show master bj far mc_swimsuit
            "Starting to feel more at ease with the whole idea, I kneel down in front of him and give his already twitching cock a few playful strokes."
            "I lick my lips at the same time, letting him get the impression that I'm looking forward to getting my lips around it."
            "Call it insincere if you like, but I just want him to feel like he's getting value for his money."
            show master bj close lick
            show mouth_insert bree zorder 1 at zoomAt(1, (840, 160))
            "I tickle his balls with one hand while guiding the tip of his cock into my mouth with the other."
            "Not taking it straight in, I kiss and lick at the head for a short while, building his anticipation for what's to come next."
            "And then, when he's already panting and biting his lip, I take him in further and begin to suck away with some gusto."
            "I don't intend to make this either particularly long or complicated, just give him a thrill and make him cum in short order."
            show master bj suck
            "After all, he's paying for a blowjob, not a six-year relationship."
            "And I don't know if his old man's body could take much more without him having a stroke or something similar."
            "I'm going at him pretty hard now, taking him almost as far in as I can manage and giving his balls a good, hard squeezing."
            "He's gasping with what I assume to be orgasmic pleasure, and not the first flushes of a heart attack, and so I redouble my efforts."
            with hpunch
            "Jerking and staying up only because he has the wall for support, he loses himself a couple of seconds later."
            show master bj suck cum inmouth
            show mouth_insert bree cum
            with hpunch
            "True to my word, I keep him in my mouth the whole time, not letting one drop of cum leak out of my mouth."
            with hpunch
            "I'm swallowing even as his cock slithers out of my mouth and he slowly slides down the wall to end up sitting in an exhausted heap before me."
            hide mouth_insert
            "As he looks to be in no condition to say a word, and as I already have his money, I get to my feet and give him a little wave goodbye."
            "Walking back to my towel and the bottle of water I brought with me, I really don't spare a thought for his fate should anyone discover him in such a state."
            "I took care of my part of the bargain, and now all I have to worry about is soaking up the sun for what's left of the day."
            $ hero.money += 100
            if hero.morality > -75:
                $ hero.morality -= 1
    $ master.flags.delay = TemporaryFlag(True, 1)
    return

label master_female_meet_event_02:
    scene bg beach
    "It's too nice of a day to spend it indoors, far better to be here at the beach."
    "I can stretch my legs, fill my lungs with the salty air and listen to the sound of heavy breathing."
    "Wait a minute...that doesn't sound right!"
    "I stop dead in my tracks, straining to hear where the sound is coming from."
    "And then I zero-in on it, coming from the middle of the dunes at the edge of the beach."
    "It's only now that I recognise the sound for what it really is, and who's making it."
    show master normal with dissolve
    "Sure enough, I find the creepy old man with the long beard squatting in the dunes."
    "He hasn't seen me yet, so I make a point of crossing my arms over my chest and clearing my throat loudly."
    bree.say "Ahem..."
    bree.say "And just what the hell do you think you're doing?!?"
    show master surprised at startle
    "Just like before, the filthy old goat leaps up into the air."
    "The feat shows off the fact that he's pretty spry for his advanced age."
    "But his hands fly away from the waist-band of his shorts at the same time."
    "Which leaves me trying to keep from wondering what they were doing just now!"
    master.say "Wha...wha..."
    master.say "What on earth do you mean?"
    master.say "I wasn't doing anything wrong, young lady!"
    "I raise an eyebrow at this, shaking my head."
    bree.say "So you're always squatting in the dunes, yeah?"
    bree.say "Where it just so happens you can see but not be seen?"
    show master angry
    master.say "How dare you slander me like that?!?"
    master.say "I was...I was just...exercising my knees!"
    master.say "That's it - I was exercising my knees!"
    show master upset
    "I roll my eyes and make to turn away."
    "But the creepy old man makes to follow me."
    show master normal
    master.say "I'm a martial artist!"
    master.say "Remember, I told you that already?"
    master.say "It's the truth - and I'll prove it to you!"
    "I'm more irritated by the fact he's following me than what he's actually saying."
    "So I round on the old creep and give him a piece of my mind."
    bree.say "Look, I don't care if you're a Jeudi Master!"
    bree.say "If I catch you doing this again, I'm calling the police."
    bree.say "Or even better, my Daddy - and he'll kick your ass!"
    master.say "Ah, but what if you let me train you in the martial arts?"
    master.say "Then you could kick my ass all on your own!"
    menu:
        "Accept" if hero.morality <= -25:
            "I'm about to say no on sheer instinct."
            "Hell, I'm even thinking about kicking him in the balls."
            "But then I actually think about it for a moment."
            "Why not call the old creep's bluff?"
            "If he's full of shit, then he'll show himself up."
            "And if he's not, I get to learn a cool martial art!"
            bree.say "Okay, you filthy old goat."
            bree.say "Let's see what you've got!"
            "For a moment it looks like the guy can't believe what he's hearing."
            "But then he shakes it off and begins to look more confident."
            show master happy
            master.say "Really?!?"
            show master normal
            master.say "I...I mean of course!"
            master.say "You won't regret this, I assure you!"
            bree.say "I'd better not."
            bree.say "Because if I do, then so will you!"
            show master happy
            show fx drop
            "The old man tries to brush off the threat with a wheezing laugh."
            "But I can see that he's actually sweating a little under my scrutiny."
            hide fx
            show master talkative at startle(0.1, 5)
            master.say "B...be back here tomorrow morning."
            master.say "We'll begin your training then."
            master.say "And you...you might want to wear something tight, yes?"
            master.say "Something you can move - and sweat in, easily!"
            show master normal
            "I can't help rolling my eyes at this rather blatant effort on his part."
            "And I sigh, wondering what I'm letting myself in for here."
            "But in the end I push aside all of my misgivings and nod."
            hide master with fade
            "Then I walk away, before I can change my mind."
            $ hero.flags.master_training = True
            $ hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for my first lesson", "master_training_female_event_01", "master_training_female_event_missed"))
            if hero.morality > -30:
                $ hero.morality -= 1
        "Refuse":
            bree.say "I don't need lessons to kick your scrawny old butt!"
            "Before I know what's happening, I've pulled back my leg."
            play sound punch_hard
            pause 0.2
            show master surprised at vshake
            "And then I plant a foot firmly in the old man's crotch."
            "So much for all his talk of being a martial arts master."
            "He wheezes and doubles over in pain as soon as the kick connects."
            show master upset at center, zoomAt (1.0, (640, 840)) with MoveTransition(0.1)
            show master at startle
            "I see his eyes water as he falls to his knees on the sand."
            hide master with moveoutbottom
            "And then he topples over onto his side, curled into a foetal position."
            "I look around, starting to feel more than a little guilty."
            "Sure, he's a disgusting old creep that probably deserved worse."
            "But on the other hand, he's old enough to be my grandfather."
            "And I just hoofed him in the balls!"
            "Not knowing what else to do, I hurry off down the beach."
            "Maybe I'll leave it a little while before I come back here again..."
            $ hero.flags.master_training = False
    return

label master_missed_training:
    scene bg beach
    bree.say "Ah..."
    bree.say "Master..."
    show master
    bree.say "I'm sorry, I wasn't able to make it the other day."
    show master angry
    master.say "I see you don't take our training seriously, my dear."
    master.say "Be back here tomorrow."
    $ hero.flags.missed_training = False
    if hero.flags.master_training and "master_training_female_event_01" not in DONE:
        $ hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for my first lesson", "master_training_female_event_01", "master_training_female_event_missed"))
    elif hero.flags.master_training and "master_training_female_event_01" in DONE and "master_training_female_event_02" not in DONE:
        $ hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the second lesson", "master_training_female_event_02", "master_training_female_event_missed"))
    elif hero.flags.master_training and "master_training_female_event_02" in DONE and "master_training_female_event_03" not in DONE:
        $ hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the third lesson", "master_training_female_event_03", "master_training_female_event_missed"))
    elif hero.flags.master_training and "master_training_female_event_03" in DONE and "master_training_female_event_04" not in DONE:
        $ hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the fourth lesson", "master_training_female_event_04", "master_training_female_event_missed"))
    elif hero.flags.master_training and "master_training_female_event_04" in DONE and "master_training_female_event_05" not in DONE:
        $ hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the fifth lesson", "master_training_female_event_05", "master_training_female_event_missed"))
    elif hero.flags.master_training and "master_training_female_event_05" in DONE and "master_training_female_event_06" not in DONE:
        $ hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the final lesson", "master_training_female_event_06", "master_training_female_event_missed"))
    return

label master_training_female_event_missed:
    "Shit, I missed my training with the master."
    "I have to go back to the beach tomorrow."
    $ hero.flags.missed_training = True
    $ master.flags.delay = TemporaryFlag(True, 1)
    return

label master_training_female_event_01(appointment=None):
    scene bg beach
    "Part of me still can't actually believe that I'm doing this, even as I walk down the beach."
    "Even after I caught that disgusting old pervert ogling girls from the safety of the dunes."
    "But it's not like I haven't seen movies and anime about martial arts, you know?"
    "I just keep telling myself that maybe he's one of those quirky old masters."
    "The kind that seem like they're senile or crazily perverted at first."
    "But then they turn out to have been using that to cover up how amazing their skills are."
    "Although that theory does seem less likely when I finally spot the guy on the beach ahead."
    "He's laid flat on his back, staring up at the sky."
    "And yeah, people lie around on the sand all the time."
    "It's kind of the thing you do at the beach, I get that."
    "But it's not like he's laid on a towel, looking like he's sunbathing."
    "In fact, he looks like he's acting out one of those scenes from old movies."
    "You know the kind - the one where someone drops a handful of change on the ground."
    "Then they pretend to pick it up while peeking up women's skirts."
    bree.say "Ah..."
    bree.say "Morning, Master..."
    "Eww...it feels so weird calling him that!"
    "But he seems to respond to the title all the same."
    scene bg beach at center, zoomAt(2.5, (240, 720))
    show master swimsuit normal at center, zoomAt(1.5, (440, 1250)), rotation (80)
    with fade
    "The old man looks me in the eye, though he doesn't get up."
    show master talkative at startle(0.1, 5)
    master.say "Good morning to my newest pupil!"
    master.say "I hope you're ready for your first lesson?"
    show master normal
    bree.say "Erm...I guess so."
    bree.say "Do I need to lie down there too?"
    show master happy at startle(0.1, 5)
    master.say "Oh no...no, no, no!"
    master.say "You're going to be standing up the whole time."
    show master normal
    "Okay...that doesn't sound too bad."
    "Maybe this is just him being eccentric?"
    show master perv at startle(0.1, 5)
    master.say "Specifically, you'll be standing over me."
    master.say "Standing over me while you're doing squats!"
    show master normal blush
    "Looks like I spoke too soon."
    "That sounds mega perverted to me!"
    bree.say "Couldn't you just stand up and watch me do that?"
    bree.say "Maybe even sit on the sand?"
    "Much to my dismay, the old man shakes his head."
    show master perv -blush at startle(0.1, 5)
    master.say "No, no, no!"
    master.say "That simply won't do, my girl."
    master.say "These exercises are intended to strengthen your body."
    master.say "Very specific parts of your body."
    master.say "And I need to be able to see that they're working too!"
    show master normal blush
    "I open my mouth to protest, but then I stop myself."
    "Sure, this all sounds crazily suspicious to me."
    "But so far he's not stepped over the line I have in my head."
    "So I shake it off and decide to give him a chance to prove himself."
    bree.say "Okay, okay..."
    bree.say "Just let me get myself into position..."
    "It's not like I need to be told how to actually do squats."
    scene bg beach
    show bree sport close d arms01 at top_to_bottom
    "So I can kind of tune the old guy out as I get started with the exercise."
    "Instead of listening to his gurgling and lewd comments, I look out to sea."
    "My hope is that I can use the natural beauty around me to distract my mind."
    master.say "Ooh..."
    master.say "Good...very good!"
    master.say "Work those thighs, my dear!"
    master.say "And the buttocks too - don't forget the lovely buttocks!"
    "I do the best I can to ignore the comments I'm hearing."
    "But it's a warm morning, and it doesn't take me long to start feeling it."
    show bree close d arms01 at bottom_to_top
    "My muscles begin ticking over nicely as I move up and down."
    "And before long I start to work up a sweat."
    "It's not like I'm soaked in perspiration."
    "But I can feel my crotch starting to get wet."
    "That and beads of sweat running between my breasts."
    show bree close d arms01 at top_to_bottom
    master.say "Oooh..."
    master.say "That's good, that's very good!"
    master.say "You're getting nice and moist."
    master.say "Moist in all the right places, my dear!"
    "How am I supposed to zone out when I can hear that?!?"
    "The creep's babbling on as he watches me squatting over him."
    "And it sounds like he's voicing all of his perverted thoughts too!"
    "But all I can do is shake my head and try to keep on going."
    "This has to come to an end sooner or later, right?"
    show bree close d arms01 at bottom_to_top
    "So I redouble my efforts, pushing my body as far as it'll go."
    "Before too long, I can feel the muscles in my legs staring to quiver."
    "The sun is beating down on me, which makes things that much worse."
    "My clothes and hair are soaked, plastered to my skin."
    "And my breath is coming in ragged gasps."
    scene bg beach
    show bree sport a annoyed blush
    bree.say "Urgh..."
    bree.say "Master...I..."
    bree.say "I have to...have to stop..."
    bree.say "Or else I'm gonna pass out!"
    scene bg beach at center, zoomAt(2.5, (240, 720))
    show master swimsuit happy at center, zoomAt(1.5, (440, 1250)), rotation (80)
    with fade
    master.say "Huh...wha..."
    master.say "What was that?!?"
    show master normal
    "I glance down to see what's the matter with the old man."
    "And even with my head spinning, I swear I see his hand down his shorts!"
    "He yanks it out as quick as a flash, grinning wickedly the whole time."
    show master talkative at startle(0.1, 5)
    master.say "Yes...yes..."
    master.say "You can stop now, my dear."
    master.say "And that's the end of today's lesson too!"
    show master normal
    "For a moment I think about challenging him on that."
    scene bg beach
    show bree sport a at left
    with fade
    "Because it doesn't seem like I learned much about martial arts."
    show master swimsuit at center with easeinbottom
    "But he starts talking again before I can catch my breath."
    show master talkative at startle(0.1, 5)
    master.say "Now, about the fee for today's lesson..."
    show master normal
    "Oh, here we go!"
    "Is this where he tries to scam me?"
    show master perv at startle(0.1, 5)
    master.say "All I require is the bra that you're wearing right now!"
    master.say "That simple, soiled undergarment is all I ask in return for my services."
    menu:
        "Accept" if hero.morality <= -30:
            "I honestly think about telling him where he can shove his services."
            "But if that's all it takes to bring the lesson to an end, so be it!"
            "I reach under my top and unhook my bra, then wriggle out of it."
            show bree b topless blush with dissolve
            "And as soon as I manage to pull it out, hand it to the dirty old man."
            "His eyes are as wide as saucers, and he clutches it to his chest."
            show master talkative at startle(0.1, 5)
            master.say "Thank you, my dear."
            master.say "Be back here tomorrow for your next lesson!"
            hide master with easeoutright
            "With that, he turns his back on me and scuttles off into the dunes."
            "Which is something I'm very thankful for."
            "I don't want to think about what he's going to do with that bra!"
            $ hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the second lesson", "master_training_female_event_02", "master_training_female_event_missed"))
            if hero.morality > -35:
                $ hero.morality -= 1
        "Refuse":
            show bree angry
            bree.say "You want my bra?!?"
            bree.say "Urgh...you're just a creepy old pervert!"
            "For all his supposed martial arts mastery, he doesn't see the kick coming."
            play sound punch_hard
            pause 0.2
            show master surprised at vshake
            "And when it connects with his groin a moment later, he goes straight down."
            show master upset at center, zoomAt (1.0, (640, 840)) with MoveTransition(0.1)
            show master at startle
            pause 0.5
            hide master with moveoutbottom
            "I don't even bother to look down at the old man as he rolls around on the sand."
            "Instead I just stride away down the beach, my head held high."
            "How in the hell did I ever let myself get suckered in by that guy?!?"
            $ hero.morality += 1
            $ hero.flags.master_training = False
    $ game.pass_time(2)
    return

label master_training_female_event_02(appointment=None):
    scene bg beach
    "Yesterday was a pretty humiliating experience all round, and it cost me a bra too!"
    "But I keep telling myself that maybe it was a one-off, and today will be different."
    "I mean, perhaps laying under me while I did squats was just some kind of weird test?"
    "Like something that the guy does to scare off students that aren't willing to commit."
    "Maybe once you're past the silly stuff, that means it's time for the real lessons."
    "And it certainly seems like he's got something more serious in mind when I spot him."
    "Because today the old man's not laid out on the sand staring up at the sky."
    show master swimsuit noglasses at right with dissolve
    "Instead he's standing on his own two feet, watching me as I walk to him over the sand."
    show master happy at center with ease
    "As I get closer, he hurries over with an eager smile on his wrinkled face."
    show master talkative at startle(0.1, 5)
    master.say "Good morning, my dear."
    master.say "Are you ready for your next lesson?"
    show master normal
    "I hope that the smile I force onto my face doesn't look too fake."
    "And that my voice doesn't sound too strained either."
    bree.say "Ah..."
    bree.say "Y...yes..."
    show master normal at center, zoomAt (1.25, (640, 840))
    "The old man raises an eyebrow and leans in a little closer."
    "Like he's prompting me to say something that's slipped my mind."
    show master talkative at startle(0.1, 5)
    master.say "Yes...what?"
    bree.say "Yes...Master?"
    show master happy
    master.say "That's better!"
    master.say "Now then, let's get down to business!"
    show master normal
    "I take a deep breath and nod, trying to show willing."
    "This has to be where the real martial arts training starts, right?"
    show master talkative at startle(0.1, 5)
    master.say "What I want you to do today, is hit me in the face!"
    master.say "No holding back, and as hard as you can!"
    show master normal
    "All I can do is blink at the old man in surprise."
    "I know that I wanted to get down to the actual martial arts."
    "But I had no idea it'd get so serious the moment that we did!"
    bree.say "You're serious?"
    bree.say "You really want me to hit you in the face?!?"
    show master happy
    "The old man smiles broadly, amused by my concern."
    "But he nods his head all the same."
    show master normal
    "I shake mine, but hold up my hands all the same."
    bree.say "Should I ball up my fist?"
    bree.say "Or hit you with an open palm?"
    show master happy at startle
    "The old man chuckles and shakes his head."
    master.say "My dear, my dear..."
    show master talkative
    master.say "You're going to have to open your mind if you want to succeed here."
    master.say "Put aside all of the assumptions filling your head and start anew."
    master.say "I never said hit me with your hands!"
    show master normal
    "I frown at this, shaking my head."
    bree.say "I don't understand, Master."
    bree.say "You don't want me to use my hands?"
    show master talkative at startle(0.1, 5)
    master.say "No, my dear, no."
    master.say "I want you to use your magnificent breasts!"
    show master normal
    bree.say "You want me to do WHAT?!?"
    show master talkative at startle(0.1, 5)
    master.say "A true martial artist can use any part of their body as a weapon!"
    master.say "And they're never thrown by being made to think outside of the box too!"
    show master normal
    "All I can do is roll my eyes and let out a frustrated groan."
    "But then I nod my head and thrust my chest forward."
    bree.say "Okay, Master, I'll do my best."
    "The old man nods, already thrusting out his chin."
    "In truth, he doesn't have to bend over much at all."
    "I might not be the tallest of girls, but he's pretty short."
    "Which means I can swing my chest and hit his face with ease."
    "And so the 'lesson' begins in earnest with the first swing."
    "Luckily for me, there aren't too many people about to see it."
    scene bg beach at center, zoomAt (1.75, (1040, 840))
    show master swimsuit normal noglasses zorder 2 at center, zoomAt (1.75, (940, 1140))
    show bree sport d arms01 zorder 1 at center, zoomAt (2.1, (340, 740))
    pause 0.5
    show bree sport d arms01 at center, zoomAt (2.1, (740, 740)) with MoveTransition(0.2)
    pause 0.5
    show bree sport d arms01 at center, zoomAt (2.1, (340, 740)) with ease
    "My breasts hit the old man on the side of his face."
    "I deliberately make the blow quite gentle, not wanting to hurt him."
    "But this doesn't seem to be what he was wanting."
    "As he instantly shakes his head at my efforts."
    master.say "Don't hold back, my dear."
    master.say "Commit yourself to the blows!"
    master.say "You need to make me feel your inner chi!"
    "Believe me, I've heard some memorable comments about my breasts in the past."
    "But nobody ever suggested that I needed to channel their inner chi!"
    "Nevertheless, my second attempt seems to meet with a better reception."
    play sound punch_hard
    show bree sport d arms01 at center, zoomAt (2.1, (740, 740)) with MoveTransition(0.1)
    pause 0.1
    with hpunch
    pause 0.4
    show bree sport d arms01 at center, zoomAt (2.1, (340, 740)) with ease
    "This time it feels more akin to a gentle slap across the cheeks."
    master.say "Good, my dear, very good!"
    master.say "Like that, but harder still!"
    "I shake my head at this."
    "But I try my best to do as he asks."
    play sound punch_hard
    show bree sport d arms01 at center, zoomAt (2.1, (740, 740)) with MoveTransition(0.1)
    pause 0.1
    show master wink with hpunch
    pause 0.4
    show bree sport d arms01 at center, zoomAt (2.1, (340, 740)) with ease
    "And the third blow actually move his head like a blow from a hand!"
    "For a moment I think the old man is going to cry out or tell me off."
    show master happy
    "But much to my surprise, he seems delighted."
    master.say "That's it, my dear!"
    master.say "Just like that!"
    show master normal
    master.say "Now do it both ways, left and right!"
    master.say "Tits on, tits off!"
    "I do as I'm told, ignoring my natural fear of hurting the guy."
    play sound punch_hard
    show bree sport d arms01 at center, zoomAt (2.1, (740, 740)) with MoveTransition(0.1)
    pause 0.1
    show master blush with hpunch
    pause 0.1
    show bree sport d arms01 at center, zoomAt (2.1, (540, 740)) with MoveTransition(0.1)
    pause 0.1
    play sound punch_hard
    show bree sport d arms01 at center, zoomAt (2.1, (740, 740)) with MoveTransition(0.1)
    pause 0.1
    show master blush with hpunch
    pause 0.4
    show bree sport d arms01 at center, zoomAt (2.1, (340, 740)) with ease
    "It hardly seems to do much to me, as he's pretty frail."
    "Yet the whole time I'm worried about him coming off worse in the exchange."
    "But the evidence seems to suggest the exact opposite."
    play sound punch_hard
    show bree sport d arms01 at center, zoomAt (2.1, (740, 740)) with MoveTransition(0.1)
    pause 0.1
    show master wink with hpunch
    pause 0.1
    show bree sport d arms01 at center, zoomAt (2.1, (540, 740)) with MoveTransition(0.1)
    pause 0.1
    play sound punch_hard
    show bree sport d arms01 at center, zoomAt (2.1, (740, 740)) with MoveTransition(0.1)
    pause 0.1
    show master with hpunch
    pause 0.4
    show bree sport d arms01 at center, zoomAt (2.1, (340, 740)) with ease
    "Every time my breasts hit his cheek, I hear a giggle of delight."
    "And his head spins around from the force of the blow."
    "I don't know if the noises he's making are from being turned-on."
    "Or else they're the beginning of him being knocked insensible."
    play sound punch_hard
    show bree sport d arms01 at center, zoomAt (2.1, (740, 740)) with MoveTransition(0.1)
    pause 0.1
    with screenshot
    show master perv blush with hpunch
    show bree sport d arms01 at center, zoomAt (2.1, (540, 740)) with MoveTransition(0.1)
    pause 0.1
    play sound punch_hard
    show bree sport d arms01 at center, zoomAt (2.1, (740, 740)) with MoveTransition(0.1)
    pause 0.1
    with screenshot
    with hpunch
    show bree sport d arms01 at center, zoomAt (2.1, (540, 740)) with MoveTransition(0.1)
    pause 0.1
    play sound punch_hard
    show bree sport d arms01 at center, zoomAt (2.1, (740, 740)) with MoveTransition(0.1)
    pause 0.1
    with screenshot
    with hpunch
    pause 0.4
    show bree sport d arms01 at center, zoomAt (2.1, (340, 740)) with ease
    "Either way his mouth is hanging open and his tongue lolling out too."
    "And I'm worried that he's actually going to pass out before I'm done."
    "When his eyes glaze over, I decide that it might be time to stop."
    bree.say "Ah, Master..."
    bree.say "I think we should stop now."
    bree.say "I'm actually losing feeling in my chest!"
    show master surprised at startle
    master.say "Huh...wha..."
    master.say "Oh...okay, my dear..."
    master.say "I think I was just about to reach nirvana there for a moment!"
    master.say "Coming back to earth is hard when you're in a mental state like that!"
    master.say "Anyway, that concludes today's lesson."
    master.say "And all that remains is the matter of payment..."
    scene bg beach
    show master swimsuit normal noglasses
    with fade
    "I feel my stomach churn at the mere mention of payment."
    "The creep wanted my bra yesterday - so what will it be today?"
    "I don't have to wait long for the answer."
    show master blush
    master.say "Today, I will need the panties that you have on!"
    menu:
        "Accept" if hero.morality <= -35:
            "Well, he already got me to give him my bra."
            "So I guess he's wanting the panties to go with them."
            "I force a smile onto my face and nod in agreement."
            master.say "Very good, my dear."
            master.say "Don't be afraid to take them off right here."
            show master perv
            master.say "I won't be embarrassed in the slightest."
            bree.say "Ah, no..."
            bree.say "I think I'll go find somewhere a little more private!"
            show master sad
            "The old man looks disappointed as I walk away from him."
            "But he can just learn to deal with it for all I care."
            hide master
            "I'm not adding public nudity to the humiliation I've already endured today."
            "As soon as I have my panties off, I ball them up and get back to him."
            show master swimsuit perv noglasses
            "He nods eagerly as I hand them over."
            master.say "Thank you, my dear."
            master.say "Be back here tomorrow for your next lesson!"
            hide master with easeoutright
            "And then he scuttles away into the dunes."
            "Again I'm relieved that he seem to want to be alone with his prize."
            "It means that I can at least try to keep the image of what he'll do then out of my head!"
            $ hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the third lesson", "master_training_female_event_03", "master_training_female_event_missed"))
            if hero.morality > -40:
                $ hero.morality -= 1
        "Refuse":
            bree.say "You want my panties?!?"
            bree.say "Urgh...you're just a creepy old pervert!"
            "For all his supposed martial arts mastery, he doesn't see the kick coming."
            play sound punch_hard
            pause 0.2
            show master surprised at vshake
            "And when it connects with his groin a moment later, he goes straight down."
            show master upset at center, zoomAt (1.0, (640, 840)) with MoveTransition(0.1)
            show master at startle
            pause 0.5
            hide master with moveoutbottom
            "I don't even bother to look down at the old man as he rolls around on the sand."
            "Instead I just stride away down the beach, my head held high."
            "How in the hell did I ever let myself get suckered in by that guy?!?"
            $ hero.flags.master_training = False
    $ game.pass_time(2)
    return

label master_training_female_event_03(appointment=None):
    scene bg beach
    "I stride onto the sand with my head held high today, determined to see this thing through."
    "I've already had two lessons with the so-called martial arts master down on the beach."
    "And both of them have been an interesting mix of exertion and humiliation on my part."
    "I have no idea just what the creepy old man has in store for me today either."
    "Maybe this time we'll actually get down to learning something that resembles martial arts."
    "Or maybe it'll be another round of thinly-veiled attempts by him to perv on me in public."
    "Either way I'm convinced that I can deal with whatever he has to throw at me today."
    show master swimsuit normal noglasses with dissolve
    "At least I am until I spot him standing on the sand by a fairly lengthy pipe."
    "He spots me before I reach him, and begins to eagerly beckon me over."
    "But he doesn't seem to notice the look of confusion that's spreading across my face."
    show master normal at center, zoomAt(1.5, (640, 1040))
    master.say "Good morning, my dear!"
    master.say "I hope you're ready for today's lesson?"
    bree.say "Erm..."
    bree.say "I guess so, Master..."
    bree.say "Just what is today's lesson?"
    show master wink
    "The creepy old man smiles at this and gives me a wink."
    play sound woosh_punch
    show master happy at startle
    "And then he produces a golf ball from one of his pockets."
    "That done, he grins at me as if he's explained himself."
    bree.say "A golf ball and a pipe, Master?"
    bree.say "I'm not sure what that's all about!"
    show master normal
    master.say "It's about suction, my dear."
    master.say "Working on improving the power of your suck!"
    bree.say "Is...is that important in martial arts?"
    show master angry
    master.say "Why, of course it is!"
    master.say "The ability to suck nice and hard is important in all walks of life!"
    show master normal
    master.say "That's why I want you to suck this ball through that pipe."
    "I look from the ball to the pipe and then back again."
    "And I realise that it's a waste of time to even wonder if he's joking."
    "After two previous doses of this guy's crap, of course I know he's serious."
    bree.say "Let me get this straight, Master."
    bree.say "You want me to get down on my hands and knees."
    bree.say "And then suck a golf ball through a pipe."
    bree.say "All of that while in plain sight of everyone on the beach?"
    show master happy
    master.say "Got it in one, my dear!"
    hide master
    show master swimsuit normal noglasses
    with fade
    "I shake my head as I walk towards the pipe."
    "And by the time I'm actually on my hands and knees, I'm resigned to my fate."
    "I'm actually going to try my best to do this thing."
    "The old man obligingly scuttles over to the other end of the pipe."
    "Then he places the golf ball in the opposite end."
    show master wink
    "He gives me a thumbs up and a crooked smile."
    "Which I take as my cue to begin sucking."
    "It comes as no big surprise that it's as hard as I expected."
    "Even with my lips around the end of the pipe, I'm struggling."
    "And all the time I'm also trying not to think about where it's been."
    "Obviously I can't see down the other end of the pipe."
    "So I have to listen for sounds of the ball moving inside of it."
    "That and keep looking at the old man for reassurance."
    "He seems to be dividing his attention between me and the ball."
    "His eyes gaze down the pipe and then up at me periodically."
    show master blush
    "And from the look of delight on his face, I take it that I'm doing well."
    "Soon I'm getting dizzy from all the sucking, losing track of time."
    "Which means that when the ball finally reaches my end, I'm not ready for it."
    "All of a sudden, I feel it lodge between my lips."
    "And I stand up looking like a suckling pig with an apple jammed in its mouth."
    "My eyes are wide with surprise."
    "But I'm just glad that I didn't swallow the damn thing!"
    show master happy -blush
    master.say "Excellent sucking, my dear!"
    master.say "Well done!"
    "I cast a wary glance at him as I pull the ball out of my mouth."
    "He still hasn't mentioned the small matter of today's payment."
    "So I have a creeping sense of dread about what's coming next!"
    show master normal
    "And right on cue, the old man opens his mouth to speak."
    master.say "The price for this priceless lesson is to put what you've learned to good use."
    master.say "Specifically, by giving me a sample of your saliva!"
    menu:
        "Accept" if hero.morality <= -40:
            "Sure, it sounds disgusting."
            "But at least I don't have to actually do anything to him!"
            show master blush
            "So I take the cup that he offers me and proceed to spit into it."
            "It takes me a while to fill it to his liking."
            "And by the time I'm done, I have the driest mouth imaginable."
            "That and a crowd of people watching me, wondering what the hell I'm doing!"
            "But it's over, and that's the point."
            show master perv -blush
            master.say "Thank you, my dear."
            master.say "Be sure to be back here, bright and early tomorrow morning."
            master.say "Because we have so much more to learn!"
            hide master with easeoutright
            "With that, he turns and scuttles off up the beach, clutching his prize."
            "And I can't say I'm sorry to see him go."
            $ hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the fourth lesson", "master_training_female_event_04", "master_training_female_event_missed"))
            if hero.morality > -45:
                $ hero.morality -= 1
        "Refuse":
            bree.say "You want me to give you my spit?!?"
            bree.say "Urgh...you're just a creepy old pervert!"
            "For all his supposed martial arts mastery, he doesn't see the kick coming."
            play sound punch_hard
            pause 0.2
            show master surprised at vshake
            "And when it connects with his groin a moment later, he goes straight down."
            show master upset at center, zoomAt (1.0, (640, 840)) with MoveTransition(0.1)
            show master at startle
            pause 0.5
            hide master with moveoutbottom
            "I don't even bother to look down at the old man as he rolls around on the sand."
            "Instead I just stride away down the beach, my head held high."
            "Pardon the pun, but how in the hell did I ever let myself get suckered in by that guy?!?"
            $ hero.flags.master_training = False
    $ game.pass_time(2)
    return

label master_training_female_event_04(appointment=None):
    scene bg beach
    "When the time comes round for the fourth lesson with the so-called martial arts master, I feel like I'm ready."
    "After all, he already humiliated me three times over the past few days, with it getting worse each time."
    "Surely he can't have anything more in store for me that compares to sucking on a pipe and then his cock!"
    "And I do have to admit that I've been feeling the benefit of all the physical exertions he's put me through."
    "He's definitely creepy, but perhaps there's a method to his madness, like one of those drunken masters?"
    show master swimsuit happy noglasses with dissolve
    "Anyway, at least I can see that he's not standing next to anything awful when I spot him on the beach."
    "But all the same, the huge grin on his face is enough to make me feel wary."
    "Maybe I shouldn't be letting my guard down just yet..."
    show master normal at center, zoomAt(1.5, (640, 1040))
    bree.say "Good morning, Master!"
    master.say "And good morning to you too, my dear!"
    master.say "Today's lesson will be about building stamina."
    "I nod happily, thinking that doesn't sound too bad."
    show master perv
    "But then I see the old man's smile turn distinctly wicked."
    show master talkative at startle(0.1, 5)
    master.say "That, and the art of dealing with distraction as well!"
    bree.say "I...I see, Master..."
    bree.say "Well...actually, I don't see!"
    bree.say "How are you going to teach me about them both?"
    "The old man holds up a hand, pointing one finger upwards."
    show master talkative at startle(0.1, 5)
    master.say "Firstly, you'll be completing a run."
    master.say "Specifically ten kilometres along the beach!"
    "I can't help looking a little surprised at the announcement."
    "I mean, I think I can handle the distance without too much trouble."
    "It's just having the run sprung on me like that which comes as a surprise."
    bree.say "Yes, Master."
    bree.say "But what about the distraction you mentioned?"
    show master perv
    "At this, the old man's smile becomes positively evil."
    "And he extends a second finger."
    master.say "Secondly, you will complete the run while using this..."
    play sound woosh_punch
    show master normal blush at startle
    "Seemingly from nowhere, he produces what's clearly a vibrator."
    "And he waves it under my nose, apparently unconcerned with anyone else seeing it."
    master.say "Specifically, with this INSIDE of you!"
    "Now my eyes pretty much pop out of my head."
    "I look this way and that, suddenly aware of every stranger within sight."
    "Without thinking, I snatch the vibrator out of the old man's hand."
    "My reason for doing this is to hide it from prying eyes."
    "But he instantly takes it as my accepting the task."
    show master happy
    master.say "Good, very good!"
    master.say "You get that thing inside of you, my dear!"
    master.say "And I'll be waiting for you once you get back."
    scene bg beach with fade
    "I walk away from where the old man is standing until I'm out of his sight."
    "And then I stop and look down at the vibrator in the palm of my hand."
    "There's nothing to stop me just tossing it side and storming off."
    "Likewise I could just do the run and tell him I had it in me the whole time."
    "But there's still that perverse part of me that won't back down from a challenge."
    "It's the same part of me that wants to show him that I'm up to it."
    "The part of me that wants to beat him at his own game."
    "And it's also the part of me that wins out in the end."
    "As I find myself turning the vibrator on and pulling down my pants."
    "It takes a few moments to work the thing into my pussy."
    "But I manage it, feeling myself shudder at it begins to work on me."
    "Oh god, this should be the least erotic thing I can imagine."
    "And yet I can feel myself getting worked up the moment I start to run."
    "Like I expected, it's not the actual run that proves to be a challenge."
    "Instead it's the fact that everyone I pass turns their heads to stare at me."
    "Sure, it's nothing new and normally something that wouldn't be an issue."
    "In fact, it can be quite flattering when someone glances your way like that."
    "It's just that right now I know that I have a vibrator in my pussy."
    "And there's the paranoid fear that, somehow, they know it too."
    "Of course I know that sounds dumb, because they can't know."
    "But that doesn't stop my mind racing whenever somebody looks my way!"
    "And all the time I can feel myself getting more aroused by the second."
    "Soon enough it's not solely down to the vibrator either."
    "The shame of what I'm feeling is becoming a source of arousal in its own right."
    "And my cheeks flush red from that, rather than any feeling of exhaustion."
    "What if I can't keep on running?"
    "What if I stop and the thing makes me cum?"
    "What if someone tries to help, thinking I'm in danger?"
    "All of this is running through my head as I run along the beach."
    "And it's one of the reasons that I find myself eating up the distance."
    show master swimsuit normal noglasses
    "Only when I see the old man ahead on the sand do I feel any sense of relief."
    "He's standing just where I judge the end of the ten kilometres to be."
    scene bg beach at center, zoomAt(1.5, (640, 1040))
    show master swimsuit normal noglasses at center, zoomAt(1.5, (640, 1040))
    with vpunch
    "So when I reach him, I let myself collapse onto the sand at his feet."
    scene bg beach at center, zoomAt(1.5, (640, 940))
    show master swimsuit normal noglasses at center, zoomAt(1.5, (640, 880))
    with vpunch
    "I can't hold it back any longer, and I feel myself cumming."
    scene bg beach at center, zoomAt(1.5, (640, 840))
    show master swimsuit normal noglasses at center, zoomAt(1.5, (640, 720))
    with vpunch
    "But by curling into a ball, I try to make it look like sheer exhaustion."
    "All the time it's happening, he's standing over me."
    "And I just know that he's touching himself and giggling in delight."
    "Finally, my orgasm comes to an end, and I yank the vibrator out of my pussy."
    scene bg beach
    show master swimsuit normal noglasses
    with fade
    master.say "Well done, my dear!"
    master.say "You CAME through in the end!"
    master.say "Now, as for payment - today I would like a sample of your urine!"
    menu:
        "Accept" if hero.morality <= -50:
            "I don't have the energy left to be able to argue with him."
            show master blush
            "So I just get up on my hands and knees, accepting the cup he offers me."
            "And I hardly care if anyone sees me pull down my pants and pee into it either."
            "I hand the cup back to him and then just sit on the sand, utterly exhausted."
            show master perv -blush
            master.say "Thank you again, my dear."
            master.say "See you tomorrow for your final lesson!"
            hide master with easeoutright
            "With that, he turns and scurries away."
            with vpunch
            "Which leaves me to collapse onto my back, panting on the sand."
            $ hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the fifth lesson", "master_training_female_event_05", "master_training_female_event_missed"))
            if hero.morality > -55:
                $ hero.morality -= 1
        "Refuse":
            bree.say "You want my piss?!?"
            bree.say "Why, when you've been taking it this whole time?!?"
            bree.say "Urgh...you're just a creepy old pervert!"
            "For all his supposed martial arts mastery, he doesn't see the kick coming."
            play sound punch_hard
            pause 0.2
            show master surprised at vshake
            "And when it connects with his groin a moment later, he goes straight down."
            show master upset at center, zoomAt (1.0, (640, 840)) with MoveTransition(0.1)
            show master at startle
            pause 0.5
            hide master with moveoutbottom
            "I don't even bother to look down at the old man as he rolls around on the sand."
            "Instead I just stride away down the beach, my head held high."
            "How in the hell did I ever let myself get suckered in by that guy?!?"
            $ hero.flags.master_training = False
    $ game.pass_time(2)
    return

label master_training_female_event_05(appointment=None):
    scene bg beach
    "I've been put through the wringer by the so-called martial arts master over the last four courses."
    "Exercising in front of him, slapping him with my boobs, sucking balls through pipes and running with a vibrator in my pussy."
    "All of that has been and gone, so now all I have to endure is the last day of him teaching me, then it's finally over."
    "Surely nothing he has in store for me can be as bad as what he's already put me through, right?"
    "And it's with that in mind that I stride confidently across the sand towards him."
    "Part of me hoped that he might be in a slightly worse mood than he seems to be this morning."
    "I guess I thought the knowledge this is almost over might have made him a little downbeat."
    "But instead he has his characteristic grin plastered all over his face."
    show master swimsuit normal noglasses with dissolve
    bree.say "Good morning, Master."
    bree.say "I'm ready for my final lesson."
    "He nods eagerly, making me even more sure that he's in good spirits."
    master.say "Good morning to you too, my dear."
    show master happy at center, zoomAt(1.5, (640, 1040))
    master.say "It's time for your last and greatest challenge!"
    "Oh dear - I don't like the sound of that!"
    "Without giving me a chance to respond, he shoves something in my face."
    "Based on it's general size and shape, as well as what I know of him, I jump backwards."
    with vpunch
    "But then I see that it's nothing more than a banana."
    "Well, it's a particularly large banana, to be sure."
    "But other than that, it's just a piece of fruit."
    bree.say "My final lesson involves a banana, Master?"
    "Already my former relief is beginning to wane."
    "And I'm remembering my previous task."
    "As well as the part of my body it involved!"
    show master normal
    master.say "Yes, my dear."
    master.say "Your final challenge is to consume this banana!"
    "For a moment I don't quite understand what I'm hearing."
    bree.say "You...you want me to eat the banana?"
    bree.say "Using my mouth?"
    show master blush
    master.say "Well...yes and no."
    master.say "I want you to use your mouth."
    master.say "But you won't be eating it in the conventional sense."
    show master perv -blush
    master.say "You're going to be swallowing it whole!"
    with vpunch
    bree.say "SWALLOW IT WHOLE?!?"
    with vpunch
    bree.say "ARE YOU CRAZY?!?"
    show master surprised at startle
    "The old man lets out a nervous laugh and looks around in obvious fear."
    show fx drop
    "I can almost see the beads of sweat starting to appear on his bald pate."
    master.say "Wh...what's the matter, my dear?"
    show master normal
    master.say "Do you think it's too hard of a lesson?"
    master.say "I suppose I could always think of something less challenging."
    show master upset
    master.say "I just thought that you were more advanced than that..."
    bree.say "Oh no...no you don't!"
    bree.say "I've been to hell and back the past few days!"
    bree.say "And you're not fobbing me off like that now - not so close to the end!"
    scene bg beach
    show swallow food banana karate
    with hpunch
    "Before I know what I'm doing, I snatch the banana out of the old man's hand."
    "Then I peel it and proceed to shove it straight into my mouth."
    "It's only when I see him smiling again that I know he's got me."
    "The sly old bastard was playing on my pride to get what he wanted!"
    "Well, I'm not going to back down now - no way!"
    show swallow food medium banana karate
    "Slowly and surely, I push the banana towards the back of my mouth."
    "I feel it hitting the back of my throat, and my gag-reflex kicks right in."
    "But I remember all the times that I deep-throated a guy."
    show swallow food closed medium banana karate
    "Hell, that and all the times I swallowed a dildo too!"
    "That lets me ignore the nausea and keep right on going."
    show swallow food deep opened banana karate
    "Inch by inch I stuff the banana into my mouth and down my throat."
    "More than once I think it's stuck and that I'm going to choke."
    show swallow food deep closed banana karate
    "But, by some minor miracle, I finally manage to swallow it down."
    "The unchewed banana hits the back of my throat and I wince at the sensation."
    show swallow food shallow opened banana karate
    "Pulling back the banana, I make a point of smiling in triumph as I meet the old man's eye."
    scene bg beach
    show master swimsuit surprised noglasses at center, zoomAt(1.5, (640, 1040))
    with fade
    "He looks suitably impressed, almost aroused by what he just witnessed."
    "So maybe I shouldn't have been surprised by what he says next."
    master.say "Most impressive, my dear."
    show master happy blush
    master.say "And in light of that, the price of today's lesson will be a blowjob!"
    menu:
        "Accept" if hero.morality <= -60:
            "I'm all but ready to slap the taste right out of the old goat's mouth."
            "But then I stop to actually think about it for a moment."
            "I just choked down a whole damn banana."
            "And sure, I'm feeling the effects right now."
            "But I didn't choke and I think I could easily do it again."
            "So maybe there is something to what this guy's doing after all."
            "And if that's the case, then perhaps I should keep my side of the bargain too."
            bree.say "Okay, okay..."
            bree.say "But we do it out of sight."
            bree.say "And we do it quickly too!"
            show master perv -blush
            "The old man nods eagerly"
            "Probably not wanting to argue the finer points of the agreement for fear of blowing it."
            "Urgh...why can't I keep from making such terrible puns?"
            scene master bj with fade
            "As soon as we're out of sight, I get down on my knees."
            show master bj far
            "He drops his shorts, and I'm able to breath a sigh of relief."
            "Sure, he has a scrawny, old-man's body to match his wrinkled face."
            "But at least his cock looks presentable and is a decent size too."
            "And of course, it's already standing to attention in anticipation of what comes next."
            "Alright, this thing isn't going to suck itself, more's the pity."
            "I lean forwards and take the head into my mouth."
            show master bj close lick tongue
            "And I start to lick and suck straight away."
            "I'm not going to phone this one in, just in case he complains afterwards."
            show master bj suck
            "But all the same, I'm not going to waste time tickling his balls either."
            "That fact doesn't seem to matter to the old man though."
            "As almost instantly I hear him panting and groaning at my efforts."
            show master bj close handjob
            "It's kind of a shame really, that he's such a creepy old codger."
            show master bj handjob up
            "Because he has a pretty nice cock, all things considered."
            show master bj handjob down closed
            "On a nicer, cuter guy this would be a pleasant experience."
            "And with that in mind, I try to keep the image of the rest of him out of my head."
            show master bj handjob up
            "Mercifully it doesn't seem to take long for him to reach his limit."
            "I can't have been going more than a couple of minutes when I hear him exclaiming."
            show master bj handjob down
            master.say "Oh yes...yes..."
            master.say "That's the way, my dear..."
            show master bj handjob up opened
            master.say "The circle is complete...now you are the master...of oral!"
            "A moment later, I feel him start to cum..."
            menu:
                "Swallow his cum":
                    show master bj handjob cum inmouth with vpunch
                    "I let the old man shoot his load in my mouth, handling him easily."
                    with vpunch
                    "Every last drop goes down my throat before I pull his cock from between my lips."
                    show master bj far normal -handjob -lick -suck
                    "I lick the last drops from the corners of my mouth and then smile up at him."
                "Pull his cock out":
                    show master bj far tongue -handjob -lick -suck
                    "I pull the old man's cock from between my lips at the last moment."
                    show master bj cumshot cum onface with vpunch
                    "And then I let him shoot his load straight into my face."
                    with vpunch
                    "I make a point of gasping in mock surprise as I look up at him."
                    show master bj -cumshot cum onface normal with vpunch
                    "Droplets of sticky semen running down my cheeks and dripping off my nose as I do so."
            scene bg beach
            show master swimsuit blush noglasses at center, zoomAt(1.5, (640, 1040))
            with fade
            "He stumbles backwards and lands on his ass in the sand, looking dazed."
            "For a moment I actually think he might be having a heart attack."
            "And I feel annoyed that the old goat could die without finishing the job of teaching me."
            "But then he seems to recover his senses, panting and wiping the sweat off his forehead."
            master.say "W...well done...my dear..."
            master.say "I...I need to recover my stamina..."
            show master happy
            master.say "For your initiation ceremony tomorrow!"
            hide master with easeoutright
            "With that, he half crawls, half scampers into the dunes."
            "Which leaves me alone to clean myself up and reflect on today's lesson."
            $ hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the next lesson", "master_training_female_event_06", "master_training_female_event_missed"))
            if hero.morality > -65:
                $ hero.morality -= 1
        "Refuse":
            bree.say "You want me to give you oral?!?"
            bree.say "Urgh...you're just a creepy old pervert!"
            "For all his supposed martial arts mastery, he doesn't see the kick coming."
            play sound punch_hard
            pause 0.2
            show master sad -blush at vshake
            pause 0.5
            hide master with moveoutbottom
            "And when it connects with his groin a moment later, he goes straight down."
            "I don't even bother to look down at the old man as he rolls around on the sand."
            "Instead I just stride away down the beach, my head held high."
            "How in the hell did I ever let myself get suckered in by that guy?!?"
            $ hero.flags.master_training = False
    $ game.pass_time(2)
    return

label master_training_female_event_06(appointment=None):
    scene bg beach with fade
    "I make sure to arrive early for my lesson with the Master today."
    "Because he's been dropping pretty heavy hints something important is going to happen."
    "So the positive side of me is hoping that he's going to teach me a really cool technique."
    "But the side of me that always looks for the negative thinks he's going to do something gross."
    "I'm still torn between the two possibilities when I walk onto the beach to look for him."
    show master swimsuit asleep noglasses at center, zoomAt(1.0, (640, 840)) with dissolve
    "And there he is, sitting cross-legged on the sand."
    "Urgh..."
    "He's probably been here for hours, eyeing up the young girls in their bikinis."
    "But as I get closer, I'm surprised to see that he has his eyes closed."
    "Is he...is he actually meditating?!?"
    show master swimsuit asleep noglasses at center, zoomAt(1.25, (640, 980)) with fade
    "Hurrying over, I lower myself onto the sand across from the old man."
    "And then I look him up and down, impressed by his posture and ability to reach a higher plane."
    show master sleepy
    master.say "Hhhngh..."
    show master asleep
    "The Master makes a sound like a broken down mill sawing up wood."
    "And it's only now that I can see he's begun to drool down his chin."
    "The silly old fool isn't meditating at all."
    "He's just fallen asleep!"
    bree.say "Master?"
    show master sleepy
    bree.say "Erm...Master?"
    show master asleep
    "I look around before I do what I have in mind next."
    "Checking that there's nobody around to see the fallout if it goes wrong."
    bree.say "MASTER!!!" with vpunch
    "I yell into his ear at the top of my voice."
    "And I give him a good, hard shove on the shoulder for good measure too."
    show master surprised at center, zoomAt(1.0, (640, 980)), vshake
    master.say "WHA..."
    show master at startle
    master.say "GHA..."
    show master afraid at startle
    master.say "UNGH..."
    hide master with easeoutbottom
    "The old man's limbs flail wildly as he's shocked awake."
    "Then he over-balanced and tumbles backwards onto the sand."
    bree.say "Are...are you okay?"
    show master swimsuit afraid noglasses at center, zoomAt(1.25, (640, 980)) with easeinbottom
    "The old man sits up again with surprising speed."
    "His head still swaying from the shock of his rude awakening."
    show master sleepy
    master.say "Oh my..."
    master.say "You really are getting the hang of this stuff, my dear!"
    show master normal
    master.say "How else could you have managed to sneak up on me like that?"
    master.say "It must be my teachings that allowed you to do it!"
    menu:
        "You taught me well":
            "I shrug and shake my head."
            "Sure, I could disagree with him."
            "But what would be the point of that?"
            if hero.morality <= -65:
                bree.say "You've taught me a lot more than that, Master."
                bree.say "Maybe I can show you how much I've learnt some time?"
            else:
                bree.say "Of course, Master..."
                bree.say "I've been taking all of your teachings to heart."
            show master happy
            "The Master nods happily, blithely agreeing with the sentiment."
        "You were asleep!":
            "I frown at him and shake my head."
            "Why does he keep coming out with this bullshit?"
            if hero.morality <= -65:
                bree.say "Don't be silly."
                bree.say "You were asleep!"
                bree.say "And I always know how to wake a guy up!"
            else:
                bree.say "Oh come on!"
                bree.say "You were asleep!"
            "The Master doesn't really seem to hear what I'm saying."
            "He just nods blithely, as if I was agreeing with him."
    show master happy at center, zoomAt(1.25, (640, 880)) with vpunch
    "Without warning, the Master jumps to his feet."
    "And once on them, he starts throwing his arms around."
    show master at hshake
    "For all the world he looks like an old fool having some kind of seizure."
    "But previous experience tells me that he's actually doing some kind of exercise."
    show master at hshake
    "As usual it's almost impossible to see what the point of it is."
    "So I just get to my feet in anticipation of the lesson beginning."
    show master at hshake
    "The Master doesn't say anything to begin with."
    with hpunch
    "Which inspires me to start copying his movements."
    "Because I figure that his warm-up routine must be worth imitating."
    show master surprised
    show fx question zorder 2
    master.say "Eh?"
    master.say "What are you doing?!?"
    bree.say "Oh..."
    bree.say "I was just trying to follow your lead, Master."
    master.say "What are you talking about?"
    show master normal
    master.say "I only got up because my butt went to sleep!"
    "I can feel my cheeks flushing red as the old man explains himself."
    "So I stop moving and just stand there, looking down at my feet."
    bree.say "So..."
    bree.say "What's today's lesson going to be, Master?"
    show master normal
    master.say "Today's lesson is that this is the last lesson!"
    master.say "Congratulations, my dear..."
    master.say "I have taught you all that I can."
    master.say "Now your studies are over."
    bree.say "Really?"
    bree.say "Wow..."
    bree.say "So I'm no longer a student - I'm a master too?"
    master.say "Erm..."
    show master upset
    master.say "I maybe wouldn't go that far..."
    show master at startle
    "The old man coughs and shakes his head."
    "Making a conscious effort to change the subject."
    show master normal
    master.say "Anyway..."
    master.say "If you would like to express your gratitude to your master."
    master.say "Now would be the appropriate time."
    "I'm a little taken aback at the lessons coming to an end."
    "So being told that it's now time to show my gratitude just adds to that."
    "I blink and nod in confusion."
    "And then I see that the Master is fumbling with his shorts."
    master.say "Very, good, my dear..."
    master.say "I have just the thing in mind!"
    bree.say "What..."
    bree.say "What are you doing?!?"
    master.say "Just dropping my short, my dear."
    show master perv
    master.say "A blow-job will be more than enough for me!"
    master.say "Think of it as the final payment for all of my teachings."
    menu:
        "Accept" if hero.morality <= -70:
            "As soon as I realise what the Master is asking of me, I'm shocked."
            "And I give serious thought to kicking him in the balls and walking away."
            "But then I start to give the matter more serious thought."
            if hero.morality <= -75:
                "I mean, he does have some big balls on him to even ask."
                "And this is going to be the last time I have to deal with his sleazy ways..."
                bree.say "Ok, old man..."
                bree.say "But this is a one-time deal!"
            else:
                "Sure, it seems like something I'd be crazy to actually do."
                "But if it does mean that we're all done with the lessons..."
                bree.say "Okay. okay..."
                bree.say "I can't believe I'm actually doing this!"
            "The Master nods gleefully."
            "Then he turns his attention back to dropping his shorts."
            show master naked with dissolve
            "Luckily for me, we're already in a deserted spot on the beach."
            "So there's no chance of anyone stumbling upon us in the middle of the act."
            "That means there's no reason not to get started."
            scene master bj with fade
            "I take a deep breath and then get down on my knees."
            show master bj far
            "And when I look straight ahead, I get quite a surprise."
            "Firstly it's right there, looking me in the face."
            "Which means that he must have already been getting hard."
            show master bj close
            "Secondly it almost pokes me in the eye."
            "And that's because it's unexpectedly huge!"
            "I gape at the sheer size of the Master's manhood for a few seconds."
            "I mean, how can something that big be attached to his scrawny frame?"
            "And how in the hell is there enough blood in him to make it get that hard?"
            "The Master seems to note my surprise."
            "And he nods in approval."
            master.say "You seem impressed, my dear."
            master.say "But you should know by now that my teachings are so very potent."
            master.say "And what you see before you is just another proof of that fact!"
            "I make a point of nodding in agreement, but keep quiet all the same."
            "The last thing I want right now is to be drawn into a conversation about his cock!"
            "Instead I lean forwards and get down to work."
            show master bj lick tongue closed
            "I close my eyes and open my mouth, taking in the head as I do so."
            "There's no need to tease him into standing to attention."
            "And I know that the Master's mind is filled with desires of the flesh."
            "So there's little need to work on him from that side of things too."
            show master bj suck
            "As soon as I have the head of his cock in my mouth, I refocus my mind."
            "All of the misgivings from before seem to fall away as I commit to the task."
            "Lips, tongue and teeth all work in harmony with one another."
            show master bj close handjob opened
            "And as my head begins to move back and forth, I can hear the Master start to sigh."
            "That's a welcome sound, as it means I can gauge the pleasure he's feeling."
            show master bj handjob up
            "As my mouth takes care of the tip, I also use my hand on the shaft."
            "It moves up and down too, slow and gentle to begin with."
            show master bj handjob down closed
            "But it doesn't take long for me to pick up speed."
            "As I do so, my grip tightens until I'm squeezing pretty hard."
            show master bj handjob up
            "At the same time I can't help nuzzling with my teeth too."
            "I'm getting steadily rougher with every second that passes."
            show master bj handjob down opened
            "And yet the Master shows no signs of objecting."
            "In fact, he seems to be lapping it up!"
            "He lowers himself a little and grab my waist."
            "I can feel him starting to lift me, and in a move only a true master can perform, my world is upside down!"
            scene master sixtynine
            show master sixtynine blow with hpunch
            "With some incredible move, he manage to rotate me around his dick, his head now between my legs."
            "He even somehow managed to lift my karate gi as I can feel his tongue working on my lips."
            "The most impressive is that he performed his move with his cock in my mouth."
            "This makes me feel bold enough to push things further still."
            show master sixtynine blow squeeze
            "And so I redouble my efforts, taking him deeper and squeezing harder."
            "By now I can hear him panting, moaning at the sensations he's feeling."
            "His muscles are starting to twitch too, then to tense up."
            "It looks like he's getting ready for something big."
            "And I can guess what it is!"
            "Which means I have mere seconds to decide what to do next."
            menu:
                "Swallow":
                    "I decide to take the path of least resistance."
                    "So when the time comes, I brace myself to swallow."
                    with hpunch
                    "Sure enough, the Master loses it a moment later."
                    show master sixtynine blow wink with hpunch
                    "But I'm ready for him when he does."
                    show master sixtynine out wink swallow
                    "And so I manage to gulp down all that he has to give."
                "Facial":
                    "Before the final moment comes, I slide his cock out of my mouth."
                    show master sixtynine out normal
                    "And I do the best I can not to move an inch as he loses it in my face."
                    show master sixtynine out wink cumshot with vpunch
                    "I close my eyes as it spatters over my nose and cheeks."
                    show master sixtynine out wink cum -cumshot onface with vpunch
                    "Not even moving when it does, gravity pulling it down to my chin."
            scene bg beach
            show master naked noglasses happy
            with fade
            "A few moment later I'm back on my feet."
            master.say "Th...thank you...my dear..."
            master.say "Truly a masterful performance!"
            "I nod, accepting the praise of my master for what might be the last time."
            "And then I turn my mind to the task of cleaning myself up!"
            if hero.morality > -75:
                $ hero.morality -= 1
        "Refuse":
            "For a moment I don't really understand what the Master just said."
            "It kind of washes over me like the rest of his jabbering nonsense."
            "But then I actually manage to focus on his words and analyse them."
            "And I can't believe what I'm hearing."
            if hero.morality <= -65:
                bree.say "Oh, I bet!"
                bree.say "You'd fucking love that, wouldn't you?"
            else:
                bree.say "Are you serious?"
                bree.say "Are you actually for real?"
            "The Master smiles and nods."
            "Apparently unaware of how badly his suggestion is going down."
            "And this only serves to make me even more irate at him."
            if hero.morality <= -65:
                bree.say "I'll give you something to remember me by!"
                bree.say "Right where you want it too..."
            else:
                bree.say "You want stimulation down there?"
                bree.say "How's about this?"
            "Quick as a flash, I pull back my leg."
            "And then I swing it forwards."
            play sound punch_hard
            pause 0.2
            show master afraid -blush at vshake
            "It connects with the Master's groin before he even knows what's happening."
            "And a moment later his face twists into a mask of sheer agony."
            show master at center, zoomAt(1.25, (640, 980)) with MoveTransition(0.1)
            show master at startle
            "I watch as he fold in half and then sinks to his knees."
            hide master with moveoutbottom
            "Finally he curls into a ball on the sand, groaning quietly."
            "I nod and smile, feeling pleased with the results of my effort."
            "Maybe his lessons are paying off after all."
            "I keep that thought in mind as I turn and walk away."
            "Feeling a new surge of confidence in the knowledge that I've surpassed my teacher."
            $ hero.flags.master_training = False
    $ game.pass_time(2)
    return

label master_preg_talk:
    $ master.flags.toldpreg = True
    $ master.flags.know_is_father = True
    "It takes me a while to track him down, but I keep looking until I finally find the Master."
    "I get the impression that he hides himself away from most people and that he's good at it too."
    show master with dissolve
    "But eventually I find him, and when he sees that it's me, he seems eager to come out of hiding."
    show master happy
    master.say "[hero.name], my dear!"
    master.say "To what do I owe this undoubted pleasure?"
    "With a nervous smile on my face, I open my mouth to explain."
    "And I have no idea of just how he's going to react to what I have to say."
    bree.say "Ah...hi there..."
    bree.say "It's nice too see you too, I guess!"
    bree.say "But...I have something I need to tell you, Master!"
    show master surprised
    "Instantly the Master's expression changes."
    "He becomes almost twitchy and suspicious."
    "And he glances around like he's afraid of being caught out."
    show master normal
    "But he scuttles towards me all the same."
    master.say "Eh?"
    master.say "Have something to tell me, do you?"
    master.say "Well, you'd better come out with it!"
    "Now it's my turn to take a furtive look around me."
    "Like I suddenly don't want anyone to overhear what I have to say."
    bree.say "I..."
    bree.say "I missed my period this month, Master."
    bree.say "So I took a test, just to be sure."
    "The Master listens intently to my every word."
    show master surprised
    "And all the time his eyes are getting ever wider."
    bree.say "It was positive."
    bree.say "I'm pregnant, Master."
    bree.say "And I'm sure you're the father - one hundred percent!"
    "The Master stares at me for a moment in complete silence."
    "I can only imagine that his brain is processing the information."
    "So I wait patiently for him to say something."
    show master normal
    master.say "You're not joking, are you?"
    "I shake my head in response."
    master.say "You really are pregnant, aren't you?"
    "This time I nod."
    "The Master rubs his chin, curling the hairs of his beard."
    "And the whole time his face is pretty much unreadable."
    "So I find myself standing there, just waiting for him to react."
    "And finally he does so, nodding and letting out a resolute grunt."
    if master.love >= 150:
        master.say "I knew it!"
        master.say "I just knew it!"
        "I frown at this, puzzled by his reaction."
        bree.say "What?"
        bree.say "You mean you knew I was pregnant?!?"
        "The Master shakes his head at this."
        show master happy
        master.say "No, no, no..."
        master.say "I mean that I knew my seed was powerful!"
        master.say "My training in the mystical arts has preserved my fertility!"
        master.say "Don't you see - you're living proof of my enduring potency!"
        bree.say "Eww..."
        bree.say "That's kind of gross!"
        "If the Master is listening to me at all, he chooses to ignore what I just said."
        "Instead he waves his arms about, gesticulating in front of me."
        master.say "This is wonderful news, my dear!"
        bree.say "It is?!?"
        master.say "Oh yes, but of course it is!"
        master.say "It means that I have been blessed with a child."
        master.say "A disciple of my own potent seed."
        master.say "To whom I can pass on all of my knowledge and wisdom!"
        bree.say "So..."
        bree.say "You think we should...keep it?"
        master.say "But of course, my dear!"
        show master normal
        master.say "And I will need your help to raise the child too."
        master.say "As a master of the mystical arts, I cannot sully my aura with physical tasks."
        bree.say "Physical tasks being...what, exactly?"
        master.say "Oh, nappies, feeding, getting up in the middle of the night, and so on."
        master.say "All of that will be your responsibility."
        bree.say "Oh will it now?"
        bree.say "I think it might be time for a new take on those mystical responsibilities of yours..."
    else:
        show master sad
        master.say "You really can't expect me to be concerned with this matter, my dear!"
        master.say "I am a master of the ancient combat arts, a devotee of a mystical order!"
        master.say "Matters of the flesh do not concern me - they are a mere distraction!"
        "My eyes almost pop out of their sockets at the Master's answer."
        "Who in the hell does the old goat think he is?"
        "And does he really think all that mystic bollocks is going to fly here?!"
        bree.say "You didn't seem to have any problem with matters of the flesh before now!"
        bree.say "Especially the kind that landed me in this mess!"
        bree.say "Stop trying to get out of this, you horrid old man!"
        show master at center, zoomAt(1.25, (640, 900)) with vpunch
        "I take a step towards the Master."
        play sound woosh_punch
        hide master
        show master surprised at center, hshake
        "But he scuttles backwards, trying to keep out of reach."
        master.say "Now, now!"
        master.say "There's no need for violence, my dear."
        master.say "Didn't I teach you better than that?"
        show master at center, zoomAt(1.25, (640, 900)) with vpunch
        bree.say "Never mind what you did or didn't teach me."
        bree.say "What about right now, huh?"
        bree.say "You're setting a pretty shitty example!"
        play sound woosh_punch
        hide master
        show master surprised at center, hshake
        "The Master keeps on backing off, dancing out of reach."
        "And soon enough I realise there's no point in keeping this up."
        "Even if I do catch a hold of him, what then?"
        "I'll just look like I'm beating up a helpless old man!"
        "So I stand still and point a finger in his direction."
        bree.say "You listen to me, you old crook!"
        bree.say "You're going to pay for this, one way or another!"
        play sound woosh_punch
        show master at right with ease
        "The Master turns to flee, still shaking his head."
        master.say "I am a master of the mystical arts!"
        master.say "I cannot be judged by the same standards as mere mortal men!"
        "That last line strikes me as being pretty ironic."
        play sound woosh_punch
        hide master with easeoutright
        "Because right now he's running away from his responsibilities."
        "Which makes him just the same as any deadbeat guy off of the street!"
        $ master.breakup()
    return

label master_find_out_pregnancy:
    $ master.flags.toldpreg = True
    show master upset
    "The Master seems to be bothered by something, but I don't know what."
    "He keeps looking around, like he's trying to spot something."
    "But no matter how hard he tries, it remains stubbornly invisible."
    master.say "Hmmm..."
    master.say "I sense a disturbance in the air."
    show master angry
    master.say "As if a thousand masculine freedoms all cried out at once..."
    show master sad
    master.say "But were silenced!"
    "I frown at him, wondering what the hell all that means."
    show master surprised
    "But then I see him staring at me with intense interest."
    master.say "Wait a minute..."
    master.say "Tell me, [hero.name]..."
    master.say "Are you with child?"
    "The question catches me totally off-guard."
    "And because of that, I can't help answering honestly."
    bree.say "Y...yes!"
    bree.say "I am!"
    bree.say "But that's not all..."
    menu:
        "It's yours":
            $ master.flags.know_is_father = True
            bree.say "The baby belongs to you, Master."
            bree.say "You're the father of my child!"
            "Suddenly the old man doesn't look too pleased with the power of his insight."
            "In fact, he looks terrified!"
            if master.love >= 160:
                master.say "A father?"
                master.say "Me?!?"
                "I can't help staring at the old man in surprise and amazement."
                "This paragon of the mystical and martial arts."
                "Who now seems terrified of a little baby!"
                bree.say "Erm...yeah!"
                bree.say "That's what I said."
                "The Master's lips move silently for a few seconds."
                "And I get the feeling he's turning something over in his mind."
                show master happy
                master.say "What am I worried about?"
                master.say "I've faced down greater challenges than this!"
                master.say "Rival masters, street gangs, even accusations of public lewdness!"
                master.say "This is no different!"
                "I nod and smile, eager to encourage him."
                bree.say "Yes, Master."
                bree.say "It'll be like I'm the master and you're the student!"
                show master normal
                master.say "Eh..."
                master.say "Don't push your luck, my dear..."
            else:
                master.say "A father?"
                master.say "Me?!?"
                "I can't help staring at the old man in surprise and amazement."
                "This paragon of the mystical and martial arts."
                "Who now seems terrified of a little baby!"
                bree.say "Erm...yeah!"
                bree.say "That's what I said."
                "The Master's lips move silently for a few seconds."
                "And I get the feeling he's turning something over in his mind."
                show master sad
                master.say "Nope..."
                master.say "Not going to happen!"
                bree.say "Wha...what do you mean?!?"
                if master.love >= 150:
                    master.say "I mean that I will continue to be your teacher."
                    master.say "But I cannot aid you in raising the child."
                    bree.say "Are you serious?"
                    bree.say "This is your kid!"
                    bree.say "You're not going to lift a finger to help?!?"
                    show master upset
                    "The old man makes things worse by shaking his head."
                    "And the smug tone of voice he's using doesn't help either."
                    show master angry
                    master.say "I must keep my mind above such earthly things."
                    master.say "We are all gifted with certain talents, my dear."
                    master.say "And changing dirty diapers is not amongst mine!"
                    show master upset
                    "I nod, trying as best I can to hide my anger."
                    "But all the time I'm scheming inside of my head."
                    "And wondering what social services will make of his spiritual excuses..."
                else:
                    master.say "I mean that's it, my dear."
                    master.say "My time as your teacher has come to an end."
                    master.say "There is no more I can teach you."
                    master.say "And for all I know, you could be lying about who knocked you up!"
                    "I can't hide my shock at his reaction."
                    bree.say "Are you serious?"
                    bree.say "I guess you can't teach parental responsibility, huh?"
                    bree.say "Just how to be a deadbeat dad!"
                    "But even as I say all of this, I know it's too late."
                    "The Master gives me a hasty bow."
                    play sound woosh_punch
                    hide master with easeoutright
                    "And then he scuttles off as fast as his skinny legs will carry him."
                    bree.say "Yeah, you'd better run away!"
                    bree.say "You're going to be hearing from social services."
                    bree.say "You lousy old creep!"
                    $ master.set_gone_forever()
        "It's not yours":
            bree.say "The baby does not belong to you, Master."
            bree.say "You're not the father of my child!"
            "Suddenly the old man doesn't look too pleased with the power of his insight."
            "In fact, he looks shocked!"
            if master.love >= 140:
                master.say "You mean..."
                master.say "You have been unfaithful to your master?"
                master.say "You have tasted the waters of another's wisdom?"
                bree.say "Erm..."
                bree.say "If by that you mean did I sleep with someone else..."
                bree.say "Then yeah, pretty much!"
                "I feel myself cringing at the mere thought of what I have to do next."
                "But I don't see any other choice."
                bree.say "Master..."
                bree.say "I fear I cannot do this alone."
                bree.say "Will you help me?"
                if master.love >= 160:
                    show master happy
                    master.say "Yes, my dear - I will help you."
                    master.say "I've faced down greater challenges than this!"
                    master.say "Rival masters, street gangs, even accusations of public lewdness!"
                    master.say "This is no different!"
                    "I nod and smile, eager to encourage him."
                    bree.say "Yes, Master."
                    bree.say "It'll be like I'm the master and you're the student!"
                    show master normal
                    master.say "Eh..."
                    master.say "Don't push your luck, my dear..."
                else:
                    master.say "I will continue to be your teacher."
                    master.say "But I cannot aid you in raising the child."
                    bree.say "Are you serious?"
                    bree.say "You're not going to lift a finger to help?!?"
                    show master upset
                    "The old man makes things worse by shaking his head."
                    "And the smug tone of voice he's using doesn't help either."
                    show master angry
                    master.say "Maybe if the child were mine it would be different."
                    master.say "But as it is not, I must keep my mind above such earthly things."
                    master.say "We are all gifted with certain talents, my dear."
                    master.say "And changing dirty diapers is not amongst mine!"
                    show master upset
                    "I nod slowly, less than happy with what I'm hearing."
                    "But I hold my tongue and just nod in agreement."
                    "After all, he's right - this isn't his child."
                    "So maybe I should be glad he didn't just straight up dump me!"
                    $ master.breakup()
            else:
                master.say "Nope..."
                master.say "Not going to happen!"
                bree.say "Wha...what do you mean?!?"
                master.say "I mean that's it, my dear."
                master.say "My time as your teacher has come to an end."
                master.say "There is no more I can teach you."
                "I can't hide my shock at his reaction."
                bree.say "Are you serious?"
                bree.say "You're going to abandon me?"
                bree.say "In my time of need?!?"
                show master upset
                "The old man makes things worse by shaking his head."
                "And the smug tone of voice he's using doesn't help either."
                show master angry
                master.say "I must keep my mind above such earthly things."
                master.say "We are all gifted with certain talents, my dear."
                master.say "And changing dirty diapers is not amongst mine!"
                show master upset
                "The Master gives me a hasty bow."
                play sound woosh_punch
                hide master with easeoutright
                "And then he scuttles off as fast as his skinny legs will carry him."
                $ master.set_gone_forever()
    return

label master_kiss_me_female:
    show master
    "I'm trying to clear my mind with some of the tricks the master's taught me."
    "But it's just not working for some reason I can't put my finger on."
    "And I guess the stress must be plain to see on my face as well."
    "Because the master lets out a sigh and shakes his head."
    "I'm about to apologise and ask him to go through it with me again."
    hide master
    show master kiss
    with fade
    $ master.flags.kiss += 1
    "But instead, he leans forwards and plants a kiss on my lips!"
    "I'm about to push him back, to yell and even slap him."
    "And that's when I feel something surging from him and into me."
    "I don't know what it is, but somehow I suddenly understand."
    "All of the lascivious stuff he comes out with doesn't freak me out anymore."
    "It all seems to make sense, and so does he!"
    "Rather than pulling away, I lean into the kiss."
    "Soon enough I'm returning it with equal passion."
    "And I feel like I'm being enlightened more with each moment that passes."
    hide master kiss with fade
    return

label master_female_event_01:
    $ master.unhide()
    "I seriously thought that now I'd officially graduated, I could look forward to seeing less of my weird little martial arts teacher."
    "But when my phone vibrates and I check the screen, I see that there's a message from him waiting to be read."
    $ nvl_mode = "phone"
    nvl clear
    master_nvl "Greetings, my dear..."
    master_nvl "Are you ready for your final sparring session?"
    master_nvl "Meet me at the allotted time and place - and we shall see how much you've learned!"
    "I can't help being a little puzzled by the messages, as I was sure he said we were done with the lessons."
    $ nvl_mode = None
    "But rather than messaging him back to ask what the hell's going on, I decide to meet up with him."
    "Because he is kind of old, and he could just have forgotten that we wrapped things up the last time."
    $ game.room = "beach"
    scene bg black
    show bg beach
    show master karate
    with fade
    "Though when I make it to the appointed meeting place, I see that there's something different about the Master."
    "Sure, he looks like the same old skinny dude that he always was, with that creepy glint in his eyes."
    "But rather than his usual combination of loud shirt and shorts, he's wearing a martial arts gi."
    if hero.morality >= 25:
        bree.say "Here I am, Master."
        bree.say "Now what's this all about?"
        bree.say "I thought that my training was over?"
    elif hero.morality <= -25:
        bree.say "Hey there, you dirty old goat!"
        bree.say "You just couldn't get me out of your head, huh?"
        bree.say "Any excuse to have your eyes all over me one more time!"
    else:
        bree.say "Ah..."
        bree.say "Hi, there...Master..."
        bree.say "Look, I don't know if I'm still supposed to even call you that."
        bree.say "Actually...I don't really know why I'm here at all!"
    show master upset
    "The old man instantly begins to shake his head and wave his hands in the air."
    show master angry
    master.say "Ach..."
    master.say "So many pointless questions!"
    master.say "Have you forgotten all that I taught you already?"
    show master upset
    "I can't help frowning as the old man dismisses my questions just like that."
    "And I'm reminded of how relieved I was when I thought my time with him had come to an end."
    "Being spoken to like a child while treated like an object was never something that I was fond of."
    "So going back to that kind of relationship with him doesn't appeal to me now one little bit."
    show master normal
    if hero.morality >= 25:
        bree.say "Honestly, I'm not sure what you taught me!"
        bree.say "And you're lucky I'm here at all."
        bree.say "So you'd better get to the point, before I leave!"
    elif hero.morality <= -25:
        bree.say "All you taught me was to endure being perved over, you old goat!"
        bree.say "And you're lucky I even bothered to turn up."
        bree.say "So get to the point already!"
    else:
        bree.say "Yeah, I'm still not sure exactly what you were teaching me!"
        bree.say "And to be honest, I almost didn't come here today."
        bree.say "So maybe you should get to the point?"
    "The old man doesn't seem to be in the least bit bothered by my defiance."
    "If anything, it seems to make him all the more determined."
    show master talkative
    master.say "Yes, yes..."
    master.say "This is the most opportune of times."
    master.say "The perfect change to assess your skills."
    master.say "One final sparring session with your master, to show all that you've learned."
    show master normal
    "All the time he's saying this, the old man is fidgeting and hopping from one foot to the other."
    "At first I think it's a new nervous tic he's developed, or that he wants to go to the bathroom."
    "But then he starts clenching his hands into fists and circling his arms in the air."
    "And I realise that he's doing those warm-ups that martial artists always show off with."
    "All of this builds up to the point where he pulls his arms out of the sleeves of his gi top."
    show master topless
    with fade
    "Then lets the whole thing fall away to reveal his naked torso."
    "I guess the visuals would have been more impressive were he younger and less scrawny."
    "But overall he kind of looks as if he's about to strain himself right now!"
    show master happy
    master.say "HA!" with vpunch
    show master talkative
    master.say "Defend yourself!"
    show master normal
    "With that, the old man leaps forwards with surprising speed."
    "But rather than being surprised, I find that I'm totally prepared."
    "Time seems to slow down for me, like it does in the movies."
    "And I can predict what he's trying to do from the posture of his body."
    "This means I can easily sidestep the clumsy punch he's aiming at my jaw."
    "Then respond with a double-handed blow of my own, directly to his chest."
    bree.say "HAH!" with vpunch
    show master surprised
    master.say "Urgh!"
    show master stuned
    "I make sure that the blow isn't hard enough to seriously hurt the old fool."
    "Though it's still enough to make him stagger backwards, a shocked expression on his face."
    "Which only becomes more exaggerated as his legs wobble and he collapses onto his ass a moment later."
    master.say "M..."
    master.say "Mmm..."
    show master happy
    master.say "Marvellous!"
    show master normal
    "I was expecting to have to help the old man to his feet."
    "Maybe even to support him while he recovered from the blow."
    "But instead he hops up like a demented Jack-in-the-box."
    "A move that makes me think there might be something to his claims after all."
    show master happy
    master.say "That was simply marvellous, my dear!"
    show master talkative
    master.say "Proof positive that you are no longer my student."
    master.say "And that you're ready for the next stage in our relationship."
    show master normal
    "At the mention of the word 'relationship' I forget all about my concerns for the old man."
    "Because I was sure that this whole thing would be the last time I'd need to see him."
    if hero.morality >= 25:
        bree.say "Just what does that mean?"
        bree.say "I'm not paying for any more lessons!"
    elif hero.morality <= -25:
        bree.say "Don't go making any presumptions, old man."
        bree.say "Me kicking your ass doesn't entitle you to touch mine in return!"
    else:
        bree.say "Our relationship?"
        bree.say "I thought you taught me everything already?"
    "Again it doesn't really seem like what I just said has really sunk in for the old man."
    "Or maybe he's just one of those older men that never really learned to listen to women."
    "Because he seems content to babble on regardless, telling anyone in range of hearing what he thinks this means."
    show master talkative
    master.say "This is a whole new stage in our relationship, my dear."
    master.say "One where you may even begin to teach me new things."
    show master happy
    master.say "Wondrous things, such as how to use the television remote without squinting."
    show master perv
    master.say "Or how to order...ahem...specialist literature on the internet web thingie!"
    show master normal
    "I take a deep breath and shake my heads as I listen to all of this."
    "Because on the one hand, I'm still not sure exactly what it means for me."
    "But on the other, I'm guessing it does mean I'm not getting shut of the old goat just yet."
    $ master.flags.delay = TemporaryFlag(True, 2)
    return


label master_female_event_02:
    if master.love.max < 40:
        $ master.love.max = 40
    scene bg black
    show bg masterhouse at center, zoomAt (1.1, (640, 720))
    play sound beach loop
    with fade
    "After the whole 'graduation sparring' incident, it seems that I was right."
    "I'm not going to be seeing the back of the Master any time soon."
    "In fact it seems as though he's convinced our relationship has now changed."
    "That we've somehow graduated to a whole different level, beyond master and pupil."
    "But let's just say that I'm sceptical of the whole idea myself."
    "Because the main thing that seems to have ascended to a new level is the sheer amount of his ogling."
    "And his schemes to achieve it are getting even more complex and convoluted than before."
    show bg masterhouse at center, traveling(1.2, 2, (680, 720)) with easeinright
    "I mean, take today as a perfect example - I'm on my way over to his place."
    "The invitation was to come over and train in his yard."
    "But I'm already anticipating the usual hanky-panky on his part."
    if hero.morality >= 25:
        bree.say "Hello, Master?"
        bree.say "I'm here - where are you?"
    elif hero.morality <= -25:
        bree.say "Come on out, you old goat..."
        bree.say "I know you're already spying on me!"
    else:
        bree.say "Hello?"
        bree.say "Is there anyone home?"
    show bg masterhouse at center, traveling(1.2, 1.2, (640, 720)) with easeinright
    pause 1.5
    show bg masterhouse at center, traveling(1.2, 1.2, (680, 720)) with easeinright
    pause 1.5
    "I'm saying all of this as I wander onto the property and through the front yard."
    "What appears to be the old man's house is pretty nondescript in nature."
    "There are a couple of old cars on the driveway that seem to be in the middle of being repaired."
    "But other than that, there's really nothing out of the ordinary to be seen."
    "It's only when I walk around the side of the house and into the back yard that things change."
    "Because that's when I see the evidence he's been preparing for our training session."
    "Or at least what I guess passes for training in his odd little head."
    "There's a table set up with a load of what look like watermelons on it."
    "A large space that I suppose would be suitable for doing almost any kind of workout."
    "And strangest of all, there's even an old fashioned projector and screen off to one side."
    "Puzzled as to what most of this stuff is for, I look around for the old man."
    master.say "Ah..."
    master.say "There you are!"
    if hero.morality >= 25:
        bree.say "What the..."
    elif hero.morality <= -25:
        bree.say "What the fuck?!?"
    else:
        bree.say "Aaargh!"
    with vpunch
    play sound hitting_bushes
    show master karate at center, zoomAt(1.0, (340, 720)) with easeinleft
    show master karate at center, traveling(1.25, 0.9, (640, 900))
    show master karate normal
    "The old man suddenly pops up from behind a well-trimmed bush in one corner of the yard."
    "And I'm just about to lay into him for peeping just like he did back at the beach."
    "But then I see he's clutching a pair of garden shears in his hands."
    "And it occurs to me that he was more likely clipping the leaves on the bush."
    show master karate upset
    master.say "Hmm..."
    show master karate talkative
    master.say "It seems that you're already letting your senses become dulled."
    master.say "That means the need for us to keep on training together is more urgent than I thought!"
    show master karate normal
    "The old man tosses the shears aside with a worrying lack of care."
    "And then he beckons for me to follow him to the table with the melons."
    show bg masterhouse at center, traveling(1.25, 0.9, (700, 720))
    show chatting_fg_livingroom_01 at flip, dark, center, zoomAt(1.0, (540, 720))
    show watermelon at center, zoomAt(0.65, (320, 840))
    show master karate talkative
    with easeinleft
    master.say "Here's our first challenge, my dear..."
    master.say "Pummeling watermelons."
    show master karate normal
    if hero.morality >= 25:
        bree.say "Are you serious?"
    elif hero.morality <= -25:
        bree.say "Anything to get your hands on a pair of melons!"
    else:
        bree.say "If you say so!"
    show master karate upset
    pause 0.3
    show master karate talkative
    master.say "You must concentrate!"
    master.say "All that matters is the completion of the task at hand."
    master.say "If we do not succeed, then I won't have ingredients for my cocktails tonight!"
    master.say "Now observe, and then do as I do."
    show master karate angry
    "I watch as the old man draws back his fist, screwing up his face in a comical manner."
    play sfx1 punch_hard
    show master karate angry at vshake
    show watermelon at vshake, center, zoomAt(0.65, (320, 840)) with ease
    "And then he punches downwards at the first melon on the table."
    "Unsurprisingly, his bony little fist bounces right off it."
    "The next thing I know, he's dancing around waving it in the air."
    show master karate afraid
    show master karate at center, traveling(1.25, 0.5, (540, 900))
    pause 0.3
    show master karate at center, traveling(1.25, 0.5, (740, 900))
    pause 0.3
    show master karate at center, traveling(1.25, 0.5, (640, 900))
    pause 0.3
    master.say "Ouch!"
    master.say "Owie!"
    show master karate sad
    master.say "Damn melons, always out to get me!"
    show master karate normal
    menu:
        "Punch the melon":
            show master karate at center, traveling(1.1, 0.9, (340, 850))
            show bg masterhouse at center, traveling(1.25, 0.9, (680, 720))
            show chatting_fg_livingroom_01 at flip, dark, center, zoomAt(1.0, (620, 760)) with easeinleft
            show watermelon at center, traveling(0.85, 1, (640, 1000))
            "I can't help shaking my head at the old man's failure."
            "And the moment I turn my attention to the melons, I think I can see what happened too."
            "It looks to me like he punched the thing at the strongest point, so no wonder he didn't break it."
            "I take a few moments to tap the melons on the table, listening to how they sound."
            "And only once I've found one that feels weaker do I prepare myself for the punch."
            "In one smooth motion, I punch down into the melon I've chosen."
            bree.say "HIYA!" with vpunch
            play sfx1 punch_light
            show watermelon at vshake
            show aletta_doggy_cumshot as juice1 at watermelon, center, zoomAt(1, (500, 1300))
            show aletta_doggy_cumshot as juice2 at flip, watermelon, center, zoomAt(1, (700, 1300))
            show aletta_doggy_cumshot as juice3 at watermelon, center, zoomAt(1, (500, 1300))
            show watermelon at watermelon, center, traveling(0.85, 0.1, (640, 1500))
            show aletta_doggy_cumshot as juice1 at watermelon, center, traveling(1, 0.2, (300, 1000))
            show aletta_doggy_cumshot as juice2 at flip, watermelon, center, traveling(1, 0.2, (900, 1000))
            show aletta_doggy_cumshot as juice3 at watermelon, center, traveling(1.1, 0.2, (280, 1020))
            pause 0.2
            hide watermelon
            hide aletta_doggy_cumshot as juice1
            hide aletta_doggy_cumshot as juice2
            hide aletta_doggy_cumshot as juice3
            with dissolve
            show master happy
            "And just as I expected, my balled fist smashed straight through."
            "The melon explodes in a shower of red pulp."
            "I turn to regard the old man, expecting him to be suitably impressed."
            show master perv noglasses
            show master_glasses at center, zoomAt(1.1, (337, 860))
            with dissolve
            "But instead I catch him staring at my ass, eyes wide as saucers!"
            if hero.morality >= 25:
                bree.say "Do you mind?"
            elif hero.morality <= -25:
                bree.say "I thought you were into melons, not peaches!"
            else:
                bree.say "Hey, eyes on the melon, buddy!"
            hide master_glasses
            show master glasses sport normal at vshake
            "The old man flinches and leaps backwards, caught in the act."
            if hero.fitness <= 50:
                $ hero.grooming -= 2
            $ hero.fitness += 1
            $ master.love += 1
        "Cut and then punch the melon":
            show master karate normal at center, traveling(1, 0.9, (340, 800))
            show bg masterhouse at center, traveling(1.25, 0.9, (680, 720))
            show chatting_fg_livingroom_01 at flip, dark, center, zoomAt(1.0, (620, 760)) with easeinleft
            show watermelon at center, traveling(0.85, 1, (640, 1000))
            "I shake my head at the old man's silly little performance."
            bree.say "No way am I just straight-up punching that thing."
            "Glancing around, I see a knife on the table."
            play sfx1 knife
            "So I snatch it up and start to cut one of the melons."
            "But I don't cut it all the way through."
            "Instead I leave it just so."
            "That done I prepare myself for the punch."
            bree.say "HIYA!" with vpunch
            "In one smooth motion, I punch down into the melon I've chosen."
            play sfx1 punch_light
            show watermelon at vshake
            show aletta_doggy_cumshot as juice1 at watermelon, center, zoomAt(1, (500, 1300))
            show aletta_doggy_cumshot as juice2 at flip, watermelon, center, zoomAt(1, (700, 1300))
            show aletta_doggy_cumshot as juice3 at watermelon, center, zoomAt(1, (500, 1300))
            show watermelon at watermelon, center, traveling(0.85, 0.1, (640, 1500))
            show aletta_doggy_cumshot as juice1 at watermelon, center, traveling(1, 0.2, (300, 1000))
            show aletta_doggy_cumshot as juice2 at flip, watermelon, center, traveling(1, 0.2, (900, 1000))
            show aletta_doggy_cumshot as juice3 at watermelon, center, traveling(1.1, 0.2, (280, 1020))
            pause 0.2
            hide watermelon
            hide aletta_doggy_cumshot as juice1
            hide aletta_doggy_cumshot as juice2
            hide aletta_doggy_cumshot as juice3
            with dissolve
            "And just as I expected, my balled fist smashed straight through."
            "The melon explodes in a shower of red pulp."
            show master perv noglasses
            show master_glasses at center, zoomAt(1, (337, 810))
            with dissolve
            "I turn to regard the old man, expecting him to be suitably impressed."
            "But instead I catch him staring at my ass, eyes wide as saucers!"
            if hero.morality >= 25:
                bree.say "Do you mind?"
            elif hero.morality <= -25:
                bree.say "I thought you were into melons, not peaches!"
            else:
                bree.say "Hey, eyes on the melon, buddy!"
            hide master_glasses
            show master glasses sport normal at vshake
            "The old man flinches and leaps backwards, caught in the act."
            $ master.love += 1
        "Refuse to punch the melon":
            show master karate normal
            "I shake my head at the old man's silly little performance."
            bree.say "No way am I punching that thing."
            bree.say "Just cut it up with a knife."
            bree.say "And maybe stop being such a weirdo?"
            show master karate sad
            "The old man looks disappointed at my refusal to play along."
            show master karate normal
            "But I keep on giving him a hard stare until he gets the message."
            $ master.sub -= 1
            $ master.love -= 1
    show bg masterhouse at center, traveling(1.25, 0.9, (640, 720))
    show chatting_fg_livingroom_01 at flip, dark, center, zoomAt(1.0, (-500, 720)) with easeoutleft
    show beach_volleyball_ball_front_03 at blacker, center, zoomAt(1.1, (0, 1220)) with easeoutleft
    show master karate talkative at center, traveling(1.25, 0.9, (640, 900))
    master.say "Alright, alright..."
    master.say "Next we're going to work on our stamina."
    show master karate normal at center, traveling(1.25, 1, (1000, 900)) with ease
    pause 1
    show master karate normal at center, traveling(1.25, 2, (200, 900)) with ease
    pause 2
    show master karate normal at center, traveling(1.25, 2, (1000, 900)) with ease
    pause 2
    show master karate normal at center, traveling(1.25, 2, (640, 900)) with ease
    pause 2
    "The old man jogs on the spot and pedals his arms."
    "As if miming what he means is more efficient than actually saying it."
    "But at least a session of jogging is more sensible than punching fruit."
    if hero.morality >= 25:
        bree.say "Jogging sounds good."
        bree.say "How far are we going?"
    elif hero.morality <= -25:
        bree.say "I normally like to exercise in a horizontal position."
        bree.say "But I can do it standing up - and I can go for miles too!"
    else:
        bree.say "Jogging sounds more sensible to me."
        bree.say "How about a couple of miles?"
    show master karate normal at center, traveling(1, 1, (700, 800)) with ease
    pause 1
    show master karate normal at center, traveling(1, 1, (440, 800)) with ease
    pause 1
    "By now the old man is literally starting to jog around the garden."
    "And at first I think he's just warming up, as he's moving like he's in slow-motion."
    show master karate talkative
    master.say "Come on, my dear..."
    master.say "Just like this - follow my lead..."
    master.say "This is how a real warrior does it!"
    show master karate normal
    "I stare at the silly old fart in sheer amazement, unable to believe what I'm seeing."
    "He's actually doing it, running around the yard pretending to be in slow-motion."
    menu:
        "Join in":
            "I stand there watching him for a while."
            "Expecting him to stop and admit that all of this is a joke."
            "But when he doesn't, I shrug and make to follow his lead."
            "I mean sure, we must look completely ridiculous right now."
            "But surely there's got to be something in all of this, right?"
            "Either that or he's totally lost his mind!"
            show master karate happy
            master.say "Yes, yes, yes..."
            master.say "Now you're getting it, my dear!"
            show master karate normal
            "I force a smile onto my face and nod."
            "Feeling like a complete fool as I move with aching slowness."
            hide master
            show master perv noglasses sport at center, zoomAt(1, (440, 800))
            show master_glasses at center, zoomAt(1, (437, 810))
            with dissolve
            "Or at least I do until I catch the old man sneaking a look at me again."
            "Even in slow-motion, he's trying to get a good eyeful as I stretch and strain."
            hide master_glasses
            show master glasses sport normal at vshake
            if hero.morality >= 25:
                bree.say "Hey, eyes front and centre!"
            elif hero.morality <= -25:
                bree.say "Jesus wept - you'll be asking me to pause and rewind next!"
            else:
                bree.say "I can see what you're doing, and it's even more obvious in slow-mo!"
            $ hero.fitness += 1
            $ master.love += 1
        "Refuse to join in":
            "I just stand there, watching in complete disbelief."
            "But even my disapproving stare doesn't seem to have any effect."
            "As the ridiculous old codger keeps right on running in slow-motion."
            "All the time I'm watching him, I'm wondering if his mind is actually gone."
            "Maybe his brain finally turned to mush and I should call social services."
            show master karate wink
            "Because this is turning into a total clown-show!"
            $ master.sub -= 1
            $ master.love -= 1
    show master karate normal at center, traveling(1.25, 0.9, (640, 900)) with ease

    "Once he's finished pretending to run, the old man points to the projector screen."
    master.say "Now the final part of our training."
    master.say "And without doubt the most important!"
    show master normal
    if hero.morality >= 25:
        bree.say "Are we going to watch some martial arts drills on the screen?"
    elif hero.morality <= -25:
        bree.say "Are we going to watch some porno movies on the screen?"
    else:
        bree.say "Are we going to watch some martial arts movies on the screen?"
    "The old man chuckles to himself and shakes his head as he fiddles with the projector."
    "As if my guess was the most ridiculous thing imaginable."
    show master karate angry
    master.say "Heh..."
    master.say "No, no, no..."
    show master karate talkative
    master.say "Much better than that."
    show master karate normal

    "The projector stutters into life as he says this."
    "And naturally I find my gaze being drawn to the screen."
    "Where I see stock footage of a fireworks display projected into it."
    show master karate talkative
    master.say "Now we will practice our kata in front of a suitable backdrop."
    master.say "Just like all the best martial artist do in the films!"
    show master normal

    "I watch as he strides in front of the screen and begins to go through various kata."
    "And it doesn't take me long to realise that he's actually serious."
    "He really thinks this is going to help!"
    menu:
        "Join in with the kata":
            show master karate wink
            "Shrugging I walk to the old man's side and starts to copy his moves."
            "Soon enough I feel myself settling into the routine of it all."
            "And to my surprise, the fireworks really do seem to be helping."
            "They're reminding me of all those classic movies I've seen in the past."
            "The ones where the master and his student consolidate all the lessons."
            "And everything starts to come together before the final showdown."
            bree.say "I..."
            bree.say "I think I get it now..."
            bree.say "This is all about...achieving a certain state of mind, right?"
            show master karate surprised
            master.say "Wha..."
            master.say "What?"
            master.say "Oh...oh yes, that's exactly right!"
            show master karate normal
            "I turn my head just as I squat down, flexing my thigh muscles."
            hide master
            show master perv noglasses sport at center, zoomAt(1.25, (640, 900))
            show master_glasses at center, zoomAt(1.25, (637, 910))
            with dissolve
            "And that's when I see the old man's staring at my ass again!"
            hide master_glasses
            show master glasses sport normal at vshake
            if hero.morality >= 25:
                bree.say "Will you please stop that?!?"
            elif hero.morality <= -25:
                bree.say "Man, all of this beating around the bush is going to get you beaten around the butt!"
            else:
                bree.say "Geez, you're going to give yourself a bleed on the brain!"
            $ hero.fitness += 1
            $ master.sub += 1
            $ master.love += 1
        "Refuse to join in":
            "I shake my head as I watch the silly old fool going through the motions."
            "He honestly seems to think that what he's doing is helping his efforts."
            "But the reality is it's only serving to make him look like a complete moron."
            "And so I walk a little way off and just wait for him to finish."
            $ master.sub -= 1
            $ master.love -= 1
    show master karate sleepy with dissolve
    "All of the prancing around in front of the screen seems to have worn the old man out."
    show master karate sleepy at swing(1.0, 1.2, 1, -1.2, 0.8), center, zoomAt(1.25, (640, 1060))
    "As he gives me a grin and then almost collapses onto his ass in from sheer exhaustion."
    hide master
    show master karate at center, zoomAt(1.25, (637, 900)), hshake
    master.say "Urgh..."
    master.say "I'm pooped!"
    show master karate happy
    master.say "But we made some serious progress today, you and I."
    show master karate normal
    "Now that things are over for the day, I feel more inclined to be kind to him."
    "And so I shake my head, giving him a rueful smile."
    bree.say "Being around you is like watching a dodgy old VHS tape stuck on repeat, you know?"
    show master karate surprised
    master.say "Eh?"
    master.say "How so?"
    show master karate stuned
    bree.say "Well, it's fuzzy and the picture's always jumping around like crazy."
    show master karate normal
    bree.say "But it still has that weird kind of authentic charm."
    bree.say "Even if it should be in a museum!"
    show master karate happy
    "I was more than half meaning what I said as a jibe at the old man."
    "But he seems to take it as a massive compliment, smiling and puffing up his chest."
    "All of which makes me think that I'm not done with his efforts to endear himself to me just yet."
    "And part of me is already wondering just what kind of silly excuse he'll cook up to see me next."
    stop sound
    scene bg black with dissolve
    return


label master_female_event_03:
    if master.love.max < 60:
        $ master.love.max = 60
    scene bg black
    show bg street at zoomAt(1.2, (640, 720))
    with fade
    "Part of me is seriously wondering why I keep giving that sleazy old man another chance."
    "But another part of me is all too ready to admit that he does have a weird kind of charm."
    "You know, not the kind of charm that makes you want to hang around someone at parties."
    "I mean the odd kind of quirky charm that makes you slowly realise someone has a hold on you."
    "The exact kind of charm that makes you agree to meet someone for 'discipline practice' - whatever the hell that is!"
    "I mean seriously, what am I walking into here?"
    "I've agreed to meet the old man on the street that he asked me too."
    "And there's a lot of people around these parts too, now that I come to notice it."
    "So surely he can't be about to pull one of his typically creepy little tricks, can he?"
    show bg street at vshake
    master.say "Hello, my dear!"
    "I can't help jumping a little as I hear the sound of his voice."
    "That and looking around, expecting to see him leap out from behind something."
    show master casual normal at center with fade
    "But much to my surprise, there he is, simply standing in the middle of the sidewalk."

    if hero.morality >= 25:
        bree.say "Oh..."
        bree.say "Good morning, Master."

    elif hero.morality <= -25:
        bree.say "Hey, why aren't you hiding from me?"
        bree.say "Don't tell me you're tired of perving over me already!"
    else:

        bree.say "Oh, there you are!"
        bree.say "Hi, I guess."
    "If he notices my surprise, then the old man doesn't seem to let it show."
    "Instead he regards me with a broad smile on his wrinkly face."
    show master talkative
    master.say "No time for that, no time for that now..."
    master.say "We're here with a purpose in mind, remember?"
    show master normal
    bree.say "Discipline practice?"
    show master normal at startle(0.1, 5)
    "The old man nods happily."
    "Clearly pleased at my remembering his words."
    show master talkative
    master.say "Precisely that, my dear."
    master.say "Now follow me!"
    show master normal at startle(0.1, 5)
    show bg street at traveling(1.2, 0.5, (740, 720))
    "The old man turns neatly on his heel and starts to walk off down the street."
    "At the same time he waves for me to follow him with one hand."
    "Left with little other choice than staying where I am, I choose to do as he asks."
    "And so I fall in a step behind him, still wondering just where we're headed."
    "I've already tried as best I can to imagine what kind of place he could be taking me."
    "Where someone as quirky and cantankerous as him would go for 'discipline practice'."
    "But no matter how hard I've tried, only the most unlikely things come to mind."
    "And so I'm more than a little surprised when he stops outside the door of a noodle shop!"
    scene bg black
    show bg ramenshop at center, zoomAt (1.2, (640, 720))
    with fade
    show master casual happy at center, startle(0.1, 5) with easeinright
    play sound door_open
    master.say "Here we are!"
    show master normal
    "I look at the frontage of the shop and then back at the old man, expecting him to say more."
    "But from the expression on his face, I can tell he's not going to be forthcoming."
    "It's not that there's anything wrong with the look of the place, quite the opposite in fact."
    "The shop looks a little old-fashioned, but it's well-kept and looks to be pretty busy."
    "Plus the smells wafting out whenever the door opens are already making me feel hungry."

    if hero.morality >= 25:
        bree.say "Is this where we're going?"

    elif hero.morality <= -25:
        bree.say "Are you for real?"
    else:

        bree.say "This is it?"
    "The old man nods, holding the door open for me to walk inside."
    play sound door_close
    show master asleep
    "And as soon as I'm actually in the place, I can see why he's smiling."
    "The scents of the food are even more intoxicating than they were outside."
    "Plus there's a pleasant buzz of happy conversation from the tables too."
    "All in all, I feel like I couldn't be in here more than a few minutes without ordering something."
    show master happy at startle(0.1, 5)
    master.say "Ah..."
    master.say "Breathe it in, my dear."
    master.say "I have been coming here for more than fifty years."
    master.say "This place is a constant in my life, a never-changing anchor for my spirit."
    master.say "Plus they're the only place that ever gets the sauce on my favourite noodles just right!"
    show master normal
    "It's all I can do to keep myself from chuckling as I nod along."
    "I mean, most enlightened masters would retreat to a picturesque waterfall to meditate."
    "Or maybe they'd go all the way to an ancient monastery in the highest mountains."
    "But it kind of figures my Master would choose a noodle bar from the seventies!"
    "Hell, the place is clean, but I could believe it hasn't been redecorated since then too."
    show sasha normal at blacker, left, zoomAt (0.95,  (320, 720)) with easeinleft
    show sasha normal at blacker, traveling(0.95, 1, (320, 720))
    "Waitress" "Oh, hi, grandpa!"
    "I watch as a pretty young waitress walks by and greets the old man."
    show master angry at startle(0.1, 5)
    "He grunts something in reply, but it doesn't wipe the smile off her face."
    hide sasha at blacker with easeoutleft
    show bg ramenshop at center, traveling(1.2, 0.5, (540, 720))
    show master at startle(0.1, 5)
    "Instead of saying anything more, he shuffles off in search of a table."
    "But when we pass the counter, more voices can be heard raised in greeting."
    show master angry at startle(0.1, 5)
    "Employee 1" "Hey, grandpa!"
    show master angry at startle(0.1, 5)
    "Employee 2" "Hello, grandpa!"
    show master angry at startle(0.1, 5)
    "Employee 3" "Grandpa, you want the usual?"
    show master angry
    "I can see that the old man's doing the best he can to ignore the greetings."
    show bg ramenshop at center, zoomAt (1.25, (500, 800)), startle(0.1, 5)
    show master angry at zoomAt(1.2, (640, 800))
    "He sits down in his seat and grabs a menu, burying his face in it."
    "And as I take the seat opposite him, I can see that he's visibly embarrassed."
    menu:
        "Why everyone calls you 'grandpa' ?":
            "I'm still trying to figure out what's bothering the old man so much."
            "Because it's not like any of the staff were being mean to him just now."
            "In fact they all sounded nothing but genuinely affectionate towards him."

            if hero.morality >= 25:
                bree.say "Do you mind if I ask why they call you that?"
                bree.say "Why they all call you grandpa?"

            elif hero.morality <= -25:
                bree.say "So, is Grandpa like your nickname in here?"
                bree.say "Because you can't really have that many grandchildren, can you?"
            else:

                bree.say "Does it bother you, them calling you that?"
                bree.say "Because they all sounded really happy to see you just now."
            "For a moment I think the old man's not going to answer the question."
            "Either that or he's going to tell me to just drop it already."
            "But then I see the irritation fade from his features."
            "And he finally puts the menu down on the table to look me in the eye."
            show master talkative at startle(0.1, 5)
            master.say "Urgh..."
            master.say "Alright, alright..."
            master.say "I'm obviously not going to get any peace until I explain it to you, am I?"
            show master normal
            "I make a point of smiling sweetly as I shake my head."
            show master talkative at startle(0.1, 5)
            master.say "I already told you that I've been coming here a long time."
            master.say "And over the years you tend to see the people who work here come and go."
            master.say "They start out working when they're young and finding their feet."
            master.say "When they're older they move onto something that pays better."
            master.say "Then new kids take over, and kids are all the same."
            master.say "They get to know you, they ask for advice and stuff."
            show master normal
            show bg ramenshop at center, zoomAt (1.25, (500, 800)), startle(0.1, 5)
            "I'm nodding as I listen to the old man explain himself."
            "Beginning to see how he's become a fixture over the passage of the years."
            show master talkative at startle(0.1, 5)
            master.say "It's not that I mind them asking my advice, you understand?"
            master.say "It's just that I don't like being called grandpa."
            master.say "Because it makes me feel old!"
            show master normal
            show bg ramenshop at center, zoomAt (1.25, (500, 800)), startle(0.1, 5)
            "I keep on nodding, trying to be as sympathetic as I can."
            "But I note that the Master doesn't say it reminds him of being old."
            "Only that it makes him feel old, which is kind of interesting."
            "Maybe suggesting that he's in denial about a lot of things."
        "Tease the Master about being called grandpa":
            "I can't keep the smile off my face as I watch the old man squirm."
            "And this seems like too good of a chance to pass up being kind."
            "Because it's usually him doing all he can to embarrass me."

            if hero.morality >= 25:
                bree.say "Oh, Master..."
                bree.say "You never mentioned that you had such a big family!"

            elif hero.morality <= -25:
                bree.say "Are they all really your grandkids?"
                bree.say "Wow..."
                bree.say "You're a pretty potent old goat, huh?"
            else:

                bree.say "'Grandpa', huh?"
                bree.say "You really have been coming in here a long time!"
            "The old man shoots me a hard glance over the top of his menu."
            show master talkative at startle(0.1, 5)
            master.say "They're disrespectful little whipper-snappers, that's what they are!"
            master.say "Like so many of their generation - no respect for their elders!"
            show master normal
            "There's no way that last jab wasn't aimed at me."
            "But I still feel like it was worth the effort."
    show master talkative at startle(0.1, 5)
    master.say "Anyway, forget about all of that nonsense."
    master.say "I don't come to this place to chat..."
    master.say "No, I come here to eat noodles!"
    show master normal
    "I watch as he sticks his head into the air, twisting his scrawny neck this way and that."
    "It's pretty obvious that he's trying to get the attention of the waiting staff."
    "But all of them seem to be too busy to notice, much to his evident frustration."
    show master talkative at startle(0.1, 5)
    master.say "What is it with the youth of today?"
    master.say "No respect for their elders, you see?"
    master.say "Too busy with their Iboys and their Cellpods!"
    show master normal
    "Picking up one of the menus, I note that there's a QR code on the back of it."
    "Maybe that's why none of the staff are paying the old man any attention?"
    "They're expecting the customers to scan the code with their phones and order that way."
    menu:
        "Help the Master to scan the QR code":
            "I feel bad that the old man's casting around like he's all at sea."
            "After all, he's been coming in here for the best part of fifty years."
            "And the QR codes must be a relatively new thing to be throwing him off so badly."
            bree.say "No worries, Master..."
            bree.say "I can handle this."
            "Before he can object, I whip out my phone and scan the code."
            "And in an instant I'm on the restaurant's site and ready to order."
            "The old man leans in, looking over my shoulder at the screen of my phone."
            show master surprised at startle(0.1, 5)
            master.say "Huh!"
            master.say "Is that a menu?"
            show master talkative
            master.say "Darn fangled new things - never needed them when I was a lad!"
            show master normal at startle(0.1, 5)
            bree.say "Okay..."
            bree.say "What am I ordering?"
            show master talkative at startle(0.1, 5)
            master.say "Super Chilli Noodle Volcano Bowl..."
            master.say "And make that two - one for me and one for you!"
            show master normal
            "I can almost feel my stomach churn at the mere thought of it."
            "But I keep the smile on my face as I place the order."
            "Telling myself that he's been eating here for decades."
            "So that has to mean something, right?"
            $ master.love += 4
            $ master.sub += 2
        "Watches the Master complain and do nothing":
            "Sure, I could easily scan the code and explain it to the old goat."
            "But there's just too much entertainment to be had from watching him rant."
            "So I decide to lean back in my seat and just watch the fun play out."
            "After all, he was the one that dragged me here against my will."
            "Now the least he can do is cause a scene to entertain me in return."
            show master talkative at startle(0.1, 5)
            master.say "Hello?"
            master.say "HELLO?!?"
            show master angry at hshake
            master.say "AAARGH!"
            show master talkative
            master.say "Am I invisible to you people?!?"
            show master normal
            "I do the best I can to keep from bursting into peals of laughter."
            show sasha normal at blacker, left with easeinleft
            "Especially when one of the waiting staff finally relents and comes over to the table."
            show sasha normal at blacker, startle(0.1, 5)
            "Waitress" "What's the matter, Grandpa?"
            "Waitress" "Did you forget how to use the QR code again?"
            "Waitress" "Want me to remind you?"
            "Of course the offer is full of good intentions."
            "But that only seems to make the whole situation worse."
            show master angry at startle(0.1, 5)
            master.say "No I do not!"
            master.say "Just get me my usual, okay?"
            show master normal
            "If the old man's rude tone bothers the waitress, she doesn't let it show."
            "Instead she just nods and smiles, as if his words haven't affected her in the slightest."
            show sasha normal at blacker, startle(0.1, 5)
            "Waitress" "Sure thing, Grandpa."
            "Waitress" "And for your companion?"
            show master talkative at startle(0.1, 5)
            master.say "She'll have the same as me!"
            show master normal
            show sasha normal at blacker, startle(0.1, 5)
            pause 0.2
            hide sasha at blacker with easeoutleft
            "The waitress nods happily and hurries off with the order."
            "Which leaves the old man still grumbling and harrumphing in his seat."
            $ master.love -= 2
            $ master.sub -= 1
    "Before the waitress arrives with our food, the old man starts fidgeting a little."
    "And then he stands up, gesturing for me to remain seated when I follow his example."
    show master talkative at startle(0.1, 5), traveling(1.2, 0.5, (640, 750))
    master.say "No need to get up, my dear."
    master.say "I just have to go to the bathroom, that's all."
    show master normal at traveling(1.2, 2.5, (-200, 750))
    "I nod and then watch as he scuttles off to answer the call of nature."
    "Making sure to note the direction for the sake of future reference."
    show sasha normal at blacker, left with easeinleft
    "Waitress" "Hey there..."
    "I look up to see the waitress from before."
    "She has the same smile on her face and is holding two steaming bowls of noodles."


    "I return the smile as she places them on the table in front of me."
    bree.say "Mmm!"
    bree.say "That smells great."
    show sasha normal at blacker, startle(0.1, 5)
    "Waitress" "I hope you like it."
    "Waitress" "Not many people order that particular dish these days."
    "Waitress" "Don't tell Grandpa this, but we only keep it on the menu because it's his favourite!"
    "The waitress lets out a little giggle as she lets me in on the secret."
    "But I can tell that there's no malice in the laughter, just fondness."
    bree.say "Wow..."
    bree.say "That's really kind of you."
    bree.say "You guys must really think a lot of him."
    show sasha normal at blacker, startle(0.1, 5)
    "The waitress nods at this."
    "Waitress" "We do, we do!"
    "Waitress" "I know that he pretends to be all dour and weird."
    "Waitress" "But underneath it all he's just a big softie!"
    "Waitress" "Actually, it's really great of you to come out to dinner with him."
    "Waitress" "He'd never admit it, but I think he's a very lonely guy."
    show bg ramenshop at center, zoomAt (1.25, (500, 800)), startle(0.1, 5)
    "I'm nodding as the waitress confides all of this in me."
    "Just taking it all in as I begin to see the old man in a very different light."
    "Maybe this explains a whole lot about him, why he behaves the way he does."
    "Is it possible that he's just putting on a front to hide the fact he's so alone?"
    show master angry at traveling(1.2, 2, (640, 750))
    master.say "Ah..."
    master.say "Sustenance!"
    show master normal at traveling(1.2, 0.5, (640, 800))
    "At the sound of the old man's voice, the waitress turns to walk away."
    show sasha normal at blacker, startle(0.1, 5)
    "But she puts a finger to her lips as she does so, and I know what that means."
    "She's asking me to keep what just passes between us to myself."
    hide sasha at blacker with easeoutleft
    "Which makes me think she also cares for the old man's pride."
    "I'm sure to smile and look excited as I pick up my chopsticks."
    show master happy
    play sound licking
    "And the old man doesn't stand on ceremony either, leaping into his meal a second later."
    "I take my time, keen to assess the ferocity of the noodles before committing myself."
    play sound licking
    pause 1.2
    play sound licking
    "But he's already shovelling and slurping like he hasn't eaten for a week!"
    "In the end I manage to make it through most of the bowl."
    "Sure, it's hot, but nothing a steady supply of cold water can't counter."
    "The old man polishes off the noodles and then picks up his bowl."
    "And I watch as he drinks the last of the sauce it was served in too."
    "Then he leans back, wiping his mouth on the back of his hand."
    show master asleep at startle(0.1, 5)
    master.say "Mmm..."
    master.say "Now that really hits the spot!"
    show master normal

    if hero.morality >= 25:
        bree.say "It was a bit spicy!"
        bree.say "But I can see why you like it."

    elif hero.morality <= -25:
        bree.say "Ah, it was okay."
        bree.say "But I can think of better ways to hit my spot!"
    else:

        bree.say "I couldn't eat that every day."
        bree.say "I don't think my guts could take it!"
    "I'm expecting the old man to say something cryptic in response."
    "Or at least to complain about something minor and inconsequential."
    "But instead he seems to become quiet and contemplative for a moment."
    show master talkative at startle(0.1, 5)
    master.say "You know, my dear..."
    master.say "I think you and I have spent quite a lot of time together now."
    master.say "More than I can remember spending with any of my previous students."
    master.say "People of your age...well, they don't usually put up with me this long!"
    show master normal

    if hero.morality >= 25:
        bree.say "Maybe I'm not like most people my age."
        bree.say "Maybe I have an old soul?"

    elif hero.morality <= -25:
        bree.say "Well, you already taught me a lot."
        bree.say "So maybe I'm hanging around to see what else I can learn from you?"
    else:

        bree.say "Yeah, I know what you mean, Master."
        bree.say "I can't explain it, but I just seem to like your company."
    show master happy at startle(0.1, 5)
    "The old man nods happily at this, as if he's happy with my answer."
    "Which I choose to take as a sign that I'm free to polish off my noodles."
    "As he seems to be lost in thought for the moment."
    "Staring into space as the bustles of the noodle shop goes on all around him."
    scene bg black with dissolve
    $ master.flags.delay = TemporaryFlag(True, 2)
    return

label master_female_event_04:
    if master.love.max < 80:
        $ master.love.max = 80
    play sound beach loop volume 0.20
    scene bg beach
    with fade
    "I'm starting to feel like I never know what's going to be in store for me when I go to call on the master."
    "Every time I show up, it seems like he's got some new crazy kind of training that he wants me to indulge in."
    "Either that or I find myself being dragged along on an adventure into his eccentric personal life."
    "So when he called me up and asked me to meet him at the beach today, it almost came as a relief."
    "Because that's where we spent most of our time together back when he was actually teaching me martial arts."
    "Well, I say he was teaching me."
    "Anyone who knows the old rascal knows that he has a very unique take on that kind of thing!"
    "All the same, it's a pretty nice day, and the beach is quiet around this time too."
    "So strolling out onto the sand is pleasant enough, even if I have no idea what he's got in store for me today."
    master.say "Hey!"
    master.say "Hey...over here!"
    "And just like that, the serenity of the beach is shattered by the sound of the master's voice."
    show bg beach at zoomAt(1.2, (600, 720))
    show master swimsuit at center, zoomAt(0.75, (940, 720))
    with fade
    "I turn to look in the direction that it came from, and see him waving frantically to me a little way off."
    "Rather than shouting back at him, I offer a wave to show that I've seen and heard him."
    play sound beach loop volume 0.10
    show bg beach at center, traveling(1.25, 1.0, (490, 740))
    show master at center, traveling(1.25, 1.0, (640, 880))
    "And I begin to make my way to where he's standing on the sand, well away from the lapping of the tide."
    "As I get closer, I make a point of scanning around to see just what he's brought with him on this occasion."
    play sound beach loop volume 0.05
    "Because I've found that any chance to be forewarned of the guy's intentions is a very good thing."
    "Right now all I can see that he has with him is a shovel, that and nothing else."
    "But before I can ask him what in the hell that's for, he launches into his usual enthusiastic pitch."
    stop sound fadeout 0.3
    show master talkative at startle(0.1, 5)
    master.say "Good morning, my dear..."
    master.say "So glad that you could make it here today."
    show master normal
    "By now it's actually more like early afternoon than morning."
    "But since when has this guy ever let reality stand in his way?"

    if hero.morality >= 25:
        bree.say "Good morning, master..."
        bree.say "I wish I could have gotten here sooner!"

    elif hero.morality <= -25:
        bree.say "I'm on time, aren't I?"
        bree.say "One more young girl for you to ogle..."
    else:
        bree.say "Hello, master..."
        bree.say "I came as fast as I could."
    "Okay, so that's not really true - I kind of dragged my heels getting here."
    "But I think we already established this relationship isn't based on total honesty."
    show master talkative at startle(0.1, 5)
    master.say "Very good, very good..."
    master.say "That kind of enthusiasm is what we're going to need."
    master.say "Because now we're well beyond the limitations of my conventional teachings."
    show master normal
    "I raise my eyebrows, making it look like I'm impressed by all of his big talk."
    "But in reality, I'm more intrigued to find out what new nonsense this is going to involve."
    bree.say "Really, master?"
    show master talkative at startle(0.1, 5)
    master.say "Oh yes indeed!"
    master.say "You've progressed so far in my tutelage that it's time to pass on more elite knowledge."
    master.say "Time to begin training you in the secret aspects of my peerless martial arts!"
    show master normal
    menu:
        "Pretend to be impressed":
            "Not wanting to sound like I'm ungrateful or cruel, I nod at this."

            if hero.morality >= 25:
                bree.say "Please continue, master..."
                bree.say "Impart upon me your wisdom."

            elif hero.morality <= -25:
                bree.say "I mean, I'd rather be leaning something a little more...intimate."
                bree.say "But maybe there'll be time for that later?"
            else:
                bree.say "Yes, master..."
                bree.say "I'm more than ready to learn!"
            "The old man nods, looking pleased at my positive attitude."
            show master talkative at startle(0.1, 5)
            master.say "That's the spirit, my dear!"
            master.say "Now let's get on with it."
            show master normal
            $ master.love += 2
        "Put the Master on the spot":
            "The old coot keeps on talking about how advanced of a pupil I'm getting to be."
            "And to me at least, that means I should be getting treated with a little more respect."
            "As well as being able to call him on some of the more outrageous examples of his bullshit."
            bree.say "That all sounds good, master..."

            if hero.morality >= 25:
                bree.say "As long as this isn't something icky and rude?"

            elif hero.morality <= -25:
                bree.say "Unless it's you're going to show me something cool?"
            else:
                bree.say "So long as this isn't something weird and creepy, yeah?"
            bree.say "Like you making me watch while you chop bits of wood using your dick?"
            "The old man seems to get more than a little flustered at my questions."
            "Puffing himself up and sticking out his scrawny chest."
            show master talkative at startle(0.1, 5)
            master.say "What do you take me for, girl?!?"
            master.say "This is nothing of the sort!"
            show master normal
            "He turns his back on me and starts to make his preparations for the so-called lesson."
            "But part of me can't help thinking that I might actually have gone and put a new idea into his head."
            "Rather than making him curtail his indecent antics as I'd intended to."
            $ master.sub += 1
    "The spade was already driven into the sand when I first laid eyes on it."
    "But the old man's never been the type to pass up the chance for some theatrics."
    play sound woosh_punch
    "So he pointlessly pulls it out and then proceeds to thrust the blade into the sand again."
    "And he does all of this while gesturing for me to look at the sand."
    show master talkative at startle(0.1, 5)
    master.say "Do you see this, my dear?"
    master.say "Do you understand what it demonstrates?"
    show master normal
    bree.say "Erm..."
    bree.say "That a spade's pretty good at digging into sand?"
    show master upset
    "The old man rolls his eyes and shakes his head."
    show master whining at startle(0.1, 5)
    master.say "No, no, no!"
    show master talkative
    master.say "It shows that the sand is strong."
    master.say "See how the spade stands up when jammed into it."
    show master normal
    "I can't help chuckling to myself, as I can see where this is going."
    menu:
        "Let the Master make his point":
            "But this will probably be over quicker if I just play along."
            "So I nod and wait for the master to explain his lesson to his pupil."
            show master talkative at startle(0.1, 5)
            master.say "This is the principle we must cultivate in ourselves."
            master.say "We must imitate the strength and resistance of the sand!"
            $ master.love += 1
        "Call the Master on the lesson":
            "And maybe if I call him on it, this will be over more quickly."
            bree.say "Let me guess..."
            bree.say "I have to be like the sand?"
            "The old man looks more than a little annoyed."
            show master whining at startle(0.1, 5)
            master.say "I..."
            master.say "Well..."
            master.say "Not necessarily - you don't know that I was going to say that!"
            show master normal
            bree.say "Oh come on, master..."
            bree.say "Almost all of your lessons are like that."
            bree.say "I have to be like something, or capture the essence of something."
            show master upset
            "The master crosses his arms over his chest, looking grumpier than ever."
            show master angry at startle(0.1, 5)
            master.say "Well maybe they are, young lady..."
            master.say "But when something works perfectly well, why change it?"
            $ master.love -= 2
            $ master.sub += 1
    show master normal
    "Without another word, he plucks the spade out of the sand and hands it to me."
    show master talkative at startle(0.1, 5)
    master.say "Today you will be undertaking special sand resistance training."
    master.say "So in short - get digging!"
    show master normal
    "I let out a defeated sigh, thinking I should have seen this coming too."
    play sound digging
    scene bg black
    show beach_sandcastle_bg_01
    show beach_sandcastle_npc_bree at center, zoomAt(1.25, (940, 820))
    show beach_sandcastle_outfits_bree_swimsuit at center, zoomAt(1.25, (940, 820))
    with fade
    "But all the same, I take the spade and start digging on the spot he points out."
    "Luckily for me, the sand here is pretty soft and it's not too hard for me."
    "Soon enough I've dug a hole that's deep enough for me to stand in."
    "So I look up at the old man, hoping that it's going to be enough."
    "But to my dismay, he simply shakes his head, holding a hand up to his chin."
    scene bg black
    show bg beach at center, zoomAt(1.25, (490, 740))
    show master swimsuit at center, zoomAt(1.25, (640, 880))
    pause 0.2
    show master talkative at startle(0.1, 5)
    master.say "Not deep enough!"
    master.say "Your chin needs to be level with the ground."
    master.say "So keep on digging!"
    show master normal
    "I do as I'm told, reasoning that it's the simplest way to get out of this mess."
    "But I can't help starting to worry about just why the hole needs to be that deep."
    "And there's only one reason that I can imagine, one that's not pleasant to imagine."
    "So when I look up and realise that the hole is about as deep as he wanted it, I feel a rising sense of dread."

    if hero.morality >= 25:
        bree.say "Phew..."
        bree.say "I hope that's deep enough?"

    elif hero.morality <= -25:
        bree.say "Okay, that's it - I'm done."
        bree.say "I wish someone would go this deep into one of my holes!"
    else:
        bree.say "Ah..."
        bree.say "I think I'm done."
    "The old man appears at the edge of the hole, now looking down on me from above."
    show master talkative at startle(0.1, 5)
    master.say "Very good."
    master.say "Now, bury yourself in the hole!"
    show master normal

    if hero.morality >= 25:
        bree.say "Oh dear..."
        bree.say "I really should have seen that coming!"

    elif hero.morality <= -25:
        bree.say "Hah - change would be a fine thing!"
        bree.say "Oh, I see...you mean this hole, right?"
    else:
        bree.say "Yeah..."
        bree.say "I was afraid you were going to say that!"
    "My mind is racing as I say all of this, looking for a way out."
    "And then I remember how hard it was to get all of that sand out of the hole."
    "Never mind putting it back while I'm still down here."
    show master talkative at startle(0.1, 5)
    master.say "Well?"
    master.say "What are you waiting for?"
    show master normal
    bree.say "I don't think I can bury myself, master."
    bree.say "I really don't think there's enough room in here."
    show master talkative at startle(0.1, 5)
    master.say "Nonsense, girl..."
    master.say "Get out of there and let me show you how it's done!"
    show master normal
    "I'm more than eager to scramble out of the hole when given the chance."
    show master at center, traveling(1.35, 0.3, (580, 860)) with ease
    pause 0.2
    hide master with moveoutbottom
    "And I do the best I can not to blow it as I watch the old man jump in there."
    play sound digging
    "Determined to prove me wrong, he instantly starts trying to use the spade."
    "Waving it around in the air as he searches for the piles of sand I made."
    "But more than anything, he manages to spill most of it over his own head."
    show master talkative at startle(0.1, 5)
    master.say "Bleugh..."
    master.say "There's sand everywhere!"
    show master normal
    bree.say "Maybe you could do with some help?"
    show master talkative at startle(0.1, 5)
    master.say "Oh..."
    master.say "What a good idea!"
    show master normal
    "The old man eagerly hands the spade up to me and keeps on working with his hands."
    "Unable to believe that he feel for it, I make sure to get straight to work."
    "And soon enough, he's beginning to disappear as the hole is filled in around him."
    stop sound
    scene bg black
    show beach_sandcastle_bg_02 at center, zoomAt(2.5, (640, 720))
    show master swimsuit normal noglasses at center, zoomAt(2.5, (640, 1720))
    show beach_sandcastle_castle_02 zorder 2 at center, zoomAt(2.5, (680, 880))
    with fade
    "In the end there's only his wrinkled head visible above the sand."
    "Looking for all the world like a deflated, hairy football."
    show master talkative at startle(0.1, 5)
    master.say "There you go, my dear..."
    master.say "Proof positive that what I asked is possible."
    show master normal
    "He's looking up at me as she says this."
    "But then the reality of his situation seems to dawn on him."
    "And his expression starts to look somewhat more concerned."
    show master talkative at startle(0.1, 5)
    master.say "Ah..."
    show master whining
    master.say "So..."
    master.say "Be a good girl and dig me out, yes?"
    master.say "Then you can bury yourself, and I promise that I'll help!"
    master.say "I mean, you must have been in tighter situations than this?"
    master.say "Heh...you probably are tighter than this yourself, right?"
    show master normal
    "Okay, that's it."
    "The dirty joke on top of all the other bullshit."
    "That's just too much for me to take."
    "I cross my arms over my chest as I look down at him."
    "And I make sure there's a non-commital look on my face as I do so."
    bree.say "Hmm..."
    bree.say "You know what, master..."
    bree.say "I'm still not totally sure about this one."
    bree.say "So I think I'll just sit it out and watch you do the training, okay?"
    "I give him a smile as I sit down on the sand a few feet away."
    "Pretending to watch him, but in reality looking out to sea and enjoying the view."
    show master whining at startle(0.1, 5)
    master.say "Hey!"
    master.say "What's the meaning of this?!?"
    master.say "You are my pupil, and I am your master..."
    master.say "That means you have to obey me!"
    show master upset
    "I shake my head, still smiling happily."
    bree.say "Uh-uh..."
    bree.say "You said I graduated from all of that, remember?"
    bree.say "Say...do you feel like an ice-cream?"
    bree.say "Because I could really go for one right now."
    show master upset blush
    "All this seems to do is press the old man's buttons even more."
    "And his face turns red as he rages at me, still trapped and helpless."
    show master angry at startle(0.1, 5)
    master.say "Ice-cream?"
    show master at vshake
    master.say "ICE-CREAM?!?"
    master.say "Of course I don't want any damn ice-cream!"
    show master upset
    bree.say "Suit yourself."
    bree.say "But I have to leave you while I go get myself one."
    bree.say "So how are we going to keep you safe while I'm gone?"
    "I scan the beach until I spot a kid's bucket that's been abandoned on the sand."
    bree.say "Perfect!"
    "Standing up, I walk over and grab it."
    "Then I return and place it straight over the old man's exposed head."
    show master surprised at startle(0.1, 5)
    master.say "What the..."
    show master_bucket zorder 1 at center, zoomAt(1.25, (600, 760)) with easeintop
    master.say "MMNGH...MMMNGH!"
    scene bg black
    show beach_icecream_bg
    show beach_icecream_seller
    show beach_icecream_seller_outfit
    show beach_icecream_breemc_01
    show beach_icecream_outfit_breemc_01_mc_swimsuit
    with fade
    "Satisfied that he'll probably still be there when I get back, I go to grab my ice-cream."
    "Then I take my own sweet time about strolling down the beach and eating at a leisurely pace."
    "By the time I'm walking back towards the place the master is buried, I can see his bucket."
    "And I can't help chuckling as people walk by it, not suspecting a thing."
    "Until they hear a burst of foul language coming from underneath."
    "Watching them jump in surprise and hurry off down the beach is enough to totally change my mood."
    scene bg black
    show beach_sandcastle_bg_02 at center, zoomAt(2.5, (640, 720))
    show master swimsuit normal noglasses at center, zoomAt(2.5, (640, 1720))
    show master_bucket zorder 1 at center, zoomAt(1.25, (600, 760))
    show beach_sandcastle_castle_02 zorder 2 at center, zoomAt(2.5, (680, 880))
    with fade
    "So by the time I make it back to him, I've completely forgotten about my previous irritation."
    bree.say "Okay, master..."

    if hero.morality >= 25:
        bree.say "I really hope that you're okay under there!"

    elif hero.morality <= -25:
        bree.say "Okay, let's get some air to this wrinkled old ball-bag!"
    else:
        bree.say "I think that's enough special resistance training for today."
    hide master_bucket with easeouttop
    "I lift the bucket of his head and pick up the spade."
    "Then I start to dig carefully around him, trying not to do him any harm in the act."
    "And to his credit, the old coot seems to have burnt off his own shitty mood too."
    "Because he looks genuinely relieved to see me, smiling up at me as I go to work."
    show master happy at startle(0.1, 5)
    master.say "Oh thank god!"
    show master talkative
    master.say "I thought for a moment that you weren't coming back."
    master.say "I thought that you were going to leave me here all night!"
    master.say "Because...well...because one of my former pupils really did to that to me."
    show master normal
    "As much as he can rub me up the wrong way, I can't help feeling sorry for the guy."
    "I mean, at times like this he looks so old and frail, like your dear old grandpa."
    bree.say "Of course I was always going to come back."
    bree.say "How would I live with myself if something bad happened to you?"
    "The master nods his head, beginning to wriggle now his shoulders are being freed."
    show master talkative at startle(0.1, 5)
    master.say "Yes, yes..."
    master.say "Of course you wouldn't - because you're a good girl."
    master.say "Why, you even thought to cover up my poor old head."
    master.say "Otherwise I'd have burned to a crisp in the sun!"
    show master normal
    "I raise my eyebrows as I consider his point."
    "At the time I only used the bucket to stick it to him."
    "But I guess he's right - that really was quite thoughtful of me!"
    "Soon enough the master's arms are free, and he starts to help dig himself out."
    scene bg beach at center, zoomAt(1.25, (490, 740)) with fade
    pause 0.3
    show master swimsuit noglasses at center, zoomAt(1.25, (640, 880)) with easeinbottom
    "Clawing away at the sand like an old dog, he tosses handfuls out of the hole."
    "And once his legs begin to emerge, he tugs them free too and scrabbles out onto the beach."
    "Then he makes a point of stretching and flexing, hopping from one foot to the other."
    "All the while his scrawny body makes sounds like that breakfast cereal."
    "The one that cracks and pops when you add the milk."
    "It looks particularly daft as the sun is beginning to set behind him."
    "And the contrast between the sublime and the ridiculous is plain to see."
    show master talkative at startle(0.1, 5)
    master.say "Aaah..."
    master.say "I can feel the benefits of that technique already..."
    master.say "It's reinvigorated me - taken years off my body!"
    show master normal
    "I'm sitting on the sand, watching him making a spectacle of himself."
    "And from here he looks as ancient and withered as ever."
    show master talkative at startle(0.1, 5)
    master.say "Part of that is because of you, my dear..."
    master.say "You know that, don't you?"
    show master normal
    bree.say "Huh?"
    bree.say "What are you talking about?"
    "Suddenly the master undergoes that same, weird transformation."
    "Right before my eyes he stops being a randy, deluded old fool."
    "And he becomes that humble, adorable grandfather figure behind all of the nonsense."
    show master talkative at startle(0.1, 5)
    master.say "Well it's true..."
    master.say "You make me forget how old I really am, my dear..."
    show master normal
    "He pauses to grimace as a pang somewhere along his spine interrupts his words."
    show master talkative at startle(0.1, 5)
    master.say "Argh..."
    master.say "Until my damn back has to go and remind me!"
    show master normal
    "I smile as I get to my feet, offering my arm to the master."
    "He takes it, waiting for me to tell him what I have in mind."
    bree.say "Come on, Master Grandpa..."
    bree.say "Let's go get you an ice-cream."
    bree.say "It'll take your mind off of your back, at least for a short while."
    "The old man nods happily, content to walk along the sand with me."
    "All thought of martial arts and silly rituals forgotten."
    "At least for the moment."
    scene bg black with dissolve
    $ master.flags.delay = TemporaryFlag(True, 2)
    return

label master_female_event_05:
    if master.love.max < 100:
        $ master.love.max = 100
    scene bg black
    show bg masterhouse at center, zoomAt(1.2, (600, 720))
    "I've been spending so much time with the master recently that when he invites me over for the evening, I don't hesitate to accept."
    "Normally I'd be more than a little hesitant to head over to a guy's place on my own and at the drop of a hat."
    "Not to mention the fact that I'm doing so as the sun is setting too, so I get there in the gloom of the night."
    "But the truth is that the bond between myself and the master is more than enough to make me feel perfectly at ease."
    "I mean sure, he's a pretty strange old guy, and I still think a lot of his so-called martial arts are complete bullshit."
    "Yet under all of that, he's shown me that he has a good heart, and we've slowly become more than teacher and pupil."
    "The very fact that he's asked me to keep on seeing him once the lessons were over speaks to that."
    "And I've started to see other sides to him that prove he's not just some weird old kook too."
    "Though I do have to admit that I'm curious as to just what he's got in mind for me tonight."
    "I've never been over to his place this late in the day before, and we normally only train in the daylight hours."
    "Part of me is expecting him to come howling out of the shadows and make me defend myself in a surprise sparring session."
    "But another wonders if I'm going to walk in on him preparing a typically imperfect candle-lit meal for the two of us."
    show bg masterhouse at traveling(1.4, 1, (750, 720))
    "And yet as I walk up to the door of his place, I find it slightly ajar."
    show master_aura at left, dark, zoomAt(1, (400, 720)) with dissolve
    "Plus there's the scent of something fragrant in the air and curls of smoke coming from inside."
    hide master_aura at center, dark, zoomAt(1, (750, 720)) with dissolve
    "Suddenly worried that the smoke might be coming from the beginnings of a fire, I hurry to open the door."
    play sound door_open
    show masterhouseinterior with fade

    if hero.morality <= 25:
        bree.say "Hey, old man?"
        bree.say "You okay in there?"
        bree.say "Because I'm not giving you the kiss of life!"
    else:

        bree.say "Master?"
        bree.say "Are you in there?"
        bree.say "Is everything okay?"
    show bg masterhouseinterior at traveling(1.2, 1, (660, 720))
    pause 1
    show bg masterhouseinterior at traveling(1.2, 1, (700, 720))
    pause 1
    show master noglasses at center, zoomAt(1.4, (640, 900)) with dissolve
    "As soon as I'm inside, I can't help feeling more than a little foolish."
    "Because now I can see that the smoke is coming from burning incense."
    "It's dotted all around the place in ornate holders."
    "And the scent I detected just now is obviously coming from it too."
    show master happy at startle(0.1, 5)
    master.say "Ah..."
    master.say "There you are, my dear."
    master.say "Your concern is appreciated."
    master.say "But as you can no doubt see, I am quite well."
    show master normal
    "Now that I'm inside of the old man's home cum dojo, I can see that he's right."
    "The lighting is suitably subdued, creating a mellow, meditative atmosphere."
    "And he's sitting cross-legged on the floor, a cushion between his ass and the floorboards."
    "Still feeling a little foolish, I walk the short distance to where he's sat."
    "And when I reach him, the master gestures for me to sit on a second cushion in front of his own."
    show master at startle(0.1, 5)
    show bg masterhouseinterior at startle(0.1, 5)

    if hero.morality >= 25:
        bree.say "Master, don't do that to me again!"
        bree.say "I was worried about you just now."

    elif hero.morality <= -25:
        bree.say "Don't do that to me again, you old goat!"
        bree.say "I don't need that kind of stress in my life."
    else:

        bree.say "Ah, yeah..."
        bree.say "I can see that now!"
    "The old man doesn't seem to me bothered in the slightest by my concern."
    show master at startle(0.1, 5)
    "In fact he makes a vague waving gesture with one open hand."
    "Like he's dismissing it without as much as a single thought."
    show master talkative at startle(0.1, 5)
    master.say "Now, now..."
    master.say "This is not the time for such petty concerns."
    master.say "True martial artists, like you and I..."
    master.say "We must engage with higher matters, physical and spiritual alike."
    show master normal
    "I find my eyebrows rising as I sit there listening to the old man."
    "Because I'm already waiting for him to make some kind of crude joke."
    "Or else to take the conversation in a totally lewd direction."
    show master talkative at startle(0.1, 5)
    "But instead he simply keeps on spouting what sounds like genuine mystical mantras."
    show master_aura zorder 1000 at center, zoomAt(1, (640, 720)), opacity(0.3)
    show master talkative
    "And it's only now that I'm beginning to notice he has a kind of glow about him too."
    show master_aura zorder 1000 at center, zoomAt(1, (640, 720)), opacity(0.6)
    show master talkative
    "Call me crazy, but tonight he really does look and sound like the real thing."
    show master_aura zorder 1000 at center, zoomAt(1, (640, 720)), opacity(1)
    show master talkative
    "Like he's transformed into a genuine personification of wisdom and enlightenment."
    "A suspicion which is only made stronger a moment later."
    show master surprised
    "When he instantly seems to tune into my sense of amazement."
    show master talkative at startle(0.1, 5)
    master.say "Is there something amiss, my dear?"
    master.say "You seem to be distracted this evening."

    if hero.morality >= 25:
        bree.say "That's so insightful of you, master!"
        bree.say "And that's what's bugging me too."
        bree.say "Just how focussed and transcendent you are!"

    elif hero.morality <= -25:
        bree.say "You could say that, yeah."
        bree.say "Normally you're all sleazy and gropy."
        bree.say "Did they finally put you on some kind of register?"
    else:

        bree.say "Well..."
        bree.say "It's you, master..."
        bree.say "You seem kind of different."
    show master happy at stepback(0.1, 3,0)
    pause 0.3
    show master happy at stepback(0.1, 3,0)
    pause 0.3
    "The master chuckles and shakes his head."
    "But his laughter feels more like fond amusement than derisive mocking."
    show master happy at startle(0.1, 5)
    master.say "Ah..."
    master.say "Most likely you are sensing the residual effects of my meditations."
    master.say "I have been deeply engrossed in them for a while now."
    master.say "Seeking the answers inside of myself to a most challenging concern."
    show master wink with dissolve
    pause 0.5
    show master normal at startle(0.1, 5)
    show bg masterhouseinterior at startle(0.1, 5)
    "I'm nodding as he tells me all of this."
    "Leaning in closer to hear all he has to say."

    if hero.morality >= 25:
        bree.say "You can confide in me, master!"

    elif hero.morality <= -25:
        bree.say "What's on your mind - is it juicy?"
    else:

        bree.say "What's bothering you?"
    show master whining at startle(0.1, 5)
    master.say "I must confess that it is the reason I asked you here tonight."
    master.say "A matter that I fear I cannot resolve without your help."
    master.say "For some time now I have been wrestling with something inside of me."
    master.say "Something deep down inside, that is only building in strength."
    master.say "And I know that one day, it must be freed!"
    show master sad
    "Almost within a heartbeat of the master saying the words, it happens."
    hide master_aura with dissolve
    show master surprised at hshake
    show bg masterhouseinterior at hshake
    "The calm, contemplative silence of the dojo is pierced by a tremendous sound."
    "Like the combination of an explosion and a tearing of flesh, it drowns out everything else."
    show master_aura at center, green, zoomAt(2, (640, 720)) with dissolve
    "And a moment later, the sweet scent of the incense is overwhelmed by something truly foul."
    "A stench like rotten eggs, bad breath and week-old garbage assaults my nostrils."

    if hero.morality >= 25:
        bree.say "Eww..."
        bree.say "I think I'm going to be sick!"

    elif hero.morality <= -25:
        bree.say "Ah fuck..."
        bree.say "That smells like a zombie's dick!"
    else:

        bree.say "Oh..."
        bree.say "Oh bloody hell!"
    show master afraid
    "As soon as I can keep myself from gagging at the awful smell, I look over at the master."
    "And the look of awkwardness on his face instantly explains the source of it all."
    show master whining at startle(0.1, 5)
    master.say "Erm..."
    master.say "Yes..."
    master.say "Sorry about that!"
    master.say "I have been sitting here for quite a while now."
    master.say "And certain things to tend to build up..."
    show master stuned
    hide master_aura with dissolve
    "All of a sudden, everything seems to slot into place."
    "The unexpected invitation, the meditative atmosphere and the talk of his struggles."

    if hero.morality >= 25:
        bree.say "That is totally disgusting, you know?"
        bree.say "Going to all that trouble to break wind in front of me!"

    elif hero.morality <= -25:
        bree.say "Honestly, I was expecting more from you."
        bree.say "Just dropping your guts at an inappropriate time's pretty lame!"
    else:

        bree.say "Yeah..."
        bree.say "That's a lot of trouble to go to just to fart in my presence!"
    "The old man is already waving his hand in the air again as I say this."
    "But at first I think he's just trying to waft away the lingering odor."
    "Because it seems to really have some staying power."
    "Hanging around stubbornly, like mustard gas in a trench."
    "It's only when she starts speaking that I realise he's actually trying to dismiss my reaction."
    show master surprised at startle(0.1, 5)
    master.say "No, no, no..."
    master.say "That was just a genuine case of bad timing, really it was!"
    master.say "Everything I said before it was the absolute truth."
    master.say "I've been wrestling with my feelings towards you, ever since you completed your studies under me."
    master.say "I feel as though we've become closer than ever - but I don't know what our roles are now!"
    show master normal
    "I can tell from the tone of the master's voice that he's being totally sincere."
    "And that knowledge makes the whole case of the flatulence just seem so silly."
    show master stuned at vshake
    show bg masterhouseinterior at vshake
    "I can't keep from bursting into laughter."
    "For a moment he simply stares at me in stunned silence."
    show master happy at vshake
    "But then he smiles and joins in, laughing with just as much helpless abandon."
    bree.say "Wow..."
    bree.say "I have to admit, I've been feeling the same way too."
    bree.say "Since we started to hang-out together and do more stuff."
    bree.say "So yeah...I get it."
    show master stuned
    "The master looks equal parts relieved and unsure."
    "The latter, I guess, because of the obvious question my answer poses."
    show master surprised blush with dissolve
    master.say "So..."
    master.say "You're not my student anymore."
    master.say "But I'd like to be more than your master."
    master.say "That is, if you'll have me?"
    show master blush normal
    menu:
        "Respond playfully":
            show master blush normal
            "Okay, that sounds pretty intense to me!"
            "And I admit that I don't know where this thing between us is going."
            "So while I want to find out, I also want to take it slowly too."

            if hero.morality >= 25:
                bree.say "I think that I want to see where this thing is going."
                bree.say "To see how it grows in a natural way, okay?"

            elif hero.morality <= -25:
                bree.say "Hey, I'm up for trying anything once!"
                bree.say "So let's keep it up and see what happens, yeah?"
            else:

                bree.say "What do you say we take it one step at a time?"
                bree.say "Keep doing what we've been doing and see where it takes us?"
            show master normal at startle(0.1, 5)
            "The master nods at this, seemingly satisfied."
            show master happy at startle(0.1, 5)
            master.say "You have a deal, [hero.name]."
            master.say "Let's see where this path will lead us!"
            $ master.love += 3
        "Respond sincerely":
            show master blush normal
            "Somehow I don't need to sit and think deeply about the question."
            "I just know that it's what I want too, that it feels right."

            if hero.morality >= 25:
                bree.say "Yes, I will!"
                bree.say "Because, in life, we should never want to stop learning."

            elif hero.morality <= -25:
                bree.say "Ah, what the hell!"
                bree.say "You'd just better be keeping some of the best lessons for last."
            else:

                bree.say "Of course I will!"
                bree.say "I feel like there's so much more you still have to teach me."
            "The master seems to be delighted with my answer."
            show master happy at startle(0.1, 5)
            "Nodding his head eagerly as I agree to his request."
            show master happy at startle(0.1, 5)
            master.say "Ah, the mists of my mind are beginning to clear!"
            master.say "I predict great things for us from this point onwards."
            $ master.love += 5
    scene bg black with dissolve
    $ master.flags.delay = TemporaryFlag(True, 2)
    return

label master_birthday_date_female:
    $ DONE["master_birthday_date_female"] = game.days_played
    scene bg street with fade
    "I'd been racking my brains, trying to figure out where I could take the Master for his birthday."
    "And I honestly think I'd gone through every possible place before I hit on what felt like the right one."
    "I discounted the cinema, because he gets handsy in the dark."
    "Going to a nightclub seemed like a bad idea, because I was worried he'd fall asleep."
    "A restaurant was out of the question, because I've seen him eating ramen - and it's not a pretty sight!"
    "But then I remembered where I like to go to relax and chill-out."
    "The pub - pretty much the perfect place to take the Master too."
    "There's food and drink, but nobody's expecting you to be all fancy about it."
    "Plus the place has lots of games that require skill and dexterity."
    "With his martial arts mastery, those should be no challenge for the old man."
    "So we agree to a date and a time."
    scene bg door pub with fade
    "Which is how I come to find myself standing outside the Winchester with him."
    show master casual noglasses at center, zoomAt(1.0, (840, 720)) with easeinright
    bree.say "Okay then..."
    bree.say "Welcome to my local, Master."
    bree.say "I hope you like it!"
    show master at center, traveling(1.25, 0.5, (640, 900))
    "The Master nods eagerly."
    "And I notice that he's digging something out of his pocket at the same time."
    show master happy
    master.say "I'm sure it will prove to be quite pleasant and agreeable, my dear."
    master.say "I have to admit that it's been a while since I frequented such an establishment."
    master.say "But have no fear, for I have come prepared!"
    show master normal
    "The Master holds up the item he's just retrieved from his pocket."
    "And I see that it's an ID card, complete with his photo."
    "Sure, his beard and moustache look shorter in it."
    "And maybe he's just a little less wrinkled than he appears now."
    "But it's definitely him."
    menu:
        "Make fun of the Master":
            "I shake my head and let out a chuckle of amusement."
            "All of which seems to puzzle the old man greatly."
            show master surprised
            master.say "Eh?"
            master.say "What's so amusing?"
            show master stuned
            bree.say "Like you don't know!"
            bree.say "The very idea they're going to check your ID!"
            show master upset
            "At this, the Master bristles."
            "His moustaches twitching as he curls his lip beneath them."
            show master angry
            master.say "It's not to prove that I'm old enough to drink!"
            show master talkative
            master.say "I need this to prove I'm eligible for an elderly person's discount!"
            master.say "Age has it's privileges."
            master.say "And discounted booze should be one of them!"
            show master normal
            "I do the best I can to stop myself laughing as he protests."
            "But in the end I have to simply hustle him inside."
            "I guess it figures."
            "The only time he'd admit his age is when it could get him a discount!"
            $ game.active_date.score += 10
        "Compliment the Master":
            "I nod my head, somehow managing not to laugh."
            "The very idea of him being asked for ID is ridiculous in the extreme!"
            bree.say "That's very conscientious of you, Master."
            bree.say "One can never be too careful."
            bree.say "But I'm sure your aura will prove your age."
            bree.say "So there'll be no need for them to see that."
            show master wink
            "At this the Master winks."
            "His moustaches twitching as his mouth curls into a smile below them."
            show master talkative
            master.say "It's not to prove that I'm old enough to drink!"
            master.say "I need this to prove I'm eligible for an elderly person's discount!"
            show master happy
            master.say "Age has it's privileges."
            master.say "And discounted booze should be one of them!"
            show master normal
            "The Master taps his nose in a conspiratorial manner."
            "Which I guess is supposed to clue me in on the supposed wisdom he's sharing."
            "I do the best I can to keep from laughing again."
            "And instead I hustle him inside."
            "I guess it figures."
            "The only time he'd admit his age is when it could get him a discount!"
            $ game.active_date.score += 20
    scene bg pub with fade
    pause 0.3
    show master casual normal noglasses at center, zoomAt(1.25, (640, 900)) with easeinright
    "As soon as we're through the doors, I feel a sense of relief wash over me."
    "There's just something so familiar and comforting about the place."
    "I really feel like I can relax here."
    show master talkative
    master.say "So..."
    master.say "Who's leg do I have to hump to get a drink around here?!?"
    show master normal
    "The sound of the Master's voice snaps me out of it."
    "And I remember why I brought him here in the first place."
    bree.say "Erm..."
    bree.say "That's not how things work around here, Master."
    bree.say "Let's go and order some drinks at the bar, okay?"
    show master happy
    "The old man nods happily, allowing me to lead the way."
    "And then he trundles after me, looking this way and that."
    "It's only when I reach the bar that I realise what he's actually doing."
    "The old goat is making sure to check out all the other girls in the place!"
    master.say "Mmm..."
    show master talkative
    master.say "I like the look of this place."
    master.say "I like it a lot!"
    show master normal
    "I'm about to say something to him."
    "But then the girl behind the bar pipes up first."
    "Barman" "Hey!"
    "Barman" "Don't I know you from somewhere?"
    "At the sound of her voice, the Master turns around."
    "He looks at the girl, straining his eyes as he does so."
    "But then he shakes his head."
    show master talkative
    master.say "I don't think so."
    master.say "Because I'd certainly remember you!"
    show master normal
    "I note that as he says this, the Master is basically looking at her cleavage!"
    "If the girl notices this at all, she doesn't say anything."
    "Instead she nods her head, looking more sure then before."
    "Barman" "Yeah, I recognise you now."
    "Barman" "Aren't you that dirty old man?"
    "Barman" "The one me and my friends caught spying on us?!?"
    "I can seem this is going to get ugly."
    "But I'm not sure what I should do about it."
    "I can see the girl's about to do something here."
    "And I have maybe a couple of seconds to act."
    menu:
        "Help the Master":
            "I can see he's not going to be able to get himself out of this."
            "So I decide to step in and help the Master out."
            bree.say "Erm..."
            bree.say "Excuse me..."
            "At the sound of my voice, the girl turns to face me."
            "Barman" "Huh?"
            "Barman" "What's this got to do with you?"
            "Barman" "Is he your grandpa or something?"
            bree.say "Ah...ha, ha..."
            bree.say "Not exactly!"
            bree.say "Anyway...he can't be the person you're talking about."
            "The girl frowns at this."
            "Barman" "Why the hell not?"
            bree.say "Well, you see this skin?"
            "I hold up the Master's scrawny arm."
            "And then I pinch his skin, stretching it a little."
            show master surprised
            master.say "Ouch!"
            show master stuned
            bree.say "Oh don't be such a big baby!"
            bree.say "Look, it's like paper it's so thin."
            bree.say "He's not allowed out in direct sunlight."
            bree.say "Or else he'd burn to a crisp."
            "The girl raises her eyebrows, her expression changing."
            "Barman" "Oh, so he's not allowed to go to the beach?"
            bree.say "Got it in one!"
            "Barman" "Okay, okay..."
            "Barman" "Sorry about all that."
            "I let out a sigh of relief."
            show master normal
            "And the Master looks like he's grateful too."
            "As I kind of just averted a potential disaster."
            $ game.active_date.score += 20
        "Stand back and watches":
            "I could step in and try to diffuse the situation."
            "But he is supposed to be the master, and I'm the pupil."
            "So shouldn't he be able to handle this all on his own?"
            "After all, it's not a fight - just a disgruntled barman_"
            show master surprised
            master.say "Erm..."
            master.say "No, no, no..."
            master.say "It wasn't me that saw you at the beach."
            show master perv
            master.say "I don't remember that tiny red bikini at all!"
            "The moment the words are out of his mouth, his fate is sealed."
            "I guess the memory of what he saw that day was just too much to handle."
            "Which is why he couldn't help blurting out that incriminating detail."
            "Barman" "So it WAS you!"
            "Barman" "You mean old creep!"
            "It's only now that I notice the girl's been doing something under the bar."
            "This whole time she's been filling a glass from the soda fountain."
            "And now she makes use of it, flinging the contents into the Master's face!"
            show master whining with vpunch
            master.say "Argh..."
            master.say "My eyes..."
            master.say "I'm blind!"
            show master sad
            bree.say "I don't think you are, Master."
            bree.say "That was just soda water."
            bree.say "Why don't you go and sit down?"
            bree.say "I'll handle getting us a drink."
            $ game.active_date.score -= 10
    show master normal
    "As soon as we have our drinks, the Master leans back in his chair."
    "And he lets out a strange kind of sigh that I've never heard from him before."
    "He seems to see the way I'm looking at him, and he nods his head with a smile."
    show master happy
    master.say "Am I doing it right?"
    show master normal
    bree.say "Well...I don't really know what you're doing."
    bree.say "So I can't say if you're doing it right or not."
    bree.say "Because I also don't know what right looks like."
    "The Master answers by making a gesture to his surroundings."
    show master surprised
    master.say "I mean do I look like I fit in around here?"
    master.say "I haven't been inside a public house is years."
    master.say "Do we have to start talking about football now?"
    master.say "Or would my breaking wind make things less awkward?"
    show master stuned
    bree.say "I can't imagine any way that would make things less awkward!"
    "The Master shrugs and makes a grunting noise."
    show master talkative
    master.say "If you insist, my dear..."
    master.say "Now what else is there to do around here?"
    master.say "We can't just sit on our rumps and drink!"
    show master normal
    "I can't help feeling more than a little put out by the comment."
    "As that's pretty much what I was planning on doing."
    "But it is the Master's birthday."
    "So I guess I should at least try to indulge him."
    if hero.has_skill("video_games") or master.love + hero.fitness >= 200:
        menu:
            "Play dartboard":
                "Pretty soon my eyes settle on the dartboard."
                "I have no idea if the old man can play the game."
                "But he's always going on about his martial arts skills."
                "So that has to count for something, right?"
                bree.say "Come on, Master..."
                bree.say "Let's play a game of darts."
                show master happy
                master.say "Ooh..."
                master.say "Now that does sound interesting."
                master.say "And something that I'd be good at too!"
                show master normal
                "I grab us two sets of darts from the bar, and we get ready to play."
                "I decide to go first, just so that I can show the Master how it's done."
                "So I take aim and get ready to throw my first dart..."
                show master surprised at startle
                master.say "OH MY GOD!"
                show master normal
                bree.say "Good try!"
                bree.say "But not good enough..."
                "I somehow manage to keep my cook as the old man shouts."
                "Which means that my throw remains true as the dart leaves my hand."
                "A fraction of a second later it thuds into the board."
                "And it lands right where I wanted to put it."
                "So I turn to face the Master with a look of triumph on my face."
                bree.say "Now then, you cheating rat!"
                bree.say "You did that on purpose!"
                bree.say "But more importantly, you tried to ruin my shot!"
                show master happy
                master.say "I have no idea what you mean!"
                master.say "I just saw something amazing out of the window."
                master.say "So absolutely astonishing that I had to remark on it."
                show master wink
                master.say "And...erm...would you believe it was so amazing that I instantly forgot what it was?"
                show master normal
                "I roll my eyes and do the best I can to ignore his blatant lie."
                show date pub dart master with fade
                "But my patience is paid back in full as the game goes on."
                "Just like he boasted, the Master is pretty good."
                "It's just that I'm better, and it soon starts to show."
                "By the end of the game, I've managed to soundly beat him."
                "Which is made that much sweeter by his failed attempts to sabotage my game."
                hide date pub dart with fade
                $ game.active_date.score += 20
            "Play game of pool":
                "Pretty soon my eyes settle on the pool table."
                "I have no idea if the old man can play the game."
                "But he's always going on about his martial arts skills."
                "So that has to count for something, right?"
                bree.say "Come on, Master..."
                bree.say "Let's play a game of pool."
                show master surprised
                master.say "Ooh..."
                show master happy
                master.say "Now that does sound interesting."
                master.say "And something that I'd be good at too!"
                show master normal
                "I grab two cues from the rack, pump the coins into the slot, and we get ready to play."
                "I decide to go first, just so that I can show the Master how it's done."
                "So I lean over the table, trying to line up my first shot..."
                bree.say "WHOA!"
                "I spin around as I feel something poke me in the ass."
                show master perv
                "Just in time to see the Master try to hide his cue behind his back!"
                show pool master with hpunch
                bree.say "Don't you dare do that again!"
                master.say "Do what, my dear?"
                master.say "I don't know what you mean!"
                bree.say "Oh yes you do."
                bree.say "And if you touch my ass with that cue again..."
                bree.say "Then I'll shove it up yours!"
                "The Master holds up his hands and backs off."
                "And it seems like my threat had the desired effect."
                "So I line myself up to take a second try at my shot."
                "As I do so, I go over my knowledge of angles and the like."
                "Basic trigonometry and all the associated formulas."
                "Because that's what pool comes down to in the end."
                "Knowing what angle to strike one ball at in order to affect another."
                "And as soon as the cue ball hits its target, I know I'm on good form."
                bree.say "Yes!"
                bree.say "I did it!"
                "In the game that follows, pretty much take the Master to the cleaners."
                "I mean, he tries his best and it's not like he's totally hopeless."
                "But there's just no way he can keep up with me."
                "And in the end I leave him far behind as I wrap it up."
                master.say "Hmm..."
                master.say "I don't think I like this game after all."
                master.say "No...not the kind of thing befitting a master of the martial arts."
                master.say "So you beating me is not really like beating me."
                master.say "Because the game is beneath me!"
                bree.say "Okay, Master..."
                bree.say "Whatever you say."
                hide pool master with fade
                $ game.active_date.score += 20
    else:
        bree.say "Hmm..."
        bree.say "There's always a pack of cards behind the bar."
        bree.say "So we could play Blackjack?"
        "The Master doesn't look to impressed with my suggestion."
        "He makes a huffy noise and shakes his head, almost like a petulant child."
        show master angry
        master.say "A card game?"
        master.say "How vulgar!"
        show master talkative at center, traveling(1.5, 0.3, (640, 1060))
        master.say "Why don't we have an arm-wrestling contest?"
        show master normal
        "The Master's own suggestion gets a similar reaction from me."
        "As I can't help shaking my head at the mere idea of it."
        bree.say "Arm-wrestling?"
        bree.say "Are you serious?!?"
        menu:
            "Insist on playing Blackjack":
                "I take one look at the Master's arms and shake my head."
                "Those things look like strings of spaghetti with knots in the middle!"
                bree.say "Sit tight, okay?"
                bree.say "I'm going to go grab the cards."
                show master whining
                "The Master opens his mouth to protest."
                show master sad
                "But then he seems to see that it's futile."
                "And so he just sits there and sulks instead."
                "As soon as I return with the cards, I get straight down to it."
                "Taking the cards out of the box, I shuffle them and then deal."
                "It doesn't take me long to explain the rules to the Master."
                "And it seems to take him even less time to start cheating."
                "I lose track of the times I have to call him out on it."
                "But all the same we seem to end up about equal in terms of wins."
                "Yet perhaps the biggest win for me is that it kept him out of trouble for a while."
                $ game.active_date.score -= 10
            "Agree to an arm-wrestling contest":
                "I take one look at the Master's arms and nod my head."
                "Those things look like strings of spaghetti with knots in the middle!"
                "There can't be any strength in them at all."
                bree.say "Okay, Master..."
                bree.say "Let's see what you've got!"
                show master happy at center, traveling(1.85, 0.3, (640, 1280))
                "The Master's face lights up."
                "And he plants his elbow on the table in front of me."
                show master talkative
                master.say "Now then, my dear..."
                master.say "Don't feel like you have to hold back."
                master.say "I may appear to be an old man."
                master.say "But I assure you that my years of..."
                show master normal
                "Without waiting, I grab the Master's hand."
                show master surprised with vpunch
                "And then I slam it down onto the table."
                master.say "Aargh!"
                show master sad
                bree.say "Yeah!"
                bree.say "I win!"
                show master whining
                master.say "I...I wasn't ready!"
                show master talkative
                master.say "How about best two out of three?"
                show master normal
                bree.say "I guess so."
                "This time we both square up on the table."
                "And then we go when the Master gives me a nod."
                show master surprised
                master.say "Urgh..."
                show master stuned with vpunch
                bree.say "Yes!"
                "Again the back of his hand slams down onto the table."
                master.say "Hmm..."
                show master whining
                master.say "I don't think I like this game after all."
                show master talkative
                master.say "No...not the kind of thing befitting a master of the martial arts."
                master.say "So you beating me is not really like beating me."
                show master happy
                master.say "Because the game is beneath me!"
                show master normal
                bree.say "Okay, Master..."
                bree.say "Whatever you say."
                $ game.active_date.score += 20
    show master normal at center, zoomAt(1.5, (640, 1060)) with fade
    "After the game, the Master seems to be a little more subdued."
    "Almost like he's in the mood for something a bit more relaxed."
    "That is until he casts a questioning glance in my direction."
    show master talkative
    master.say "So, my dear..."
    master.say "Do you have something to present to me?"
    master.say "Maybe a little token of appreciation to mark my birthday?"
    show master normal
    if not hero.has_gifts:
        "Damn it!"
        "I knew there was something I'd forgotten."
        "Looks like I'm going to have to lie my way out of this one."
        bree.say "If by gift, you mean something that will enhance your existence..."
        bree.say "Then my gift to you is to be the very best student you ever had!"
        show master sad
        "The Master frowns at this, grumbling to himself."
        "And he shakes his head, showing his disapproval."
        show master whining
        master.say "Urgh..."
        master.say "The old 'gift of Karma' excuse!"
        master.say "Something I can't eat or drink."
        master.say "And something that definitely won't let me put my hand inside it's panties!"
        $ game.active_date.score -= 20
        $ master.love -= 10
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_33
        if _return != "done":
            if _return != "None" and _return != "exit":
                "I should have known that was coming!"
                "But luckily for me I remembered to get the old man a gift."
                "And so I don't hesitate to pull it out and hand it over."
                show master happy
                "The Master's face lights up as he takes it from me."
                play sound [paper_ripping_1, paper_ripping_2]
                "But once he starts to tear off the wrapping paper, I see his expression change."
                bree.say "What's the matter, Master?"
                bree.say "Is there something wrong with your gift?"
            if _return:
                show master happy
                "The Master's eyes are so wide by now I think they're going to pop out of his head."
                "And as soon as he has the gift unwrapped, he goggles at it in what looks like sheer amazement."
                show master talkative
                master.say "I...I never thought I'd own one of these!"
                master.say "How could you have known?!?"
                show master normal
                bree.say "Oh, I don't know..."
                bree.say "Would you believe it was a lucky guess?"
                $ game.active_date.score += 20
            else:
                show master sad
                "The Master makes a muttering sound as he finishes unwrapping the gift."
                "And then he plonks it down on the table in front of him, shaking his head."
                show master whining
                master.say "Not a very inspired choice, my dear."
                master.say "I'd suggest that you try harder next time!"
                show master sad
                bree.say "Erm..."
                bree.say "Thanks for being honest..."
                $ game.active_date.score -= 10
    show master normal
    "By now the Master is starting to look a little worse for wear."
    "We've had more than a few rounds, and I'm wondering if he can hold his booze."
    "I've made a point of slowing down my own drinking in order to keep an eye on him."
    "But he's still downing his own drinks at an alarming rate."
    "And when he finishes the one he's currently on, he slams it down on the table."
    show master happy
    master.say "Aah!"
    master.say "Time for another round?"
    show master normal
    menu:
        "Agree to another round":
            "I suppose one more round couldn't hurt."
            "He's probably already as drunk as he's going to get."
            "So what difference is it going to make?"
            bree.say "Okay, Master..."
            show master happy
            bree.say "Leave it to me."
            "I hurry over to the bar and order another round of the same."
            show drink pub master casual with fade
            "And then I put the Master's glass down in front of him."
            "He reaches for it without hesitation, raising it straight to his lips."
            bree.say "You might want to make that one last, Master."
            bree.say "I think you're a little..."
            master.say "Aah!"
            master.say "Urp..."
            master.say "Oops!"
            "I watch in horror as the Master downs the drink in one go."
            "Then slams the glass down on the table and lets out a massive belch."
            "The after effects are almost as instant and impressive too."
            "Because then his eyes roll back into his head."
            "And he topples off of his chair!"
            "I hurry over to pick him up off the floor."
            "Feeling the eyes of everyone in the place on me as I do so."
            $ game.active_date.score += 20
        "Decide the Master has had enough":
            "I think it's about time someone cut the old man off."
            "Heaven knows how much he drinks on a normal occasion."
            "But right now he looks like he's on the verge of passing out."
            bree.say "Okay, Master..."
            show master happy
            "The Master's face lights up as he hears me say the words."
            "Obviously thinking that I'm agreeing to his suggestion."
            bree.say "I think that's quite enough for you."
            bree.say "Time to switch to something non-alcoholic."
            show master sad
            "Of course the Master's expression now turns into a grimace."
            "And he narrows his eyes at me."
            show master whining
            master.say "A good pupil would obey her master..."
            master.say "Especially on his birthday!"
            show master sad
            bree.say "Oh yeah?"
            bree.say "And a good master wouldn't exploit his pupils like that!"
            bree.say "So you'd better start sobering up, old man!"
            $ game.active_date.score -= 10
    scene bg pub
    show master casual blush normal noglasses at center, zoomAt(1.25, (640, 900))
    "By the time we're ready to leave the pub, the Master is pretty pickled."
    show master at center, traveling(1.85, 0.5, (640, 1280))
    "I have to help him up and sling his arm over my shoulder as we walk to the door."
    show bg street with fade
    "And as soon as the fresh air hits him outside, his legs seem to buckle under him."
    bree.say "Whoa!"
    bree.say "At least try to stand up, yeah?"
    show master talkative
    master.say "What are you talking about?"
    master.say "I'm finely perfect!"
    show master normal
    "I look around, beginning to think about calling a cab."
    "But then it occurs to me that the Master might not be ready to call it a night."
    bree.say "So..."
    bree.say "What's it going to be, huh?"
    bree.say "You want to go home or stay out a little longer?"
    if game.active_date.score >= 80 and master.sexperience >= 1:
        "At the mere mention of going on, the Master seems to perk up."
        "He raises his head and then begins to nod it eagerly."
        bree.say "Of course, my dear..."
        show master happy
        bree.say "There's still life in me yet!"
        bree.say "After all, bed's for sleepy people."
        bree.say "Let's get a kebab and go to a disco!"
        "I nod and do the best I can to keep the Master on his feet."
        "But I have no idea where we're going to go."
        "Or exactly what we can do with him in this state."
        "I guess I'll just have to think of something along the way."
        call master_birthday_sex_female from _call_master_birthday_sex_female
    else:
        "The Master shakes his head and groans."
        show master whining
        master.say "Urgh..."
        master.say "There must have been something in that last drink."
        master.say "I feel like my strength has been drained away!"
        show master sad
        bree.say "Erm..."
        bree.say "Does that mean you want to go home?"
        show master happy
        master.say "YES!"
        master.say "Send me home, my dear!"
        show master normal
        show bg taxi car
        with fade
        "It takes a while for me to flag down a taxi."
        "Because most of the drivers seem unwilling to take the Master."
        "And in his current state, I can't say that I blame them."
        "Eventually one does pull over and I bundle him into the back seat."
        scene bg taxi with fade
        "As the taxi drives away, I reflect that maybe this wasn't such a great idea."
        "Maybe next time I should take him somewhere without alcohol..."
    return

label master_birthday_sex_female:
    "Since the Master told me that today's his birthday, I've been trying to make it special for him."
    "And what better way to end it than with something that's sure to be right up the old goat's street?"
    $ game.room = "bedroom4"
    scene bg bedroom4
    show master
    with fade
    "So I make a point of bringing him back to my place and then sneaking him upstairs to my bedroom."
    master.say "Ooh..."
    master.say "Your house is very fancy, my dear..."
    master.say "The décor is not to my taste, but I suppose it's rather nice."
    "I can't help frowning as I open the door to my room and usher him inside."
    "Because it sounds to me like he's trying to make small-talk, and that he's not very good at it."
    if hero.morality >= 25:
        bree.say "Erm...yes, Master - thank you!"
    elif hero.morality <= -25:
        bree.say "Are you seriously telling me you give a crap?"
    else:
        bree.say "Since when are you interested in interior design?"
    "I'm pretty much hustling the Master in through the door as I say this to him."
    "And he hops over the threshold like I jabbed him with a taser or something."
    "All of which is beginning to clue me into what the actual problem might be."
    "In short, I think he's pretty nervous!"
    master.say "Oh..."
    master.say "Oh no, my dear..."
    master.say "I was just...trying to make small-talk, that's all!"
    "Sensing the need to take the lead, I put a pleasant smile on my face."
    "And then I take hold of the Master's hand, gently leading him over to my bed."
    "This seems to do the trick, making him break out into a pleasant smile."
    "In fact he looks like he's kind of spellbound as I guide him down onto the mattress."
    "He just keeps on gazing up at me, grinning the whole time."
    "And part of me is getting worried that he might be having some kind of funny turn."
    if hero.morality >= 25:
        bree.say "Are you okay, Master?"
        bree.say "Just nod if you are."
    elif hero.morality <= -25:
        bree.say "Is there anyone in there?"
        bree.say "Nod if you want to see boobies!"
    else:
        bree.say "Hello, Earth to the Master?"
        bree.say "Nod if you can hear me."
    "That seems to do the trick, as the old man nods his head slowly."
    "As it looks like that's the best I'm going to get, I take it as my cue to get undressed."
    "Now normally I'd be inclined to make that at least a little part of the show too."
    "But under the circumstances, I'm worried about him being able to take it."
    "So instead I keep things simple, removing my clothes at a slow pace."
    "And letting him see everything that happens along the way too."
    "Even with me being so careful, the sight of me stripping seems to have an effect."
    "The Master sits there, happily watching me as each item of clothing comes off."
    "And more than once I feel the temptation to toss something his way."
    "But then I remember my previous misgivings, and drop the item of clothing onto the floor instead."
    "Once I'm completely naked, I kneel down in front of him and start to take off his clothes too."
    "The Master still seems to be totally stunned by what's happening to him."
    "Which means that he offers no resistance to my efforts."
    "And the fact he only wears a shirt and a pair of shorts makes it a simple task too."
    "But the moment his shorts come down, I can't keep myself from giggling."
    "Because his cock instantly pops up, as stiff as a board and swaying from side to side."
    master.say "I...I..."
    master.say "I'm ready for action - as always!"
    if hero.morality >= 25:
        bree.say "Oh yes, Master - I can certainly see that!"
    elif hero.morality <= -25:
        bree.say "Hah...I can see that!"
    else:
        bree.say "You don't say!"
    "I'm crawling forwards as I say this, eyeing it up with obvious intent."
    "And for all of his bravado, the Master starts to back away from me as I do so."
    "He scuttles backwards and onto the bed, heading for the pillows."
    "And he only stops when there's nowhere else to go, landing on his back."
    "Now that my blood's up, I can't stop to think about being gentle with him."
    "I've seen how healthy and vital his manhood looks now."
    "And to me it seems like one that could belong to a guy a quarter of his age."
    "So yeah, I want it badly - I want it in me!"
    scene bg black
    show master cowgirl
    with fade
    "As the Master is laid out on his back, I straddle him, cowgirl style."
    "And in doing so, I pin his scrawny frame to the mattress."
    master.say "R...remember what I taught you, my dear..."
    master.say "Use all of your skills for the challenge ahead, yes?"
    master.say "Because I'll know if you're holding anything back!"
    "I can't help chuckling to myself as the old man issues his challenge."
    "Because I can hear the trepidation in his voice as he does so."
    "And I know full well that I'm the one in charge now."
    "So rubbing a hand up and down the shaft of his cock, I steer it between my thighs."
    "Preparing to give him the best birthday present humanly possible."
    menu:
        "Fuck pussy":
            "Lowering myself into position, I let the head of his cock lightly brush the lips of my pussy."
            "And the sound that he makes is more than enough to encourage me to go further still."
            "It's a combination of a gasp and a cry of sheer joy, as his mouth opens wide."
            call check_condom_usage (master) from _call_check_condom_usage_159
            master.say "Oh..."
            master.say "Oh my goodness!"
            "I keep chuckling to myself as the Master shudders beneath me, unable to resist my attentions."
            "And it makes such a change to the usual form his lessons take, where he's in charge and I follow his lead."
            "All the time he's nodding and urging me on, yet he remains laid out on his back while I have him pinned down."
            "But it's not like I need his encouragement, as things are already going just as I planned."
            "With every pass that the head of his cock makes over my lips, I can feel myself beginning to melt."
            "The muscles of my body relaxing as the feelings of pleasure and anticipation increase."
            "Soon enough I can hear the sound of my own breathy gasps over the Master's moans."
            "Then, little by little, I feel the sensation of myself opening to him down there."
            "I'm sure to take things as slow as I possibly can, drawing it out so that the moment lasts."
            "And the result is that everything I'm feeling is that much more intense."
            "I must be taking him into me no more than half an inch at a time."
            "And even with his generous size, that can't take too long to get done."
            "Yet to me it feels like an eternity as he gradually fills me all the way."
            show master cowgirl at startle(0.05, -10)
            "Once he can't go any deeper, I take a moment to savour the feeling."
            "Then, without warning, I leap into action, pushing down hard from above."
            "The Master's eye pop open and he looks like he's been woken from a deep sleep."
            master.say "Urgh!"
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "Before he can form an actual word, I'm moving again."
            "This time rising upwards as far as I can go, then plunging down a second time."
            "But now I'm not pausing or giving him the chance to recover."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "Oh no, now I'm riding him as hard as I dare, and for all he's worth."
            "I keep on moving, watching as his wiry muscles tense and twinge."
            "And I have to give the old goat credit, he seems to be as fit as he's always claiming."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "Which is a definite relief, as I feel myself begin to pick up speed."
            "Part of me wishes that I had a cowboy hat to hand for what I'm doing."
            "So that I could use it to whip the Master, to urge him to go faster and harder still."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "As it is, I have to rely on the motions of my own body to make that happen."
            "Even though my legs are bent, it feels like I'm almost jumping up and down."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "The sound of the mattress and the bedframe creaking beneath us is getting ever louder."
            "And part of me is starting to get a little worried that it might give way."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "Glancing around, I take my eyes off the Master for a moment."
            "But when I look back, I'm alarmed to see that his eyes have rolled back into his head."
            "Worse, there's a thin trickle of blood coming from one of his nostrils!"
            if hero.morality >= 25:
                bree.say "Oh no..."
                bree.say "Master, are you okay?"
            elif hero.morality <= -25:
                bree.say "Fucking hell..."
                bree.say "I thought that only happened in manga!"
            else:
                bree.say "Oh shit..."
                bree.say "Have I killed him?!?"
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "I'm so distracted that I don't notice a strange sensation coming from beneath me."
            "It's like an odd rumbling, as if I'm sitting on something that's shaking."
            "And it's only when I look down that I realise what's actually going on."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "Because the Master's entire lower half is jiggling and writhing."
            "His skinny legs are jerking on the bed, his groin practically vibrating."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "All of which can mean only one thing."
            bree.say "Aargh..."
            bree.say "The old codger's about to blow!"
            menu:
                "Let him cum inside" if CONDOM:
                    "Knowing that we remembered to use a condom, I don't have to worry about anything."
                    with vpunch
                    "Well, that is apart from holding on as the Master explodes inside of me a moment later."
                    with vpunch
                    "And it really does feel like an explosion, as I'm swept along with him."
                    with vpunch
                    "There's no way that I can resist being made to cum a second later."
                    "The sensation so intense that it's all I can do to stay upright!"
                "Let him cum inside" if not CONDOM:
                    with vpunch
                    "The Master explodes inside of me, and there nothing I can do to hold back."
                    with vpunch
                    "And it really does feel like an explosion, as I'm swept along with him."
                    with vpunch
                    "There's no way that I can resist being made to cum a second later."
                    "The sensation so intense that it's all I can do to stay upright!"
                "Pull out":
                    "The last thing that I manage to do before my own orgasm hits is to lift myself as high as I possibly can."
                    with vpunch
                    "Then I feel him sliding out of my pussy, gasping as the sensation adds to what he's already feeling."
                    with vpunch
                    "And I only just manage it before the Master explodes beneath me, everything he has to give hitting my belly and thighs."
                    with vpunch
                    "There's no way that I can resist being made to cum a second later."
                    "The sensation so intense that it's all I can do to stay upright!"
        "Fuck ass":
            "Lowering myself into position, I let the head of his cock lightly brush between my buttocks."
            "And the sound that he makes is more than enough to encourage me to go further still."
            "It's a combination of a gasp and a cry of sheer joy, as his mouth opens wide."
            master.say "Oh..."
            master.say "Oh my goodness!"
            "I keep chuckling to myself as the Master shudders beneath me, unable to resist my attentions."
            "And it makes such a change to the usual form his lessons take, where he's in charge and I follow his lead."
            "All the time he's nodding and urging me on, yet he remains laid out on his back while I have him pinned down."
            "But it's not like I need his encouragement, as things are already going just as I planned."
            "With every pass that the head of his cock makes around my hole, I can feel myself beginning to melt."
            "The muscles of my body relaxing as the feelings of pleasure and anticipation increase."
            "Soon enough I can hear the sound of my own breathy gasps over the Master's moans."
            "Then, little by little, I feel the sensation of myself opening to him down there."
            "I'm sure to take things as slow as I possibly can, drawing it out so that the moment lasts."
            "And the result is that everything I'm feeling is that much more intense."
            "I must be taking him into me no more than half an inch at a time."
            "And even with his generous size, that can't take too long to get done."
            "Yet to me it feels like an eternity as he gradually fills me all the way."
            show master cowgirl at startle(0.05, -10)
            "Once he can't go any deeper, I take a moment to savour the feeling."
            "Then, without warning, I leap into action, pushing down hard from above."
            "The Master's eye pop open and he looks like he's been woken from a deep sleep."
            master.say "Urgh!"
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "Before he can form an actual word, I'm moving again."
            "This time rising upwards as far as I can go, then plunging down a second time."
            "But now I'm not pausing or giving him the chance to recover."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "Oh no, now I'm riding him as hard as I dare, and for all he's worth."
            "I keep on moving, watching as his wiry muscles tense and twinge."
            "And I have to give the old goat credit, he seems to be as fit as he's always claiming."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "Which is a definite relief, as I feel myself begin to pick up speed."
            "Part of me wishes that I had a cowboy hat to hand for what I'm doing."
            "So that I could use it to whip the Master, to urge him to go faster and harder still."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "As it is, I have to rely on the motions of my own body to make that happen."
            "Even though my legs are bent, it feels like I'm almost jumping up and down."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "The sound of the mattress and the bedframe creaking beneath us is getting ever louder."
            "And part of me is starting to get a little worried that it might give way."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "Glancing around, I take my eyes off the Master for a moment."
            "But when I look back, I'm alarmed to see that his eyes have rolled back into his head."
            "Worse, there's a thin trickle of blood coming from one of his nostrils!"
            if hero.morality >= 25:
                bree.say "Oh no..."
                bree.say "Master, are you okay?"
            elif hero.morality <= -25:
                bree.say "Fucking hell..."
                bree.say "I thought that only happened in manga!"
            else:
                bree.say "Oh shit..."
                bree.say "Have I killed him?!?"
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "I'm so distracted that I don't notice a strange sensation coming from beneath me."
            "It's like an odd rumbling, as if I'm sitting on something that's shaking."
            "And it's only when I look down that I realise what's actually going on."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "Because the Master's entire lower half is jiggling and writhing."
            "His skinny legs are jerking on the bed, his groin practically vibrating."
            show master cowgirl at startle(0.05, -10)
            pause 0.2
            show master cowgirl at startle(0.05, -10)
            "All of which can mean only one thing."
            bree.say "Aargh..."
            bree.say "The old codger's about to blow!"
            menu:
                "Let him cum inside":
                    with vpunch
                    "The Master explodes inside of my ass, and there nothing I can do to hold back."
                    with vpunch
                    "And it really does feel like an explosion, as I'm swept along with him."
                    with vpunch
                    "There's no way that I can resist being made to cum a second later."
                    "The sensation so intense that it's all I can do to stay upright!"
                "Pull out":
                    "The last thing that I manage to do before my own orgasm hits is to lift myself as high as I possibly can."
                    with vpunch
                    "Then I feel him sliding out of my ass, gasping as the sensation adds to what he's already feeling."
                    with vpunch
                    "And I only just manage it before the Master explodes beneath me, everything he has to give hitting my belly and thighs."
                    with vpunch
                    "There's no way that I can resist being made to cum a second later."
                    "The sensation so intense that it's all I can do to stay upright!"
    "Once it's all over, I feel the urge to make some kind of sarcastic comment."
    "To joke about how the circle is complete, and now I'm the master, not the student."
    "But I'm way too exhausted to be able to do any of that right now."
    show cuddle master with fade
    "So instead I just roll off the Master and land heavily on the mattress."
    "Not knowing if I'll be able to rise again or pass out completely."
    scene bg black with dissolve
    pause 0.3
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
