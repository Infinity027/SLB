init python:

    Event(**{
    "name": "ayesha_event_02",
    "label": "ayesha_event_02",
    "conditions": [
        IsDone("ayesha_event_01"),
        HeroTarget(
            IsGender("male"),
            Or(
                IsRoom("alley"),
                HasRoomTag("street"),
                ),
            ),
        PersonTarget(ayesha,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("defended", False),
            MinStat("love", 25),
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    "do_once": False,
    "once_week": True,
    "quit": False,
    })

    CallEvent(**{
    "name": "ayesha_event_03",
    "label": "ayesha_event_03",
    "duration": 4,
    "conditions": [
        IsDone("ayesha_event_02"),
        IsNotDone("ayesha_event_03b"),
        HeroTarget(IsGender("male")),
        IsHour(9, 16),
        IsSeason(1),
        HasVehicle(),
        PersonTarget(ayesha,
            IsActive(),
            MinStat("love", 40),
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    })

    Event(**{
    "name": "ayesha_event_04",
    "label": "ayesha_event_04",
    "conditions": [
        Or(
            IsDone("ayesha_event_03"),
            IsDone("ayesha_event_03b"),
            ),
        IsNotDone("ayesha_event_04b"),
        HeroTarget(
            IsGender("male"),
            IsActivity("cinema_with"),
            IsRoom("cinema"),
            ),
        PersonTarget(ayesha,
            IsActive(),
            MinStat("love", 60),
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "ayesha_event_04b",
    "label": "ayesha_event_04b",
    "conditions": [
        Or(
            IsDone("ayesha_event_03"),
            IsDone("ayesha_event_03b"),
            ),
        IsNotDone("ayesha_event_04"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_cinema")),
        PersonTarget(ayesha,
            OnDate(),
            MinStat("love", 60),
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "ayesha_event_05",
    "label": "ayesha_event_05",
    "conditions": [
        Or(
            IsDone("ayesha_event_04"),
            IsDone("ayesha_event_04b"),
            ),
        IsHour(10, 14),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")),
        PersonTarget(ayesha,
            Not(IsHidden()),
            MinStat("love", 80),
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "ayesha_event_06",
    "label": "ayesha_event_06",
    "conditions": [
        IsDone("ayesha_event_05"),
        IsDayOfWeek(6, 7),
        IsHour(9, 14),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")),
        PersonTarget(ayesha,
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "ayesha_event_07",
    "label": "ayesha_event_07",
    "conditions": [
        IsDone("ayesha_event_06"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1")),
        PersonTarget(ayesha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "ayesha_event_08a",
    "label": "ayesha_event_08a",
    "conditions": [
        IsDone("ayesha_event_07"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("gym"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(ayesha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 130),
            IsFlag("manager", True)
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "ayesha_event_08b",
    "label": "ayesha_event_08b",
    "priority": 500,
    "conditions": [
        IsDone("ayesha_event_07"),
        IsNotDone("ayesha_event_08b_date"),
        HeroTarget(IsActivity("ask_date")),
        PersonTarget(ayesha,
            IsActive(),
            MinStat("love", 130),
            IsFlag("manager", False)
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    })

    Event(**{
    "name": "ayesha_event_09",
    "label": "ayesha_event_09",
    "conditions": [
        Or(
            IsDone("ayesha_event_08a"),
            IsDone("ayesha_event_08b_date")
            ),
        IsTimeOfDay("afternoon", "evening"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(ayesha,
            Not(IsHidden()),
            MinStat("love", 155),
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "ayesha_event_10",
    "label": "ayesha_event_10",
    "conditions": [
        IsDone("ayesha_event_09"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1"),
            ),
        PersonTarget(ayesha,
            OnDate(),
            MinStat("love", 180),
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "ayesha_sub_event_01",
    "label": "ayesha_sub_event_01",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(ayesha,
            IsActive(),
            MinStat("sub", 50),
            MinStat("sexperience", 1),
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "ayesha_sub_event_04",
    "label": "ayesha_sub_event_04",
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("date_livingroom"),
            OnDate()),
        MinDateScore(75),
        PersonTarget(ayesha,
            OnDate(),
            MinFlag("bdsm_training", 2),
            MinStat("sub", 70),
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "ayesha_preg_talk",
    "label": "ayesha_preg_talk",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(ayesha,
            Not(IsPresent()),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    })

label ayesha_preg_talk:
    $ ayesha.flags.toldpreg = True
    "I've been looking forward to seeing Ayesha again after a couple of days during which she's been pretty hard to reach."
    "Whenever I call her up, she's always too busy to talk, or else her phone goes straight to voicemail and I don't get a reply."
    "I dismissed it as nothing at first, just bad luck and poor timing on my own part."
    "But after a while, I began to get worried that there might be something going on."
    "So when Ayesha calls me up out of the blue, I'm more than eager to answer the phone."
    "In fact, hearing her voice is enough to make me instantly forget all about my worries."
    mike.say "Hey, Ayesha!"
    mike.say "I'm so glad you called."
    ayesha.say "R...Really?"
    "The odd response and the quivering in Ayesha's voice come as a genuine surprise to me."
    "She's usually so self-assured and confident, but my desire to get back in touch with her makes me ignore it all."
    "Perhaps she's just feeling a little out of sorts from us not catching up for a while too?"
    mike.say "Well...yeah, Ayesha."
    mike.say "I haven't been able to get you out of my mind since we last met up."
    "There's silence on the other end of the line as Ayesha pauses."
    "And for a moment I'm genuinely scared that she's going to hang up on me without an explanation."
    "But then I hear her sigh, and she starts speaking again."
    ayesha.say "That's sweet, [hero.name]."
    ayesha.say "Really it is..."
    ayesha.say "But we need to meet up, as soon as possible."
    mike.say "Sure thing, Ayesha."
    mike.say "That's just what I was thinking too!"
    "And that's how I come to be waiting for her at the appointed time and place."
    "By now, the initial thrill of hearing from Ayesha has begun to wear off."
    "Which means that the strangeness of her words is finally starting to bother me."
    "But still, when she actually turns up, I feel my heart almost skip a beat."
    mike.say "Ayesha!"
    mike.say "Hey, Ayesha - over here!"
    show ayesha sad
    "Ayesha nods at me, hurrying over as she waves for me to be quiet."
    "She looks almost embarrassed at the attention I'm giving her, like it's not welcome for some reason."
    ayesha.say "Okay, okay."
    ayesha.say "I see you already, [hero.name]."
    "Puzzled by the way she's behaving, I try to press Ayesha and find out why."
    mike.say "What's the matter, Ayesha?"
    mike.say "Did I do something to piss you off?"
    "At these last few words, a strange look passes over Ayesha's face, and I see her expression soften."
    ayesha.say "Oh hell, [hero.name]."
    ayesha.say "It wasn't something you did."
    ayesha.say "It was something WE did."
    "With that, she thrusts something into my hand with enough force for it too smart."
    "I look down and see that it's a plastic tube of some kind, no more than twenty centimetres long."
    "But it's only when I turn it over that what the thing actually is becomes clear."
    mike.say "Ayesha..."
    mike.say "This is a pregnancy test!"
    mike.say "Are you telling me you need to use this?!?"
    ayesha.say "In answer to your first question - no, it's not."
    ayesha.say "And the second - no, I don't."
    ayesha.say "It's a USED pregnancy test, and I already know the result."
    "I can't stop myself from finding the little window where the result is shown."
    "And what I read there really does leave me speechless."
    show ayesha blush
    ayesha.say "That last time you rode me bareback was amazing."
    show ayesha sad
    ayesha.say "But yeah, [hero.name] - I'm pregnant."
    ayesha.say "And before you ask, I'm going to get rid of it."
    menu:
        "Agree that Ayesha should have a termination":
            "I feel like I've been punched in the gut one moment."
            "But then like the weight of the world's been lifted off of my shoulders the next."
            mike.say "Shit, Ayesha!"
            mike.say "I feel like a piece of shit saying this."
            mike.say "But you're probably right."
            "Ayesha looks at me for a moment, staring deep into my eyes."
            "I get the feeling that she was maybe expecting me to say something else."
            "But then she looks down at the ground, nodding slowly."
            ayesha.say "Yeah..."
            $ ayesha.love -= 4
            ayesha.say "I guess we're on the same page here."
            "I nod my head, keen to move on and get the matter decided."
            mike.say "You're right, Ayesha."
            mike.say "I'm not ready to be a father yet."
            mike.say "And you..."
            "At this, I see Ayesha's eyebrow rise with interest."
            "She raises her head to look straight at me as I finish what I was about to say."
            mike.say "Well...you're not the motherly type - are you?"
            "Ayesha shakes her head sadly and lets out a weary sigh."
            ayesha.say "I guess not."
            "I choose to put the sadness in her voice down to realising I'm right."
            mike.say "Trust me, Ayesha - you're making the right choice."
            $ ayesha.set_flag("aborted", val=1, mod="+")
            $ ayesha.unpreg()
        "Disagree, Ayesha shouldn't have a termination":
            "I feel like I've just been punched in the gut."
            "Like the air's been sucked right out of me."
            mike.say "Wha..."
            mike.say "No, Ayesha - you can't do that!"
            show ayesha angry
            "Ayesha instantly bristles at this, and I realise that was a poor choice of words."
            ayesha.say "Screw you, [hero.name]."
            ayesha.say "My body, my choice!"
            "Holding my hands up in a gesture of contrition, I try to calm down the suddenly raging Amazon."
            mike.say "Whoa, hold on there."
            mike.say "That came out all wrong."
            show ayesha normal
            "Ayesha says nothing, only raising one eyebrow in a quizzical manner."
            "Which tells me that whatever I say next, it had better be good."
            "If not, I'll most likely end up getting snapped clean in two for my troubles..."
            mike.say "I meant to say that I don't want you to, Ayesha, not that you can't."
            mike.say "Of course it's your choice in the end."
            mike.say "But I just heard about a baby we both had a hand in making."
            mike.say "And when I did, my heart skipped a beat!"
            show ayesha blush
            "Any hint of anger vanishes from Ayesha's eyes in an instant."
            ayesha.say "Wh...what are you saying, [hero.name]?"
            mike.say "Ayesha, what do you think I'm saying?!?"
            mike.say "I love you, and I want to raise that kid together - just the two of us."
            "Ayesha looks down at herself, staring at the powerful muscles of her arms."
            show ayesha sad
            ayesha.say "But, [hero.name] - look at me!"
            ayesha.say "Can you see these hands cradling a little kid?"
            show ayesha blush
            mike.say "And pushing them in a stroller, feeding them a bottle, singing them to sleep too."
            mike.say "Ayesha, you'd make a great mom."
            mike.say "And the kid would love you more than anything in the whole world too."
            show ayesha sad
            ayesha.say "How can you know that, [hero.name]?"
            show ayesha blush
            mike.say "Because that's already how much I love you, Ayesha."
            $ ayesha.love += 6
            "Ayesha doesn't say a word in response, just wraps me in her arms and pulls me close."
            "I return the gesture, enjoying the sensation of her firm body against mine."
            "And my head is already starting to fill with dreams of the family we'll raise together..."
            $ ayesha.flags.keptbaby = True
    return

label ayesha_event_01:
    $ ayesha.unhide()
    "I'm keeping up my regular visits to the gym, but lately it's begun to feel like I'm just stuck in a rut with my routine."
    "No matter what I do, nothing seems to make a difference or to be enough to push me to the next level, and it's starting to frustrate me."
    "If this goes on for much longer, I'm worried that I'll end up quitting the place altogether, then god knows how I'll keep in shape."
    "So I make a point of talking to Hanna about the problem as soon as I get the chance."
    "She's promises to hook me up with a personal trainer the next time I'm at the gym, which sounds promising."
    "And so, when I'm next down there, I hurry to get changed and out of the locker-room."
    "Hanna told me that my new trainer would know I was coming and be waiting for me when I was ready."
    "But when I get out into the gym, I glance around and can't see any of the staff that I recognise standing around."
    show ayesha work with dissolve
    "The only person I know by sight is Ayesha, and so I shrug and make to hunt down one of the trainers."
    show ayesha angry
    ayesha.say "Hey there, fuck face!"
    ayesha.say "Where'd you think you're going?"
    show ayesha work normal
    "I look around at Ayesha, more surprised than alarmed by her calling me that for a second time."
    "There's a different quality to her voice on this occasion too, more jocular and familiar."
    "It's almost as if she's using it as a rib now, rather than an out-and-out insult."
    mike.say "I...I was just going to go and..."
    "I point lamely to the nearest piece of gym equipment, still wondering what concern of hers my routine could be."
    show ayesha close work
    ayesha.say "Oh no you don't!"
    ayesha.say "You're not laying a finger on anything - not without my say so!"
    "Wait a minute - she can't be..."
    "Can she?!?"
    mike.say "You're not my..."
    ayesha.say "Your new personal trainer?"
    ayesha.say "I sure as hell am, [hero.name]!"
    mike.say "But...since when do you work here?"
    "Ayesha shakes her head at my incredulity, as though it should have been obvious to me she was on the gym's payroll."
    ayesha.say "Since your friend Hanna noticed that I was shit-hot at what I do and hired me."
    "I blink at this in disbelief."
    hide ayesha
    show ayesha work
    mike.say "I thought that you were a wrestler?"
    ayesha.say "I am - but that doesn't come close to paying the bills."
    "I manage to keep myself from adding something about finding Englishmen to grind into bread..."
    ayesha.say "I have all of the qualifications for the job, more than enough, even."
    show ayesha happy
    ayesha.say "And you're my first client, [hero.name]."
    show ayesha happy at startle
    "She laughs in a way that reminds me of Vikings in the movies, hands on her hips."
    ayesha.say "If I'm honest, I think she gave you to me as a kind of test."
    ayesha.say "But don't worry - I promise to be gentle!"
    show ayesha normal
    "I nod, trying to laugh along with the amazon as she tells me of the fate that awaits me."
    "But her description of the workout she has planned and the logic behind it kind of passes me by."
    "All I can think about is the way that she said I'd been given to her - like a virgin given as tribute to a rampant barbarian warrior!"
    "And it comes as no surprise whatsoever that Ayesha intends to work me like a dog."
    "At times I think she'd welcome the addition of a whip to the tools at her disposal."
    "But that thought leads to disturbing mental images, and so I hastily push it to one side and concentrate instead on not dying."
    "However, there's one thing that keeps on catching my attention throughout the work-out."
    "And that's the sight of Ayesha herself, matching me on each and every piece of equipment or routine."
    "Covered in a sheen of fine perspiration, she moves like a machine."
    "Yet all the same, there's a certain and undeniable beauty to her as well."
    "I'd never thought that a girl so muscular and powerful could be feminine as well."
    "As we come to the end of the work-out and begin to cool down, I feel compelled to make small-talk with Ayesha."
    "Maybe a friendly compliment would help to win her over, or even get to know her a little better?"
    menu:
        "Compliment her muscles":
            mike.say "Don't take this the wrong way, Ayesha."
            mike.say "But your physique really is something else!"
            "Ayesha raises an eyebrow at this, but the smile on her face is guarded all the same."
            show ayesha happy
            ayesha.say "Thanks, [hero.name]."
            ayesha.say "I work hard to keep it looking that way."
            show ayesha normal
            ayesha.say "But then you've just had a little sample of that, so you know what I mean!"
            "I nod at this, unable to disagree."
            mike.say "I sure do!"
            mike.say "That work-out went a long way to getting me out of the rut I've been stuck in!"
            "Ayesha nods in approval."
            ayesha.say "Stick with me, fuck face."
            ayesha.say "I promise that I'll have you posing and flexing before you know it!"
            show ayesha happy
            "I laugh at this, and Ayesha joins me, the smile on her face now more genuine."
            "Well, I feel like I'm about to die of exhaustion."
            "And I've just been promised that there's worse to come."
            "But at least I feel like I've broken down some of the barriers between Ayesha and me."
            "Working-out with her looks like it could lead to a us actually becoming friends."
            "And who knows, in time, maybe even more."
        "Compliment her beauty":
            mike.say "Don't take this the wrong way, Ayesha."
            mike.say "But...you're...you're so beautiful!"
            $ ayesha.love += 5
            show ayesha work surprised
            "At this, I see Ayesha's eyes widen and her mouth fall open in surprise."
            mike.say "Ah...I'm sorry."
            mike.say "That came out all wrong!"
            mike.say "I must sound like such a creep..."
            show ayesha blush
            "While her eyes remain wide, Ayesha shakes her head as she tries to say something in response."
            ayesha.say "No, [hero.name], no..."
            ayesha.say "You don't sound creepy."
            ayesha.say "It's...sweet of you to think that."
            ayesha.say "But, I'm not used to people saying things like that to me."
            "Now it's my turn to shake my head in disbelief."
            mike.say "Why's that, Ayesha?"
            show ayesha sad
            "There's more than a little pain visible in her eyes as she answers."
            ayesha.say "People make fun of me..."
            "The words seem so strange, coming from someone so physically intimidating."
            "And yet they sound as sincere and honest as anything I've heard her say before now."
            "I want to say something helpful, to comfort her suddenly."
            "But when Ayesha notices me reaching out a hand to her, her mood changes in an instant."
            show ayesha normal
            "Barriers seem to go up again, she resumes her former demeanour of bluff confidence."
            ayesha.say "So, same time next week?"
            "I smile at this, trying to humour her efforts to cover up the previous show of emotion and weakness."
            mike.say "Okay, Ayesha, you're hired!"
            "Already my mind is awash with thoughts of what just happened between us."
            "At the very least, it seems that Ayesha is someone with hidden, unplumbed depths which I have yet to discover."
    if ayesha.love.max < 25:
        $ ayesha.love.max = 25
    return

label ayesha_event_02:
    "I know it's the kind of thing that everyone says, but I really am just walking down the street, minding my own business."
    "And that's when I hear the sound of people shouting and laughing out loud a little way up ahead."
    "Normally, I'd just check it out in passing, making sure to keep my head down and my eyes averted."
    "Hey, I'm not a coward - I just don't want to get dragged into something that could get out of hand."
    "But when I cast my gaze over what's actually going on, I see that it involves an instantly familiar face."
    "It's a couple of guys on the other side of the street, typical asshole jock types that never actually grew up."
    show ayesha angry
    "The problem is that the person they're shouting, on the same side of the street as me, is none other than Ayesha."
    "And as I get closer, I begin to hear what they're saying."
    "Shady guy" "Hey, shouldn't trolls like you be under a bridge or something?"
    "Handsome man" "Whoa, careful, man - she'll grind your bones to make her bread!"
    "Shady guy" "Ha ha...fee fi fo femme!"
    "I can see that Ayesha's trying as best she can to ignore them."
    "But she still winces at every insult, almost like it's a physical blow."
    "Like I already said, I'd usually just walk on by."
    "But can I really do that when it's someone I know on the receiving end?"
    menu:
        "Do nothing":
            "I guess that the answer is yes, I can."
            "Ayesha's a big girl - in fact, she's bigger than any girl I ever met before!"
            "Surely she can handle being hollered at by a couple of jerks in the street?"
            "It's with this thought in mind that I hang back and make sure that she doesn't see me."
            "Any moment I expect her to fire back with some insults of her own."
            "That or to simply shake her head in disgust and walk away from the guys with her dignity intact."
            show ayesha sad
            "But instead, I see her almost begin to shrink into herself as she shuffles slowly away."
            "And with each subsequent insult from the guys across the street, Ayesha huddles down further."
            "It's a sight that leaves me astonished and wondering if I made the right decision after all."
            "How can Ayesha be so confident and cocky in the wrestling ring, yet so meek in the real world?"
            "But by now, it's too late for me to step up and make the save."
            "So all I can do is shake my head and keep on walking."
        "Defend Ayesha" if hero.charm >= 20:
            $ ayesha.flags.defended = True
            if ayesha.love.max < 40:
                $ ayesha.love.max = 40
            "It's a pretty weird thing, to see someone so confident and cocky in a wrestling ring react like that."
            "But it doesn't take me long to remember that the real world is very different to the world of pro-wrestling."
            "And what Ayesha needs right now is for someone to step in like her tag-team partner would in the ring!"
            "That's why I don't hesitate to stride up to her side, making it clear to everyone that I'm with her."
            mike.say "Hey, Ayesha."
            mike.say "What's with these two pencil-dicked arseholes?"
            show ayesha surprised at startle
            "I'm sure to pitch my voice so it can be heard while gesturing over my shoulder at the guys in question."
            "At first Ayesha looks surprised to see me seemingly appear out of nowhere."
            show ayesha happy
            "But the look on her face soon turns into one of relief as she realises that I'm here to help."
            ayesha.say "Oh, hey, [hero.name]."
            ayesha.say "Am I ever glad to see you!"
            "In contrast, the looks on the faces of the two guys across the street couldn't be more different."
            show ayesha normal
            "Suddenly finding the odds evened up, they make a desperate effort to reassert their former dominance."
            "Shady guy" "Butt out, man."
            "Handsome man" "Yeah, let Queen Kong fight her own battles!"
            "I raise an eyebrow at this, looking first to Ayesha and then back at her abusers."
            mike.say "Whoa there, wait a minute."
            mike.say "You think I'm stepping in to save her?"
            "I chuckle and shake my head."
            mike.say "Nah, I'm doing it to save you two pricks!"
            mike.say "Because I'm pretty sure I could kick your asses."
            mike.say "But I KNOW that she could eat the pair of you alive."
            mike.say "Oh, and then she'd use your cocks for toothpicks - because that's how small they are!"
            "The first guy bristles at my tirade of insults, and makes to cross the road."
            "But his companion seems to have a sliver more brains in his head, and holds him back."
            "Shady guy" "What the hell, man?!?"
            "Handsome man" "We don't need this kind of hassle, dude."
            "The first guy looks like he's going to protest, but then he shrugs off his friend and nods."
            "I guess the prospect of beating up a complete stranger to get their hands on a woman finally dawned on them as being a bad idea."
            "They slope off down their side of the street, no doubt muttering conciliatory words to each other."
            $ ayesha.love += 10
            show ayesha b blush
            ayesha.say "Thanks, [hero.name]."
            ayesha.say "But you didn't have to do that..."
            mike.say "I know, Ayesha, I know."
            mike.say "I understand that you're a modern woman."
            mike.say "That you don't need to be rescued by a knight in shining armour and all that."
            mike.say "But I don't like people ganging up on my friends, you know?"
            show ayesha happy
            "Ayesha smiles at this, clearly embarrassed at my show of loyalty to her."
            "But then she looks me in the eye, the nervous quality returning to her voice as she speaks."
            ayesha.say "So..."
            ayesha.say "We...we are friends then?"
            "Ayesha smiles at this."
            "And the change on her face makes me feel a strange warm kind of fluttering in my chest."
    return

label ayesha_event_03b:
    play music "music/roa_music/2am.ogg" loop fadeout .5 fadein .5
    if ayesha.love.max < 60:
        $ ayesha.love.max = 60
    scene bg street
    show ayesha b date
    with fade
    "It's an unusually pleasant night, and so Ayesha and I decide to forget about a taxi."
    "Instead we choose to walk home along some of the more picturesque streets in my neighbourhood."
    "There's almost nobody else out at this hour, so we're alone most of the way."
    "And it's really nice to have Ayesha's arm hooked in mine the whole time too."
    "We're just chatting away, talking about everything and nothing in particular."
    "But then I notice we're passing the gates of a local cemetery."
    "I stop and smile at Ayesha, nodding towards the open gates."
    mike.say "Hey, Ayesha."
    mike.say "We should cut through here."
    "Ayesha looks like she wants to just keep on walking."
    "But she humours me all the same, stopping and looking at the gates."
    show ayesha b annoyed
    ayesha.say "I...I don't know about that, [hero.name]."
    ayesha.say "It looks pretty dark in there."
    ayesha.say "Might be safer to stay where there's streetlights."
    menu:
        "It's way faster this way.":
            "I shake my head, dismissing Ayesha's concerns."
            mike.say "Don't worry, Ayesha."
            mike.say "I've walked this way a thousand times."
            "By now I'm already halfway through the gates."
            "And not wanting to let go of me, Ayesha is forced to follow."
            mike.say "And anyway, you're a badass wrestler."
            mike.say "Nobody's going to mess with you!"
            scene bg cemetery with fade
            show ayesha date annoyed at right with moveinright
            "Walking between the headstones, I see that Ayesha's still nervous."
            "She shakes her head, but keeps on following me all the same."
            ayesha.say "It...it's not that, [hero.name]."
            ayesha.say "I'm not scared of people..."
            mike.say "Ayesha..."
            mike.say "You have to be kidding me!"
            mike.say "You're not really afraid of ghosts, are you?"
            "Now I can see embarrassment as well as fear on Ayesha's face."
            "But there's no denying it - she really is afraid of ghouls and ghosts!"
            ayesha.say "I...I might be!"
            "I start to laugh, about to make fun of Ayesha."
            "But a sound from further into the cemetery stops me dead."
            "It's weird, kind of like a long, low moan."
            "Just the kind of thing you'd hear if this were a horror film."
            show ayesha surprised at startle
            ayesha.say "[hero.name]..."
            show ayesha sad at right4 with move
            show fx question at right4
            ayesha.say "What was that?!?"
            "I love the fact that the unexpected sound makes Ayesha cling to me."
            "But maybe not how tightly she crushes me against her as she does so!"
            mike.say "Urgh..."
            mike.say "I...I don't know, Ayesha."
            mike.say "But it came from over there..."
            show ayesha sad at right with move
            "Almost dragging Ayesha behind me, I follow the direction of the sound."
            "It seems to be coming from some crypts a little way off of the path."
            "I weave between the headstones, narrowing it down to one with an open gate."
            "With a finger to my lip, I motion for Ayesha to keep quiet."
            "And then I lean through the doorway, using the torch on my phone to see inside."
            "The most I'm expecting to see is kids fooling around."
            show vincent teaser zorder 3 at top_mostleft, blacker
            show violaine zorder 1 at left, blacker
            with dissolve
            "But what's revealed is a pair of figures standing against the wall."
            "I can't see either of their faces, as one has it's back to me."
            "And it's also standing in front of the other."
            "In fact, it's looming over them - doing something to their neck!"
            hide vincent teaser
            show vincent teaser zorder 3 at top_mostleft
            with dissolve
            "Suddenly, the first figure spins around to face me."
            "In the light of my phone, I'm presented with a pasty, white visage."
            "Huge eyes stare at me from above gaunt cheekbones."
            "And red lips peel back from pointed teeth."
            with vpunch
            mike.say "Fucking hell, Ayesha!"
            mike.say "It's the Undead!"
            show fx question zorder 2 at top_mostleft
            "Vincent" "What?!?"
            "Vincent" "Where?!?"
            hide violaine
            show violaine zorder 4 at left5 with dissolve
            violaine.say "I think he means us, Vincent!"
            "Vincent" "Oh...I see...that's a little bit embarrassing."
            "Vincent" "And would you mind not shining that thing in my eyes too?"
            show ayesha at right5 with move
            "Ayesha moves further into the crypt, staring at the pair."
            ayesha.say "Y...you're not vampires?"
            "I can see now that the second figure is a goth girl."
            "She blinks at the light too, but nods a the same time."
            violaine.say "No, more's the pity!"
            show ayesha normal
            ayesha.say "And he wasn't drinking your blood?"
            "Vincent" "Eww, no."
            "Vincent" "Of course not - that'd be awful!"
            "Vincent" "Very unhygienic."
            "I finally feel like I can lower my phone."
            "With an awkward smile on my face, I try to explain myself."
            mike.say "Ah, sorry about bursting in on you just now."
            mike.say "We heard a strange sound and thought someone might be in trouble."
            mike.say "I'm [hero.name] and this is Ayesha."
            violaine.say "Oh, it's okay."
            violaine.say "It's nice to meet new people once in a while."
            "Vincent" "Yes..."
            "Vincent" "We don't have many friends - if you can believe that!"
            mike.say "Ah...yeah..."
            mike.say "Well, we'd better get going."
            mike.say "Maybe we'll see you guys around?"
            violaine.say "I hope so, [hero.name]!"
            "Violaine holds my eye for a second longer than necessary."
            "Which lets me get a good look at her for the first time."
            "And she's actually gorgeous, a real beauty."
            "The goth look only serving to make her all the more intriguing."
            "She smiles, clearly aware that I'm checking her out and liking the attention too!"
            ayesha.say "Come on, [hero.name]."
            ayesha.say "We really do have to go now!"
            "I let Ayesha bundle me out of the crypt."
            "But I can't help glancing back over my shoulder for one last glimpse of Violaine."
            $ ayesha.sub += 2
            $ game.flags.waitCemetery3some = TemporaryFlag(True, 1)
            $ Room.find("cemetery").unhide()
        "Fine":
            "I take a second glance through the gates."
            "It does look seriously gloomy in there right now."
            "Maybe Ayesha's right after all."
            "We could shave a couple of minutes off the walk."
            "But what's the point if it comes at the cost of getting mugged?"
            mike.say "Okay, Ayesha."
            mike.say "You've got a point."
            "Ayesha looks instantly relieved at this."
            "But as we resume our walk, I can't help wondering."
            "Was there something else behind her not wanting to walk through the cemetery at night?"
            $ ayesha.love += 2
    $ DONE["ayesha_event_03b"] = game.days_played
    return

label ayesha_event_03:
    if ayesha.love.max < 60:
        $ ayesha.love.max = 60
    ayesha.say "Hey, [hero.name]."
    ayesha.say "What's up?"
    mike.say "Hey Ayesha."
    mike.say "It's perfect beach weather today."
    mike.say "You want to come to the beach with me?"
    ayesha.say "I...I don't know..."
    mike.say "Aw, what?!?"
    mike.say "Come on, Ayesha - you'll have a great time, I promise!"
    "There's a silence on the other end of the line."
    "And I can almost hear Ayesha agonising over the matter."
    ayesha.say "Okay, [hero.name], if you say so..."
    mike.say "Great, Ayesha."
    mike.say "I'll see you there!"
    "As I put down the phone and gather my things, I still can't figure out just why Ayesha seemed so reluctant."
    "The thought is still bugging me as I wait for her to arrive in the car-park a short while later."
    "She practically owns the gym when she's there, and I've seen her in the wrestling ring too."
    "Why would the notion of hitting the beach bother her so much?"
    "But almost as soon as I see Ayesha walking towards me, all other thoughts disappear from my mind."
    "She's wearing a bathing-suit and very little else, her bag slung over her shoulder."
    "And she looks simply stunning, like something out of a dream - or a fantasy even!"
    "Though as she comes closer, I note that her face seems to reflect her mood over the phone."
    "So I choose to ignore that fact and try to cheer her up instead."
    scene bg beach
    show ayesha swimsuit
    with fade
    mike.say "Wow, Ayesha."
    mike.say "And I thought you looked good in your workout gear!"
    show ayesha swimsuit blush
    "Ayesha seems to be almost flustered by the compliment, clutching at her bag and refusing to meet my eye."
    ayesha.say "What are you talking about, [hero.name]?"
    ayesha.say "Everyone stares at me when I wear this thing in public."
    ayesha.say "I think it scares people - even the guys!"
    "I shake my head in sheer amazement at what Ayesha just said."
    hide ayesha
    show ayesha swimsuit normal
    mike.say "Ayesha, how could you even think that?"
    mike.say "If anyone's staring at you in that outfit, they're doing it in awe!"
    ayesha.say "Oh don't, [hero.name]."
    ayesha.say "I do look at my own reflection in the mirror, you know?"
    "I keep on shaking my head, not believing what she says."
    mike.say "Then you must have been looking in a busted mirror, Ayesha!"
    "I reach out and take hold of her hand."
    mike.say "Come on, you'll see how wrong you've got it!"
    "And with that, I pull her after me and onto the sand."
    "Ayesha allows me to lead her, and even to object when she tries to pick secluded spots for us to settle in."
    hide ayesha
    "Soon enough, I've found what I think is the perfect place for us to spread out our towels and claim as our own."
    "But when I kneel down to do just that, I get a face-full of sand for my troubles."
    mike.say "Arrgh!"
    "Luckily for me, not too much of it goes into my eyes, so I can still see what's going on."
    "Beefy guy" "Oops!"
    "Beefy guy" "Sorry about that, buddy."
    "I look up to see a typically burly beach jock towering over me."
    "He seems genuinely concerned and upset, admitting to being responsible for what just happened."
    mike.say "Shit..."
    mike.say "What happened?"
    "Beefy guy" "I was just jogging past, man."
    "Beefy guy" "Must have kicked up some sand!"
    "I could have gotten hot with the guy, really told him off for what he did."
    "But he basically just apologised and took total responsibility for the whole thing."
    "So I open my mouth, intending to let him off the hook..."
    "Beefy guy" "Wha..."
    "Beefy guy" "Oww...shit!"
    show ayesha swimsuit angry
    ayesha.say "Kick sand in MY date's face, huh?!?"
    ayesha.say "Let's see how tough you REALLY are!"
    "I can only watch as Ayesha steps up behind the poor guy and puts him in some kind of wrestling hold."
    "It looks incredibly painful, as though it hurts for him to move even a single muscle."
    ayesha.say "Apologise...NOW!"
    "Beefy guy" "Arrgh...I...I already did!"
    ayesha.say "Funny, I didn't hear you?"
    "Beefy guy" "Urgh...okay...okay..."
    "Beefy guy" "I'm sorry!"
    ayesha.say "That's more like it!"
    show ayesha swimsuit normal
    "And with that, Ayesha releases him, planting a kick up his ass as he turns to run."
    "She stands with her fists planted firmly on her hips, nodding with satisfaction as he goes."
    menu:
        "Tell Ayesha it was an accident":
            "I can't keep myself from laughing, no matter how hard I try."
            "And the moment that it bursts out of me, Ayesha turns around, a puzzled look on her face."
            ayesha.say "Huh?"
            ayesha.say "What's so funny?"
            mike.say "It was kind of an accident, Ayesha."
            mike.say "The guy didn't do it on purpose."
            mike.say "And he was saying sorry when you pounced on him!"
            "For about a minute, Ayesha stands as still as a statue."
            "She just stares at me, a look of utter embarrassment spreading across her face."
            "And then the spell breaks."
            "Her head flicks between me and the direction in which the poor guy fled."
            $ ayesha.sub += 10
            ayesha.say "But I just..."
            ayesha.say "I thought that..."
            show ayesha annoyed
            ayesha.say "Oh shit!"
            "It's then that I stop laughing, becoming instead concerned for Ayesha."
            mike.say "Hey, hey..."
            mike.say "It's okay, Ayesha."
            show ayesha sad
            ayesha.say "How can it be okay, [hero.name]?"
            ayesha.say "I just assaulted a guy for basically no reason!"
            "I shake my head, trying to dismiss her feelings of guilt."
            mike.say "It was just an honest mistake, Ayesha, that's all."
            mike.say "The guy should have stood his ground and told you as much."
        "Hide it from her":
            "I know full well that Ayesha just misread the situation completely."
            "But I'm not about to shoot her down when she came rushing to my aid like that."
            mike.say "Wow..."
            mike.say "Thanks, Ayesha."
            mike.say "You know, I didn't think that kind of thing actually happened for real!"
            $ ayesha.love += 5
            "Ayesha shakes her head as she helps me to my feet, still glaring after the poor guy."
            ayesha.say "The world can be a pretty cruel place, [hero.name]."
            ayesha.say "I know that much from personal experience."
            "I can't help staring deep into Ayesha's eyes as she says this."
            "Her voice is so filled with conviction and not a little pain."
            "It makes me wonder what in the hell happened to her in the past."
            "How could someone so strong and so beautiful have ever been vulnerable enough to get hurt?"
            mike.say "Well, I don't think that guy'll be back anytime soon!"
    mike.say "But anyway..."
    mike.say "It was pretty impressive from where I was standing!"
    show ayesha blush
    ayesha.say "R...Really?"
    mike.say "Sure, Ayesha."
    mike.say "The way you came to rescue me like that, well..."
    mike.say "It was pretty hot!"
    "Ayesha still looks as embarrassed as before."
    show ayesha happy
    "But now she can't help starting to smile, even laughing a little."
    ayesha.say "You know..."
    ayesha.say "Most guys don't like it when I do that."
    mike.say "Then I guess you're lucky that I'm not most guys!"
    "I lie down on the towels now spread on the sand, just waiting for us to relax."
    "Propping my head up on one arm, I pat the spot beside me."
    mike.say "Now..."
    mike.say "How about you come and guard me while I soak up some sun?"
    "Ayesha laughs and shakes her head at this."
    "But she doesn't hesitate to take me up on the offer..."
    return

label ayesha_event_04:
    if ayesha.love.max < 80:
        $ ayesha.love.max = 80
    show ayesha casual
    "Going to the cinema tonight was kind of a last moment decision for Ayesha and me, but I'm looking forward to it all the same."
    "The only problem is that it means neither of us has come out with any idea of just what we actually want to see."
    "This results in the pair of us standing around in the lobby, looking at the showing times and titles of what's on here."
    "It's a massive bonus if one of the posters within sight is for an actual movie we see listed."
    "Otherwise we have to resort to either guessing what a film is about, based on the title and the rating."
    "And before you say it, we do try to look them up on our phones."
    "But the signal is notoriously poor here, as is the free Wi-Fi too."
    "What can I say - I guess they're more interested in people watching the films than surfing the internet."
    "Anyway, we might have had some serious fun just choosing a movie at random."
    "But we're both afflicted with that condition unique to people trying to make the best impression they can..."
    ayesha.say "I don't know, [hero.name]."
    ayesha.say "Maybe you should be the one to choose?"
    mike.say "No, Ayesha, really."
    mike.say "It's fine for you to choose."
    show ayesha sad
    ayesha.say "But what if I choose something that sucks?"
    mike.say "Well...what if I choose something that sucks too?"
    show ayesha normal
    ayesha.say "It'll be fine, [hero.name]."
    ayesha.say "Please, I really want you to be the one to choose!"
    "I'm about to keep on arguing when I realise that we could be here all night."
    "Even if we end up seeing a lame movie, it has to be better than seeing nothing at all, right?"
    "So I nod my head and set myself to narrowing down the choices before me."
    "It seems like there are two movies starting pretty soon."
    "And choosing between two should make things that much easier."
    "The first movie is called 'Wigs and Witches'."
    "It's one of those serious, historical dramas, in this case about the Salem Witch Trials."
    "The second is 'The Exterminator'."
    "This looks like some kind of Sci-Fi thriller flick, about a time-travelling pest control agent from the future."
    "But which one would be Ayesha's kind of thing?"
    menu:
        "Sci-Fi thriller":
            "I sneak a quick glance at Ayesha as I struggle to make up my mind."
            "Does she really strike as the type to go in for a historical drama?"
            "I mean, she practically lives in the gym and moonlights as a professional wrestler!"
            "She has to be more into throwaway action films with a wafer-thin plot, doesn't she?"
            mike.say "I think we should see this one, Ayesha."
            show ayesha annoyed
            ayesha.say "'The Exterminator'?"
            ayesha.say "Really, [hero.name]?"
            show ayesha normal
            "But then she seems to remember our agreement, and just shrugs."
            show bg cinemaroom with fade
            "We hurry to buy the tickets, just making it to our seats in time for the trailers."
            "And as the film begins, I hope that I made the right decision!"
            "It doesn't take me long to realise where all of the money went when they made this film."
            "The special effects are pretty amazing."
            "And there whole thing feels like one long action scene from start to finish."
            "But almost the second it's over and the credits roll, I realise I don't remember a thing about the actual plot!"
            "As we leave the theatre, I can see that Ayesha isn't exactly grinning from ear to ear either."
            mike.say "Ah, what's up, Ayesha?"
            mike.say "Didn't you like the film?"
            "She curls her lip at the question, as if afraid to answer it."
            ayesha.say "If I tell you, do you promise that you won't be upset?"
            mike.say "Yeah, Ayesha, of course."
            mike.say "You can tell me - I won't get mad."
            "Ayesha nods and lets out a sigh before she speaks again."
            ayesha.say "It was...exciting, I suppose..."
            ayesha.say "But I really wished that we'd seen the other one instead."
            mike.say "I...I thought you'd be into that kind of thing, Ayesha."
            mike.say "If I'd known, I wouldn't have chosen it!"
            show ayesha happy
            "Ayesha actually smiles at my horror, starting to chuckle to herself."
            ayesha.say "Oh, [hero.name], that's kind of sweet!"
            ayesha.say "Dumb, but cute."
            ayesha.say "Just for the record - having muscles doesn't mean I don't have a brain too!"
            "I shake my head, embarrassed at the fact I misjudged Ayesha so badly."
            mike.say "I...erm...well..."
            mike.say "I'm sorry, Ayesha."
            mike.say "Please don't hold it against me!"
            show ayesha normal
            ayesha.say "It's okay, [hero.name]."
            ayesha.say "I suppose this is all just part of getting to know a person."
            show bg cinema
            "Walking out of the cinema, I find myself smiling too."
            "It seems there's depths to Ayesha that I haven't even begun to explore yet..."
        "Historical drama":
            "I sneak a quick glance at Ayesha as I struggle to make up my mind."
            "Does she really strike as the type to go in for a historical drama?"
            "But then it hits me that I'm just assuming she likes action films because of her appearance, nothing more."
            "And anyway, I'd prefer the historical drama myself, so I decide to be honest in my choice."
            mike.say "I think we should see this one, Ayesha."
            show ayesha annoyed
            ayesha.say "'Wigs and Witches'?"
            ayesha.say "Really, [hero.name]?"
            show ayesha normal
            "But then she seems to remember our agreement, and just shrugs."
            show bg cinemaroom with fade
            "We hurry to buy the tickets, just making it to our seats in time for the trailers."
            "And as the film begins, I hope that I made the right decision!"
            "Sure, it starts off slowly and the subject matter is pretty heavy stuff."
            "But it doesn't take long before I find myself getting drawn into the film in a big way."
            "There might not be any impressive special effects or people running away from explosions on offer."
            "And yet I can't help feeling that I'm lost in the world of witch-crazed colonial America."
            "But as the credits roll and we get up to leave the theatre, I'm already dreading Ayesha's reaction."
            "Which is why I'm amazed to see a smile plastered across her face as we stand in the lobby."
            $ ayesha.love += 10
            show ayesha happy
            ayesha.say "Thanks for picking that film. [hero.name]."
            ayesha.say "It was the one that I'd have chosen myself."
            ayesha.say "But I didn't want to look like I was being pushy!"
            mike.say "Really?!?"
            mike.say "I was worried that..."
            show ayesha angry
            "Ayesha narrows her eyes and cocks her head on one side as she regards me."
            ayesha.say "Let me guess, [hero.name]."
            ayesha.say "You assumed that I'd be into mindless action films, right?"
            mike.say "No...no, Ayesha."
            mike.say "I said I was WORRIED that you might be."
            mike.say "And now that worry's been proven wrong."
            show ayesha happy
            "Ayesha laughs at my desperate attempts to save face, and then takes hold of my hand."
            ayesha.say "Nice save there, smooth guy!"
            ayesha.say "Now let's get out of here before I find out what other worries you have about me!"
            show bg cinema with fade
            "Walking out of the cinema, I find myself laughing too."
            "It seems there's depths to Ayesha that I haven't even begun to explore yet..."
    $ game.pass_time(4, True)
    return

label ayesha_event_04b:
    call ayesha_event_04 from _call_ayesha_event_04
    $ game.active_date.score = 75
    $ game.room = "map"
    return

label ayesha_event_05:
    if ayesha.love.max < 100:
        $ ayesha.love.max = 100
    "I have to admit that when Ayesha surprised me with a call that I wasn't expecting, I had high hopes."
    "I was just waiting for her to say that she'd made last-minute plans to do something crazy and fun."
    "But my hopes were dashed pretty quickly, almost as soon as I heard the tone of her voice."
    ayesha.say "Ah..."
    ayesha.say "Hey, [hero.name]."
    mike.say "Hey, Ayesha."
    mike.say "You don't sound too good."
    mike.say "What's up?"
    "I hear Ayesha sigh on the other end of the line."
    ayesha.say "Is it really that obvious?"
    mike.say "Sorry, Ayesha."
    mike.say "But, yeah...it kind of is."
    ayesha.say "Damn it..."
    ayesha.say "I at least wanted to say hi before we got into it!"
    "Before I was just worried about Ayesha's mood."
    "But now she's got me concerned that whatever's eating her is to do with me too."
    "Or to be more specific, that it's to do with us as an item."
    mike.say "Is...is it something I've done, Ayesha?"
    mike.say "If it is then we can talk about it..."
    "As if sensing that I'm about to go into 'I can change' mode, Ayesha cuts me off."
    ayesha.say "No, [hero.name]!"
    ayesha.say "God no!"
    ayesha.say "It's nothing you've done, trust me."
    "She pauses, taking a deep breath before going on with what she has to say."
    ayesha.say "You've been great, really good to me."
    ayesha.say "And that's kind of why I wanted to ask for your advice."
    ayesha.say "I have to make a choice, and I want to talk to you about it."
    ayesha.say "I want to talk to someone that cares for me...okay?"
    mike.say "Sure thing, Ayesha."
    mike.say "Whatever you need - I'm already there!"
    show bg house with fade
    "I'm out of the door and on the way almost as soon as Ayesha and I agree on a place to meet."
    "I guess that I should be relieved that she's not wanting a serious discussion about our relationship."
    "But all the same, I'm genuinely worried about whatever it is that Ayesha actually wants to discuss."
    show bg street with fade
    "My guts churn the whole way there, solely out of concern for her, and not myself."
    "A fact that brings home to me just how much I've come to care for Ayesha in our short time together."
    show bg park with fade
    "By the time we meet up, I almost convinced that she's going to tell me she's found a lump or something as dramatic."
    show ayesha normal casual with dissolve
    mike.say "Ayesha, there you are!"
    mike.say "I got here as fast as I could."
    show ayesha sad
    "Ayesha shakes her head in confusion, making me instantly aware that I'm probably overreacting."
    show ayesha happy
    "And yet I can see from the way that she smiles, my concern is also an unexpected comfort to her."
    ayesha.say "Settle down, [hero.name] - I'm not dying or anything crazy!"
    show ayesha sad
    ayesha.say "Oh shit - is that what you thought this was about?!?"
    "All I can do is give a helpless shrug and an awkward smile of my own."
    show ayesha blush
    ayesha.say "[hero.name], that's so sweet!"
    show ayesha normal
    ayesha.say "But no, I really do just need your advice on something."
    "I swallow loudly, trying to feel like a serious adult that's here to offer sage advice."
    "Which is hard when Ayesha's just made me feel like a puppy that's too cute not to pet."
    mike.say "Ah...ahem..."
    mike.say "Okay, Ayesha - fire away."
    "Now it's Ayesha's turn to steel herself for what lies ahead."
    "She takes a deep breath and then looks me straight in the eye."
    ayesha.say "[hero.name], I've got an offer."
    ayesha.say "And it's one that I'm seriously considering too."
    "I wait for her to say more, but it soon becomes clear she's not going to."
    mike.say "Erm..."
    mike.say "An offer for what exactly, Ayesha?"
    "Ayesha slaps her forehead with one hand."
    show ayesha sad
    ayesha.say "Urgh..."
    ayesha.say "Of course - I haven't told you yet!"
    ayesha.say "You see how this thing's got me all mixed up?"
    "I nod, trying to seem as at ease with this as I can."
    "But the truth is that I'm just not used to seeing Ayesha this confused."
    show ayesha normal
    ayesha.say "You already know all about my wrestling."
    ayesha.say "But I've always dabbled in MMA on the side too."
    ayesha.say "It was more a way to keep my edge than something I was serious about."
    ayesha.say "Anyway, my record's pretty good - for an amateur, that is."
    ayesha.say "And I've been offered a spot in a local tournament."
    ayesha.say "It's nothing massive, but it could open doors for me in the future."
    "Ayesha pauses for a moment, and I can sense that the question she wants to ask me is coming."
    ayesha.say "Thing is, it's a risk - obviously."
    ayesha.say "And I wanted to ask what you think, [hero.name]."
    ayesha.say "Should I do it?"
    ayesha.say "Or should I stick to wrestling?"
    "The moment that I think of Ayesha in an MMA fight, my instinct is to say no."
    "In fact, the way my gut almost wrenches at the image of her being hurt is enough to take me by surprise."
    "But then I take a moment to consider the question a little more rationally, with less emotion colouring my vision."
    "And I begin to wonder if I'm wrong to be so against the idea, too protective of Ayesha."
    "After all, it's not like she's some delicate waif of a girl, now is it?"
    menu:
        "Tell Ayesha to go for it":
            $ ayesha.flags.mma = True
            "I want to tell Ayesha that this is a terrible idea and that she should just say no."
            "But if I did that, I know full well it'd be for my own selfish reasons."
            "Aside from the fact that she's built like an Amazon, Ayesha's not stupid."
            "She knows her own body and what she's capable of doing with it too."
            "So if I say anything other than yes, I'd be guilty of holding her back for my own sake."
            mike.say "The fact that someone scouted you means they think you're good enough."
            mike.say "So if it's what you want, then you should probably do the MMA thing."
            ayesha.say "Huh...really?"
            ayesha.say "I was almost sure you'd say no."
            mike.say "I won't lie, Ayesha."
            mike.say "The thought scares me more than a little..."
            mike.say "Well, to be honest, it scares me a lot!"
            ayesha.say "But then why..."
            "I hold up my hand, letting Ayesha know that I'm not done explaining myself."
            mike.say "Because I know you can handle yourself, Ayesha."
            mike.say "I know you won't get into anything that's beyond you."
            $ ayesha.love += 4
            show ayesha happy
            "I see a relieved smile begin to spread across Ayesha's face."
            ayesha.say "Thanks, [hero.name]."
            ayesha.say "It means a lot to know you believe in me that much."
            show ayesha normal
            mike.say "There's only one thing you have to promise me, Ayesha."
            ayesha.say "Ah...what's that?"
            mike.say "Just don't ask me to be your sparring partner, okay?"
            show ayesha happy
            "Ayesha shakes her head as she laughs at me."
            "And I'm pleased beyond words to see her happy once again."
        "Tell Ayesha not to do it":
            "A big part of me knows that I'm being selfish, that Ayesha can handle herself perfectly well."
            "But if something were to happen to her, I'd always have that weighing on my conscience."
            "Just because Ayesha's built like an Amazon, it doesn't mean that she's superhuman."
            "And if this is really how I feel, then I owe it to her to be totally honest."
            mike.say "Ayesha, I hate to say this."
            mike.say "But I really think doing the MMA thing would be the wrong choice."
            show ayesha angry
            $ ayesha.love -= 4
            ayesha.say "Oh...really?"
            ayesha.say "Yeah, I was pretty sure you'd say no."
            mike.say "I won't pretend that I'm not being selfish, Ayesha."
            mike.say "But just thinking about you in there..."
            mike.say "It scares me, Ayesha."
            mike.say "It scares me a lot!"
            "For a moment, it looks like Ayesha is going to open her mouth and fire straight back."
            show ayesha sad
            "But then I see the expression on her face change, as if the fight is draining out of her."
            "It hurts me to see her look so downcast all of a sudden, and I almost consider taking back what I just said."
            "Before I can even start to say the words, Ayesha nods and gives me a sad little smile."
            ayesha.say "I should be thankful that you're being honest with me, [hero.name]."
            ayesha.say "I know a lot of guys that'd have told me to go for it."
            ayesha.say "They'd do it just because they thought it was what I wanted to hear."
            ayesha.say "But you told me the truth, I guess because you really care about me..."
            mike.say "I'm sorry, Ayesha."
            mike.say "But I hate the idea of anyone hurting you."
            mike.say "Well...that and I was worried you might ask me to be your sparring partner..."
            $ ayesha.sub += 2
            show ayesha happy
            "Ayesha shakes her head as she laughs at me."
            "And I'm pleased beyond words to see her happy once again."
    return

label ayesha_event_06:
    if ayesha.love.max < 120:
        $ ayesha.love.max = 120
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Ayesha")
    if not result:
        $ hero.cancel_event()
        $ ayesha.love -= 5
        return
    ayesha.say "Hey, [hero.name] - are you free this afternoon?"
    mike.say "Ah, sure, Ayesha."
    mike.say "I hadn't made any plans that I can't ditch."
    mike.say "Especially if I'm ditching them for you!"
    "I picture Ayesha smiling at my blatant flattery, shaking her head a little."
    ayesha.say "Okay, okay - enough with the charm offensive!"
    ayesha.say "Thing is, there's a pretty big show in the park."
    mike.say "But that's today!"
    ayesha.say "Yeah, I know, I know."
    mike.say "A wrestling show?"
    ayesha.say "No, a damn dog show, [hero.name]."
    ayesha.say "Of course it's a wrestling show!"
    ayesha.say "In fact, it's a tournament, the best this town has."
    ayesha.say "They have it once a year, in the park and it's kind of a big deal."
    mike.say "And you scored tickets?"
    ayesha.say "Even better - I got booked to work it!"
    ayesha.say "I'm replacing someone that dropped out at the last minute."
    mike.say "That's great news, Ayesha."
    mike.say "I'm sure you'll smash it!"
    mike.say "And you want me to come and watch?"
    "At this, Ayesha pauses, taking a pretty deep breath."
    "It doesn't take a genius to know that there's going to be a catch of some kind."
    ayesha.say "Sure, [hero.name]."
    ayesha.say "Everyone that's booked gets a couple of free tickets - front row too."
    ayesha.say "Things is...I wondered if you'd help me out of a tight spot?"
    "Here it comes!"
    mike.say "Ah...what's that, Ayesha?"
    ayesha.say "Well, I was supposed to have a manager for this show."
    ayesha.say "But the guy that they hired just got injured somehow."
    ayesha.say "He won't be here, and I wondered if you might...you know, take his place?"
    menu:
        "Refuse to manage Ayesha":
            "Almost the same moment that I hear those words come out of Ayesha's mouth, my guts churn with genuine fear."
            "It wasn't so long ago that I stopped watching wrestling to I could have forgotten what happens to the managers at ringside."
            "Those guys are out there alone, supposed to have the back of the wrestler they're managing."
            "But the reality is that they have an entire crowd of crazed fans at their backs the whole time."
            "They're almost as hated as the villainous wrestlers, and a far easier target that's closer than the guys in the ring."
            "What does she even want from me?"
            "To be torn apart by a bunch of prepubescent fanboys and neckbeards that live in their mom's basement?!?"
            mike.say "I...I'm flattered, Ayesha, really I am."
            mike.say "But I wouldn't know the first thing about being a manager."
            ayesha.say "You sure, [hero.name]?"
            ayesha.say "I thought it'd be fun - you and me, out there together?"
            mike.say "No, Ayesha - I'd just get in the way!"
            $ ayesha.love -= 4
            "Ayesha sounds a little disappointed with my answer, letting out a gentle sigh."
            "But then she shrugs it off, as if pushing her feelings aside."
            ayesha.say "Okay, if that's how you feel, I won't twist your arm."
            ayesha.say "I don't need a manager to get heat."
            ayesha.say "And at least I'll have you in the front row to cheer me on!"
        "Agree to manage Ayesha":
            "I feel a pang of fear at the mere thought of being out there, in front of a baying crowd."
            "But then the image of Ayesha in her wrestling gear pops into my head, pushing everything else aside."
            "Did I mention just how good she looks in skin-tight spandex?"
            "I've been working up the courage to ask Ayesha to wear her wrestling gear just for me."
            "You know - alone and behind closed doors?"
            "But for now, I'll settle for walking down to the ring by her side while she's dressed like that!"
            mike.say "Wow, Ayesha - that sounds like a great idea!"
            ayesha.say "Really, you will?"
            $ ayesha.love += 4
            ayesha.say "Wow, thanks, [hero.name]."
            ayesha.say "That's a weight off of my mind!"
            mike.say "Don't you worry about a thing, Ayesha."
            mike.say "I'll be your eyes and ears at ringside - just you wait and see!"
            ayesha.say "Don't worry about anything either."
            ayesha.say "You won't have to do too much of anything."
            ayesha.say "Your job is basically to follow me to the ring."
            ayesha.say "Well, that and look a little seedy - you know, sleazy?"
            mike.say "I think I can manage that!"
            $ ayesha.flags.manager = True
    ayesha.say "Okay, so that's sorted."
    ayesha.say "Now get your ass down here as soon as you can."
    ayesha.say "My first match is in less than an hour!"
    mike.say "Shit, really?!?"
    mike.say "I'm already on my way!"
    show bg house with fade
    "And I'm not joking either, as I'm already grabbing what I need and heading for the door."
    show bg park with fade
    "By the time I arrive at the park, I'm an exhausted bag of nerves, sure that I'm already too late."
    "The place isn't hard to find, as I quickly spot a wrestling ring surrounded by rows of seating."
    "And there's not likely to be more than one of those in the park today, now is there?"
    "I make my way over to the barriers that encircle the makeshift arena, looking for the way in."
    "But then I see a snaking queue of people in wrestling T-shirts, an obvious clue as to where I can find it."
    if not ayesha.flags.manager:
        "I join the back of the queue, checking my watch and praying that I haven't missed Ayesha's first match."
        "It seems to take forever for me to reach the front, and when I do, I remember that I don't have a ticket on me."
        "Doorman" "Ticket please?"
        mike.say "Ah, I'm a friend of Ayesha's."
        mike.say "She's sorting out my ticket."
        "Doorman" "Name?"
        mike.say "[heroname]."
        mike.say "[heroname] [hero.family_name]."
        "Doorman" "Yeah, I got you down here."
        "He waves me through the gate, handing me a ticket as he does so."
        "I offer what I think is a pleasant enough smile in return."
        "It's then I realise that the fans around me are frowning and shaking their heads."
        "For a moment I think they're just jealous of me getting a freebie and too rude to keep it to themselves."
        "But then I remember that Ayesha's supposed to be one of the bad guys, a heel wrestler."
        "And I just outed myself as one of her friends!"
        "Lowering my head, I hurry off in search of my seat."
        "I soon find that Ayesha wasn't lying - it's right on the front row."
        "As I sit down, I'm already vowing to keep my voice down and just watch the show."
        "After all, the last thing I want is to be lynched by a mob of angry fans!"
        "But for all of my promises to myself, it all goes out the window the moment Ayesha's music plays over the PA."
        "Glancing back over the crowd, I see her emerge from behind the curtain and stride down the aisle to the ring."
        "And from there, I forget all about keeping my allegiance hidden from those around me."
        show ayesha happy fight with moveinright
        "There she is, my Amazon, my goddess in spandex."
        "She's here to take care of business."
        "She's going to kick ass!"
        "I don't know if Ayesha hears me bellowing over all the other fans in attendance."
        "But as she walks past the barrier in front of me, I see her catch my eye."
        $ ayesha.love += 2
        "It lasts no more than a second, and then she gives me a single wink."
        "And that's it, I can feel my heart hammering in my chest."
        "I feel like a kid again, watching weekend afternoon wrestling and screaming at the TV!"
        "Now I just don't care what the fans to either side of me think."
        "I'm hollering for Ayesha, and they can go suck it!"
        "I watch as she climbs the stairs and steps between the ropes."
        "The rest is a blur of cheering, booing and my own rollercoaster of emotions."
        "I'm up with every move that Ayesha makes and down each time she's on the receiving end."
        "She dominates her first opponent, crushing the girl with a running powerslam."
        "The second gives Ayesha more of a fight, but succumbs to her bear-hug."
        "Which makes me feel oddly jealous..."
        "But in her third-round bout, Ayesha seems to have met her match."
        "This girl is smaller, but the crowd's right behind her from the get-go."
        "Somehow she always seems able to outsmart Ayesha, or counter her moves at just the right moment."
        "Then, in the dying moments of the match, Ayesha wraps her arms around her opponent's waist."
        "The helpless girl is driven, head-first into the mat, with a German suplex."
        "I hear the sound of the referee hammering the canvas."
        "One...two...three!"
        "Music plays, and for a moment I'm elated."
        "But then I realise it's the other girl's music, not Ayesha's."
        "What happened?"
        "Who screwed up?"
        "The smaller girl gets shakily to her feet as the referee lifts her arm in victory."
        "No way - he counted Ayesha's shoulders down, not her opponent's!"
        "This is bullshit!"
        "This is the greatest injustice in the history of humankind!"
    if ayesha.flags.manager:
        "I walk straight to the front of the queue, trying to ignore the indignant looks this earns me."
        "Instead I keep my eyes focused on the guys working the gate, waving a hand for their attention."
        "Doorman" "Can I help you?"
        mike.say "I'm with Ayesha."
        mike.say "I'm her..."
        "Before I can say the word, I remember that we're the bad guys and I'm standing next to the fans."
        "So I lean forwards and try to hiss the word at a volume that only the doorman will hear."
        mike.say "I'm her manager!"
        "Doorman" "Name?"
        mike.say "[heroname]."
        mike.say "[heroname] [hero.family_name]."
        "Doorman" "Yeah, I got you down here."
        "He waves me through, pointing the way backstage."
        "I almost stumble over Ayesha as I wander through the dressing room."
        "But then she stands up, pulling on the last of her wrestling gear and getting ready to lace her boots."
        show ayesha happy fight
        $ ayesha.love += 4
        ayesha.say "Hey, [hero.name] - you made it!"
        mike.say "H...hey, Ayesha!"
        "I can hear the tremble in my voice, and my heart beating in my ears."
        "You see I've never been this close to Ayesha in her costume before now."
        "Dry-mouthed, I gulp at the sight of her - my Amazon, my goddess in spandex."
        show ayesha normal fight
        ayesha.say "Don't worry, [hero.name]."
        ayesha.say "It's okay - everyone's nervous the first time!"
        mike.say "Wha...what?"
        ayesha.say "The first time you go out and perform in front of a crowd."
        ayesha.say "But you don't have to worry about anything - just follow my lead, okay?"
        mike.say "Yeah, Ayesha - sure thing!"
        "I nod, recalling how the villainous managers I've watched used to behave."
        mike.say "You're sure you don't want me to insult the crowd, or interfere in the match?"
        ayesha.say "The first one, use your judgement."
        ayesha.say "Trust me, you'll know if it's right or not."
        ayesha.say "And the second - no way!"
        ayesha.say "You just leave all the action in the ring to me, yeah?"
        "I nod for a second time, and then someone calls her name."
        ayesha.say "Come on, manager - we're up!"
        "The next thing I know, we're standing behind the curtain as Ayesha's music starts to play over the PA."
        "What follows is a blur of colour, noise and emotion."
        "Before I could only see a wrestling ring and rows of folding chairs."
        "But as we walk through the curtain and down the aisle to the ring, it becomes so much more."
        "Somehow it's been transformed into an arena of dreams, a theatre of physical combat."
        "When we reach the ringside, Ayesha nods for me to stay where I am."
        "Then she catches my eye as she climbs into the ring."
        "It lasts no more than a second, and then she gives me a single wink."
        "And that's it, I can feel my heart hammering in my chest."
        "Now I just don't care what the fans behind me think or say."
        "I become a one-man chorus, cheering for my charge."
        "I'm up with every move that Ayesha makes and down each time she's on the receiving end."
        "She dominates her first opponent, crushing the girl with a running powerslam."
        "The second gives Ayesha more of a fight, but succumbs to her bear-hug."
        "Which makes me feel oddly jealous..."
        "But in her third-round bout, Ayesha seems to have met her match."
        "This girl is smaller, but the crowd's right behind her from the get-go."
        "Somehow she always seems able to outsmart Ayesha, or counter her moves at just the right moment."
        "Then, in the dying moments of the match, Ayesha wraps her arms around her opponent's waist."
        "The helpless girl is driven, head-first into the mat, with a German suplex."
        "I hear the sound of the referee hammering the canvas and my own hand thumping the ring apron."
        "One...two...three!"
        "Music plays, and for a moment I'm elated - I turn to face the baying fans in triumph."
        "But then I realise it's the other girl's music, not Ayesha's."
        "What happened?"
        "Who screwed up?"
        "The smaller girl gets shakily to her feet as the referee lifts her arm in victory."
        "No way - he counted Ayesha's shoulders down, not her opponent's!"
        "I call the result bullshit, curse the referee for being an incompetent bastard."
        "And then I let Ayesha lean her weight on me as we make our way backstage to the jeering of the fans."
    show ayesha normal fight
    "After the matches are all over and the winner of the tournament has been crowned, I find Ayesha in the locker-room."
    show ayesha happy fight
    "She looks tired and more than a little beaten up, but all the same, she smiles at the sight of me."
    show ayesha normal fight
    ayesha.say "Hey, [hero.name]."
    ayesha.say "Be honest - how did I look out there?"
    menu:
        "Treat the matches as real" if not ayesha.flags.manager:
            call ayesha_event_06_manager_postgame from _call_ayesha_event_06_manager_postgame_1
        "Treat the matches as \"real\"" if ayesha.flags.manager:
            "Deciding to play along a bit, I dig deep for what ever dribble of acting talent I had long since buried."
            call ayesha_event_06_manager_postgame from _call_ayesha_event_06_manager_postgame_2
        "Treat the matches as fake":
            mike.say "You were great, Ayesha, really great."
            mike.say "Hell, you even made me believe that you were an evil bitch!"
            $ ayesha.love += 2
            show ayesha happy fight
            "Ayesha laughs out loud at my words, clearly amused by what I just said."
            ayesha.say "How do you know that I'm not putting on an act the rest of the time?"
            ayesha.say "Maybe the only time I'm the real me is in the wrestling ring."
            ayesha.say "You ever consider that, huh?"
            mike.say "You know, Ayesha, I never did until you just said so."
            mike.say "Maybe I should watch my step around you - in case you put those moves on me too?"
            "Ayesha raises a single eyebrow at this, her smile becoming almost wicked."
            ayesha.say "You make it sound like that's something you'd like..."
            mike.say "Aw..."
            if ayesha.flags.manager:
                mike.say "You mean that you'd turn on your own manager?"
            else:
                mike.say "You mean that you'd turn on me?"
            "Getting up and walking over to where I stand, Ayesha leans in close."
            if ayesha.flags.manager:
                ayesha.say "I can fire you any time I like."
                ayesha.say "So you'd better do your job to MY satisfaction..."
                $ ayesha.love += 2
                $ ayesha.sub -= 4
            else:
                "I can see an amused spark in her eyes."
                ayesha.say "I dunno, I can imagine a few fun ways that could turn out."
                $ ayesha.sub -= 2
    "She kisses me lightly on the lips, lingering for a moment to enjoy the sensation."
    "And then she does it again, longer this time and with a release of tension that I swear I can feel too."
    "When the kiss is over, she lets out a satisfied sigh."
    ayesha.say "Of course, the REAL fun always happens at the party after the show..."
    return

label ayesha_event_06_manager_postgame:
    mike.say "You were great, Ayesha, really great."
    mike.say "I don't know what the hell that referee was thinking in the last match!"
    "The earnest manner in which I say this seems to make Ayesha sit up and pay attention."
    "She raises her eyebrows and looks at me with genuine interest."
    ayesha.say "Is that so?"
    mike.say "You bet it is, Ayesha!"
    mike.say "He should be stripped of his stripes!"
    mike.say "Or whatever it is that lets a referee...referee!"
    "Ayesha makes a snorting sound, and then bursts into laughter."
    $ ayesha.love += 4
    show ayesha happy fight
    ayesha.say "Oh, [hero.name], that's so funny!"
    ayesha.say "I know that you know this is all a show."
    ayesha.say "But you pretending to be some dumb fan that doesn't..."
    ayesha.say "That's cheered me up SO much!"
    "I feel my cheeks begin to burn with humiliation."
    "But I manage to force a smile onto my face and laugh along with Ayesha."
    "Maybe it's better to let her think that was a joke than make a complete fool of myself!"
    "Ayesha doesn't seem to notice however, as she gets up and walks over to where I'm standing."
    return

label ayesha_event_07:
    if ayesha.love.max < 130:
        $ ayesha.love.max = 130
    show ayesha
    ayesha.say "You actually want to go and wander around the mall?"
    ayesha.say "Are you sure, [hero.name]?"
    ayesha.say "I thought that was something only kids did?"
    mike.say "I don't mean hanging around and comparing Pokemon with the local teenagers, Ayesha!"
    mike.say "More like taking a leisurely stroll around the place."
    mike.say "You know, just spending some time together?"
    ayesha.say "Okay, [hero.name]."
    ayesha.say "If you say so..."
    "I feel a little puzzled as we wrap up the call after agreeing a time and place to meet."
    "I guess I just assumed that everyone knew taking a walk around the mall was a thing."
    "But maybe Ayesha just never did that kind of thing back when she was a kid?"
    "Which I suppose is all the more reason for me to introduce her to it now."
    "When I meet up with Ayesha a short while later, I can instantly see that she's still not at ease with the idea."
    "And so I put on my best smile in the hope of showing her that this is a perfectly normal thing to be doing."
    mike.say "Hey, Ayesha."
    mike.say "Thanks for letting me talk you into this."
    show ayesha happy
    ayesha.say "Ah...hey, [hero.name]."
    ayesha.say "I suppose it's good to try something new, right?"
    mike.say "Sure, Ayesha, sure it is."
    mike.say "Say, why don't we go grab a coffee?"
    show ayesha normal
    "As we start our stroll around the mall, Ayesha still seems visibly nervous."
    "She glances around and hesitates before speaking, as though she fears something unexpected will happen."
    "I know that she's trying her best to enjoy herself, but is that going to be enough?"
    "Maybe I need to step up and make sure this thing doesn't go south before it's too late..."
    menu:
        "Talk about yourself":
            mike.say "I still can't believe that you didn't do this when you were younger, Ayesha!"
            mike.say "When I was a teenager, we spent practically every minutes of free time we had there."
            "Ayesha gives me a pained smile, shaking her head as she does so."
            ayesha.say "If you say so, [hero.name]."
            ayesha.say "I guess that I was just more into..."
            mike.say "Boring stuff?"
            mike.say "Yeah?"
            mike.say "Am I right?"
            $ ayesha.love -= 10
            "I cut Ayesha off before she can finish what she was about to say."
            "It's a shitty thing to do, believe me, I know that."
            "But I'm still worried that she's going to bring the whole thing down without realising it."
            "That's why I feel like I have to step in and kind of throw shade on what she's saying."
            show ayesha sad
            ayesha.say "I don't know about that..."
            mike.say "Don't worry about it, Ayesha."
            mike.say "I was never one of the cool kids either."
            mike.say "But at least I knew where the best places were to hang out."
            mike.say "You must have been some kind of uber geek back in the day!"
            "Ayesha's smiles now looks more pained than ever, almost like it's stuck onto her face."
            ayesha.say "Ha...yeah..."
            ayesha.say "I must have been a real sad case..."
            mike.say "But that was then, Ayesha."
            mike.say "And this is now."
            mike.say "You can still make up for lost time, you know?"
            "Ayesha lets out a weary sigh before answering my question."
            show ayesha normal
            ayesha.say "If you say so, [hero.name]..."
        "Ask her what's wrong" if hero.charm >= 50:
            mike.say "Ayesha, I really did mean it when I said I was grateful you came here."
            mike.say "But all being said, you don't seem to be enjoying yourself."
            mike.say "Would you prefer we went somewhere else instead?"
            show ayesha annoyed
            ayesha.say "Ah, it's just me, [hero.name]."
            ayesha.say "And...well...if I tell you..."
            ayesha.say "You'll think it's stupid."
            show ayesha normal
            "I shake my head at this, wanting Ayesha to feel she can open up to me."
            mike.say "I won't, Ayesha - I promise."
            show ayesha sad
            ayesha.say "Okay, if you insist..."
            ayesha.say "I told you I never hung out in places like this, yeah?"
            ayesha.say "Well, it was kind of because I never had any friends to hang out with."
            "Ayesha's confession takes me by complete surprise."
            "I find it almost impossible to imagine her having been some kind of loner."
            mike.say "Really?"
            "Ayesha nods silently."
            "Her smiles becomes sad even as I look on."
            ayesha.say "I had one person that I could call a friend when I was a kid."
            ayesha.say "And when we spent time together, we were studying or reading in the library."
            "For a moment I can't actually square this image with the girl that I see before me."
            "Understand that I'm not trying to say that Ayesha comes over as anything less than intelligent."
            "But she's such an intimidating physical presence."
            "A library just doesn't suggest itself as her natural habitat."
            mike.say "I'm sorry, Ayesha."
            mike.say "I didn't mean to make you uncomfortable."
            ayesha.say "I know that, [hero.name]."
            ayesha.say "And I know I should try to get out of my comfort zone."
            mike.say "Well, I'm not used to hanging out in libraries either, Ayesha."
            mike.say "So maybe we should make that the venue for our next date?"
            show ayesha happy
            "I see a little of the sadness drain from Ayesha's smile at this."
            "She looks at me sideways, raising her eyebrows as she does so."
            ayesha.say "I don't know, [hero.name]."
            ayesha.say "Maybe you're not cool enough for the library!"
    "The rest of the time we spend at the mall seems to make up for our first, faltering steps."
    "And while I sense that Ayesha's still not totally at ease with the place, she makes an effort to enjoy herself all the same."
    "I can't help thinking that my words have really sunk in, that she's taken them to heart."
    "I'm not sure that Ayesha's discovered a wonderful new place to come and spend her free time."
    "But I do hope that she might not be so hesitant to return here in the future, should I make the suggestion."
    return

label ayesha_event_08a:
    if ayesha.love.max < 155:
        $ ayesha.love.max = 155
    scene bg gym
    "I should have been hitting the gym for my regular workout right about now."
    "But Ayesha catches me before I make it into the guys locker-room to change."
    show ayesha casual
    ayesha.say "Hey, [hero.name]..."
    ayesha.say "Get geared up and come find me in the sparring gym!"
    "I spin around on my heel, taken completely by surprise."
    mike.say "Huh?"
    mike.say "What for, Ayesha?"
    mike.say "I was just going to work-out!"
    show ayesha annoyed
    "Ayesha shakes her head at this."
    "And she crosses her arms over her chest too."
    "All of which tells me she means business!"
    ayesha.say "Are you my manager or not, [hero.name]?"
    ayesha.say "Because I need a certain level of commitment from my team!"
    ayesha.say "Don't tell me that you're going to let me down, are you?"
    "Now I'm the one shaking my head."
    "Because the last thing I want is to let Ayesha down."
    "And who knows, this might be an even better work-out than mine."
    "Plus I get to be all 'hands-on' with Ayesha too!"
    mike.say "Ah...yeah, Ayesha..."
    mike.say "I mean no - I won't let you down!"
    mike.say "I'll be there as soon as I get changed."
    hide ayesha with moveoutleft
    scene bg gym at blur(16), dark with dissolve
    "Ayesha nods and strides away, leaving me to hurry into the locker-room."
    "I hastily get changed and stuff my things into a locker."
    scene bg gym with dissolve
    show ayesha sport at mostright4 with dissolve
    "And then I almost run to the place where I know Ayesha will be waiting."
    "She doesn't see me as I walk in, as her back is turned."
    "I open my mouth to announce my presence."
    "But the words die in my mouth as I see what Ayesha's doing."
    "She's wearing the same spandex she always does in the gym."
    "And it's doing an amazing job as she stretches and warms up."
    "I can't help standing there in silence, just watching."
    "The combination of muscles and feminine curves - it's incredible!"
    "Sometimes I think I could just stand and watch Ayesha flex forever..."
    show ayesha blush
    show fx exclamation at mostright4
    ayesha.say "[hero.name]!"
    ayesha.say "Are you just going to stand there staring?"
    hide fx
    show ayesha angry
    ayesha.say "Get your ass over here!"
    mike.say "Oops..."
    mike.say "Sorry, Ayesha!"
    mike.say "I'm coming, I'm coming..."
    show ayesha at center
    "I scurry over to the mats where Ayesha's waiting."
    "She's all limbered up by now, ready to go."
    "She's even rubbing her hands together!"
    show ayesha normal
    ayesha.say "Okay, coach..."
    ayesha.say "Here's the deal!"
    ayesha.say "I feel like I need to work on my grappling game."
    ayesha.say "Specifically take-downs and floor-work, right?"
    "I nod, trying to look like I'm taking all of this in."
    mike.say "And how can I help with that, Ayesha?"
    mike.say "I mean, I've watched some pro-wrestling on TV."
    mike.say "But I'm not exactly a world-class grappler."
    show ayesha happy
    "Ayesha smiles at this, curling one side of her mouth."
    "And I can't say that I really like the look in her eyes either!"
    ayesha.say "Don't worry about being competitive, [hero.name]."
    ayesha.say "What I need is practice and a willing body, that's all."
    ayesha.say "Just lend me yours for a while - promise I won't break anything!"
    "I start to back off out of sheer instinct when I hear this."
    "And I'm holding my hands up in a gesture of surrender already."
    show ayesha annoyed
    "But at the same time, Ayesha drops into a fighting stance."
    show ayesha at right5 with move
    "She spreads her legs and lowers her centre of gravity."
    show ayesha at left5 with move
    "And to be perfectly honest, I'm not sure what happens next."
    show ayesha at center with move
    "She moves one way and I try to leap in the other."
    hide ayesha
    "But then she's behind me in the blink of an eye."
    "I feel her arms wrap around my waist."
    "And then the room turns upside down!"
    with vpunch
    with vpunch
    show layer master at blur
    "The next thing I know, the floor hits me in the face."
    "Or maybe I hit the floor - it's hard to tell!"
    mike.say "Urgh..."
    mike.say "I...I..."
    show layer master at blur(5)
    mike.say "Ayesha..."
    "As if in answer to my call, I feel someone grab my arms."
    show layer master at blur(0)
    with hpunch
    "Then a weight drops onto the middle of my back."
    "And I feel like I'm being folded in half!"
    mike.say "Aaargh!"
    mike.say "What the hell?!?"
    mike.say "What's happening to me?!?"
    show ayesha close sport angry
    ayesha.say "Suck it up, cupcake!"
    ayesha.say "This is the Camel Clutch."
    ayesha.say "And it's just for starters!"
    show layer master at blur(15)
    with hpunch
    with hpunch
    with hpunch
    "Ayesha leans back, and I feel like I'm trapped in a rowing machine."
    "I swear that I can hear tendons stretching and bones creaking."
    "Any moment I think that I'm going to pass out."
    show ayesha close normal
    ayesha.say "Okay..."
    ayesha.say "Time to change it up..."
    show layer master at blur(8)
    "A moment later, Ayesha releases me from the hold."
    "But I only have time to take a single gasping breath."
    "Because then she slides over my prone form and grabs my legs."
    "I'm unceremoniously flipped onto my back as she ties me up again."
    "This time Ayesha has her legs entwined in mine."
    "And she's slapping her hands on the mats to gain leverage."
    show ayesha close angry
    ayesha.say "Figure Four leg-lock, sucker!"
    ayesha.say "Iconic, classic and lethal!"
    mike.say "Yeah, Ayesha..."
    show layer master at blur(0)
    mike.say "I believe you!"
    mike.say "Please...please don't break my legs!"
    show ayesha close happy
    "Ayesha laughs in triumph, but she doesn't show me any mercy."
    show ayesha close angry with vpunch
    "If anything, she applies even more pressure than before."
    "I'm slapping my hands on the matt and begging."
    "But Ayesha's well and truly in the zone."
    "I don't know if she can even hear me pleading for release!"
    show ayesha close annoyed
    "Without warning, Ayesha moves again."
    "Even in my current state, I'm not totally dumb."
    "I know full well that she's not letting up on me."
    "So I roll onto my belly and crawl for all I'm worth!"
    with vpunch
    "I make it maybe a metre before Ayesha pounces on me again."
    "She scoops up my legs and seems to tie them in a knot."
    with vpunch
    "Then she straddles my back and sits down hard."
    "This feels like the first hold that she put on me."
    "But it's all going on at the other end of my body."
    show layer master at blur(10)
    show ayesha close angry
    with hpunch
    with vpunch
    with hpunch
    ayesha.say "Texas Clover-Leaf!"
    ayesha.say "There's no escaping this one, [hero.name]!"
    "Ayesha leans back, bending my spine as she does so."
    "I'm beyond crying for mercy by now."
    "All I can do is slap my hand weakly on the matt."
    show layer master at blur(5)
    show ayesha close happy
    "Finally Ayesha breaks the hold."
    "I crumple into a heap on the floor, unable to move."
    show ayesha -close
    "She stretches and flexes her muscles, looking pleased with herself."
    mike.say "Ah...Ayesha..."
    show layer master at blur(0)
    mike.say "Did I do okay?"
    "My voice is half smothered by the matt."
    show ayesha sad
    "And I must look pretty awful, as Ayesha's eyes go wide."
    "All of the bravado seems to drain out of her as she hurries over to me."
    ayesha.say "Ah, hell..."
    show fx drop
    ayesha.say "I'm sorry, [hero.name]."
    ayesha.say "I get carried away like this sometimes."
    ayesha.say "Are you going to be okay?"
    hide fx
    "I wince as Ayesha helps me up off the matt."
    "But I nod and do my best to tough it out."
    "I don't want to look like a total wimp in front of her."
    mike.say "Ooh..."
    mike.say "I'll be okay, Ayesha."
    mike.say "It probably looks worse than it feels!"
    mike.say "Did I help your training?"
    mike.say "Because that's the important thing."
    "Ayesha keeps on supporting me as I hobble towards the door."
    "And I can see that she's feeling more than a little guilty."
    ayesha.say "Maybe we keep your role from being physical in future, [hero.name]?"
    ayesha.say "After all, you're my manager - not my coach!"
    "I nod and smile, enjoying Ayesha's fussing over me."
    "It's not something that I should be exploiting for too long."
    "But milking it for just a little while can't hurt."
    "And after all the punishment I just took, I think I deserve it!"
    return

label ayesha_event_08b:
    show ayesha
    mike.say "Hi, Ayesha, do you want to go out with me tomorrow evening?"
    show ayesha sad
    ayesha.say "Oh..."
    ayesha.say "I'm sorry [hero.name], but I have something plan tomorrow night."
    ayesha.say "There's a pro-wrestling show and I want to watch how it goes."
    show ayesha happy
    ayesha.say "But hey, why won't you come with me?"
    mike.say "Yeah, great idea Ayesha, I'll go with you!"
    hide ayesha
    $ hero.replace_activity()
    $ hero.calendar.add(game.days_played + 1, DateAppointment(20, "ayesha", "Wrestling show (Ayesha)", "ayesha_event_08b_date", "missed_ayesha_event_08b_date"))
    return

label missed_ayesha_event_08b_date(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Ayesha is going to be mad."
        $ ayesha.love -= 10
    $ DONE.pop("ayesha_event_08b", None)
    $ storytracker.refresh()
    return

label ayesha_event_08b_date(appointment=None):
    if ayesha.love.max < 155:
        $ ayesha.love.max = 155
    scene bg street
    show ayesha casual
    with fade
    "Being with someone always works best when you have something in common, like a shared interest."
    "But sometimes you find that your other half is heavily into something that you're not into yourself."
    "At times like that you really can't just choose to ignore it and hope that it'll go away."
    "Because it won't - your partner's not going to give up their passions just to keep you sweet."
    "And if you want to keep them sweet, you're going to have to suck it up and indulge them."
    scene bg arena at flip, dark, center, zoomAt (2.5, (-300, 1020))
    show ayesha casual normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "Which is exactly how I've ended up sitting in the front row at a local pro-wrestling show."
    "Ayesha's into the sport...or entertainment...or whatever, and she's dragged me along with her."
    "In fact, she's so into it that she's a wrestler herself!"
    "But tonight she's told me that she's just a regular fan."
    mike.say "You're sure you're not going to wrestle tonight, Ayesha?"
    mike.say "Because I've seen some wrestling in my time."
    mike.say "And I know they like to surprise the audience, yeah?"
    show ayesha happy at startle
    "Ayesha lets out a snort of laughter and shakes her head."
    ayesha.say "You mean a swerve, [hero.name]?"
    ayesha.say "Nah - don't worry about that."
    ayesha.say "I'm just here to watch and soak up the atmosphere, that's all!"
    "I nod and let the matter drop."
    "But I'm not completely convinced."
    "Part of me thinks we're going to be jumped at any moment."
    "That somebody's going to come at me swinging a folding chair."
    scene bg arena at flip, dark, dark, center, zoomAt (2.5, (-300, 1020))
    show ayesha casual normal at dark, center, zoomAt(1.5, (640, 1040))
    with fade
    "Before I can share my concerns with Ayesha, the lights go down."
    play music "music/TeknoAXE/simple_metal.ogg" loop fadein .5
    "And then loud rock music starts to play over the PA system."
    show ayesha happy at startle with dissolve
    "The people sitting around us start to go crazy - Ayesha too!"
    show ayesha normal
    "All of this makes me feel like I'm at a rock concert, rather than a sporting event."
    "I watch as a guy in a suit walks down the aisle."
    "He has a microphone, so I assume he's the ring announcer."
    "My suspicions are confirmed when he climbs into the ring and starts the show."
    "MC" "Ladies and gentlemen..."
    "MC" "Welcome to Pro Wrestling BANG!"
    "MC" "Our first contest is scheduled for one fall!"
    "Crowd" "ONE FALL!"
    with vpunch
    "I jump in my seat as the entire crowd shouts the words together."
    show ayesha happy at startle
    "Ayesha notes my surprise and chuckles, clearly amused."
    "MC" "Introducing first, weighing in at one hundred and thirty pounds..."
    show ayesha normal
    "MC" "The Muay Thai Mistress..."
    "MC" "Magrat!"
    "Suitably hardcore music plays as a tough-looking girl walks down the aisle."
    "She's more ripped than most guys I've seen and she's even wearing an eye-patch!"
    "I have no idea if it's real of a part of her gimmick - and I'd be scared to ask!"
    "She climbs into the ring and I see she's wearing kick-boxing gear."
    "MC" "And her opponent, from Osaka Japan..."
    "MC" "Weighing in at two hundred sixty pounds..."
    "MC" "Edna Hyundai..."
    "The music that plays this time is more like something I'd expect to hear at a spa!"
    "It's all oriental flutes and ethereal strings."
    "But when I see Ms Hyundai for myself, I can't help gasping in surprise."
    "She's walking down the aisle, throwing what looks like white powder around."
    "And she's frikin huge!"
    "I thought the first girl looked tough - but this one is terrifying!"
    "And from the crazy kimono she's wearing, she must be a sumo wrestler."
    "Unlike the kick-boxer, this girl doesn't climb straight into the ring."
    "Instead she walks around the outside while the crowd jeers at her."
    mike.say "What's she doing, Ayesha?"
    mike.say "Everyone seems to hate her guts!"
    mike.say "Why is she talking to them?"
    ayesha.say "She's the heel, [hero.name], the bad guy."
    ayesha.say "She wants the fans to hate her and get worked up."
    ayesha.say "That's part of her job, to make them get into it by hating on her!"
    show ayesha annoyed
    "As the sumo wrestler gets closer, I notice Ayesha sitting back."
    "In fact, it's almost like she's shrinking down into her chair."
    "The sight is pretty funny, as there's no chance of her hiding herself."
    "Ayesha's way too tall for that to work!"
    mike.say "What's up, Ayesha?"
    mike.say "It's not like you to back down from a bully!"
    ayesha.say "It's not that, [hero.name]."
    ayesha.say "I've wrestled Edna in the past."
    ayesha.say "And I don't want her to see me!"
    "But as I turn my head to look where Edna is, it's already too late!"
    "Edna" "By my sacred ancestors!"
    "Edna" "If it isn't Ayesha the Amazon!"
    show fx anger
    "Edna" "Skulking in the crowd with all the other scum, I see?"
    "Edna" "And with a scrawny little degenerate on your arm too!"
    hide fx
    "Puzzled by this last comment I look around me."
    "That is until Ayesha stands up and puts me right."
    ayesha.say "She's talking about you, [hero.name]!"
    mike.say "Oh...I see..."
    mike.say "Wait a minute - she just insulted me!"
    menu:
        "Defend Ayesha and yourself":
            "I can feel my heckles rising with every word."
            "Each one that Edna speaks makes me madder than before."
            show ayesha surprised at startle
            show fx exclamation
            mike.say "Who are you calling a degenerate, butter-ball?!?"
            mike.say "What's the matter with guys under five hundred pounds, huh?"
            hide fx
            mike.say "You worried that I could beat you in a sprint to the buffet?!?"
            "Edna looks instantly surprised at the way I'm firing back at her."
            "Maybe she wasn't expecting me to put up any resistance."
            "Or perhaps my words have hit her where it hurts."
            "Either way the crowd oohs and ahhs in response to the exchange."
            "Edna" "You shut your filthy mouth!"
            "Edna" "And anyway...this is glandular - I can't help it!"
            mike.say "Yeah, you keep telling yourself that, girl."
            mike.say "Your problem is the hole at one end's bigger than the hole at the other!"
            mike.say "But don't worry about your ass."
            mike.say "Because Ayesha the Amazon's gonna kick it!"
            hide ayesha
            show ayesha casual a angry
            with hpunch
            "And I feel my heart beat faster at what she does next."
            show ayesha annoyed
            $ ayesha.sub += 2
            show ayesha b
            pause 1
            show ayesha a
            pause 1
            show ayesha b
            "Ayesha flexes her muscles, making her arms ripple."
            show ayesha a
            pause 1
            show ayesha b
            "She's pulling off poses that you see in body-building competitions."
            ayesha.say "Yeah, you bet I'm the Amazon!"
            ayesha.say "And this Amazon's ready to kick your ass!"
            show ayesha angry
            ayesha.say "Nobody insults my man and gets away with it!"
            "Suddenly the crowd begins to chant as one."
            show ayesha annoyed
            "Crowd" "Ayesha...Ayesha...Ayesha!"
            "Edna literally snarls at this."
            "But she backs off all the same, rolling into the ring."
            show ayesha happy
            "I turn to Ayesha, my eyes wide with admiration and affection."
            "And, if I'm honest, not a small amount of carnal desire too!"
            mike.say "Ayesha...you're my hero!"
            $ ayesha.love += 2
            show ayesha blush
            ayesha.say "What?!?"
            ayesha.say "Aw...stop it, [hero.name]!"
            show ayesha happy
            ayesha.say "Actually, don't stop it - I like being your hero!"
        "Let Ayesha defend you":
            mike.say "Is...is she allowed to do that?!?"
            "Edna" "I don't need your permission to insult you, worm!"
            $ ayesha.sub -= 2
            "I look at Edna and then back at Ayesha."
            "I can't actually believe that I'm being spoken to like this."
            "After all, I paid good money to come here and watch a wrestling show."
            "Now I feel like I'm being hassled by a bully in the street!"
            show ayesha angry
            ayesha.say "Hey, butter-ball - eyes on me!"
            "When Ayesha speaks, it's with a command that can't be ignored."
            "I instantly recognise it as the tone she takes in the ring."
            "Everyone within earshot is looking at her now."
            hide ayesha
            show ayesha casual a angry
            with hpunch
            "And I feel my heart beat faster at what she does next."
            show ayesha b
            pause 1
            show ayesha a
            pause 1
            show ayesha b
            "Ayesha flexes her muscles, making her arms ripple."
            show ayesha a
            pause 1
            show ayesha b
            "She's pulling off poses that you see in body-building competitions."
            show ayesha annoyed
            ayesha.say "Yeah, you bet I'm the Amazon!"
            ayesha.say "And this Amazon's ready to kick your ass!"
            show ayesha angry
            ayesha.say "Nobody insults my man and gets away with it!"
            "Suddenly the crowd begins to chant as one."
            show ayesha annoyed
            "Crowd" "Ayesha...Ayesha...Ayesha!"
            "Edna literally snarls at this."
            "But she backs off all the same, rolling into the ring."
            show ayesha happy
            "I turn to Ayesha, my eyes wide with admiration and affection."
            "And, if I'm honest, not a small amount of carnal desire too!"
            mike.say "Ayesha...you're my hero!"
            $ ayesha.love += 5
            show ayesha blush
            ayesha.say "What?!?"
            ayesha.say "Aw...stop it, [hero.name]!"
            show ayesha happy
            ayesha.say "Actually, don't stop it - I like being your hero!"
    show ayesha casual happy at dark, center, zoomAt(1.5, (640, 1040)) with fade
    play music "music/roa_music/2am.ogg" loop fadein .5
    "Once both of the wrestlers are in the ring, we sit back down."
    "Soon enough the match is underway and the attention is off Ayesha and me."
    "But I feel her take hold of my hand and give it an affectionate squeeze."
    "This makes me smile, and my heart leaps in my chest once again."
    "And you know what, I actually end up getting a kick out of the show."
    "But maybe that's more to do with enjoying spending the time with Ayesha than the actual wrestling!"
    scene bg black with dissolve
    return

label ayesha_event_09:
    if ayesha.love.max < 180:
        $ ayesha.love.max = 180
    "I'm minding my own business, just chilling around the house when my phone rings."
    "I pull it out and glance casually at the caller ID, seeing that it's Ayesha calling."
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Ayesha")
    if not result:
        $ hero.cancel_event()
        $ ayesha.love -= 5
        return
    "That puts a smile on my face and makes me take the call without hesitation."
    "Because who wouldn't want to talk to the gorgeous Amazon they're dating, right?"
    mike.say "Hey there, Ayesha!"
    mike.say "What's up?"
    ayesha.say "No time for chit-chat, [hero.name]!"
    ayesha.say "I need you to meet me at the arena - ASAP!"
    "Ayesha's urgency catches me totally off-guard."
    mike.say "Wha...what?"
    mike.say "What's the matter, Ayesha?"
    mike.say "Is it some kind of emergency?"
    ayesha.say "You could say that, yeah!"
    ayesha.say "I got a last minute booking."
    ayesha.say "I'm wrestling in the big show tonight."
    ayesha.say "The one for the company that's on national TV!"
    mike.say "No way!"
    mike.say "Ayesha, that's great news!"
    mike.say "This could be your big break!"
    ayesha.say "I know, [hero.name] - I'm so pumped for this!"
    ayesha.say "So you'll come to the show?"
    ayesha.say "I know it's short notice, but I could really use your support."
    if ayesha.flags.manager:
        ayesha.say "If you're up for it, I'd like you to manage me and be at ringside."
        "I'm still reeling from the news that Ayesha just gave me."
        "That and planning how I'm going to get to the arena."
        "But I know the moment she asks me what my answer is going to be."
        mike.say "If you want me to manage you, Ayesha, then you've got it!"
        mike.say "Whatever you need - I'm right there by your side!"
        mike.say "Or at least I will be...as soon as I get there."
        "Ayesha can't help letting out a gasp of joy."
        "Which in turn makes me all the more sure I made the right choice."
        ayesha.say "That's great, [hero.name]!"
        ayesha.say "We need to pull out all the stops for this one."
        ayesha.say "So get your ass down here, pronto!"
    else:
        ayesha.say "Or you could come along and cheer me on from the crowd?"
        ayesha.say "They've given me a front-row ticket that you can use."
        "I'm still reeling from the news that Ayesha just gave me."
        "That and planning how I'm going to get to the arena."
        "I can't handle actually managing her on top of all that!"
        mike.say "I'll be there as soon as I can, Ayesha."
        mike.say "But I want to use that front-row ticket."
        mike.say "It's too short notice for me to manage you though."
        mike.say "I'm afraid I'd screw up and blow your big chance!"
        "There's a short silence on the other end of the line."
        "Which tells me that Ayesha is thinking it over."
        "But then she lets out a snort of resignation."
        ayesha.say "Yeah, I guess you're right!"
        ayesha.say "It's a bit of an ask - maybe too much of one."
        ayesha.say "I'll have to make do with having you at ringside."
        ayesha.say "But get your ass here, pronto!"
    "I honestly do drop everything and rush over to the arena."
    scene bg street with dissolve
    "And when I get there, I'm amazed at the size of the crowd outside."
    "But that's not a problem for me, as I see Ayesha waving at me from a side entrance."
    show ayesha fight annoyed at mostleft5 with moveinleft
    ayesha.say "Hey, [hero.name]..."
    ayesha.say "Over here!"
    with hpunch
    "I hurry over, fighting my way through the mass of fans."
    mike.say "Hey, Ayesha..."
    mike.say "I finally made it!"
    scene bg street at blur(16), dark
    show ayesha close fight annoyed
    with vpunch
    "My reward for this is to be grabbed by the collar."
    scene bg arena at flip, dark, center, zoomAt (2.5, (-300, 1020))
    show ayesha close fight
    with vpunch
    "And then Ayesha yanks me into the building."
    if ayesha.flags.manager:
        "She looks me up and down, evidently inspecting my appearance."
        "And then she nods her head with what I take to be satisfaction."
        show ayesha close normal
        ayesha.say "Good...good..."
        ayesha.say "You look like enough of a creep to be my manager!"
        mike.say "Hey!"
        "Before I can object, I get a better look at Ayesha."
        "She looks like a warrior queen from ancient times."
        "Well...at least one dressed in spandex!"
        "And I've never wanted her more than I do right now!"
        show ayesha close annoyed
        ayesha.say "Hey, [hero.name]..."
        ayesha.say "Eyes on the prize, yeah?"
        show ayesha close normal
        ayesha.say "Do your job well, and you get to handle the goods after the show!"
        mike.say "Wha..."
        mike.say "Oh...okay, Ayesha!"
        "She nods as she leads me into the locker-room."
        show ayesha -close
        ayesha.say "This shouldn't be too hard."
        ayesha.say "I'm working face, so I don't need you to run interference."
        ayesha.say "The most you should have to do is react to the bumps I take, yeah?"
        "Just then another girl walks over, but she stops in the corner of my vision."
        "Girl" "Hey, Ayesha..."
        "Girl" "You wanna go over the match now?"
        "Girl" "Or just call it in the ring?"
        show ayesha annoyed
        ayesha.say "Call it in the ring, Edna."
        ayesha.say "Oh, by the way - this is my manager, [hero.name]."
        "Edna's voice is sweet and heavily accented, reminding me of an anime character."
        "I turn around, expecting to be greeted by a petite little Japanese girl."
        show ayesha at right
        "But when I see Ms Hyundai for myself, I can't help gasping in surprise."
        "She's frikin huge!"
        "I thought Ayesha looked tough - but this one is terrifying!"
        "And from the crazy kimono she's wearing, she must be a sumo wrestler."
        mike.say "I...I...I..."
        "Far from being offended at my surprise, Edna giggles instead."
        "And the sound is like a delicate bell tinkling away in the hands of a fairy."
        "Edna" "I guess he's new!"
        "Edna" "See you out there, Ayesha."
        "Edna" "Break a leg!"
        show ayesha at center
        "Soon enough, it's time for us to go out to the ring."
        "Ayesha and I wait behind the curtain for the MC to announce us."
        scene bg arena at flip, blur(8), dark, dark, center, zoomAt (2.5, (-300, 1020)) with dissolve
        pause 2.0
        "MC" "Ladies and gentlemen..."
        "MC" "Welcome to Pro Wrestling BANG!"
        "MC" "Our first contest is scheduled for one fall!"
        "Crowd" "ONE FALL!"
        "MC" "Introducing first, weighing in at two hundred and fifty pounds..."
        "MC" "The Terrible Tigress..."
        "MC" "The Princess of Pain..."
        "MC" "The Amazon Ayesha!"
        scene bg arena at flip, dark, center, zoomAt (2.5, (-300, 1020))
        show ayesha fight at right
        with dissolve
        "We walk through the curtain to the sound of Ayesha's music."
        "And we're bathed in the sound of the cheering crowd."
        "I follow Ayesha to the ring, opening the rope for her to climb in."
        "MC" "And her opponent, from Osaka Japan..."
        "MC" "Weighing in at two hundred sixty pounds..."
        "MC" "Edna Hyundai..."
        show ayesha annoyed

        "The music that plays this time is more like something I'd expect to hear at a spa!"
        "It's all oriental flutes and ethereal strings."
        "But when I see Ms Hyundai for myself, I can't help gasping in surprise."
        "She's walking down the aisle, throwing what looks like white powder around."
        "The sweet, giggling girl from the locker-room is gone."
        "And in her place is a mean, snarling hell-bitch!"
        "As soon as she climbs into the ring, Edna rushes over to Ayesha."
        "They square off as the referee struggles to get between them."
        "I do my best to help, but I end up getting pushed away."
        "I land on my ass and use that as an excuse to roll out under the bottom rope."
        "Leaning on the edge of the ring, I try to prepare myself for what follows."
        "Then the bell rings and the match actually gets underway."
        show ayesha angry at right5 with hpunch
        "And for all that I know it's not a real sport, I'm totally hooked!"
        "Maybe it's my emotional connection to Ayesha that does it."
        show ayesha at right4 with vpunch
        "Or maybe I'm just more susceptible to this kind of stuff than I thought."
        "Either way I'm hammering on the ring, cheering Ayesha on one moment."
        "Then I'm wishing a painful death upon Edna the next."
        "Well, that and cursing the referee for not siding with Ayesha too!"
        with hpunch
        show ayesha annoyed at mostright5
        with vpunch
        "I sense something important is on the cards when Ayesha goes down hard."
        "She lands in the corner, and Edna starts to climb the turnbuckles."
        "Reaching the top, she pauses, the yells at the top of her voice."
        "Edna" "BANDAI!"
        "Oh shit - she's going to land on Ayesha!"
        show ayesha at mostright4
        "But then Ayesha's on her feet, grabbing Edna from underneath."
        show ayesha angry at right5
        "She lifts the other girl into the air, then slams her down to the matt!"
        show ayesha at left4
        with vpunch
        with vpunch
        with vpunch
        mike.say "TIGRESS BOMB!"
        mike.say "FUCK YEAH!"
        "Ayesha throws herself on top of Edna, hooking her massive leg."
        "The referee starts hammering the matt."
        "One, two...THREE!"
        show ayesha annoyed at center
        "That's it, Ayesha's the winner!"
        "Everyone in the crowd goes wild."
        "I roll into the ring just as the referee is raising Ayesha's hand in victory."
        "Grabbing the other and doing the same, I join in the celebrations."
    else:
        "A moment later she thrusts the ticket into my hand."
        "Then she shoves me in the direction of the seating."
        show ayesha -close
        mike.say "Whoa..."
        mike.say "Wait a minute, Ayesha!"
        mike.say "I just wanted to say break a leg!"
        show ayesha normal
        "Ayesha's expression softens at this."
        ayesha.say "I'm sorry, [hero.name]."
        ayesha.say "I think the nerves are getting to me, you know?"
        "I nod, trying to show that I understand."
        "But at the same time I'm smiling too."
        "In the hope of inspiring confidence in Ayesha."
        mike.say "Hey..."
        mike.say "What have you got to be nervous about, Ayesha?"
        mike.say "You're the frikin Amazon - a total goddess of the ring!"
        show ayesha blush
        "Ayesha blushes a little and waves away my compliments."
        ayesha.say "Ah, shut-up with the flattery!"
        show ayesha happy
        ayesha.say "But thanks for the vote of confidence."
        hide ayesha with dissolve
        "With that, she turns and walks back towards the locker-room."
        "I hurry off to find my seat, settling down at ring-side."
        scene bg arena at flip, blur(8), dark, dark, center, zoomAt (2.5, (-300, 1020)) with dissolve
        pause 2
        "Ayesha wasn't kidding either - I'm right behind the barricade!"
        "Soon the place is full to the brim with fans."
        "People are starting to clap and cheer."
        scene bg arena at flip, dark, center, zoomAt (2.5, (-300, 1020)) with dissolve
        play music "music/TeknoAXE/simple_metal.ogg" loop fadein .5
        "And then loud rock music starts to play over the PA system."
        "The people sitting around us start to go crazy!"
        "All of this makes me feel like I'm at a rock concert, rather than a sporting event."
        "I watch as a guy in a suit walks down the aisle."
        "He has a microphone, so I assume he's the ring announcer."
        "My suspicions are confirmed when he climbs into the ring and starts the show."
        "MC" "Ladies and gentlemen..."
        "MC" "Welcome to Pro Wrestling BANG!"
        "MC" "Our first contest is scheduled for one fall!"
        with vpunch
        "Crowd" "ONE FALL!"
        "I jump in my seat as the entire crowd shouts the words together."
        "I can never get used to that!"
        "I know that Ayesha's not in the first match of the night."
        "She's in the third or fourth, I think."
        "So I can just sit back and wait until then."
        "The matches all look really impressive and exciting."
        "And the crowd seems to be into all of it too."
        "But I don't feel involved until I hear Ayesha's music play."
        "MC" "Introducing first, weighing in at two hundred and fifty pounds..."
        "MC" "The Terrible Tigress..."
        "MC" "The Princess of Pain..."
        "MC" "The Amazon Ayesha!"
        show ayesha fight at mostright4 with dissolve
        "I jump to my feet as Ayesha strides down the aisle."
        "And the moment I spot her, I feel weak at the knees!"
        "She looks like a warrior queen from ancient times."
        "Well...at least one dressed in spandex!"
        "And I've never wanted her more than I do right now!"
        show ayesha at right with ease
        "I watch, transfixed as she reaches the ring and climbs inside."
        "MC" "And her opponent, from Osaka Japan..."
        "MC" "Weighing in at two hundred sixty pounds..."
        "MC" "Edna Hyundai..."
        show ayesha annoyed
        "The music that plays this time is more like something I'd expect to hear at a spa!"
        "It's all oriental flutes and ethereal strings."
        "But when I see Ms Hyundai for myself, I can't help gasping in surprise."
        "She's walking down the aisle, throwing what looks like white powder around."
        "And she's frikin huge!"
        "I thought Ayesha looked tough - but this one is terrifying!"
        "And from the crazy kimono she's wearing, she must be a sumo wrestler."
        "As soon as she climbs into the ring, Edna rushes over to Ayesha."
        "They square off as the referee struggles to get between them."
        "Then the bell rings and the match actually gets underway."
        show ayesha angry at right5 with hpunch
        "And for all that I know it's not a real sport, I'm totally hooked!"
        "Maybe it's my emotional connection to Ayesha that does it."
        show ayesha at right4 with vpunch
        "Or maybe I'm just more susceptible to this kind of stuff than I thought."
        "Either way I'm up and cheering Ayesha on one moment."
        "Then I'm wishing a painful death upon Edna the next."
        "Well, that and cursing the referee for not siding with Ayesha too!"
        with hpunch
        show ayesha annoyed at mostright5
        with vpunch
        "I sense something important is on the cards when Ayesha goes down hard."
        "She lands in the corner, and Edna starts to climb the turnbuckles."
        "Reaching the top, she pauses, the yells at the top of her voice."
        "Edna" "BANDAI!"
        "Oh shit - she's going to land on Ayesha!"
        show ayesha at mostright4
        "But then Ayesha's on her feet, grabbing Edna from underneath."
        show ayesha angry at right5
        "She lifts the other girl into the air, then slams her down to the matt!"
        show ayesha at left4
        with vpunch
        with vpunch
        with vpunch
        mike.say "TIGRESS BOMB!"
        mike.say "FUCK YEAH!"
        "Ayesha throws herself on top of Edna, hooking her massive leg."
        "The referee starts hammering the matt."
        "One, two...THREE!"
        show ayesha happy at center
        "That's it, Ayesha's the winner!"
        "Everyone in the crowd goes wild."
        "Which includes me, hugging strangers and cheering like a lunatic."
    scene bg arena at flip, dark, dark, center, zoomAt (2.5, (-300, 1020))
    show ayesha fight sad at center, zoomAt(1.5, (640, 1040))
    with fade
    "Afterwards, I find Ayesha in the locker-room."
    "She's holding an ice-pack against her shoulder."
    "And she looks like the very image of exhaustion."
    "Even so, she looks up at me with a smile."
    mike.say "You okay, Ayesha?"
    mike.say "It looked like you took some serious punishment out there!"
    show ayesha normal
    ayesha.say "Nah...it's just the usual aches and pains, [hero.name]."
    ayesha.say "I'll be fine, so don't worry about me."
    mike.say "Yeah...I think I will, if that's all the same to you!"
    show ayesha happy at startle
    "Ayesha laughs ruefully at this."
    "Then she swings a playful punch at my chest."
    show ayesha annoyed
    "But the motion makes her wince as she strains her shoulder."
    ayesha.say "Ah...shit..."
    show ayesha normal
    ayesha.say "Maybe you're right!"
    ayesha.say "Look, I need to hit the showers."
    show ayesha happy
    ayesha.say "You want to come hold the towel for me?"
    ayesha.say "Maybe even help me out a little bit more?"
    "Ayesha adds a wink to underline her meaning."
    "Then she chuckles as I nod with undisguised enthusiasm."
    return

label ayesha_event_10:
    if ayesha.love.max < 200:
        $ ayesha.love.max = 200
    scene bg clothesshop
    show ayesha casual
    with fade
    "One of the things that I love about Ayesha is the way that she's a tough cookie on the outside."
    "But once you get beneath the surface, she's warm and sensitive, even a little vulnerable too."
    "And that makes her all the more intriguing and endearing, knowing what she's hiding inside."
    "But once she's opened up to you, it's almost impossible for Ayesha to fool you again."
    "All of the macho posing and tough behaviour can't hide the real Ayesha that you know is underneath."
    "Which is why I know that something is up as soon as she starts trying to pull it on me."
    show ayesha happy
    ayesha.say "Hah!"
    ayesha.say "Will you just look at that silly little girl over there!"
    ayesha.say "No way you'd ever get me wearing something as skimpy as that!"
    ayesha.say "Plus they'd never have it in my size, oh no!"
    "Ayesha puts on a comical voice, imitating an imagined and unhelpful employee."
    ayesha.say "'Oh...sorry, madam...there's NO demand for it in YOUR size!'"
    "I frown and cock my head on one side as I regard Ayesha."
    "And I raise an eyebrow with interest."
    mike.say "Ayesha..."
    mike.say "What's bothering you?"
    show ayesha blush
    "Ayesha's head snaps around at the question, so fast I almost jump."
    "But the look on her face is one of shock and surprise."
    "Her eyes are wide and she almost looks like she's starting to sweat too!"
    show fx drop
    ayesha.say "Wha...what?"
    ayesha.say "I don't know what you mean!"
    hide fx
    "I give Ayesha an ironic smile and shake my head."
    mike.say "Oh come on, Ayesha!"
    mike.say "It's not like you to bad-mouth random girls for their fashion sense."
    mike.say "You're usually the one to be sticking up for them."
    mike.say "Seems to me like you're trying to use it as a distraction."
    "Ayesha blinks a couple of times, then looks away."
    "All the time her lips are moving."
    "But no words come out of her mouth."
    show ayesha annoyed
    "Finally she makes an awkward grunting sound."
    "And I take this to be a sign of her surrendering."
    ayesha.say "Urgh..."
    ayesha.say "I hate it when you do that, [hero.name]!"
    ayesha.say "When you read me like a book!"
    "I'm trying to stay humble and look understanding right now."
    "But I still can't keep myself from a wry smile of satisfaction."
    mike.say "Never mind all that, Ayesha."
    mike.say "Just tell me what's on your mind, okay?"
    show ayesha normal
    "Ayesha nods."
    ayesha.say "Okay, okay..."
    ayesha.say "But this is pretty hard for me to admit."
    ayesha.say "I'm not used to opening up to people like this..."
    ayesha.say "But...I love you, [hero.name]!"
    "I nod as my smile becomes more genuine and natural."
    mike.say "I know that, Ayesha."
    mike.say "And I love you too."
    mike.say "Is that all you wanted to say?"
    mike.say "Because I kind of felt like we'd made it there already!"
    show ayesha annoyed
    "Ayesha shakes her head."
    "Evidently she has more to say."
    ayesha.say "Me too, [hero.name], me too."
    ayesha.say "But I do have more to say."
    show ayesha sad
    ayesha.say "Being as big as I am, I always felt like I had to be tough."
    ayesha.say "Like I had to stop being feminine and hide that side of me."
    ayesha.say "People expected me to be a big, tough bruiser, so that's what I pretended to be."
    show ayesha happy
    ayesha.say "But with you it's different somehow."
    ayesha.say "With you I feel like I can drop the charade and just be me."
    ayesha.say "It's weird, because you make me feel like a real woman."
    ayesha.say "But you make me feel stronger than ever - and not in a physical sense either."
    ayesha.say "If any of that makes sense!"
    mike.say "I think so, Ayesha."
    mike.say "It feels like you're the real you around me."
    mike.say "Like you're supposed to be as magnificent as your body looks."
    mike.say "But it goes along with the gentle, loving girl that's inside too."
    "Ayesha nods again, her eyes wide and almost glistening with tears."
    ayesha.say "That's it - that's what I mean!"
    ayesha.say "You talk about me and it sounds just right."
    ayesha.say "That's exactly who I want to be!"
    mike.say "Well...that's who you are in my eyes, Ayesha!"
    hide ayesha
    show ayesha kiss casual
    with fade
    $ ayesha.flags.kiss += 1
    "Ayesha responds by throwing her arms around me."
    "Her embrace is like that of an intense bear-hug."
    "But to me it feels so comforting that I could stay there forever."
    "Her head nestles against my neck, Ayesha sighs with contentment."
    ayesha.say "Mmm..."
    ayesha.say "I love you SO much, [hero.name]!"
    mike.say "I love you too, Ayesha."
    mike.say "More than you can ever know!"
    return

label ayesha_male_ending:




    if renpy.has_label("ayesha_achievement_3") and not game.flags.cheat:
        call ayesha_achievement_3 from _call_ayesha_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "Part of me still can't believe this is actually happening, that the big day is finally here."
    "I know it's a massive cliche, one of those things that everyone seems to come out with in this position."
    "But when you find yourself there, you realise pretty quickly that it's true for the most part."
    "All of your time and effort goes into the planning, and that time passes in the blink of an eye."
    "Now I find myself standing at the altar in the chapel, in front of almost everyone I know."
    "All eyes are either on me or else the doors that she's about to walk through."
    "And that's Ayesha, of course - the girl that I'm about to marry!"
    "It seems like only yesterday that she was stretching the life out of me in the gym!"
    "Somehow we went from that to this - agreeing to share the rest of our lives together!"
    "I shake my head, still not fully able to make sense of it all."
    "I guess that's another old cliche that's actually true..."
    "Life is what happens while you're making plans!"
    "That's when it all starts to swing into motion."
    "The moment I take my mind of the moment, the music begins to swell."
    "The sound of the track Ayesha chose to come down the aisle to snaps me back to reality."
    "I turn to look at the doors to the chapel again, and then I see them open."
    show ayesha happy wedding at center, zoomAt (1.0, (640, 730)) with dissolve
    "And once Ayesha sweeps into the place, she's all I can think about."
    "Seriously, I can't keep my eyes off her for even a single second."
    "Brides always look amazing on their wedding days, that's a given."
    "And I could go on about how beautiful Ayesha is for hours."
    "But she's never looked as good as she does right now."
    show ayesha happy wedding at center, traveling (1.5, 5.0, (640, 1040))
    "As she strides down the aisle, her dress is paying for itself with every step."
    "Everyone says that Ayesha's an Amazon, that she's got the build of a warrior woman."
    "Well today she looks more like a warrior queen, regal and commanding as she walks towards me."
    if ayesha.is_visibly_pregnant:
        "Part of me always wondered what Ayesha would look like pregnant."
        "And now I know that the answer - she looks amazing!"
        "Somehow her curving belly makes her even more feminine."
        "And I couldn't be more proud to be the father of her child."
    else:
        "It's funny, I'm so used to seeing Ayesha dressed in nothing but spandex at the gym."
        "And I know the lines of her body so well I can see it even when I close my eyes."
        "Yet somehow the dress she has on makes me want to see more of her with her clothes on!"
        "It gives her an elegance that's totally new and very intriguing indeed!"
    show ayesha at center, zoomAt (1.5, (640, 1040)) with dissolve
    "As she reaches the altar and stands by my side, I can't help grinning."
    "Ayesha smiles too, but she turns her gaze away, just slightly."
    "It's a gesture that reveals just how nervous she must be right now."
    "And it also reminds me of the sweet, sensitive side she possesses."
    "To most people it remains hidden beneath the persona she uses in the wrestling ring."
    "But I count it an honour that she revealed it to me, that she let me in on that little secret."
    ayesha.say "Oh my god..."
    ayesha.say "This is SO weird!"
    mike.say "I know what you mean!"
    mike.say "I can't believe it's finally happening?"
    show wedding ayesha with fade
    "Priest" "Ahem..."
    "At the sound of the priest's voice, both Ayesha and I jump a little."
    show wedding ayesha priest with dissolve
    "The next moment we're almost standing to attention, trying to look alert."
    "Priest" "Very good!"
    "Priest" "Shall we begin?"
    "As one, Ayesha and I nod."
    "Then we share a sly smile with each other."
    "God I'm going to love being married to this woman!"
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these two people in the bonds of holy matrimony..."
    "You know how the rest goes, right?"
    "It's a wedding after all."
    "Even if you've never been to one in real life, you've seen one on the TV."
    "The only part that anyone really cares about comes when the priest starts talking about the vows."
    "Priest" "Do you, Ayesha..."
    "Like this bit right now!"
    "Priest" "Take [hero.name], to be your lawful, wedded husband?"
    ayesha.say "I do."
    "Priest" "Very good."
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take this woman, Ayesha, to be your lawful, wedded wife?"
    mike.say "I do."
    "Once the vows have been exchanged, the priest glances around the chapel."
    "Priest" "I call upon those here present..."
    "Priest" "That if you know any lawful reason..."
    "Priest" "That these two people may not be joined in holy matrimony..."
    "Priest" "Speak now, or forever hold your peace!"
    "There's the traditional pause, followed by a ripple of nervous laughter."
    "But thankfully nobody storms into the chapel or stands up from the pews."
    "Priest" "Very good..."
    "Priest" "It is therefore my pleasure to pronounce you married."
    "Priest" "You may kiss the bride!"
    show wedding ayesha -priest with dissolve
    "I make to sweep Ayesha off her feet and kiss her with all my might."
    "But she beats me to the punch, pulling the same stunt on me."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show ayesha kiss wedding
    with fade
    $ ayesha.flags.kiss += 1
    "Ayesha laughs as she plants a small kiss on my lips."
    "Then she returns me to my feet, having made her point."
    "We embrace as equals, and the kiss is all the more passionate for it."
    "The wedding is over, and Ayesha's actually my wife!"
    "I'm married to the strongest, most beautiful and sweetest woman in the world!"
    "And I can't wait to see where the life we'll share together will take us."
    scene ayesha ending
    with fade
    ayesha.say "Okay, okay..."
    ayesha.say "This is going to be pretty hard, so bear with me."
    ayesha.say "I'm a pretty private kind of person and I don't like talking about myself."
    ayesha.say "What?"
    ayesha.say "Yes, I know that I do the whole professional wrestling thing."
    ayesha.say "But that's different, more like acting, you know?"
    ayesha.say "It's so extreme that it's almost like being able to hide in plain sight."
    ayesha.say "So here goes..."
    ayesha.say "The first time I laid eyes on [hero.name]...let's just say I wasn't impressed!"
    ayesha.say "All I saw was another typical guy at the gym, pumping himself up to impress the girls."
    ayesha.say "There are a thousand guys like that, and all they see when they look at me is my size."
    ayesha.say "And yes, I know that it's kind of a hard thing to ignore."
    ayesha.say "But it's always been a double-edged sword for me."
    ayesha.say "When you're this big, everyone makes assumptions."
    ayesha.say "They assume that you're going to be a bully and throw your weight around."
    ayesha.say "So that makes them think they're the good guy if they get their shots in first."
    ayesha.say "And when you fight back, what else are you doing but proving them right?"
    ayesha.say "So yes, maybe that is why I tend to put on a front of being a tough chick!"
    ayesha.say "That's how I thought it was going to be with [hero.name] too."
    ayesha.say "That he was going to be a guy that was all mouth."
    ayesha.say "The kind that I'd need to stretch on the mat and teach a lesson."
    ayesha.say "But then I don't know how it happened..."
    ayesha.say "He started to see through the act that I was putting on in front of him."
    ayesha.say "[hero.name] was convinced there was another side to me underneath."
    ayesha.say "And I wanted to let him know that he was right."
    ayesha.say "But I guess I was scared to let him in - scared of being hurt."
    ayesha.say "It took a while, but I eventually started to get more comfortable around him."
    ayesha.say "And I could begin to open up to the guy, let him get to know the real me."
    ayesha.say "I suppose it helped that he's kind of goofy, and that he tires so hard!"
    ayesha.say "He hides it well, but I still think it bugs him that I always win when we arm-wrestle!"
    ayesha.say "But what's more important is how [hero.name] helped me to reconnect with my femininity."
    ayesha.say "It was always there, hidden under my tough-girl image like everything else."
    ayesha.say "A little at a time, [hero.name] seemed to be able to coax it back out into the open."
    ayesha.say "Before long I was starting to feel confident showing off my body outside of a wrestling ring."
    ayesha.say "I was wearing dresses when we went to fancy places on dates."
    ayesha.say "And I even felt confident enough to wear a bikini at the beach or by the poolside!"
    ayesha.say "[hero.name] loved my muscles as much as part of the total package that's me."
    ayesha.say "And I loved the fact that someone was liking the look of me as a real woman too."
    ayesha.say "By the time he popped the question, I was pretty much in love with him."
    ayesha.say "Well...I suppose I should be honest about this..."
    ayesha.say "I was totally in love with the guy, and I still am!"
    if ayesha.is_visibly_pregnant or ayesha.flags.mikeBabies >= 1:
        ayesha.say "I mean, I was already pregnant with Andrew and Mitchel at the time."
        ayesha.say "But it wasn't like a shotgun wedding or anything of that kind."
        ayesha.say "[hero.name] and I were already committed to raising the boys when they arrived."
        ayesha.say "And he's been the perfect father to them from the moment they were born."
        ayesha.say "Although I do think he worries they'll take after me."
        ayesha.say "So one day he'll be the smallest person in the house!"
    else:
        ayesha.say "Of course I agreed to marry him, and it was the happiest day of my life."
        ayesha.say "I've not looked back since that moment, and I can't wait to see where we end up."
        ayesha.say "And I don't think it'll be too long before our family starts to grow either!"
    ayesha.say "And it's not like he demanded that I give up my career when I became his wife either."
    ayesha.say "In fact [hero.name]'s done all that he can to encourage me and make me a success."
    ayesha.say "He was always there when I was working the local independent promotions."
    ayesha.say "Either in front row or in my corner, and backstage after the match."
    ayesha.say "[hero.name] was my manager, cheerleader and number one fan."
    ayesha.say "And when things started to take off, he was there too."
    ayesha.say "He came on the road with me when I got bookings in other cities."
    ayesha.say "Then he did the same when I got booked in other countries too."
    ayesha.say "But best of all were the tours of Japan."
    ayesha.say "Now there's a culture that really appreciates a woman of my stature!"
    ayesha.say "The memories that [hero.name] and I made over there will last a lifetime."
    ayesha.say "And I hope that we'll last a lifetime too."
    ayesha.say "Because as much as I could never have predicted meeting him..."
    ayesha.say "Now I can't even begin to imagine what my life would be like without him."
    ayesha.say "And yes..."
    ayesha.say "I do still call him 'fuck face' on occasion."
    ayesha.say "But only when he deserves it, or I REALLY want to get his attention..."

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not ayesha.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_4
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_4
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label ayesha_sub_event_01:
    "For all that she's so physically imposing and puts out strong vibes, Ayesha can still be pretty nervous at times."
    "Like right now, for instance - she's been beating about the bush for what feels like ages, trying to get her words out."
    show ayesha normal
    ayesha.say "Ah, [hero.name]..."
    ayesha.say "There was kind of something that I..."
    ayesha.say "You know, something I wanted to...ask you?"
    mike.say "Sure thing, Ayesha - you can ask me anything."
    mike.say "What is it?"
    "Ayesha looks away for a moment, as if she's embarrassed."
    "But then she seems to gather her courage and ask anyway."
    ayesha.say "Well, you know that I've been training for more MMA fights?"
    "I feel my mouth go dry at the thought of Ayesha pounding her opponents in the ring."
    "That and my cock getting harder by the second too!"
    mike.say "Yeah, Ayesha."
    mike.say "How could I forget!"
    ayesha.say "I...I wondered if you'd help me?"
    show ayesha sad
    ayesha.say "Help me with my training?"
    "By now I'm almost sweating at the possibility of grappling with Ayesha in spandex."
    "And who knows - we might end up having an 'accident' and doing something else too..."
    mike.say "Of course, Ayesha."
    mike.say "I'd love to help out any way that I can."
    mike.say "Would you like me to spar with you?"
    mike.say "If you do, please be gentle!"
    "Ayesha shakes her head at this, looking more embarrassed than ever."
    "She clears her throat before she speaks, obviously building up to something."
    show ayesha normal
    ayesha.say "Ah, no..."
    ayesha.say "I was thinking more of my..."
    ayesha.say "My pain threshold!"
    mike.say "Wait...what?!?"
    mike.say "You want me to hurt you?"
    ayesha.say "No, no, no!"
    show ayesha annoyed
    ayesha.say "Well...yes, kind of..."
    "By now, Ayesha's so embarrassed by what she's saying that she can hardly meet my eye."
    ayesha.say "I was thinking that we could make it fun, you know?"
    ayesha.say "Maybe play some games?"
    show ayesha blush
    ayesha.say "In the bedroom?"
    "It takes me a couple of seconds to grasp what she's trying to say."
    "But then it dawns on me why she's so bashful about the whole thing."
    mike.say "Oh...OH....I get it!"
    mike.say "You mean like whips and ropes?"
    mike.say "Kinky stuff, yeah?"
    ayesha.say "Well...yeah."
    ayesha.say "I've always been kind of curious about that kind of thing."
    ayesha.say "And this way we could both get something out of it..."
    menu:
        "I'm not into this kind of stuff":
            "Part of me really wants to experiment with Ayesha, and it could be fun."
            "But I don't know the first thing about that kind of thing."
            "And I'm already starting to get worried someone might end up hurt."
            mike.say "Ah...I'd like to, Ayesha."
            mike.say "But I wouldn't even know where to start!"
            ayesha.say "Oh...okay, okay."
            show ayesha sad
            ayesha.say "It's fine if you don't want to."
            ayesha.say "Thanks for being honest enough to say so!"
            "The mood's turned distinctly awkward."
            "But I think it's for the best."
            $ ayesha.sub -= 2
        "I might have some ideas":
            "Suddenly all I can think of is Ayesha."
            "Naked and bound in a compromising position."
            mike.say "That sounds amazing, Ayesha!"
            mike.say "When can we get started?!?"
            "Ayesha can't suppress a surprised giggle."
            "She looks amazed at my enthusiastic response."
            ayesha.say "Whoa, settle down, [hero.name]!"
            show ayesha happy
            ayesha.say "This kind of thing needs some serious planning, you know?"
            ayesha.say "But don't worry - we'll get it on!"
            show ayesha blush
            ayesha.say "In fact, are you free in a week?"
            "The smile that slowly spreads across her face sums it all up perfectly."
            "I have no idea what she has in mind."
            "But it's going to be a hell of a lot of fun finding out!"
            $ hero.calendar.add(game.days_played + 7, LabelAppointment((16, 19), "ayesha", "Meet with Ayesha", "ayesha_sub_event_02", "ayesha_sub_event_02_missed"))
    return

label ayesha_sub_event_02_missed:
    "Shit I missed my date with Ayesha."
    $ ayesha.love -= 10
    $ hero.calendar.add(game.days_played + 7, LabelAppointment((16, 19), "ayesha", "Meet with Ayesha", "ayesha_sub_event_02", "ayesha_sub_event_02_missed"))
    return

label ayesha_sub_event_02(appointment=None):
    scene bg bedroom1
    "I have to admit that I'm nervous, never having done this kind of thing before now."
    "But I did agree to help Ayesha increase her toughness for the rigours of the MMA circuit."
    "So it'd be pretty weak of me to cry off now that we're actually about to go through with it."
    "The problem is that I'm just not used to hurting a fly, let alone another human being!"
    "I don't even know if Ayesha being a girl actually makes it better or worse."
    "And that's before I take into account the fact she's built like an Amazonian goddess too!"
    "Can I really inflict pain on someone that I have feelings for?"
    "Can I actually get off on it too?"
    "All of this is preying on my mind as Ayesha closes the door to my bedroom and turns to face me."
    show ayesha normal with dissolve
    ayesha.say "Are you okay, [hero.name]?"
    ayesha.say "Because you look kinda nervous..."
    menu:
        "I'm ok" if hero.sexperience >= 30 and ayesha.sub >= 50:
            mike.say "Ah, yeah..."
            mike.say "This is all new to me, Ayesha."
            mike.say "But don't worry about it - I'll be fine."
            ayesha.say "I'm pretty nervous too, [hero.name]!"
            show ayesha happy
            ayesha.say "But if you're sure..."
            mike.say "I am, Ayesha."
            mike.say "I agreed to help you do this."
            mike.say "And I won't let you down."
            "Ayesha smiles and nods, clearly reassured by my words."
        "We should wait.":
            mike.say "Erm, no, Ayesha..."
            mike.say "I'm so sorry - but I'm just not okay with this."
            mike.say "Hurting you, even if you want it, doesn't feel right."
            "Ayesha nods."
            "She looks disappointed, but also a little relieved."
            ayesha.say "It's okay, [hero.name]."
            show ayesha sad
            ayesha.say "I'd rather you were honest than did something just to please me."
            "She looks down, chuckling to herself."
            "It's then I notice her cheeks are flushing."
            ayesha.say "Actually, it's kinda nice."
            ayesha.say "Knowing that you're not okay with hurting me!"
            ayesha.say "It makes me feel loved."
            $ ayesha.love += 1
            $ hero.calendar.add(game.days_played + 14, LabelAppointment((16, 19), "ayesha", "Meet with Ayesha", "ayesha_sub_event_02", "ayesha_sub_event_02_missed"))
            $ hero.cancel_activity()
            return
    if ayesha.sub.max < 60:
        $ ayesha.sub.max = 60
    "Sure that we're going ahead with this thing, I pull out the instrument I'll be using."
    "I see Ayesha's eyes go wide as she sees it for the first time."
    "But she nods all the same and begins to walk slowly towards me."
    mike.say "Now, Ayesha."
    mike.say "Strip down!"
    "I honestly don't know where the air of command in my voice comes from."
    show ayesha naked
    "But when I see Ayesha jump in surprise and hurry to obey..."
    "Well, let's just say that it's more than enough to start getting me hard!"
    mike.say "Come here, Ayesha."
    mike.say "Right here - and then lie down!"
    "I watch as Ayesha stops a little way from me and lies down over the bed."
    call ayesha_bdsm_choices from _call_ayesha_bdsm_choices
    scene bg bedroom1
    "Once we're done, I watch as Ayesha put her panties back."
    show ayesha sport topless
    "She does so gingerly, as if her ass is still sensitive from the spanking."
    "Ayesha smiles at me, a little awkwardly at first."
    show ayesha sport -topless happy
    "But then I see that it's not only the cheeks down there that are burning."
    mike.say "How are you feeling, Ayesha?"
    mike.say "Are you okay?"
    ayesha.say "Y...yeah, I'm okay."
    show ayesha blush
    ayesha.say "That was really...nice!"
    mike.say "Ah, yeah..."
    mike.say "I enjoyed it too!"
    mike.say "See you next week then!"
    $ hero.calendar.add(game.days_played + 7, LabelAppointment((16, 19), "ayesha", "Meet with Ayesha", "ayesha_sub_event_03", "ayesha_sub_event_03_missed"))
    $ game.pass_time()
    $ DONE["ayesha_sub_event_02"] = game.days_played
    return

label ayesha_sub_event_03_missed:
    "Shit I missed my date with Ayesha."
    $ ayesha.love -= 10
    $ hero.calendar.add(game.days_played + 7, LabelAppointment((16, 19), "ayesha", "Meet with Ayesha", "ayesha_sub_event_03", "ayesha_sub_event_03_missed"))
    return

label ayesha_sub_event_03(appointment=None):
    scene bg bedroom1
    "I have to admit that I'm nervous, never having done this kind of thing before now."
    "But I did agree to help Ayesha increase her toughness for the rigours of the MMA circuit."
    "So it'd be pretty weak of me to cry off now that we're actually about to go through with it."
    "The problem is that I'm just not used to hurting a fly, let alone another human being!"
    "I don't even know if Ayesha being a girl actually makes it better or worse."
    "And that's before I take into account the fact she's built like an Amazonian goddess too!"
    "Can I really inflict pain on someone that I have feelings for?"
    "Can I actually get off on it too?"
    "All of this is preying on my mind as Ayesha closes the door to my bedroom and turns to face me."
    show ayesha normal with dissolve
    ayesha.say "Are you okay, [hero.name]?"
    ayesha.say "Because you look kinda nervous..."
    menu:
        "I'm ok" if hero.sexperience >= 30 and ayesha.sub >= 60:
            mike.say "Ah, yeah..."
            mike.say "This is all new to me, Ayesha."
            mike.say "But don't worry about it - I'll be fine."
            ayesha.say "I'm pretty nervous too, [hero.name]!"
            show ayesha happy
            ayesha.say "But if you're sure..."
            mike.say "I am, Ayesha."
            mike.say "I agreed to help you do this."
            mike.say "And I won't let you down."
            "Ayesha smiles and nods, clearly reassured by my words."
        "We should wait.":
            mike.say "Erm, no, Ayesha..."
            mike.say "I'm so sorry - but I'm just not okay with this."
            mike.say "Hurting you, even if you want it, doesn't feel right."
            "Ayesha nods."
            "She looks disappointed, but also a little relieved."
            ayesha.say "It's okay, [hero.name]."
            show ayesha sad
            ayesha.say "I'd rather you were honest than did something just to please me."
            "She looks down, chuckling to herself."
            "It's then I notice her cheeks are flushing."
            ayesha.say "Actually, it's kinda nice."
            ayesha.say "Knowing that you're not okay with hurting me!"
            ayesha.say "It makes me feel loved."
            $ ayesha.love += 1
            $ hero.calendar.add(game.days_played + 14, LabelAppointment((16, 19), "ayesha", "Meet with Ayesha", "ayesha_sub_event_03", "ayesha_sub_event_03_missed"))
            $ hero.cancel_activity()
            return
    if ayesha.sub.max < 70:
        $ ayesha.sub.max = 70
    "Sure that we're going ahead with this thing, I pull out the instrument I'll be using."
    "I see Ayesha's eyes go wide as she sees it for the first time."
    "But she nods all the same and begins to walk slowly towards me."
    mike.say "Now, Ayesha."
    mike.say "Strip down!"
    "I honestly don't know where the air of command in my voice comes from."
    show ayesha naked
    "But when I see Ayesha jump in surprise and hurry to obey..."
    "Well, let's just say that it's more than enough to start getting me hard!"
    mike.say "Come here, Ayesha."
    mike.say "Right here - and then lie down!"
    "I watch as Ayesha stops a little way from me and lies down over the bed."
    call ayesha_bdsm_choices from _call_ayesha_bdsm_choices_1
    scene bg bedroom1
    "Once we're done, I watch as Ayesha put her panties back."
    show ayesha sport topless
    "She does so gingerly, as if her ass is still sensitive from the spanking."
    "Ayesha smiles at me, a little awkwardly at first."
    show ayesha sport -topless happy
    "But then I see that it's not only the cheeks down there that are burning."
    mike.say "How are you feeling, Ayesha?"
    mike.say "Are you okay?"
    ayesha.say "Y...yeah, I'm okay."
    show ayesha blush
    ayesha.say "That was really...nice!"
    mike.say "Ah, yeah..."
    mike.say "I enjoyed it too!"

    mike.say "You should rest a little before our next session."
    $ game.pass_time()
    $ DONE["ayesha_sub_event_03"] = game.days_played
    return

label ayesha_sub_event_04_missed:
    "Shit I missed my date with Ayesha."
    $ ayesha.love -= 10
    $ hero.calendar.add(game.days_played + 7, LabelAppointment((16, 19), "ayesha", "Meet with Ayesha", "ayesha_sub_event_04", "ayesha_sub_event_04_missed"))
    return

label ayesha_sub_event_04(appointment=None):
    scene bg bedroom1
    "I'm getting a little more comfortable with the idea of doing the kinkier stuff with Ayesha now."
    "Which is lucky for me, as she seems to be getting a taste for that kind of thing too!"
    "So much so, in fact, that we've agreed to take it to the next level."
    "And this time we're going to be trying something quite a bit more adventurous."
    "I just hope that all of this is really helping with her pain threshold."
    "You know, making her better able to endure the punishment she has to take in her MMA matches."
    "Because that was kind of the original point of all this."
    "The chance to get into BDSM and all that stuff was just supposed to be a bonus!"
    "All that being said, I'm still feeling the effects of the nerves when Ayesha finally shows up."
    "So much so that it's an actual relief to see that she seems to be feeling the same way too!"
    show ayesha with dissolve
    ayesha.say "Hey, [hero.name]."
    ayesha.say "So here we are, yeah?"
    ayesha.say "Ready to level up the kink factor?"
    "She doesn't need to come right out and say it."
    "We both know that this is the point where we could call the whole thing off."
    "The question is whether or not either of us is actually going to do it..."
    menu:
        "Let's start" if hero.sexperience >= 50 and ayesha.sub >= 70:
            mike.say "That's the idea, Ayesha."
            mike.say "I really enjoyed myself the last time we messed around like that."
            mike.say "I think we both learned a hell of a lot too."
            ayesha.say "I guess you're right, [hero.name]."
            show ayesha normal
            ayesha.say "And I have to admit..."
            ayesha.say "I had a great time too."
            ayesha.say "I haven't been able to stop thinking about you spanking me!"
            mike.say "Hopefully you'll get the same thrill out of what I have planned today."
            mike.say "It's a bit more intense than last time."
            mike.say "But if you trust me, I'm sure it'll be okay."
            ayesha.say "Sure thing, [hero.name]."
            show ayesha happy
            ayesha.say "I trust you completely."
        "We should wait a little more.":
            mike.say "I feel like I'm supposed to say yes."
            mike.say "But I'm really not, Ayesha."
            mike.say "Spanking you was one thing."
            mike.say "But this...this is starting to feel like actual torture!"
            "Ayesha looks a little disappointed at the admission."
            "Yet she's mature enough to nod, accepting that's just how I feel."
            ayesha.say "It's okay, [hero.name]."
            show ayesha sad
            ayesha.say "I'd rather you were honest than did something just to please me."
            "She looks away, stifling a laugh."
            "As she does so, I can't help seeing that she's actually blushing."
            ayesha.say "I'm sorry, it's just touching, you know?"
            show ayesha happy
            ayesha.say "I like it that you're not okay with hurting me."
            ayesha.say "It's sweet."
            $ ayesha.love += 1
            $ hero.calendar.add(game.days_played + 14, LabelAppointment((16, 19), "ayesha", "Meet with Ayesha", "ayesha_sub_event_04", "ayesha_sub_event_04_missed"))
            $ hero.cancel_activity()
            return
    if ayesha.sub.max < 85:
        $ ayesha.sub.max = 85
    "We both nod, knowing that we're about to get down to it for real."
    "And it's now that I choose to pull out the instrument that we'll be using for the first time."
    "Ayesha's gaze is instantly fixated upon it, and I see her swallow in anticipation."
    "But all the same, she begins to strip off her clothes and make for the bed."
    call ayesha_bdsm_choices from _call_ayesha_bdsm_choices_2
    scene bg bedroom1
    show ayesha naked
    "Neither of us seems to be able to talk for a good while afterwards."
    "Ayesha for the obvious reasons and me because I just inflicted them on her."
    "But eventually, she rolls onto her side and gives me a lazy, exhausted smile."
    ayesha.say "You know, I never thought pain could be so much fun?"
    show ayesha naked blush
    mike.say "Well, didn't a wise man once say - pain is so close to pleasure?"
    ayesha.say "[hero.name], are you REALLY quoting Queen lyrics at me right now?!?"
    "Ayesha laughs and shakes her head, letting me know that she's joking."
    "In fact, she seems like she's nothing but blissful and satisfied."
    "Which makes two of us."
    "And so I smile in return."
    if game.active_date:
        $ game.active_date.score = 100
        mike.say "Let's do this again next week!"
        $ hero.calendar.add(game.days_played + 7, LabelAppointment((16, 19), "ayesha", "Harder training with Ayesha", "ayesha_sub_event_05", "ayesha_sub_event_05_missed"))
    return

label ayesha_sub_event_05_missed:
    "Shit I missed my date with Ayesha."
    $ ayesha.love -= 10
    $ hero.calendar.add(game.days_played + 7, LabelAppointment((16, 19), "ayesha", "Meet with Ayesha", "ayesha_sub_event_05", "ayesha_sub_event_05_missed"))
    return

label ayesha_sub_event_05(appointment=None):
    scene bg bedroom1
    "I'm getting a little more comfortable with the idea of doing the kinkier stuff with Ayesha now."
    "Which is lucky for me, as she seems to be getting a taste for that kind of thing too!"
    "So much so, in fact, that we've agreed to take it to the next level."
    "And this time we're going to be trying something quite a bit more adventurous."
    "I just hope that all of this is really helping with her pain threshold."
    "You know, making her better able to endure the punishment she has to take in her MMA matches."
    "Because that was kind of the original point of all this."
    "The chance to get into BDSM and all that stuff was just supposed to be a bonus!"
    "All that being said, I'm still feeling the effects of the nerves when Ayesha finally shows up."
    "So much so that it's an actual relief to see that she seems to be feeling the same way too!"
    show ayesha with dissolve
    ayesha.say "Hey, [hero.name]."
    ayesha.say "So here we are, yeah?"
    ayesha.say "Ready to level up the kink factor?"
    "She doesn't need to come right out and say it."
    "We both know that this is the point where we could call the whole thing off."
    "The question is whether or not either of us is actually going to do it..."
    menu:
        "Let's start" if hero.sexperience >= 50 and ayesha.sub >= 85:
            mike.say "That's the idea, Ayesha."
            mike.say "I really enjoyed myself the last time we messed around like that."
            mike.say "I think we both learned a hell of a lot too."
            ayesha.say "I guess you're right, [hero.name]."
            show ayesha normal
            ayesha.say "And I have to admit..."
            ayesha.say "I had a great time too."
            ayesha.say "I haven't been able to stop thinking about you spanking me!"
            mike.say "Hopefully you'll get the same thrill out of what I have planned today."
            mike.say "It's a bit more intense than last time."
            mike.say "But if you trust me, I'm sure it'll be okay."
            ayesha.say "Sure thing, [hero.name]."
            show ayesha happy
            ayesha.say "I trust you completely."
        "We should wait a little more.":
            mike.say "I feel like I'm supposed to say yes."
            mike.say "But I'm really not, Ayesha."
            mike.say "Spanking you was one thing."
            mike.say "But this...this is starting to feel like actual torture!"
            "Ayesha looks a little disappointed at the admission."
            "Yet she's mature enough to nod, accepting that's just how I feel."
            ayesha.say "It's okay, [hero.name]."
            show ayesha sad
            ayesha.say "I'd rather you were honest than did something just to please me."
            "She looks away, stifling a laugh."
            "As she does so, I can't help seeing that she's actually blushing."
            ayesha.say "I'm sorry, it's just touching, you know?"
            show ayesha happy
            ayesha.say "I like it that you're not okay with hurting me."
            ayesha.say "It's sweet."
            $ ayesha.love += 1
            $ hero.calendar.add(game.days_played + 14, LabelAppointment((16, 19), "ayesha", "Meet with Ayesha", "ayesha_sub_event_05", "ayesha_sub_event_05_missed"))
            $ hero.cancel_activity()
            return
    if ayesha.sub.max < 100:
        $ ayesha.sub.max = 100
    "We both nod, knowing that we're about to get down to it for real."
    "And it's now that I choose to pull out the instrument that we'll be using for the first time."
    "Ayesha's gaze is instantly fixated upon it, and I see her swallow in anticipation."
    "But all the same, she begins to strip off her clothes and make for the bed."
    call ayesha_bdsm_choices from _call_ayesha_bdsm_choices_3
    scene bg bedroom1
    show ayesha naked
    "Neither of us seems to be able to talk for a good while afterwards."
    "Ayesha for the obvious reasons and me because I just inflicted them on her."
    "But eventually, she rolls onto her side and gives me a lazy, exhausted smile."
    ayesha.say "You know, I never thought pain could be so much fun?"
    show ayesha naked blush
    mike.say "Well, didn't a wise man once say - pain is so close to pleasure?"
    ayesha.say "[hero.name], are you REALLY quoting Queen lyrics at me right now?!?"
    "Ayesha laughs and shakes her head, letting me know that she's joking."
    "In fact, she seems like she's nothing but blissful and satisfied."
    "Which makes two of us."
    "And so I smile in return."
    $ DONE["ayesha_sub_event_05"] = game.days_played
    return

label ayesha_birthday_date_male:
    $ DONE["ayesha_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "date"
    scene bg gym
    "I hurry into the gym, glancing at my watch as I push through the doors."
    "Glancing around, I'm already looking for any sign of Ayesha in the lobby."
    "But she's nowhere to be seen, and I can't help cursing under my breath."
    "We agreed to meet here at this time - so where in the hell is she?"
    "Just then I see her emerge from a doorway, chatting to another couple of girls."
    "And I don't hesitate to hurry over."
    "Ayesha sees me coming, and promptly ends her conversation."
    "She's waving off the other girls as I reach her."
    show ayesha sport with dissolve
    ayesha.say "Hey, [hero.name]!"
    ayesha.say "I'm almost ready for our date."
    ayesha.say "Just need to shower and change, okay?"
    "Ayesha seems to totally miss the fact that I look flustered."
    "Doesn't she know that we're going to be late?"
    if ayesha.sub >= 90:
        show ayesha annoyed
        "Suddenly the expression on Ayesha's face changes dramatically."
        "She shakes her head and looks embarrassed with herself."
        "Then she shuffles closer to me, where nobody else can hear."
        "And she speaks while staring at her feet."
        show ayesha sad
        ayesha.say "I..."
        ayesha.say "I'm sorry, [hero.name]."
        ayesha.say "I've been at work all day."
        ayesha.say "And I forgot that you're not one of my colleagues or clients."
        "I put a finger under Ayesha's chin, lifting her head."
        "And I make sure I'm smiling when she meets my eye."
        mike.say "Apology accepted, Ayesha."
        mike.say "Now run along and get yourself ready."
        mike.say "You can make it up to me by being obedient for the rest of the night."
        show ayesha normal
        $ game.active_date.score += 15
        "Ayesha nods eagerly, and then hurries off to do as she's told."
        hide ayesha with easeoutleft
    else:
        menu:
            "That's fine":
                "I take a deep breath, hold it for a second and then let it out."
                "There's no need to lose my cool here and ruin the date before it starts."
                mike.say "Sure thing, Ayesha."
                mike.say "We're cutting it a little fine for the time I booked the table."
                mike.say "But don't worry - I'll call them while you're in the shower."
                mike.say "And I'll have them move it back, okay?"
                show ayesha annoyed
                "Ayesha looks surprised to hear that we're running late."
                ayesha.say "Oh no!"
                ayesha.say "Should I have been ready earlier?"
                mike.say "It's no problem, Ayesha."
                mike.say "The day can't start until you're there."
                mike.say "We're celebrating your birthday, after all!"
                show ayesha normal
                $ game.active_date.score += 15
                "Ayesha nods and smiles, reassured that everything's okay."
                "Then she hurries off to get ready."
                hide ayesha with easeoutleft
            "I'll wait!":
                "Doesn't she realise how much trouble I went to getting us that reservation?"
                "You'd think Ayesha would be a little more grateful than that!"
                mike.say "We have reservations, Ayesha!"
                mike.say "That means we have to turn up on time!"
                show ayesha annoyed
                "Ayesha looks surprised to hear that we're running late."
                "But she looks even more surprised at the tone I'm using with her."
                ayesha.say "O...okay, [hero.name]..."
                ayesha.say "I'm sorry to cause a hold up..."
                ayesha.say "I'll try to be quick, yeah?"
                "I nod at this, but my expression is still one of frustration."
                "I shake my head as Ayesha hurries off to get ready."
                hide ayesha with easeoutleft
                "Fantastic, just fantastic."
                $ game.active_date.score -= 10
                "We haven't even got to the restaurant yet."
                "And already things are going wrong."
    "True to her word, Ayesha's back sooner than I would have thought possible."
    "And she looks great too!"
    show ayesha date normal with easeinleft
    "There's no trace of the exertions of the gym about her."
    "She smells absolutely amazing."
    "And the outfit that she has on gets the seal of approval from me too!"
    show ayesha happy
    ayesha.say "Come on, [hero.name]..."
    ayesha.say "Let's go eat already!"
    scene bg door restaurant with fade
    "Luckily for us, I chose to book a table at a restaurant within walking distance."
    scene bg restaurant with fade
    $ ayesha.flags.forceLocation = (game.days_played, game.hour, "restaurant")
    "So soon after we step out of the gym, Ayesha and I are walking into the place."
    "A member of the waiting staff greets us and checks the reservation."
    show ayesha date normal at center, zoomAt(1.5, (740, 1040)) with easeinright
    "Then we're shown to our table without further delay."
    show ayesha date annoyed at center, zoomAt(1.5, (640, 1040)) with ease
    "But as we're sitting down, I notice that Ayesha looks uncomfortable."
    mike.say "What's the matter, Ayesha?"
    mike.say "Don't you like the look of the place?"
    "Ayesha shakes her head."
    ayesha.say "No, [hero.name]..."
    ayesha.say "It's not that..."
    ayesha.say "I just feel like people are...looking at me, you know?"
    "I glance around, and I can't say that I see anyone staring."
    "But I do notice that Ayesha must be the tallest woman in here by a clear foot!"
    if ayesha.sub >= 90:
        mike.say "You shouldn't be worrying about anyone but me, Ayesha."
        mike.say "The only person that should concern you is me."
        "Ayesha nods her head."
        "And she forces a smile onto her face."
        show ayesha blush
        ayesha.say "Of...of course, [hero.name]!"
        ayesha.say "How foolish of me."
        "I nod to show my approval, and let the matter drop."
        "But the reminder does seem to have had the desired effect."
        show ayesha happy
        "Now Ayesha's eyes are focused solely on me."
        "And she seems to be forgetting all about her previous concerns."
        $ game.active_date.score += 15
    elif hero.charm >= 65:
        mike.say "Of course they're staring, Ayesha."
        mike.say "They've never seen a woman as stunning as you before!"
        show ayesha surprised
        "Ayesha looks at me, blinking in surprise."
        ayesha.say "Y...you're just saying that, [hero.name]..."
        show ayesha blush
        ayesha.say "And it's kind of you..."
        "I shake my head and reach out to take Ayesha's hand."
        mike.say "Don't say that, Ayesha!"
        mike.say "I mean it - you look amazing tonight."
        mike.say "And who cares why anyone else is looking at you?"
        mike.say "Just remember I'm doing it because I can't get enough of what I see."
        "Ayesha blushes and turns away for a moment."
        show ayesha happy
        "But when she looks me in the eye again, it's with a newfound confidence."
        $ game.active_date.score += 15
    else:
        mike.say "Of course they're staring at you, Ayesha..."
        mike.say "You're freaking huge!"
        "I shrug helplessly."
        "Because what else am I going to say?"
        "That's the truth, and there's no denying it."
        show ayesha blush
        "Ayesha blushes and hunkers down in her seat."
        "Yeah, as if that's going to make her stand out any less!"
        show ayesha angry
        ayesha.say "Okay, okay..."
        ayesha.say "You made your point!"
        show ayesha annoyed
        ayesha.say "Can we just drop it now?"
        $ game.active_date.score -= 10
    "Before we sit down at the table, Ayesha pauses by her chair."
    show ayesha normal
    "It looks like she's waiting for something to happen."
    "And for a moment, I'm not sure what it could be."
    "But then I realise what the problem is."
    if ayesha.sub >= 90:
        "Ayesha must be waiting for permission to sit down!"
        mike.say "Be seated, Ayesha."
        show ayesha happy
        "Ayesha nods gratefully and does as she's told."
        "And then I sit down myself."
        "Secure in the knowledge that everyone knows their place."
        $ game.active_date.score += 15
    else:
        menu:
            "Pull out her chair":
                "Ayesha must be waiting for me to pull her chair out for her."
                "Wow - I can be such a dumbass sometimes!"
                "I hurry around to Ayesha's side of the table."
                "And I pull out her chair, gesturing for her to sit down."
                show ayesha date happy at center, zoomAt(1.5, (640, 1140)) with ease
                "Ayesha nods and smiles happily, letting me know that I was right."
                "Once she's comfortably seated, I can return to my own seat."
                "And I sit down on it secure in the knowledge that I just scored myself a couple of bonus points there."
                $ game.active_date.score += 15
            "Sit first":
                "Ayesha must be waiting for me to sit down first."
                "Wow - she has such good manners!"
                "Not wanting to keep her waiting, I pull out my chair and sit down."
                show ayesha surprised
                "Ayesha looks at me in surprise, like that wasn't supposed to happen."
                show ayesha annoyed at center, zoomAt(1.5, (640, 1140)) with ease
                "But then she seems to shake it off and sits down herself."
                "Yet she has a look on her face like she's more than a little disappointed."
                $ game.active_date.score -= 10

    show restaurant meal ayesha date with fade
    "Ayesha picks up a menu and starts to look at what's on offer."
    "I've pretty much made up my mind that I want to devour a steak."
    "But I make a point of pretending to read it too, just for show."
    ayesha.say "Hmm..."
    ayesha.say "I wonder if they'd do me a couple of plain chicken breasts?"
    ayesha.say "I'm gonna ask..."
    ayesha.say "But you know how weird some places can be about special orders, right?"
    if ayesha.sub >= 90:
        mike.say "Since when have you been ordering for yourself, Ayesha?"
        mike.say "That's something your master should be doing for you."
        mike.say "I'll be having the steak, medium-rare."
        mike.say "And I think that'll do for you too."
        "Ayesha's eyes go wide as she realises her mistake."
        "She lowers her head and nods demurely."
        ayesha.say "Yes, master."
        ayesha.say "Of course, [hero.name]."
        show restaurant meal ayesha ayeshahappy
        ayesha.say "That sounds just perfect."
        $ game.active_date.score += 15
    else:
        if hero.fitness >= 85:
            "At first I wonder why Ayesha would want plain chicken breast."
            "But then I remember that it's high in protein and low in fat."
            "She must be eating it as part of her training regimen."
            mike.say "I know, Ayesha."
            mike.say "But you should still make a point of asking."
            mike.say "Diet's super important when you're in training."
            "Ayesha nods at this happily."
            "And she looks impressed at my knowledge on the subject too."
            show restaurant meal ayesha ayeshahappy
            ayesha.say "You're right, [hero.name]."
            ayesha.say "I shouldn't be afraid to ask."
            $ game.active_date.score += 15
        else:
            "Urgh!"
            "Why would anyone want plain chicken breast?"
            mike.say "That sounds really boring, Ayesha!"
            mike.say "Aren't we supposed to be celebrating?"
            mike.say "At least ask them to put some sauce on it or something!"
            "Ayesha frowns at me over her menu."
            "And I don't need to be told that she's less than impressed."
            show restaurant meal ayesha ayeshabored
            ayesha.say "I need something that's high in protein and low in fat, [hero.name]!"
            ayesha.say "Don't you remember that I'm in training right now?"
            ayesha.say "Honestly, sometimes I think you don't listen to a word I say!"
            $ game.active_date.score -= 10

    "The waiter shows up a few minutes later, interrupting our conversation."
    "But that's no big deal, as we were more than ready to order anyway."
    "After he takes our orders, it's literally only a minute or two until they turn up."
    "The speediness of the service seems a little odd."
    "But it looks like Ayesha doesn't mind at all."
    show restaurant meal ayesha ayeshahappy
    ayesha.say "Mmm!"
    ayesha.say "Finally..."
    ayesha.say "I could eat a horse!"
    "She picks up her knife and fork, then almost pounces on her food."
    "Which leaves me to just shrug and follow her lead."
    if randint(0, 1) == 0:
        "As we're tucking into our meals, I hear a sound under the table."
        "But when I make to look under there, Ayesha reaches out and stops me."
        ayesha.say "Whoa..."
        show restaurant meal ayesha -ayeshahappy
        ayesha.say "No need for that, [hero.name]."
        ayesha.say "I just kicked my shoes of, that's all."
        ayesha.say "My feet are aching from being up on them all day!"
        "I raise an eyebrow at the explanation."
        "And at the same time I use my feet to slip off my own shoes."
        mike.say "Leave it to me, Ayesha..."
        "Ayesha looks puzzled for a moment."
        "But the she feels my feet begin to massage hers under the table."
        ayesha.say "Whoa!"
        ayesha.say "You want to play footsie with me?"
        if hero.has_skill("massage"):
            "I nod and smile as I use my toes and the soles of my feet."
            "What I want to do is massage Ayesha's with them."
            "Then I can move on up the leg."
            "And who knows where it'll end!"
            "I watch as Ayesha's face melts into an expression of bliss."
            "As the muscles of her feet relax, so does she."
            "Pretty soon she's sinking back into her chair."
            "And I have to pull back on the massage a moment later."
            "Because I'm afraid she might fall out of her chair!"
            show restaurant meal ayesha ayeshahappy
            ayesha.say "Oh, man..."
            ayesha.say "Where did you learn to do that?"
            "Ayesha's smiling at me as she says this."
            "But she has a hungry look in her eyes now."
            "One that reminds me of a lioness eyeing up her next meal!"
            $ game.active_date.score += 15
        else:
            "I nod and smile as I use my toes and the soles of my feet."
            "What I want to do is massage Ayesha's with them."
            "Then I can move on up the leg."
            "And who knows where it'll end!"
            "But a moment later, Ayesha's face creases up."
            "And she grimaces in pain."
            show restaurant meal ayesha ayeshabored
            ayesha.say "Arrgh..."
            ayesha.say "Oh hell..."
            ayesha.say "You gave me a cramp!"
            "I watch, cringing in horror as Ayesha writhes from the pain."
            "And I pull my feet back as she tries to rub life back into her leg."
            $ game.active_date.score -= 10
    else:
        "We're happily eating our meals when I notice that there's something wrong."
        "Cutting into the steak on my plate, I prod the exposed middle with a finger."
        "Seeing what I'm doing, Ayesha leans in closer and catches my eye."
        show restaurant meal ayesha -ayeshahappy
        ayesha.say "What's the matter, [hero.name]?"
        ayesha.say "Is there something wrong with your meal?"
        "I look up and nod my head."
        mike.say "Yeah, Ayesha..."
        mike.say "I don't think this is cooked all the way through."
        ayesha.say "Oh..."
        ayesha.say "So what are you going to do about it?"
        menu:
            "Ask quietly for the waiter's attention":
                mike.say "Don't worry, Ayesha."
                mike.say "I just need to let the waiter know, that's all."
                "Looking around, I manage to catch the waiter's eye."
                "And then I wave him over with a smile."
                show restaurant meal waiter ayesha
                "Waiter" "Anything the matter, sir?"
                mike.say "Sorry, but I don't think this is cooked all the way through."
                "The waiter leans in to examine the steak."
                "And then he nods curtly."
                "Waiter" "I see what you mean, sir."
                "Waiter" "I'll have this replaced right away."
                "Waiter" "Terribly sorry about that."
                show restaurant meal ayesha ayeshahappy -waiter
                "I look over to see that Ayesha looks relieved."
                "Probably because I handled that with a minimum of fuss."
                $ game.active_date.score += 15
            "Make a scene to get the waiter's attention":
                mike.say "There's only one thing to do in a situation like this."
                mike.say "And that's to complain in the strongest manner possible!"
                "Ayesha holds up her hands and shakes her head."
                show restaurant meal ayesha ayeshabored
                "But I make a point of ignoring her."
                "Looking around, I manage to catch the waiter's eye."
                "And then I wave him over with a frown."
                "Waiter" "Anything the matter, sir?"
                show restaurant meal waiter ayesha ayeshabored
                mike.say "You bet there is!"
                mike.say "My steak is undercooked!"
                mike.say "What kind of shitty service is this?!?"
                "And then he nods curtly."
                "Waiter" "I see what you mean, sir."
                "Waiter" "I'll have this replaced right away."
                "Waiter" "Terribly sorry about that."
                mike.say "And so you should be!"
                show restaurant meal -waiter ayesha ayeshabored
                "I look over to see Ayesha visibly cringing in her seat."
                "For some reason, she looks like she wants to ground to open and swallow her up!"
                $ game.active_date.score -= 10
    scene bg black
    show restaurant meal ayesha date
    "Ayesha must be pretty hungry from her day working at the gym."
    "Because she's tearing into her food like she's starving!"
    "I guess she's enjoying it too, because she's in a world of her own."
    "But when I glance around, I see that people are starting to look over here."
    "It doesn't take me long to realise what they're looking at either."
    "A genuine Amazon the likes of Ayesha, demolishing her meal."
    "Well, that's not something you see every day!"
    "I'm just not sure that being the centre of attention is such a good thing!"
    if ayesha.sub >= 90:
        "I cough to get Ayesha's attention."
        "And she looks up at the sound."
        "So I know that all of her attention is on me."
        mike.say "Ahem..."
        mike.say "Small, neat bites, Ayesha."
        mike.say "You're not a horse eating out of a nose-bag!"
        "Ayesha nods and looks down at the table."
        show restaurant meal ayesha ayeshablush
        "The shame of what she's done written all over her face."
        "I nod and allow myself a smile."
        "Because I know she's been put in her place."
        $ game.active_date.score += 15
    else:
        menu:
            "Ask about her food":
                "I think for a moment, and then an idea comes to me."
                mike.say "Ayesha..."
                mike.say "Have you let this stuff rest in your mouth a little?"
                mike.say "I mean, really taken the time to savour it?"
                show restaurant meal ayesha ayeshabored
                "Ayesha looks a little puzzled at first."
                "But then she seems to take my advice."
                "She starts to chew slowly, really taking her time."
                "And I see a smile spread slowly across her face as she does so."
                show restaurant meal ayesha ayeshahappy
                ayesha.say "Wow..."
                ayesha.say "I see what you mean!"
                ayesha.say "That's pretty special."
                ayesha.say "I'm so used to cramming down junk from the vending machines at work."
                ayesha.say "I don't usually have the time to enjoy my food!"
                "I smile and nod, happy to have been able to avoid a scene."
                $ game.active_date.score += 15
            "Tell Ayesha off":
                "I hiss through my teeth at Ayesha."
                "Hoping that nobody will hear me doing so."
                mike.say "Ayesha!"
                mike.say "Ayesha!"
                "She looks up at me from her plate."
                "And from the expression on her face, I can see she's totally clueless."
                show restaurant meal ayesha ayeshabored
                ayesha.say "Huh?"
                mike.say "Will you take it easy?"
                mike.say "People are starting to stare at you!"
                show restaurant meal ayesha -ayeshabored
                "Ayesha looks around, seeming to notice for the first time."
                "And as soon as she does, Ayesha's face drops."
                show restaurant meal ayesha ayeshabored
                ayesha.say "Oh god..."
                ayesha.say "This is SO embarrassing!"
                "I nod and roll my eyes."
                "Letting her know that I think so too."
                $ game.active_date.score -= 10
    scene bg black
    show restaurant meal ayesha date
    "Once we've finished our main courses, the waiter takes away the plates."
    "And we fall into a natural kind of lull, just waiting for him to return."
    "It's about then that I realise Ayesha is studying me intently."
    "In fact, it's like she's waiting for me to do something."
    show restaurant meal ayesha ayeshahappy
    ayesha.say "It was so nice of you to suggest we do this, [hero.name]."
    ayesha.say "Not just going out to a nice restaurant."
    ayesha.say "But doing it on my birthday too..."
    "I wasn't sure what Ayesha was hinting at before."
    "But that last statement made it pretty plain."
    "She's obviously wondering if I got her a gift for her birthday."
    if not hero.has_gifts:
        "Well...this is awkward!"
        "I didn't actually get anything for Ayesha."
        "I was kind of thinking that the meal at the restaurant was enough!"
        mike.say "Well, you know, Ayesha..."
        mike.say "Some guys would buy you a flashy gift."
        mike.say "Something you'd probably forget all about before too long."
        mike.say "But not me - I'm giving you great memories instead!"
        "I smile, trying to sell Ayesha on the idea."
        "And she nods slowly."
        show restaurant meal ayesha ayeshabored
        "But I can tell that she's more than a little disappointed."
        $ game.active_date.score -= 20
        $ ayesha.love -= 10
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_4
        if _return != "done":
            if _return not in ["None", "exit"]:
                "Which is a convenient chance to show her that's just what I did!"
                "I smile and pull out the gift from where I've been hiding it."
                mike.say "That's not all, Ayesha..."
                mike.say "Here you go - happy birthday!"
                "Ayesha lets out a surprisingly girlish giggle of delight."
                show restaurant meal ayesha ayeshahappy
                ayesha.say "Ooh!"
                ayesha.say "Thank you!"
                show restaurant meal ayesha -ayeshahappy
                if _return:
                    play sound [paper_ripping_1, paper_ripping_2]
                    "As soon as she tears off the paper, Ayesha's face lights up."
                    ayesha.say "[hero.name]..."
                    show restaurant meal ayesha ayeshahappy
                    ayesha.say "This is amazing!"
                    ayesha.say "It's just what I wanted!"
                    $ game.active_date.score += 15
                    mike.say "No worries, Ayesha."
                    mike.say "I'm glad you like it."
                else:
                    play sound [paper_ripping_1, paper_ripping_2]
                    "The moment she tears off the paper, Ayesha's face falls."
                    ayesha.say "Oh..."
                    ayesha.say "Thanks...I guess."
                    "I shake my head, concerned at her reaction."
                    mike.say "Erm..."
                    mike.say "Isn't that what you wanted?"
                    "Ayesha suddenly snaps out of it."
                    show restaurant meal ayesha ayeshabored
                    "And I see her force a smile onto her face."
                    ayesha.say "Oh..."
                    ayesha.say "Yeah, [hero.name]..."
                    ayesha.say "It's great...just great."
                    $ game.active_date.score -= 10
            else:
                "Well...this is awkward!"
                "I didn't actually get anything for Ayesha."
                "I was kind of thinking that the meal at the restaurant was enough!"
                mike.say "Well, you know, Ayesha..."
                mike.say "Some guys would buy you a flashy gift."
                mike.say "Something you'd probably forget all about before too long."
                mike.say "But not me - I'm giving you great memories instead!"
                "I smile, trying to sell Ayesha on the idea."
                "And she nods slowly."
                show restaurant meal ayesha ayeshabored
                "But I can tell that she's more than a little disappointed."
                $ game.active_date.score -= 20
                $ ayesha.love -= 10
    scene bg black
    show restaurant meal ayesha date
    "Ayesha picks up the menu for a second time."
    "And she turns straight to the dessert section."
    "I watch as her eyes scan the page."
    "Then I see them light up."
    "But that doesn't last for long."
    "She seems to remember something."
    "And then she lets out a sigh."
    mike.say "What's up, Ayesha?"
    mike.say "Don't you like the dessert selection?"
    ayesha.say "Oh no, it's not that."
    ayesha.say "I just looked at the calorie content on some of them."
    ayesha.say "And there's no way I can eat a whole one."
    ayesha.say "Not with the nutrition plan I'm on right now!"
    if ayesha.sub >= 90:
        "I shake my head at Ayesha."
        mike.say "You'll only be ordering a dessert if I say so, Ayesha."
        mike.say "My word is more important than any ridiculous diet."
        mike.say "You remember that!"
        "Ayesha lowers her eyes and nods her head."
        show restaurant meal ayesha ayeshablush
        ayesha.say "Yes, [hero.name]."
        ayesha.say "Thank you, [hero.name]."
        $ game.active_date.score += 15
    else:
        menu:
            "We can share":
                "Something in what Ayesha just said catches my attention."
                mike.say "Wait a minute, Ayesha..."
                mike.say "If you eat a WHOLE one?"
                mike.say "Like...you could eat half of one and be okay?"
                "Ayesha nods."
                show restaurant meal ayesha ayeshahappy
                ayesha.say "Yeah, [hero.name]..."
                ayesha.say "That wouldn't put me over the limit."
                mike.say "Then we'll just share one!"
                "I call the waiter over and we order Ayesha's choice of dessert."
                "And I'm sure to ask for two spoons as well."
                "Once it arrives, we both attack it with gusto."
                $ game.active_date.score += 15
            "That seems reasonable":
                "I shake my head and smile."
                mike.say "That's the price you have to pay, Ayesha."
                mike.say "No pain, no gain!"
                show restaurant meal ayesha ayeshabored
                "I call the waiter over and order myself a dessert."
                "And I do the best I can to ignore Ayesha as I eat it."
                "After all, I don't want to let her staring ruin my appetite!"
                $ game.active_date.score -= 10
    "Once the meal is over, we settle the bill and leave a generous tip."
    "Then it looks like Ayesha and I are ready to call it a night."
    "Not that I want to end the date myself."
    "I'm just prepared for the fact that Ayesha might want to."
    scene bg door restaurant
    show ayesha date normal
    with fade
    mike.say "So..."
    mike.say "Where do we go from here, Ayesha?"
    mike.say "I understand if you're tired - you've had a long day at the gym!"
    if game.active_date.score >= 80 and ayesha.sexperience >= 1:
        "Ayesha shakes her head, a smile spreading across her face."
        "And then she grabs me by the wrist."
        show ayesha blush
        ayesha.say "Oh..."
        ayesha.say "I think I have a little something left in the tank!"
        "Before I can say another word, Ayesha turns and walks away."
        "And I'm dragged along with her, too surprised to offer any resistance."
        "Ayesha pulls me into a nearby alley, walking almost to the end of it."
        "Once we're sure not to be seen from the street, she stops."
        "And then she slams me bodily into the wall."
        scene bg alley
        show ayesha blush date
        with fade
        ayesha.say "I had SUCH a good time tonight, [hero.name]."
        ayesha.say "But now I need you to make it even better."
        ayesha.say "I need you to fuck me..."
        ayesha.say "And I want it REAL hard too!"
        call ayesha_birthday_sex from _call_ayesha_birthday_sex
    else:
        "Ayesha nods hastily."
        "And then she adds a nod for good measure."
        "Though I get the feeling it's not one hundred percent genuine in nature..."
        ayesha.say "Oooh..."
        ayesha.say "Damn right, [hero.name]!"
        ayesha.say "I had a great time tonight."
        show ayesha annoyed
        ayesha.say "But I am pretty bushed!"
        "I nod, knowing when to admit defeat."
        mike.say "Okay, Ayesha..."
        mike.say "Let's get you home."
        "I turn and begin trying to hail a taxi for Ayesha."
        "Because it looks like our date has come to a natural conclusion."
        hide ayesha
    return

label ayesha_birthday_sex:
    scene bg alley
    show ayesha date blush
    with fade
    "I must have done something right on our date tonight."
    "Because Ayesha is all over me."
    "In fact, she's almost manhandling me right now!"
    "I've never seen her acting like this before."
    "She's dragged me off the street and into a back-alley."
    "And now she's on me like a wild animal!"
    "Ayesha uses all of her weight to push me hard against the wall."
    hide ayesha
    show ayesha kiss date
    with fade
    $ ayesha.flags.kiss += 1
    "Then she plants her lips on mine, kissing me almost desperately."
    "I can already feel the effect she's having on my body."
    "My heart is pounding in my chest."
    "I feel hot, almost prickly with need for her."
    "And needless to say, my cock is so hard that it hurts!"
    "Suddenly Ayesha breaks off the kiss, gasping as she does so."
    hide ayesha kiss
    show ayesha date blush at center, zoomAt(1.5, (640, 1040))
    with fade
    ayesha.say "Uh..."
    ayesha.say "Ah..."
    ayesha.say "[hero.name]..."
    ayesha.say "I can't hold back!"
    "Ayesha wraps me in her arms, squeezing me against her."
    "Now I can feel her heart pounding too."
    "And I can smell the sweet scent of her perspiration."
    "It's like a pheromone to me, making me want her all the more."
    ayesha.say "I...I need it!"
    ayesha.say "Right now!"
    "I nod eagerly, wanting noting more than to please her."
    "Being wrapped up by Ayesha isn't in the least bit scary."
    "And having a woman toss me about doesn't feel emasculating."
    "It's more like she's a predatory animal, stalking and capturing me."
    "One that's in heat, pulsing with a musky, intoxicating sexuality."
    "All of a sudden I feel something click in my head."
    "I realise that Ayesha's not trying to dominate me."
    "Rather she's trying to make me match her physicality."
    "That thought gives me the impetus to take matters into my own hands."
    "Ayesha already made this a rough affair, so I decide to keep it that way."
    "I slip my arms out of her bear-hug."
    "And then I grab hold of her buttocks with my hands."
    "Ayesha yelps in surprise as I squeeze them."
    "But that's not all I'm trying to do, as I also lift her off her feet."
    "Turning around, I only stop once she's the one with her back to the wall."
    "Making contact with the bricks doesn't dull Ayesha's ardour one bit."
    "In fact she nods and clings on even tighter than ever."
    "And when I use my hands to pull up her skirt, she does all she can to help."
    ayesha.say "Oh yeah..."
    ayesha.say "That's it..."
    ayesha.say "I can almost feel you inside of me!"
    "Clumsily we fumble with Ayesha's panties."
    "They're yanked down to her knees, then her ankles."
    "And finally she raises one leg, pulling them over her foot."
    "They slide down her other leg, falling to the ground to be forgotten."
    "That done, I press her against the wall."
    scene bg black
    show ayesha stand alley date
    with fade
    "She yelps in surprise again, but clings onto me harder still."
    "I can only guess that's because she's not used to being moved around."
    "That most guys are afraid to take the lead with her and get physical."
    "More the fool them."
    "She's panting the whole time, like my show of strength is turning her on."
    "And then she begins to rub the head against the lips of her pussy."
    "Now it's my turn to feel an instant surge in my desire for her."
    "As if her hand on the shaft wasn't enough!"
    "No, what's really turning me on is the fact that Ayesha's wet as hell down there."
    show ayesha stand vaginal pose2
    "The head of my cock slips and slides over the folds of her pussy."
    "And it's only a matter of seconds until I start to sink into her."
    show ayesha stand pose1 pain
    "Ayesha moans as I fill her, allowing me to take total control."
    "Before she was assertive and demanding."
    "But now she seems content to put herself in my hands."
    show ayesha stand normal
    "The sensation is something else, feeling a lioness turn into a kitten!"
    "And while we started things out rough, they now take a more gentle turn."
    show ayesha stand pose2
    "I'm not pounding away at Ayesha like my life depends on it."
    "Instead I take my time, making sure that every movement counts."
    show ayesha stand pose1
    "And she seems to appreciate my efforts more with each passing second."
    "Ayesha's head is laid on my shoulder, her arms around my waist."
    show ayesha stand pose2
    "She switches between kissing my neck and muttering with pleasure."
    "But the real reward for me is the feeling of her body against mine."
    show ayesha stand pose1
    "Every inch of her muscles are relaxed, almost limp in my arms."
    "Honestly, I feel like I'm embracing a goddess in repose!"
    show ayesha stand pose2
    "I forget that I was dragged into an alleyway a few moments ago."
    "All that matters to me is Ayesha and the act of giving her pleasure."
    show ayesha stand pose1 pleasure
    ayesha.say "Mmm..."
    ayesha.say "[hero.name]..."
    ayesha.say "Don't stop..."
    show ayesha stand pose2
    "I chuckle to myself at the very idea of me stopping now."
    "And in response I begin to pick up a little more speed."
    show ayesha stand pose1
    pause 0.35
    show ayesha stand pose2 at startle(0.05,-10)
    "Ayesha nods and I hear her start to pant with more intensity."
    "Slowly her grip on me tightens, the strength returning to her limbs."
    show ayesha stand pose1
    pause 0.35
    show ayesha stand pose2 at startle(0.05,-10)
    "It's kind of how I imagine being squeezed by a python must feel."
    "But with the thrill of fulfilment on the cards."
    show ayesha stand pose1
    pause 0.35
    show ayesha stand pose2 at startle(0.05,-10)
    "Rather than the threat of imminent death!"
    "I'm determined not to surrender my strength though."
    show ayesha stand pose1
    pause 0.25
    show ayesha stand pose2 at startle(0.05,-10)
    "And so I meet Ayesha's awakening with all that I have left."
    show ayesha stand pose1
    pause 0.25
    show ayesha stand pose2 at startle(0.05,-10)
    "This means that she starts to grunt and gasp as I thrust into her."
    show ayesha stand pose1
    pause 0.15
    show ayesha stand pose2 at startle(0.05,-10)
    pause 0.25
    show ayesha stand pose1
    pause 0.15
    show ayesha stand pose2 at startle(0.05,-10)
    "But the sounds coming out of me are every bit as intense and fierce too."
    show ayesha stand pose1
    pause 0.15
    show ayesha stand pose2 at startle(0.05,-10)
    pause 0.25
    show ayesha stand pose1
    pause 0.15
    show ayesha stand pose2 at startle(0.05,-10)
    "I have no intention of stopping before the end."
    show ayesha stand pose1
    pause 0.15
    show ayesha stand pose2 at startle(0.05,-10)
    pause 0.25
    show ayesha stand pose1
    pause 0.15
    show ayesha stand pose2 at startle(0.05,-10)
    "And the only thing that slows me down is the sensation of losing it."
    show ayesha stand pose1 ahegao
    pause 0.15
    show ayesha stand pose2 at startle(0.05,-10)
    pause 0.25
    show ayesha stand pose1
    pause 0.15
    show ayesha stand pose2 at startle(0.05,-10)
    pause 0.25
    show ayesha stand pose1
    pause 0.15
    show ayesha stand pose2 with hpunch
    pause 0.25
    show ayesha stand pose1
    pause 0.15
    show ayesha stand pose2 creampie with hpunch
    "Ayesha follows my example as I shoot my load into her."
    with hpunch
    "Her arms and legs hug me like those of a bear."
    with hpunch
    "And I swear that even the muscles of her pussy are squeezing the life out of me!"
    "In the end, only the wall keeps us up on our feet."
    "And we're left clinging to each other, trembling and spent."
    $ ayesha.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
