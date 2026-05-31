init python:
    
    Event(**{
        "name": "shawn_female_event_01",
        "label": "shawn_female_event_01",
        "max_girls": 1,
        "conditions": [
            HeroTarget(
                IsGender("female"),
                HasRoomTag("pub"),
                MinStat("charm", 25),
                Not(OnDate()),
                Not(IsActivity()),
                ),
            Or(
                PersonTarget(shawn,
                    MaxStat("love", 20),
                    ),
                IsNotDone("shawn_female_event_02"),
                ),

            ],
        "once_month": True,
        "do_once": False,
        "quit": False,
        })
    
    
    CallEvent(**{
        "name": "shawn_female_event_02",
        "label": "shawn_female_event_02",
        "duration": 3,
        "conditions": [
            HeroTarget(
                IsGender("female"),
                ),
            PersonTarget(shawn,
                Not(IsHidden()),
                Not(IsPresent()),
                IsActive(),
                ContactKnown(),
                Not(IsActivity("sleep")),
                MinStat("love", 20),
                ),
            IsDone("shawn_female_event_01"),
            ],
        "do_once": True,
        })
    
    
    Event(**{
        "name": "shawn_female_event_03",
        "label": "shawn_female_event_03",
        "duration": 1,
        "conditions": [
            IsDone("shawn_female_event_02"),
            IsDayOfWeek("123456"),
            IsHour(7, 11),
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                IsRoom("bedroom4"),
                ),
            PersonTarget(shawn,
                Not(IsHidden()),
                MinStat("love", 40),
                IsFlag("shawndelay", False),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "shawn_female_event_04",
        "label": "shawn_female_event_04",
        "duration": 1,
        "conditions": [
            IsDone("shawn_female_event_03"),
            IsDayOfWeek("123456"),
            IsHour(19, 23),
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                HasRoomTag("pub"),
                Not(IsActivity()),
                ),
            PersonTarget(shawn,
                IsPresent(),
                Not(IsHidden()),
                MinStat("love", 60),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "shawn_female_event_05",
        "label": "shawn_female_event_05",
        "duration": 1,
        "conditions": [
            IsDone("shawn_female_event_04"),
            IsDayOfWeek("123456"),
            IsHour(19, 23),
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                HasRoomTag("pub"),
                Not(IsActivity()),
                ),
            PersonTarget(shawn,
                IsPresent(),
                Not(IsHidden()),
                MinStat("love", 80),
                IsFlag("shawndelay", False),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "shawn_female_event_06",
        "label": "shawn_female_event_06",
            "duration": 1,
            "conditions": [
                IsDone("shawn_female_event_05"),
                IsDayOfWeek("123456"),
                IsHour(19, 23),
                HeroTarget(
                    IsGender("female"),
                    Not(OnDate()),
                    HasRoomTag("pub"),
                    IsActivity("work_pub_female"),
                    ),
                PersonTarget(shawn,
                    IsPresent(),
                    Not(IsHidden()),
                    MinStat("love", 100),
                    ),
                ],
            "do_once": False,
            "once_day": True,
            })
    
    CallEvent(**{
        "name": "shawn_female_event_07",
        "label": "shawn_female_event_07",
            "duration": 3,
            "conditions": [
                IsDone("shawn_female_event_06"),
                Not(IsDone("shawn_female_event_08")),
                IsHour(9, 16),
                HeroTarget(
                    IsGender("female"),
                    Not(OnDate()),
                    ),
                PersonTarget(shawn,
                    Not(IsHidden()),
                    Not(IsPresent()),
                    IsActive(),
                    ContactKnown(),
                    Not(IsActivity("sleep")),
                    MinStat("love", 110),
                    ),
                ],
            "do_once": False,
            "once_week": True,
            })
    
    Event(**{
        "name": "shawn_female_event_08",
        "label": "shawn_female_event_08",
            "duration": 1,
            "conditions": [
                IsDone("shawn_female_event_07"),
                IsHour(9, 16),
                HeroTarget(
                    IsGender("female"),
                    Not(OnDate()),
                    Not(IsActivity("work")),
                    ),
                PersonTarget(shawn,
                    Not(IsPresent()),
                    Not(IsHidden()),
                    MinStat("love", 140),
                    IsFlag("shawndelay", False),
                    ),
                ],
            "do_once": True,
            })
    
    Event(**{
        "name": "shawn_female_event_09",
        "label": "shawn_female_event_09",
            "duration": 1,
            "conditions": [
                IsDone("shawn_female_event_08"),
                HeroTarget(
                    IsGender("female"),
                    IsRoom("date_pub"),
                    ),
                PersonTarget(shawn,
                    OnDate(),
                    MinStat("love", 160),
                    IsFlag("shawndelay", False),
                    ),
                ],
            "do_once": True,
            })
    
    Event(**{
        "name": "shawn_female_event_10",
        "label": "shawn_female_event_10",
            "duration": 1,
            "conditions": [
                IsDone("shawn_female_event_09"),
                HeroTarget(
                    IsGender("female"),
                    Not(IsActivity()),
                    ),
                PersonTarget(shawn,
                    Not(IsHidden()),
                    MinStat("love", 180),
                    IsFlag("shawndelay", False),
                    ),
                ],
            "do_once": True,
            })
    
    Event(**{
        "name": "shawn_female_sub_01",
        "label": "shawn_female_sub_01",
        "duration": 1,
        "conditions": [
            IsDone("shawn_female_event_04"),
            
            IsNotDone("shawn_female_yandere_01"),
            HeroTarget(
                IsGender("female"),
                IsRoom("date_restaurant"),
                ),
            PersonTarget(shawn,
                OnDate(),
                MinStat("love", 90),
                MinStat("sub", 25),
                IsFlag("shawndelay", False),
                ),
            ],
        "do_once": True,
        })
    
    SpecificTalkSubject(**{
        "name": "shawn_female_sub_02",
        "label": "shawn_female_sub_02",
        "display_name": "About submissiveness",
        "duration": 0,
        "icon": "button_shawn",
        "conditions": [
            IsDone("shawn_female_sub_01"),
            HeroTarget(
                IsGender("female"),
                ),
            PersonTarget(shawn,
                IsActive(),
                MinStat("love", 130),
                MinStat("sub", 30),
                Not(IsFlag("breeNickname", "family_name")),
                IsFlag("shawndelay", False),
                ),
            ],
        "once_day": True,
        })
    
    Event(**{
        "name": "shawn_female_sub_03",
        "label": "shawn_female_sub_03",
        "duration": 1,
        "conditions": [
            IsDone("shawn_female_sub_02"),
            IsTimeOfDay("afternoon", "evening"),
            HeroTarget(
                IsGender("female"),
                IsRoom("bedroom4"),
                Not(IsActivity()),
                ),
            PersonTarget(shawn,
                MinStat("love", 170),
                MinStat("sub", 80),
                IsFlag("shawndelay", False),
                ),
            ],
        "do_once": True,
        })
    
    Activity(**{
        "name": "shawn_female_yandere_01",
        "display_name": "Call the bitch",
        "label": "shawn_female_yandere_01",
        "duration": 1,
        "icon": "smartphone",
        "conditions": [
            IsDone("shawn_female_event_04"),
            IsNotDone("shawn_female_sub_01"),
            
            HeroTarget(
                IsGender("female"),
                HasSkill("yandere"),
                HasRoomTag("home"),
                Not(IsActivity()),
                ),
            PersonTarget(shawn,
                Not(IsHidden()),
                MinStat("love", 110),
                IsFlag("shawndelay", False),
                ),
            ],
        "do_once": True,
        })
    
    Activity(**{
        "name": "get_rid_of_the_bitch",
        "display_name": "Get rid of the bitch",
        "label": "shawn_female_yandere_02",
        "duration": 2,
        "icon": "palla",
        "conditions": [
            IsDone("shawn_female_yandere_01"),
            IsNotDone("shawn_female_sub_01"),
            
            IsHour(22, 5),
            HeroTarget(
                IsGender("female"),
                HasSkill("yandere"),
                Not(IsActivity()),
                ),
            PersonTarget(shawn,
                MinStat("love", 130)
                ),
            ],
        })
    
    Event(**{
        "name": "shawn_preg_talk",
        "label": "shawn_preg_talk",
        "conditions": [
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                IsFlag("pregnancy_father", "shawn"),
                Or(
                    MinCounter("pregnant", 60),
                    IsFlag("foundpreg"),
                    ),
                ),
            PersonTarget(shawn,
                IsPresent(),
                Not(IsHidden()),
                IsFlag("toldpreg", False),
                MinStat("sexperience", 1),
                ),
            ],
        "do_once": False,
        })
    
    
    
    Event(**{
        "name": "shawn_kiss_me_female",
        "label": "shawn_kiss_me_female",
        "max_girls": 1,
        "conditions": [
            HeroTarget(IsGender("female")),
            PersonTarget(shawn,
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
        "name": "shawn_find_out_pregnancy",
        "label": "shawn_find_out_pregnancy",
        "conditions": [
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                MinCounter("pregnant", 30),
                CounterChanceChecker("pregnant", 50)
                ),
            PersonTarget(shawn,
                IsPresent(),
                Not(IsHidden()),
                IsFlag("toldpreg", False),
                MinStat("sexperience", 1),
                ),
            ],
        "do_once": False,
        })

label shawn_female_event_01:
    if shawn.love.max < 20:
        $ shawn.love.max = 20
    "The interior of the bar greets me with the typical noise, a wall of jukebox music and clinking glasses and dishes and laughter and people's voices rising louder and louder, vying for attention by speaking over the clamor."
    "I could never tell if I love it or hate it, but it's a familiar and homey kind of claustrophobia, anyway, and I make my way into it, slipping past a few standing crowds and making my way to the bar."
    "The barstool greets me with a cushion flattened and splitting from years of weight and abuse as I plop myself down onto it, leaning my elbows onto the counter."
    "Barkeeper" "Whatcha gettin', Miss?"
    bree.say "Just a Coke, for now."
    "I haven't thought yet about exactly what I'm looking for as my poison, but it doesn't hurt to start with a double shot of some caffeine and sugar."
    "Barkeeper" "Comin' up."
    "I settle myself in, grabbing one of the drink menus and exhaling a sigh as I let my eyes trail down the list."
    shawn.say "Hey."
    "A voice beside me, intimate and husky beneath the intoxicated shouting of the rest of my room, catches my attention immediately as directed to me."
    show shawn date nice at center, zoomAt(1.25, (640, 920)) with easeinright
    shawn.say "[hero.name], isn't it?"
    show shawn smile
    "My eyes snap from the menu to the man beside me, leaned over onto the bar top himself with a frosty glass in one hand."
    "I recognize him almost immediately; Shawn, from the electronics store."
    "A helpless smile flashes across my face."
    bree.say "Oh, hey! Small world."
    show shawn happy at startle
    "He chuckles."
    show shawn nice
    shawn.say "Small town, I guess."
    show shawn smile
    "It's not, really, but I get what he means."
    "I guess it's kind of inevitable that drinking-aged adults will eventually end up at the local hotspot, sooner or later."
    "Still, I might expect friends or enemies or exes or professors, but I wouldn't have thought I'd bump into the geek-store-guy here, halfway through a glass of Jack."
    bree.say "How're you doing?"
    show shawn normal
    "He shrugged, giving his glass a slight tip."
    show shawn sadsmile
    shawn.say "Crappy enough to end up here, but a little better now that I am."
    show shawn smile
    "Despite the grim response, he speaks it with an air of humor, and I giggle as he takes another swig from his glass."
    show shawn talkative
    shawn.say "So."
    show shawn smile
    "He shifts his gaze back over to me."
    "His eyes have that slight haze to them that tells me this isn't his first drink, but he's definitely still in his senses enough that there's a sharpness in them, still, and no slur to his words."
    "I'm glad; it's always made me feel a little uncomfortable to see people intoxicated, when they might not be acting their best, especially when we're basically still strangers."
    show shawn talkative
    shawn.say "On to the real, important questions -- how'd you like the game?"
    show shawn smile
    menu:
        "I'm glad you asked.":
            $ shawn.love += 1
            "The game! I almost forgot about that."
            "The bartender hands me my Coke, but I'm too distracted by the images suddenly flooding my head to thank him, and he moves away, unbothered."
            bree.say "Oh yeah!"
            "I close my hands over the icy cold glass, drawing it in close to my chest."
            "It gives that pleasing, muted tinkle as the ice cubes clatter against each other, and I draw a deep sip of it through the straw before continuing, giving myself time to gather my thoughts."
            show shawn date nice
            shawn.say "It was good, right?"
            show shawn smile
            "He can obviously see it on my face, a clear amusement in his eyes as he waits for my reply."
            bree.say "Hell yeah, it kicked ass!"
            "I launch, helplessly, into one of my tirades..."
            "Ranting about the gameplay, the graphics, how well the music matched the scenes, getting my blood pumping when it needed to and reeling me in when the moment got serious and making me cry when the story turned dark."
            "I can get a bit overwhelming, sometimes, when I do this, I know, but if I've got something to say it just kind of wells up inside me and… comes out."
            "Sometimes I can see the regret on the faces of the people who asked the question and prompted my full-blown, spontaneous game reviews."
            "But Shawn seems genuinely invested in what I'm saying, sipping occasionally at his drink, and there's a light of investment and amusement and agreement in his eyes as I ramble on and on."
            show shawn date happy
            "The same smile is on his face the entire time."
            "It's dorky, I know… but just the sincerity of his question, and his willingness to listen… it warms something inside of me to be able to spill my guts to someone about it."
            "It's like, that feeling of being with a friend who fills a void."
            "When I've gotten most of the major thoughts out of my head, and I start taking moments to breathe, Shawn finally gets some words in edgewise and we talk about what we both liked, what we didn't like, what drove us crazy and what characters were our favorites."
            "At least an hour has to have passed by the time I finally sit myself back and exhale a breath that carries the fading ghost of my vented opinions, and I poke at the remaining ice at the bottom of my empty cup."
            bree.say "Sorry. I know I can get a little long-winded about this kind of thing."
            "Shawn shakes his head, and there's a gentle sincerity to his voice and the action that eases my embarrassment immediately."
            show shawn date nice
            shawn.say "Nah, I asked. Besides, it's nice to be able to talk to someone about it. Most of our customers are geriatric."
            show shawn smile
            "I snicker."
            "There's a light, breezy feeling in my chest, where a weight I didn't even realize had been there was lifted."
            "I didn't even realize how much I'd been wanting to get my thoughts out about it until now."
            "I'm glad I came here tonight."
            "The bartender stops nearby, tapping his finger in indication before my empty glass."
            "I guess he's learned through years of experience to not try to interrupt someone as mindlessly engaged in a conversation as I obviously was."
            "Barkeeper" "Refill? Or were you ready for something else?"
        "I haven't started it yet.":
            "My mind trips over the question for a second before I realize what he means."
            "That game he sold me on… shoot."
            "I haven't gotten around to starting it just yet."
            "A wave of guilt rushes over me."
            "It's not a big deal; we hardly know each other, and it's not like I made him a promise or anything."
            "I just feel like it's a missed opportunity on a conversation that might have been nice to have… it's not super often that I get to talk to someone about games, really."
            "I have a feeling the guilt I feel is written all over my face, like a sad puppy."
            bree.say "Crap… I haven't gotten to it yet."
            show shawn sad
            "Shawn looks disappointed, and I feel immediately even worse."
            show shawn talkative
            shawn.say "Ah. No problem."
            show shawn normal
            "He takes another sip of his drink."
            show shawn talkative
            shawn.say "You playing a lot of other games?"
            show shawn smile
            "I've got a couple, but I feel like the reality is that it got set on a shelf and just… lost, somehow, beneath everything else going on."
            bree.say "Um… yeah, I guess so."
            "My noncommittal answer seems to give him the hint not to push the subject."
            "For a geek, I'm grateful at his ability to read social cues."
            "I poke at the ice in my Coke for a few seconds in the quiet that falls between us, and, thankfully, the bartender returns, earning my attention."
            "Barkeeper" "Was there anything else you needed?"
        "It was garbage.":
            $ shawn.love -= 1
            "The game?"
            "Oh."
            "My nose wrinkles slightly, and I fix my gaze on the bubbles of carbonation rising through my drink."
            "I almost forgot I had gotten it on his recommendation."
            bree.say "Not my thing, I guess."
            "Though I'm not watching him, I can see a subtle shift in his expression and posture from my peripheral as he deflates a little bit under my reply."
            show shawn surprised
            shawn.say "Oh, no?"
            show shawn sad
            "He sounds disappointed."
            "I feel a little bit bad, but… it really was trash."
            "The jokes fell flat for me."
            "The characters never managed to elicit much emotion from me, through their victories or their tragedies."
            "I know not everything will suit everyone."
            "But it feels super awkward to sit here in the quiet that follows."
            "I know he really liked it, and I can feel from the discontent radiating off of him that he was expecting me to, too, and he's let down."
            "There goes that thread of conversation."
            "Thankfully, the bartender saves the both of us, returning to stop before me and earning my attention."
            "Barkeeper" "Was there anything else you needed?"
    "I think for a moment before glancing over to Shawn's glass, still held loosely in his hand on the counter top."
    bree.say "I'll have what he's got."
    "The bartender nods, shifting his gaze over to Shawn."
    "Barkeeper" "And a refill for you?"
    "Shawn nods, sliding the near empty glass forward."
    show shawn talkative
    shawn.say "Sure, one more."
    show shawn normal
    "The tender collects his glass and turns to get us our drinks, and Shawn looks back over to me, seeming to hesitate for a second over his words."
    show shawn nice
    shawn.say "You know, it's been a while since I've seen a girl like you that's into gaming."
    show shawn smile
    bree.say "A girl like me?"
    "I have a feeling I know where this is going."
    "He's not the first to give me this speech, anyway."
    "He shifts himself on his stool to face me a little more."
    show shawn nice
    shawn.say "You know. Outgoing. Charming. Funny."
    show shawn smile
    "The next word takes a fleeting, easily missed moment of stalling before it comes out."
    show shawn nice
    shawn.say "Beautiful, obviously."
    show shawn smile
    "Yep, this old song and dance."
    "Still, having him say it to my face like that, and the earnestness behind his words that, I'm sure, is at least partially fueled by the alcohol…"
    "I feel my face flush, and I give a nervous smile and tuck a lock of my hair behind my ear, just to busy my hands."
    bree.say "I mean, I'm not the only one, y'know? We're out there."
    "He doesn't say anything back at first, just looking at me, like there's something going through his head that he's not saying out loud."
    "The bartender returns and sets our drinks down in front of us."
    "Shawn waits until he walks back away before he speaks again."
    show shawn nice
    shawn.say "Maybe we could keep in touch."
    show shawn smile
    "He ventures, steeled by his liquid courage."
    show shawn nice
    shawn.say "You can tell me about some of your favorites?"
    show shawn smile
    menu:
        "Give him my number.":
            $ shawn.love += 1
            "I can't help but smile."
            "It's a niche I've needed for a while, really, but deep down a part of me has always wanted someone to just be able to sit at the bar and geek out with."
            "Who knows, maybe he's even good, and we can kick some ass in some co-op games."
            bree.say "Yeah. I think I'd like that."
            show shawn date happy
            "His face lights up at my response, which warms my heart, just a little bit."
            "It feels good to make friends with common interests."
            "Someone who I can say with some confidence is into me for more than just my body or my pretty face."
            "He pulls out his phone eagerly and plugs my number in."
            "I see that he saves me as \"Gamer Girl - [hero.name]\" and smile helplessly."
            "Nerds are so cute sometimes."
        "How about you give me yours?":
            "I'd be lying if I said I wasn't always secretly hoping for a friend I can geek out with."
            "Over beers, or over energy drinks and half-empty chip bags at 3AM -- you know, the good stuff."
            "Still, I feel like it might be a little risky to hand my number over to someone who might be more entranced by the idea of the Gamer Grrl than he is with a real human being, and I don't want this to escalate too quickly."
            "If I keep it slow, maybe we can foster this friendship before it moved too quickly into a fantasy."
            bree.say "How about you give me your number, and I'll let you know when I've got some thoughts to share?"
            show shawn date nice
            "He smiles and snorts a soft laugh."
            "There's that look in his eyes that knows that it's sometimes a tactic of girls who have no intention of texting you at all."
            "But I'm not weaseling out of it entirely."
            "I'll just shoot him a message when I have something to say… and, preferably, when he's not tipsy and trying to hit on me."
            show shawn happy
            shawn.say "Deal."
            show shawn smile
            "He gives me his number, and I punch it into my phone."
            $ hero.smartphone_contacts.append("shawn")
        "No thanks.":
            $ shawn.love -= 1
            "I could have seen that coming a mile away."
            "I give a sympathetic smile and a small head shake, and he nods slightly and turns back to his glass, as if it was the response he was expecting."
            bree.say "It's kind of soon, still. Maybe after we catch each other a few more times out in the wild?"
            show shawn talkative
            shawn.say "Yeah."
            show shawn sad
            "He nods again, a small and resigned gesture."
            show shawn talkative
            shawn.say "Sounds like a plan."
            show shawn sad
            "He sits himself back from the bar, stretching his arms out in front of himself with fingers interlocked."
            show shawn talkative
            shawn.say "Well, I've actually got some work to do back home."
            show shawn sad
            "He takes the remainder of his glass and pounds down the rest of it before getting to his feet."
            show shawn sadsmile
            shawn.say "I'll see you around, [hero.name]."
            show shawn sad
            "I give him a warm smile and take a sip of my own drink, warm and burning as it goes down."
            bree.say "See you around."
            return

    $ shawn.unhide()
    return

label shawn_female_event_02:
    if shawn.love.max < 40:
        $ shawn.love.max = 40
    "I know that Shawn's kind of a nerd."
    "Okay, okay...that doesn't even begin to cover it."
    "He's a massive nerd - probably an even bigger one than [mike.name], which is really saying something!"
    "But the way I figure it is that I'm a total nerd too, so we should have a hell of a lot in common."
    "And it's not just that we're both nerds either."
    "I get the feeling that underneath being a bit sniffy, Shawn's a really sweet natured guy."
    "Plus you can just bet that he has a lot of passion in him, too."
    "Because nerds are all about the passion."
    "So I figure that what I need to do to win him over is indulge the nerd side of things."
    "And I think that I have just the thing to do it, as I call Shawn up."
    show screen expression "smartphone_calling" pass ("Shawn")
    show breemc b evil at center, zoomAt (3.5, (840, 2040))
    with fade
    "Even before the phone rings once, Shawn picks up on the other end."
    "So he's enthusiastic, which I take as a good sign."
    shawn.say "Hey, [hero.name]..."
    shawn.say "It's so great to hear from you!"
    "I didn't think it had been that long since I last spoke to Shawn."
    "But he makes it sound like we haven't exchanged a single word in months."
    show breemc talkative
    bree.say "Oh..."
    bree.say "Oh yeah, Shawn..."
    bree.say "It's nice to talk to you too."
    show breemc normal
    "There's a short, awkward moment as we both fall silent."
    "And then I realise it's because I was the one that called Shawn."
    "So he's obviously waiting for me to say something."
    shawn.say "So..."
    shawn.say "Did you just call me up to touch base?"
    shawn.say "Or is this a botty call, huh?"
    show breemc evil
    bree.say "Erm..."
    bree.say "I think you mean booty call, Shawn."
    show breemc talkative
    bree.say "But no, that's not why I'm calling you."
    show breemc normal
    "I can almost feel Shawn cringing on the other end of the line."
    "And then he's scrabbling to recover his composure, while laughing off his mistake."
    shawn.say "Of course, [hero.name]..."
    shawn.say "Of course..."
    shawn.say "I was just joking around, that's all."
    show breemc talkative
    bree.say "Anyway..."
    bree.say "The reason I called was to ask if you wanted to come to the movies with me."
    bree.say "They're showing a season of Sombrero Zombie movies at the multiplex right now."
    show breemc normal
    "I feel like I can feel Shawn's reaction on the other end for a second time."
    "Only this is more like he's freaking out with unsuppressed excitement."
    shawn.say "You mean Jorge B Sombrero, the king of independent Mexican zombie films?!?"
    shawn.say "How did I not know this was happening?"
    shawn.say "I love that guy's films!"
    shawn.say "Dammit, I knew I was working too hard - it's dulled my connection to pop-culture!"
    show breemc smile
    bree.say "So what, Shawn?"
    bree.say "Does that mean you want to come along?"
    show breemc normal
    shawn.say "Of course I do!"
    shawn.say "I'll see you there, [hero.name]..."
    shawn.say "Asap!"
    hide screen smartphone_calling
    hide breemc
    with fade
    "Shawn ends the call before I can say anything more."
    "So all I can do is take it that we're going on a date to the movies."
    "That and hurry out of the house and get to the multiplex as soon as possible."
    scene bg cinema
    show shawn at center, zoomAt(1.25, (640, 920))
    with fade
    "When I finally make it there, Shawn's beaten me to it."
    "And he's still as eager as he was over the phone."
    show shawn happy
    shawn.say "[hero.name]..."
    show shawn nice
    shawn.say "You're finally here!"
    show shawn smile
    bree.say "I came as soon as I could, Shawn."
    bree.say "So..."
    bree.say "What are we going to see?"
    show shawn normal
    "Shawn and I find a list of what's on and when it's all starting."
    "And it looks like we have two choices."
    show shawn nice
    shawn.say "'Evening of the Reanimated Revenants' is just about to start."
    shawn.say "That's like, the very first zombie movie Sombrero ever made."
    show shawn smile
    bree.say "Hmm..."
    bree.say "But if we wait a few minutes, we can catch 'Planet of the Putrid Ghouls'."
    bree.say "That's the one that really made his films blow up back in the day."
    show shawn normal
    "Shawn and I are both nodding and looking thoughtful."
    "Because it seems we both know the merits of each film."
    "And neither of us is enough of a jerk to overrule the other."
    "But at this rate we're going to miss both films."
    "So I make the decision to break the stalemate."
    menu:
        "Follow Shawn's idea":
            bree.say "Okay, Shawn..."
            bree.say "Coming to see a zombie film was my idea."
            bree.say "But that makes you my guest today."
            bree.say "So we'll see 'Evening of the Reanimated Revenants'."
            "Shawn looks like he was all set to argue with me."
            show shawn stuned
            "But then he realises that I'm letting him have his own way."
            "And his expression changes to one of genuine surprise."
            show shawn surprised
            shawn.say "You're serious?"
            shawn.say "Wow...that's really cool of you, [hero.name]."
            show shawn nice
            $ shawn.love += 2
            shawn.say "And trust me, you won't regret your choice!"
            show shawn smile
            "I nod and smile, pleased to see how happy I've made Shawn feel."
        "Stand to my choice":
            bree.say "Okay, Shawn..."
            bree.say "Coming to see a zombie film was my idea."
            bree.say "So I'm saying that I get to make the decision."
            bree.say "And we're seeing 'Planet of the Putrid Ghouls'."
            show shawn embarrassed
            "Shawn looks like he's about to argue with me."
            "But then he seems to realise something and change his mind."
            show shawn normal
            "Probably that he doesn't want to blow his chance to be on a date with me!"
            show shawn complain
            shawn.say "Okay, [hero.name]..."
            shawn.say "You win."
            $ shawn.sub += 1
            show shawn sad
            "I nod and smile, choosing to ignore the frown on Shawn's face."
    "We hurry to buy our tickets and some snacks from the concession stand."
    "Then Shawn and I find the screen where our film is showing and locate our seats."
    scene bg cinemaroom
    show shawn smile at center, zoomAt(1.5, (640, 1200))
    with fade
    "As soon as the lights go down, we're transported to a different world."
    scene bg cinemaroom at dark, dark
    show shawn smile at dark, dark, center, zoomAt(1.5, (640, 1200))
    with dissolve
    "One where the bodies of the recently deceased refuse to rest in peace."
    "Where the few living survivors struggle to escape becoming their next meal."
    "And where civilisation as we know it decays more quickly than the unquiet dead."
    "Shawn and I are obviously enjoying the chance to rewatch a classic film we both love."
    "But at the same time we're also pointing out little bits of trivia to each other the whole time."
    "And soon it becomes almost like a competition to see who's the biggest geek."
    "Whether or not we can come up with something that the other doesn't already know."
    "Even better if the trivia we throw out actually impresses the other person too."
    "All too soon the movie is over."
    scene bg cinemaroom
    show shawn smile at center, zoomAt(1.25, (640, 920))
    with fade
    "As the credits roll we shuffle out of the theatre and back to reality."
    "Feeling that weird sensation of returning to our own lives from a world of fantasy."
    "Shawn shakes his head as we thread our way through the crowds."
    "Seemingly annoyed as people all but walk into him without seeing him in front of them."
    scene bg cinema
    show shawn angry at center, zoomAt(1.25, (640, 920))
    with fade
    shawn.say "Urgh..."
    show shawn talkative
    shawn.say "It's not hard to see where they got the idea for the zombies from!"
    shawn.say "So many people are just wandering around without a thought in their heads."
    show shawn smile
    "I nod my head in agreement."
    bree.say "I know what you mean!"
    bree.say "An actual zombie apocalypse could be happening right now."
    bree.say "And nobody would be any the wiser!"
    show shawn happy at startle
    "Shawn chuckles at my observation."
    show shawn smile
    "But then he shakes his head."
    show shawn sadsmile
    shawn.say "I sometimes think it's already started, [hero.name]."
    shawn.say "And by the time everyone notices, it'll be too late."
    show shawn normal
    "I keep on smiling at Shawn as he says all of this."
    "Though I notice that the look on his face is pretty serious."
    bree.say "We're still joking, right?"
    bree.say "I mean..."
    bree.say "You don't actually think that zombies are a real thing?"
    show shawn embarrassed
    "Shawn shoots me a knowing look."
    "One that makes it obvious he thinks I'm being naive."
    show shawn talkative
    shawn.say "Oh come on, [hero.name]..."
    shawn.say "You know there are insects that can burrow into your brain and take it over, right?"
    shawn.say "Strains of bacteria that make your nervous system go crazy?"
    shawn.say "All the pieces are there, ready to be put together."
    shawn.say "As soon as that happens - boom, hordes of zombies!"
    show shawn embarrassed
    menu:
        "You're kidding right?":
            "I let out a peal of laughter and shake my head."
            bree.say "Oh, Shawn..."
            bree.say "I love that you're so into all of this stuff."
            bree.say "But you really should get out and touch grass sometime soon."
            bree.say "Zombie hordes?"
            bree.say "I mean, really?"
            show shawn normal
            "Shawn looks like he's about to start arguing his case again."
            "But then he sees that our conversation is getting some attention."
            "A significant number of the other cinema-goers are looking at us now."
            "And they seem to be more than a little interested in what he's about to say."
            show shawn sadsmile
            shawn.say "I..."
            shawn.say "Erm..."
            show shawn happy
            shawn.say "I had you going for a second, didn't I?"
            show shawn smile
            "I can't help narrowing my eyes at Shawn."
            bree.say "What are you trying to say?"
            bree.say "That you were joking just now?"
            show shawn sadsmile
            shawn.say "Of course I was, [hero.name]!"
            shawn.say "We all know zombies aren't real."
            show shawn smile
            "I nod and smile."
            "More amused by Shawn's back-tracking than anything else."
            $ shawn.sub += 1
        "Harumph... You have a point":
            bree.say "I have heard of all that stuff, Shawn..."
            bree.say "And at least some of it has to be true."
            bree.say "So maybe you're right."
            bree.say "We just need to be more vigilant in future."
            show shawn smug
            "Shawn looks like he's about to start explaining more about his theories."
            show shawn embarrassed
            "But then he sees that our conversation is getting some attention."
            "A significant number of the other cinema-goers are looking at us now."
            "And they seem to be more than a little interested in what he's about to say."
            "So he puts a hand around my shoulder and hurries me out of the place."
            show shawn talkative
            shawn.say "You're more right than you know, [hero.name]..."
            shawn.say "But there's always someone listening in, you know?"
            shawn.say "The people in power are trying to cover it all up."
            shawn.say "And they have ways of finding out what you're discussing too!"
            show shawn normal
            "Normally I'd be the first to laugh something like that off."
            "But maybe sitting through a zombie movie's expanded my mental horizons."
            "Because Shawn's making a lot of sense right now."
            "And I can't help glancing around at everyone looking our way."
            "Beginning to wonder who they are and why they're suddenly so interested in us."
            $ shawn.love += 2
    $ shawn.flags.shawndelay = TemporaryFlag(True, 1)
    return

label shawn_preg_talk:
    $ shawn.flags.toldpreg = True
    $ shawn.flags.know_is_father = True
    show shawn
    "It's hard to pin Shawn down, even when you need to speak to him about something serious."
    "He seems to react like he's got zero time to spare for you, like he's always busy with work."
    "I think he'd like me to believe that he's in demand because they can't cope without him."
    "But I know full well that all he does is manage a crappy little electronics store."
    "So when he tries to worm his way out of talking to me, I have to put my foot down."
    "Unfortunately that means that he's already pissed off and surly when we meet up later."
    "But by now I know Shawn well enough to be sure he's all talk and no trousers."
    "So I just steam straight on in there, taking no prisoners."
    "After all, this is seriously important - so I'm not pussy-footing around!"
    show shawn at center, zoomAt(1.5, (640, 1080)) with fade
    bree.say "Hey, Shawn..."
    bree.say "Thanks for finding time to fit me in!"
    "Shawn crosses his arms over his chest."
    "And it's all he can do to keep from rolling his eyes."
    show shawn talkative
    shawn.say "Don't make a joke out of it, [hero.name]!"
    shawn.say "I had to leave Amy in charge to be here."
    shawn.say "I'll be lucky if she doesn't burn the place down before I get back!"
    show shawn normal
    "I respond to all of this with a care-free smile, just brushing it off."
    "Because I'm not about to get side-tracked by Shawn's bullshit."
    bree.say "Whatever, Shawn..."
    bree.say "I'm sure they couldn't cope without you."
    bree.say "But you're really going to want to hear this..."
    show shawn annoyed
    "Shawn's eyes narrow as he senses the serious nature of what I have to say."
    "And I can finally see that he's getting the idea he needs to listen."
    show shawn talkative
    shawn.say "Okay, [hero.name]..."
    shawn.say "I get the message."
    shawn.say "What is this all about?"
    show shawn normal
    bree.say "I missed my last period, Shawn."
    bree.say "So I took a test, just to be sure."
    bree.say "And it came back positive."
    show shawn stuned
    "Shawn's eyes go wide and he turns visibly paler than normal."
    show shawn surprised
    shawn.say "You mean..."
    shawn.say "You're..."
    show shawn stuned
    bree.say "Yeah, Shawn..."
    bree.say "I'm pregnant."
    play sound spank
    show shawn at startle
    "Shawn slaps a hand against his forehead."
    "Then he shakes his head like he can't believe what he's hearing."
    show shawn surprised
    shawn.say "Urgh..."
    shawn.say "I can't believe this is happening!"
    shawn.say "I should never have let us do it without protection!"
    show shawn stuned
    "All I can do is offer up a weak smile."
    bree.say "We both kind of dropped the ball, Shawn."
    bree.say "But now we've got to decide what we're going to do about it."
    if shawn.love >= 150:
        show shawn surprised
        shawn.say "What do you mean, [hero.name]?"
        shawn.say "We're going to have a baby together, what else?"
        show shawn smile
        "All I can do is stare blankly at Shawn."
        "I was prepared for him to panic, or accuse me of cheating, even run away."
        "But the last thing I expected was for him to look me in the eye and accept it."
        bree.say "Y...you really mean that, Shawn?"
        show shawn stuned
        "Shawn looks at me with a puzzled expression on his face."
        show shawn talkative
        shawn.say "I'm not like some other guys, [hero.name]."
        shawn.say "They're just overgrown little boys."
        shawn.say "But I'm a real man, the kind that takes responsibility."
        shawn.say "How else do you think I've climbed so high in the retail industry?"
        show shawn smile
        bree.say "I...I have no idea, Shawn."
        bree.say "But this is serious, yeah?"
        bree.say "We're talking about bringing up a kid together!"
        show shawn nice
        shawn.say "We can handle it, [hero.name]."
        shawn.say "I know that we can handle it."
        show shawn smile
        "I find myself nodding and smiling as I listen to Shawn."
        "His confidence seems to be rubbing off on me."
        "Maybe he's right and I'm the one who's been over-thinking it."
        bree.say "Okay, Shawn..."
        bree.say "If you think we can do it..."
        bree.say "Then we'll do it - together!"
        show shawn happy
        "Shawn nods and smiles, taking hold of my hand."
        "And for the first time since I took the test, actually feel a little better."
        "It might just be the fact that I've finally been able to share this with someone else."
        "But even if that's all there is behind the feeling, I'll take it."
        hide shawn with fade
    else:
        show shawn surprised
        shawn.say "What are we going to do about it?!?"
        shawn.say "We're going to get rid of it, [hero.name]!"
        shawn.say "That's what we're going to do!"
        show shawn normal
        "I knew that was one of the options, of course I did."
        "And I thought I was prepared for Shawn to suggest it too."
        "But there's just something about the way he says it."
        "It sounds so final, and I realise that my mind's not made up yet."
        bree.say "Slow down there, Shawn!"
        bree.say "I don't want to rush into doing something I'll regret."
        "Shawn stares at me in amazement."
        "It's like he can't believe what he's hearing."
        show shawn vangry
        shawn.say "You either get rid of it, [hero.name]..."
        shawn.say "Or whatever you do, you'll be doing it on your own!"
        show shawn upset
        bree.say "Shawn!"
        bree.say "I can't believe you're saying that!"
        bree.say "This is a human life we're talking about."
        bree.say "It's our child, for god's sake!"
        "But no matter what I say, Shawn's having none of it."
        show shawn vangry
        shawn.say "No way, [hero.name]!"
        shawn.say "I have a life and a career."
        shawn.say "I'm going places in life."
        shawn.say "I can't let a kid ruin all of that!"
        show shawn upset
        bree.say "What are you talking about?"
        bree.say "You run a shitty little electronics store!"
        show shawn angry
        shawn.say "Not if you have your way I don't."
        shawn.say "So keep your claws out of me, [hero.name]!"
        shawn.say "And do what you want with the kid."
        shawn.say "Just leave me out of it!"
        hide shawn with easeoutright
        "With that, Shawn turns on his heel and storms away."
        $ shawn.breakup()
    return

label shawn_kiss_me_female:
    show shawn
    "Shawn's just one of those shy, geeky guys - you know?"
    "The kind where you have to make the first move if you want to get anywhere."
    "Or at least that's how I thought it was."
    "Which is why my eyes pop open in surprise when Shawn takes the initiative."
    hide shawn
    show shawn kiss
    with fade
    $ shawn.flags.kiss += 1
    "Before I know what's happening, he leans in and plants his lips against mine."
    "I can feel my heart begin beating faster in my chest."
    "And almost as soon as that happens, my instincts take over."
    "I return the kiss with mounting enthusiasm."
    "It just feels so right, so natural."
    "Like I'm communicating with Shawn on whole different level."
    "And now that it's started, neither of us seems to want it to end!"
    hide shawn kiss with fade
    return

label shawn_find_out_pregnancy:
    $ shawn.flags.toldpreg = True
    "Shawn always gets this look about him when he's suspicious."
    "[mike.name]'s seen it too, tell me he uses it on shoplifters in the electronics store."
    "And right now, he's using it on me as he studies my belly from afar."
    "I can't say that I blame him, it seems to be getting bigger by the day."
    shawn.say "[hero.name]..."
    shawn.say "Call me nosey if you like..."
    shawn.say "But you wouldn't happen to be pregnant, would you?"
    "There doesn't seem to be any point in denying it."
    "As I soon won't be able to hide it from anyone."
    bree.say "You got me, Shawn."
    bree.say "I am pregnant."
    bree.say "But I should also tell you that..."
    menu:
        "It's yours":
            $ shawn.flags.know_is_father = True
            bree.say "You're the father."
            bree.say "The baby is yours!"
            "Shawn gapes in surprise at this."
            "Like he can't actually process the information."
            if shawn.love >= 160:
                "But slowly I can see a change coming over Shawn's face."
                "Like he's finally getting to grips with what I just told him."
                shawn.say "Whoa..."
                shawn.say "That's...that's kind of cool!"
                "I'm pretty surprised to hear him react in a positive manner."
                "And so I can't quite believe what I'm hearing."
                bree.say "You really mean that, Shawn?"
                bree.say "You're happy you're going to be a father?"
                "Shawn nods as he looks at me."
                "And I can see more of the confusion disappearing with each moment that passes."
                shawn.say "Uh...yeah!"
                shawn.say "I always wanted to be a father."
                shawn.say "I just never knew when I wanted it to happen."
                shawn.say "And I guess now is as good a time as any!"
                bree.say "That's great, Shawn."
                bree.say "Because I'm going to need all the help I can get!"
                "This seems to awaken more awareness in Shawn."
                "And he nods gravely."
                shawn.say "Oh yeah..."
                shawn.say "Maybe it's about time I asked for that raise at the electronics store..."
            else:
                "But slowly I can see a change coming over Shawn's face."
                "Like he's finally getting to grips with what I just told him."
                shawn.say "Oh no!"
                shawn.say "No way!"
                "I make to reassure Shawn, to calm him down."
                "But he's already backing away from me, shaking his head."
                bree.say "It's okay, Shawn..."
                bree.say "We're both in this thing together."
                bree.say "We can work it out between us, yeah?"
                "Shawn keeps on shaking his head at me."
                "And I can see more of the confusion disappearing with each moment that passes."
                shawn.say "No, no, no..."
                shawn.say "I see what's happening here..."
                shawn.say "You're trying to trap me!"
                if shawn.love >= 150:
                    "Almost as soon as he says the words, Shawn stops."
                    "It's like he seems to realise how crazy he sounds."
                    "Then he shakes his head."
                    shawn.say "Sorry, [hero.name], sorry..."
                    shawn.say "I might have gone a bit mad there."
                    shawn.say "This is just heavy news, yeah?"
                    "I nod, but keep my expression serious."
                    bree.say "I know that, Shawn."
                    bree.say "But we still have to deal with it."
                    "Now Shawn nods too."
                    shawn.say "We will, [hero.name]..."
                    shawn.say "I just need a little time to get my head around it."
                else:
                    shawn.say "Well it's not going to work, [hero.name]..."
                    shawn.say "Because we're over!"
                    shawn.say "This relationship's finished!"
                    "Up to now I've tried to be nice to Shawn."
                    "Tried to coax him into accepting reality."
                    "But that's too much for me to take."
                    "And my patience snaps."
                    bree.say "Shawn, you spineless goon!"
                    bree.say "You can't run away from this!"
                    bree.say "We have a baby to think of!"
                    "But my words don't seem to have the desired effect."
                    "Because Shawn's already turned on his heel."
                    "And now he's running away."
                    "Literally running away!"
                    $ shawn.set_gone_forever()
        "It's not yours":
            bree.say "You're not the father."
            bree.say "The baby is someone else's!"
            "Shawn gapes in surprise at this."
            "Like he can't actually process the information."
            if shawn.love >= 150:
                "Suddenly I see a change in Shawn's expression."
                "It's like something I just said cut through all the confusion."
                shawn.say "Wait...what?!?"
                shawn.say "You're going to have a baby?"
                "I nod, trying to keep things focused on that point alone."
                "Shawn must realise that means I cheated on him."
                "But the baby's the most important thing right now."
                bree.say "That's right, Shawn..."
                bree.say "And I could use your help to handle it."
                menu:
                    "Ask Shawn to help with the baby":
                        if shawn.love >= 160:
                            "Shawn frowns at this."
                            "Then he looks at me and nods his head."
                            shawn.say "I'm not crazy about the idea, [hero.name]."
                            shawn.say "But I'm also not a complete bastard."
                            shawn.say "So I'll help out where I can."
                            "I feel a surge of relief as Shawn says this."
                            "And I make myself a promise to pay back his kindness."
                            "That and not to take advantage of his tolerance either."
                            bree.say "Oh, thank you, Shawn!"
                            bree.say "You won't regret this - I promise you!"
                        else:
                            "Shawn frowns at this."
                            "Then he looks at me and shakes his head."
                            shawn.say "That's pretty bold, you cheating cow!"
                            bree.say "But..."
                            bree.say "What about the baby?"
                            shawn.say "What about YOUR baby, you mean!"
                            shawn.say "I think I can get over you sleeping around, [hero.name]."
                            shawn.say "But I'm not going to help raise another man's child!"
                            "I nod slowly, willing to let it go."
                            "I guess I should be thankful Shawn didn't just dump me."
                            "And who knows, maybe I can talk him round later?"
                            $ shawn.breakup()
                    "I won't bother you about it":
                        pass
            else:
                show shawn sad
                "Suddenly I see a change in Shawn's expression."
                "It's like something I just said cut through all the confusion."
                shawn.say "Wait...what?!?"
                shawn.say "Didn't you just admit to cheating on me?"
                "I frown and shake my head."
                "Trying to keep focused on the issue of the baby."
                bree.say "That's not the point, Shawn."
                bree.say "The baby's the important thing."
                bree.say "The human life at the centre of all this!"
                shawn.say "Bollocks, [hero.name]!"
                shawn.say "Stop trying to change the subject!"
                shawn.say "If the kid's not mine..."
                shawn.say "Then you've been fucking around, yeah?"
                "I roll my eyes at his stubborn refusal to see things my way."
                "And then I give in to the fact that he's not going to shift his stance."
                bree.say "Okay, Shawn, okay..."
                bree.say "I might have slept with someone else."
                bree.say "Happy now?"
                shawn.say "Of course I'm not happy, you cheating cow!"
                shawn.say "Consider yourself dumped!"
                bree.say "But..."
                bree.say "What about the baby?"
                shawn.say "What about YOUR baby, you mean!"
                shawn.say "Not my kid, not my problem!"
                "With that, Shawn turns on his heel and walks away."
                $ shawn.set_gone_forever()
    return

label shawn_birthday_date_female:
    $ DONE["shawn_birthday_date_female"] = game.days_played
    $ game.active_date.clothes = "casual"
    scene bg cinema with fade
    "Shawn and I have been seeing each other for a while now, which means we've had a good few dates in that time."
    "And I feel that I've really gotten to know him well, enough for him to start to open up about himself to me."
    "Two of the things that I've learned about Shawn are that he loves movies, and his birthday is coming up real soon."
    "So it feels like a no-brainer that I should take him to the cinema to watch the former while we celebrate the latter."
    "Shawn seemed to be really up for the idea too, and so we made plans to meet up on the big day and indulge ourselves."
    "The only problem is that now the big day is here, I'm the one that's running late!"
    "First I couldn't find the outfit that I was planning to wear."
    "The car wouldn't start, so I had to call a taxi."
    "And every single person I come across seems to be determined to get in my way!"
    "So by the time I make it into the cinema lobby, I'm feeling pretty flustered."
    bree.say "Excuse me!"
    bree.say "Hey, I'm walking here!"
    bree.say "Are you trying to have me step on your face?!?"
    "I turn away from the last person to have had the misfortune to cross my path."
    show shawn embarrassed at center, zoomAt (1.25, (640, 900)) with fade
    "And I find myself staring straight into Shawn's face."
    "He looks a little nervous as he waves to me."
    "Probably because he's just seen me snapping at all those people."
    show shawn nice
    shawn.say "Erm..."
    shawn.say "Hi, [hero.name]..."
    shawn.say "I was starting to wonder if you were going to make it!"
    show shawn embarrassed
    "The comment instantly flies sideways up my ass."
    "And I feel myself getting ready to launch into a tirade at Shawn too."
    menu:
        "Calm yourself before replying to Shawn":
            "Sure, I'm feeling totally stressed out right now."
            "But none that is Shawn's fault."
            "Plus he's trying to lighten the mood."
            "So I probably shouldn't take it out on him."
            bree.say "Urgh..."
            bree.say "I nearly didn't, Shawn!"
            bree.say "I don't know what's the matter with me today."
            bree.say "Everything I touch just seems to go wrong!"
            show shawn happy
            "Shawn nods and gives me a sympathetic smile."
            show shawn nice
            shawn.say "I know how that feels, [hero.name]..."
            shawn.say "But that's the great thing about the movies."
            shawn.say "You get to switch off and forget all about your problems."
            shawn.say "Spend an hour or two in another world, right?"
            show shawn happy
            bree.say "You sure do!"
            bree.say "Now let's go and grab some tickets."
            $ game.active_date.score += 15
        "Reply to Shawn straight away":
            "I'm feeling totally stressed out right now."
            "And it's all because I've been trying to get here on time."
            "Can't Shawn see that?"
            bree.say "Of course I was going make it here, Shawn!"
            bree.say "We've been planning this for ages, haven't we?"
            bree.say "And I almost killed myself trying to make it on time!"
            show shawn sad at center, traveling (1.15, 0.3, (640, 860))
            "Shawn takes a step backwards as I say all of this."
            "And I can see from the look on his face that he's a little intimidated too."
            "Urgh..."
            "I should probably have tried to calm myself down before I said anything."
            "Now we're already off to a bad start."
            bree.say "Look, let's just forget about it, okay?"
            bree.say "Forget about it and go grab our tickets."
            show shawn normal
            "Shawn nods and hurries to do as he's told."
            "But I note that he's still keeping quiet."
            "Probably because he's scared of what'll happen if he doesn't."
            $ game.active_date.score -= 10
    show shawn normal at center, zoomAt (1.5, (640, 1080)) with fade
    "Together we make our way over to the counter selling the tickets."
    "And then we stand in the queue until we make it to the front."
    "There's only one film that the both of us want to see."
    "And so when the woman behind the counter asks, we already know the answer."
    "Woman" "What film are you wanting to see?"
    bree.say "Brogue One!"
    show shawn nice
    shawn.say "A Shoe Wars Story!"
    show shawn normal
    "The woman nods and begins to print out the tickets."
    "Woman" "That'll be thirty dollars, please."
    "As one, Shawn and I make to pay for the tickets."
    "Which makes for a super awkward moment."
    menu:
        "Insist on paying for the tickets":
            "I don't hesitate to push Shawn's hand away."
            "And I make sure to shake my head as I do so."
            bree.say "What do you think you're doing, Shawn?"
            bree.say "I'm the one taking you out for your birthday!"
            bree.say "So put your money away and let me treat you."
            show shawn surprised
            "Shawn looks to the left and the right."
            "Almost like he's worried that people are watching."
            "But all the same, he puts his money back in his pocket."
            "Though I notice he does look a little sheepish as he does so."
            show shawn normal
            shawn.say "Erm..."
            show shawn nice
            shawn.say "Okay, [hero.name]..."
            shawn.say "If you insist!"
            show shawn embarrassed
            "For a moment I wonder what could be bothering Shawn."
            "But then as I pay for the tickets, it dawns on me."
            "I did kind of make him look like he's my bitch!"
            "Like, not totally or"
        "Suggests that they go halves":
            "I'm kind of taken by surprise, as I'd been assuming I was paying."
            "After all, I am supposed to be taking Shawn out to celebrate his birthday."
            "But I guess he's one of those old-fashioned guys that wants to foot the bill."
            "I'm not really comfortable with that, but I could easily offend him here."
            "Though maybe there's a third option..."
            bree.say "Looks like we both had the same idea!"
            bree.say "So how about we go halves on this one?"
            "For a moment I think that Shawn's going to argue."
            show shawn normal
            "But then he cocks his head on one side and nods."
            shawn.say "Erm..."
            show shawn nice
            shawn.say "Okay, [hero.name]..."
            shawn.say "If you insist!"
            show shawn embarrassed
            "Shawn still looks like he's a little thrown by the idea."
            "But he doesn't complain or sulk once we've bought the tickets."
            "So I take that as a win."
            $ game.active_date.score -= 10
    "Once we have our tickets, my mind naturally turns to grabbing snacks."
    "And I lead the way over to the counter that's selling all that stuff."
    "Shawn doesn't seem as enthusiastic as me, trailing behind most of the way."
    "And once we're there, it seems like he's not actually going to get anything."
    bree.say "What's the matter, Shawn?"
    bree.say "Are you not feeling hungry?"
    "Shawn shakes his head at my questions."
    show shawn sadsmile
    shawn.say "It's not that, [hero.name]."
    shawn.say "I just don't really like cinema food."
    shawn.say "I mean, it's all pretty bad for you."
    shawn.say "And it's really expensive too!"
    if hero.has_skill("iron_stomach") or hero.has_skill("cooking") or shawn.love + hero.charm >= 200:
        menu:
            "Order nachos":
                bree.say "What's the matter, Shawn?"
                bree.say "Don't you want some of those nachos?"
                bree.say "The cheese sauce looks amazing!"
                "At the mention of the sauce, Shawn seems to go a little pale."
                show shawn complain
                shawn.say "Urgh..."
                shawn.say "You can't be serious?!?"
                shawn.say "That stuff sounds awful going in."
                shawn.say "And even worse coming out too!"
                show shawn normal
                "I shrug off Shawn's objections and order myself the nachos anyway."
                "Because what does it matter to him?"
                "I'm going to be the one eating them!"
                bree.say "Ooh!"
                bree.say "Make sure to put a bunch of those chillis on there too!"
                "With the tray of Nacho's in my hands, I turn and present them to Shawn."
                "I can't help taking a deep breath, my senses filling with the scent of melty cheese!"
                "But if Shawn was looking pale before, he's now beginning to turn green."
                show shawn complain
                shawn.say "Oh god!"
                shawn.say "I can't believe you're actually going to eat that!"
                show shawn normal
                "I nod and smile, picking up a nacho to prove that I'm serious."
                "And then I shove it straight into my mouth, savouring the salty taste."
                "Shawn, on the other hand, looks away in total disgust."
                $ game.active_date.score -= 10
            "Complaining about the food":
                "And the moment that I scan what's on offer, I think I know why."
                bree.say "Urgh..."
                bree.say "This is all junk-food!"
                bree.say "And it's not even good junk food either!"
                "Shawn comes closer, gazing over my shoulder."
                show shawn complain
                shawn.say "Yeah, [hero.name]..."
                shawn.say "I mean, it's all pretty bad for you."
                shawn.say "And it's really expensive too!"
                show shawn normal
                "I shake my head and walk up to the counter."
                "And Shawn follows close on my heels."
                show shawn surprised
                shawn.say "Erm, [hero.name]..."
                shawn.say "What are you doing?"
                show shawn normal
                bree.say "The only logical thing I can do, Shawn..."
                bree.say "I'm complaining!"
                show shawn complain
                shawn.say "Oh..."
                shawn.say "Do you really have to?"
                show shawn normal
                "But I'm not listening to Shawn's objections."
                "Instead I get the member of staff's attention."
                "And then there's no holding back."
                bree.say "Hey you!"
                bree.say "Where do you get off selling slop like this?"
                "Woman" "Huh?"
                bree.say "Where's the humous and olives?"
                bree.say "Where's the artisanal bread and hand-made preserves?"
                "Woman" "I have no idea what you're talking about!"
                "I cross my arms over my chest and turn away in disgust."
                bree.say "Humph..."
                bree.say "They should really be ashamed of themselves!"
                show shawn sadsmile
                shawn.say "I...I guess so, [hero.name]."
                shawn.say "Wow..."
                shawn.say "Look at how many people are staring at us all of a sudden!"
                show shawn embarrassed
                "Now that we're all ready to go, it's time to go grab our seats."
                "Shawn and I hurry into the theatre as the lights go down."
                "Just in time to find out where we're going to be sitting."
                $ game.active_date.score += 15
            "Forget about the snacks and go directly theater":
                scene bg cinemaroom
                show shawn normal
                with fade
                "But when we find the numbers on our tickets, we get a surprise."
                "Because a couple of guys are already sitting in them!"
                show shawn vangry
                shawn.say "Hey!"
                shawn.say "You're sitting in our seats!"
                show shawn upset
                "Woman" "So what?"
                bree.say "So we want to sit in them."
                bree.say "So move your butts!"
                "Woman" "Oh yeah?"
                "Woman" "And what if we don't?"
                show shawn angry
                "I put a big smile on my face as I answer."
                bree.say "Then I just walk over there and talk to the usher."
                bree.say "There's one of them right by the door."
                bree.say "I'm sure they'll be able to sort this out."
                bree.say "And everyone in the theatre will just have to wait while all of that happens."
                show shawn normal
                "The guy suddenly seems to lose his cocky attitude."
                "And he glances around at all of the other people in the theatre."
                "Which doesn't help matters, as most of them are staring daggers at him."
                "Woman" "Okay, okay..."
                "Woman" "We're moving, geez!"
                "The guys resentfully shuffle out of the seats."
                "Which allows Shawn and I to flop down into them."
                show shawn nice
                shawn.say "Ooh..."
                shawn.say "The seats are still warm."
                show shawn happy
                bree.say "Savour it, Shawn."
                bree.say "That warmth is how winning feels!"
                $ game.active_date.score += 15
    else:
        menu:
            "Forget about the snacks":
                "I listen to what Shawn has to say for himself."
                "And normally I wouldn't let it stop me from ordering what I wanted."
                "But this is supposed to be Shawn's night out."
                "So I guess I could make an exception this once."
                bree.say "Okay, Shawn..."
                bree.say "I'll pass on the snacks."
                bree.say "But don't complain if you hear my stomach rumbling during the film!"
                show shawn happy
                "Shawn chuckles and shakes his head."
                show shawn nice
                shawn.say "Better your stomach rumbling than other sounds you could make."
                shawn.say "There's nothing worse than the sound of someone eating gassy stuff."
                shawn.say "And then the inevitable sounds and smells that follow!"
                show shawn normal
                $ game.active_date.score += 15
            "Decide to get herself snacks":
                "I listen to what Shawn has to say for himself."
                "And then I shrug it off and turn to order myself some snacks."
                bree.say "Whatever, Shawn..."
                bree.say "You do you!"
                bree.say "Just don't try to sneak any of my snacks during the movie!"
                show shawn sad
                "Shawn watches in silence as I scoop up all the stuff I ordered."
                "And yeah, maybe I did go a little crazy because of his disapproval."
                "But it's not like I get to go to the movies every day, now is it?"
                "So what's the problem in indulging myself on the rare occasion that I do?"
                "My arms full of snacks, I start to make my way to the theatre."
                "Though my progress is slow, as I almost spill my snacks more than once!"
                $ game.active_date.score -= 10
    scene bg black with dissolve
    pause 1.0
    scene bg cinemaroom
    show shawn normal at center, zoomAt (1.5, (640, 1080))
    with fade
    "When the end credits roll, Shawn and I stay right where we are."
    "Because we're both waiting for that sweet, sweet post credits scene."
    "And when it appears, we feel the glow of nerdish joy watching it."
    "Only then do we haul our asses out of our seats and head for the lobby."
    "Back in the light of reality, I feel weirded out as usual."
    "But as my brain slowly comes back to the real world, I get chatty again."
    bree.say "Whoa..."
    bree.say "Back to reality!"
    show shawn nice
    shawn.say "Speaking of reality..."
    shawn.say "It is someone's birthday, right?"
    show shawn normal
    if not hero.has_gifts:
        "Oh crap..."
        "I went and forgot all about Shawn's birthday present!"
        "Wait a minute..."
        "Maybe I can wriggle my way out of this?"
        bree.say "Yeah, Shawn..."
        bree.say "And that's why I brought you to see a film, remember?"
        show shawn nice
        shawn.say "Oh yeah..."
        shawn.say "Of course, [hero.name]."
        show shawn normal
        "It's an awkward end to the conversation."
        "But at least it's over and we can move on to talking about something else."
        $ game.active_date.score -= 20
        $ shawn.love -= 10
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_31
        if _return != "done":
            if _return not in ["None", "exit"]:
                bree.say "Okay, Shawn..."
                bree.say "You can stop fishing."
                bree.say "Here you go."
                "I hand over the present that I've been holding onto for Shawn."
                play sound [paper_ripping_2, paper_ripping_1]
                "And he doesn't hesitate to start tearing off the wrapping paper."
                if _return:
                    show shawn surprised
                    "But as soon as he sees what's inside, Shawn's jaw drops open."
                    bree.say "What's the matter, Shawn?"
                    bree.say "Is there something wrong?"
                    show shawn nice
                    shawn.say "No...no, [hero.name]..."
                    shawn.say "I just...I have no idea where you found this!"
                    shawn.say "It's so bloody cool!"
                    show shawn happy
                    $ game.active_date.score += 20
                else:
                    show shawn stuned
                    "But as soon as he sees what's inside, Shawn's enthusiasm seems to drain away."
                    bree.say "What's the matter, Shawn?"
                    bree.say "Is there something wrong?"
                    show shawn sadsmile
                    shawn.say "No...no, [hero.name]..."
                    shawn.say "It's great, I guess..."
                    show shawn normal
                    $ game.active_date.score -= 10
            else:
                "Oh crap..."
                "I went and forgot all about Shawn's birthday present!"
                "Wait a minute..."
                "Maybe I can wriggle my way out of this?"
                bree.say "Yeah, Shawn..."
                bree.say "And that's why I brought you to see a film, remember?"
                show shawn sadsmile
                shawn.say "Oh yeah..."
                shawn.say "Of course, [hero.name]."
                show shawn normal
                "It's an awkward end to the conversation."
                "But at least it's over and we can move on to talking about something else."
                $ game.active_date.score -= 20
                $ shawn.love -= 10
    bree.say "So..."
    bree.say "What did you think?"
    show shawn sadsmile
    shawn.say "Well, I always try to go into these things prepared for disappointment..."
    show shawn nice
    shawn.say "Which was totally unnecessary this time - because it was amazing!"
    menu:
        "Agrees with Shawn's opinion":
            bree.say "I know, right?"
            bree.say "Easily the best one in ages!"
            show shawn happy
            "Shawn nods his head in agreement."
            "And I can see he's pleased with my answer."
            show shawn nice
            shawn.say "I'm so glad you said that, [hero.name]."
            shawn.say "I usually come to see these films with [mike.name]."
            shawn.say "But he just never seems to get it, you know?"
            shawn.say "You on the other hand - you understand what it's all about!"
            show shawn happy
            bree.say "You know what they say, Shawn..."
            bree.say "Great minds think alike!"
        "Disagrees with Shawn's opinion":
            bree.say "Nah..."
            bree.say "I liked bits here and there."
            bree.say "But it wasn't one of the best."
            show shawn sad
            "Shawn looks at me like I'm talking nonsense."
            "And he shakes his head to show his disappointment."
            show shawn surprised
            shawn.say "Are you for real, [hero.name]?"
            show shawn complain
            shawn.say "I usually come to see these films with [mike.name]."
            shawn.say "Because he seems to get all of this stuff, to understand it."
            shawn.say "I dunno..."
            shawn.say "Maybe I should have come with him instead."
            show shawn sad
            bree.say "Well if that's how you really feel..."
            bree.say "Then maybe you should come with him next time!"
    scene bg cinema
    show shawn normal at center, zoomAt (1.25, (640, 900))
    with fade
    "We walk out of the cinema and onto the street."
    "And that's when I realise it's earlier than I thought."
    bree.say "It's not too late, Shawn..."
    bree.say "You want to do something else?"
    bree.say "Or call it a night?"
    if game.active_date.score >= 80 and shawn.sexperience >= 1:
        show shawn happy
        "Shawn shakes his head as soon as I'm done talking."
        shawn.say "I'm not ready to call it a night, [hero.name]!"
        shawn.say "There must be a hundred things we could do right now."
        show shawn normal
        "I'm pleased to hear that Shawn wants to extend our date."
        "But I make a point of playing it down a little."
        "As I don't want to seem to grateful or desperate."
        bree.say "Okay, Shawn..."
        bree.say "That's cool."
        bree.say "But what are we going to do?"
        show shawn nice
        shawn.say "Let's walk and talk for now."
        shawn.say "I'm sure we'll think of something before too long."
        show shawn normal
        "With that, I put my arm in Shawn's."
        "And we stroll off together down the street."
        call shawn_birthday_sex from _call_shawn_birthday_sex
    else:
        "Shawn takes a look around, noting the fact it's still light."
        show shawn sad
        "But then he shakes his head and lets out a yawn."
        show shawn complain
        shawn.say "Ooh..."
        shawn.say "You know what, [hero.name]..."
        shawn.say "Sitting around in the dark for a couple of hours really takes it out of me!"
        shawn.say "I think I need to go home and get an early night."
        show shawn embarrassed
        "I can't help narrowing my eyes at this."
        "Because Shawn's yawning sounded more than a little put on."
        "But what am I going to do, call him on it?"
        "Accuse him of coming up with an excuse to end the date early?"
        "So instead I just nod and smile."
        bree.say "Whatever you say."
        bree.say "But we should do this again soon, right?"
        show shawn sadsmile
        shawn.say "Don't worry, [hero.name] - I'll call you."
        hide shawn with easeoutright
        "And with that, Shawn turns on his heel and walks away."
    return

label shawn_birthday_sex:
    scene bg street
    show shawn happy at center, zoomAt (1.25, (640, 900))
    with fade
    "I'm pretty sure that I managed to pull out all the stops and give Shawn the birthday date of a lifetime."
    "Because he's been walking on air ever since it officially came to an end, and he doesn't seem to want it to end!"
    "But the thing is that I have to take him somewhere quickly so that I can capitalise on all of that goodwill."
    "And the nearest place that I can think of is my house, so that's where I tell the taxi-driver to take us."
    "Once we're there, I do the best I can to hustle Shawn up the path and to the front-door."
    scene bg house
    show shawn embarrassed at center, zoomAt (1.25, (640, 900))
    with fade
    shawn.say "Erm..."
    shawn.say "[hero.name]..."
    show shawn normal
    "I'm fumbling around for my keys as I reach the porch, not really paying much attention."
    bree.say "Yeah, Shawn..."
    bree.say "Is there a problem?"
    show shawn sadsmile
    shawn.say "Isn't this..."
    shawn.say "Isn't this [mike.name]'s place?"
    show shawn normal
    "I'm just opening the door as I hear the question."
    "And I can't help turning around with a puzzled look on my face."
    bree.say "Huh?"
    bree.say "What are you talking about?"
    "Shawn shrugs, beginning to look more than a little sheepish."
    show shawn sadsmile
    shawn.say "Well..."
    shawn.say "Doesn't he live here?"
    show shawn normal
    bree.say "Yes, Shawn..."
    bree.say "[mike.name] lives here, but so does Sasha, and so do I."
    bree.say "And I don't have to get their permission to bring guys home either!"
    show shawn sadsmile
    shawn.say "It just feels a little weird, that's all."
    show shawn normal
    "Putting my balled fists on my thighs, I shoot Shawn a hard glance."
    bree.say "What's worse, Shawn?"
    bree.say "Fooling around in there while feeling weird?"
    bree.say "Or walking home alone feeling perfectly normal, but without getting any?"
    show shawn embarrassed blush
    "As soon as I put it in such stark terms, Shawn seems to change his tune."
    "Because he starts nodding and even makes to hurry into the house past me."
    show shawn nice
    shawn.say "Point taken, [hero.name]..."
    shawn.say "Point taken..."
    show shawn normal
    "Relieved that we're now on the same page, I close the door behind us."
    scene bg livingroom
    with fade
    pause 0.3
    show shawn normal at center, zoomAt (1.25, (640, 900)) with easeinright
    "And then I lead the way to the sitting room."
    bree.say "[mike.name]?"
    bree.say "Sasha?"
    bree.say "You guys home?"
    show shawn stuned at center, zoomAt (1.0, (640, 900)), startle
    "Shawn flinches a little as I call out my housemate's names."
    show shawn embarrassed
    "But when there's no response, he seems to begin relaxing at last."
    "I'm smiling and trying to make light of the whole situation by now."
    "So I decide to call out again."
    bree.say "Don't come into the sitting-room for a while, yeah?"
    bree.say "Shawn and I are going to have noisy sex in here!"
    show shawn stuned at center, zoomAt (1.0, (640, 900)), startle
    "Even though he knows that we're alone in the house, this still seems to shock Shawn."
    show shawn happy at center, zoomAt (1.0, (640, 900)), startle
    "But much to my delight, he laughs in a guilty manner, rather than being scared."
    "In fact it seems to have amused him so much that he gets in on the act himself."
    show shawn embarrassed
    shawn.say "Erm..."
    show shawn nice
    shawn.say "Yeah, [mike.name]..."
    shawn.say "I'm just going to like...like..."
    shawn.say "Screw your housemate here, you know?"
    show shawn happy
    shawn.say "Have sexual intercourse with her, and all that stuff!"
    show shawn normal
    "Yeah, I know that it's kind of awkward."
    "But that's one of the things that makes Shawn so cute."
    "So I nod at everything he's saying."
    "And at the same time, I start to take off my clothes too."
    "As soon as he realises what I'm doing, Shawn stops talking."
    show shawn surprised blush
    "And instead he starts gaping at me."
    "It's almost like I can feel his eyes travelling over my body."
    show shawn stuned
    "The feeling getting more real and more intense the closer I get to being naked."
    "I can't remember the last time I had a more captivated audience for something like this."
    "And pretty soon the temptation becomes too much to resist."
    "So as soon as it comes to the time to take off my panties, I turn my back on Shawn."
    "Then I toss them over my shoulder, managing to make them land straight on his head!"
    show shawn surprised
    shawn.say "Oh..."
    shawn.say "Oh wow..."
    shawn.say "[hero.name], I...I don't know what to say!"
    show shawn embarrassed
    "I turn my head to look back over my shoulder at Shawn."
    "And as soon as he's looking me in the eye, I let out a giggle."
    bree.say "Ha, ha..."
    bree.say "Oh, Shawn, you don't have to say anything."
    bree.say "Just get naked, and then let nature take it's course!"
    show shawn surprised
    "Shawn stares at me for a few seconds longer."
    "The whole time his mouth is hanging open and his eyes are kind of glazed over."
    "But then it's like a switch flicks in his head, and his whole demeanour changes."
    show shawn normal
    "Suddenly his eyes are clear and his expression determined, like he knows just what to do."
    "And the next thing I know, he's almost tearing at his own clothes as he walks towards me."
    "I know that I kind of had to goad Shawn into acting like this, into taking the initiative."
    "But now that he is, I can't help feeling more that a little excited at the prospect."
    "He's one of those guys that can be so shy and awkward most of the time."
    "Yet when that fire's lit inside, there's no stopping him!"
    show shawn naked with dissolve
    "By the time Shawn makes it over to me, he's totally naked."
    "And a quick glance down shows me that he's more than ready to take up my challenge."
    "That sense of anticipation and excitement is building now, getting bigger all the time."
    "I still have my back turned to him, and I don't make any effort to turn around."
    show shawn nice at center, traveling (1.5, 1.0, (640, 1080))
    "This means that when he reaches out for me, he embraces me belly to back."
    "A shiver runs down my spine as his hands travel around and begin to caress me."
    scene bg black
    show shawn reverse cowgirl livingroom smile at zoomAt(1.5, (0, 0))
    with fade
    "At once they're all over my hips, belly and then my breasts."
    "Shawn's touch is gentle and yet there's no hint of him being afraid any longer."
    "He explores me with a growing sense of confidence too."
    "And when he begins to plant kisses on my neck, I feel myself begin to melt."
    show shawn reverse cowgirl closed
    bree.say "Mmm..."
    show shawn reverse cowgirl normal back
    bree.say "Oh yeah..."
    bree.say "Just like that, Shawn, just like that!"
    show shawn reverse cowgirl smile
    "I don't know if he hears me or not, but Shawn does exactly as I ask."
    "He treats me to more of the same, keeping the motions yet increasing the intensity."
    "I can already feel the sensation of his manhood brushing against me."
    "But when it slides between my thighs, I almost go weak at the knees!"
    "I know that I want it, and I want it badly."
    "Yet I need to know that once I have it, I can enjoy every last moment."
    "That's why I begin to lower myself down towards the ground."
    "I'm sure to keep myself pressed against Shawn as I do so."
    "My hope is that he'll read my intentions and follow me."
    "Or at the very least hurry after me if I wander out of his grasp."
    "My luck seems to be in this time, as he follows me down without a hitch."
    "But once we're crouching on the ground, I decide that it's time for me to take over."
    show shawn reverse cowgirl livingroom at traveling (1.0, 1.0, (0, 0))
    "Gently pushing Shawn down further still, I straddle his thighs."
    "And still with my back turned to him, I reach down and grab his cock."
    "Shawn gasps the moment that my fingers close around the shaft."
    "The sound is really gratifying."
    "Almost as much as the sensation of the thing in the palm of my hand."
    "I feel like the moment is right to get things moving."
    "That if I try to pause and savour the feeling for too long it could pass."
    "So raising myself up, I push Shawn's member between my thighs for real this time."
    "Lowering myself back down slowly, I wait for it to slide against the lips of my pussy."
    "When it does, the motion is smooth and achingly slow."
    "But I have to bite my lip, causing myself real pain."
    "Because the feeling of it makes me want to rush what comes next."
    "The desire to have him inside of me is becoming more intense with each passing second."
    "And now I'm having to fight to keep from forcing him into me."
    "Somehow I manage to keep a hold of myself, to stay in control."
    "Moving up and down, I drag the tip in the same motion."
    "Each pass makes Shawn gasp and moan."
    "But at the same time I have to keep my mouth tightly shut."
    "My teeth grind together from the effort of restraining myself."
    "And only when the lips of my pussy begin to open do I even think of letting go."
    "At first, Shawn slips inside by perhaps an inch."
    "Then another follows, and another."
    show shawn reverse cowgirl vaginal pleasure
    "My mouth opens as well, and I let out a moan for every one."
    bree.say "Ah..."
    bree.say "Oh..."
    show shawn reverse cowgirl closed
    bree.say "Oh fuck..."
    show shawn reverse cowgirl down back
    "It feels like it takes forever for him to get all the way inside."
    "And while he does, I seem to be frozen, totally unable to move."
    "But once I know that he can't go any deeper, all of that seems to change."
    "My body simply won't accept that there's nothing more to be had."
    hide shawn reverse cowgirl
    show shawn reverse cowgirl vaginal up back pleasure livingroom
    "And so I begin to lift myself up and then lower my body of my own accord."
    "Slowly at first, but getting faster with each passing second."
    show shawn reverse cowgirl up smile
    pause 0.2
    show shawn reverse cowgirl down at startle(0.05,-10)
    pause 0.2
    show shawn reverse cowgirl up
    pause 0.2
    show shawn reverse cowgirl down at startle(0.05,-10)
    "Soon enough I'm riding Shawn's cock as though my life depends on it."
    show shawn reverse cowgirl up smile
    pause 0.2
    show shawn reverse cowgirl down at startle(0.05,-10)
    pause 0.2
    show shawn reverse cowgirl up
    pause 0.2
    show shawn reverse cowgirl down at startle(0.05,-10)
    "The memory of his hands all over me is still fresh in my mind."
    show shawn reverse cowgirl down closed
    "And I find myself waiting for them to return as I bounce on his cock."
    "Luckily for me it doesn't take long for Shawn to remind me of it either."
    show shawn reverse cowgirl up smile
    pause 0.2
    show shawn reverse cowgirl down at startle(0.05,-10)
    pause 0.2
    show shawn reverse cowgirl up
    pause 0.2
    show shawn reverse cowgirl down at startle(0.05,-10)
    "He grabs me by the haunches first, almost like he's hanging on for dear life!"
    "But as I settle into a rhythm and he matches it, that changes."
    show shawn reverse cowgirl up smile
    pause 0.2
    show shawn reverse cowgirl down at startle(0.05,-10)
    pause 0.2
    show shawn reverse cowgirl up
    pause 0.2
    show shawn reverse cowgirl down at startle(0.05,-10)
    "I feel his hands begin to wander again, exploring me for a second time."
    "Just like before the sensation only serves to add to my pleasure."
    show shawn reverse cowgirl up
    pause 0.2
    show shawn reverse cowgirl down at startle(0.05,-10)
    pause 0.2
    show shawn reverse cowgirl up
    pause 0.2
    show shawn reverse cowgirl down at startle(0.05,-10)
    "And that's because I swear I can feel the delight Shawn's experiencing too."
    "Some guys just pinch and squeeze, like they're checking out fruit."
    "But with Shawn I feel like he cherishes the change to touch me."
    "Like he's being indulged and wants to make the absolute most of it."
    show shawn reverse cowgirl up smile
    pause 0.2
    show shawn reverse cowgirl down at startle(0.05,-10)
    pause 0.2
    show shawn reverse cowgirl up
    pause 0.2
    play sound spank
    show shawn reverse cowgirl down ahegao slap with hpunch
    "Even when he surprises me by giving my ass a pretty hard slap, it only serves to thrill me."
    "As it speaks to me of the way his confidence must be growing."
    "And my response is to speed up without a conscious thought."
    show shawn reverse cowgirl up back -slap
    pause 0.15
    show shawn reverse cowgirl down at startle(0.05,-10)
    pause 0.15
    show shawn reverse cowgirl up
    pause 0.15
    show shawn reverse cowgirl down at startle(0.05,-10)
    "By now I'm almost throwing my weight down onto Shawn."
    show shawn reverse cowgirl up
    pause 0.15
    show shawn reverse cowgirl down at startle(0.05,-10)
    pause 0.15
    show shawn reverse cowgirl up
    pause 0.15
    show shawn reverse cowgirl down at startle(0.05,-10)
    "At the same time he's thrusting upwards too."
    show shawn reverse cowgirl up
    pause 0.15
    show shawn reverse cowgirl down at startle(0.05,-10)
    pause 0.15
    show shawn reverse cowgirl up
    pause 0.15
    show shawn reverse cowgirl down at startle(0.05,-10)
    "I don't know how long we've been going at it so far."
    "But one thing I do know is that I can't keep it up much longer."
    show shawn reverse cowgirl up
    pause 0.15
    show shawn reverse cowgirl down at startle(0.05,-10)
    pause 0.15
    show shawn reverse cowgirl up
    pause 0.15
    show shawn reverse cowgirl down at startle(0.05,-10)
    "Like he's reading my mind, Shawn speaks up too."
    shawn.say "Ah..."
    shawn.say "[hero.name]..."
    show shawn reverse cowgirl up
    shawn.say "I'm going to...going to cum!"
    menu:
        "Make him cum inside":
            show shawn reverse cowgirl up
            pause 0.15
            show shawn reverse cowgirl down at startle(0.05,-10)
            pause 0.15
            show shawn reverse cowgirl up
            pause 0.15
            show shawn reverse cowgirl down at startle(0.05,-10)
            "I make sure to keep my weight pressing down on Shawn as it happens."
            "Burying him deep inside of me the moment that he shoots his load."
            show shawn reverse cowgirl up
            pause 0.15
            show shawn reverse cowgirl down at startle(0.05,-10)
            pause 0.15
            show shawn reverse cowgirl up
            pause 0.15
            show shawn reverse cowgirl down creampie with vpunch
            "I was sure that I couldn't feel more than I was the moment before."
            show shawn reverse cowgirl up
            pause 0.15
            show shawn reverse cowgirl down creampie with vpunch
            "But as soon as he fills me, I realise how wrong I was."
            show shawn reverse cowgirl up ahegao
            pause 0.15
            show shawn reverse cowgirl down creampie with vpunch
            "Bracing myself against his thighs, I hold on until the very end."
            "Just praying that my muscles won't turn to jelly before it's over."
        "Pull him out":
            "Allowing myself to go higher than before, I lift myself off of Shawn."
            show shawn reverse cowgirl up -vaginal ahegao
            "I gasp as his cock slides out of me, and I hear him doing the same."
            "Then I sit back down, having a second to collect myself before it happens."
            show shawn reverse cowgirl cumshot with vpunch
            "Shawn covers the small of my back a moment later, and I feel it running downwards."
            show shawn reverse cowgirl cum body with vpunch
            "Though all the time I'm still feeling the effects of my own climax."
            with vpunch
            "Bracing myself against his thighs, I hold on until the very end."
            "Just praying that my muscles won't turn to jelly before it's over."
    $ shawn.sexperience += 1
    scene bg livingroom with fade
    "Afterwards we hurry to get cleaned up and collect our clothes."
    "Then we dress as quickly as we can, trying to hide all of the evidence."
    "Because suddenly the idea of [mike.name] or Sasha walking in seems terrifying."
    "And neither of us wants to have to explain why we're naked in the sitting-room."
    "Never mind own up to any suspicious stains on the carpet."
    return

label shawn_female_event_03:
    if shawn.love.max < 60:
        $ shawn.love.max = 60
    $ shawn.flags.nodate = False
    $ shawn.flags.nokiss = False
    scene bg bedroom4 with fade
    "I never thought I was one of those people that always had their phone in their hand and their eyes on the screen."
    "At least that was until I woke up this morning and reached out for mine like I do before I even have my eyelids open."
    "Looking at the blank screen with an equally blank expression, at first I have no idea of what's going on right now."
    "Swiping the screen over and over again, I'm met with nothing at all every time, which is starting to make me worry."
    "Frowning I begin to wonder if I forgot to plug the thing in to charge last night."
    "A quick check confirms not only that I didn't, but also that the charger is still plugged into the phone."
    "Sitting up and still fiddling with the thing, the only conclusion I can reach is that it's totally broken."
    "As soon as I accept the reality of the situation, I feel a sudden surge of panic welling up inside of me."
    "All at once I'm worrying about people trying to get hold of me and urgent messages going unseen."
    "The sensation takes me totally by surprise, as like I already said, I never thought I was addicted to my phone."
    "But I guess I was wrong, as all I can think about is the urgent need to get up, get out of the house and get it fixed."
    scene bg livingroom with fade
    "Once I have my clothes on and I'm leaving the house, I realise I should find a repair shop."
    "No worries, I'll just check the internet..."
    "Oh no I won't, because my phone's not working!"
    scene bg street with fade
    "Okay, okay...I can remember that there's an electronics store that's good for this kind of thing."
    "I'll call a taxi and head straight over there..."
    "Oh no I won't, because my phone's not working!"
    "Urgh..."
    "I'm starting to sense a pattern here!"
    "So feeling like a person living in the dark ages, I do the best I can to hurry to the electronics store."
    scene bg mall1 with fade
    "It's only when I make it to the doors that I remember something important."
    "This is the store where [mike.name]'s told me Shawn works as the manager."
    "The thought restores a little of my shattered confidence."
    "Because that means Shawn has to be really good with technical stuff, right?"
    scene bg electronic with fade
    "I really hope so, because I'm still pining for my texts and emails as I push the door open and step inside."
    "Ignoring all of the shiny new things on the shelves and racks, I make straight for the main desk."
    "That's where I'm expecting to see Shawn's familiar face, smiling as he greets his newest customer."
    "Then he'll tell me it's no big deal, and fix my phone in record time, like an electronic knight in shining armour."
    show amy normal work at center, zoomAt(1.25, (640, 880)) with easeinleft
    amy.say "Hi there..."
    amy.say "My name's Amy..."
    amy.say "How can I help you today?"
    "That can't be right."
    "When did Shawn turn into a bored-looking goth girl?"
    "And since when did he start calling himself 'Amy'?"
    "I shake my head a little, trying to tune back into reality."
    "Of course this Amy girl isn't Shawn - am I really that out of it?"
    bree.say "Oh..."
    bree.say "Of course you are..."
    bree.say "I was kind of looking for Shawn?"
    bree.say "Is he around at all?"
    show amy flirt at startle
    "Rather than answering my question, Amy laughs."
    "And her mouth curls into an ironic, knowing smile."
    amy.say "Huh..."
    amy.say "I guess there's a first time for everything!"
    show amy normal
    "I can't help showing my confusion."
    bree.say "I..."
    bree.say "I don't know what you mean."
    show amy flirt
    amy.say "This is the first time a pretty girl came in here and asked to see Shawn!"
    amy.say "The only people who do that are usually his friends."
    amy.say "All of whom are guys, and some of whom are even geekier than he is."
    amy.say "If you can believe that!"
    show amy normal
    menu:
        "Defend Shawn":
            "I'm totally aware of the fact that Shawn's a nerd."
            "Hell, it's something that's made me chuckle more than once in the past."
            "But for some reason, when I hear it coming from this girl, it's different."
            "When I listen to her making fun of him, it just really makes me dislike her."
            bree.say "Wait a minute, Amy..."
            bree.say "Isn't Shawn the manager of this store?"
            "Amy seems surprised by the tone that I'm taking with her."
            "She stops laughing and becomes a little more serious."
            amy.say "Yeah, he's the manager here."
            amy.say "What's that got to do with anything?"
            "I raise an eyebrow, like I'm looking her over."
            bree.say "Doesn't that also mean he's your boss?"
            bree.say "So is it really a good idea to be so disrespectful of him?"
            show amy embarrassed
            "Amy looks even more surprised than before."
            shawn.say "You know what, Amy..."
            shawn.say "The lady does have a point!"
            show amy at center, zoomAt(1.25, (340, 880))
            show shawn smile work at center, zoomAt(1.25, (840, 900))
            with easeinright
            "Amy turns leaps away from Shawn at the same time."
            "No doubt mortified that he was able to walk up behind her and hear what she was saying."
            amy.say "I'm..."
            amy.say "I'm gonna go take my break!"
            hide amy
            show shawn work at center, zoomAt(1.25, (640, 900))
            with easeoutleft
            "Amy scuttles off into the back of the store, leaving me alone with Shawn."
            show shawn smug
            shawn.say "Don't mind her, [hero.name]..."
            shawn.say "I'll pay her back when it's time for her annual review!"
            $ hero.morality += 1
        "Joke about Shawn":
            "I guess that I can believe what Amy's saying is true."
            "Shawn is a total nerd after all."
            "And as much as I like the guy, I don't know if I could work with him."
            "Plus everyone has a right to bitch about their boss, right?"
            "It's like an unwritten rule no matter where you work."
            bree.say "Don't let him hear you saying that, Amy..."
            bree.say "Or else he'll try to prove you wrong."
            bree.say "You know, by talking for an hour about how he's just passionate about sci-fi."
            bree.say "And how you have to be really intelligent to like that kind of stuff!"
            "Amy chuckles again, shaking her head."
            show amy flirt
            amy.say "Wow..."
            amy.say "You really do know Shawn, don't you?"
            amy.say "I mean, before I worked here I thought I'd met massive geeks."
            amy.say "But he's like, what, the total king of the nerds or something?"
            shawn.say "I'm totally the king of this store, that's for sure!"
            show amy at center, zoomAt(1.25, (340, 880))
            show shawn smile work at center, zoomAt(1.25, (840, 900))
            with easeinright
            "Amy turns leaps away from Shawn at the same time."
            "No doubt mortified that he was able to walk up behind her and hear what she was saying."
            show amy embarrassed
            amy.say "I'm..."
            amy.say "I'm gonna go take my break!"
            show shawn smug
            shawn.say "Yeah, Amy..."
            shawn.say "You probably should do that."
            hide amy
            show shawn work at center, zoomAt(1.25, (640, 900))
            with easeoutleft
            "Amy scuttles off into the back of the store, leaving me alone with Shawn."
            "I realise that I have no idea how much of what we were talking about he actually heard."
            "Which means I also have no way of knowing if he heard me joking about him too."
            $ hero.morality -= 1
    show shawn nice
    shawn.say "So, [hero.name]..."
    shawn.say "Is this a social visit?"
    shawn.say "Or are you gracing my store as a customer?"
    show shawn smile
    "By way of an answer, I pull out my phone and place it on the counter."
    show shawn normal
    "Then I slide it over to Shawn, who doesn't hesitate to pick it up."
    bree.say "As a customer, I'm afraid."
    bree.say "I woke up to find my phone wouldn't turn on."
    bree.say "And I was hoping that you could fix it?"
    "Shawn's turning the phone over in his hands as I explain myself."
    "And I can see that he's nodding all the time he's listening to me."
    show shawn talkative
    shawn.say "Uh-huh..."
    shawn.say "Is that so?"
    show shawn normal
    bree.say "So..."
    bree.say "Do you know what the problem is?"
    show shawn smile
    "Much to my relief, Shawn looks up from the phone with a smile on his face."
    show shawn nice
    shawn.say "I do, [hero.name]..."
    shawn.say "Must have fixed a hundred of this model in the past."
    shawn.say "And it's almost always the same thing."
    shawn.say "Wait here a second, okay?"
    hide shawn with easeoutright
    "I nod and then watch as Shawn disappears into the back of the store."
    "And I'm expecting to have to wait a good while before he comes back."
    "Something made far worse thanks to the obvious lack of a phone to entertain myself with."
    "But it can't be more than a couple of minutes before Shawn reappears."
    show shawn smile work at center, zoomAt(1.25, (640, 900))
    with easeinright
    "He hands me my phone, and I instinctively swipe the screen."
    "Which, much to my delight, instantly comes to life!"
    bree.say "Shawn, you fixed it..."
    bree.say "You're a genius!"
    show shawn smug
    "Shawn gives me a self-deprecating smile and shakes his head."
    show shawn nice
    shawn.say "That's a bit over the top, [hero.name]!"
    shawn.say "I'm just pretty darn good at fixing phones."
    shawn.say "And yours was a doddle."
    show shawn smile
    "I'm smiling back at him as I reach for my money."
    bree.say "So how much do I owe you for the repair?"
    "Much to my surprise, Shawn waves away my attempt to pay."
    show shawn nice
    shawn.say "No need for that, [hero.name]..."
    shawn.say "It's on the house."
    show shawn happy
    shawn.say "Any chance to help out a friend."
    show shawn smile
    menu:
        "Accept the freebie":
            "I certainly wasn't expecting that."
            "And part of me wonders if I should insist on paying."
            "But then I see the way that Shawn's smiling at me."
            "And it makes me realise that he really must see me as a friend."
            "So I'd be throwing that back in his face if I refused his offer."
            bree.say "Aww..."
            bree.say "Thank you, Shawn!"
            bree.say "That's so kind of you."
            "Shawn waves away my thanks in the same way he waved away my money a moment before."
            show shawn nice
            shawn.say "Don't mention it, [hero.name]..."
            shawn.say "I just hope I see you down here whenever you need anything electronic."
            shawn.say "Or even if you just want to drop by and hang out some time."
            $ shawn.love += 2
        "Insist on paying":
            "I certainly wasn't expecting that."
            "And I'm all set to just thank Shawn and let him give me a freebie."
            "But then I see the way that he's smiling at me."
            "And it occurs to me that he's hoping I might become more than just a friend."
            "Though I really like the guy, I'm also afraid of leading him on."
            "I want to see how our friendship develops naturally."
            "So letting him do me favours like this one probably isn't a good idea."
            bree.say "I appreciate the offer, Shawn..."
            bree.say "But I really should pay you for the repair."
            show shawn sadsmile
            shawn.say "Don't be silly, [hero.name]!"
            shawn.say "It's not like it cost the earth."
            show shawn smile
            "Thinking quickly, I manage to hit on what I hope is a good excuse."
            bree.say "It's not that, Shawn..."
            bree.say "This is a work phone, you know?"
            bree.say "And they're really concerned about the insurance they pay for."
            bree.say "If I don't have a receipt for this repair and they find out..."
            show shawn normal
            "Shawn seems to instantly get where I'm going with this."
            "Because he nods and starts to ring the whole thing through the till."
            show shawn complain
            shawn.say "Say no more, [hero.name]..."
            shawn.say "I know how these pen-pushers can be!"
    show shawn smile with fade
    "After that, I hang around in the store a little longer."
    "Just chatting to Shawn about random stuff that comes to mind."
    scene bg street with fade
    "Then I excuse myself and set off for home."
    "Almost walking into several trees and lampposts on the way as I stare at my newly-repaired phone."
    return




label shawn_female_event_04:
    if shawn.love.max < 80:
        $ shawn.love.max = 80
    scene bg pub
    "I know that some girls aren't comfortable going into a café on their own, let alone a bar."
    "But I see The Winchester as different, because it's the local pub."
    "That means it's different from a bar, more like a vital part local life, or a community hub."
    "So I don't feel in the least but awkward strolling in there when I'm on my own."
    "Most of the bar staff know me by name, and I'm likely to see people I know already in there too."
    "And I'm proven right as soon as I make it to the bar and take a look around."
    "Because as I say hi to the barman and order a drink, I spot Shawn at a table in the back."
    "I'm about to head over there, drink in hand."
    "But then I see something else that makes me stop and stare."
    "There's someone else sitting at the table with Shawn."
    "Now that wouldn't normally be a strange thing, because it's not like he doesn't have any friends."
    "It's just that almost all of them seem to be guys equally or even more geeky than Shawn is himself."
    "And believe me, that's no geeky guy sitting with him."
    "From what I can see, it's a girl."
    "And even from here I can tell that it's a pretty hot one too!"
    "Suddenly I feel an odd surge of emotion as I watch them talking."
    "I don't know what it is exactly."
    "But I have the strangest feeling it could be actual jealousy!"
    "Though maybe that's not quite it..."
    "Could it be concern for Shawn?"
    "Yeah, that sounds more like it - concern that this girl's way out of his league."
    "It must be genuine worry that she's going to hurt a really nice guy."
    "That makes so much more sense than me being jealous!"
    "And it also makes up my mind that I should go over there and introduce myself."
    "Then I can make sure that tramp doesn't eat poor Shawn alive!"
    "Doing the best I can to look casual, I walk over to their table."
    "And then I pretend to have just spotted Shawn."
    bree.say "Oh, what a coincidence..."
    bree.say "Shawn, fancy seeing you in here!"
    show shawn stuned at center, zoomAt(1.5, (640, 1080)) with fade
    "At the sound of my voice, Shawn looks up in surprise."
    "And I can instantly see that he has that starry-eyed look about him."
    "The one that guys only get when they're totally obsessed with something."
    show shawn surprised
    shawn.say "B...[hero.name]?"
    shawn.say "Hey, [hero.name]!"
    shawn.say "What are you doing here?"
    show shawn smile
    "I hold up my drink and take a sip as an answer to the question."
    bree.say "Same thing as anyone else, Shawn..."
    bree.say "Just popped in for a cool, refreshing drink!"
    bree.say "How about you?"
    "I'm feeling pretty pleased with myself that all of Shawn's attention is now on me."
    "But that doesn't seem to go unnoticed, as his attention is soon torn away again."
    show shawn stuned at center, zoomAt(1.5, (440, 1080))
    show palla vangry at center, zoomAt(1.5, (840, 1040))
    with easeinright
    palla.say "AHEM!"
    palla.say "I'm still here, you know?"
    palla.say "And I'm not going to be ignored!"
    show palla annoyed
    "As soon as his companion speaks up, the spell is broken."
    "Shawn's head spins back in her direction once again."
    "And just like that, almost all of his attention is back on her."
    show shawn complain
    shawn.say "Oh..."
    shawn.say "Oh no..."
    shawn.say "Sorry, Palla, sorry!"
    show shawn sad
    "Shawn seems to be almost grovelling in front of this Palla girl."
    "Like he's actually worried he offended her by talking to me for a few seconds."
    "Not waiting for an invitation, I pull out a chair and sit down at their table."
    "And I kind of do this because I'm betting it'll go down with Palla like a turd in her drink."
    "Which, from the look on her face, is exactly right."
    show shawn normal
    show palla angry
    palla.say "Humph..."
    show palla joke
    palla.say "Why don't you just go ahead and invite yourself into our conversation?"
    show palla normal
    "Of course Palla's words are dripping with sarcasm."
    "But I choose to totally ignore that, knowing it'll irritate her even more."
    show palla annoyed
    bree.say "Oh..."
    bree.say "That's so sweet of you, Palla!"
    bree.say "I'm [hero.name], by the way."
    bree.say "Are you another one of Shawn's friends?"
    show shawn smile
    "Shawn nods his head and makes to open his mouth."
    "Obviously eager to answer in the affirmative."
    show shawn nice
    shawn.say "Yea..."
    show shawn normal
    "But Palla cuts right across him, just like he's not there at all."
    "And his laugh is enough to curdle milk."
    show palla joke
    palla.say "HAH!"
    palla.say "His friend?"
    palla.say "He wishes I was!"
    show palla normal
    "Shawn seems to have recovered enough to speak up for himself by now."
    "And he rubs a hand on the back of his head, doing the best he can to smile."
    "But it doesn't take a genius to spot that he looks seriously embarrassed."
    show shawn happy
    shawn.say "Ha, ha!"
    shawn.say "Oh, Palla..."
    shawn.say "You're so funny!"
    show shawn nice
    shawn.say "You crease me up all the time."
    show shawn sadsmile
    "Without even turning to look at me, Shawn goes on."
    show shawn talkative
    shawn.say "Palla's my housemate, [hero.name]..."
    shawn.say "We live together."
    show shawn normal
    "I nod."
    bree.say "I see."
    bree.say "Just like [mike.name], Sasha and me."
    show palla submissive
    "Palla lets out a long sigh and shakes her head."
    "Somehow she manages to make every word she says to me sound like it's a chore."
    show palla talkative
    palla.say "How many times, Shawn?"
    palla.say "We do not live together."
    palla.say "We are both tenants of the same rental property."
    palla.say "The way you put it implies a social bond between us where none exists."
    show palla normal
    "I find myself blinking in disbelief at the way Palla's talking to Shawn."
    "I mean, she makes it sound like he's something she found on the sole of her shoe!"
    "I'm about to ask him if he's really going to let her talk to him like that."
    "But then I see the way that he's looking at her, almost mooning over her."
    "And I realise that he's totally obsessed with this awful girl!"
    show shawn nice
    shawn.say "Oh, [hero.name]..."
    shawn.say "Isn't Palla a riot?"
    shawn.say "She could totally be in that 'Intercourse in the Inner-city' TV series!"
    show shawn sadsmile
    "I tend to agree with Shawn on that one."
    "Because she seems to be more than enough of a bitch!"
    bree.say "I don't know, Shawn..."
    bree.say "I never saw that series."
    "Shawn's about to say something else."
    "No doubt praising Palla's other imaginary virtues."
    "But instead she cuts him off by standing up without warning."
    show palla talkative
    palla.say "I need to go and powder my nose."
    palla.say "I'll be right back."
    hide palla
    show shawn smile at center, zoomAt(1.5, (640, 1080))
    with easeoutright
    "As soon as Palla's gone, I lean in and smile at Shawn."
    bree.say "Do you think she means put on more make-up or snort something off the toilet seat?"
    show shawn stuned
    "But rather than laughing along with me, Shawn looks genuinely shocked."
    show shawn surprised
    shawn.say "[hero.name]!"
    shawn.say "How can you talk about Palla like that?"
    shawn.say "She's not that kind of girl!"
    show shawn normal
    menu:
        "Tell Shawn that Palla treats him like dirt":
            "I can see that this girl is just stringing Shawn along."
            "That she's using him for whatever he'll offer up."
            "And all she has to do is keep fluttering her eyelashes on occasion."
            "He might not like to be told as much."
            "But I feel like I have to speak up."
            bree.say "Then what kind of girl is she, Shawn?"
            bree.say "Because she sounds like the kind that looks down her nose at you!"
            "Shawn gapes at me, his eyes going wide."
            "And he's already started shaking his head."
            show shawn talkative
            shawn.say "What are you talking about, [hero.name]?!?"
            shawn.say "Palla and I are friends...good friends!"
            shawn.say "It just takes a while to tune into her sense of humour, that's all."
            show shawn normal
            "I can't help rolling my eyes as Shawn makes excuses for Palla."
            bree.say "You think you're her fried, Shawn."
            bree.say "But she doesn't see you the same way."
            "Shawn tries to say something in response."
            "But more than once he seems to stumble over his words."
            "And when he finally comes out with it, his answer is a pretty weak one."
            show shawn talkative
            shawn.say "Well..."
            shawn.say "Maybe..."
            shawn.say "Maybe you're just a little jealous of Palla."
            shawn.say "It's nothing to be ashamed of, [hero.name] - most women are!"
            $ shawn.love -= 1
            $ hero.morality += 3
        "Apologise and tell Shawn that Palla seems nice":
            "I can see that nothing I say is going to get through to Shawn."
            "He's in that special place guys go mentally when they fixate on a girl."
            "She could probably slap him in the face and he'd thank her for the privilege."
            "Plus I run the risk of turning him against me if I keep dumping on Palla too."
            "So the only thing I can do is to play along."
            bree.say "I'm sorry, Shawn..."
            bree.say "I sometimes do this when I meet someone new."
            bree.say "I use humour to hide my nerves, you know?"
            show shawn smile
            "Shawn seems to soften as I say all of this."
            "Which I guess means that he's buying it."
            show shawn nice
            shawn.say "I can understand you being nervous, [hero.name]..."
            shawn.say "Palla's just so smart and beautiful..."
            shawn.say "She's like something out of a Hollywood movie!"
            show shawn smile
            "Urgh..."
            "If he goes on like this, I'm going to throw up!"
            bree.say "She seems...very nice."
            "Shawn just nods and smiles at this."
            "His head probably filled with dreamy images of Palla right now."
            $ shawn.love += 1
            $ hero.morality -= 3
    show shawn normal at center, zoomAt(1.5, (440, 1080))
    show palla whining at center, zoomAt(1.5, (840, 1040))
    with easeinright
    palla.say "Shawn..."
    palla.say "I'm tired of this place now."
    palla.say "So I'm going somewhere else."
    show palla annoyed
    "Shawn and I turn to see that Palla's come back from the bathroom."
    "And it looks like she's ready to leave the pub."
    "But I note that she makes no attempt to invite Shawn along with her."
    "Even so he hurries to leap up and out of his seat to do so."
    "And he almost knocks the table over in the effort too!"
    show shawn nice
    shawn.say "O...okay, Palla..."
    shawn.say "Wait for me!"
    show shawn normal
    show shawn normal at center, zoomAt(1.5, (640, 1080))
    show palla at center, zoomAt(1.5, (1040, 1040))
    with ease
    "I offer up a little wave as they walk away."
    bree.say "Bye, Shawn..."
    bree.say "Bye, Palla..."
    bree.say "It was nice meeting you!"
    show palla joke
    palla.say "Of course it was..."
    palla.say "Even if the feeling wasn't mutual!"
    hide shawn
    hide palla
    with easeoutright
    "My mouth drops open as that awful girl manages to get the last word."
    "And I'm left there wondering if she invited Shawn along with her tonight at all."
    "Or if he just followed her from their place like a love-sick puppy!"
    "Yeah...I definitely don't like this Palla, not at all."
    "And it's totally because of how she's treating poor, innocent Shawn."
    "I mean, it's not like I'm jealous of all the attention he's giving her."
    "No, it's nothing like that."
    "I'm just being a good friend, showing concern for the guy."
    "And anyway, even if she is pretty and well-dressed, she's not good enough for him."
    "Shawn's sweet and funny, in a nerdy kind of way."
    "He needs a girl that appreciates him for who he is."
    "Not one that looks at him like a cockroach she found in her dinner!"
    $ shawn.flags.shawndelay = TemporaryFlag(True, 1)
    return


label shawn_female_event_05:
    if shawn.love.max < 100:
        $ shawn.love.max = 100
    scene bg door pub with fade
    "It's weird, but a short time back I'd have been worried about it being just Shawn and me at The Winchester."
    "You know how it is when you're just starting to get used to a person, and it's still kind of awkward?"
    "I'd have made an excuse to get out of it, or insisted that someone like [mike.name] come along too as an unofficial chaperone."
    show shawn normal at center, zoomAt(1.25, (640, 920)) with fade
    "But when Shawn and I find ourselves outside the pub, I just open my mouth and the words come right out."
    bree.say "Hey, Shawn..."
    bree.say "You want to grab a drink?"
    show shawn stuned
    "Shawn seems a little surprised to hear me making the invitation."
    show shawn smile
    "But even so he starts nodding almost instantly."
    show shawn talkative
    shawn.say "Erm..."
    shawn.say "I was thinking of maybe heading home."
    show shawn nice
    shawn.say "But yeah, I could go for one right now."
    show shawn smile
    "I nod too, pleased to hear that Shawn's up for it too."
    bree.say "That's great, Shawn..."
    bree.say "Let's go inside and get ourselves a cold one."
    scene bg pub with fade
    "As we're walking in, Shawn seems to be looking around the whole time."
    show shawn embarrassed at center, zoomAt(1.5, (940, 1080)) with easeinright
    "Like he's expecting to see something or someone when we get inside the pub."
    show shawn at center, zoomAt(1.5, (640, 1080)) with ease
    "And he's still doing it when we get to the bar."
    "I'm about to ask him what's up, when the barman walks over."
    "Barman" "What can I get you guys?"
    "I look over at Shawn."
    bree.say "Beer?"
    show shawn nice
    shawn.say "Oh yeah!"
    show shawn smile
    bree.say "Two beers, please."
    "I make to pay for the drinks."
    "But I see that Shawn's already trying to do the same thing."
    menu:
        "Let Shawn buy the beers":
            "I shrug and put my own card away."
            "Which Shawn takes as permission to step up and pay."
            "I don't want him to think that I'm taking advantage of his kindness."
            "But then it is just one round of drinks for the two of us."
            "And I guess it'll make him happy too."
            $ shawn.love += 1
        "Insist on buying the beers" if hero.money >= 25:
            "I shake my head and push his card to one side."
            bree.say "This was my idea, so I'll get the drinks."
            show shawn upset
            "Shawn looks like he's about to argue."
            "But then shrugs and puts his card away."
            "I hope I haven't upset him too much by doing that."
            "Though this way I do feel a little more like I'm the one in control here."
            $ hero.money += 25
            $ shawn.love -= 1
    show shawn annoyed with fade
    "It's just then that I notice Shawn's gone back to looking a little uneasy."
    "So I feel like I have to ask him what's up."
    bree.say "Are you okay, Shawn?"
    bree.say "Because you seem like you're waiting for something to happen."
    bree.say "And I really don't know what it is!"
    show shawn embarrassed
    "Shawn shrugs as we wait for the barman to pour our drinks."
    "And I can see that he looks more than a little embarrassed."
    show shawn talkative
    shawn.say "Well..."
    shawn.say "I was expecting there to be other people here, you know?"
    shawn.say "Like [mike.name] or Jack, or your other housemate."
    show shawn sadsmile
    "Now I'm the one that's beginning to feel confused."
    "I can't help frowning and shaking my head at Shawn."
    bree.say "But I didn't say we were meeting anyone else."
    bree.say "So why would you even think that?"
    "Shawn seems to realise just how crazy he's starting to sound."
    "And he holds up his hands, like he's about to level with me."
    show shawn talkative
    shawn.say "Okay, [hero.name]..."
    shawn.say "It's kind of like this..."
    shawn.say "I'm not exactly used to girls asking me to go for a drink with them."
    shawn.say "To be more specific, with JUST them, yeah?"
    shawn.say "It's usually that I get to tag along, but only as part of a bigger group."
    show shawn embarrassed blush
    "Well now I understand what the problem is!"
    bree.say "Well I guess that means I'm not a normal girl!"
    bree.say "No, wait...that doesn't sound quite right..."
    bree.say "I mean I'm an unusual kind of girl - if that makes sense?"
    show shawn nice
    shawn.say "Erm...yeah..."
    shawn.say "I think I get the essence of what you're trying to say!"
    show shawn sadsmile
    "I can't help beginning to laugh at how stupid we both sound."
    show shawn happy at startle
    "And it helps when Shawn starts to laugh along with me."
    "The mutual laughter seeming to mean we can draw a line under the confusion and move on."
    scene drink_room_pub
    show shawn casual smile at center, zoomAt(1.75, (440, 1180))
    show drink_table_pub_victor
    show drink_room_fg_pub
    with fade
    "With our drinks in hand, we find a place to sit."
    show shawn sadsmile
    "But then we find ourselves staring at each other in an awkward silence."
    bree.say "Sooo..."
    bree.say "We really should talk about something, right?"
    show shawn talkative
    shawn.say "I guess so..."
    shawn.say "That's what people in these kind of situations do."
    show shawn normal
    bree.say "So do we talk about sports?"
    show shawn complain
    shawn.say "Urgh - too physical!"
    show shawn talkative
    shawn.say "How about politics?"
    show shawn normal
    bree.say "Hell no - sure to end in disaster!"
    bree.say "How about..."
    show shawn talkative
    shawn.say "Maybe we could try..."
    show shawn nice
    "[hero.name] & Shawn" "Science Fiction!"
    show shawn smug
    "Shawn's eyes go wide and I see his entire face seem to light up."
    show shawn happy
    "And I guess the same thing must be happening to me at the same time."
    "Because I can see that I'm feeling mirrored in his face too."
    bree.say "That's perfect, Shawn!"
    show shawn nice
    shawn.say "[hero.name], you read my mind!"
    show shawn smile
    "But then something else seems to strike Shawn."
    show shawn nice
    shawn.say "But, [hero.name]..."
    shawn.say "Sci-fi is such a vast and diverse cultural phenomenon."
    shawn.say "Where on earth are we going to start?"
    show shawn smile
    "I'm amazed to find that my reaction is the exact opposite of Shawn's."
    "Rather than feeling overwhelmed and intimidated, I have an instant answer."
    bree.say "We go for the big one, Shawn..."
    bree.say "We talk about the greatest sci-fi franchise of them all!"
    show shawn stuned
    "Shawn's eyes are wide as he shakes his head in disbelief."
    show shawn surprised
    shawn.say "[hero.name]..."
    shawn.say "You don't mean..."
    show shawn stuned
    "But I set my features in a determined expression as I nod."
    bree.say "Yes I do..."
    bree.say "We talk about Star Soldiers!"
    show shawn happy at startle
    "Then we both collapse into more peals of helpless laughter."
    "Enjoying the silliness and fake drama we just cooked up between us."
    show shawn nice
    shawn.say "I mean there's obviously things that we'll both agree on."
    shawn.say "We are, after all, sane and intelligent human beings."
    show shawn smile
    bree.say "Well at least one of us is!"
    show shawn talkative
    shawn.say "You know what I mean, [hero.name]..."
    shawn.say "Like we agree that the first six films are the best."
    show shawn smile
    "As soon as Shawn says the words, I start shaking my head."
    bree.say "Three!"
    show shawn surprised
    shawn.say "Huh?"
    show shawn stuned
    bree.say "You mean three, not six."
    bree.say "The prequels are a total dumpster fire!"
    "Shawn looks at me like I just announced that I killed someone."
    show shawn surprised
    shawn.say "Oh, [hero.name]..."
    shawn.say "Tell me it's not true!"
    shawn.say "Tell me you're not a prequel-hater?!?"
    show shawn stuned
    bree.say "But, but, but..."
    bree.say "They're all shallow, boring commercials for kid's toys!"
    show shawn sad
    "Shawn shakes his head."
    show shawn complain
    shawn.say "[hero.name], [hero.name], [hero.name]..."
    shawn.say "You have to get over this obsession with a perfect, imagined past."
    shawn.say "Once you do that, you'll realise the importance of merchandising."
    show shawn sadsmile
    "I'm about to launch into another attack on Shawn's position."
    "But then I shake my head as I realise how crazy all of this is."
    bree.say "Oh my god..."
    bree.say "Why are we even arguing about this?"
    bree.say "We can just agree to disagree, can't we?"
    show shawn smile
    "Shawn frowns."
    show shawn embarrassed
    shawn.say "Hmm..."
    show shawn complain
    shawn.say "I don't know if I can agree to that!"
    show shawn sadsmile
    bree.say "SHAWN!"
    "Shawn holds up his hands in a gesture of surrender."
    show shawn happy
    shawn.say "Kidding!"
    shawn.say "Sure we can do that, [hero.name]."
    show shawn smile
    "After that we manage to have something that resembles an adult conversation."
    "And we even keep it going for another couple of rounds."
    "Which I guess proves that we can both love sci-fi and be sensible adults at the same time."
    $ shawn.love += 1
    return


label shawn_female_event_06:
    if shawn.love.max < 120:
        $ shawn.love.max = 120
    scene bg pub with fade
    "Working at The Winchester might sound like less fun than being in there to drink with your friends."
    "And well...I have to admit that it kind of is!"
    "But that doesn't mean that working there is any kind of a drag."
    "It's actually a pretty sweet gig, compared to some of the shitty places I've worked in the past."
    "And one of the best things about it is on account of it being a pub, rather than a bar."
    "Because that means it's like a really important part of the local community, you know?"
    "The people that come in there to drink are regulars, familiar faces from the neighbourhood."
    "Which means that you soon get to know their names and when they're likely to walk through the door."
    "Pretty soon you start to remember their usual order and where they like to settle down to drink it."
    "And before much longer you're chatting with them about what's going on in their lives and your own."
    "Okay, I know that it's not the most demanding job that I could have gone out and applied for."
    "But that means I have the headspace to be able to think while I'm pulling pints or collecting glasses."
    "And it's great when people I know come into the pub too."
    "Because it gives me a chance to say hi and grab a few words with them."
    "You know, maybe ask them when they next want to hang out?"
    "Or at least it was until Shawn started coming in so regularly."
    "At first I thought his social life was just on the upswing."
    "You know, that he was coming in to meet people and hang out."
    "But every time it seems to turn out that he's just in here on his own."
    "And he's always here until the pub closes too, totally wasted by the time we call last orders."
    "More than once I've had to help the other bar-staff carry him outside and call him a taxi."
    "Something that's made a hundred times worse because of the fact he knows me as a friend."
    "So when he's drunk and slobbering, he's always asking for me too."
    "And I think some of the other staff are starting to resent me for it."
    "Like they assume he comes in here and gets slaughtered because of the fact he knows me!"
    show shawn blush hat complain at center, zoomAt(1.0, (640, 900)), swing(1.0, 1.0, 1.0, -3.0, 2.0)
    shawn.say "Urgh..."
    show shawn embarrassed
    shawn.say "Burp..."
    show shawn complain
    shawn.say "[hero.name]..."
    shawn.say "[hero.name]...I want the...the same again!"
    show shawn embarrassed
    "I'm in the middle of serving another customer when I hear Shawn shouting for me."
    play sound glass
    "And what's worse, he seems to think it'll help to pound his glass on the table too."
    bree.say "Just a second, Shawn..."
    bree.say "I'm a little busy right now, okay?"
    "I turn back to the customer I'm serving and offer them an apologetic smile."
    "But it doesn't take Shawn long to start up with the shouting again."
    show shawn complain
    shawn.say "Aw, come on, [hero.name]..."
    if shawn.sexperience < 1:
        shawn.say "I thought we were supposed to be mates!"
    elif shawn.sexperience >= 1:
        shawn.say "I thought we were like, a fucking item!"
    shawn.say "So that means you should serve me first, yeah?"
    show shawn annoyed
    play sound glass
    "Shawn's still hammering his glass down on the bar as he says all of this."
    "But I keep my head turned towards my current customer, tyring to ignore him."


    "That is until I hear the familiar sound of breaking glass."
    "As one, every head in the room turns towards Shawn."
    "And I see that he's standing there with a dumb look on his face."
    "Just staring at the empty hand where the glass used to be."
    "The remains of it are scattered all over the bar."
    "And it's a miracle that he isn't bleeding all over it too."
    show shawn complain
    shawn.say "Huh..."
    shawn.say "Where'd my glass go?"
    show shawn embarrassed
    "Luckily for me I've just finished with my customer."
    "So I shoot over to confront Shawn."
    show shawn at center, zoomAt(1.5, (640, 1350)), swing(1.0, 1.0, 1.0, -3.0, 2.0) with fade
    bree.say "What's wrong with you tonight, Shawn?"
    bree.say "You're more drunk than ever!"
    "Shawn does that thing where drunks take offence."
    "But they kind of reel backwards and look at you in disbelief and disgust at the same time."
    show shawn vangry
    shawn.say "Ah..."
    shawn.say "Don't lecture me..."
    shawn.say "Just gimme another one!"
    show shawn embarrassed
    "Part of me wants to confront Shawn, to really let him have it with both barrels."
    "But everyone in the pub is still watching us and there's glass everywhere too."
    "So I figure the easiest thing to do is to keep him quiet until I can clean up the mess."
    bree.say "Okay, okay..."
    "I pull the drink as quickly as I can, meaning it's mostly head."
    "But when I shove it into Shawn's open hands, he doesn't seem to notice."
    bree.say "There you go."
    bree.say "I hope you're happy now!"
    show shawn nice
    shawn.say "Absolutely ecstatic, that's me!"
    show shawn embarrassed
    "Shawn sways off with his drink, and I hurry to sweep up the glass."
    "But by the time I'm done, I haven't calmed down one iota."
    "If anything, I'm more mad than I was before I started."
    "Storming around the bar, I walk right up to the table where Shawn's sitting."
    "And then I poke a finger right into his face."
    bree.say "You need to modify your behaviour, mister!"
    bree.say "You're rude, embarrassing and totally showing me up."
    bree.say "And worst of all, you could have seriously hurt someone."
    "Shawn rolls his eyes and waves his hand at me."
    "Almost like he's dismissing me from his presence."
    show shawn vangry
    shawn.say "Ah..."
    shawn.say "Leave me alone, [hero.name]..."
    shawn.say "You're a barmaid, not my therapist!"
    shawn.say "Go change the barrel or something else that's actually useful..."
    show shawn embarrassed
    bree.say "Don't you speak to me like that!"
    bree.say "You know that I can bar you from this place, right?!?"
    show shawn complain
    shawn.say "Urgh..."
    shawn.say "I don't have to stay here and take this from you!"
    show shawn embarrassed
    "Shawn suddenly lurches up and out of his seat."
    "The motion pushes over the table he was sat at."
    "And I have to leap backwards as his drink spills onto the floor."
    hide shawn with easeoutright
    "But before I can say anything more to him, he's swaying towards the door."
    "I think about following him, but then dismiss the idea."
    "Because I'm worried about what I'd say to him if I did confront him right now."
    "So instead I shake my head, and then begin to clean up the mess he's left in his wake."
    $ shawn.love -= 5
    return


label shawn_female_event_07:
    if shawn.love.max < 140:
        $ shawn.love.max = 140
    "I'm still wincing every time I think of just how drunk Shawn was the last time I saw him in The Winchester."
    "He was rude and surly, totally unlike the guy I know him to be when he's sober."
    "So I'm dreading having to call him up and see how he is the next day, but I make myself do it all the same."
    play sound cell_vibrate loop
    "I wait as the phone rings, and it takes a while for Shawn to pick up on the other end."
    show screen expression "smartphone_calling" pass ("Shawn")
    show breemc b gloomy at center, zoomAt (3.5, (840, 2040))
    with fade
    stop sound
    shawn.say "Urgh..."
    shawn.say "[hero.name]..."
    shawn.say "Is that you?"
    "He sounds absolutely awful, like he can hardly manage to sting a few words together."
    "But at least he's awake and making sense, which has to count for something."
    "So I take a deep breath and then launch into it."
    show breemc b hesitating
    bree.say "Yeah, Shawn..."
    bree.say "It's me."
    bree.say "Just wanted to check in on you..."
    bree.say "Well, you know...after last night?"
    "There's a moment of silence on the other end of the line."
    show breemc b dazed
    "And I realise that Shawn's struggling to remember the night before."
    shawn.say "Erm..."
    shawn.say "Could you help me out, [hero.name]?"
    shawn.say "Maybe jog my memory a little?"
    shawn.say "I'm afraid it's all a bit fuzzy!"
    show breemc b annoyed
    "I feel a surge of annoyance at Shawn as he asks the question."
    "As if it wasn't enough I had to deal with his drunken antics last night."
    "Now I have to walk him through it all again and remind him of all the shit he perpetrated too!"
    show breemc b sad
    bree.say "Okay, Shawn..."
    bree.say "Let's just say it was bad, and leave it at that."
    show breemc b gloomy
    "Shawn lets out a groan on the other end of the line."
    "And I get the impression that he's feeling like death warmed over right now."
    "Plus I just told him that he made a complete fool of himself in public last night."
    "But at least I can derive a little pleasure from the fact he's suffering on so many levels."
    shawn.say "Okay, look..."
    shawn.say "Whatever it was that I did..."
    shawn.say "I'm sorry, yeah?"
    "I can tell that Shawn's desperate for me to let him off the hook."
    "Probably so that he can crawl away and curl up in a corner somewhere."
    "But the irony is that I'm too good of a friend to let that happen."
    show breemc b talkative
    bree.say "Nah, Shawn..."
    bree.say "That's not going to cut it."
    bree.say "Not this time."
    bree.say "I want you to meet me for a coffee and a serious talk."
    show breemc b blank
    "Shawn sighs on the other end of the line."
    shawn.say "Fine, fine..."
    shawn.say "I'll be there as soon as I can."
    shawn.say "Just promise you'll keep your voice down."
    shawn.say "Every word you're saying is making my skull pound!"
    hide screen smartphone_calling
    scene bg black with dissolve
    pause 0.3
    scene bg coffeeshop with timelaps
    "I'm not surprised when I make it to the spot where we're supposed to meet first."
    show shawn sick at center, zoomAt(1.25, (840, 900))
    show shawn_glasses at center, zoomAt(1.25, (840, 900))
    with easeinright
    "But when I see Shawn shuffling towards me, I see that he looks even worse than he sounded on the phone."
    show shawn at center, traveling(1.5, 1.0, (640, 1080))
    show shawn_glasses at center, traveling(1.5, 1.0, (640, 1080))
    "He's hunched over, skin pale and clammy, and it seems that the light is really making him squint."
    "For a moment my instincts kick in, and I start to feel sorry for him."
    "But then I have a flashback to last night, and any hint of sympathy vanishes."
    show shawn at center, zoomAt(1.5, (640, 1180))
    show shawn_glasses at center, zoomAt(1.5, (640, 1180))
    with ease
    bree.say "Fuck sake, Shawn..."
    bree.say "You look as bad as you were behaving in the pub last night!"
    show shawn sad
    hide shawn_glasses
    "Shawn looks up to meet my eye, and I can see that he's not putting it on either."
    show shawn complain
    shawn.say "Oh lay off, [hero.name]..."
    shawn.say "My head feels like a pig shat in it!"
    show shawn sad
    bree.say "Well that does kind of serve you right!"
    bree.say "You were being a complete asshole last night."
    bree.say "I came that close to barring you from the pub."
    "Shawn squints painfully as I hold up my hand."
    "But I'm not sure he can really see my thumb and forefinger a fraction of an inch apart."
    show shawn talkative
    shawn.say "Okay, [hero.name], okay..."
    shawn.say "I already said I'm sorry."
    show shawn sadsmile
    shawn.say "It won't happen again, I promise."
    show shawn normal
    "Okay, now comes the really hard part."
    "I put a serious expression on my face."
    "And then I shake my head."
    bree.say "You and I both know that's bullshit, Shawn."
    bree.say "I've seen you almost every night for the past two weeks."
    bree.say "And you were totally shit-faced each time."
    show shawn talkative
    shawn.say "I've just been dealing with some difficult stuff recently, that's all."
    shawn.say "I needed to get away from my problems for a while, to forget about them."
    shawn.say "It's going to pass, like it always does."
    show shawn normal
    "I might not be a qualified councillor or therapist."
    "But I know denial when I hear it."
    "And I'm not going to let Shawn talk his way out of this one."
    bree.say "No it won't, Shawn..."
    bree.say "Because you're acting like an addict right now."
    bree.say "I think you need some serious help."
    bree.say "Like therapy or something, yeah?"

    if shawn.love >= 120:
        "I'm totally expecting Shawn to laugh in my face."
        "Either that or start fobbing me off with more bullshit."
        "But instead he throws me a curve-ball, by staying totally silent."
        "Almost like he's really struck by what I just said to him."
        "And when he speaks, that's pretty much how it seems."
        show shawn talkative
        shawn.say "Oh my god..."
        shawn.say "You're right, [hero.name]..."
        shawn.say "I've been kidding myself that I was okay this whole time."
        shawn.say "But you hit the nail on the head - I am turning into an addict."
        shawn.say "Hell, I probably am one already!"
        show shawn sad
        "Having been prepared for a fight, my adrenaline is up."
        "So I'm left kind of wrong-footed when Shawn admits I'm right."
        bree.say "I..."
        bree.say "I'm so relieved to hear you say that!"
        bree.say "You don't know how worried I've been for you, Shawn."
        "This really does get Shawn's attention."
        "He looks at me in genuine surprise."
        show shawn sadsmile
        shawn.say "Well that settles it then..."
        shawn.say "I really do need to get help!"
        show shawn smile
        "I find myself smiling as relief floods my body."
        "And the weight of the world seems to be lifted off my shoulders."
        $ shawn.love += 5
        $ shawn.flags.shawndelay = TemporaryFlag(True, 6)
    else:

        "It doesn't take long for Shawn's mood to change."
        "Like he's finally getting tired of listening to me."
        "And all he wants is to get away."
        show shawn complain
        shawn.say "Oh stop it, [hero.name]..."
        shawn.say "You're not a bloody doctor..."
        shawn.say "All you're doing is sticking your nose in my business!"
        show shawn annoyed
        "I shake my head, tyring to change Shawn's mind."
        bree.say "That's not how it is, Shawn..."
        bree.say "I'm trying to help you..."
        bree.say "Help you before it's too late!"
        show shawn sadsmile at startle
        "Shawn lets out a rueful chuckle."
        show shawn talkative
        shawn.say "Then help me by leaving me alone."
        shawn.say "And don't worry about barring me from The Winchester either."
        shawn.say "Because I'm going to be giving it a wide berth in future!"
        show shawn normal at center, zoomAt(1.5, (640, 1080)) with ease
        "Shawn turns away from me and then starts to walk away."
        show shawn normal at center, zoomAt(1.5, (840, 1080)) with ease
        "I hold out my hand, trying to get his attention."
        bree.say "Shawn..."
        bree.say "Wait!"
        "But it's no good."
        hide shawn with easeoutright
        "Shawn flatly ignores me and strides off."
        "Which I guess means that our chance to talk is over."
        "But whether our friendship is too, I can't say."
        $ shawn.love -= 5
    $ hero.morality += 1
    return


label shawn_female_event_08:
    if shawn.love.max < 160:
        $ shawn.love.max = 160
    "It's been a good while since Shawn and I had the confrontation about his drinking."
    "And I have to confess that after he went off to get professional help, we kind of lost contact for a short while."
    "Not like we didn't want to have anything to do with each other, nothing serious like that."
    "I guess he was just feeling ashamed of the way that he'd let himself go off the rails."
    "And on my part I needed some time and space to process my emotions before seeing him again."
    "But it seems like he's resurfaced within the past day or so, hopefully doing a lot better."
    "Because I have a text message on my phone from him, asking if we can meet up."
    "Not feeling like I want to start talking to Shawn just yet, I fire off a reply."
    "I keep the message friendly and maybe a little more non-committal than I would have otherwise."
    "And I basically agree to meet him for a chat, to catch up and see how he's doing."
    "I have to admit that I'm nervous about seeing Shawn again."
    "Part of me is still kind of sore form the way he behaved before he decided to get help."
    "He showed me up at work and made a total asshole out of himself a whole bunch of times."
    "But that's rubbing up against the part of me that really likes the guy and wants to know he's okay."
    "So yeah, I'm kind of being pulled in two directions on the way to meet him."
    scene bg coffeeshop
    show shawn normal
    with fade
    "And when I get there, I noticed that something's different right from the start."
    "Because Shawn's beat me to it, where he was late the last time."
    "I slow down as I see him waiting for me."
    "More because it's a surprise than on account of not wanting to be seen."
    "But it's already too late for that, as he just happens to turn and spot me."
    show shawn sadsmile
    "I see a smile appear on Shawn's face, but even from this far away I can tell it's a nervous one."
    "And he waves to me as I walk the last of the short distance between us."
    "I raise a hand and wave back, putting what's probably an equally nervous smile on my face too."
    show shawn smile at center, zoomAt(1.5, (640, 1080)) with fade
    "But as I get closer, the smile begins to become more genuine."
    "And that's because I can begin to see how much better Shawn's looking."
    "Before he got the professional help, he was starting to look totally wrecked."
    "I remember his eyes being hollow and his skin kind of pale in weird, waxy way."
    "Plus he always looked like he was lacking sleep and sweaty."
    "Now his skin is almost glowing, as pale as Shawn usually is."
    "There's a real light in his eyes, and he seems fresh as a daisy too!"
    bree.say "Hey, Shawn!"
    show shawn nice
    shawn.say "Hey, [hero.name]!"
    show shawn smug
    "Shawn throws his arms wide as we walk up to each other."
    "But I can't tell if he's punching the air or trying to go in for a hug."
    menu:
        "Go for a hug":
            "I'm still feeling a little awkward around Shawn."
            "But I feel like I need to make a show of the fact I support him."
            "To make a gesture that shows I'm the real deal when it comes to being a friend."
            "So I throw my arms around him and jump into the hug."
            show shawn at center, traveling(2.5, 0.5, (640, 1680))
            bree.say "Oh, Shawn..."
            bree.say "It's great to see you!"
            "Shawn takes me by surprise with the way he hugs me in return."
            "Rather than being a standard, friend-to-friend affair, it's a proper bearhug!"
            show shawn nice
            shawn.say "Aargh..."
            shawn.say "It's great to see you too, [hero.name]!"
            show shawn nice at center, traveling(1.5, 0.3, (640, 1080))
            $ shawn.love += 4
        "Punch the air":
            "I'm kind of still feeling a little awkward around Shawn."
            "So I decide to go for the safer option and punch the air."
            bree.say "Yay..."
            bree.say "It's so great to see you!"
            show shawn sad
            "Shawn seems a little disappointed that I didn't go for the hug."
            "But he does the best he can to hide the fact and be positive."
            show shawn nice
            shawn.say "It's great to see you too, [hero.name]!"
            $ shawn.sub += 2
    shawn.say "And it's great to finally be out of that place as well."
    show shawn normal at center, traveling(1.25, 0.3, (640, 900))
    "I take a step back from Shawn as he says this."
    show shawn normal at center, zoomAt(1, (640, 720))
    "Already beginning to worry that he's dumping on the help he's received."
    bree.say "What does that mean, Shawn?"
    bree.say "You're looking and sounding so much better."
    bree.say "Please tell me you're doing whatever they told you to do?"
    show shawn smile
    "As soon as he hears the question, Shawn starts to wave his hands at me."
    show shawn nice
    shawn.say "Oh no..."
    shawn.say "No, no, no..."
    shawn.say "That's not what I meant!"
    shawn.say "I just meant it's good to be out of the whole 'therapy' thing, you know?"
    shawn.say "Back in the real world, yeah?"
    show shawn smile
    "I cock my head on one side, still not totally convinced."
    bree.say "So..."
    bree.say "That means you're...better?"
    "Shawn nods eagerly, leaping on the chance to answer in the affirmative."
    show shawn nice
    shawn.say "Oh yeah, [hero.name]..."
    shawn.say "So much better!"
    show shawn sadsmile
    shawn.say "Not totally better, because they told me nobody ever is."
    shawn.say "I'm...a...a work in progress - that's what they called it."
    show shawn smile
    "Now I can feel myself starting to buy into what Shawn's telling me."
    "His words and demeanour are beginning to sound totally credible."
    bree.say "Well that's great to hear, Shawn..."
    bree.say "I mean, you really look better."
    bree.say "And you sound a lot happier too."
    show shawn happy
    "Shawn's smile becomes even wider than before."
    show shawn nice
    shawn.say "Thanks for that, [hero.name]..."
    shawn.say "I feel like this really opened my eyes."
    shawn.say "They taught me to be honest about myself, to look inside for the answers."
    shawn.say "And I realised that I have a hole in me, one I was trying to fill with the booze."
    show shawn normal
    "I know that most of what Shawn's saying is typical psycho-babble."
    "But the mention of him being lacking somehow, that cuts through everything else."
    "And it makes my heart ache for him as a friend and someone I care about."
    bree.say "And this hole..."
    bree.say "They helped you to fill it?"
    "Shawn shakes his head."
    "But then he also shrugs, as if to say it's not so serious."
    show shawn talkative
    shawn.say "No, [hero.name]..."
    shawn.say "But it's kind of a positive thing that I know it's there."
    shawn.say "Like I said, they told me I have to think of myself as a work in progress."
    shawn.say "Finding what I really need to fill that hole might take me a while."
    show shawn normal
    "All I can do is nod slowly."
    "Because that does make sense."
    "Shawn's always throwing himself into work."
    "Or else he's binging on comic-books and video-games."
    "Hell, he even runs after awful girls like uppity bitch Palla."
    bree.say "Well, all of that sounds good."
    bree.say "Just let me know if I can help you fill that hole, okay?"
    show shawn nice
    shawn.say "Don't worry, [hero.name]..."
    shawn.say "I sure will!"
    $ hero.morality += 3
    $ shawn.flags.shawndelay = TemporaryFlag(True, 3)
    return


label shawn_female_event_09:
    if shawn.love.max < 180:
        $ shawn.love.max = 180
    scene bg street
    show shawn smile at center, zoomAt(1.25, (640, 920))
    with fade
    "Ever since I convinced Shawn to get professional help for his drinking problem, things have been on an upward turn for us."
    "He's almost totally back to his old self, funny and thoughtful in a self-conscious and geeky kind of way."
    "Sure, he still has the occasional blip, where the stress of his job seems to make him feel down."
    "But it's weird, because he always seems to pick up again as soon as we're hanging out together."
    "I'm starting to think that there must be some kind of a connection between the two things."
    "Yet whenever we're together, I never seem to be able to remember to bring it up with Shawn."
    "And that's because we always have so much fun and end up laughing the whole time instead!"
    "But today is kind of a big deal in a small way, if that even makes sense."
    scene bg door pub
    show shawn smile at center, zoomAt(1.25, (640, 920))
    with fade
    "It's the first time that Shawn and I have come down to The Winchester together since..."
    "Well, since he kind of made a fool of himself while he was totally wasted."
    show shawn normal at center, zoomAt(1.25, (340, 920)) with ease
    "And as we reach the door, I can tell from the loom on his face that he's nervous."
    show shawn complain at center, zoomAt(1.25, (540, 920)) with ease
    shawn.say "Ah..."
    shawn.say "You know what, [hero.name]..."
    shawn.say "Maybe I'm not ready for this after all?"
    show shawn sadsmile
    shawn.say "We could always go somewhere else instead?"
    show shawn sad
    "I plant my fists on my thighs and give Shawn a little frown."
    "And then I look him straight in the eye."
    menu:
        "Sympathise with Shawn":
            bree.say "Look, Shawn..."
            bree.say "I know this must be hard for you."
            bree.say "But it's kind of like a part of your recovery, yeah?"
            show shawn complain
            "Shawn looks like he wants to argue with me."
            show shawn normal
            "But my supportive tone seems to make him hesitate."
            show shawn talkative
            shawn.say "You're right..."
            shawn.say "I'm just worried someone's going to recognise me."
            shawn.say "Or one of your colleagues will bar me!"
            $ shawn.love += 2
        "Tell Shawn to get over it":
            bree.say "Of come on, Shawn..."
            bree.say "You're not backing out now, are you?"
            show shawn stuned
            "Shawn looks a little surprised at my tone of voice."
            "Kind of like he was expecting more sympathy from me."
            show shawn complain
            shawn.say "Well the thought had crossed my mind!"
            shawn.say "What if someone recognises me?"
            shawn.say "What if I get barred?!?"
            $ shawn.sub += 1
    show shawn upset
    "I shake my head as I push the door open."
    "And taking hold of Shawn's hand, I pull him inside."
    scene bg pub with fade
    pause 0.3
    show shawn normal at center, zoomAt(1.25, (640, 920)) with ease
    bree.say "Most of the regulars have been there themselves, Shawn."
    bree.say "And I already spoke to the other bar-staff."
    bree.say "I explained you were going through a bad patch."
    bree.say "They all understand, and they're willing to let it go."
    "Shawn nods as I explain all of this to him."
    "But I can see that he's still looking nervous as we walk into the taproom."
    show shawn embarrassed
    "He glances this way and that, as if he expects someone to jump out and ambush him."
    "Luckily for us, the place seems pretty quiet."
    "So we can easily find an empty table in a deserted corner."
    bree.say "You sit here while I get the drinks in, okay?"
    show shawn at center, zoomAt(1.25, (440, 920)) with ease
    "Shawn nods, and then his eyes drift to one of the TV screens mounted on the wall."
    "I glance at it in passing, seeing images of people in face-masks and soldiers with rifles."
    "A map of Africa pops up on the screen, but I've seen many stories just like it in the past."
    hide shawn with fade
    "So I ignore what the anchors are actually saying and make for the bar."
    "When I get there I have to wave and shout to get the attention of the bartender."
    "Because he seems to be watching the same channel on another screen closer to the bar."
    bree.say "Hey!"
    bree.say "Over here!"
    bree.say "What does a girl have to do to get served in this place?!?"
    "Bartender" "Oh..."
    "Bartender" "Sorry, [hero.name]..."
    "Bartender" "Looks like we could be in for another pandemic!"
    bree.say "Urgh..."
    bree.say "I hope not."
    bree.say "I was so hairy at the end of the last one..."
    bree.say "I almost turned into a Neanderthal!"
    "As soon as I have our drinks, I hurry back to the table."
    scene drink_room_pub
    show shawn casual sad at center, zoomAt(1.75, (440, 1180))
    show drink_table_pub_victor
    show drink_room_fg_pub
    with fade
    "But when I get there, I feel a surge of irritation."
    "As Shawn seems to be just as engrossed as the bartender was."
    bree.say "Shawn..."
    bree.say "Earth to Shawn!"
    show shawn surprised
    shawn.say "Huh..."
    show shawn nice
    shawn.say "Hey, [hero.name]..."
    show shawn complain
    shawn.say "This is some crazy shit - sounds like rabies or something!"
    show shawn upset
    "I wave away Shawn's concerns with one hand."
    "And I push his drink across the table with the other."
    bree.say "No need to worry about that."
    bree.say "I've had all my shots."
    bree.say "And plus it's on the other side of the world."
    bree.say "With like, an ocean between us and all that!"
    show shawn sad
    "Shawn doesn't look totally convinced with my reasoning."
    "But he does the polite thing in nodding and turning away from the TV screen."
    show shawn talkative
    shawn.say "You're probably right, [hero.name]."
    shawn.say "Something about it just bugs me though."
    shawn.say "Like I've heard about this happening before, you know?"
    show shawn upset
    bree.say "Of course you have, Shawn..."
    bree.say "It sounds like every disaster movie I ever watched."
    show shawn smile
    "A light seems to come on behind Shawn's eyes."
    "And he nods, beginning to look relieved."
    show shawn nice
    shawn.say "That's probably it."
    shawn.say "Trust you to hit the nail on the head, [hero.name]!"
    show shawn smile
    "I shrug and smile, holding up my hands."
    bree.say "What can I say?"
    bree.say "I am totally amazing!"
    show shawn happy
    shawn.say "Oh yeah, [hero.name]..."
    shawn.say "You're totally amazing - perfect, even!"
    show shawn nice
    "Shawn says this with such enthusiasm and sincerity."
    "And his eyes are practically sparkling as he says it too."
    "But the moment that he sees me staring at him, all that changes."
    show shawn embarrassed blush
    "Now he seems awkward and embarrassed."
    "Yet he stumbles on regardless."
    "Almost like he's been forced into spilling his guts."
    show shawn talkative
    shawn.say "I...I really mean that, [hero.name]!"
    shawn.say "You're totally amazing..."
    shawn.say "More amazing than any other girl I've met...ever!"
    shawn.say "I'm really scared to do this..."
    shawn.say "But I have to, or else I'll go crazy."
    show shawn smile
    "Shawn pauses to take a deep breath, puffing up his chest."
    "Then he lets it all out as he goes for whatever this is going to be."
    show shawn nice
    shawn.say "[hero.name], will you...will you be my girlfriend?"
    show shawn smile
    menu:
        "Of course I will!":
            "I feel a sudden surge of excitement and exhilaration take hold of me."
            "There was no way I could have predicted what Shawn was going to say."
            "But somehow I'm totally sure of what my response should be."
            "And I probably couldn't stop it bursting out of me if I tried."
            bree.say "Yes..."
            bree.say "Of course I will!"
            show shawn sad
            "Much to my surprise, this doesn't seem to please Shawn."
            "Because he kind of looks down at the table, shaking his head."
            show shawn talkative
            shawn.say "It's..."
            shawn.say "It's okay, [hero.name]..."
            shawn.say "I don't know what I was even thinking asking you that!"
            shawn.say "You and me, they very idea of..."
            "All of a sudden, Shawn stops and looks up at me."
            show shawn surprised
            shawn.say "Wait..."
            shawn.say "Wait a minute, [hero.name]..."
            shawn.say "Did you say yes as in 'yes'?"
            shawn.say "Or yes as in 'no'?"
            show shawn stuned
            "I have no idea how I could possibly do the latter."
            "But I'm willing to chalk that up to Shawn's brain being all over the place."
            "After all, he did just muster up the courage to ask me out!"
            bree.say "The first one, Shawn."
            bree.say "As in 'yes, I will be your girlfriend'!"
            "As the realisation dawns on him, Shawn almost bounces in his seat."
            show shawn surprised
            shawn.say "Really?"
            show shawn happy
            shawn.say "Oh my..."
            shawn.say "Oh my god!"
            shawn.say "I can't believe this is actually happening!"
            show shawn smile
            "I reach across the table and pinch Shawn's arm."
            show shawn vangry
            shawn.say "OUCH!"
            show shawn surprised
            shawn.say "What was that for?!?"
            show shawn smile
            bree.say "Just to show you're not dreaming, Shawn..."
            bree.say "Now you know that all of this is real!"
            "Shawn nods, but he keeps a close eye on me after that."
            "Almost like he suspects that more pinching might be on the cards."
            show shawn happy
            "But soon enough we're talking intently about what lies ahead for the both of us."
            "The doom and gloom being reported on the TV fading into the background."
            $ shawn.love += 10
        "I'm sorry Shawn...":
            "I can already feel the sinking sensation taking hold in my gut."
            "And that must be reflected on my face too."
            "Because Shawn's expression becomes one of genuine dismay."
            show shawn complain
            shawn.say "Oh no, [hero.name]..."
            shawn.say "Not that face!"
            shawn.say "I know what that face means..."
            shawn.say "I've seen it so many times before!"
            show shawn sad
            "Well that's a kick in the teeth!"
            "Shawn's the kind of guy that's been turned down more times than a hotel bed."
            "So of course he knows the look in the face of a girl about to say no!"
            bree.say "Oh, Shawn..."
            bree.say "It's not that you're not a nice guy, okay?"
            bree.say "It's just that..."
            "Shawn shakes his head."
            show shawn sadsmile
            shawn.say "Let me guess..."
            shawn.say "You love me..."
            shawn.say "But it's the kind of love that exists between two best friends?"
            show shawn sad
            "I blink in surprise, as that's exactly the words I was going to use."
            bree.say "Erm..."
            bree.say "Uncanny..."
            bree.say "But basically, yeah."
            show shawn casual sad at center, zoomAt(1.75, (840, 880)) with ease
            "Shawn sighs and gets up from the table."
            show shawn talkative
            shawn.say "I thought as much."
            shawn.say "And that means I should get going."
            show shawn sad
            bree.say "You don't have to do that, Shawn..."
            bree.say "Can't we just stay friends?"
            "Shawn shakes his head."
            show shawn talkative
            shawn.say "No, [hero.name]..."
            shawn.say "I love you way too much for that to work."
            shawn.say "If things stayed the same, I'd end up resenting you."
            hide shawn with easeoutright
            "With that, Shawn turns his back on me and walks out of the pub."
            "And I'm left thinking that I just killed off a friendship."
            "All for the sake of wanting to keep it alive."
            $ shawn.love -= 20
    $ hero.replace_activity()
    return


label shawn_female_event_10:
    if shawn.love.max < 200:
        $ shawn.love.max = 200
    "Shawn's not the kind of guy that finds it easy to hide his intentions at the best of times."
    "And the fact that I'm female seems to make it that much harder for him to pull it off too."
    "I guess it comes from the years of suffering that most male nerds are forced to endure."
    "So that he just starts giving off signals without even realising that he's doing so."
    show shawn embarrassed at center, zoomAt(1.25, (740, 920)) with fade
    "Like right now for example, Shawn's practically twitching every time I look in his direction."
    show shawn normal
    "And it's even worse when I look around and catch him in the act of watching me."
    show shawn stuned at center, zoomAt(1.0, (740, 920)), startle
    "When that happens he almost jumps out of his skin!"
    show shawn embarrassed at center, zoomAt(1.25, (740, 920))
    "So I guess that the best thing would be for me to put an end to his suffering."
    bree.say "Erm..."
    bree.say "Shawn..."
    show shawn smile at center, zoomAt(1.25, (640, 920)) with ease
    "I wait for Shawn to turn his head in my direction again."
    "Noting as he does so the unconvincing look of cool composure on his face."
    show shawn nice
    shawn.say "Yeah, [hero.name]..."
    shawn.say "What's up?"
    show shawn smile
    "I keep smiling in what I hope is a reassuring manner."
    "And I prepare to call Shawn's bluff."
    bree.say "I was about to ask you the same thing."
    bree.say "You're really jittery today, Shawn..."
    bree.say "And you look like you're sweating too!"
    show shawn stuned blush
    "Shawn looks at me like I'm not making any sense."
    "Which of course only makes him look even more suspect."
    "As well as increasing the amount of sweat he's producing."
    show shawn sadsmile
    shawn.say "Okay, Shawn..."
    shawn.say "This is it..."
    shawn.say "This is the moment we've practiced for!"
    show shawn embarrassed
    "For a moment I'm not sure what Shawn's trying to say, or even who he's talking to."
    "Because he's kind of looking past me, like I've become transparent or something."
    "But then I realise that he's trying to psyche himself up, to talk himself into something."
    bree.say "Okay, Shawn..."
    bree.say "There's never going to be a better time than right now."
    bree.say "So whatever you've got, go ahead and hit me with it."
    "I'm standing there, thinking that I'm the one in control."
    "That whatever Shawn has in mind, it's going to be easy for me to handle."
    show shawn talkative at center, traveling(1.75, 0.3, (640, 1240))
    "But then he does something that throws me for a complete loop."
    "Shawn gets down on one knee, right in front of me."
    "And the next thing I know, he has a ring in his hand."
    "An actual ring!"
    show shawn nice at center, zoomAt(1.75, (640, 1480)) with ease
    shawn.say "[hero.name]..."
    shawn.say "Since we've been together..."
    shawn.say "I've been the happiest I can ever remember being."
    shawn.say "And that's a feeling that I don't want to end."
    shawn.say "So I have to ask...will you marry me?"
    show shawn smile
    "Hell, I thought Shawn getting down on one knee was throwing me."
    "But he just more than doubled down on it, didn't he?"
    "I mean, I'm not imagining it, am I?"
    "He just literally asked me to marry him!"
    menu:
        "YES!":

            "I've actually thought about this in the past."
            "About the chances of Shawn and I being something that would last."
            "But as soon as he pops the question, I don't even hesitate."
            bree.say "YES!"
            bree.say "Yes, I will marry you!"
            "I thrust out my hand."
            "And then I wait eagerly for Shawn to put the ring on my finger."
            show shawn embarrassed
            "But instead he just kneels there, looking up at me blankly."
            bree.say "Erm, Shawn..."
            bree.say "You heard me, right?"
            bree.say "You heard that I said 'yes'?"
            "The words seem to hit Shawn like a slap in the face."
            show shawn stuned
            "Because he shakes his head and suddenly looks more awake."
            show shawn surprised
            shawn.say "Oh..."
            shawn.say "Oh yeah..."
            show shawn sadsmile
            shawn.say "I'm sorry, [hero.name], I was preparing myself for the opposite answer."
            shawn.say "I guess I never really thought what I'd do if you said yes!"
            show shawn smile
            bree.say "Well I did!"
            "I present my hand a second time."
            "And on this occasion Shawn slides the ring onto my finger."
            show shawn talkative at center, zoomAt(1.75, (640, 1240)) with ease
            "He stands up, grinning and rubbing the back of his head."
            show shawn nice
            shawn.say "This is all kind of a shock for me, [hero.name]..."
            shawn.say "I'm still trying to get my head around it!"
            show shawn happy
            bree.say "You know it's usually the other way, right?"
            bree.say "The person being asked to marry you is the stunned one."
            bree.say "Like, because you're supposed to know all about it?"
            "All Shawn can do is shrug and smile."
            "So I feel like I should let him off."
            "I mean he already managed to stumble through the proposal."
            "I don't want to break him before we actually get to the altar!"
            $ shawn.set_fiance()
            $ shawn.love += 5
        "I'm not ready for this, Shawn":

            "I know that Shawn's a great guy, and I like him a hell of a lot."
            "But there's no way I want to marry anyone right now."
            "Including him!"
            bree.say "Ah..."
            bree.say "This is kind of awkward, Shawn..."
            bree.say "Because I'm just not ready to take that kind of step."
            "I'm expecting Shawn to be devastated by my turning him down."
            "For him to put the ring away and get up, totally crushed."
            show shawn normal -blush at center, zoomAt(2.25, (640, 1780)) with vpunch
            "But instead he shuffles closer to me, holding it up to my face."
            show shawn complain
            shawn.say "Are you really sure about that, [hero.name]?"
            shawn.say "Because I hear what you're saying..."
            shawn.say "But I also didn't hear you actually use the word 'no'!"
            show shawn sad
            "I can't help taking a step backwards as Shawn shuffles forwards on his knees."
            show shawn at center, zoomAt(3, (640, 2180)) with vpunch
            "But as soon as I do that he comes closer again, until I have nowhere else to go."
            bree.say "Okay, Shawn..."
            bree.say "The only reason you didn't hear me say it was because I was trying to be nice."
            bree.say "But if that's what you need, then so be it..."
            bree.say "No, Shawn, I will not marry you!"
            "By now I'm moving sideways in the hope of getting away."
            "But Shawn's still following me on his knees."
            show shawn complain
            shawn.say "Ah..."
            shawn.say "But that's such a vague answer, isn't it?"
            shawn.say "You don't say if that's just now, or forever."
            shawn.say "Like, maybe we could say you'll marry me at a specific date in the future?"
            show shawn normal
            "Waving my arms over my head, I feel like screaming."
            bree.say "Okay, Shawn..."
            bree.say "You asked for this."
            bree.say "I will not marry you now or at any time in the future, specified or otherwise."
            bree.say "So take that ring and shove it straight up your backside!"
            "I feel a small sense of validation as Shawn finally puts the ring away."
            show shawn sad at center, zoomAt(1.25, (640, 920)) with fade
            "But it melts away as he gets to his feet, his face beginning to fall."
            "Because now he's reacting exactly like I expected him to do in the first place."
            show shawn complain
            shawn.say "Okay, [hero.name], okay..."
            shawn.say "I get the message, loud and clear."
            shawn.say "There's no need to get nasty though!"
            show shawn upset
            "My eyes are almost bulging out of their sockets as Shawn says this."
            "But somehow I manage to keep my own mouth closed and not scream at him."
            hide shawn with dissolve
            "Instead I turn on my heel and just walk away."
            "Hoping that time and space will help me to calm down."
            "At least to the point where I can see him again without rising thoughts of bloody murder."
            $ shawn.love -= 10
    return



label shawn_female_ending:
    scene bg map day at center, blur(3) with dissolve
    play music "<from 2 to 20>music/darren_curtis/into_oblivion.ogg" loop fadein 0.5 fadeout 5.0


    "Hello?"
    "Can you hear me?"
    "Damn it, I hope this thing is working okay."
    show map_apocalypse
    show fx fog at dark
    with dissolve
    "It's the only one I've been able to find in the past six months that would even turn on."
    "And I don't have time to go out into the wasteland and start looking for another one."
    "Not when we're stockpiling and reinforcing the defences in preparation for the winter."
    "That reminds me, I need to get [mike.name] working on repairing those fences and electrifying them."
    "They took a beating the last time Dwayne's warband tried to mount a raid."
    "Wait a minute..."
    "That's not why I'm making the recording."
    "There was something else..."
    "Something I needed to get preserve..."
    "Our story - that's it!"
    "I was supposed to be making a recording of how [hero.name] and I came to be here."
    "A recounting of the events that lead to us being at the forefront of this war."
    if bree.is_visibly_pregnant:
        "I guess I'm doing this more for George's sake than ours."
        "After all, he's one of the kids growing up in this hell."
        "So he deserves to know a little about how the world used to be."
        "But hopefully his mum and dad will still be around when he's older."
        "That way we can help to fill in all the gaps for the little guy."
        "Maybe even try to get things back to something like the way they were before it all went down."
    else:
        "I guess I'm doing this more for other people's sake than ours."
        "After all, there's an entire generation kids growing up in this hell."
        "So they deserve to know a little about how the world used to be."
        "But hopefully we'll still be around when they grow up, us and other survivors from our generation."
        "That way we can help to fill in all the gaps for them, bring them right up to speed."
        "Maybe even try to get things back to something like the way they were before it all went down."
    "But yeah...[hero.name] and me...our story."
    "You have to understand that when the world you know ends, everything changes."
    "One moment you're fretting about your job, the bills and your streaming subscriptions."
    "Maybe even planning a wedding with the girl of your dreams."
    "And the next you realise that you should have been paying more attention to the news."
    "So you remember when [hero.name] and I were in The Winchester?"
    "The time there was a story on the TV about a medical emergency in Africa?"
    "Well it only went and turned out to be the start of it all."
    scene bg black
    show shawn ending zombies at center, dark
    with dissolve
    stop sound fadeout 1


    "A one hundred percent genuine zombie apocalypse."
    "Before [hero.name] and I could even pick out the flowers for the wedding it was over here."
    "People were dropping dead and then coming back as bloody zombies."
    "And of course, they had to be the kind that really want to eat you too."
    play sound knife
    scene bg black with fade
    queue sound knife_stab
    show fx fog at blood with hpunch
    "I barely made it out of my own flat, having to decapitate Palla along the way."
    "Then I was forced to fight my way across town to reach [hero.name]'s place."
    "I picked up Amy on my travels, and together we stormed right in there."
    scene bg black
    show shawn ending bg
    show shawn_ending_zombie2 at swing(1.0, 0.8, 1.0, -0.7, 0.6), center, zoomAt(1.05, (640, 1130))
    show shawn_ending_zombie3 at swing(1.0, 0.8, 1.0, -0.8, 0.4), center, zoomAt(1.05, (640, 1130))
    with dissolve
    "We only just managed to save [hero.name], [mike.name] and his chubby mate Jack from being eaten by a zombified Sasha."
    "But then we needed a place to hold up, and so I came up with the perfect plan."
    "If we could only make it to The Winchester and hole up there."
    "We'd have the perfect place for a night out and a zombie safehouse under one roof!"
    "And once I got everyone on board, everything went according to plan."
    "Well, if you don't count all the times we nearly got eaten."
    "Oh, and the fact that Jack was bitten and turned into a zombie too!"
    "But after that, it was perfect and we all settled in to let it all wash over."
    "[mike.name] even managed to chain zombie Jack up in the cellar."
    "And it turns out he even remembered how to play on the Z-Box!"
    "All we had to do was wait for the authorities to restore law and order."
    "Or at least that's what I hoped would happen."
    "Turns out nobody in charge was really up to the job."
    "That means the ever increasing hordes of the undead just swept over everything."
    "And if we wanted to stay alive, rather than join them in undeath, there was only one option."
    "We were going to have to knuckle down and do it all ourselves."
    "So that's exactly what we did, [hero.name] and I taking the lead."
    "We fortified The Winchester, turning it into a home and fortress."
    "We trained our bodies and brains, learning all that we could."
    "Then we started to mount expeditions into the wasteland that used to be our city."
    play music "music/TeknoAXE/simple_metal.ogg" loop
    scene bg black
    show shawn ending bg bodies
    show shawn_ending_zombie2 at swing(1.0, 0.8, 1.0, -0.7, 0.6), center, zoomAt(1.05, (640, 1130))
    show shawn_ending_zombie3 at swing(1.0, 0.8, 1.0, -0.8, 0.4), center, zoomAt(1.05, (640, 1130))
    with vpunch
    pause 0.5
    play sound shotgun1
    show shawn ending bodies fire with hpunch
    pause 0.2
    show shawn ending bodies -fire
    pause 0.2
    play sound shotgun_reload
    pause 0.5
    play sound shotgun1
    show shawn ending bodies fire with hpunch
    pause 0.2
    show shawn ending bodies -fire
    pause 0.2
    play sound shotgun_reload
    show shawn_ending_zombie1 at swing(1.0, 0.8, 1.0, -0.7, 0.6), center, zoomAt(1.5, (240, 1330))
    show shawn_ending_zombie1 at swing(1.0, 0.8, 1.0, -0.7, 0.6), center, traveling(1.05, 10.0, (640, 1130))
    show shawn_ending_zombie4 at swing(1.0, 0.8, 1.0, -0.7, 0.6), center, zoomAt(1.5, (1040, 1330))
    show shawn_ending_zombie4 at swing(1.0, 0.8, 1.0, -0.8, 0.5), center, traveling(1.05, 15.0, (640, 1130))
    "It was hard, and it still is, every day bringing new challenges."
    "But the fact that we're all alive and still fighting means we're winning."
    "Hell, we're even getting used to occasionally zombified family and friends."
    play sound shotgun1
    show shawn ending bodies fire with hpunch
    pause 0.2
    show shawn ending bodies -fire
    pause 0.2
    play sound shotgun_reload
    "Then blowing them away with a precise shot to the head!"
    "And sure, this isn't the life that [hero.name] and I had planned."
    "But you know what, I sometimes think that we're happier this way."
    play sound shotgun1
    show shawn ending bodies fire with hpunch
    pause 0.2
    show shawn ending bodies -fire
    pause 0.2
    play sound shotgun_reload
    "I mean, did we really have that much to look forward to the way things were?"
    "We'd have gone to work, nine to five every day."
    "Then come home and just binged TV series on stream."
    play sound shotgun1
    show shawn ending bodies fire with hpunch
    pause 0.2
    show shawn ending bodies -fire
    pause 0.2
    play sound shotgun_reload
    "In this world, with a zombie apocalypse on the go, we're truly alive."
    "We have to be fit, fast and the best we can be just to make it through the day."
    "And when we do that, and live to see another dawn, we feel truly alive!"
    "So on balance, I probably wouldn't change a thing."
    "Because I have my girl by my side, we're fighting and we're winning too!"
    scene bg black with dissolve
    stop sound fadeout 0.5
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()
    return


label shawn_female_sub_01:
    if shawn.sub.max < 60:
        $ shawn.sub.max = 60
    scene bg street
    show shawn date smile noglasses
    "I'm really looking forward to getting to eat at a restaurant with Shawn tonight."
    "Work and studying for college have been kind of crazy these past few weeks."
    "And so I feel like I deserve a chance to just relax and enjoy myself a little."
    "Plus it's easy to change gear when you're on a date with a guy like Shawn."
    "You'd know exactly what I mean if you were in my shoes as he turns up at the restaurant."
    show shawn nice
    shawn.say "You know look amazing [hero.name]!"
    shawn.say "Is that a new dress?"
    show shawn happy
    shawn.say "And did you do something different with your hair?"
    show shawn smile
    "I can't help blushing and letting out a giggle of delight as Shawn gushes over me."
    "Because no matter how modern and liberated I try to be, I still love a little flattery."
    bree.say "Oh, Shawn..."
    bree.say "Stop it!"
    bree.say "Actually...don't stop it!"
    bree.say "I'm kind of enjoying all the compliments."
    show shawn smile
    "Shawn's nodding eagerly as he leads me into the restaurant."
    scene bg restaurant with fade
    pause 0.3
    show shawn date smile noglasses at center, zoomAt(1.25, (940, 900)) with easeinright
    "And I guess this is just one of the perks that comes along with dating a geekier kind of guy."
    "Like, I'm not falling into that old cliché."
    "You know, the idea that they're always grateful for any kind of attention?"
    "But there is something to be said for the way that they're a lot more humble."
    "I guess when you don't have women falling over themselves to be with you, it makes you try harder."
    show shawn date smile at center, zoomAt(1.25, (640, 900)) with ease
    "As we make it to the table, Shawn hurries to get behind me."
    "I have no idea what he's doing."
    "But my guess is that he wants the seat nearest to me."
    bree.say "Erm..."
    bree.say "It's okay, Shawn..."
    bree.say "We can swap seats if you like?"
    show shawn normal
    "But when I turn around, I see that I've totally misread the situation."
    "Because Shawn's standing there with the chair in his hands."
    "And he's obviously trying to pull it out so that I can sit down."
    menu:
        "Let Shawn pull out your chair":
            bree.say "Oh..."
            bree.say "Sorry, Shawn!"
            show shawn smile
            "I oblige Shawn by sitting on the chair."
            "And the I let him shuffle me up to the table."
            "Because if he wants to be a gentleman tonight, that's fine."
            "I have no problem letting him spoil me just a little."
            $ shawn.love += 1
            $ game.active_date.score += 10
        "Tell him you can pull your chair on your own":
            bree.say "It's okay, Shawn..."
            bree.say "I can manage on my own."
            show shawn sad
            "Shawn looks a little put out at first."
            show shawn sadsmile
            "But then he puts a smile on his face."
            "And the matter seems to be forgotten."
            "So I take care of sitting myself down at the table."
            $ shawn.sub += 1
    hide shawn
    show restaurant meal shawn date nomeals
    with fade
    "Shawn hands me a menu and opens his own."
    "Then he scans up and down the list of dishes."
    shawn.say "So, [hero.name]..."
    shawn.say "What do you like the look of?"
    shawn.say "I gotta say, I'm in the mood for a steak!"
    "I shrug as I begin to take a look at what's on offer."
    bree.say "Oh, I really don't know what I feel like tonight, Shawn."
    bree.say "But I kind of feel like steak would be a little too heavy!"
    "Shawn responds to this without missing a beat."
    shawn.say "You're totally right, [hero.name]..."
    shawn.say "Who wants a ton of meat sitting in their guts?"
    shawn.say "I should totally order fish instead!"
    "I can't help looking up from my menu and frowning."
    bree.say "What's up with that, Shawn?"
    show restaurant meal shawn date happy
    "Shawn gives me a confused smile."
    "Looking like he has no idea what I'm talking about."
    show restaurant meal shawn date -happy
    shawn.say "What do you mean?"
    shawn.say "I just said fish sounds good, that's all."
    bree.say "No, Shawn..."
    bree.say "You said you wanted steak."
    bree.say "Then two seconds later you flipped to fish!"
    show restaurant meal shawn date bored
    "Shawn still doesn't seem to understand what I'm getting at."
    "Because he just shrugs and shakes his head."
    show restaurant meal shawn date -bored
    shawn.say "So I changed my mind?"
    shawn.say "So what?"
    "I guess that he does have the right to change his mind."
    "So I just decide to leave it and move on."
    show restaurant meal shawn date waiter
    "A moment later the waiter arrives to take our orders."
    "But I see that he's carrying a bottle of wine."
    bree.say "Oh..."
    bree.say "I don't think that's ours."
    bree.say "They didn't take our drinks order yet."
    shawn.say "Oh no, I called ahead, [hero.name]..."
    show restaurant meal shawn date happy
    shawn.say "I wanted to make sure they had a bottle of this warmed and ready for us."
    show restaurant meal shawn date -happy
    shawn.say "Apparently it's one of the best red wines that you can get!"
    "I can't help grimacing at this."
    "Something that Shawn spots instantly."
    shawn.say "What's the matter, [hero.name]?"
    shawn.say "I thought this would be a nice surprise."
    bree.say "It would if we'd chosen to go with the steak."
    bree.say "But if we're having fish, we need white wine!"
    "As soon as he hears me say this, Shawn leaps out of his seat."
    "And I see him intercept the waiter before he even makes it to the table."
    "I watch as Shawn starts to speak to the guy, gesticulating pretty wildly."
    "Then the waiter nods and turns around before walking away again."
    "When Shawn makes it back to the table, I'm more than a little curious."
    bree.say "So..."
    bree.say "What was all that about?"
    shawn.say "No issue, [hero.name]..."
    shawn.say "I just made him take it back and get some white wine instead."
    menu:
        "Thanks for that!":
            "I shrug and decide to let it go."
            bree.say "Red for meat, white for fish."
            bree.say "Makes perfect sense."
            show restaurant meal shawn date happy
            "Shawn gives me a nod and a smile in response."
            shawn.say "Exactly, [hero.name]..."
            shawn.say "It pays to be adaptable!"
            show restaurant meal shawn date -happy
            $ shawn.love += 1
            $ game.active_date.score += 10
        "You didn't have to...":
            bree.say "Shawn..."
            bree.say "Is it just me..."
            bree.say "Or are you trying too hard tonight?"
            show restaurant meal shawn date bored
            "Shawn looks at me with a puzzled expression on his face."
            "Like he really doesn't know what I'm talking about."
            show restaurant meal shawn date -bored
            shawn.say "What do you mean by that?"
            shawn.say "I ordered red when I thought we were having steak."
            shawn.say "We changed that to fish, so I changed it to white."
            "I decide to just let it go."
            "So I give Shawn a nod of my own."
            "And then I drop the whole matter."
            $ shawn.love -= 2
    show restaurant meal shawn date -nomeals -waiter with fade
    "Once we have our food, I feel like we're really getting into the swing of things."
    "The fish is great and the wine goes so well with it that I find myself drinking quite a lot."
    "In fact it doesn't take me long to feel more than a little tipsy."
    bree.say "Oh, Shawn..."
    bree.say "Don't let me have any more wine..."
    bree.say "I think it's starting to go to my head!"
    shawn.say "Okay, [hero.name]..."
    "Shawn picks up the wine bottle and starts looking around."
    bree.say "What are you doing?"
    shawn.say "Just looking for someone to take the wine, [hero.name]..."
    shawn.say "Like you asked?"
    "I scrunch my mouth up as I stare at Shawn."
    "Because something is starting to occur to me."
    bree.say "Shawn..."
    bree.say "Put the bottle down."
    "Without saying a word, Shawn does as I tell him."
    bree.say "Now pick it up again."
    "Once more Shawn does exactly as he's told."
    bree.say "Now recite the alphabet backwards!"
    shawn.say "You want me to do what?!?"
    bree.say "Recite the alphabet backwards, right now!"
    "For a moment I think that Shawn's going to laugh in my face."
    "But then he just nods and starts doing as he's told."
    shawn.say "Okay, okay..."
    shawn.say "Z...Y...X..."
    bree.say "It's okay, Shawn..."
    bree.say "You can stop that now."
    "Shawn nods and does as I tell him."
    "And the look on his face shows me that he's still eager to please."
    shawn.say "Just let me know if you want me to do it again, yeah?"
    "I nod in response."
    "But the truth is that I'm not really paying attention."
    "Instead I'm turning all of this over in my head."
    "And I'm also fast coming to the conclusion that Shawn can't say no to me."
    "I mean, I know that most guys like him are eager to please a girl."
    "But he's leaping to obey my every word, like he can't help himself."
    "Maybe this is the tell-tale signs of something deeper in Shawn."
    "Maybe it's not just that he's eager to please."
    "Could it be that he's actually submissive by nature?"
    "Hmm...that could have some real perks for me as his girlfriend."
    "Of course I'd never take advantage of Shawn's nature, or exploit him."
    "But it could be a whole lot of fun having a truly submissive boyfriend."
    "As the meal goes on, I find myself liking the idea more and more."
    "And if this really is something that's a natural part of Shawn's character, then it's not like I'm taking advantage of him."
    "In fact, it'd be far more like me accepting the real Shawn and encouraging him to embrace it too."
    "That's it - this is a chance to emancipate Shawn from the shackles of his free-will."
    "To put him in the place where he was always intended to be."
    "Plus I'm going to get to have some real good times along the way!"
    $ shawn.sub += 2
    $ hero.replace_activity()
    return


label shawn_female_sub_02:
    show shawn smile at center, zoomAt(1.15, (640, 830))
    "After coming to the revelation that Shawn's probably a natural sub, I can't stop thinking about the whole thing."
    "The way that he pretty much did whatever I asked him to at the restaurant the last time, no matter how unreasonable it might have been."
    "It makes me begin to rethink the relationship that we've been building together since we decided to begin dating."
    "Back then I just thought that Shawn was a typical geeky guy, always eager to please the woman in his life."
    "But now that I know he's submissive, I really feel like I should be taking that into account."
    "And it's going to mean redefining some of the fundamental elements of our relationship."
    "Plus it'd be better to make the necessary changes now, rather than later when it would be much harder to do."
    "Perhaps the best place to start is the way that Shawn addresses me, because that's kind of a fundamental thing."
    "So as soon as the chance presents itself, I raise the subject with him."
    bree.say "Shawn..."
    bree.say "We need to talk."
    show shawn stuned at center, zoomAt(1.25, (640, 920))
    show fx exclamation
    with hpunch
    "The second the words are out of my mouth, I know I've screwed up."
    "Shawn's head snaps around at speeds that should have sent his neck into spasms."
    "And his eyes are as big as saucers, filled with panic."
    show shawn surprised
    shawn.say "Oh no..."
    shawn.say "What is it?"
    shawn.say "What did I do wrong this time?!?"
    show shawn stuned
    "I hold up a hand, trying to calm Shawn down."
    bree.say "It's okay, Shawn..."
    bree.say "I didn't mean that kind of talk!"
    show shawn surprised
    shawn.say "I swear that I'll be a better boyfriend, [hero.name]!"
    shawn.say "Just don't dump me, please?!?"
    show shawn stuned
    "I feel the need to raise my voice and regain control of the situation."
    with vpunch
    bree.say "SHAWN!"
    bree.say "I am not going to dump you, okay?"
    show shawn smile
    "Shawn instantly goes from blind panic to total relief."
    "Which only helps to convince me of his truly submissive nature."
    show shawn sadsmile
    shawn.say "Oh thank you, [hero.name]..."
    shawn.say "Thank you!"
    show shawn smile
    bree.say "You see this is what I want to discuss, Shawn."
    bree.say "I feel like there's a natural power dynamic in our relationship."
    bree.say "One where I'm on top and you're underneath, you know?"
    show shawn smug
    "Shawn's mouth twists into a nervous smile as he hears me out."
    show shawn nice
    shawn.say "But, [hero.name]..."
    shawn.say "You make it sound like I'm kind of weak..."
    shawn.say "You know, easily dominated?"
    show shawn smile
    bree.say "Urgh..."
    bree.say "But you are, Shawn!"
    show shawn surprised blush
    shawn.say "Oh..."
    shawn.say "Of course I am, [hero.name]!"
    shawn.say "If you say so!"
    show shawn embarrassed
    bree.say "Okay, Shawn..."
    bree.say "Let's take this one step at a time."
    bree.say "It might help if you started calling me something more suitable."
    bree.say "Like...how about...'Miss [hero.family_name]'?"
    if shawn.sub >= 50:
        "Shawn looks at me like a dog that's been given a direct command."
        "And then he nods, letting me know that he plans to obey."
        show shawn happy
        shawn.say "I can do that, [hero.name]..."
        show shawn complain
        shawn.say "Oops!"
        show shawn nice
        shawn.say "I mean, Miss [hero.family_name]!"
        show shawn smile
        "I feel a surge of triumph as Shawn bends himself to my will."
        "Not just because he's doing as I say here and now."
        "But also because it means that I can probably get him to do much more."
        "And the possibilities are already beginning to suggest themselves to me."
        $ shawn.flags.breeNickname = "family_name"
        if shawn.sub.max < 80:
            $ shawn.sub.max = 80
    else:
        show shawn stuned
        "Shawn looks at me in amazement."
        show shawn happy -blush at startle
        "And then he bursts out laughing."
        show shawn nice
        shawn.say "Oh, [hero.name]..."
        shawn.say "That's so fucking funny!"
        shawn.say "But you have to be kidding, right?"
        shawn.say "I can't call you that with a straight face!"
        show shawn smile
        "I can already feel my cheeks beginning to burn with embarrassment."
        "And so I decide to let the whole thing drop to save face."
        "Maybe I can try again when Shawn's had a chance to let all of this sink in?"
    return


label shawn_female_sub_03:
    if shawn.sub.max < 100:
        $ shawn.sub.max = 100
    scene bg bedroom4 with fade
    shawn.say "Erm..."
    shawn.say "[hero.name]?"
    shawn.say "Are you in there?"
    shawn.say "I came over as fast as I could..."
    shawn.say "I really want to see this surprise you have for me!"
    "I'm actually holding my breath as Shawn opens the door to my bedroom."
    "And as he says all of this, I can feel my heart pounding in my chest too."
    "I called him up and asked him to come over, which is pretty standard stuff."
    "But asking him to come straight up to my bedroom..."
    "Well that is a little different."
    bree.say "Oh yeah, Shawn..."
    bree.say "I'm right here waiting for you."
    bree.say "So get your ass in here!"
    "I keep the tone of my voice playful and yet authoritative too."
    "Just the right combination to lure him inside my bedroom."
    "And at the same time let him know that it's not a matter of choice."
    "It works too, as the door opens further still and Shawn peeks around it."
    "I've chosen to stand in a spot where he won't be able to see me until he's all the way inside."
    show shawn normal at center, zoomAt(1, (840, 720)) with easeinright
    "This means that he soon has to walk almost into the centre of the room, still looking for me."
    show shawn at center, zoomAt(1, (640, 720)) with ease
    "As soon as the door swings closed behind him, I leap into action."
    "Pushing it all the way shut, I step out from behind it."
    bree.say "There you are, Shawn..."
    bree.say "You silly little man!"
    "It's not like I'm bellowing the words or being crazily aggressive as I say all of this."
    "And maybe it's the fact that I've taken Shawn by surprise that makes him almost leap out of his skin."
    "But then the outfit that I have on right now might have something to do with it too."
    show shawn surprised
    shawn.say "Aaargh!"
    shawn.say "[hero.name[0]]...[hero.name]..."
    shawn.say "Is that really you?!?"
    show shawn stuned
    "I guess I should explain that some things have happened since I discovered Shawn was a sub."
    hide shawn
    show breemc z dominatrix with dissolve
    "And one of those things is that I went on a shopping spree and bought myself a few things."
    "Foremost amongst them was the outfit that I'm wearing right now."
    "I don't think I've ever worn something that showed off so much of my body that wasn't underwear before."
    "Or that featured quite as much rubber, leather, studs and squeaked with every move I make."
    hide breemc
    show shawn stuned at center, zoomAt(1.25, (640, 880))
    "But it does seem to have been money well spent, as Shawn is gaping at me in amazement."
    show shawn surprised
    shawn.say "[hero.name]..."
    shawn.say "You look..."
    shawn.say "I mean..."
    show shawn stuned at center, traveling(1.5, 1.0, (640, 1040))
    "He's reaching out to touch me as he tries to get his words out."
    "And without thinking, I pull out the riding crop I bought too."
    "Then I use it to strike out at Shawn's approaching hand."
    "I don't put much force into the blow, but the effect is pretty dramatic."
    show shawn surprised
    "As Shawn yelps in pain and cowers away from me."
    play sound spank
    with hpunch
    pause 0.1
    show shawn vangry
    shawn.say "OUCH!"
    show shawn complain
    shawn.say "[hero.name]..."
    shawn.say "That really hurt!"
    show shawn stuned
    bree.say "Silence, worm!"
    bree.say "From now on, you speak only when I give you permission."
    bree.say "Understood?"
    "Wow...I must really be getting into this whole dominatrix thing."
    "Because the words just come flowing out of me without any effort."
    "And Shawn is soon nodding his head and keeping his mouth shut."
    bree.say "Now take off your clothes..."
    bree.say "And do it quickly!"
    "All it takes is another wave of the crop, and Shawn's hurrying to obey."
    play sound spank
    with hpunch
    "I watch with growing satisfaction as he tears off his clothes and tosses them aside."
    show shawn naked
    show insert shawn whip at center, zoomAt(1.0, (640, 620))
    with hpunch
    "Once he's naked, I stride around him, looking his exposed body up and down."
    bree.say "Hmm..."
    bree.say "Now this is more like it."
    bree.say "This is what I like to see!"
    "I do the best I can not to make eye-contact with Shawn as all of this is going on."
    "Because I'm worried that if I do, it'll break the spell and things will go back to normal."
    "But what I can catch in passing glances seems to tell me that it's all going to plan."
    "Shawn's eyes are as big as saucers, but he's also looking totally focussed on doing as I say."
    "And the fact that he hasn't once disobeyed me or tried to stand up for himself means it's working."
    "I'm sure that he's beginning to get the gist of it too, and that he's starting to enjoy himself."
    "Not least because I can see his cock starting to inflate and stand to attention!"
    bree.say "But I still think you need to be taught a lesson, Shawn..."
    bree.say "I need to make a show out of you and teach you your proper place!"
    "I tap the tip of his cock with the crop, just a tiny flick."
    show shawn blush at startle
    "But it's enough to make Shawn jump backwards."
    "Then I follow it up with another to one of his buttocks."
    "This sends him right back in the opposite direction."
    "And while he's still disoriented, I begin ordering him around."
    bree.say "Get to the bed - right now!"
    "Shawn turns to obey."
    "But I cut him off before he can move an inch."
    bree.say "Did I say walk?"
    bree.say "Men walk, worms crawl..."
    bree.say "And since I already told you that you're a worm..."
    bree.say "You get on your hands and knees!"
    show shawn at center, zoomAt(1.5, (640, 1240)) with ease
    "Shawn instantly drops onto his hands and knees."
    show shawn at center, zoomAt(1.5, (340, 1240)) with ease
    "Then he starts crawling towards the bed as fast as he can go."
    "I follow him the whole way, offering small taps of encouragement."
    "And soon enough he's up and onto the bed, eyes wide with excitement."
    bree.say "Now..."
    bree.say "What are you?"
    show shawn surprised
    shawn.say "Huh?"
    shawn.say "What?!?"
    show shawn stuned
    "Shawn looks puzzled at this."
    "I don't know if he's genuinely confused at the command."
    "Or if this is a last show of unconscious defiance on his part."
    "But either way, there's only one possible response I can give."
    play sound whip
    show shawn stuned
    show insert shawn whip a
    with hpunch
    "The sound of the crop striking his butt is like the cracking of a whip."
    "And Shawn's entire body quivers as he absorbs the first serious blow."
    show shawn surprised
    with hpunch
    shawn.say "Aaargh!"
    show shawn stuned
    bree.say "You're a worm!"
    bree.say "What are you?!?"
    show shawn embarrassed
    shawn.say "A WORM!"
    shawn.say "I'm a worm, [hero.name]!"
    show shawn stuned
    show insert shawn whip b
    play sound whip
    with hpunch
    "I land the second blow almost without a conscious thought."
    "And it's every bit as hard as the first."
    show shawn surprised
    shawn.say "Oooh..."
    shawn.say "Oh lordy..."
    show shawn stuned
    bree.say "Who am I, worm?"
    bree.say "What title are you to use when addressing me?"
    "I have the crop lined up for a third blow."
    "But Shawn blurts out an answer before it lands."
    show shawn complain
    shawn.say "MISS [hero.family_name!u]!"
    shawn.say "You're Miss [hero.family_name]!"
    show shawn stuned
    show insert shawn whip c
    play sound spank
    with hpunch
    "Of course this doesn't spare Shawn a third blow."
    "But it does mean that this one lands with less force."
    shawn.say "Mmm..."
    bree.say "That's good, worm..."
    bree.say "You're starting to learn your place."
    bree.say "But you still need to be disciplined."
    "With that, I begin to spank Shawn for real."
    play sound whip
    show shawn complain
    with hpunch
    pause 1
    play sound whip
    with hpunch
    pause 1
    play sound whip
    with hpunch
    "I only use the crop to begin with, seeing how it leaves his butt covered in red stripes."
    play sound spank
    with hpunch
    pause 1
    play sound spank
    with hpunch
    "Pretty soon I switch over to using my hand, enjoying the sensation of his butt quivering."
    play sound spank
    with hpunch
    "And the sounds coming out of him begin to change too, going from cries to moans."
    show shawn stuned
    "I keep checking on Shawn's manhood too, making sure it stays hard."
    "Because the truth is that I keep thinking about it more and more as I spank him."
    "My pussy is starting to feel hot, and that means I'm starting to want him badly."
    "But its when I see the first drop of precum glistening on the tip that I know it for sure."
    "Though there's no way I can just come out and ask Shawn to fuck me senseless."
    "That would shatter the whole dynamic we've built up here, as well as killing the mood."
    "So instead I give him a good, hard shove on the shoulder."
    "This is enough to send Shawn tumbling over on the bed."
    "And as soon as he lands on his back, I step up and straddle him."
    scene shawn cowgirl
    show shawn cowgirl opened dominatrix
    with fade
    bree.say "Now that you've been disciplined, it's time for a reward."
    "I reach down and grab hold of Shawn's cock, squeezing it hard."
    bree.say "By which I mean you get to reward me for the effort of disciplining you!"
    "Shawn looks up at me, his eyes wide."
    "But I note that he's nodding his head too."
    shawn.say "Urgh..."
    shawn.say "Yeah..."
    shawn.say "Ouch!"
    "I tug on his cock harder than before."
    "And then I look him in the eye."
    bree.say "I didn't give you permission to speak, worm..."
    bree.say "So you button your lip!"
    "To add weight to my chastising Shawn, I sit down on him with all my weight."
    "And while he puffs and pants, I shove the head of his cock hard against my pussy."
    show shawn cowgirl vaginal
    "It's all that I can do to keep a straight, serious face as I do so."
    "And I can feel my teeth biting down on my lip, harder and harder."
    "Because I've been so focussed on dominating Shawn that I lost track of myself."
    "I knew that I wanted him inside of me, that I was desperate for the release of it."
    "But the whole time I've been building up Shawn's desire, I was doing the same to me too!"
    "It's all I can do to keep from whimpering pathetically as the lips of my pussy begin to part."
    "I have one hand on Shawn's shoulder, and I'm using the other to guide him into me."
    "Him holding me would be a great help right now, but his arms are down by his sides."
    "And I guess that I've kind of intimidated him into keeping them there."
    "So I only have myself to blame for that one!"
    "All of which means I have to be careful to keep my balance as I slide down and onto him."
    "More than once I almost tip over and fall as he's filling me up."
    show shawn cowgirl vaginal at stepback(0.1, 10, 5)
    "The sensation of my pussy taking him in is literally that intense."
    "My eyes are closed and I'm holding my breath until I know that he can't go any deeper."
    "Then I make a point of gathering myself, rallying my strength and resolve."
    "Because I have to keep up my act and remain dominant even now."
    "Or else all of my previous efforts will be for nothing."
    show shawn cowgirl at stepback(0.1, 10, 5)
    "Opening my eyes and letting out a breath, I begin to move up and down."
    "Before now I thought the hardest thing would be dominating Shawn."
    "But compared to keeping my cool now, that was a piece of cake!"
    show shawn cowgirl closed
    "I do the best I can to keep my face a superior mask of authority."
    "While inside I feel like I'm melting and turning into goo."
    "My instinct is to tear off the outfit that I'm wearing."
    show shawn cowgirl at stepback(0.1, 10, 5)
    pause 0.2
    show shawn cowgirl at stepback(0.1, 10, 5)
    "That and to ride Shawn as if my life depended on it."
    "But somehow I manage to keep myself under a degree of control."
    show shawn cowgirl at stepback(0.1, 10, 5)
    pause 0.2
    show shawn cowgirl at stepback(0.1, 10, 5)
    "I push myself down onto Shawn's cock, then bounce back up again."
    "And every time I do so it feels like a tiny battle in a much larger war."
    show shawn cowgirl at stepback(0.05, 10, 5)
    pause 0.2
    show shawn cowgirl at stepback(0.05, 10, 5)
    "I come close to losing control each time, only holding on by a hair's breadth."
    "I'm praying that Shawn cums first, so I can follow close on his heels."
    "Because if I go before he does, I know that'll be the end of my control."
    "And it'll look like he was the one in control after all."
    show shawn cowgirl at stepback(0.05, 10, 5)
    pause 0.2
    show shawn cowgirl at stepback(0.05, 10, 5)
    "It's with that in mind I gaze down at Shawn."
    "And I soon realise that he's red in the face."
    "Almost like he's holding something back."
    show shawn cowgirl at stepback(0.05, 10, 5)
    pause 0.2
    show shawn cowgirl at stepback(0.05, 10, 5)
    "For a moment I'm totally stumped, unable to figure out what's wrong with him."
    "But then, out of the blue, I make the connection."
    bree.say "Oh for fuck's sake..."
    bree.say "Cum, you worm..."
    bree.say "I give you my permission to cum!"
    show shawn cowgirl pleasure with hpunch
    shawn.say "URGH!"
    with hpunch
    "Shawn does as he's told a second later, exploding inside of me like a grenade."
    show shawn cowgirl ahegao with hpunch
    "Now I'm really battling to keep myself from doing the same thing."
    "My body remains still even as my mind descends into total chaos."
    "And all that there is to let on I'm coming is the occasional twitch and spasm."
    "I somehow manage to hold on until the very end, feeling like I'm losing my mind."
    "But when my orgasm is finally over, I prepare to resume my dominating persona."
    $ shawn.sexperience += 1
    $ shawn.sub += 2
    scene bg bedroom4 with fade
    "And that's when I hear the sound of Shawn's snoring, like someone sawing wood."
    "I feel the sudden urge to slap him awake again, like he's insulting me."
    "Then I remember how hard I've been pushing him tonight."
    "That and the fact he's asleep means that I can finally drop the dominatrix act."
    "So instead I slide off of Shawn and take off the squeaky outfit."
    "It feels like being liberated from prison or released from bondage."
    if game.hour > 19 or game.hour < 6:
        "And without it, I begin to realise just how tired I actually am."
        "So I slump back down on the bed, snuggling up to Shawn."
        "And it's not long before I'm falling asleep myself."
        call sleep ("shawn") from _call_sleep_33
    return

label shawn_female_yandere_01:
    "I like to think that I'm a pretty tolerant person, that I can get on with most people."
    "But if there's one thing that I cannot tolerate, it's watching someone I like get exploited."
    "Which is why I haven't been able to get the image of Shawn and Palla out of my mind."
    "Ever since I ran into the pair of them at The Winchester, I keep revisiting the whole thing in my head."
    "At first I thought that I was just being jealous."
    "Envying the way that Shawn was hanging on her every word."
    "But then I remember the way that she talked to be behind his back."
    "Pretty much admitting that she thought he was a sucker and there for the taking."
    "And it seems as though Shawn's not going to do a damn thing about it either."
    "So I guess that means someone else is going to have to step up and take responsibility."
    "All it takes is the chance for me to get hold of Shawn's phone while he's in the bathroom."
    "I already figured out the pin number by watching him unlock it, so getting into it isn't a problem."
    "What's more of a challenge is resisting the temptation to read the texts he and Palla have been exchanging."
    "But somehow I manage to fend off the temptation and find her number instead."
    "That's what I really need in order to get my plan off the ground."
    "Armed with Palla's number, a wait a while, just to make sure neither of them suspects anything."
    "And then I call her up."
    show screen expression "smartphone_calling" pass ("Palla")
    show breemc b normal at center, zoomAt (3.5, (840, 2040))
    with fade
    palla.say "Hello?"
    palla.say "Who is this?"
    "Palla's voice is cold and demanding, just like I remember her being in the pub."
    "But I guess that she is getting a call from a totally unknown number."
    "So I try to keep that in mind as I answer her questions."
    bree.say "Oh..."
    bree.say "Hi, Palla..."
    bree.say "It's [hero.name] here, yeah?"
    "There's a short pause on the other end of the line, like Palla's trying to place the name."
    "And all I can do is wait for her to reply, hoping the time she's taking is a good sign."
    palla.say "Hmm..."
    palla.say "[hero.name]..."
    palla.say "Now where do I know that name from?"
    "I take that as my chance to leap in and reintroduce myself."
    show breemc talkative
    bree.say "I'm one of Shawn's friends..."
    bree.say "We met in The Winchester a couple of days ago."
    bree.say "You remember me, right?"
    palla.say "Oh yes - that [hero.name]!"
    "Palla's tone changes from one of cold suspicion to neutral acceptance."
    "I can't say that she sounds friendly, just that she's no longer openly hostile."
    palla.say "To what do I owe the honour?"
    palla.say "And more importantly - how did you get my number?"
    "Okay, [hero.name]...time to make with the lies!"
    show breemc hesitating
    bree.say "Oh..."
    bree.say "I asked Shawn if I could have your number."
    bree.say "Because I wanted to ask..."
    show breemc normal
    bree.say "Are you like, a designer or a fashion journalist?"
    bree.say "It's just that you were SO well dressed when we met."
    bree.say "What you had on, it was in the hottest magazines like, the next month!"
    "I know full well that Palla's a total clothes horse."
    "Because Shawn happily spilled his guts about her habits and obsessions when I asked him."
    "And I'm banking on her being vain enough to respond to all of my flattery."
    palla.say "Oh no, I'm not one of those people."
    palla.say "I'm just naturally ahead of the curve, a genuine trend-setter!"
    palla.say "And I'm assuming that you want to pick my brains on the subject?"
    "I have to bite my tongue as Palla totally takes the bait."
    "Got to keep on stroking her obviously massive ego while I reel her in."
    show breemc hesitating
    bree.say "I'd love to, Palla..."
    bree.say "If you could spare the time?"
    palla.say "Of course, [hero.name], of course..."
    palla.say "We can meet at the pub where you saw me with Shawn."
    palla.say "Just don't be late!"
    hide screen smartphone_calling
    hide breemc
    with fade
    "Palla ends the call without another word."
    "And as soon as she does so, I get up and head out of the door."
    $ game.room = "pub"
    scene bg pub with fade
    "Hurrying to The Winchester, I go straight inside."
    show drink nonpc with fade
    "I settle down at what looks like a decent table to await Palla's arrival."
    scene bg pub with fade
    show palla at center, zoomAt(1.0, (940, 720)) with easeinright
    "Soon enough she strides in like she owns the place."
    "I give her a wave, and she responds with a small nod of the head."
    show palla at center, zoomAt(1.0, (840, 720)) with ease
    "Then she gestures to a table where she's standing."
    "Which I guess means that she wants me to go over there."
    menu:
        "Stay put":
            "It's pretty petty of me, I know."
            "But I pretend not to understand what Palla's trying to tell me."
            show palla annoyed at center, traveling(1.25, 0.5, (640, 880))
            "I keep on shrugging and shaking my head until she's forced to walk over."
            scene drink_room_pub zorder 1
            show drink_table_pub_nonpc zorder 3
            show drink_room_fg_pub zorder 4
            with fade
            show palla noacc annoyed zorder 2 at center, zoomAt(1.75, (1040, 800)) with easeinright
            bree.say "Hi, Palla..."
            bree.say "What were you waving your arms for?"
            "Palla looks a little pissed with me."
            "But I can see that she's trying to keep a handle on it."
            palla.say "Hello, [hero.name]..."
            palla.say "I was trying to say that's the best table in the place."
            palla.say "It has the best angles to be seen from."
            palla.say "So we should go and..."
            "I follow Palla's gaze."
            "Just in time to see someone else claiming the table."
            palla.say "Damn it!"
            bree.say "Oh no, what a shame!"
            bree.say "I guess we'll just have to sit here."
            show palla at flip, center, zoomAt(1.75, (1040, 800))
            pause 0.3
            show palla at flip, center, zoomAt(1.75, (500, 800)) with ease
            pause 0.3
            show palla at flip, center, zoomAt(1.75, (440, 1140)) with ease
            "I just about manage to keep a smirk off my face as I say this."
            "Loving the fact I've already got one over on Palla."
            $ hero.morality -= 1
        "Go over to Palla":
            "Not wanting to blow it, I get up and hurry over."
            scene drink_room_pub
            show palla noacc at flip, center, zoomAt(1.75, (440, 1140))
            show drink_table_pub_nonpc
            show drink_room_fg_pub
            with fade
            "Palla's already sitting down, like a queen on her throne."
            "And she makes no effort to get up as I arrive either."
            show palla talkative
            palla.say "Hello, [hero.name]..."
            palla.say "This is the best table in the place."
            palla.say "It has the best angles to be seen from."
            palla.say "So I always insist on sitting here."
            show palla normal
            "I nod as I pull out a chair and sit down."
            bree.say "Oh yeah..."
            bree.say "I see what you mean."
            "Palla nods and smiles, evidently approving of my reaction."
            "And sure, it means that she's got the upper hand."
            "But what does that matter if it puts her at ease?"
            $ hero.morality += 1
    show palla normal with fade
    "We order drinks and a little something to snack on."
    "And then I turn to Palla, trying to look serious."
    bree.say "So, Palla..."
    bree.say "Fashion and all that?"
    "I can see that Palla's in her element right now."
    "Holding court as she prepares to share her wisdom with me."
    show palla talkative
    palla.say "Well, [hero.name]..."
    palla.say "My philosophy has always been..."
    "What?"
    "You didn't expect me to clue you in on all of that guff, did you?"
    "All you need to know is that Palla can bang on about clothes for bloody ages!"
    "And it doesn't take me long to lose interest either."
    "It's only when she mentions her living arrangements that my interest reawakens."
    palla.say "Of course wardrobe space is a problem."
    palla.say "Unless you can convince your housemates to let you use theirs."
    palla.say "But then Shawn hardly even bothers to iron his clothes anyway."
    palla.say "So keeping them in a pile on the floor doesn't bother him!"
    show palla normal
    "At the mention of Shawn's name, I take my chance."
    "Thinking that I can steer the conversation in that direction."
    bree.say "Shawn let's you use his wardrobe space?"
    bree.say "Aww...that's so like him."
    show palla flirt
    "Palla raises an eyebrow and gives me a wry smile."
    show palla joke
    palla.say "Oh, [hero.name]..."
    palla.say "You have NO idea, of what he'll do for me!"
    show palla wink
    palla.say "Shawn's one of those guys you can wrap around your finger, if you know how."
    show palla normal
    "I feel a sensation of anger flaring in my gut as Palla describes Shawn."
    "Because I can't stand the casual way she's gloating about using him."
    "But all she's done so far is say that he's a sucker for a pretty girl."
    "Which describes like ninety nine percent of straight guys with a pulse."
    "So I'm going to need to dig a little deeper."
    "To give her the chance to out herself as the gold-digging skank I think she is."
    bree.say "Oh, but you have to be so careful with that kind of guy, Palla."
    bree.say "They can get so obsessed with you so quickly."
    bree.say "You need to be watch what you ask them for, even what you say in passing."
    bree.say "Or else before you know it, they're selling their organs for you!"
    show palla happy
    "Palla just chuckles and shakes her head at this."
    show palla talkative
    palla.say "Are you serious, [hero.name]?"
    palla.say "You make it sound like a girl should be mothering that kind of guy!"
    palla.say "If they're that naive, then they need to be smartened up."
    palla.say "And if they still don't get it, then they deserve everything they get!"
    show palla normal
    "Okay, okay..."
    "So Palla just admitted that she's cool with leeching off of guys."
    "But I'm going to need more, and specifics about her relationship with Shawn."
    "So let's give the old financial independence a poke, see what that flushes out."
    bree.say "Well, Palla..."
    bree.say "When you put it like that..."
    bree.say "But you're just using Shawn for gratification, right?"
    bree.say "Like, you must be successful on your own?"
    bree.say "Or else how would you afford to dress as nice as you do?"
    bree.say "Clothes as fancy as those can't be cheap."
    bree.say "Especially when there's rent and bills to pay!"
    "I gesture to the fashionable outfit Palla has on."
    show palla happy
    "But she just laughs and shakes her head."
    show palla talkative
    palla.say "Ha!"
    palla.say "Okay, [hero.name]..."
    palla.say "I'll let you in on a little secret."
    show palla normal
    "Palla smiles like a smug cat as she crooks a finger to beckon me closer."
    "I feel a little like I'm being lured in by a predatory animal."
    "But I lean towards her all the same."
    show palla talkative
    palla.say "I can't remember the last time I paid a bill, or for my rent!"
    palla.say "I just dropped a couple of hints around Shawn, pouted in the right places..."
    palla.say "And just like magic, he promised he'd take care of it all!"
    show palla normal
    "Again I feel the surge of rage building in me."
    "If Palla were just taking the occasional bit of help from Shawn, I could handle it."
    "Even if she was leeching off of him and felt guilty about it, I could understand."
    "But what really makes me mad is the way that she's so proud of herself."
    "That and how she seems to think I'm naive for not doing the same thing!"
    bree.say "Oh my..."
    bree.say "Shawn's paying for everything?"
    bree.say "He must really care about you, Palla!"
    show palla happy
    "Palla nods and chuckles, a totally derisive sound."
    show palla talkative
    palla.say "Oh yeah..."
    palla.say "The little sad-sack is ga-ga for me."
    palla.say "All I have to do is keep showing him the tiniest hint of affection."
    palla.say "Just a little light flirting here and there, that's all it takes."
    palla.say "If I keep that up, he's mine for as long as I want!"
    show palla normal
    "By now I'm starting to feel like I can't keep this up any longer."
    "Palla's gloating his getting to be too much for me to bear."
    "So I make a point of finishing my drink and making to get up."
    bree.say "Well, it's been great talking to you, Palla..."
    bree.say "You really opened my eyes to a whole lot of stuff!"
    bree.say "We should do this again some time."
    show palla flirt
    "Palla raises an eyebrow at the suggestion."
    palla.say "Hmm..."
    show palla talkative
    palla.say "I'll check my diary and get back to you, okay?"
    show palla normal
    "But before I can leave, Palla gestures to the drinks."
    show palla talkative
    palla.say "Would you mind getting these?"
    show palla whining
    palla.say "I'm running low on funds right now."
    palla.say "And the Bank of Shawn isn't open until he gets off work!"
    show palla normal
    "Stunned that she'd be so bold, I can't summon words to respond."
    "Instead I just nod my head as I walk away from the table."
    scene bg pub with fade
    "Making it to the bar, I feel a desperate need to hit back."
    "So when the bartender comes over, I concoct a plan."
    bree.say "Hey there..."
    bree.say "My friend at the table over there said she'd get the tab."
    "Bartender" "Sure thing!"
    bree.say "Oh, and she also said to add a large gratuity as well."
    "Bartender" "That's very kind of her!"
    bree.say "Yeah, she's a real giving kind of gal!"
    $ game.room = "street"
    scene bg street with fade
    "With that, I walk out of The Winchester."
    "Wondering what kind of chaos I'm leaving in my wake."
    return

label shawn_female_yandere_02:
    "Now that I know just how much of a freeloading skank Palla is, it's time to take positive action."
    "If she's not going to change her ways and stop leading poor Shawn on, then I'll have to stop her myself."
    "All it takes is a little bit of online research into household items that can be used to manufacture poisons."
    "That and a last minute invite to Shawn and Palla, asking if they want to meet up at a nightclub this evening."
    "I spin them some bullshit story about my friends ditching me, and that's all it takes to reel Shawn in."
    "And as soon as he talks Palla into saying yes, everything is in place."
    "All I have to do now is wait for the right moment."
    scene bg street with fade
    "Waiting for Shawn and Palla outside the nightclub, I can't help straightening my outfit."
    "And that's because I put a lot of care into choosing what I have on tonight."
    "It can't possibly be something out of fashion, as that might make Palla scrutinise me more closely."
    "But at the same time, it can't be something that's way ahead of the curve either."
    "As that might make her think that I'm actively trying to out do her."
    palla.say "Nice try with the outfit, [hero.name]..."
    palla.say "But you really should have asked my advice!"
    shawn.say "Hey, [hero.name]..."
    shawn.say "Are you ready to party?"
    palla.say "Urgh..."
    palla.say "Shawn..."
    palla.say "What have I told you about using the word 'party' as a verb in my presence?"
    "Well, there can't be any mistaking that little exchange for anybody else."
    "So I smooth my outfit one last time while taking a deep breath."
    "And with a fake smile pulling at my features, I turn to face them."
    show shawn date at right with easeinleft
    show palla date at left with easeinleft
    bree.say "Hey, guys..."
    bree.say "I'm SO glad you could make it tonight."
    bree.say "When everyone else pulled out on me, I thought the night was ruined!"
    "Shawn instantly nods, making it plain that he empathises with me."
    show shawn talkative
    shawn.say "No problem at all, [hero.name]..."
    shawn.say "Anything to help you out."
    show shawn normal
    "Palla, on the other hand, isn't nearly as genuine."
    show palla mindless
    palla.say "Aww..."
    palla.say "Poor little you!"
    show palla b happy
    palla.say "But aren't you lucky I was here to save you?"
    show palla a normal
    show shawn talkative
    shawn.say "Erm..."
    show shawn noglasses
    shawn.say "Don't you mean we?"
    show shawn normal
    show palla joke
    palla.say "I know what I meant."
    show palla normal
    "I'm still smiling as I nod at Palla."
    "Because that's exactly how I want her to be acting tonight."
    "So long as she's got her nose in the air, thinking she's not paying attention to the little things."
    "Which means that her guard is going to be down too."
    bree.say "I really am grateful, Palla..."
    bree.say "Tonight would have been dead in the water without you guys."
    scene bg nightclub
    with fade
    play music "music/darren_curtis/feel_it_in_your_feet.ogg" loop fadein 0.5
    "We're walking into the nightclub as I say all of this."
    show shawn date noglasses at right with easeinleft
    show palla date at left with easeinleft
    "But Palla just nods in agreement, as if there's no need for words."
    "Then she kind of gestures towards the bar."
    "No sooner has she done this than Shawn leaps into action."
    show shawn nice
    shawn.say "I'll get the drinks!"
    show shawn smile
    menu:
        "Insist on getting the drinks myself":
            bree.say "Oh no, Shawn..."
            bree.say "Let me get the first round in!"
            show shawn normal
            "I kind of leap at Shawn as I say this."
            "And the move seems to surprise the both of them."
            "So I do the best I can to explain myself."
            bree.say "You know..."
            bree.say "Because I invited you along - so you're my guests?"
            "Shawn shrugs and motions for me to go right ahead."
            "I breathe a sigh of relief and get right on it."
            "Because I want to be able to slip my little additive into Palla's drink myself."
            $ shawn.sub += 1
        "Allow Shawn to get the drinks":
            "Being able to slip my little additive into Palla's drink at the bar would have been useful."
            "But I figure that I can still manage to get close enough once Shawn gets back."
            "Plus letting him buy the drinks is sure to lessen suspicions towards me."
            bree.say "Sure thing, Shawn..."
            bree.say "You know my poison!"
            $ shawn.love += 2
    show bg vip
    show palla happy at center, zoomAt(1.5, (940, 1040))
    show shawn happy at center, zoomAt(1.5, (340, 1040))
    with fade
    "As soon as we all have drinks, I get ready to make my move."
    "The moment Palla puts down her drink, I step up and pour the poison into it."
    "Luckily for me, she has a habit of swirling it whenever she picks it up."
    "So the poison is quickly mixed in."
    scene bg nightclub
    show shawn date noglasses happy at right
    show palla date happy at left
    with fade
    "Now all I have to do is wait, and so I just pretend to enjoy the night."
    "That works out for me pretty well, until we're on the dancefloor."
    show palla whining
    "Palla starts to cough, putting a hand to her throat."
    show palla b at center, zoomAt(1.5, (640, 1040)) with dissolve
    "Nobody else seems to notice at first, and I make a point of ignoring her too."
    show palla with hpunch
    "But it's when she starts foaming at the lips, the shit really hits the fan!"
    hide palla with easeoutbottom
    play sound body_fall
    show shawn stuned at hshake
    pause 1
    show palla death nomc with fade
    "Palla collapses to the floor, the foam beginning to turn red as she does so."
    "Of course people instantly start to rush to help, and chaos erupts in the nightclub."
    "But now I have to figure out the best way for me to play it."
    menu:
        "Rush to Palla's side":
            "The best thing would be to look shocked and try to help."
            "So I rush over and kneel down beside Palla as she twitches on the ground."
            show palla death -nomc with vpunch
            bree.say "Palla?"
            bree.say "Can you hear me?"
            "I lean in while others are trying to do various things."
            "But I make a point of leaning my weight on her chest as I do so."
            "In the confusion, nobody can see that I'm doing all I can to smother Palla."
            "And in the end, I don't really know if it makes any difference."
            "But I do get a sense of satisfaction once I know it's all over."
            $ hero.morality -= 3
        "Cling onto Shawn":
            "The last thing I want is for Shawn to get too close to Palla."
            "Maybe even for her to be able to spit out some final words to him."
            "So I pretty much thrown myself into his arms, playing the weak little woman for all I'm worth."
            scene bg nightclub
            show shawn surprised date at center, zoomAt(1.5, (640, 1100))
            bree.say "Shawn..."
            bree.say "I'm so scared!"
            bree.say "What's happening to poor Palla?"
            "I can tell that Shawn's torn right now."
            "Part of him obviously wants to run to Palla, to do anything he possibly can to save her."
            "But another part is battling with an entire lifetime of being told he should be a gentleman."
            "And in the end that's what wins out, as he stay holding onto me as Palla lies dying a few feet away."
            shawn.say "I..."
            shawn.say "I don't know, [hero.name]..."
            shawn.say "Maybe someone spiked her drink?"
            show shawn upset
            $ hero.morality -= 1
    show vincent teaser at blacker, center, zoomAt(2, (1100, 1420)) with easeinright
    "Customer" "Oh fuck..."
    "Customer" "She's..."
    "Customer" "She's dead!"
    "As soon as the word gets out, the chaos in the nightclub turns into uproar."
    "I press myself further into Shawn's shoulder, acting like I'm frightened for my life."
    show shawn normal at center, zoomAt(1.7, (640, 1240))
    "And it works perfectly, as I feel him holding me tighter than ever."
    "I allow myself a smile as my actions keep him from going to Palla's fast cooling corpse."
    "And also because they keep all of his attention focussed on me alone."
    "I predict that he's going to need to spend a lot of time with me in the days and weeks to come."
    "Helping me to get over the loss of dear, sweet Palla."
    "And in that time, I think we're going to grow very, very close!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
