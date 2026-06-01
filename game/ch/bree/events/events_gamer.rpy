init python:
    InteractEvent(**{
    "name": "bree_event_05",
    "label": "bree_event_05",
    "duration": 2,
    "conditions": [
        IsDone("bree_event_03"),
        IsNotDone("bree_event_04"),
        IsDayOfWeek("123456"),
        IsHour(18, 20),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        HasSkill("video_games"),
        PersonTarget(bree,
            IsActive(),
            MinStat("love", 80),
            ),
        ],
    "priority": 500,
    "do_once": True,
    "music": "music/roa_music/juice.ogg",
    })

    InteractEvent(**{
    "name": "bree_event_06",
    "label": "bree_event_06",
    "conditions": [
        IsDone("bree_event_05"),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(bree,
            IsActive(),
            MinStat("love", 100),
            MinStat("sub", 50),
            MinStat("sexperience", 1),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    InteractEvent(**{
    "name": "bree_event_07",
    "label": "bree_event_07",
    "conditions": [
        IsDone("bree_event_06"),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(bree,
            IsActive(),
            MinStat("love", 110),
            MinStat("sexperience", 1),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_08",
    "label": "bree_event_08",
    "duration": 6,
    "conditions": [
        IsDone("bree_event_07"),
        HeroTarget(IsGender("male")),
        IsHour(8, 20),
        PersonTarget(bree,
            Not(IsHidden()),
            IsFlag("tournament", False),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_09",
    "label": "bree_event_09",
    "duration": 1,
    "conditions": [
        IsDone("bree_event_08"),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("breedelay", False),
            MinStat("love", 130),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_10",
    "label": "bree_event_10",
    "duration": 1,
    "conditions": [
        IsDone("bree_event_09"),
        IsHour(7, 20),
        HeroTarget(
            IsGender("male"),
            IsActivity("play_videogames"),
            IsRoom("livingroom"),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            IsFlag("breedelay", False),
            MinStat("love", 140),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_11",
    "label": "bree_event_11",
    "duration": 2,
    "conditions": [
        IsDone("bree_event_10"),
        HeroTarget(IsGender("male")),
        IsHour(10, 14),
        PersonTarget(bree,
            Not(IsHidden()),
            IsFlag("breedelay", False),
            MinStat("love", 150),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_12",
    "label": "bree_event_12",
    "duration": 2,
    "conditions": [
        IsDone("bree_event_11"),
        IsDayOfWeek("67"),
        IsHour(8, 18),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("breedelay", False),
            MinStat("love", 160),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    InteractEvent(**{
    "name": "bree_event_13",
    "label": "bree_event_13",
    "duration": 5,
    "conditions": [
        IsDone("bree_event_12"),
        IsHour(20, 0),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(bree,
            IsActive(),
            IsFlag("breedelay", False),
            MinStat("love", 170),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    InteractEvent(**{
    "name": "bree_event_14",
    "label": "bree_event_14",
    "conditions": [
        IsDone("bree_event_13"),
        IsHour(16, 0),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(bree,
            IsActive(),
            IsFlag("breedelay", False),
            MinStat("love", 180),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    InteractEvent(**{
    "name": "bree_event_15",
    "label": "bree_event_15",
    "duration": 1,
    "conditions": [
        IsDone("bree_event_14"),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(bree,
            IsActive(),
            IsFlag("breedelay", False),
            MinStat("love", 190),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    InteractEvent(**{
    "name": "bree_event_16",
    "label": "bree_event_16",
    "duration": 1,
    "conditions": [
        IsDone("bree_event_15"),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(bree,
            IsActive(),
            IsFlag("breedelay", False),
            MinStat("love", 200),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_17",
    "label": "bree_event_17",
    "duration": 1,
    "conditions": [
        IsDone("bree_event_16"),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom"),
            Or(
                IsActivity("play_videogames"),
                IsActivity("play_videogames_with_bree"),
                ),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("breedelay", False),
            Not(IsActivity("sleep")),
            ),
        RoomTarget("livingroom",
            NPCNumber(1),
            NPCInRoom("bree",),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_event_18",
    "label": "bree_event_18",
    "duration": 1,
    "conditions": [
        IsDone("bree_event_17"),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom"),
            Or(
                IsActivity("play_videogames"),
                IsActivity("play_videogames_with_bree"),
                ),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("breedelay", False),
            Not(IsActivity("sleep")),
            ),
        RoomTarget('livingroom',
            NPCNumber(1),
            NPCInRoom('bree'),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    "quit": False,
    })

label bree_event_05:
    if bree.love.max < 100:
        $ bree.love.max = 100
    show bree
    "[bree.name]'s holding a flyer in her hand, crinkled at the edges."
    show bree talkative
    bree.say "You won't believe what I found!"
    show bree normal
    "I raise an eyebrow."
    mike.say "A job?"
    show bree surprised
    bree.say "Wha- no! But... yes. Shut up!"
    show bree normal at center, zoomAt(1.5, (640, 1140)), vshake
    "[bree.name] plops down on the couch next to me. She hands the flyer over to me and I take it with a tired hand. I look down at it."
    "When my eyes focus, I'm drawn to the bright colours, explosive graphics, and the main header."
    "Arcade Tournament! Join us at 7PM for a battle against gamers! Prize of 500{image=gui/icons/icon_money.png}! Sign up to compete today!"
    mike.say "A tournament?"
    show bree happy
    bree.say "Yeah, a tournament!"
    show bree normal
    mike.say "Are you saying you want to enter?"
    show bree smile
    bree.say "Like, yeah! You see the prize money, right? I can totally pay for rent with that."
    show bree normal
    mike.say "I mean, if you really want to, I don't care. Do you really think you can win?"
    show bree smile
    bree.say "I might as well try, ya know? It'll be good money until I can find a job."
    show bree normal
    mike.say "Alright, alright. You know it says there's an entry fee?"
    show bree sad
    pause 0.5
    show bree flirt
    "[bree.name]'s face falls for a millisecond, but in just as much time she's batting her eyes at me."
    show bree smile blush
    bree.say "Okay, I know I owe you for rent, but will you help me? Please? Please, please? I'll totally make it up to you!"
    show bree flirt -blush
    "I sigh. The fee isn't too much- 15{image=gui/icons/icon_money.png}. If [bree.name] can really win this, then it would be well worth it."
    menu:
        "Pay the Fee" if hero.money >= 15:
            show bree happy
            bree.say "Thank you so much! You won't regret it, I promise!"
            mike.say "Yeah, yeah. You better win!"
            $ bree.love += 1
            $ hero.money -= 15
        "Refuse":
            mike.say "Sorry, I can't do that. I need to pay for my own things."
            show bree sad
            bree.say "Aww. Alright. I'll have to figure something out then."
            bree.say "Maybe I can ask Sasha when she gets home."
            $ bree.love -= 1
    show bree normal
    mike.say "Do you know what game the competition is for?"
    "[bree.name] promptly takes the flyer out of my hands, flips it, and has me stare at the back. Oh. Alley Brawler."
    "I can vaguely remember a magazine guide and a cartridge of that game on [bree.name]'s shelf in her room. Maybe she really did have a chance."
    show bree happy
    bree.say "See! I can do it."
    show bree normal
    mike.say "Yeah, okay. But this is coming up in a few days."
    show bree smile
    bree.say "Don't worry! We can go to the arcade to practice."
    show bree normal
    mike.say "Um- we?"
    show bree smile
    bree.say "Yes, we. I need someone to compete against! Let's go! The arcade's gonna close soon."
    menu:
        "No Way":
            $ bree.love -= 1
            mike.say "No- no way. I just got home from work."
            show bree talkative blush
            bree.say "Please! You gotta help me, [hero.name]."
            show bree flirt -blush
            mike.say "Sorry. I need my sleep."
            show bree sad
            bree.say "...Alright."
            return
        "Fine, Let's Go":
            $ bree.love += 1
            $ bree.flags.wentToArcade = True
    mike.say "What, now?"
    hide bree
    show bree at center, zoomAt (1.25, (640, 880))
    with vpunch
    "[bree.name]'s pulling me off the couch before I can blink."
    mike.say "Hey- woah! Can we at least pick up some coffee on the way?"
    scene bg black with dissolve
    pause 0.1
    scene bg arcade with dissolve
    "There's not too many people in line at the arcade machine [bree.name] wants to use."
    show kat casual zorder 2 at center, zoomAt(1.25, (640, 1100))
    show bree a casual zorder 1 at left
    with dissolve
    "In fact there's only one person- a girl, sitting in a pulled up chair, with wrappers and a paper cup set on top of it."
    "It didn't look like she was moving."
    show bree a smile at right4 with ease
    bree.say "Hiya!"
    bree.say "How long do you think you'll be using that?"
    show bree normal
    "Girl" "..."
    "Girl" "Until I'm done."
    "Thank god we picked up coffee."
    "I can already tell where this is going."
    show bree talkative
    show fx question at right4
    bree.say "What does that mean? Done with the round?"
    show bree sadsmile
    "The other girl doesn't answer, instead tapping away on the bright arcade buttons."
    show bree a vangry
    bree.say "Hey!"
    show bree a annoyed
    "[bree.name] knocks on the top of the machine with her knuckles, grabbing the other girl's attention."
    show bree a vangry
    bree.say "You can't, like, hog the game!"
    show bree a angry
    "Girl" "Yeah. I can. I'm playing as long as I want. Now fuck off, blondey."
    show bree surprised at vshake
    "[bree.name] seems to be shocked into silence- honestly, I kind of am too."
    show bree gloomy
    "[bree.name] looks over at me with pleading eyes. Did she want me to do something?"
    menu:
        "Intimidate":
            $ bree.love += 1
            if hero.fitness < 50:
                "I puff out my chest and step forward."
                "I could ask nicely, but she didn't seem like the kind of person to listen."
                mike.say "Let her have a turn."
                "She mockingly coos at me, puckering her lips."
                "Girl" "Ooh~! Is the boyfriend coming to save the wench in distress?"
                mike.say "Don't call her that."
                "Girl" "Aw, what are you going to do? Stare at me to death?"
                mike.say "Wha-"
                "Girl" "Either you and your blonde slut get out of my face or I scream 'rape'. Your choice."
                show bree at right5 with ease
                "Before I can answer, [bree.name] grabs onto my elbow. I look back at her in irritation, but her expression says to back down."
                show bree sad
                bree.say "C'mon, [hero.name]. We can come back tomorrow or something."
                show bree sadsmile
                mike.say "But-"
                show bree talkative at right with ease
                bree.say "Let's go."
                show bree sadsmile
                mike.say "..."
                mike.say "Okay."
                scene bg mall1
                show bree gloomy
                with fade
                "[bree.name] leads me out of the arcade until we come to the mall's street."
                "I feel a little bad for not getting the game for her, but there was always tomorrow."
            else:
                mike.say "How old are you, seriously? Move."
                "Girl" "Oh yeah? What are you going to do?"
                mike.say "You can get up yourself or I can move you and your little chair out to the street."
                show bree surprised
                show fx exclamation at right4
                bree.say "[hero.name]!"
                show bree stuned at right5 with move
                "I ignore [bree.name]'s whisper of disapproval in favour of staring the girl down- which was quite easy, considering she was already sitting."
                "Her lips are pursed, as if considering if I'd really do it."
                "Girl" "... Fine. I'm leaving. Geez, teach your boyfriend how to chill."
                hide kat
                show kat casual at center, vshake
                "She promptly stands up and leaves, not sparing either of us another glance."
                hide kat with easeoutleft
                "I move to wipe off the scraps she left behind and set the paper cup on the floor next to the machine."
                $ bree.love += 1
                show bree sadsmile at center with ease
                bree.say "..."
                show bree smile
                bree.say "... Thanks, [hero.name]."
                show bree sadsmile
                mike.say "No problem."
                mike.say "Something wrong?"
                "[bree.name] looks pale, now that I'm looking at her."
                show bree talkative
                bree.say "No. I just... think you should be nice about it next time."
                show bree sadsmile
                mike.say "Uh, sure. Sorry."
                show bree normal
                "[bree.name] shakes her head lightly and throws me a small smile, before standing in front of the game."
                "She doesn't look at me as the screen lights up her face in the darkness of the arcade."
                "She makes a few offhand quips as she starts a new game, but I could tell something was wrong."
        "Persuade":
            $ bree.love += 1
            if hero.knowledge < 50:
                "The best way to ask was to ask nicely, right?"
                mike.say "Hey, can you let her have a chance?"
                "The girl tears her eyes away from the screen."
                mike.say "..."
                mike.say "Please?"
                "A few seconds pass with a silence that makes me think she didn't hear me. Until she bursts out laughing."
                "Girl" "You're so cute! Honestly, you're adorable. But, really, leave me alone or this will get ugly."
                mike.say "Really?"
                show bree at right5 with ease
                "She shoots both of us a bone chilling glare. In the side of my vision, I see [bree.name] take a step back."
                show bree sad
                bree.say "Let's get out of here."
                show bree gloomy
                mike.say "Fine. We can come back tomorrow."
                "Girl" "I wouldn't count on that!"
                scene bg mall1
                show bree gloomy
                with fade
                "[bree.name] leads me out of the arcade until we come to the mall's street."
                "I feel a little bad for not getting the game for her, but there was always tomorrow- whether that bitch likes it or not."
            else:
                mike.say "Hey- listen."
                "I step in front of [bree.name], facing the girl who was still halfheartedly paying attention to both of us."
                mike.say "This is a public place. You can't exactly keep people from playing. So you either finish your game or we get the manager and see what he has to say? But we don't want to get mixed up in that, do we?"
                "For the first time, the girl tears her eyes away from the screen. Her irises are piercing, giving me a glare that probably sends other people running."
                hide kat
                show kat casual at center
                "A moment of silence passes of an intense staring contest, but it breaks once she forcefully grabs her paper cup and shoves the chair out from under her."
                "Girl" "Fine. Whatever. I don't want to be here anyway."
                hide kat with moveoutleft
                "With that, she walks off. I almost think she'll shoulder check me by the look on her face, but I'm surprised when I'm left alone."
                show bree flirt at center with move
                bree.say "..."
                $ bree.love += 2
                show bree smile
                bree.say "Wow! Thanks, [hero.name]! That was, like, super cool."
                show bree normal
                mike.say "Yeah, no problem. She was a bitch about it anyway."
                show bree happy
                bree.say "Mega bitch."
                show bree normal
                "I smile at her wording as she pushes the chair aside and chooses to stand instead."
                "The screen flashes with vibrant colours at the start of a new game."
                show bree smile
                bree.say "Will you still coach me a little?"
                show bree normal
                "Coaching was a strong word. In fact, she was probably better than me."
                mike.say "Yeah, of course."
        "Stay out of it":
            $ bree.flags.stayedoutkat = True
            $ bree.love -= 1
            "Something tells me I should stay out of this. In fact, so should [bree.name]. This girl didn't exactly seem stable."
            show bree sad
            bree.say "Hey! You can't- This is- ..."
            "Girl" "What's wrong? Dick got your tongue?"
            show bree stuned blush
            "[bree.name] turns bright red at this, stuttering at the other girl's blatant phrasing."
            "Girl" "Ha! I knew it. All you blondes are sluts. Is he your pimp? This is hilarious! Your own pimp can't even stand up for you!"
            show bree vangry
            show fx anger at right4
            bree.say "Shut up! Don't talk about him like that!"
            show bree angry
            "Wait, me?"
            mike.say "[bree.name], maybe we should-"
            "Girl" "He speaks! Tell me, how much did you have to pay her to get with someone that looks like you?"
            show bree at right5 with ease
            "By the end of her sentence, there's a sudden splash and a screech. I blink, until I realize [bree.name] had turned the girl's cup upside down on her head."
            "Brown, bubbly liquid, which I can only assume is soda, spills from her hair and down her shirt."
            show kat at vshake
            "Girl" "What the hell!"
            hide kat
            show kat at center, vshake
            "She stands up, desperately trying to shake herself off. She gives out another shriek of frustration before rushing off in the direction of the bathrooms."
            "Girl" "Bitch!"
            "..."
            "I look over at [bree.name], whose face is still red, but this time I recognize it at anger."
            mike.say "Um... maybe we should get out of here before she gets back."
            "She numbly nods, regret suddenly crashing over her with the fall of her expression."
            hide bree with easeoutright
            "I take her hand and lead her outside of the arcade. She immediately turns to face me."
            scene bg mall1
            show bree a casual sad
            with fade
            bree.say "I'm not like that, [hero.name], I swear! I don't know what I was thinking."
            show bree gloomy
            mike.say "It's fine. She had it coming anyway, so I wouldn't feel too bad."
            show bree sadsmile
            "[bree.name] doesn't look convinced."
            mike.say "You can't tell me she wasn't a bitch."
            bree.say "..."
            show bree evil
            bree.say "A total bitch."
            show bree annoyed
            "I give her a smile."
            mike.say "How about we head home? We can come back tomorrow."
            show bree smile
            bree.say "... Okay."
    hide bree
    return

label bree_event_06:
    if bree.love.max < 110:
        $ bree.love.max = 110
    if bree.sub.max < 75:
        $ bree.sub.max = 75
    scene bg livingroom
    show bree fuckgames at center, zoomAt(1.5, (960, 750))
    with fade
    "Walking into the sitting room, I'm treated to the sight of [bree.name] laid on her belly in front of the TV, a controller clutched in her hands."
    "And a second later I hear her let out the loudest moan possible, without even looking away from the screen."
    "Instantly I know that the moan was meant for my ears, as she can clearly see my reflection in front of her."
    "And I can't help rolling my eyes as I silence a groan that almost come out of my own mouth in response."
    "Oh great - [bree.name]'s binging on the videogames again!"
    "Now just let me say that I'm not hating on the fact that one of my female housemates is an avid gamer."
    "Male or female, it's a pretty sweet habit in someone you happen to live with."
    "And I even consider myself a gamer, at least with a small 'G'."
    "Plus I'm not that possessive of the console that we have in the sitting room."
    "But let's just say that [bree.name] happens to be one of those gamers that's always into the latest thing."
    "And the flipside of that is how she tends to get very bored very quickly once she's beaten a game."
    "I flop down on the sofa behind [bree.name], making a point of ignoring the continued moans she's letting out."
    "Sure, it might sound like I'm being a complete dick to her right now."
    "But look at it from my point of view - she's basically fishing for someone to listen to her complaining."
    "If I hadn't been caught in that very same trap more than once before, I might be a little more sympathetic."
    show bree fuckgames angry
    bree.say "Urrgh!"
    bree.say "Boring, boring, boring!"
    "Well, that pretty much seals my fate."
    "When [bree.name] switches from silent to vocal attention seeking, you know that she's serious!"
    "So now I have one of two possible choices."
    "One is to get up and walk straight out of the room, which risks serious repercussions."
    "And the other is to just get it over with and bite the bullet."
    "Can you guess which one I'll choose?"
    mike.say "Hey, [bree.name]."
    mike.say "I get the oddest feeling you're trying to tell me something."
    mike.say "Could it be that you're a little bored?"
    show bree fuckgames normal
    "Almost instantly, [bree.name] rolls onto her side and looks back over her shoulder at me."
    "She holds the controller in one hand and uses the other to gesture vaguely back at the TV screen."
    bree.say "It's this damn game, [hero.name]."
    bree.say "I've beaten it on every difficulty setting already."
    bree.say "And I've unlocked all of the trophies too!"
    "I can't help but shrug at [bree.name]'s litany of First World problems."
    mike.say "Yeah, I know that sucks."
    mike.say "But couldn't you, I don't know...play something else?"
    "This suggestion is met with a groan that's worthy of a stropping teenager."
    "And [bree.name] even kicks her legs on the floor, almost as if she's having a tantrum."
    bree.say "That's no good, [hero.name]."
    bree.say "I've beaten all of those too."
    bree.say "And it's ages until payday - so I'm broke and I can't buy anything new!"
    "For a moment I almost forget that I'm actually talking to another adult."
    "And I'm seriously considering telling [bree.name] to go to her room and finish her homework."
    "But then I remember that she's supposed to be a grown woman, and another idea occurs to me."
    "One that could be a hell of a lot more fun and save me from her whining all at once..."
    mike.say "I bet you couldn't beat the game if you had, I don't know, maybe a...distraction?"
    "I see [bree.name]'s eyebrows shoot up at this, letting me know that I've caught her interest."
    bree.say "A distraction?"
    bree.say "What kind of distraction?"
    "I shrug, trying for all I'm worth to look like I'm just suggesting something off the top of my head."
    mike.say "I don't know, [bree.name]."
    mike.say "Maybe something that normally takes up all your attention?"
    bree.say "Like what, [hero.name]."
    "Looks like she's biting."
    "Now it's time to reel her in."
    mike.say "Well, it'd have to be a thing someone else can do to you."
    mike.say "Perhaps..."
    mike.say "Nah - you'd never go for that!"
    "[bree.name] shakes her head almost the same second that I seem to dismiss the idea."
    "Now I know that I've hooked her!"
    bree.say "No, no..."
    bree.say "What were you going to say?"
    "Okay...here goes nothing!"
    mike.say "What if you let me fuck you?"
    bree.say "Huh?!?"
    mike.say "While you play the game - I could fuck you as a distraction?"
    "It's now that I see realisation dawning on [bree.name]'s face for the first time."
    "And then her lips curl slowly into a smile as she ponders the suggestion."
    bree.say "Ah, [hero.name]."
    mike.say "Yeah?"
    bree.say "Sasha's out, right?"
    mike.say "Right."
    bree.say "And the door's locked, right?"
    mike.say "Right."
    bree.say "Okay, you got it!"
    "For a moment, I can't believe what I'm hearing."
    mike.say "Really?!?"
    bree.say "Yeah, really!"
    "And just to make herself clear, [bree.name] turns back onto her belly in front of me."
    "But this time she makes damn sure that I see how she raises her ass and stretches as she does so."
    "If that wasn't enough of an open invitation, I watch as she then pulls down her panties too!"
    bree.say "Hmm..."
    bree.say "What are you waiting for, [hero.name]?"
    bree.say "Plug your joystick into me, and let's get playing already!"
    "I nod frantically as I pull down my own pants and clamber onto the floor behind [bree.name]."
    hide bree fuckgames
    show bree fuckgames dick
    with vpunch
    "In my haste, I almost trip over myself and end up half falling onto her."
    bree.say "Oooh!"
    bree.say "I guess player one's ready!"
    bree.say "His joystick certainly feels like it's nice and stiff..."
    "Looking over her shoulder, I can see that [bree.name]'s about to start a new game."
    "Which means that I need to hurry up and choose where I plug myself in..."
    menu:
        "Fuck her ass" if bree.flags.anal >= 2:
            "I'm guessing that [bree.name]'s expecting me to make straight for her pussy."
            "And as inviting as that is, it's also the most obvious choice on offer."
            "But the idea here is to change things up a little and relieve her sense of boredom."
            "So that's why I take one cheek in each hand and part her buttocks."
            bree.say "Huh?"
            bree.say "What are you..."
            "Before she can get the rest of the words out, I push myself into her ass."
            bree.say "Oh..."
            bree.say "Oh god..."
            bree.say "Ooooh god!"
            show bree fuckgames -dick fx
            "[bree.name]'s moans become longer and more drawn out."
            "And at the same time, I keep on sinking deeper into her."
            "The muscles of her ass contract, trying to keep me out."
            "But I have all of my weight pressing down on her right now."
            "And so the feeling of them being pushed aside is almost indescribable."
            "The whole time I'm looking over [bree.name]'s shoulder at the TV."
            "Not at the action that's happening in the game, but at her reflection in the screen itself."
            "I watch the effect it has on her as I begin to move in and out."
            "Her mouth is already hanging open, and her eyes rolling up into her head."
            "[bree.name] tries as best she can to keep on playing the game."
            "But I can see that she's already doing badly."
            "She keeps on taking her eyes off of the screen and fumbling with the controller."
            "Her on-screen presence seems to be as much affected as she is."
            "The jerky actions of her fingers and thumbs translating into random, crazy movements in the sprite."
            "All of this only serves to make me try even harder."
            "And I pound [bree.name]'s ass all the more."
            show bree fuckgames fx lose
            "Somehow seeing my efforts render her incapable of playing is a massive turn on!"
            "I know that I've got [bree.name] beaten when she finally drops the controller on the floor."
            "At the same time she half collapses over it, any hint of resistance disappearing."
            show bree fuckgames ahegao with hpunch
            "She makes small panting noises as I feel myself getting ready to cum."
            with hpunch
            "And as I lose it, as deep into her ass as I can get, I happen to glance up at the screen."
            with hpunch
            "All that there is to see on there is the all too familiar 'Game Over' screen."
            "Of course, I can't help smirking as I look down at [bree.name]."
            "Thinking how appropriate that statement is for the mess she's in right now."
        "Fuck her pussy":
            $ CONDOM = False
            if hero.has_condom():
                menu:
                    "Equip a shield":
                        $ CONDOM = hero.use_condom()
                    "Nah defence is for losers. Swing that sword":
                        pass
            "I guess this brings a whole new meaning to the term 'plug in and play'!"
            "But awful puns aside, all I have eyes for right now is [bree.name]'s tight little pussy."
            show bree fuckgames -dick
            "And as soon as I get the head of my cock down there, I begin to rub it against her lips."
            "They're already getting slick, and that makes me all the more eager to get inside of her."
            "All it take is a little change of angle, and I can feel it happening."
            bree.say "Mmm..."
            bree.say "Oooh yeah!"
            bree.say "Player one has entered the game!"
            "I wanted to take things slow, to draw this out as long as I could."
            "But it feels so good to be inside of [bree.name] that I struggle not to just let go."
            show bree fuckgames fx
            "And that's when my eyes fall on the TV screen, seeing her reflection in it."
            "Sure, she has a pretty big smile on her face, letting me know she's liking it."
            "And yet it's the action taking place on the screen that suddenly catches my attention."
            "I knew that [bree.name] was pretty good at this game already."
            "But now she looks like she's totally smashing it!"
            "As I push in and out of her, I watch her sprite move and the score on screen begin climb."
            "It'd be pretty impressive under any other circumstances."
            "Even more so with the knowledge that she's currently taking a pounding!"
            "There's also something oddly familiar about the way in which [bree.name]'s playing too."
            "I can't quite put my finger on it at first."
            "But then I realise that she's moving and reacting in a strange kind of rhythm with my own."
            "Soon it's almost impossible for me to keep my eyes off of the screen."
            "And I could swear that it feels like I'm the one playing the game, rather than [bree.name] herself."
            "The better the pace and tempo that I manage to achieve, the better the results on the screen."
            "Pretty soon I can't help giving a mental cheer and congratulating myself whenever something good happens in the game."
            with hpunch
            "Which means it should come as no surprise that I feel myself cumming as [bree.name] faces down a serious boss challenge."
            with hpunch
            "Almost the very same moment that the boss goes down in flames, I lose myself inside of her."
            show bree fuckgames ahegao with hpunch
            "I can still feel my cock inside of [bree.name] and hear her panting before me."
            "But all the same, the screen that's congratulating the player on their victory feels like it's just for me..."
    $ bree.sexperience += 1
    hide bree
    return

label bree_event_07:
    if bree.love.max < 120:
        $ bree.love.max = 120
    scene bg livingroom
    "Even before I make it in there, I can already hear the noise of simulated carnage coming from the sitting room."
    "The familiar sounds of gunfire, explosions and the pitiful cries of the wounded and dying fill my ears."
    "And I know exactly what it all means - [bree.name]'s winding down and relaxing on the Zbox again!"
    "Sure enough I'm greeted by the usual seizure-inducing lightshow as soon as I actually walk into the room."
    mike.say "Hey [bree.name]."
    mike.say "Committing pixelated genocide again, huh?"
    show bree surprised sleep at center, zoomAt(1.5, (640, 1140))
    show fx question
    bree.say "Wha..."
    show bree smile
    bree.say "Oh...hi, [hero.name]."
    bree.say "Can't talk right now - playing!"
    show bree normal
    "[bree.name] doesn't even bother to pause the game as she says this."
    "Instead she turns her head in my direction for a couple of seconds."
    show bree stuned
    "But then something seems to go wrong for her on the screen."
    show bree angry
    "Her gaze snaps back towards the TV, and she mutters a curse under her breath."
    "I can't be sure if the foul language is directed towards me or the universe in general."
    "And so I choose to ignore it, instead taking the chance to sit down on the sofa beside [bree.name]."
    "I know better than to sit too close for fear of distracting her for a second time."
    "But a little distance also means that I can check her out without fear of being caught in the act."
    "[bree.name]'s sitting cross-legged on the sofa, wearing nothing but her MLP t-shirt and panties."
    show bree normal
    "She bobs up and down as she plays the game, alternately cheering and cursing according to her luck."
    "Sure, I live with her and I get to see this kind of thing pretty often."
    "But it's still quite a sight to happen upon in the sitting room!"
    show bree vangry
    bree.say "Oooh..."
    bree.say "No you don't!"
    show bree smile
    show fx exclamation
    bree.say "HAH - take that!"
    show bree evil
    bree.say "You see what happens when you mess with me, asshole?!?"
    show bree normal
    "I can't help but have my attention dragged away from admiring the sight of [bree.name] in her panties."
    "The veritable verbal assault that she's delivering makes me want to see the screen for myself."
    "What on earth could have inspired her to get that worked up?"
    mike.say "Oh, Star Vixen!"
    mike.say "Yeah, this level's a real pain in the ass."
    "But then I actually take in what's happening on the screen."
    "And I can't help starting in sheer amazement."
    mike.say "Wow, [bree.name] - that's a pretty incredible score to have racked up!"
    mike.say "You're crazy good at this game."
    show bree angry
    show fx anger
    with vpunch
    bree.say "EAT SHIT AND DIE, MOTHERFUCKER!!!"
    show bree surprised
    bree.say "What...oh, not you, [hero.name]!"
    show bree talkative
    bree.say "Yeah, I guess I've been playing this game a lot."
    bree.say "I can almost play it with my eyes closed now."
    bree.say "And it's getting kinda boring."
    show bree sadsmile
    "I frown at this, trying to think of a solution."
    "Even though [bree.name]'s not asked for one, I still feel compelled to help out any way I can."
    mike.say "Well..."
    mike.say "You could try giving yourself a handicap?"
    show bree talkative
    bree.say "I dunno, [hero.name]."
    bree.say "I'm already on the highest difficulty setting as it is!"
    show bree sadsmile
    mike.say "Something else then..."
    mike.say "Maybe try doing something at the same time?"
    show bree hesitating
    show fx question
    bree.say "Like what, exactly?"
    show bree normal
    "I don't know where the idea comes from, but it pops into my head all the same."
    "And before I can really think about what I'm saying, the words just leap out of my mouth."
    mike.say "Bet you couldn't beat that level while you're giving me a blowjob."
    "For the first time since I came into the room, [bree.name] actually pauses the game."
    show bree stuned blush
    "She turns her head to regard me with an odd look on her face."
    "It's half shock and half what looks like amused intrigue."
    show bree surprised
    show fx question
    bree.say "Are you serious?"
    show bree stuned
    mike.say "I...I guess so."
    mike.say "Yeah, [bree.name], I am!"
    show bree evil
    "I watch as a slow smile spreads across [bree.name]'s face."
    show bree smile
    bree.say "Okay, [hero.name] - you're on!"
    "Part of me can't believe my luck that she actually said yes."
    "But another part of me is already trying to play it off as no big deal!"
    show bree naked with dissolve
    "So I make the best show I can of smiling casually as [bree.name] restarts the game, get undressed and then unzips my flies."
    scene bg black
    show bree bjgames
    with fade
    "She pulls my cock out with one hand, holding the joypad with the other."
    show bree bjgames down
    "Her attention is split between the console and my cock."
    show bree bjgames back medium
    "But that doesn't mean it takes long for me to get as hard as a rock at her touch."
    show bree bjgames up big
    "[bree.name] rubs the shaft with her hand as she manoeuvres herself into position."
    "I lay back on the sofa, letting her sprawl across my lap and hold the joypad out before her."
    show bree bjgames back
    "From this position, I can barely see over her shoulder."
    show bree bjgames down lick
    "But I can feel her lips already wrapping around the head of my cock."
    "As she needs both hands to play the game, [bree.name] has no choice but to put it straight into her mouth."
    show bree bjgames up blow -big
    "This means that the blowjob effectively starts before she's playing the game."
    "And I have the pleasure of feeling her try to get into a position where everything will work."
    "[bree.name] finally manages to get herself ready, but saliva is already running down the sides of my cock!"
    show bree bjgames down
    "And when she hits the button to start her game, the action begins in earnest."
    "At first, [bree.name] seems to be paying far more attention to the game than to me."
    show bree bjgames back
    "All she can do is mouth my cock in a vague manner."
    "Which means that she produces more drool for herself than pleasure for me!"
    show bree bjgames up
    "But soon she begins to settle into a rhythm that's more enjoyable."
    "There's no way that she can hope to perform oral gymnastics on me right now."
    show bree bjgames down
    "In fact most of her actual attention is focused on playing the game."
    "And the upshot of that is that the blowjob becomes more about quantity than quality."
    show bree bjgames up
    "Don't get me wrong here - I love oral when it's full of finesse."
    "But there's something gratifying about having my cock in [bree.name]'s mouth this whole time."
    show bree bjgames back
    "All the while she's sucking and licking at it absently."
    "It's almost like her mouth is just there for the sake of getting me off!"
    show bree bjgames up
    "The passive experience gets taken to a whole other level as [bree.name] really gets into the game."
    "She begins to move her head up and down in sympathy to the actions playing out on the screen."
    show bree bjgames down
    "When her starfighter pulls up or swoops down, her head does so too."
    "And she sways from one side to the other as it banks and rolls."
    show bree bjgames back sweat
    "The sensation's pretty incredible."
    "All the more so because I never know what's coming next."
    show bree bjgames down
    "Watching the starfighter as it moves on-screen, I almost feel like my cock's become a joystick!"
    show bree bjgames up serious
    "But then I feel the blowjob become suddenly more intense."
    show bree bjgames down
    "And I realise that [bree.name]'s fast approaching the most challenging part of the level!"
    "She's about to face the boss, and I'm feeling every little bit of adrenaline in her body."
    show bree bjgames back anger
    "[bree.name] squares up to the final challenge, and I can feel the end coming for me too."
    show bree bjgames down inmouth blush with vpunch
    "Almost the exact same moment that she lands the killer blow, I blow my own load."
    show bree bjgames down breath -serious -anger with hpunch
    "We both shoot together, but the game's not quite over for [bree.name] just yet."
    with hpunch
    "She drops the joypad and grabs hold of my cock."
    show bree bjgames medium -blow -inmouth -blush
    "[bree.name] pulls it out of her mouth so that she can swallow without choking."
    "And then she wipes away the last strings of cum and saliva from her lips."
    show bree bjgames up small -sweat -breath
    mike.say "Are...are you okay, [bree.name]?"
    bree.say "Ah...ah..."
    bree.say "Yeah..."
    show bree bjgames lose
    bree.say "I think...I beat...my high score!"
    $ bree.flags.tournament = TemporaryFlag(True, 5)
    hide bree
    return

label bree_event_08:
    if bree.love.max < 130:
        $ bree.love.max = 130
    "On the day of the actual tournament, I prepare myself like I'm some kind of serious athlete."
    "Seriously, I'm running up and down the stairs while shadow-boxing and all that stuff!"
    "The whole time I'm giving myself a pep-talk worthy of a prize fighter or marathon runner."
    "And when it's actually time to go, I run out of the front door hyped and ready for anything."
    show bg street with fade
    "All of which means I'm already in the zone when I meet [bree.name] outside the venue."
    show bree casual talkative with dissolve
    bree.say "Oh, [hero.name], are you okay?"
    show bree normal
    mike.say "Wh...what's that, [bree.name]?"
    mike.say "Why wouldn't I be okay?"
    show bree hesitating
    bree.say "It's just that..."
    bree.say "Well, you look a little intense, you know?"
    bree.say "And sweaty too!"
    show bree normal
    mike.say "I'm fine, [bree.name], trust me."
    mike.say "I'm just ready to do this thing, okay?"
    show bree smile
    bree.say "Sure, [hero.name], if you say so..."
    bree.say "Let's just get in there, yeah?"
    hide bree with easeoutleft
    "I nod, following close on [bree.name]'s heels as she hurries inside."
    scene bg arena with fade
    "I let out an impressed whistle as [bree.name] and I walk into the room where the tournament is being held."
    "It's huge, more like an arena than somewhere that you'd think to sit down and play videogames."
    "There's a stage, a fancy lighting rig, huge screens on the walls."
    "Not to mention row upon row of seating for spectators too."
    show bree casual at center, zoomAt(1.25, (640, 880)) with dissolve
    mike.say "Whoa, [bree.name] - this is some SERIOUS shit!"
    show bree happy
    bree.say "Well, duh, [hero.name]!"
    show bree smile
    bree.say "Esports are a big deal these days, didn't you know?"
    bree.say "This was never going to happen in the basement of some nerd's mom!"
    show bree normal
    "I shake my head, still trying to come to terms with how impressive the whole thing is."
    mike.say "Yeah, yeah..."
    mike.say "But I thought we'd be in one of those function rooms, you know?"
    mike.say "The kind they rent out for wedding receptions and business seminars!"
    show bree happy
    bree.say "Oh, [hero.name]!"
    bree.say "You're so cute when you're out of your depth!"
    show bree normal
    "I choose to ignore the backhanded compliment and instead glance around the hall."
    mike.say "That looks like the place you sign in, over there."
    show bree smile
    bree.say "Come on - let's get our names down."
    show bree normal at center, traveling(1.5, 0.3, (640, 1040))
    "[bree.name] grabs me by the hand, pulling me after her."
    hide bree
    show bree casual
    with fade
    "We're quickly signed in and handed official-looking lanyards with our names on them."
    show bree happy
    bree.say "Oooh - these are fancy!"
    show bree normal
    "She's still fiddling with her lanyard as we find our seats on the stage."
    show bree smile
    bree.say "I wonder who we're gonna be up against?"
    show bree normal at left with ease
    show kat casual at right with easeinright
    show fx anger at right
    kat.say "Urgh..."
    kat.say "Not you two again!"
    show bree sad
    show fx drop at left
    bree.say "Eww..."
    if bree.flags.wentToArcade:
        show bree vangry
        bree.say "[hero.name], look!"
        bree.say "It's that awful girl - the one from the arcade!"
        show bree annoyed
        "I look around to see that [bree.name]'s right."
        "Standing there is the same hollow-eyed girl with lilac hair."
        "The one that was hogging the coin-op machine in the mall arcade."
    else:
        "[bree.name] leans over and whispers:"
        show bree vangry
        bree.say "She was an awful player I met at the arcade once."
        show bree annoyed
    "I lean forward to scrutinise her lanyard."
    mike.say "So, you're...'CandyBarKiller'?"
    kat.say "Yeah, but it's 'Kat' to my friends."
    hide fx
    hide kat
    hide bree
    play music "music/TeknoAXE/simple_metal.ogg" loop
    hide screen overlay_ui
    play sound woosh_punch
    show arenakat with moveinleft
    kat.say "And neither of you losers are my friend!"
    play sound woosh_punch
    show arenabree with moveinright
    bree.say "Yeah, well you can call me 'PrincessNinjaKitty'."
    window hide
    $ quick_menu = False
    show arenatext with dissolve
    pause 0.25


    show arenabigtext at hshake with dissolve
    pause 2.5
    hide arenatext
    hide arenabigtext
    window show
    $ quick_menu = True
    with dissolve
    bree.say "And this right here is 'PsychoRockGod'!"
    "Kat's lip curls at the way [bree.name] pronounces our gaming handles."
    kat.say "Whatever!"
    kat.say "BlackDevilDog and I are gonna wipe the floor with your asses!"
    "Guy" "What's up, Kat?"
    "Guy" "Are these sorry specimens some of our opposition?"
    "I see a tall, pale and worryingly thin guy appear at her side."
    "He looks down his long nose at us, pushing his glasses back up with a bony finger."
    kat.say "Don't worry, Colin."
    kat.say "We can take 'em!"
    mike.say "You guys talk a good fight."
    mike.say "But we're going to let our playing do all the talking for us!"
    bree.say "Yeah, bring it on!"
    hide arenakat
    hide arenabree
    show screen overlay_ui
    show bree casual at center, zoomAt(1.5, (640, 1040))
    with dissolve
    "And just like that, we're into it."
    "[bree.name] and I have been practicing every chance that we had leading up to this."
    "But even so, it's still going to be tough to beat the other players we're up against."
    "The first time we get to take a break, [bree.name] and I study the leader board."
    mike.say "We're doing pretty good so far."
    mike.say "I really think we've got a chance of winning this thing, [bree.name]!"
    show bree evil
    bree.say "Yeah, but we've got serious competition from these two creeps!"
    show bree normal
    "I see what she means."
    "CandyBarKiller and BlackDevilDog are out there in the lead."
    mike.say "We're going to have to out-play them then."
    show bree smile
    bree.say "Maybe..."
    bree.say "Maybe not..."
    show bree normal
    mike.say "What do you mean, [bree.name]?"
    show bree talkative
    bree.say "Well, I've been watching that Colin guy play."
    show bree normal
    "I raise an eyebrow at her using his real name, rather than his gaming handle."
    show bree vangry
    bree.say "[hero.name] - I'm not calling him BlackDevilDog!"
    show bree talkative
    bree.say "Anyway..."
    bree.say "I'm almost one hundred percent sure he's using a cheat of some kind."
    bree.say "And I think we should tell the judges too!"
    show bree normal
    menu:
        "Report the cheater":
            $ bree.love += 2
            mike.say "Yeah, [bree.name]."
            mike.say "We should do that."
            hide bree with easeoutright
            "I watch as [bree.name] walks over to the nearest tournament official and shares her concerns with them."
            "And then we both try to act nonchalant as the same official approaches BlackDevilDog."
            "Colin" "What's this all about?"
            "Judge" "We've had an accusation of cheating."
            show kat at left with easeinleft
            kat.say "That's bullshit!"
            "Judge" "Just let me look at your station, please?"
            show bree casual evil at right with easeinright
            "I see CandyBarKiller eyeing us suspiciously."
            show fx question at left
            kat.say "Was it them?"
            kat.say "Did they put you up to this?"
            "Judge" "I can't share that information."
            "Judge" "But I can tell you that your partner's a cheater."
            "The pair of them stare at the screen as the official presents his findings."
            "Colin" "What...no...I..."
            "Colin" "Someone must have framed me!"
            "Judge" "Whatever, dude - you're still disqualified."
            show kat at left, vshake
            kat.say "He's right - you're a goddamn cheater!"
            "She shakes her head in disbelief as the official drags BlackDevilDog away."
        "Be cautious":
            $ bree.sub += 1
            $ bree.love -= 1
            mike.say "Are you SURE about this, [bree.name]?"
            mike.say "Because if they don't find anything..."
            mike.say "Well, it's going to look like sour grapes on out part!"
            show bree talkative
            bree.say "It WAS more of a hunch than anything else..."
            show bree sadsmile
            mike.say "Look, [bree.name], I think we can beat these guys anyway - cheaters or not!"
            show bree talkative
            bree.say "Okay, [hero.name] - let's do it!"
            hide bree
            show bree normal casual
            with fade
            "My next match just so happens to be against BlackDevilDog."
            "And whether [bree.name]'s right about him cheating or not, it's the fight of my life!"
            "For the longest time I think that he's going to walk away with it."
            "But then I see my chance and I take it."
            show bree happy at right with ease
            show fx exclamation at right
            bree.say "Yay!"
            bree.say "[hero.name], you won!"
            show bree normal
            show kat at left with easeinleft
            kat.say "Colin, you...you lost!"
            "Colin" "No way...I can't lose!"
            "Colin" "Not when I was using that ch..."
            show kat at left, vshake
            kat.say "That what?!?"
            "Colin" "That...that championship winning technique."
            "Colin" "That's what I meant to say!"
            "CandyBarKiller shakes her head in disbelief at BlackDevilDog's excuses."
    show bree normal
    "That leaves [bree.name] to square off against CandyBarKiller in the finals."
    "And a quick glance at the leader board tells me this will be the deciding match."
    mike.say "Ah, [bree.name]..."
    mike.say "I don't want to pile the pressure on."
    mike.say "But..."
    show bree hesitating
    bree.say "I know, I know!"
    bree.say "... Thanks, [hero.name]."
    bree.say "I can make sense of the leader board too, [hero.name]!"
    show bree flirt
    mike.say "Okay, [bree.name]."
    mike.say "You can do this - I believe in you!"
    show bree wink
    "[bree.name] nods and smiles, yet I can hear her trying to control her breathing."
    "I want to say more, but that'd only distract her even more."
    show bree normal at right5 with ease
    "All I can do now is sit back and watch."
    with fade
    "CandyBarKiller's good - and I mean REALLY good."
    "But I must have been way too distracted by the fact [bree.name] likes to play videogames in her panties."
    "Because she takes everything that the other girl has to throw at her."
    "And then [bree.name] fights back like a demon."
    "As surprised as I am by how good [bree.name] is, the effect on her opponent is much greater."
    "Almost immediately I can see a change come over CandyBarKiller."
    "I glance over and see actual beads of sweat standing out on her forehead."
    "She's struggling to keep up with [bree.name]!"
    "For a moment it looks like they're evenly matched."
    "But then [bree.name] seems to switch into some kind of beast mode."
    "And from then on, there's nothing that her opponent can do to keep from having her ass kicked!"
    "When the knockout blow lands, [bree.name] jumps up out of her chair."
    "She throws her arms around my chest, almost squeezing the air out of my lungs."
    play music "music/roa_music/juice.ogg" loop
    show bree happy at center with ease
    show fx exclamation at center
    bree.say "I won...I won...I won!"
    show bree normal
    mike.say "That was amazing, [bree.name]!"
    mike.say "I never knew you could play like that."
    show kat at left
    kat.say "Ah...hey there..."
    kat.say "It's [bree.name], isn't it?"
    mike.say "What do you want now?"
    mike.say "Come to accuse her of cheating, huh?"
    "CandyBarKiller stares at her feet, looking embarrassed."
    kat.say "No..."
    kat.say "I...I just wanted to congratulate her, that's all."
    show bree evil blush
    bree.say "Thanks, CandyBarKiller - that's sweet of you!"
    kat.say "Kat..."
    kat.say "My name's 'Kat'."
    bree.say "Oh..."
    bree.say "Okay - Kat it is then!"
    hide kat with easeoutleft
    show bree happy
    "I watch Kat turn and walk away through the crowd."
    "And I wonder what was really behind her sudden change of heart."
    "Did [bree.name] beat some actual humility into her just now?"
    "Or is there something more subtle going on there?"
    "I shake my head, reminding myself that I need to help [bree.name] celebrate her victory."
    "Whatever Kat's deal might be, it can wait for some other time."
    $ bree.love += 2
    $ bree.flags.breedelay = TemporaryFlag(True, 2)
    hide bree
    return

label bree_event_09:
    if bree.love.max < 140:
        $ bree.love.max = 140
    scene bg livingroom
    "It's always the same - the more you try to play something down, the more obvious it becomes."
    show bree casual at center, zoomAt(1.25, (640, 880)) with dissolve
    "That's why [bree.name]'s been staring at me almost since the moment that she walked into the room."
    "I've tried not making eye contact, even turning my back to her."
    "But I can almost feel it when she finally turns around and asks me the inevitable question."
    show bree hesitating
    bree.say "Erm...[hero.name]?"
    show bree normal
    "Okay, here we go!"
    mike.say "Go ahead, [bree.name]."
    mike.say "Ask the question!"
    show bree stuned
    "[bree.name] looks suitably startled by my response."
    show bree normal
    "But she shakes it off pretty quickly, recovering her focus to as I suggested."
    show bree talkative
    bree.say "Oh...okay..."
    show bree hesitating
    bree.say "Is there something...different about you today?"
    bree.say "It's been bugging me since I walked in."
    bree.say "But I just can't seem to put my finger on it!"
    show bree normal
    "[bree.name] shrugs helplessly to underline the point."
    "She doesn't get an answer at first, just a resigned sigh."
    "And then I force myself to address the proverbial elephant in the room."
    mike.say "Don't worry, [bree.name] - you can be straight with me."
    mike.say "It's my hair, isn't it?"
    show bree stuned
    "[bree.name] blinks in confusion, and then shakes her head."
    show bree surprised
    show fx question
    bree.say "Your hair, [hero.name]?"
    bree.say "What do you mean?"
    show bree stuned
    mike.say "Come on, [bree.name] - I know how it must look!"
    show bree surprised
    show fx question
    bree.say "Huh?!?"
    show bree talkative
    bree.say "It looks the same as always."
    show bree stuned
    mike.say "It doesn't, [bree.name] - it needs cutting."
    mike.say "But when I went to get it done, my barber's was closed!"
    show bree talkative
    bree.say "You go to Seville's, don't you?"
    bree.say "That hipster place where they all have beards and wear flat-caps?"
    show bree normal
    mike.say "That's the one, yeah."
    show bree happy
    "[bree.name] giggles at the thought of the place."
    bree.say "Who knows - maybe there was a moustache emergency and they all got called away!"
    show bree normal
    "I frown at this, and [bree.name]'s face drops visibly."
    show bree evil
    bree.say "I...I'm sorry, [hero.name]."
    show bree happy
    bree.say "What if I cut your hair for you instead?"
    show bree normal
    menu:
        "Why not?":
            $ bree.love += 2
            "Would it really be that much of a disaster to let [bree.name] have a go?"
            "Even if she screws it up, hair has a habit of growing back."
            "And I could always use the money I'd save for something else..."
            mike.say "Okay, [bree.name] - you're on."
            show bree surprised
            bree.say "Really?"
            show bree smile
            bree.say "I...I mean great!"
            show bree normal
            "Before I can change my mind, [bree.name] hustles me into a chair."
            "I find a towel wrapped around my neck."
            "And then I hear the somewhat disconcerting sound of scissors snapping beside my ear."
            hide bree
            scene bree scissorhands
            with fade
            bree.say "Now sit still, [hero.name]."
            bree.say "I used to practice this on my dolls when I was little!"
            mike.say "You used to what?!?"
            show bree scissorhands suspicious
            "But it's too late to back out now, as I hear the first of many snips."
            "What looks like a rather large clump of hair falls into my lap."
            "And I hear [bree.name] sucking her teeth in what sounds like consternation."
            show bree scissorhands waiting
            bree.say "Oooh, darn it!"
            bree.say "Now I'll have to even it out a little..."
            "There's a second snip, and another clump falls into my lap from the opposite direction."
            "And, if anything, this one looks bigger than the last!"
            show bree scissorhands suspicious
            mike.say "Erm...[bree.name]?"
            bree.say "No need to panic, [hero.name]."
            bree.say "I know what I did wrong."
            bree.say "And I can fix it, super quick too!"
            show bree scissorhands waiting
            "What follows is a veritable flurry of snipping and cascading hair."
            "I hardly dare move for fear of ruining the final product."
            "Well, that and losing a piece of my ears too!"
            scene bg livingroom
            show bree casual smile
            show fx question
            bree.say "All done - what do you think?"
            show bree normal
            menu:
                "Love it":
                    "[bree.name] proudly directs me to the nearest mirror."
                    "And once there, she invites me to inspect her handiwork."
                    "I stare at my reflection in the mirror for a couple of seconds."
                    scene bree scissorhands
                    show bree scissorhands suspicious
                    "And then I start to nod my head, beginning to like what I'm seeing."
                    "It's a little different to what I'm used too, a little rougher too."
                    "But I'm sure that, with a little product and styling, I can make it work."
                    mike.say "[bree.name] - it looks pretty good!"
                    scene bg livingroom
                    show bree casual hesitating
                    show fx question
                    bree.say "Really?!?"
                    show bree smile
                    bree.say "You went so quiet just now."
                    show bree happy
                    bree.say "I was worried I'd screwed it up pretty badly!"
                    show bree normal
                    mike.say "Nah, [bree.name] - it's fine."
                    mike.say "Maybe don't give up the day-job."
                    mike.say "But I'd let you do this again in a pinch."
                    show bree flirt
                    "[bree.name] positively beams at the praise."
                    "She waves off the compliments, sure."
                    "But I can see that, underneath the humility, she's pretty proud of herself."
                    $ bree.love += 3
                "What have you done?":
                    "[bree.name] proudly directs me to the nearest mirror."
                    "And once there, she invites me to inspect her handiwork."
                    "I stare at my reflection in the mirror for a couple of seconds."
                    scene bree scissorhands
                    show bree scissorhands suspicious fail
                    "And then I start to shake my head, unable to believe what I'm seeing."
                    "I look like someone that's been held down and sheered like a sheep!"
                    mike.say "[bree.name] - what have you done?!?"
                    scene bg livingroom
                    show bree casual surprised
                    bree.say "Is...is it that bad?"
                    show bree stuned
                    mike.say "Bad?!?"
                    mike.say "I'll have to wear a hat!"
                    mike.say "At least until I can pay someone to fix it..."
                    show bree sad
                    show fx drop
                    bree.say "Oh...I'm sorry, [hero.name]."
                    hide bree with easeoutright
                    "[bree.name] turns and walks away, looking dejected at my reaction."
                    "But what other choice did I have?"
                    "She's made a complete disaster out of my hair!"
                    $ bree.sub += 5
                    $ bree.love -= 5
        "No, no way, never!":
            $ bree.sub += 5
            $ bree.love -= 5
            "It's bad enough that I couldn't get in to my usual barber's shop."
            "But the last thing I want is [bree.name] doing an enthusiastic but amateurish job of it instead!"
            mike.say "No, [bree.name], no."
            mike.say "I couldn't let you do that."
            show bree talkative
            bree.say "It's no trouble, [hero.name], really."
            show bree smile
            bree.say "I used to give all of my dolls haircuts when I was little!"
            show bree normal
            "And she thinks that makes her qualified to be turned loose on my scalp?!?"
            mike.say "I...I have this thing about my hair, you see."
            mike.say "It's really more like a medical condition."
            show bree annoyed
            "[bree.name] cocks her head on one side, narrowing her eyes at this."
            "It doesn't take a genius to tell that she's not convinced."
            mike.say "Honestly, [bree.name] - you need to have graduated from barber's school to be able to handle it!"
            show bree sad
            bree.say "Okay, [hero.name] - if you say so."
            hide bree with easeoutright
            "She turns and walks away, looking more than a little disappointed at being rejected."
            "But I wouldn't let just anyone go at me with a pair of scissors."
            "So what other choice did I have?"
    $ bree.flags.breedelay = TemporaryFlag(True, 1)
    hide bree
    return

label bree_event_10:
    if bree.love.max < 150:
        $ bree.love.max = 150
    scene bg livingroom with fade
    pause 0.1
    show bree at center, zoomAt(1.0, (640, 720)) with easeinright
    "I always feel a little guilty when I'm engrossed in playing on the Zbox and [bree.name] walks into the room."
    "It's crazy, I know - but she's such a hard-core gamer that I can't help thinking that I'm in her spot."
    "We exchange the usual smiles, neither of us actually speaking out of mutual respect as fellow gamers."
    "But the whole time I know that she's watching me play over my shoulder, and it's starting to get awkward."
    "'But, [hero.name],' I hear you ask, 'why would that be awkward?'"
    "Well, the very moment that I pause the game, pretending to take a break, [bree.name] puts it into words."
    show bree smile
    bree.say "You're playing Demons and Demigods, yeah?"
    show bree normal
    mike.say "That's right."
    show bree talkative
    bree.say "[hero.name] - who's the hot babe you were just chatting to, huh?"
    show bree normal
    mike.say "What hot babe, [bree.name]?"
    show bree evil
    bree.say "Oh, come on, [hero.name]."
    show fx anger
    bree.say "If you're gonna play dumb, don't play THAT dumb!"
    show bree normal
    mike.say "You...you mean her?"
    mike.say "That's Thyra - she's a Valkyrie."
    mike.say "I met her on a quest the other week."
    mike.say "You think she's hot?"
    show bree stuned
    "[bree.name] rolls her eyes and chuckles in amusement at my blatant effort to sound incredulous."
    show bree surprised
    bree.say "You're telling me you don't?!?"
    show bree normal
    mike.say "Well, I honestly hadn't noticed."
    mike.say "It's not the first thing you check out when you're slaying monsters, [bree.name]!"
    show bree at center, traveling(1.25, 0.3, (640, 880))
    "[bree.name] shakes her head and leans in a little closer, pointing at the screen."
    "She taps an icon that both my character and Thyra have next to their names."
    show bree talkative
    bree.say "I do happen to play this game too, [hero.name]."
    bree.say "And I know that icon means a couple of PCs are married."
    show bree evil
    bree.say "So should I be jealous of your pixelated spouse?"
    show bree annoyed
    mike.say "It's not like that at all, [bree.name]."
    mike.say "Honestly, it's all about the buffs being married in the game gives you."
    mike.say "You should see how much you get for sleeping in the marital bed too!"
    "I know that last point was a mistake the moment the words leave my mouth."
    show bree vangry
    bree.say "Oh, really?"
    show fx anger
    bree.say "And what goes on in that marital bed, I wonder?"
    show bree angry
    "I can feel myself starting to perspire as [bree.name] needles me ever more."
    "The worst thing is that I can't tell where she's going with this."
    "I know she's enjoying the chance to make me squirm."
    "But there's also a tinge of actual jealousy in her words that makes me wary."
    "I need to do or say something to claw back a little control."
    menu:
        "Let's meet Thyra together":
            $ bree.love += 2
            $ bree.sub += 2
            mike.say "Look, [bree.name] - it's not like that."
            mike.say "Thyra's player seems really cool."
            mike.say "In fact, they asked me to meet up with them out of the game."
            show bree surprised
            show fx question
            bree.say "They did what?!?"
            show bree vangry
            bree.say "And what did you say, huh?"
            show bree angry
            mike.say "I haven't said anything...yet."
            mike.say "But how about we both go and meet them?"
            show bree stuned
            "The suggestion seems to catch [bree.name] totally off-guard."
            "She frowns, and I can see her working it through her brain."
            show bree surprised
            bree.say "But...why would you want me there?"
            show bree annoyed
            mike.say "[bree.name], I don't even know if they're a guy or a girl!"
            mike.say "If you come along we can make it clear that we're together."
            mike.say "That way no one has to come right out and say they're spoken for."
            bree.say "Hmm..."
            show bree talkative
            bree.say "I suppose that does kind of make sense."
            show bree normal
            mike.say "So if I arrange to meet with them, you'll come too?"
            show bree smile
            bree.say "Okay, [hero.name], okay."
            bree.say "But she'd better not be hotter than me in real life!"
            show bree normal
            mike.say "[bree.name], how could anyone be hotter than you?"
            show bree flirt
            bree.say "Ooh, you...you flatterer!"
            $ bree.flags.meetthyra = 1
        "Fine... I won't meet Thyra":
            $ bree.love += 4
            mike.say "Okay, [bree.name] - cards on the table."
            mike.say "Thyra's player just sent me a DM in the game."
            mike.say "They want to meet me for real."
            show bree vangry
            show fx anger
            bree.say "WHAT?!?"
            bree.say "That computer-generated hussy!"
            show bree angry
            mike.say "Whoa, settle down there!"
            mike.say "I'm not going to actually meet them, [bree.name]!"
            show bree surprised
            show fx question
            bree.say "Y...you're not?"
            show bree stuned
            mike.say "That's the point I was trying to make."
            mike.say "I'm cool with being married to a character in an MMORPG."
            mike.say "But I don't want to get it on with them in real life!"
            show bree annoyed blush
            "[bree.name] looks down at the ground, clearly embarrassed at her outburst."
            show bree talkative
            bree.say "Oh...okay."
            show bree annoyed
            mike.say "Look, [bree.name] - if it's really bugging you, I can break it off in the game too."
            show bree talkative
            bree.say "No...no, [hero.name]."
            bree.say "Don't do that."
            bree.say "I was just being silly, that's all."
            bree.say "What am I like - letting myself get jealous of a sprite in a videogame!"
            show bree normal
            "We exchange smiles and I get back to my game."
            "But I can still sense [bree.name] looking over my shoulder the whole time."





















    $ bree.flags.breedelay = TemporaryFlag(True, 3)
    hide bree
    return


label bree_event_11:
    if bree.love.max < 160:
        $ bree.love.max = 160
    if not bree.flags.meetthyra:
        return
    scene bg coffeeshop
    "I know that I passed off the idea of meeting Thyra's player is no big deal to [bree.name]."
    "But I can't help feeling nervous as we arrive at the appointed meeting place."
    "It's almost like, of all the possibilities, I don't know what would be the worst."
    "If the player's a girl and she's hot, then there's the obvious awkwardness that would cause."
    "No way is [bree.name] going to take kindly to someone that's a potential rival."
    "On the other hand the player turns out to a guy, then there's no way that [bree.name] can get jealous."
    "But what if he's some kind of freak gamer - one that's devilishly handsome and charming?"
    "That would mean I'd be the one getting jealous instead!"
    "I'm just starting to wonder if this was all a mistake, [bree.name] starts scanning faces."
    "Looks like she's already scoping out the potential candidates that are already here!"
    show bree casual at center, zoomAt(1.5, (640, 1040)) with dissolve
    bree.say "Hmm..."
    show bree smile
    bree.say "I wouldn't mind if it were him."
    show bree normal
    mike.say "Huh?"
    show bree smile
    bree.say "That guy over there with the laptop - he's cute!"
    show bree flirt
    mike.say "Ah, [bree.name]..."
    mike.say "What happened to this being platonic and, you know...not weird?"
    show bree happy
    bree.say "Oh, come on, [hero.name]."
    show bree smile
    bree.say "It's kind of exciting, don't you think?"
    show bree happy
    bree.say "Like one of those spy movies where people meet up in secret!"
    show bree normal
    mike.say "Whatever you say, [bree.name]."
    mike.say "Anyway, it can't be him."
    show bree sad
    bree.say "Aww, spoilsport - why not?"
    show bree annoyed
    mike.say "Because Thyra's player told me they'd be wearing headphones, and he's not."
    show bree talkative
    bree.say "Well, not right now - but maybe he has some in his bag?"
    show bree normal
    mike.say "Give it up, [bree.name]."
    mike.say "They said they'd have on a t-shirt with a mushroom on it too."
    show bree a
    "[bree.name] crosses her arms over her chest in a defiant gesture."
    "She makes a huffing sound, not ready to give up on her hopes just yet."
    show bree evil
    bree.say "Well, that doesn't sound very mature to me!"
    show bree normal
    mike.say "No, but it does sound like a gamer."
    mike.say "Someone like that girl over there!"
    "[bree.name] and I look over to a girl with violet hair."
    "She's alone and fits the description I've been given almost perfectly."
    show bree surprised
    show fx exclamation
    bree.say "Wait a minute - she looks familiar."
    show bree stuned
    "I nod, thinking that I recognise something about her too."
    "But I just can't put my finger on it..."
    show bree casual at center, traveling(1.25, 0.3, (340, 880))
    show kat casual at center, zoomAt(1.25, (940, 880))
    show fx anger at right
    with easeinright
    kat.say "Urgh..."
    kat.say "Not you two losers again!"
    "Now that her attention is focused on us, I can finally place the girl."
    "She's one of the players we competed against in the gaming contest not long since."
    "And it seems like she's still holding the same grudge from back then too!"
    "It's then that a terrible possibility occurs to me..."
    mike.say "Thyra?"
    mike.say "Is that you?"
    "The girl's face drops visibly."
    show fx question at right
    kat.say "Ax?"
    kat.say "Y...you're Ax?!?"
    "I rub the back of my head with a hand, grinning awkwardly."
    hide fx
    mike.say "Ah...well..."
    mike.say "Small world, huh?"
    show bree surprised
    show fx question at left
    bree.say "What's going on, [hero.name]?"
    bree.say "Oh no - it's not..."
    bree.say "Please tell me she's not the one we're here to meet?!?"
    menu:
        "Leave immediately":
            mike.say "Don't worry, [bree.name]."
            mike.say "We're not staying here a minute longer."
            mike.say "Come on, we're leaving!"
            "The girl with the violet hair shakes her head at this."
            "But she has a wry smile on her face says she's also amused."
            kat.say "Yeah, that's right."
            kat.say "You two just turn tail and run."
            kat.say "I should have figured you'd be cowards in real life!"
            show bree casual vangry
            show fx anger at left
            bree.say "Hey!"
            bree.say "[hero.name] - have you heard what she's saying about us?"
            show bree angry at center, zoomAt(1.25, (300, 880))
            show kat at center, zoomAt(1.25, (980, 880))
            with ease
            "I put myself between the two girls, making sure they're separated."
            mike.say "Don't listen to her, [bree.name]."
            mike.say "She's still bitter that we beat her ass, that's all."
            show fx anger at right
            kat.say "Oh yeah?!?"
            mike.say "The way I see it, she's the loser here."
            mike.say "You and me, we have each other."
            mike.say "She's the one creeping around on an MMORPG, looking for company."
            mike.say "Here in the real world, she's all on her own!"
            show bree smile
            "[bree.name] grins like a cat that got the cream at this."
            show bree normal at center, traveling(1.5, 0.3, (340, 1040))
            "She practically sticks her tongue out as she takes hold of my arm."
            show bree smile
            bree.say "Let's go, [hero.name]."
            bree.say "We can go home and play all kinds of fun games together."
            show bree evil
            bree.say "All she can do is play with herself!"
            show bree normal
            "I can't help laughing at the implications of what [bree.name] just said."
            "So much so that I don't hear the insults the girl yells at our backs as we walk away together."
        "Let's talk for a minute":
            mike.say "Whoa there..."
            mike.say "Let's just back up a minute, okay?"
            hide bree
            hide kat
            show bree kat coffee talk bangry kangry
            with fade
            "[bree.name] and the girl look at me with irritated expressions."
            "But they both shut up like I asked."
            show bree kat coffee talk mangry talkbree
            mike.say "[bree.name], this isn't the gaming tournament."
            mike.say "And if I remember correctly, it was her partner that cheated, not her."
            mike.say "So don't keep on holding it against her."
            "[bree.name] makes a huffing noise, and all but stamps her foot in frustration."
            "She nods though, at least agreeing that I have a point."
            show bree kat coffee talk talkkat
            mike.say "And you..."
            kat.say "Kat..."
            kat.say "My name's Kat!"
            mike.say "Kat, the same thing goes for you too."
            mike.say "This is us starting over, right now."
            mike.say "You liked me well enough in the MMORPG."
            show bree kat coffee talk mnormal
            mike.say "So why is it any different now we've met, huh?"
            "I watch as Kat recreates [bree.name]'s own reaction almost perfectly."
            show bree kat coffee talk knormal
            "But then her face cracks into a smile."
            kat.say "I guess you did kick some serious ass in the tournament, [bree.name]."
            kat.say "More than this guy right here did!"

            show bree kat coffee talk bnormal talkbree
            bree.say "Hee, hee..."
            bree.say "Thanks, Kat - he is kinda like a dead weight sometimes!"
            show bree kat coffee talk mangry
            mike.say "Hey!"
            "Sure, I wanted everyone to put their differences aside and get on."
            "But not for them both to side against me!"
            bree.say "Oh, calm down, [hero.name]."
            bree.say "I was only teasing!"
            kat.say "Is he always this sensitive?"
            bree.say "Most of the time, yeah."
            bree.say "But he has his uses too."
            show bree kat coffee talk bnormal mnormal talkkat
            bree.say "So, Kat - what was this Ax like then?"
            kat.say "Well, I'm not gonna lie, [bree.name]."
            kat.say "I did want to get my hands on his mighty weapon."
            bree.say "It was an impressive chopper then?"
            "Kat nods, and they both look at me a very certain way."
            show bree kat coffee talk mblush bblush kblush talkbree
            "Suddenly I feel like I'm being sized up like a cut of prime steak."
            bree.say "I'll let you into a little secret, Kat."

            bree.say "It's pretty impressive outside of the game too!"
            kat.say "Is that so?"
            show bree kat coffee talk talkkat
            kat.say "You think we could arrange a demo?"
            "I swallow audibly."
            "And I'm already wondering just what the two of them have in mind."
            show bree kat coffee talk bnormal talkbree

            bree.say "Oh, I'm sure we can let you try out the hardware..."
            $ bree.flags.befriendKat = True
    $ bree.flags.breedelay = TemporaryFlag(True, 6)
    if Person.find('kat') and 'fafow' in DLCS:
        $ kat.unhide()
    hide kat
    hide bree
    return

label bree_event_12:
    if bree.love.max < 170:
        $ bree.love.max = 170
    scene bg livingroom
    show bree
    "When [bree.name] told me that her dad was going to be in town for a couple of days, the news gave me some really mixed feelings."
    "On the one hand, I'm really curious to meet one of her parents, as she's never talked about them all that much."
    "In fact, when it comes to [bree.name]'s past, my knowledge pretty much starts from the moment she moved into the house."
    "I think she must know far more about my own history than I do about hers!"
    "But on the other hand, it's always an intimidating thing to meet your girlfriend's father."
    "I mean, you kind of assume that they're going to be suspicious of the guy that's dating their daughter!"
    "[bree.name] stays tight-lipped about just what I can expect from her dad."
    "Almost up to the very moment the guy's supposed to be walking through the door!"
    play sound door_knock
    "It's only when she hears a knock at the front door that she finally breaks her silence."
    show bree talkative
    bree.say "Okay, [hero.name] - he's here."
    show bree at right5 with ease
    bree.say "Just leave most of the talking to me, okay?"
    show bree normal
    mike.say "Erm...okay, [bree.name]."
    mike.say "If you say so!"
    show bree talkative at right with ease
    bree.say "And remember, my Dad's a little old-fashioned."
    bree.say "He's got a pretty quirky sense of humour too."
    hide bree with easeoutright
    "I wonder what the hell that even means."
    "But I fix a smile on my face and nod all the same."
    scene bg house
    show breedad
    with wiperight
    "[bree.name] opens the door to reveal a man well into his middle years."
    "He's stocky, with a face that's stuck in an impatient expression."
    "One of those guys that looks like he enjoys beer and watching football."
    "And probably thinks all men of my generation are pussies by default."
    "I can't see the family resemblance at all."
    "Guess [bree.name]'s mom must be the one she gets her looks from!"
    show bree happy at top_mostleft with easeinleft
    bree.say "Daddy!"
    bree.say "You're here!"
    show bree normal
    "If anything, his frown seems to deepen at this sweet greeting from his daughter."
    show bree at left4 with ease
    "He makes some kind of huffing noise as [bree.name] throws her arms around his neck."
    "It's only now I see that he's actually glaring at me the whole time!"
    show fx anger
    breesdad "Harumph..."
    breesdad "So, this is the dump you're paying good money to live in?"
    show fx anger
    breesdad "They're still fleecing renters in this shit-hole city!"
    show bree at left5 with ease
    "[bree.name] releases her grip on her dad and laughs at what he just said."
    show bree smile
    bree.say "Oh, Daddy - it's a great place, really."
    show bree normal
    breesdad "Whatever, [bree.name]."
    breesdad "It's the low lives that you gotta look out for as well."
    "He's looking right at me again as he says this!"
    show bree at left with ease
    bree.say "Don't worry about that."
    show bree happy
    bree.say "My housemates are the best."
    show fx anger
    breesdad "Harumph..."
    breesdad "Last I heard, you were living with some Satanist chick and a doofus millennial!"
    show fx exclamation at left
    show bree talkative
    bree.say "Sasha's not a Satanist, Daddy!"
    bree.say "She just likes to dress in black and listen to music about the devil, that's all!"
    show bree normal
    "I wait a moment for [bree.name] to refute her dad's damning description of me too."
    "But she simply turns in my direction and waves me over to where they're standing."
    show bree smile
    bree.say "Daddy, this is [hero.name]."
    bree.say "[hero.name], this is my Dad."
    show bree normal
    "Not sure what else to do, I hold out my hand for him to shake."
    "[bree.name]'s dad proceeds to clasp my hand in his own, which is like a catcher's mitt."
    "And then he crushes it with all of his considerable strength."
    "I swear I can feel the bones grinding against each other."
    "But I do my best to grit my teeth and bear it."
    scene bg livingroom
    show bree happy at right5
    show breedad at left5
    with fade
    "What follows is a painful tour of the house and it's various features."
    show bg kitchen with fade
    pause 1
    show bg secondfloor with fade
    pause 1
    show bg bedroom2 with fade
    pause 1
    show bg bathroom with fade
    pause 1
    show bg pool with fade
    "[bree.name] shows off one thing after another, and her dad pisses all over it."
    scene bg livingroom
    show bree evil zorder 2 at right5
    show breedad zorder 1 at left5
    with fade
    "By the time we're done, I can see the sheer effort it's taking her to keep on smiling."
    show bree talkative
    show fx question at right5
    bree.say "Well, Daddy - what do you think?"
    show bree normal
    hide fx
    show fx anger at left5
    breesdad "What do I think?!?"
    breesdad "I think you'd have done better getting knocked up in high-school!"
    show bree stuned
    "The statement hits me pretty hard, but [bree.name] looks like she was just punched in the gut."
    menu:
        "Defend [bree.name]":
            if bree.sub.max < 100:
                $ bree.sub.max = 100
            mike.say "Jesus Christ!"
            mike.say "She's already winning in life just by getting away from you!"
            "[bree.name]'s dad looks at me, his eyes suddenly bulging out of their sockets."
            "He splutters and gasps, as though he can't believe someone would talk to him like that."
            show breedad at left4 with move
            show fx anger at left4
            breesdad "What did you just say, you little shit?!?"
            mike.say "Your daughter's clever, kind and genuine."
            mike.say "Any real man would be proud of her."
            mike.say "But all you've done since you got here is shit on her."
            show fx anger at left4
            breesdad "Why I ought to..."
            "I can see him squaring up to me, spoiling for a fight."
            "I don't want to end up brawling with [bree.name]'s dad in front of her."
            "But I'm not backing down from the belligerent old fart now."
            show bree vangry at right5, vshake
            show fx anger at right5 with hpunch
            bree.say "STOP IT!"
            show bree at right5, vshake
            bree.say "BOTH OF YOU - STOP IT RIGHT NOW!"
            show bree angry
            "The sound of [bree.name]'s raised voice puts an end to the whole thing."
            mike.say "[bree.name], I'm sorry..."
            breesdad "You heard what he said to me..."
            show bree vangry
            bree.say "Oh shut up, Daddy."
            bree.say "[hero.name] was just standing up for me."
            bree.say "And that's something you've never done!"
            show bree annoyed
            show fx drop at left4
            "[bree.name]'s dad makes to say something."
            "Maybe trying to explain himself or make an excuse."
            "But she's on a roll now, and there's no stopping her!"
            show bree talkative
            bree.say "It's pretty funny that you don't like it here."
            bree.say "Because I chose to go to a uni this far from home to get away from that place."
            show bree vangry
            show fx anger at right5
            bree.say "To get away from YOU!"
            show bree angry
            show breedad at center with ease
            breesdad "Princess..."
            show fx drop at center
            breesdad "You don't mean that..."
            show bree vangry
            show fx anger at right5
            bree.say "Don't princess me, you mean old bastard!"
            bree.say "I've had it up to here with you."
            bree.say "Get out, and don't come back until you learn some manners!"
            hide bree
            hide breedad
            with easeoutright
            play sound door_slam
            "And with that, [bree.name] literally shove him out the door, slamming it behind him."
            show bree angry at right with easeinright
            mike.say "Are you okay, [bree.name]?"
            show bree at center with ease
            "She looks up at me, and for a moment I think that I'm next."
            show bree normal
            "But then her face breaks into a smile."
            show bree smile
            bree.say "Actually, [hero.name], I'm feeling better than ever!"
            show bree smile
            bree.say "I should have stood up to him years ago."
            bree.say "You just gave the kick in the pants I needed to actually do it!"
            show bree sadsmile
            "She hugs me tight, squeezing me against her amazing body."
            "And I return the gesture with the same enthusiasm."
            "All the time I'm thinking that her dad must really be some piece of work."
            "Especially if he could treat a girl as wonderful as [bree.name] like trash."
        "Keep quiet":
            bree.say "Ah..."
            bree.say "Ha, ha..."
            show bree happy at right with ease
            bree.say "You're so funny, Daddy!"
            show bree normal
            breesdad "Harumph..."
            breesdad "Yeah, I'm a regular riot."
            "I keep looking at [bree.name] in open shock."
            "Any moment I'm expecting her to shut this guy up."
            "But all she does is smile meekly and let him walk all over her!"
            show breedad at center with ease
            breesdad "Well, if that's all you've got to show me - I'm leaving."
            show bree smile
            bree.say "Okay, Daddy."
            bree.say "Give my love to Mom!"
            show bree normal
            breesdad "Yeah, like I want an excuse to talk to her!"
            hide breedad with easeoutright
            hide fx
            show bree at center with ease
            "And with that, he's gone."
            mike.say "Wow, [bree.name]!"
            mike.say "That's what you call quirky?!?"
            show bree sad
            show fx drop
            bree.say "I know, I know..."
            bree.say "I guess I just thought it might be different this time."
            show bree talkative
            bree.say "You know, with the two of us being here?"
            show bree normal
            "All I can offer is a shrug and a shake of the head."
            mike.say "I thought you just wanted me to meet your dad [bree.name]."
            mike.say "You never said anything picking a fight with him!"
            show bree dazed
            show fx anger
            bree.say "Harumph..."
            "I can see that [bree.name]'s upset with how things went with her dad."
            "But it's not my place to fight her battles for her."
            "Is it?"
    $ bree.flags.breedelay = TemporaryFlag(True, 2)
    hide bree
    return

label bree_event_13:
    if bree.love.max < 180:
        $ bree.love.max = 180
    scene bg livingroom
    "You know how it is when you're sitting up late on the couch, just chilling and watching random crap."
    show watch tv bree with dissolve
    "I'm enjoying the chance to have [bree.name] snuggled up next to me, no pressure on me to do anything but relax."
    "But then I see the time, and I can't help letting out a pretty loud yawn when I realise the lateness of the hour."
    "The sound and the fact it makes my chest heave is enough to shake [bree.name] out of being sleepy and half-awake too."
    "She yawns too, reacting in unconscious sympathy and pushing herself against me as she does so."
    "And sleepy as I am, the sensation is pretty nice!"
    hide watch tv bree
    show bree sad blush at center, zoomAt(1.5, (640, 1140))
    with dissolve
    bree.say "Huh..."
    bree.say "What happened?"
    show bree sleepy
    mike.say "Sorry, [bree.name]."
    mike.say "I just saw the time."
    show bree smile
    bree.say "Oh, is that all?"
    bree.say "I thought I'd been drooling on you in my sleep or something!"
    show bree sleepy
    "I chuckle at the way her sleepiness has made her so honest."
    "Normally she'd never have admitted something like that!"
    mike.say "No..."
    mike.say "It's just that I need to turn in for the night."
    show bree sad
    bree.say "Aww..."
    show bree happy
    bree.say "Can't we just sleep here, on the sofa?"
    show bree sleepy
    "The pleading tone of [bree.name]'s voice is so cute I almost say yes."
    "But in the end, I shake my head and make to get up."
    mike.say "The last time I did that, I had a sore neck for a week!"
    mike.say "No, I want to sleep in my own bed tonight, okay?"
    "[bree.name] grumbles and groans a little more."
    show bree sadsmile at center, traveling(1.0, 0.5, (640, 720))
    "Though she's already hauling herself up from the sofa."
    show bg secondfloor with fade
    "We stumble upstairs, both yawning openly now."
    show bree flirt
    "At the bathroom door, I kiss [bree.name] on the top of the head and slip inside."
    scene bg bathroom with fade
    "A wash and brush of my teeth later, I stagger to my room."
    "But I'm puzzled to see a light coming from under the door."
    "Assuming I must have left the bedside lamp on earlier, I let myself in."
    scene bg bedroom1
    show bree sleep smile at center, zoomAt(1.25, (640, 880))
    with fade
    bree.say "I chose this side of the bed, [hero.name]."
    bree.say "Is that okay?"
    show bree normal
    "I stand still for a moment, trying to make sense of what I'm seeing."
    "[bree.name]'s sitting up in my bed, the covers pulled up to her waist."
    "She's dressed for sleep, and I wonder if I missed something along the way to here."
    mike.say "Ah, [bree.name]..."
    mike.say "I don't know if you misunderstood."
    mike.say "But I'm WAY too tired to fool around with you tonight!"
    show bree happy
    "At this, [bree.name] gives me a sweet smile."
    "She shakes her head and pats the pillow beside her."
    show bree smile
    bree.say "Oh, don't worry about that, [hero.name]."
    bree.say "I'm beat too!"
    bree.say "It was just so nice cuddling up to you on the sofa tonight."
    bree.say "I thought we could keep on snuggling in bed!"
    show bree blush
    bree.say "And if you're all rested in the morning..."
    bree.say "Well, maybe you could wake me up in a fun way?"
    show bree flirt -blush
    menu:
        "Let [bree.name] stay":
            $ bree.love += 3
            "As tired as I am, I can already feel my cock stirring at the thought of sleeping beside her."
            "I know that I'm way too tired to perform tonight, but the morning is a different matter entirely."
            "So what have I got to lose by letting her stay?"
            mike.say "That sounds great, [bree.name]."
            mike.say "But if I oversleep, you have to wake me."
            mike.say "If you know what I mean..."
            show bree blush
            "[bree.name]'s cheeks flush a little and she can't suppress a giggle."
            "But she nods eagerly as I undress and climb into the bed beside her."
            "As soon as I'm under the covers, [bree.name] nestles her back into my belly."
            "She's so warm and soft against me, and she smells so good too."
            "A part of me wonders why in the hell we don't sleep like this every night!"
            bree.say "Mmm..."
            show bree smile
            bree.say "Good night, [hero.name]."
            bree.say "Sweet dreams too!"
            show bree flirt
            mike.say "They will be, so long as you're in them, [bree.name]."
            show cuddle bree dressed with fade
            "[bree.name] giggles again, this time at the corny line I just used on her."
            "And the sound is the last thing that I can recall hearing."
            "Because the next thing I know, I'm drifting off to sleep for real."
            "Soothed by the warmth of [bree.name]'s body, I submit willingly."
            "And the last thing I think of is the promise of that same body in the morning."
            call sleep ("bree dressed") from _call_sleep
        "Ask [bree.name] to leave":
            $ bree.love -= 3
            $ bree.sub += 1
            "God, she looks so hot just lying there!"
            "But I just know that I'm not going to get any sleep if I let her stay."
            "After all, how could I keep my hands off of her?"
            mike.say "Maybe another time, [bree.name]."
            mike.say "I just need to drop straight off tonight, you know?"
            show bree stuned
            "[bree.name] looks a little taken aback by my answer."
            show bree sadsmile
            "But she soon shakes it off and gives me a forced smile."
            show bree at center, traveling(1.0, 0.3, (940, 720))
            "She nods as she hops out of my bed and walks towards the door."
            show bree smile
            bree.say "Sure thing, [hero.name], if that's what you want."
            bree.say "Remember, I'm only a couple of doors away."
            bree.say "Just in case you change your mind..."
            hide bree with easeoutright
            "And with that, she's gone and I'm alone again."
            "The irony is that as soon as I jump into bed, I find that I can't sleep."
            "My mind starts spinning on how I just sent [bree.name] packing like that."
            "Sure, she seemed okay with it on the surface."
            "But what if she was just pretending to be okay for my benefit?"
            "So I lay awake for a long time, worrying about what I've done."
            "And when morning comes around, I feel dead tired."
            "That and like I was a jerk to [bree.name] as well!"
            call sleep from _call_sleep_22
    $ game.room = "bedroom1"
    $ bree.flags.breedelay = TemporaryFlag(True, 2)
    hide bree
    return

label bree_event_14:
    if bree.love.max < 190:
        $ bree.love.max = 190
    scene bg livingroom
    "I can always tell when [bree.name]'s been hitting the books really hard."
    "Cramming for an exam or flogging herself to complete an assignment, the result is just the same."
    "It leaves her frazzled and frustrated in a way that nothing else comes close to."
    "And I usually keep as far away as possible when she's in that state too."
    show bree a annoyed at right with easeinright
    "So when I see her approaching, I make to wrap up what I'm doing and flee the room."
    show bree a normal at right4 with ease
    "But it looks like I've left it a moment too late, as I feel her gaze settle on me."
    show bree talkative
    bree.say "There you are, [hero.name]."
    bree.say "I've been looking for you!"
    show bree normal
    "I stop, dead in my tracks, trying to look like I'm not eager to escape."
    "A feeling made all the more pressing by the fact I can see [bree.name]'s hiding something behind her back."
    mike.say "Ah, yeah, [bree.name] - here I am!"
    mike.say "What can I do for you?"
    "Almost as soon as I say this, I realise the mistake I've made."
    show bree b flirt at center, zoomAt(1.0, (640, 720)) with ease
    "[bree.name]'s expression becomes instantly sweet and solicitous."
    "And I can see that she's using most of her remaining energy to turn on the charm."
    show bree smile blush
    bree.say "Well..."
    bree.say "You know that I've been working on my dissertation for uni?"
    show bree normal
    "How could I not know that?"
    "[bree.name]'s been complaining about the amount of work she's had to put in almost non-stop."
    "In fact, I can't readily recall her talking about anything else for at least the past week!"
    mike.say "Ah, let me think..."
    mike.say "Yeah, [bree.name] - you might have mentioned it in passing, just the once."
    show bree smile
    "[bree.name] smiles at this, letting me know that I've said just the right thing."
    show bree at center, traveling(1.5, 0.3, (640, 1040))
    "She leans in a bit closer, reminding me suddenly of an angler reeling in their catch."
    show bree talkative
    bree.say "The thing is, [hero.name], it's REALLY been a grind."
    bree.say "But I'm almost, nearly, just about there."
    bree.say "One more push and I think it'll be done."
    show bree normal
    "I have the feeling that there's something she's not saying."
    "And it's hanging over the conversation like a piano dangling over my head right now."
    mike.say "That's great news, [bree.name]."
    mike.say "I remember how hard my dissertation was."
    mike.say "I was so tired when I finished it, I must have slept for a week!"
    show bree happy
    "[bree.name]'s smile becomes wider still, and she cocks her head on one side."
    "Now I feel like the fish on the end of a hook, about to be yanked out of the water!"
    show bree talkative
    bree.say "That's what I wanted to ask, [hero.name]."
    bree.say "You've done one of these before."
    bree.say "So could you maybe...check it over for me?"
    show bree normal
    "I blink in surprise, as I'd been expecting something much more onerous than that."
    "Checking over [bree.name]'s dissertation shouldn't take me more than an hour or so at the most."
    mike.say "Of course, [bree.name]."
    mike.say "I'd be happy to look through it and let you know what I think."
    show bree happy -blush
    show fx question
    bree.say "Oh, would you, [hero.name]?"
    bree.say "That's SO great of you."
    show bree normal
    "She pulls a thick folder out from behind her back and shoves it into my hands."
    "Unprepared for this, I almost drop the whole thing as I struggle to keep a hold of it."
    mike.say "Ah, [bree.name]..."
    mike.say "Couldn't you just send me the file in an email or something?"
    mike.say "There must be all of your notes and research in here!"
    show bree annoyed blush
    "Only now does [bree.name]'s expression become even the slightest bit guilty."
    "She looks away for a moment, as if too embarrassed to look me in the eye."
    show bree evil
    bree.say "Erm, well...that's the thing."
    bree.say "There's no draft yet, just the notes."
    bree.say "But it's all there, I swear it is."
    bree.say "It just needs...organising, that's all!"
    show bree normal
    "I shake my head, weighing up the considerable wedge of paper in my hands."
    mike.say "[bree.name], I thought you said you wanted me to check it over?"
    mike.say "This sounds more like you want me to write the entire thing for you!"
    "Now it's [bree.name]'s turn to shake her head."
    show bree talkative
    bree.say "No, no, no..."
    bree.say "I just want your advice on what should go where, [hero.name]."
    bree.say "You know - what I should say, what I shouldn't say and why."
    bree.say "I can do the rest, I promise!"
    show bree normal
    "I think about the implications of what [bree.name]'s asking me to do, trying to weigh-up the right and wrong of it."
    "My gut tells me that I should just say no, leave her to do the work on her own."
    "But this is [bree.name], a girl I have feelings for and want to see do well in whatever she sets her mind to."
    "So what's it to be?"
    "My conscience, or my affection for [bree.name]?"
    menu:
        "I'll help you" if hero.knowledge >= 70:
            $ bree.love += 2
            "Feeling the weight of the folder in my hands again, a thought occurs to me."
            "There's a hell of a lot of work that must have gone into this thing already."
            "Which also means [bree.name]'s probably used up all of her energy doing the research."
            "So she's not going to be at her best when she sits down to write it all up either."
            "All I'd really be doing is some editing and arranging while she rests up for the final push."
            mike.say "Okay, [bree.name]."
            mike.say "You look like you've earned a rest."
            mike.say "Go have a lie down and I'll get started on this, okay?"
            show bree happy
            "[bree.name] positively beams at my answer."
            show bree sleepy blush at center, traveling(2.0, 0.3, (640, 1340))
            "She leans in to kiss me on the cheek too!"
            show bree smile at center, traveling(1.5, 0.2, (640, 1040))
            bree.say "Thanks, [hero.name] - you're the best!"
            show bree normal
            mike.say "It's nothing, [bree.name]."
            mike.say "Just do me a favour, okay?"
            show bree talkative
            show fx question
            bree.say "What's that?"
            show bree normal
            mike.say "Brew some strong coffee."
            mike.say "Because I feel like I'm going to be pulling an all-nighter for this one!"
            $ game.pass_time(6)
        "You have to do it alone":
            $ bree.love -= 2
            "No, I can't do it."
            "If [bree.name] can't do this on her own, then she hasn't earned the qualification at the end of it all."
            mike.say "No, [bree.name]."
            mike.say "I'll read it once you've written it, I promise."
            mike.say "But it's really got to be your work, you know?"
            show bree gloomy -blush
            "[bree.name]'s face falls as soon as I say this."
            "She takes hold of the folder when I hand it back."
            "But I can see that she's a little crushed by my answer."
            show bree sad
            bree.say "Okay, [hero.name], okay."
            bree.say "I guess you're right."
            show bree gloomy
            "She lets out a weary sigh and turns to leave."
            show bree sad at center, traveling(1.25, 0.3, (740, 880))
            bree.say "I shouldn't get lazy, not this close to finishing my course."
            show bree talkative
            bree.say "Just do me a favour and brew some strong coffee, okay?"
            bree.say "I think I'm gonna be pulling an all-nighter on this one!"
    $ bree.flags.breedelay = TemporaryFlag(True, 1)
    hide bree with fade
    return

label bree_event_15:
    if bree.love.max < 200:
        $ bree.love.max = 200
    scene bg livingroom
    show bree annoyed at center, zoomAt(1.25, (940, 880)) with easeinright
    "[bree.name] walks into the room carrying a battered cardboard box, one that's vaguely familiar to me."
    show bree at center, zoomAt(1.25, (640, 880)) with ease
    pause 0.3
    show bree at center, zoomAt(1.25, (640, 1000)) with ease
    "And as she sits down and starts to rummage through it, I suddenly recall where I've seen it before."
    "It's one of the boxes that [bree.name] stashed in the attic when she first moved in here."
    "I read the words 'School Stuff' scrawled on the side in marker pen."
    "And that kind of give away the nature of the contents!"
    "I know that I have a box just like that sitting back home too."
    "But then I think about it, and realise that I know almost nothing about [bree.name]'s life before she lived here."
    show bree at center, traveling(1.35, 0.3, (640, 1040))
    "Curious as to just what revelations might be waiting inside the box, I lean over her shoulder."
    mike.say "Hey, [bree.name]."
    mike.say "What have you got there?"
    "At the sound of my voice in her ear, [bree.name] almost jumps out of her skin."
    show bree surprised at center, zoomAt(1, (640, 1040)), vshake
    bree.say "Oh, [hero.name]!"
    show fx question
    bree.say "What...this?"
    show bree talkative
    bree.say "Nothing really, just some old junk from school."
    bree.say "I decided it was time I went through it all, you know?"
    bree.say "Decided what was worth keeping and what I should dump in the trash!"
    show bree normal
    "I nod, understanding where she's coming from."
    mike.say "It's tough though, isn't it?"
    mike.say "Not just to decide what to keep, I mean."
    mike.say "Looking through old stuff can stir up bad memories."
    show bree happy
    "[bree.name] smiles and shakes her head, as though I said something silly."
    show bree smile
    bree.say "What are you talking about, [hero.name]?"
    bree.say "Being at school was the best time of my life!"
    bree.say "I sometimes wish that I could go back there, even now."
    show bree normal
    "Wow - that is not a sentiment that I can identify with at all."
    "[bree.name] must have had a very different experience of high-school to me!"
    "It's then that I notice a book with a glossy cover in the box."
    "It has a date on the front and the name of the school [bree.name] must have attended."
    mike.say "Your school actually had year-books?!?"
    mike.say "I thought they were just something in Hollywood movies!"
    "Without thinking too much of it, I reach out to grab the book from the box."
    play sound woosh_punch
    show bree surprised at center, traveling(1.75, 0.2, (640, 1200))
    pause 0.1
    show bree surprised at center, traveling(1.35, 0.2, (640, 1040))
    "But [bree.name] surprises me by leaping forward and snatching it away."
    bree.say "NO!"
    bree.say "Don't..."
    show bree stuned blush
    mike.say "Whoa, [bree.name]!"
    mike.say "What's the matter?!?"
    "I see that [bree.name]'s cheeks have turned red."
    "Which means she's fully aware of just how crazy her outburst was."
    "But she's clutching the year-book to her chest all the same."
    show bree talkative
    bree.say "I...I'm just..."
    bree.say "Protective of this book...okay?"
    bree.say "It's the only copy of the picture..."
    bree.say "I mean book...the only copy of the book I have!"
    show bree sadsmile
    "I fix [bree.name] with a stare, one that says I want an answer."
    "At first she tries her hardest to play dumb."
    "But then she lets out a frustrated sigh and seems to give it up."
    show bree evil
    bree.say "Okay, okay..."
    bree.say "I'm not fond of my picture in here."
    bree.say "I got rid of all the other ones from the same time."
    bree.say "But I couldn't get rid of the year-book, as it has too many memories for me."
    show bree annoyed
    mike.say "[bree.name], you HAVE to let me see it now."
    mike.say "If you don't, I'll end up stealing it to sneak a look!"
    show bree talkative
    bree.say "Fine, [hero.name], I'll let you see."
    show bree vangry
    bree.say "But you have to promise not to be unkind, okay?"
    show bree annoyed
    mike.say "Okay, [bree.name] - I promise."
    show bree normal
    "But as she opens up the pages of the year-book, I don't know what to expect."
    "I just hope that I can keep my promise!"
    show bree smile
    bree.say "There..."
    show bree normal
    "I look down to where she's pointing, and I have to shake my head to believe my eyes."
    "The girl in the picture is unmistakably [bree.name]."
    "But she's also chubby, more than a little spotty and sporting a brace on her teeth."
    show bree sad
    bree.say "You see?"
    show bree gloomy
    "[bree.name] wails as she stabs the page with her finger."
    show bree sad
    bree.say "I was a fat, ugly geek!"
    show bree gloomy
    menu:
        "No, you weren't":
            $ bree.love += 3
            mike.say "You're being WAY too hard on yourself, [bree.name]!"
            show bree surprised
            show fx question
            bree.say "R...really?"
            show bree stuned
            mike.say "Sure you are."
            mike.say "No one's finished growing at that age."
            mike.say "There's too much going on to know who you are too."
            show bree hesitating
            bree.say "Now I think about it, things were pretty crazy back then."
            show bree normal
            "I nod and smile, trying to reassure [bree.name] as best I can."
            mike.say "I'll grab some pictures of myself next time I visit home."
            mike.say "You should see some of the phases I went through as a teenager!"
            show bree happy at startle
            "[bree.name] can't help giggling at the thought of this."
            show bree smile
            bree.say "You mean you weren't always this handsome and manly?"
            show bree normal
            "She elbows me playfully in the ribs."
            "And I'm pleased to see that she's already cheering up."
            mike.say "Seriously though, [bree.name] - you were a cute kid."
            mike.say "And you kept something from that photo too."
            show bree surprised
            show fx question
            bree.say "Oh no, what's that?"
            show bree stuned
            mike.say "Your smile, [bree.name]."
            mike.say "It's still as lovely now as it was back then."
            show bree smile
            bree.say "Aww..."
            bree.say "That's kind of cheesy, [hero.name]!"
            bree.say "But I like it!"
            show bree flirt
            "[bree.name] plants a kiss on my lips, and then we thumb through the year-book together."
            "She opens up, telling me one story after another about her past."
            "But all I can think about is the promise of our future together."
        "Fat and ugly, indeed":
            $ bree.love -= 3
            $ bree.sub += 1
            mike.say "Wow, [bree.name]."
            mike.say "How did you get through customs with all that metal in your mouth?!?"
            show bree vangry
            bree.say "Hey, that's pretty mean!"
            show bree angry
            mike.say "Yeah, but it's not the whole of it, either."
            mike.say "I mean, I've heard of puppy fat."
            mike.say "But that must have been an entire litter right there!"
            play sound punch_hard
            pause 0.1
            with hpunch
            "[bree.name] makes a huffing noise as she slams the year-book closed."
            "She does this so fast that I only just manage to keep from losing a finger!"
            show bree vangry
            show fx anger at center, zoomAt(1.35, (640, 1040))
            bree.say "You promised you wouldn't be mean."
            bree.say "But if you're going to keep on making jokes, then I'm leaving!"
            show bree at center, zoomAt(1.35, (640, 920)) with ease
            pause 0.1
            hide bree with easeoutright
            "With that, she shoves the year-book back into the box and storms out."
            "Even after she's gone, I still can't help chuckling at the mental image of the photo."
    $ bree.flags.breedelay = TemporaryFlag(True, 1)
    hide bree with fade
    return

label bree_event_16:
    scene bg livingroom
    show bree gloomy at center, zoomAt (1.25, (640, 880))
    with fade
    "The emotions in the room are so powerful that you could almost reach out and touch them."
    "The feeling of loss and grief so thick in the air that you could cut them with a knife!"
    "[bree.name] and I are both feeling the exact same way right now, struggling to contain our feelings."
    "But I've taken it upon myself to be the strong one on this occasion."
    "And so I force the words to come out of my mouth."
    "The words that neither of us ever wanted to hear spoken in this house."
    mike.say "We have to face it, [bree.name]."
    mike.say "He's just come to the natural end of his life, that's all."
    show bree cry
    bree.say "Oh, [hero.name], it can't be true, it just can't!"
    bree.say "What about all the good times we had together?"
    bree.say "What about all the memories?"
    show bree gloomy
    "I shake my head, trying as best I can to comfort her."
    mike.say "I remember all of those good times too, [bree.name]."
    mike.say "But we knew from the moment that we brought him home this day would come."
    mike.say "There's just no way round it."
    show bree cry
    bree.say "No, [hero.name], don't say it!"
    show bree gloomy
    mike.say "We have to face reality [bree.name]."
    mike.say "The Zbox is screwed."
    mike.say "It's time to buy a new games console!"
    "[bree.name] wrings her hands for a moment, and I honestly think she might start to cry."
    show bree stuned
    "But then her eyes widen and her face lights up with what can only be delight."
    show bree surprised
    bree.say "Ooh, I just remembered something."
    show bree happy
    show fx exclamation
    bree.say "The Zbox Zero is on sale at the mall!"
    show bree normal
    "I nod at this, as I was thinking the exact same thing."
    mike.say "Well, what are we waiting for?"
    mike.say "Let's go grab one!"
    show bree talkative
    bree.say "Wait a minute, [hero.name]."
    bree.say "Even at the sale price, it's still really expensive!"
    show bree annoyed
    "I blink at this, not really understanding why that would be a problem."
    "I have more than enough disposable income at the moment to cover it."
    "Is she actually thinking that I was expecting her to buy the console herself?"
    mike.say "Don't worry, [bree.name]."
    mike.say "I have enough in the bank to cover it."
    mike.say "I can even raid my savings if I have to!"
    show bree blank
    "[bree.name] looks at me a little awkwardly."
    show bree talkative
    bree.say "I wasn't trying to get you to pay for it, [hero.name]."
    bree.say "I was thinking that we could go halves, you know?"
    bree.say "Since we both use the console a lot and, well..."
    bree.say "We have been getting closer these past few months."
    show bree b smile blush
    bree.say "It'd be like the first serious thing we've bought as a couple..."
    show bree flirt -blush
    menu:
        "Agree to split in half":
            $ bree.love += 3
            mike.say "Hmm..."
            mike.say "I suppose you're right, [bree.name]."
            mike.say "We are the ones that used the old Zbox the most around here."
            mike.say "And it would be kind of cool to know it belonged to the both of us too!"
            show bree happy
            "[bree.name] clasps her hands under her chin, smiling at me in obvious delight."
            show bree smile
            bree.say "So that's settled then?"
            bree.say "We're going to go halves on it?"
            show bree normal
            mike.say "Okay, [bree.name] - let's do it!"
            "I know this is going to sound crazy."
            "And we're only wrangling on the specifics of buying a games console."
            "But this still feels like an important step forward in terms of our relationship."
            "It's kind of the first major financial decision [bree.name] and I have made together."
            "As well as being the first investment that we've made as a couple too."
            mike.say "So, shall we go hit the mall?"
            show bree smile
            bree.say "Sure thing, [hero.name]."
            bree.say "And if we hurry, we might still get one of those limited edition models."
            show bree happy
            show fx exclamation
            bree.say "You know - the ones that are PINK!"
            hide bree with easeoutright
            "My jaw drops as [bree.name] hurries off, expecting me to follow."
            "Is she serious?"
            "What have I let myself in for?!?"
        "Buy it alone":
            $ bree.love -= 3
            $ bree.sub += 1
            mike.say "Hmm..."
            mike.say "I hear what you're saying, [bree.name]."
            mike.say "But this isn't like going halves on a meal."
            mike.say "I feel like I'd want to own something like a Zbox Zero outright."
            show bree annoyed
            "[bree.name] looks more than a little annoyed at my reasoning."
            show bree a
            "She crosses her arms over her chest and gives me a huffy look."
            show bree talkative
            bree.say "I don't get it, [hero.name]."
            bree.say "We shared the old Zbox the whole time we had it!"
            bree.say "What's wrong with us buying something together?"
            show bree angry
            "All I can do is shrug at this and shake my head."
            mike.say "I'm sorry, [bree.name]."
            mike.say "I just don't think I'm ready for that kind of commitment just yet!"
            hide bree with easeoutright
            "[bree.name] turns her back on me, evidently sulking at being rejected."
            "And I can already sense that she's going to make me pay for this one!"
    $ bree.flags.breedelay = TemporaryFlag(True, 1)
    with fade
    return

label bree_event_17:
    scene bree zbox games
    show bree zbox games nobree
    with fade
    "I'm in the zone today, totally killing it on the Zbox and on course to beat my own high-score!"
    "The real world seems to have faded away to almost nothing."
    "And all I can think about is playing the game to the bitter end!"
    bree.say "Urgh..."
    bree.say "[hero.name]!"
    bree.say "How can you STILL be on the Zbox?!?"
    "[bree.name]'s voice is pitched at that perfect level, the one that cuts through everything else."
    "Which means that it instantly snaps me back to reality."
    "Or in my case, more specifically the living room of the house."
    "I pause the game and look up, my eyes still swimming from the change of perspective."
    scene bg livingroom
    show bree a angry
    with fade
    mike.say "Huh?!?"
    mike.say "What's the matter, [bree.name]?"
    mike.say "Did I forget to schedule in a toilet break again?"
    "[bree.name]'s standing over me, hands balled into fists and planted on her hips."
    "And from the look on her face, I know that I'm in serious trouble right now!"
    show bree a vangry
    bree.say "Oooh!"
    bree.say "You're such a selfish pig sometimes, [hero.name]!"
    bree.say "Do you know how long I've been waiting to do something with you?"
    show bree a angry
    mike.say "Erm...no, [bree.name]!"
    mike.say "I've been playing on here most of the day."
    mike.say "So I don't even know what time it is!"
    show bree a stuned
    "[bree.name]'s eyes go wide at this."
    "And she actually stamps her foot!"
    show bree a vangry at center, vshake
    bree.say "Well it's time to stop - NOW!"
    bree.say "Turn that damn thing off and pay me some attention!"
    show bree a vangry blush
    bree.say "I'm MEGA horny, [hero.name]!"
    show bree a angry
    mike.say "I can't, [bree.name]."
    mike.say "I'm on a roll here!"
    "[bree.name] makes a harrumphing sound and shakes her head."
    show bree a vangry
    bree.say "Well I'm not taking no for an answer!"
    bree.say "Everyone else is out of the house right now."
    bree.say "So you can damn well multi-task!"
    show bree underwear angry at center, hshake with dissolve
    "With that, [bree.name] boldly pulls down her panties."
    show bree naked at center, hshake with dissolve
    "And then she starts trying to climb onto my lap!"
    show bree naked at center, zoomAt(1.5, (640, 1040)) with hpunch
    "She's really serious about this."
    hide bree
    show bree zbox games nakedbree with hpunch
    "She's going to try to ride me while I play on the Zbox!"
    menu:
        "It might be challenging" if hero.stamina:
            "I make a few grunting sounds as [bree.name] scrambles into my lap."
            "And I'm also sure to make them sound louder than the strictly need to be."
            "But I don't actually try and stop [bree.name] form getting her way."
            "After all, if she can pull this off, what's not to like?"
            "I get to have her fuck me while I keep on playing video games!"
            "[bree.name] puffs and pants as she tries to get herself into position."
            "She already has my flies open and my cock out of my pants."
            "And I'm starting to get hard just from watching her efforts."
            "In the end, she wraps her legs around my waist."
            "[bree.name] then leans herself forwards until her chin's on the floor."
            show bree zbox games nakedbree nakedmike
            bree.say "I just have to..."
            bree.say "Wriggle a little this way..."
            bree.say "And squirm a little that way..."
            bree.say "Oh...oh yeah...that's it!"
            "The sensation of [bree.name] doing all this is pretty amazing."
            "I can feel just how wet her pussy is the moment she's on top of me."
            "She wasn't joking when she said she was crazily horny!"
            "Her lips slide over my cock a couple of time."
            "Then she gets the angle just right."
            "And I feel myself slip straight into her."
            "Seriously, there's almost no resistance."
            "[bree.name] sinks straight down onto my cock."
            "And she doesn't stop until it's as deep inside of her as it can go."
            bree.say "Oooh..."
            show bree zbox pleasure
            bree.say "Oh yeah..."
            bree.say "I've got it..."
            bree.say "I've got your joystick inside me!"
            "I lean forwards, planting my hands on [bree.name]'s ass."
            "My joypad fits right on top of it."
            "Like...like it's a pair of soft, pink cushions!"
            mike.say "Here we go..."
            mike.say "This is the good part!"
            "Leaning forwards thrusts my cock harder and deeper into [bree.name]."
            "And she moans, nodding with enthusiasm as she thinks I'm getting into it."
            "The truth is that I'm loving the sensation of being buried inside her."
            "But I'm actually getting an adrenaline rush from the game at the same time."
            bree.say "That's it..."
            bree.say "That's what I want..."
            bree.say "Please...fuck me like that!"
            "I lean forwards even further, my hands now on [bree.name]'s lower back."
            "The joypad's pressed against her buttocks as I pull her closer."
            "She feels really good around my cock."
            "Pretty soon I can't tell which is spurring me on more."
            "The excitement of the game or [bree.name] riding me as I play it!"
            bree.say "Oh fuck..."
            bree.say "I'm gonna cum!"
            "[bree.name]'s as good as her word."
            "A moment after she says the words, it happens."
            "Her orgasm makes her muscles squeeze at my cock."
            "And her entire body twitches before me."
            "It doesn't take long for her to put me over the top either."
            show bree zbox ahegao with vpunch
            "I shoot my load into [bree.name] just as I pull the joypad backwards."
            with vpunch
            "This means that she gets everything I have to give as deep as I can go."
            with vpunch
            "And once I'm done, she practically slithers onto the floor at my feet."
            bree.say "Oh wow..."
            bree.say "I think..."
            bree.say "I think you just got a new high score!"
            $ bree.love += 2
        "I need to end my level":
            "What in the hell does [bree.name] think she's doing?!?"
            "I never jumped on her like this when she was playing on the Zbox!"
            "I'm not some household appliance she can got off on whenever she wants!"
            mike.say "What the hell, [bree.name]!"
            mike.say "Get off me!"
            bree.say "No way, [hero.name]!"
            bree.say "I'm horny, I already told you that!"
            bree.say "You've gotta help me out!"
            with hpunch
            "We struggle for a while, and I suppose it must look pretty comical."
            "[bree.name] trying to straddle me while I'm twisting to push her off."
            "But eventually, [bree.name] overbalances and tumbles off me altogether."
            "She lands on her ass with a squeal of pain."
            with vpunch
            scene bg livingroom
            show bree lose naked at center, zoomAt(1.5, (640, 1140)), vshake
            bree.say "Ow!"
            bree.say "Ow, ow, ow!"
            show bree vangry
            bree.say "Nice going, [hero.name] - now you've hurt my butt!"
            hide bree
            show bree naked angry at center, vshake
            "[bree.name] gets to her feet and storms out of the room."
            hide bree with easeoutright
            "I watch her go in silence, waiting until I'm sure she's out of earshot."
            "Then I unpause the game and start playing again."
            "I'm sure [bree.name] will calm down soon, then she'll be fine."
            "Maybe she'll use a vibrator or something?"
            "Anyway, who cares?"
            "I've got a personal best to beat..."
            $ bree.sub += 1
            $ hero.cancel_event()
    $ bree.flags.breedelay = TemporaryFlag(True, 2)
    with fade
    return

label bree_event_18:
    scene bg livingroom
    "I've finally managed to snag some time on the Zbox, and I'm going to make the most of it."
    "I got to the console before [bree.name] could claim it for herself this time, which is pretty rare."
    "And it looks like everyone else is out of the house too, so I shouldn't have any interruptions."
    scene bree zbox games
    show bree zbox games nobree
    with fade
    "Just me, the Zbox and some good, old-fashioned gaming fun!"
    bree.say "Oh, [hero.name]..."
    bree.say "I see you're playing on the Zbox again!"
    "At the sound of [bree.name]'s voice, I pause the game and look up."
    "Her head is peeking around the side of the door."
    "And I can see she has a mischievous look on her face too."
    mike.say "What the hell?"
    mike.say "I thought you went out, [bree.name]?"
    "[bree.name] shakes her head at this."
    bree.say "Oh no."
    bree.say "Everybody else did - but not me!"
    mike.say "Well you'd better tell me what you want, [bree.name]."
    mike.say "And before you even ask, you're not getting me off the Zbox!"
    "[bree.name] chuckles and shakes her head again."
    bree.say "No way, [hero.name]."
    bree.say "I don't want to stop you playing."
    bree.say "I want to help you, like last time..."
    "With that, [bree.name] walks around the door and into the living room."
    scene bg livingroom with fade
    show bree naked normal at right with easeinright
    "My eyes go wide the instant she does so, as she's totally naked!"
    mike.say "B...[bree.name]..."
    mike.say "What happened to your clothes?!?"
    show bree smile
    bree.say "Oh, I took those off so I'd be ready."
    show bree blush at center with ease
    bree.say "So what do you say?"
    bree.say "Wanna fuck me while you play?"
    bree.say "Just think of me as the ultimate gaming peripheral!"
    show bree flirt -blush
    menu:
        "Let's try this new peripheral" if hero.stamina:
            $ peripheral = randint(0, 2)
            if peripheral == 0:
                "I did have some specific goals in mind for my gaming session tonight."
                "There were things I wanted to achieve, goals I wanted to reach."
                "But are those things really worth passing up a chance like this?"
                "I certainly don't think so!"
                mike.say "Okay, [bree.name]..."
                mike.say "Hop on!"
            elif peripheral == 1:
                "The last time [bree.name] offered to do this for me it was great."
                "Sure, I might not have performed as well as usual."
                "Playing the game, I mean!"
                "But I'd love to do it all over again."
                mike.say "Jump right on, [bree.name]!"
                mike.say "Let me take you for a ride you'll never forget!"
            else:
                "Of course I want [bree.name] to ride my cock while I play videogames."
                "What kind of a fool would I have to be to say no to that?"
                "So I pat my lap and smile up at [bree.name]."
                mike.say "Okay, [bree.name]..."
                mike.say "Plug yourself in and let's play!"
        "I need to focus":
            "Wow...what an offer!"
            "But I really need to be at the top of my game right now."
            "There's so much progress I need to make if I want to progress."
            "And having [bree.name] bouncing up and down on my cock won't help."
            mike.say "Sorry, [bree.name]..."
            mike.say "I'm going to have to say no this time."
            show bree naked vangry at hshake
            bree.say "WHAT?!?"
            bree.say "Are you actually serious?"
            bree.say "I'm offering to let you fuck me while you play videogames!"
            bree.say "You're literally never going to get a better offer than that!"
            show bree angry
            "I smile and shrug helplessly."
            mike.say "Maybe another time, [bree.name]?"
            mike.say "But not now."
            show bree annoyed at right with ease
            "[bree.name] lets out a snort of frustration and storms out of the room."
            hide bree with easeoutright
            "A gesture that might have been a little more impressive had she not been naked."
            "All I can do is shake my head and get back to my game."
            "Because now I really do need to make this an epic gaming session."
            "Otherwise I just turned her down for nothing like a chump!"
            $ bree.sub += 1
            $ hero.cancel_event()
            $ bree.flags.breedelay = TemporaryFlag(True, 2)
            with fade
            return
    scene bree zbox games
    show bree zbox games nakedbree nakedmike
    with fade
    "[bree.name] claps her hands together with glee as she hurries over."
    "I move my arms to the sides as she clambers into my lap."
    "And then I lean back, not moving while she pulls out my cock."
    "[bree.name] strokes it up and down, looking over her shoulder at me the whole time."
    if peripheral == 0:
        bree.say "Mmm..."
        bree.say "I know just which port this plugs into!"
    elif peripheral == 1:
        bree.say "Oh my..."
        bree.say "I hope I have enough memory free!"
        bree.say "Need to be ready for when this RAMs into me!"
    else:
        bree.say "Now let's see..."
        bree.say "I wonder if I need an adaptor for this thing!"
    "[bree.name] begins to rub the head of my cock against her pussy."
    "She must have been more than ready for this."
    "Because she's already nice and wet down there."
    "But that's no problem for me, because she's got me hard in record time!"
    "[bree.name] moans as she pushes herself downwards, legs wrapping around my waist."
    "There's a moment of resistance, her pussy putting up a token fight."
    "And then it surrenders, letting her sink down onto my cock."
    "[bree.name] keeps on going, lowering herself until her chin is on the floor."
    "At the same time, I'm going as deep inside of her as possible."
    if peripheral == 0:
        bree.say "Your [bree.name] is now fully installed!"
        bree.say "Please use her as you will!"
    elif peripheral == 1:
        bree.say "That's all the way inside of me, [hero.name]!"
        bree.say "Now you'd better let me have it!"
    else:
        bree.say "Ooh..."
        bree.say "Looks like we're compatible formats!"
        bree.say "Let's exchange data, [hero.name]!"
    "I can't help chuckling at [bree.name]'s cheesy puns."
    "But I suppose that I should be grateful she's getting into the spirit of things."
    "I start to move my hips at the same time as I unpause the game."
    "And at first it's hard to keep that up and play at the same time."
    "I keep paying too much attention to one thing and ignoring the other."
    "If I focus on the game, I hear [bree.name] pouting."
    "But if I turn my attention to her, I begin to do badly in the game."
    "Suddenly I realise what the problem is - I'm overthinking everything."
    "Of course I can't play the game like a pro and fuck [bree.name] at the same time."
    "What I need to do is step back and see everything as a whole."
    "Taking a deep breath, I try to let go of my concerns."
    "I begin to play in a more laid-back manner."
    "And at the same time I settle into a gentle rhythm while fucking [bree.name] too."
    "After that, it all just seems to fall into place."
    "I feel like a mystic meditating on matters spiritual."
    "Or at least a guy having great sex while playing the game of his life!"
    "I feel confident enough to pick up speed now."
    "I lean forwards, using [bree.name]'s pert ass like a cushion."
    "My joypad is pressing down on her from above."
    "Just like my cock is thrusting into her from below."
    if peripheral == 0:
        bree.say "Oh..."
        bree.say "Oh wow..."
        bree.say "Whatever your doing..."
        bree.say "Keep doing it!"
    elif peripheral == 1:
        bree.say "Wow..."
        bree.say "Don't know which you're playing better..."
        bree.say "The game..."
        bree.say "Or me!"
    else:
        bree.say "You're gonna beat your high-score..."
        bree.say "And I'm gonna get high off of it when you do!"
    show bree zbox games pleasure
    "Things are really starting to get intense now."
    "I'm thrusting back and forth into [bree.name]."
    "And the action on the screen's getting crazy too."
    "I lean forward even further, my hands around the small of [bree.name]'s back."
    "I have a firm grip on the joypad, which presses her against me harder still."
    "There's a sound in the air that I can't place at first."
    "But then I realise it's the noises that we're both making."
    "[bree.name] and I are grunting and moaning like crazy right now!"
    "I'm about to beat an elusive challenge in the game."
    "And it just so happens that I'm about to shoot my load too!"
    "Not to be outdone, [bree.name] has news of her own to share..."
    if bree.sexperience % 3 == 0:
        if peripheral == 0:
            bree.say "Oh fuck..."
            bree.say "Oh fuck..."
            bree.say "I'm gonna cum!"
        elif peripheral == 0:
            bree.say "Here it comes, [hero.name]!"
            bree.say "You'd better be ready for it!"
        else:
            bree.say "I can't..."
            bree.say "I can't hold on any longer..."
            bree.say "I'm losing it!"
    else:
        bree.say "Oh, shit..."
        bree.say "I want it harder!"
        bree.say "On the floor...fuck me down there, please!"
        "Fuck the videogame, I can play that anytime."
        "Right now all that matters is fucking [bree.name]."
        "I toss the joypad aside, not even bothering to pause the game."
        "Then, with my cock still inside [bree.name], I push her onto the floor."
        scene bree doggy
        show bree doggy vaginal livingroom
        "I use all of my weight as I come down on top of her."
        "And this pushes my cock even deeper into her than before."
        "[bree.name] cries out, voicing the pleasure that she's feeling."
        show bree doggy vaginal scream
        "But I'm not done yet, not even close."
        "Taking a handful of her hair, I raise [bree.name] up."
        "At the same time I have a hand under her belly too."
        "And with these, I get her into the perfect position."
        "Then I start to make quick, powerful thrusts from below."
        show bree doggy vaginal ahegao
        "[bree.name] wails with each one, and I can feel her body tensing."
        "It's too much for her to take, and it pushes her over the edge."
        menu:
            "Cum inside":
                "I shoot my load into [bree.name] just as she arches her back like a bow."
                show bree doggy vaginal cuminpussy with hpunch
                pause 0.25
                with hpunch
                "This means that she gets everything I have to give as deep as I can go."
                with hpunch
                "And once I'm done, she practically slithers onto the floor at my feet."
            "Pull out":
                "At the last moment I pull backwards and out of [bree.name]'s pussy."
                show bree doggy -vaginal dickout with hpunch
                pause 0.25
                with hpunch
                "She groans as my cock pops out of her, shooting it's load over her back."
                show bree doggy cumshot cumonass with hpunch
                "And once I'm done, she practically slithers onto the floor at my feet."
        $ bree.flags.breedelay = TemporaryFlag(True, 2)
        $ bree.sexperience += 1
        with fade
        return
    "[bree.name]'s as good as her word."
    "A moment after she says the words, it happens."
    "Her orgasm makes her muscles squeeze at my cock."
    "And her entire body twitches before me."
    show bree zbox games ahegao
    "It doesn't take long for her to put me over the top either."
    menu:
        "Cum inside":
            with hpunch
            "I shoot my load into [bree.name] just as I pull the joypad backwards."
            with hpunch
            "This means that she gets everything I have to give as deep as I can go."
            with hpunch
            "And once I'm done, she practically slithers onto the floor at my feet."
        "Pull out":
            "At the last moment I pull backwards and out of [bree.name]'s pussy."
            show bree zbox games cumshot with hpunch
            pause 0.25
            with hpunch
            "She groans as my cock pops out of her, shooting it's load over her back."
            show bree zbox games onbody with hpunch
            "And once I'm done, she practically slithers onto the floor at my feet."
    $ bree.flags.breedelay = TemporaryFlag(True, 2)
    $ bree.sexperience += 1
    with fade
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
