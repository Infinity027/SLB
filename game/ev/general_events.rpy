init python:
    
    Event(**{
        "name": "love_lesbian_adjust",
        "label": "love_lesbian_adjust",
        "priority": 0,
        "do_once": False,
        "quit": False,
        "once_day": True,
        })
    
    Event(**{
        "name": "samantha_event_01",
        "label": "samantha_event_01",
        "duration": 1,
        "priority": 500,
        "conditions": [
            IsHour(10, 17),
            MinDaysPlayed(7),
            HeroTarget(
                IsGender("male"),
                IsRoom("map")
                ),
            ],
        "do_once": True,
        "music": "music/roa_music/the_one.ogg",
        })
    
    Event(**{
        "name": "hanna_event_01",
        "label": "hanna_event_01",
        "duration": 1,
        "priority": 500,
        "conditions": [
            IsHour(10, 17),
            MinDaysPlayed(8),
            HeroTarget(
                IsGender("male"),
                IsActivity("train_hard", "train"),
                IsRoom("gym", "gymmachine"),
                MinStat("fitness", 20),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "ayesha_teaser",
        "label": "ayesha_teaser",
        "conditions": [
            IsDone("hanna_event_01"),
            IsHour(10, 17),
            IsDayOfWeek(1, 3, 5),
            HeroTarget(
                IsGender("male"),
                HasRoomTag("gym"),
                Not(IsFlag("ayeshateaser")),
                IsFlag("gymmember"),
                ),
            ],
        "priority": 500,
        "do_once": True,
        })
    
    Activity(**{
        "name": "ayesha_teaser_2",
        "display_name": "Go to Ayesha's show",
        "label": "ayesha_teaser_2",
        "duration": 0,
        "conditions": [
            IsDone("ayesha_teaser"),
            HeroTarget(
                IsGender("male"),
                Not(OnDate()),
                ),
            IsDayOfWeek(6, 7),
            IsHour(14, 18),
            PersonTarget(bree,
                Not(IsHidden())
                ),
            ],
        "icon": "ayesha",
        "do_once": True,
        })
    
    Event(**{
        "name": "alexis_event_01",
        "label": "alexis_event_01",
        "duration": 1,
        "priority": 500,
        "conditions": [
            IsHour(10, 20),
            HeroTarget(
                IsGender("male"),
                Not(OnDate()),
                MinFlag("promoted", 6),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "minami_event_01",
        "label": "minami_event_01",
        "duration": 1,
        "priority": 500,
        "conditions": [
            HeroTarget(IsGender("male")),
            IsHour(10, 20),
            MinDaysPlayed(13),
            ],
        "do_once": True,
        })
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    Event(**{
        "name": "lexi_event_01",
        "label": "lexi_event_01",
        "duration": 1,
        "priority": 500,
        "conditions": [
            IsHour(22, 4),
            MinDaysPlayed(9),
            HeroTarget(
                IsGender("male"),
                Not(OnDate()),
                IsRoom("alley"),
                MinStat("money", 250),
                IsFlag("lexiDelay", False),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "harmony_event_01",
        "label": "harmony_event_01",
        "duration": 1,
        "priority": 500,
        "conditions": [
            HeroTarget(
                IsGender("male"),
                IsActivity("attend_mass"),
                IsRoom("church"),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "harmony_event_02",
        "label": "harmony_event_02",
        "duration": 1,
        "priority": 500,
        "conditions": [
            HeroTarget(
                IsGender("male"),
                IsActivity("attend_mass"),
                IsRoom("church"),
                IsFlag("harmonystart", 1),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "palla_event_01",
        "label": "palla_event_01",
        "duration": 1,
        "priority": 500,
        "conditions": [
            IsHour(14, 18),
            MinDaysPlayed(10),
            HeroTarget(
                IsGender("male"),
                Not(OnDate()),
                IsRoom("mall1", "mall2"),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "office_party_set_up",
        "label": "office_party_set_up",
        "priority": 500,
        "conditions": [
            IsDayOfWeek("123"),
            HeroTarget(
                IsGender("male"),
                IsActivity("work", "workhard", "work_personal", "workhard_personal"),
                MinFlag("promoted", 5),
                ),
            PersonTarget("aletta",
                Not(IsHidden()),
                HasRoomTag("work"),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "office_party_missed",
        "label": "office_party_missed",
        "priority": 500,
        "conditions": [

            IsDayOfWeek("6"),
            HeroTarget(
                IsGender("male"),
                IsFlag("officeparty")),
            ],
        })
    
    Event(**{
        "name": "bree_sasha_pet_request",
        "label": "bree_sasha_pet_request",
        "duration": 1,
        "priority": 100,
        "conditions": [
            IsTimeOfDay("afternoon", "evening"),
            MinDaysPlayed(40),
            HeroTarget(
                IsGender("male"),
                Not(OnDate()),
                HasRoomTag("home"),
                ),
            PersonTarget(bree,
                Not(IsHidden()),
                HasRoomTag("home"),
                ),
            PersonTarget(sasha,
                Not(IsHidden()),
                HasRoomTag("home"),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "choose_dog",
        "label": "choose_dog",
        "duration": 1,
        "priority": 500,
        "conditions": [
            IsDone("bree_sasha_pet_request"),
            IsTimeOfDay("morning", "afternoon"),
            MinDaysPlayed(47),
            HeroTarget(
                IsGender("male"),
                IsFlag("chosen_pet", 'dog'),
                IsFlag("petdelay", False),
                Not(OnDate()),
                HasRoomTag("home"),
                ),
            PersonTarget(bree,
                Not(IsHidden()),
                HasRoomTag("home"),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "choose_cat",
        "label": "choose_cat",
        "duration": 1,
        "priority": 500,
        "conditions": [
            IsDone("bree_sasha_pet_request"),
            IsTimeOfDay("morning", "afternoon"),
            MinDaysPlayed(47),
            HeroTarget(
                IsGender("male"),
                IsFlag("chosen_pet", 'cat'),
                IsFlag("petdelay", False),
                Not(OnDate()),
                HasRoomTag("home"),
                ),
            PersonTarget(sasha,
                Not(IsHidden()),
                HasRoomTag("home"),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "name_dog",
        "label": "name_dog",
        "duration": 1,
        "priority": 500,
        "conditions": [
            IsDone("choose_dog"),
            IsTimeOfDay("afternoon", "evening"),
            MinDaysPlayed(50),
            HeroTarget(
                IsGender("male"),
                IsFlag("petdelay", False),
                Not(OnDate()),
                HasRoomTag("home"),
                ),
            PersonTarget(bree,
                Not(IsHidden()),
                HasRoomTag("home"),
                ),
            PersonTarget(sasha,
                Not(IsHidden()),
                HasRoomTag("home"),
                ),
            ],
        "do_once": True,
        })
    
    Event(**{
        "name": "name_cat",
        "label": "name_cat",
        "duration": 1,
        "priority": 500,
        "conditions": [
            IsDone("choose_cat"),
            IsTimeOfDay("afternoon", "evening"),
            MinDaysPlayed(50),
            HeroTarget(
                IsGender("male"),
                IsFlag("petdelay", False),
                Not(OnDate()),
                HasRoomTag("home"),
                ),
            PersonTarget(bree,
                Not(IsHidden()),
                HasRoomTag("home"),
                ),
            PersonTarget(sasha,
                Not(IsHidden()),
                HasRoomTag("home"),
                ),
            ],
        "do_once": True,
        })

label love_lesbian_adjust:
    call expression f"love_lesbian_adjust_{hero.gender}" from _call_expression_404
    return
label love_lesbian_adjust_male:
    python:

        for g in [g for g in Person.all_people(ignore_hidden=True) if hasattr(g, "lesbian") and g.love > 25 and g.lesbian > 15]:
            
            g.love -= (g.lesbian - 15)
    return

label minami_event_01:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice")
    if not result:
        $ hero.cancel_event()
        return
    mike.say "Ah...hey there - what's up?"
    minami.say "Hiya, hello there, big brother!"
    minami.say "Can you even believe how long it's been since we last spoke?!?"
    minami.say "I'm great - as you can kind of hear - how's you?"
    minami.say "Mom and Dad say hi too, and how are you, and all that other boring crap too!"
    minami.say "Well, [hero.name], are you even there?"
    minami.say "Say something, big bro!"
    "Did you ever imagine a person that can encapsulate the experience of an extreme sugar-rush just by talking to you?"
    "Make your head spin and you swear that your heart's pounding in your chest the whole time they're around?"
    "Well, I have, trust me."
    "And more than that, I actually grew up with them too."
    mike.say "Uh...hey, Minami."
    mike.say "Yeah...it's been a long time, I guess!"
    minami.say "It sure has, big bro!"
    minami.say "We've got so much catching up to do..."
    mike.say "Well...I was kind of thinking about maybe coming home some time soon."
    minami.say "No need to worry about that."
    minami.say "You'll be seeing me sooner than you think!"
    mike.say "Oh...okay, Minami."
    "Maybe I should back up a little here and explain a couple of things?"
    "And before you get the wrong idea, Minami's my little sister."
    "What's up with that - I'm allowed to have a little sister!"
    "I never mentioned her before now because it never came up in conversation..."
    "Anyway, she's a couple of years younger than me, and our folks adopted her when I was very young."
    "So we grew up together, and she's always been a part of my life."
    "Or at least she was until I moved out and got a place of my own."
    "Sure, she's intense and she can be a massive pain some of the time."
    "But she's also sweet, sensitive and loving."
    "And so yeah, I love her too, okay?"
    "Get over it."
    "Wait...what did she just say about seeing me soon?!?"
    mike.say "Ah, Minami..."
    mike.say "When you say I'll be seeing you soon..."
    minami.say "Oh dear, big bro!"
    minami.say "Did you go and forget that this is going to be my first semester at college?"
    "Of course, she'd told me that she was thinking of applying to the same college as me."
    "But that feels like ages ago, back when she graduated from high-school."
    "I guess I must have figured that I had plenty of time to plan for that."
    "So I pushed it to the back of my mind, then promptly forgot all about it."
    mike.say "Erm...no, Minami..."
    mike.say "How could I forget about something as important as that?"
    "In response to this, she lets out a high-pitched squeal that could be used as an instrument of torture."
    minami.say "That's SO great!"
    minami.say "I mean, yeah - Mom and Dad said you'll be busy and all that."
    minami.say "You know, they're all '[hero.name] has a job, Minami' and 'don't be a burden, Minami'!"
    minami.say "But I just know that we're going to have so much fun together!"
    minami.say "You can show me around all the coolest places to hang out."
    minami.say "And introduce me to all of your friends too."
    "She pauses for effect, and giggles a little, unable to contain herself as she broaches the next subject."
    minami.say "And I'm SO looking forward to finally meeting your girlfriend too!"
    minami.say "Just think of all the girly things we could do together - all the stories I could tell her about you..."
    mike.say "Okay, okay...let's take this a step at a time, yeah?"
    mike.say "We can talk about all of that stuff once you're here."
    minami.say "Don't worry - I'll text you and let you know when to expect me."
    mike.say "Wait...what?"
    "But she's hung up before I can pump her for more details."
    return

label office_party_missed:
    $ game.flags.officeparty = False
    if "office_party_set_up" in DONE:
        $ del DONE["office_party_set_up"]
    "Shit, I missed the office party. Aletta is going to be mad."
    $ aletta.love -= 4
    return

label office_party_set_up:
    show aletta
    aletta.say "[hero.name], there is an office party this Friday, I expect you to be there."
    mike.say "Count me in Aletta."
    aletta.say "Dress accordingly or you will not be able to get in..."
    $ hero.calendar.add(game.calendar.get_next_day_of_week("friday"), LabelAppointment(20, "aletta", "Office Party", "office_party", "office_party_missed"))
    hide aletta
    return

label office_party(appointment=None):
    $ game.flags.officeparty = False
    $ game.flags.officepartyDelay = TemporaryFlag(True, 14)
    $ DONE["office_party"] = game.days_played
    scene bg street
    "I'd be lying if I said I want to attend."
    "Hanging out with coworkers outside of work feels too much like... work."
    "It takes a lot to get myself ready and out the door, but I manage with the knowledge that [bree.name] will nag me all night for being antisocial if I don't."
    "Besides, I figure the worst case scenario is I get a few free drinks, wedge myself into a corner somewhere, and observe everyone else making idiots out of themselves for an hour or two before heading home."
    "My feet scuff the cold pavement as I drag them toward the restaurant, looming posh and intimidating before me."
    scene bg door restaurant with fade
    "Le Magnifique is scrawled over the doorway in illuminated, pretentious calligraphy."
    "Ugh."
    "At least it wasn't held in the office, anyway. I'm not sure I'd be able to force myself there after hours to pretend to socialize, whether [bree.name] nagged me or not."
    "Drawing a deep breath, I raise my hand and press it to the the ornate door handle."
    "The cold metal bites against my palm. After one final, torturous moment of hesitation, I pull the door open and allow myself inside."
    scene bg restaurant with fade
    "The pessimism clouding my head dissipates like a fine mist almost immediately under the warm atmosphere and uptempo music that greets me."
    "Familiar faces pepper the dim red mood lighting, laughing and sipping casually at their drinks."
    "They look completely different when they aren't staring at computer screens under bleak fluorescent bulbs."
    "Almost like... people who could be friends, rather than the lifeless mannequins that I've come to think of as coworkers."
    "Bodies that I've only ever seen in frumpy office attire sway before me in slinky evening dresses, curves accentuated by the hot red accents of light."
    "Before I can become too entranced by the sight, something snaps me abruptly back to attention."
    show cassidy date
    "Girl" "Hey there, stranger."
    "I jump at the sound of an unfamiliar voice, coming clear and confident from what feels like just over my shoulder."
    "I manage to get my mind back together enough to turn to the source, realizing all at once that I had frozen, staring, in the doorway."
    "Girl" "You're letting in all the cold air."
    mike.say "Oh."
    "I step forward from the door, allowing it to swing closed behind me with a final chilly gust."
    mike.say "Right, sorry about that. Uh, long day."
    "The girl in front of me just hums a breezy note, though her expression doesn't change."
    "I can't tell if it's a sound of amusement or just dry acknowledgement."
    "She stands leaning against the wall beside the doorway, looking luxurious in the shadows between two ornate pillars with a wineglass held delicately between two of her slender fingers."
    "Her dark eyes look me up and down, shamelessly sizing me up like an object on a shelf."
    "For some reason, my mouth has gone completely dry standing there before her. I swallow and manage to make myself speak."
    menu:
        "Ask if she's a new employee":
            mike.say "I don't think I recognize you from the office. Are you new?"
            "She gives a soft and smoky laugh that is almost lost beneath the bass of the music. I expect her to step forward from the wall and address me, but she doesn't."
            "Girl" "I've never been in your office."
            "She takes a long, purposeful drink of her wine to punctuate the sentence, watching me with eyes as fierce and determined as an animal over the brim of the glass."
            "I say nothing, and she casually lowers her gaze to the ruby liquid as she finishes her sip, shading those hawk's eyes beneath thick, dark lashes."
            "Girl" "My daddy is your CEO."
            "Oh."
        "Compliment her" if hero.charm >= 25:
            mike.say "Hello, beautiful. I didn't catch your name."
            $ cassidy.love += 1
            "She seems unimpressed, watching me for another second before dropping her gaze to the ruby liquid in her glass, swirling it idly."
            "Girl" "That's because I didn't give it."
            "One of those kinds of girls. That's fine, I've dealt with them before. I give my most charming smile in return, refusing to let her break me."
            mike.say "Consider this my formal request, then. You must be new in the company. I'm positive I would remember you if I'd seen you around."
            "Her dark eyes turn up to me. I expect her to step forward from the wall to shake hands, or at least smile at my charm, but she does neither."
            "I get the immediate impression that she does not consider us peers at all, which is only further cemented by her reply."
            "Girl" "My daddy owns your company."
            "Oh."
        "Ask if she crashed the party" if hero.charm >= 25:
            mike.say "You're not from the office, right? You just here to get some free wine?"
            $ cassidy.sub += 1
            "I smile, hoping that my negging comes across as charming despite my nerves."
            "She doesn't seem particularly charmed. Not so much as a hint of a smile touches the corners of her lips, though I watch almost desperately for one."
            "Girl" "My daddy's company paid for this wine."
            "Daddy's company?"
    mike.say "Dwayne?"
    "She takes a long, slow sip of her drink, watching me with eyes as cutting and calculating as a hawk's over the rim of her glass."
    "Her silence, her body language, and the distinct impression of being talked down upon were all answer enough."
    "She seems to enjoy the discomfort I'm obviously doing a poor job of concealing, finding myself suddenly face to face with the daughter of my boss's boss's boss, intimidating and gorgeous."
    "The first trace of amusement curls at one corner of her full lips, and I feel some of the panic inside of me soften."
    "Girl" "It's Cassidy."
    mike.say "Cassidy."
    "I have to swallow again before I can regain some composure. I need to get it together -- it isn't like she's a celebrity or anything."
    "No... it's worse than that."
    "A celebrity has less looming, imposing power over my livelihood."
    "I remind myself that she isn't my boss -- just a family member of the CEO, who I'd never even met -- and try to act like a part of me isn't withering inside before her."
    mike.say "Nice to meet you. My name's [hero.name]."
    "I hold out my hand."
    "She looks down at it for only a moment, though it feels like an awkward eternity, before she finally deems me worthy, stepping forward from the wall and taking it with the hand not still cradling her wine glass."
    cassidy.say "Pleasure."
    "I breathe a silent sigh of relief, and my smile spreads until it's nearly beaming as I give the soft grip of her hand a single shake."
    mike.say "Pleasure's all mine."
    "I release her hand and step back."
    "The music is pulsing through the room like a heartbeat, and though I know there are people all around us, my attention is fixed ahead of me."
    "She folds her arm back beneath the one holding her wineglass and seems to wait for me to say something."
    if hero.charm >= 25:
        menu:
            "Compliment her" if hero.charm >= 50:
                $ cassidy.love += 1
                mike.say "You look stunning, have I mentioned that?"
                "She doesn't blush or giggle, shifting her weight and looking almost bored."
                "I get the impression she gets told that a lot, whether by horny guys or just people trying to suck-up to the princess."
                "Either way, though, this time I do detect the tiniest hint of a smile on her primly pursed, full lips. I think it's satisfaction, though, more than swooning."
                cassidy.say "You haven't."
                "She replies, locking eyes with me and tilting her wine glass slightly in my direction as she continues..."
                cassidy.say "But thank you."
                mike.say "That dress is amazing."
                "I give a vague nod back over my shoulder toward the crowd."
                mike.say "Definitely makes you stand out."
                "Her smile spreads a little further. My eyes lock on her lips, and I wonder how soft they are beneath the velour of her lipstick."
                cassidy.say "It's Chanel."
                "I nod and look impressed, though all I really understand about that is that it means the scrap of fabric covering her body cost more than my rent... probably a couple months' rent."
            "Joke":
                "So what's someone like you doing mingling with the commoners?"
                "She exhales a soft laugh, quirking her brows slightly, as if surprised to find me amusing."
                cassidy.say "Daddy was here, he told me I might as well come down with him, since I had nothing else to do."
                cassidy.say "Make an appearance, you know."
                "She raises her empty hand and gives a slow, regal wave, one a queen might give while standing at an ornate railing, overlooking her subjects."
                "It's my turn to snort a laugh."
                mike.say "'Was' here?"
                "She nods, giving her eyes a slight roll and glancing irritably to the side."
                cassidy.say "I lost sight of him. He could be in the back in some VIP lounge or down the road with some business colleagues that stopped by, buying each other drinks."
                cassidy.say "He's impossible to keep track of. Social butterfly."
                "I give my best look of sympathy."
                mike.say "So you're stranded here."
                "She shrugs one bare shoulder."
                cassidy.say "Someone will eventually swoop in to rescue me and take me home."
                "I must have let something devious glint in my eyes, because she shoots a lidded look back to me and gave a single, small, curt shake of her head."
                cassidy.say "Don't hold your breath."
    else:
        "Don't you have better places to be, then?"
        $ cassidy.love -= 1
        "Her lip curls, slightly but perceptibly, as though she's suddenly found herself looking at some kind of unpleasant animal."
        cassidy.say "Yes, I do."
        "She turns her gaze away from me purposefully and won't reply to anything else I say to her. Eventually I give up and wander away, thoroughly and totally ignored."
    mike.say "Well, I guess I should make my way over to the actual party."
    cassidy.say "I guess you should."
    mike.say "Maybe I'll see you around more often?"
    "I do my best to only sound hopeful enough to be flattering, and not desperate."
    "I think I succeed, but as always, her mild and unmoved expression makes it hard to tell."
    cassidy.say "If you look in the right places."
    "I think I might have to go out of my way to figure out what those right places are."
    mike.say "I'll look forward to it, then."
    "She only smiles faintly, maybe a little amused. I hope she's laughing with me, and not at me."
    "She curls the fingers of her free hand in a wave, dismissing me, and I turn back to the rest of the party, stepping away from her shadowed corner of the room."
    hide cassidy
    if aletta.love <= 150:
        show aletta date
        "I sigh and decide to make the most of it, looking to find some cute female to flirt with when suddenly I spot Aletta from across the way."
        "We make eye contact and I quickly look away but it is too late."
        "She excuses herself and starts to come over to me."
        "I hope to find someone to quickly talk to, because who really wants to talk to their boss outside of work? But I don't have any such luck."
        aletta.say "Hello [hero.name], nice of you to come. We have had a wonderful turnout this year."
        mike.say "Um yes. It looks like it."
        "I look into my drink and then all around and it is quiet for a moment before continues."
        aletta.say "Anyway, I just wanted to let you know I think you have been doing an amazing job at work lately."
        aletta.say "I don't know what's changed, but you have really stepped up your game. Keep up the good work."
        "I'm not sure what to say."
        menu:
            "Say Thank you.":
                mike.say "Thank you Aletta, that means a lot. I'll do my best."
                "I see a flash of a small smile."
                aletta.say "I'm sure you will."
                if Person.is_not_hidden("aletta"):
                    $ aletta.love += 1
            "Say about time you noticed.":
                mike.say "Well, it's about time you noticed how hard I work."
                "She makes a displeased face."
                aletta.say "Just because it isn't said, doesn't mean I don't notice."
            "Say nothing.":
                if Person.is_not_hidden("aletta"):
                    $ aletta.sub += 1
                "I simple nod and take a drink."
        aletta.say "Well anyway, I also came over here to let you know that cameras will be going into the old copier room next week because supplies has been going missing so..."
        "You can imagine how embarrassing getting caught on camera doing anything... personal... with another employee would be."
        "I nearly choke on my drink."
        "Before I can say anything she holds up her hand."
        aletta.say "No need to say anything. I didn't see anything, hear anything, or say anything. I just thought you would like to know."
        "She takes a drink of her glass and I feel myself start to sweat. Was it getting hotter in here?"
        aletta.say "Come on, there is someone I would like you to meet. She is new to the company. She has been making eyes at you all night."
        "That gets my attention."
        mike.say "Really who?"
        "Aletta waves her hand."
        aletta.say "Come on, follow me."
        aletta.say "She's been with us a few months, but works in a different department."
        mike.say "Oh, makes sense why I haven't noticed her tonight."
        "We make our way over to the other side of the restaurant."
        aletta.say "This is Lavish, Lavish this is [hero.name]."
        show aletta date at left
        show lavish date at right
        "Lavish suddenly blushes and reaches out to shake my hand."
        lavish.say "Nice to meet you [hero.name] I have heard a lot about you."
        "She flashes a smile to Aletta and I wonder what is going on."
        mike.say "You do look familiar, have we met before?"
        "Lavish" "Oh um not really. Just in passing."
        mike.say "Oh oh right! I knocked all those files out of your hands... Sorry about that."
        "I give a nervous laugh but she gives a laugh of her own."
        lavish.say "That's alright."
        aletta.say "So, [hero.name], Lavish starts work in your area soon."
        aletta.say "I thought if she needed anything you would be a good one to help her out until she gets the hang of things."
        "Lavish beams at this and nods her head."
        "By now I realize that this girl has a crush on me, and I have to admit she is cute."
        "Wait, did my boss just set me up with someone?"
        mike.say "Of course, I wouldn't mind helping out at all. My desk is fairly easy to find."
        aletta.say "[hero.name] has been doing rather well lately. I'm sure you two could learn from each other."
        lavish.say "Oh yes! Aletta has told me how you have been leaving others in the dust."
        hide lavish
        show aletta date
        "I quickly turn to Aletta who looks like she has been put on the spot."
        mike.say "Has she now? Well I don't know if I would say that."
        hide aletta
        show lavish date at center
        lavish.say "Don't be modest! Your numbers have been great this last month!"
        "The only way for her to know that is if Aletta had shown her."
        "I turn to say something to her but she is no where to be found."
        "I shake my head."
        mike.say "Would you like to go get another drink with me?"
        "She gives me a look like I just made her night."
        lavish.say "Sure."
        hide lavish
    $ game.pass_time(3, needs=True)
    return

label palla_event_01:
    show palla at left
    show audrey normal at right
    "As I walk down the mall, I notice Audrey talking to a cute redhead."
    show audrey happy
    audrey.say "Hey."
    show audrey normal
    mike.say "Hola."
    show palla blank
    "The redhead glances over at me, her eyes judgmental."
    show palla talkative
    palla.say "Hi..."
    show palla blank
    show audrey talkative
    audrey.say "This is Palla. We've been friends for, like, forever!"
    show audrey normal
    show palla talkative
    palla.say "It's... nice... to meet you, [hero.name]. Audrey can't seem to stop talking about you."
    show palla blank
    show audrey talkative
    audrey.say "Hey, I talk about more than him, you know!"
    show audrey normal
    show palla talkative
    palla.say "Certainly hyping him up, though. If you like him, you like him. I can't account for your... tastes."
    show palla blank
    show audrey talkative
    audrey.say "Look, we gotta go. See you at work."
    hide audrey with easeoutleft
    show palla at center with ease
    "After Audrey leaves, Palla smirks."
    show palla talkative
    palla.say "Yes... hope to see you real soon."
    hide palla with easeoutleft
    "I'm left wondering just what the heck is going on with this Palla girl."
    "Was she being condescending... or was she flirting?"
    $ game.flags.pallastart = 1
    hide palla
    hide audrey
    return

label alexis_event_01:
    play sound cell_vibrate loop
    "Oh, looks like a new number."
    "Maybe someone calling in regards to work?"
    stop sound
    $ result = renpy.call_screen("smartphone_choice")
    if not result:
        $ hero.cancel_event()
        return
    mike.say "Hello? This is [heroname] [hero.family_name]."
    alexis.say "[hero.name]? [hero.name], do you remember me? OMG, it's me, Alexis!"
    mike.say "A... Alexis!? Wow, yeah, it has been awhile!"
    scene expression f"bg {game.room}" at blur(16), dark with dissolve
    show alexis with dissolve
    "Alexis... she was my girlfriend back in high school."
    "I was close to her family."
    "She and her sister Kylie were both pretty close back then, but after the 'incident,' all three of us kinda just fell apart."
    "I mean, the fact that she cheated on me with the PE teacher wasn't exactly good for our relationship, either."
    hide alexis with dissolve
    scene expression f"bg {game.room}" with dissolve
    mike.say "So, uh, how'd you get this number?"
    alexis.say "I found out from the company's directory, of course."
    alexis.say "I heard from a friend of a friend online that you got that big-time promotion."
    alexis.say "So, I thought I'd congratulate you."
    mike.say "Oh, thank you!"
    "In reality, it's really nice to hear from her again, but I got to make sure."
    mike.say "You're not just calling to say 'congrats,' are you?"
    "She giggles, the amount of times she's laughed during this conversation tells me she most certainly has an ulterior motive."
    "Time to see if it will be in my favor or not."
    alexis.say "You know me too well. Don't you?"
    alexis.say "You got me."
    alexis.say "Here's the deal: You got that cushy new job."
    alexis.say "I got myself a new dress."
    alexis.say "I was thinking we'd meet for dinner. What do you say?"
    menu:
        "No (Never meet Alexis again)":
            mike.say "Yeah, no."
            mike.say "Alexis. You had your chance."
            mike.say "I gave you my high school years, and you repaid me by cheating on me the first chance you could get."
            mike.say "In fact, Kylie has been cooler than you were."
            mike.say "I'm sorry, but I'm not going to fall for your trap again."
            alexis.say "Kylie!?"
            alexis.say "That psycho bitch? You don't know what you're messing with. She's-"
            mike.say "I'm not listening to you anymore, Alexis. Good bye."
            alexis.say "Wait. [hero.name]!"
            play sound phone_calling
            "I can't believe she had the nerve to try and scam me into paying her dinner."
            "Guess only one of us has moved on with our lives."
            "How pathetic."
            return
        "Yes":
            $ game.flags.alexisstart = True
            mike.say "Dinner? Yeah, actually that sounds great."
            mike.say "I haven't been able to properly celebrate yet. Where were you thinking?"
            alexis.say "Oh, just a little place called Tres Riche."
            mike.say "T... Tres Riche!? That's expensive!"
            alexis.say "Not for someone in your tax bracket, it isn't."
            "Well, that's certainly true, now..."
            "I am about to get into a lot of expendable riches."
            "I could splurge and impress my old girlfriend."
            mike.say "Well, when would you like to go?"
            "She pauses for a moment, her extended 'hmmmmm...' makes me feel she's just playing it up."
            alexis.say "I'll call you to let you know."
    mike.say "Works for me. Will I pick you up, or..."
    alexis.say "That's fine. I'll just meet you there."
    alexis.say "Let's take baby steps getting back into each other's lives."
    alexis.say "You know? Not like I'm gonna bang you on our first date, haha."
    mike.say "Well, it wouldn't be the first time..."
    alexis.say "Hm?"
    mike.say "Nothing, nothing. I'll see you there, okay?"
    alexis.say "Sounds great to me. See ya, Honey."
    play sound phone_calling
    "Heh... 'Honey.' It's been a long time since someone's called me that."
    "Well, new position, old girlfriend."
    "Things seem to be looking up for [hero.name]!"
    return

label harmony_event_02:
    scene bg church
    "I almost can't bring myself to go back to church after what happened last time."
    "Aside from the sheer embarrassment of it all, did it have to be a girl like that that walked in on me?"
    "Whenever I close my eyes, all I can see is her face as she got the entire load at almost point-blank range."
    "She's so innocent and pure that it felt as wicked as stabbing a puppy with a kebab skewer."
    "But in the end, I force myself to go back and sit in the same pew, trying to keep my head down."
    "I figure that if I can make it through the entire service without anyone cornering me, then I'm safe."
    "Because if they were going to confront me about it, why would they wait for their chance to do so?"
    "I mumble my way through the entire thing, nodding furiously whenever the priest mentions the idea of sin and going to Hell."
    "The passage of time seems to stop for me, and I'm just staring a hole in the floor between my feet like my life depends on it."
    "But then the sound around me changes to people mumbling and the tread of feet."
    "I look up to see that everyone on the same pew as me is getting up and filing out of the church."
    "That's it - the service is finally over!"
    "I hurry to follow the example of my fellow service-goers, shuffling out of the place as quickly as I can manage."
    "The fresh air outside never tasted so good, like freedom at long last..."
    show harmony
    "Girl" "Erm...hello..."
    "I recognise the voice instantly, as my blood runs chill in my veins."
    "Turning around slowly, I see the same curvy figure, the same cheery dress and the same open, innocent face."
    mike.say "H...Hello..."
    "I can see that the smile on her face is pained, as if this is every bit as hard for her as it is for me."
    "I suppose that's something at least, I know she's not confronting me to get angry or show me up in front of the rest of the congregation."
    mike.say "Look...about last week, I don't..."
    "A flush of resolution suddenly crosses her face, and she holds up a firm hand to keep me from going any further."
    "Girl" "PLEASE..."
    "She almost leaps at the realisation of just how loud and shrill her own voice is."
    "After coughing demurely, she gathers herself and tries again."
    "Girl" "Please, don't feel the need to mention it - I mean really, please don't."
    "Girl" "The good book tells us that it is only he without sin that shall cast the first stone of condemnation."
    "Girl" "John, chapter eight, verse seven."
    "I blink in surprise as she adds the source of the quote almost under her breath, like it's an unconscious tic."
    "Managing a weak smile, I try to console myself with the fact that she's apparently not mad at me cumming right in her face."
    mike.say "That's very Christian of you..."
    "Girl" "Well, that is why we're both here, after all!"
    "All I can offer is a slight chuckle in way of response."
    mike.say "Okay...if there's nothing else..."
    "I begin to turn away, and then I feel a hand suddenly grabbing my wrist."
    "Looking down, I see that the hand belongs to the church girl, and her grip's surprisingly strong."
    "Casting my gaze back up at her, she almost jumps and lets go as she realises that she's technically manhandling me right now."
    "Girl" "Sorry...I just wanted to ask you something, if that's okay?"
    "God, her eyes are so huge, and her body..."
    "I find myself nodding as I feel drawn in by the gravitational pull of her unfeasibly huge breasts."
    "Girl" "Oh, that's great!"
    "Girl" "I was wondering if you'd like to join me for some private Bible study classes?"
    "Girl" "You know, seeing as you're obviously such a terrible sinner and in serious danger of becoming a lost soul!"
    "What - Bible study, sinner, lost soul!"
    "My head snaps up and I look her straight in the eye."
    menu:
        "Refuse (Never meet Harmony again)":
            mike.say "Ah, no...I don't think that would be a good idea."
            "Girl" "But..."
            "I cut her off before she can come up with a perfectly sensible reason to disagree with me."
            mike.say "I'm actually undertaking an intense course of biblical study myself, in order to purge myself of my particular demons."
            "Girl" "Those would be the same ones you were busy purging yourself of last week in the spare room?"
            "I try to ignore the barbed nature of her question and press on regardless."
            mike.say "And as the good book tells us - 'God helps those who help themselves'."
            mike.say "Hezekiah, chapter six, verse one."
            "She frowns at my quote, wrinkling her nose in the cutest way imaginable."
            "Girl" "I think that verse is apocryphal!"
            "By now, I've managed to break away and escape into the crowd."
            mike.say "Thanks for the compliment, I made it up myself!"
        "Accept":
            $ game.flags.harmonystart = 2
            mike.say "Urm, yeah...sure, why not."
            "She positively beams at me, and I find myself returning the smile before it even dawns on me that I just said yes."
            "Girl" "Oh, that's just wonderful news!"
            harmony.say "I shall introduce myself then, Harmony, pleased to meet you."
            harmony.say "When you did...what you did to me last week, I was convinced it was the work of the Devil!"
            harmony.say "But somehow, I couldn't get the image of your face out of my thoughts...and my dreams..."
            harmony.say "So I spent time in quiet prayer and contemplation, asking God to show me the truth."
            "Her eyes are beginning to shine with a zealous light that's really becoming quite unnerving as she goes on."
            harmony.say "And he's revealed to me that it was all a clever plan to test my faith and charge me with the task of saving your soul for him!"
            "Jesus, does she ever stop talking about God?"
            "Especially when there are so many more enjoyable uses I can already think of putting her mouth to!"
            "Ah, yes...well maybe she does kind of have a point about me there..."
            "Who knows, I might actually get something out of these classes that makes me a better person?"
            "And even if not, it's an excuse to spend some one-on-one time with her under legitimate circumstances."
    "As I walk away through the rapidly thinning crowd of the congregation, I can't help but shake my head in confusion."
    "Am I not supposed to come to church so that I can feel better about myself?"
    "Not accumulate even more hang-ups and desires of a carnal nature?"
    return

label harmony_event_01:
    scene bg church
    "As I am waiting for the church service to start I am having trouble remembering why I came here again."
    "My dress clothes are itchy and hot, not to mention the fact that I had woken up late and with a serious personal problem and had had no time to take care of it."
    "It isn't really noticeable in these pants, but I still can't wait to go home and take care of it."
    "And with it taking so long for service to start I don't know if I am going to last."
    "How guilty would I feel for jacking off in a church bathroom?"
    "I look forward then as something catches my eye and my mouth drops open."
    show harmony
    "This beautiful- no gorgeous- little curvy red head had just walked up to the choir and was passing out the music."
    "My eyes follow her and I can't seem to look away."
    "That's when I notice my little problem in my pants just became a big one."
    hide harmony
    menu:
        "Masturbate in the bathroom":
            "Quickly excusing myself I hurry off to find the nearest restroom."
            "I am sure God would forgive me, after all, it was a human need."
            "I can't help it."
            "To my annoyance though, I reach the only discrete bathroom and an out of order sign is hanging on the door."
            "I groan loudly."
            "I am not walking in front of everyone with a hard on in church to go jack off in the bathroom."
            "Looking around I find a spare room and quickly step inside."
            "I check the time and then quickly undo my pants and free my member."
            "If I make it quick and then use some hand sanitizer that is everywhere in this place I will be fine."
            "I try to stay quiet but I am so horny I can't hold back the moan as I move my hand up and down my cock."
            "I don't know what it is about that girl but she really has me going."
            menu:
                "Imagine her sucking you off":
                    "I start to imagine her cute lipstick less mouth around my cock, bobbing up and down."
                    "The picture in my head is so pretty, but something just doesn't feel right about imagining someone I don't know giving me a blowjob while I jack off in a church."
                "Imagine getting to know her":
                    "I start to imagine what it would be like to meet her."
                    "She seems really sweet from what I saw of her interacting with the others."
                    "She might be a goody-two-shoes, but I find myself wanting to know more about her than just what she looks like."
            "Seeing that time is getting away from me I start moving my hand up and down my cock as fast as I can as my breathing picks up."
            "It just feels so good I can't help myself."
            "Suddenly I hear the door knob turn and panic flows over me, knowing that whoever opens that door is about to see me with my hand around my cock jerking off at the speed of light."
            "Girl" "Is someone in here? Is everything okay?"
            show harmony
            "The door swings open and to my horror it is the redhead freckle faced girl I was admiring earlier."
            show harmony cum
            "The sight of her is too much and before I can stop myself or turn I cum, and some of it lands on her innocent face."
            "She looks horrified at me and quickly looks at me touching my cum on her face, she then looks off to the side."
            "Girl" "I'm... I'm so sorry to walk in on you sir!"
            "Girl" "I... I didn't realize!"
            hide harmony
            "And with that she was off."
            "My heart pounding but for a whole different reason now, I quickly stuff myself back in my pants and go to find some place to clean up."
            "As I wash up I think about how weird it is that I'm the one in the wrong but yet she is the one who apologized."
            "Whatever her reason is, I'm sure I'm not getting a date with her anytime soon."
            $ game.flags.harmonystart = 1
        "Wait until you get home (Never meet Harmony again)":
            "I decide I don't have the guts to go take care of my needs in a church so I just sit there and try to hide my erection the best I can."
            "I don't realize I am staring until the second time she glances my way, and instead of a cute smile I get a uncertain frown and then she walks away."
            "I wait but I never see her come back, and I am not sure where she went."
            "Great going, idiot. I think. You scared her off."
            "So much for getting a date with the cutie now."
    return

label lexi_event_01:
    $ game.flags.lexiDelay = TemporaryFlag(True, 1)
    scene bg alley
    "I start making my way down the street, feeling another presence lingering nearby."
    "So I look over."
    "That's...when I see her."
    show lexi happy
    "She definitely stands out, leaning against the wall with her arms folded like she was just waiting for me to come along."
    "Bleached blonde hair, an outfit leaving little to the imagination. Taut denim shorts, from which I can clearly see a pink thong saying hello."
    "The top she is wearing is white and near transparent, I can see her nipples even from a distance."
    "She has a nice face, coupled with some silver piercings."
    "Frankly...she looks like a bit of a slut."
    "But! I suppose I can't judge on first glance..."
    "Girl" "Hi there stranger."
    "I fix my collar instinctively, fidgeting."
    "I wasn't expecting her to be interested in talking with me."
    "After all...I don't think I stand out all that much compared to other guys."
    "But maybe to her..."
    "Girl" "Well? Cat got your tongue or somethin'?"
    mike.say "No I...I'm not."
    "Girl" "Clearly..."
    "Her painted lips curl into a dark smile."
    "Girl" "What's your name?"
    "I didn't even realize it, but I'm already standing before her, talking with her casually like this."
    "I find myself telling her anyway."
    mike.say "[hero.name]...and yours?"
    "She tilts her head a little."
    "Girl" "The name's Lexi, love."
    lexi.say "Were you out with your friends tonight then?"
    mike.say "Yeah, basically."
    lexi.say "Did you have fun?"
    "I barely noticed it before, but she's gravitating closer towards me with every passing second."
    lexi.say "Did you, eh?"
    mike.say "Well uh...yeah. Yeah it was fun..."
    lexi.say "But I bet I could show you something a lot more enjoyable..."
    menu:
        "Follow her":
            $ game.flags.lexiStart = True
            pass
        "Don't follow her (Never meet Lexi again)":
            "I leave the skank behind me as I walk away."
            return
    "Wondering what on earth she means, I find myself being lured anyway."
    "Lexi waggles the fingers on one hand to encourage me along, while she backs up step by step into a nearby alleyway."
    "There's a smart part of me that's screaming 'STAY AWAY'."
    "Yet there's also a part of me that can't resist one bit..."
    "Before I even really know what I'm doing, I'm halfway down the path with her."
    "She keeps on beckoning me more, and I can't resist, I have to follow."
    "What I don't see is the hidden menace in her eyes."
    lexi.say "I think this should be private enough for us, right? Neat little spot."
    mike.say "Private enough for what?"
    "I'm only playing dumb. She knows and I know."
    "Just like that she comes sauntering closer, deliberately thrusting her chest forward."
    "Now that I feel I have a pass to look at her assets, I can acknowledge how stacked she is."
    "Lexi only confirms that by pressing up against my front and groaning just a little bit, as if she's already getting off on this."
    lexi.say "I know they were the first thing that you looked at. It's okay, you don't have to be shy..."
    mike.say "...Are you...sure about this?"
    lexi.say "Sure about what, big guy?"
    "'Big guy'? I've always felt kinda lanky, so I can only guess she means..."
    mike.say "Well...I mean we don't even know each other-"
    lexi.say "Oh come on, do we have to?"
    "She winks and brings her bottom lip beneath her teeth."
    "I glance down a little shyly, noting the piercing she has in her bellybutton."
    lexi.say "Why don't you just hush up and let me give you a night to really remember?"
    "Well, she's inviting it, so how can I resist? We both seem to want this."
    "So I let her start to feel me up, and meanwhile my own hands raise to her..."
    "Only...I don't even get a chance to touch her. And her hands are only at my shoulders when she suddenly pulls back."
    "As I look at her, startled, I can see her eyes aren't focusing on me anymore."
    "Something...behind me?"
    "Slowly...uneasily...I turn."
    hide lexi
    show danny
    thug_say "Hey buddy, what you doin'?"
    if not game.flags.thugfight:
        "Behind me, standing at the exit of the alleyway, is a tough looking guy. And I mean tough."
        "He's about as buff as they come, and stands tall at what must be over 6'4..."
        "Tan skinned with a biker's sort of hairdo."
        "Plus he's wearing a leather jacket, and that's all I really need to know."
        hide danny
        show lexi annoyed
        lexi.say "Danny, thank God you're here."
        "Surprised again, I look back at Lexi after hearing that."
        "She's leaning against the alley wall like some sort of damsel in distress, arm above her head and everything."
        mike.say "Lexi!? What are you doing? What are you saying!?"
        lexi.say "What do you mean, creep!?"
        "...'Creep'?"
        mike.say "Lexi..."
        hide lexi
        show danny
        $ thug_name = "Danny"
        thug_say "Okay, I think it's about time we get this over with."
        "Wondering what he means by such an ominous statement, I turn around, only for him to snatch my collar with both hands and hoist me up."
        "Guy must be strong, I wouldn't say I'm short."
        "Either way, I hit the wall hard and groan."
        "The back of my head blooms with pain, my vision weakening momentarily."
        "When it clears again, I can look down and see him grinning up at me."
        "In the background, Lexi has a similar expression."
        "So...she really set me up then?"
        "Maybe I should have expected this. I should have seen it coming, it was just too good to be true."
        show danny fist angry
        thug_say "Any last words before I pummel you into the ground?"
        "So this is it."
        "I die getting beaten in an alleyway by some mobster and his sly fox of a girlfriend."
        "Last words, eh?"
        "Do I have any regrets? Probably. Probably many, but I haven't got a time machine have I?"
        mike.say "...I guess...not..."
        thug_say "Great, saves me some time. Maybe if you get lucky you'll still be alive."
        "So it really is finished."
        "He might not finish me off completely, but I have a feeling that if I come to after this, I won't have a wallet anymore."
        "Sneaky little scheme they're running, must earn them a lot."
        "...But...is it truly the end?"
        "Am I really going to let myself get humiliated like this?"
        "I feel a sudden rush of adrenaline. Am I really giving up?"
        "How could I do it so easily after everything I've been through in my life before this?"
        "No...this is nothing, right? All I have to do is stop him."
        python:
            d = 25
            if not hero.has_skill("martial_arts"):
                d += 25
        if not hero.fitness >= d:
            "I swing my fist and hit him right between the legs. That should work, right?"
            "The toe of my shoe hits him hard, it almost hurts me too with how firmly I kick him."
            "I expect it to make him crumple."
            "Except...he doesn't even flinch. Just stares back at me mockingly."
            thug_say "Oh? Was that supposed to tear me down?"
            mike.say "Wai-!!"
            play sound punch_hard
            pause 0.2
            show danny fight win lexi at center, hshake
            pause 0.2
            with hpunch
            "Before I can even beg, he slams my head hard with his fist."
            "Pain throbs. I black out immediately..."
            "It was so easy for him. Proof I was definitely outmatched."
            hide danny
            scene bg black with dissolve
            pause 1
            scene bg alley with fade
            "I don't know how long I'm left lying there. Eventually I wake up again though."
            "My skull feels fit to burst, but I manage to sit up. Immediately my hands go for my pockets."
            "Gone. My wallet is gone."
            if hero.money > 500:
                $ hero.money -= 500
            else:
                $ hero.money.val = 0
            $ hero.grooming -= 5
            $ hero.energy -= 5
            $ hero.fun -= 5
            mike.say "Dammit!"
            "I slam my free hand down on the wet concrete, and look up above."
            "Rain spits down upon me like I'm being mocked or something."
            "I guess it must have started while I was knocked out. I'm not even sure how long I was."
            "At the very least it's still dark, the only light coming from the street lamps that reflect in the puddles too."
            "Either way, I force myself to stand up and groan, clutching the crown of my head and feeling a little blood there."
            "Of course, I did hit the wall pretty fucking hard. In a way I actually am lucky to be alive."
            "With strength like that, he could have done a lot worse..."
            "But I am alive, and I can move forward from this. And hopefully forget."
            "Especially Lexi."
            "I hope I never have to see her ever again."
        else:
            play sound punch_hard
            pause 0.2
            show danny fight lose lexi at center, hshake
            pause 0.2
            with hpunch
            "All the training I had at the gym is not for nothing."
            "I take a karate stance and hit him right in the stomach..."
            "He falls to the ground like a sack of beans, vomiting his lunch..."
            thug_say "Urgh..."
            hide danny
            show lexi angry
            lexi.say "Danny!!"
            "I quickly make a break for it, still clenching my sore fist."
            "That's right. Like hell I'm getting mugged tonight!"
            "I press on, eyeing the exit of the alleyway like it's the finish line for a race."
            lexi.say "Wait! [hero.name] wait!!"
            "Hearing Lexi calling me, I turn and glare over my shoulder at her. She's rushing after me, and she looks desperate now."
            "It's bizarre. Only minutes ago she was acting like I was some kind of stalking pervert that she wanted to shake off her shoe."
            "Yet now she thinks she can run after me and expect me to stop for her?"
            if hero.has_motor_vehicle:
                mike.say "If you think I'm driving your accomplice to the hospital you can forget it."
            else:
                mike.say "If you think I'm driving your accomplice to the hospital you can forget it. I don't even have a car."
            "I scoff, and start moving again."
            "I wish I had never even met her in the first place. For sure, I shouldn't have followed her in here so willingly."
            "I can feel myself sobering up with all the adrenaline, and realizing what a mistake I made."
            "I only hope that I never see her again..."
            $ game.flags.thugfight = 1
            $ game.flags.dannyvictory = 1
        call injured from _call_injured_14
    else:
        thug_say "Oh, it's you.."
        thug_say "Sorry sir, I didn't recognize you."
        thug_say "Come on Lexi, let's get out of here."
        $ game.flags.dannyvictory = 2
    return

label hanna_event_01:
    $ game.flags.hannastart = 1
    "While I'm working on my set, I have the strangest notion that I'm being watched."
    "I glance around the gym, watching as others workout without paying attention to anyone else in the facility."
    "After all, it's only polite to keep to yourself when you're working out."
    "What kind of weirdo would just be watching people instead of working out?"
    "But that's when my eyes catch them."
    show hanna treadmill with fade
    "Hotpants."
    "Running on the treadmill."
    "How can a girl wear such tight, short shorts and still be able to run?"
    "I may have not found the one checking me out, but I have stopped all things to check her out."
    "A sports bra, too? This girl is practically wearing nothing while out in public."
    "Is it possible she wants people to see her dressed like this? I know she's distracting me."
    "I feel light-headed as the blood rushes down from my face to regions further south."
    "Shit, I need to make sure no one notices the tent in my shorts, but-"
    show hanna sport sweat
    "She turns her head, her large gray blue eyes catching mine for a moment."
    "Her short blond hair practically blinds me as it reflects off of the light of the room, but I keep my glance upon her."
    "She smiles and waves. First contact, yes! Over her sun-kissed skin, I can still see the blush that forms as she sees me."
    "As if on reflex, she wipes the sweat from her brow, but a moment later, she looks down over her sweaty, hardly-dressed body."
    "Her deep red blush covering all of her face before she finally stops her machine and jogs back to the locker rooms, disappearing."
    hide hanna with moveoutleft
    "Who is that girl...?"
    "She's not bad looking at all, but... can someone who wears something like THAT be so shy?"
    "Or, is she hiding something?"
    "Will it be a good idea to try to find out, I wonder as I finish up my set and take a swig of my water."
    "Maybe, just maybe..."
    $ game.flags.ayeshateaser = TemporaryFlag(True, 2)
    return

label ayesha_teaser:
    scene bg gym
    "You always notice a new face at the gym, and for the most part, all they justify is a quick glance on account of their novelty."
    "Okay, if it's a particularly cute girl or a guy that you're instantly jealous of."
    "Then you might sneak a couple more glances when you think they're not looking."
    "But on this occasion, I was quite literally stopped in my tracks by the sight of someone new."
    "I tend to avoid the boxing ring and the mats where the meatheads and MMA freaks work out."
    "Maybe it's just me, but there's not much in it for me watching a pair of angry, buzz-cut guys in Lycra shorts grinding on each other."
    "So this means that when I walk by that part of the gym, I'm usually not really paying much attention."
    "I can see that there are two people sparring in the ring right now."
    "One's a regular that I vaguely recognise from among the other angry buzz-cut guys in shorts."
    "The other's hidden by the first guy, and all I can see of them is that they're pretty much handing him his own ass in there!"
    show ayesha normal
    "It's only when I get further away that I can see the other person sparring is actually a girl."
    "But what a girl!"
    "She must be at least six feet in height and built like an amazon."
    "Dressed in black Lycra shorts and a bra-top, her dark brown skin is slick with sweat from exertion, and her ebony braids whip back and forth as she moves."
    "I watch transfixed, as she demolishes the formidable guy she's sparring with, taking him apart piece-by-piece."
    hide ayesha
    show hanna normal
    if "hanna_event_02" in DONE:
        hanna.say "Like watching a lioness toy with her next meal, isn't it?"
        "I tear my eyes away from the action in the ring and see that Hanna's walked up beside me while I was distracted."
        mike.say "Uh...yeah...that pretty much sums it up!"
        "Hanna chuckles and shakes her head at my evident fascination."
    else:
        hanna.say "Like watching a lioness toy with her next meal, isn't it?"
        "I tear my eyes away from the action in the ring and see that the girl from the treadmill has walked up beside me while I was distracted."
        mike.say "Uh...yeah...that pretty much sums it up!"
        "The girl chuckles and shakes her head at my evident fascination."
    hanna.say "For the record, her name's Ayesha."
    hanna.say "She only just started training here a week or two ago."
    hanna.say "And word in the locker-room is that most of the beefcakes are already afraid of stepping into the ring with her!"
    "I shake my head as I look back to see the guy in the ring go down under a flurry of blows."
    "And then I gulp in genuine astonishment as I see Ayesha follow him down, sit astride his chest and begin to pummel him on the ring canvas."
    mike.say "She's...she's quite something!"
    mike.say "What is she - some kind of MMA fighter or martial artist, or something?"
    if "hanna_event_02" in DONE:
        "Hanna shrugs at the question, shaking her head again."
    else:
        "The girl shrugs at the question, shaking her head again."
    hanna.say "I don't know about any of that stuff."
    hanna.say "But someone that's had the privilege of being on the receiving end of her ground and pound told me that she's a wrestler."
    mike.say "A wrestler?"
    mike.say "Which kind - amateur or fake?"
    if "hanna_event_02" in DONE:
        "Hanna looks me in the eye before she answers, her expression becoming serious for a moment."
    else:
        "The girl looks me in the eye before she answers, her expression becoming serious for a moment."
    hanna.say "The latter - but I wouldn't let her hear you call it that!"
    "I shrug, sure that I can't possibly be overheard while Ayesha's still sparring."
    mike.say "Fake then - strange when she looks so tough in there!"
    hide hanna
    if "hanna_event_02" in DONE:
        "Hanna rolls her eyes at my dismissive comment and walks away, leaving me standing alone again."
    else:
        "The girl just rolls her eyes at my dismissive comment and walks away, leaving me standing alone again."
    "I take a last look round the gym and turn to head for the showers."
    ayesha.say "HEY, FUCK-FACE!"
    show ayesha angry
    "I turn around, an expression on my face that makes me look like I've been slapped hard with a wet fish."
    ayesha.say "Yeah, you - don't stand there with that dumb look on your fucking face!"
    ayesha.say "Who else am I gonna be shouting at, asshole?!?"
    "I continue to gape silently as I see Ayesha striding towards me, pulling off her MMA gloves with a face like thunder."
    ayesha.say "You're a little man with a real big mouth, you know that?"
    "Oh shit - did she actually hear what I just said?"
    ayesha.say "Where in the hell do you get off calling how I make a living fucking FAKE?!?"
    "As if there's a need to underline the fact that she did hear me just now, Ayesha thumps me in the chest with the flat of her hand."
    "I'm not prepared for the strength of the blow at all, and it sends me staggering back a couple of feet."
    "The pain is pretty bad, but I feel like she's also knocked the air out of my lungs too."
    "I just have enough time to see her advancing on me again and make up my mind as to what my next move should be."
    menu:
        "Stand up to her":
            "I've been abused, verbally and physically, in front of the entire gym, which makes me see red."
            "As Ayesha comes towards me, I pull myself up and meet her with all the force that I can muster."
            mike.say "Back off, you muscle-bound bitch!"
            "I make sure to get in her face as much as possible as I say this, trying to ignore the good few inches that she has on me in height."
            mike.say "This is the twenty-first century, in case, being a throwback cave-woman, you hadn't noticed."
            mike.say "Don't think for a second that I won't fight back if you pick a fight with me!"
            show ayesha normal
            "Though she doesn't back down one iota at this, I see a slight raise of an eyebrow and the hint of a smile from Ayesha."
            ayesha.say "Is that so?"
            ayesha.say "Well, maybe next time you think about running your dick-licker around me, you should keep it shut and see me in the ring instead?"
            ayesha.say "Think about it, tough guy!"
            hide ayesha
            "And with that, she breezes past me towards the women's locker-room."
            "I rub the back of my neck, puzzling over her sudden change in attitude."
            "Was she really that mad, or was she just feeling me out to see if I'd stand up for myself?"
        "Apologise":
            "Ayesha looks so powerful and imposing as she towers over me that I can't help but cower away from her."
            mike.say "Okay, okay...I'm sorry for what I said!"
            mike.say "It was dumb of me, and I just didn't think...please don't hurt me!"
            "I look at Ayesha from behind the shield of my own hands."
            "And I'm surprised to see her angry expression soften as she looks at me."
            mike.say "Please...I don't know any martial arts or wrestling stuff..."
            show ayesha blush
            ayesha.say "It's okay, I'm not going to hurt you."
            ayesha.say "I was just...mad...that's all."
            "As the anger leaves her face, I begin to see how beautiful Ayesha actually is up close."
            "She has deep, dark eyes and a sensual mouth that's somehow a little sad in its aspect."
            ayesha.say "You should keep comments like that to yourself, you know?"
            "I nod hesitantly."
            ayesha.say "Whatever you might think about wrestling, it's what I do to put food on the table, man."
            ayesha.say "It might not be as legit as you like your fights to be, but it's fucking hard on the body."
            "I nod furiously, and she nods once to acknowledge my own."
            hide ayesha
            "All of that said, she walks past me, towards the women's locker-room."
    "Once I'm showered and changed, I hurry out of the gym, hoping not to bump into Ayesha a second time."
    if "hanna_event_02" in DONE:
        "But as I pass the reception desk, Hanna calls me over, waving something in her hand."
    else:
        "But as I pass the reception desk, the girl from before calls me over, waving something in her hand."
    show hanna
    hanna.say "Hey, Ayesha asked me to give you these!"
    "I take what she's holding out to me, already dreading just what they might turn out to be."
    hanna.say "It's tickets to her next wrestling show - front row as well."
    hanna.say "I guess someone made an impression on our resident amazon, eh?"
    if "hanna_event_02" in DONE:
        "I can't help but groan, both at the look on Hanna's face and the prospect of seeing Ayesha wrestle."
    else:
        "I can't help but groan, both at the look on the girl's face and the prospect of seeing Ayesha wrestle."
    "But do I really have a choice of whether to go along to the show or not?"
    return

label ayesha_teaser_2:
    scene bg gym empty
    "I was nervous about the tickets that Ayesha gave to me to her wrestling show, and torn as to whether I should go along or not."
    "The plus side was, of course, that the tickets were free and the show was happening at the same gym that I work out at."
    "On the other hand, while I watched it as a kid, pro-wrestling's never really been my thing since I grew up and sort of became a responsible adult."
    "And I'm still pretty intimidated by Ayesha in her own right."
    "Add to that the theatrics and over-the-top trappings of wrestling, and it might just be too much for me to handle."
    "But then I remembered that I had two tickets, and thus the ability to bring along a companion to make the whole thing that much easier to bear."
    "My thoughts went immediately to Jack, not least because I knew that he was pretty into wrestling and fit the image I had in my head of a typical grapple fan too."
    "The only problem was that didn't want to look like one by default too."
    "Plus there was the fact I would have to listen to his encyclopedic and exhaustive knowledge of wrestling as well."
    "Those two counts against him were enough to score a pin-fall against him and set me to looking for another potential companion instead."
    "I was afraid that Sasha would just laugh in my face, so that left [bree.name] as the next name on my list."
    "Selling it to her as a kind of performance art and theatre with added acrobatics and simulated combat seemed to do the trick."
    "It's only when we arrive at the gym and find our seats in the front row that [bree.name] finally realises that I've not been strictly honest with her."
    show bree casual
    bree.say "Hey, that looks just like a wrestling ring right there!"
    bree.say "And there's a hell of a lot of fat, sweaty neck-beards in wrestling t-shirts here too!"
    bree.say "[hero.name], be honest - is this really a piece of experimental theatre?"
    "I shrug and try to look like the whole thing is an amusing misunderstanding."
    "But the look on [bree.name]'s face tells me I'm having little success."
    mike.say "Okay, okay...it IS a wrestling show."
    mike.say "So technically I did sort of tell you a lie."
    "[bree.name] gives me the stare of death, easily wiping the already weak smile right off of my face."
    mike.say "Sorry, okay - I just needed someone kind of normal to come with me to this thing."
    bree.say "I guess I should be flattered to know that I qualify as at least 'kind of normal'!"
    "I have to rescue this situation, and quickly - I can't let [bree.name] walk out and leave on my own after we've gotten this far."
    mike.say "Look, [bree.name] - cards on the table, okay?"
    "I hold up my hands up in a gesture of surrender."
    "And I'm relieved to see her shake her head at first, but then nod in grudging agreement."
    bree.say "You better make this good, [hero.name]!"
    mike.say "Honestly, [bree.name] - there's this girl at the gym who's wrestling on the show tonight."
    "[bree.name] looks instantly more interested at the mere mention of a woman being involved in tonight's proceedings."
    bree.say "Oh, you mean like on that GLOW show?"
    "Fate seems to have dropped a golden opportunity into my unsuspecting lap."
    "And I don't hesitate to grab it with both hands, then hang on for dear life."
    mike.say "Yes, exactly like that!"
    "[bree.name] smiles and even claps her hands together a little in a show of delight."
    bree.say "I LOVED that show - why didn't you say it was going to be like that from the start?"
    "The truth is that I have literally no idea if there's going to be anything like the damn show happening here tonight."
    "I don't follow wrestling and I didn't see GLOW either."
    "But I'm not going to stop that from giving me an in with [bree.name] to get her interested keeping her buttocks on her folding seat for the duration."
    bree.say "So, you were telling me about this girl from the gym?"
    "Shit, I'd all but forgotten about explaining Ayesha to [bree.name], thinking that the connection with her wrestling TV show would be enough to seal it."
    mike.say "Yeah...well, she kind of gave me the tickets to the show."
    mike.say "And I was a bit scared to come along on my own..."
    "I watch as [bree.name]'s eyes glaze over at my words, and she clasps her hands together with a sickly grin on her face."
    bree.say "Aww, [hero.name] - that's so sweet!"
    "I look at her with a look of almost sheer disbelief on my face."
    mike.say "What...you really mean that?!?"
    bree.say "Of course I do - she's desperate to have you come along and support her while she performs."
    bree.say "And you're so embarrassed about seeing her again that you needed a friend to come along for moral support!"
    bree.say "Seriously, it's like a plot from a romantic movie or something!"
    "Oops, she thinks that this is some kind of fairytale, with Ayesha as the shy little princess."
    "What's she going to think when she sees her for the first time and realises that she's more likely to grind my bones to make her bread?!?"
    "But I can hopefully deal with that problem when it arises, so there's no point bringing it up here and now."
    "The show starts a couple of moments later, mercifully cutting off the chance for [bree.name] to ask any more questions."
    hide bree
    "What follows is pretty much the kind of thing that I'd been expecting to see."
    "Rock music blares from the PA system, and one after another, a steady stream of gaudily-dressed wrestlers parade to the ring and ply their trade."
    "I soon find myself forgetting any misgivings I had as the over-the-top feel of it all actually starts to hook me and draw me in."
    "[bree.name] and I are soon laughing at the comedy spots, clapping at the aerial feats and even booing and hurling abuse at the villains who taunt the crowd."
    "The only fly in the ointment is that whenever a female wrestler appears, [bree.name] instantly coos over her and demands to know if the newcomer is the mysterious Ayesha."
    "So when the last match of the show is announced, and a brooding thrash-metal track begins to play, I can see a look of confusion on [bree.name]'s face."
    "This only becomes more pronounced as Ayesha's name is called over the PA and she strides out onto the stage like a conquering amazon."
    show ayesha fight
    "She's wearing yellow spandex with black stripes, a tiger's head on her belt and mask on her face completing the outfit."
    "Ayesha plays the part to the full, raising her arms and slashing with her hands to imitate a big cat as she growls at the audience."
    hide ayesha
    show bree casual
    "[bree.name] finally manages to tear her eyes away from Ayesha long enough to give me a shocked glance that speaks volumes."
    bree.say "THAT'S HER?!?"
    "The volume of the music saves [bree.name]'s shout from being audible to anyone other than me, and I nod in way of answer."
    "I raise my eyebrows and shrug in a manner that I hope lets her know this is the reason that I'm intimidated by Ayesha, and not the cutesy reason she had concocted beforehand."
    "Ayesha's opponent is a far smaller blonde oriental girl, dressed in grungy clothes and strutting around the ring with a cocky arrogance."
    bree.say "It can't be her against that other girl - she'll use the poor thing as a tooth-pick!"
    "I nod, unable to do anything but agree with [bree.name]'s assessment of the odds in the match that's about to begin."
    hide bree
    show ayesha fight
    "But as soon as the bell rings, I remember the fact that we've both been conned into forgetting about pro-wrestling."
    "This isn't a straight-up athletic competition, rather it's a choreographed performance that's supposed to pull at the audience's emotions."
    "I'm proven right as Ayesha initially overwhelms her smaller foe and the audience instantly shows its disapproval."
    "But then the smaller girl uses her quickness and smarts to duck and dodge, and the crowd's right there behind her."
    "As I watch Ayesha in the ring, I begin to appreciate the subtlety with which she's delivering her performance."
    "Far from being the monstrous villain that she's playing, I can start to see that she's taking great pains to keep the other girl safe while still making it look convincing."
    "I even feel myself becoming concerned for Ayesha when it's her turn to be the one taking the beating."
    "I never said she wasn't a striking woman to look at, but seeing her show vulnerability really brings home the fact that she's actually quite beautiful too."
    "But a moment later, I'm snapped out of my contemplation by the action spilling out of the wrestling ring and onto the floor."
    "Ayesha charges towards her opponent, only to have her pull down the top rope at the very last minute."
    "She keeps on going, pitching out of the ring and tumbling into the front row."
    "And, as fate would have it, she's falling straight towards me!"
    menu:
        "Protect yourself":
            $ protect = False
            hide ayesha
            "I might be able to pull off being a gentleman and act all chivalrous in better circumstances than this."
            "But the mere sight of Ayesha's substantial frame plummeting towards me means that I'm reacting on instinct alone."
            "All that I can do is grab for [bree.name] in the seat next to me and do my best to drag her into Ayesha's path to save myself."
            "Everything happens so fast that I'm sure she doesn't have the time to figure out what I just did."
            "People are scattering and folding chairs are skittering across the floor, making everything a mass of confusion."
            show ayesha fight
            "I look up in time to see Ayesha laid almost face-down on the ground perhaps a few feet from where I ended up being thrown."
            "For a moment, I can't see any trace of [bree.name] whatsoever."
            "But then Ayesha pulls herself up onto her elbows, and I can see that the smaller girl is trapped beneath the amazon."
            "[bree.name] looks petrified at first, but then a strange look seems to pass between them, one that I really can't make sense of at all."
            "I watch as Ayesha gets up slowly, pulling [bree.name] to her feet with a gentleness that belies her hulking frame."
            "[bree.name] allows herself to be drawn up, staring wide-eyed at the other woman the whole time."
            "Neither of them speak, but I see Ayesha cup [bree.name]'s chin in her hand for a moment before turning and walking away."
            "[bree.name]'s cheeks instantly flush a bright red at this, even more so when she sees me watching the silent exchange."
            "What was all of that?"
            "Did they just flirt with each other or something?!?"
        "Protect [bree.name]" if hero.fitness >= 50:
            $ protect = True
            hide ayesha
            "There's no time to even think about moving out of the way, yet everything seems to happen in slow motion."
            "I look up and see Ayesha, silhouetted against the lights above the ring and baring down on me."
            "She reminds me of an angel - not the flouncy pleasant kind, but the pissed-off avenging, wrath of God kind."
            "As she comes closer, I wonder if this is really such a bad way to go."
            "I mean, it has to beat being squashed by a truck or smeared across the tracks by an express train, right?"
            "And then she actually hits me, at which point everything becomes a scrabbling mess of flying people and folding chairs."
            "When the world finally begins to make some kind of sense again, the first thing I realise is that I have something big and heavy atop me."
            "And of course, that would be Ayesha herself, laid with her back to my belly as she struggles to regain her own senses too."
            "She seems to have no idea that she's atop me, and so when she begins to writhe and wriggle, I feel every single movement of her body against mine."
            "Ayesha tries to turn onto her belly a couple of times before she finally succeeds."
            "Her powerful limbs and firm muscles feel like they're giving me an impromptu and undisciplined massage the whole time."
            "And when at last she's on her belly, she's also still on top of me, easily covering and pinning me to the ground."
            "Before she hauls herself back to her feet, she looks down at me with eyes that are only now coming back to full awareness."
            "I can't manage anything but a nervous grin, which makes her face melt into an amused and almost predatory smile."
            "I've never been this close to Ayesha before, and I can't help noticing that her eyes are a deep, enchanting shade of brown."
            "Her smile is all the more intriguing thanks to her exceptional stature and the strength she exudes."
            "Trust me - this close up, it's almost like a pheromone that she exudes from her very pores!"
            show ayesha fight curious
            ayesha.say "Aww, don't be scared, man - I'm a real safe worker."
            "I feel her hand on my groin as she starts to get to her feet, squeezing me so that I feel an exquisite pain."
            show ayesha fight happy
            ayesha.say "I won't hurt you - unless you really want me to..."
            "And with that, she's up and climbing back into the ring to finish her match."
    hide ayesha
    "[bree.name] and I almost stagger out of the gym once the wrestling show is finally over."
    "Both of us have gotten far more involved in the evening's proceedings than we ever intended to."
    "Which means we're a little bruised and emotionally drained as we stagger home together."
    "Neither of us says anything, but it's safe to assume Ayesha's as much on [bree.name]'s mind as she is mine."
    if protect:
        if not demo:
            $ hero.smartphone_contacts.append("ayesha")
        "It's then that I reach into my pocket and feel something that I don't recall putting in there myself."
        "I discover a crumpled note, with a hastily-written name and a mobile number on it."
        "Of course, the name is 'Ayesha', and I can guess that the number is hers as well."
        "She must have shoved it into my pocket during the confusion when she fell out of the ring."
        "I stare at the note for a moment, and then cram it back into my pocket before [bree.name] can see it too."
    "I don't know if tonight has made me more or less afraid of Ayesha, and I don't know which would be the better of the two options either."
    $ game.pass_time(1)
    return



label samantha_event_01:
    show bg street
    samantha.say "..."
    samantha.say "Oh my gosh! Hey old roomie!"
    show samantha normal at center, zoomAt(1, (640, 720)) with fade
    pause 0.3
    show samantha normal at center, traveling(1.5, 0.5, (640, 1040))
    "I turn to see Samantha rushing up to me, a sweet smile on her face."
    "A touch of bitterness rises in me at the sight of her, but I suddenly feel bad- I couldn't be mad at her."
    "After all, I'd found my roommates pretty quickly, so I suppose everything was alright."
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey Cupcake."
    else:
        mike.say "Hey, Sam."
    "She's carrying a steaming cup of coffee, which I can only assume is filled to the brim with sugar."
    show samantha happy
    samantha.say "It's good to see you! I'm sorry I didn't get to say goodbye when we moved out."
    show samantha normal
    mike.say "Oh, well..."
    menu:
        "It's alright, I understand.":
            mike.say "If I know Ryan, he probably popped the question on you out of nowhere. I get it."
            show samantha talkative
            samantha.say "Thanks. You always know what to say, don't you?"
            $ samantha.love += 1
        "You should really tell me before you run off next time.":
            mike.say "You really had me panicking there for a minute. I wish you would have talked to me first."
            show samantha talkative
            samantha.say "... I'm sorry. You're right."
    samantha.say "Anyway~"
    if game.hour < 12:
        samantha.say "What are you doing out so early? Last I checked, you loved your sleep."
        show samantha normal
        mike.say "My roommates wake up pretty early, so I might as well be useful to society too."
        "I can see Samantha's scepticism at my words, but I would never admit my newfound... enthusiasm for my roommates."
    else:
        samantha.say "Where are you headed at this time of day?"
        show samantha normal
        mike.say "Just looking for something to do I guess- it was lucky I ran into you!"
    mike.say "So, how's that whole thing going? Did you guys find a nice apartment?"
    show samantha talkative
    samantha.say "Oh yeah! It's a lot smaller than the house, but really cozy. Ryan can be so romantic sometimes."
    show samantha normal
    "I could see the hearts rise in Samantha's eyes. Pushing down the urge to roll my eyes at their fluffy relationship, I couldn't help but admire her passion and commitment."
    "Still, I desperately try to move the conversation before she can start talking nonstop about her boyfriend."
    mike.say "You're still moving in, right? You left a few things back at our old place. You should come get them before Sasha and [bree.name] end up finding them."
    show samantha surprised
    samantha.say "Sasha and [bree.name]? You got two girls! Ryan didn't tell me that part about the replacements."
    show samantha flirt
    "She raises her eyebrows at me suggestively with a spark of playfulness in her eyes."
    show samantha happy
    samantha.say "You can finally get a girlfriend!"
    show samantha normal
    "I groan."
    mike.say "Don't say that! They're just there to help me pay for rent."
    show samantha talkative
    samantha.say "Aw, don't deny it! I know there's love hiding somewhere in that heart of yours."
    show samantha normal
    "The eye roll finally comes. Even though I knew she was teasing me, I couldn't help but feel a little irritated. Samantha suddenly elbows me."
    show samantha talkative
    samantha.say "C'mon, you know I'm just kidding. Even though it wouldn't hurt to get out there."
    show samantha happy
    "Samantha giggles, but I choose to ignore that last part. Finally, the conversation dies down a little."
    show samantha normal
    menu:
        "Ask about university":
            mike.say "How's uni going for you?"
            show samantha talkative
            samantha.say "It's alright. I should really find a tutor for some of it though."
            show samantha normal
            mike.say "I can always help you with some of that."
            show samantha talkative
            samantha.say "Oh, that's okay. Ryan said he would study with me soon!"
            show samantha normal
            mike.say "..."
            mike.say "That's good."
            "Samantha smiles and squints at me with warm eyes."
            show samantha talkative
            samantha.say "You remember my major, right?"
            show samantha normal
            mike.say "Um..."
            menu:
                "Literature":
                    mike.say "You want to write books."
                    show samantha happy
                    samantha.say "Yeah! Thanks for remembering."
                    show samantha normal
                    $ samantha.love += 1
                "Nursing":
                    "I could tell by the look on her face that I was wrong."
                    show samantha talkative
                    samantha.say "Nope! You know I've always wanted to write children's books. English literature!"
                    show samantha normal
                    mike.say "Oops..."
                "Education":
                    show samantha talkative
                    samantha.say "Haha! I love kids, but not that much. I'd rather make stories for them- English literature!"
                    show samantha normal
        "Ask about work":
            mike.say "Is the bakery far from your new apartment?"
            show samantha talkative
            samantha.say "It's not too bad. I can still walk there!"
            show samantha normal
            mike.say "That's good, at least."
            show samantha talkative
            samantha.say "I could be across town and still get there! Anything is worth those tasty discounts."
            show samantha normal
            "Ever since Samantha told me about her job at the bakery, I knew the only reason she went there was for the never ending sweets."
        "Ask about Ryan":
            show samantha happy
            samantha.say "Ryan!"
            show samantha normal
            "Her face lit up when I mentioned her boyfriend's name. She clasped her hands together in adoration."
            show samantha talkative
            samantha.say "I still can't believe we're living alone now. It's like all my dreams are coming true so fast!"
            show samantha normal
            mike.say "At least you're happy."
            show samantha talkative
            samantha.say "Aw, thanks. You should find happiness too, you know! When you find a sweet girl of your own and settle down, maybe we can trade some stories and advice!"
            show samantha normal
            mike.say "Trade stories? It feels like I already know everything about your boyfriend just from talking to you all the time."
            show samantha talkative
            samantha.say "Well, we can do something else then. You know I can't help it!"
            show samantha normal
    play sound msg_receive
    show samantha stuned
    "Samantha abruptly perks up and I hear her cell phone ring. She took it out from her back pocket and keenly put it to her ear."
    show samantha talkative at center, traveling(1.25, 0.5, (940, 880))
    samantha.say "Hey, Ryan!"
    show samantha normal
    "I hold back a groan. Everything would be about Ryan now- not that it wasn't before, but it seemed to be weighing down on me even more than usual in this moment."
    show samantha talkative
    samantha.say "Yeah, of course I did!"
    samantha.say "I'll be over as soon as I can!"
    samantha.say "Alright, love you too. See you in a bit!"
    show samantha normal at center, traveling(1.5, 0.5, (640, 1040))
    "She pressed one of the bright buttons on her phone screen and waved it around with excitement."
    show samantha talkative
    samantha.say "I'm sorry! I have to go; Ryan's taking me out!"
    show samantha normal
    "I chuckle with no real emotion behind my tone."
    mike.say "Ryan always takes you out."
    show samantha talkative
    samantha.say "I know! Isn't he a sweetheart?"
    show samantha normal
    menu:
        "Have fun.":
            show samantha talkative
            samantha.say "Thanks! We definitely will. Make sure you find something to do today! I don't wanna come back and find you still wandering around!"
            show samantha normal
            mike.say "I'm not wandering!"
            "Samantha giggles, but turns to leave, waving back at me with a look of fondness in her deep blue eyes."
            "I give a single wave back and watch as she skips away to get ready for her date."
            $ samantha.love += 1
        "Make sure you come to pick up your stuff.":
            show samantha talkative
            samantha.say "I will, I will! Stop worrying about it, I promise I'll get to it by the end of the week."
            show samantha normal
            "Before I can say anything else, she's already checking her phone as it buzzes with life."
            show samantha talkative
            samantha.say "Sorry, but I've really gotta go! I don't want to miss anything! See you later!"
            show samantha normal
            "With that, she turned and sped her way back to her new house to meet her boyfriend."
    hide samantha with easeoutright
    pause 0.3
    return

label bree_sasha_pet_request:
    scene bg livingroom
    show bree normal at left
    show sasha normal at right
    "I can always tell when [bree.name] and Sasha want something from me."
    "The clue is in the way they'll sidle up, trying to look nonchalant."
    "Normally they're both pretty forward in speaking their minds."
    "So coming at me sideways is a dead giveaway."
    "But oddly, neither of them ever seems to notice!"
    show bree smile
    bree.say "[hero.name]..."
    bree.say "We wanted to talk to you about something..."
    show bree normal
    show sasha shout
    sasha.say "Yeah, we do..."
    sasha.say "But we promise it won't take long!"
    show sasha normal
    "Oh, and I should have mentioned the tone of voice they use too."
    "It's sweet and innocent, almost to the point of making me smirk."
    "I imagine those are the voices they use on their dads when they want something."
    mike.say "Huh?"
    mike.say "Oh...hey guys!"
    mike.say "What was it you wanted to ask me?"
    show sasha embarrassed
    show bree hesitating
    "[bree.name] and Sasha look at each other for a moment."
    "And it seems each one is urging the other to speak first."
    "In the end, [bree.name] breaks the silence, blurting out her words."
    show bree talkative
    bree.say "We were thinking..."
    bree.say "This is a pretty big house, right?"
    show bree normal
    show sasha shout
    sasha.say "And we've got plenty of room."
    sasha.say "Even with all of us living here."
    show sasha normal
    show bree happy
    bree.say "So we could handle a new addition, yeah?"
    show bree normal
    show sasha happy
    sasha.say "Maybe the patter of tiny feet?"
    show sasha normal
    "I've been listening intently up to this point."
    "Happily letting the girls spin out their question."
    "But at the mention of tiny feet, I snap out of it."
    mike.say "Wha...what?!?"
    mike.say "You mean have a baby?!?"
    show bree surprised at startle
    show sasha stuned at startle
    bree.say "WHAT?!?"
    show bree stuned
    show sasha shocked
    sasha.say "No way!"
    sasha.say "Why would you even think that?!?"
    show sasha stuned
    mike.say "What else does 'patter of tiny feet' mean?!?"
    show bree hesitating
    show sasha embarrassed
    "[bree.name] and Sasha exchange another hasty glance."
    "And now they seem to understand my reaction."
    sasha.say "Erm..."
    show sasha shout
    sasha.say "Maybe I should have said little paws instead!"
    show sasha normal
    show bree smile
    bree.say "Yeah, Sasha - maybe you should!"
    show bree normal
    "I feel a sudden sense of relief."
    "And also a little bit foolish too."
    mike.say "You..."
    mike.say "You mean you want a pet?"
    "[bree.name] and Sasha nod at the same moment."
    "And it seems like they're feeling relieved too!"
    show bree smile
    bree.say "That's right!"
    show bree normal
    show sasha shout
    sasha.say "Yeah, we want a pet!"
    show sasha normal
    bree.say "Something cute and furry to cuddle!"
    show bree normal
    show sasha shout
    sasha.say "Something warm and soft to pet!"
    show sasha normal
    show bree smile
    show fx exclamation at left
    bree.say "It has to be a dog!"
    show bree normal
    show fx exclamation at right
    show sasha shout
    sasha.say "No, it's got to be a cat!"
    show sasha normal
    "Now I see where this is going."
    "Not only do they need me on board to get a pet."
    "They've also been arguing over what kind to get as well."
    "Looks like I'm going to be the one with the casting vote."
    menu:
        "I like dogs":
            "Just the thought of having a cat around the place turns me off."
            "They're evil little bastards, hissing and spitting all the time."
            "Plus they claw the furniture and their shit stinks worse than anything!"
            "Dogs, on the other hand, are one hundred percent amazing creatures."
            "Intelligent, loyal and loving - having one around the place would be amazing!"
            mike.say "I've always wanted a dog of my own."
            mike.say "So let's go get one!"
            "[bree.name] is instantly delighted with my choice."
            show bree happy
            bree.say "Yay!"
            bree.say "We're gonna get a doggy!"
            show bree normal
            "But of course, Sasha doesn't feel the same way."
            show sasha vangry
            sasha.say "Oh great, that's just what we need around here."
            sasha.say "Another dumb, drooling moron that humps everything!"
            show sasha annoyed
            "But [bree.name] and I hardly even acknowledge Sasha's reaction."
            "We're already too engrossed in planning for the new arrival."
            show bree smile
            bree.say "We're going to need dog food, a leash and a bed..."
            show bree normal
            mike.say "And treats - don't forget the treats!"
            show bree happy
            bree.say "Oh..."
            bree.say "We can't forget the actual dog!"
            $ bree.love += 4
            $ sasha.love -= 4
            $ game.flags.chosen_pet = "dog"
        "I prefer cats":
            "Just the thought of having a dog around the place turns me off."
            "They're stupid furry bastards, slobbering and barking all the time."
            "Plus they're super needy and you have to pick up after them too!"
            "Cats, on the other hand, are one hundred percent amazing creatures."
            "Independent, regal and elegant - having one in the house would be amazing!"
            mike.say "I've always wanted to own a cat."
            mike.say "So let's go get one!"
            "Sasha's instantly delighted with my choice."
            show sasha happy
            sasha.say "Yes!"
            sasha.say "We're gonna get a kitty!"
            show sasha normal
            "But of course, [bree.name] doesn't feel the same way."
            show bree vangry
            bree.say "Oh great, that's just what we need around here."
            bree.say "Another uppity, catty bitch that scratches everything up!"
            show bree annoyed
            "But Sasha and I hardly even acknowledge [bree.name]'s reaction."
            "We're already too engrossed in planning for the new arrival."
            show sasha shout
            sasha.say "We're going to need cat food, a collar and a bed..."
            show sasha normal
            mike.say "And treats - don't forget the treats!"
            show sasha happy
            sasha.say "Oh..."
            sasha.say "We can't forget the actual cat!"
            $ bree.love -= 4
            $ sasha.love += 4
            $ game.flags.chosen_pet = "cat"
        "No animals!":
            "Just the thought of having either a cat or a dog around the place turns me off."
            "Cats are evil little bastards, hissing and spitting all the time."
            "Plus they claw the furniture and their shit stinks worse than anything!"
            "And dogs are stupid furry bastards, slobbering and barking all the time."
            "Plus they're super needy and you have to pick up after them too!"
            "I never understand why people want to burden themselves with pets."
            mike.say "Ah..."
            mike.say "I don't want either."
            mike.say "Pets are just a hassle I don't need!"
            show bree stuned
            show sasha stuned
            "[bree.name] and Sasha look at me in amazement."
            "It's like I'm speaking a language they don't understand."
            show bree surprised
            bree.say "But...but..."
            show bree sad
            bree.say "How can you not want a cute doggy?!?"
            show bree gloomy
            show sasha surprised
            sasha.say "What's wrong with you?"
            sasha.say "What have you got against a sweet kitty?!?"
            show sasha sad
            "All I can do is shrug and shake my head."
            "It's like someone asking me why I like to breath oxygen."
            mike.say "I'm just not a pet person, okay?"
            mike.say "Some people are and some people aren't."
            mike.say "So I'd rather not have a bothersome animal in the house!"
            show bree sad
            bree.say "Well...I think you're just being mean!"
            show bree gloomy
            show sasha vangry
            sasha.say "Yeah - thanks for nothing!"
            hide bree
            hide sasha
            with easeoutright
            "[bree.name] and Sasha walk off in a huff."
            "But I feel better for having stood my ground."
            "I just know that they'd have gotten tired of the thing before too long."
            "And then I'd have ended up picking up the shit of an animal I never wanted to start with!"
            $ bree.love -= 4
            $ sasha.love -= 4
    $ game.flags.petdelay = TemporaryFlag(True, 7)
    return

label choose_dog:
    $ game.room = "street"
    scene bg animalshelter with fade
    "The time has finally come for [bree.name] and I to go down to the local animal shelter and pick out a dog."
    "We've already bought all the stuff we can get our hands on without having an actual dog."
    "And I think we're both more than a little nervous about meeting our potential new fur-baby."
    show bree casual at center, zoomAt(1.25, (640, 880)) with dissolve
    "As soon as we get inside the place, [bree.name] grabs hold of my arm, trembling with excitement."
    show bree surprised
    bree.say "Oh...my...god!"
    show bree happy
    bree.say "It's actually happening!"
    show bree smile
    bree.say "We're going to be parents!"
    bree.say "I...I mean pet owners!"
    bree.say "How are you feeling, [hero.name]?"
    bree.say "Are you as excited as me?!?"
    show bree normal
    menu:
        "Of course I am":
            "I know that I should reign it in and be the sensible one here."
            "But I'm bursting at the seams with excitement."
            "I just can't keep it in!"
            mike.say "I'm shaking, [bree.name]!"
            mike.say "Feel my hand if you don't believe me!"
            "[bree.name] accepts the invitation to take my hand."
            "But she squeezes it and then holds it tight instead."
            "And we share a meaningful look as we prepare to meet our new pet."
            $ bree.love += 2
        "Keep calm":
            "The truth is that I'm almost as exited as [bree.name] is right now."
            "But this is a serious choice we're about to make."
            "It's a commitment to care for a living thing."
            "So I need to be the responsible one here."
            mike.say "I'm excited to meet them, [bree.name], for sure."
            mike.say "But we still need to make sure we pick the right dog, okay?"
            show bree stuned
            "[bree.name] looks surprised for a moment, but then she nods."
            show bree smile
            bree.say "You're right, [hero.name]."
            show bree talkative
            bree.say "Be serious now."
            show bree smile
            bree.say "And then, when we get them home, spoil the dog rotten!"
            show bree normal
            $ bree.love += 1
            $ bree.sub += 1
        "Meh...":
            "I can't help laughing and shaking my head at [bree.name]'s excitement."
            "It's so her to be childish at a time like this."
            mike.say "You could at least try to keep a lid on it, [bree.name]!"
            mike.say "Maybe pretend to be an adult until we're out of here?"
            mike.say "After all, we want them to think we can handle a dog!"
            show bree annoyed
            "[bree.name] looks more than a little hurt."
            "But she seems to take the warning to heart."
            show bree talkative
            bree.say "O...okay, [hero.name]."
            bree.say "But you don't have to be so mean to me!"
            show bree normal
            $ bree.sub += 2
    with fade
    "Pretty soon we're inside the place and we go through the necessary paperwork."
    "I guess they have to check us out before they'll hand over a dog to our care."
    "But once the boring stuff is done, we get shown through to the actual kennels."
    "And from that point on, [bree.name] and I are assaulted with constant canine cuteness!"
    "Almost every dog we see seems to come alive at the sight of us."
    "They bark and yelp, all trying to get the attention of a potential new owner."
    "But the member of staff taking care of us steers a path in a definite direction."
    show bree flirt
    bree.say "Aww!"
    show bree surprised
    show fx question
    bree.say "What about this little guy?"
    show bree smile
    mike.say "Yeah, he looks great!"
    show bree normal
    "Shelter staff" "Sorry, he doesn't fit your profile."
    "Shelter staff" "We narrowed it down to these two possibilities..."
    "I look in the direction they're pointing."
    "And I see two very different dogs staring up at me."
    "One is a gorgeous golden retriever."
    "It looks instantly friendly and more than a little intelligent."
    "The other is an odd little dog that looks like a pug of some kind."
    "It's face is a mass of wrinkles and it snorts more than it breathes."
    "Plus I swear I hear it fart while we're standing there too!"
    show bree happy
    bree.say "Oh dear..."
    bree.say "They're both such cuties!"
    show bree smile
    bree.say "Which one do you like best, [hero.name]?"
    show bree normal
    "I take a second look at the dogs, trying to make up my mind."
    menu:
        "I like the golden retriever":
            "Sure, the pug's cute - but I hear they have serious health issues."
            "And the retriever just looks like so much less hassle in those stakes."
            "Plus he's simply gorgeous, and I can already see myself walking him with pride."
            mike.say "Ah..."
            mike.say "It's a tough choice, [bree.name]!"
            mike.say "But I think we should take the big guy."
            show bree happy
            "[bree.name] claps her hands together in sheer delight."
            show bree smile
            bree.say "Oh, I'm so glad you said that, [hero.name]!"
            bree.say "He's the one I really wanted too!"
            $ bree.love += 1
        "I like the pug":
            "Sure, the retriever's cute - but he's not as funny looking as the pug!"
            "If I had a dog like that, I'd spend so much time laughing at it."
            "That's why I know that we have to choose the pug."
            mike.say "We've got to get the pug, [bree.name]!"
            mike.say "He's just so freaky-looking!"
            mike.say "Don't you think?"
            show bree stuned
            "Instantly I can feel everyone staring at me."
            "It's like I said the worst thing possible."
            show bree talkative
            bree.say "Erm...no."
            bree.say "I think we'll take the retriever."
            bree.say "We're getting a pet to be a companion."
            bree.say "Not for you to laugh at it!"
            $ bree.sub += 1
        "Let [bree.name] choose":
            "Sure, the pug's cute - but I hear they have serious health issues."
            "And the retriever just looks like so much less hassle in those stakes."
            "Plus he's simply gorgeous, and I can already see myself walking him with pride."
            "But maybe [bree.name]'s got a better eye for these things than me?"
            mike.say "I don't know, [bree.name]."
            mike.say "It's a tough choice!"
            mike.say "Maybe you should have the final say?"
            show bree stuned
            "[bree.name] looks at me in surprise for a moment."
            show bree normal
            "Then she nods and smiles."
            show bree smile
            bree.say "Aw...thanks, [hero.name]!"
            bree.say "The pug's sweet, for sure."
            show bree happy
            bree.say "But I think we should adopt the big guy!"
            $ bree.love += 2
    show bree happy with fade
    "With the big decision made, it's just a matter of signing the paperwork."
    show dog at left
    "And in what feels like no time, [bree.name] and I walk out of the shelter with him on a leash."
    "I can't help smiling like a fool at the sight of the dog."
    "[bree.name]'s beaming too, constantly cooing over him and talking to him like he's a baby."
    "And for his own part, the dog seems to be the happiest of all."
    "He walks beside us and keeps looking up, as if to check we're still there."
    "And it's then that I realise I'm walking along with two stunning blondes!"
    "Of course, I wouldn't dare to say as much to [bree.name]."
    "But the thought does make me smile a little wider than before."
    $ game.flags.petdelay = TemporaryFlag(True, 3)
    return

label name_dog:
    scene bg livingroom
    show dog zorder 3 at center, zoomAt(0.8, (640, 720))
    with fade
    "It's been a couple of days since we picked the dog up from the shelter."
    "And he's been settling in pretty well since then, endearing himself to everyone."
    "Even Sasha, who was dead set on having a cat, seems to be warming to the big lug!"
    "I've been walking him every chance I get, and that's what makes me realise something."
    "When I let him off the lead for a run, what am I supposed to shout to call him back?"
    "I've been getting by on 'boy' and the usual 'good dog'."
    "But we haven't actually decided on a name for him yet!"
    "As soon as I get back in from our latest walk, I call out to the girls."
    mike.say "[bree.name]...Sasha..."
    mike.say "Get in here!"
    show bree zorder 2 at left with easeinleft
    show sasha zorder 1 at right with easeinright
    "[bree.name] appears first, and then Sasha a moment later."
    show bree smile
    bree.say "What's up, [hero.name]?"
    show bree normal
    show sasha shout
    sasha.say "Yeah - what's with all the shouting?"
    show sasha normal
    "I point to the dog, who's happily scratching his ear with his back paw."
    mike.say "The dog..."
    mike.say "We never decided what to call him!"
    show bree stuned
    "[bree.name] looks instantly shocked by this, her eyes going wide."
    "She kneels down and starts to cuddle the dog."
    "Who obviously loves all the sudden and unexpected attention."
    show bree talkative
    bree.say "Oh, my poor little baby!"
    bree.say "How did we ever forget!"
    show bree sad
    bree.say "Can you ever forgive your mommy?"
    show bree sadsmile
    "Sasha and I both stare at this show of affection for a moment."
    "But then she looks up at me and shrugs."
    show sasha whining
    sasha.say "Geez..."
    sasha.say "I thought you guys decided that already?"
    sasha.say "But if not, I say we call him 'Bruce'."
    show sasha shout
    sasha.say "He looks like a Bruce to me!"
    show sasha normal
    show bree talkative
    bree.say "Oh no!"
    bree.say "He is SO not a Bruce!"
    show bree smile
    bree.say "Are you, baby?"
    bree.say "He's a 'Zack', aren't you, my precious?"
    show bree normal
    show sasha annoyed
    "Sasha rolls her eyes at this."
    show sasha shout
    sasha.say "What about you, [hero.name]?"
    sasha.say "What do you think we should call the drool-machine?"
    show sasha normal
    "I look the dog square in the face for a moment."
    "And then it comes to me..."
    menu:
        "Zack's great":
            mike.say "I agree with you, [bree.name]."
            mike.say "I think Zack suits him."
            "[bree.name] hugs the dog even closer to her."
            "And the animal just sits there and takes it."
            show bree happy
            bree.say "Yay!"
            show bree smile
            bree.say "Congratulations, Zack!"
            bree.say "You finally got a name!"
            $ bree.love += 2
            $ sasha.love -= 1
            $ game.flags.pet_name = "Zack"
        "Bruce seems fine":
            mike.say "I agree with you, Sasha."
            mike.say "I think Bruce suits him."
            show bree annoyed
            show sasha happy
            "[bree.name] looks disappointed, hugging the dog closer to her."
            show sasha normal
            "But Sasha smiles, as though she finally has something invested in the animal."
            show sasha shout
            sasha.say "Welcome to the family, Bruce."
            sasha.say "You're noisy, messy and you hump everything."
            sasha.say "You'll fit in just fine!"
            $ sasha.love += 1
            $ game.flags.pet_name = "Bruce"
        "Let me think":
            mike.say "You know..."
            mike.say "I think he's more of a 'François'!"
            mike.say "If you ask me, he just gives off a Gallic vibe."
            "[bree.name] hugs the dog even closer to her."
            "And the animal just sits there and takes it."
            show bree happy
            bree.say "Yay!"
            show bree smile
            bree.say "Congratulations, François!"
            bree.say "You finally got a name!"
            show bree normal
            show sasha normal
            "Sasha smiles, as though she finally has something invested in the animal."
            show sasha shout
            sasha.say "Welcome to the family, François."
            show sasha happy
            sasha.say "You're noisy, messy and you hump everything."
            sasha.say "You'll fit in just fine!"
            $ sasha.love += 1
            $ bree.love += 1
            $ game.flags.pet_name = "François"
    return

label choose_cat:
    $ game.room = "street"
    scene bg animalshelter
    "So we agreed that it was time to get a pet for the house and that it was going to be a cat."
    "We went out and bought a collar, litter tray and a ton of food from the pet store."
    "And now the big day has come around at last - Sasha and I are off to the shelter to pick out our new feline companion!"
    "I feel more than a little nervous myself, daunted by the fact I'm about to become a pet-owner."
    "But all it takes is one glance to see that Sasha's crackling with nervous energy!"
    "She manages to keep a lid on it as we fill in the paperwork at the desk."
    show sasha casual at center, zoomAt(1.25, (640, 880)) with dissolve
    "But it starts to spill out as we're waiting to be shown into the actual cattery."
    show sasha happy
    sasha.say "I can't believe it, [hero.name]!"
    show sasha shout
    sasha.say "It's actually happening!"
    sasha.say "We're gonna get a kitty!"
    sasha.say "Can YOU believe it?"
    sasha.say "This is great, right?"
    show sasha normal
    menu:
        "Yeah!!!":
            "Part of me knows that I should be trying to be the adult here."
            "After all, we need to come off as responsible potential cat-owners."
            "But I'm just as excited as Sasha, maybe even more so!"
            mike.say "I know what you mean, Sasha."
            mike.say "I can't believe this is really happening myself!"
            mike.say "We're like minutes away from owning a cat all of our own!"
            "Without prompting, Sasha reaches out and takes hold of my hand."
            "She squeezes it tightly and smiles like the proverbial cat that got the cream."
            $ sasha.love += 2
        "Let's stay calm":
            "I know that I'm feeling every bit as excited as Sasha is right now."
            "But we have to show the staff at the shelter we're serious about this."
            "And that means at least one of us needs to behave in a mature manner."
            mike.say "I'm excited too, Sasha."
            mike.say "But let's save the gushing for when we get back home, okay?"
            mike.say "We want them to know we're serious about caring for this cat."
            mike.say "That we're mature enough to handle the responsibility."
            show sasha normal
            "Sasha nods at this, taking the suggestion to heart."
            show sasha shout
            sasha.say "You're right, [hero.name]."
            sasha.say "I'll try to keep a lid on it."
            $ sasha.love += 1
            $ sasha.sub += 1
        "Meh...":
            "What's Sasha trying to do?"
            "Make the shelter staff think that we're a pair of morons?"
            "They're going to be watching us like hawks."
            "So we need to be on our best behaviour!"
            mike.say "Quit it with the childish shit, Sasha!"
            mike.say "We're supposed to be responsible adults here."
            mike.say "You're going to make them think we're idiots talking like that!"
            show sasha annoyed
            "Sasha looks instantly chastened by my words."
            "She casts her gaze down to her feet, refusing to meet my eye."
            show sasha whining
            sasha.say "O...okay, [hero.name]..."
            sasha.say "I get it!"
            sasha.say "But there's no need to be so mean..."
            $ sasha.sub += 2
    show sasha normal with fade
    "Finally the member of staff arrives to take us into the cattery."
    "And then we're ushered into a world of fabulous feline finery."
    "There are pens holding cats to either side of us."
    "And every one of them looks more adorable than the last."
    "Shelter staff" "We've looked at your circumstances."
    "Shelter staff" "And we've narrowed it down to two candidates."
    "They point towards a couple of pens before us."
    "In the first is a petite, short-haired black cat."
    "It seems to respond as soon as we look down at it."
    "And I can even hear it purring through the glass."
    "The second pen contains something that seems to be more fur than cat."
    "And a flat, wrinkled face stares up at us from the middle of it all."
    "I'm pretty sure there's a cat in there somewhere."
    "But it seems less than impressed at the sight of us."
    show sasha happy
    sasha.say "Oh man..."
    show sasha shout
    sasha.say "They're both SO cute!"
    sasha.say "I don't know how I'm going to choose between them!"
    sasha.say "What do you think, [hero.name]?"
    show sasha normal
    menu:
        "Why not the black cat":
            "I can't stop looking at the crazy-haired cat."
            "And I'm sure it'd be a real conversation-starter."
            "But I can't choose a cat for such a frivolous reason."
            "So the black cat is the only option."
            mike.say "I think we should take the black one, Sasha."
            mike.say "He looks really healthy."
            mike.say "And friendly too."
            show sasha happy
            "Sasha punches the air, taking me by surprise."
            sasha.say "Yeah!"
            show sasha shout
            sasha.say "Great minds think alike, [hero.name]!"
            sasha.say "That's the one I wanted too."
            $ sasha.love += 1
        "I like this ball of fur":
            "I can't stop looking at the crazy-haired cat."
            "I'm sure it'd make a great conversation-starter."
            "And what better reason could there be to choose a cat?"
            "So there's really only one option."
            mike.say "I think we should take the hairy one."
            mike.say "It's really goofy-looking."
            mike.say "People are gonna die laughing when they see it!"
            show sasha upset
            "Instantly I see Sasha and the shelter worker frown at me."
            "And I can feel a wave of disapproval from their direction."
            show sasha whining
            sasha.say "No, [hero.name], we're not getting that one!"
            sasha.say "That's a terrible reason to choose a cat."
            sasha.say "We're getting the black one, and that's that."
            $ sasha.sub += 1
        "Let Sasha choose":
            "I can't stop looking at the crazy-haired cat."
            "And I'm sure it'd be a real conversation-starter."
            "But I can't choose a cat for such a frivolous reason."
            "On the other hand, the black cat looks healthier."
            "And it seem pretty friendly too."
            "How am I supposed to decide?"
            mike.say "You know what, Sasha..."
            mike.say "Getting a cat was your idea."
            mike.say "So you should be the one to choose."
            show sasha stuned
            "Sasha stares at me in amazement."
            show sasha surprised
            sasha.say "Really?"
            sasha.say "Are you serious?"
            show sasha normal
            "I nod and Sasha doesn't hesitate for a moment."
            show sasha happy
            sasha.say "I choose the black one."
            sasha.say "It looks healthy and friendly too!"
            $ sasha.love += 2
    show sasha happy with fade
    "After that, all that's left to do is sign the last of the paperwork."
    show cat at left
    "And then the shelter staff bundles the cat into a cardboard carrier."
    "Sasha picks it up, and I can hear the faint sound of it mewing inside."
    "As we walk back to the car, I can't help noticing the similarity between the two."
    "Sasha's sleek, graceful and black-haired too."
    "And right now she's almost purring like the cat is too!"
    $ game.flags.petdelay = TemporaryFlag(True, 3)
    return

label name_cat:
    scene bg livingroom
    show cat zorder 3 at center, zoomAt(0.8, (640, 720))
    with fade
    "It's been a couple of days since Sasha and I went to the shelter to pick up the cat."
    "And the little guy's already settling in, strutting around the house like he owns the place!"
    "But I guess that's just cats for you - they're seldom lacking in self-confidence."
    "We're all adjusting to having him around too, enjoying the chance to spoil him rotten."
    "Even [bree.name], who actually wanted a dog, seems to be slowly warming to him too."
    "Sure, I've almost tripped over him a couple of times."
    "And dealing with his litter tray is literally the shits!"
    "But he's working out well and becoming a welcome addition to the house."
    "That's why it's such a shock when Sasha comes running up to me."
    sasha.say "[hero.name]!"
    show sasha shocked zorder 1 at left with easeinleft
    sasha.say "We're terrible kitty parents!"
    sasha.say "The worst pet-owners ever!"
    show sasha sad
    mike.say "Huh?"
    mike.say "What's wrong, Sasha?"
    mike.say "The cat seemed fine the last time I saw him."
    show sasha whining
    sasha.say "That's just it, [hero.name]!"
    sasha.say "'The cat'!"
    sasha.say "We didn't even remember to give him a name!"
    show sasha annoyed
    show bree stuned zorder 2 at right with easeinright
    "The sound of Sasha's voice soon brings [bree.name] into the room."
    "And she looks just as puzzled as I am."
    show bree surprised
    bree.say "What's going on in here?"
    bree.say "Did somebody die or something?"
    show bree stuned
    mike.say "No, [bree.name]."
    mike.say "Sasha was just telling me that we forgot to name the cat!"
    "I do the best I can to sound serious as I answer the question."
    "But [bree.name] still rolls her eyes and shakes her head."
    show bree talkative
    bree.say "Oh, that!"
    bree.say "I was thinking..."
    show bree smile
    bree.say "Wouldn't 'Nicky' be a great name for him?"
    show bree happy
    bree.say "He looks like a Nicky to me!"
    show bree normal
    "Sasha seems to recover her senses at the suggestion."
    "And now she's the one shaking her head."
    show sasha wtf
    sasha.say "No way, [bree.name]!"
    sasha.say "I already decided we should call him 'Lennie'!"
    show sasha shout
    sasha.say "After the frontman from Metallikea!"
    show sasha normal
    "Almost instantly the pair of them realise the other's not going to budge."
    "And so they resort to the next trick in their arsenal."
    show bree smile
    bree.say "[hero.name]..."
    bree.say "You like my name, right?"
    show bree normal
    show sasha shout
    show fx exclamation at right
    sasha.say "No he doesn't, [bree.name]!"
    sasha.say "You like my choice!"
    show fx question at left
    sasha.say "Right, [hero.name]?"
    show sasha normal
    menu:
        "Nicky suits it":
            mike.say "Hmm..."
            mike.say "I dunno, Sasha..."
            mike.say "He kinda looks like a 'Nicky' to me!"
            show bree happy
            "[bree.name] looks triumphant at this."
            show sasha stuned
            "But Sasha scowls at me."
            show sasha shocked with vpunch
            sasha.say "WHAT?!?"
            show sasha vangry
            sasha.say "You traitor!"
            show sasha angry
            mike.say "And you did get to choose the kind of pet we got, Sasha."
            mike.say "So maybe letting [bree.name] choose his name will balance things out?"
            show bree happy
            bree.say "Yay!"
            show sasha annoyed
            bree.say "Congratulations, Nicky - you've got a name!"
            show bree normal
            "[bree.name] and I celebrate by stroking Nicky, who purrs happily."
            "But Sasha just stands there, glowering at us the whole time."
            $ bree.love += 1
            $ game.flags.pet_name = "Nicky"
        "Hum... Lennie, I like it":
            mike.say "Hmm..."
            mike.say "I agree, Sasha..."
            mike.say "He sure looks like a 'Lennie' to me!"
            show sasha happy
            "Sasha looks triumphant at this."
            show bree stuned
            "But [bree.name] scowls at me."
            show bree vangry
            bree.say "Hey, no fair!"
            bree.say "Sasha got to choose a cat over a dog."
            bree.say "But I don't even get a say in naming him?!?"
            show bree annoyed
            mike.say "I'm sorry, [bree.name]."
            mike.say "Sasha's choice just suits him better!"
            show sasha happy
            sasha.say "Yay!"
            sasha.say "Congratulations, Lennie - you've got a name!"
            show sasha normal
            "[bree.name] and I celebrate by stroking Lennie, who purrs happily."
            "But [bree.name] just stands there, glowering at us the whole time."
            $ bree.love -= 1
            $ sasha.love += 2
            $ game.flags.pet_name = "Lennie"
        "Let me think":
            mike.say "Hmm..."
            mike.say "I think you're both wrong..."
            mike.say "He doesn't look like a 'Nicky' or a 'Lennie' to me!"
            show bree surprised
            show sasha surprised
            "[bree.name] and Sasha stand there with their mouths hanging open."
            "Both of them were expecting me to agree with them."
            "But I've evidently thrown them a curve-ball!"
            bree.say "What?"
            show bree stuned
            sasha.say "You don't like either name?"
            show sasha stuned
            mike.say "No, I think he's more of a 'Joey'."
            mike.say "And seeing as you two can't agree, we'll go with that."
            show sasha whining
            sasha.say "But...but I chose him at the shelter!"
            show sasha sad
            show bree sad
            bree.say "And I wanted a doggy, not a cat!"
            show bree gloomy
            mike.say "Congratulations, Joey - you've got a name!"
            "I celebrate by stroking Joey, who purrs happily."
            show bree normal
            show sasha normal
            "And eventually [bree.name] and Sasha seem to relent."
            "They join me in fussing the cat too."
            "And the issue seems to be settled."
            $ bree.love += 1
            $ sasha.love += 1
            $ game.flags.pet_name = "Joey"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
