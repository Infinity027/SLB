init python:
    
    Event(**{
        "name": "mike_female_shower_bj",
        "label": "mike_female_shower_bj",
        "duration": 1,
        "conditions": [
            HeroTarget(
                IsGender("female"),
                IsActivity("take_a_shower")),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                MinStat("love", 100),
                ),
            ],
        "once_week": True,
        "do_once": False,
        })
    
    Event(**{
        "name": "mike_female_livingroom_bj",
        "priority": 500,
        "label": "mike_female_livingroom_bj",
        "duration": 1,
        "conditions": [
            HeroTarget(
                IsGender("female"),
                IsActivity("watch_tv_with_everyone_female")),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                MinStat("love", 100),
                ),
            ],
        "once_day": True,
        "do_once": False,
        })
    
    Event(**{
        "name": "mike_female_event_01",
        "label": "mike_female_event_01",
        "duration": 1,
        "conditions": [
            HeroTarget(
                IsGender("female"),
                IsRoom("livingroom")),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                MinStat("love", 10),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_female_event_02",
        "label": "mike_female_event_02",
        "duration": 1,
        "conditions": [
            IsHour(12, 17),
            IsDone("mike_female_event_01"),
            HeroTarget(
                IsGender("female"),
                IsRoom("bedroom4")),
            PersonTarget(mike,
                Not(IsHidden()),
                IsRoom("kitchen"),
                MinStat("love", 20),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_female_event_03a",
        "priority": 500,
        "label": "mike_female_event_03a",
        "duration": 1,
        "conditions": [
            IsDone("mike_female_event_02"),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("pub"),),
            PersonTarget(mike,
                Not(IsHidden()),
                MinStat("love", 30),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_female_event_03b",
        "priority": 500,
        "label": "mike_female_event_03b",
        "duration": 1,
        "conditions": [
            IsDone("mike_female_event_03a"),
            IsTimeOfDay("morning"),
            HeroTarget(
                IsGender("female"),
                IsRoom("kitchen")),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_female_event_04",
        "label": "mike_female_event_04",
        "duration": 1,
        "conditions": [
            IsDone("mike_female_event_03b"),
            HeroTarget(
                IsGender("female"),
                IsActivity("watch_tv_with_mike")),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                MinStat("love", 40),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_female_event_05a",
        "label": "mike_female_event_05a",
        "duration": 1,
        "conditions": [
            IsDayOfWeek("67"),
            IsDone("mike_female_event_04"),
            HeroTarget(
                IsGender("female"),
                IsRoom("cinema")),
            PersonTarget(mike,
                Not(IsHidden()),
                MinStat("love", 50),
                Not(IsFlag("delay"))
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_female_event_05b",
        "label": "mike_female_event_05b",
        "duration": 1,
        "conditions": [
            IsDone("mike_female_event_04"),
            IsTimeOfDay("afternoon", "evening"),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("home"),
                ),
            PersonTarget(mike,
                HasRoomTag("home"),
                Not(IsHidden()),
                MinStat("love", 50),
                Not(IsFlag("delay"))
                ),
            PersonTarget(sasha,
                HasRoomTag("home"),
                Not(IsHidden()),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_female_event_05c",
        "label": "mike_female_event_05c",
        "duration": 1,
        "conditions": [
            IsDone("mike_female_event_04"),
            IsHour(19, 23),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("pub"),),
            PersonTarget(mike,
                Not(IsHidden()),
                MinStat("love", 50),
                Not(IsFlag("delay"))
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_female_event_05d",
        "label": "mike_female_event_05d",
        "duration": 1,
        "conditions": [
            IsDone("mike_female_event_05a", "mike_female_event_05b", "mike_female_event_05c"),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("home"),
                ),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                MinStat("love", 50),
                Not(IsActivity("sleep")),
                Not(IsFlag("delay")),
                ),
            ],
        "do_once": True,
        })
    
    Activity(**{
        "name": "mike_female_event_06",
        "label": "mike_female_event_06",
        "duration": 1,
        "conditions": [
            
            IsDone("mike_female_event_05d"),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("park"),
                MaxStat("hunger", 5),
                ),
            PersonTarget(mike,
                Not(OnDate()),
                Not(IsHidden()),
                HasRoomTag("park"),
                MinStat("love", 60),
                ),
            ],
        "display_name": "Eat a sandwich",
        "icon": "picnic",
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_female_event_07",
        "label": "mike_female_event_07",
        "duration": 1,
        "conditions": [
            IsHour(8, 12),
            IsDone("mike_female_event_06"),
            HeroTarget(
                IsGender("female"),
                IsRoom("university")),
            PersonTarget(mike,
                Not(IsHidden()),
                MinStat("love", 80),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_female_event_08",
        "priority": 500,
        "label": "mike_female_event_08",
        "duration": 3,
        "conditions": [
            IsDone("mike_female_event_07"),
            IsTimeOfDay("morning"),
            HeroTarget(
                IsGender("female"),
                IsRoom("kitchen")),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                MinStat("love", 100),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_female_event_09",
        "label": "mike_female_event_09",
        "duration": 1,
        "conditions": [
            IsDone("mike_female_event_08"),
            HeroTarget(
                IsGender("female"),
                IsRoom("date_mall1")
                ),
            PersonTarget(mike,
                OnDate(),
                MinStat("love", 120),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_female_event_10",
        "label": "mike_female_event_10",
        "duration": 1,
        "priority": 500,
        "do_once": True,
        "music": "music/roa_music/smile_for_me.ogg",
        "conditions": [
            IsDone("mike_female_event_09"),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("pub"),),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                Not(HasCheated()),
                MinStat("love", 140),
                ),
            ],
        })
    
    Event(**{
        "name": "mike_female_event_11a",
        "label": "mike_female_event_11a",
        "duration": 1,
        "priority": 500,
        "do_once": True,
        "music": "music/roa_music/smile_for_me.ogg",
        "conditions": [
            IsDone("mike_female_event_10"),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("home"),
                ),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                Not(HasCheated()),
                MinStat("love", 160),
                ),
            ],
        })
    
    Event(**{
        "name": "mike_female_event_12a",
        "label": "mike_female_event_12a",
        "duration": 1,
        "priority": 500,
        "do_once": True,
        "music": "music/roa_music/smile_for_me.ogg",
        "conditions": [
            IsDone("mike_female_event_11a"),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("mall_southside"),
                ),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                Not(HasCheated()),
                MinStat("love", 180),
                ),
            ],
        })
    
    Event(**{
        "name": "mike_female_job_event_01",
        "label": "mike_female_job_event_01",
        "duration": 1,
        "priority": 500,
        "do_once": True,
        "music": "music/roa_music/smile_for_me.ogg",
        "conditions": [
            MinDaysPlayed(60),
            IsTimeOfDay("afternoon", "evening"),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("home"),
                ),
            PersonTarget(mike,
                Not(IsHidden()),
                HasRoomTag("home"),
                Not(IsActivity("sleep")),
                ),
            ],
        })
    
    Event(**{
        "name": "mike_female_wedding_invite",
        "priority": 500,
        "label": "mike_female_wedding_invite",
        "conditions": [
            HeroTarget(IsGender("female")),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                MinStat("love", 100),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_preg_talk",
        "label": "mike_preg_talk",
        "conditions": [
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                IsFlag("pregnancy_father", "mike"),
                Or(
                    MinCounter("pregnant", 60),
                    IsFlag("foundpreg"),
                    ),
                ),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                IsFlag("toldpreg", False),
                MinStat("sexperience", 1),
                ),
            ],
        "do_once": False,
        })
    
    Event(**{
        "name": "mike_find_out_pregnancy",
        "label": "mike_find_out_pregnancy",
        "conditions": [
            HeroTarget(
                IsGender("female"),
                Not(OnDate()),
                MinCounter("pregnant", 30),
                CounterChanceChecker("pregnant", 50)
                ),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                IsFlag("toldpreg", False),
                MinStat("sexperience", 1),
                ),
            ],

        "do_once": False,
        })
    
    Event(**{
        "name": "mike_job_offer_female",
        "label": "mike_job_offer_female",
        "duration": 1,
        "conditions": [
            IsTimeOfDay("afternoon"),
            IsDone("mike_female_job_event_01"),
            HeroTarget(
                IsGender("female"),
                HasRoomTag("home"),
                ),
            PersonTarget(mike,
                Not(IsHidden()),
                HasRoomTag("home"),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "mike_asleep",
        "label": "mike_asleep",
        "priority": 1500,
        "conditions": [
            HeroTarget(IsRoom("bedroom6")),
            PersonTarget(mike,
                IsPresent(),
                Not(IsHidden()),
                IsActivity("sleep"),
                ),
            ],
        "do_once": False,
        "once_hour": False,
        })

label mike_female_event_01:
    if mike.love.max < 20:
        $ mike.love.max = 20
    $ mike.flags.cried = False
    scene bg livingroom
    "It's always a little awkward when you first move into a new house."
    "You have to get used to the place and remember where everything is."
    "But it's even worse when you have new housemates to get to know too."
    "Because they're always going to be really complicated to figure out."
    "Way more so than trying to get to grips with a new washing machine or oven!"
    "Part of me wants to get to know [mike.name] and Sasha as soon as I possibly can."
    "But another part of me is worried that if I do that, they'll think I'm pushy and rude!"
    show sasha casual at center with easeinleft
    "I guess it's easier with Sasha, as she always seems to be doing something."
    hide sasha with easeoutright
    "She has her studies and a job, as well as being in some kind of band."
    "But [mike.name]'s a different story."
    show mike work sad at right with easeinright
    "I know that he has a day-job, one that he doesn't talk about much."
    "But it seems to stress him out, as he's always tired and cranky when he gets home."
    "And I'm pretty sure that he has friends, but he doesn't seem to see much of them."
    show mike happy at center with ease
    "All in all, I think he's pretty lonely."
    show mike sad at left with ease
    "Maybe a little sad too!"
    hide mike with easeoutleft
    "So in the end, I make up my mind to do something about it."
    "[mike.name] acts like he's living alone, but that's not true."
    "I think he needs to know that Sasha and I are here for him."
    "Or at least that I'm here for him..."
    scene bg black with timelaps
    scene bg livingroom with timelaps
    "So I spend some time racking my brains to think up a solution."
    "What can I do with [mike.name] that'll make him feel less lonely?"
    menu:
        "Joke with [mike.name]":
            "Maybe what [mike.name] needs is to have more fun around the house?"
            "Maybe he needs to see his housemates as his friends too?"
            "I wait for [mike.name] to walk into the room."
            show mike at right with easeinright
            "And the moment that he does, I look for my opening."
            "There it is - he's holding it in the palm of his hand!"
            bree.say "What ya got there, [mike.name]?"
            bree.say "A bagel?"
            show mike down at center with ease
            "[mike.name] looks down at the bagel clutched in his hand."
            "And then he looks back up at me, a little puzzled."
            mike.say "Erm..."
            mike.say "Yeah, [hero.name], it's a bagel."
            bree.say "How is it?"
            bree.say "Because it looks pretty good!"
            "[mike.name] shrugs, still looking confused."
            mike.say "I guess it's not bad."
            "The moment the words are out of his mouth, I'm ready."
            "And then I pounce, unleashing all of my comedic genius upon him."
            bree.say "Not only that, [mike.name]..."
            bree.say "But it's knot-bread!"
            if hero.charm >= 20:
                "[mike.name] stares at be blankly for a few seconds."
                "Then he shakes his head and laughs out loud."
                show mike happy
                mike.say "Ouch, [hero.name]!"
                mike.say "That was like the worst joke I ever heard!"
                "I cock my head on one side and frown a little."
                bree.say "Oh yeah?"
                bree.say "Well if it's so terrible - why are you laughing?"
                mike.say "Because it's SO bad it's kinda funny, [hero.name]!"
                "I can't help my frown slowly turning into a smile."
                "And a few moments later, I'm laughing too."
                "Sure, [mike.name]'s laughing at me, not with me."
                "But at least he's laughing, which was the entire point."
                bree.say "Well forgive me for not being a natural comedian, [mike.name]!"
                mike.say "Oh, [hero.name]..."
                mike.say "Are all of your jokes that bad?"
                bree.say "Oh hell no!"
                bree.say "Most of them are FAR worse..."
                $ mike.love += 5
                return
            else:

                "[mike.name] stares at be blankly for a few seconds."
                show mike sad
                "Then he shakes his head and frowns."
                mike.say "What are you even talking about, [hero.name]?"
                mike.say "Of course it's bread!"
                mike.say "What do you think a bagel's even made of?!?"
                "He starts to turn and walk away."
                "Which leaves me struggling to explain myself."
                bree.say "No, no, no..."
                bree.say "It's a joke, don't you see?"
                bree.say "It's a knot made of bread..."
                bree.say "And knot-bread sounds like not bread!"
                "But [mike.name]'s already walked out of the room."
                "And he's done it at a pace that suggests he wanted to escape pretty quickly too!"
                "Urgh...well done, [hero.name] - you sure blew it this time!"
                $ mike.love -= 5
                return
        "Bake a cake for [mike.name]":
            "Maybe what [mike.name] needs is to see the house as a proper home."
            "A place where he lives part of his life and makes memories."
            "Not just somewhere he comes to sleep when he's not at work."
            "But how can I make this place feel more homely?"
            "I know - I can bake a cake!"
            "Sure, I'm no domestic goddess."
            scene bg kitchen with dissolve
            "But [mike.name] doesn't know that, does he?"
            "And I can just look up a recipe on the internet."
            "I mean, how hard can it be?"
            "As soon as I have the ingredients in front of me, I get started."
            "And pretty soon the kitchen is filled with the unmistakable smell of baking!"
            mike.say "Ah, [hero.name]..."
            mike.say "What's that smell?"
            mike.say "Are you actually baking something?!?"
            show mike at top_mostright
            "I look up to see [mike.name] hanging around in the doorway."
            "And I almost giggle at the way he's trying to hide his interest."
            show mike at center with move
            "He looks like he could have floated in here drawn by his nose."
            "You know how cartoon characters are drawn to the smell of food?"
            bree.say "Oh, hey, [mike.name]!"
            bree.say "Yeah, I thought I'd just knock us up a cake."
            bree.say "No big deal, I bake all the time."
            "Yeah, it's a lie."
            "But it's only a small one."
            "And if it cheers the poor guy up, what the hell!"
            "Just then the oven pings."
            bree.say "Oops!"
            bree.say "Looks like it's ready."
            bree.say "You want to have first taste of it?"
            "[mike.name] nods eagerly."
            "And then he watches in fascination as I take the cake out of the oven."
            "As soon as it's cool enough, I cut him a slice and hand it over."
            "We exchange smiles as [mike.name] bites into the slice of cake."
            "And I watch his face with interest, waiting to see his reaction."
            if hero.has_skill("cooking"):

                "[mike.name]'s still smiling as he chews the cake."
                "But I can soon see a change in his face."
                "Before now I kinda felt like he might have been humouring me."
                "But now his eyes are lighting up in a way you just can't fake."
                "He keeps on chewing longer than strictly necessary."
                "And it's almost like he doesn't want to swallow to keep the experience going!"
                bree.say "Erm..."
                bree.say "So..."
                bree.say "How is it?"
                show mike happy
                "[mike.name] waves his hands in the air and nods his head."
                mike.say "[hero.name]!"
                mike.say "You're a genius!"
                mike.say "That was, like, the best cake ever!"
                "I like to think I'm a modern kind of girl."
                "That I want a guy to respect me for who I am, not my domestic skills."
                "But even so, I can't help feeling my heart flutter a little at the praise."
                bree.say "You...you really think so?"
                mike.say "Hell yeah, [hero.name]!"
                mike.say "Nobody can cook these days."
                mike.say "But you're like...like the king of cooking!"
                mike.say "That makes you a treasure, you know?"
                "I'm blushing now, grinning like a fool."
                "And I want to see [mike.name] eat even more of my cake."
                "Hell, he can have the whole thing if he keeps giving me compliments like that!"
                $ mike.love += 5
                return
            else:

                "[mike.name]'s still smiling as he chews the cake."
                "But I can soon see a change in his face."
                "To his credit, he manages to keep on smiling."
                "Though his eyes betray the fact he's not having a good time."
                "And when he swallows, it looks visibly painful too!"
                bree.say "Erm..."
                bree.say "So..."
                bree.say "How is it?"
                "I swear [mike.name]'s eyes are actually watering as I ask the question."
                mike.say "Urgh..."
                mike.say "Yeah..."
                mike.say "It's...nice, [hero.name]...real nice!"
                bree.say "Oh...that's okay then!"
                "Suddenly [mike.name] shudders, and his stomach makes a worrying sound."
                "I open my mouth to say something, but he claps a hand over his own lips."
                hide mike with moveoutright
                "The other hand he holds up to silence me, and then he dashes out of the kitchen."
                "Leaning out of the door, I watch him literally run to the bathroom."
                "And as soon as the door is closed, I hear the sound of him heaving up his guts."
                "Urgh...well done, [hero.name] - you sure blew it this time!"
                $ mike.love -= 5
                return
        "Watch TV with [mike.name]":
            "I notice that everyone tends to watch TV on their laptops around here."
            "And most of the time we're all doing it alone in our rooms too!"
            "But there's a perfectly good TV in the sitting room, and sofas as well."
            "Maybe [mike.name] would feel more at home if someone watched TV in there with him?"
            "That's why I make sure that I'm in there with the TV on when he passes the doorway."
            bree.say "Oh..."
            bree.say "Hey, [mike.name]!"
            "At the sound of me calling his name, [mike.name] stops in his tracks."
            "Then he sticks his head around the doorframe, a curious look on his face."
            mike.say "Huh?"
            mike.say "What's up, [hero.name]?"
            "I give him what I hope is my best smile."
            "And at the same time, I pat the sofa cushion beside me."
            bree.say "I wondered if you'd mind keeping me company?"
            bree.say "I was just going to watch some TV."
            bree.say "But if you've got something better to do..."
            "[mike.name] shakes his head as he walks into the sitting room."
            mike.say "No, [hero.name]..."
            mike.say "I can spare you the time."
            "He walks over and takes the spot on the sofa beside me."
            show watch tv mike nopopcorn
            mike.say "So..."
            mike.say "What are we watching?"
            menu:
                "Choose a Romcom":
                    "Thinking quickly, I decide that it has to be something light."
                    "I don't want to scare [mike.name] off with a show that's going to bring him down."
                    bree.say "I was thinking..."
                    bree.say "How about a romcom?"
                    "[mike.name] frowns and kind of shrugs."
                    mike.say "Okay, [hero.name]..."
                    mike.say "Sounds fine to me."
                    "We settle down to watch the film together."
                    "I don't remember the name of the film, or the actors in it."
                    "But it's one of those by-the-numbers romcoms, you know?"
                    "The guy's cute, but he's kind of a jerk."
                    "The girl's pretty, but she's kind of a geek."
                    "They have a date, and it doesn't go well."
                    "So they confront each other about it."
                    "And they find they're really mad at each other because they're in love."
                    "But both of them were too proud to be able to admit it."
                    "I sit back, expecting to be entertained, but not blown away."
                    "And the next thing I know, the end credits are rolling."
                    mike.say "Aw, man!"
                    mike.say "It's over already?"
                    bree.say "You mean..."
                    "I pause to make a snuffling noise and wipe my nose."
                    bree.say "You mean you liked it?!?"
                    "[mike.name] shrugs and instantly tries to play it down."
                    mike.say "What?"
                    mike.say "I...well...it was pretty good, I guess!"
                    bree.say "Wait a minute, [mike.name]..."
                    bree.say "Are you crying?"
                    mike.say "Who, me?"
                    mike.say "No...I just have something in my eye, that's all!"
                    "I nod and decide to let the matter drop."
                    mike.say "I really enjoyed that, [hero.name]."
                    mike.say "You think we could do it again some time soon?"
                    bree.say "Sure, [mike.name]."
                    bree.say "Just hit me up when you want to, okay?"
                    hide watch tv
                    "[mike.name] nods as he gets up and walks out of the door."
                    "And I can't help smiling once he's gone."
                    "Because that seemed to go totally according to plan!"
                    $ mike.flags.cried = True
                    $ mike.love += 5
                    return
                "Choose a reality show":
                    "Thinking quickly, I decide that it has to be something light."
                    "I don't want to scare [mike.name] off with a show that's going to bring him down."
                    bree.say "I was thinking..."
                    bree.say "How about a reality show?"
                    "[mike.name] frowns and kind of shrugs."
                    mike.say "Okay, [hero.name]..."
                    mike.say "Sounds fine to me."
                    "We settle down to watch the show together."
                    "It's one of those forgettable ones, set on a really pretty island."
                    "All of the people on the show look like they could be models."
                    "And they all seem to be very high on themselves too!"
                    "I'm not sure what the actual point of the show is."
                    "But everyone seems to be cheating on everyone else at the same time!"
                    mike.say "Urgh..."
                    mike.say "Give me a break!"
                    "I glance sideways at [mike.name], trying to gauge his mood."
                    "And I can instantly see that he's not at all impressed."
                    bree.say "Erm..."
                    bree.say "What's up, [mike.name]?"
                    mike.say "Ah...it's just these types of show, [hero.name]."
                    mike.say "It's like they always find the worst people possible to be on them."
                    bree.say "Oh...so you don't like the contestants on the show?"
                    mike.say "It's not just that."
                    mike.say "They're also proving just how pathetic the relationship between a boy and a girl can be!"
                    bree.say "I...I'm sorry, [mike.name]!"
                    bree.say "Should we watch something else instead?"
                    mike.say "Nah, [hero.name] - I think I'll just go to my room."
                    mike.say "I kinda want to be alone right now."
                    hide watch tv
                    "With that, [mike.name] gets up and walks out of the room."
                    "Urgh...well done, [hero.name] - you sure blew it this time!"
                    $ mike.love -= 5
                    return

label mike_female_event_02:
    if mike.love.max < 30:
        $ mike.love.max = 30
    "I run my fingers along the spines of the books on my shelf. A comic book I haven't read in a while catches my eye."
    "The Revengers in: The Making of a Villain"
    "This particular issue stars Tin Man, Hot Thunder, Falcon Eye, Brown Recluse, Pilot Canada, and Bulk. The story details how each of them met and fought against Manos."
    "Manos, the villain, became evil when he was young and lost one of his hands in a duel. He felt off-balance ever since. He was just about to blow up the world, when--"
    "Bulk makes a run for Manos, and slams him into the ground -- BOOM!"
    "Biff! Wham! Thwip! Smack!"
    "I hear a series of loud clangs coming from the kitchen downstairs. Sounds like someone's rooting around in the kitchen to make a meal. I return my attention to the page."
    "The full Revengers team surrounds Manos. He begs them to stop and reconsider."
    "Why should we trust you?"
    "You see, I have...The Glove of Eternity! All I have to do is slip this on, snap my fingers, and the ENTIRE WORLD will explode!"
    "Pilot Canada retorts, 'How are you going to do that? The glove is left-handed. It won't fit on your right hand, Manos.'"
    "Manos is visibly upset and makes to punch Pilot Canada."
    "JOLT and BOOMMM -- Hot Thunder throws his lightning boomerang axe at Manos, intercepting the blow..."


    pause 0.4
    with hpunch
    "A jarring clatter comes from outside my room, causing me to jump. I mutter an expletive and vent to myself about the noise."
    bree.say "Christ that scared me. I know I didn't hear that sound effect in my head. Ok...back to reading..."
    "..."
    "..."
    "..."
    "Actually, I would feel bad if I didn't check it out. Better safe than sorry."
    "I place a bookmark in between my pages because I am no heathen and I leave the comic book on my bed before heading downstairs."
    show bg secondfloor
    "I quickly run and skip a few stairs on my way down."
    show bg kitchen
    show mike casual sad
    "Upon turning into the kitchen, I see [mike.name] with both hands on his head, eyes shut."
    "...and a cast iron skillet on the floor."
    bree.say "[mike.name]? [mike.name], are you alright? What did you do?"
    "[mike.name] opens his eyes halfway and stammers."
    mike.say "Nothing, really, I just hit my head on something!"
    bree.say "What's the skillet doing on the floor? Did you drop it when you hit your head? Which cabinet did you whack yourself on?"
    show mike down
    "[mike.name]'s expression grows more pained, but it doesn't seem to be from whatever he hit his head on."
    mike.say "I... tossed the skillet because I was just messing around and this one was a bit lighter than I expected, so..."
    mike.say "...I twirled it a bit too hard and I hit myself on top of my forehead."
    "I pause, trying hard to stifle a laugh. I did feel bad but the scene playing out in my imagination was really funny and I couldn't help it."
    mike.say "Really? You're laughing at me? This is why I didn't want to tell you."
    "[mike.name] scowls and turns away from me, upset."
    bree.say "If you'd caught me in the kitchen with one suspiciously solitary kitchen item on the floor, I'm sure you'd let out a giggle too!"
    mike.say "I mean, at least you asked if I was okay first I guess?"
    bree.say "You're welcome!"
    "I said cheerily with a slightly obnoxious attitude."
    "[mike.name] returned my sass with a roll of his eyes and a groan. He closed his eyes and held his hand to his face."
    mike.say "Fuck...it's swollen...and honestly I'm a little dizzy."
    bree.say "Ok well we can't keep you on the floor. Are you able to move to sit down at the table?"
    mike.say "Yeah...hold on..."
    "He gives forth a grunt as he stands slowly, in pain. His stomach rumbles greedily."
    bree.say "Alright. I feel bad for you, so I'll do the cooking. With my... great... cooking talents. Don't worry, I haven't killed anyone yet."
    mike.say "That sounds suspicious."
    bree.say "Like the skillet?"
    mike.say "..."
    "[mike.name] purses his lips in exasperation. I flash him a shit-eating grin."
    "[mike.name] nodded as if to say 'yeah, okay, you little shit.'"
    mike.say "Yes, [hero.name]. Like the skillet."
    "He looked pointedly at me. I looked around nervously."
    bree.say "S-So, uh, what's for dinner?"
    mike.say "Well...I was going to make a mushroom risotto but since you're so confident in your own cooking."
    "It was clear he was being sarcastic when addressing my confidence."
    mike.say "I think I'll live if you can whip me up some bacon and eggs. Nobody can screw that up, not even you."
    "I'm relieved but I'm not going to show it. I crinkle my nose and pout at him. When I turn back toward the stove, I smile to myself."
    "Surely I won't burn everything. Maybe just a few things. I click the dial on the stove up to a 6 to begin heating the pan."
    mike.say "Alright. Because I don't want you to make a shield out of prayers and tin foil, you should make the bacon in the oven."
    bree.say "You can make bacon in the oven?!"
    "[mike.name]'s head finds his way into his hands. I suspect it isn't in response to his swollen head."
    mike.say "Oh dear, what am I going to do with you? Yes. That's THE way to make it. You like bacon at restaurants, right?"
    bree.say "More than anything, of course."
    mike.say "Great. We'll get you at least good enough to where you can pretend they're similar."
    "I scowl at him."
    bree.say "I'm starting to see why this frying pan hit you in the face."
    mike.say "Shut up. Set the oven to 400 and put bacon on a foil-lined tray and stick it in. Set a timer for 20 minutes. Once it dings, you're golden."
    "I start preheating the oven."
    mike.say "Oh, put butter or coconut oil on the skillet."
    bree.say "Where... is the coconut oil?"
    mike.say "Pantry, top shelf. Can you reach it?"
    bree.say "I can always climb!"
    "I fetch the... tub (is it a tub? It just looks like a jar of mayonnaise...) of coconut oil and take a spoonful of the stuff and let it melt in the pan."
    "The oven also dings, and I push the sheet of bacon in once the oven stops breathing on me."
    mike.say "I feel like I could go for some scrambled eggs. Crack open three, unless you want some, and then just poke the yolks and stir them a bit."
    bree.say "All right. I'll have three also."
    mike.say "Shouldn't change the process. Carry on, chef!"
    "I roll my eyes. If anything, HE'S the chef. I'm just the cooking monkey."
    bree.say "I feel like you're the rat under that guy's hat in that cartoon movie we saw a while back."
    mike.say "Rats in my Soupie? Haha yeah I guess it's a little like that. I tell you how to cook, and you just do it."
    bree.say "Or maybe you're the mean critic at the end and my food is so good I bring happiness back into your life?"
    "[mike.name] looked at me in disbelief."
    mike.say "You? Cooking food that good? Are you high?"
    bree.say "You wish. Just watch. These eggs and bacon are gonna blow your mind, Mr. Pessimist!"
    mike.say "Hey, stir the eggs! I don't want an omelet!"
    "I yelp, afraid I'd burned them, and stirred them vigorously. A little too vigorously...a blob of half-cooked egg goes flying, narrowly missing [mike.name]'s face. He ducked. Surprisingly quick reflexes for someone with a head injury. Maybe he's not that hurt after all."
    mike.say "Watch it!"
    bree.say "AAAHH, SHIT! I'm sorry! I'm making a huge mess! Uggghh I don't wanna have to clean this..."
    mike.say "Oh, leave me the dishes."
    "Might be the hottest thing I've ever heard. Willingly being helpful? Scandalous."
    bree.say "W..Wait like really?"
    mike.say "Well yeah...you're doing the cooking FOR me. It's only fair I clean up since I'm incapacitated."
    "I get a fuzzy feeling in my chest. He didn't have to insist, after all."
    bree.say "Thanks."
    mike.say "Of course."
    "The eggs look... solid, so I move the pan off the heat. I also take the bacon out of the oven since it'd been about twenty minutes. Looks crispy."
    bree.say "Order up, got eggs and bacon!"
    "I plate the food and saunter over to the table, forks and knives in tow as well."
    mike.say "Well, nothing smells burnt."
    bree.say "Will you cut that out, shitlord? Now, I did a nice thing for you, stop bagging on me."
    mike.say "You're right. I'm sorry. Thank you for helping me and cooking."
    "Feeling triumphant, I strike a pose, crossing my arms and looking down my nose at him."
    bree.say "That's right. Now, let's eat."
    show mike happy
    mike.say "This is really good. I'm impressed, [hero.name]."
    bree.say "Thanks, [mike.name]."
    "We finish eating and I put the dishes in the sink for [mike.name] to clean later. I go back to my room and flop down to pick up the comic book again."
    mike.say "Welp. Back to reading."
    return

label mike_female_event_03a:
    if mike.love.max < 40:
        $ mike.love.max = 40
    scene bg door pub with fade
    "It's been a few days now since I got myself moved into the house."
    "And I feel like I'm settling in pretty well, liking the place a lot."
    "But I still haven't ventured out much and I don't know the neighbourhood at all."
    "Which is the main reason I say yes when I get invited to the local pub by Samantha."
    "I didn't deal with her when I was getting everything sorted to move in."
    "It was Ryan, her partner that handled most of the calls that set it up."
    "So I'm eager to check out some of the local amenities."
    "But I also want to see if I can pump Samantha for more details on [mike.name]."
    "I get the feeling they were close, but he clams up whenever I mention Samantha and Ryan around him."
    scene bg pub with fade
    "I follow the directions to the pub and step inside."
    "It hits me then that I don't know what Samantha looks like."
    show samantha casual with dissolve
    "But then I see a girl waving at me from across the taproom."
    "Oh crap - she's gorgeous!"
    "She's tall and has that kind of long, flowing chestnut hair!"
    "In short, she's the kind of girls that guys write poetry about!"
    "Trying to hide my feelings of inadequacy, I smile and hurry over."
    show samantha happy at center, zoomAt(1.5, (640, 1140))
    samantha.say "Hi there!"
    samantha.say "You must be [hero.name], yeah?"
    show samantha normal
    "I nod as I sit down."
    "All the time hoping the smile on my face seems genuine."
    bree.say "That's me!"
    bree.say "And you must be Samantha?"
    show samantha happy
    "Samantha laughs and waves a hand at me."
    samantha.say "Oh please..."
    samantha.say "Call me Sam."
    show samantha normal
    samantha.say "Everybody apart from my mother does!"
    "I nod, my smile becoming a little more forced as I do so."
    bree.say "Erm..."
    bree.say "Okay...Sam..."
    bree.say "I gotta say, I did wonder why you wanted to meet me."
    bree.say "I mean, Ryan already did all of the checking up on me."
    bree.say "And I'm all moved into the house now too!"
    bree.say "I've got no complaints either."
    bree.say "The house is great."
    bree.say "So are [mike.name] and Sasha - I'm sure we'll all be great friends."
    "Sam smiles and nods."
    samantha.say "I know, [hero.name], I know."
    samantha.say "Don't think of this as me checking you out."
    samantha.say "It's more like me being curious of who's moving in with [mike.name]."
    "I'm obviously not as good at hiding my surprise as I am my other emotions."
    "Because my eyebrows shoot up as soon as Sam admits to her true motive."
    bree.say "Oh...I see!"
    bree.say "Or, actually...I don't..."
    bree.say "Why would you be interested in who [mike.name] lives with, Sam?"
    "Sam doesn't seem the least bit thrown by the question."
    samantha.say "[mike.name], Ryan and I lived together for long time, [hero.name]."
    samantha.say "And I think it's fair to say the three of us were close friends back then."
    samantha.say "Hell, I'd like to think that we still are."
    samantha.say "The house was a fun place to live because we were so close."
    bree.say "Hmm..."
    bree.say "You said it 'was' a fun place."
    bree.say "So I guess it stopped being fun at some point?"
    show samantha sad
    "Sam lets out a sigh, and her expression becomes a little sad."
    "But she nods her head all the same, committed to telling the whole story."
    samantha.say "Things changed when I found out that Ryan had feelings for me."
    samantha.say "You know - romantic feelings?"
    "I nod, trying to resist the urge to press Sam for more details."
    "If I push her too hard, she might clam up and leave me hanging here!"
    samantha.say "I was confused at first."
    samantha.say "Because I always had a suspicion that it was [mike.name] who felt like that."
    samantha.say "That he'd be the one to make a move on me."
    bree.say "But you're with Ryan now, right?"
    show samantha normal
    "Sam shakes her head, as if reminding herself of the fact."
    samantha.say "Oh yeah..."
    samantha.say "And I love the guy."
    samantha.say "Believe me, we couldn't be happier!"
    samantha.say "But once we got together, [mike.name]..."
    samantha.say "He...well, he kinda changed."
    bree.say "What happened, Sam?"
    samantha.say "I always hoped that we could still be friends, yeah?"
    "I nod and smile at this, trying to look supportive."
    "But at the same time I'm amazed she could even think that'd happen!"
    show samantha sad
    samantha.say "But [mike.name] started becoming distant from us both."
    samantha.say "It was like he was cold with us all the time."
    samantha.say "And then I figured it out."
    samantha.say "[mike.name] wasn't jealous of Ryan for being with me."
    samantha.say "He was jealous of me for being with Ryan!"
    "I blink in confusion."
    "And then I shake my head."
    bree.say "Huh?"
    bree.say "Isn't that the same thing?"
    show samantha normal
    "Sam chuckles and shakes her head."
    "And the gesture makes me feel like a dumb little kid."
    samantha.say "Oh, [hero.name]!"
    samantha.say "Don't you see?"
    samantha.say "[mike.name] was never in love with me."
    samantha.say "He was in love with Ryan!"
    bree.say "But, but, but..."
    bree.say "Ryan's a boy..."
    bree.say "So that would mean..."
    samantha.say "That [mike.name]'s gay."
    samantha.say "What else could it mean, [hero.name]?"
    "I stare at Sam, my eyes wide with surprise."
    "Don't get me wrong, I'm not upset at the idea of [mike.name] being gay."
    "I'm just amazed that I didn't see it coming myself."
    "I...I guess I just never picked up any of the signals."
    "But then Sam has known him a lot longer than me..."
    show samantha sad
    samantha.say "So you can see how all of this would be hard for him?"
    "Sam's question snaps me back to reality."
    bree.say "Hard for him?"
    samantha.say "Yeah, [hero.name] - hard on [mike.name]."
    samantha.say "His two best friends got together and moved out."
    samantha.say "Plus he lost out on the guy he's in love with."
    bree.say "Oh...yeah..."
    bree.say "That would be tough to handle."
    "Sam nods, but then puts on a smile."
    show samantha happy
    samantha.say "But now things should be looking up for [mike.name]."
    samantha.say "Because he has two brand new housemates to look after him."
    samantha.say "Doesn't he?"
    show samantha normal
    "Now it's my turn to nod and smile."
    "But to be honest, I don't feel like I have a choice."
    "On the one hand I feel a lot of sympathy for [mike.name]."
    "But on the other I kind of feel like Sam's loading all her guilt onto me."
    "She gets to go home to Ryan and play happy families together."
    "While I have to go back to the house and look after poor old [mike.name]!"
    bree.say "I'll do all I can to look out for him, Sam."
    bree.say "Don't worry about that."
    "Sam takes hold of my hand and gives it a squeeze."
    samantha.say "Thank you, [hero.name]."
    samantha.say "I just knew you were the right choice to move into the house."
    samantha.say "Now if there's anything you need, just get in touch, okay?"
    samantha.say "But now I have to fly - Ryan's taking me out for dinner!"
    hide samantha
    show samantha
    pause 0.2
    hide samantha with moveoutright
    "I keep the smile on my face until Sam's out of the door."
    "And once she's gone I frown as I sink down into my seat."
    "I thought I was just moving into a shared house."
    "But now it feels like I signed up to be [mike.name]'s carer or something!"
    return


label mike_female_event_03b:
    scene bg kitchen
    "I can't seem to get over what Sam told me about [mike.name] being gay, no matter how hard I try."
    "Like I said before, it's not that I have a problem with it, I'm just surprised, that's all."
    "I thought that I was pretty good at picking up on the subtle hints that a guy likes guys."
    "But if Sam's right, then [mike.name] managed to fly right under my radar!"
    "Now I can't help studying him every time he walks into the room."
    "All the time I'm trying to spot the hints that I must have missed before."
    "Like right now, I'm sitting in the kitchen, just minding my business."
    show mike casual down at right with moveinright
    "Then [mike.name] happens to walk in, and instantly I'm sizing up his every move."
    show mike normal at right4 with move
    mike.say "Hey, [hero.name]..."
    mike.say "What are you doing?"
    "I smile at him, trying to look innocent."
    bree.say "Oh, nothing much..."
    bree.say "I was just staring at my phone, that's all."
    "I might have a bland smile on my face."
    "But inside my head it's a different story."
    "In there it's like how that killer robot from the future sees things."
    "You know the movie I mean, right?"
    "'Killer Robot from the Future', I think it was called..."
    "It's like I'm analysing [mike.name] from every angle possible."
    "And at the same time, my brain is processing all the information I can gather."
    show mike at left5 with move
    mike.say "I'm feeling a little hungry, [hero.name]."
    mike.say "You mind if I knock myself up something to eat?"
    "Hmm..."
    "He's well-spoken and pretty polite."
    "But then there are some rare examples of straight guys that have manners too."
    bree.say "Of course, [mike.name]."
    bree.say "No problem at all."
    show mike down at right5 with move
    "I watch as [mike.name] walks over to the stove and starts gathering ingredients."
    "And I can't help noticing that he's looking like he picked his outfit with care."
    "I mean, yeah, gay guys are supposed to be sharp-dressers."
    "But he could just have a gay friend that gives him pointers in that department."
    show mike normal at right4 with move
    mike.say "Oh, [hero.name]..."
    "I look up as [mike.name] turns to address me."
    mike.say "Where are my manners!"
    mike.say "I was going to whip up an omelette."
    mike.say "But I should have asked if you wanted one too."
    mike.say "So how about it?"
    "Oh, and he's also thoughtful too!"
    "And able to admit that he's made a mistake."
    "Both of which aren't things you often see in the average straight guy."
    bree.say "Erm..."
    bree.say "Okay, [mike.name]..."
    bree.say "That sounds quite nice."
    show mike down at right5 with move
    "It doesn't take long for [mike.name] to knock up the omelettes."
    "And while he dishes them up, I consider a few more points."
    "I know that he studies, which means that he's well-educated."
    "And he looks after his body by working out at the gym."
    "Both of those should be ticks in the gay column."
    "But then he does follow competitive sports too."
    "And he spends a lot of time playing videogames."
    "So there's two ticks for the straight column too!"
    if mike.flags.cried:
        "Ah, but he did cry when we were watching the romcom the other night."
        "And I'm pretty sure that wasn't because he was bored to tears either!"
    "Lost in thought, I fork some of the omelette into my mouth."
    bree.say "Oh..."
    bree.say "Oh my god!"
    show mike normal at center with move
    "[mike.name] looks up, concern written all over his face."
    mike.say "[hero.name]!"
    mike.say "What's the matter?"
    bree.say "The omelette..."
    bree.say "It's frikin amazing!"
    show mike blush
    "[mike.name] looks relieved at first, then a little embarrassed."
    mike.say "Oh...thanks, [hero.name]."
    mike.say "It's just a little something I made up myself."
    mike.say "It kind of became my go-to meal in college!"
    show mike normal
    "I smile as I shovel more of the delicious omelette into my mouth."
    "So he's an excellent cook, which straight guys aren't."
    "But he's also kind of humble with it, which gay guys aren't."
    "Damn it - one thing keeps cancelling out the other!"
    "What I need is a fool-proof test."
    "Something that'll answer the question beyond any doubt."
    "But what kind of test would that be?"
    menu:
        "Try to get [mike.name]'s attention with my body":
            "Well, there's always one sure way to see if a guy's into girls."
            "Because the ones that are can't help staring at the female body!"
            "Making sure as much is on show as possible, I lean across the table."
            bree.say "Oh, [mike.name]..."
            bree.say "This top I have on..."
            bree.say "Do you think it's too tight?"
            bree.say "You know, does it show off too much cleavage?"
            if hero.charm >= 20:
                show mike blush
                "[mike.name]'s eyes go wide, and I swear I see his pupils dilate too!"
                "His mouth opens and he makes a strange kind of groaning sound."
                "And then he finally seems to remember how to speak."
                mike.say "N...no...[hero.name]!"
                mike.say "Not at all!"
                mike.say "That's just the right sized breast...I...I mean vest!"
                "Hmm...so he likes my boobs."
                "That has to mean he's more likely to be straight, right?"
            else:
                show mike down
                "[mike.name] makes a kind of harrumphing noise and looks away."
                mike.say "Maybe that's something you should ask Sasha, yeah?"
                mike.say "And also, make sure it's not while she's eating, [hero.name]!"
                "Okay, so he wouldn't stare at my breasts."
                "But that could just be because he thinks it's inappropriate."
                "Mental note - apparently flashing your boobs at the dinner table is rude."
        "Quizz [mike.name] about his musical tastes":
            "Wait a minute - what about music?"
            "That's somewhere straight and gay guys are miles apart, right?"
            bree.say "I was meaning to ask, [mike.name]..."
            bree.say "What kind of music are you into?"
            bree.say "I mean, do you like musicals and stuff like Elton John?"
            bree.say "Or are you more of a rock guy?"
            bree.say "Maybe even heavy metal?"
            if hero.knowledge >= 20:
                "[mike.name] looks thoughtful at the question."
                "He swallows a mouthful of omelette, and then replies."
                mike.say "I guess I like all different kinds of music, [hero.name]."
                mike.say "A little bit of this and a little bit of that."
                mike.say "My tastes are kind of eclectic."
                "Arrgh...not the old 'I like a bit of everything' answer!"
                "That doesn't tell me anything."
                "Well, apart from maybe that [mike.name] has no taste in music whatsoever..."
            else:
                "[mike.name] shakes his head at the question, frowning a little."
                "He swallows a mouthful of omelette, and then replies."
                mike.say "[hero.name]..."
                mike.say "Do you have to quiz me while I'm eating?"
                mike.say "It's kind of bad for the digestion!"
                "Hmm...all that tells me is that he's got better manners than I do."
                "Which doesn't answer any of my questions."
        "Quizz [mike.name] about his fitness regimen":
            "Okay, okay..."
            "Think, [hero.name], think!"
            "I know that [mike.name] works out."
            "But what parts of his body does he put all the effort into?"
            "Straight guys are all about looking buff."
            "So they're into pumping up their arms and chests."
            "But gay guys know how important it is to have a tight ass."
            "So they focus on stuff like that."
            if hero.fitness >= 20:
                bree.say "Hey, [mike.name]..."
                bree.say "I'm wanting to find a gym around here."
                bree.say "And I've seen a couple that are pretty close."
                bree.say "But I need one where I can work on my arms and my thighs too."
                bree.say "Where do you go?"
                "[mike.name] looks thoughtful for a moment."
                "And then he answers my question."
                mike.say "Hmm..."
                mike.say "I know what you mean, [hero.name]."
                mike.say "I like to work on both of those areas too."
                mike.say "Good thing is that at my gym you can get a good workout in both places."
                mike.say "Don't worry, I'll get you the address as soon as I have a free second."
                "Damn it!"
                "He answered the question, but didn't tell me anything."
                "So he works on his biceps and his butt!"
                "Does that mean he swings both ways?!?"
            else:
                bree.say "Hey, [mike.name]..."
                bree.say "When you're at the gym, yeah?"
                bree.say "Do you work on your biceps or your butt?"
                "[mike.name] looks at me sideways, frowning at the question."
                mike.say "That's a little personal, don't you think?"
                mike.say "How would you feel if I asked you about your butt, [hero.name]?"
                "I nod and look away, already feeling my cheeks flush red."
    show sasha at right with moveinright
    sasha.say "Hey guys..."
    sasha.say "Mmm!"
    sasha.say "Something smells good!"
    "Our conversation is interrupted as Sasha breezes into the room."
    "For a moment I think that she might be able to help me with my investigation."
    "But then I take a second look at her and remember something important."
    "Sasha's one of those girls that doesn't dress in a very feminine way."
    "And when you add that to the fact that she's pretty flat-chested..."
    "Well...she's hardly going to get [mike.name]'s motor going, is she?"
    bree.say "Hey, Sasha..."
    bree.say "[mike.name] and I were just..."
    mike.say "Hi, Sasha!"
    mike.say "You look pretty awesome today!"
    "I stare at [mike.name] in sheer amazement as he cuts me off and talks right over me."
    "And I can see that his eyes are wider than ever as he pretty much ogles her."
    sasha.say "You think, [mike.name]?"
    sasha.say "Huh...I just threw on what I'm wearing, you know?"
    mike.say "You still look good, Sasha!"
    show sasha happy
    "Sasha laughs and shakes her head."
    sasha.say "Whatever, [mike.name], whatever..."
    sasha.say "I gotta run, okay?"
    hide sasha with moveoutright
    "[mike.name] and I nod as Sasha hurries out of the room."
    "And even after she's gone, I keep on staring at [mike.name]."
    "Did he just give me a blatant clue right there?"
    "I mean, Sasha's pretty boyish, isn't she?"
    "So maybe he does like guys after all."
    return

label mike_female_event_04:
    if mike.love.max < 50:
        $ mike.love.max = 50
    $ hero.replace_activity()
    show tv breemc mike
    "I flip through the channels with a glazed look over my eyes, snacking on popcorn one-by-one. The flavor of the butter is nostalgic from when I'd have family movie night."
    bree.say "No... no... no... boringgg..."
    "A movie I recognize is on."
    bree.say "OH WAIT! Is this what I think it is?"
    "It's 'There's Something Regarding Mary'. I haven't seen it in a long time but I remember laughing at it until my sides hurt... and I think Dan Steeler and Cami Daya are great actors."
    "Oh, and we're lucky! It's just beginning. It's the pre-prom scene where Tod gets his frank and beans stuck in the zipper. Classic."
    bree.say "HA!"
    "I fill up the room with laughter. It's just as funny as I remember."
    "[mike.name] laughs along, clutching at his knee and leaning forward."
    mike.say "Hahaha! Oh, I love this movie. I haven't seen it in a few years."
    bree.say "Yeah, me too. I used to watch it a lot growing up."
    "We watch while chatting about some scenes we enjoyed as kids and how they hold up to us now."
    "The scene where the dog attacks Tod begins. Neither of us can hold our laughter in the moment the dog flies out the window and we both start to tear up."
    "We continue watching the movie once our sides come back down from orbit."
    "A commercial break comes on. [mike.name] gets up to go get some more water."
    "When he returns, he sits down beside me again, a little closer than before. Probably on accident. I noticed but I didn't show any signs that I did."
    "I turn my attention back to the TV. Tod is whacking off before his big date with Mary. Just prior, his friend advised him to masturbate before his date in order to think clearly. He loses his cum, it lands on his ear, and she mistakes his jizz for hair gel."
    bree.say "Is that shit really true?"
    mike.say "Is what?"
    bree.say "What Tod's friend was saying about the baby gravy making men unable to think straight. Does jerking it before dates actually work?"
    mike.say "..."
    "[mike.name] gives me an awkward look, like he doesn't know how to take what I just asked, or rather, like he completely didn't expect it."
    bree.say "Actually, sorry, that's totally weird and overly personal. Boundaries crossed. Never mind. I'll shut up now. Right now."
    mike.say "Haha no, I just thought it was a strange thing to ask your roommate. Are you trying to hint that you're into me or something?"
    "I scoff and roll my eyes."
    bree.say "As if!"
    "I try my best to laugh it off."
    mike.say "Anyways, to answer your question, yes... that is definitely a thing. Everything else gets kind of pushed out of your brain and it only clears up after you come. It's weird."
    bree.say "Huh. I always thought the whole 'post-nut clarity' thing was a meme."
    mike.say "Nope, it definitely exists."
    bree.say "Interesting."
    "[mike.name] chews on his lip, nods, and falls silent, focusing his attention back onto the movie. I let him handle his light embarrassment on his own, but I giggle to myself and shake my head."
    "Finally, Tod tells Mary how he really feels. He realizes that the other men chasing Mary don't really love her and he realizes it's probably the same for him so he gives up on her."
    "I feel [mike.name] shift positions on the couch next to me. I glance over at him to find him staring intently at the screen with a look on his face I've only seen from other women. Appreciation?"
    "After Tod leaves, Mary runs after him and tells him she loves him after all."
    "I glance over at [mike.name]. He's got a cute dopey smile on his face."
    bree.say "I had no idea you were such a sap, [mike.name]."
    "I tease him...maybe a little too roughly. He seems really invested in what's happening on the TV."
    "[mike.name] rolls his eyes, chuckles, and bites back."
    mike.say "Fuck off, [hero.name]."
    "His eyes fall to the floor."
    mike.say "After all... he's got a point. Sometimes people just don't really love you. They sometimes only care about what they get from you. Like money, validation... or real emotions that they don't return. People use you for what you can give. There's no reciprocation."
    "I wasn't prepared for the mood to get so heavy. I struggle to say something appropriate, but decide to listen instead."
    mike.say "Your best isn't always enough. It's a hard pill to swallow. I guess that's why I..."
    "He trails off. I pry a little bit."
    bree.say "Why you what?"
    mike.say "Oh, right...why I like..."
    "I almost can't stand the way he hesitates. I hold back the urge to tell him to just spit it out. [mike.name] heaves out a long, tired sigh as if he knows how I'll react."
    mike.say "...Romance books, romcoms, weddings. You know, girly shit. It gives me hope."
    bree.say "Hope? That's really different."
    mike.say "That even though my best isn't enough for some people, it'll be enough for the right person. When I find them."
    "We spend a few seconds in silence."
    "I get the feeling [mike.name] is a bit self-conscious about this. I fill my mouth with a few kernels of popcorn so I don't say something stupid."
    mike.say "Ugh, this was embarrassing. Can you just forget I said anything?"
    bree.say "No! I--"
    mike.say "You don't have to say it. I know I'm an idiot."
    bree.say "Don't cut me off. That's rude. What I was GOING to say was that I don't know what happened to make you feel this way or whatever, but yeah, I definitely think there's someone for everyone. So you know, don't get discouraged and shit."
    mike.say "..."
    bree.say "..."
    mike.say "..."
    bree.say "...WHAT!?"
    "I raised my voice on accident. Silences like these make me a bit nervous. Oops."
    mike.say "Jesus, keep it down."
    bree.say "Sorry, I got nervous."
    mike.say "Nervous?"
    bree.say "Yeah, long pauses make me feel weird. Like I said something totally off-base and the person next to me is just inwardly cringing and judging me. I can't stand them."
    mike.say "Oh, no, I- well... thanks, I think. I appreciate it."
    "Ah, he's very self-conscious."
    bree.say "Yeah, well, don't get used to it. I charge for therapy you know."
    mike.say "What's the charge, Dr. [hero.name]?"
    bree.say "One popcorn kernel."
    mike.say "Alright."
    hide tv bree mike
    show mike
    "[mike.name] stands up, taking the popcorn bowl with him."
    bree.say "Bitch you better get back here with that."
    mike.say "Catch!"
    "And he throws a kernel at me."
    "It hits my nose."
    bree.say "GAH! I THINK IT'S BROKEN! No more therapy for you."
    mike.say "Oh, heck, no wait, let's try again. Ready?"
    bree.say "Aaaaahhhhhh!"
    "I open my mouth comically wide."
    "He tosses another kernel."
    "I lean back to catch it as it arcs towards me. I get it, but I fall over. Fwumpf. The couch catches me."
    mike.say "Beautiful dive. Ten out of ten. Gold medal, even."
    bree.say "Yes, yes I know, I know."
    "I try to bow a bit from my defeated position."
    "[mike.name] claps."
    "Buzz! Buzz! [mike.name] retrieves his phone from his pocket."
    mike.say "Shit, it's getting late. I need to say good night. I have work in the morning."
    "He begins tidying up and I rise to help him."
    bree.say "Sure, thanks for staying up with me. I had fun."
    mike.say "See you another time."
    bree.say "Yeah, see you. Good night!"
    mike.say "Good night, [hero.name]."
    $ mike.flags.delay = TemporaryFlag(True, 1)
    return

label mike_female_event_05a:
    if mike.love.max < 60:
        $ mike.love.max = 60
    scene bg cinema
    "It always seems weird to me when people say they can't imagine going to the movies on their own."
    "Because that's one of the things that I've always loved doing, sneaking off to the cinema all alone."
    "Yeah, I know - this is the twenty-first century, and you can stream all that stuff at home."
    "And yeah, the tickets are a stupid price, not to mention the insane cost of a tub of popcorn!"
    "But there's still something special about sitting down in a theatre and watching a film on the big screen."
    "Tonight's just one of those nights when I've got the urge and I can't resist it."
    "So I've slipped out of the house and come to the cinema to catch a late showing."
    "It doesn't really matter what I get to see, just that I see something."
    "And that's how I find myself staring at the posters in the lobby."
    "I'm literally planning on buying a ticket for the first film that takes my fancy."
    "But that's when I hear a familiar voice."
    mike.say "No way, Morgan!"
    mike.say "The first one was awful, remember?"
    mike.say "So there's no way I want to see the sequel!"
    "Recognising [mike.name]'s voice, I spin around."
    "At the same time my eyes are hunting for him too."
    show mike at right5 with dissolve
    "I spot him on the other side of the lobby, his back turned to me."
    "I'm about to shout to him and walk over there, but then I freeze."
    "And that's because I see who he's talking to."
    show morgan at top_mostright with dissolve
    morgan.say "Yeah, yeah, I know."
    morgan.say "But how many sci-fi movies that sucked had a better sequel, [mike.name]?"
    morgan.say "Exterminator 2 was way better than the original."
    morgan.say "And Extraterrestrials is in another league above Extraterrestrial!"
    "I look around for a place to hide, and find a spot where I'm sure they won't see me."
    "And then I lean forwards, trying as best I can to listen in on their conversation."
    "Okay, okay...I know how it looks."
    "But hear me out, yeah?"
    "The girl that [mike.name]'s with, the one called Morgan."
    "She's not exactly the traditional picture of femininity."
    "I mean, she makes Sasha look like the girliest of girly girls!"
    "That doesn't mean she's not pretty, in a kind of boyish way..."
    "But she's definitely got some serious masculine overtones about her."
    show mike happy
    show morgan happy
    "And there's something else too, something about the way they're talking."
    "It's the kind of banter that you can only get between really good friends."
    "The kind of friends that are totally comfortable in each other's company."
    "[mike.name] and Morgan are disagreeing one moment, then laughing and joking the next."
    "It's...well, it's like two guys that are the best of buddies!"
    "They're even leaning in close enough to touch most of the time."
    "And more than once one of them has a hand on the other."
    "They're just touching a shoulder or squeezing an arm."
    "But I know that if I touched [mike.name] like that he'd jump out of his skin!"
    "That's not the point though, is it?"
    "I'm not watching them out of jealousy, am I?"
    "No, no...I'm watching them because I'm trying to figure [mike.name] out."
    "And I can't help thinking this might be more evidence of the way he swings!"
    "Just then, [mike.name] and Morgan seem to make up their minds and choose a film."
    hide morgan
    hide mike
    with moveoutright
    "Luckily they don't see me as they hurry to the box office."
    "And I take the chance to slip away and get the hell out of the cinema."
    "I know that I was supposed to be seeing a film myself."
    "But now that plan's been blown out of the water."
    "My head's so full of speculation that I doubt I could concentrate on a movie."
    "And the last thing I want is to bump into them when our films turn out."
    "Instead I hurry back home, trying to figure out what all of this means."
    $ mike.flags.delay = TemporaryFlag(True, 1)
    return

label mike_female_event_05b:
    if mike.love.max < 60:
        $ mike.love.max = 60
    "It's not that the house has walls thinner than you'd expect."
    "More that the sound I can hear is crazily loud."
    "And it's not hard to tell what it is either."
    "Two voices raised in anger - that can only mean one thing."
    "There's a row going on somewhere in the house right now."
    "And it can only be between Sasha and [mike.name]!"
    "Part of me thinks that I should find them and intervene."
    "That's what a good housemate would do, I guess?"
    "But it's also what a really brave and assertive housemate would do too."
    "And right now, that's not me!"
    "The last thing I want is to be caught in the middle of their fight."
    "And who knows - I could end up making things worse by getting involved."
    "So yeah, I'm not proud to admit it, but I hide away until the arguing stops."
    scene bg livingroom
    "Once the sound of voices has faded away, I sneak out again."
    "I'm looking this way and that, afraid of bumping into Sasha or [mike.name]."
    "So when I see someone come storming out of a doorway, I leap backwards."
    "Luckily for me this just means I flatten myself against the wall."
    "It's also lucky they don't see or hear me."
    "But I guess they're still too pissed from the argument to notice anything else."
    "At first I think that it's Sasha I'm looking at."
    "The black clothes and ripped tights are usually a dead giveaway."
    show mike crossdress at right, dark with moveinright
    "But then I see that the person's way too tall and well built to be Sasha."
    "Huh...I guess it could be another member of that band she's in."
    "I haven't met any of Sasha's bandmates yet, so it seems likely."
    "I think that I solved the puzzle until the tall girl turns her head a little."
    "It's just enough for me to see her face in profile."
    "And what I see makes me gasp in surprise."
    hide mike
    show mike crossdress angry at right
    show mike crossdress angry at center with move
    "That's not a girl at all."
    "It's a guy dressed in girl's clothes!"
    "And...oh my!"
    "It's not just any guy, either."
    "That's [mike.name]!"
    "For a moment I'm worried that he's heard the sound of me gasping."
    "So I press myself harder against the wall."
    "As if it'll make a difference - which it won't!"
    show mike crossdress angry at left with move
    "[mike.name] looks pretty pissed right now, like he's still angry from the argument."
    "The last thing that I want is to have to talk to him while he's mad and in drag!"
    "But a moment later he shakes his head and hurries off."
    hide mike with moveoutleft
    "Which leaves me to slink back to my room, keeping as quiet as I can along the way."
    "I'm feeling like I need to spend some time lying down."
    "Because what I just saw was kind of hard to process."
    "I mean, I was struggling with the idea that I didn't notice [mike.name] was gay."
    "But I could never have imagined that he might be a transvestite too!"
    $ mike.flags.delay = TemporaryFlag(True, 1)
    return

label mike_female_event_05c:
    if mike.love.max < 60:
        $ mike.love.max = 60
    scene bg pub
    "I was kind of distracted the first time I went to the local pub, what with meeting Sam and all."
    "But I got a really good vibe from the place all the same, and I find myself wanting to go back."
    "So the first chance I get, I decide to head down there and grab a drink."
    "I figure that I deserve it, after all this trying to get a handle on [mike.name] and the way he swings."
    "The problem is that I haven't been in there more than a couple of minutes when I recognise someone."
    show ryan smile with dissolve
    "It's Ryan, Sam's partner and [mike.name]'s former housemate, maybe even former friend too."
    "I'm not feeling up to talking, so I do the best I can to avoid being seen."
    ryan.say "Hey there..."
    ryan.say "It's [hero.name], isn't it?"
    ryan.say "Yeah...I thought it was you!"
    "Ah shit - busted!"
    "I turn around, forcing a smile onto my face."
    bree.say "Oh..."
    bree.say "Hi, Ryan!"
    bree.say "Fancy seeing you here."
    "Ryan lets out a laugh that sounds more than a little fake to me."
    "And he shakes his head like I just said something really dumb too."
    ryan.say "And why would that be, [hero.name]?"
    ryan.say "I did used to live around here, remember?"
    ryan.say "This was my local back then too!"
    "I'm still holding my smile and nodding."
    "It's weird, but I'm not reading Ryan the same way I was before."
    "Maybe it's because of all the details I've had filled in since then."
    "But now the charm he turned on the first time I met him seems a little false."
    "Ah, maybe that's just me being sympathetic towards [mike.name]."
    "I should really give this guy the benefit of the doubt."
    bree.say "I guess so, Ryan."
    "I look around the pub and then back at Ryan."
    bree.say "Is Sam not with you?"
    bree.say "I wouldn't mind chatting to her if she is..."
    "I'm surprised at how quickly Ryan reacts to this."
    show ryan annoyed
    "It's almost like he's cutting me off and shutting me down."
    ryan.say "Oh no, [hero.name], she's not here."
    ryan.say "We're engaged - not joined at the hip!"
    "I shrug, deciding to let it drop."
    "But then it occurs to me that I should ask Ryan about [mike.name]."
    "Hearing his version of the story might help to straighten things out."
    bree.say "Sam was telling me all about the three of you."
    bree.say "How close you were to [mike.name]?"
    bree.say "Well...before what went down..."
    "At the mere mention of [mike.name]'s name, Ryan rolls his eyes and groans."
    show ryan smile
    ryan.say "Urgh..."
    ryan.say "To be honest, [hero.name], I'm tired of talking about the whole thing."
    ryan.say "I mean, I like the guy."
    ryan.say "But he's kind of a loser, yeah?"
    "I can't hide my surprise at what Ryan just said."
    "I thought Sam said they were all friends?"
    bree.say "You really think he's a loser?"
    ryan.say "Look at the evidence, [hero.name]!"
    ryan.say "He's hopeless when it comes to relationships."
    ryan.say "And that job of his - what does he even do?"
    ryan.say "When he describes it, people fall asleep!"
    bree.say "Oh...I see."
    bree.say "It doesn't sound like you have a lot in common."
    show ryan annoyed
    ryan.say "You know how it is, [hero.name]."
    ryan.say "I tried to pull [mike.name] up with me."
    show ryan smile
    ryan.say "But all that did was make him jealous of my own success!"
    "I can't help frowning at Ryan's account of how things went down."
    "I mean, is this guy for real?"
    "He makes it sound like [mike.name]'s just some bitter little nerd!"
    "I'm still stewing on that thought when Ryan leans in closer."
    "Now the smile on his face has turned distinctly sleazy."
    "And he surprises me again by reaching out and touching my hair."
    "He twines a lock of it around his fingers."
    "That is until I take a step backwards."
    show ryan annoyed
    ryan.say "Hey..."
    ryan.say "Where are you going, [hero.name]?"
    ryan.say "We're not done talking!"
    bree.say "We're not?"
    show ryan smile
    ryan.say "No way!"
    show ryan angry
    ryan.say "I'm done talking about losers like [mike.name]."
    show ryan smile
    ryan.say "What I want to do is talk about you!"
    "Ryan follows me as I take a few more steps backwards."
    "And I don't need to be told what he has in mind either!"
    menu:
        "Tell Ryan off politely":
            "I put as sweet of a smile on my face as I can possibly manage."
            "But at the same time I hold up a hand, stopping Ryan's advance."
            bree.say "I'm sorry, Ryan."
            bree.say "But I think there's been some kind of misunderstanding here."
            bree.say "You and I are acquaintances at best, not even really friends."
            bree.say "And this is a level of intimacy that I'm not comfortable with."
            show ryan annoyed
            "Ryan seems to be more surprised by the assertive tone of my voice than anything."
            "He stops and blinks, the looks around the pub like he sees it for the first time."
            bree.say "Oh yes, this IS your local - isn't it?"
            bree.say "And I suppose a lot of these people know you AND Sam, right?"
            bree.say "So we wouldn't want them to get the wrong idea, would we?"
            ryan.say "Ah..."
            ryan.say "Maybe you're right, [hero.name]..."
            ryan.say "Come to think of it...I should really get going!"
            $ hero.morality += 1
        "Tell Ryan off fiercely":
            "I put a wry smile on my face and raise an eyebrow."
            "And I hold up a hand, stopping Ryan's advance."
            bree.say "You can stop right there, Ryan!"
            bree.say "Look, I don't know what bullshit you sold to Sam."
            bree.say "But it won't work on me, okay?"
            show ryan annoyed
            "Ryan seems to be more surprised by the assertive tone of my voice than anything."
            "He stops and blinks, clearly rethinking his actions."
            show ryan smile
            ryan.say "[hero.name]..."
            ryan.say "I think we got off on the wrong foot here!"
            bree.say "Nah, Ryan..."
            bree.say "I think both my feet are firmly on the ground right now."
            bree.say "And it's pretty clear that no woman's ever going to be good enough for you."
            bree.say "So why don't you do all of us girls a favour, and go fuck yourself?"
            show ryan angry
            ryan.say "Ah..."
            ryan.say "You know what, [hero.name]..."
            show ryan annoyed
            ryan.say "I should really get going!"
            $ hero.morality -= 1
        "Remind Ryan about Samantha":
            "I put as sweet of a smile on my face as I can possibly manage."
            "But at the same time I hold up a hand, stopping Ryan's advance."
            bree.say "I meant to ask, Ryan..."
            bree.say "How is Sam doing since I saw her last?"
            show ryan annoyed
            "Ryan seems to be more surprised by the assertive tone of my voice than anything."
            "He stops and blinks, clearly rethinking his actions."
            ryan.say "Wh...what are you talking about, [hero.name]?"
            ryan.say "What's she got to do with this?"
            bree.say "I was meaning to call her up."
            bree.say "You know that we swapped numbers, yeah?"
            bree.say "Maybe I should just call her up right now and have that conversation?"
            bree.say "And I can ask her how what you're doing right now means for your engagement, yeah?"
            ryan.say "Ah..."
            ryan.say "You know what, [hero.name]..."
            ryan.say "I should really get going!"
    "I watch, shaking my head, as Ryan beats a hasty retreat."
    hide ryan with dissolve
    "What a total and utter scumbag!"
    "I wonder if Sam knows what he gets up to behind her back?"
    "And you know what - it's making me rethink a lot of stuff."
    "Not least Sam's insisting that [mike.name]'s in love with Ryan."
    "Sure, he might well be gay."
    "But how could he fall for a douche like that?!?"
    $ mike.flags.delay = TemporaryFlag(True, 1)
    return

label mike_female_event_05d:
    "I've been going over the [mike.name] issue in my head for what feels like forever."
    "And it just doesn't feel like there's any way I can solve it on my own."
    show mike down with dissolve
    "So I decide what I need to do is confront [mike.name] and let him know what I think."
    "Sure, it might go badly, blow up in my face or something like that."
    "But I need to get it out in the open before it drives me insane!"
    bree.say "Erm..."
    bree.say "[mike.name]..."
    show mike normal
    "[mike.name] looks up at the sound of my voice."
    mike.say "Oh..."
    mike.say "Hey, [hero.name]!"
    "He seems to notice the look on my face a moment later."
    "And his own expression turns worried as a result."
    mike.say "Are you okay, [hero.name]?"
    mike.say "You look like you've got the weight of the world on your shoulders!"
    bree.say "Yeah, you could say that."
    bree.say "Look...I need to talk to you about something, okay?"
    "[mike.name] nods."
    mike.say "Okay, [hero.name]."
    mike.say "I'm listening."
    "I force a smile onto my face."
    "Then I take a deep breath."
    "And I say what I have to say..."
    menu:
        "Tell him you know that he is gay":
            "There's no point in beating about the bush."
            "So I just come right out and say it."
            bree.say "Look, [mike.name]..."
            bree.say "I've been talking to Sam and Ryan."
            bree.say "And well...I know all about you being gay."
            bree.say "But I'm okay with it!"
            "For a moment I think that [mike.name]'s staring at me in silence out of sheer amazement."
            "But then he starts shaking his head, like he can't believe what he's hearing."
            mike.say "[hero.name]..."
            mike.say "What are you talking about?"
            bree.say "It's okay, [mike.name]."
            bree.say "You don't have to hide it from me!"
            "[mike.name] shakes his head at this."
            mike.say "I don't know what Sam and Ryan have been telling you, [hero.name]."
            mike.say "But I'm not gay!"
            "Now it's my turn to gape in amazement."
            bree.say "What do you mean you're not gay?!?"
            show mike angry
            mike.say "Exactly that, [hero.name] - I'm not gay!"
            "[mike.name] turns away and mutters under his breath."
            bree.say "I...I'm sorry, [mike.name]!"
            bree.say "Sam's kind of convinced that you are!"
            mike.say "It's okay, [hero.name], it's okay."
            mike.say "I'm not mad at you."
            mike.say "But I think I need to have a serious chat with Sam and Ryan!"
            hide mike with moveoutleft
            "With that, he storms off."
            "Which leaves me alone and feeling more than a little foolish."
            $ mike.love -= 2
        "Tell that you like him a lot no matter who he loves":
            "There's no point in beating about the bush."
            "So I just come right out and say it."
            bree.say "Look, [mike.name]..."
            bree.say "I just wanted to say that I like you a lot."
            bree.say "And that won't change no matter who you fall in love with."
            bree.say "Boy or girl!"
            "For a moment I think that [mike.name]'s staring at me in silence out of sheer amazement."
            "But then he starts shaking his head, and he lets out a peal of laughter."
            show mike happy
            mike.say "Well, thanks for that, [hero.name]!"
            mike.say "That's very modern of you."
            mike.say "But I do kind of only like girls!"
            "Now it's my turn to gape in amazement."
            bree.say "What do you mean you're not gay?!?"
            show mike normal
            mike.say "Exactly that, [hero.name] - I'm not gay!"
            mike.say "Why, did you think I was?"
            bree.say "I...I thought you might be!"
            mike.say "You did?"
            mike.say "Hmm...I guess I should be kind of flattered!"
            mike.say "I thought I was way too rough around the edges to pass for gay!"
            bree.say "I...I'm sorry, [mike.name]!"
            show mike happy
            mike.say "It's okay, [hero.name], it's okay."
            mike.say "I'm not mad at you."
            mike.say "In fact, I think it's kind of funny!"
            "I smile and manage to let out a little chuckle."
            "But I still can't feeling more than a little foolish."
            $ mike.love += 2
        "Tell him to forget Ryan and find his perfect man instead":
            "There's no point in beating about the bush."
            "So I just come right out and say it."
            bree.say "Look, [mike.name]..."
            bree.say "I just wanted to say that I understand being attracted to someone."
            bree.say "But I think that you should forget about Ryan, yeah?"
            bree.say "He's a jerk, and your perfect man is still out there."
            bree.say "You just need to find him."
            "For a moment I think that [mike.name]'s staring at me in silence out of sheer amazement."
            "But then he starts shaking his head, like he can't believe what he's hearing."
            mike.say "[hero.name]..."
            mike.say "What are you talking about?"
            bree.say "It's okay, [mike.name]."
            bree.say "You don't have to hide it from me!"
            "[mike.name] shakes his head at this."
            mike.say "I don't know what you've heard, [hero.name]."
            mike.say "But I'm not gay!"
            mike.say "And even if I was, I'd never be interested in Ryan!"
            "Now it's my turn to gape in amazement."
            bree.say "What do you mean you're not gay?!?"
            bree.say "And you're NOT in love with Ryan?!?"
            mike.say "Right on both counts, [hero.name]!"
            bree.say "I...I'm sorry, [mike.name]!"
            bree.say "That's what Sam told me..."
            mike.say "It's okay, [hero.name], it's okay."
            mike.say "I'm not mad at you."
            mike.say "But I think I need to have a serious chat with Sam!"
            hide mike with moveoutleft
            "With that, he walks off, muttering and shaking his head."
            "Which leaves me alone and feeling more than a little foolish."
    return


label mike_female_event_06:
    if mike.love.max < 80:
        $ mike.love.max = 80
    "The air smells fresh with hints of mowed grass. I start my brisk walk towards the park."
    "I wonder to myself why I'm in such a rush, but I figure I can take a break by looking at the birds once I'm where I want to be...wherever that is."
    "As I near the entrance of the park, I hear an older couple's conversation as they pass me."
    "Old Woman" "My, but wasn't that young gentleman playing the guitar so well?"
    "Old Man" "I haven't heard playing like that since Jimmy Hendrick's concert back in 1969."
    "Old Woman" "Haha! We were wild back then, weren't we?"
    "Old Man" "I was always wild for you, my rose."
    "I smile to myself. What a cute older couple, I muse, thinking about whether or not I'd ever find someone like that, too."
    "Looking up, I find myself in an unfamiliar area. I must have taken a turn off of the main path without having realized."
    "After the initial panicked thought of 'Where the fuck am I', I continue in the direction I'm already headed."
    "I mutter under my breath."
    bree.say "Well, this path has to loop around or go straight through the park so it's not like I'm totally lost."
    bree.say "Besides, I've never been in this part before, so may as well enjoy the adventure."
    "I loop around into a sight I recognize."
    "The park's main playground seems so far away... how long did I walk for without paying attention?"
    "I hear the pleasant starting strums of a song from a guitar."
    show mike casual with dissolve
    "Following the source, I find myself standing in front of [mike.name]."
    bree.say "[mike.name]! Hello!"
    show mike happy
    "[mike.name]'s eyebrows rise in clear surprise, lowering his guitar and putting his hand on the strings to stop the sound quickly."
    mike.say "[hero.name], h-hey!"
    bree.say "I heard an adorable older couple talking about how well a young gentleman played a guitar."
    "It looks like I found him! How about a song?"
    show mike normal
    mike.say "Oh, no, I couldn't, I haven't practiced in a while... I'm not ready to perform!"
    bree.say "Stage fright? I get it. It's okay, I won't push you into it."
    mike.say "Thanks, [hero.name]."
    "I didn't want to create an awkward moment, so I tried to change the subject."
    "Maybe when he's practiced a bit more, he'll play for me."
    "Or maybe he'll play for me if we just get to know each other a bit more."
    bree.say "I left the house a little while ago because it was really quiet without hearing the crashing of skillets. When did you get here?"
    mike.say "Ha ha, very funny. I got here about an hour or two ago? I can't really remember...time flies when I'm practicing."
    bree.say "Oh, you've been out here for a bit. No wonder people are making such a buzz about your playing."
    show mike happy
    "[mike.name] tries to hide a somewhat sheepish smile."
    "I notice."
    bree.say "I'm also a bit hungry. I haven't eaten yet, so I made an easy meal to have here in the park. Have you had anything?"
    show mike normal
    mike.say "No, but I did bring some food. I just have a sandwich and some juice."
    bree.say "What are you, six? That's an elementary school meal!"
    mike.say "Yeah? Well what did you bring?"
    "I have the same thing...I didn't expect him to call me out. I could make it sound really fancy, though."
    bree.say "Well, I have risen special dough to encompass a slice of roasted turkey bird with some aioli and cheese from the jack of pepper. Additionally, I have brought the liquid extract of a dozen apples."
    show mike happy
    mike.say "That's... damn it, [hero.name], that's just what I brought!"
    "I let out a laugh louder than I meant. Banter with [mike.name] is always really fun."
    bree.say "Ha! I couldn't tell you I'd brought the same thing after giving you a bit of shit though, now could I?"
    "My stomach growls audibly."
    bree.say "U-Uh, anyway, want to eat some food?"
    "[mike.name] shake his head in pretend disbelief, hop off the surface of the picnic table he had perched on, and gesture to the other side."
    mike.say "Sure thing. Let's have these fancy elementary school lunches."
    mike.say "Nothing but the finest for this palate."
    "[mike.name] chuckles and unwraps his sandwich. I follow suit."
    "After a couple of bites, I decide to break the silence."
    bree.say "Speaking of elementary."
    show mike normal
    "I swallow and clear my throat. [mike.name] looks up at me, listening casually."
    bree.say "This one time I fucked up really bad."
    "His expression changes to one of confusion."
    mike.say "How bad could a 6 year old fuck up?"
    bree.say "I was at lunch and was sitting right by my best friend, April. It was burger day - our favorite day. She hated mustard but I loved it. I was having a lot of trouble opening that damn packet. I swear the mustard packets were harder to open than the ketchup's!"
    mike.say "Ok...but where's this going?"
    bree.say "I'm gonna tell you, sheesh! Anyway so she was taking her turn talking and I was listening, still trying to get the mustard open while facing her. I squeezed really hard. Too hard. The packet just...released itself over her, lines of mustard all over. The look on her face..."
    "I start chuckling. [mike.name] stares at me in disbelief."
    bree.say "She was so fuckin' mad at me. She was actually so mad she got up and told the teacher on me. I was shocked! It's not like I did it on purpose! We were best friends and everything!"
    show mike happy
    mike.say "...Wow. So you've just always been clumsy then?"
    bree.say "You're one to talk, Captain Skillet."
    mike.say "Are you ever going to let that one go?"
    bree.say "Not in a million years. Now..."
    "I grab my food and take a bite, uttering my next few words with a face full of turkey sandwich."
    bree.say "Tell me one of your stories."
    show mike normal
    mike.say "Wh--What?! Why should I? You told me yours completely unsolicited, why do I have to tell you one now, just because you told me one?"
    bree.say "Come onnnn, don't you want to actually get along with your roommates? How are you ever going to become friends with me and Sasha if you never open up?"
    mike.say "...Just because I live with you doesn't mean we have to be friends."
    bree.say "But doesn't it make living together that much more fun?!"
    "[mike.name] pauses, thinking, and exhales with exasperation."
    mike.say "Okay, fine. Here's mine. I was like 6 and I loved cartoons when I was growing up. I rushed home every day to watch DragonSphere S. My favorite was Roku. He was the coolest! I wanted to be just like him."
    "Oh no, this is already too funny...I try to stifle a laugh."
    mike.say "One day my school milk cartons had him on the back and a message saying something like, 'Want to be super strong? Drink your milk!' and from then on I legitimately believed that if I drank enough milk I would be able to go Super Duper."
    bree.say "Oh...oh no..."
    mike.say "What?"
    bree.say "That's...BAHAHAHA, THAT'S REALLY CUTE OH MY GOSH."
    "[mike.name]'s cheeks turn reddish and he shoots back defensively."
    mike.say "Yeah well I liked that show, and Roku was my hero!"
    bree.say "No, I totally get you. I loved that show too!"
    mike.say "No shit? Okay...well, I do have one more story."
    bree.say "I'm here. Hit me."
    mike.say "Well, after DragonSphere S, the next show was Luna Pilot."
    "I actually watched an episode or two but once my friend came over unannounced and made fun of me for watching a girls' show so I just brushed it off as like 'oh yeah this was just on after DragonSphere' but I really did want to get into it. I never did though."
    "I stare at him."
    "..."
    "..."
    mike.say "What??"
    bree.say "That's literally my favorite show from childhood. I...LOVE...Luna Pilot. I collect so much merch from it, I honestly wonder how I pay rent sometimes."
    mike.say "Good to know your healthy spending habits, [hero.name]."
    bree.say "It's a hyperbole, butthead."
    "I fire back, rolling my eyes but smiling. He's such a little shit."
    bree.say "So what you're saying is, you wouldn't mind...I don't know, re-watching it? With me?"
    mike.say "Yeah, for sure! And I can tell you all the characters and which episodes are fillers and which have stories. Oh and I can tell you all about the really deep lore...I have all the figures!"
    bree.say "My favorite is Cadet Jupiter! She has the power of lightning and she's honest and kind but also the strongest on the team--"
    show mike happy
    mike.say "Wow you really DO like this show, huh?"
    "Suddenly self-aware after nerding out like that, I shut up really quickly."
    bree.say "Y-Yeah, I do...sorry to like...go off like that."
    mike.say "Hey, I do the same for DSS so no worries. I have a few figures myself."
    "He winks at me to reassure me...but something about him looks incredibly sexy right now...him just being himself, and loving what he loves."
    mike.say "Maybe after Luna Pilot we can watch DSS together too."
    bree.say "It's a deal."
    show mike normal
    "..."
    "We let a moment of silence fill the air. Neither of us want to stop the conversation but we don't want it to drag on, either."
    bree.say "[mike.name]."
    mike.say "Yeah?"
    bree.say "Ah...n-never mind. I...just realized I gotta get back. I'll see you, yeah?"
    "I get up and hurry to gather my belongings, shoving my trash into my tote bag because littering is for assholes."
    show mike happy
    mike.say "Sure. See you at home. It was good talking to you. I'm glad we bumped into each other."
    bree.say "Me too!"
    "I grin widely and wave, while making my way back home."
    bree.say "Okay, bye see you back at home!"
    mike.say "Bye!"
    show mike normal
    "..."
    "[mike.name] pauses to think and wonders aloud to himself."
    mike.say "When did I start to like the idea of us sharing a home together as more than roommates...? Whatever. She's probably not into me. I'll just forget it."
    "[mike.name] turns his attention back to his guitar and strums a melancholy tune that lifts through the air, making even the sunshine seem a little weary with heartbreak despite the beauty of the afternoon."
    $ hero.hunger += 3
    return

label mike_female_event_07:
    if mike.love.max < 100:
        $ mike.love.max = 100
    $ mike.flags.nodate = False
    "I arrive at the university library and notice all the study tables are occupied. Great. Wonder if I can score a private room? Doubtful. I shouldn't even try wasting my time and energy. Instead, I opt to scope out the back hallways, near the classrooms."
    "As I explore, I realize I've never fully familiarized myself with the ins and outs of these corridors. I round a corner and see what seems to be an alcove just up the way."
    "I peek into the area and see none other than [mike.name], his supplies sprawled out on the floor in front of him. He's dozed off."
    show mike
    "I loudly clear my throat to signal my presence and he starts, his eyes opening and darting around in an effort to get his bearings as quickly as possible."
    bree.say "Sorry. I didn't mean to scare you. I was looking for a quiet place to study that wasn't crowded. Mind if I join you here?"
    "[mike.name]'s voice is scratchy and he responds with a groggy nod."
    mike.say "Yeah sure."
    "He clears his throat and moves his things aside to clear a space for me. I sit gingerly beside him."
    bree.say "So, you probably know what I'm about to ask."
    mike.say "I just woke up...please spare me the guessing game."
    bree.say "Oof, grouchy are we?"
    mike.say "Maybe a little. But not too much."
    bree.say "What's your major?"
    mike.say "Computer science. I code. I thought you knew that?"
    bree.say "Nope, didn't know."
    mike.say "Yup. Working full time at a company and part time as a student."
    bree.say "Ah yes, so I know you don't sleep."
    mike.say "That I don't."
    bree.say "Rough. Sorry."
    "I unzip my bag and begin setting up my study space next to him, settling in."
    mike.say "You?"
    bree.say "Me what?"
    mike.say "Your major."
    bree.say "Oh! Right. Biology."
    mike.say "Why biology?"
    bree.say "I love science and specifically I love the study of how nature works. It's intriguing."
    mike.say "So you're like an organic mechanic."
    "I laugh, caught off guard."
    bree.say "Yeah, in a way I guess you could say that."
    "I bury my nose in my book, highlighter in hand to bring certain phrases to my attention for later."
    "A few minutes pass and I feel like [mike.name] wants to talk to me more, but also wants to respect my space."
    "I want to talk too, but I really can't afford to take another break just yet."
    "The page drones on about the structure of cells, the way they send signals to each other, and how division occurs."
    "I learned this in high school. You'd think I could just skip this part and compound on what I know already."
    "I lean my head back on the wall."
    "..."
    "..."
    "My butt goes numb. I stand up, put my cheeks against the wall, and lean forward in an effort to touch the floor directly in front of me."
    mike.say "Yeah, the floor isn't too comfortable."
    bree.say "You can say that again."
    mike.say "I can, but I won't."
    bree.say "What are you working on?"
    mike.say "Calc."
    bree.say "Oh?"
    mike.say "Yeah these differential equations are annoying. Not hard per se. Just annoying...I already know this material well."
    bree.say "I'm in a similar boat, I'm just re-hashing stuff I knew."
    mike.say "Still, it's essential. You know in the Kung Fu Kid, how Shisho Miyazaki tells Danny-san Wax On, Wax Off? This is that."
    bree.say "..."
    mike.say "What?"
    bree.say "That is arguably THE nerdiest thing I've ever heard come out of your mouth. And I would know. I AM one."
    "[mike.name] scoffs and cracks a smile. My heart melts a little bit."
    mike.say "Anyway...the thing about differentials is, not only are their solutions often unclear, but whether solutions are unique or exist at all are also notable subjects of interest."
    bree.say "Tell me more."
    "[mike.name] pauses and blushes. As I suspected."
    mike.say "Well...a differential equation is one with a function and one or more of its derivatives."
    mike.say "A function, as you know, relates an input to an output."
    mike.say "And a derivative is what shows the increment by which that function changes."
    bree.say "So far I follow..."
    "I think...?"
    mike.say "Basically, the function went from being one thing to another."
    mike.say "Like how we went from being almost total strangers, to roommates, to friends, to--"
    "[mike.name] catches himself and immediately falls silent."
    "..."
    "..."
    "..."
    "..."
    "The tension is palpable. He's made it obvious with the slip of his tongue. But it isn't like I didn't feel the same way. Fuck it, I'll rip the bandage off."
    bree.say "Lovers, right? Is that what you were going to say?"
    mike.say "...Yes."
    show mike blush
    "[mike.name]'s voice is low and meek, as if I'll hurt him."
    bree.say "You should know I feel the same way."
    "[mike.name]'s stiffened posture relaxes considerably."
    mike.say "You really mean that?"
    bree.say "I do. I've sort of been waiting on you to ask me but I didn't want to rush things."
    mike.say "I've...I would have asked earlier, but...I've had a lot of heartbreak in the past."
    mike.say "I just didn't want to open myself up and be vulnerable just to get screwed over again."
    bree.say "I understand. In a way, I guess it's good that I decided to come here."
    bree.say "Admittedly, I'm not getting as much studying done as I'd anticipated but I'm happy we cleared the air and both finally confessed."
    show mike normal
    mike.say "I'm sorry to hold you up. Studies are important. When's your test?"
    bree.say "The day after tomorrow."
    "A wave of visible panic washes over [mike.name]."
    mike.say "That soon?! Seriously?! And you're studying NOW?"
    bree.say "Didn't I say I know all of this already?"
    mike.say "You--You did...ok, valid point."
    bree.say "But?"
    mike.say "But you should still brush up a little bit more."
    bree.say "I can do that. Do you...mind if I lean up against you?"
    mike.say "Sure. I'd like that."
    "I nestle up to [mike.name]'s side, lean on him, and rest my head on his shoulder. He makes a surprisingly good pillow. I feel instantly at ease."
    "I pick my book up again, and begin where I left off. Sitting together in silence like this is nice."
    "After some time passes, an announcement comes overhead signalling that the library will close soon. We exchange glances, gather our respective supplies, and pack up to leave."
    bree.say "Wanna walk home together?"
    mike.say "Sure. And...let's go out tomorrow. I promise to have you back at a decent time so you can study. Sound good?"
    bree.say "Sounds perfect."
    mike.say "Awesome. It's a date. I'll meet you in the kitchen when you wake up and we can decide from there what we want to do."
    show mike blush
    "I notice one of his hands is free and slip my hand into his, eliciting another blush response from him."
    bree.say "Sounds great. Let's go home."
    "[mike.name] nods and walks with me, side-by-side."
    return

label mike_female_event_08:
    if mike.love.max < 120:
        $ mike.love.max = 120
    show mike
    "I wake up and head to the kitchen to meet [mike.name], who has already made himself a breakfast of caprese and Melba toast. I can't help but gaze at it longingly as my stomach growls."
    bree.say "Wow, looks fancy."
    mike.say "It's nothing, really. I just didn't feel like putting a lot of work into breakfast today. Couldn't sleep well."
    bree.say "Why, nervous?"
    "The look on his face suggests maybe I shouldn't tease him. I soften my tone and smile."
    bree.say "Hey, it's okay. Me too."
    mike.say "You want some?"
    "He gestures at the plate before him, offering his food to me."
    bree.say "I thought you'd never ask!"
    mike.say "Don't think I didn't catch you staring."
    bree.say "Don't worry. Soon I'll look at you that way, too."
    show mike blush
    "[mike.name]'s face turns a brilliant red and he turns away to pour himself some water. Probably to pour himself a strong cup of composure, too."
    "As he does that, I grab a small plate from the cabinet and put a modest portion aside for myself."
    bree.say "Thanks."
    mike.say "Don't mention it. So, what do you want to do today?"
    bree.say "Hmm...not really sure. Wanna start with breakfast together, and we can talk about it?"
    mike.say "That sounds fine."
    "I take a seat across the table from him and cut into my caprese, stacking the mozzarella on top of the tomato and dipping it into a small pool of glaze nearby."
    "The tomato is crisp and juicy. The glaze is light and not overpowering. Delicious."
    mike.say "How is it?"
    bree.say "Wonderful!"
    show mike happy
    "[mike.name] chuckles."
    mike.say "Yeah, your face kinda says it all."
    "Now it's my turn to blush."
    bree.say "Hey...how come you refused so adamantly to sing for me that day at the park?"
    show mike normal
    "He pauses, surprised."
    mike.say "I didn't realize it meant that much to you. The last time I did...it didn't really end well."
    bree.say "What happened?"
    show mike sad
    "[mike.name] leans forward, resting his full arm on the table, and brings his other to rest on the back of his neck, sighing."
    mike.say "She laughed at me and called me pathetic. It was...soul crushing."
    "My face grew somber as the reality of what had happened set in."
    bree.say "That's awful. I'm sorry."
    show mike normal
    "[mike.name] shrugged."
    mike.say "It happened. I learned a lesson. I'm okay now."
    bree.say "Yeah, but...I just realized that's...exactly what I want. But now it feels like it's too much to ask of you."
    mike.say "You want me to serenade you? Really?"
    bree.say "I don't want to pressure you into doing something out of your comfort zone but...yeah, I really do. I wanted it then too."
    mike.say "It...it is, but not TOO far out. I feel comfortable with you - like I can trust you."
    "I muster up the most genuine tone I have."
    bree.say "You can."
    mike.say "Okay. Well, you look like you've finished your food and I'm just about done as well. Why don't you go shower and get dressed and I'll pack us a lunch?"
    bree.say "You don't need to shower?"
    mike.say "I did before I made breakfast. You're the one who was late, Miss Sleeps-All-Day."
    bree.say "Don't tease a lady about taking her beauty rest. She'll get ugly."
    mike.say "I doubt that's possible."
    "Bested, I wordlessly whirl around and bury my face in my hands."
    "Fuck, that was really cute."
    hide mike
    scene bg bathroom
    "I make my way to the bathroom and close the door firmly behind me, locking it."
    "Sighing, I turn on the water and let it get almost too hot. I pull my PJ shirt up over my head and slip out of my bottoms. My naked skin welcomes the hydrating mist the shower creates."
    "I turn to my reflection in the mirror. It's fuzzy with fog but not indiscernible yet."
    bree.say "Okay...just be calm. It's a first date. It's whatever. Don't screw it up."
    "I hop into the shower and begin scrubbing my body clean. I turn my attention to my hair. After everything, I turn off the water and pat myself dry with the towel. I quickly brush my teeth and head back to my room."
    "I get dressed and hike back to the bathroom to use the blow dryer."
    scene bg livingroom
    show mike casual
    "After I'm finally finished, I find [mike.name] in the living room with his guitar case, a folded blanket, and a picnic basket. He was watching some TV while waiting on me. I clear my throat."
    mike.say "Oh hey! Nice, let's get a move on. Follow me."
    hide mike
    scene bg park
    show mike casual
    "[mike.name] and I walked to the park, guitar case and picnic gear in tow. It wasn't that long ago when I trekked the same path he was now leading me down, but it seemed different today. Were we walking for longer?"
    bree.say "[mike.name], where are we going?"
    mike.say "There's a spot I like. I just need to remember…"
    "He trails off and I continue along silently, enjoying the singing of the birds and the fair breeze rustling through the leaves of the tree-lined path."
    mike.say "Here we go."
    "He motions toward a small passage off the main way. We walk along for a few more minutes and come upon an undisturbed clearing. Unprompted, I unfurl the blanket and lay it gently on the ground. I sit and set the basket beside me."
    "[mike.name] removes his instrument from its case and begins tuning."
    bree.say "This is a nice little spot. How did you find it?"
    mike.say "Truth be told, I have an adventurous streak. I noticed this walkway months ago and when I first discovered this area, I immediately fell in love. It's quiet and I don't have an audience when I'm trying to practice. It's nice."
    bree.say "And secluded."
    mike.say "Yes, that too."
    "The notes of the guitar float calmly through the air as he warms up with a few easy riffs and chords. It's weird, but music always makes me feel physically at ease the same way a massage would."
    "[mike.name] begins humming a tune and eventually words form to match. His eyes are closed but I stare at him in awe. I can't believe he's making this all up on the spot."
    bree.say "[mike.name]...that was really touching."
    "I fight sappy tears from welling up in my eyes."
    mike.say "Thank you for being here with me. I like you a lot, [hero.name]. I'd like to keep seeing you."
    bree.say "It's my pleasure. I like you a lot too, [mike.name]. I really don't understand how someone could have possibly called you pathetic and laughed. Heartless. I'm angry just thinking about it."
    mike.say "Thanks but don't worry too much about it. I'm fine now, I promise."
    bree.say "It's in the past."
    mike.say "Yeah, exactly."
    "We continue our date talking, sharing as many details about ourselves as possible. We bring up our pasts and banter a bit. Eventually we get hungry and have lunch."
    hide mike
    scene bg livingroom
    "Upon eating our fill, we head back home and chill on the couch watching TV."
    "I begin to doze off, my head on his lap. I'm supremely content. I'll study later. Right now...everything's perfect."
    return

label mike_female_event_09:
    if mike.love.max < 140:
        $ mike.love.max = 140
    "Today's supposed to be date day for me and [mike.name], but neither of us could come up with any serious ideas."
    "So in the end, we just decided to keep it casual and head down to the mall for a bit of window shopping."
    "Sure, it's not the most exciting or romantic way to spend time together."
    "But sometimes it's not where you are that counts, it's who you're with, right?"
    "And my positive mental attitude seems to be paying off as well."
    "Because [mike.name] and I are walking around the mall, arm-in-arm."
    "We're talking about everything and nothing all at once."
    "And we're generally having a good time, being the perfect couple."
    bree.say "Ooh, [mike.name]..."
    bree.say "Come have a look at this!"
    "I point to the shiny thing that's caught my attention in the window of the nearest store."
    "But for some reason [mike.name] doesn't seem to hear me at all, and he makes no response."
    "Looking up I expect to see him sneaking a glance at his phone or something like that."
    bree.say "[mike.name]!"
    bree.say "Are you even listening to me?"
    "Instead of finding a sheepish [mike.name] looking up from his phone, I see something else entirely."
    show mike sad with dissolve
    "[mike.name]'s staring off into the middle distance, eyes wide and a wistful expression on his face."
    "And it doesn't take me long to see what's caught his attention either."
    "There's a girl walking towards us, and not just any girl."

    "She's one of those girls you want to hate on first sight."
    "Her hair is that perfect shade of brown you could never get out of a bottle."
    "She's blessed with a face so sweet and innocent she could charm the birds out of the trees."
    "And she has a perfectly placed and formed mole that only makes her even more memorable."
    "Worse still, she's obviously cast a spell over [mike.name]!"
    show samantha normal at right with moveinright
    show mike normal at left with moveinleft
    samantha.say "Oh, hey, [mike.name]."
    samantha.say "Fancy seeing you here!"
    mike.say "H...hey, Sam!"
    mike.say "I know, I know - small world, right?"
    "The moment I hear [mike.name] say that name, it all makes sense."
    "This must be Samantha, the girl who lived with [mike.name] before Sasha and I moved in."
    "And the one that he's always talking about like she's the one that got away!"
    samantha.say "I was just here to pick something up for Ryan."
    samantha.say "How about you?"
    mike.say "Oh, you know..."
    mike.say "Just hanging out, killing time! - the usual!"
    "Before now I'd been keeping silent while they greeted each other."
    "And I was patiently waiting for [mike.name] to make the introductions."
    "But now it sounds like he's trying to make out that I'm not even here!"
    bree.say "Ahem..."
    bree.say "I said -AHEM!"
    "[mike.name] jumps a little at the sound of my voice."
    "Which does nothing to reassure me."
    "But Sam seems to handle the situation far better."
    "She turns to face me, an irritatingly friendly smile on her face."
    samantha.say "Oh, sorry..."
    show samantha happy
    samantha.say "You must be [hero.name], right?"
    samantha.say "Sorry, you know how it is when old friends bump into each other!"
    "Urgh...why does she have to be so nice and reasonable?"
    "This Sam would be so much easier to hate if she acted like a bitch!"
    "I feel torn as she smiles at me, waiting for an answer."
    "I want to show her that [mike.name] and I are an item now."
    "But I don't want to look like a complete bitch in front of her."
    show samantha normal
    "Because that way I'll end up in [mike.name]'s bad books too!"
    if hero.morality >= 25:
        "No, I need to be on my best behaviour here."
        "Otherwise [mike.name] really is going to think he'd be better off with her!"
        bree.say "Hi, Samantha!"
        bree.say "I should have guessed it was you."
        bree.say "[mike.name]'s told me so many stories about the three of you!"
        "Sam smiles and nods happily."
        show mike down
        "But I see [mike.name] flinch at the implicit mention of this Ryan guy."
        "I guess that there must be a rivalry of some kind between them."
        samantha.say "Oh please, call me Sam - everybody else does!"
        show samantha annoyed
        samantha.say "And he did, did he?"
        "Samantha chuckles and casts an accusing glance at [mike.name]."
        "On cue he begins to turn red and look embarrassed."
        mike.say "Well I..."
        show mike normal
        mike.say "You know how it is..."
        mike.say "I was just filling [hero.name] in on who's who!"
        "Sam looks back at me, shaking her head."
        show samantha happy
        "And we both burst into laughter at the same time."
        samantha.say "Well he'll have left out some stuff, [hero.name]."
        show samantha normal
        samantha.say "Most likely all the stuff that makes him look bad!"
        samantha.say "So we'll have to get together and I can fill in the gaps for you, okay?"
        "I smile back at Sam, relieved that the pressure's been shifted onto [mike.name]."
        bree.say "You know what, Sam..."
        bree.say "That sounds like a lot of fun!"
        bree.say "We can compare notes on him when we do that!"
        samantha.say "I'll get [mike.name] to send me your number, okay?"
        samantha.say "Now I really do have to get along."
        samantha.say "See you soon, [mike.name]."
        samantha.say "And nice to meet you too, [hero.name]!"
        hide samantha with moveoutright
        "Once Sam's out of sight, I slip my arm into [mike.name]'s."
        show mike normal at center with moveinleft
        bree.say "She seems nice."
        mike.say "Ah...yeah, [hero.name]..."
        mike.say "And you seemed to get on great."
        show mike happy
        mike.say "Which is...great, I guess..."
    elif hero.morality <= -25:
        "I don't like the idea of [mike.name] holding a torch for this girl."
        "And I like the idea of her hanging around in his life even less!"
        "So screw the consequences - I need to mark my territory!"
        bree.say "Oh..."
        bree.say "So you'd be Sam, right?"
        "Sam seems a little taken aback at my tone of voice."
        "But she does the best she can to cover it up and carry on."
        show samantha annoyed
        samantha.say "Ah...yes...that's me!"
        bree.say "Mmm..."
        "I look Sam up and down with undisguised admiration."
        bree.say "Yeah, I can see why [mike.name] likes you so much!"
        bree.say "You're one hot babe, Sam!"
        "Sam's eyes go wide at this, and she looks a little shocked."
        "I see her shoot a glance at [mike.name], looking for help."
        show samantha surprised
        samantha.say "Erm...[mike.name]?"
        samantha.say "What exactly is she talking about?"
        samantha.say "What have you been telling her about our relationship?!?"
        "[mike.name] shrugs and shakes his head."
        "And in that moment he seems utterly helpless."
        mike.say "N...nothing, Sam!"
        show mike down
        mike.say "Nothing but the truth - I swear it!"
        "I tut and shake my own head at [mike.name]."
        "And I make sure to drape myself over him as I reply."
        bree.say "He's just trying to be a gentleman, Sam."
        bree.say "The truth is that [mike.name] here's got the hots for you."
        bree.say "I mean serious unrequited love kind of thing!"
        "Sam gasps and raises her hands to her mouth."
        samantha.say "Oh, [mike.name]..."
        show samantha sad
        samantha.say "I never knew!"
        samantha.say "You never told me..."
        mike.say "How could I, Sam?!?"
        mike.say "You were with Ryan..."
        mike.say "And he was my friend!"
        "I let out a peal of laughter."
        "And that turns their attention back to me."
        bree.say "There's a simple solution to all of this, you know."
        bree.say "We could just agree to share him, Sam."
        bree.say "[mike.name]'s got a nice BIG cock!"
        show mike blush
        bree.say "And he obviously wants to fuck us both."
        bree.say "So why don't we let him have the two of us at once?"
        show samantha happy
        samantha.say "Yes..."
        show samantha annoyed
        samantha.say "No..."
        show samantha flirt
        samantha.say "I don't know!"
        show samantha normal blush
        samantha.say "I...I have to go - right now!"
        "With that, Sam turns and hurries away."
        hide samantha with moveoutright
        "Once Sam's out of sight, I slip my arm into [mike.name]'s."
        show mike blush at center with moveinleft
        "He seems dazed, almost like he's in a trance."
        bree.say "She seems nice."
        mike.say "Ah...yeah, [hero.name]..."
        show mike happy
        mike.say "And you seemed to get on great."
        mike.say "Which is...great, I guess..."
        $ mike.sub += 1
    else:
        "Okay, I need to walk a fine line here."
        "I have to let Sam know that [mike.name]'s taken."
        "But at the same time I can't be a bitch about it either."
        bree.say "Oh...Samantha, right?"
        bree.say "[mike.name]'s told me all about you!"
        "Sam smiles and nods happily."
        samantha.say "Oh please, call me Sam - everybody else does!"
        show samantha normal
        samantha.say "And he did, did he?"
        "Samantha chuckles and casts an accusing glance at [mike.name]."
        "On cue he begins to turn red and look embarrassed."
        mike.say "Well I..."
        show mike down
        mike.say "You know how it is..."
        mike.say "I was just filling [hero.name] in on who's who!"
        bree.say "He mentioned that you and...Ryan, was it?"
        bree.say "He mentioned that you're an item?"
        bree.say "That must have been hard in a shared house!"
        show samantha annoyed
        "Sam looks a little thoughtful."
        "But she nods her head all the same."
        samantha.say "Yeah, it can be tough."
        show samantha normal
        samantha.say "You want your privacy, of course."
        samantha.say "Then you have [mike.name] here - wandering around in his underwear!"
        show samantha happy
        mike.say "HEY!"
        show mike angry
        mike.say "I'm standing right here, you know?"
        "I make sure to laugh along with Sam."
        "But at the same time I lean a little closer to [mike.name]."
        bree.say "Aw, I'm sorry, honey!"
        bree.say "Trust me, Sam - he's getting a taste of his own medicine now."
        bree.say "Our housemate Sasha, she does the same thing all the time!"
        bree.say "Doesn't she, babe?"
        show mike normal
        "[mike.name] nods and shakes his head."
        mike.say "Yeah, you're right."
        mike.say "For a girl, she can be a real slob!"
        show samantha normal
        "Sam nods, seeming to see that we're together for the first time."
        samantha.say "We should meet up for a drink, [hero.name]."
        bree.say "You know what, Sam..."
        bree.say "That sounds like a lot of fun!"
        bree.say "We can compare notes on him when we do that!"
        samantha.say "I'll get [mike.name] to send me your number, okay?"
        samantha.say "Now I really do have to get along."
        samantha.say "See you soon, [mike.name]."
        show samantha happy
        samantha.say "And nice to meet you too, [hero.name]!"
        hide samantha with moveoutright
        "Once Sam's out of sight, I slip my arm into [mike.name]'s."
        show mike at center with moveinleft
        bree.say "She seems nice."
        mike.say "Ah...yeah, [hero.name]..."
        show mike happy
        mike.say "And you seemed to get on great."
        mike.say "Which is...great, I guess..."
    $ mike.love += 2
    $ game.active_date.score = 50
    return

label mike_female_event_10:
    if mike.love.max < 160:
        $ mike.love.max = 160
    scene bg pub
    "When I decided to come down to the pub, I was hoping for a chance to unwind a little."
    "Sure, it's not like I really have a lot of shit to forget about, just the usual stress of life."
    "But it's been a long week and I want to end it on a high note, you know?"
    "And it's all going pretty well to begin with."
    "I have a drink on the go, and I can feel myself finally starting to relax."
    "Which just happens to be the same moment I spot a familiar face on the other side of the pub."
    show mike date at left with dissolve
    "It's [mike.name], standing there with a drink in his hand and a smile on his face."
    "I didn't know he was even going out tonight, let alone that he'd be in the pub too."
    "No worries - I'll just go over there and..."
    "Wait a minute...who's that girl he's talking to?"
    show hanna date at left4, dark with dissolve
    "They're looking very into the conversation they're having."
    "Is he..."
    "He is!"
    "[mike.name]'s flirting with her!"
    if mike.sexperience >= 5:
        "What in the hell does he think he's doing over there?"
        "I thought that we were supposed to be an item."
        "We never agreed to this being an open relationship either!"
        "Now he's flirting with some trollop in the nearest pub?"
        "Well...actually...she's a pretty cute-looking trollop!"
        "But that doesn't change the fact he's bang out of order!"
    elif mike.sexperience >= 2:
        "Damn it!"
        "This is where I'm supposed to be all liberated and modern."
        "Sure, we slept together a couple of times already."
        "But we kind of agreed that there were no strings attached."
        "[mike.name] should be free to flirt with whoever the hell he likes."
        "But it just bugs me, you know?"
        "Like, I saw [mike.name] first."
        "And I kind of feel like I should be the one getting all of his attention!"
    else:
        "Yeah, yeah, yeah..."
        "I know what you're thinking, okay?"
        "He's a free agent, and there's nothing between us."
        "And I know that I'm being jealous and territorial."
        "But it just bugs me, you know?"
        "Like, I saw [mike.name] first."
        "And I kind of feel like I should be at the front of the queue!"

    "I try to keep a smile on my face as I walk over to where they're standing."
    "And it's worth the effort, even if only for the look I see appear on [mike.name]'s!"
    hide hanna
    show mike date at left4
    show hanna date at right4
    with dissolve
    bree.say "Hey, [mike.name]!"
    bree.say "Why didn't you tell me you were coming out for a drink?"
    bree.say "We could have come down here together!"
    "The girl [mike.name]'s talking to looks at me and then at him."
    "She's clearly expecting him to introduce me."
    "That and to explain the situation away too!"
    mike.say "Ah..."
    mike.say "Hey, [hero.name]!"
    mike.say "Fancy bumping into you here!"
    "Girl" "[mike.name]!"
    "Girl" "Aren't you going to introduce me?"
    "I smile innocently."
    bree.say "Yeah, [mike.name]..."
    bree.say "Aren't you going to introduce us?"
    mike.say "Erm..."
    mike.say "[hero.name], this is Hanna."
    mike.say "Hanna, this is [hero.name]."
    mike.say "A...friend of mine!"
    "I laugh and shake my head at this."
    bree.say "Oh, [mike.name], dear..."
    bree.say "You're so funny!"
    "I'm pretty much decided that this is going to be me fucking with [mike.name]."
    "But I'm not quite sure how I'm going to go about it..."
    menu:
        "Remind [mike.name] of his prior commitments":
            "Wait a minute..."
            "What if I'm over-thinking this?"
            bree.say "That's no way to introduce your girlfriend, is it?"
            "The girl's face is a picture as I drop [mike.name] in the shit."
            "She plants her balled fists on her hips and glares at him."
            show hanna angry
            hanna.say "What the hell, [mike.name]?"
            hanna.say "You didn't say anything about a girlfriend!"
            "[mike.name]'s holding his hands up as she says this."
            "Like he's trying to explain himself and hold her off at the same time."
            mike.say "W...wait a minute..."
            mike.say "It's really more like friends with benefits!"
            show hanna at right5 with move
            "That explanation doesn't seem to have the desired effect."
            play sound spank
            show mike b sad at left4, hshake
            "And instead it earns [mike.name] a pretty mean slap across the face."
            hide hanna with moveoutright
            bree.say "Oh..."
            bree.say "Oh fuck!"
            "I can't help laughing at the palm-shaped mark on [mike.name]'s face."
            "That and the fact the girl just stormed out of the pub."
            show mike sad at center with move
            mike.say "Aah..."
            mike.say "[hero.name]!"
            mike.say "Was that really necessary?"
            bree.say "I dunno, [mike.name]..."
            bree.say "It sure made me feel better!"
            $ mike.love -= 5
            $ mike.sub += 5
        "Try to get [mike.name]'s attention onto you":
            "Well, it looks like I'm going to have to fight fire with fire."
            "If [mike.name]'s eyes are all over this bitch, I need to change that."
            "What I need to do is get those eyes on me again!"
            "With that in mind, I put on my most seductive smile."
            "And then I make to remind [mike.name] what he's already got right here!"
            if hero.charm >= 50:

                "I literally drape myself over [mike.name], wrapping my limbs around him."
                "All the time I'm moaning and sighing too, adding to the effect."
                "[mike.name] seems totally overwhelmed by my efforts."
                "He stares at me, wide-eyed the whole time."
                "And I can already feel something stiffening in his pants!"
                bree.say "Mmm..."
                bree.say "Go find another guy to giggle at, bitch."
                bree.say "Because this one's spoken for!"
                "The girl's face is a picture as she watches me."
                "But all she can do is shake her head in amazement."
                "Then she turns and hurries out of the pub."
                mike.say "Erm...[hero.name]..."
                mike.say "Was that really necessary?"
                bree.say "Of course it was, [mike.name]..."
                bree.say "And I'm sure it made us both feel better!"
                $ mike.love += 5
                $ mike.sub += 5
            else:

                "It's at times like this I realise how dumb that saying actually is."
                "Firefighters don't fight fire with fire, they use water."
                "What I'm trying to do just seems to make things worse too!"
                "I make to drape myself over [mike.name], but I trip over my own feet."
                play sound body_fall
                pause 0.3
                with vpunch
                "That means I go tumbling forwards and onto the floor."
                "Landing in a heap at [mike.name]'s feet, I can feel my cheeks burning."
                show hanna annoyed
                hanna.say "Erm..."
                hanna.say "[mike.name]..."
                hanna.say "What is she doing?"
                "I don't get to hear [mike.name]'s response to the question."
                "Because I'm up and headed for the door before I'm fully on my feet."
                "I don't even bother to look back over my shoulder."
                "I just flee the scene, hoping that what just happened went largely unnoticed."
                $ mike.love -= 5
                $ mike.sub -= 5
        "Try to win the girl away from [mike.name]":
            $ hero.morality -= 5
            "Two can play this game."
            "And that's something I'm going to prove to [mike.name]."
            bree.say "That's no way to introduce your girlfriend, is it?"
            "The girl's face is a picture as I drop [mike.name] in the shit."
            show hanna a angry
            "She plants her balled fists on her hips and glares at him."
            hanna.say "What the hell, [mike.name]?"
            hanna.say "You didn't say anything about a girlfriend!"
            "[mike.name]'s holding his hands up as she says this."
            "Like he's trying to explain himself and hold her off at the same time."
            mike.say "W...wait a minute..."
            bree.say "Oh dear..."
            bree.say "Did [mike.name] here not explain?"
            bree.say "We're kind of adventurous."
            bree.say "By which I mean - we like to mix it up!"
            "I take hold of the girl's hand as I say this."
            "And then I press it against my chest."
            if hero.charm >= 50:

                show hanna blush
                "The girl smiles, happily letting me place her hand on my breast."
                "She even giggles a little as she gives it a gentle squeeze!"
                mike.say "Erm..."
                mike.say "[hero.name]..."
                mike.say "What are you doing?"
                bree.say "What does it look like, [mike.name]?"
                bree.say "I'm beating you at your own game!"
                "The girl giggles again as she takes hold of my hand."
                "And neither of us looks back as she lets me lead her away from [mike.name]."
                $ mike.love += 5
                $ mike.sub += 5
            else:

                "The girl responds by yanking her hand away almost the next moment."
                show hanna sad
                "Then she looks at [mike.name], horror written all over her face."
                hanna.say "Erm..."
                hanna.say "[mike.name]..."
                hanna.say "What is she doing?"
                "[mike.name] shakes his head."
                mike.say "I have no fucking idea!"
                "I can feel my cheeks burning as my attempts to seduce the girl fail."
                "I don't get to hear what either of them says next."
                "Because I'm headed straight for the door."
                "I don't even bother to look back over my shoulder."
                "I just flee the scene, hoping that what just happened went largely unnoticed."
                $ mike.love -= 5
                $ mike.sub -= 5
    return

label mike_female_event_11a:
    if mike.love.max < 180:
        $ mike.love.max = 180
    scene bg livingroom
    "I feel like [mike.name] and I have kind of been at odds with each other for the past few days."
    "Especially after the incident where I found him chatting up another girl in the pub."
    "I mean, we talked about that afterwards, and it seemed to come down to nothing at all."
    "We weren't clear on the boundaries of our relationship and exactly what we wanted from each other."
    "So what happened was kind of down to the both of us failing to communicate."
    "We decided to let it drop, and neither of us has brought it up since then."
    "But I still feel like we need to do something that'll help to clear the air."
    "And that's why we're currently hammering away at each other in the middle of the living room."
    "Hey - what kind of a filthy mind do you have?!?"
    show play console mike with dissolve
    "I mean we're playing on the Zbox together!"
    mike.say "YES!"
    mike.say "I got you this time, [hero.name]!"
    mike.say "Prepare to have your ass handed to you!"
    bree.say "Oh no, [mike.name]!"
    bree.say "Whatever am I going to do?"
    "[mike.name]'s too busy anticipating the sweet taste of victory to notice my sarcastic tone."
    "And his eyes are focused on the TV screen, so he doesn't see the grin on my face."
    mike.say "Yes, yes, yes..."
    mike.say "Wha...what?!?"
    mike.say "No, no...NOOO!"
    bree.say "[mike.name] - what happened?"
    bree.say "I thought you had this one in the bag?"
    "[mike.name] throws his controller down on the floor."
    hide play console
    show mike angry at center, zoomAt(1.5, (640, 1040))
    with dissolve
    "And then he turns around and points a finger at me."
    show mike surprised
    mike.say "What the hell, [hero.name]?"
    mike.say "I had you on the ropes!"
    mike.say "What did you do?"
    show mike upset
    "I keep my smile innocent as I shrug off [mike.name]'s accusations."
    bree.say "I dunno, [mike.name]..."
    bree.say "Maybe I just got lucky?"
    "[mike.name] mutters under his breath as he picks up his controller."
    bree.say "You want to go again?"
    bree.say "Maybe you'll beat me this time?"
    "[mike.name] narrows his eyes as he scrutinises me."
    "But then he nods, unable to resist the offer of a rematch."
    show mike shout
    mike.say "Okay, [hero.name]..."
    mike.say "But no cheating this time!"
    show mike smile
    bree.say "Of course not!"
    bree.say "I wouldn't dream of it..."
    hide mike
    show play console mike
    "Soon enough we're at it again, both hammering away at out controllers."
    "I'm confident that I can hammer [mike.name] again too."
    "And maybe that's making me a little too cocky."
    "Because [mike.name]'s suddenly on fire, playing like a demon."
    bree.say "Hey!"
    bree.say "I thought you said no cheating?"
    "Now it's [mike.name]'s turn to play the innocent and enjoy my irritation."
    mike.say "No cheating here, [hero.name]."
    mike.say "You're just being left in the dirt by a superior player!"
    bree.say "Urgh..."
    bree.say "You can be such an asshole sometimes!"
    mike.say "Call me names all you like, [hero.name]."
    mike.say "This asshole still beat you!"
    "I'm about to throw my controller down on the floor, just like [mike.name] did before."
    hide play console
    show mike normal at center, zoomAt(1.5, (640, 1040))
    with dissolve
    "But then I stop as a thought occurs to me."
    bree.say "Oh..."
    bree.say "That's weird!"
    mike.say "What do you mean, [hero.name]?"
    show mike surprised
    mike.say "What's weird?"
    show mike normal
    bree.say "Well...normally when I have to compete with someone, it never works out for me."
    bree.say "Like, all that happens is I get mad and then I can't even think straight."
    bree.say "But with you it's different, like competing with you makes me focus."
    bree.say "You know what I mean?"
    show mike annoyed
    "[mike.name] looks thoughtful for a moment."
    show mike smile
    "And then he nods in agreement."
    show mike happy
    mike.say "Yeah, [hero.name] - me too."
    mike.say "And I get a much bigger buzz from winning when it's you."
    mike.say "More than when I beat other people at something."
    show mike smile
    bree.say "Oh god - me too!"
    bree.say "It's almost like winning or losing isn't what's important."
    show mike happy
    mike.say "Yeah, so long as I'm playing the game with you!"
    show mike smile
    bree.say "Hey...you know what this reminds me of?"
    show mike happy
    mike.say "It kinda reminds me of the other day in the pub, [hero.name]."
    show mike smile
    bree.say "Exactly!"
    bree.say "When we were competing for that girl's attention."
    bree.say "It was like I could feel an electricity between us."
    bree.say "An almost...sexual tension!"
    "[mike.name] nods at this."
    show mike happy
    mike.say "Yeah, [hero.name] - it's like you're reading my mind!"
    show mike smile
    if hero.morality <= -25:
        menu:
            "Suggest a game to [mike.name]":
                "Suddenly an idea pops into my head."
                "And I can't wait to suggest it to [mike.name]."
                bree.say "Ooh, ooh..."
                bree.say "[mike.name], we should do it again!"
                show mike surprised
                mike.say "Are you serious, [hero.name]?"
                mike.say "You want to go out and hit on a girl?"
                mike.say "You and me, at the same time?"
                show mike normal
                bree.say "Exactly that, [mike.name]..."
                bree.say "But this time it'll be different."
                bree.say "Because this time it'll be a competition, with rules too!"
                menu:
                    "Push him a little":
                        show mike shout
                        mike.say "You know what, [hero.name]..."
                        show mike happy
                        mike.say "That sounds like fun!"
                        show mike smile
                        "I nod and smile."
                        bree.say "Great, [mike.name]..."
                        bree.say "I knew you were the adventurous type!"
                        $ mike.love += 5
                        $ flirtgame = 0
                    "Wait for his answer":
                        show mike shout
                        mike.say "Erm...no, [hero.name]..."
                        mike.say "I don't think that's a good idea."
                        show mike sad
                        "I can't help groaning and rolling my eyes."
                        bree.say "Oh, [mike.name]..."
                        bree.say "You're such a boring bastard sometimes."
                        bree.say "I thought guys dreamed of doing stuff like that!"
                        $ mike.love -= 5
                        $ flirtgame = False
                        return
    else:
        "Suddenly I see a light go on behind [mike.name]'s eyes."
        "And I'm guessing that he's just had an idea."
        show mike happy
        mike.say "Oh man..."
        mike.say "What about this, [hero.name]..."
        mike.say "We should totally do the same thing again!"
        show mike smile
        bree.say "Are you serious, [mike.name]?"
        bree.say "You think we should go out and both hit on the same girl?"
        show mike happy
        mike.say "Yeah, [hero.name]..."
        mike.say "But this time we make it an official competition."
        mike.say "We agree on the rules, yeah?"
        show mike smile
        menu:
            "Agree to the competition":
                bree.say "You know what, [mike.name]..."
                bree.say "That sounds like fun!"
                show mike happy
                "[mike.name] nods and smiles."
                mike.say "Great, [hero.name]..."
                mike.say "I knew you were the adventurous type!"
                $ mike.love += 5
                $ flirtgame = 0
            "Do not agree to the competition":
                bree.say "No, [mike.name]..."
                bree.say "I don't think I like the sound of that."
                show mike sad
                "[mike.name] lets out a groan and rolls his eyes."
                show mike shout
                mike.say "Urgh..."
                mike.say "Whatever, [hero.name]..."
                mike.say "I just thought you were more adventurous than that!"
                $ mike.love -= 5
                $ flirtgame = False
                return
    show mike happy
    mike.say "Okay, so we're agreed."
    mike.say "But now we have to figure out the rules of the competition."
    mike.say "And I say that, for number one, we both have to agree on the target."
    mike.say "Like, it has to be someone that we both think is hot!"
    show mike smile
    "I shake my head, trying to make out that I'm a little offended."
    "But I have to admit that [mike.name] does make a good point."
    bree.say "Okay, [mike.name], okay..."
    bree.say "A little shallow, maybe..."
    bree.say "But I guess this whole thing is pretty shallow."
    show mike happy
    mike.say "So it's agreed?"
    show mike smile
    bree.say "Agreed - we both have to find the target attractive."
    bree.say "And the aim is to...what?"
    bree.say "Get them to kiss you?"
    "[mike.name] shakes his head at this."
    show mike shout
    mike.say "Nah, [hero.name]..."
    mike.say "Too easy."
    show mike normal
    bree.say "Hah...I gotta admire your confidence, [mike.name]!"
    bree.say "Okay...more than a kiss."
    bree.say "So, rule two..."
    bree.say "How about they have to agree to go on a date?"
    show mike smile
    "This time [mike.name] nods in agreement."
    show mike happy
    mike.say "That's more like it, [hero.name]."
    mike.say "A date - or something a little more kinky!"
    show mike smile
    "I hold a hand up right there, stopping [mike.name] in his tracks."
    bree.say "Whoa, cowboy!"
    bree.say "That's going to be rule three right there..."
    bree.say "No sex!"
    show mike normal
    "[mike.name] looks like he's going to flat-out object for a second."
    show mike perv
    "But then I see a sly look creep onto his face."
    mike.say "I suggest a slight amendment to that rule, [hero.name]..."
    mike.say "No sex...UNLESS we're both involved!"
    show mike normal
    "I ponder the idea for a moment."
    "And then I nod."
    bree.say "Sounds fair to me, [mike.name]."
    bree.say "So rule three is no sex, unless both of us are in on it."
    show mike shout
    mike.say "Fourth and final rule - it's best out of three?"
    show mike normal
    "I nod and hold out my hand for [mike.name] to shake."
    "He doesn't hesitate to take it and seal the deal."
    show mike smile
    bree.say "Agreed."
    show mike happy
    mike.say "Agreed."
    show mike smile
    "I can feel [mike.name] squeezing my hand pretty hard."
    show mike blush
    "And once we've shaken hands, he doesn't seem keen to let go."
    "But then I can't say that I'm pulling away either."
    "In fact...is it just me, or is it getting hot in here?"
    bree.say "[mike.name]..."
    show mike happy
    mike.say "Yeah, [hero.name]?"
    show mike smile
    bree.say "Are you feeling a little, you know..."
    show mike happy
    mike.say "I dunno, [hero.name]..."
    mike.say "But I am feeling a little, that way..."
    show mike smile
    "The next moment I feel like my body switches into autopilot."
    "All I can think about is how kinky what we just cooked up together sounds."
    "And that's making me aware of just how close I am to [mike.name] right now."
    "More specifically, how close I am to a certain part of his anatomy!"
    hide mike
    show mike kiss
    with dissolve
    $ mike.flags.kiss += 1
    "We both seem to lurch forward at the same moment."
    "And by some small miracle, we avoid butting heads."
    "Instead our lips meet, and that's the spark that sets us off."
    "The very next moment [mike.name] and I are all over each other."
    "We both drop our controllers, the Zbox forgotten."
    "Now the only thing we want to play with is each other!"
    "I have no idea if Sasha is even in the house right now."
    "But the thought of her walking in isn't enough to stop me."
    "Instead I decide that the best idea is to make a lot of noise."
    "That way she should know what's going on and give the sitting room a wide berth."
    "Sure, she'll know what we're fucking in here."
    "But that's better than missing out on what I want right now!"
    hide mike
    show mike blush at center, zoomAt(1.5, (640, 1040))
    bree.say "Oh fuck..."
    bree.say "[mike.name]...I feel so fucking horny!"
    mike.say "Ah..."
    mike.say "Me too, [hero.name]...me too!"
    bree.say "I want your cock in me SO badly!"
    "[mike.name] nods, desperate to give me what I'm asking for."
    "Normally I'd be the one calling the shots and dictating the positions."
    "But right now all I want is for him to get on with it and fuck me!"
    "So I let him take the lead, allowing him to lay me down on my back."
    "We're a crazy tangle of arms and legs as we tumble onto the floor."
    "Both of us trying to undress ourselves and the other at the same time."
    "But then I finally feel [mike.name]'s cock brush against my thighs."
    "Without asking for permission, I reach down and grab it."
    "This makes him gasp and me giggle."
    "It's hard and getting harder by the moment."
    "And I know that it's going to feel so good inside of me!"
    "At the same time I can feel myself getting excited too."
    "My pussy feels like it's melting down there!"
    mike.say "[hero.name]..."
    mike.say "Please..."
    mike.say "Don't tease me!"
    "I'm still giggling as [mike.name] pleads with me."
    "Because that's exactly what I'm doing with him."
    "And I'm enjoying every second that it lasts."
    "But I can't keep him waiting forever."
    scene bg black
    show mike missionary
    with fade
    "I have to decide what I'm going to do with him..."
    menu:
        "Guide him to my pussy":
            "And that's a fucking no brainer!"
            "My pussy's so wet right now."
            "It's almost doing the thinking for me!"
            "And all it takes is a little yank on [mike.name]'s cock..."
            "The motion seems to set him on autopilot."
            "He lowers himself down and onto me."
            "And at that same time, I steer him home with one hand."
            bree.say "Mmm..."
            show mike missionary pleasure
            bree.say "Oh, [mike.name]..."
            show mike missionary normal
            "I can't help it, there's no way I can keep quiet."
            "The moment I feel the sensation of [mike.name]'s cock against my lips..."
            show mike missionary vaginal at stepback(0.1, 10, 0)
            "It's like my whole body reacts, wanting to draw him in."
            "I can feel the hunger in him too, the need to have me."
            "But that doesn't mean [mike.name] lets himself go like an animal."
            "Instead he keeps enough control to take things slowly."
            "I can feel everything he does thanks to his patience."
            "But at the same time, I can feel the barely suppressed desire in him too!"
            "[mike.name] sinks into me a little at a time."
            "His cock fills me more with each moment that passes."
            "Part of me wants to urge him on, to demand he go faster."
            show mike missionary normal
            "But instead I bite my lip, whimpering as he goes ever deeper."
            show mike missionary at stepback(0.1, 10, 0)
            "[mike.name] pauses when he can't go any further."
            "By now he's laid atop me, his head beside mine."
            "Which means I can whisper into his ear."
            show mike missionary pleasure
            bree.say "[mike.name[0]]...[mike.name]..."
            bree.say "Fuck me..."
            bree.say "Fuck me now!"
            show mike missionary normal
            "Obedient as ever, [mike.name] springs into action at my command."
            "Well, maybe springs is a little too emphatic!"
            "But what he does do is start to move inside of me."
            show mike missionary at stepback(0.1, 10, 0)
            "Slowly at first, and then with ever more speed."
            "And the feeling on my end?"
            "Well, what can I say?"
            show mike missionary at stepback(0.1, 10, 0)
            "It's everything I want and more!"
            "Soon enough I have my arms and legs wrapped around [mike.name]."
            show mike missionary at stepback(0.1, 10, 0)
            "I'm clinging to him like I'm afraid he's going to escape."
            "But there's no chance of that, not as deep as he's going!"
            show mike missionary pleasure at stepback(0.1, 10, 0)
            "Every time he fills me, I hear myself moaning with pleasure."
            "And yet it sounds like the sounds are coming from someone else."
            show mike missionary at stepback(0.1, 10, 0)
            "Because I'm so lost in the sensations I'm experiencing..."
            "The world around me seems a million miles away."
            show mike missionary at stepback(0.1, 10, 0)
            "I'm ready to ride this thing to the end."
            "To take it as long as [mike.name] can keep on giving it."
            "But all of a sudden I feel a change in him."
            "It's like he gets a second wind, a new surge of energy."
            show mike missionary at stepback(0.1, 10, 0)
            pause 0.15
            show mike missionary at stepback(0.1, 10, 0)
            "And before I know it, his speed and intensity are increasing!"
            "Before he was sinking into me deep and slow."
            show mike missionary at stepback(0.1, 10, 0)
            pause 0.15
            show mike missionary at stepback(0.1, 10, 0)
            "Now he's pounding away like his life depends on it."
            bree.say "[mike.name[0]]...[mike.name]..."
            show mike missionary at stepback(0.1, 10, 0)
            pause 0.15
            show mike missionary at stepback(0.1, 10, 0)
            bree.say "I...I'm..."
            bree.say "I'm gonna cum!"
            show mike missionary at stepback(0.1, 10, 0)
            pause 0.15
            show mike missionary at stepback(0.1, 10, 0)
            "I'm not joking either!"
            "I can feel my whole body starting to tingle."
            show mike missionary ahegao at stepback(0.1, 10, 0)
            pause 0.15
            show mike missionary at stepback(0.1, 10, 0)
            "And then it happens, waves of pleasure spreading out from the centre."
            "I cling to [mike.name] more tightly than ever, crying out as I lose it."
            show mike missionary at stepback(0.1, 10, 0)
            pause 0.15
            show mike missionary creampie with hpunch
            "I seem to take him with me too, as I feel him cumming inside me."
            with hpunch
            "That only serves to make the feeling even more intense."
            with hpunch
            "[mike.name] groans and I squeal as we cling onto each other."
            $ mike.love += 2
        "Guide him to my ass":
            "And that's a fucking no brainer!"
            "My pussy's so wet right now."
            "It's almost doing the thinking for me!"
            "But I still feel like playing games with [mike.name]."
            "And all it takes is a little yank on [mike.name]'s cock..."
            "The motion seems to set him on autopilot."
            "He lowers himself down and onto me."
            "And at that same time, I lift myself up just a little..."
            bree.say "Mmm..."
            show mike missionary pleasure
            bree.say "Oh, [mike.name]..."
            bree.say "Put it in my ass!"
            show mike missionary normal
            "I can't help it, there's no way I can keep quiet."
            "The moment I feel the sensation of [mike.name]'s cock between my buttocks..."
            show mike missionary anal at stepback(0.1, 10, 0)
            "It's like my whole body reacts, wanting to keep him out when I want to draw him in."
            "I can feel the hunger in him too, the need to have me."
            "But that doesn't mean [mike.name] lets himself go like an animal."
            "Instead he keeps enough control to take things slowly."
            "I can feel everything he does thanks to his patience."
            "But at the same time, I can feel the barely suppressed desire in him too!"
            "[mike.name] sinks into me a little at a time."
            "His cock fills me more with each moment that passes."
            "Part of me wants to urge him on, to demand he go faster."
            show mike missionary normal
            "But instead I bite my lip, whimpering as he goes ever deeper."
            show mike missionary at stepback(0.1, 10, 0)
            "[mike.name] pauses when he can't go any further."
            "By now he's laid atop me, his head beside mine."
            "Which means I can whisper into his ear."
            show mike missionary pleasure
            bree.say "[mike.name[0]]...[mike.name]..."
            bree.say "Fuck me..."
            bree.say "Fuck me now!"
            show mike missionary normal
            "Obedient as ever, [mike.name] springs into action at my command."
            "Well, maybe springs is a little too emphatic!"
            "But what he does do is start to move inside of me."
            show mike missionary at stepback(0.1, 10, 0)
            "Slowly at first, and then with ever more speed."
            "And the feeling on my end?"
            "Well, what can I say?"
            show mike missionary at stepback(0.1, 10, 0)
            "It's everything I want and more!"
            "Soon enough I have my arms and legs wrapped around [mike.name]."
            show mike missionary at stepback(0.1, 10, 0)
            "I'm clinging to him like I'm afraid he's going to escape."
            "But there's no chance of that, not as deep as he's going!"
            show mike missionary at stepback(0.1, 10, 0)
            "Every time he fills me, I hear myself moaning with pleasure."
            "And yet it sounds like the sounds are coming from someone else."
            show mike missionary at stepback(0.1, 10, 0)
            "Because I'm so lost in the sensations I'm experiencing..."
            "The world around me seems a million miles away."
            show mike missionary at stepback(0.1, 10, 0)
            "I'm ready to ride this thing to the end."
            "To take it as long as [mike.name] can keep on giving it."
            "But all of a sudden I feel a change in him."
            "It's like he gets a second wind, a new surge of energy."
            show mike missionary at stepback(0.1, 10, 0)
            pause 0.15
            show mike missionary at stepback(0.1, 10, 0)
            "And before I know it, his speed and intensity are increasing!"
            "Before he was sinking into me deep and slow."
            show mike missionary at stepback(0.1, 10, 0)
            pause 0.15
            show mike missionary at stepback(0.1, 10, 0)
            "Now he's pounding away like his life depends on it."
            bree.say "[mike.name[0]]...[mike.name]..."
            show mike missionary at stepback(0.1, 10, 0)
            pause 0.15
            show mike missionary at stepback(0.1, 10, 0)
            bree.say "I...I'm..."
            bree.say "I'm gonna cum!"
            show mike missionary at stepback(0.1, 10, 0)
            pause 0.15
            show mike missionary at stepback(0.1, 10, 0)
            "I'm not joking either!"
            "I can feel my whole body starting to tingle."
            show mike missionary ahegao at stepback(0.1, 10, 0)
            pause 0.15
            show mike missionary at stepback(0.1, 10, 0)
            "And then it happens, waves of pleasure spreading out from the centre."
            "I cling to [mike.name] more tightly than ever, crying out as I lose it."
            show mike missionary at stepback(0.1, 10, 0)
            pause 0.15
            show mike missionary creampie with hpunch
            "I seem to take him with me too, as I feel him cumming inside me."
            with hpunch
            "That only serves to make the feeling even more intense."
            with hpunch
            "[mike.name] groans and I squeal as we cling onto each other."
            $ mike.sub += 1
    hide mike missionary
    show mike naked
    with fade
    "Once it's over, [mike.name] rolls off me and we both start getting dressed."
    show mike casual -naked
    "Neither of us says a word until we're fully clothed again."
    "But it's like I can feel the spark that's still passing between us."
    "I just know that this game is going to be beyond exciting."
    "And we're going to have a lot of fun seeing how far we can take it."
    return

label mike_female_event_12a:
    if mike.love.max < 200:
        $ mike.love.max = 200
    scene bg mall1
    "Since [mike.name] and I agreed to the little seduction competition, I've been positively buzzing."
    "I can't wait for the chance to pit my skills against [mike.name]'s and see who comes out on top."
    "But whenever I seem to spot a likely target, he turns them down for the silliest reasons."
    "They're either too tall or too short, too fat or too skinny."
    "Or else he doesn't like the style they're trying to pull off."
    "It's like he's using any excuse that he can think of to dismiss them!"
    "I'm getting pretty tired of it, and I sense that he's aware of the fact."
    "So he tries to make amends as best he can."
    "We've come to the mall so that he can pick up something or other that he wants."
    show mike with dissolve
    "Which is when he stops me and starts to open up."
    mike.say "[hero.name]..."
    mike.say "Maybe we're going about this the wrong way?"
    bree.say "Huh..."
    bree.say "What do you mean, [mike.name]?"
    mike.say "This whole competition thing, yeah?"
    mike.say "Just pointing out random girls doesn't seem to be working."
    bree.say "Hmm..."
    bree.say "Yeah, it doesn't, does it?"
    "[mike.name] raises his arms like he's trying to show off the Mall."
    mike.say "And that's why I wanted to come here."
    bree.say "I thought you wanted to buy some junk?"
    "[mike.name] shakes his head."
    mike.say "No, [hero.name]..."
    mike.say "That was just an excuse to get you to the mall."
    mike.say "Now we're here, we can go on the hunt!"
    bree.say "The hunt?!?"
    bree.say "What are we hunting for, [mike.name]?"
    mike.say "Girls, [hero.name] - we're hunting for girls!"
    "I look around the place for a moment, thinking about what he just said."
    "The place really is full of people, hundreds, maybe even thousands of them."
    "And I know that lots of them come here to show off their and be seen."
    bree.say "You think we should actually look for a girl?"
    bree.say "Not just choose one at random?"
    "[mike.name] nods, happy that I'm finally catching on."
    mike.say "Yeah, [hero.name]..."
    mike.say "The other way wasn't working."
    mike.say "Here we can both go looking for a girl together."
    mike.say "And there's so much choice it's insane!"
    bree.say "Okay, [mike.name]..."
    bree.say "Sounds good to me!"
    "Together, [mike.name] and I take to stalking the mall."
    "We're on the lookout, searching everywhere we go."
    "No girl can hope to escape our gaze as we go on the hunt."
    "But we still seem to have the same old problem."
    "One of us spots a girl, and the other rejects her."
    "After a while, it's getting a little tiresome."
    bree.say "Okay, okay..."
    bree.say "We're getting nowhere fast."
    bree.say "We need to take a break!"
    show mike sad
    "[mike.name] nods, and I can see that he's eager to agree with me."
    "Most likely because this was his idea."
    "And he won't want to see it go south without a fight."
    mike.say "I hear you, [hero.name]..."
    mike.say "Erm..."
    show mike normal
    mike.say "Oh, I know - how about we grab a coffee?"
    bree.say "Yeah, [mike.name]..."
    bree.say "That does sound like a good idea."
    bree.say "Let's go."
    "Obviously it doesn't take us long to locate a coffee shop."
    "The mall's crammed with them, and they're all pretty decent."
    "So I don't even bother to check out the name as we walk in."
    scene bg coffeeshop
    "I just relax and allow the divine scent of the coffee to carry me along."
    "But then I see her, a few places ahead of us in the queue!"
    bree.say "[mike.name], [mike.name]..."
    bree.say "What about her?"
    bree.say "The goth girl over there?"
    "I start to point out my potential target."
    "But to my surprise, [mike.name] pushes my arm down."
    mike.say "Yeah, [hero.name], yeah..."
    mike.say "I see her, okay?"
    "I frown, surprised by [mike.name]'s reaction."
    "I always kinda thought he had a thing for goths."
    bree.say "What's up, [mike.name]?"
    bree.say "Do you know that girl?"
    bree.say "Oh...she's not an ex of yours, is she?"
    "[mike.name] shakes his head at this."
    mike.say "Sorry, [hero.name] - I didn't mean to react like that."
    mike.say "She's not an ex, but I do kind of know her."
    mike.say "Her name's Amy, and she works in the same store as Shawn."
    mike.say "He's introduced us maybe once."
    mike.say "But I don't think she'd recognise me."
    bree.say "Oh, I see!"
    bree.say "Is Shawn her boss?"
    bree.say "Like, does she work under him?"
    "[mike.name] chuckles at this and shakes his head."
    mike.say "Let's just say Shawn would like to have her under him!"
    "I gasp as I realise what [mike.name]'s implying, and then I let out a dirty giggle."
    bree.say "So is she out of bounds?"
    bree.say "Because of Shawn?"
    "[mike.name] laughs again."
    mike.say "Hell no!"
    mike.say "Fuck Shawn - she's one hundred percent a possibility."
    mike.say "I just didn't want her to see you pointing, that's all."
    "I nod, now seeing [mike.name]'s point."
    bree.say "Okay, [mike.name]..."
    bree.say "The game is afoot!"
    mike.say "Yeah, [hero.name]..."
    mike.say "Good hunting!"
    "We're both smiling as we begin to close in on the unsuspecting Amy."
    "But I know that the smiles are just for the sake of appearances."
    "From this point on, it's everyone for themselves!"
    "The only problem is that [mike.name] and I are the same distance from Amy."
    "And we're in a fucking coffee shop, so we can't go rushing over there either."
    "Which means that we both end up doing this weird trot over to her."
    show mike at left5 with move
    "I end up on her left and [mike.name] on her right."
    "I think she's reaching out to grab a coffee stirrer or something."
    "And we both reach out towards her at the same time."
    show amy embarrassed at right4, vshake
    "Amy jumps as [mike.name] and I put a hand over hers together."
    amy.say "Whoa!"
    amy.say "What the hell?!?"
    bree.say "Oh, sorry..."
    bree.say "I wanted a stirrer and I wasn't looking!"
    mike.say "Oh...oh yeah..."
    mike.say "Me too!"
    show amy normal
    "Amy pulls her hand away, already looking more than a little concerned."
    amy.say "Erm..."
    amy.say "Do you always get the stirrer BEFORE your coffee?"
    "[mike.name] and I manage to laugh nervously at the same time."
    bree.say "Okay, confession time!"
    bree.say "I needed an excuse to come over here and talk to you."
    mike.say "How weird is that?"
    mike.say "I was doing the exact same thing!"
    amy.say "Ah...yeah..."
    amy.say "That's pretty fucking weird..."
    bree.say "But weird in a good way, right?"
    bree.say "So how about it, Amy?"
    bree.say "You want to sit down and have a coffee with me?"
    mike.say "Or maybe you want me to save you from weird girls, huh?"
    mike.say "In which case you can come have a coffee with me instead!"
    if hero.charm >= 50:
        amy.say "Wait a minute..."
        amy.say "I know you, don't I?"
        "She points at [mike.name], studying him intently."
        "Which makes him squirm on the spot, like he's being interrogated."
        mike.say "Erm..."
        mike.say "I don't know about that..."
        show amy embarrassed
        amy.say "No, I DO know you!"
        amy.say "You're one of Shawn's creepy mates that's always hanging around the store!"
        amy.say "What happened - did he put you up to this?!?"
        "I sense my chance to step in and save the day."
        "Well, for myself that is!"
        bree.say "Eww!"
        bree.say "That's SO creepy!"
        bree.say "You want me to call security..."
        bree.say "Oh, sorry - I didn't get your name!"
        show amy normal
        amy.say "Amy, I'm Amy..."
        bree.say "I'm [hero.name]."
        bree.say "And YOU..."
        "I poke [mike.name] in the chest with a finger."
        bree.say "You'd better back off, mister - right now!"
        "[mike.name]'s mouth opens and closes, but no words come out."
        hide mike with moveoutright
        "Then he turns on his heel and hurries out of the coffee shop."
        "Which leaves me alone with Amy."
        amy.say "Whoa..."
        amy.say "Thanks, [hero.name] - what a fucking freak!"
        amy.say "I don't know how to thank you..."
        bree.say "Erm...well..."
        bree.say "Would a date be too much to ask, Amy?"
        "Amy looks surprised for a moment."
        show amy flirt
        "But then she seems to look me up and down with a smile."
        amy.say "You know what, [hero.name]..."
        amy.say "I think it's the least you deserve!"
        if flirtgame is not False:
            $ flirtgame += 1
    elif hero.charm >= 40:
        amy.say "Wait a minute..."
        amy.say "I know you, don't I?"
        "She points at [mike.name], studying him intently."
        "Which makes him squirm on the spot, like he's being interrogated."
        mike.say "Erm..."
        mike.say "I don't know about that..."
        amy.say "No, I DO know you!"
        amy.say "You're one of Shawn's mates!"
        mike.say "I might be..."
        amy.say "Oh come on, man!"
        amy.say "I remember you - you're [mike.name]!"
        amy.say "And I also remember you because you seemed to be a nice guy."
        amy.say "Not like some of the other creeps Shawn knows!"
        "[mike.name] looks surprised by this unexpected turn of events."
        "But Amy's on a roll."
        amy.say "And who's your friend, [mike.name]?"
        amy.say "I mean, you are together, aren't you?"
        amy.say "It's pretty obvious!"
        bree.say "I'm [hero.name], Amy."
        bree.say "And yeah, we kind of are together!"
        show amy blush
        "Realisation dawns on Amy and she looks amazed."
        amy.say "Oh...my...god!"
        amy.say "Is this some kind of game?"
        amy.say "Where couples try to pick up someone?"
        amy.say "For like a threesome or something?"
        "I look at [mike.name], and he shrugs."
        "I guess he thinks that sounds like a plan!"
        bree.say "Okay, Amy, cards on the table..."
        mike.say "You're right, we were trying to pick you up."
        bree.say "We both saw you and thought we'd like to take you on a date."
        mike.say "Just the three of us, yeah?"
        "Amy's grin is instant and genuine."
        show amy flirt
        "And she actually claps her hands together in delight!"
        amy.say "You bet I would!"
        amy.say "This is going to be SO fucking hot!"
        "Okay, so it looks like [mike.name] and I are even on this one..."
    elif hero.charm >= 30:
        amy.say "Wait a minute..."
        amy.say "I know you, don't I?"
        "She points at [mike.name], studying him intently."
        "Which makes him squirm on the spot, like he's being interrogated."
        mike.say "Erm..."
        mike.say "I don't know about that..."
        amy.say "No, I DO know you!"
        amy.say "You're one of Shawn's mates!"
        mike.say "I might be..."
        amy.say "Oh come on, man!"
        amy.say "You have to save me from this freaky girl!"
        bree.say "HEY!"
        bree.say "Who are you calling freaky?!?"
        "Even as I say this, I realise that shouting at a stranger in public is pretty freaky."
        "But at the same time, [mike.name]'s catching on fast and changing his strategy."
        mike.say "Sure thing...it's Amy, isn't it?"
        amy.say "That's right...and you're...[mike.name]!"
        mike.say "Don't worry, Amy..."
        mike.say "I'll deal with this crazy person!"
        "[mike.name] pokes me in the chest with a finger."
        mike.say "You'd better back off, lady - right now!"
        "My mouth opens and closes, but no words come out."
        "Then I turn on my heel and hurry out of the coffee shop."
        "Which leaves [mike.name] alone with Amy."
        "I pause just outside the coffee shop, listening to what happens next."
        amy.say "Whoa..."
        amy.say "Thanks, [mike.name] - what a fucking freak!"
        amy.say "I don't know how to thank you..."
        mike.say "Erm...well..."
        mike.say "Would a date be too much to ask, Amy?"
        "Amy looks surprised for a moment."
        show amy flirt
        "But then she seems to look [mike.name] up and down with a smile."
        amy.say "You know what, [mike.name]..."
        amy.say "I think it's the least you deserve!"
        "Damn it - looks like that's one for [mike.name] and a big fat zero for me!"
        if flirtgame is not False:
            $ flirtgame -= 1
    else:
        "With [mike.name] and I advancing on her, Amy seems to feel threatened."
        show amy angry
        "She takes a step backwards and holds up her coffee like it's a weapon."
        amy.say "Look, you creeps..."
        amy.say "I don't know what kind of deal you've got going on here."
        amy.say "But I'm not going to get caught up in it."
        amy.say "I've read stories about people like you."
        amy.say "Your victims wake up in a motel bathroom full of ice..."
        amy.say "And with their kidneys missing too!"
        "[mike.name] and I exchange a meaningful look."
        "And without the need to say a word, we each know the score."
        "We blew it this time, and we only have ourselves to blame."
        "We both hold up our hands and follow Amy's example."
        "Stepping backwards we make sure to offer no obstacle to her."
        hide amy with moveoutright
        "And she takes the chance, slipping out of the coffee shop as quickly as she can."
        "We stand there in silence for a moment, watching her go."
        "Then I snort and shake my head."
        bree.say "Erm...yeah..."
        bree.say "I kinda think we got in our own way there, [mike.name]!"
        mike.say "Yeah, [hero.name], yeah..."
        mike.say "But at least you never met her before now."
        mike.say "Fuck knows what she's going to tell Shawn if she remembers me!"
        if flirtgame is not False:
            $ flirtgame -= 2
    return

label mike_female_ending:
    $ game.hour = 16
    $ game.room = "church"
    $ game.season = 1

    scene bg church wedding with fade
    "I'm not gonna try to be all edgy and different by pretending I haven't thought a lot about this moment."
    "Because just like every girl out there, I've spent ages planning out the day of my wedding inside my head."
    "But the reality is that when it actually happens, it's so much more scary and exciting, all at the same time."
    "I mean, part of me still can't believe that I'm really marry [mike.name], of all people!"
    "Okay, okay...I know how that sounds, but hear me out."
    "At first he was just a housemate that I found I liked hanging out with."
    "Then he became that rarest of things, a really good male friend."
    "But my feelings kind of crept up on me, and before I knew it, I was falling for the guy."
    "I can't explain how it happened, it just did."
    "I fell for his goofy jokes and his silly obsessions."
    "Oh, and the fact he's a sweet, loving person obviously helped."
    "And now here I am, standing outside the doors to the chapel, waiting to walk in."
    "Sure, we discussed whether or not we should do things the traditional way or not."
    "We could have both been at the altar from the start of the ceremony."
    "Hell, [mike.name] even joked that he should be the one to walk down the aisle!"
    "But in the end we decided that we'd just go with the groom at the altar and the bride coming down the aisle."
    "I'm already worried about dad's head exploding any time I mention [mike.name]."
    "So anything that raises his blood pressure is probably not a good idea."
    if hero.pregnant:
        "I'm thinking about this as I cradle the curve of my belly in both hands."
        "Which makes me wonder if the cut of my dress really is that flattering to it!"
        "But there's no time to worry about that right now."
        "Plus [mike.name] and I are proud of the fact we're going to be starting a family together."
        "So I'm not going to let that intimidate me either."
    else:
        "It's at times like this when I'm glad we didn't add anymore stress into the mix."
        "Like, imagine if we'd not been so careful when we were having fun together."
        "And I was standing here, visibly pregnant with [mike.name]'s kid!"
        "I guess I should be thankful for small mercies like that."
    "All of this and more is running around inside of my head when I hear something from inside the chapel."
    "It seems really familiar, but I just can't seem to place it."
    "Straining to listen, it suddenly hits me - that's the music we chose for me to enter to!"
    "Shaking myself in an effort to wake my brain up, I shove the doors open."
    "And then I walk into the chapel, doing the best I can to look confident as I do so."
    "But of course it doesn't work."
    "I'm walking straight into a confined space, packed with my friends and family."
    "Plus every head in the place is turned to look in my direction too!"
    "Part of me wants to turn on my heel and run right out of there."
    "But then I happen to look up."
    show mike b wedding smile at center, zoomAt(1.0, (640, 740)) with dissolve
    "And I see [mike.name], waiting for me at the altar."
    "I swear it's only the look on his face that makes me change my mind."
    "He's got that big, dumb smile on his face, like he's dumbstruck at the mere sight of me."
    show bg church wedding at center, traveling(1.25, 3.0, (640, 900))
    show mike b at center, traveling(1.5, 3.0, (640, 1080))
    "That's what makes me take one step forwards, and then another."
    "The urge to close the distance between us, so that I can get to [mike.name]."
    "I so badly want to hear what he has to say to me that I forget all about my fears."
    "I can't hear the music anymore, and I can hardly see the guests filling the pews."
    "All I want to do is make it over there to him, because he's all that matters to me."
    show wedding mike with fade
    "It seems like all I have to do is blink, then I'm standing right beside [mike.name]."
    mike.say "[hero.name]..."
    mike.say "You look..."
    mike.say "I mean..."
    mike.say "Just look at you!"
    "For a moment I'm confused by [mike.name]'s getting so tongue-tied."
    "But then I remember this is the first time he's seen me in the dress."
    "So I do a quick turn on the spot for his benefit."
    bree.say "Why, thank you, [mike.name]..."
    bree.say "You look very handsome too!"
    "I see [mike.name]'s cheeks flush a little at the compliment."
    "Which is so cute I want to kiss him, right there and then."
    "Priest" "I think we've established that everyone looks very fetching."
    "Priest" "So shall we begin?"
    show wedding mike priest with dissolve
    "As one, [mike.name] and I snap to attention as the priest addresses us."
    "We're nodding and doing the best we can to get into position at the same time too."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these two people in the bonds of holy matrimony."
    "You know how the rest of the ceremony goes."
    "And the truth is that most of it is a blur to me."
    "It's a wonder that I remember when I have to speak up along the way."
    "Priest" "Do you, [hero.name]..."
    "Priest" "Take this man, [mike.name]..."
    "Priest" "To be your lawful, wedded husband?"
    bree.say "I do!"
    "Priest" "And do you, [mike.name]..."
    "Priest" "Take this woman, [hero.name]..."
    "Priest" "To be your lawful, wedded wife?"
    mike.say "You bet I do!"
    "The priest seems slightly amused by [mike.name]'s enthusiasm."
    "But he remains professional, pushing on with the ceremony."
    "Priest" "I call upon those here present..."
    "Priest" "That if they know of any lawful reason..."
    "Priest" "Why these two may not be wed..."
    "Priest" "Speak now, or forever hold your peace!"
    "There's the usual awkward silence, in which most of the guests chuckle away."
    "But I'm actually biting my lip, praying that my dad keeps his big mouth shut."
    "And to my immense relief, he actually does so!"
    "Priest" "Very good..."
    "Priest" "It is therefore my pleasure to pronounce you husband and wife."
    "Priest" "You may kiss the groom."
    show wedding mike -priest with dissolve
    "I don't hesitate to act on the invitation."
    "In fact I seem to have taken [mike.name] by complete surprise."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show mike kiss wedding
    with fade
    $ mike.flags.kiss += 1
    "Because he ends up being the one to get bent over as I kiss him!"
    "Thankfully he soon recovers, and the kiss becomes a more even affair."
    "But neither of us seems to feel the need to apologise or stop for a moment."
    "And that's because we're married now, and there's going to be time for that later."
    hide mike kiss
    show mike wedding b smile at center, zoomAt(1.5, (640, 1080))
    with fade
    "Right now all we want to do is celebrate that fact, and to hell with anyone else."
    "We did it, we're married!"
    "And this is the beginning of the rest of our lives."

    scene bg park
    show mike ending
    with fade
    mike.say "I'm going to do this thing - but it's got to be a one-time deal!"
    mike.say "I can't imagine anyone wanting to hear me do this all the time..."
    mike.say "So, me and [hero.name]...[hero.name] and me..."
    mike.say "I guess the best thing would be to start at the start?"
    mike.say "So I was kinda bummed-out at the time [hero.name] moved into the house."
    mike.say "Ryan had just moved out, taking Sam along with him."
    mike.say "And their lives looked like a proper fucking fairy-tale to me."
    mike.say "But I was losing the girl I thought that I loved to a massive prick."
    mike.say "All that made me kind of resentful to whoever was going to be taking their places."
    mike.say "But then [hero.name] walked into the house and into my life."
    mike.say "And all of a sudden, I found myself forgetting all about Sam."
    mike.say "Well, maybe not completely - I still sort of held a torch for a while there."
    mike.say "But the important thing was that my relationship with [hero.name] was so very different."
    mike.say "What does that mean?"
    mike.say "Well for one thing, I wasn't smitten with her from the first moment we met."
    mike.say "Of course I couldn't help noticing the fact that she was totally gorgeous."
    mike.say "But my lingering feelings for Sam sort of kept me from seeing it at the start."
    mike.say "No, what made me warm to [hero.name] so quickly was the fact we had a lot in common."
    mike.say "That and just the fact she was so much fun to be around, you know?"
    mike.say "Before I knew what was happening, we were playing on the Z-Box together."
    mike.say "Hanging out around the house and laughing together like old friends."
    mike.say "I guess that's what became the foundation of our relationship."
    mike.say "We were friends before we became anything more - and we're still friends now."
    mike.say "Things with [hero.name] seemed to evolve naturally, without either of us noticing at first."
    mike.say "Hanging out turned into grabbing drinks together down the pub."
    mike.say "Everyone else was there to begin with, but soon it became just the two of us."
    mike.say "Our nights out together kind of turned into dates without me realising it."
    mike.say "And so, by the time our feelings were growing, it just seemed natural."
    mike.say "But don't think I mean it was all like, yeah, whatever!"
    mike.say "Realising that [hero.name] and I were becoming more than friends was amazing."
    mike.say "Those first kisses and intimate moments..."
    mike.say "Oh man!"
    mike.say "I'm getting goosebumps just remembering them!"
    mike.say "So yeah, admitting our feelings to ourselves and each other was a total rush!"
    mike.say "I'd like to say that it was all plain-sailing from there and we never looked back."
    mike.say "But we did hit a couple of bumps along the way."
    mike.say "One of the biggest being [hero.name]'s dad."
    mike.say "What a prick he was!"
    mike.say "And still is..."
    mike.say "But anyway, fuck him."
    mike.say "We're married now and there's nothing he can do about it."
    mike.say "Having [hero.name] in my life focussed me in ways I'd never imagined possible."
    mike.say "Before her, I went to work and did as little as I could to get by."
    mike.say "But now I march in there every morning and work my damn ass off!"
    mike.say "And all because I have her to come home to in the evening."
    if hero.pregnant:
        mike.say "Oh, and then of course there's Poppy!"
        mike.say "I can't forget that I'm working to provide for my little man too."
        mike.say "I maybe should have mentioned that we're a family now."
        mike.say "But you did ask me to start at the start, so that's on you."
    else:
        mike.say "And I have all the motivation I need to work harder still."
        mike.say "Because I get the feeling we're going to be starting a family soon."
        mike.say "I mean, [hero.name] hasn't come right out and said as much yet."
        mike.say "But I keep seeing the way she looks at people with their kids."
        mike.say "That can only mean that she's getting broody, right?"
        mike.say "And who knows, maybe grandkids will finally make her damn dad happy too..."
    mike.say "[hero.name]'s career took off like a rocket too, after we got married."
    mike.say "She's a biologist, and a really good one too."
    mike.say "Ah, man - I'm so damn proud of her!"
    mike.say "She even writes books and stuff like that."
    mike.say "We still manage to catch up to Sasha every once in a while."
    mike.say "Ask her how things are going with the band and if she's back with Scottie again."
    mike.say "But [hero.name] and I are both secretly glad not to have to listen to her practice anymore!"
    mike.say "And since Sasha moved out, we have the house all to ourselves."
    mike.say "So it's kind of become our own little castle!"
    mike.say "Though [hero.name] keeps hinting that we should think about buying a place of our own."
    mike.say "And with the money that we're both bringing in, I think it's only a matter of time."
    mike.say "Oh, and we still manage to play on the Z-Box together, just like before."
    mike.say "Only some of the games we like to play, they're now calling retro!"
    mike.say "Can you believe that?!?"
    mike.say "It's like they're trying to fool us into thinking we got old or something!"
    mike.say "And I still beat [hero.name] when we play."
    mike.say "Well...at least some of the time anyway."
    mike.say "What?"
    mike.say "I have to say something clever and philosophical to finish off?"
    mike.say "Well you could have told me that before we got started!"
    mike.say "Erm..."
    mike.say "Okay, I got something!"
    mike.say "Guys, if you get the chance, always marry a gamer-girl."
    mike.say "Because they're totally awesome!"
    mike.say "Huh?"
    mike.say "What was wrong with that?"
    mike.say "Well screw you guys, I thought it was very philosophical!"
    scene bg black with dissolve
    pause 0.3
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label mike_female_wedding_invite:
    "You always come across those types of guys that are just the worst at hiding their motivations, you know?"
    "The ones that, when they want to ask you something that's awkward for them, they can never just come out with it straight."
    "They hang around, havering and trying to find a way to make you ask them what's the matter to keep from speaking up themselves."
    "[mike.name]'s a prime example of that type - and he's doing it to me right now."
    show mike blush
    "I think he's made about three attempts to spit out whatever he has to say to me since he stopped me as I passed him."
    "And now he's going red from embarrassment and rubbing the back of his head like he has lice."
    mike.say "I...erm, that is...I just wondered if..."
    "I roll my eyes, trying not to look too exasperated with him."
    bree.say "[mike.name], just come out and say it, yeah?"
    bree.say "Do you need something?"
    mike.say "No..."
    bree.say "Do you want something?"
    mike.say "Not really..."
    bree.say "Do you want to ask me something?"
    mike.say "Yes..."
    bree.say "Well, what is it?"
    "[mike.name] begins to mumble again, but I can see that he's clutching a crumpled piece of paper in his hand."
    bree.say "Is it something to do with that?"
    "He looks down at the paper in surprise, as if he'd forgotten it was even there."
    mike.say "Yes...that's it - I wanted to ask if you'd come with me?"
    "I can't help but begin to chuckle, realising that he's remembered what he wants to ask me, but not why."
    bree.say "Come with you to what, [mike.name]?"
    mike.say "To the wedding...I need a plus one."
    mike.say "Would you come, [hero.name] - you'd be doing me a massive favour if you did?"
    bree.say "Maybe I'd be more likely to say yes if you actually told me who was getting hitched?"
    "[mike.name] looks taken aback for the second time in the space of a couple of minutes."
    "I can see that, whoever the happy couple might be, the fact that he's been invited to the wedding has got him in a complete spin."
    mike.say "Sam and Ryan, you know them?"
    "The names are familiar, as if I've heard him mention them before now."
    "But I still can't quite put my finger on just who they are and what their relationship to him might be."
    "I shake my head and shrug my shoulders, smiling the whole time."
    mike.say "They used to live here, with me...before you and Sasha moved in?"
    "Ah, that Sam and Ryan!"
    "I don't think [mike.name] ever showed me pictures of them."
    "But I got the distinct impression that he and Ryan were rivals, rather than actual friends."
    "And as Sam is most likely short for Samantha and the pair are getting married..."
    "Well, it doesn't take a genius to guess what the rivalry was about, does it?"
    "Feuding friends, a potential love-triangle and all at the same wedding I'm being invited to crash."
    "Can I say no to a front-row seat?"
    "But, of course, that doesn't mean I can't bust [mike.name]'s chops a little before I give him my answer..."
    bree.say "Did you ask Sasha already?"
    bree.say "Because she might be jealous if I say yes and you didn't!"
    "[mike.name] starts to blurt an answer, but I cut him off before he can get it out."
    bree.say "Wait a minute - DID you already ask Sasha?"
    bree.say "If you did and she said no, then am I your SECOND choice for a plus one?!?"
    mike.say "[hero.name], please!"
    mike.say "I didn't ask Sasha yet, because I wanted to ask you first!"
    bree.say "Oooh, [mike.name] - she's going to be really pissed when she finds out she's your second choice!"
    show mike normal
    mike.say "Can we leave Sasha out of this?"
    mike.say "Are you going to come to the wedding or not?"
    menu:
        "Refuse the invitation":
            bree.say "You know what, [mike.name] - you should have asked Sasha first."
            show mike sad
            "He looks at me almost with desperation in his eyes."
            mike.say "You mean..."
            bree.say "Yeah, [mike.name] - I'm gonna have to pass on this one, sorry."
            bree.say "I know you've got unresolved issues with these guys."
            bree.say "And I don't want to get dragged into it too."
            bree.say "Maybe you should ask Sasha - she might enjoy the drama?"
        "Accept the invitation":
            bree.say "Okay, [mike.name] - you got your precious plus one!"
            show mike happy
            "His face instantly lights up at the news."
            bree.say "But we need to establish some ground rules, okay?"
            show mike normal
            "Now I can see trepidation stealing in to dampen his mood."
            mike.say "Erm, okay..."
            bree.say "For one thing, I'm coming as your friend."
            bree.say "Don't go introducing me as your fiancee or anything like that."
            mike.say "I guess so..."
            bree.say "Also, any and all hand-holding, dancing and miscellaneous touching will be at my discretion."
            mike.say "Yeah, whatever - so long as you're coming, right?"
            bree.say "If all that's understood, then yes, I'm in."
            $ mike.flags.acceptweddinginvite = True
    "[mike.name] wanders off, still looking a little bit dazed and out of it."
    "If just getting the invitation through the post is enough to get him so wound up and out of it, then what will he be like at the actual wedding?"
    return

label mike_female_livingroom_bj:
    "I think that I knew what we were watching on the TV when I first slumped down on the sofa and flicked it on."
    "But that must have been more than an hour ago now, and in that time, Sasha and [mike.name] have both come and gone more than once."
    "Every time one of them arrives, they seem to manage to change the channel without me noticing."
    "Which means that I keep thinking the original show I was watching has had some crazily random plot twists in this episode."
    "By the time Sasha finally announces that she's turning in for the night, I'm thinking that I should be doing the same."
    "My eyes are already getting heavy and it's all that I can do to keep from yawning every couple of seconds too."
    "But just as I'm about to lift my weary head and mumble words to that effect, I see that [mike.name]'s well awake and watching me from the other end of the sofa."
    "What intrigues me enough to put off going straight to bed is the look in his eyes."
    "The last time that I can recall seeing it, he was gazing longingly at a huge pizza while crazily hungry."
    "It only takes a quick glance down to see what the actual cause is."
    "[mike.name] has his hand inside of his shorts, and it looks as though he's smuggling a canoe down there right now!"
    "My gaze travels back up to meet his own, and we exchange what passes for a knowing glance."
    bree.say "What's up, [mike.name] - you got a problem down there?"
    mike.say "Um, yeah...maybe you could..."
    mike.say "I don't know...help me out with it?"
    "He smiles awkwardly, trying to look nonchalant, like he tosses out lines like that to me all the time."
    "I try not to smirk, amused by how much he sounds like something out of a cheap porno film."
    menu:
        "Refuse to give [mike.name] a blowjob":
            $ mike.love -= 2
            "I give [mike.name] a wide smile, fluttering my eyelids in his direction and looking down at his crotch."
            bree.say "Oh, I'd love to, [mike.name]."
            bree.say "But didn't I tell you - I'm on a strictly non-sausage diet for the rest of the month."
            bree.say "Doctors orders, I'm afraid!"
            "I haul myself up from the sofa as he opens his mouth to protest."
            bree.say "So if you're having trouble with the wiener in your shorts, I'd suggest you tackle it yourself!"
            "I pluck a cushion up from the sofa as I walk past where he's sitting, and then hurl it at him."
            "Walking through the door a moment later, I don't have the pleasure of seeing it hit the intended target."
            "But the sound of [mike.name]'s pained cry behind me is reward enough in of itself."
        "Agree to give [mike.name] a blowjob":
            $ mike.love += 2
            "I really should just say no and go get some much needed sleep."
            "But all the same, there's just something wicked inside of me that can't help being turned on by the request."
            "I'm pretty keen on [mike.name] anyway, and I've already seen the goods, which adds to the appeal."
            "Though it's the chance to be spontaneous that really makes my mind up for me."
            "Well...that and the danger of being caught in the act by Sasha too!"
            "Without saying a word, I lean forwards and lower myself onto my belly."
            "And then I crawl the short distance between us, until I'm leaning across [mike.name]'s thighs."
            "His hand is still shoved down his shorts, and so I slap his wrist until he hastily yanks it out."
            "I look up at him with a raised eyebrow, as if scolding him for having the audacity to get in my way."
            "Taking hold of the waistband of his shorts, I tug them down until his cock is fully exposed."
            "Strained against the elastic, it bobs up as soon as it's free, almost slapping me on the end of the nose."
            bree.say "Whoa there..."
            bree.say "Hello Mr Enthusiastic!"
            show bj breesasha bree
            "Reaching out with one hand, I begin to stroke the length of his shaft, pouting a little as I do so."
            bree.say "Hmm...you took all of the fun out of getting it all stiff..."
            bree.say "Oh well, I guess I'll just have to work twice as hard to make up for it, won't I?"
            "At this, I give [mike.name] an evil wink."
            bree.say "Just tell me one thing - did you get THIS big thinking about me?"
            "It doesn't really matter either way, as I'm going to suck his cock no matter what the answer."
            "And I know that guys can get random erections at the strangest of times and places."
            "But it's fun to see him nod furiously, as though I won't touch his dick unless it's stiff for me."
            bree.say "Well, then I'd be VERY rude to refuse to put it in my mouth, wouldn't I?"
            bree.say "Just plain ungrateful if I didn't lick it and suck on it..."
            "And with that, I raise my head so that I can place a kiss and a tiny lick on the very tip of his cock."
            "I can't help giggling as I feel a shiver run through him, going from head to toe."
            bree.say "Mmm...cock that's hard for me tastes SO good!"
            show bj breesasha breesuck breeclosed
            "Before he can as much as draw a single breath, I wrap my lips around the head and caress it with my tongue."
            "I keep on watching him as I take ever more of it into my mouth, as if seeking his approval the whole time."
            "Of course, he's gripping the sofa like his life depends on it."
            "But he gasps and nods frantically all the same."
            "Taking his cue, I swallow him as completely as I can manage in one move."
            "I hear [mike.name] gasp at the sensation, and the corners of my mouth tug into what would otherwise be a smile."
            "All this time I've been warming my hands, and now I use one to cup his balls and the other to encircle the base of his cock."
            "Knowing that I can only do so much with him this deep in my mouth without choking, I used them to compensate."
            "One hand squeezes his balls, now gentle, now hard."
            "The other travels up and down the portion of his shaft not inside of my mouth."
            mike.say "Ah..shit..."
            mike.say "[hero.name]...that's...that's..."
            "I choose to take the fact that he can't even finish the sentence as a seal of approval on my efforts."
            "After all, it's always nice for a girl to feel appreciated!"
            "Speaking of his showing his gratitude - I sense a sudden twitching at the base of his cock."
            menu:
                "Take it on the face" if hero.morality < -50:
                    $ mike.love += 2
                    $ mike.sub -= 1
                    if hero.morality > -75:
                        $ hero.morality -= 1
                    "I let [mike.name]'s cock slide out of my mouth the moment before he cums."
                    "This means that I'm looking right at his cock when it actually happens."
                    "I thought I was ready for it, but it hits me harder and faster than I was expecting."
                    "And there's a lot more of it too - I guess he really was bursting to get it out!"
                    "I gasp and splutter as [mike.name] paints my face with sticky white streaks."
                    "There's nothing I can do to keep some of it from getting in my mouth either!"
                    "When he's finally done cumming, I collapse onto the sofa as it runs down and drips from my chin."
                "Take it in the mouth":
                    show bj breesasha breecummouth
                    "And a moment later, [mike.name] cums in my mouth with all of the pent up energies I've stoked inside of him."
                    menu:
                        "Spit out [mike.name]'s cum":
                            show bj breesasha breewink normal wet -breecummouth
                            "As I lift my head and release his cock from my mouth in the same motion, I allow the cum to seep out too."
                            "It dribbles from between my open lips and down over [mike.name]'s cock, glistening as it comes."
                            "I make no effort to close my mouth until the very last of it has slid off of my tongue, mixed with my saliva."
                            "And then I watch as it runs down his shaft, making it look like a novelty candle form a fetish shop."
                            "Licking my lips, I point to his now sagging cock."
                            bree.say "Clean yourself up, [mike.name] - you've gotten yourself into a terrible mess!"
                        "Swallow [mike.name]'s cum" if hero.morality < -25:
                            "I've worked damn hard for this, and so I'm not about to let a single drop of my reward go to waste."
                            show bj breesasha breewink cumshare -breecummouth
                            $ mike.love += 1
                            "Sucking at [mike.name]'s cock as though my life depends upon it, I swallow all that he has to give me."
                            "Gasping for breath and licking my lips, I release him and almost roll over on the sofa in exhaustion."
                            "I'm a sweaty mess, still cleaning the last drops of his cum from my chin with the back of my hand."
                            "But by way of contrast, I've never seen [mike.name]'s cock looking more pristine."
                            "I smile at him weakly as he begins to droop, my own breathing finally starting to return to something like normal."
            hide bj breesasha
    return

label mike_female_shower_bj:
    "It's been a long day, and all that I can think about doing right now is stepping into a steaming hot shower to wash the worst of it away and then collapse into bed."
    $ renpy.sound.play("sd/shower.ogg", loop=True)
    "I start the water running and leave it to get to that elusive point where it's just right before I get inside, brushing my teeth and taking care of other small tasks while I wait."
    "As soon as I'm done, I shove a hand inside and find that the temperature's not quite perfect, but good enough for me to jump in regardless."
    "It only takes a couple of minutes standing under the cascade of water for me to begin feeling the effects in the best way possible."
    "Muscles that have been tense all day are now loosening and knots in my body that I had no idea were even there fall away as the warmth seeps into my limbs."
    "I take my time over actually getting cleaned up, doing all that I can to make it an extension of relaxing."
    "And yet I'm still done well before I'm ready to get out of here."
    "Guilt tells me that I'm just wasting water staying in here any longer, not to mention hogging the bathroom."
    "Worse still, my brains just too tired to come up with a good enough excuse to ignore all of that as well!"
    "But then, as if in answer to my prayers, I hear the sound of the bathroom door opening."
    mike.say "Erm...hello?"
    mike.say "Sasha...[hero.name]?"
    mike.say "Who's in here?"
    "I open the shower door just enough to stick my head out."
    show mike blush with dissolve
    "And I can see [mike.name] doing pretty much the same thing on the other side of the bathroom."
    bree.say "It's me, [mike.name] - just in the shower."
    "He looks more than a little embarrassed at having disturbed me, immediately beginning to apologise."
    mike.say "Oops, sorry!"
    mike.say "I just needed to use the facilities - but I'll go downstairs instead."
    menu:
        "Let [mike.name] go downstairs":
            bree.say "Don't let me keep you from answering the call of nature!"
            hide mike with dissolve
            "[mike.name] nods a little awkwardly and ducks back out of the bathroom, leaving me to wrap up my shower in peace."
            "A few minutes later, I hop out and wrap myself in a towel before heading to my own room and bed."
        "Tell [mike.name] to go ahead and use the toilet in the bathroom" if hero.morality < 25:
            $ mike.love += 1
            bree.say "It's okay, you can just go ahead and use the one in here - so long as it's not a sit-down affair."
            mike.say "Are...are you sure?"
            bree.say "Don't be a prude, [mike.name]!"
            bree.say "Besides, the glass is all steamed-up anyway."
            bree.say "And the sound of the water means I won't hear a thing."
            mike.say "Umm...okay - if you say so!"
            hide mike with dissolve
            "[mike.name] hurries into the bathroom as I close the shower door."
            "He doesn't need to know that I can see him perfectly well, as it'd only make him feel self-conscious."
            "Truth be told, I like playing the part of the laid-back female housemate."
            "The one that's almost like another guy, but still gets him hot under the collar."
            "I know it's a cheap thrill, watching him as he has his cock in his hand."
            "But what [mike.name] doesn't know won't hurt him."
            "Once he's done, [mike.name] nods a little awkwardly and ducks back out of the bathroom, leaving me to wrap up my shower in peace."
            "A few minutes later, I hop out and wrap myself in a towel before heading to my own room and bed."
            scene bg bedroom4 with fade
            "I fall asleep with the mental image of his dick still on my mind."
            $ game.room = "bedroom4"
        "Invite [mike.name] into the shower for a blowjob" if hero.morality < -25 or (mike.sexperience and hero.morality < 50):
            bree.say "Why would you want to do that?"
            bree.say "Go up here and then hang around afterwards."
            bree.say "If you do, I promise that I'll do something for you with it that's much more fun!"
            $ mike.love += 2
            "I really don't know where the urge to suddenly get so flirty and frisky with [mike.name] comes from."
            "Just a couple of minutes before I was ready to get out of the shower and jump straight into bed."
            "Maybe it's the relief of being loosened up by the shower, or the fact that he's coming in here with his dick on his mind."
            "I know this makes me sound like some kind of cock-crazed hussy - but all I have on my mind right now is the exact same thing!"
            "I guess that with the stress of the day finally washed away, I've got the head-space to start thinking about more enjoyable stuff."
            mike.say "Do...do you mean what I think you mean?"
            bree.say "Tell you what - you take care of business and then join me in here."
            bree.say "Then we can see if I am or not!"
            hide mike with dissolve
            "I can't suppress the laughter that slips out as I close the door on [mike.name], seeing how he hurries to attend to the call of nature."
            "The sound of him hastily stripping his clothes off follows soon afterwards."
            "And it can't be more than a few seconds later that he opens the shower door and steps nervously inside."
            "It's sweet that he's so eager and yet still showing trepidation, so I start out being gentle with him."
            "At first all he gets is a chaste kiss on the lips, followed by another on the side of his jaw."
            "Next come his neck, and then his chest, as I make my way downwards."
            scene mike shower bj with fade
            "By the time I'm crossing his stomach and going below his waist, I'm also sinking down onto my knees."
            "My hands follow, tracing parallel lines down the side of his body until they come to rest on his thighs."
            "Needless to say, [mike.name]'s already perked up a great deal since he joined me in the shower."
            "This means that he needs only a little bit more encouragement from me to get him standing to attention."
            "I give this to him by wrapping my lips around the very tip of his cock, just enough to be able to lick at it with my tongue."
            "Keeping my head still, I coax him fully erect and at the same time manage to make the rising of his cock push the head further into my mouth."
            show mike shower bj mouth
            show sexinserts head bree zorder 1 at center, zoomAt(1, (720, 810))
            "This means that by the time he's as big as he's going to get, he's already in there and feeling the sensation of my tongue around him."
            "Only now that he's inside of my mouth do I actually touch his cock with my hands, encircling it with a finger and thumb and then rubbing gently up and down."
            "[mike.name]'s leaning back against the tiled wall by now, his head leant back so that the water from the shower is streaming down over his face."
            "I can hear him moaning at the feeling of what I'm doing to him, overcome by the moment."
            "And he's not the only one enjoying himself either."
            "The feeling of his cock in my mouth is better than I could have imagined it to be."
            "Warm and slippery, washed totally clean by the water of the shower."
            "It's so good to caress that I just don't want to let it go."
            "But I'm going to have to soon, as I can tell from [mike.name]'s suddenly changing his posture that he's on the brink of cumming."
            $ mike.flags.showerbj = True
            menu:
                "Aim it at the floor" if hero.morality >= 25:
                    $ mike.love -= 1
                    $ mike.sub += 1
                    if hero.morality >= 25:
                        $ hero.morality -= 1
                    "This may be all fun and games for [mike.name], but there's a limit to what I'm going to let him do to me."
                    "The thought of letting him shoot his entire load into my mouth is just too disgusting to think about."
                    show mike shower bj -mouth cumshot bodycum
                    hide sexinserts
                    "And so as he finally cums, I make sure his cock is nowhere near my mouth and pointed safely down at the floor of the shower cubicle."
                    "All the same, I keep on smiling up at him in a demure and pleasant manner."
                    "After all, I don't want him to know how much I loathe the idea of swallowing his cum, now do I?"
                "Spit it out" if -25 <= hero.morality <= 0:
                    if hero.morality >= 0:
                        $ hero.morality -= 1
                    "Opening my mouth as wide as I can manage, I let [mike.name] release himself straight onto my tongue without even flinching."
                    show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
                    "I manage to catch almost all of it and then close my mouth again, smiling up at him to make it plain I enjoyed the experience."
                    show mike shower bj -mouth cumshot bodycum
                    "The cum washes around in my mouth for a few moments, and then I choose a convenient opportunity to discreetly spit it out again."
                    hide sexinserts
                    "[mike.name] doesn't see me doing this, and even if he did, he can't begrudge me anything after what I just let him use my mouth for!"
                "Swallow" if -50 <= hero.morality <= -25:
                    $ mike.love += 1
                    if hero.morality >= -25:
                        $ hero.morality -= 1
                    "I kneel before [mike.name], my mouth wide open and my tongue sticking out, hoping that I don't look too much like an eager dog as I do so."
                    "The moment that he cums, I can't help rising up on my haunches, just a little, in order to make sure that I catch the whole thing."
                    show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
                    "The white streamers land mostly on my tongue, some dripping onto my chin before I can curl it and save them from being lost."
                    "Soon I have a veritable mouthful of cum, all pooled in the middle of my tongue."
                    show sexinserts head bree -cum zorder 1 at center, zoomAt(1, (720, 810))
                    "I swallow it down slowly and with a look of infinite satisfaction on my face, savouring like it was a rare delicacy or a fine wine."
                    hide sexinserts
                    "Finally, I lick my lips for the last few droplets, relishing every single speck that I can find."
                "Finsh with a bang" if hero.morality <= -50:
                    $ mike.love += 2
                    $ mike.sub -= 1
                    if hero.morality > -75:
                        $ hero.morality -= 1
                    "Slowly I draw him out of my mouth, teasing him with tongue, teeth and lips one final time."
                    "He loses it just as I pull the head of his cock between my lips in a last kiss."
                    show mike shower bj -mouth cumshot facial
                    hide sexinserts
                    "This means that a little of his cum clings to my lips, but the rest is able to erupt in the open."
                    "It does so less than an inch from my face, meaning that I get showered in tight, looping whorls even as the actual shower washes them away again."
                    "I make no effort to speed the water's efforts to cleanse me of [mike.name]'s cum, instead smiling up at him in amusement."
            "Neither of us speaks as we let the shower clean us up one final time."
            "But I note that [mike.name] silently takes hold of my hand as we walk out of the bathroom, not letting go until we reach my bedroom door and I slip inside."
            scene bg bedroom4 with fade
            "Sleep comes easily after that, and the last thing on my mind before I drift off is the feeling of his cock between my lips."
            $ game.room = "bedroom4"
    stop sound
    return

label mike_preg_talk:
    $ mike.flags.toldpreg = True
    $ mike.flags.know_is_father = True
    show mike
    "Urgh..."
    "This is going to be like pulling the plaster off of a wound."
    "I can either do it slowly and experience long, drawn out pain."
    "Or I can rip it straight off and then wait for the pain to hit me."
    "So I'm going to choose the latter option and get it over with."
    "Luckily, [mike.name] and I live under the same roof as each other."
    "Which means tracking him down to tell him is the easiest part."
    bree.say "[mike.name]..."
    mike.say "Oh..."
    mike.say "Hey, [hero.name]!"
    mike.say "Wow...you look good."
    mike.say "You're practically glowing!"
    "I can't help flushing a little as [mike.name] offers me the compliment."
    "Isn't that what people usually say to a pregnant woman?"
    "Does he know what I'm about to tell him already?"
    "I mean, he's not exactly the kind of guy who spots that stuff."
    bree.say "Ah..."
    bree.say "Yeah, [mike.name]..."
    bree.say "Here's the thing - that's because I'm kinda pregnant!"
    "[mike.name]'s eyes pop open at the mere mention of the word pregnant."
    "In fact, they almost pop out of his head!"
    mike.say "Are you serious, [hero.name]?!?"
    mike.say "I mean, like really serious?"
    "I can't help frowning at this, crossing my arms over my chest."
    "What does he think this is, a fucking stand-up audition?"
    bree.say "Of course I'm serious, [mike.name]!"
    bree.say "You don't think I'd joke about something so serious, do you?"
    mike.say "No, [hero.name]..."
    mike.say "No, of course not."
    mike.say "And...do you know who the father is?"
    "Now it's my turn to have my eyes go wide."
    "I stare at [mike.name] in sheer amazement."
    "And I shake my head in disbelief."
    bree.say "Of course I do, [mike.name]!"
    bree.say "It's you, you dumbass!"
    bree.say "Why do you think I'm telling you?"
    bree.say "Or do you think I've been sleeping around behind your back?!?"
    "[mike.name]'s lips start moving, but no words come out."
    "So all I can do is stand there and wait."
    "Wait for his brain to catch up with his mouth."
    if mike.love >= 150:
        mike.say "No way, [hero.name]!"
        mike.say "No fucking way!"
        mike.say "You mean I'm going to be a dad?"
        "I'm almost too shocked to take in [mike.name]'s reaction."
        "I'd prepared myself for the worst possible scenario."
        "Like that he'd instantly freak out and leave me."
        "But I never really planned for him being over the moon."
        bree.say "Y...yeah, [mike.name]!"
        bree.say "I'm gonna be a mommy and you're gonna be a daddy."
        "[mike.name] makes to reach out and touch my stomach."
        "But then he stops himself and looks up at me."
        mike.say "C...can I, [hero.name]?"
        mike.say "Can I feel them in there?"
        "I feel myself blushing as I'm flooded with emotion."
        "[mike.name] seems to be so into the idea that I'm just not prepared."
        bree.say "It's a bit early for that, [mike.name]."
        bree.say "You won't feel a thing for a while yet!"
        mike.say "Oh...okay, [hero.name]."
        mike.say "But can I do it anyway?"
        mike.say "Just because I know the little one's in there?"
        "I nod and watch as [mike.name] puts his hand on my belly."
        "He looks equal parts delighted and amazed."
        "And my own feelings are beginning to build up too."
        "Suddenly I'm seeing images of [mike.name] and I together as parents."
        "Seriously, all I wanted to do was tell him about it."
        "But now I'm already planning our future together as a family!"
        "I know that I should get a hold of myself."
        "But maybe I'll just keep indulging myself a little longer..."
    else:
        mike.say "No way, [hero.name]!"
        mike.say "No fucking way!"
        mike.say "How can you be pregnant?!?"
        "I can't believe that [mike.name]'s reacting like this."
        "I mean sure, it's a massive shock."
        "But aren't we supposed to be in this thing together?"
        bree.say "I don't know, [mike.name]..."
        bree.say "Maybe it had something to do with all those times we did it bareback, huh?"
        bree.say "You remember that?"
        "[mike.name] is already shaking his head as he starts to back away."
        "He keeps holding out his hands like he's scared of me coming closer."
        mike.say "No way, [hero.name]..."
        mike.say "I can't handle this..."
        mike.say "It's too much!"
        bree.say "Seriously, [mike.name]?"
        bree.say "How do you think I feel right now?"
        bree.say "I could do with a little support from you!"
        "[mike.name] just keeps on shaking his head at me."
        "And he's starting to turn away."
        "Like he's seriously going to make a run for it."
        mike.say "You have to handle this, [hero.name]."
        mike.say "Because I can't be a father!"
        mike.say "And you're not coming near me until it's dealt with!"
        mike.say "This thing is over, [hero.name]."
        mike.say "You and me - we're SO over!"
        "With that said, he really does run off."
        "Which leaves me alone and feeling abandoned."
        "And I have no idea what I'm going to do next."
        $ mike.breakup()
    return

label mike_female_job_event_01:
    "At the sound of someone whistling, I look up from what I'm doing."
    show mike casual happy at left with easeinleft
    "That's when I see [mike.name] come into the room, almost skipping along!"
    bree.say "Hmm..."
    bree.say "Someone looks pleased with themselves!"
    show mike at center with ease
    "[mike.name] stops in his tracks and treats me to a self-satisfied smile."
    show mike normal
    mike.say "That'd be the same guy that just got himself a promotion!"
    mike.say "Specifically this guy here!"
    show mike happy
    "[mike.name] points his thumbs at himself."
    "And if anything, his grin becomes wider than before."
    bree.say "Oh, really?"
    bree.say "Congratulations, [mike.name]."
    bree.say "You do seem to work really hard, so you must have earned it."
    "I can see that my compliments are having an effect on [mike.name]."
    "As he nods eagerly, soaking up the praise I'm heaping onto him."
    "But then I see a slight change come over him."
    "And there's a subtle change in his expression too."
    show mike normal
    mike.say "Actually, [hero.name]..."
    mike.say "I was planning on going out to celebrate tonight."
    mike.say "Like having a meal at a nice restaurant, you know?"
    "I smile and nod, wondering where this is going."
    bree.say "That sounds like a great idea, [mike.name]."
    bree.say "The perfect way to reward yourself."
    mike.say "Thing is, [hero.name]..."
    show mike blush
    mike.say "I wondered if you wanted to come along too?"
    "I can't help my eyes going wide at the question."
    "Did he..."
    "Did he just ask me out?"
    "Like on a real date?"
    menu:
        "Yes!" if mike.love >= 50 or not mike.flags.nodate:
            "I don't even need to think about my answer."
            "It just pops into my head and then out of my mouth."
            bree.say "Sure thing, [mike.name]."
            bree.say "That sounds like a great idea!"
            show mike happy
            mike.say "Great!"
            mike.say "I'm just going to get changed."
            mike.say "Then we can head off to the restaurant."
            "Suddenly he stops and looks me up and down."
            mike.say "Erm..."
            show mike down
            mike.say "You might want to get changed, yeah?"
            mike.say "This place is a little fancy!"
            $ mike.love += 2
        "A date? Really?":
            "Hmm...this awkward!"
            "I really feel like [mike.name]'s putting me on the spot here."
            bree.say "Oh no, [mike.name]!"
            bree.say "I already have plans for tonight."
            show mike sad
            "[mike.name] looks instantly disappointed."
            mike.say "Aw!"
            mike.say "No way, [hero.name]!"
            mike.say "Can't you cancel and come out with me instead?"
            "I shake my head, trying to look as disappointed as I can."
            bree.say "Sorry, [mike.name] - no can do."
            bree.say "And besides, you probably already have all your friends coming along."
            bree.say "I'd just be getting in the way."
            "[mike.name] shrugs and then nods, letting me know that he's giving up."
            show mike normal at left with ease
            "Then he turns and walks away, leaving me feeling a little guilty."
            hide mike with easeoutleft
            "But that's better than being talked into a date I don't want to go on."
            $ mike.sub += 1
            return
    scene bg restaurant with fade
    show mike date normal at right5 with easeinright
    "When we get to the restaurant, I'm suddenly glad that I did change."
    "Because [mike.name] wasn't kidding when he said this place was fancy!"
    "I mean, it's not fit for the King and Queen of England or anything like that."
    "But it's fancy enough to make me feel more than a little out of my league!"
    bree.say "Erm..."
    bree.say "[mike.name]?"
    mike.say "Yeah, [hero.name]?"
    bree.say "Is this the right place?"
    bree.say "I feel like we should have pulled up in a limo or something!"
    show mike at center with ease
    "[mike.name] waves away my concerns and pulls out my chair for me to sit down."
    mike.say "Don't worry about it, [hero.name]."
    mike.say "This is just a special occasion, that's all."
    scene bg black
    show restaurant meal mike
    with fade
    "But when the waiter comes over with the menus, I feel even worse."
    "The guy's one hundred percent snooty, looking down his nose at me."
    "What's worse, one glance at the menu fills me with fear."
    bree.say "[mike.name]!"
    bree.say "This menu's all screwy!"
    bree.say "It's like they messed up all the words."
    "At this, the waiter sniggers under his breath."
    "But [mike.name] leans closer to me, a concerned look on his face."
    mike.say "It's in French, [hero.name]!"
    show restaurant meal mike bored
    mike.say "Didn't you learn to speak French in high-school?"
    "How do I tell him that I was too busy cutting class back then?!?"
    bree.say "Of course I did, [mike.name]!"
    bree.say "But I forgot all that stuff since then!"
    show restaurant meal mike -bored
    mike.say "Well..."
    mike.say "I could order something for you?"
    menu:
        "Yes, please":
            "I shrug and hand the menu over to [mike.name]."
            bree.say "Why not, [mike.name]."
            bree.say "After all, you're paying the bill!"
            show restaurant meal mike happy
            "[mike.name] nods and proceeds to order something for me."
            "It sounds like 'Brick-Tech with Pom-Frets."
            $ mike.love += 2
            "But I trust his judgement and just go with it."
        "I should be able to decipher the menu":
            "The mere suggestion of letting someone order for me makes my blood boil."
            bree.say "No way!"
            bree.say "I can handle it myself!"
            "Glancing down at the menu, I choose something at random."
            "Because food is food, right?"
            "Chances are whatever I order it'll be good."
            bree.say "I'll have the..."
            bree.say "Es...Car...Got..."
            bree.say "Yeah?"
            show restaurant meal mike bored
            "[mike.name] and the waiter both raise their eyebrows at my choice."
            $ mike.sub += 1
            "And I smile, choosing to take that as evidence they're impressed."
    show restaurant meal mike -bored -happy
    "Soon enough our food arrives and we get down to eating it."
    "[mike.name]'s ordered us some wine, and it's going down pretty well."
    "It even manages to cover up the fact my food tastes a little funky."
    "I can see that [mike.name]'s doing the best he can to impress me tonight."
    "Like he really wants me to enjoy myself and have a good time."
    "But the problem is that I feel like I'm having to put on act the whole time."
    "This place is so fancy I can't be myself for fear of offending someone!"
    menu:
        "I can't stand this place":
            "This is just plain stupid."
            "I'm pretending to like this stuff just to please [mike.name]."
            "But I know that I'm wasting his money trying to do that."
            "And I just can't keep my conscience from bugging me about it!"
            bree.say "Urgh..."
            show restaurant meal mike bored
            mike.say "What's the matter, [hero.name]?"
            mike.say "Is there something wrong with your food?"
            mike.say "Because I can always have the waiter take it back..."
            bree.say "NO!"
            show restaurant meal mike -bored
            bree.say "I mean...no, please don't do that!"
            bree.say "Look, [mike.name]..."
            bree.say "I have to come clean - I don't like this kind of place."
            "I wince, waiting for [mike.name] to tell me off."
            "But instead he looks oddly relieved."
            mike.say "You don't?"
            show restaurant meal mike happy
            "I nod, which makes him shake his head and laugh."
            mike.say "Ha!"
            mike.say "Neither do I!"
            "Now it's my turn to look surprised and shake my head."
            bree.say "What do you mean you don't like this?!?"
            bree.say "Coming here was your idea!"
            mike.say "Yeah, well...I was kind of trying to impress you."
            show restaurant meal mike blush
            mike.say "My boss is always talking about this place."
            mike.say "And he's like this high-flying, stylish kind of guy..."
            "I can't help giggling as [mike.name] admits all of this."
            bree.say "Actually, [mike.name]..."
            show restaurant meal mike -blush
            bree.say "I'd rather have a burger down the pub!"
            "[mike.name] leans back in his chair, looking relieved."
            mike.say "Me too!"
            mike.say "But what about all this?"
            "He gestures to the food and wine on the table."
            "I glance around, scoping out the inside of the restaurant."
            bree.say "You know..."
            bree.say "We are really close to the door."
            bree.say "And the waiter's just gone into the back..."
            mike.say "[hero.name]!"
            mike.say "Are you suggesting we dine and dash?!?"
            "By way of answer, I push back my seat and stand up."
            "Then I make a dash for the door."
            "I hear [mike.name] struggling to follow me."
            scene bg street
            show mike date happy
            with hpunch
            "Then we're out into the street and running down the sidewalk."
            "We duck into an alleyway and then out onto another street."
            "Once there, we hail a cab and ask the driver to take us to the local pub."
            $ mike.love += 4
            $ hero.morality -= 1
            "And the whole way there I can feel my heart beating with excitement."
        "I can at least try":
            "I figure that the best thing to do is just try to fit in."
            "After all, [mike.name] invited me along and he's the one paying."
            "If he wanted to come here, that must mean he likes this kind of thing."
            bree.say "Mmm!"
            bree.say "This is really nice, [mike.name]!"
            bree.say "I don't know why I never came here before now."
            show restaurant meal mike happy
            "[mike.name] smiles and nods."
            "But I can't help thinking that his smile looks a little forced."
            "Maybe that's because of the prices that I saw on the menu!"
            mike.say "I..."
            mike.say "I know just what you mean, [hero.name]."
            mike.say "This is so much better than eating burgers or something like that!"
            "At the mere mention of burgers and junk food, I feel my heart begin to ache."
            "Urgh...I'd SO rather be eating something like that right now!"
            "But I'm here and I'm eating whatever the hell this stuff is."
            "So all I can do is pull off a smile that looks as strained as [mike.name]'s."
            $ mike.sub += 2
            $ hero.morality += 1
            "And by the time we're done eating, I feel like I'm getting indigestion too!"
    return

label mike_find_out_pregnancy:
    $ mike.flags.toldpreg = True
    show mike at center, zoomAt(1.5, (640, 1040))
    "I can see the way that [mike.name]'s looking at me right now."
    "And I can almost read his mind too, predicting his thoughts."
    "But there's no way that I'm going to come out and tell him."
    "He's going to have to do that for himself!"
    mike.say "[hero.name]..."
    bree.say "Yes, [mike.name]?"
    mike.say "Tell me the truth, okay?"
    mike.say "Are you pregnant?"
    "I take a deep breath."
    "And then I nod as I let it out."
    bree.say "Yes, [mike.name]..."
    bree.say "I'm pregnant."
    menu:
        "It's yours":
            $ mike.flags.know_is_father = True
            bree.say "And you're the father!"
            show mike surprised
            "[mike.name]'s eyes bulge at the revelation."
            "And his mouth opens and closes, but nothing comes out at first."
            if mike.love >= 160:
                "Suddenly the mental blockage seems to clear."
                "And [mike.name] starts babbling at me."
                show mike down
                mike.say "Are...are you serious, [hero.name]?"
                show mike normal
                mike.say "I'm going to be a dad?!?"
                mike.say "Are you telling me the truth?"
                bree.say "Yes, [mike.name]..."
                bree.say "Of course I am!"
                bree.say "I wouldn't lie about something so important."
                show mike happy at startle
                "[mike.name]'s almost dancing on the spot as I say all of this."
                "Which I guess means that he's delighted with the news."
            else:
                "Suddenly the mental blockage seems to clear."
                "And [mike.name] starts babbling at me."
                show mike down
                mike.say "Are...are you serious, [hero.name]?"
                mike.say "Please, tell me you're lying?"
                bree.say "Yes, [mike.name]..."
                bree.say "Of course I am!"
                bree.say "I wouldn't lie about something so important."
                show mike surprised
                mike.say "But...but...but..."
                show mike sad
                mike.say "I can't be a father - I'm too young!"
                bree.say "Well I'm afraid that you are."
                bree.say "So what are you going to do about it?"
                if mike.love >= 150:
                    "[mike.name] looks like he's going to blow-up on me for a moment."
                    show mike down
                    "But then he kind of sags and shakes his head."
                    mike.say "I dunno, [hero.name]."
                    mike.say "I have no idea what I'm going to do!"
                    show mike sad
                    mike.say "I just know I'm not ready for this."
                    bree.say "What does that mean, [mike.name]?"
                    show mike at center, zoomAt(1.25, (640, 940))
                    "[mike.name] shrugs and starts to back away."
                    mike.say "I guess it means that I'm not going anywhere, [hero.name]."
                    mike.say "But don't expect any help from me raising the kid."
                    show mike normal
                    mike.say "Not until I get my own shit straightened out first!"
                else:
                    mike.say "I'll tell you what I'm going to do, [hero.name]!"
                    show mike normal
                    mike.say "I'm going to get as far away from you and that brat as I can!"
                    mike.say "And don't even think about trying to track me down either!"
                    bree.say "WHAT?!?"
                    bree.say "You useless asshole!"
                    hide mike with easeoutright
                    "By the time I say this, [mike.name]'s already turned and left."
                    "He's literally running away from me as fast as he can go!"
                    "Maybe I should take a lesson from his reaction there?"
                    "I mean, do I really want to rely on a guy that runs away from responsibility?"
                    $ mike.set_gone_forever()
        "It's not yours":
            bree.say "And you're not the father!"
            show mike surprised
            "[mike.name]'s eyes bulge at the revelation."
            "And his mouth opens and closes, but nothing comes out at first."
            if mike.love >= 140:
                show mike down
                "[mike.name] closes his eyes and shakes his head."
                "And for a moment I think he's going to say it's all over."
                show mike annoyed
                "But then he opens his eyes and lets out a sigh."
                mike.say "Urgh..."
                mike.say "Wow, [hero.name]..."
                mike.say "Just wow!"
                mike.say "I thought you were going to tell me I was the father."
                mike.say "But that's not going to happen."
                show mike sad
                mike.say "So I'm just going to have to deal with reality, I guess."
                bree.say "Y...you're not going to leave me?"
                "[mike.name] shakes his head again."
                "And I get the impression he's trying hard to master his temper right now."
                mike.say "No, [hero.name]..."
                show mike annoyed
                mike.say "But I am mad as hell."
                mike.say "And it's going to take me some time to accept this."
                bree.say "I...I understand, [mike.name]."
                menu:
                    "Ask [mike.name] to help with the baby":
                        bree.say "But I have to ask you one more question..."
                        bree.say "Will you help me with the baby when it arrives?"
                        if mike.love >= 160:
                            "[mike.name] sighs and then nods his head."
                            mike.say "Urgh..."
                            mike.say "I guess so, [hero.name]."
                            show mike normal
                            mike.say "What kind of a guy would I be if I left you on your own?"
                            "I feel a surge of relief pass through me."
                            "And just knowing [mike.name] will be there seems to make things better."
                            "I can't help thinking that I really don't deserve a guy like him."
                            "And that I need to take this whole thing as a warning."
                            "That and change my ways!"
                        else:
                            show mike down
                            "[mike.name] chuckles and shakes his head."
                            mike.say "No, [hero.name]..."
                            show mike normal
                            mike.say "I'm not going to do that."
                            mike.say "I'll be here whenever you need me."
                            mike.say "But I'm not raising someone else's kid for them!"
                            hide mike with easeoutright
                            "With that, he turns on his heel and walks away."
                            "I guess he has his reasons."
                            "And at least he didn't dump me!"
                            "But I guess when it comes to the baby, I'm on my own."
                            $ mike.breakup()
                    "I won't bother you about it":
                        pass
            else:
                "[mike.name] stares at me like he suddenly doesn't know me."
                "And he shakes his head slowly as he does so."
                mike.say "Wow, [hero.name]..."
                mike.say "Just wow!"
                mike.say "I thought you were going to tell me I was the father."
                mike.say "And I was ready to accept that, really I was."
                show mike angry
                mike.say "But you're telling me it's somebody else's baby?!?"
                "I do the best I can to appeal to [mike.name]."
                "Trying to explain myself to him."
                bree.say "Look, [mike.name]..."
                bree.say "I know this looks bad!"
                show mike surprised
                "[mike.name] looks amazed, and he takes a step back."
                mike.say "Bad?"
                show mike normal
                mike.say "No, [hero.name]."
                mike.say "Bad would be you slept with someone else."
                mike.say "Or bad would be you're pregnant."
                mike.say "Both at once is SO much worse!"
                show mike sad
                mike.say "This is the end, [hero.name]..."
                mike.say "We're over!"
                bree.say "No, [mike.name]..."
                bree.say "Wait!"
                hide mike with easeoutright
                "But it's too late."
                "[mike.name]'s already striding off, leaving me standing there alone."
                $ mike.set_gone_forever()
    scene bg black with dissolve
    return

label mike_job_offer_female:
    show mike at center, zoomAt(1.5, (640, 1040))
    "The moment that [mike.name] walks up to me, I can see that he's got something on his mind."
    "He's one of those guys that becomes more obvious the more he tries to hide something."
    "So it's all I can do to keep from laughing as he tries to play it straight in front of me."
    mike.say "Oh..."
    mike.say "Hey, [hero.name]!"
    mike.say "What are you doing?"
    bree.say "Oh, not much, [mike.name]."
    bree.say "How about you?"
    show mike annoyed
    "[mike.name] shrugs and casts his gaze around."
    mike.say "Same here, you know?"
    show mike happy
    mike.say "Just hanging out, killing some time..."
    show mike normal
    "I wait patiently as [mike.name] starts to run out of things to say."
    "And soon enough he's forced to abandon the small-talk."
    show mike down
    "Now he has to either say what he wants to say or walk away again."
    "Both of which are potentially painful choices!"
    show mike normal
    mike.say "Oh, yeah..."
    mike.say "There was something I wanted to ask you!"
    "Trying to look as innocent and surprised as I can, I nod at [mike.name]."
    bree.say "Oh, really?"
    bree.say "Good thing you remembered, [mike.name]!"
    mike.say "Well..."
    mike.say "You know I got a promotion at work?"
    bree.say "Yeah, [mike.name]..."
    bree.say "I think I remember you mentioning it once or twice."
    "Yeah, right!"
    "It's all he's been talking about since it happened!"
    mike.say "The thing is that I'm taking on more responsibility too."
    mike.say "Like, my workload's gone through the roof!"
    bree.say "Yeah, that kinda happens when you get promoted."
    mike.say "Anyway..."
    mike.say "The new job comes with the option to hire people to work under me."
    mike.say "Like I can have a personal assistant to help out with it all."
    "I nod along as [mike.name] explains himself."
    "And so far it all sounds pretty logical."
    bree.say "So what, [mike.name]?"
    bree.say "You want me to help you write an ad for the job?"
    bree.say "Maybe look at some of the CVs you get sent?"
    show mike blush
    "At this I see [mike.name]'s cheeks flush red."
    "And he seems to get a lot more nervous."
    mike.say "Erm..."
    mike.say "No, [hero.name]..."
    mike.say "I was more thinking of offering the job to you."
    mike.say "Like...would you want to be my personal assistant?"
    menu:
        "Accept":
            "The moment [mike.name] comes out with his offer, I know what my answer is going to be."
            "And there's nothing I can do to stop myself from blurting it out either."
            bree.say "Of course I would!"
            bree.say "I'd love to be your PA, [mike.name]!"
            show mike surprised
            "[mike.name] looks more than a little surprised at my answer and the way I deliver it."
            show mike normal
            "But he does the best he can to put on a professional face and press on."
            mike.say "Oh..."
            mike.say "Really, [hero.name]?"
            mike.say "Well...that's great news!"
            mike.say "But you didn't even let me get to the actual details of the position."
            mike.say "You know, like the pay, the hours and what you'd be doing under me?"
            "At the mere mention of being under [mike.name] in any capacity makes me blush."
            "And I tell myself that I have to make this look like I'm doing it for the job."
            "I can't let [mike.name] know that I want to spend more time around him."
            "And that taking the job is just a means to that end."
            bree.say "Oh, I'm sure we can work all of that out later."
            bree.say "I mean, it's not like I've signed a contract or anything, is it?"
            bree.say "All I did was say yes to the idea of the job."
            show mike happy
            "[mike.name] nods at this."
            "And I nod too, trying to add weight to his convictions."
            show mike down
            mike.say "I've got to admit, [hero.name]..."
            mike.say "I was pretty nervous about asking you!"
            bree.say "Oh?"
            bree.say "Why's that?"
            show mike normal
            mike.say "Well..."
            mike.say "We're housemates, and I'd like to think that we're friends too."
            mike.say "If we're working together, that kind of changes things."
            "I shake my head, eager to dismiss his concerns."
            bree.say "Of course we're friends, [mike.name] - good friends."
            bree.say "And that's why this is going to work out just fine."
            bree.say "Our friendship is strong enough to last through working together."
            bree.say "And we can always bitch about the boss behind his back when we get home!"
            show mike happy
            "[mike.name] nods, seemingly convinced by my pitch."
            mike.say "Okay, [hero.name], okay..."
            show mike normal
            mike.say "I'll get HR started on the paperwork as soon as I'm back in the office."
            mike.say "Then we can get you an interview and all that stuff."
            mike.say "But don't worry - that'll just be a formality!"
            hide mike with dissolve
            "I watch as [mike.name] hurries off, hoping that I've made the right decision."
            "I want to spend as much time with him as possible."
            "I just have to rely hope this is the right way to do it."
        "Refuse":
            "The moment [mike.name] comes out with his offer, I know what my answer is going to be."
            "And there's nothing I can do to stop myself from blurting it out either."
            bree.say "No way!"
            show mike surprised
            "[mike.name] looks more than a little shocked at my answer and the way I deliver it."
            show mike annoyed
            "But he does the best he can to put on a reasonable face and press on."
            mike.say "Oh..."
            mike.say "Really, [hero.name]?"
            mike.say "You didn't even let me get to the actual details of the position."
            mike.say "You know, like the pay, the hours and what you'd be doing under me?"
            "Urgh..."
            "The idea of talking about the finer details just makes me more sure than ever."
            "I know that I don't want to end up working with [mike.name]."
            "I just have to find a way to let him down gently."
            bree.say "You know how it is, [mike.name]."
            bree.say "I have my studies and a part-time job already."
            bree.say "And I can only keep that up because it's so casual and flexible."
            show mike normal
            mike.say "I can be flexible too, [hero.name]!"
            mike.say "The position doesn't have to be full-time either."
            "I shake my head, trying to cut him off before he can be reasonable."
            "Because if I don't, it's going to become obvious I just don't want his damn job!"
            bree.say "No, [mike.name], no..."
            bree.say "You need someone that's dedicated to the job."
            bree.say "Plus you don't want to come home to a work colleague either."
            bree.say "Home should be somewhere you can unwind from work."
            bree.say "A place where you can bitch about the boss and your colleagues too!"
            show mike sad
            "[mike.name] looks disappointed, almost like he's going to argue with me again."
            "But then he sighs and nods, letting me know that he's defeated."
            show mike annoyed
            mike.say "Ah..."
            mike.say "I guess you're right, [hero.name]."
            mike.say "Better to have you at home as a friend than at work as a colleague."
            bree.say "Yeah, [mike.name] - it's more fun that way!"
            show mike normal
            mike.say "Hmm..."
            mike.say "I wonder if Sasha's interested in the job..."
            "I'm about to open my mouth and say something."
            hide mike with dissolve
            "But then I stop myself and just watch as [mike.name] hurries off."
            "I mean, he's going to have the same whole argument over again with Sasha."
            "But at least it means that he's out of my hair for a while."
    $ Room.find("office").unhide()
    return

label mike_birthday_date_female:
    $ DONE["mike_birthday_date_female"] = game.days_played
    $ game.active_date.clothes = "date"
    scene bg street with fade
    "It's always kind of awkward when you start dating one of your housemates."
    "And I know people that would avoid it like the plague for that very reason."
    "But there's just something about [mike.name] that makes me forget all that stuff."
    "Something that makes me all the more determined to make this thing we have work."
    "Don't ask me to tell you exactly what it is though, as I can't put my finger on it."
    "Maybe it's because we were friends before we got involved?"
    "We already knew all those weird, quirky little things about each other and liked them, you know?"
    "But one thing all that hanging-out together does mean is that you want to make the dates special."
    "Like, you already go for a pint down the local and play videogames together."
    "So actually going out needs to be something more than that."
    "Especially when the occasion is your boyfriend's birthday."
    "Not that I'm planning anything in the way of a surprise for it."
    "[mike.name]'s been dropping hints and reminding me it was coming up for what feels like forever!"
    "So he knows that we're celebrating his birthday."
    "But he doesn't know what we're actually doing."
    scene bg door restaurant with fade
    "At least he didn't until I told him to meet me outside of a particular restaurant."
    "I think that must have been a dead giveaway, even for a guy!"
    "I figured a nice restaurant would be a real change for our date."
    "Instead of just doing slobby stuff or hanging out at the pub."
    show mike annoyed date with easeinleft
    "But as I walk up to the place, I see [mike.name]'s already there."
    "And he doesn't seem to be very happy either."
    bree.say "Hey, [mike.name]..."
    bree.say "I see you found the restaurant okay?"
    show mike sad
    "At the sound of my voice, [mike.name] spins around."
    "And he looks even more unhappy up close."
    mike.say "[hero.name]..."
    mike.say "Where in the hell have you been?!?"
    bree.say "What are you talking about?"
    bree.say "I thought this was the time we agreed to meet?"
    "[mike.name] shakes his head."
    mike.say "No, [hero.name]..."
    mike.say "That was like, almost half an hour ago!"
    "I frown as I pull out my phone and check the time."
    "And it looks like [mike.name]'s right, I am pretty late."
    menu:
        "Apologise to [mike.name]":
            "I fell awful as I put my phone away."
            "[mike.name] must have felt like a total fool waiting here for me on his own."
            bree.say "I am SO sorry, [mike.name]..."
            bree.say "I don't know how I lost track of time like that."
            bree.say "What can I do to make it up to you?"
            "I'm honestly expecting [mike.name] to detail a list of demands."
            "But instead the offer seems to embarrass him more than a little."
            "He's almost blushing, looking around like people are staring at us."
            show mike blush
            mike.say "It's okay, [hero.name]..."
            mike.say "You said sorry, and that's what matters."
            mike.say "Let's...let's get inside, okay?"
            "I nod and follow [mike.name] into the restaurant."
            "But I'm still baffled by the instant change in [mike.name]'s mood."
            "It's almost like my show of contrition was too much for him."
            "And as soon as I made it he got mad with himself!"
            "Some guys are so weird."
            $ game.active_date.score += 15
        "Tell [mike.name] it's not a big deal":
            "I shrug as I put my phone away."
            "Not sure what [mike.name]'s so upset about."
            bree.say "So I'm a little late."
            bree.say "So what?"
            bree.say "We can still go in there and eat."
            show mike surprised
            "[mike.name] looks more than a little amazed at my response."
            mike.say "Are you serious?"
            mike.say "I've been stood here for all that time."
            mike.say "People have been staring at me."
            mike.say "One of the waiters even came out to check if I was okay!"
            show mike annoyed
            bree.say "Geez, [mike.name]..."
            bree.say "Will you let it go already?"
            bree.say "We're supposed to be having a fun night out."
            bree.say "So stop being such a miserable git!"
            "[mike.name] rolls his eyes and looks away."
            "And he's still muttering under his breath as we walk into the restaurant."
            $ game.active_date.score -= 10
    scene bg restaurant with fade
    pause 0.1
    show mike date normal at right with easeinright
    "Once we're inside, I look around the place."
    "I'm trying to figure out how things work here."
    "Like, do we need to go to the bar?"
    "Or is one of the waiters going to come over and check our reservation?"
    "Waiter" "Ahem..."
    "At the sound of someone clearing their throat, [mike.name] and I turn around."
    "And that's when we see a well-dressed waiter standing by a podium."
    "It's pretty obvious that he's trying to get our attention."
    mike.say "Erm..."
    mike.say "Are we supposed to go over there or something?"
    menu:
        "Play it like I know the drill":
            "The truth is that I'm as clueless as [mike.name] when it comes to this kind of thing."
            "But this does remind me of all the posh restaurants I've seen in the movies."
            "And everyone seems to talk to a waiter at one of those before sitting down."
            "So maybe I can play it off as no big deal?"
            bree.say "Of course he is, [mike.name]..."
            bree.say "That's the maitre d', the guy in charge!"
            bree.say "He's the big cheese in a place like this."
            show mike shout
            "[mike.name] looks at me in genuine surprise as we walk over to the podium."
            mike.say "Huh?"
            mike.say "I never thought you knew all about stuff like this."
            mike.say "All I know is what I've seen in the movies!"
            bree.say "Oh yeah, I know all about fancy shit."
            bree.say "Just follow my lead, okay?"
            show mike down
            "[mike.name] nods and does as he's told."
            "But I see him narrow his eyes all the same."
            "Almost like he doesn't quite believe me."
            $ game.active_date.score += 5
        "Admit that I am as clueless as [mike.name]":
            "The truth is that I'm as clueless as [mike.name] when it comes to this kind of thing."
            "But this does remind me of all the posh restaurants I've seen in the movies."
            "And everyone seems to talk to a waiter at one of those before sitting down."
            "Though trying to fake it could blow up in my face."
            "So I decide that honesty is the best policy."
            bree.say "I think so, [mike.name]..."
            bree.say "They do that in the movies, right?"
            "[mike.name] nods at this."
            mike.say "Yeah, you're right..."
            mike.say "Like, that guy's the...maitre d'?"
            bree.say "That's it, [mike.name]!"
            show mike happy
            "[mike.name] nods, looking pleased to have recalled something vaguely relevant."
            "Together we walk over to the podium and give the waiter a smile."
            "Or at least what I hope passes for one in a place like this."
            $ game.active_date.score += 15
    show mike down at right5 with ease
    show ryan at left, blacker with dissolve
    "[mike.name] and I walk over to where the waiter is standing."
    "But even now that we know what he wants, he still doesn't seem pleased."
    "Waiter" "Sir..."
    "Waiter" "Madam..."
    "Waiter" "If you were looking for directions to the nearest burger bar..."
    "Waiter" "You'll find one of them about five blocks down from here."
    "With that, he makes a gesture towards the entrance and the street beyond."
    "I can tell straight away that we're being judged."
    "But that fact seems to be lost on [mike.name]."
    show mike surprised
    mike.say "Burger Bar?"
    show mike happy
    mike.say "Oh no, my dude..."
    mike.say "We have a reservation right here!"
    show mike normal
    "Waiter" "I see..."
    "Waiter" "Oh dear!"
    show mike surprised
    "[mike.name] turns to me, a confused look on his face."
    mike.say "What's his problem, [hero.name]?"
    mike.say "We did make a reservation, didn't we?"
    bree.say "Erm..."
    bree.say "I don't think that's the problem here."
    bree.say "I think he's looking down his nose at us, [mike.name]!"
    show mike angry
    "[mike.name]'s eyes go wide as I tell him the truth."
    mike.say "What?!?"
    mike.say "Why would he do that?"
    mike.say "What a total jerk!"
    menu:
        "Stand up to the waiter" if hero.has_skill("video_games"):
            bree.say "Don't worry about it, [mike.name]..."
            bree.say "I've dealt with worse than him."
            "[mike.name]'s about to say more."
            "But then he sees the look in my eyes."
            show mike normal
            "And he instantly closes his mouth, nodding silently."
            "Which leaves me to deal with the rude waiter."
            bree.say "I guess you don't know who I am, yeah?"
            "Waiter" "No, madam..."
            "Waiter" "I can't say that I do."
            bree.say "Well you're probably not a gamer then."
            bree.say "Because any of my one million plus followers would have done."
            bree.say "And let me tell you, they LOVE to read my reviews of places like this."
            bree.say "Just wait until they hear about the shitty way I've been treated here."
            "Sure, the waiter might be working at an old-fashioned restaurant."
            "But he still knows more than enough about social media to be worried."
            "Waiter" "Did...did you say a million followers?"
            bree.say "Actually, I said a million plus!"
            "Waiter" "In that case, please accept my apologies."
            "Waiter" "And let me see about getting you seated!"
            $ game.active_date.score += 15
        "Suggest they keep quiet":
            bree.say "I know, [mike.name], I know..."
            bree.say "But the waiters are always kind of rude in places like this."
            bree.say "It's sort of like a tradition."
            "[mike.name] opens his mouth to protest."
            show mike down
            "But then he seems to think better of it."
            "And he just shrugs instead."
            mike.say "Okay, [hero.name]..."
            mike.say "If you say so."
            "Which leaves me to deal with the rude waiter."
            bree.say "My companion is right."
            bree.say "We do have a reservation."
            bree.say "Right there!"
            "The waiter glances down at where I'm pointing."
            "Waiter" "Oh yes."
            "Waiter" "There you are."
            "Waiter" "I suppose I should show you to your table."
            "Waiter" "Come along and do try to keep up."
            "He strides off, leaving [mike.name] and I to hurry after him."
            "And all the way to the table I'm hoping whoever serves us will be a little less rude."
            $ game.active_date.score -= 15
        "Bluff the waiter" if hero.charm >= 100:
            bree.say "Don't worry about it, [mike.name]..."
            bree.say "I've dealt with worse than him."
            "[mike.name]'s about to say more."
            "But then he sees the look in my eyes."
            show mike normal
            "And he instantly closes his mouth, nodding silently."
            "Which leaves me to deal with the rude waiter."
            bree.say "Just what do you mean by 'oh dear'?"
            bree.say "Our reservation is right there."
            bree.say "And we're on time too."
            bree.say "Would you like me to call the owner and discuss your attitude with him?"
            "At this the waiter draws himself up to his full height."
            "Waiter" "Are you trying to suggest that you know Monsieur Francois?!?"
            bree.say "Are you trying to suggest that I don't?"
            "I already have my phone out, ready to make a call."
            "Obviously I don't know this Francois guy at all."
            "But the waiter has no way of knowing that."
            "Waiter" "There is no reason to place that call."
            "Waiter" "Please accept my apologies."
            "Waiter" "And let me see about getting you seated!"
            $ game.active_date.score += 20
    show restaurant meal mike nomeals with fade
    "[mike.name] and I are shown over to our table and seated."
    "But it seems like we only have time to glance down at the menus in front of us."
    "Because a moment later I hear the sound of someone approaching the table."
    "As one we look up to see a member of the waiting staff smiling at us warmly."
    "On the one hand, [mike.name] seems relieved to see it's not the rude waiter from before."
    "But on the other, I can see that this new waiter is making him feel a little awkward."
    "Which is kind of understandable, because she's female."
    "And in addition to that, she's pretty much drop-dead gorgeous too!"
    "Waitress" "Good evening, sir..."
    "Waitress" "And, madam..."
    show restaurant meal mike blush
    mike.say "H...h...hi!"
    bree.say "Hello there."
    "Waitress" "Are you ready to order?"
    "[mike.name] and I exchange clueless glances, looking like confused goldfish."
    "And this must be something the waiter's used to."
    "Because she simply smiles and leans in a little closer."
    "Waitress" "If you'd like..."
    "Waitress" "I could recommend something that's particularly good tonight?"
    show restaurant meal mike -blush happy
    "I can feel a flood of relief sweeping over me."
    "And the expression on [mike.name]'s face lets me know he's feeling the same."
    bree.say "That sounds like a great idea."
    bree.say "Right, [mike.name]?"
    show restaurant meal mike blush -happy
    mike.say "Oh yeah, [hero.name]..."
    mike.say "That'd be great!"
    "The waiter nods and reels off the things we'll be eating."
    "But I don't think either of us is really listening."
    "Instead we're exchanging more awkward glances."
    mike.say "She was..."
    mike.say "Erm..."
    mike.say "Nice?"
    menu:
        "Agree with [mike.name] but tell him not to flirt":
            "I roll my eyes and shake my head."
            bree.say "It's okay, [mike.name]..."
            bree.say "I can handle you seeing pretty girls when we're on a date."
            bree.say "It doesn't make me insane with jealousy!"
            show restaurant meal mike -blush happy
            "[mike.name] seems visibly relieved as soon as I say this."
            "And he lets out a sigh of relief too."
            mike.say "Phew..."
            mike.say "That's really cool of you, [hero.name]."
            mike.say "Like, some girls really freak out about that kind of thing!"
            mike.say "But what about the size of her..."
            "I hold my hand up, cutting [mike.name] off before he can finish."
            bree.say "Whoa there!"
            bree.say "I'm not that cool with it, [mike.name]."
            bree.say "Just keep your eyes on me from now on, okay?"
            "[mike.name] nods quickly, eager to do as he's told."
            "And I see him visibly trying to keep his eyes pointed in my direction too."
            $ game.active_date.score += 10
        "Agree with [mike.name] and tell him I like the waiter too":
            "I don't hesitate to nod in agreement."
            bree.say "Isn't she though?"
            bree.say "Very beautiful girl."
            show restaurant meal mike -blush happy
            "[mike.name] seems visibly relieved as soon as I say this."
            "And he lets out a sigh of relief too."
            mike.say "Phew..."
            mike.say "That's really cool of you, [hero.name]."
            mike.say "Like, some girls really freak out about that kind of thing!"
            bree.say "It's okay, [mike.name]..."
            bree.say "I can handle you seeing pretty girls when we're on a date."
            bree.say "Especially when they get my motor running too!"
            show restaurant meal mike -happy bored
            "[mike.name]'s eyes go wide at the admission."
            "And for a moment I think he's going to have a funny turn."
            show restaurant meal mike blush -bored
            mike.say "Th...tha..."
            mike.say "That's great, [hero.name]..."
            mike.say "Really modern of you as well!"
            "I watch as [mike.name] tries his best to process this new information."
            "And to decide if he should see the waiter as a treat for his eyes."
            "Or as a potential rival for my affections!"
            $ game.active_date.score += 20
    "[mike.name] and I are both curious to see just what the waiter will serve us."
    "And when she comes back, we're straining to see what she's carrying."
    show restaurant meal mike -nomeals -blush -happy with dissolve
    "But it's hard to keep up the excitement when she puts down two bowls of soup."
    "Waitress" "There you go..."
    "Waitress" "Two bowls of gazpacho soup."
    "Waitress" "Bon appetit!"
    "[mike.name] waits for the waitress to walk away from the table before he says anything."
    "And even then he looks around to make sure that she's not still withing earshot."
    mike.say "Soup?"
    mike.say "That's like the most boring thing I can imagine!"
    bree.say "Yeah, I know..."
    bree.say "But I still think we should give it a try."
    bree.say "It could turn out to be the best soup you've ever tasted."
    "[mike.name] shrugs and proceeds to lift a spoonful to his mouth."
    show restaurant meal mike -nomeals bored
    "I watch as he swallows it, and a look of disgust appears on his face."
    bree.say "What's the matter?"
    bree.say "You look like you've been poisoned!"
    mike.say "Urgh..."
    mike.say "It's fricking cold!"
    mike.say "What kind of a place is this?"
    if hero.has_skill("cooking") or hero.knowledge >= 100:
        menu:
            "It’s a gazpacho isn't it ?" if hero.has_skill("cooking"):
                "[mike.name] looks like he's about to call for the waiter."
                "But I manage to reach out and put my hand on his."
                "Which is enough to stop him in his tracks."
                bree.say "Wait a minute, [mike.name]..."
                bree.say "The waiter said this was gazpacho soup."
                mike.say "Did she get that wrong too?"
                mike.say "Then we've got that to complain about too!"
                bree.say "No, no, no..."
                bree.say "This is definitely gazpacho soup."
                bree.say "Because it's supposed to be served cold."
                "[mike.name] stares at me blankly, like I've gone insane."
                mike.say "You have to be kidding?"
                bree.say "I'm afraid not."
                "This time [mike.name] looks like he believes me."
                "And he also looks more than a little relieved too."
                show restaurant meal mike blush -bored
                mike.say "Thanks, [hero.name]..."
                mike.say "I'd have looked like a complete fool complaining about that!"
                $ game.active_date.score += 20
            "I think I already saw that in a cookbook" if kat.love + hero.knowledge >= 200:
                "[mike.name] looks like he's about to call for the waiter."
                "But I manage to reach out and put my hand on his."
                "Which is enough to stop him in his tracks."
                bree.say "Wait a minute, [mike.name]..."
                bree.say "The soup's not luke warm, like it went cold."
                bree.say "It's practically chilled!"
                mike.say "Did they screw up cooking it as well?"
                mike.say "Then we've got that to complain about too!"
                bree.say "No, no, no..."
                bree.say "I don't think they could be that slack."
                bree.say "I think the soup is supposed to be cold."
                "[mike.name] stares at me blankly, like I've gone insane."
                mike.say "You have to be kidding?"
                bree.say "I'm serious."
                bree.say "I'm sure I've heard about kinds of soup that you eat cold."
                bree.say "Like, they're pretty fancy - delicacies, you know?"
                bree.say "Just the kind of thing they'd serve in a place like this."
                "This time [mike.name] looks like he believes me."
                "And he also looks more than a little relieved too."
                show restaurant meal mike blush -bored
                mike.say "Thanks, [hero.name]..."
                mike.say "I'd have looked like a complete fool complaining about that!"
                $ game.active_date.score += 20
    else:
        "I shake my head, totally taken by surprise."
        "At the same time, [mike.name]'s already looking for the waitress."
        "And when he sees her, he starts to wave for her attention."
        "Waitress" "Is there a problem, sir?"
        mike.say "You bet there is."
        mike.say "This soup is cold!"
        "The waitress looks puzzled by [mike.name]'s complaint."
        "But not like she's surprised at the news."
        "More like she doesn't understand the reason he's making it."
        "Waitress" "But, sir..."
        "Waitress" "It's gazpacho..."
        "Waitress" "It's supposed to be served cold."
        show mike blush
        "[mike.name] and I begin to go red at the exact same moment."
        "Something that's not helped by the people on the nearby tables chuckling at us either."
        $ game.active_date.score -= 20
    "After the shock of the gazpacho soup, things seem to calm down a little."
    "The rest of the food the waitress picks out for us is more familiar and less challenging."
    "So much so that we're eager to see what comes next."
    show restaurant meal mike -blush
    "And it's while we're waiting between courses that [mike.name] decides to ask me a question."
    mike.say "So, [hero.name]..."
    mike.say "Did you get me anything for my birthday?"
    mike.say "You know, like a gift?"
    mike.say "I mean...it's okay if you didn't."
    mike.say "I'm just asking, that's all."
    "I can't help smiling and letting out a chuckle at this."
    bree.say "That's being pretty forward, [mike.name]!"
    mike.say "Yeah, I know..."
    mike.say "Maybe it was the gazpacho soup that did it!"
    if not hero.has_gifts:
        "There's no way that I can hide the fact I didn't get him anything."
        "So let's just hope that talk about it not mattering was for real."
        bree.say "I have to confess, [mike.name]..."
        bree.say "I didn't get you anything."
        bree.say "I was hoping the date would be enough?"
        show restaurant meal mike bored
        "Despite what [mike.name] says, I can read his face like a book."
        "He's disappointed that I didn't get him anything."
        "But he's doing all he can to hide the fact from me."
        $ game.active_date.score -= 20
        $ mike.love -= 10
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_21
        if _return != "done":
            if _return not in ["None", "exit"]:
                bree.say "Well you're in luck, [mike.name]..."
                bree.say "Because I did!"
                "[mike.name] can't help grinning as I hand the gift over."
                play sound [paper_ripping_2, paper_ripping_1]
                "But as soon as he's torn the paper off, his expression changes."
                bree.say "What is it?"
                bree.say "Is there something wrong?"
                if _return:
                    show restaurant meal mike happy
                    mike.say "Something wrong?"
                    mike.say "No, [hero.name]..."
                    mike.say "This is perfect!"
                    mike.say "Like...the best gift ever!"
                    "I can't help feeling a surge of pride as I watch [mike.name] open his gift."
                    "Looks like my instincts were right and he loves what I got him."
                    $ game.active_date.score += 20
                else:
                    show restaurant meal mike bored
                    mike.say "Erm..."
                    mike.say "No, [hero.name]..."
                    mike.say "Everything's fine."
                    "Despite what [mike.name] says, I can read his face like a book."
                    "He's not impressed with the gift that I bought him."
                    "But he's doing all he can to hide the fact from me."
                    $ game.active_date.score -= 10
            else:
                "There's no way that I can hide the fact I didn't get him anything."
                "So let's just hope that talk about it not mattering was for real."
                bree.say "I have to confess, [mike.name]..."
                bree.say "I didn't get you anything."
                bree.say "I was hoping the date would be enough?"
                show restaurant meal mike bored
                "Despite what [mike.name] says, I can read his face like a book."
                "He's disappointed that I didn't get him anything."
                "But he's doing all he can to hide the fact from me."
                $ game.active_date.score -= 20
                $ mike.love -= 10
    show restaurant meal mike -bored -happy with fade
    "I guess we must be having fun, because time seems to fly in the restaurant."
    "And before I know it, we're settling the bill and getting ready to leave."
    scene bg street
    show mike date
    with fade
    "It's a little different to a normal date, as we're both going home to the same address."
    "But that doesn't mean I'm spared the awkward moment that always comes towards the end of a date."
    "The point where someone has to raise the possibility of keeping things going a little longer."
    "So here goes..."
    bree.say "How are you feeling, [mike.name]?"
    bree.say "Are you tired yet?"
    bree.say "Because I think I have some life left in me yet!"
    if game.active_date.score >= 80 and minami.sexperience >= 1:
        "At the mere mention of the subject, [mike.name]'s attention is piqued."
        "And he begins to nod his head even before he gets a single word out."
        show mike happy
        mike.say "Are you serious, [hero.name]?"
        mike.say "Because I'm not tired..."
        mike.say "Not by a long way!"
        "I can feel my trepidation fading away at [mike.name]'s response."
        "And the warming sense of knowing that he's having a good time."
        bree.say "I mean..."
        bree.say "I don't have any specific plans."
        bree.say "Maybe we can discuss it in the taxi?"
        mike.say "Sounds good to me."
        mike.say "Let's go find one!"
        call mike_birthday_sex from _call_mike_birthday_sex
    else:
        "At the mere mention of the subject, [mike.name] starts to yawn."
        "And he begins to shake his head even before he gets a single word out."
        show mike sad
        mike.say "Are you serious, [hero.name]?"
        mike.say "Because I'm totally beat..."
        mike.say "I could fall asleep on my feet!"
        "I feel an instant surge of disappointment at [mike.name]'s answer."
        "It's made all the more crushing because I know what it means."
        "And that's that he didn't have a good time tonight."
        bree.say "Okay, [mike.name]..."
        bree.say "If that's what you want?"
        scene bg taxi car with fade
        "My question goes unanswered as [mike.name]'s already hailing a taxi."
        "The ride back to the house is silent and awkward."
        scene bg livingroom with fade
        "And once we're home, [mike.name] makes his excuses in the hallway."
        "Then he heads straight for his room."
        $ game.room = "livingroom"
    return

label mike_birthday_sex:
    scene bg taxi car with fade
    "[mike.name] and I have had the entire tide home in the taxi to come to a decision."
    scene bg house with fade
    "But as we step out onto the curb and walk up the path, we're still discussing it."
    show mike date
    mike.say "It's simple, [hero.name]..."
    mike.say "My room's the closest to the front door."
    mike.say "So we can just save time by doing it in there."
    "I pause in the act of opening the door to disagree."
    bree.say "Uh-uh, [mike.name]..."
    bree.say "If there's anyone in, then they'll hear us!"
    bree.say "We'd be better off upstairs in my room."
    scene bg secondfloor with fade
    "Before [mike.name] can open his mouth to respond, I get the door open."
    "And I hurry into the hallway with him close on my heels."
    show mike date with easeinleft
    mike.say "No, [hero.name]..."
    mike.say "I still think that..."
    "As one, [mike.name] stops talking and I raise a hand for silence."
    "We're both scanning the hallway and listening out for a familiar sound."
    bree.say "I don't hear loud heavy metal."
    mike.say "And there are no boots for me to trip over either."
    mike.say "You know what that means, right?"
    bree.say "I sure do - it means Sasha's out!"
    "[mike.name] and I exchange a look of pure glee."
    "Because we know this means we have the house to ourselves."
    show mike happy at startle
    "Clasping hands, we do a silly little dance, right there in the hallway."
    "Just our way of celebrating the chance to do as we please without consequence."
    scene bg bedroom1 with fade
    pause 0.2
    show mike date with easeinright
    "And at the end of it, [mike.name] makes to pull me towards his bedroom."
    "But I put on the breaks, resisting his efforts."
    mike.say "What's the matter, [hero.name]?"
    mike.say "We can go where we like."
    bree.say "I know, I know..."
    bree.say "But that doesn't mean we have to the most obvious thing."
    bree.say "Not when we have the chance to be creative!"
    "[mike.name] looks at me with a questioning expression."
    scene bg secondfloor
    show mike normal date at startle
    "So I decide to take matters into my own hands, pulling him up the stairs."
    "Unlike me, he seems happy to be lead, at least for the moment."
    "So I waste no time in climbing up the stairs and onto the landing."
    mike.say "[hero.name]!"
    mike.say "How is your room any less obvious than mine?"
    "By way of answer, I walk straight past the door to my own room."
    "And instead I stop in front of Sasha's door."
    "[mike.name]'s eyes go wide as I open it and walk inside."
    "But I note as I do so that he makes no effort to stop me."
    scene bg bedroom3 with fade
    show mike date with easeinleft
    bree.say "You see, [mike.name]?"
    bree.say "We can get it on at home and still make it exciting!"
    mike.say "You mean make it scary, [hero.name]!"
    mike.say "I hate to think what Sasha'd say if she caught us doing this."
    bree.say "Then what are we waiting for?"
    bree.say "The longer we take, the more likely it is she'll be back!"
    "To underline my point, I grab hold of [mike.name]'s collar."
    "And I use it to march him over to the bed."
    "Once we're there, I half pull and half trip him."
    "Sending him tumbling onto Sasha's bed."
    show mike perv
    mike.say "Whoa..."
    "There's no time for [mike.name] to say anything more than that."
    "Because I make sure that I follow him down onto the mattress."
    "And as soon as he lands, I'm on top of him."
    show mike naked with dissolve
    "I don't wait for permission to start stripping off his clothes either."
    "Slowly I feel him starts to recover from the surprise."
    "At first his hands just clutch helplessly at me."
    "But soon enough I feel them actually starting to move with a purpose."
    "And that is to begin undressing me too."
    "Little by little we manage to strip each other naked."
    show mike kiss naked with fade
    $ mike.flags.kiss += 1
    "A task made that much harder by the fact we're entwined and moving the whole time."
    "[mike.name] and I have our lips locked together, tongues engaged in an embrace too."
    "I swear neither of us specifically makes a move below the waist."
    "But things down there seem to have a mind all of their own."
    show mike reverse cowgirl with fade
    "I find myself gasping in surprise at the first sensation of his cock touching me."
    "And the only thought it inspires in my head is that I want more of the same."
    "I want it quickly too, which is why my hand slithers down there."
    "Using the other on his shoulder to brace myself, I begin to direct traffic."
    "Every move that I make sends him sliding over and against me."
    "And each time I come close to getting him where I want, he slips away."
    "What I'm feeling is a powerful mixture of pleasure and frustration."
    "Which only serves to push me on harder than ever to get what I want."
    "It's only when [mike.name] seems to realise the challenge I'm facing that things start to change."
    "Because I feel the sensation of his hands reaching up to take hold of me."
    "Somehow that seems to make a difference, and together we work it out."
    show mike reverse cowgirl vaginal closed
    "Suddenly the head of his cock is running the length of my pussy."
    "All of that energy is being spent in one place alone."
    "And as soon as it's concentrated, things begin to change."
    "I feel myself opening up to him, slowly at first."
    "But as he starts to inch his way inside, momentum builds."
    "I'm sure this is how it's going to be, a little at a time."
    "So when all of my resistance seems to disappear a second later, it's like stepping off of a cliff."
    "Without warning, [mike.name] plunges the rest of the way into me."
    show mike reverse cowgirl blush
    "In a second I'm filled, with him so deep in me that there's nowhere I can go."
    "I have no idea if the sensation was the same for [mike.name]."
    "And I assume that it wasn't as intense on his side."
    "Because within seconds I feel him start to move in earnest."
    "I want to call out to him, to tell him that he should take it slowly."
    show mike reverse cowgirl -closed pain
    "But I can't find it in me to speak, and so I'm left at his mercy."
    "And it soon becomes apparent that [mike.name]'s not going to show me any."
    "As if all of his needs and appetites have been unleashed, he sets a crazy pace."
    "All I can do is hold on for dear life and try to ride it out until the end."
    "I can vaguely recall that this whole thing was my idea."
    "That I thought putting [mike.name] in a perilous position would make it that much more exciting."
    "Well I certainly got what I wanted."
    "I can't remember the last time I saw him like this."
    "[mike.name]'s working like a machine, pushing me to my very limits."
    "I couldn't stop him now, not even if I wanted to."
    "Normally I'd encourage him to explore my body to add to the pleasure."
    "But right now I'm actually thankful his hands are gripping me so tightly."
    "Because I don't think I could take anything more than he's already giving me."
    "At the same time, I don't feel like I'm in total control of my own body."
    "Every chance I get, I feel myself pressing down and grinding on him."
    "As if I want to push things further still, to be totally overwhelmed."
    "It's only when I feel myself on the verge of climax that I feel the promise of relief."
    bree.say "Oh fuck..."
    bree.say "[mike.name]..."
    show mike reverse cowgirl -pain ahegao with hpunch
    bree.say "Here I go!"
    with vpunch
    "Somehow the orgasm that sweeps over me changes the dynamic in a second."
    with vpunch
    "Where before [mike.name] was the one holding onto me, now I'm pinning him to the bed."
    "His hands drop helplessly to his sides, as if in a gesture of surrender."
    "And I feel the muscles in my abdomen squeezing him like never before."
    "But my moment of triumph is short-lived, as the inevitable happens."
    show mike reverse cowgirl -pain ahegao cumshot with vpunch
    "[mike.name] follows me, shooting his load a few seconds later."
    with vpunch
    "And that's all it takes to turn my muscles to water again."
    with vpunch
    "I collapse atop him, gasping and panting."
    "For a long while we lie there, both still and mostly silent."
    "But the reality of where we are slowly begins to dawn."
    scene bg bedroom3 with fade
    "Little by little we drag ourselves off of Sasha's bed."
    "And then we hunt around the room until we find all of our clothes."
    "That done, we slink out of the door and into safer parts of the house."
    "Each of us hoping that we won't get caught."
    "And all the time still feeling the after-effects of what we just did together."
    $ mike.sexperience += 1
    return

label mike_asleep:
    show sleep mike
    "[mike.name] is sleeping, I should leave before I wake him up..."
    $ game.room = "livingroom"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
