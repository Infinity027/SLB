init python:
    
    Event(**{
        "name": "scottie_female_event_01",
        "priority": 500,
        "label": "scottie_female_event_01",
        "conditions": [
            MinDaysPlayed(7),
            HeroTarget(
                IsGender("female"),
                IsRoom("livingroom")
                ),
            PersonTarget(sasha,
                IsPresent(),
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "scottie_female_event_02",
        "label": "scottie_female_event_02",
        "conditions": [
            IsDone("scottie_female_event_01"),
            HeroTarget(IsGender("female")),
            PersonTarget(scottie,
                IsPresent(),
                Not(IsHidden()),
                Not(IsFlag("delay")),
                MinStat("love", 20),
                ),
            ],
        "do_once": True,
        "quit": False,
        })
    
    Event(**{
        "name": "scottie_female_event_03",
        "label": "scottie_female_event_03",
        "conditions": [
            IsDone("scottie_female_event_02"),
            HeroTarget(IsGender("female"),
                       Or(
                           HasRoomTag("street"),
                           IsRoom("alley"),
                           ),
                       ),
            PersonTarget(scottie,
                Not(IsHidden()),
                Not(IsFlag("delay")),
                Not(IsActivity("sleep")),
                MinStat("love", 40),
                ),
            ],
        "do_once": True,
        "quit": False,
        })
    
    Event(**{
        "name": "scottie_female_event_04",
        "label": "scottie_female_event_04",
        "conditions": [
            IsDone("scottie_female_event_03"),
            HeroTarget(IsGender("female")),
            PersonTarget(scottie,
                Not(IsPresent()),
                Not(IsHidden()),
                ContactKnown(),
                Not(IsActivity("sleep")),
                MinStat("love", 60)
                ),
            ],
        "do_once": True,
        "quit": False,
        })
    
    Event(**{
        "name": "scottie_female_event_05",
        "label": "scottie_female_event_05",
        "conditions": [
            IsDone("scottie_female_event_04"),
            HeroTarget(IsGender("female"),
                       IsRoom("nightclub", "nightclubbar")),
            PersonTarget(scottie,
                Not(IsHidden()),
                Not(IsFlag("delay")),
                MinStat("love", 80),
                ),
            ],
        "do_once": True,
        "quit": False,
        })
    
    Event(**{
        "name": "scottie_female_event_06",
        "label": "scottie_female_event_06",
        "conditions": [
            IsDone("scottie_female_event_05"),
            HeroTarget(IsGender("female"),
                       ),
            PersonTarget(scottie,
                OnDate(),
                Not(IsFlag("delay")),
                MinStat("love", 100),
                ),
            InInventory("sexy_date_equip"),

            ],
        "do_once": True,
        "quit": False,
        })
    
    
    Event(**{
        "name": "scottie_preg_talk",
        "label": "scottie_preg_talk",
        "conditions": [
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                IsFlag("pregnancy_father", "scottie"),
                Or(
                    MinCounter("pregnant", 60),
                    IsFlag("foundpreg"),
                    ),
                ),
            PersonTarget(scottie,
                IsPresent(),
                Not(IsHidden()),
                IsFlag("toldpreg", False),
                MinStat("sexperience", 1),
                ),
            ],
        "do_once": False,
        })
    
    
    
    Event(**{
        "name": "scottie_kiss_me_female",
        "label": "scottie_kiss_me_female",
        "max_girls": 1,
        "conditions": [
            HeroTarget(IsGender("female")),
            PersonTarget(scottie,
                IsPresent(),
                Not(IsHidden()),
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
        "name": "scottie_find_out_pregnancy",
        "label": "scottie_find_out_pregnancy",
        "conditions": [
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                MinCounter("pregnant", 30),
                CounterChanceChecker("pregnant", 50)
                ),
            PersonTarget(scottie,
                IsPresent(),
                Not(IsHidden()),
                IsFlag("toldpreg", False),
                MinStat("sexperience", 1),
                ),
            ],
        "do_once": False,
        })

label scottie_female_event_01:
    scene bg livingroom
    "Sitting slumped on the sofa, all I want to do is zone out and watch some TV."
    "I thought that I was alone in the house, until I hear the usual loud music and stomping that tells me Sasha's home too."
    "I grab the remote and turn up the TV in the hope of drowning her out, but then I hear an equally loud noise from the hallway."
    play sound door_banging
    "It sounds like someone knocking really hard on the door, for some reason ignoring the bell."
    "I'm not expecting any visitors, but I doubt Sasha can even hear herself think over her music."
    "Rather than start a yelling match, I reluctantly haul myself up and slope towards the front door."
    bree.say "All right, all right - I'm coming already!"
    show bg house
    show scottie casual
    with wiperight
    "I open the door, only to be confronted by a raised fist that stops within an inch of my surprised face."
    show scottie surprised at startle
    scottie.say "Huh?"
    bree.say "Fucking hell!"
    show scottie blush
    scottie.say "Oh...erm...sorry, I guess."
    show scottie embarrassed
    bree.say "Yeah, you'd better be - who in the hell are you and what do you want?!?"
    "The owner of the fist is a suddenly nervous-looking guy in a baseball cap, band T-shirt and shorts."
    "His long blonde hair is gathered in a scruffy ponytail and I notice he's quite well-built into the bargain."
    "The look on his face going from mad to unsure makes me think he's probably not the sharpest tool in the box."
    show scottie blush
    scottie.say "Well...I guess I want to know if Sasha's in...is she?"
    "That answers a lot of questions."
    "If this guy had a label, it'd read 'Sasha's Ex' and be plastered all over him."
    show scottie casual normal
    "I'm about to yell that she has a visitor, when I hear the sound of Sasha's door opening behind me."
    sasha.say "Jesus, Scottie - what part of 'fuck off and don't come back' don't you understand?"
    scene bg livingroom
    show sasha casual angry
    with fade
    pause 0.2
    show scottie casual normal at center, zoomAt(1.0, (1040, 730)) with moveinright
    "Scottie seems to take this as an invitation to come inside, and I step neatly aside to clear his path to the apparent object of his intentions."
    show sasha annoyed at left
    show scottie casual normal at right
    with move
    scottie.say "I know what that means, Sasha - I'm not as dumb as I look!"
    "I try not to laugh at the implications of what Scottie just said."
    show scottie casual angry
    scottie.say "I don't get how you think you can just dump me like this, you mean bitch!"
    show sasha casual normal
    sasha.say "What's to get?"
    sasha.say "We had a fling, I got bored and I dumped your stupid ass - that's it."
    scottie.say "You're some cold whore!"
    sasha.say "Yeah, whatever - but this is one cold whore that's through putting up with your shit."
    show scottie at right4 with move
    "Scottie scowls at Sasha, and for a moment I wonder if he's going to take a swing at her."
    "Then I wonder if Sasha's assuming I'll help her if he does!"
    show scottie b sad at right5 with move
    "But then he pauses and an odd look comes over his face as he does so."
    "It takes me a moment to realise what's happening, but it actually looks like he's making a visible effort to think."
    scottie.say "Well forget you, bitch - I can get myself some action just like that."
    "He tries to click his fingers, fails on the first attempt and then manages a half-snap on the second."
    "Then he turns to me, what I suppose he thinks constitutes a suave smile spreading across his face."
    show scottie b casual happy at center with move
    scottie.say "Hey there!"
    "Is he actually dumb enough to try hitting on me, right here and in front of Sasha after that messy verbal exchange?"
    show scottie normal
    scottie.say "I didn't catch your name before - what is it?"
    bree.say "You mean before when you almost punched me in the face?"
    scottie.say "Yeah, that's right - so what's your name?"
    show scottie at right
    show sasha casual annoyed at left5
    with move
    sasha.say "Urrgh...this is [hero.name], my housemate."
    sasha.say "And I don't think her type is a slobbering ape like you!"
    show sasha normal
    "Suddenly they're both looking at me, waiting for me to take a side."
    menu:
        "Shoot him down":
            "Though he's not bad-looking and too dumb to know he's dumb, I'm still pretty pissed at him barging in here like a blind bull."
            bree.say "I'm sorry, are you actually asking me what I think of you?"
            "Scottie nods, seemingly confused at the notion of being asked a question about a question."
            bree.say "You might have made a better impression if you hadn't come round here, bellowing and letting your cock do all the thinking for you."
            bree.say "Worse still, underneath all of the bravado, you're really just coming crawling back after Sasha dumped you."
            bree.say "Pretty pathetic, all in all."
            show scottie happy
            scottie.say "Erm...does that mean you like me or not?"
            bree.say "Only if I could find some use for a pitiable moron that has to let his prick do all the thinking because it's so much smarter than his brain."
            show scottie joke
            scottie.say "Am I hearing a maybe?"
            show scottie sad
            bree.say "Not unless it's a maybe you'll evolve into something more resembling a human being, you dumbass loser."
            show scottie at center, zoomAt(1.0, (1040, 730)) with move
            "Scottie seems to finally understand, and makes a defeated noise as he shuffles towards the open door."
            "But as he looks back over his shoulder, I can't help seeing an odd kind of interest in his eye."
            "Could it be that he's actually a little intrigued by the way I just chewed him out in front of Sasha like that?"
        "Lead him on" if hero.morality >= 0:
            if scottie.love.max < 20:
                $ scottie.love.max = 20
            $ scottie.unhide()
            "I try to put the fact he's currently behaving like an ass aside and weigh Scottie up fairly."
            "He's pretty cute and he's in great shape, so maybe I'm just not seeing him at his best right now."
            bree.say "You're both mad right now, so nobody's seeing things straight."
            bree.say "I'm sure Scottie's not like this all the time."
            bree.say "Otherwise you'd never have dated him in the first place, Sasha."
            show sasha casual annoyed
            show scottie happy
            "This last comment produces a grin from Scottie and a disgusted frown from Sasha."
            scottie.say "That's right - I'm only mad now 'cos she made me that way!"
            sasha.say "You lying prick!"
            bree.say "Okay, that's enough - I'm sure you were both pricks at one time or another."
            sasha.say "So what are you trying to say, [hero.name]?"
            bree.say "I don't know - maybe that I think it's worth getting Scottie's side of the story...in private some time?"
            show scottie joke
            scottie.say "Yes, score one for me!"
            sasha.say "Whatever, [hero.name] - it's your funeral."
            hide sasha with moveoutleft
        "Lead him on" if hero.morality < 0:
            if scottie.love.max < 20:
                $ scottie.love.max = 20
            $ scottie.unhide()
            "For all that Scottie seems to be dumb as a post and too headstrong for anyone's good, I can't help being attracted to him all the same."
            "I guess it's the idea of being with someone so uncomplicated and impulsive, how exciting that might be."
            bree.say "Maybe I like the idea of being carried off by a big ape like this guy!"
            $ scottie.love += 10
            show sasha surprised
            sasha.say "Tell me you didn't just say that?!?"
            bree.say "Jeez, Sasha - you already made it plain you don't want him anymore."
            bree.say "Move over and give someone else a chance, eh?"
            "I wink suggestively at Scottie, giving him my best approximation of a bimbo's giggle."
            show sasha annoyed
            show scottie blush
            "Scottie looks genuinely shocked, but soon recovers his ludicrous swagger once more."
            show scottie happy
            scottie.say "Yeah, Sasha - you had your chance, now stop cramping my game here."
            sasha.say "Okay, [hero.name] - but just don't say I didn't warn you about this asshole when he fucks you around, just like he did with me."
            hide sasha with moveoutleft
            bree.say "Wow, I thought she'd never leave us alone."
            bree.say "And wow again - how did she ever manage to let go of this body you've got under those clothes?"
            scottie.say "Ah, who cares about her - let's talk more about us."
    hide scottie with moveoutright
    "Scottie leaves soon after the conversation ends, turning on his heel and stomping back out of the front door."
    "I suppose this is what always happens when you live with housemates, their pasts messing with your present."
    if Person.is_not_hidden("scottie"):
        "But Scottie feels to me like the kind of past that might be more than a little fun to mess with."
        "Or be messed with by."
    $ scottie.flags.delay = TemporaryFlag(True, 1)
    return
label scottie_female_event_02:
    if scottie.love.max < 40:
        $ scottie.love.max = 40
    "I'm still not one hundred percent sure about Scottie, and I'm cautious about letting things get too serious between us before I know him better."
    "Of course I've been burnt by trusting guys that seemed to be nice in the past and turned out to be jerks and creeps."
    "But then he's super cute, and I do love the thrill of knowing that I have him when Sasha probably still wants him too."
    "I mean, the more that she calls him an asshole and says she's well rid of him..."
    "That just means that she's trying to cover up and play it cool - right?"
    "Anyway, we're supposed to be meeting up right now."
    "Why we're actually meeting I don't actually know."
    "But I'm hoping that it's for something fun!"
    "This is the perfect chance for Scottie to really pull it out of the bag and prove that Sasha's wrong about him."
    "So, fingers crossed!"
    scottie.say "[hero.name] - over here!"
    show scottie casual with dissolve
    "I turn around to see Scottie waving his entire arm in the air to get my attention."
    "And I don't think I realised before just how masculine those arms really are."
    "Even through his T-shirt, I can see how stacked Scottie really is."
    "I know it sounds stupid, but I get a real thrill from thinking about just how much of a bad boy he is..."
    bree.say "Hi, Scottie!"
    "For some reason I can't seem to keep the adoration that I'm feeling for the sight of him out of my voice."
    "The result is that I kind of end up sounding like a giggly schoolgirl in front of her crush in the playground."
    "But I can't tell if Scottie even notices."
    "Hell, maybe he just assumes every girl he meets goes a little weak at the knees in his presence."
    "He has that kind of dumb, cocksure confidence about him for sure."
    show scottie b happy
    scottie.say "Oh, babe - I was so stoked when you said that you'd come meet me."
    scottie.say "It's like SUCH a weight off of my mind!"
    show scottie normal
    "I nod, expecting him to actually tell me what the point of all this is within his next couple of breaths."
    "But instead, he just stands there in silence, clearly expecting me to say something in response."
    bree.say "Erm, Scottie..."
    bree.say "I kinda feel like you're waiting for me to say something here?"
    "He looks at me with an intense, and yet still blank expression on his face, as if he's struggling to figure something out."
    scottie.say "Ah, man!"
    scottie.say "I was trying so hard to remember I was meeting you that I forgot to tell you why I was meeting you!"
    "Wow - there's no way he's clever enough to pull off acting that dumb."
    "I guess that means he's actually that dumb!"
    bree.say "So...are you going to tell me why now?"
    scottie.say "Oh, yeah - I probably should!"
    "I offer him a smile at his, trying not to look as though I'm totally convinced that he's a moron."
    show scottie a
    scottie.say "Well, [hero.name]...you see...the thing is..."
    scottie.say "I've been trying to get it together to ask you..."
    "I nod enthusiastically, thinking that this is going somewhere that could totally redeem him in my eyes."
    "If he manages to say the right thing here, I could so easily believe that he's sweet, as well as dumb."
    scottie.say "To ask you if you'd lend me some cash to tide me over?"
    scottie.say "Just til the end of the month, when I get my next pay-check, that's all!"
    menu:
        "Agree to lend Scottie the money (100$)" if hero.money >= 100:
            "Though I can't keep the surprise and annoyance off of my face when he finally blurts it out, I can't stay mad at Scottie for too long."
            "He instantly looks like a kicked puppy, shuffling his feet and not knowing where to look."
            "But is it really his fault that I found out what he actually wanted like this?"
            "After all, he did say that he forgot to tell me beforehand."
            "And that means I came her with a head full of ideas that I just thought up myself, without any help from him."
            bree.say "I'll level with you, Scottie."
            bree.say "That's not what I was expecting to hear you say!"
            bree.say "But I think that we both got our wires crossed a little here too."
            "Sensing that he's being tossed a bone, Scottie begins to nod his head vigorously at this."
            show scottie sad
            scottie.say "Yeah, sorry, [hero.name]."
            scottie.say "When I have a couple of things on my mind, stuff kind of gets jumbled up."
            show scottie normal
            scottie.say "You know how it is, right?"
            "I nod and smile, all the time wondering just how many things it takes to get Scottie that confused."
            "I can't honestly believe it's any more than one or two things at any given time..."
            bree.say "Okay, Scottie - don't worry about it."
            bree.say "I can lend you a couple of dollars if it'll help you out."
            bree.say "Just promise me that you'll tell me up front next time, yeah?"
            $ hero.money -= 100
            $ scottie.love += 3
            show scottie sad
            "Scottie at least has the decency to look a little ashamed as he nods in agreement."
            "Shaking my head once more, I reach for my purse."
        "Refuse to lend Scottie the money":
            "At the revelation that I've been asked here just so that he can scab money off of me, I can't keep a lid on my temper for a moment longer."
            bree.say "WHAT...you...you stupid, insensitive, selfish asshole!"
            show scottie surprised at startle
            "Scottie literally flinches away from the intensity of my sudden verbal tirade."
            "He looks left and right, as if hoping that someone will hear what I'm saying and come to his aid."
            scottie.say "Whoa, whoa...babe, calm down!"
            bree.say "Don't tell me to calm down."
            bree.say "In fact, don't ever tell me what to do...EVER!"
            bree.say "And don't call me 'babe', or else I'll start calling you 'dumbass'!"
            show scottie sad
            "Still backing off from me, Scottie holds up his hands."
            "The gesture could as easily be to plead with me to stop as it could to actually shield himself from an imagined fist in the jaw."
            show scottie angry
            scottie.say "Alright, alright...geez!"
            scottie.say "If I'd have known that you were this uptight about money, I'd never have asked for a loan in the first place!"
            "I sigh and shake my head as I start to walk away."
            bree.say "If you think this is just about you pleading for a handout, then you're dumber than you look!"
            $ scottie.love -= 3
            show scottie sad
            "Scottie seems lost for words as I leave him standing there, or at least unable to come up with a anything smart to say."
            "I can't help thinking that maybe I overreacted a little."
            "But then again, maybe Sasha was right about him all along."
    $ scottie.flags.delay = TemporaryFlag(True, 1)
    return

label scottie_female_event_03:
    if scottie.love.max < 60:
        $ scottie.love.max = 60
    scene expression f"bg {game.room}"
    "I'm just walking down the street, minding my own business like always."
    "Hell, I'm not even looking at my mobile when it happens."
    "So part of me can't actually believe what I'm hearing."
    "Mugger" "Hey, blondie..."
    "Mugger" "Give me your fucking money - right now!"
    show ryan casual angry zorder 2 at center, blacker with vpunch
    "I freeze on the spot, finally noticing the guy in front of me."
    "He looking me straight in the eye, a deadly serious look on his face."
    "And worst of all, he's clutching something inside of his pocket."
    "I don't know if it's a knife, a gun or even something harmless."
    "But I'm not about to take a gamble on it being the latter!"
    "I raise my hands in a gesture of surrender."
    bree.say "Okay, okay..."
    bree.say "Whatever you say..."
    bree.say "Just let me get it out of my pocket..."
    "The mugger nods, his eyes darting this way and that."
    if hero.morality <= -50:
        "It's while he's looking the other way that I spot an alleyway nearby."
        "That must be where he was hiding, waiting for a victim to walk by."
        "Nobody would have been able to see him down there, that's for sure."
        "And that's when I have an idea..."
        bree.say "Are you sure you want my money?"
        "The mugger stops looking around at this and stares at me again."
        "I can see that he's confused by the question."
        "He pushes whatever's in his pocket at me with more force."
        "Mugger" "What in the hell are you talking about, bitch?!?"
        "Mugger" "I told you to give me your damn money!"
        bree.say "Okay, if you say so..."
        bree.say "I just thought I could do something else for you instead."
        bree.say "You know, something nice?"
        bree.say "Maybe in private, down that alley?"
        "I cock my head in the direction of the alley and wink at him."
        "The mugger glances over there and then back at me."
        "I can almost see the gears turning inside of his head."
        "For a moment I think he's going to say no."
        "But then he nods and grabs hold of my arm."
        "Mugger" "Okay..."
        "Mugger" "But no tricks!"
        "I feel him jab the object in his pocket into the small of my back."
        "Unfortunately I can't tell anything more about what it is."
        "So I nod and allow myself to be shoved into the alleyway."
        scene bg alley with fade
        "Once we're far enough down it to be out of sight, he stops."
        "Mugger" "Okay, bitch..."
        "Mugger" "Get on with it already!"
        "I nod, trying my best to look like he's the one on charge here."
        "And at the same time I'm getting down on my knees in front of him."
        show breemc bj mugger with fade
        "I don't waste any time in unzipping his flies and pulling out his cock."
        "The mugger divides his attention between me and the entrance to the alley."
        "But I make a point of keeping my eyes on the task at hand."
        show breemc bj tip
        pause .25
        show breemc bj base
        pause .25
        show breemc bj tip
        pause .25
        show breemc bj base
        pause .25
        show breemc bj tip
        pause .25
        show breemc bj base
        "Luckily for me he's a good size and it doesn't take much to excite him."
        "I guess there's a thrill to this situation."
        "Though maybe more for him than me!"
        "What I'm feeling is a mixture of danger and excitement."
        "I don't waste time indulging in foreplay."
        show breemc bj blowjob
        "Instead I dive straight in, taking the head into my mouth."
        "It's a rough and hurried affair, with me swallowing him without hesitation."
        "After that, I work him as hard and fast as I dare, my head moving back and forth."
        show breemc bj medium
        pause .25
        show breemc bj small
        pause .25
        show breemc bj medium
        pause .25
        show breemc bj small
        pause .25
        show breemc bj medium
        pause .25
        show breemc bj small
        "Mugger" "Yeah..."
        "Mugger" "That's right..."
        "Mugger" "You'd better suck hard!"
        "I do the best I can to nod as I work on him."
        "And I can feel my cheeks starting to burn with the shame of it all."
        "Not that the sensation does anything to stop me pushing onwards."
        show breemc bj medium
        pause .25
        show breemc bj small
        pause .25
        show breemc bj medium
        pause .25
        show breemc bj small
        pause .25
        show breemc bj medium
        "In fact, there's something thrilling about the position I'm in."
        "I can almost forget that I was the one who suggested this."
        "Instead I feel like I'm helpless, forced into what I'm doing."
        "And that makes the humiliation all the more thrilling!"
        "I redouble my efforts, speeding up the pace as much as I dare."
        "Mugger" "Fuck me..."
        "Mugger" "I'm gonna lose it..."
        "Mugger" "Swallow this if you can!"
        show breemc bj big cum with hpunch
        "A moment later he shoots his load in my mouth."
        with hpunch
        "I gag and cough as it hits the back of my throat."
        "But I don't dare spit it out for fear of making him mad."
        "Instead I wait for him to pull his cock out of my mouth."
        show breemc bj handjob breath -cum
        "And then I swallow everything down as quickly as I can."
        "Gasping for breath, I look up, ready to ask if I can go."
        hide breemc bj with fade
        "But the mugger's already gone, leaving me alone in the alleyway."
        "I can just hear the sound of his footsteps as he runs away down the other end of the alley."
        "All I can do is get to my feet and try to straighten myself up."
        "I guess things could have worked out much worse than they just did."
        "And on the plus side, I didn't get robbed."
        "Not that I had any money on me to begin with."
        "I mean, who carries cash these days?!?"
    else:
        $ scottie.flags.saviour = True
        scottie.say "Hey, creep..."
        scottie.say "What the fuck do you think you're doing, huh?"
        show ryan casual angry zorder 2 at right4, blacker
        show scottie angry zorder 1 at left4
        with hpunch
        "All of a sudden, the mugger cries out in pain."
        "And I see Scottie's head appear over his shoulder."
        "Mugger" "Arrgh!"
        bree.say "No, Scottie!"
        bree.say "He's got something in his pocket!"
        show scottie joke at left4, vshake
        "Scottie laughs at my warning."
        "He jerks his arm and I see he's got hold of the mugger's arm too."
        "It's the one he was using to threaten me just now."
        "And Scottie wrenches it violently, pulling his hand out of his pocket."
        "The mugger loses his grip on what he was holding, and it drops onto the floor."
        show scottie normal
        scottie.say "It was just his phone, [hero.name]!"
        scottie.say "This guy's full of shit - aren't you, man?"
        with hpunch
        "Scottie twists the mugger's arm again, making him scream in pain."
        "Mugger" "Aargh!"
        "Mugger" "Yeah, man...whatever you say!"
        "Mugger" "I'm full of shit, okay?"
        show scottie a joke at left4, vshake
        "Scottie laughs out loud and lets the mugger go."
        play sound punch_hard
        pause 0.2
        with hpunch
        "But before he can take a step, Scottie kicks him in his ass."
        hide ryan casual angry with moveoutbottom
        "This sends the mugger tumbling to the ground in a heap."
        "I expect him to get up and try to fight back."
        "But instead he scrambles to his feet and runs away, not stopping to look back."
        "Scottie watches him go, still laughing heartily."
        show scottie angry at center with move
        "Then he stomps on the phone the mugger dropped for good measure."
        "I'm still trembling a little from my ordeal."
        "And sure, Scottie totally overdid it when he got physical just now."
        "But that doesn't stop my heart fluttering at the thought of him coming to my rescue."
        "Maybe this is how a damsel in distress feels when a knight rides in to save her?"
        "Sure, he might be an oaf under the shining armour and have no manners to speak of."
        "But you can't deny he's manly and briming with confidence!"
        if hero.morality <= -25:
            bree.say "Wow..."
            bree.say "Thanks, Scottie!"
            bree.say "I'm so lucky you showed up when you did!"
            show scottie normal
            "Scottie stops stamping on the mobile and turns too face me."
            show scottie happy
            "A grin spreads across his face and he shakes his head."
            scottie.say "No worries, [hero.name]."
            scottie.say "Someone needed to kick that creep's ass."
            scottie.say "I'm just glad he didn't hurt you before I got here!"
            "I can feel myself blushing, and I can't stop it."
            "Other parts of me are reacting as well."
            "Parts I can't even begin to mention!"
            "Ah, who am I trying to kid?"
            "Scottie's display of manhood just now - it's really turning me on!"
            bree.say "Well, I think you deserve a reward, Scottie!"
            bree.say "How about we sneak into that alley over there?"
            bree.say "Then I can thank you properly!"
            "Scottie looks over at the alleyway, then back at me."
            "For a moment I can see his brain struggling to make sense of my offer."
            "He narrows his eyes, as if he suspects some kind of trick."
            show scottie shy
            "But finally, recognition appears in his eyes."
            show scottie blush
            scottie.say "You mean that, [hero.name]?"
            "I nod and smile."
            scottie.say "Oh, wow..."
            scottie.say "Sure thing!"
            "I take Scottie by the hand and we hurry into the alleyway."
            scene bg alley
            show scottie
            with fade
            "As soon as we're out of sight, I kneel down in front of Scottie."
            show breemc bj
            "It only takes a few second to unzip his pants and get his cock out."
            show breemc bj tip
            pause .4
            show breemc bj base
            pause .4
            show breemc bj tip
            pause .4
            show breemc bj base
            pause .4
            show breemc bj tip
            "Scottie gasps as I begin to stroke him gently."
            "And it doesn't take long for him to get nice and hard too."
            "I start out gently and slowly, kissing and licking at the base of the shaft."
            "But as I inch my way higher, I make things ever more intense."
            "This means that by the time I reach the tip, Scottie's enthralled."
            "He's leaning against the wall, gasping with pleasure."
            show breemc bj blowjob
            "I smile and then take his cock into my mouth."
            "After that I close my eyes and devote myself to the task at hand."
            show breemc bj medium
            pause .3
            show breemc bj small
            pause .3
            show breemc bj medium
            pause .3
            show breemc bj small
            pause .3
            show breemc bj medium
            pause .3
            show breemc bj small
            "All I can think about is giving Scottie as much pleasure as possible."
            "My head bobs up and down as I go ever faster."
            show breemc bj medium
            pause .15
            show breemc bj small
            pause .15
            show breemc bj medium
            pause .15
            show breemc bj small
            pause .15
            show breemc bj medium
            pause .15
            show breemc bj small
            pause .15
            show breemc bj medium
            pause .15
            show breemc bj small
            pause .15
            show breemc bj medium
            pause .15
            show breemc bj medium
            "And the whole time there's the fear of somebody seeing what I'm doing."
            "That makes me feel dirty, but also thrills me to the very core."
            "What if they think I'm a prostitute and Scottie's a client?"
            "What if the police stumble across us before I'm done?"
            scottie.say "Oh fuck, [hero.name]..."
            scottie.say "What are you doing to me?"
            scottie.say "I'm gonna lose it!"
            "Oops...looks like there's no chance of being found out before it's over!"
            show breemc bj big cum with hpunch
            "Scottie grabs hold of my shoulders, holding me in place."
            "Which means I have no choice but to swallow."
            show breemc bj big cum with hpunch
            $ scottie.love += 5
            "He shoots his load into my mouth a moment later."
            show breemc bj big cum with hpunch
            "But the fact I knew what was coming means that I can handle it."
            show breemc bj handjob base breath -cum
            "I swallow it down, breathing heavily as Scottie pulls out of my mouth."
            hide breemc bj
            show scottie b normal
            with fade
            "He makes himself decent while I get up and do the same."
            "And then he looks at me with a smile on his face."
            scottie.say "Thanks, [hero.name]."
            scottie.say "I should save you more often!"
            "I laugh and smile, which is the reaction I know Scottie wants."
            "But the truth is that he probably doesn't need to go to such lengths."
            "The most he needs to do is ask nicely when I'm in a good mood."
            "Maybe even just ask when I'm not!"
            "But I'm not about to tell him that..."
        else:
            bree.say "Wow..."
            bree.say "Thanks, Scottie!"
            bree.say "I'm so lucky you showed up when you did!"
            show scottie b normal
            "Scottie stops stamping on the mobile and turns too face me."
            show scottie happy
            "A grin spreads across his face and he shakes his head."
            scottie.say "No worries, [hero.name]."
            scottie.say "Someone needed to kick that creep's ass."
            scottie.say "I'm just glad he didn't hurt you before I got here!"
            "I can feel myself blushing, no matter how hard I try not to."
            "I know that Scottie's a dumb-ass, but he did save me back there."
            bree.say "Maybe I need a guy like you around more often, Scottie?"
            bree.say "I'm sure you'd come in useful!"
            $ scottie.love += 2
            scottie.say "Any time, [hero.name], any time!"
            scottie.say "Just call my name, and I'll be there!"
    $ scottie.flags.delay = TemporaryFlag(True, 1)
    return

label scottie_female_event_04:
    play sound cell_vibrate
    "When my mobile rings I don't think much of it."
    "As usual, I just pull it out and check who's calling."
    "If it's someone that I want to talk to, then I'll answer it."
    play sound cell_vibrate
    "If not, then I guess they're just going have to go to voicemail!"
    "But when I look at the caller ID, I see that it's Scottie."
    if scottie.flags.saviour:
        "As soon as I see his name, I remember the incident with the mugger."
        "That creep tried to rob me in the middle of the damn street!"
        "But it was Scottie that came out of nowhere to save me."
        "And the memory gives me a little thrill."
        play sound cell_vibrate
        "So much so that I answer the call without a second thought."
    else:
        play sound cell_vibrate
        "Huh, I wonder what he could want?"
        "Truth be told, I'm getting to like Scottie."
        "Sure, he's kind of dumb - but in a cute way."
        "Problem is that I still sort of see him as Sasha's ex!"
        menu:
            "Take the call":
                "But that's never going to change while I'm keeping him at arm's length."
                "Sasha and Scottie have been over since forever."
                "And there's no reason for me not to be friends with the guy."
                "That's why I take the call."
            "Pretend that you didn't see Scottie's call":
                "Maybe I just need some more time to make sense of the guy?"
                play sound cell_vibrate
                "Which means that taking personal calls from him isn't on the cards."
                "I put my phone away and let the call go to voicemail."
                "That way I can check it later and see what Scottie wanted."
                "If he's serious then he'll likely leave me a message."
                "If not, then it couldn't have been worth my time anyway!"
                $ scottie.love -= 2
                $ hero.cancel_event()
                return
    bree.say "Hey, Scottie!"
    bree.say "I wasn't expecting a call from you!"
    scottie.say "Hey there, [hero.name]..."
    scottie.say "Just thought I'd surprise you, yeah?"
    "I do my best not to giggle at Scottie's tone of voice."
    "He sounds so cheesy, like he really thinks he's all that!"
    "I know that I should shut him down on stuff like that."
    "But it's so funny how he thinks he's god's gift to womankind!"
    bree.say "Come on, Scottie."
    bree.say "You didn't just call me to hear the sound of my voice!"
    scottie.say "I might have, [hero.name]!"
    scottie.say "I might have!"
    scottie.say "But, no...you're right - I didn't!"
    scottie.say "I wanted to ask you out on a date."
    "Scottie says it in such a casual manner I don't get what he means at first."
    "But then it dawns on me that he really did just ask me out on an actual date!"
    "And he has the balls to just drop it in there too, like it's a done deal!"
    bree.say "You want to take me out?"
    bree.say "Like on a real date?"
    bree.say "Just you and me?"
    scottie.say "Erm...yeah!"
    scottie.say "You do know what a date is, right?"
    bree.say "Of course I know what a date is!"
    bree.say "I'm not a moron, Scottie!"
    scottie.say "Whoa, [hero.name]!"
    scottie.say "Calm down there!"
    scottie.say "Most girls are pretty excited at the idea of a date with your's truly!"
    scottie.say "But you're kind of weirding me out right now..."
    menu:
        "Agree to go on a date with Scottie":
            if scottie.love.max < 80:
                $ scottie.love.max = 80
            "Wait a minute, wait a minute..."
            "What in the hell am I doing here?"
            "I'm accusing Scottie of acting like a jerk."
            "But I'm doing the exact same thing in return!"
            "All the guy did was call me up and ask me out on a date."
            "It's not like he's committed some kind of crime!"
            bree.say "Sorry, Scottie."
            bree.say "Just ignore me, okay?"
            bree.say "I'm not having the best day."
            "The moment I apologise, it's like someone hit the reset button on Scottie."
            "Suddenly he's the upbeat, confident guy that he was when we started the call all over again."
            scottie.say "Hey, no worries, [hero.name]!"
            scottie.say "We all have brain-fart days!"
            scottie.say "So what do you say?"
            scottie.say "Are we gonna go on a date or what?"
            bree.say "That depends, Scottie."
            bree.say "What did you have in mind?"
            scottie.say "Keep it simple, [hero.name]."
            scottie.say "That's my motto!"
            "Yeah, and a perfect description of himself too!"
            scottie.say "I was thinking we could go out for a couple of drinks."
            scottie.say "Then maybe go to a night-club after that?"
            "I'm about to make a cutting comment about his lack of originality."
            "But then I stop myself, remembering that I was going easy on him."
            bree.say "You know what, Scottie..."
            bree.say "That sounds like a good idea."
            bree.say "Nice and easy - no pressure."
            $ scottie.love += 2
            scottie.say "Sweet, [hero.name]!"
            scottie.say "We're gonna have a great time!"
            "We thrash out the details, and then end the call."
            "And just like that it's all arranged."
            $ scottie.flags.delay = TemporaryFlag(True, 1)
        "Hard pass on this":
            "Who in the hell does this guy think he is?"
            "He calls me up out of nowhere and asks me out on a date."
            "And he acts like he's the one doing me a favour by asking!"
            "Scottie really need to be taken down a peg or two!"
            bree.say "Yeah, Scottie, that's not me weirding you out."
            bree.say "It's your pea-brain over-heating with trying to think!"
            scottie.say "Hey!"
            scottie.say "There's no need to be mean, [hero.name]!"
            bree.say "Okay, Scottie, okay..."
            bree.say "Let's make a deal."
            bree.say "I'll stop being mean to you when you stop being a jerk!"
            $ scottie.love -= 10
            "I end the call before Scottie can reply."
            "It's a petty thing to do, and I know it."
            "But I really feel like I needed to have the last word."
            "My phone rings again as Scottie tries to call back."
            "But I let the call go to voicemail."
            "And then I ignore the texts that he sends afterwards too."
            "I'll talk to him sooner or later."
            "But that'll be once I've calmed down."
            "And when I think he's been in the dog-house long enough!"
            $ scottie.set_gone_forever()
    return

label scottie_female_event_05:
    scene bg street
    if scottie.love.max < 100:
        $ scottie.love.max = 100
    "Part of me wondered why Scottie would go to the trouble of calling me up and asking me to a nightclub."
    "I mean, I know that it's a pretty normal thing for a guy to do when he's getting to know a girl."
    "But Scottie's not exactly a normal kind of guy, you know?"
    "He's more the kind to just turn up unannounced and tell you that he's taking you to a club."
    "So that you have the choice of saying yes because he's putting you on the spot."
    "Or else getting pissed with him and telling him that he's an insensitive jerk!"
    "I've actually gotten to thinking that this might be his way of showing me I've got him all wrong."
    "Maybe when I meet him at the nightclub, I'll get to see a whole different side to the guy?"
    "Like he'll turn up wearing something that's not a band T-shirt."
    "And he'll be a little bit more polite when he speaks to me, you know?"
    scottie.say "Hey, hey, hey!"
    scottie.say "[hero.name] baby!"
    scottie.say "I love how your ass looks in that outfit!"
    "I turn around at the sound of Scottie's voice and see him walking towards me."
    show scottie at right with easeinright
    "That greeting and the fact he's in a Metallikea T-shirt just proved me wrong!"
    show scottie at center with ease
    "But at least it looks like he's broken out one of his newer T-shirts for the occasion."
    bree.say "Hi, Scottie..."
    bree.say "You're a little later than we agreed."
    bree.say "I was starting to get worried you'd stand me up!"
    show scottie joke at center, startle
    "Scottie makes a derisive snorting sound at the mere suggestion."
    show scottie b at center, zoomAt(1.5, (640, 1040))
    "He shakes his head as he drapes an arm around my shoulder."
    "And he starts to lead me into the nightclub as he explains himself."
    scottie.say "Hah, that's pretty funny, [hero.name]!"
    scottie.say "Like I'd miss a date with a hottie like you!"
    scottie.say "You've just got to understand that I'm a casual kind of guy."
    scottie.say "And if I'm late, then you've just gotta wait around for me, understand?"
    "I can't help frowning at the arrogance of what Scottie just said to me."
    "I'm about to give him a piece of my mind as we walk into the nightclub."
    scene bg nightclub
    show scottie b at center, zoomAt(1.5, (640, 1040))
    with fade
    "But the moment I hear the pounding volume of the music, I decide to let it go this once."
    "There's no point in me telling Scottie off if he's not even going to hear me."
    "Much better to just try to try and have a good time with him."
    "But that's his one free pass for the night used up."
    "If he's that boorish with me again, I'll make sure he regrets it!"
    "The club is pretty packed out tonight, almost full to capacity."
    "This means that we have to fight our way wherever we want to go."
    "But that doesn't seem to be a problem for Scottie."
    with hpunch
    "With a firm hold on my hand, he barges his way through the crowds."
    show scottie b angry
    "And when anyone doesn't take to kindly to being pushed aside, he's unfazed."
    "More than once I see a guy turn round to give Scottie a threatening stare."
    "But they always think better of it when they get a good look at him!"
    "Look, I'm not saying that Scottie's like a bully or anything."
    "But it is kind of a thrill to be with someone that's just so confident!"
    show scottie b normal
    scottie.say "You wanna drink, [hero.name]?"
    scottie.say "Or should be dance first?"
    bree.say "Huh?"
    bree.say "What was that, Scottie?"
    show scottie b at center, zoomAt(1.0, (640, 1040)), vshake
    scottie.say "YOU WANT A DRINK OR A DANCE?!?"
    "The very moment that Scottie raises his voice, the music stops."
    "It's only the briefest silence between tracks as the DJ selects the next one."
    "But it's enough for Scottie to be heard by almost every single person in the place!"
    show scottie b embarrassed
    "Oddly that seems to embarrass him when everything else was like water off a duck's back."
    bree.say "Let's get a drink first, Scottie."
    bree.say "Give everyone a moment to forget what just happened, yeah?"
    "Scottie nods and together we slink over to the bar."
    show scottie b normal with fade
    "But once we're there, he seems to regain a little of his normal swagger."
    scottie.say "This round's on me, [hero.name]."
    scottie.say "What can I get you?"
    "I'm so used to splitting things on dates that Scottie's offer takes me by surprise."
    menu:
        "A drink would be nice":
            "It's a little bit old-fashioned."
            "But I can see that Scottie's just trying to be nice."
            "So I decide to let it slide just this once."
            bree.say "Oh, thanks, Scottie!"
            bree.say "I'll have whatever you're having!"
            show scottie happy
            "Scottie nods happily and orders the drinks."
            "Then we turn to check out the dance-floor."
            $ scottie.sub -= 1
        "No thanks":
            bree.say "What do you think this is, Scottie?"
            bree.say "The twentieth century?"
            show scottie surprised
            "Scottie looks at me blankly."
            scottie.say "Huh?"
            bree.say "I'm a modern girl, Scottie!"
            bree.say "I can pay for my own damn drink!"
            show scottie sad
            scottie.say "Oh...okay, [hero.name]!"
            scottie.say "Geez..."
            scottie.say "I was just trying to be nice..."
            "Trying to move things on, we turn to check out the dance-floor."
            $ scottie.sub += 1
            show scottie normal
    bree.say "Wow!"
    bree.say "It looks pretty crowded out there!"
    bree.say "Maybe we should wait for it to quiet down a little?"
    show scottie joke at startle
    "Scottie snorts and shakes his head at this."
    scottie.say "No way, [hero.name]!"
    scottie.say "If you wanna dance, then we're gonna dance."
    scottie.say "We just need to make all these losers move out of our way!"
    "Scottie takes hold of my hand for a second time and makes straight for the dance-floor."
    "I follow in his wake, watching as he shoulders his way through the crowd."
    "It's just like what happened before, Scottie making a path for me."
    "And I have to admit that he's pretty good at it!"
    "Soon enough we're almost in the middle of the dance-floor."
    "Scottie seems to think this is a decent spot."
    hide scottie
    show dance scottie
    with fade

    "So he stops and makes a claim on his newly-won territory."
    "Almost as soon as he does so, the DJ plays a track I love."
    "I don't know if Scottie like it too."
    "Or maybe he's just trying his best to impress me."
    "Either way, we're pressed close together as we dance."
    "It's hot and I can feel myself beginning to sweat."
    "Bodies are pressing against us on all sides."
    "But none of them are as close to me as Scottie is right now!"
    if hero.morality <= -50:
        "I think the drinks that we had just now must have been stronger than I'm used to."
        "Because the moment that I start to dance with Scottie, it's like I can't help myself."
        "All I can hear is the pounding of the music and all I can feel is his body against mine."
        "But Scottie's looking better and better every time I look at him!"
        "He has that cute, dumbass smile."
        "Those muscles that I just want to squeeze so badly too!"
        "And when he put his hands on me..."
        "Whoa...wait a minute..."
        "Am I falling for this guy?"
        "Do I have serious feelings for Sasha's ex?"
        "Just as that thought enters my head, Scottie pulls me closer than ever."
        "I can feel every one of his hard muscles under his clothes."
        "His arms are so strong...they make me feel so safe."
        "Before I know it, I'm clinging onto Scottie."
        "In fact I'm grinding myself against him for all I'm worth."
        "Scottie's kissing me at the same time."
        "His tongue is in my mouth, mine in his."
        "Our hands are everywhere, stroking and caressing."
        "And I can feel just how hard his cock is too!"
        "God I want that thing inside of me right now!"
        "I don't care if that makes me sound desperate."
        "Because that's just how I feel!"
        "I want to grind against Scottie until it makes me cum!"
        "No...it's not enough!"
        "This time it's me grabbing hold of Scottie's hand."
        hide dance
        show scottie
        with fade
        "But this time I'm dragging him off the dance-floor."
        hide scottie with moveoutright
        "He follows without any resistance, letting me lead the way."
        "I make straight for the bathroom, not stopping to explain myself."
        scene bg restroom
        show scottie blush
        with fade
        "But once we're inside one of the cubicles, my intentions are pretty obvious."
        "Scottie braces himself against the walls as I tear at his pants." with hpunch
        "It should be easy to open his flies, but I'm almost desperate by now."
        "And I fumble around, trying to get at his cock."

        show breemc bj restroom with fade
        "Once I actually manage it, there's no need to waste any more time."
        "Scottie's as hard as he's going to get, aroused from watching me."
        show breemc bj blowjob
        pause .25
        show breemc bj medium
        pause .25
        show breemc bj small
        pause .25
        show breemc bj medium
        pause .25
        show breemc bj small
        pause .25
        show breemc bj medium
        pause .25
        show breemc bj small
        "So I dive straight in, sucking on the head like my life depends on it."
        "There's no room for fancy technique here."
        "This is just me getting what I need as quickly as possible."
        "But the idea of that seems to appeal to Scottie."
        "And he gasps with delight as my head begins to bob up and down."
        show breemc bj medium
        pause .25
        show breemc bj small
        pause .25
        show breemc bj medium
        pause .25
        show breemc bj small
        pause .25
        show breemc bj medium
        pause .25
        show breemc bj small
        "He's not the only one enjoying it either."
        "Scottie's cock feels so good in my mouth."
        "It's everything that I hope it would be and more."
        "I can't help whimpering as I work him with my mouth."
        "And I can feel just how wet my pussy is too."
        "I desperately want to slide my fingers down there..."
        "But I need to keep myself focused on Scottie!"
        scottie.say "Oh, fuck..."
        scottie.say "You're fucking amazing..."
        scottie.say "I...I never had a BJ like this before!"
        "I feel a strange surge of pride as Scottie praises me."
        "Like I know that I should feel a little dirty to be doing this."
        "But that makes it feel all the more exciting."
        "I kind of feel good for being bad, crazy as that sounds!"
        show breemc bj medium
        pause .25
        show breemc bj big
        pause .25
        show breemc bj medium
        pause .25
        show breemc bj big
        pause .25
        show breemc bj medium
        pause .25
        show breemc bj big
        scottie.say "Oh shit..."
        scottie.say "[hero.name]..."
        scottie.say "I'm gonna..."
        show breemc bj cum with hpunch
        $ scottie.love += 5
        "A moment later, Scottie shoots his load."
        with hpunch
        "I don't think about stopping for even a second."
        "Instead I do my best to swallow every single drop!"
        show breemc bj handjob breath -cum
        "Once he's done, I put his cock away and zip him up."
        show scottie kiss with fade
        $ scottie.flags.kiss += 1
        "Then I kiss him full on the lips."
        $ scottie.sub += 5
        "And I enjoy the look in his eyes when he realises what's still on my tongue!"
    elif hero.morality <= -25:
        "I think the drinks that we had just now must have been stronger than I'm used to."
        "Because the moment that I start to dance with Scottie, it's like I can't help myself."
        "All I can hear is the pounding of the music and all I can feel is his body against mine."
        "But Scottie's looking better and better every time I look at him!"
        "He has that cute, dumbass smile."
        "Those muscles that I just want to squeeze so badly too!"
        "And when he put his hands on me..."
        "Whoa...wait a minute..."
        "Am I falling for this guy?"
        "Do I have serious feelings for Sasha's ex?"
        "Just as that thought enters my head, Scottie pulls me closer than ever."
        "I can feel every one of his hard muscles under his clothes."
        "His arms are so strong...they make me feel so safe."
        "Before I know it, I'm clinging onto Scottie."
        "In fact I'm grinding myself against him for all I'm worth."
        hide dance
        show scottie kiss
        with fade
        $ scottie.flags.kiss += 1
        $ scottie.love += 3
        $ scottie.sub += 2
        "Scottie's kissing me at the same time."
        "His tongue is in my mouth, mine in his."
        "Our hands are everywhere, stroking and caressing."
        "And I can feel just how hard his cock is too!"
        "God I want that thing inside of me right now!"
        "I don't care if that makes me sound desperate."
        "Because that's just how I feel!"
        "I want to grind against Scottie until it makes me cum!"
    else:
        "I know that I should keep a close eye on Scottie in a situation like this."
        "But the truth is that I'm having too much of a good time to be worried."
        "And it's not like I'm here against my will either."
        "I want to cut loose and have some serious fun tonight."
        "And Scottie's the perfect guy to do that with too."
        "Soon enough we're lost in the act of dancing together."
        "And the truth is that he's got a natural kind of talent for it."
        "Because he's not hung up about himself, Scottie just lets go."
        "And for once I'm sure that his attention is all on me."
        "Maybe I've had a little too much to drink and it's lowering my inhibitions."
        "But Scottie's looking better and better every time I look at him!"
        "He has that cute, dumbass smile."
        "Those muscles that I just want to squeeze so badly too!"
        "And when he put his hands on me..."
        "Whoa...wait a minute..."
        "Am I falling for this guy?"
        "Do I have serious feelings for Sasha's ex?"
        "Just as that thought enters my head, Scottie pulls me closer than ever."
        "I can feel every one of his hard muscles under his clothes."
        "His arms are so strong...they make me feel so safe."
        "It's not Scottie that makes the next move, it's me."
        hide dance
        show scottie kiss
        with fade
        $ scottie.flags.kiss += 1
        $ scottie.love += 3
        "Before I know what I'm doing, I kiss him."
        "Scottie reacts on sheer instinct, and the kiss becomes passionate."
        "Our tongues are the ones dancing now, cheesy as that sounds!"
        "But the worst thing is that I know I want so much more."
    scene bg black with dissolve
    scene bg street
    show scottie happy
    with dissolve
    "At the end of the night, we're aching, sweaty and exhausted."
    "But both Scottie and I have a massive smile on our faces."
    bree.say "I had a great time tonight, Scottie."
    bree.say "We should do this more often, yeah?"
    scottie.say "Any time you like, [hero.name]."
    scottie.say "I love having fun."
    scottie.say "And I love girls that are fun too!"
    "I nod eagerly, already looking forward to seeing him again."
    "Part of me wants to just come out and ask Scottie if this means we're an item."
    "You know, if we're now officially dating?"
    "But I get the feeling he's one of those guys that never just comes out and says it."
    "So I leave the question unasked and instead try to tell myself it's no big deal."
    "Do I really need a formal declaration from Scottie?"
    "Maybe I need to learn to be more laid back, just like he is..."
    $ scottie.flags.delay = TemporaryFlag(True, 1)
    scene bg black with dissolve
    return

label scottie_female_event_06:
    if scottie.love.max < 120:
        $ scottie.love.max = 120
    scene bg livingroom
    "When Scottie told me that he wanted to pick where we'd go on our next date I was sceptical."
    "And when he doubled down on that and also said that it was going to be a surprise, I almost said no."
    "But then I remembered that we've been having a pretty good time together recently."
    "That I've been seeing a different side of the guy to the one he usually shows to the world."
    "So I swallowed all of my misgivings and just thought what the hell."
    scene bg livingroom at blur(16), dark with dissolve
    "And that's how I ended up here, with Scottie's hands over my eyes."
    scene bg taxi at blur(16), dark with dissolve
    "He guides me out of the taxi and into the place we're going for our date."
    "I can hear the sound of voices and music in the background too."
    bree.say "Oh..."
    bree.say "Is it a nightclub, Scottie?"
    bree.say "Or maybe a gig!"
    bree.say "Are we seeing a band?"
    "I hear Scottie let out a guffawing laugh."
    scene poledance
    show poledance harmony shiori at center, blur(5)
    with wipeup
    "And then he takes his hands away from my eyes."
    show scottie at left5, blur(5) with dissolve
    scottie.say "Nah, [hero.name]..."
    scottie.say "It's way better than that!"
    "I blink as the light in the room overwhelms my eyes for a moment."
    "Then I squint to see where I am as my vision begins to clear."
    scene poledance
    show poledance harmony shiori
    show scottie at left5
    with dissolve
    "I can see tables with people drinking."
    "There's a stage, with someone doing something on it..."
    "It's a girl..."
    "Is she..."
    "Is she taking her clothes off?!?"
    bree.say "This is a strip club!"
    bree.say "Scottie, you brought me to a strip club?!?"
    show scottie happy at startle
    scottie.say "Surprise, [hero.name]!"
    scottie.say "Isn't this place great?"
    scottie.say "There's booze, music and hot girls!"
    scottie.say "All of the best things in life, right here!"
    show scottie perv
    "Scottie does his typical thing of grinning like a fool as he answers me."
    "Then he sweeps his arm around in a kind of grand gesture, like he's showing the place off."
    show scottie normal
    "I can't help following him as he turns around, doing a complete three hundred and sixty degree rotation."
    "I can see that he's expecting me to be impressed, even as bowled over as he seems to be with the place."
    "So I don't really have any other choice but to look him in the eye and give him my honest opinion."
    if hero.morality >= 25:
        bree.say "Oh...my...god..."
        bree.say "I can't believe it, Scottie!"
        bree.say "I can't believe you actually brought me to a strip club!"
        show scottie surprised
        "A puzzled look appears on Scottie's face."
        "It's like he really can't understand what's wrong."
        scottie.say "Huh?!?"
        scottie.say "What's the problem, [hero.name]?"
        show scottie sad
        scottie.say "You know how much I like hot chicks, right?"
        show scottie -sad
        scottie.say "I mean, that's why I like you!"
        "I shake my head at this."
        "I mean, I know Scottie's a little dumb."
        "But this is too bone-headed even for him!"
        bree.say "Of course I know that, Scottie."
        bree.say "But you're dating me."
        bree.say "So you're not supposed to be looking at other girls!"
        bree.say "And you're definitely not supposed to be taking me somewhere to ogle them!"
        show scottie surprised
        "Scottie's looking more confused than ever by now."
        show scottie embarrassed
        "He's actually getting a little flushed."
        "And he's looking around the place like he's worried."
        "I follow his glance for a moment, and it looks like he's onto something."
        "More than a few of the other patrons are starting to look in our direction."
        "But what's strange is that most of them are staring daggers at him!"
        "I'm a little confused, as I thought this kind of place was all about exploiting women."
        "Is it possible that they're actually hyper aware of the way this place looks to girls like me?"
        "That they're super keen to come down on a guy that looks like he's messing with a woman?"
        "Even if I don't want to be here, there's no way I want Scottie to get his ass kicked!"
        "And some guys that look like bouncers are starting to come this way!"
        bree.say "Look, Scottie..."
        bree.say "Let's just forget about it and go, okay?"
        show scottie -blush
        scottie.say "Ah..."
        scottie.say "You know what, [hero.name]..."
        scottie.say "That sounds like a great idea!"
        scene bg alley with fade
        "Together we hurry out of the strip club and onto the street."
        "All I can hope is that Scottie really does forget all about this."
        "Or even better, that he doesn't and learns his lesson from it."
        $ scottie.love -= 2
        $ scottie.flags.delay = TemporaryFlag(True, 1)
        $ game.active_date.score = 25
        $ game.active_date.stay = False
        $ game.pass_time(2)
        return
    elif hero.morality <= -25:
        bree.say "Oh...my...god..."
        bree.say "Why didn't you just say you wanted to come do a strip club, Scottie?"
        bree.say "This is going to be so much fun!"
        show scottie happy
        "Scottie's face lights up at my positive reaction."
        "And I can see the swagger returning in the way he's holding himself."
        scottie.say "Ah, you know me, [hero.name]."
        scottie.say "I wanted to surprise you."
        scottie.say "But you're still the hottest girl in here, by a mile!"
        "It's a cheesy line and I know that Scottie's trying to butter me up."
        "But I'm not about to let that spoil my mood and the chance to have a good time."
        bree.say "So what are we waiting for, Scottie?"
        bree.say "We're not going to see anything from here!"
        scottie.say "You're right, [hero.name]!"
        scottie.say "Let's go grab a drink!"
        show scottie at center, zoomAt(1.5, (440, 1140)) with fade
        "We do just that, then we settle into a booth with a good view."
        "And I don't know who enjoys the show more, Scottie or me!"
        "I can just sit back and have a good time watching."
        "But bless the poor guy, he's facing a serious dilemma."
        "Part of him wants to watch the girls gyrating on the stage."
        "But another wants to watch me watching them!"
        "I'm guessing that Scottie's one of those guys with serious fantasies."
        "The kind of guy that wonders if girls like to look at other girls."
        "I can see how he's staring at me, studying my every reaction."
        "So I decide to play around with him a little."
        "You know, have some fun at his expense?"
        bree.say "Ooh..."
        bree.say "That girl is SO hot!"
        bree.say "Don't you think, Scottie?"
        show scottie blush
        scottie.say "Wha...what?!?"
        scottie.say "Which girl is that, [hero.name]?"
        bree.say "The one on the stage of course, silly!"
        bree.say "Don't you think she's got really nice breasts?"
        "I try to keep from laughing as Scottie sweats in his seat."
        "How can a guy that acts so macho turn into a mess like this?"
        "Is it really that hard for him to handle a girl talking about that kind of stuff?"
        "You know, the exact same kind of stuff he's always going on about himself?"
        scottie.say "I...I guess so, [hero.name]!"
        scottie.say "B...but maybe they're a little too big?"
        bree.say "I didn't know they could BE too big, Scottie!"
        bree.say "Are hers bigger than mine?"
        bree.say "I can't quite tell from over here."
        show scottie -blush
        scottie.say "I dunno, [hero.name]!"
        scottie.say "I didn't measure them last time I saw them!"
        "I can't hold it in any longer and I start to giggle at Scottie."
        "He soon catches on that I just made him the butt of my joke."
        "And I see him glancing around, looking for a means to get back at me."
        scottie.say "Look, [hero.name]..."
        scottie.say "They've got an amateur hour coming up next!"
        scottie.say "You should get up there yourself."
        scottie.say "Show them how it's done, yeah?"
        if hero.morality <= -50:
            "We've been drinking a hell of a long time by now."
            "I'm struggling to see straight."
            "My speech is kind of slurred too, making me talk crap."
            "And the world seems to be so simple, all a matter of black and white."
            "Shit - this must be what it's like to be Scottie!"
            "Maybe that's why I stand up the moment I make sense of his suggestion."
            bree.say "Hell yeah, Scottie!"
            bree.say "I could do all of that gyrating shit!"
            bree.say "You just watch me..."
            "Almost as soon as he sees me rise to my feet, Scottie looks worried."
            "He makes to stop me, but I brush him aside as I stride out of the booth."
            "Before he can get up, I'm already climbing onto the stage."
            "All I can see is the pole in the centre of it."
            "And I focus all of my efforts on reaching that spot."
            "As soon as I get there, I turn to face the audience."
            "At first, the light blinds me and I have to hold up a hand to my eyes."
            "But my vision soon adjusts, letting me see that all other eyes in the place are on me!"
            "Some of the patrons are already cheering me on."
            "Others are just sitting back, waiting to see what happens next."
            "Scottie's the only one staring at me with concern in his eyes."
            "Well, here goes - I'll show him!"
            scene poledance
            show poledance bree
            with fade
            "From nowhere the music starts up, and I just go for it."
            "I don't have a plan, just let the rhythm take me."
            "Before I know it, I'm hugging the pole as I begin to strip off."
            "It's like running really fast down a steep hillside."
            "I start out slow, feeling more than a little trepidation."
            "But soon I start to pick up speed, and it becomes exhilarating!"
            "I hardly realise that I'm already down to my underwear."
            "And as I tear these off too, the crows cheers me on."
            show poledance bree naked with dissolve
            "I know I'm drunk right now, okay."
            "But this feels so liberating, so empowering..."
            "Why didn't I think of doing something like this before!"
            "Most of the faces in the crowd remain a blur as I twist around the pole."
            "Oddly though, I always seem to be able to pick out Scottie's features."
            "And as I dance, the trepidation on his face is slowly replaced with something else."
            "It takes me a while, but finally I realise it's amazement, sheer and unadulterated amazement."
            "Well, that and more than a little naked lust..."
            "But wasn't that the point of getting up here in the first place?"
            "Once the dance is over and the music stops, I grab my clothes and hurriedly pull them back on."
            "Then I hurry back to the booth where Scottie is waiting for me."
            scene bg stripclub
            show scottie blush at center, zoomAt(1.5, (440, 1140))
            with fade
            scottie.say "That was..."
            scottie.say "Wow..."
            scottie.say "That was amazing, [hero.name]!"
            bree.say "Why thank you, Scottie!"
            bree.say "But I think that used up the last of my energy."
            bree.say "You think we could go home soon?"
            scottie.say "Yeah, [hero.name]!"
            scottie.say "Anything you say!"
            "I give Scottie a weak smile as he ushers me towards the exit."
            "And it feels good to have come here and conquered this place."
            scene bg alley with fade
            "As we leave I'm sure that I could come back here anytime and own the stage again."
            $ scottie.love += 2
            $ scottie.flags.delay = TemporaryFlag(True, 1)
            $ game.active_date.score = 100
            $ game.active_date.stay = False
            $ game.pass_time(2)
            return
        else:
            bree.say "Nice try, Scottie!"
            bree.say "But that's not going to happen!"
            show scottie blush
            scottie.say "Aw..."
            scottie.say "Please, [hero.name]?!?"
            bree.say "No way!"
            bree.say "You got me into a strip club."
            bree.say "And you got me to ogle girls with you too."
            bree.say "Don't try pushing your lucky, Scottie!"
            show scottie sad
            "Scottie gives a sigh of defeat and shrugs his shoulders."
            scottie.say "Ah..."
            scottie.say "It was worth a try!"
            show scottie -sad
            "With that he lets the matter drop and we get back to watching the show."
            "The rest of the night passes in the same way."
            "We sink more drinks and watch more girls dancing."
            "And by the time we're leaving, I'm struggling to see straight."
            scene bg alley with fade
            "My speech is kind of slurred too, making me talk crap."
            "And the world seems to be so simple, all a matter of black and white."
            "Shit - this must be what it's like to be Scottie!"
            "I need to get home and sober up quickly!"
            $ scottie.love += 2
            $ scottie.flags.delay = TemporaryFlag(True, 1)
            $ game.active_date.score = 25
            $ game.active_date.stay = False
            $ game.pass_time(2)
            return
    else:
        bree.say "Oh...my...god..."
        bree.say "Why didn't you just say you wanted to come do a strip club, Scottie?"
        bree.say "There was no need for all of the theatrics back there!"
        show scottie surprised
        "A puzzled look appears on Scottie's face."
        "It looks like I've thrown him off with my question."
        show scottie sad
        scottie.say "Well..."
        scottie.say "You might have said no, [hero.name]!"
        scottie.say "Some chicks are like that, yeah?"
        scottie.say "They only like a guy looking at them!"
        "I roll my eyes at this and shake my head."
        "Scottie really is too dumb for words most of the time."
        "And he's even more bone-headed when he's trying his best to be smart."
        bree.say "Yeah, Scottie, I might."
        bree.say "But I might not, you know?"
        bree.say "It's kind of nice when you give a girl a choice."
        bree.say "I shows that you respect her right to choose, Scottie!"
        show scottie -sad
        "Scottie actually looks like he's getting a little flushed."
        "Like he really gets the point I just made."
        scottie.say "Okay, [hero.name], okay."
        scottie.say "I'll ask next time, I promise!"
        scottie.say "So..."
        scottie.say "You don't want to leave?"
        "This isn't my idea of a typical date night."
        "But I'm not so uptight that I can't handle it."
        "I give Scottie a smile and shake my head."
        "He seems to have suffered enough."
        "So it's time to cut the poor guy some slack."
        bree.say "No, Scottie, I don't."
        bree.say "For the record, this looks like it could be fun."
        bree.say "But that doesn't mean I want to make a regular thing of it, okay?"
        "Now it's Scottie's turn to nod."
        show scottie happy
        "And I can see the relief on his face."
        scottie.say "That's great, [hero.name]!"
        scottie.say "Let's go grab a drink!"
        "We do just that, then we settle into a booth with a good view."
        "And I actually do find that I enjoy myself more than I thought I would."
        "But maybe a large part of that is because I get to watch Scottie the whole time."
        "My guess is that he thought this was going to be the best of both worlds."
        "That he's get to ogle the girls on stage and be with me at the same time."
        show scottie shy
        "But the truth is that he looks awkward whenever I catch him staring at the girls on stage."
        "And when I give him a sweet smile, he really doesn't know what to do with himself!"
        scene bg alley with fade
        "By the time we leave, Scottie's more confused than I've ever seen him."
        "And I can't help actually feeling sorry for the poor guy!"
        $ scottie.love += 1
        $ scottie.flags.delay = TemporaryFlag(True, 1)
        $ game.active_date.score = 50
        $ game.active_date.stay = False
        $ game.pass_time(2)
    return

label scottie_preg_talk:
    $ scottie.flags.toldpreg = True
    $ scottie.flags.know_is_father = True
    show scottie
    "I've been dreading this moment ever since I took the damn pregnancy test."
    "As if it wasn't bad enough dealing with the fact that I'm actually pregnant."
    "On top of that I also have to break the news to a meathead like Scottie."
    "Just my luck that I'd end up in a mess like this with him of all guys!"
    "And, as usual, it's not like Scottie helps matters."
    "I can't help thinking a smarter guy would have picked up on my mood by now."
    "Maybe not figured out what was wrong, but at least guess there was something up."
    "Instead, Scottie's his usual oblivious self."
    "So it looks like I'm going to have to do this the hard way..."
    bree.say "Ah, Scottie..."
    scottie.say "Huh?"
    scottie.say "What's up, [hero.name]?"
    bree.say "I...kind of have something I need to tell you."
    "Scottie looks around and then shrugs."
    scottie.say "Whatever, [hero.name]..."
    scottie.say "I'm right here."
    scottie.say "Lay it on me!"
    "I take a deep breath and try to prepare myself for the task ahead."
    "This is going to be tough!"
    bree.say "Okay, Scottie..."
    bree.say "This is going to be pretty hard for you to hear."
    bree.say "But I took a test the other day - and I was positive!"
    show scottie happy
    "Scottie surprises me by nodding and cracking a smile."
    scottie.say "That's my girl, [hero.name]!"
    scottie.say "You're always positive - always looking on the bright side!"
    "I stare at Scottie in complete amazement for a few seconds."
    "It's like my brain can't actually process just how dumb he really is."
    bree.say "No, Scottie, you moron!"
    bree.say "I'm talking a about a PREGNANCY test!"
    bree.say "And positive means I'm pregnant!"
    show scottie surprised at center, startle
    "Scottie's eyes almost pop out of his head as realisation dawns on him."
    "He shakes his head, like he's trying to jump-start his brain rather than show his disbelief."
    scottie.say "Whoa, [hero.name]..."
    scottie.say "That's crazy news!"
    scottie.say "But, like...who's the daddy?"
    "Now it's my turn to stare in genuine disbelief."
    bree.say "You are, you dimwit!"
    bree.say "I haven't been sleeping with anyone else."
    bree.say "And why in the hell would I be telling you if you weren't?!?"
    show scottie normal
    "Scottie holds his hands up as he backs off in the face of my rage."
    scottie.say "I...I dunno, [hero.name]!"
    scottie.say "Maybe because I'm such a cool guy?"
    scottie.say "Like a shoulder to cry on or something?"
    "I brush Scottie's feeble explanations aside."
    bree.say "No, Scottie..."
    bree.say "I'm telling you because this kid's yours!"
    bree.say "So what are you going to do about it?"
    if scottie.love >= 150:
        scottie.say "You mean it, [hero.name]?"
        scottie.say "I'm gonna be a dad?"
        scottie.say "Like, for real?!?"
        "I don't know what I was expecting from Scottie."
        "Maybe that he'd go into denial or try to worm his way out of it."
        "But I never thought he'd be excited at the prospect!"
        bree.say "Well...yeah, Scottie."
        bree.say "If we decide to keep it..."
        show scottie surprised
        "Suddenly I see a change come over Scottie's face."
        "Before he was confused and excited in equal measures."
        "But now he looks shocked, even horrified."
        scottie.say "Y...you mean like an abortion?!?"
        scottie.say "[hero.name], you just told me a second ago I was gonna be a dad."
        scottie.say "Now you're talking about getting rid of our kid?!?"
        "I can feel my cheeks flushing as Scottie stares at me."
        "I threw the mention of a termination in there because I kind of thought I had to."
        "I guess I was assuming he'd baulk at the mere mention of responsibility."
        "But now I'm starting to feel like a pretty cold bitch!"
        bree.say "I...I'm not saying that's what we have to do, Scottie!"
        bree.say "I'm just keeping an open mind, you know?"
        bree.say "I thought you might be against keeping it."
        show scottie normal
        scottie.say "Nah, [hero.name]!"
        show scottie happy
        scottie.say "I think we'd make great parents!"
        scottie.say "We should start a family."
        scottie.say "It'll be great!"
        "All I can do is smile and nod."
        "I'm starting to feel a little swept away by Scottie's enthusiasm."
        "But for the moment, I just go along with it."
        "Because it's better to have him on board than not."
    else:
        scottie.say "Wait a minute, [hero.name]..."
        scottie.say "It's YOU that's pregnant, right?"
        "I frown as soon as I hear the change in Scottie's tone."
        "All of a sudden the panic is gone, replaced by something else."
        "It's a sly tone of voice that I've heard him use on rare occasions."
        "One that reminds me of a dog that thinks it's being smart."
        bree.say "I'm the one carrying the baby, Scottie."
        bree.say "But you're still the father."
        "Scottie lets out a chuckle and grins."
        show scottie annoyed
        "Then he shakes his head and waves me away."
        scottie.say "Yeah, but I'm still right, aren't I?"
        scottie.say "You're the one having the baby, not me!"
        scottie.say "So the way I see it, this is your problem, not mine!"
        bree.say "Haven't you been listening to me this whole time?"
        bree.say "It doesn't matter who's carrying the baby."
        bree.say "As the father, you're responsible too!"
        bree.say "I...I'll take a DNA test to prove it if I have to!"
        show scottie angry
        scottie.say "No way, [hero.name]!"
        scottie.say "Your kid can't have my DNA - not if I don't want it to!"
        scottie.say "That'd be like breaking copyright or something!"
        "I can feel myself losing it with Scottie."
        "It's like I can't take anymore of his stupidity."
        bree.say "You wait and see, you deadbeat!"
        bree.say "I'll make sure you do what's right!"
        hide scottie with moveoutright
        "Scottie just chuckles again and starts to walk away."
        "Which makes me feel worse than ever."
        "I mean, do I really have the time and money to take him to court?"
        "And what am I going to get out of him even if I manage it?"
        "I feel like things just went from bad to worse for me."
        $ scottie.breakup()
    return


label scottie_kiss_me_female:
    call scottie_greet from _call_scottie_greet
    show scottie
    "I feel so guilty admitting that I'm getting the hots for Scottie."
    "I mean, he and Sasha are one hundred percent over, right?"
    "So it's not like I'm going behind her back with the guy, is it?"
    "Yeah, I know he's kinda dumb and he can he a jerk sometimes."
    "But can you really blame me when he's such a hottie?"
    "And those muscles too!"
    "But yeah, a little bit of it is because I want to know what it's like."
    "And a part of me wants to know what Sasha was getting before they split up too!"
    "I mean...Sasha's not that much prettier than me, right?"
    hide scottie
    show scottie kiss
    with dissolve
    $ scottie.flags.kiss += 1
    "I'm still thinking about all of that when I feel his lips against mine."
    "And from that moment on, everything else seems to disappear from my thoughts."
    "Oh god - he's kissing me!"
    "It's really happening - and it's everything I hope it would be!"
    hide scottie kiss with dissolve
    return

label scottie_find_out_pregnancy:
    $ scottie.flags.toldpreg = True
    show scottie annoyed
    "Scottie's got that look on his face, the one that I used to think meant he was constipated."
    show scottie at center, zoomAt(1.15, (640, 850))
    "But with more experience of his expressions, I now know that it actually means he's thinking."
    "Or at least what passes for thinking in Scottie's case."
    bree.say "What's up, Scottie?"
    show scottie surprised
    scottie.say "Huh?"
    bree.say "You look like you've got something on your mind."
    show scottie annoyed
    "In response to this, Scottie frowns and knits his brows."
    "But he nods all the same, letting me know I was right."
    scottie.say "Yeah, [hero.name]..."
    scottie.say "There's something different about you."
    scottie.say "I think you're that thing, you know?"
    bree.say "What thing is that, Scottie?"
    scottie.say "That thing where lady has a baby inside of her, yeah?"
    "I can't help rolling my eyes at Scottie's childish turn of phrase."
    "But I have to admit that he's right for once."
    bree.say "If you mean pregnant, Scottie..."
    bree.say "Then you're right - I am pregnant."
    show scottie surprised
    "Scottie's face contorts as he starts to digest the news."
    "But unfortunately for him, there's another surprise coming."
    menu:
        "It's yours":
            $ scottie.flags.know_is_father = True
            bree.say "There's one more thing you need to know, Scottie..."
            "I take a deep breath and then just say it out loud."
            bree.say "The baby's yours!"
            "Scottie looks puzzled at this revelation."
            "Which is odd, as I was expecting him to be shocked."
            show scottie normal
            scottie.say "Nuh-uh, [hero.name]!"
            scottie.say "You're the one that's pregnant."
            scottie.say "Not me!"
            "Oh geez - how dumb is this guy?!?"
            bree.say "I mean you're the father, Scottie!"
            if scottie.love >= 160:
                show scottie happy
                "Suddenly Scottie's expression changes."
                "He cracks a smile and looks genuinely elated."
                scottie.say "You really mean that, [hero.name]?"
                scottie.say "You're having MY kid?"
                bree.say "Of course I am, Scottie!"
                bree.say "It's not like I've been sleeping with anyone else, is it?"
                show scottie surprised
                "Scottie looks confused for a moment."
                scottie.say "Well I dunno, [hero.name]..."
                scottie.say "I have no clue how this stuff works!"
                bree.say "Well that is how it works, Scottie."
                bree.say "And...you're okay with that?"
                show scottie happy
                "Scottie's beaming again as he nods his head."
                scottie.say "Of course I am!"
                scottie.say "This is gonna be great, [hero.name]!"
                scottie.say "We're gonna have a baby!"
            else:
                show scottie sad
                "Scottie starts to shake his head."
                "And he backs off a little too."
                show scottie surprised
                scottie.say "Oh no..."
                scottie.say "Oh hell no!"
                bree.say "You can't just deny it, Scottie!"
                bree.say "That won't change the fact you're the father of my child!"
                show scottie angry
                scottie.say "Wait a minute..."
                scottie.say "You could be lying!"
                scottie.say "Yeah, that's it - you have to be lying!"
                bree.say "I promise you I'm not, Scottie!"
                bree.say "So what are you going to do about it?"
                if scottie.love >= 150:
                    show scottie sad
                    scottie.say "I dunno, [hero.name]..."
                    scottie.say "I dunno..."
                    "I can see that Scottie's brain is pretty fried right now."
                    "Well, what passes for a brain in his thick head, that is."
                    "So maybe the best thing is to back off a little."
                    "That way he might come around to the idea on his own."
                    bree.say "Look, Scottie..."
                    bree.say "I know this is a lot to process."
                    bree.say "So maybe you take some time, yeah?"
                    bree.say "Then hit me up when you've made sense of it all?"
                    show scottie normal
                    "Scottie nods slowly, starting to look a little more confident."
                    "That might be just because I've let him off the hook for a while."
                    "But it's the best I'm going to get right now."
                    "I smile."
                    show scottie happy
                    "Then he smiles."
                    hide scottie with easeoutright
                    "And then I watch him walk away, looking like he's in a daze."
                else:
                    show scottie sad
                    scottie.say "What am I gonna do about it?"
                    scottie.say "I'll tell you what I'm gonna do, [hero.name]..."
                    show scottie angry
                    scottie.say "I'm gonna dump your ass!"
                    "Now it's my turn to be shocked."
                    with vpunch
                    bree.say "WHAT?!?"
                    bree.say "Scottie, you dumb bastard!"
                    bree.say "You're as useless as you are stupid!"
                    hide scottie
                    show scottie angry
                    "Scottie's backing off for real now."
                    "Almost like he's scared of what I'm going to do next."
                    scottie.say "I'm gonna get out of here too!"
                    scottie.say "Right now!"
                    show scottie at right5 with move
                    "With that, Scottie turns on his heel."
                    hide scottie with moveoutright
                    "Then he literally runs away."
                    "Which leaves me standing alone, fuming in silence."
                    $ scottie.set_gone_forever()
        "It's not yours":
            bree.say "There's one more thing you need to know, Scottie..."
            "I take a deep breath and then just say it out loud."
            bree.say "The baby's not yours!"
            show scottie surprised
            "Scottie blinks and then just stares at me blankly."
            "But I'm used to this by now, and I wait for his brain to process the information."
            show scottie happy
            "And the first sign that this is happening comes when a smile spreads across his face."
            scottie.say "Whoa..."
            scottie.say "That's great news, [hero.name]!"
            bree.say "It is?"
            scottie.say "Yeah, [hero.name]..."
            scottie.say "It means I'm off the hook!"
            bree.say "So..."
            bree.say "You're okay with me having slept with another guy?"
            if scottie.love >= 140:
                show scottie sad
                scottie.say "Well..."
                scottie.say "That kinda sucks, [hero.name]."
                show scottie normal
                scottie.say "But I guess nobody's perfect."
                "I'm pretty surprised to hear something so reasonable come out of Scottie's mouth."
                bree.say "You're okay with it?"
                bree.say "I thought you'd dump me for sure?"
                "Scottie shakes his head."
                "But then another question occurs to me."
                menu:
                    "Ask Scottie to help with the baby":
                        bree.say "So if you're not going to dump me..."
                        bree.say "Will you help me with the baby?"
                        if scottie.love >= 160:
                            "Scottie shrugs and then nods."
                            scottie.say "I dunno what I can do to help, [hero.name]..."
                            scottie.say "But if you tell me what you need, I'll do my best."
                            "Sure, it's not the most reassuring promise of help."
                            "But it does sound genuine, and that makes up for a lot."
                        else:
                            "Scottie shakes his head."
                            scottie.say "You just told me this isn't my baby, [hero.name]!"
                            show scottie sad
                            scottie.say "And I don't know the first thing about them anyway."
                            scottie.say "So I dunno what I could do to help!"
                            "Sure, it's not the answer I was hoping for."
                            "But at least Scottie's being honest."
                            "And he's not making promises he can't keep."
                            $ scottie.breakup()
                    "I won't bother you about it":
                        pass
            else:
                show scottie surprised
                scottie.say "Wait...what?!?"
                scottie.say "How does that work?"
                bree.say "Well..."
                bree.say "If you're not the father, Scottie..."
                bree.say "Then I must have slept with someone else!"
                show scottie annoyed
                "Scottie's face darkens as I explain the situation to him like I would to a simpleton."
                "And it looks like he finally gets what I've been trying to tell him."
                show scottie angry
                scottie.say "Wait..."
                scottie.say "You slept with someone else?!?"
                scottie.say "That's it, [hero.name]!"
                scottie.say "You're on the express train to Dumpsville, population one!"
                scottie.say "And the one's you, by the way!"
                bree.say "Well, duh!"
                bree.say "But what about the baby, Scottie?"
                show scottie surprised
                "Scottie looks at me like I'm not making sense."
                scottie.say "What's that got to do with me?"
                show scottie sad
                scottie.say "You just told me it's not mine."
                show scottie angry
                scottie.say "So it's not my problem!"
                hide scottie
                show scottie angry
                "Scottie turns on his heel and starts to walk away."
                show scottie at right5 with move
                bree.say "That's it?"
                bree.say "You're just going to walk away?!?"
                show scottie at right with move
                scottie.say "I'm gonna find someone that won't sleep with other guys!"
                scottie.say "And isn't knocked-up either!"
                hide scottie with moveoutright
                $ scottie.set_gone_forever()
    return

label scottie_birthday_date_female:
    $ DONE["scottie_birthday_date_female"] = game.days_played
    $ game.active_date.clothes = "swimsuit"
    scene bg beach with fade
    "I finally managed to winkle the date of Scottie's birthday out of him."
    "And as luck would have it, that happened only a few days before it was coming up."
    "So after putting our heads together, we decided that we should do something too mark the occasion."
    "Well, more like I decided that we should do something special."
    "Scottie would have been happy to just hang around at my place and drink beer all day!"
    "But in the end I was able to convince him that we should spend the day at the beach instead."
    "The weather report said that it was going to be a sunny day, and so far it's been right."
    "The only problem is that I got held up on the way to the beach."
    "So as I hurry along the path that leads to the sand, I know that I'm already late."
    "I just hope that Scottie isn't too mad at me for being so tardy."
    show scottie swimsuit happy at left with dissolve
    "Suddenly I spot him up ahead, and I feel a surge of relief."
    "And that's because he has a huge smile plastered across his face."
    show scottie at center, zoomAt(1.25, (640, 880))
    "But as I get closer, that relief turns into irritation."
    "That's because I can now see exactly what Scottie's doing over there."
    "He keeps pulling poses that show off his muscles."
    "And there's a crowd of girls in their swimsuits urging him on."
    "As soon as he finishes posing, they all start flaunting themselves in his general direction!"
    show scottie joke
    "Scottie's all smiles and winks."
    "And they're all giggles and blowing kisses."
    "I can already feel my blood starting to boil at the sight of them."
    "But luckily for me, Scottie's not seen me yet and none of the girls seem familiar."
    "All of which means the ball is firmly in my court."
    menu:
        "Demand to know what Scottie's doing":
            "Part of me wants to just turn right around and go home."
            "Our date hasn't even officially started yet."
            "And Scottie's already flirting with other girls!"
            "But I decide that I have to hear his explanation."
            show scottie at center, zoomAt(1.5, (640, 1040))
            "So I walk straight up to him and make my feelings known."
            bree.say "SCOTTIE!"
            bree.say "What the hell are you doing?!?"
            show scottie surprised at startle
            "At the sound of my voice, Scottie literally jumps into the air."
            "He spins around to face me at the same time, a look of horror on his face."
            scottie.say "[hero.name[0]]...[hero.name]?"
            scottie.say "When did you get here?"
            "I cross my arms over my chest."
            "And I give Scottie my best pissed-off glare."
            bree.say "In time to see you flirting with those bimbos!"
            bree.say "What were you doing, Scottie?"
            bree.say "Picking which one you'd hit on if I didn't show?"
            show scottie annoyed
            "Scottie waves his hands in front of him and shakes his head."
            scottie.say "Oh, come on, [hero.name]..."
            scottie.say "It wasn't like that."
            show scottie embarrassed
            scottie.say "Those girls just asked me to show them my muscles, that's all!"
            bree.say "Yeah, and then they'd have been asking to see something else too."
            bree.say "Something that starts out soft and gets hard!"
            show scottie annoyed
            scottie.say "Okay, okay...I get it, [hero.name]!"
            scottie.say "And I'm sorry, yeah?"
            scottie.say "I'll do whatever it takes to make it up to you - I promise!"
            bree.say "You'd better, Scottie."
            bree.say "Because as of right now, you're on probation, Mister!"
            $ game.active_date.score -= 10
            "Scottie looks crestfallen, but he nods all the same."
        "Try to beat the girls at their own game":
            "Part of me wants to walk right over there and give Scottie a piece of my mind."
            "But then I wonder what's really bothering me about all of this."
            "Scottie flirts with other girls all the time, sometimes without even realising it."
            "So could it be the fact that he's not giving me attention that's the problem?"
            "Well, we can soon do something about that."
            "I'm wearing a swimsuit, just like those girls."
            "And the last time I checked, Scottie liked the look of me in one of those too."
            bree.say "Hey, Scottie..."
            bree.say "Sorry to keep you waiting."
            bree.say "Did you miss me?"
            show scottie surprised
            "As soon as Scottie turns in my direction, I leap into action."
            show scottie at center, zoomAt(1.5, (640, 1040))
            "I walk towards him while making sure that my body moves in a seductive manner."
            "Honestly it's more of a swagger than a walk, everything rolling and bouncing."
            "I'm also careful to run my hand through my hair and toss my head just so."
            show scottie perv
            "All of which adds to the effect I can see that I'm having on Scottie right now."
            "I do the best I can not to chuckle to myself as his jaw drops open."
            "And I can tell that all of his attention is focused on me now."
            "It's almost as if the other girls had ceased to exist altogether."
            $ game.active_date.score += 15
            scottie.say "WHOA!"
            scottie.say "[hero.name]..."
            scottie.say "You look SO amazing!"
            bree.say "Why, thank you, Scottie."
            bree.say "Aren't you going to introduce me to your new friends?"
            show scottie surprised
            scottie.say "Huh?"
            scottie.say "Who are you even talking about?"
            "I point to the other girls."
            "Making sure they know I'm talking about them."
            bree.say "Those girls there, Scottie."
            bree.say "The ones you were showing-off for just now."
            show scottie embarrassed
            scottie.say "Oh, forget them, [hero.name]!"
            scottie.say "They're just some random girls that showed up."
            show scottie perv
            scottie.say "I don't care about them, not now that you're here!"
            "The girls all frown and shout abuse at Scottie."
            "But he doesn't hear it, or else he chooses to ignore it on purpose."
            "Then he offers me his arm and I take it."
            "And we walk away to the sound of the snubbed girls protests."
    show scottie normal with fade
    "It doesn't take us long to find a decent spot on the beach."
    "And pretty soon we're spreading out our towels on the sand."
    "Now that we're settled, we sit down and start to enjoy our little part of the beach."
    "Scottie squints and holds a hand up to his eyes as he surveys the area."
    scottie.say "Wow..."
    scottie.say "I hope the sun doesn't get any hotter!"
    scottie.say "I don't think I could take it."
    bree.say "Hmm..."
    bree.say "It's close to midday."
    bree.say "I think this is about as hot as it's going to get."
    bree.say "We should probably stay put until it cools down a little."
    bree.say "But we need to put on some sun-block so we don't burn."
    show scottie happy
    "Scottie's face seems to light up at the mention of putting on sun-block."
    scottie.say "Alright, [hero.name]!"
    scottie.say "Does that mean I get to rub some one you?"
    bree.say "I don't know about that, Scottie."
    bree.say "I usually like to put it on myself."
    bree.say "That way I can be sure it's even and that I didn't miss a spot."
    show scottie sad
    "As quickly as it lit up before, Scottie's face now falls."
    "And he looks at me with the eyes of a puppy that's been denied a treat."
    menu:
        "Relent and let Scottie put on you sun-block":
            "I know that I should stick to my guns on this one."
            "But the puppy-dog eyes are just too much for me."
            "And it is his birthday too."
            "So giving in isn't as bad as it would be otherwise."
            bree.say "Okay, Scottie..."
            bree.say "Here you go."
            show scottie happy
            $ game.active_date.score += 15
            "Scottie's smile returns as I hand him the sun-block."
            bree.say "But you'd better do a good job..."
            bree.say "You hear me?"
            show beach cream scottie swimsuit with fade
            "Scottie nods eagerly as I lie down and get comfortable."
            "And I have to admit, what follows is a pretty pleasant experience."
            "I mean, I don't know if he covers every spot as well as I'd have liked."
            "But the feel of his hands on my body is really nice."
            "Especially where he lingers in order to make sure the sun-block is really rubbed in."
            "Although I do note that he returns to a few spots I thought were already done."
            "And he tends to linger in spots that are a little out of the way."
            "You know the ones that I mean - the softer, squishier parts of the female anatomy."
            "But I decide to let it slide."
            "Because I am letting him do this as a birthday treat."
            "And okay, I admit it - I'm enjoying it too!"
        "Stick to your guns an puts on your own sun-block":
            "I tear my gaze away before Scottie can make me feel guilty."
            "And I shake my head to make my stance on the matter clear."
            bree.say "Don't give me that look, Scottie!"
            bree.say "I just want to do this one thing for myself, okay?"
            scottie.say "Okay, [hero.name], okay..."
            $ game.active_date.score -= 10
            "Scottie sighs as he squeezes out a handful of sun-block."
            "And then he starts to rub it all over himself in earnest."
            "I do the best I can to ignore what he's doing."
            "But it's applying the sun-block to myself that helps the most."
            "It requires me to concentrate and make sure I do a good job."
            "So soon all thought of Scottie and his pouting fade into the background."
            "Once I have every exposed part of my body covered, it's time to relax."
            "And that involves lying back on my towel and closing my eyes."
            "I can still hear Scottie muttering to himself as I wait for the sun to get lower in the sky."
            "But I tell myself that it wasn't worth the risk of skin-cancer just to make him happy."
            "Even if it is his damn birthday!"
    scene bg beach with fade
    "I'm having such a nice time just lying in the sun that I seem to lose track of time."
    "In fact, I think I might have dozed off for a short while, actually been asleep."
    "Because the sound of Scottie's voice jolts me back to reality when he speaks."
    scottie.say "Hey, [hero.name]!"
    bree.say "Wha..."
    bree.say "What the..."
    bree.say "I don't wanna go to school, Daddy!"
    show scottie swimsuit joke at center, zoomAt(1.5, (640, 1040)) with dissolve
    scottie.say "Erm..."
    scottie.say "Who mentioned anything about school, [hero.name]?"
    scottie.say "But, if you really want to call me Daddy..."
    scottie.say "I guess I can go with that!"
    bree.say "Urgh...no way, Scottie!"
    bree.say "I'm just a little groggy, that's all."
    show scottie sad
    "Scottie looks a tiny bit disappointed."
    "But he nods all the same."
    show scottie normal
    scottie.say "Whatever, babe..."
    scottie.say "I was just wondering - is it time to do some stuff yet?"
    if randint(0, 2) == 0:

        scottie.say "Like..."
        scottie.say "Do you know what time it is?"
        scottie.say "I'd look at my phone."
        scottie.say "But it's buried at the bottom of my bag."
        if hero.knowledge >= 75:
            "I squint as I sit up, considering Scottie's question."
            "And it's the sun making me do so that stirs a memory."
            "I'm sure I can recall my dad telling how to use the position of the sun to tell the time."
            "Now if I can just remember how to do it..."
            bree.say "You need to calculate the hour angle of the sun, Scottie."
            show scottie surprised
            scottie.say "You need to do the what now?!?"
            bree.say "You figure out the angle of the sun against a reference point."
            bree.say "And that should tell you roughly what time it is."
            "I'm already looking for a likely reference point."
            "And as soon as I find one, I hold up a hand to check the angle."
            bree.say "There you go, Scottie..."
            bree.say "It's a little after two."
            bree.say "Perfect time to get up and do something fun!"
            "Scottie looks at me with disbelief written all over his face."
            "Then he scrambles for his bag and retrieves his phone."
            scottie.say "No way!"
            show scottie happy
            scottie.say "You're right, [hero.name]."
            scottie.say "You must be some kind of genius!"
            $ game.active_date.score += 15
            "I know that I should tell Scottie I'm not."
            "But maybe I'll do that a little later."
            "No harm in letting him think that for a short while."
        else:
            "I look up at the sky, my eyes still bleary from sleep."
            "And I instantly regret it, as the sun blinds me."
            bree.say "Jesus..."
            bree.say "I can tell you that the sun's still out, Scottie."
            bree.say "But that's about the only thing I know!"
            show scottie sad
            $ game.active_date.score -= 10
            "Scottie looks disappointed with my answer."
            "He shrugs and refuses to meet my eye."
            scottie.say "Huh..."
            scottie.say "I thought you might know how to tell from the sun or something."
            scottie.say "Like how long the shadows are and stuff?"
            scottie.say "I kinda thought you were smart, [hero.name]!"
            bree.say "What do you want from me, Scottie?"
            bree.say "A lecture or something?"
            bree.say "Just look at your phone like a normal person!"
    elif randint(0, 2) == 1:

        scottie.say "I was just wondering, [hero.name]..."
        scottie.say "You wanna go play a little volleyball?"
        scottie.say "Looks like the court is empty right now."
        scottie.say "So we could play a little one-on-one!"
        "I'm still stretching the sleep out of my body as Scottie asks the question."
        "But the idea strikes me as a pretty good one, so I nod in agreement."
        bree.say "Sure, Scottie - let's go."
        scene beach volleyball
        show beach volleyball scottie
        with fade
        if hero.fitness >= 75:
            "We hurry over to the volleyball court before anyone else can take the spot."
            "And Scottie doesn't waste any time in launching the ball over the net."
            scottie.say "Get ready, [hero.name]..."
            scottie.say "Because I'm not taking any prisoners!"
            "I nod and hurry to intercept the ball."
            "But from that moment on, everything falls into place for me."
            "My hands strike the ball perfectly, sending it straight back."
            "And Scottie struggles to get under it as best he can."
            "My moves make him fumble, stumble and even fall."
            "But the end finally comes when I blast the ball at him."
            "Scottie goes for it, but overreaches badly."
            "The ball sails past him as he goes plummeting into the sand."
            "The sand flying into the air."
            "His face getting buried in it."
            "Even the cry he lets out sounds like a drawn-out moan to my ears."
            "Spitting out sand, he looks up as I walk over to him."
            $ game.active_date.score += 15
            "But he smiles as I help him up."
            scottie.say "Ouch..."
            scottie.say "Did you see that, [hero.name]?"
            scottie.say "I was...letting you win."
            scottie.say "Yeah, that's it - I was letting you beat me!"
        else:
            "We hurry over to the volleyball court before anyone else can take the spot."
            "And Scottie doesn't waste any time in launching the ball over the net."
            scottie.say "Get ready, [hero.name]..."
            scottie.say "Because I'm not taking any prisoners!"
            "I nod and hurry to intercept the ball."
            "But from that moment on, nothing seems to go right for me."
            "I stumble and miss the ball, awarding the first point to Scottie."
            "Then I proceed to fumble, trip and fall my way through the game."
            "The end finally comes when I make one last effort to blast the ball back over the net."
            "But all I manage to do is overreach myself and miss by a country mile."
            "The ball sails past me as I go plummeting into the sand."
            "Everything seems to happen in slow-motion."
            scene bg beach with hpunch
            "The sand flying into the air."
            "My face getting buried in it."
            "Even the cry I let out sounds like a drawn-out moan to my ears."
            show scottie swimsuit sad with dissolve
            "Spitting out sand, I look up to see Scottie standing over me."
            "And he has a worried look on his face as he helps me up."
            scottie.say "Ouch..."
            scottie.say "Maybe this wasn't such a good idea after all?"
            $ game.active_date.score -= 10
    else:

        scottie.say "It's still so hot, [hero.name]!"
        scottie.say "I feel like I'm gonna pass out from it or something."
        bree.say "Yeah, Scottie..."
        bree.say "Me too!"
        "I take a moment to glance around."
        "And my eyes soon settle on the ice-cream stand."
        bree.say "Hey, Scottie..."
        bree.say "Ice-cream?"
        show scottie happy
        scottie.say "Great idea, [hero.name]!"
        scottie.say "Let's go!"
        $ renpy.show("beach_icecream_bg", tag="first_tag")
        $ renpy.show("beach_icecream_seller", tag="second_tag")
        $ renpy.show("beach_icecream_seller_outfit", tag="third_tag")
        with fade
        "We both leap up and hurry over to the ice-cream stand."
        "But just as we get there, I see the member of staff behind the counter putting up a sign."
        "A sign that has the word 'Closed' written on it too!"
        scottie.say "Ah, bummer!"
        scottie.say "We're out of luck, [hero.name]."
        bree.say "Maybe not, Scottie."
        bree.say "Leave this to me."
        "I take a deep breath and walk over to the stand."
        if hero.charm >= 75:
            bree.say "Hey there!"
            bree.say "Can I get two ice-creams please?"
            "At the sound of my voice, the staff member turns around."
            "But they don't look too pleased to see me."
            "Staff member" "Nah, sorry..."
            "Staff member" "We just closed."
            "They point at the sign."
            "And I look down at it as if I never saw the thing before."
            "Then I look back up and give them a smile."
            bree.say "Oh don't worry."
            bree.say "I'll let it go this time."
            bree.say "So long as you're quick with the ice-cream."
            "The staff member looks confused."
            "And they shake their head at me."
            "Staff member" "Erm..."
            "Staff member" "I already said we were closed."
            bree.say "I know, but I was here before you put the sign up."
            bree.say "You just weren't paying attention, that's all."
            bree.say "But I won't tell your manager, this time at least."
            "I add a sweet smile."
            "But I raise my eyebrows just to make plain that I'm serious."
            "Staff member" "Oh...okay, okay..."
            scene beach icecream
            show beach icecream scottie
            with fade
            "The staff member hurries to make the ice-creams and hand them over."
            $ game.active_date.score += 15
            "Then I pay, hand one to Scottie and we walk away happily."
        else:
            bree.say "Excuse me..."
            bree.say "Are you closed right now?"
            "The member of staff behind the counter looks up at me."
            "Then they look down at the sign they just put up."
            "Staff member" "That's what the sign says."
            "Staff member" "So I guess we are."
            "That said, they turn away to resume doing whatever they were doing."
            bree.say "Excuse me!"
            bree.say "I wasn't done talking to you yet."
            "Without turning to face me, the staff member shrugs."
            "Staff member" "Well I'm done talking to you."
            "Staff member" "This conversation's over."
            bree.say "You're being very rude and unhelpful."
            bree.say "You know that, right?"
            "Staff member" "And you're distracting me from my work."
            "Staff member" "So I guess we're about even."
            bree.say "How dare you!"
            bree.say "I want to talk to your manager!"
            "Staff member" "What are you, lady?"
            "Staff member" "A Karen in training?"
            "I open my mouth to say something in return."
            "But then the implications of the insult really hit home."
            "I feel my cheeks flushing and I turn to run away."
            show scottie swimsuit surprised
            scottie.say "What's up, [hero.name]?"
            scottie.say "Are we getting ice-cream or not?"
            bree.say "No, Scottie..."
            bree.say "We are not!"
            $ game.active_date.score -= 10
    scene bg beach with fade
    "Now that the sun's lower in the sky, we can pretty much do what we please."
    "And the first thing that we do is take a long, relaxing walk along the beach."
    "This takes us away from the water and closer to the dunes, where the tall grasses grow."
    "Scottie and I are just talking as we walk, chatting about whatever comes to mind."
    show scottie swimsuit annoyed with dissolve
    "But I can see that his attention keeps being drawn to the long grass."
    "It's like he can see something moving in there, but can't tell what it is."
    bree.say "Are you okay, Scottie?"
    bree.say "What is it you see in there?"
    bree.say "Another one of those pesky squirrels?"
    "Scottie shakes his head as he gazes over the dunes."
    scottie.say "Nah, [hero.name]..."
    scottie.say "I'd know if it was one of those evil little bastards!"
    scottie.say "This is much bigger, about the size of a man..."
    "I'm about to ask Scottie what in the hell it could be."
    hide scottie with easeoutright
    "But before I can say anything, he tenses and then springs into the grass."
    "I can hear a strangled cry and then a lot of thrashing about."
    "Then there are voices coming from the same direction."
    scottie.say "Hah!"
    scottie.say "Got you now, you old pervert!"
    master.say "Unhand me, you young whipper-snapper!"
    master.say "Or else you'll regret it, I swear!"
    show scottie swimsuit angry at left4
    show master sad noglasses at right4
    with easeinright
    if Person.is_not_hidden("master"):
        "As Scottie emerges from the grass, I see he's holding onto someone."
        "It's a wrinkled-up old man in Bermuda shorts and a loud Hawaiian shirt."
        "Scottie has him by the scruff of his neck and keeps shaking him every now and then."
        scottie.say "This guy was watching us from in there, [hero.name]."
        scottie.say "And when I caught him, he had his hand in his pants too!"
        bree.say "Master?"
        bree.say "Is that you?!?"
        scottie.say "Huh?"
        scottie.say "You know this old creep?"
        bree.say "Yeah, I do."
        bree.say "He taught me martial arts."
        bree.say "Or at least that's what he told me he was doing at the time."
        master.say "No, no, no, no!"
        master.say "This is all just a big misunderstanding."
        master.say "I was meditating, that's all."
        master.say "A technique that requires manipulation of the groinal chakra."
        master.say "One that needs controlled breathing too."
        master.say "Hence all the panting and groaning."
        master.say "You have to believe me!"
        show master at hshake
        "Scottie shakes the old man one more time, making him yelp."
        "And then he looks at me, genuine annoyance in his eyes."
        scottie.say "You want me to rough him up a bit, [hero.name]?"
        scottie.say "I think he needs to be taught a lesson!"
        menu:
            "Tell Scottie to beat-up the Master":
                "I don't hesitate to nod my head."
                "The Master's had this coming for a long time."
                bree.say "Yeah, Scottie..."
                bree.say "He deserves to get his ass-kicked!"
                scottie.say "Alright!"
                scottie.say "Watch me kick some old man ass!"
                master.say "Be warned..."
                master.say "I am a master of the mystical combat arts!"
                "Scottie laughs and nods his head at this."
                scottie.say "Ah, ah!"
                scottie.say "One punch!"
                scottie.say "All I am going to do is one lousy punch!"
                show master angry at mostright4 with ease
                "But then the old man squares up to Scottie, fists raised."
                master.say "Hmm, so one punch it is!"
                master.say "{cps=20}Kaaaa -{/cps}{w=0.85}{nw}"
                master.say "{cps=20}meeee -{/cps}{w=0.85}{nw}"
                master.say "{cps=20}haaaa -{/cps}{w=0.85}{nw}"
                master.say "{cps=20}doooo -{/cps}{w=0.85}{nw}"
                play sound punch_hard
                pause 0.2
                scene bg beach
                $ renpy.show(f"master beats {active_girl.id}")
                master.say "{cps=30}KEEEEEEEEEEEEEEEEEENNN!!!{/cps}" with hpunch
                "And then he surprises everyone by literally shooting a fireball!"
                "The fireball hits Scottie square in the chest, and he crashes to the ground."
                $ game.active_date.score -= 10
                scottie.say "OOF!"
                "As I stand petrified, the Master walks away from his defeated opponent."
                "And then I rush to Scottie."
                scene bg beach
                show scottie swimsuit angry at center, zoomAt(1.5, (640, 1040))
                "I am relieved to see that his pride is more hurt than his body."
                scottie.say "Dirty old creep!"
                scottie.say "He's lucky I was holding back, [hero.name]!"
            "Tell Scottie to let the Master go":
                "Part of me is so mad at being perved over I want to say yes."
                "But I just can't bring myself to wish something like that on him."
                "The Master just looks so frail and pathetic as he squirms in Scottie's grasp."
                bree.say "No, Scottie..."
                bree.say "He looks scared enough already."
                bree.say "You should let him go."
                "Scottie shakes his head."
                "And for a moment I think he's going to argue."
                "But then he lets the Master go."
                "Though not before he lands a kick on his fast-retreating backside."
                scottie.say "Dirty old creep!"
                scottie.say "He's lucky you were here to hold me back, [hero.name]."
                $ game.active_date.score += 15
    else:
        "As Scottie emerges from the grass, I see he's holding onto someone."
        "It's a wrinkled-up old man in Bermuda shorts and a loud Hawaiian shirt."
        "Scottie has him by the scruff of his neck and keeps shaking him every now and then."
        scottie.say "This guy was watching us from in there, [hero.name]."
        scottie.say "And when I caught him, he had his hand in his pants too!"
        bree.say "Eww!"
        bree.say "That's SO disgusting!"
        master.say "No, no, no, no!"
        master.say "This is all just a big misunderstanding."
        master.say "I was meditating, that's all."
        master.say "A technique that requires manipulation of the groinal chakra."
        master.say "One that needs controlled breathing too."
        master.say "Hence all the panting and groaning."
        master.say "You have to believe me!"
        show master at hshake
        "Scottie shakes the old man one more time, making him yelp."
        "And then he looks at me, genuine annoyance in his eyes."
        scottie.say "You want me to rough him up a bit, [hero.name]?"
        scottie.say "I think he needs to be taught a lesson!"
        menu:
            "Tell Scottie to beat-up the Master":
                "I don't hesitate to nod my head."
                bree.say "Yeah, Scottie..."
                bree.say "He deserves to get his ass-kicked!"
                scottie.say "Alright!"
                scottie.say "Watch me kick some old man ass!"
                master.say "Be warned..."
                master.say "I am a master of the mystical combat arts!"
                "Scottie laughs and nods his head at this."
                scottie.say "Ah, ah!"
                scottie.say "One punch!"
                scottie.say "All I am going to do is one lousy punch!"
                show master angry at mostright4 with ease
                "But then the old man squares up to Scottie, fists raised."
                master.say "Hmm, so one punch it is!"
                master.say "{cps=20}Kaaaa -{/cps}{w=0.85}{nw}"
                master.say "{cps=20}meeee -{/cps}{w=0.85}{nw}"
                master.say "{cps=20}haaaa -{/cps}{w=0.85}{nw}"
                master.say "{cps=20}doooo -{/cps}{w=0.85}{nw}"
                play sound punch_hard
                pause 0.2
                scene bg beach
                $ renpy.show(f"master beats {active_girl.id}")
                master.say "{cps=30}KEEEEEEEEEEEEEEEEEENNN!!!{/cps}" with hpunch
                "And then he surprises everyone by literally shooting a fireball!"
                "The fireball hits Scottie square in the chest, and he crashes to the ground."
                $ game.active_date.score -= 10
                scottie.say "OOF!"
                "As I stand petrified, the old man walks away from his defeated opponent."
                "And then I rush to Scottie."
                scene bg beach
                show scottie swimsuit angry
                with fade
                "I am relieved to see that his pride is more hurt than his body."
                scottie.say "Dirty old creep!"
                scottie.say "He's lucky I was holding back, [hero.name]!"
            "Tell Scottie to let the Master go":
                "Part of me is so mad at being perved over I want to say yes."
                "But I just can't bring myself to wish something like that on him."
                "The old man just looks so frail and pathetic as he squirms in Scottie's grasp."
                bree.say "No, Scottie..."
                bree.say "He looks scared enough already."
                bree.say "You should let him go."
                "Scottie shakes his head."
                "And for a moment I think he's going to argue."
                show scottie at center
                hide master
                with easeoutright
                "But then he lets the old man go."
                "Though not before he lands a kick on his fast-retreating backside."
                scottie.say "Dirty old creep!"
                scottie.say "He's lucky you were here to hold me back, [hero.name]."
                $ game.active_date.score += 15
    scene bg beach with fade
    "Scottie and get back to the spot we dropped our towels a few minutes later."
    show scottie swimsuit at center, zoomAt(1.75, (640, 1240)) with dissolve
    "He sits down and does the best he can to seem nonchalant about it."
    show scottie embarrassed
    "But Scottie's not fooling me, because he's kind of like a dog trying to be secretive."
    "No matter how hard her tries, it written all over his face and his actions alike."
    bree.say "Come on, Scottie..."
    bree.say "Out with it!"
    show scottie surprised
    scottie.say "H...how did you know that, [hero.name]?"
    scottie.say "How do you always know?!?"
    bree.say "I dunno, Scottie."
    bree.say "I guess I must be psychic or something."
    "Scottie looks at me like he might actually think I'm being serious."
    "And the he proceeds to spill his guts."
    show scottie normal
    scottie.say "Well..."
    scottie.say "I was kinda wondering if you got me a present..."
    scottie.say "You know, because it's my birthday and stuff?"
    if not hero.has_gifts:
        "Damn it!"
        "I knew there was something that I'd forgotten."
        "But maybe I can still wriggle my way out of this one."
        bree.say "Erm..."
        bree.say "You didn't want a gift this year, Scottie."
        bree.say "You told me yourself - don't you remember?"
        "Scottie stares at me blankly for a moment."
        show scottie sad
        "Then he shakes his head and shrugs."
        scottie.say "Huh..."
        scottie.say "That doesn't sound like something I'd say."
        scottie.say "But if you say so, [hero.name]...then it must be true."
        scottie.say "Because I know you'd never lie to me."
        $ game.active_date.score -= 20
        "I nod and smile, trying to keep a straight face."
        "While at the same time I can feel guilt twisting my guts."
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_22
        if _return != "done":
            if _return not in ["None", "exit"]:
                bree.say "Of course I got you something, Scottie."
                bree.say "I have it right here..."
                "I reach into my bag and pull out the gift."
                "Then I hand it over to Scottie."
                play sound [paper_ripping_1, paper_ripping_2]
                "He takes it and eagerly starts to tear off the wrapping paper."
                "But he stops in his tracks when he sees what's inside."
                if _return:
                    show scottie happy
                    scottie.say "WHOA!"
                    bree.say "What's the matter, Scottie?"
                    bree.say "Is it what you wanted?"
                    scottie.say "You bet it is, [hero.name]."
                    scottie.say "This is perfect!"
                    scottie.say "It's the best present ever!"
                    $ game.active_date.score += 15
                    "I can't help smiling as Scottie stares in amazement at his gift."
                    "It was pretty hard to get my hands on."
                    "But so worth it to be able to bask in this much glory."
                else:
                    show scottie surprised
                    scottie.say "Huh..."
                    bree.say "What's the matter, Scottie?"
                    bree.say "Don't you like it?"
                    show scottie happy
                    scottie.say "No, [hero.name]..."
                    show scottie sad
                    scottie.say "It's great, really...great."
                    $ game.active_date.score -= 10
                    "It's not hard to tell when Scottie's lying."
                    "But I decide not to press him any further."
                    "I already feel humiliated by his reaction."
                    "And I don't want to make it any worse than it already is."
            else:
                "Damn it!"
                "I knew there was something that I'd forgotten."
                "But maybe I can still wriggle my way out of this one."
                bree.say "Erm..."
                bree.say "You didn't want a gift this year, Scottie."
                bree.say "You told me yourself - don't you remember?"
                "Scottie stares at me blankly for a moment."
                show scottie sad
                "Then he shakes his head and shrugs."
                scottie.say "Huh..."
                scottie.say "That doesn't sound like something I'd say."
                scottie.say "But if you say so, [hero.name]...then it must be true."
                scottie.say "Because I know you'd never lie to me."
                $ game.active_date.score -= 20
                "I nod and smile, trying to keep a straight face."
                "While at the same time I can feel guilt twisting my guts."
    scene bg beach with fade
    "The afternoon's drawing on by now, and the sun's starting to sink lower in the sky."
    "I can already feel a chill coming in on the breeze, signalling a change in the weather."
    "All of which tells me that it'll soon be time to pack up and head for home."
    "With that in mind, I start to put a few things back into my bag."
    show scottie swimsuit at center, zoomAt(1.75, (640, 1240)) with dissolve
    scottie.say "What are you doing, [hero.name]?"
    scottie.say "It's not time to go home yet, is it?"
    bree.say "Not right now, Scottie."
    bree.say "But it soon will be."
    scottie.say "Not before I've been in the waves it won't!"
    scene bg beach
    show scottie happy swimsuit
    with fade
    "Scottie leaps up and starts to run towards the water."
    scottie.say "Come on, [hero.name]!"
    hide scottie with easeoutleft
    "Scottie sprints the short distance to the water."
    "And he's waving for me to follow him the whole way."
    "But when I don't come as quickly as he'd like, he kicks at the water."
    "And it's strong enough for me to be splashed pretty heavily!"
    with hpunch
    bree.say "Arrgh!"
    bree.say "I'm soaked!"
    menu:
        "Move your towel further up the beach to get away":
            "Frowning at Scottie, I pick up my towel and move out of range."
            "I have my back to him the whole time I'm doing this."
            "And when I turn back I can see that Scottie's still looking at me."
            "From the look on his face, he doesn't seem to get that I'm pissed at him."
            "So I make a point of sitting back down and looking away."
            "When I finally take the time to look again, he's not there."
            "And I have to scan around to find out where he's gone."
            "Then I feel myself getting annoyed as I see what he's doing."
            "Scottie's showing-off to those same girls from earlier!"
            "I do the best to catch his eye, but he doesn't look in my direction."
            "So all I can do is sit there and watch him splashing around with them."
            "By the time he comes walking out of the water, I'm seriously pissed."
            "But I have to do the best I can to make it look like I couldn't care less."
            "Because if I don't, he'll know that I was jealous!"
            $ game.active_date.score -= 10
        "Go down to the water to get Scottie back":
            show playing water beach scottie with fade
            "Now it's my turn to leap up and run down to the water."
            "And once I'm there, I don't hesitate to splash Scottie back."
            "He seems to approve of this, because he returns the favour."
            "And within a short space of time we're both dripping wet."
            "But after that we just keep on playing."
            "Fooling around in the water like we don't have a care in the world."
            $ game.active_date.score += 15
            "This should be tiring me out, using up the last of my energy."
            "As we've been here most of the day, and the weather's been warm."
            "But instead the coolness of the water reinvigorates me."
            "Once we finally choose to walk back to the sand, I check the time."
            "And I'm amazed to find that we've been out there longer than I thought."
            "Now it really is getting towards a time when we should be leaving the beach."
    scene bg beach
    show scottie swimsuit
    with fade
    "With our things packed away, Scottie and I begin to walk away from the sand."
    "I think we both know that the date's coming to a natural end."
    "Though I find myself wondering if it's the end of the day altogether."
    bree.say "So what are your plans now, Scottie?"
    bree.say "Are you heading straight home?"
    bree.say "Or have you got something else planned for later?"
    if game.active_date.score >= 80 and scottie.sexperience >= 1:
        "Scottie shakes his head the moment I ask the question."
        scottie.say "No, [hero.name]..."
        scottie.say "I got nothing going on."
        show scottie blush
        scottie.say "Unless you...wanna do more stuff with me?"
        "I can't help smiling at the question."
        "And I don't hesitate to nod my head."
        bree.say "I'd love that, Scottie!"
        bree.say "Let's go and find somewhere we can talk, yeah?"
        bree.say "Maybe somewhere a little more private?"
        "Now it's Scottie's turn to nod eagerly."
        "And he takes hold of my hand as we hurry off together too."
        call scottie_birthday_sex_female from _call_scottie_birthday_sex_female
    else:
        "Scottie looks thoughtful for a moment."
        "Not quite like he's trying to remember something."
        "But suspiciously like he's trying to think something up instead."
        show scottie sad
        scottie.say "Erm..."
        scottie.say "Yeah, [hero.name]..."
        scottie.say "I do have to do something later."
        scottie.say "I gotta...put my books into alphabetical order - that's it!"
        "I look at Scottie through narrowed eyes."
        "Because I'm not sure that he even owns a single book."
        "But he seems to be sticking with that explanation."
        "So I find myself having to nod in agreement."
        bree.say "If you say so, Scotty."
        bree.say "Okay, see you later."
        show scottie happy
        scottie.say "Same to you, [hero.name]!"
        hide scottie with dissolve
        "After that, we part ways."
        "And I'm left with an odd feeling of dissatisfaction."
    return

label scottie_birthday_sex_female:
    scene bg beach with fade
    "I take hold of Scottie's hand and start pulling him in the direction that will take us off the beach."
    "He comes willingly, happy to hang behind me to begin with, but then increasing his pace as we get going."
    show scottie swimsuit joke with easeinleft
    "Pretty soon he's the one starting to pull ahead, and I find myself being drawn after him instead."
    scottie.say "Come on, [hero.name]..."
    scottie.say "I know a shortcut through the dunes."
    show scottie at right with ease
    scottie.say "It's this way!"
    hide scottie with easeoutright
    bree.say "Okay, Scottie, okay!"
    bree.say "I'm coming as fast as I can."
    scene bg beach at center, zoomAt(1.25, (720, 720))
    show bg beach at center, traveling(1.25, 15.0, (480, 720))
    with fade
    "I find myself being jerked off the path and taking a detour into the dunes and long grass."
    "It's a part of the beach that I don't know too well myself, so I'm trusting Scottie's judgement here."
    "Normally that's a thing that I'd be more than a little reluctant to consider doing."
    "But as this is just a simple shortcut, I think that I can make an exception just this once."
    "The real problem that I'm facing is the way Scottie keeps on speeding up."
    "At first I could match his pace pretty well, and I was sure of my footing too."
    "But now he really does seem to be getting carried away."
    "And I find that I'm starting to stumble as I struggle to keep up."
    bree.say "S...Scottie..."
    bree.say "Slow down..."
    bree.say "Or I'm going to..."
    with hpunch
    bree.say "Whoa!"
    "As fate would have it, what I was trying to warn of happens just as I'm about to speak the words."
    "I feel my feet catch on a root or a buried rope of grass."
    "And I go tumbling, head over heels, into the sand."
    scene bg beach at center, zoomAt(1.25, (480, 720))
    show scottie surprised swimsuit at center, zoomAt(2.0, (640, 1340))
    with vpunch
    "In the confusion of the fall, Scottie goes down with me."
    with hpunch
    "Half because I'm hanging onto him and half because he tries to hold me up."
    with vpunch
    "Luckily we're falling down on sand, so there's something soft to land on."
    with vpunch
    "But still I feel the impact of the fall and of Scottie landing atop me."
    "There's a moment of confusion as we struggle to untangle our limbs."
    "And I can still feel the sensation of adrenaline running through my veins."
    bree.say "Dam it..."
    scottie.say "Oh man..."
    bree.say "How did we..."
    scottie.say "What happened..."
    "My hand happens upon something firm, and I grab hold of it without thinking."
    "I have no idea why I do it."
    "Maybe because I think it'll help me to stand up?"
    "Whatever the reason, I start out by giving it a good, hard tug."
    scottie.say "Ouch!"
    show scottie blush
    scottie.say "Erm, [hero.name]..."
    scottie.say "Is there any reason you're yanking on my dong?"
    scottie.say "I mean, it's okay with me."
    scottie.say "But I just wondered why!"
    show scottie joke
    "I'm looking Scottie in the eye as he's saying all of this."
    "And I can already feel my cheeks starting to turn red."
    "But I can also feel something else."
    "I can feel his hands starting to move over my body!"
    "But his face shows no sign of recognition."
    bree.say "Are you checking me for bruises right now?"
    bree.say "Because your hands are all over me!"
    show scottie blush
    scottie.say "They are?!?"
    scottie.say "Well what about you, [hero.name]?"
    scottie.say "You keep on rubbing me down there too!"
    show scottie shy
    "It's like the pair of us aren't in control of our bodies."
    "Our brains are babbling away to each other this whole time."
    "But our bodies have just decided to leave them out of it."
    hide scottie
    show scottie kiss swimsuit
    with fade
    $ scottie.flags.kiss += 1
    "And without a hint of warning, we suddenly pounce on each other."
    "I say that because it's not like only one of us does it."
    "And neither of us is taken by surprise in the slightest."
    "One moment we're stroking and squeezing."
    "The next we're wrapped up in each other, rolling in the sand."
    "I don't know which one of us it is that starts stripping-off the other."
    "Because the moment it starts to happen, it goes both ways."
    show scottie kiss naked with dissolve
    "Pretty soon Scottie and I are both naked."
    "We're kissing like our lives depend on it."
    "And when we're not, we're panting in desperation."
    "There's no way to decide who's going where or in what position."
    scene scottie doggy
    show scottie doggy nonpc beach
    with fade
    "I just end up laid on my belly in the sand."
    "And Scottie ends up on top of me."
    "Neither of us feels the need to ask the other if this is what we want."
    "Somehow we just know where this is going and what it means."
    "I feel Scottie half pinning me to the ground as he gets into position."
    "And I can feel his cock too, bigger and harder than ever now."
    "It pushes between my thighs, intent of reaching it's goal."
    "All the time I'm nodding too, urging Scottie on to do it."
    show scottie doggy -nonpc pleasure
    "Suddenly I feel the weight of his body pushing downwards."
    "And then everything changes."
    "Because now I can feel the head of his cock."
    "Or to be more specific, I can feel it pressing against my pussy."
    "Scottie begins to move up and down, drawing it in the same motion."
    "And with each pass that it makes, I can feel my resistance ebbing away."
    "Every time I hold my breath, willing it to break through."
    "But when it finally does, I'm not prepared in the slightest."
    show scottie doggy vaginal pain
    "As the lips of my pussy part, my eyes burst open."
    "Scottie makes short work of pushing ahead, not stopping once."
    "And that means I'm almost overwhelmed in those first few seconds."
    "He's sure to sink all the way in at first, filling me totally."
    "And then he begins to move in earnest, thrusting in and out."
    "I feel like a puppet on the end of strings as he does all of this."
    "Every reaction and movement of my body seems to be in response to his."
    "I'm sure that if I were to try to move on my own, it'd prove to be impossible."
    "All I can do is lie there and surrender myself to the experience."
    "This is what's happening, and there's no other choice but to ride it out."
    "Luckily for me, the sand is soft and warm under my belly."
    "So as I find myself being pushed down into it, I'm in no discomfort."
    "Which is a relief, as Scottie seems determined to drive me into the ground!"
    "Not that I have any complaints about my treatment."
    "My senses are overwhelmed and my whole being awash with pleasure."
    "I've lost track of time, of how long we've been here."
    "And I'm even beginning to forget where we are too."
    "I have no idea if I'm making any noise or if I've fallen silent."
    "It doesn't seem to make a difference to Scottie anyway."
    "He keeps right on going the whole time."
    "That is until I feel a change in the sensations from my body."
    "Everything suddenly becomes more intense."
    "Despite how impossible that seemed a moment before."
    "I'm about to have an orgasm, I know it."
    "I don't know how, but I'm one hundred percent sure."
    "And it comes just as Scottie freezes inside of me."
    "There's not even time to fully realise that he has before it happens."
    show scottie doggy ahegao creampie with hpunch
    "Scottie lets go inside of me, at the same second that my orgasm hits."
    with hpunch
    "Before I know it, I'm literally clawing at the sand."
    with hpunch
    "My body trying to burrow it's way downwards for release."
    "But nothing comes from the action, and instead I have to simply ride it out."
    scene bg beach with fade
    "I think that I must have blacked out along the way."
    "Or else simply lost the ability to comprehend my senses."
    "Because I come round not on my belly but on my back."
    "Scottie's laid at my side, staring up at the sky."
    "Neither of us says a word."
    "Pretty soon we'll have to get up and get dressed."
    "Otherwise someone's sure to discover us lying here naked."
    "But for now at least, all we can do is gaze up at the clear, blue sky."
    $ scottie.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
