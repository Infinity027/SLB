init python:
    Event(**{
    "name": "audrey_help_at_work",
    "label": "audrey_help_at_work",
    "conditions": [
        HeroTarget(IsActivity("work", "workhard", "work_personal", "workhard_personal")),
        PersonTarget(audrey,
            Not(IsHidden()),
            IsRoom("office")
            ),
        ],
    "chances": 10,
    "music": "music/roa_music/esperanza.ogg",
    "do_once": False,
    "once_week": True,
    })

    InteractEvent(**{
    "name": "audrey_talk_breakup",
    "max_girls": 1,
    "label": "audrey_talk_breakup",
    "do_once": True,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasRoomTag("work")),
        PersonTarget(audrey,
            IsActive(),
            MinStat("love", 20),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "chances": (audrey, "love", 20),
    })

    Event(**{
    "name": "audrey_gay_mistake",
    "label": "audrey_gay_mistake",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            MinStat("charm", 20),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            IsRoom("office")
            ),
        'audrey.love.max == 30',
        ],
    "chances": 10,
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_event_01",
    "label": "audrey_event_01",
    "conditions": [
        Not(IsDone("audrey_event_01b")),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),
            MinStat("fitness", 20),
            MinStat("charm", 20),
            IsFlag("dannydead", False),
            ),
        PersonTarget(audrey,
            IsPresent(),
            HasRoomTag("pub"),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "priority": 500,
    "do_once": True,
    })

    Event(**{
    "name": "audrey_event_01b",
    "label": "audrey_event_01b",
    "conditions": [
        Not(IsDone("audrey_event_01")),
        Or(
            IsDone("samantha_event_A02"),
            PersonTarget(samantha,
                IsFlag("divorced")
                )
            ),
        HeroTarget(
            Not(IsFlag("ryandead")),
            IsGender("male"),
            HasRoomTag("pub"),
            MinStat("fitness", 20),
            MinStat("charm", 20),
            IsFlag("dannydead", True),
            ),
        PersonTarget(audrey,
            IsPresent(),
            HasRoomTag("pub"),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "priority": 500,
    "do_once": True,
    })

    Event(**{
    "name": "audrey_event_02",
    "label": "audrey_event_02",
    "duration": 1,
    "conditions": [
        Or(
            IsDone("audrey_event_01"),
            IsDone("audrey_event_01b")
            ),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("work")),
        PersonTarget(audrey,
            Not(IsHidden()),
            HasRoomTag("work"),
            MinStat("love", 40),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "priority": 500,
    "do_once": True,
    })

    Event(**{
    "name": "audrey_event_03",
    "label": "audrey_event_03",
    "duration": 1,
    "conditions": [
        IsDone("audrey_event_02"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("gym")),
        PersonTarget(audrey,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 60),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "priority": 500,
    "do_once": True,
    })

    Event(**{
    "name": "audrey_event_04",
    "label": "audrey_event_04",
    "duration": 1,
    "conditions": [
        IsDone("audrey_event_03"),
        Not(IsDone("audrey_event_04b")),
        IsSeason(0, 1),
        IsDayOfWeek(6, 7),
        IsHour(12, 16),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(HasRoomTag("waterpark"))),
        PersonTarget(audrey,
            MinStat("love", 80)
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "priority": 500,
    "clothes": "swimsuit",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_event_04b",
    "label": "audrey_event_04b",
    "duration": 1,
    "conditions": [
        IsDone("audrey_event_03"),
        Not(IsDone("audrey_event_04")),
        IsSeason(2, 3),
        IsDayOfWeek(6, 7),
        IsHour(12, 16),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(HasRoomTag("park"))),
        PersonTarget(audrey,
            MinStat("love", 80)
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "priority": 500,
    "do_once": True,
    })

    Event(**{
    "name": "audrey_event_05",
    "label": "audrey_event_05",
    "conditions": [
        Or(
            IsDone("audrey_event_04"),
            IsDone("audrey_event_04b")
           ),
        IsHour(19),
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(audrey,
            MinStat("love", 100),
            Not(IsFlag("delay"))
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "priority": 500,
    "clothes": "date",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_event_06",
    "label": "audrey_event_06",
    "conditions": [
        IsDone("audrey_event_05"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            MinStat("charm", 50),
            ),
        PersonTarget(audrey,
            HasRoomTag("work"),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_event_07",
    "label": "audrey_event_07",
    "conditions": [
        IsDone("audrey_event_06"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal"),
            MinStat("charm", 60),
            ),
        PersonTarget(audrey,
            HasRoomTag("work"),
            MinStat("love", 120),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_event_08",
    "label": "audrey_event_08",
    "conditions": [
        IsDone("audrey_event_07"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal")),
        PersonTarget(audrey,
            HasRoomTag("work"),
            MinStat("love", 140),
            ),
        ],
    "duration": 1,
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_event_09",
    "label": "audrey_event_09",
    "conditions": [
        IsDone("audrey_event_09_intro"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("mcoffice"),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            HasRoomTag("mcoffice"),
            MinStat("love", 160),
            ),
        ],
    "duration": 1,
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_event_10",
    "label": "audrey_event_10",
    "conditions": [
        IsDone("audrey_event_09"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("work")),
        PersonTarget(audrey,
            HasRoomTag("work"),
            IsFlag("scaredloved", False)
            ),
        ],
    "duration": 1,
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    AfterDateEvent(**{
    "name": "audrey_sub_event_01",
    "label": "audrey_sub_event_01",
    "priority": 500,
    "conditions": [
        IsTimeOfDay("evening", "night"),
        HeroTarget(IsGender("male")),
        MinDateScore(90),
        PersonTarget(audrey,
            OnDate(),
            MinStat("sub", 15),
            MinStat("sexperience", 1),
            ),
        ],
    "duration": 1,
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_sub_event_02",
    "label": "audrey_sub_event_02",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("date_cinemaroom")
            ),
        PersonTarget(audrey,
            Not(IsFlag("subevent")),
            OnDate(),
            MinStat("sub", 25),
            MinStat("sexperience", 2),
            ),
        ],
    "duration": 1,
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_sub_event_03",
    "label": "audrey_sub_event_03",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("workhard", "workhard_personal"),
            HasRoomTag("mcoffice"),
            ),
        PersonTarget(audrey,
            Not(IsFlag("subevent")),
            MinStat("sub", 75),
            MinStat("sexperience", 5),
            ),
        ],
    "duration": 1,
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_spanking_start",
    "label": "audrey_spanking_start",
    "priority": 200,
    "conditions": [
        IsDone("shiori_scold_3"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal")),
        PersonTarget(audrey,
            HasRoomTag("work"),
            MinStat("love", 90),
            MinStat("sub", 25),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_spanking_1",
    "label": "audrey_spanking_1",
    "priority": 200,
    "conditions": [
        IsDone("audrey_spanking_start"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal")),
        PersonTarget(audrey,
            HasRoomTag("work"),
            IsFlag("spankingdelay", False),
            MinStat("love", 110),
            MinStat("sub", 50),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_spanking_2",
    "label": "audrey_spanking_2",
    "priority": 200,
    "conditions": [
        IsDone("audrey_spanking_1"),
        HeroTarget(
            IsGender("male"),
            IsActivity("work", "workhard", "work_personal", "workhard_personal")),
        PersonTarget(audrey,
            HasRoomTag("work"),
            IsFlag("spankingdelay", False),
            MinStat("love", 130),
            MinStat("sub", 75),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_kiss_me",
    "label": "audrey_kiss_me",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(audrey,
            IsPresent(),
            Not(IsHidden()),
            MinFlag("kiss", 1),
            MinStat("love", 150),
            ),
        ],
    "chances": 20,
    "once_day": True,
    "do_once": False,
    "music": "music/roa_music/esperanza.ogg",
    "quit": False,
    })

    Event(**{
    "name": "audrey_preg_talk",
    "label": "audrey_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(audrey,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    })

    Event(**{
    "name": "audrey_investigation_callback",
    "label": "audrey_investigation_callback",
    "conditions": [
        IsNotDone("cassidy_investigation_complete"),
        IsHour(12, 18),
        PersonTarget(audrey,
            Not(IsPresent()),
            Not(IsHidden()),
            MinCounter("investigationcallback", 2),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "audrey_go_to_the_gym",
    "label": "audrey_go_to_the_gym",
    "conditions": [
        HeroTarget(IsGender("male")),
        Not(InInventory("sport_clothes")),
        PersonTarget(audrey,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "audrey_date_at_home",
    "label": "audrey_date_at_home",
    "conditions": [
        IsTimeOfDay("evening", "night"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_livingroom"),
            HasStamina()
            ),
        PersonTarget(audrey,
            OnDate(),
            MinStat("sexperience", 5),
            MinStat("love", 140),
            MinStat("sub", 40),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "audrey_give_address",
    "label": "audrey_give_address",
    "priority": 1000,
    "conditions": [
        PersonTarget(audrey,
            IsActive(),
            MinStat("love", 110),
            MinStat("sexperience", 1),
            ),
        ],
    "music": "music/roa_music/sleepless_nights.ogg",
    "chances": 25,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "audrey_apartment_first_visit",
    "label": "audrey_apartment_first_visit",
    "conditions": [
        IsTimeOfDay("evening"),
        HeroTarget(
            IsGender("male"),
            IsRoom("audreylivingroom"),
            ),
        PersonTarget(audrey,
            Not(IsActivity("sleep")),
            HasRoomTag("audreyhome"),
            IsFlag("addressknown", True),
            ),
        ],
    "music": "music/roa_music/esperanza.ogg",
    "do_once": True,
    })


label audrey_go_to_the_gym:
    "You know that feeling that you get, the one where you keep looking up and catching someone stealing a glance?"
    "It's like they've got something on their mind that they really want to say, but can't pluck up the courage to do it."
    "So they keep on casting their eyes your way in the hope that you'll catch on and ask then what the hell's the matter."
    "You know it has to be something bad too, because they'd rather annoy you until you broach the subject than say it of their own volition."
    "Well all of that's happening to me right now, and it's getting to the point where I simply can't stand it any more."
    show audrey
    if audrey.flags.nickname == "toy":
        mike.say "Little toy, for god's sake."
    else:
        mike.say "Audrey, for god's sake."
    mike.say "What's bugging you?"
    show audrey frown
    "Audrey suddenly prickles, no doubt aware that I'm onto her."
    audrey.say "What...what do you mean?"
    if audrey.flags.nickname == "toy":
        mike.say "Don't play the innocent with me, my little Toy."
    else:
        mike.say "Don't play the innocent with me, Audrey."
    mike.say "If you've got something to say, then just come out and say it!"
    show audrey mock
    "In typical Audrey fashion, she shakes her head and curls her lip in an exasperated manner, as if I'm the one being unreasonable here."
    audrey.say "Okay, whatever - if it'll make you get off of my back!"
    "I brace myself for what's coming next, trying to remember just how aggravating Audrey's capable of being with little to no effort."
    audrey.say "It's nothing really."
    audrey.say "Just that I was looking at the size of your arms..."
    audrey.say "And your chest..."
    audrey.say "And your gut..."
    "Nodding with each new part of my anatomy that she mentions, I'm already thinking that this can't be good."
    show audrey joke
    audrey.say "I mean - do you even know what the inside of a gym looks like?"
    mike.say "So what - you're telling me that I'm fat?!?"
    show audrey normal
    "Audrey shakes her head and lets out a resigned sigh, as though she were expecting me to react in just this manner."
    audrey.say "No, I never used that word, [hero.name]."
    audrey.say "I just think that you could use a bit of...tightening up in some departments, that's all."
    mike.say "Tightening up?!?"
    audrey.say "Hey, I wasn't the one that said you were fat!"
    audrey.say "That's what was kicking around inside of your own head, not mine."
    "And of course, that makes what Audrey's said perfectly fine, I guess!"
    "But then I find myself looking down at my own belly for a moment, pressing an experimental finger into it."
    "Much to my surprise, it sinks in far more than I would have expected it to."
    "Maybe Audrey does have a point after all?"
    "But still, there was no need to be so blunt about it!"
    mike.say "Hmm...I do feel a little more doughy around the middle."
    mike.say "I guess it couldn't hurt to renew my gym membership..."
    show audrey mock
    audrey.say "Don't forget to buy something new to work out in, [hero.name]."
    "I look at her in askance, amazed that she's tagging on another criticism in addition to the first."
    mike.say "Hey, I have stuff that I can work out in!"
    audrey.say "Oh please - I've seen your casual wardrobe."
    audrey.say "Those faded T-shirts and saggy sweatpants make you look like white trash!"
    mike.say "Well...maybe I could buy something a bit more fitted and flattering?"
    show audrey happy
    "Audrey smiles at this, most likely sensing that she's talking me round and winning the argument."
    audrey.say "That's just what I was thinking."
    audrey.say "What's the point of owning a work of art and putting it in a trashy old frame?"
    show audrey normal
    "I nod at this, but at the same time find myself wondering if I've just been given good advice."
    "Or else been skilfully manipulated into doing exactly what Audrey wants."
    show screen message(title="Go to the gym!",what="Audrey told you to go to the gym but you will need {b}Sports clothes{/b} to be able to go there.")
    pause
    hide screen message
    hide audrey
    return

label audrey_date_at_home:
    show audrey
    "I think that Audrey was expecting me to suggest that we go out somewhere for our date."
    "But I'm way too knackered from work to be able to go out and be around a bunch of people."
    "That's why I insisted that she just come over here and chill with me on the couch."
    "[bree.name]'s doing something in her room that's going to keep her out of my hair all night."
    "And Sasha's one hundred percent focused on a gig that her band have in the next few weeks."
    "So she's out at the practice room rehearsing until her fingers bleed!"
    "That means Audrey and I have the living room to ourselves."
    "And she's agreed to just spend the evening with me watching whatever on the TV."
    "Yet there's still that hint of attitude about her."
    "Like she's doing what I asked her, but she's not happy about it."
    "She's sitting next to me on the couch, keeping pretty quiet."
    "But I decide to risk a sideways glance at her."
    show fx question
    audrey.say "What are you looking at, [hero.name]?"
    "Ah, shit - caught in the act!"
    mike.say "Erm..."
    mike.say "Nothing, Audrey!"
    mike.say "Just checking you're okay, that's all."
    mike.say "Ah...are you?"
    mike.say "Okay, that is - are you okay?"
    "Audrey shakes her head as I begin to babble at her."
    show audrey joke
    audrey.say "Geez, [hero.name]!"
    audrey.say "I'm okay - okay?"
    mike.say "Okay, okay..."
    show audrey normal
    "I take the time to think about what I say next."
    "Even if it's just to avoid saying okay one more time."
    mike.say "I just wanted to say thanks for being so understanding, Audrey."
    mike.say "I don't think I could have faced being around a crowds tonight."
    mike.say "And I know this is pretty quiet..."
    mike.say "But we can still have fun, right?"
    show audrey flirt
    "Audrey gives me a smile as she raises one eyebrow."
    audrey.say "Who said we have to be quiet, huh?"
    audrey.say "And we can do SO much fun stuff here."
    audrey.say "Stuff we can't get away with in public!"
    "I find myself blinking in surprise."
    mike.say "Oh yeah, Audrey..."
    mike.say "I guess you're right!"
    "I feel Audrey taking hold of my hand."
    "Actually, she's squeezing it pretty hard!"
    "I can't help gazing down, so I'm no longer looking her in the eye."
    "That's the only excuse that Audrey needs to pounce."
    "And I really do mean pounce!"
    "One moment she's sitting beside me on the couch."
    show audrey close with vpunch
    "The next she's straddling me, pinning me down."
    mike.say "Wha..."
    mike.say "What the..."
    audrey.say "Shut the fuck up, [hero.name]!"
    audrey.say "Shut up and kiss me!"
    hide audrey
    show audrey kiss
    with fade
    $ audrey.flags.kiss += 1
    "In don't have time to protest."
    "But it's not like I want to get away!"
    "That's why I busy myself doing as Audrey demands."
    "At the same time she starts pulling at her own clothes."
    "Even with Audrey's tongue shoved down my throat, I can see what she's doing."
    show audrey kiss underwear with dissolve
    $ audrey.flags.kiss += 1
    "And I know that she's not trying to strip herself naked right now."
    "All she's trying to do is tear off enough of her clothes."
    "Enough for us to take things to the next level."
    "My suspicions are confirmed when I feel Audrey fumbling with my flies."
    "She unzips my pants and shoves her hand inside, not asking for permission."
    "Then she drags my cock out, squeezing it as she does so."
    hide audrey
    show audrey close with fade
    "Audrey breaks off the kiss at almost the same moment."
    "Which means that I can't keep from expressing how it feels!"
    mike.say "Oh shit!"
    mike.say "Audrey, be careful with that!"
    audrey.say "Don't shit yourself, [hero.name]!"
    audrey.say "I won't be gentle."
    audrey.say "But I promise I won't break anything!"
    "Audrey passes my cock from one hand to another as she moves."
    show audrey reverse cowgirl livingroom naked with fade
    "And she doesn't stop until she has her back to me."
    "I think the position she's in is called reverse cowgirl, or something like that."
    "But I'm not about to stop her and ask about it!"
    audrey.say "Come on, [hero.name]!"
    audrey.say "What are you waiting for?"
    audrey.say "A written invitation to fuck me?"
    "I guess we're doing this thing!"
    "Part of me is worried about [bree.name] or Sasha walking in on us."
    "But that's not the part of me that seems to be calling the shots."
    "Because I find myself taking a firm hold of Audrey."
    "Then I pull her roughly down and onto me."
    audrey.say "Oh yeah..."
    audrey.say "That's what I'm talking about!"
    menu:
        "Fuck her pussy":
            "Audrey has a firm hold on my cock, and she's aiming it in one direction."
            "Which just happens to be squarely between her legs and at her pussy."
            "And I can't see anything wrong with going right along with that too."
            "So as I pull Audrey down, I thrust myself forwards as well."
            "This means that the head of my cock makes contact with the lips of her pussy."
            "I can instantly feel that she's both hot and wet down there."
            "But all the same, Audrey's pussy doesn't let me straight in."
            "Instead the head of my cock slides upwards and along her lips."
            "The pressure that we're both exerting can be felt every second it's happening."
            "And I'm sure that it'll just slide straight off any moment."
            show audrey reverse cowgirl vaginal audreyahegao
            "But then the resistance vanishes, and I can feel myself sinking into her."
            "All that pressure is still there, and now it's pushing me deeper and harder."
            audrey.say "Oh..."
            show audrey reverse cowgirl audreypleasure
            audrey.say "Oh fuck!"
            "At first Audrey seems to be urging me on the same way she was before I got inside of her."
            "But with each thrust I make into her pussy, the tone of her voice changes a little more."
            "Pretty soon she's beginning to sound like the sensations are overwhelming her."
            "The change might be subtle to anybody else's ears."
            "But to me it's proof positive that the dynamic between us is changing."
            "Before, Audrey was the one taking the lead, making me follow her."
            "Now she's the one that's in my hands."
            "She's the one with my cock deep inside of her."
            "And I can see, hear and feel just how much she's loving it."
            mike.say "You like that, huh?"
            audrey.say "Y...yeah!"
            mike.say "You want more?"
            audrey.say "P...please..."
            "I can't help smiling to myself as Audrey begs for more."
            "It's not like I'm one of those guys that gets off on dominating women."
            "But being able to turn the tables on a manipulative girl like Audrey..."
            "Well, that's something entirely different."
            "I guess I'm technically still giving her exactly what she wants."
            "But it's the fact she's so desperate for it that's turning me on."
            "That's why I practically launch myself into it."
            show audrey reverse cowgirl mikepleasure
            "Keeping a firm hold on Audrey, I start to pound her harder than ever."
            "And the effect is pretty much instant."
            "She moans and gasps, writhing around in my lap."
            "I feel like Audrey's trying to work herself up and down on my cock."
            "But at the same time the sensations she's feeling are just too much for her."
            "If I loosened my grip on her, I'm pretty sure she'd fall off and end up in a heap on the floor!"
            "All the time I'm going as fast and as hard as I can."
            "I'm loving every second of it, but I'm sweating and starting to pant."
            "And Audrey seems to be showing no signs of slowing down anytime soon!"
            "How much more of this is she going to demand from me before she cums?"
            "Is she going to ride me into the ground?"
            "Am I going to pass out from sheer exhaustion?"
            "But a moment later, I realise none of that is going to happen."
            "And that's because I'm about to lose it myself."
            "Right now Audrey seems to out of it to care what happens."
            "So I guess all of that is in my hands!"
            menu:
                "Cum inside":
                    "I strengthen my hold on Audrey just in time."
                    show audrey reverse cowgirl audreyahegao creampie with vpunch
                    "Because a moment later I let go, shooting my load."
                    with vpunch
                    "I'm as deep inside of Audrey as I can get."
                    with vpunch
                    "Which means that she takes everything I have to give."
                    "Audrey cries out as I fill her pussy."
                    "But there's nowhere for her to go."
                    "Instead she has to endure, riding it out until the end."
                "Pull out":
                    show sexinserts belly audrey zorder 2 at center, zoomAt(1, (740, 970))
                    "Taking a stronger hold of Audrey, I make my move."
                    "All it takes is a firm pull down for me and a push up for her."
                    show audrey reverse cowgirl out
                    "The result is that my cock pops out of her just at the right moment."
                    "As Audrey yelps at the sensation, I feel myself lose it."
                    show sexinserts belly audrey zorder 2 at center, zoomAt(1, (740, 970))
                    show audrey reverse cowgirl cumshot
                    with vpunch
                    pause 0.2
                    with vpunch
                    "I cum while holding nothing back, shooting my load over her."
                    with vpunch
                    "It spatters onto Audrey's belly, running down the curve of her hips."
                    hide sexinserts
        "Fuck her ass":
            "Audrey has a firm hold on my cock, and she's aiming it in one direction."
            "Which just happens to be squarely between her legs and at her pussy."
            "But I think that it's about time I started to assert myself."
            "So as I pull Audrey down, I pull back as well."
            "This means that the head of my cock is wedged firmly between the cheeks of her ass."
            "I can instantly feel her tense and begin to squirm as I do so."
            "But all the same, I keep a firm hold on Audrey and push onwards."
            "Now I can feel the head of my cock pressing to enter her ass."
            "The pressure that we're both exerting can be felt every second it's happening."
            "And I'm sure that it'll just slide straight off any moment."
            show audrey reverse cowgirl anal audreyahegao
            "Audrey seems to be doing all that she can to resist."
            "But still she's sinking down onto me more with each second that passes."
            audrey.say "Oh..."
            audrey.say "Oh fuck!"
            show audrey reverse cowgirl audreypleasure
            audrey.say "What the hell..."
            "At first Audrey seems to be doing all that she can to keep it from happening."
            show audrey reverse cowgirl audreyahegao
            "But with each fraction of an inch I make it inside, the tone of her voice changes a little more."
            "Pretty soon she's beginning to sound like the sensations are overwhelming her."
            "The change might be subtle to anybody else's ears."
            "But to me it's proof positive that the dynamic between us is changing."
            "Before, Audrey was the one taking the lead, making me follow her."
            "Now she's the one that's in my hands."
            "She's the one with my cock deep inside of her."
            "And I can see, hear and feel just how much she's loving it."
            mike.say "You like that, huh?"
            mike.say "You like the feel of it in your ass?"
            show audrey reverse cowgirl audreypleasure
            audrey.say "Y...yeah!"
            mike.say "You want more?"
            audrey.say "P...please..."
            "I can't help smiling to myself as Audrey begs for more."
            "It's not like I'm one of those guys that gets off on dominating women."
            "But being able to turn the tables on a manipulative girl like Audrey..."
            "Well, that's something entirely different."
            "I guess I'm technically still giving her exactly what she wants."
            "But it's the fact she's so desperate for it that's turning me on."
            "That's why I practically launch myself into it."
            show audrey reverse cowgirl mikepleasure
            "Keeping a firm hold on Audrey, I start to pound her harder than ever."
            "And the effect is pretty much instant."
            "She moans and gasps, writhing around in my lap."
            "I feel like Audrey's trying to work herself up and down on my cock."
            "But at the same time the sensations she's feeling are just too much for her."
            "If I loosened my grip on her, I'm pretty sure she'd fall off and end up in a heap on the floor!"
            "All the time I'm going as fast and as hard as I can."
            "I'm loving every second of it, but I'm sweating and starting to pant."
            "And Audrey seems to be showing no signs of slowing down anytime soon!"
            "How much more of this is she going to demand from me before she cums?"
            "Is she going to ride me into the ground?"
            "Am I going to pass out from sheer exhaustion?"
            "But a moment later, I realise none of that is going to happen."
            "And that's because I'm about to lose it myself."
            "Right now Audrey seems to out of it to care what happens."
            "So I guess all of that is in my hands!"
            menu:
                "Cum inside":
                    "I strengthen my hold on Audrey just in time."
                    show audrey reverse cowgirl creampie audreyahegao with vpunch
                    "Because a moment later I let go, shooting my load."
                    with vpunch
                    "I'm as deep inside of Audrey as I can get."
                    with vpunch
                    "Which means that she takes everything I have to give."
                    "Audrey cries out as I fill her ass."
                    "But there's nowhere for her to go."
                    "Instead she has to endure, riding it out until the end."
                "Pull out":
                    show sexinserts belly audrey zorder 2 at center, zoomAt(1, (740, 970))
                    "Taking a stronger hold of Audrey, I make my move."
                    "All it takes is a firm pull down for me and a push up for her."
                    show audrey reverse cowgirl out
                    "The result is that my cock pops out of her just at the right moment."
                    "As Audrey yelps at the sensation, I feel myself lose it."
                    show sexinserts belly audrey zorder 2 at center, zoomAt(1, (740, 970))
                    show audrey reverse cowgirl cumshot with vpunch
                    pause 0.2
                    with vpunch
                    "I cum while holding nothing back, shooting my load over her."
                    with vpunch
                    "It spatters onto Audrey's belly, running down the curve of her hips."
                    hide sexinserts
            $ audrey.flags.anal += 1
    hide audrey with fade
    "As soon as I loosen my grip on her, Audrey slides off me."
    "She collapses onto the couch like a ragdoll, not moving once she's there."
    "I know that I should tell her to put her clothes on, in case someone walks in."
    "But right now all I can do is sit there, panting and trying to recover myself."
    "And to think, this was supposed to be nothing more than a quiet night in front of the TV!"
    $ game.active_date.score += 75
    $ game.pass_time(2)
    $ audrey.sexperience += 1
    return

label audrey_spanking_2:
    $ audrey.flags.spankingdelay = TemporaryFlag(True, 3)
    "I don't really have a dedicated secretary working under me at my current pay grade, and I'm in the habit of writing letters, emails and memos myself whenever I need them."
    "But I do on occasion find myself inundated to the point where I have to ask one of the people that I'm responsible for in the office to take dictation and write up my words for me."
    "Normally I'd ask Shiori to handle it, as she's insanely eager to please and terrified of screwing up even the smallest, most insignificant of tasks."
    "But on one particular occasion she was nowhere to be seen and I was forced to resort to the desperate measure of having Audrey do it instead."
    "Everything seemed to go off without a hitch, until I look back over the file the next day and just so happen to glance at the copy of the letter inside of it."
    if audrey.flags.nickname == "toy":
        mike.say "TOY - get in my office...NOW!"
    else:
        mike.say "AUDREY - get in my office...NOW!"
    show audrey with moveinleft
    "Despite the fact that I'm yelling at the top of my voice and visibly annoyed, Audrey takes her own sweet time sauntering into my office."
    "She has a look of sublime innocence on her face that only serves to make me become instantly more irate with her."
    "There's no way that she can pretend to be ignorant of what's making me angry, or of what she's gone and done."
    audrey.say "Yes, [hero.name] - what can I do for you?"
    "I hold up the copy of the offending letter, doing so with a finger and thumb, as though it were smeared in something unmentionable."
    if audrey.flags.nickname == "toy":
        mike.say "Toy, please tell me that you didn't let this go out."
    else:
        mike.say "Audrey, please tell me that you didn't let this go out."
    "She cocks her head on one side and leans in a little closer to see just what I'm referring to, still playing the innocent party."
    show audrey frown
    audrey.say "Isn't that the letter you had me type up yesterday?"
    audrey.say "I was sure to see that it went out in last night's mail, just like you asked me to."
    "Seeing that she intends to keep on playing this game until someone blinks, I shake my head in frustration."
    if audrey.flags.nickname == "toy":
        mike.say "You do understand, don't you, Toy, how dictating a letter works?"
    else:
        mike.say "You do understand, don't you, Audrey, how dictating a letter works?"
    mike.say "You're not a court reporter, taking it all down word for word!"
    mike.say "For example, I don't think the client will be too impressed with this part here."
    "I point to a particularly offensive passage somewhere in the middle of the letter."
    mike.say "Specifically this one where you chose to quote me as saying - 'whatever, give the sleazy old creep some bullshit excuse'!"
    "Audrey cocks her head, doing her best approximation of a puzzled expression."
    show audrey annoyed
    audrey.say "Oops...I guess I must have been daydreaming when they went through that one back in clerical slave school!"
    "At that, I have to bite my tongue to keep from saying something that I might later regret."
    "Not only has she deliberately put me in a compromising position, she's now throwing it in my face for asking her to take down the letter in the first place!"
    "I find that all I can do is close my eyes and force myself to count slowly to ten."
    "But when I open my eyes, Audrey is still standing there, that same look of mock-innocence barely concealing the smugness."
    "So I bite my lip and close my eyes again, counting to twenty this time."
    "When I open my eyes for the second time, my efforts to control myself have clearly done nothing but amuse Audrey."
    show audrey mock
    "She's smiling openly now, even beginning to get the giggles at how mad she's managed to make me in so short a space of time."
    "I should be able to rise above all of this petty shit, just give her a bollocking and then report the matter to HR."
    "The worst part of it is that I know why she's doing this to me, what she wants to happen next."
    "And I also know that I'm getting ever closer to giving in and letting her have it too."
    "Audrey, of course, knows all about the dilemma that I'm currently wrestling with, can read it in my expression."
    "She keeps the smile on her face as she walks slowly around the side of my desk, holding my eye the whole time."
    "As she gets closer, I instinctively push my chair back in order to keep some distance between us."
    "But that only means that I collide with the back wall of my office as she keeps coming on."
    "Seeing that I'm out from under the desk, Audrey leans in closer and actually lowers herself until she's over my lap."
    hide audrey
    show spank audrey
    "And then she lays herself across my thighs, looking back over her shoulder with that same feigned innocence as she does so."
    audrey.say "Well, it sounds like I've been a very bad girl."
    audrey.say "So you're going to have to punish me...aren't you?"
    "I take a deep breath, already unable to concentrate on anything other than the weight of her across my lap."
    "If I'd been able to, then I should have told her to stay on her own side of the desk or else get he hell of my lap well before now."
    "Resigned to the fact that there's no way out of this, I begin to raise my hand to strike the first blow..."
    show spank audrey up
    "But then I pause, considering the fact that I've already spanked Audrey in the past."
    "Surely if I'm going to mete out the same punishment again, I need to step things up a notch?"
    if not audrey.flags.sexywork:
        "Pulling down Audrey's skirt to reveal her buttocks, I quickly follow this action by grabbing the waistband of her panties and yanking them down as well."
    show spank audrey ready pulled
    "For the first time since she stepped into my office, I hear a squeal that tells me events have taken a turn which Audrey had not anticipated."
    "This only serves to make me all the more intent on following through with the notion, and I give her bare ass a swift slap for the sake of getting things started."
    show spank audrey up
    pause 0.3
    show spank audrey spank surprised
    play sound spank
    with hpunch
    "The first couple of slaps are relatively gentle, just a taster of what's to come."
    show spank audrey up normal
    pause 0.3
    show spank audrey spank marks
    play sound spank
    with hpunch
    "But all the same, the cheeks on Audrey's face are soon as red as those of her backside."
    show spank audrey up
    pause 0.3
    show spank audrey spank
    play sound spank
    with hpunch
    "As I step up the intensity of the blows, I hear her begin to yelp over the sound of my hand making contact with her buttocks."
    show spank audrey up
    pause 0.3
    show spank audrey spank pleasure
    play sound spank
    with hpunch
    "Audrey wriggles and squirms relentlessly as I continue to spank her, pushing herself against my groin."
    "The effect is enough to make me hope that I don't have to get up and leave the office in a hurry any time soon."
    "Because if that were the case, I'd be walking out bent double right now."
    "Soon we seem to be lost in a world of our own, each getting off on what we're doing or having done to us."
    "So much so that neither of us hears the door to my office being opened..."
    hide spank
    show shiori work
    shiori.say "Good morning [hero.name]!"
    shiori.say "I wondered if you wanted some...BUTTOCKS!"
    "I look up in horror to see Shiori standing in the doorway, face aghast at what she's just walked in on."
    mike.say "Shiori...it's...it's not what it looks like!"
    show shiori work blush
    "Who in the hell am I trying to kid?"
    "What else could this be, other than exactly what it looks like?"
    "Shiori stands rooted to the spot for what feels like forever, and then backs out of my office without saying another word."
    hide shiori
    "Both Audrey and I are perfectly still now that we've been left alone once more."
    "I begin to wonder if Shiori's barging in on us like that has ruined the moment, and whether I should just stop."
    "But my hand, which had come to rest on Audrey's backside, slightly between her buttocks, suddenly makes an intriguing discovery."
    show spank audrey marks spank pulled
    "Rather than being put off by what just happened, my fingertips can now feel just how slick and wet she's become as a result."
    "The dirty little bitch actually got turned on by us being caught in the act!"
    menu:
        "Finger her pussy":
            "Up until this moment, I've been totally focused on spanking Audrey's ass, to the point of ignoring everything else."
            "But now I find my finger unconsciously circling the edges of her pussy, feeling just how invitingly wet it's become."
            "Without saying a word or giving any other kind of warning, I begin to gently stroke the inner folds."
            show spank audrey fingerpussy surprised
            "Audrey responds to this unexpected turn of events by gasping and then proceeding to twitch and wriggle."
            "Having her doing so in my lap is quite something, and so I just can't help but push my finger slowly inside."
            show spank audrey fingerpussy normal
            "Audrey's moaning by now, a sound that's somewhere between arousal and humiliation."
            "As if the combination of being seen with her panties down and now being fingered roughly is just too much, she begins to buck in my lap."
            show spank audrey fingerpussy pleasure
            "When her climax finally comes over her, Audrey pants and cries with the spasms of her pussy, exposed and with nowhere to hide for the sake of her dignity."
        "Fingers her ass":
            "My guess is that Audrey's expecting me to either keep on spanking her buttocks or else take advantage of her exposed pussy."
            "But this is supposed to be a punishment, and so what would be the point in giving her what she wants?"
            show spank audrey fingerass surprised
            "Instead I part her buttocks and push a finger firmly into her anus, enjoying the way in which it twitches and tries to resist me."
            "Mirroring the reaction of her sphincter muscles, Audrey lets out a cry of alarm and struggles to see what I'm doing to her."
            "But she's in no position to put up any kind of resistance, and I easily hold her down while pushing the finger in still further."
            "Slowly, Audrey's yelps of pain turn into subdued moans of acceptance and submission, as she feels me press in as deep as I can go."
            "Intrigued to see how pliable her ass is, I push in another finger and then a third, each with the reception of a rise in her moans."
            show spank audrey fingerass normal
            "Soon I feel like I'm engaged in the act of slowly turning Audrey into some kind of perverted glove-puppet."
            "Then, before I can even think of putting another finger inside of her, she begins to twitch and jerk."
            show spank audrey fingerass pleasure
            "I don't know exactly what brings her off this time, but she cums with most of my fingers buried deep inside of her ass."
        "Continues spanking Audrey":
            "Perhaps she thinks that I've stopped because the feel of her wet pussy is enough to distract me from the task that I've already started."
            show spank audrey up
            pause 0.3
            show spank audrey spank
            play sound spank
            with hpunch
            "But one massive crack on her already red and ruddy buttocks from the flat of my hand is enough to dispel any such illusions."
            "If anything, Audrey resumes squealing and yelping even more loudly than before now that the spanking has begun anew."
            "In fact, she's becoming so loud by now that I'm starting to get seriously worried about someone hearing her and coming to investigate."
            "The only choice that I seem to have is between stopping entirely or pressing on with even more gusto."
            show spank audrey up
            pause 0.3
            show spank audrey spank
            play sound spank
            with hpunch
            "And so I choose the latter option, now whaling on Audrey's ass for all that I'm worth."
            "I swear that I can almost see the ripples that spread out from each impact of my palm in slow-motion."
            "The sight reminds me of those films run at ultra-slow speeds to capture the sight of droplets hitting water."
            "But it's the desperate gasping that Audrey's beginning to make that eventually pulls me back into the moment."
            show spank audrey up
            pause 0.3
            show spank audrey spank
            play sound spank
            with hpunch
            "Red-faced and panting almost desperately, I'm not sure that she can take much more of this."
            show spank audrey up
            pause 0.3
            show spank audrey spank
            play sound spank
            with hpunch
            "I give her one final slap of epic proportions, and then leave her, gasping and sweating across my lap."
    $ audrey.sub += 5
    hide spank
    $ hero.replace_activity()
    $ game.pass_time(1)
    return

label audrey_spanking_1:
    $ audrey.flags.spankingdelay = TemporaryFlag(True, 3)
    "My job's never been the easiest part of my daily life to manage, or the one that's given me the least amount of stress on a regular basis."
    "But at least it has the redeeming quality of paying me enough to put a roof over my head and fill the refrigerator."
    "It's just that recently things seem to have gotten a lot harder to handle in the office."
    "Almost as if something was actively working against me, making my daily grind that much harder to handle."
    show aletta
    "That's why I almost bite the head off of Aletta when she appears at my door."
    aletta.say "Oh, [hero.name] - do you have a moment?"
    mike.say "Aletta...what in the hell do you want?"
    "Aletta raises an eyebrow at the tone of my voice, luckily for me more in intrigue than offence."
    show aletta annoyed
    aletta.say "Well, it looks like someone hasn't had their required dosage of caffeine this morning!"
    mike.say "Sorry...sorry, Aletta."
    mike.say "I guess I'm just pretty strung out this morning, that's all."
    "Aletta gives me a cryptic smile and crosses her arms over her considerable chest."
    show aletta flirt
    aletta.say "Well, what if I were to say that I could help make things that little bit easier for you?"
    mike.say "I'd say please do!"
    "Aletta nods before continuing, clearly pleased to have me indulge her."
    aletta.say "You recall how you have that file where all of the mail keeps disappearing?"
    "I nod eagerly at the mention of the troublesome case she mentions, my interest piqued."
    mike.say "Of course I do - every letter the client claimed to have sent seemed to vanish into a black hole!"
    show aletta normal
    aletta.say "Oh, it wasn't anything so dramatic as that."
    aletta.say "More like disappearing into the shredder down in the mailroom!"
    mike.say "WHAT?!?"
    "I stand up and slam my hands down on the desk, more for the sake of making a noise than anything else."
    show aletta flirt
    "Aletta's grinning like a Cheshire Cat by now, simply loving the reaction that she's managed to get out of me."
    "If she could, I really think she'd be making a satisfied purring sound too."
    aletta.say "Let's just say that I happened to walk in on Audrey this morning."
    aletta.say "And that I caught her red-handed - shoving all of the correspondence for that file into the shredder."
    show aletta normal
    "Trying to control my temper, I pick up the receiver of the phone on my desk and dial the number for Audrey's extension."
    audrey.say "Hello?"
    mike.say "Audrey, would you mind stepping in here for a moment?"
    audrey.say "Okay...sure, I'll be right there."
    mike.say "Thank you so much..."
    "It only takes one glance from my quietly seething expression to Aletta's gloating smile for Audrey to realise she's in some rather deep shit."
    show aletta at right with move
    show audrey at left with moveinleft
    "Credit where it's due though, she still makes a valiant effort to appear none the wiser as to what's going on."
    audrey.say "Erm...you said that you wanted to see me?"
    show aletta happy
    "Aletta simply can't keep herself from letting out a sudden laugh at the other girl's feigned innocence."
    aletta.say "He knows all about it - I told him what I saw you doing in the mailroom, you stupid little bitch!"
    show aletta normal
    "I cast a quick glance at Aletta, catching her eye."
    menu:
        "Let Aletta stay" if aletta.love >= 150 and aletta.sexperience >= 1 and aletta.sub >= 25:
            $ aletta_stay = True
            "I really should tell Aletta to get the hell out of here while I deal with Audrey in the only way that seems to work."
            "But there's just something about the gloating look that she has on her face right now that turns me on as much as the thought of spanking Audrey."
            mike.say "Audrey, get your ass here, right now and bend over the edge of my desk."
            mike.say "You deserve to be punished for what you've done."
            mike.say "And Aletta here deserves a reward, so she can watch me discipline you."
            "While Audrey slinks over to the indicated spot, Aletta looks shocked."
            "But I can't tell if she's more taken aback by the revelation that I'm about to spank Audrey or that I've invited her to watch."
            "Whatever the case, while she remains silent, I see that she also makes no effort to leave."
            "I nod at this, and she quietly closes the door as I push back my chair and go to stand behind Audrey."
        "Tell Aletta to leave":
            $ aletta_stay = False
            "I can see from the look on Aletta's face that she almost desperately wants to stay and see me chew Audrey out."
            "But the problem with that is the punishment I had in mind is a bit more extreme and definitely more corporal in nature."
            "I can't honestly go ahead with it if I'm going to have Aletta looking over my shoulder, so she's got to go."
            mike.say "Aletta, would you excuse us for a moment?"
            mike.say "Audrey and I have to straighten a few things out in our working relationship."
            mike.say "And as I'm sure you know, disciplinary matters are strictly confidential."
            "I can tell from the irritation on Aletta's face that she's loathe to give in, but I've got her on a technicality."
            "She gives me a terse nod and strides out, leaving me alone with Audrey."
            hide aletta with moveoutleft
            mike.say "Audrey, get your ass here, right now and bend over the edge of my desk."
            mike.say "You deserve to be punished for what you've done."
    "As much as I know that this is pretty much what Audrey's been trying to push me into doing for some time now, I'm simply too hot to back down."
    "Before she was just playing stupid pranks on me around the office, but this has been a cause of stress for me in the past few weeks."
    "If she thought that getting me mad was going to be some kind of game, then I'm determined to prove her wrong."
    hide aletta
    hide audrey
    show spank audrey spank surprised
    play sound spank
    with hpunch
    "Without a word of warning, I clap a hand on Audrey's thigh."
    "The blow is hard enough to make a slapping sound, and I hear her gasp in surprise - maybe even arousal."
    "Not pulling the hand away, I use it to roughly pull her already short skirt up, exposing her backside."
    show spank audrey spank pleasure pulled
    "With my other hand on the back of her neck, I squeeze one of her buttocks as hard as I dare, making her gasp again."
    mike.say "I used to think that you were just being playful, Audrey."
    mike.say "I used to think that you were kind of the office clown around here."
    "I give her ass another hard squeeze, just to keep her attention focused on what I'm saying."
    mike.say "But now I see that I was wrong, and Aletta's right."
    mike.say "Only you're not a stupid little bitch - you're a spiteful little bitch!"
    "This time I practically crush her buttock in my hand, sure that I must have left bruises on her behind."
    "Audrey squeals at the sensation, trying to keep from making enough noise to have someone look in on us to see what's the cause of it all."
    mike.say "What you did caused me a lot of hassle."
    mike.say "It was a real pain in the ass."
    mike.say "So now I'm going to give you a pain in the ass in return..."
    show spank audrey up
    pause 0.3
    show spank audrey spank surprised
    play sound spank
    with hpunch
    "I deliver the first slap with the palm of my hand almost before the words are out of my mouth, giving Audrey no time in which to prepare."
    "Her panties do nothing to cushion the blow, and the sharp sound my hand makes upon contact with her buttocks almost drowns out her cry of alarm."
    "Even though I start out slowly, actually trying to make a true punishment out of this, I can't help quickening my pace."
    show spank audrey up normal
    pause 0.3
    show spank audrey spank
    play sound spank
    with hpunch
    "For all of her yelps and cries of pain, I can tell just how much Audrey must be enjoying what I'm doing to her right now."
    show spank audrey up
    pause 0.3
    show spank audrey spank
    play sound spank
    with hpunch
    "Soon all thought of actually inflicting pain on her for the sake of teaching her a much needed lesson falls by the wayside."
    "All I can think about is the sight of her curvaceous body bent and prone over my desk."
    "The sound of her panting breath is making me breathe heavily almost in sympathy."
    show spank audrey up
    pause 0.3
    show spank audrey spank marks
    play sound spank
    with hpunch
    "And every time my hand makes contact with her ass, I can't help but marvel at just how good it feels."
    "By now my cock is so hard that I can feel it pressing against the waistband of my shorts."
    show spank audrey up pleasure
    pause 0.3
    show spank audrey spank
    play sound spank
    with hpunch
    "The only thing covering Audrey's reddening buttocks and what lies between them is a flimsy pair of panties."
    "It would be so easy to pull them down and discipline her in another way entirely."
    "My hand hovers over my flies for a moment..."
    "But then I seem to snap back to reality, as the weight of what I was thinking of doing hits home."
    "Shaking my head, I deliver one final, mighty blow to Audrey's backside and then yank her skirt back down again."
    hide spank
    if aletta_stay:
        $ audrey.sub += 10
        $ aletta.sub += 5
        show audrey at right
        show aletta at left
        "Before I can do anything to dismiss Audrey from my presence, Aletta gives her a vicious shove in the small of the back."
        aletta.say "Now run along, bitch - unless you want to be punished some more?"
        "Audrey looks back over her shoulder, as if contemplating whether or not to stand up to Aletta."
        "But then she turns and makes hastily for the door, and I think that I can see the beginning of tears in her eyes as she does so."
        "I slump down in my chair, wondering if I made the right choice in being so hard on Audrey."
        "But there seems to be no doubt in Aletta's mind, as she regards me with an admiration that almost seems to verge on actual physical hunger."
        hide aletta
    else:
        $ audrey.sub += 5
        show audrey
        "I give her a rough shove in the small of the back, pushing her towards the door in order to let her know that I'm done with her."
        "She staggers a little as she tries in vain to regain a little of the defiance and dignity that the spanking has cost her."
        "Stopping at the door to my office, Audrey looks back for a moment, as if expecting me to say something."
        "But I just sit back down behind my desk and make a dismissive gesture with my hand, unwilling to lose the upper hand I hope that this has gained me in our relationship."
        "Somehow, I doubt that this will be the last time that I find myself having to get hands on when it comes to dealing with Audrey in the workplace."
    hide audrey
    $ hero.replace_activity()
    $ game.pass_time(1)
    return

label audrey_spanking_start:
    $ audrey.flags.spankingdelay = TemporaryFlag(True, 3)
    "I'm so engrossed in the file open on my desk before me that I fail to even look up at the sound of the door to my office opening."
    "The fact that the person that's just walked in makes no attempt to identify themselves or say what they want isn't enough to make me do so either."
    "Past experience tells me that if they stay silent, then it's likely to be Aletta, waiting huffily for me to pay her attention."
    "Or if the person begins to make apologetic sounds in the next couple of seconds, then it's Shiori, demurely waiting for me to deign to notice her existence as usual."
    show audrey
    audrey.say "Hey, wake up - I haven't got all day!"
    "Now I have to admit, that was not what I was expecting to hear."
    "I look up to see Audrey standing in front of my desk, no sign of anything whatsoever in her hands that would make her visit work-related."
    "Taking a deep breath, I put down my pen and try to manage at least a ghost of a smile at her unasked for presence before me."
    mike.say "Audrey, to what do I owe the pleasure of this unexpected visit?"
    "She has a sardonic, superior smile on her face as she regards me."
    "But seeing as how that's more often than not her default expression, it doesn't help me guess at her purpose."
    "Audrey walks forwards so that she can sit on the edge of my desk."
    "She's sure to see that her skirt rides up as she crosses her legs, affording me a fine view of her hemline riding up to reveal her thighs."
    "Leaning forwards, she reclines on one elbow, as though she were posing for a revealing photoshoot."
    audrey.say "I just thought that I should drop by and let you know that I'm onto you..."
    "As distracting as it is to have her draped over my desk right now, I still manage to get my words out in an honest response."
    mike.say "Audrey, I have absolutely no idea what you're talking about."
    mike.say "Would you either start making sense or get the hell out of my office, please?"
    "Audrey raises her eyebrows at my statement of denial."
    show audrey frown
    audrey.say "Oh, but I think you do know what I mean."
    audrey.say "I've been having a little chat with Shiori on her breaks."
    audrey.say "And she's been very eager to tell me all about the private meetings you've been having."
    show fx exclamation
    audrey.say "The private spanking meetings!"
    "Oh shit - now she's got my attention!"
    mike.say "Audrey, whatever happens between myself and other co-workers is none of your business!"
    "Audrey immediately jumps on what I just said, like a cat pouncing on its prey."
    show audrey normal
    audrey.say "Aha - I knew it, you have been spanking Shiori's pasty little behind!"
    audrey.say "And I'll bet it was right here in your office too!"
    "I try to keep from reacting to the accusation, but I can already feel my cheeks turning red."
    mike.say "Now you're just putting words in my mouth, Audrey."
    mike.say "I admitted to no such thing!"
    show audrey annoyed
    audrey.say "Ah, but you didn't deny it, did you?"
    audrey.say "Anyone can tell you that's as good as admitting that you're guilty!"
    mike.say "Who can tell you that - what are you even talking about?"
    "I lean back in my chair, trying as best I can to come across as calm and pragmatic."
    "But inside I'm already dreading the next question I have to ask and just where it might lead."
    mike.say "Okay, Audrey - what do you want?"
    "At this, she pulls back a little, putting a hand on her chest as if shocked by my line of questioning."
    show audrey normal
    audrey.say "What on earth can you be implying?"
    "I give her what I hope looks like a begrudging grin."
    mike.say "Come on - we both know you're not the Mother Theresa type, Audrey!"
    mike.say "There's no way that you'd come to me just for the sake of Shiori and some misplaced sense of sisterhood."
    mike.say "So I'll ask you again, Audrey...what do you want from me?"
    "She shrugs and makes a sound that's intended to be taken as nonchalant."
    audrey.say "Well, you see I'm a pretty modern kind of girl, [hero.name]."
    audrey.say "And one of the things that I'm passionate about in the workplace is equality, regardless of sex, gender or race."
    show audrey flirt
    audrey.say "So when I hear that Shiori has been getting a bonus that I haven't..."
    "Audrey sighs dramatically."
    show audrey annoyed
    audrey.say "Well, it makes me feel slighted, to say the very least."
    "Now I'm the one that's sighing."
    "Or maybe groaning at the inevitable conclusion I see fast approaching."
    mike.say "And do tell me, Audrey - how do you see there being a resolution to this most vexatious of issues in our department?"
    "Audrey's smile only becomes wider now, as she's clearly delighted to have reeled me in so far."
    "She uncrosses her legs and lowers them to the floor so that her backside is facing me across the desk."
    "Then she hitches down her shorts, so that her ass is revealed beneath her pantyhose and knickers."
    show audrey normal
    audrey.say "I would like to propose fair and equal treatment for my ass."
    "I have to admit that the fact she says this with a straight face does add to the moment somewhat."
    audrey.say "I feel it would only be right that my posterior receive regular spankings from yourself at regular intervals of my choosing."
    mike.say "Or in layman's terms..."
    audrey.say "Yeah...I want you to spank my ass."
    show audrey flirt
    audrey.say "Good and hard, as and when I want it."
    mike.say "And if I don't?"
    show audrey normal
    audrey.say "Then I go running to HR and squeal on you for being a massive perv."
    "She gives me a sickly smile to underline her sincerity on the last point."
    "I take a deep breath, blow out my cheeks and shake my head."
    mike.say "Hell, Audrey, I don't see how you leave me any other choice..."
    menu:
        "Refuse":
            $ audrey.sub -= 5
            $ audrey.love -= 5
            mike.say "I'm going to have to ask you to leave, and take your filthy little collection of lies with you."
            show audrey angry
            "There's a genuine look of shock and surprise on Audrey's face as she shakes her head at me."
            "I'm damn sure that she's already steaming mad and plotting her next step to get her revenge."
            "But there's a part of me that's sure she's never been rebuffed like this when she's played these games in the past."
            audrey.say "Okay, if that's the way you want it."
            audrey.say "I'll be going to HR, you can be sure of that."
            audrey.say "But it won't be right now."
            audrey.say "Might be tomorrow, might be next week, or even next month."
            audrey.say "So enjoy thinking about it while that's hanging over you!"
            "She storms out in an appropriately dramatic fashion."
            "But I can't help thinking that by calling her bluff like that, I might just have begun to earn her begrudging respect."
        "Accept":
            $ audrey.flags.spanking = 1
            $ audrey.sub += 5
            $ audrey.love += 5
            mike.say "But to give you exactly what you want."
            show audrey blush
            "I try to keep from smiling, and I think that I manage to keep the effort from Audrey's notice."
            mike.say "So long as I have your word that you won't go to HR, I will agree to spank you, as and when you desire."
            "Audrey regards me with a triumphant look, almost as though she can't believe that I gave in to her demands so easily."
            "She nods her approval and turns to leave."
            audrey.say "I'll hold you to that promise, but leave the exact time and place open-ended!"
            "I just nod and let her go, trying not to crack a smile as she walks out."
            "I'm quite happy to let Audrey think that she's got one over on me, whether she really has or not."
            "Especially when the upshot of that is her coming to my office at semi-regular intervals to spank her brains out."
            "It's almost like I've been able to get my hands on that impressive ass of hers without even trying!"
            $ audrey.flags.start_spanking = True
    "Once she's gone and I'm alone in my office once again, I shake my head and go back to my work on the file in front of me."
    "I have a vague memory of someone telling me that I shouldn't try to get a job in an office, as it was all boring, monotonous routine."
    "I think that if I met that person again, I might just be tempted to slap them across the face."
    $ hero.replace_activity()
    $ game.pass_time(1)
    return

label audrey_sub_event_03:
    "I look up from my desk, my tongue almost hanging out of my mouth as I do so."
    "My head's been so occupied with work I only just realised how thirsty I am!"
    "But that can't be right - I've been swilling coffee like there's no tomorrow."
    "Urgh...that's part of the problem - I have a serious case of coffee-mouth too!"
    "What I need is cool, crisp water, and lots of it."
    "And there's only one place to get it in the office."
    "To the water-cooler I go!"
    scene bg breakroom with fade
    "Hurrying out of my office, I make straight for the nearest one."
    "I just want to grab a cup of water and get straight back into it."
    "The closest water-cooler to me is just around the corner."
    "And I'm pretty sure it'll be deserted as it's a little out of the way too."
    "A moment later, I set eyes on my goal."
    "There's the cooler, full of ice-cold water!"
    audrey.say "Oh..."
    show audrey
    audrey.say "Hey, [hero.name]!"
    "Audrey seems to appear out of nowhere, stepping into my path."
    "I look over her shoulder at the water-cooler, trying to step around her."
    mike.say "Audrey, I..."
    mike.say "Would you mind..."
    mike.say "I want to..."
    show audrey joke
    show fx question
    "At first Audrey chooses to play dumb, pretending not to understand."
    "She follows my movements, blocking me from getting around her."
    hide fx
    "But then she looks over her shoulder and pretends to have a revelation."
    audrey.say "Oh, I see!"
    audrey.say "You want the water-cooler, right?"
    audrey.say "Well, you're higher up the ladder than me, [hero.name]!"
    show audrey happy
    audrey.say "So let me get that for you, okay?"
    "Audrey turns to use the water-cooler."
    "But I keep on trying to reach it myself."
    "Normally Audrey would rather let me die of thirst than get me a cup of water."
    "So you can understand why I'm not taking this sudden show of helpfulness at face value."
    mike.say "Ah..."
    mike.say "No..."
    mike.say "Audrey...I can..."
    show audrey joke
    "What follows is an undignified scrum between the two of us."
    show audrey at right with hpunch
    "Audrey trying to use the water-fountain while keeping me away from it."
    show audrey at left with hpunch
    "And me trying to get around her and reach the fountain at the same time."
    hide audrey
    show audrey close with hpunch
    "Soon enough the result is that we're both leaning against the thing in a tangle of limbs."
    "But more importantly, Audrey is pinned between myself and the fountain."
    show audrey close blush
    audrey.say "Well this is awkward..."
    audrey.say "Don't you think, [hero.name]?"
    "Audrey underlines her point by grinding her ass against me."
    "I can feel the soft curve of her buttocks as they rub against my cock."
    "And almost the same second, I also feel myself starting to get hard."
    "Audrey must feel it too, as she lets out a filthy laugh."
    show audrey close surprised
    audrey.say "Oh my!"
    audrey.say "Is this actual sexual harassment?"
    show audrey close joke
    audrey.say "Or is your dick too limp to back it up, huh?"
    "Audrey laughs again as she reaches back to roughly squeeze my dick."
    menu:
        "Show her who's the boss":
            if audrey.sub.max < 100:
                $ audrey.sub.max = 100
            "Suddenly all thought of my thirst disappears."
            "Now what I have is a hunger."
            "An almost desperate hunger - for Audrey!"
            "Without telling her what I have in mind, I spring into action."
            show audrey surprised
            show fx exclamation
            "I put one hand on Audrey's shoulder, shoving her harder against the water-fountain."
            "The other I use to reach under her skirt and roughly yank down her panties."
            scene audrey standing with hpunch
            audrey.say "Oh..."
            audrey.say "Oh fuck..."
            audrey.say "What are you doing?!?"
            mike.say "What does it feel like, Audrey?"
            mike.say "I'm backing it up!"
            "I hear Audrey start to gasp in delight."
            "She nods and pushes her ass harder against me."
            audrey.say "Now you're talking!"
            audrey.say "You show me how you do it, [hero.name]!"
            audrey.say "I've been a bad girl, haven't I?"
            "By now I have my flies open and my cock out."
            "It's harder than ever as I listen to Audrey beg for it."
            mike.say "You're the worst, Audrey!"
            mike.say "A spiteful little bitch!"
            "I mean every word that I'm saying."
            "But by god she's a sexy little bitch too!"
            "I line myself up and thrust forwards."
            "There's no time to be careful and make sure I'm on target."
            "All I can think about is fucking Audrey, quick and dirty."
            "She squeals as the head of my cock slides along the lips of her pussy."
            "I don't get inside that time, but I can feel how hot and wet she is."
            "Grabbing Audrey with a firmer hold, I try again."
            "This time I hit the spot, and I feel myself pushing into her."
            audrey.say "Oh shit..."
            show audrey standing pleasure
            audrey.say "It's so big..."
            audrey.say "I fucking love it!"
            audrey.say "Fuck me hard - PLEASE?!?"
            "I'm already doing that as Audrey's begging me."
            "I push as far as possible into her, feeling my cock fill her."
            "And then I start thrusting in and out as fast as I can go."
            "I don't want to earn myself credit for going long or being sensitive."
            "All I want is to pound Audrey to within an inch of her life!"
            "And I seem to be doing a pretty good job from the word go."
            "Pressed up against the water-fountain, Audrey's already panting and moaning."
            "Her skirt hitched up around her waist, tongue hanging out like a parched dog."
            "Audrey looks back over her shoulder at me as I fuck her."
            "But her eyes are beginning to glaze over and her expression is one of blank pleasure."
            "I'm literally taking out all of my frustrations on her right now."
            "It's like she knows that's what my motivation is."
            "And she's loving it too!"
            audrey.say "Mmm..."
            audrey.say "Yeah...fuck yeah..."
            audrey.say "Bad girl...I'm a...bad girl..."
            "The dazed state that Audrey's in only gets worse a moment later."
            with vpunch
            "And that's because I lose it, cumming inside her."
            show audrey standing ahegao cum with vpunch
            "The end is as rough as the rest of it, one final thrust."
            "When it's over, Audrey goes limp, like a rag-doll."
            "If it weren't for me and the water-fountain, I honestly think she's collapse!"
            scene bg breakroom
            show audrey naked blush flirt
            with fade
            "I hastily pull my cock out of her and stuff it back into my pants."
            "She comes around enough to fumble with her panties."
            "But as she tries to pull them up, cum is already seeping out of her."
            "It runs down the inside of her leg, soaking into her stockings."
            show audrey work -naked
            $ audrey.love += 4
            audrey.say "Th...thanks, [hero.name]..."
            audrey.say "Gotta...go...lie down..."
            audrey.say "Legs are like...like jelly!"
            "She wanders off, staggering from side to side."
            "And all I can do is watch in silence."
            "Though I do admit to feeling an odd sense of pride at the sight too!"
            $ audrey.sexperience += 1
        "Stay professional":
            "I let out an exasperated sigh."
            "Then I throw my arms up in the air and take a step backwards."
            "This removes me from contact with Audrey."
            "But more importantly it shows that I have no intention of touching her either."
            mike.say "The size of my bodily organs is not an acceptable subject for discussion in the workplace, Audrey."
            mike.say "You should really reserve that kind of thing for social events taking place away from the office."
            show audrey annoyed -close
            "Audrey gasps at this, turning to face me."
            "She looks seriously annoyed at my actions."
            "But there's really nothing she can do about it."
            "I'm playing it strictly by the book from this point on."
            "And any more shenanigans on her part will only make her look like the guilty party."
            $ audrey.sub += 2
            audrey.say "Oh..."
            audrey.say "So that's how it is, huh?"
            audrey.say "Well forget you, [hero.name]."
            audrey.say "I thought you were different."
            show audrey angry
            audrey.say "But it turns out you're just another empty suit!"
            hide audrey with easeoutleft
            "With that, Audrey storms off."
            "Which finally leaves me free to use the water-fountain."
            "I mean really - the things I have to do to get a drink around here!"
            $ hero.cancel_event()
    $ hero.cancel_activity()
    $ game.room = "breakroom"
    return

label audrey_sub_event_02:
    scene bg cinemaroom
    "I've been itching to see the film Audrey and I are sitting down to watch for ages now."
    "Goblins was one of those cult classics from way back in the eighties that just gets cooler with time."
    "And it's been like almost a forty year wait for them to make and release a sequel to it."
    "Of course Jack's already seen it half-a-dozen time, and he's desperate for me to see it too."
    "Because he's on the verge of exploding from not wanting to spoil the film for me!"
    "So it's kind of important that I devote myself to the experience, you know?"
    show audrey annoyed casual with dissolve
    "The only problem is that I had to drag Audrey along to see it with me."
    "Even as the trailers are ending and the film is starting, she's still complaining!"
    show audrey angry
    audrey.say "I can't believe I let you talk me into this!"
    audrey.say "Dates are supposed to be fun for both of us, you know?"
    mike.say "Keep your voice down, Audrey!"
    mike.say "Some of us are trying to watch the film here!"
    show audrey annoyed
    audrey.say "Urgh..."
    audrey.say "Fine, [hero.name], have it your way!"
    show audrey mock
    audrey.say "I'll just have to find a way to make my own fun..."
    "That sounds pretty ominous, and normally I'd call Audrey out on it."
    show audrey annoyed
    "But she hisses those words at me just as the film finally begins."
    "And that means that my attention is instantly drawn away."
    show audrey cinema bj popcorn with fade
    "Soon enough I find myself forgetting all about her vague promises."
    "Because I'm sinking into a warm, comforting bed of nostalgic goodness!"
    "The film's great, far better than I'd expected it to be."
    "In my head I'm already preparing to discuss it at length with Jack."
    "And to be honest, I'd kind of forgotten that Audrey was even there!"
    show audrey cinema bj mikepleasure with vpunch
    "That's why I can't help jumping in my seat when I feel someone touching me."
    "I throw most of my popcorn in the air and let out a yelp of surprise."
    "But luckily for me it happens almost exactly as a jump-scare on the screen."
    "Which means that everyone else in the place is doing the same thing."
    "I look down and see a hand on my groin, opening my flies."
    show audrey cinema bj audreyhappy mikesurprised
    "And a quick glance to my side shows me that it belongs to Audrey!"
    "It's kind of a relief to find that it's my date that's feeling me up."
    "But that doesn't solve the actual problem of what she's doing."
    mike.say "Audrey!"
    mike.say "Stop it!"
    "Audrey smiles and shakes her head."
    "She's starting to sink down in her seat too."
    "It looks like she means business!"
    menu:
        "Let Audrey have her way":
            if audrey.sub.max < 75:
                $ audrey.sub.max = 75
            "I know better than to argue with Audrey when she in this kind of mood."
            "At least if she's occupied, then I know Audrey's kind of contained too."
            "The I can hopefully watch the movie without further interruption."
            "And who knows, I might even enjoy what she's going to do to me as well!"
            "So all I do is hold my hands up in a gesture of surrender."
            "She nods happily at this, then gets straight back to it."
            show audrey cinema bj blowjob
            "Within mere moments, Audrey has my cock out of my pants."
            "She leans in close and starts to stroke it to life."
            "Even though I'm concentrating on the film, this doesn't take long."
            "It's like I'm leaving my body in her hands while my mind is on higher things."
            "And Audrey seems perfectly happy with that arrangement."
            "I can feel her licking and kissing around the base of the shaft."
            "This means that I'm soon hard and standing to attention."
            show audrey cinema bj mikepleasure
            "Now her attentions become even more intense."
            "Audrey squeezes my balls as she licks her way higher."
            "By the time she reaches the tip, I'm biting my lip."
            "And when she takes it into her mouth, I feel my heart begin to pound in my chest."
            "But then Audrey chooses to work it slowly and with infinite care."
            "Her head moves up and down gracefully."
            "And she uses her lips, tongue, even her teeth like an expert."
            "I'm still watching the film, taking in everything on the screen."
            "Yet I can feel everything that she's doing to me at the same time."
            "I know the hairs on the back of my neck are standing up."
            "And I can feel my hands digging into the padded arms of my seat."
            "I must be twitching and writhing more than I realise."
            "Because I begin to feel Audrey using her weight to pin me down."
            show audrey cinema bj mikesurprised watching -popcorn
            "Suddenly I notice that she's not got my cock in her mouth anymore."
            "The suspicion is confirmed a moment later when I hear her chuckling."
            show audrey cinema bj mikehappy
            "And then, before I can object, she's crawling up and over me."
            "Audrey's sure to stay as low as she can, making sure she's not seen."
            "But that doesn't stop her from getting into the exact position she wants."
            show audrey reverse cowgirl cinema with fade
            "Before I know what she's trying to do, Audrey's straddling me in my seat."
            "She reaches back wit one hand, grabbing my cock as she directs traffic down there."
            show audrey reverse cowgirl vaginal mikepleasure audreyahegao
            "Then she pushes it hard against her groin, and I discover she's ditched her panties!"
            "How she managed to pull off something like that is beyond me."
            "But it's also that last thing on my mind as I feel how slick she is right now!"
            show audrey reverse cowgirl mikenormal audreypleasure
            "It only takes a few seconds for me to begin pushing inside of her."
            "Audrey speeds this up even more by pushing down with all her weight."
            "Her head is resting on my shoulder now."
            "And so I hear her gasping and panting as I fill her up."
            "Then she starts to grind, almost desperately, against me."
            "My hands reach out and take hold of her haunches."
            "My eyes are still fixed on the screen, but I can't help myself."
            show audrey reverse cowgirl audreyahegao
            "I squeeze Audrey tight and push her downwards as I thrust up from below."
            "This makes her squeal into my ear, almost too loud for comfort!"
            "Realising this, she buries her head against my neck."
            show audrey reverse cowgirl audreypleasure
            "Then Audrey uses her lips to kiss my neck, nibbling and licking too."
            "This isn't romantic sex where we're both expressing ourselves in a beautiful manner."
            "It's quick, dirty fucking in a public place, made hotter by the danger of getting caught!"
            "I keep on thrusting roughly into Audrey, desperate to have her despite everything."
            "And she clings to me like a needy animal in heat, squealing as I pound her."
            "Thankfully it can't go on like this for too long."
            $ audrey.love += 5
            show audrey reverse cowgirl mikepleasure audreyahegao creampie with vpunch
            "Soon enough I make one last push, then shoot my load into Audrey."
            with vpunch
            "She stiffens, curling into a ball as she cums too."
            show audrey reverse cowgirl exhausted vaginaldrip -creampie with vpunch
            "Then she slides off me, flopping into her own seat."
            $ game.active_date.score += 40
            audrey.say "Mmm..."
            audrey.say "I...I...I..."
            audrey.say "Whoo..."
            "Audrey continues to babble quietly to herself for the rest of the film."
            "But at least now she's satisfied and happy to leave me in peace."
            show audrey reverse cowgirl mikenormal
            "And now I know what I have to do to get her to shut the hell up in future."
            "Just fuck her in public, and everything will be fine!"
            $ audrey.sexperience += 1
        "Stop Audrey":
            hide audrey
            show audrey surprised casual with hpunch
            "My hand shoots out and grabs Audrey's wrist."
            show audrey frown
            "Instantly she looks up, a frown on her face."
            audrey.say "Hey!"
            audrey.say "What the hell?"
            show audrey angry
            audrey.say "I want to have some fun too!"
            mike.say "There's plenty of time for that later."
            mike.say "Can't you control yourself for once?"
            $ game.active_date.score -= 40
            $ audrey.sub += 2
            show audrey frown
            "Audrey shoots me a look that could curdle milk."
            "And then she roughly yanks her hand out of my grasp."
            hide audrey
            "After that she crosses her arms over her chest and turns away."
            "Sure, she's starting to sulk and she'll be pissed when the film's over."
            "But at least I can actually watch it in relative peace now."
            "So I put all thought of that to the back of my mind."
            "And I turn all of my attention to watching the film."
            "There's going to be time enough to grovel for forgiveness after the end credits roll..."
            $ hero.cancel_event()
    $ audrey.flags.subevent = TemporaryFlag(True, 1)
    $ hero.replace_activity()
    return

label audrey_sub_event_01:
    if audrey.sub.max < 25:
        $ audrey.sub.max = 25
    "Audrey and I just had one hell of a good time together, a date where everything went well."
    "Both of us are beaming as we walk back home, chatting about this and that without a care in the world."
    "We could have taken the quickest route back and saved maybe as much as twenty minutes of walking."
    "But I chose to lead us into the park instead, that way we can enjoy the scenery as we stroll."
    scene bg park
    show audrey casual with fade
    "Normally the path we're on would be pretty full of dog-walkers, joggers and the like."
    "But it's getting late, and so we don't see many other people about as we cross the park."
    "We're about halfway along the path, near a small wooded area, when I notice Audrey looking around."
    "At first I think she must have seen something in the trees."
    "And so curious to be let in on it too, I ask her what it is."
    mike.say "What have you seen, Audrey?"
    mike.say "Anything interesting - like a fox or a badger?"
    show audrey annoyed
    "Audrey turns to face me, a sardonic grin on her face."
    audrey.say "Foxes and badgers?"
    audrey.say "What the actual fuck, [hero.name]?!?"
    audrey.say "I'm looking for a place to get dirty."
    show audrey joke
    audrey.say "I don't know what you're looking for!"
    show audrey close with hpunch
    "With that, Audrey grabs hold of my wrist."
    "Then she starts dragging me towards the tree-line."
    "I go along with her at first out of sheer surprise."
    "Well, that and the fact that she's deceptively strong too!"
    "But if I don't do something soon, Audrey will have me over there in a few seconds!"
    menu:
        "Let Audrey have her way":
            "And what, exactly, is the problem with that?"
            "I don't know exactly what Audrey has in mind."
            "But I'm not about to miss the chance to find out!"
            "So I let Audrey pull me off the path and into the woods."
            show audrey happy
            "The whole time she's grinning at me, winking too."
            "And that alone is enough to start getting me hard."
            "As soon as we're far enough into the woods not to be seen, Audrey stops."
            "I mean, I think we're far enough in not to be seen from the path."
            "I can't really be sure - but I think that's kind of the idea!"
            show audrey flirt
            audrey.say "Now you just stand nice and still, okay?"
            audrey.say "And let me do what I do best..."
            hide audrey with moveoutbottom
            "Audrey's lowering herself down as she says this."
            "She's kneeling on the ground in front of me."
            "And she's hastily tugging at my flies too!"
            "I keep looking down at Audrey and then up at the treeline."
            "I don't know which is making my heart race the most."
            "On the one hand I'm desperate for her to get started."
            "But on the other I'm terrified of someone spotting us too!"
            show audrey bj park with fade
            "It's as I'm looking away from her that Audrey gets my cock out."
            "I gasp and shudder as she wastes no time in getting down to it."
            audrey.say "Mmm..."
            audrey.say "There you are!"
            audrey.say "Already nice and hard too!"
            "Before I can say a word, Audrey leans forwards."
            "She doesn't bother with foreplay of any kind."
            "And she doesn't pay attention to anything but the tip."
            "Almost like she's desperate, she just parts her lips."
            show audrey bj blowjob
            "And then she takes it into her mouth."
            "Audrey makes it hasty and sloppy, licking and sucking from the start."
            "I know from experience that she can do this in a more refined manner."
            "But the sloppiness somehow adds to the experience, makes it that much hotter!"
            show audrey bj blink
            "Audrey's head goes back and forth, faster by the second."
            "At the same time she's working the shaft of my cock with one hand."
            "The combination is almost too much for me to handle."
            "I'm fighting to keep from cumming almost as soon as she hits her stride."
            "But I hold on desperately, wanting as much of this treatment as I can get."
            show audrey bj normal
            "It's then that I see people walking along the path beyond the trees."
            "I almost lose it then, shoot my load into Audrey's mouth."
            "But by some miracle I manage to hold on."
            "I'm holding my breath too, as if it makes a difference."
            "I doubt anyone can hear me panting from so far away."
            "No matter what logic tells me, I'm still sure they're getting closer."
            "In fact, I'm sure they'll spot me any moment now!"
            mike.say "Ah..."
            mike.say "Oh fuck..."
            mike.say "Audrey!"
            "At the sound of my voice, Audrey springs into action."
            show audrey bj out
            "She pulls my cock out of her mouth, still holding it tight."
            $ audrey.love += 2
            show audrey bj blink cumshot with vpunch
            "Then she closes her eyes and parts her lips as I lose it."
            with vpunch
            "Audrey gasps and giggles in delight as I shoot my load into her face."
            with vpunch
            "It stripes her cheeks and nose with sticky, white bands."
            show audrey bj dickcum
            "And a good amount lands in her open mouth too."
            "Audrey swallows it happily, then licks her lips."
            "She smiles up at me, totally taking my mind off the walkers on the path."
            "And all I can do is watch as she licks herself, and my cock, clean again."
        "Don't let Audrey do whatever she wants":
            "What in the hell is she doing?"
            "We can't do anything like that in the park!"
            "The chances are somebody's going to see or hear us."
            "We could even get arrested, end up with a criminal record!"
            mike.say "I don't think so, Audrey!"
            mike.say "That can wait until we get home."
            show audrey normal -close
            "I'm resisting Audrey's pulling as I say this."
            "And I see the expression on her face change as a result."
            "Pretty soon she stops pulling and plants her fists on her hips."
            audrey.say "What's the problem, [hero.name]?"
            audrey.say "Don't you want to have a little fun?"
            mike.say "Yeah, Audrey, I do."
            mike.say "But back at my place."
            mike.say "Not in the middle of the damn park!"
            show audrey annoyed
            "Audrey lets out a snort of irritation."
            "In fact, I almost expect her to stamp her foot."
            audrey.say "Don't be such a prude!"
            audrey.say "We'd be behind those trees."
            audrey.say "It's not like we'd be screwing around out in the open!"
            "I shake my head and start walking away."
            mike.say "Sorry, Audrey."
            mike.say "It's not happening!"
            "Audrey stands on the spot for a moment, still fuming away."
            show audrey angry
            $ audrey.love -= 5
            $ audrey.sub += 5
            "Then she snorts for a second time and hurries after me."
            audrey.say "You win, you puritanical bore!"
            audrey.say "But you mark my words, [hero.name]..."
            audrey.say "You'd better do something seriously dirty to me to make up for it!"
    $ audrey.flags.subevent = TemporaryFlag(True, 1)
    $ hero.replace_activity()
    return

label audrey_event_10:
    if audrey.love.max < 200:
        $ audrey.love.max = 200
    "It's been a while since I tried to confess my feelings to Audrey."
    "And I can't help noticing that she's been avoiding me this whole time."
    "Which is weird for her, as she doesn't usually miss a chance to torment me."
    "And what with me actually telling her that I was in love with her..."
    "Well, I'd have thought she'd have enough material to torture me for a long time to come!"
    "But no - even when I see her across the office, Audrey hurries away."
    "And no matter what I do, she's nowhere to be found when I try to reach her."
    "In the end, it's purely by chance that I manage to corner her."
    "We're passing each other and I blurt out a greeting before she can pull her disappearing act."
    mike.say "Audrey!"
    mike.say "How have you been?"
    show audrey annoyed
    "I can see that Audrey's not happy to be forced into speaking with me."
    "But I'm talking to her in a public place, and so she's obliged to put on a front."
    "Otherwise the gossip from her blanking me would start almost instantly."
    "And that's probably the last thing that she wants right now."
    audrey.say "Oh...oh, hi, [hero.name]."
    audrey.say "I've been good...you know?"
    mike.say "That's great to hear."
    mike.say "I've been wanting to talk to you."
    mike.say "Ever since we had that chat the other day..."
    mike.say "I kind of feel like you've been avoiding me!"
    show audrey at zoomAt (1.25, (650, 850))
    "At the mere mention of that subject, Audrey leans in closer."
    "She practically hisses the next thing that she says into my ear."
    audrey.say "Okay, [hero.name], okay."
    audrey.say "You win - we'll talk about it."
    audrey.say "But not here!"
    "I nod in agreement, trying to show Audrey that I understand her terms."
    "And then I find myself being herded into a more secluded spot."
    "Once there, she turns on me, hands planted firmly on her thighs."
    if hero.flags.isceo:
        scene bg ceo
    else:
        scene bg personal
    show audrey annoyed
    audrey.say "Ah...okay...okay..."
    audrey.say "I'll start, [hero.name]."
    audrey.say "You're right - I have been avoiding you."
    mike.say "Oh...I'm sorry, Audrey."
    mike.say "I didn't mean to make it awkward."
    "Audrey looks me in the eye for the first time."
    "And then she laughs out loud."
    show audrey happy
    audrey.say "How was it ever going to be anything but awkward?"
    audrey.say "Asking me into your office and telling me that you love me?"
    mike.say "Like I already said, Audrey - I'm sorry."
    mike.say "If you don't feel the same way..."
    "Audrey holds her hand up, cutting me off in mid-flow."
    "She laughs again, but this time it sounds more rueful."
    audrey.say "I didn't say that, [hero.name]!"
    audrey.say "That's what makes it awkward."
    audrey.say "That I DO feel the same way!"
    "It takes a moment for me to fully comprehend what Audrey's saying."
    "I can understand the words she used, but not in the combination she used them."
    mike.say "Wait...what?!?"
    mike.say "You mean that..."
    "Audrey shrugs and offers me a weak smile."
    "A smile that looks honest and makes her appear almost vulnerable too."
    show audrey flirt
    audrey.say "I like you, [hero.name] - is that so hard to believe?"
    audrey.say "I mean...I don't often fuck people I hate!"
    mike.say "But, Audrey..."
    mike.say "You can be so...so spikey at times!"
    mike.say "Well...most of the time, if I'm honest!"
    show audrey normal
    audrey.say "I...I find it hard to tell people how I feel, [hero.name]."
    audrey.say "So I tend to get their attention in other ways, you know?"
    audrey.say "If it helps you to know it - I only tease people I really like!"
    mike.say "So that means you must REALLY like me!"
    show audrey mock
    "Audrey lets out another laugh at this."
    "But she nods her head at the same time."
    audrey.say "Oh, I could torment you to death, [hero.name]!"
    mike.say "That...kind of sounds like fun, Audrey!"
    show audrey happy
    "Audrey, leans her head on my shoulder, smiling up at me."
    audrey.say "Sounds like a challenge to me!"
    audrey.say "Shall we start by admitting that we like each other?"
    audrey.say "Then we can see where that takes us?"
    "I nod with a genuine feeling of enthusiasm."
    "And I lean my head against Audrey's."
    $ audrey.flags.nodate = False
    $ audrey.unhide()
    $ hero.cancel_activity()
    return

label audrey_event_09_intro:
    "This isn't something that I'm looking forward to - not in the slightest."
    "But it's getting to the point now where Audrey's almost constantly on my mind."
    "Well, to be more precise, my feelings for her are what's always on my mind."
    "I thought it was just that she was getting under my skin, bugging me the whole time."
    "But even the chance to burn some of by us doing it doesn't seem to have helped."
    "In fact, since we fucked like crazy right here in my office, it's only got worse!"
    "It's made me realise that what I feel for Audrey is far deeper than I thought."
    "I think I might actually be in love with her!"
    "There's no way of getting round it either, not while we're working together."
    "So that's why I'm going to get her in here and confront her with my feelings."
    "Still, I'm not about to summon Audrey into my office knowing that."
    "And so I cook up some rubbish about needing a file or some other routine bullshit."
    "Which means I have to wait for her to get her ass in gear and actually show up!"
    "When she finally graces me with her presence, Audrey already looks suitably annoyed."
    $ DONE["audrey_event_09_intro"] = game.days_played
    return

label audrey_event_09:
    if audrey.love.max < 180:
        $ audrey.love.max = 180
    show audrey annoyed
    audrey.say "Urgh..."
    audrey.say "Do you really need me to do this thing?"
    if not (shiori.hidden and lavish.hidden):
        audrey.say "Couldn't Shiori or Lavish do it instead?"
        audrey.say "They're always jumping at the chance to kiss your ass!"
    elif shiori.hidden and not lavish.hidden:
        audrey.say "Couldn't Lavish do it instead?"
        audrey.say "She's always jumping at the chance to kiss your ass!"
    elif lavish.hidden and not shiori.hidden:
        audrey.say "Couldn't Shiori do it instead?"
        audrey.say "She's always jumping at the chance to kiss your ass!"
    "Not for the first time I try to ignore Audrey's rudeness."
    "Ignore it and focus on what I actually have to talk to her about instead."
    mike.say "Ah, no, Audrey."
    mike.say "This is something they can't handle."
    mike.say "Because it's something that doesn't concern them."
    mike.say "Just you and me..."
    show audrey normal
    "Only now do I see recognition dawning on Audrey."
    "And as I expected, her mood begins to change at the same time."
    "Where before she was sullen and moody, now she becomes flirty and amused."
    show audrey flirt
    audrey.say "Oh, [hero.name]!"
    audrey.say "Why didn't you just say it was about us?!?"
    audrey.say "After all, we both know that I'm living inside of your head right now!"
    "I can't help but nod, much to Audrey's evident delight."
    mike.say "Ah, yeah, Audrey."
    mike.say "That is pretty much what this is about."
    show audrey happy
    show fx exclamation
    audrey.say "Ha!"
    audrey.say "I knew it!"
    mike.say "You're right, Audrey."
    mike.say "No matter how hard I try, I can't get you out of my head."
    mike.say "I...I love you!"
    show audrey normal
    "At the mere mention of that word, Audrey's expression changes again."
    "But where before she became confident, now she looks suddenly unsure."
    show audrey frown
    "Audrey frowns at me, crossing her arms over her chest."
    show fx question
    audrey.say "Wha...what do you mean?"
    audrey.say "I don't get it, [hero.name]!"
    "All I can do is shrug and shake my head."
    "I knew this would be hard, but I can't stop now."
    mike.say "I mean what I say, Audrey."
    mike.say "I can't stop thinking about you."
    mike.say "I get tongue-tied at the mention of your name."
    mike.say "I even invent bullshit reasons like this to get you into my office."
    mike.say "I mean that I've fallen in love with you."
    show audrey awkward at hshake
    "Now Audrey's the one shaking her head as she looks at me in disbelief."
    audrey.say "Oh no, I'm not falling for that one, [hero.name]."
    show audrey frown
    audrey.say "You can't kid a kidder, I know all the signs!"
    audrey.say "You're just saying all of this to get back at me...right?"
    "For a moment I'm not sure what in the hell I'm supposed to say to convince her."
    "I was fully prepared for Audrey to laugh in my face and call me pathetic."
    "I had no idea that she'd react to my confession like this!"
    mike.say "No, Audrey, I'm not kidding."
    mike.say "I'm just being honest with you."
    mike.say "Because I don't know what else to do!"
    "Audrey's still shaking her head as she begins to back towards the door."
    "At first I thought that she was annoyed or irritated by the idea."
    "That my being in love with her would be something she saw as a joke."
    "But now I'm starting to wonder if the notion doesn't actually scare her!"
    show audrey scared
    audrey.say "I...I'm going to walk out of here now."
    audrey.say "I'm going to walk out of here and pretend this didn't happen!"
    hide audrey with moveoutleft
    "All I can do is watch Audrey do just that, letting out a sigh as she goes."
    "Left alone in my office, I try to tell myself that wasn't too bad of a result."
    "At the very least I managed to tell her how I felt."
    "And that might go some way towards clearing the air between us."
    "But I'll admit that I'd been hoping for a hell of a lot more than that!"
    $ audrey.flags.scaredloved = TemporaryFlag(True, 3)
    $ audrey.flags.nodate = True
    $ audrey.hide()
    $ audrey.flags.forceLocation = (game.days_played, game.hour, "work")
    $ hero.cancel_activity()
    return

label audrey_event_08:
    if audrey.love.max < 160:
        $ audrey.love.max = 160
    if audrey.sub < 50:
        "It's one of those days when everything seems to have landed on my desk at once."
        "Everyone wants their pound of flesh, and they're hounding me to make sure they get it too."
        "At this rate, I'll be lucky if I make it home before dark tonight, or at all!"
        "So the last thing I need is to hear the sound of my office door opening."
        show audrey flirt with moveinright
        "Or to look up and see that it's Audrey standing there, grinning like a Cheshire cat."
        "I let out a sigh of frustration as I fix her with a seriously intense glare."
        mike.say "This had better be important, Audrey."
        mike.say "I'm kind of up to my neck here!"
        "I gesture to the piles of paperwork that are covering my desk."
        "But nothing I say or do seems to have the desired effect on her."
        "Instead, Audrey just walks over to my desk and leans on the edge."
        "She looks at the closest pile of papers, stacked precariously high."
        show audrey mock
        audrey.say "Oh, I see, [hero.name]."
        audrey.say "So much hard work for poor little you!"
        audrey.say "And it'd be such a shame if someone happened to do this..."
        "Suddenly and without warning, Audrey shoves the pile sideways."
        "It goes tumbling off of the desk, sheets spreading across the floor."
        "I'm up and out of my chair a second later, fists clenching with rage."
        mike.say "What the hell, Audrey!"
        mike.say "Do you know how much time you just cost me?!?"
        "I begin to walk around the desk towards her."
        "But Audrey quickly backs away, clinging to the edge of the desk as she goes."
        "As soon as she comes to another pile of paperwork, she does the same thing."
        "And she'd sure to hold my eye as she shoves each one to the floor."
        show audrey mock blush
        mike.say "Audrey!"
        mike.say "Fucking hell!"
        "I'm literally running after her by now as she flees around the desk."
        "It's only when she's pushed the last pile of papers to the floor that I catch her."
        "I finally grab hold of Audrey, pinning her back against the desk."
        "And in that moment, I realise that she's been leading me on the whole time."
        "From the look in her eyes and the way she's panting, I can tell."
        "This is what Audrey wanted from the start!"
        show audrey flirt
        audrey.say "Are...are you mad, [hero.name]?"
        audrey.say "Did I make your blood boil, huh?"
        "Another time I might have been able to pull myself back."
        "But Audrey's spent so long chipping away at me like this."
        "I know she wants it."
        "And so maybe I should give it to her."
        "Audrey gasps out loud as I push her further back over the desk."
        "And she gasps a second time when I pull down her panties too!"
    else:
        "It's one of those days when everything seems to have landed on my desk at once."
        "Everyone wants their pound of flesh, and they're hounding me to make sure they get it too."
        "At this rate, I'll be lucky if I make it home before dark tonight, or at all!"
        "I need a break, something to bleed off the stress before I go insane."
        "And almost without thinking, I pick up the phone and call Audrey's extension."
        audrey.say "Yeah..."
        audrey.say "What is it now?"
        "I ignore the flagrant disrespect in her tone and choice of words."
        "There are bigger things at stake right now than Audrey's bad attitude."
        mike.say "You, Audrey, I want you."
        mike.say "So get your ass in here on the double."
        "There's a pause on the other end of the line as Audrey reels from what I just said."
        "I guess she's used to being the one that gives out the rude tongue-lashings, not receiving them."
        "And just as she's about to mount some kind of response, I slam down the receiver."
        "It's a petty thing to do."
        "But it feels really good to be giving Audrey a taste of her own medicine."
        "And sure enough, a few moments later the door to my office flies open."
        show audrey angry
        "Audrey all but storms in, apparently still fuming from our brief telephone conversation."
        audrey.say "You mind telling me what the hell..."
        mike.say "Oh, shut up, Audrey."
        "I cut Audrey off dead, not giving her the chance to demand an explanation."
        show audrey awkward
        "Again, Audrey's caught off-guard and reeling as I push her around verbally."
        mike.say "You're not here to tell me what you think, okay?"
        mike.say "I have a ton of work, you can see that."
        "I gesture to the precarious piles of paperwork covering my desk."
        show audrey normal
        audrey.say "I..."
        audrey.say "I can see..."
        mike.say "I thought I told you to shut up already?"
        mike.say "All I need is to burn off some stress, Audrey."
        mike.say "In short, I need a fuck-toy - and you're it."
        show audrey surprised blush
        "Audrey's eyes go so wide I think they're going to pop out of her head."
        "Her mouth moves silently as she shakes her head."
        "And I think this is actually the first time I've seen her lost for words!"
        mike.say "What are you waiting for, Audrey?"
        mike.say "Take off your panties, get on this desk and spread your legs!"
        show audrey flirt
        "To make my point, I push the closest pile of papers off of the desk."
        "They go spilling onto the floor, landing a little way from where Audrey is standing."
        "For a moment I don't think that she's going to do it, that I've pushed her too far."
        "But then something seems to click inside of Audrey's head and she rushes to obey."
        "I stand up from my chair, pushing over more of the pile of paper to make room for her."
        "All the time Audrey is pulling down her panties."
        "She kicks them aside as she clambers onto the desk."
    menu:
        "Doggy" if hero.sexperience >= 20:
            call audrey_fuck_office_doggy from _call_audrey_fuck_office_doggy
        "Cowgirl":
            call audrey_fuck_office_cowgirl from _call_audrey_fuck_office_cowgirl
    $ hero.cancel_activity()
    return

label audrey_event_07:
    if audrey.love.max < 140:
        $ audrey.love.max = 140
    show audrey photocopy text kiss
    "I didn't really notice the photocopy at first, as it was just sitting there atop my already teetering 'in pile' when I walked into the office and sat down at my desk."
    "In fact, I'd switched on my desktop, checked my voice messages and opened most of the mail that looked in any way interesting before my eyes drifted in its direction."
    "The first thing that catches my attention was the fact that I'm looking at an A3 sheet of paper that had the unmistakable sheen of having come out of the photocopier."
    "Most of the time, things get scanned these days, so there's not much need to use the copier, and sheets of that size are even rarer."
    "But when I actually look down and took note of just what the image is on the glossy paper, I immediately snatch it up for fear of someone walking in and seeing it."
    "There, on the paper, was the unmistakable, life-sized image of a backside, pressed up against the glass of the copier."
    "It's full and feminine in shape, wearing sexy knickers."
    "There's the print of a kiss in red lipstick on one of the buttocks."
    "Written in marker on the other is 'Guess Who?', the writing exaggerated so as to hide it's owner's usual hand."
    "It's not either Valentine's day or April Fool's Day, so this has more of the air of a generally smutty prank about it."
    if Person.is_not_hidden("lavish"):
        hide audrey photocopy
        show lavish blush
        "I risk a glance up from the image of the backside, and find myself staring right into the wide, confused eyes of Lavish."
        "She has a pad and pencil in her hand, and I recall now that I asked her to be available to take the dictation of a letter before I left the office last night."
        "The shocked expression on her face makes it clear that she's already seen just what the photocopied image is."
        "Lavish continues to stare at me, like a proverbial deer in the headlights, clearly waiting for some kind of explanation."
        mike.say "Now, Lavish - let's not overreact, shall we?"
        "She glances over her shoulder at the photocopier in the corner of the outer office and then back at the image."
        "Unconsciously, her hand strays to her own ass."
        lavish.say "But...[hero.name]...someone must have..."
        mike.say "Yes, Lavish - someone obviously thought it'd be funny to sit on the photocopier and...well, copy their backside..."
        "She looks at me now, clearly beginning to wonder how such a thing came to be on my desk, let alone dedicated to me with a signature in lipstick."
        lavish.say "Mister [hero.family_name]...did you..."
        menu:
            "Deny responsibility":
                $ lavish.love += 1
                mike.say "No...no, Lavish...I did not ask anyone to do this for my own gratification!"
                mike.say "There are strict rules and guidelines in the HR handbook that forbid anything of the kind..."
                "I try to calm myself down a little."
                mike.say "...as I'm sure you're aware."
                "Lavish just continues to stare at me with those huge, innocent eyes of hers."
                "She's not challenging me on my explanation, but she's not exactly jumping to agree with me either."
                mike.say "No, this is clearly someone's idea of a a joke...and a sick one at that!"
                mike.say "Maybe you could help me to identify the culprit?"
                "Lavish looks at me sideways."
                lavish.say "Let me get this straight, Mister [hero.family_name]."
                lavish.say "What you're saying is that you want me to try and identify one of my colleagues from a copy of their buttocks?"
                mike.say "Erm...maybe not in so many words, Lavish."
                mike.say "How about we limit your role to simply letting me know if you see anything suspicious?"
                lavish.say "Well, I'll be sure to sound the alarm if I see anyone else photocopying their backsides, Mister [hero.family_name]."
                "And with that, she mercifully turns and walks out of my office before I can dig an even deeper hole for myself to fall into."
            "Lead her on":
                $ lavish.love -= 10
                $ lavish.sub += 10
                "Well, I may not have, but what if I let poor, innocent little Lavish think that I did?"
                mike.say "Well, Lavish...I know that you're young, and probably very idealistic."
                mike.say "And believe me, all that woke stuff is great - in the world of social media and your college friends."
                mike.say "But this is the world of work, the REAL world."
                mike.say "And sooner or later, you have to learn that there are certain...favours, if you like."
                mike.say "These favours are the grease that keeps the wheels of commerce turning."
                mike.say "Do you know what I mean?"
                "Lavish swallows nervously, but she nods all the same."
                lavish.say "I...I think so, Mister [hero.family_name]."
                lavish.say "I think that you're saying you want me to do that for you."
                "She points a shaking finger at the photocopy on the desk."
                "I shake my head quickly."
                mike.say "No, Lavish - I'm not ASKING you to do anything."
                mike.say "I'm telling you that, if you chose, of your own volition and wholly without my coercion, to do certain things for my benefit."
                "At this, I glance briefly down at the image of the compressed buttocks for a moment."
                mike.say "Then I would, in turn, be inclined to bear them in mind, when it came time to make any decisions as to your future in this department."
                mike.say "Do you follow, Lavish?"
                "She nods hastily, smiling without it touching any other part of her face as she leaves my office."
                "And with that seed planted, all that I have to do now is find the culprit lurking out there to whom these buttocks belong."
        hide lavish
    else:
        "I risk a glance up from the image of the backside, looking through the glass of my office door and into the space beyond."
        "Who could have done this and left it here for me to find?"
        "Even worse, what if someone else had walked in here and found it lying on my desk?!?"
        hide audrey photocopy
    "Unless someone from another department is behind this, then there are only really three viable candidates to hand."
    "I see Aletta stride by, her face already looking like thunder, probably on her way to chew someone out."
    "Audrey is just sitting at her desk, openly checking her phone during office hours, seemingly without a care in the world."
    if Person.is_not_hidden("shiori"):
        "And Shiori is desperately piling up files on her own desk, as though she's trying to look busy."
    "I can only guess that whoever left this here for me to find is still wearing what can be seen in the image."
    "And that part of the thrill they're getting out of this is making me sweat over just who is behind it."
    "So, find the pantyhose, find the culprit."
    "It should be that simple, right?"
    "Wrong - of course not!"
    "It only takes a cursory glance around to confirm that, on this of all days, the three of them have chosen to wear almost identical black pantyhose to work!"
    "I can see that I'm not going to be able to solve this little mystery by just sitting here and scrutinising the image of the backside."
    "The fact that it's pressed up against the glass of the copier means that it really could belong to any of the three potential suspects."
    "And just in case you were wondering, it's a very nice ass indeed!"
    "I don't want you to hear all of this half-assed detective bullshit from me and think that I was doing it because the sight of the backside had upset me in any way."
    "I fully confess to taking some time out to appreciate it."
    "My concern was more for the sake of being drawn into someone's kinky games in the workplace and the possible repercussions for me in the future should this kind of thing become a habit."
    "And so, I was going to have to do some amateur sleuthing."
    $ photo_leave = False
    $ accuse_aletta = False
    $ accuse_shiori = False
    while not photo_leave:
        menu:
            "Accuse Aletta" if aletta.love >= 50 and not accuse_aletta:
                $ accuse_aletta = True
                "I fire off a short email to Aletta, asking if she had a moment to discuss something in my office, keeping things suitably vague."
                "Maybe choosing to confront her is a bit rash, but Aletta's always been forceful and upfront about things."
                "So if it is her, chances are she'll just up and admit it."
                "But then again, if not..."
                "A few minutes later, Aletta comes striding into my office, an expectant look on her face."
                show aletta angry
                aletta.say "Couldn't you have just explained whatever it is you want to discuss in your email?"
                aletta.say "You might not be particularly busy this morning, but I can assure that I am!"
                mike.say "Well, Aletta...thing is, this isn't really the kind of thing I can discuss in an email."
                "She raises one eyebrow, showing that if she's not impressed, at least she's a little intrigued."
                mike.say "You see, I found this on my desk this morning."
                "I hold up the image for Aletta to see, and at first she squints at it, as though she's not sure exactly what she's looking at."
                aletta.say "Is that what I think it is?"
                mike.say "It's an ass, Aletta - the question is, just who's ass is it?"
                aletta.say "Well, I can't say that I recognise it myself..."
                "Aletta trails off as she suddenly realises the inference that I'm making."
                aletta.say "[hero.name]...you're not seriously suggesting that I..."
                mike.say "I'm not suggesting it was you, Aletta."
                mike.say "Just giving you a chance to admit it...if it is you, that's all."
                "Aletta's expression darkens instantly and she crosses her arms over her chest."
                aletta.say "How dare you!"
                mike.say "What did I do, Aletta?"
                mike.say "I didn't accuse you of anything - but you have black tights on and a shapely butt!"
                mike.say "What was I meant to think?"
                aletta.say "This conversation is over!"
                aletta.say "And if you have any further complaints of this nature, then I suggest that you go through the correct channels and contact HR!"
                $ audrey.love -= 5
                $ aletta.love -= 5
                "With that, Aletta turns on her heel and storms out of my office."
                hide aletta
            "Accuse Shiori" if Person.is_not_hidden("shiori") and shiori.love >= 50 and not accuse_shiori:
                $ accuse_shiori = True
                "I put a call through to Shiori's desk phone, just asking her to come into my office, nothing more."
                "Sure enough, less than a minute later, Shiori comes hurrying in to see what it is that I want."
                show shiori
                shiori.say "Hello [hero.name], good morning - what was it that you wanted?"
                "In a way, this should be far easier than confronting either Aletta or Audrey."
                "But I still need to remember that, under her innocent exterior, Shiori still likes to be manipulative in her own unique ways."
                "I hold up the image, waiting for its significance to register on her face."
                show shiori blush
                shiori.say "Oh...oh dear...[hero.name]!"
                "I nod in agreement, thinking that Shiori has easily grasped what the issue is here."
                mike.say "I think you can see my problem, Shiori, can't you?"
                "Shiori nods slowly, glancing back over her shoulder in the general direction of the photocopier."
                "So, it was her after all!"
                mike.say "I think you already know what we have to do in order to remedy this situation, don't you, Shiori?"
                "She gulps and nods, clearly a little scared of what lies ahead."
                shiori.say "I...think so..."
                mike.say "Well, what are you waiting for?"
                mike.say "No time like the present!"
                shiori.say "Really, [hero.name]...right here and now?"
                mike.say "Erm...why not?"
                shiori.say "Because people will see me!"
                shiori.say "Can't I put my bottom on the photocopier when everyone else has gone home for the night?"
                "She can clearly read from my expression that there's been a misunderstanding."
                shiori.say "Oh...I thought you wanted me to..."
                mike.say "No, Shiori...I thought that you already..."
                "Shiori puts her hand in front of her mouth and giggles, I suspect both at the miscommunication and my evident resulting embarrassment."
                shiori.say "Oh no, this can't be my bottom - I don't own any panties as wild as those!"
                shiori.say "All of mine are soft, and white and..."
                mike.say "Alright, alright, Shiori...I get the picture!"
                $ audrey.love -= 5
                $ shiori.love += 5
                "Still giggling to herself, Shiori leaves me alone with the image of the mystery backside once more."
                hide shiori
            "Accuse Audrey":
                $ photo_leave = True
                "It's with a growing sense of dread that I call up Audrey's desk phone and ask her to step into my office."
                "I see her give her habitual shrug and grunt of annoyance at being interrupted at work by work."
                "But she gets up and comes over all the same."
                "I should have guessed right from the start that this kind of trick has Audrey's name written all over it."
                "What's not so clear to me is just why it bothers me so much and I'm almost afraid of confronting her."
                "Is it about the power dynamic, or am I just scared of admitting that there's something maddeningly sexy about the whole thing?"
                show audrey
                if Person.is_not_hidden("shiori"):
                    "Where Aletta would have strode in and Shiori scuttled as meekly as a mouse, Audrey saunters as though we're casual acquaintances, rather than superior and subordinate."
                else:
                    "Where Aletta would have strode in, Audrey saunters as though we're casual acquaintances, rather than superior and subordinate."
                audrey.say "What's up, boss man!"
                mike.say "Audrey, would it kill you to show me even the smallest degree of respect?"
                mike.say "Maybe call me 'Boss' or even 'Mister [hero.family_name]' every once in a while?"
                audrey.say "I don't know...it might...so I think, why take the risk?"
                "I shake my head, hating that she makes me sound more like a bitter old man every time we have this little talk."
                mike.say "Anyway...that's not what I called you in here to discuss."
                mike.say "This is..."
                "I slide the image across the top of my desk towards Audrey."
                "It's turned so that she can read the words written upon it with ease."
                "At the sight of it, she smiles wickedly, giving me all of the proof that I need to know that she really is the culprit."
                "Without saying another word, Audrey turns and proceeds to sit down on the image, lining her ass up with the one on the paper."
                show audrey blush
                audrey.say "If the shoe fits - or maybe in this case, the butt-plug!"
                mike.say "So it was you - you admit it!"
                audrey.say "Phfft...of course it was me!"
                if Person.is_not_hidden("shiori"):
                    audrey.say "Shiori's too much of a little mouse and Aletta couldn't have gotten her massive horse's ass on there for the pole she's got stuck up it!"
                else:
                    audrey.say "Aletta couldn't have gotten her massive horse's ass on there for the pole she's got stuck up it!"
                "I really should reprimand her for speaking about her colleagues in such a derogatory manner."
                "But right now, I'm more interested in the matter at hand."
                mike.say "Would you mind telling me why you felt the need to do it?"
                "Audrey's got her hands on the desktop now, leaning backwards as she looks at me over her shoulder."
                audrey.say "Oh, I just thought it might keep you from getting chewed out by HR, that's all!"
                mike.say "What...what do you mean by that?!?"
                audrey.say "Oh, don't play the innocent with me - I've seen how you look at me!"
                show audrey happy
                audrey.say "I figured that if you had this to keep you occupied, it might stop everyone else from noticing how much time you devote to staring at the real thing!"
                $ audrey.love += 5
                "With that, she kicks her legs and stands up from the desk, making sure to bend over a little as she does so."
                "As she straightens up, Audrey runs her hands up her body and sighs in a suggestive manner."
                "A second later and she's gone, leaving me speechless, confused and more than a little aroused."
                hide audrey
            "Investigate" if not accuse_shiori and not accuse_aletta:
                $ photo_leave = True
                "I decide that it'd be a bad idea to call any of the women into my office and present them with my accusations."
                "If they turn out to have a valid alibi, then not only would I end up with proverbial egg on my face, the whole thing would be out in the open too."
                "I slide out of my office door, trying as best I can to appear casual."
                if not shiori.hidden:
                    show shiori
                    "The first girl that I come across is Shiori, ploughing through the files on her desk in the usual determined and yet incompetent manner she possesses."
                    mike.say "Erm...Shiori?"
                    "Her head bobs up with a suitably cute and eager smile plastered across it."
                    shiori.say "Yes, [hero.name] - what can I do for you?"
                    mike.say "I need the...Zimmerman file...that's it - can you look the Zimmerman file out for me?"
                    "Shiori nods and is instantly on her feet and heading for the last and lowest drawer of the filing cabinets."
                    "I follow discretely as she begins to bend down, then gets on her knees in order to reach to the very back of the drawer."
                    "Her skirt isn't exactly long, but it's still not riding up nearly enough to let me see her panties yet."
                    mike.say "That's great, Shiori - keep on digging in the back until you find it!"
                    "Finally she leans that little bit further and I can see..."
                    "...the very edge of her neat, pristine, white panties."
                    shiori.say "Here you go, [hero.name]!"
                    mike.say "What...oh, right...just put it on my desk, Shiori."
                    $ shiori.sub += 5
                    hide shiori
                    "I hurry off, leaving Shiori looking a little puzzled and rather deflated."
                show aletta
                "I catch up with Aletta in the lift lobby, and before I can even speak to her, I notice that she's looking agitated."
                mike.say "Hey, Aletta - what's up?"
                aletta.say "What...oh, hello [hero.name]."
                aletta.say "Ah, it's nothing really - I just lost an earring on my way into the office this morning."
                aletta.say "The pair had some sentimental value."
                mike.say "Sentimental...really?"
                "Aletta frowns at my comment."
                aletta.say "Yes, sentimental - I might be professional when it's appropriate, but I'm not made of ice!"
                "At times, she could have fooled me."
                "Thinking as quickly as I can, I point to the far corner of the room."
                mike.say "What's that over there, something catching the light?"
                "Aletta rolls her eyes at me, but as she's already stated the sentimental value of the missing earring, she can hardly refuse to investigate."
                "Which means in order to do so, she has to bend down as far as possible."
                "I follow her into the corner, straining to see the first sign of her underwear as her skirt begins to ride up."
                "At first I don't think that I can see anything, but then I realise she has on a pair of panties in a matching shade of black to her tights."
                aletta.say "No, that's not it!"
                $ aletta.sub += 5
                "I manage to stand up a mere second before Aletta does, and she eyes me suspiciously, but then shakes her head and walks back to call a lift."
                hide aletta
                if not shiori.hidden:
                    "Two down and one to go - so it must be Audrey!"
                else:
                    "It must be Audrey!"
                "Asking around the office lets me know that she was last seen making for the stationary cupboard."
                "When I arrive, I find the door ajar."
                "Checking that no one else is around, I sneak inside."
                show audrey
                "Almost instantly, I see Audrey crouched in the far corner, struggling to reach something buried on a low shelf."
                "She still hasn't shown any sign of noticing me, so I creep closer and hide behind a shelf to watch."
                "Audrey leans further and further forwards, paying no attention to the fact that her barely acceptable skirt is already almost at the top of her thighs."
                "I lean forward myself, watching as it begins to creep up and over her buttocks."
                "Soon I can see the entire curve of Audrey's ass, and my dick starts to get stiff at the sight."
                "Her legs are so shapely and perfect beneath those black pantyhose that I almost forget why I'm actually doing this."
                "Finally I can see the red fabric of her panties that proves she's the culprit."
                "I could sneak out now and confront her with the evidence later."
                "But instead I remain rooted to the spot, watching as her skirt rises even higher."
                "By now, Audrey's skirt is fully hiked up around her waist, leaving her ass exposed to view."
                "She must be close to reaching what she's after, as she begins to drag herself forwards and then fall back again repeatedly."
                "All the time she's making these small, intense sighing and gasping noises, as if the effort is taxing her physically."
                "At my best guess, it takes me perhaps five minutes of watching this, sweating, fearing discovery and feeling my cock stiffen still further, before I realise that she's not looking for anything at all."
                show audrey happy
                mike.say "Very clever, Audrey...you can come out now."
                "I watch as Audrey eases herself backwards and out of the hole she had cleared for herself amongst the boxes of stationary."
                "She's smiling, clearly pleased with herself, and none too quick to pull her skirt back down either."
                audrey.say "Why boss, whatever do you mean?"
                mike.say "You know full well what I mean - I have something in my office that belongs to you!"
                show audrey blush
                $ audrey.sub += 5
                audrey.say "Oh, you feel free to hang on to it - maybe it'll help you keep the image fresh in your mind!"
                hide audrey
    "And with that, I'm alone again."
    "The worst thing is that I now have to get through the rest of the day with all of this still fresh in my mind."
    return

label audrey_event_06:
    if audrey.love.max < 120:
        $ audrey.love.max = 120
    $ audrey.flags.nodate = False
    $ audrey.unhide()
    "I haven't honestly calmed down or stopped ruminating over it since the incident happened the other night."
    "How I actually managed to get home from a restaurant where Audrey had walked out on me with cum-stained pants..."
    "Well, that's another story and doesn't bear repeating here."
    "What really matters is that this is the first chance I've had to confront her about it and demand an explanation."
    "Was planning on sending her a firm email or leaving a message on her phone telling her that I wanted her in my office first thing."
    "But she almost leaps out from behind her desk as soon as she sees me walk in and close my office door behind me."
    play sound door_knock
    "I can hear her knocking even before I've managed to sit down."
    "And so I don't, instead choosing to lean against my desk, arms crossed."
    mike.say "Come in!"
    show audrey with moveinleft
    "The door opens a second later, as Audrey slips in and then closes it behind her."
    audrey.say "Before you say anything - no, I don't know what gets cum stains out of a pair of cheap pants!"
    show audrey joke
    "She sniggers almost as she says this, not letting me get a single word in before the insults start to fly from her lips."
    mike.say "Audrey, I really don't..."
    show audrey mock
    audrey.say "Oh, I'm sorry - were they your favourite pair?"
    audrey.say "The one's that were so shiny you could see your face in them?"
    audrey.say "Don't worry, I'm sure the thrift store will have another pair in some day!"
    show audrey normal
    "I never really understood the way people described a red mist descending over them."
    "But meeting Audrey really cleared that one up for me rather neatly."
    "It's almost like I suddenly can't actually hear what she's saying any more."
    "I can see her mouth moving, and from way she's standing, I know she's still insulting me."
    "There's just nothing else apart from the unshakable feeling that I want her to stop."
    "I just know that I want her to shut up - and I don't care how it happens."
    "I just want the words to stop coming out of her filthy, disgusting mouth..."
    menu:
        "Keep calm":
            $ audrey.love -= 20
            $ audrey.sub -= 20
            "In that moment, I could as easily have seen myself doing something to harm Audrey as I could doing nothing at all."
            "It honestly felt like a simple choice between two alternatives, with no care for the consequences of either."
            "A cold sweat breaks out on the back of my neck as I realise just how close I came to lashing out at her."
            mike.say "I...I don't care, Audrey."
            audrey.say "What?"
            "She cocks her head on one side, genuinely surprised at being stopped in her tracks."
            mike.say "I said I don't care, Audrey - about what happened the other night, about what you're saying to me now, none of it."
            mike.say "What I'd like you to do is get out of my office."
            mike.say "RIGHT NOW!"
            "Audrey looks at me with a mixture of amazement and contempt on her face."
            "But, to my great relief, she finally does as she's told."
            hide audrey with moveoutleft
            "She might have said something on the way out, but I ignore it and deliberately look at the wall until she's gone."
        "Lash out" if hero.fun <= 5 or hero.sexperience >= 5:
            show audrey surprised
            "My hand moves before I realise what I'm doing, and far faster than I thought I was capable of moving."
            show audrey scared
            "Audrey's words are choked off raggedly and her eyes bulge with shock and what looks like genuine fear."
            "Simply relieved to have her stop speaking, I feel a similar sense of shock as I it dawns on me just why she shut up."
            "As reality comes back to the fore, I see my own hand clamped firmly around Audrey's throat, squeezing hard."
            "For a moment, I genuinely can't make sense of what I'm doing, and so I keep on doing it."
            "In the end, it's Audrey's expression that makes me snap out of it."
            show audrey blush
            "I can see that beneath the real fear, there's a glimmer in her eyes that belies a deeper emotion."
            "This only starts to make sense when I notice that she's not struggling against me in any real sense."
            "In fact, my grip doesn't feel strong enough to choke the life out of her now that I can feel my limbs once more."
            "So the reddening of her cheeks and the sweat starting to bead at her temples must be on account of something else entirely."
            "I let go of her with some considerable effort, and she staggers to my desk."
            "Once there, Audrey takes a series of deep, rasping breaths as she eyes me in a disturbing manner."
            "Shouldn't she be mad, screaming for help or threatening me with, well...anything right about now?"
            "Instead, she almost looks like her eyes are eating me up."
            mike.say "Audrey...I'm sorry...I don't know what came over me..."
            $ audrey.sub += 2
            $ audrey.love += 2
            "In response, her smile is, if anything, a bit unnerving."
            show audrey mock
            audrey.say "Heh...heh...I do, [hero.name]..."
            audrey.say "You just accidentally behaved like a real man for a change..."
            audrey.say "But don't worry...you're already turning back into a little pussy..."
            "She lets out a cough before she can go on."
            audrey.say "I can practically hear your cock withering up back inside of you right now."
            audrey.say "You should see if one of the guys in the office wants to fuck the puckered little hole it leaves behind and call you his bitch!"
            menu:
                "Restrain myself":
                    $ audrey.love -= 10
                    $ audrey.sub -= 10
                    "I shake my head, not knowing if I should be more ashamed at myself for what I just did."
                    "Or else more sorry for Audrey that she wants to provoke more of it."
                    mike.say "I'm sorry, Audrey - but I'm not going to rise to your barbs again."
                    mike.say "I understand if you want to take this up with human resources."
                    mike.say "But I do feel that there are more than a few instances of your own behaviour that would interest them too, were I to bring them up."
                    "Audrey looks for a moment as if she's about to begin another tirade."
                    "But then something just seems to go out of her all of a sudden, and she shakes her head as she makes to leave."
                    hide audrey with moveoutleft
                    "She says more before she's out of the door, but I tune her out and then collapse into my chair."
                    "I still can't believe she made me mad enough to lash out like that."
                    "Or that she really seemed to want to provoke me further!"
                "Give her what she deserves" if hero.fun <= 5 or hero.sexperience >= 10:
                    $ audrey.love += 3
                    $ audrey.sub += 3
                    call audrey_fuck_office_desk from _call_audrey_fuck_office_desk
    hide audrey
    return

label audrey_event_05:
    play sound cell_vibrate loop
    "My mobile vibrate and I look down to see that the call is from Audrey, which means I really have to try to finish groaning before I answer it."
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Audrey")
    if not result:
        $ hero.cancel_event()
        $ audrey.love -= 5
        return
    mike.say "Hey, Audrey - what do you want now?"
    audrey.say "My, my - who's a sourpuss today?"
    audrey.say "Keep that up and I won't tell you about the nice surprise I have planned for tonight, [hero.name]!"
    "I sigh in resentment and shake my head."
    mike.say "Okay, Audrey - what have you got planned?"
    audrey.say "You are inviting me to that new restaurant that just opened up in the city."
    menu:
        "No":
            mike.say "Nah, Audrey - thanks for the offer, but I think I'll take a rain-check on this one."
            audrey.say "Huh...whatever, [hero.name] - your loss!"
            "And with that, she cuts me off dead."
            $ hero.cancel_event()
            $ audrey.love -= 5
            return
        "Yes":
            "I know I shouldn't, but I really do like the look of that place..."
            mike.say "Okay, Audrey, I'll come along."
            audrey.say "Great, so it's a date then!"
    "As I put my phone down again, I'm already wondering if I've made the right decision."
    "Or just another terrible mistake that happens to involve Audrey."
    $ game.pass_time(1)
    scene bg restaurant
    show audrey eat date
    with fade
    "Even though I am dressed in a fancy suit that I would normally be uncomfortable in, I don't even notice it as I look toward Audrey."
    "With it being a Friday evening, the lighting lowered, and it is nice and warm in the restaurant, this date is much more cozy than I expected it to be."
    "I expected it to be stuffy and boring since she insisted on a classy restaurant."
    "I can't help but smile as I watch her reading the dessert menu in her stunning black dress that fits her so well."
    "I'm imagining her stripped out of it though, laid out on my couch in front of a fireplace as we make love when she glances up and catches me looking."
    audrey.say "What are you thinking?"
    menu:
        "Tell her":
            mike.say "I'm imagining what I want to do to you later."
            $ audrey.love += 1
        "Tease her":
            mike.say "Wouldn't you like to know."
            $ audrey.sub += 1
    show audrey eat handjob
    "She gives me a mischievous look and scoots herself closer to me."
    "At first she lays her head on my shoulder and raises her hand on my leg."
    show audrey eat transparent
    "I don't even care or think about her getting makeup on my shirt."
    "I just enjoy her being closer to me and lean my head on top of hers closing my eyes when I suddenly feel her hand sliding up my leg under the table."
    show audrey eat handjob close pleasure dick
    "My eyes fly open and I straighten back up in surprise as her hand wraps around my dick and pull it out of my pants."
    mike.say "Audrey, what are you doing?"
    show audrey eat open
    audrey.say "What do you think I am doing?"
    mike.say "This is supposed to be a special night."
    audrey.say "Oh don't worry, it will be."
    show audrey eat speed with hpunch
    "She starts to rub me off and I fight with myself about whether I should let her do it or not."
    menu:
        "Make her stop":
            "I quickly grab her hand and look her in the eyes."
            show audrey eat -pleasure
            mike.say "Not right now. Save that for later. We are in a classy place and you should act like it young lady."
            "She starts to pout and gets out of my grip only to quickly reach for my dick again."
            "I grab her wrist again and tell her."
            mike.say "I said no. Unless you want punished in front of everyone, you better stop."
            "She stops trying and goes back to her meal with a pout."
            show audrey eat eating solid -dick
            audrey.say "Fine, but I better get that wine I like, the expansive kind."
            $ audrey.love -= 4
            $ audrey.sub += 2
            "I chuckle and kiss her neck."
            mike.say "Anything for you my sweet."
        "Let her keep doing it":
            "I can't find a reason to make her stop as it starts feeling good, better than good, so I don't say anything and causally move to give her more access to my crotch."
            "I try to not let it show on my face what she is doing, and have to act like I am clearing my throat to hide a moan."
            "Luckily everyone else is so into their partner no one notices us and our activities."
            mike.say "Ohhh... Audrey... Mmm. You're... you're so... gooood to me."
            "It is a struggle to form words as she picks up the pace and I have to grip onto my knee with one hand and the table cloth with the other."
            "It gets increasingly hard to keep my breathing in control and I want so badly for her hand to be rubbing off my bare cock but we can't do that here."
            "It will have to wait for later."
            show audrey eat kissing close
            $ audrey.flags.kiss += 1
            "She leans forward and kisses my lips slowly, then gives it a little bite and I start to lose focus."
            "A small moan escapes my lips."
            "I don't care at this point if anyone hears but I hear her laugh."
            show audrey eat open
            audrey.say "Does that feel good, [hero.name]?"
            "I give her a look because I don't trust myself to form words right at that moment."
            show audrey eat eating pleasure
            "Just then the waiter comes with our food and I panic a little and expect her to let go, but she doesn't stop."
            "She keeps rubbing me off while talking casually to the waiter and I start to sweat."
            "It is all I can do to not give it away, and Audrey is expertly managing to make it look like we are just holding hands under the table."
            show audrey eat solid
            "Waiter" "And there you go. If you need anything else just let me know."
            audrey.say "Of course, thank you."
            "Audrey talks so causal if I were the waiter I never would have guessed what was going on."
            "It turns me on and makes me lust for her even more."
            audrey.say "You better start eating or that waiter is going to come over here wondering what is wrong with your food, and you are already looking a little red."
            "I realize she is right and look for the waiter, realizing he keeps glancing this way."
            show audrey eat close handjob
            "I quickly pick up my fork but only manage to take a couple bites."
            "This is impossible!"
            "I am hungry for something but it isn't food."
            "This woman is driving me mad."
            "I finally just leaned into her neck like I am whispering sweet things into her ear, but really I am whimpering and begging her to stop."
            mike.say "Audrey, enough... I can't take much more."
            "That just makes her take a stronger grip and start stroking harder."
            "I grunt and grab hold of her arm."
            show audrey eat transparent
            mike.say "Audrey-I'm going to-."
            show audrey eat open with vpunch
            "Before I can say anything I cum as a tremor goes through my body."
            show audrey eat -speed with vpunch
            "I close my eyes tight and have to lean onto her shoulder to not fall out of my chair, still holding onto her wrist maybe a little to tight as I hear her laugh at me."
            show audrey eat alone solid
            "When I finally manage to calm back down and catch my breath Audrey is licking her fingers clean before she stands up."
            mike.say "Where are you going?"
            audrey.say "Home. I'm a bit tired."
            "With a smirk she walks away just as the check comes."
            "I look at the bill and then down at my pants and see the large stain on the front of them."
            "There is no way I am walking out of here without someone noticing."
            "And Audrey is already far gone so I don't even have her to walk in front of me to hide it."
            "She isn't going to get away with this one once we got back home."
    $ audrey.flags.nodate = True
    $ audrey.hide()
    $ game.pass_time(4)
    $ hero.fun -= 5
    $ hero.energy -= 2
    return

label audrey_kiss_me:
    call audrey_greet from _call_audrey_greet_5
    show audrey
    "When Audrey begins her usual routine of teasing and invading my personal space, I let her."
    hide audrey
    show audrey kiss with fade
    $ audrey.flags.kiss += 1
    "And it's only when she's leaned in and tried to kiss me for perhaps the hundredth time, that she suddenly realises she's succeeded."
    "Before she can react, I increase her surprise tenfold my returning the kiss."
    "Gently and falteringly, we start to feel each other out from this strange and chance meeting."
    "Audrey seems to become almost timid now, as if she's been exposed and unnerved by getting the very thing that she's always claimed to want from me."
    "But she soon recovers sufficiently for the kiss to go from being awkward and unsure to easier and ever more enjoyable."
    hide audrey kiss with fade
    return

label audrey_preg_talk:
    show audrey annoyed
    $ audrey.flags.toldpreg = True
    "I can't help looking sideways at Audrey, studying her with real curiosity."
    "And at that same time, I'm hoping that she doesn't catch me doing it too!"
    "I'm sure that there's something on her mind that's pretty serious."
    "I figure this because she's being quiet, which is unusual for her."
    mike.say "Audrey..."
    mike.say "Are you okay?"
    "Audrey looks up in surprise, her eyes wide."
    audrey.say "Huh?"
    audrey.say "Oh...it's nothing, [hero.name]."
    audrey.say "I was just thinking, that's all."
    "I raise my eyebrows, trying to get more out of her."
    mike.say "Anything I can help with?"
    audrey.say "Yeah, maybe you can."
    audrey.say "What do you think of pregnant women?"
    "The question seems to come out of nowhere."
    "And I find myself shrugging as I try to answer it."
    mike.say "I don't know, Audrey."
    mike.say "Maybe that they look like it's exhausting?"
    "Audrey shakes her head, letting me know that's the wrong answer."
    audrey.say "No, not like that!"
    audrey.say "I mean do you think they can be hot?"
    audrey.say "You know, are they sexy?"
    menu:
        "Agree":
            mike.say "Well, yeah..."
            mike.say "It's a bit weird, I know."
            mike.say "But I do think they're kind of sexy!"
            audrey.say "Ah..."
            audrey.say "That's good..."
            "I see an awkward, almost pained expression appear on Audrey's face."
            "But when she looks at me, it's with a serious determination in her eyes."
            show audrey normal
            audrey.say "Because I'm pregnant."
            audrey.say "And it's yours."
            mike.say "Are you serious, Audrey?!?"
            audrey.say "Of course I am!"
            audrey.say "I wouldn't joke about something like this."
            "Audrey pauses to suck in a deep breath."
            audrey.say "And I want to keep it too."
            menu:
                "Agree":
                    "For a moment, I can't help wondering about what Audrey just asked me."
                    "If she would have said the same thing had I answered in the negative."
                    "But then I dismiss the thought as nothing more than me overthinking it."
                    "What does any of that matter when we're going to have a baby together?"
                    mike.say "So do I, Audrey."
                    mike.say "This is amazing - we're going to be parents!"
                    "Audrey throws her arms around me and I return the gesture."
                    "And it doesn't take long for me to notice she's almost clinging to me."
                    show audrey blush
                    audrey.say "Ah, [hero.name]..."
                    audrey.say "You promise that you'll still want me?"
                    audrey.say "You know - when I'm the size of a cow?"
                    mike.say "I already said so, Audrey."
                    mike.say "You know that I'm crazy about you."
                    mike.say "And you know I love pregnant bellies too."
                    mike.say "So you're going to be my perfect woman!"
                    "Audrey chuckles, her head buried against my chest."
                    audrey.say "You better promise, [hero.name]."
                    show audrey flirt
                    audrey.say "You better fuck me when I look like a hot Buddha!"
                    $ audrey.love += 10
                    $ audrey.sub += 5
                "Disagree":
                    "A thought occurs to me, even as I'm reeling from the news."
                    "Why in the hell was Audrey asking me about pregnant bellies just now?"
                    "Surely she didn't say she wanted to keep it because of my answer?"
                    "Surely she wouldn't decide just based on that?"
                    mike.say "Audrey, be honest with me."
                    mike.say "Would you have wanted to keep it if I said I didn't like pregnant bellies?"
                    mike.say "Because that's not how you make decisions like this!"
                    show audrey annoyed
                    "Audrey suddenly looks evasive, like she'd rather be somewhere else."
                    audrey.say "I...I don't know..."
                    audrey.say "That's part of it, [hero.name]."
                    audrey.say "I didn't think you'd want me if I were the size of a cow!"
                    mike.say "I'm sorry, Audrey."
                    mike.say "But I can't start a family for the sake of you feeling sexy!"
                    mike.say "I...I think we need to rethink keeping the baby."
                    audrey.say "Okay..."
                    audrey.say "I guess..."
                    $ audrey.love -= 20
                    $ audrey.unpreg()
        "Disagree":
            mike.say "Urgh..."
            mike.say "I've got to be honest, Audrey."
            mike.say "I think pregnant bellies are kind of gross!"
            $ audrey.love -= 10
            $ audrey.sub -= 5
            show audrey sad
            audrey.say "Oh..."
            audrey.say "Okay..."
            "I see an awkward, almost pained expression appear on Audrey's face."
            "But when she looks at me, it's with a serious determination in her eyes."
            show audrey angry
            audrey.say "That really sucks, [hero.name]."
            audrey.say "Because I'm pregnant."
            audrey.say "And you're the father!"
            mike.say "Are you serious, Audrey?!?"
            audrey.say "Of course I am!"
            audrey.say "I wouldn't joke about something like this."
            audrey.say "And before you ask, I don't want to keep it either!"
            menu:
                "Agree":
                    "I feel like I'm reeling from one blow as the next lands."
                    "In one breath Audrey tells me that she's pregnant."
                    "And in the next she also tells me that she wats a termination!"
                    "I don't feel like I have any choice but to agree with her."
                    mike.say "Fucking hell, Audrey!"
                    mike.say "If that's how you feel..."
                    audrey.say "I already said it was, [hero.name]!"
                    audrey.say "Don't even try to talk be out of it."
                    mike.say "I...I wasn't, Audrey."
                    mike.say "I promise I wasn't."
                    audrey.say "Good - then it's decided."
                    mike.say "I guess so..."
                    $ audrey.love -= 20
                    $ audrey.unpreg()
                "Disagree":
                    "The mention of Audrey being pregnant snaps me out of it."
                    "Making me realise that she's talking about my kid here."
                    "That and the fact she just said she wants a termination."
                    "I'm involved in this thing too, damn it!"
                    mike.say "Hold on one fucking second, Audrey!"
                    mike.say "If you're having my kid, I get a say in what happens too."
                    mike.say "Where do you get off just telling me you're getting rid of it?"
                    "Audrey curls her lip and crosses her arms over her chest."
                    "Which means she's getting ready for a fight."
                    audrey.say "What do you care, huh?"
                    audrey.say "You're the one that just told me pregnant bellies are a turn-off!"
                    "I find myself shaking my head in amazement."
                    mike.say "Jesus, Audrey."
                    mike.say "That's not the same as saying I don't want to keep my kid!"
                    mike.say "And for the record, I'm not going to leave you over this either."
                    mike.say "And that's because I love you!"
                    show audrey awkward
                    "Audrey stares at me, her eyes wide with surprise."
                    audrey.say "I...I do too, [hero.name]."
                    audrey.say "Love you, that is..."
                    mike.say "Okay, now we've settled that - can we talk about this?"
                    mike.say "I'm sure we can work it out."
                    show audrey normal
                    audrey.say "Okay, [hero.name]."
                    audrey.say "Let's talk..."
    return

label audrey_event_01b:
    "All I wanted to do was head down to the pub to unwind after a long, stressful day."
    "You know, just sink a couple of beers and forget all about my problems for a while?"
    "But as soon as I walk into the place, I recognise a couple of faces almost instantly."
    show audrey at left with moveinleft
    "Firstly there's Audrey, a girl that works in the same office as me."
    "I don't really know her that well, and she always seems a little spikey to me."
    show audrey at center with move
    "So we just kind of nod and smile at each other, exchanging awkward waves as we pass."
    hide audrey with dissolve
    show ryan casual smile at right with moveinright
    "But a moment later I see the second person that I know, and it's even more awkward."
    "Ryan lurches out of the crowd, looking like he's already well on the way to being plastered."
    show ryan at left with move
    "Luckily for me, he seems more interested in making it to the bar."
    "So with a sigh of relief, I manage to slip by without him seeing me."
    "As far as I know he's still steaming from me telling Sam all about his cheating."
    "And the last thing I want right now is to be confronted and accused of ending his marriage!"
    hide ryan with dissolve
    "I settle down in a corner where I'm pretty sure Ryan won't notice me."
    "And, for a short while at least, it seems like my plan's working."
    "Ryan keeps on hanging around the bar, downing one drink after another."
    "He doesn't seem likely to move anytime soon, unless he falls down on his ass!"
    "But all of that changes a short while later, much to my dismay."
    "The first thing I notice is the sound of raised voices at the bar."
    show audrey ryan flirt with dissolve
    "And I recognise them as belonging to Ryan and Audrey."
    "Ryan sounds slurred and surly, just as I'd expect."
    "But Audrey sounds more than a little pissed."
    "And the volume seems to be rising by the second!"
    ryan.say "H...hey...HEY!"
    ryan.say "I asked you a question..."
    ryan.say "I asked you a damn question!"
    audrey.say "Yeah, you did."
    audrey.say "And I told you to get lost!"
    "I see Ryan visibly prickle at the way Audrey's talking to him."
    "He leans over her, trying to use his height to intimidate Audrey."
    ryan.say "I don't like being spoken to like that!"
    ryan.say "You should be nicer to someone like me..."
    ryan.say "Nicer to a guy that's being nice to you!"
    audrey.say "Hah!"
    audrey.say "I saw you coming a mile off, buddy!"
    audrey.say "I've got a built-in radar for small-dick assholes like you!"
    "Ryan's eyes go wide at this last insult and he puffs himself up like a bull-frog."
    "Is he...is he actually going to make this physical?!?"
    "I know Ryan's an asshole - but surely he's not that big of an asshole?"
    menu:
        "Step in":
            hide audrey
            show ryan casual angry at left
            show audrey annoyed zorder 2 at right
            if audrey.love.max < 40:
                $ audrey.love.max = 40
            $ audrey.unhide()
            $ fight = True
            $ audrey.flags.greeted = TemporaryFlag(True, "day")
            "Before I know what I'm doing, I'm up and out of my seat."
            "I shove my way through the crowd of drinkers to reach the bar."
            "And then I insert myself between Audrey and Ryan."
            mike.say "Hey, Audrey!"
            mike.say "Did I introduce you to Ryan here?"
            "It's hard to tell which one of them is more surprised."
            "Both Audrey and Ryan take a step backwards."
            "Which is a relief for me, as it means there's space between them."
            mike.say "Ryan and I used to live together."
            mike.say "And we were pretty good friends too."
            mike.say "That is until I caught him cheating on his wife-to-be!"
            audrey.say "Eww!"
            audrey.say "What a fucking creep!"
            "Ryan's face has a thunderous look of rage on it by now."
            "And he spins me around to face him, eyes wide and crazy."
            ryan.say "Is this how it's going to be now, huh?"
            ryan.say "You popping up to talk shit about me everywhere I go?"
            ryan.say "Ruining every chance I have to hit on a girl?"
            ryan.say "Even a cheap little slut like this one?!?"
            audrey.say "HEY!"
            audrey.say "I heard that, creep!"
            ryan.say "Like I care!"
            "I put a hand on Ryan's shoulder, trying to steer him away from Audrey."
            with hpunch
            "And it works, as he looks down at it like I just rubbed shit on his shirt."
            ryan.say "Don't touch me..."
            "I sense him winding up and balling his fist before I see it."
            "And there's only a split-second before the punch connects..."
            if hero.fitness >= 90 or (hero.fitness >= 50 and hero.has_skill("martial_arts")):
                "But Ryan always talked a good fight, never able to back it up."
                "And right now he's more than halfway drunk too."
                show ryan casual angry zorder 2 at center with move
                with hpunch
                "So his punch is slow and clumsy to say the least!"
                "I can easily step to the side as he swings wildly."
                play sound punch_hard
                pause 0.2
                hide audrey
                show ryan fight punchryan at center, hshake
                pause 0.2
                with hpunch
                "And then plant a punch of my own on his chin for good measure."
                "Ryan lets out a grunt of pain and collapses against the bar."
                "If it weren't for the furniture saving him, he'd be on his ass."
                hide ryan
                show ryan casual angry zorder 2 at left
                show audrey annoyed zorder 1 at right
                ryan.say "Y...you bastard!"
                ryan.say "You broke my fucking jaw!"
                "By now the bar-staff have alerted the bouncers on the door of the pub."
                "And they appear a moment later to deal with the situation."
                "I make a show of holding my hands up and stepping away from Ryan."
                "I figure the whole thing was seen by multiple witnesses."
                "So there's no need to protest my innocence."
                "But Ryan doesn't seem to feel the same way."
                $ audrey.love += 5
                ryan.say "What are you waiting for?"
                ryan.say "That guy attacked me!"
                ryan.say "I was just standing here, minding my own business."
                ryan.say "And he punched me - everyone saw him do it!"
                "The bouncers look around, searching for confirmation of Ryan's account."
                "Most of the bar-staff shake their heads."
                "After all, they really did see what went down."
                "But it's Audrey that's the first to speak up in my defence."
                show audrey angry
                audrey.say "Bullshit, you lying creep!"
                audrey.say "[hero.name] was just trying to help me get rid of you."
                audrey.say "You went to sucker-punch him, and he defended himself!"
                "That seems to be good enough for the bouncers."
                hide ryan with moveoutleft
                show audrey normal blush at center with move
                "They pounce on Ryan before he can do something that he'll regret."
                "It only takes a few moments for them to bundle him out the door."
                "And then it's remarkable how quickly things return to normal."
                "I watch as Audrey thanks the bouncer and the bar-staff."
                "Audrey finally turns her attention to me as I shake life back into my hand."
                audrey.say "Thanks for helping me out, [hero.name]."
                show audrey annoyed
                audrey.say "But I'm sorry that creep ended up trying to hit you!"
                "I shake my head, waving away Audrey's concern."
                mike.say "Don't mention it, Audrey."
                mike.say "We need to stick up for each other."
                mike.say "Especially when it comes to jerks like Ryan!"
                show audrey normal
                "Audrey nods in agreement."
                audrey.say "Yeah, I know, I know."
                audrey.say "But at least let me buy you a drink, yeah?"
                show audrey happy
                audrey.say "My way of saying thanks!"
                "I nod and smile, which gets the same in return from Audrey."
                show audrey normal
                "She orders us both another drink, and we chat while we wait."
                "Maybe tonight didn't turn out to be as relaxing as I'd hoped."
                "But at least I got to help Audrey out when she was in a jam."
                "And I have to admit, punching Ryan in the jaw felt pretty damn good too!"
            else:
                "I try to lurch out of the way, but Ryan's too fast for me."
                play sound punch_hard
                pause 0.2
                hide audrey
                show ryan fight punchmike at center, hshake
                pause 0.2
                with hpunch
                "His fist slams into my jaw, and I can already feel my legs collapsing under me."
                hide ryan
                show ryan casual angry zorder 2 at center with hpunch
                "Somehow I manage to hold onto the bar, keeping myself from falling down."
                show audrey annoyed zorder 1 at right
                "And before I regain my senses, the door-staff on duty steps into the fray."
                "And they pounce on Ryan before he can do something that he'll regret."
                hide ryan with moveoutleft
                show audrey at center with move
                "It only takes a few moments for them to bundle him out the door."
                "And then it's remarkable how quickly things return to normal."
                "I watch as Audrey thanks the bouncer and the bar-staff."
                "Audrey finally turns her attention to me as I nurse my aching jaw."
                show audrey normal blush
                audrey.say "Thanks for helping me out, [hero.name]."
                show audrey sad
                audrey.say "But I'm sorry that creep ended up hitting you!"
                "I shake my head, waving away Audrey's concern."
                "The truth is that I'm in an immense amount of pain right now."
                "But I want to preserve at least a little of my pride."
                mike.say "Don't mention it, Audrey."
                mike.say "We need to stick up for each other."
                mike.say "Especially when it comes to jerks like Ryan!"
                show audrey normal
                "Audrey nods in agreement."
                "And I try as best I can to get back to relaxing with a beer."
                "But the fact that my jaw's still aching makes that quite a challenge."
            call injured from _call_injured_4
        "Do nothing":
            "I know that I should get up and do something."
            "Maybe put myself between them or even just tell Ryan to back off."
            "But before I can will myself into action, somebody beats me to it."
            hide audrey ryan flirt
            show ryan casual smile at left
            show audrey annoyed at right
            "One of the bar-staff yells to the bouncers on the door of the pub."
            hide ryan with moveoutleft
            "And they pounce on Ryan before he can do something that he'll regret."
            "It only takes a few moments for them to bundle him out the door."
            "And then it's remarkable how quickly things return to normal."
            show audrey at center with move
            "I watch as Audrey thanks the bouncer and the bar-staff."
            "And all I can do is shake my head in amazement."
            hide audrey with dissolve
            "That could have gone down in a very different and much worse manner!"
            $ audrey.set_gone_forever()
    return

label audrey_event_01:
    show audrey danny
    if audrey.hidden:
        "I see Audrey, My colleague from work, she seems a little scared."
    else:
        "I see Audrey, she seems a little scared."
    "A suspicious man is talking to her."
    thug_say "Do you live on a chicken farm?"
    thug_say "'Cause you sure know how to raise a cock."
    audrey.say "Please go away."
    thug_say "You are so selfish!"
    thug_say "You're going to have that body the rest of your life and I just want it for one night."
    "Audrey looks at me with expectation in her eyes."
    menu:
        "Help her":
            if audrey.love.max < 40:
                $ audrey.love.max = 40
            $ audrey.unhide()
            $ fight = False
            $ audrey.flags.greeted = TemporaryFlag(True, "day")
            hide audrey
            hide audrey danny
            show danny close
            mike.say "Hey man, she said to let her be and go on your way."
            show danny angry
            thug_say "Fuck off, don't mess with my squeeze."
            mike.say "I said to leave her alone."
            menu:
                "Pretend she's yours":
                    mike.say "That's my pussy your messing with, and I don't like when others play with my toys."
                    thug_say "Didn't know that fine piece of ass was taken."
                    thug_say "I'll get another slut to take care of my pole."
                    hide danny
                    show audrey
                    audrey.say "Thanks for the help."
                    mike.say "It was nothing."
                    audrey.say "Arent you a little cocky?"
                    show audrey blush
                    audrey.say "So, I am your 'pussy' and you don't like when people 'mess' with me?"
                    mike.say "Ahem..."
                    audrey.say "Oh, and your 'toy' too..."
                    mike.say "It was to make him go away..."
                    audrey.say "Well, I do hope that's true."
                    audrey.say "Thanks for the help."
                    mike.say "It was nothing."
                    $ audrey.flags.toy = 1
                    $ audrey.sub += 5
                "Attack him":
                    mike.say "I'll have to kick your ass then."
                    $ fight = True
                "Intimidate him":
                    mike.say "If you don't go I'll crush your balls like walnuts and make you eat what's inside."
                    if hero.fitness >= 25 or hero.charm >= 25:
                        thug_say "Ok, ok, don't be so work up about some pussy."
                        hide danny
                        show audrey
                        audrey.say "Thanks for the help."
                        mike.say "It was nothing."
                        $ audrey.love += 2
                    else:
                        "He doesn't seem impressed."
                        $ fight = True
            if fight:
                python:
                    d = 50
                    if not hero.has_skill("martial_arts"):
                        d += 25
                if hero.fitness >= d:
                    play sound punch_hard
                    pause 0.2
                    show danny fight lose at center, hshake
                    pause 0.2
                    with hpunch
                    "I punch the jerk in the guts and kick him in the nuts."
                    "After that I throw him out of the pub."
                    hide danny
                    mike.say "Are you okay Audrey?"
                    show audrey
                    audrey.say "I am fine [hero.name], thanks for the help."
                    $ audrey.love += 5
                    $ game.flags.thugfight = 1
                else:
                    play sound punch_hard
                    pause 0.2
                    show danny fight win at center, hshake
                    pause 0.2
                    with hpunch
                    "I try to punch the jerk, but he is faster than me."
                    "I get punched instead."
                    $ hero.grooming -= 5
                    $ hero.energy -= 5
                    $ hero.fun -= 5
                    thug_say "You're not worth the trouble bitch."
                    "He then spit on me and leaves."
                    hide danny
                    show audrey
                    audrey.say "Are you okay [hero.name]?"
                    mike.say "I am fine, at least he left."
                    audrey.say "Thanks for the help."
                    mike.say "It was nothing."
                call injured from _call_injured_5
            hide audrey
        "Don't get involved":
            hide audrey danny
            "I leave her to fend for herself."
            $ audrey.set_gone_forever()
    return

label audrey_event_02:
    show audrey
    if audrey.love.max < 60:
        $ audrey.love.max = 60
    "I see Audrey."
    "I walk over to talk about what happened the other night."
    "Maybe invite her on a date."
    mike.say "Hey Audrey, what's up?"
    "She turns to me looking less than amused."
    audrey.say "Hello [hero.name], shouldn't you be working?"
    "She turns back to the coffee pot in the break room. Her shift hadn't started yet."
    "Her ass looks so good in those jeans."
    "What am I doing? This is Audrey... and we are at work!"
    mike.say "Um yeah... I just wanted to ask you-."
    "She turns back to be, looking annoyed."
    audrey.say "Ask me what?"
    mike.say "Err... I just wanted to see what happened the other night?"
    audrey.say "What do you mean? I went home."
    audrey.say "Thanks for your help with that guy, I have to work now."
    "She brushes past me coldly and I'm so confused."
    "Is this the same Audrey that had been flirting with me everyday at work?"
    mike.say "Are- are you mad?"
    "She stopped in her tracks."
    audrey.say "Why would I be mad? I said thank you for helping."
    mike.say "No I mean about-."
    audrey.say "I don't know what you are talking about."
    "She turns and walks away then, but there is still a sexy sway to her hips."
    hide audrey with dissolve
    "What is going on here?"
    scene bg black with dissolve
    pause 1.0
    scene bg office
    with dissolve
    "I volunteer for overtime just to see what would happen with Audrey."
    "She wasn't flirting with me like usual."
    "I wonder if I did something wrong."
    "Maybe I should bring her flowers?"
    "Then again she wasn't flirting with any of the guys tonight."
    "I sigh and turn off my computer."
    show audrey
    "As I am walking out I see Audrey again and smile."
    mike.say "Hey-."
    "She promptly ran into me as if she hadn't seen me, spilling her cold coffee down the front of me."
    mike.say "Hey!"
    audrey.say "Oh, sorry about that. Guess I didn't see you there."
    mike.say "You really should be more-."
    "I notice that she leans toward me more, and I can see that she's not wearing a bra."
    mike.say "...careful."
    "I finish my sentence."
    audrey.say "I should be. I'm so clumsy. I guess I could take lessons from you."
    "She gives me a wink and my mind is spinning as she walks away."
    hide audrey
    "... Totally confused."
    return

label audrey_event_03:
    if audrey.love.max < 80:
        $ audrey.love.max = 80
    $ audrey.flags.nokiss = False
    "Damn I must have it bad."
    show audrey
    "That girl across the room looks like Audrey."
    "Wait."
    "It is Audrey!"
    "I think about jumping off to go say hello, but decide to watch for a moment instead."
    "She has tight short shorts on and a t-shirt that form fits to her breasts."
    "She gets on one of the bikes across from me, seeming to have not noticed I'm there yet."
    "She starts to pedal and my eyes fall down to her ass."
    "I like the way it moves and want to hold it in my hands."
    "I don't know how long I have been staring when I suddenly realize there is a mirror in front of her."
    "And she is looking into it back at me with a smirk on her face."
    "I feel my face heat up along with my pulse picking up with embarrassment."
    "How long has she known I was staring?"
    "She gets off then and stretches her arms high over her head."
    "I see part of her stomach as her shirt goes up."
    "Then she bends over all the way to touch her toes with her feet shoulder width apart."
    "She has a thong on!"
    if game.hour >= 20 or game.hour <= 5:
        "Blue. She's wearing blue tonight."
    else:
        "Blue. She's wearing blue today."
    menu:
        "Go over to Audrey":
            "I shut the treadmill off and hop off quickly."
            "I am standing just behind Audrey before I know it."
            mike.say "Hey."
            "She stands up suddenly as if she wasn't expecting me to be there."
            "Maybe she didn't see me?"
            show audrey blush
            audrey.say "Oh hey."
            "She smirks."
            audrey.say "What are the odds of running into each other here?"
            "I find myself not knowing what to say and scanning her over."
            "I hear her laugh."
            audrey.say "Did you like the show?"
            "Okay so she did know I was watching her."
            mike.say "Yeah.. When do I get to see more?"
            "She is smirking again and reaches into her shirt."
            "My eyes go wide but then I see her pull out a piece of paper."
            "I take it thinking I have gotten her number and she walks away."
            hide audrey
            "I open it up."
        "Don't go over to Audrey":
            "I decide not to go over to Audrey, wanting to see what more I can see."
            "But I am sadly disappointed when she stands up looking pissed."
            "She turns around and starts walking towards me."
            "I swallow hard because I don't know what to expect."
            "When she stops right in front of me, and reaches down the front of her shirt I quickly shut off the machine."
            "Handing me a piece of paper."
            hide audrey
    show audrey note
    pause 99
    hide audrey note
    "I look back up to see Audrey is already half away across the gym and try to wait until she is out of sight."
    "I try not to look like I am in a hurry to go find her."
    "I wave to one of my buddies and keep going, glad that I'm not finding anyone I have to stop to talk to."
    "I round the corner to the locker rooms and I try to look casual."
    "Before I know what is happening, I feel something hit the side of my face and my whole head turns to the side."
    show audrey
    "Holding the side of my face I look around furious and see Audrey in the shadows."
    "Audrey just slapped me!"
    "What the hell!"
    menu:
        "Show her who's the boss.":
            "I reach forward and grab a fistful of her hair on top."
            "Pushing her against the wall where no one can see us I growl."
            mike.say "What do you think you are doing, slapping me?"
            "With a smirk she says."
            $ audrey.sub += 2
        "Be gentle":
            "I rub the side of my face, less angry that I know it is Audrey."
            "I calmly ask."
            mike.say "Why did you slap me?"
            "Some of her cockiness slips but she says."
            $ audrey.love += 2
    audrey.say "I was getting your attention. And that was for watching me for so long and not coming to say Hi."
    audrey.say "Come on, I wanta show you something."
    "She motions for me to follow her down a short hallway I hadn't paid much attention to."
    "Even in the dark I can still see her hips sway."
    audrey.say "I found this a while ago. But haven't had a chance to use it."
    "I get nervous wondering what she is talking about."
    "We come up to a green door and she opens it before flipping on the light."
    "It's an old smaller version of one of the locker rooms."
    "As soon as I'm in she shuts the door and I hear her lock it behind us."
    "I feel my heart start to race as I start to wonder what she is hoping to get out of this."
    "I know what I want, but I doubt she has protection and I know I don't."
    show audrey topless with dissolve
    "I turn to her and she has taken her t-shirt of."
    audrey.say "Sorry, that old thing was all sweaty..."
    "Her voice was sexy and I was losing control of my thoughts."
    audrey.say "I hope you don't mind."
    "She flutters her eyelashes at me."
    "I quickly shake my head."
    mike.say "Not at all."
    "Again with the no bra..."
    "She walks seductively over to me and wraps her arms around my neck."
    menu:
        "Take charge":
            "I instantly take charge."
            "I pick her up and she wraps her legs around my waist."
            "I back up until I feel the bench that is against the wall at the back of my knees and sit down with her in my lap as we make out."
            show audrey kiss naked with fade
            $ audrey.flags.kiss += 1
            "I run my fingers through her hair roughly and hear her moan right before I slip my tongue into her mouth for the first time."
            "This was too good to be true."
            $ audrey.sub += 2
        "Be passive":
            "I decide to let her take charge."
            "She pushes me until I'm backed up against a bench on the wall and then she pushes me down to sit on it."
            "I watch eagerly as she climbs on top of me with one leg on either side of my lap."
            show audrey kiss naked with fade
            $ audrey.flags.kiss += 1
            "She takes my face in both her hands and kisses me slowly at first."
            "Then it gets rougher."
            "She slides her tongue into my mouth and I get embarrassed at how fast I am getting hard."
            "Suddenly she lets go looking bored."
            $ audrey.sub -= 2
    hide audrey kiss
    show audrey sport topless sad
    with fade
    "I hear her sigh as she pushes back."
    show audrey joke
    if game.season in [0, 1]:
        audrey.say "Wanta know what's wet?"
        "I can't believe she just asked me that."
        "I can't help but smirk."
    else:
        audrey.say "Wanta know what's beautiful during cold seasons?"
    mike.say "Sure."
    show audrey happy
    if game.season in [0, 1]:
        audrey.say "Waterparks."
        mike.say "What?"
        audrey.say "Waterparks. There's one downtown."
        audrey.say "They're one of my favorite things to do during the summer."
    else:
        audrey.say "Park."
        mike.say "What?"
        audrey.say "Park. There's one downtown."
        audrey.say "They're one of my favorite things to do during the winter."
    audrey.say "Take me there and you might get lucky."
    audrey.say "Meet me there next weekend at 2pm."
    "She gets off of me then to go collect her shirt and slips it on over her head before leaving me there to wonder what the hell just happened, and how we got so close with nothing happening again!"
    hide audrey
    return

label audrey_event_04b:
    play sound cell_vibrate
    pause 1.0
    "It's a text from Audrey."
    audrey.say "Meet me at the park, now."
    menu:
        "Go":
            pass
        "Don't go":
            $ audrey.love -= 10
            $ hero.cancel_event()
            return
    if audrey.love.max < 100:
        $ audrey.love.max = 100
    $ audrey.flags.nodate = False
    scene bg black with dissolve
    pause 1.0
    scene bg park
    with dissolve
    "I stand next to the yellow by the gates to the park feeling unsure and stupid."
    "What if this was just a trick and she wasn't really coming?"
    "I check the time again, she still has a few minutes."
    show audrey casual joke
    audrey.say "Whoa, [hero.name]!"
    audrey.say "You're puffing like a steam train!"
    audrey.say "Seriously, I found you by following your steaming breath!"
    "At the sound of Audrey's voice, I find myself forgetting all about the cold."
    "I turn to face her and I can't help breaking into a huge, dumb smile."
    show audrey normal
    mike.say "H...hi..."
    mike.say "Hi, Audrey!"
    "Luckily for me, Audrey seems to take my stammering as an effect of the cold."
    "In reality I'm trying to take in just how good she looks in her winter clothes."
    "Seriously, I've spent so many hours mentally undressing Audrey at work."
    "And it feels weird to be so turned-on by the sight of her wrapped up against the cold."
    "But that's how it is - she looks sophisticated and glamorous too."
    "Like some mysterious girl from Eastern Europe, you know?"
    "Maybe even a female spy on a mission to meet up with a fellow agent!"
    show audrey flirt
    audrey.say "So is a walk in the park's a hot date to you?"
    "And just like that, Audrey brings me back to reality with a bump."
    "She shakes her head and raises an eyebrow."
    show audrey mock
    audrey.say "This is going to be a walk in the park, sure."
    audrey.say "But only in a literal sense!"
    show audrey normal
    "Trying to ignore Audrey's barbs, I offer her my arm."
    "And to my surprise, she's quick to take it."
    "Maybe she's actually going to give this a chance to succeed?"
    "I don't waste any time in beginning our walk."
    "And before too long, we're strolling along the paths together."
    "There's no awkward silence either, just pleasant small-talk."
    "Everything seems to be going to plan."
    show audrey happy
    "That is until Audrey catches sight of the playground."
    "Immediately I feel her pulling me towards it."
    mike.say "Uh...what's the matter, Audrey?"
    mike.say "That's the playground - where kids are supposed to play, yeah?"
    mike.say "I thought we could go see the lake, where there's swans and stuff."
    mike.say "You know, romantic things...for adults?"
    "Audrey shakes her head and makes a dismissive tutting sound."
    audrey.say "No way, [hero.name]!"
    audrey.say "I haven't been on a swing in years."
    audrey.say "And I want you to push me on one...now!"
    "Audrey quickly drags me over to the swings, which are conveniently empty."
    "She seems not to notice, or more likely ignores, the parents and their kids around us."
    "And a few moments later, she's sat on one of the swings, clutching the chains tightly."
    audrey.say "Come on, [hero.name]!"
    audrey.say "You'd better push me as high as you can!"
    menu:
        "Push Audrey hard" if hero.fitness >= 25:
            mike.say "You asked for it, Audrey!"
            "Trying really hard to follow Audrey's lead, I make an effort to ignore the parents watching us."
            show audrey swing mike with fade
            "And I begin to push the swing as hard and fast as I possibly can."
            "Since I'm no weakling and Audrey's not very heavy, it doesn't take long to pick up speed."
            "Soon enough she's swinging higher and higher into the air with each pass."
            audrey.say "Oh yeah!"
            audrey.say "That's it!"
            audrey.say "That feels so good!"
            audrey.say "I want it harder, faster, higher!"
            "I'd have to be pretty dumb not to notice what Audrey's doing right now."
            "The demanding and the way she's gasping with excitement."
            "I'm more used to hearing that kind of talk in the bedroom!"
            "And the worst thing is that it's working too!"
            "Audrey kicks her legs out and tosses her head from side to side."
            "The result is that all I can think of is getting my hands on her."
            "Even with everyone around us watching, my head is full of dirty thoughts."
            "And I can feel my cock getting hard inside my shorts too."
            $ audrey.sub += 2
            audrey.say "Oh...oh god..."
            audrey.say "I'm getting dizzy..."
            audrey.say "Let me down!"
            hide audrey
            show audrey casual happy with fade
            "Once she's back on solid ground, Audrey seems to make a speedy recovery."
            audrey.say "Mmm...I enjoyed that!"
            audrey.say "How was it for you?"
        "Push Audrey gently":
            mike.say "Okay, Audrey - hold on tight!"
            "I try to make it sound like I'm going to push Audrey as fast as she's demanding."
            "But in reality, I can feel the eyes of the parents all around me."
            "It feels like they're boring into my skull the whole time!"
            show audrey swing mike with fade
            "And so I do my best to push Audrey without making a spectacle of myself."
            "If I'm lucky, I can make this look like a quirky, romantic scene."
            "Like something you'd see in a cute rom-com, right?"
            "Rather than an embarrassed guy pushing a crazy exhibitionist on a kid's swing!"
            audrey.say "Aw, come on!"
            audrey.say "You can do better than that!"
            mike.say "No way, Audrey!"
            mike.say "I'm giving it all I've got!"
            audrey.say "Bullshit!"
            audrey.say "I want it harder, faster, higher!"
            $ audrey.sub -= 2
            $ audrey.love -= 5
            "Somehow Audrey manages to make every word sound dirty."
            "Like she's demanding I fuck her harder, rather than push her on a swing."
            "And I can feel myself getting ever more embarrassed the whole time."
            hide audrey
            show audrey casual angry
            with fade
            "Plus, when she finally gives up on the swing, Audrey's none too pleased with my performance."
            audrey.say "Well, that was a disappointment!"
            mike.say "I...I'm sorry, Audrey."
            mike.say "I was having problems getting it up!"
            mike.say "The swing, that is...getting the swing up that high!"
    show audrey normal
    "We walk away from the playground and towards the lake."
    "But my head is spinning like I was the one that went on the swing just now."
    "So as soon as I spot an empty bench, I suggest that we take a seat."
    "Audrey seems reluctant at first, but then I point out the swans on the lake."
    audrey.say "Huh..."
    audrey.say "It's funny, but I never really noticed them before!"
    audrey.say "I guess they are kind of pretty."
    "I nod, eager to encourage Audrey's interest in the birds."
    "I can't remember the last time I heard her talking like that."
    "Like she's actually warming up to the idea of genuine romance."
    mike.say "Of course they are, Audrey."
    mike.say "Swans are like a symbol of true love, you know?"
    mike.say "Because they mate for life!"
    show audrey joke
    audrey.say "But what if the girl swan finds the guy swan cheated on her?"
    audrey.say "Or she sees a new guy swan that's way hotter than her current guy swan?"
    "I can't help chuckling at Audrey's questions."
    mike.say "I don't know, Audrey."
    mike.say "I'm not an expert on the sex-lives of swans!"
    mike.say "They're just supposed to be romantic, that's all."
    "Audrey gives me a strange sideways glance at this."
    hide audrey
    show audrey kiss casual with fade
    $ audrey.flags.kiss += 1
    "It's one that I can't fathom, until she kisses me a moment later."
    "I'm surprised by the move, but I return the kiss as soon as I can."
    menu:
        "Make the kiss heavier" if hero.sexperience >= 5:
            "Almost instantly I can feel my passions begin to rise."
            "For a moment I think about holding back, keeping it clean."
            "But then Audrey teases pushing her tongue between my lips."
            "And that's what pushes me over the edge!"
            "What am I - some kind of prude?"
            "Shaking off any intentions of holding back, I lean into the kiss."
            "Audrey responds instantly, her tongue darting into my mouth."
            "I have one arm wrapped around her shoulder, pulling her close."
            "And the other one is on her thigh, squeezing it gently."
            "Audrey whimpers with pleasure as I do this."
            "And so I begin to slide my hand up higher."
            "This only serves to make the kiss feel that much more intense."
            "Audrey moans as my fingers slide closer to her crotch."
            "I get them as close as I dare, feeling the warmth between her legs."
            "I can imagine what's going on in her panties right now."
            "Almost picture the way her pussy must be glistening and wet!"
            hide audrey kiss
            show audrey casual surprised blush
            with fade
            "To my surprise, it's Audrey that breaks off the kiss a moment later!"
            $ audrey.sub += 2
            audrey.say "Uh...whoa..."
            audrey.say "Not...not here..."
            audrey.say "But maybe later...okay?"
            audrey.say "Somewhere a little more private?"
        "Keep the kiss innocent":
            "Almost immediately I can feel my passions begin to rise."
            "Audrey teases pushing her tongue between my lips."
            "And my instincts tell me to throw caution to the wind."
            "But somehow I find the strength of will to resist my urges."
            "We just had what passes for a pretty romantic moment."
            "And I don't want to ruin that by pouncing on Audrey a second later!"
            "I have no idea if she picks up on that or not."
            "But I take the fact she doesn't demand more as a positive sign."
            hide audrey kiss
            show audrey casual happy with fade
            "And she smiles at me once the kiss comes to an end."
            "Which I choose to take as a positive sign."
    show audrey normal
    "I nod and stand up, not feeling the need to say any more."
    "Audrey stands too, and takes my arm again."
    "We stroll around the park for a little longer after that."
    "But we seem to be heading back in the direction that we came."
    "And soon enough we end up at the gates of the park once more."
    show audrey flirt
    audrey.say "I've got to admit it, [hero.name]."
    audrey.say "This wasn't nearly as lame as I thought it would be!"
    mike.say "Erm...thanks, Audrey...I think!"
    mike.say "We should do this again some time."
    "Audrey smiles and waves over her shoulder as she walks away."
    "And I find myself genuinely smiling as she does so."
    "Maybe this was a good idea after all."
    $ audrey.flags.delay = TemporaryFlag(True, 1)
    return

label audrey_event_04:
    play sound cell_vibrate
    pause 1.0
    "It's a text from Audrey."
    audrey.say "Meet me at the waterpark, now."
    menu:
        "Go":
            pass
        "Don't go":
            $ audrey.love -= 10
            $ hero.cancel_event()
            return
    if audrey.love.max < 100:
        $ audrey.love.max = 100
    $ audrey.flags.nodate = False
    scene bg black with dissolve
    pause 1.0
    scene bg waterpark
    with dissolve
    "I stand next to the yellow fountain in the shade feeling unsure and stupid."
    "What if this was just a trick and she wasn't really coming?"
    "I check the time again, she still has a few minutes."
    show audrey swimsuit blush with dissolve
    "I look up and realize she is walking my way."
    "She has a red and black checkered bikini swimsuit top on, with what looks like black bikini bottoms."
    "My eyes are glued to her."
    audrey.say "Hey, nice to see you made it. I wanta go on that."
    "She points to one of the tallest water slide."
    "I am not exactly fond of rides that high but...."
    "I didn't want her to think I was a wimp if I didn't go."
    mike.say "Uh, sure. Let's go see how long the line is."
    "I wasn't sure at all what I was getting myself into, but she squeals."
    show audrey happy
    audrey.say "Come on!"
    "Grabbing my hand she pulls me along with her to go check out the ride."
    "Unfortunately, the line is short because it is still early."
    "Of course, part of the deal was that I pay for everything, so when we got up front I gave the man the tickets."
    "It is still too early to buy wristbands."
    "In no time we are being strapped in."
    audrey.say "This is going to be fun."
    "Without warning I feel her grab my crotch and I tense."
    "She gives it a squeeze but then quickly lets go when then worker walks by."
    "I was confused as to which part she thought was fun."
    "Is she wanting me to touch her?"
    "I look around but I don't have the nerve she does. So I wait until the ride starts moving."
    show audrey waterslide with fade
    "Once we are in a dark tunnel, I take one hand off the bar and place it on her leg, sliding my hand up to tight."
    menu:
        "Slide hand up":
            "Slowly, as the ride pick up speed I slip my hand up toward her bikini bottom."
            "She doesn't stop me so I keep going."
            "When I reach as high as I can I start to rub my thumb against the top of her leg and she presses her leg up against mine to encourage me."
            "I move to do more, but suddenly the tunnel ends and I am forced to grab onto the bar tight with both hands as we plunge several hundred feet downward."
            $ audrey.sub += 1
        "Don't slide hand up":
            "I chicken out and decide not to feel her up."
            "I glance at her and she seems to be waiting for something."
            "I don't know what to do and she seems to be getting impatient."
            "Just when I decide to do something the tunnel ends and I am forced to grab onto the bar tight with both hands as we plunge several hundred feet downward."
    "I hear her let out a scream and I wish I was the one making her scream."
    audrey.say "[hero.name], this is aaaaaaaamazzzzzzing!"
    "Before I could answer we slashed down into the first pool of water. Now that I have to admit is cool."
    "Plus it gave me an idea."
    "I wonder, since she likes waterparks, if I could get her to do it in a pool?"
    "Just as quickly as we hit the water we were going back up and sideways several hundred feet."
    "By the time the ride was over we were both soaked and our limbs felt weak."
    hide audrey
    show audrey swimsuit happy
    with fade
    "She hops out of the ride and giving me no time at all and tells me."
    audrey.say "I wanta go again! But on that one over there!"
    "This girl was going to wear me out. At least this one doesn't seem as high."
    scene bg black with dissolve
    pause 1.0
    scene bg waterpark
    with dissolve
    show audrey swimsuit with dissolve
    "By the end of the day I think we have hit every roller coaster there is."
    "We step away from the one we just got off and Audrey grabs my hand for the first time since we first got there."
    audrey.say "Come here."
    "I don't have a choice but to follow, and she leads me to a quiet area behind one of the rides where no one can see us."
    "I see a bench and walk over to it to sit down with her."
    "She leans in so I do the same."
    show audrey kiss swimsuit with fade
    $ audrey.flags.kiss += 1
    "Again, just like when we were in the gym locker room we are a tangle of hair and limbs."
    menu:
        "Feel her up":
            "I start to slide my hand up her leg but she slaps it away."
            audrey.say "Not in public."
            $ audrey.sub += 1
            menu:
                "Keep going":
                    mike.say "I'll do whatever I want."
                    "She seems to decide that I can, in fact, do whatever I want and lets me."
                    $ audrey.sub += 1
                "Stop":
                    "I'm disappointed but I decide to enjoy the kiss at least."
        "Don't feel her up":
            "I decide it's too dangerous to try and feel her up right now, someone might see us and call security."
            "Kissing is good enough."
    "Just when I think I can't breathe she pulls back."
    scene bg waterpark
    show audrey swimsuit
    with fade
    "I hear her sigh."
    audrey.say "Well, that was not a half bad date."
    audrey.say "You can try and invite me on more of those."
    "I have a broad smile on my face until I hear her say."
    audrey.say "But don't bring me on lame ones."
    "My smile fell and I watch as she goes."
    "Somehow I feel like an idiot again."
    hide audrey
    $ game.room = "map"
    $ audrey.flags.delay = TemporaryFlag(True, 1)
    return

label audrey_gay_mistake:
    show audrey
    audrey.say "Hey gorgeous, how's it going?"
    mike.say "Mindlessly typing on a keyboard under fluorescent lights..."
    mike.say "Does it get better than this?"
    audrey.say "Question. You're not dating anybody, are you, because I met somebody who would be perfect for you."
    mike.say "Ah, y'see, perfect might be a problem. Had you said 'co-dependent', or 'self-destructive'..."
    audrey.say "Do you want a date Saturday?"
    mike.say "Yes please."
    audrey.say "Okay. He's cute, he's funny, he's-"
    mike.say "He's a he?"
    audrey.say "Well yeah!"
    audrey.say "...Oh God. I- just- I thought- Good, Audrey."
    audrey.say "I'm just gonna go flush myself down the toilet now..."
    audrey.say "Okay, goodbye..."
    $ audrey.love += 1
    $ game.flags.gaymistake = 1
    return

label audrey_talk_breakup:
    "At first I think that it's nothing, that I'm just being paranoid."
    "But no matter how I try, I can't shake of the feeling of being watched."
    "Eventually the feeling becomes so bad that it's actually stopping me from working."
    "So with a sigh, I glance up from what I'm doing to take a look around the office."
    "I figure the quicker I prove to myself there's nobody there, the quicker I can get over it."
    "But then I let out a yelp of genuine surprise and almost jump out of my chair."
    show audrey
    "There, leaning on my desk with her chin resting on the palms of her hands, is Audrey."
    "She doesn't seem the least bit shocked by my reaction to her presence."
    "Instead she keeps right on looking at me with a beaming smile on her face."
    "I put one hand on my desk and the other over my heart, feeling it still racing."
    mike.say "Uh..."
    mike.say "Audrey..."
    mike.say "Was there...was there something you wanted me for?"
    "Still with the smile on her face, Audrey gives me a casual shake of the head."
    audrey.say "Nah, not really."
    audrey.say "I was just thinking - that's all."
    mike.say "You were thinking?"
    mike.say "Do...do you normally stare at people when you do that?"
    audrey.say "Only when they're the thing I've been thinking about."
    "I'm still more than a little irate and weirded out by Audrey's actions."
    "But apparently I've been on her mind."
    "So much so that she felt compelled to stare at me."
    "Call me a typical guy, but when someone that looks like Audrey admits that..."
    "Well, I'm more than keen to hear what she has to say about me!"
    mike.say "Oh, really?"
    mike.say "And just what were you thinking about me?"
    audrey.say "I was just wondering - how long has it been since you went on a date?"
    "Well hello - this sounds more than a little promising."
    "Under any other circumstances, I could choose to take that as an insult."
    "But instead I choose to play it straight, sensing a greater prize at stake."
    mike.say "Well, it's not like I really have a problem in that area."
    mike.say "But work's been so hectic lately, taking up my time."
    mike.say "I guess there's been no room for that kind of thing!"
    show audrey flirt
    "Audrey shakes her head, a look of sympathy on her face."
    audrey.say "It's a crying shame, that's what it is."
    audrey.say "A good-looking guy like you being on his own."
    audrey.say "Especially one that takes such good care of himself too!"
    "I can't help being flattered by Audrey's kind words."
    "But she's not wrong - I do take pains to make sure I look this good on a daily basis."
    mike.say "I...I try my best, Audrey!"
    "She nods at this, and I sense that she's about to get to the point of her visit."
    audrey.say "You do, [hero.name], really you do."
    audrey.say "And it's not like it goes without notice either."
    mike.say "It doesn't?"
    audrey.say "Oh no - I was only talking to Gregory in accounting about it yesterday."
    "Now that's not what I was expecting to hear - that she's been discussing me with other guys!"
    mike.say "Erm...what would Gregory have to say about me?"
    audrey.say "Well, let's just say that he's been admiring you from afar."
    audrey.say "And I told him that I might just mention that fact to you."
    "Suddenly I can feel the rug being pulled out from under my feet."
    mike.say "But...but...he's gay, isn't he?!?"
    audrey.say "Actually, I think he's bi."
    audrey.say "But that might be splitting hairs..."
    mike.say "I'm fine with Gregory is, Audrey - I'm a pretty modern guy."
    mike.say "The only problem is that I'm straight!"
    show audrey surprised
    "Audrey stands up at this, as if what I just said came as some kind of revelation to her."
    audrey.say "No way - shut the front door!"
    mike.say "Seriously - I am!"
    mike.say "I thought it was pretty obvious?"
    show audrey mock
    "Audrey frowns and shakes her head."
    audrey.say "Apparently not to bi guys."
    audrey.say "Or straight women either!"
    mike.say "Well I am, okay!"
    mike.say "I'm not in denial, closeted or curious."
    mike.say "Just straight."
    audrey.say "Fine, fine - whatever you say..."
    audrey.say "So what should I tell Gregory?"
    mike.say "Tell him what I just told you - I'm flattered, but not interested."
    "Audrey nods and turns to walk out of my office without saying another word."
    "In a perfect world, that would mean that I'd said my piece and the matter was settled."
    "But I can't help thinking that she's actually saving her breath for the sake of the gossip that's going to follow."
    $ audrey.love += 1
    hide audrey
    return

label audrey_help_at_work:
    show audrey
    audrey.say "[hero.name], could you help me with something?"
    $ result = renpy.display_menu([("Sure", 1), ("No, I don't have time", 2)])
    if result == 1:
        show audrey work happy
        audrey.say "Thank you. I am cleaning up the archive room."
        "Fuck, that will take a while..."
        "We clean the archive room together."
        $ game.pass_time(needs=True)
        $ audrey.love += 1
        audrey.say "Thank you [hero.name].."
    else:
        show audrey work angry
        audrey.say "Thanks for nothing then."
        $ audrey.love -= 1
    hide audrey
    return

label audrey_male_ending:

    if renpy.has_label("audrey_achievement_3") and not game.flags.cheat:
        call audrey_achievement_3 from _call_audrey_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church
    scene bg church wedding
    with fade
    "Back when I first met Audrey, I could never have imagined that we'd end up here."
    "It was all I could manage to be in the same room as her without getting angry."
    "And so the idea that I'd ever learn to tolerate her seemed pretty far out."
    "The notion that we might actually get together and eventually tie the knot..."
    "Well, that would have sounded like crazy-talk!"
    "But here we are, with me standing at the altar."
    "And looking over my shoulder for her walking down the aisle."
    "As I do so for what feels like the hundredth time, the music begins to play."
    "And just like that, everything becomes real."
    show audrey wedding with dissolve
    "Audrey appears at the far end of the chapel and begins to walk towards me."
    "I don't think I've ever seen her look more beautiful than she does right now."
    "Sure, she technically shouldn't be wearing white."
    "But it looks good on her all the same."
    "Maybe it looks so good because I know the reasons why she shouldn't be wearing it too!"
    if audrey.is_visibly_pregnant:
        "The cut of the dress can't hide the fact that Audrey's pregnant either."
        "But then it's never something that we've tried to hide."
        "Just a reminder that we're ready to start a family."
        "That and spend the rest of our lives together."
    else:
        "The cut of the dress is pretty traditional."
        "But that just means it shows off Audrey's beauty that much more."
    "And she still has that same look in her eye."
    "The one that she always had when she was torturing me back in the office."
    "The one that lets me know she's thinking wicked thoughts!"
    "But there's going to be enough time for things like that later."
    "And so I make an effort to push any such thoughts out of my head."
    "I need to focus on slipping the ring onto Audrey's finger."
    "Slipping other things into other places can wait..."
    show audrey wedding at center, zoomAt (1.5, (640, 1040)) with fade
    "As soon as Audrey reaches my side, she shoots me a conspiratorial glance."
    "I can't help smiling back at her, probably looking goofy as I do so."
    "I'm just so happy to be doing this that I can't help letting it show."
    "Keeping my voice to a whisper, I lean closer to Audrey."
    mike.say "Thanks for bothering to turn up!"
    mike.say "Just make sure you behave yourself, okay?"
    audrey.say "Speak for yourself, [hero.name]."
    audrey.say "This is my big day."
    show audrey flirt
    audrey.say "If I want to make it memorable, then I will!"
    show wedding audrey with fade
    "Just hearing the defiance in Audrey's voice thrills me."
    "I can't keep myself from getting excited at the thought of what she could have in mind!"
    show wedding audrey priest with dissolve
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today to witness the union of these two souls..."
    "We both make a show of paying attention as the priest begins the ceremony."
    "And I wonder with each moment that passes just when Audrey will make her move."
    "Priest" "Do you, [hero.name], take Audrey to be your lawful, wedded wife?"
    mike.say "I do."
    "Priest" "And do you, Audrey, take [hero.name] to be your lawful, wedded husband?"
    audrey.say "I do."
    "I find myself blinking in genuine surprise."
    "Did we just get through the vows without incident?"
    "Priest" "Then, unless anyone present knows of any reason these two may not be married..."
    "This is it, the point where anyone can throw a spanner into the works."
    "If Audrey had something planned, this is when she's going to do it..."
    "Priest" "Then I now pronounce you husband and wife."
    "Priest" "You may kiss the bride."
    show wedding audrey -priest with dissolve
    "I'm almost too shocked to do as the priest says."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show audrey kiss wedding with fade
    $ audrey.flags.kiss += 1
    "And so Audrey lays one on me as I just stand there looking stunned."
    "After that, everything seems to carry on as normal."
    hide audrey
    show audrey happy wedding at center, zoomAt (1.5, (640, 1040))
    with fade
    "And it's so weird to me that it all seems to pass by in a blur."
    "Before I know it, Audrey and I are on the floor for the first dance."
    show audrey talkative
    audrey.say "Hey, [hero.name]!"
    audrey.say "Are you feeling okay?"
    show audrey sadsmile
    mike.say "Huh...wha..."
    mike.say "Oh...yeah, Audrey, I'm okay."
    mike.say "I guess I was just expecting you to do something..."
    mike.say "Well, something outrageous, I guess!"
    show audrey joke
    audrey.say "During the ceremony?"
    show audrey mock
    audrey.say "Oh, [hero.name], that's so predictable!"
    audrey.say "No, I was just waiting for the right moment..."
    show audrey flirt
    "With that, Audrey shoulders out of her dress."
    "Right there, on the dance-floor and in front of all the guests."
    "Her breasts are bared, her nipples getting harder by the moment."
    "My mouth moves, but no words come out."
    scene audrey ending bj with fade
    "And I find myself doing nothing to stop her as she kneels down in front of me."
    "It takes no more than a couple of seconds to unzip my flies and pull out my dick."
    show audrey ending bj lick
    "And then Audrey wraps her lips around the end of it, licking and sucking."
    "I look up from what Audrey's doing and around at the assembled guests."
    show audrey ending bj blow
    play sound audrey_moans_blowjob_medium loop
    "Of course, everyone's stunned into silence, unable to process what's happening."
    show audrey ending bj phones
    "But then I see the first of the inevitable phones appear in someone's hand."
    "That's the moment the dam breaks, and soon there's a phone in every hand."
    "Almost all the guests there are filming as Audrey sucks my cock."
    "I don't know if it's the perverse nature of what's happening to me."
    "That or some kind of kink I never knew I had for public acts of indecency."
    show audrey ending bj close
    "Either way, my cock is as hard as stone the whole time Audrey's working on it."
    "I try not to make eye-contact with anyone else while it's happening."
    "But Audrey seems to be intent on taking her time."
    "She's good at this kind of thing, yet I know she's dragging the blowjob out too!"
    "And that's when I get the notion to do something drastic."
    "I know that I could tell her to stop what she's doing."
    "But somehow it seems to me that would be the worst thing I could do."
    "It'd shatter the weird moment that she's created."
    "Worse, it'd make everyone think that I don't approve of what she's doing."
    "I mean, I don't really know if I DO approve of it."
    "But she's my wife, and I feel like I should be on her side right now!"
    "Which is why I drag my cock out of Audrey's mouth and pull her to her feet."
    "From there, I hike up her dress and pull down her panties."
    "She hardly has time to realise what's happening before I push into her."
    scene audrey ending fuck
    show audrey ending fuck phones
    with fade
    "Audrey gasps as I slip my hands under her thighs, lifting her off the ground."
    show audrey ending fuck vaginal pleasure b
    play sound slide_in
    "And she keeps on gasping and moaning as I begin to fuck her."
    "It's not the most gentle or relaxed sex, more a desperate coupling."
    show audrey ending fuck a
    "But the people watching us are still getting to see quite a show."
    play sexsfx1 fuck_calm loop
    play sound audrey_moans_happy_medium loop
    show audrey ending fuck a
    pause 0.35
    show audrey ending fuck b
    pause 0.35
    show audrey ending fuck a
    pause 0.35
    show audrey ending fuck b
    "Audrey has her hands around my neck, holding on for dear life."
    show audrey ending fuck a
    pause 0.25
    show audrey ending fuck b
    "And I seem to be driven by sheer nervous energy, keeping on to the very end."
    show audrey ending fuck a
    pause 0.25
    show audrey ending fuck b at startle(0.05,-10)
    pause 0.25
    show audrey ending fuck a
    pause 0.25
    show audrey ending fuck b at startle(0.05,-10)
    "It's not long before I can feel myself reaching the end."
    show audrey ending fuck a
    pause 0.15
    show audrey ending fuck b at startle(0.05,-10)
    pause 0.15
    show audrey ending fuck a
    pause 0.15
    show audrey ending fuck b at startle(0.05,-10)
    pause 0.15
    show audrey ending fuck a
    pause 0.15
    show audrey ending fuck b at startle(0.05,-10)
    "And when it finally happens, I don't hold back for a moment."
    show audrey ending fuck a ahegao
    pause 0.15
    show audrey ending fuck b at startle(0.05,-10)
    pause 0.15
    show audrey ending fuck a
    pause 0.15
    show audrey ending fuck b at startle(0.05,-10)
    pause 0.15
    show audrey ending fuck a
    pause 0.15
    show audrey ending fuck b with vpunch
    pause 0.15
    show audrey ending fuck cum b with vpunch
    stop sound fadeout 1
    stop sexsfx1 fadeout 1
    "Audrey yelps as I shoot my load into her, squirming and wriggling in my grasp."
    "I don't remember what happens after that, everything really does become a blur!"
    "There are pictures and I've seen some of the videos."
    "Oh shit...the videos!"
    "But that's really all that I can recall about consummating my wedding in public!"
    scene bg office
    show audrey close
    with fade
    audrey.say "Finally, I get the chance to tell my own side of the story for once."
    audrey.say "No more of [hero.name] getting me wrong and making me look mean!"
    audrey.say "Okay, okay...he's not that bad, I admit it."
    show audrey flirt
    audrey.say "And I DO like to be mean to him sometimes."
    audrey.say "But can you blame me when he makes it so much fun?"
    audrey.say "I suppose that's all I thought it was going to be between us."
    audrey.say "Back when I first started working under him, it seemed like a bit of fun."
    audrey.say "I knew from the moment I laid eyes on [hero.name] that he was the right type."
    audrey.say "Trying his best to look like the big man around the office."
    audrey.say "But there was no way he could keep his eyes off of me."
    show audrey happy
    audrey.say "I mean, I can't blame the guy for having good taste, now can I?"
    audrey.say "And so I knew that I could have some serious fun with him."
    audrey.say "Which is exactly what I did!"
    audrey.say "It took him a while to catch onto the fact that I actually liked him too."
    audrey.say "But then that's the average guy for you, isn't it?"
    audrey.say "No matter how high their IQ might be, they can't read a woman for shit!"
    audrey.say "I think he was enjoying it all really, me teasing him every day in the office."
    audrey.say "Because he came around in the end."
    audrey.say "You know, that he started to realise I liked him?"
    audrey.say "And...well, yeah...I'll admit it now."
    show audrey annoyed
    audrey.say "He did kind of turn the tables on me when he went and said that he loved me."
    audrey.say "I suppose that was what I'd wanted to happen."
    audrey.say "But maybe it crept up on me too, while I was having my fun at his expense."
    audrey.say "I was so caught up in teasing and torturing [hero.name] at the time."
    audrey.say "I wasn't really aware of where it was going and what my feelings were."
    show audrey normal
    audrey.say "Anyway, who wants to hear about that kind of stuff?"
    audrey.say "It's boring and it doesn't matter."
    audrey.say "The ring on my finger proves that, right?"
    audrey.say "We were never going to be an ordinary couple."
    audrey.say "What happened at the wedding reception proved that!"
    audrey.say "And we're going places now that we've tied the knot too."
    audrey.say "Having me at his side really lit a rocket under [hero.name] at work."
    audrey.say "He's climbing the corporate ladder at a crazy speed now, aiming for the top!"
    audrey.say "Of course most of it is down to having me as his PA, but he still does his part."
    audrey.say "He moved out of that suburban dive he was renting as soon as we were married."
    audrey.say "And now we have a penthouse apartment that suits our lifestyle so much more."
    if audrey.is_visibly_pregnant:
        audrey.say "And there's plenty of room for the new addition to the family too."
        audrey.say "We don't know if it's a boy or a girl, as we chose not to find out."
        audrey.say "But either way, we can't wait to meet them when they get here!"
    else:
        audrey.say "We can look down on everyone else from way up here."
        audrey.say "And if we ever choose to start a family, there's plenty of room."
    audrey.say "But before I make it sound like we're the perfect couple, I'll level with you."
    show audrey flirt
    audrey.say "I still LOVE to torment [hero.name] every chance that I get."
    audrey.say "The only difference is that now I'm pretty sure he's enjoying it."
    audrey.say "Well, most of the time anyway!"
    audrey.say "What, you think those high-flyers in their stylish offices are working all the time?"
    audrey.say "Ha - shows what you know!"
    audrey.say "Once that door's closed and the blinds are down..."
    audrey.say "Well, I think I'll leave that one to your imagination."
    audrey.say "Think of it as one last tease!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not audrey.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_3
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_3
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label audrey_birthday_date_male:
    $ DONE["audrey_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "casual"
    scene bg street
    "Normally it's not too hard to get a girl to tell you the date of her birthday."
    "I mean most people are pretty open with that kind of information once you get to know them."
    "Not least because they like the idea of celebrating it with you when the big day arrives."
    "But with Audrey, it was kind of hard to wring the info out of her and it took a while."
    "Kind of like she was reluctant to open up about herself like that."
    "Which seemed a little odd to me, as she's not exactly the shy, retiring type."
    "You know what I mean?"
    "To be honest, she usually comes across as the kind of person that likes to create chaos."
    "And to be the centre of attention whenever she manages to pull it off."
    "That's why I've really tried to make a special effort, to do something different."
    "Maybe the whole idea of a date on her birthday is out of Audrey's comfort zone."
    "So doing the usual kind of stuff probably isn't going to cut it."
    "I just hope that the choices I've made are going to pay off!"
    "And to be honest, we could have gotten off to a better start."
    "I told Audrey to meet on this specific street at this specific time."
    "But so far, there's been no sign of her."
    "I keep on glancing around, scanning the faces of the people passing."
    "And when I'm not doing that, I'm taking out my phone to check the time."
    "Yet none of the faces are Audrey's and the time just keeps ticking on by."
    "I'm really starting to get worried about her when..."
    show audrey casual happy at center, zoomAt(2.0, (840, 1340)) with vpunch
    audrey.say "HEY, [hero.name]!"
    audrey.say "SURPRISE!"
    with vpunch
    mike.say "WHA..."
    mike.say "WHOA..."
    "Audrey must have managed to sneak up on me while I was looking the other way."
    "That's how she was able to get right up beside me and shout straight into my ear!"
    show audrey at center, traveling(1.5, 1.0, (640, 1040))
    "I spin around, still feeling more than a little panicked from her making me jump."
    "And the first thing I see is the huge grin on Audrey's face."
    show audrey joke
    audrey.say "Wow..."
    audrey.say "You really shit yourself!"
    show audrey mock
    audrey.say "I should sneak up on you more often."
    menu:
        "Laugh it off":
            "I put a wry grin on my face and nod my head."
            "And I add a suitably slow clap as well."
            mike.say "Well done, Audrey..."
            mike.say "If I ever play hide and seek, I'll come ask you for advice!"
            show audrey annoyed
            "Audrey looks a little caught off-guard by my response."
            "I don't think she was expecting me to call her out on being childish."
            "And the dead-pan way I handled it seems to have left her on the back-foot."
            audrey.say "Erm..."
            audrey.say "It was just a joke, you know?"
            audrey.say "That's all..."
            mike.say "I know that, Audrey."
            mike.say "It's just that now I'm an adult, I like my jokes to be observational."
            mike.say "Rather than the kind of slapstick shit I laughed at as a kid!"
            $ game.active_date.score -= 10
            show audrey angry
            "Audrey opens her mouth to say something in response."
            show audrey frown
            "But then she seems to think better of it."
        "Tell her to never do that again":
            "I don't like being shown up at the best of times."
            "But being humiliated in the middle of the street like that..."
            "Well that's just a step too far, if you ask me!"
            mike.say "Please don't do that again, Audrey?"
            mike.say "I'm stressed enough as it is."
            mike.say "And I'm afraid you're going give me a heart-attack!"
            $ game.active_date.score += 15
            show audrey happy
            "Audrey rolls her eyes and waves away my pleas like they're nothing."
            audrey.say "Oh come on!"
            audrey.say "You need to lighten up a little, [hero.name]."
            show audrey joke
            audrey.say "Being all uptight and anxious is far worse for you."
            audrey.say "Keep that up and you'll worry yourself into an early grave without my help!"
            "I can't help frowning at Audrey's response."
            "Trying to ignore her flippant attitude and just get on with the date instead."
    scene bg street
    show audrey casual normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "I take hold of Audrey's hand and begin to lead her off down the street."
    "She comes willingly, but I can still see the usual glint in her eye."
    "The same one that makes her constantly look for the change to cause trouble."
    show audrey joke
    audrey.say "So..."
    audrey.say "What have you got in mind?"
    audrey.say "Something cliche, like a candle-lit meal?"
    show audrey happy
    audrey.say "Or are you going to be more daring?"
    audrey.say "Maybe take me somewhere like a strip-club?!?"
    mike.say "Oh no, Audrey..."
    mike.say "You're not getting anything out of me."
    mike.say "This is going to be a total surprise."
    scene bg taxi
    show audrey casual annoyed at center, zoomAt(1.5, (640, 1040))
    with fade
    "I have to make a turn up ahead in order to reach our destination."
    "But I don't let Audrey know about it until the very moment we reach it."
    "And even then I do it by lurching off in that direction without a word."
    show audrey angry
    audrey.say "Hey!"
    audrey.say "You could give me a warning, you know?"
    show audrey annoyed
    audrey.say "And where are we going anyway?"
    scene bg alley
    show audrey casual normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "Audrey looks around her as I lead us down a narrow alleyway."
    show audrey surprised
    audrey.say "Ooh!"
    show audrey joke
    audrey.say "Are we going to hire a hooker or something?"
    audrey.say "Because I'd be totally down with that, just for the record."
    "I shake my head and let out snort of amusement."
    "Then I point to the stairs of a nearby fire-escape."
    mike.say "Just for the record, Audrey..."
    mike.say "We are not hiring a hooker!"
    mike.say "Now, would you mind?"
    show audrey annoyed
    "I begin to climb the stairs, motioning for Audrey to follow me."
    "She looks more than a little confused, but she does as I ask."
    scene bg rooftop with fade
    pause 0.5
    show audrey casual surprised with easeinright
    "And it doesn't take me long to lead her up to the roof of the building."
    "Where I've already been busy setting up everything we should need for our date."
    "I've chosen this rooftop because it has a commanding view over the city."
    "And I've also spread out a rug with a picnic lunch on it too."
    "Audrey takes a look at everything I've prepared."
    "Which leaves an odd look on her face, one I'm not used to seeing her pull."
    mike.say "Are you okay, Audrey?"
    audrey.say "Erm...yeah..."
    audrey.say "This is just not what I was expecting!"
    "I don't think I'm flattering myself too much to say this."
    "But I feel like I'm a pretty good judge of people."
    "Like I know what they're feeling just from watching them."
    "And I'm getting that same feeling with Audrey right now."
    if hero.charm >= 80:
        mike.say "I know it's a little out of left-field."
        mike.say "But you've never struck me as ordinary, Audrey."
        mike.say "Actually, I'd say you were anything but!"
        mike.say "So I figured you might like something out of the ordinary?"
        show audrey happy
        "I see a smile beginning to creep onto Audrey's face."
        show fx exclamation
        show audrey awkward
        "And it happens as she realises that I just paid her a compliment."
        "A pretty big one too."
        audrey.say "I've been called a lot of things by guys."
        audrey.say "Most of them things I'd like to forget."
        hide fx
        show audrey annoyed blush
        audrey.say "But I think that I kinda like that one."
        audrey.say "You mean I'm quirky, right?"
        audrey.say "Different, but in a good way?"
        mike.say "That's exactly it, Audrey!"
        mike.say "I knew you'd get it."
        $ game.active_date.score += 20
        show audrey normal
        "Audrey looks pleased, like she just passed a test."
        "But more importantly, like she's looking forward to the rest of our date too."
    else:
        mike.say "You love it, don't you?"
        mike.say "You'd never come out and say it."
        mike.say "But this is exactly what you wanted me to do, right?"
        show audrey angry
        "Audrey frowns and shakes her head at this."
        "And then she lets out a snort of derision."
        $ game.active_date.score -= 10
        audrey.say "What planet are you actually living on, [hero.name]?"
        audrey.say "I said that because I couldn't believe you'd take on a date to a damn rooftop!"
        audrey.say "I mean sure, it's pretty original - I'll give you that."
        audrey.say "But what do you think, that I have some weird secret fetish for urban squalor?!?"
        "I'm about to start apologising."
        "But Audrey holds up her hand, stopping me in my tracks."
        show audrey frown
        audrey.say "Don't start trying to explain yourself now, okay?"
        audrey.say "It'll do fine."
        audrey.say "So let's just leave it at that and try to have a good time."
    scene bg rooftop at center, zoomAt(1.25, (640, 740))
    show audrey casual at center, zoomAt(1.5, (640, 1140))
    with fade
    "As soon as we're sitting on the blanket, I see that Audrey's watching me with interest."
    "But I'm feeling more than prepared for this moment, ready to spring into action."
    "Because I've planned this whole thing down to the final detail."
    "And I want all of it to come off just the way I envisioned it."
    if hero.has_skill("foodie"):
        "Reaching behind my back, I grope for something I hid up here earlier."
        "And as soon as I feel my fingertips brushing it, I make my move."
        show audrey surprised
        mike.say "Ta da!"
        mike.say "You can't have a picnic without food."
        mike.say "So I went to the trouble of knocking this up for us."
        "Audrey looks on with interest as I place the picnic hamper in front of her."
        "And that interest only becomes more apparent as I start to take out the food."
        "All of which I lovingly prepared myself from only the finest ingredients."
        show audrey normal
        "Once most of it's been unpacked, I motion for her to dig in."
        "Audrey seems keen to sample what's on offer."
        show fx exclamation
        show audrey surprised
        "But as soon as she's swallowed a mouthful, I see her eyes go wide."
        "And I'm instantly worried that she hates the taste of what she's chewing."
        mike.say "Audrey..."
        mike.say "What's wrong?"
        mike.say "Does it really taste that bad?"
        hide fx
        show audrey blush
        "Audrey shakes her head and takes another mouthful."
        "But she doesn't even pause to look me in the eye as she does so."
        audrey.say "Uh-uh..."
        audrey.say "It's...mmm..."
        $ game.active_date.score += 15
        show audrey happy -blush
        audrey.say "It's totally amazing!"
        mike.say "Oh..."
        mike.say "Well, that...that's great!"
        "Audrey keeps on nodding as she shovels food into her mouth."
        "And I watch her, filling with pride as I do so."
        "That is until I realise that she's not going to stop."
        "So I have to jump in too before there's nothing left!"
    else:
        "Reaching behind my back, I grope for something I hid up here earlier."
        "And as soon as I feel my fingertips brushing it, I make my move."
        show audrey surprised
        mike.say "Ta da!"
        mike.say "Here you go, Audrey..."
        mike.say "Flowers for your birthday!"
        show audrey angry
        "As soon as she sees the bouquet in my hand, Audrey reels backwards."
        "And she tries as best she can to cover her nose and mouth."
        $ game.active_date.score -= 10
        audrey.say "Urgh!"
        audrey.say "Keep those things away from me..."
        audrey.say "I get seriously bad hay-fever!"
        if hero.knowledge >= 50:
            "I shake my head and push the flowers closer still."
            mike.say "It's okay, Audrey..."
            mike.say "I know all about your allergies."
            mike.say "That's why these are fake flowers."
            show audrey annoyed
            "Audrey stops trying to pull away."
            "And she looks down at the bouquet in genuine surprise."
            audrey.say "They are?"
            $ game.active_date.score += 25
            show audrey normal
            audrey.say "That's...really thoughtful..."
            audrey.say "Thank you, [hero.name]!"
            "I keep on smiling as Audrey finally accepts the bouquet."
            mike.say "Sorry there's no scent from them."
            audrey.say "Oh no, don't apologize for that."
            show audrey happy
            audrey.say "Normally I'd be sneezing myself to death by now!"
        else:
            "Of course she does!"
            "Audrey's always complaining about the plants in the office."
            "How on earth could I forget something like that?"
            mike.say "Oh shit!"
            mike.say "Audrey..."
            mike.say "I'm so sorry!"
            show audrey annoyed
            "I look this way and that."
            "Desperately searching for a way to get rid of the bouquet."
            "But in the end, the only thing I can think to do is toss it away."
            "And that means throwing it straight off the top of the building."
            "I wince as the expensive bunch of flowers flies out of my hand."
            "And I keep on hoping that I don't hear the sound of it landing on someone down there."
            "Plus I have to deal with the way Audrey's still glaring at me the whole time too."
    show audrey casual normal
    "Audrey's still busy eating her share of the picnic food right now."
    "So I take advantage of her distraction and reach for one more thing."
    "Because you obviously can't have food without drink to go with it."
    "And as this is a special occasion, I brought along something a little stronger than usual."
    mike.say "Feeling thirsty, Audrey?"
    mike.say "This might help things slip down more easily."
    menu:
        "Take out the champagne":
            "I hold up a bottle of champagne and a couple of flutes."
            "Fully expecting Audrey to be impressed by the gesture."
            "Because all girls like the idea of celebrating with champagne, right?"
            show audrey annoyed
            "But as soon as she sees what I'm holding, Audrey kind of frowns."
            "Then she wrinkles up her nose, almost like she's not too bothered."
            audrey.say "Okay, [hero.name]..."
            audrey.say "If that's all you brought along."
            mike.say "Huh?"
            mike.say "You do realise this is champagne, right?"
            mike.say "You know, the stuff that's like liquid romance?"
            "Audrey takes the glass that I offer her."
            "But I can already see that she has an ironic grin on her face."
            $ game.active_date.score -= 10
            show audrey joke
            audrey.say "How many sappy romcoms did you watch to figure that out?"
            audrey.say "Or was it from reading a bunch of romance novels in your spare time?"
            show audrey sad
            audrey.say "Here's a tip for you..."
            audrey.say "Real girls don't all pop for the same stuff."
            "I nod, trying not to let on how disappointed I am."
            "And I vow to remember what she just told me in future."
        "Take out a beer":
            "I hold up one of the cans of beer that I brought along."
            "Fully expecting Audrey to tell me that I'm an unromantic slob."
            show audrey surprised
            "But her eyes light up at the sight of it."
            "And she all but snatches the can out of my hand."
            show audrey normal
            "Audrey doesn't stand on ceremony either."
            "She immediately pops the can open."
            "And then she drains off what looks like half of it in one go."
            $ game.active_date.score += 15
            show audrey happy
            audrey.say "Aah..."
            audrey.say "That's better!"
            audrey.say "And it's a relief too."
            mike.say "What do you mean, Audrey?"
            show audrey normal
            audrey.say "Well, I was worried you were going to bust out champagne or something like that."
            audrey.say "And I just hate that stuff!"
            "I feel an instant surge of relief as she says this."
            "Because I had been finding it hard to choose between champagne and beer."
            "But it looks like I made the right choice after all."
            mike.say "Oh, I never had you down as a champagne girl, Audrey."
            mike.say "Don't worry about that!"
    show audrey normal
    "Audrey finishes her drink and then seems to pause for a moment."
    "At first I think she's looking out at the view over the city."
    "But then I realise that she's actually looking straight at me."
    "And as soon as I return her gaze, she opens her mouth to speak."
    show audrey happy
    audrey.say "Well this is all very nice..."
    audrey.say "But it's not the kind of present a girl can keep as a memento, is it?"
    if not hero.has_gifts:
        "Oh no, I knew that I'd forget something!"
        "But did it have to be something that important?"
        "Looks like I'm going to have to talk my way out of this one."
        mike.say "You can keep the memories, Audrey."
        mike.say "Those will last forever."
        mike.say "And they're totally priceless."
        show audrey sad
        "Audrey lets out a groan and shakes her head."
        audrey.say "Okay, [hero.name]..."
        audrey.say "I get it."
        audrey.say "You forgot my present."
        $ game.active_date.score -= 20
        $ audrey.love -= 10
        audrey.say "Don't worry, I'll get over it!"
        "Ouch!"
        "That leaves me feeling like the lousiest guy in the world."
        "But at least it sounds like Audrey's willing to let it go."
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_3
        scene bg rooftop
        show audrey casual normal at center, zoomAt(1.5, (640, 1040))
        if _return != "done":
            if _return not in ["None", "exit"]:
                mike.say "No need to go dropping hints, Audrey..."
                mike.say "I got you a present."
                mike.say "I was just waiting for the right moment to hand it over."
                show audrey happy
                "Audrey's face lights up as I give her the gift."
                play sound [paper_ripping_2, paper_ripping_1]
                "And then she tears it open without pause or hesitation."
                if _return:
                    show audrey surprised
                    "But as soon as she sees what's inside, Audrey's eyes almost pop out of their sockets."
                    mike.say "What's the matter, Audrey?"
                    mike.say "Are you okay?"
                    audrey.say "I..."
                    audrey.say "I don't know what to say..."
                    show audrey happy blush
                    $ game.active_date.score += 20
                    audrey.say "This is totally fucking awesome!"
                else:
                    show audrey sad
                    "But as soon as she sees what's inside, that enthusiasm seems to disappear."
                    mike.say "What's the matter, Audrey?"
                    mike.say "Don't you like it?"
                    $ game.active_date.score -= 10
                    audrey.say "Meh..."
                    audrey.say "It's kind of lame, [hero.name]!"
            else:
                "Oh no, I knew that I'd forget something!"
                "But did it have to be something that important?"
                "Looks like I'm going to have to talk my way out of this one."
                mike.say "You can keep the memories, Audrey."
                mike.say "Those will last forever."
                mike.say "And they're totally priceless."
                show audrey sad
                "Audrey lets out a groan and shakes her head."
                audrey.say "Okay, [hero.name]..."
                audrey.say "I get it."
                audrey.say "You forgot my present."
                $ game.active_date.score -= 20
                $ audrey.love -= 10
                audrey.say "Don't worry, I'll get over it!"
                "Ouch!"
                "That leaves me feeling like the lousiest guy in the world."
                "But at least it sounds like Audrey's willing to let it go."
    scene bg rooftop
    show audrey casual normal at center, zoomAt(1.5, (640, 1040))
    with fade
    $ game.hour = 20
    "By now the sun is beginning to set, and the lights are coming on all over the city."
    "Audrey and I watch as the familiar view becomes something almost magical to behold."
    "Now this is why I chose to bring her up here, so that we could watch the sunset together."
    "I consciously inch closer to Audrey, slipping my arm around her shoulder."
    menu:
        "Create a romantic moment":
            mike.say "Will you just look at that view, Audrey..."
            mike.say "A city that's home to thousands of people."
            mike.say "All of that hustle and bustle, all of that noise."
            mike.say "Yet here we are, high above it all."
            mike.say "It's pretty romantic, don't you think?"
            show audrey happy
            "I hear Audrey snigger under her breath."
            "And then she jabs me in the ribs with her elbow."
            "Not hard enough to make me take my arm from around her shoulder."
            "But hard enough to shake me out of the mood to be gushing and emotional."
            mike.say "Ouch!"
            mike.say "What the hell, Audrey?"
            show audrey mock
            audrey.say "Yeah, yeah, yeah..."
            audrey.say "It's a really nice view, [hero.name]."
            $ game.active_date.score -= 10
            show audrey annoyed
            audrey.say "But it's still the same noisy, smelly old city."
            audrey.say "There's probably going to be a plane flying overhead any second."
            audrey.say "And someone beneath us about to take a dump too!"
            "I take a deep breath and then let it out as a sigh."
            "Because I'm feeling suitably chastised for my efforts."
        "Create a personal moment":
            mike.say "Will you just look at that view, Audrey..."
            mike.say "A city that's home to thousands of people."
            mike.say "All of that hustle and bustle, all of that noise."
            mike.say "How in the hell haven't we both gone postal by now?"
            mike.say "I mean, I can easily think of half-a-dozen people I'd include in a murderous rampage!"
            show audrey happy
            "I hear Audrey snigger under her breath."
            "And then I feel her snuggle a little closer to me."
            audrey.say "I'd want to start at work for sure."
            show audrey joke
            audrey.say "Make sure I get my co-workers before the police could stop me!"
            "I laugh and nod too."
            mike.say "Yeah..."
            if not game.flags.dwaynedead:
                mike.say "Wouldn't want to miss out on adding Dwayne to the list!"
            audrey.say "You see this is why we get on, [hero.name]."
            show audrey happy
            audrey.say "Anyone else would be all 'ew, ew...you can't laugh at that!'."
            audrey.say "'Wanting to shoot people at work is wrong!'."
            $ game.active_date.score += 20
            show audrey happy
            audrey.say "But not you, because you don't have a stick up your ass."
            "I guess by Audrey's standards, that's a serious compliment."
            "I take a deep breath and then let it out as a sigh."
            "Because I'm feeling suitably pleased with my efforts."
    "Pretty soon the sun has set and it's starting to get dark."
    "The view out over the city is still quite something to look at."
    "But I guess that we have seen what we came up here to see."
    "So it feels like this is a good time to call an end to the date."
    show audrey normal
    mike.say "It's getting late, Audrey..."
    mike.say "You want to think about calling it a day?"
    mike.say "I mean we don't have to..."
    mike.say "Not if you want to do something else?"
    show audrey yawn
    if game.active_date.score >= 80 and audrey.sexperience >= 1:
        "Audrey stretches and lets out a yawn."
        "But I can't figure out if she's putting it on or not."
        show audrey happy
        audrey.say "You know what..."
        audrey.say "I am feeling pretty tired."
        show audrey flirt
        audrey.say "What do you say we lie down right here?"
        audrey.say "Just you and me?"
        "I don't need to have it spelled out to me."
        "And I don't need to be asked twice."
        "I nod eagerly."
        mike.say "Oh, I think we can manage that."
        mike.say "No problem at all..."
        call audrey_birthday_sex from _call_audrey_birthday_sex
    else:
        "Audrey stretches and lets out a yawn."
        "But I can't figure out if she's putting it on or not."
        show audrey normal
        audrey.say "You know what..."
        audrey.say "I am feeling pretty tired."
        audrey.say "Mind if we do call it a day?"
        mike.say "No, of course not..."
        "I hurry to collect up all of the things."
        "And then I follow Audrey back down the fire-escape."
        scene bg street
        show audrey casual
        with fade
        "Once we're out of the alleyway and back on the street, she waves goodbye."
        hide audrey with easeoutleft
        "Then she turns on her heel and walks away into the night."
        "Which leaves me to make my way back home on my own."
        "Hoping that she really was tired and I did enough to impress her."
    return

label audrey_birthday_sex:
    "I'm expecting this to go pretty much as it would in a romantic movie."
    hide audrey
    show audrey kiss casual with fade
    $ audrey.flags.kiss += 1
    "Audrey and I inching close together and then beginning to kiss."
    "Hands all over each other's bodies and slowly sinking down onto the blanket."
    "And that's the image I have in my head, until the very moment Audrey pounces."
    "Without a word of warning, she literally throws herself at me."
    "I'm taken completely by surprise, falling backwards and landing hard."
    "But even then it's not like I get a single moment to recover my senses."
    "Because Audrey's lips are suddenly pressed against mine."
    "And I can feel her hands tearing at my clothes too!"
    "Or to be more specific, she's fumbling around with my flies."
    "Audrey manages to get them open before I can coordinate my limbs."
    "And she wastes no time in pulling out my cock a moment later."
    show audrey kiss naked with dissolve
    "I feel her squeeze it, but there's no way I can make a sound."
    "Because as she does so, Audrey pushes her tongue into my mouth."
    "I have no idea what she's doing after that, as I can't see a thing."
    "But I can feel her wriggling around on top of me the whole time."
    "Audrey only lets up once she seems to be in the exact position she wants."
    "Then she pulls her tongue out of my mouth and sits up."
    show audrey close flirt blush naked -kiss
    "I make to part my lips and say something."
    hide audrey
    show audrey cowgirl rooftop big
    with vpunch
    "But quick as a flash, she pushes herself downwards."
    "And that's when I find out why she was keen to position herself just so."
    "There's only a few brief seconds in which I can gasp at the sensation."
    "As all of Audrey's weight presses her pussy down onto my cock."
    "Because that's as long as it takes for her lips to begin to part."
    mike.say "Oh..."
    show audrey cowgirl vaginal pleasure with vpunch
    mike.say "Oh fuck..."
    mike.say "Audrey!"
    show audrey cowgirl normal
    "Audrey replies by chuckling with undisguised delight."
    "I had no idea that she was more than ready to do it."
    "I was expecting to have to coax her open in order to get inside."
    "But instead I find myself laying there as her body swallows me whole."
    audrey.say "What's the matter, [hero.name]?"
    audrey.say "Don't you like it when a woman takes control?"
    audrey.say "A modern guy like you should be up for that!"
    show audrey cowgirl pleasure
    "As if she needs to add weight to what she's saying, Audrey pushes down again."
    "And this time she manages to make it all the way down to base of the shaft."
    "For all that she's gloating over pinning me down, this still affects her."
    "Having me so deep inside makes Audrey close her eyes and bite her lip."
    "But I also know that she's too damn stubborn to let that stop her."
    show audrey cowgirl speed
    "And she proves me right a moment later as she begins to ride me."
    show sexinserts chest audrey zorder 1 at center, zoomAt(1, (700, 770)) with dissolve
    "Her breasts instantly begin to bounce and sway, mere inches from my face."
    "The sight causes a sudden surge of excitement and desire in me."
    "I can feel myself thrusting up from below."
    "The urge to get as deep into her as possible taking hold."
    "Before now, Audrey was the one in charge and setting the pace."
    "Audrey moans as I finally get into my swing for the first time."
    audrey.say "Mmm..."
    audrey.say "That's it..."
    audrey.say "Fuck me harder..."
    audrey.say "I've been...a...bad...girl!"
    mike.say "You bet you have, Audrey..."
    mike.say "You're...a dirty...dirty little bitch!"
    "Audrey gasps as I tighten my hold on her."
    "But she's not expecting what happens next."
    show audrey cowgirl ahegao
    "Her eyes are wide with surprise and her pupils dilated with pleasure."
    "But even better, I can see that she's nodding too, urging me on to do more."
    "I keep right on thrusting back and forth."
    with vpunch
    "I'm going harder and faster than ever."
    "It doesn't take long for the effects to be visible, to see what's happening to Audrey."
    "Her entire body is rocking back and forth from my efforts."
    "Those hypnotic breasts jiggling like crazy."
    "And at the same time, Audrey's eyes are losing their focus."
    "I watch with satisfaction as they glaze over and roll back into her head."
    "But that still doesn't make me want to slow down for as much as a second."
    "In fact it only makes me want to do more, to push Audrey as far as I possibly can."
    "And that's just what I do, putting everything that I have into the effort."
    "Audrey seems to be able to take it to begin with."
    "She absorbs everything like a sponge and still seems able to take more."
    show audrey cowgirl ahegao
    "But slowly I can see a change in the way she's moving and the sounds she's making."
    "It looks like...yes, she's starting to cum!"
    "Within moments, Audrey's in the throes of her orgasm."
    "And the way she's moving is so intense that she's..."
    "She's taking me with her!"
    "I can't help it - there's nothing I can do to resist!"
    show audrey cowgirl creampie ahegao with vpunch
    "With one last thrust, I let go and shoot my load into Audrey."
    with vpunch
    "The sense of release is intense, almost indescribable."
    show audrey cowgirl -speed with vpunch
    "And the moment it's done, I feel the effects of all my efforts."
    hide sexinserts
    show audrey cowgirl pleasure
    "All of my energy seems to be gone, and now my muscles are turning to water."
    "Neither of us says a word or makes an effort to move."
    "We just lie there, panting and gasping as the sweat dries on our naked bodies."
    "At some point we'll get up and put our clothes back on."
    "But for now, I'm struggling just to keep myself from passing out!"
    $ audrey.sexperience += 1
    $ game.room = 'rooftop'
    return

label audrey_give_address:
    show expression f"bg {game.room}" at blur(16) with dissolve
    "I'm kind of drifting off into a world of my own when I feel the sensation of a hand on my shoulder."
    "Snapping back to reality, I look around to see Audrey giving me a gentle shake with the same hand."

    if audrey.sub >= 80:
        show audrey surprised with hpunch
        audrey.say "Oh, [hero.name]…"
        audrey.say "I...I didn't mean to startle you!"
        show audrey stuned
    else:

        show audrey whining with hpunch
        audrey.say "Geez, [hero.name]…"
        audrey.say "Are you that fucking bored with me that you're falling asleep?!?"
        show audrey upset
    show expression f"bg {game.room}" at blur(0) with hpunch
    "I shake my head, throwing off the last of my momentary confusion."
    mike.say "Ah..."
    mike.say "No, Audrey..."
    mike.say "I was just a little distracted, that's all."
    "Audrey nods at this, more like she wants to move the conversation on than because she actually agrees with me."

    if audrey.sub >= 80:
        show audrey talkative with dissolve
        audrey.say "Of course, [hero.name], of course..."
        audrey.say "I just wondered if you might..."
        show audrey happy at startle(0.05,-10)
        audrey.say "Well, if you might like to have my address?"
        show audrey normal
    else:

        show audrey talkative
        audrey.say "Yeah, yeah, whatever..."
        audrey.say "The important thing is that I wanted to give you my address."
        show audrey happy at startle(0.05,-10)
        audrey.say "I just realised you don't have it, even though we're dating already!"
        show audrey normal
    "My eyes go wide at the realisation that I don't already have it."
    "And I don't hesitate to nod my head at the idea."
    mike.say "Sure, Audrey..."
    mike.say "Of course I want to know your address!"
    $ audrey.flags.addressknown = True
    return

label audrey_apartment_first_visit:
    scene bg hallway with fade
    "I can't believe that I'm feeling as nervous as I am right now."
    "After all, I'm not doing anything more than walking up to Audrey's front-door."
    scene bg door hallway at center, zoomAt(1, (640, 720)) with fade
    "And I managed that part, because there it is, right in front of me."
    "Now all I have to do is actually knock on the damn thing."
    "So I raise my hand and ball it into a fist."
    show bg door hallway at center, traveling(1.5, 0.3, (640, 1040))
    pause 0.3
    play sound door_knock
    "And then I rap my knuckles on the door, making sure the sound is as loud as possible."
    "I can see that there are lights on in there, so I'm going to assume that she's home."
    "But even so, the seconds that follow seem to stretch on for a crazily long time."
    "And in that weird, dilated few moments, I can actually feel myself starting to worry."
    "Like there's a chance she's gone out and I'll be left standing here on the doorstep."
    "Or even crazier still, that Audrey's inside and deliberately choosing to ignore me."
    "All thoughts that vanish in an instant when I hear the sound of someone moving inside."
    "At once time seems to return to normal and my dumb worries simply fade away."
    scene bg black with dissolve
    pause 0.5
    scene bg audreylivingroom
    show audrey at center, zoomAt(1.5, (640, 1040))
    with wiperight
    "Then the door opens and I'm greeted by the sight of Audrey in the doorway."

    if audrey.sub >= 80:
        show audrey happy
        audrey.say "[hero.name]!"
        show audrey talkative
        audrey.say "You made it!"
        audrey.say "I'm so glad you came."
        show audrey shy
        "Audrey seems to almost be looking down at her feet as she says all of this."
        "As if she's too shy to actually look me in the eye."
        mike.say "Erm..."
        mike.say "Well, you did invite me, Audrey..."
        mike.say "And I did say that I'd come!"
        show audrey normal blush
        "Audrey looks embarrassed as she nods and gestures for me to come inside."
        show audrey talkative
        audrey.say "Of course I did!"
        show audrey shy
        audrey.say "So come on inside already."
    else:

        show audrey talkative
        audrey.say "So, you managed to find your way here without getting lost?"
        show audrey mock
        audrey.say "Maybe you're not as dumb as you look, [hero.name]!"
        show audrey happy at startle
        "Audrey chuckles at her own attempt to be humorous."
        show audrey normal
        "And I manage to put a crooked smile on my face at the same time too."
        mike.say "Yeah, Audrey..."
        mike.say "I'd have been here earlier too, if you didn't write the directions down in crayon!"
        show audrey happy
        audrey.say "Touche, [hero.name]!"
        show audrey shy
        audrey.say "Now get yourself inside before you hurt yourself trying to be funny."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
