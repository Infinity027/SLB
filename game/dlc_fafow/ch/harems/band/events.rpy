











init python:
    Event(**{
    "name": "band_harem_amy_event_01",
    "label": "band_harem_amy_event_01",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_event_01"),
        PersonTarget("amy",
            Not(IsHidden()),
            IsFlag("amydelay", False),
            Not(HasRoomTag("pub"),),
            MinStat("love", 50),
            ),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_pub"),
            ),
        PersonTarget(kleio,
            OnDate(),
            MinStat("sexperience", 1),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })


    Event(**{
    "name": "band_harem_amy_event_02",
    "label": "band_harem_amy_event_02",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("band_harem_amy_event_01"),
        PersonTarget("amy",
            Not(IsHidden()),
            IsFlag("amydelay", False),
            Not(HasRoomTag("pub"),),
            MinStat("love", 70),
            ),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_pub"),
            ),
        PersonTarget(kleio,
            OnDate(),
            MinStat("sexperience", 1),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "band_harem_amy_event_03",
    "label": "band_harem_amy_event_03",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_event_01"),
        PersonTarget("amy",
            Not(IsHidden()),
            IsFlag("amydelay", False),
            Not(HasRoomTag("waterpark")),
            MinStat("love", 100),
            ),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_waterpark"),
            ),
        PersonTarget(anna,
            OnDate(),
            MinStat("sexperience", 1),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "band_harem_amy_event_04",
    "label": "band_harem_amy_event_04",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("band_harem_amy_event_03"),
        PersonTarget("amy",
            Not(IsHidden()),
            IsFlag("amydelay", False),
            Not(HasRoomTag("waterpark")),
            MinStat("love", 120),
            ),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_waterpark"),
            ),
        PersonTarget(anna,
            OnDate(),
            MinStat("sexperience", 1),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "band_harem_amy_event_05",
    "label": "band_harem_amy_event_05",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_event_01"),
        PersonTarget("amy",
            Not(IsHidden()),
            IsFlag("amydelay", False),
            Not(IsRoom("amusement")),
            MinStat("love", 130),
            ),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_amusement"),
            ),
        PersonTarget(sasha,
            OnDate(),
            MinStat("sexperience", 1),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "band_harem_amy_event_06",
    "label": "band_harem_amy_event_06",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("band_harem_amy_event_05"),
        PersonTarget("amy",
            Not(IsHidden()),
            IsFlag("amydelay", False),
            Not(IsRoom("amusement")),
            MinStat("love", 140),
            ),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_amusement"),
            ),
        PersonTarget(sasha,
            OnDate(),
            MinStat("sexperience", 1),
            ),
        ],
    "duration": 1,
    "do_once": True,
    })

    Event(**{
    "name": "band_harem_amy_event_07",
    "label": "band_harem_amy_event_07",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        "len([peace_flags for peace_flags in [amy.flags.peace_with_anna, amy.flags.peace_with_kleio, amy.flags.peace_with_sasha, amy.flags.possible_peace_with_anna, amy.flags.possible_peace_with_kleio, amy.flags.possible_peace_with_sasha] if peace_flags]) >= 2",
        IsDone("band_harem_amy_event_02", "band_harem_amy_event_04", "band_harem_amy_event_06"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        PersonTarget("amy",
            IsFlag("amydelay", False),
            IsActive(),
            MinStat("love", 150),
            ),
        ],
    "duration": 0,
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "band_harem_amy_event_08",
    "label": "band_harem_amy_event_08",
    "display_name": "About Amy",
    "duration": 0,
    "icon": "button_amy",
    "conditions": [
        IsDone("band_harem_amy_event_07"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(kleio,
            IsActive(),
            ),
        PersonTarget("amy",
            Not(IsHidden()),
            MinStat("love", 160),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "band_harem_amy_event_09",
    "label": "band_harem_amy_event_09",
    "display_name": "About Amy",
    "duration": 0,
    "icon": "button_amy",
    "conditions": [
        IsDone("band_harem_amy_event_07"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(anna,
            IsActive(),
            ),
        PersonTarget("amy",
            Not(IsHidden()),
            MinStat("love", 160),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "band_harem_amy_event_10",
    "label": "band_harem_amy_event_10",
    "display_name": "About Amy",
    "duration": 0,
    "icon": "button_amy",
    "conditions": [
        IsDone("band_harem_amy_event_07"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(sasha,
            IsActive(),
            ),
        PersonTarget("amy",
            Not(IsHidden()),
            MinStat("love", 160),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "amy_join_band_harem",
    "label": "amy_join_band_harem",
    "priority": 1500,
    "conditions": [
        IsDone("band_harem_amy_event_08", "band_harem_amy_event_09", "band_harem_amy_event_10"),
        "len([g for g in [anna, kleio, sasha] if g.flags.amy_accepted]) >= 2",
        PersonTarget("amy",
            Not(IsHidden()),
            ),
        ],
    "duration": 0,
    "do_once": True,
    })

    Event(**{
    "name": "band_harem_amy_event_11",
    "label": "band_harem_amy_event_11",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsDone("amy_join_band_harem"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        PersonTarget("amy",
            IsFlag("amydelay", False),
            InHarem("band"),
            IsActive(),
            MinStat("sub", 90),
            MinStat("love", 200),
            ),
        ],
    "duration": 0,
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "amy_concert_naked",
    "label": "amy_concert_naked",
    "display_name": "About our gigs",
    "icon": "gig_talk",
    "duration": 0,
    "conditions": [
        IsDone("gig"),
        HeroTarget(IsGender("male")),
        PersonTarget(amy,
            IsActive(),
            InHarem("band"),
            Not(IsFlag("agree_concert_naked")),
            ),
        PersonTarget(anna,
            Or(
                IsFlag("agree_concert_naked"),
                And(
                    IsNotDone("anna_concert_naked"),
                    Not(IsFlag("agree_concert_naked")),
                ),
            ),
            InHarem("band"),
            ),
        PersonTarget(kleio,
            Or(
                IsFlag("agree_concert_naked"),
                And(
                    IsNotDone("kleio_concert_naked"),
                    Not(IsFlag("agree_concert_naked")),
                ),
            ),
            InHarem("band"),
            ),
        PersonTarget(sasha,
            Or(
                IsFlag("agree_concert_naked"),
                And(
                    IsNotDone("sasha_concert_naked"),
                    Not(IsFlag("agree_concert_naked")),
                ),
            ),
            InHarem("band"),
            ),
        ],
    "once_week": True,
    })

label amy_join_band_harem:
    $ Harem.join_by_name("band", "amy")

    return

label band_harem_amy_event_01:
    scene bg pub
    show kleio casual
    with fade
    "When the atmosphere is right and you're having a good time, there's nowhere as much fun as your local pub."
    "And tonight The Winchester is totally packed, the atmosphere and good vibes almost bursting out of the place."
    "Or maybe I'm just biased because I'm in the middle of a great date with Kleio right now."
    "Well, that and the fact we've both downed more than a few pints since we walked into the place too!"
    "Kleio and I are totally enthralled in the debate we're having about life, the universe and everything."
    "And we both think that we're on the brink of putting the world's problems to bed."
    "That's how brilliant the ideas we keep on coming up with sound to me."
    "But I have to admit that there is a small voice in the back of my head that's not so sure."
    "A voice that keeps on trying to remind me of just how much we've both had to drink."
    show kleio talkative
    kleio.say "Yeah, yeah, yeah..."
    kleio.say "That's exactly what we need to do..."
    kleio.say "We could like, save the human race!"
    show kleio normal
    mike.say "That's what I mean, Kleio!"
    mike.say "I bet nobody ever thought of it before us."
    mike.say "Wait a minute..."
    mike.say "We should...we should...write it all down!"
    "I start rummaging through my pockets, looking for a pen and something to write on."
    "And Kleio seems to be totally onboard with my efforts, as she does all she can to help."
    show kleio talkative
    kleio.say "Hey..."
    kleio.say "Hey, Loverboy..."
    kleio.say "You could write it on the back of this beer mat!"
    show kleio normal
    mike.say "No, no, no..."
    mike.say "It'd never fit, Kleio!"
    mike.say "I'd need like, a hundred of them!"
    "I'm waving my hands in the air to emphasize my point."
    "But for some reason, Kleio doesn't seem to be answering me."
    show kleio annoyed
    "I stare at her for a few seconds, waiting for her to remedy her mistake."
    "But when she doesn't, I follow her gaze."
    "Because whatever's distracting her, I want to know what it is!"
    "It takes me a second, but eventually I spot a familiar face over by the door."
    "It's Amy, and it looks like she just walked into the pub."
    mike.say "Good thinking, Kleio..."
    mike.say "Maybe Amy has a pen and some paper on her!"
    show kleio angry
    kleio.say "If she does, then I'm gonna shove it up her ass!"
    show kleio upset
    "I'm totally amazed by the violence of Kleio's reaction."
    "But before I can ask what the hell's gotten into her, she's up and on her feet."
    "And then she proceeds to push and shove her way across the crowded pub."
    "All the time making a bee-line for Amy!"
    "It takes me a second to react, but then I'm on my feet too."
    "And I'm hurrying after Kleio, trying to keep in her wake."
    "On the way I also try to apologise as best I can for her rudeness too."
    "Saying sorry here and picking people up off the floor there."
    "This means that once Kleio reaches the unsuspecting Amy, I'm a little behind her."
    "So I can't step in before she gets to place a hand on the other girl's shoulder."
    "Without saying a word, Kleio spins Amy around to face her."
    show kleio angry at left
    show amy normal at right
    kleio.say "You've got some nerve coming in here, you bitch!"
    kleio.say "You remember this is the band's local?!?"
    kleio.say "The same band you stabbed in the fucking back!"
    show kleio upset
    show amy surprised
    amy.say "What the actual fuck?!?"
    show amy angry
    amy.say "Shit, Kleio..."
    amy.say "Can't you let it go, you crazy bint?"
    show amy pout
    "It doesn't seem that Amy was expecting to see Kleio in here."
    "Or at least she wasn't expecting to get both barrels of her in the face like that!"
    "She looks totally shocked by the sudden outburst too."
    "So much so that I feel the need to step in and break it up."
    "Or at least pull Kleio away from her before things go too far."
    if amy.flags.told_about_band:
        "And I move extra fast to do so too."
        "Because I know full well what the source of the bad blood is here."
        "Kleio might have mentioned the fact that Amy used to be in her band."
        "But I already knew that she was a former member of the Deathless Harpies."
        "So it's no surprise that things are going down like this."
        mike.say "Whoa..."
        mike.say "Whoa, whoa, whoa..."
        mike.say "I get it, Kleio, I get it!"
        mike.say "But isn't it time to let go of what happened in the past?"
        mike.say "To forgive and move on?"
    else:
        "I start waving my arms in the air again."
        "But this time it's as I put myself between Kleio and Amy."
        mike.say "Whoa..."
        mike.say "Whoa, whoa, whoa..."
        mike.say "What's all of this even about?"
        mike.say "Kleio, I didn't know you and Amy knew each other!"
        "Kleio still seems to be trying her beat to get past me and reach Amy."
        "But the other girl takes this as her chance to escape any immediate danger."
        "And she backs off, well out of Kleio's reach."
        show kleio annoyed
        kleio.say "There's nothing to, know..."
        kleio.say "Just that she's a traitor and a bitch!"
        show kleio upset
        "I'm still holding Kleio back as I look to Amy."
        "And I do so kind of hoping that she'll be more forthcoming."
        show amy whining
        amy.say "Sorry, [hero.name]..."
        amy.say "I didn't know you knew her either."
        amy.say "We used to be in a band together."
        amy.say "And, as you might have guessed, it didn't work out!"
        show amy sad
        show kleio talkative
        kleio.say "Yeah, and who's fault was that?!?"
        show kleio upset
        mike.say "I get it, Kleio, I get it!"
        mike.say "But isn't it time to let go of what happened in the past?"
        mike.say "To forgive and move on?"
    show kleio talkative
    kleio.say "No way!"
    kleio.say "It's time I gave her the beating she deserves!"
    show kleio upset
    "At first I think that Kleio's just puffed up on alcoholic bravado."
    "But then she actually takes a swing at Amy."
    "And that's when I find myself leaping into action."
    "Catching Kleio around the waist, I trap her in a reverse bear-hug."
    "But even when I have a firm hold on her, she keeps trying to reach Amy."
    "And I find myself lifting her off the ground to keep her from doing so."
    mike.say "Kleio..."
    mike.say "Will you stop it!"
    show kleio angry
    kleio.say "No way, Loverboy..."
    kleio.say "I wanna kick her ass!"
    show kleio upset
    "By now almost everyone in the pub has stopped what they're doing."
    "And their attention is focussed solely on Kleio, Amy and myself."
    "I don't want to let go of Kleio for fear of what she'll do."
    "So it seems to me that the only option is to keep hold of her."
    "That and to begin making for the exit, carrying Kleio with me."
    mike.say "Erm..."
    mike.say "Sorry, Amy!"
    mike.say "This really isn't how I wanted things to play out tonight, yeah?"
    show kleio angry
    kleio.say "Will you put me the fuck down?"
    kleio.say "You can watch me pummel that bitch into the middle of next week."
    kleio.say "It'll be fun, I promise!"
    show kleio upset
    show amy whining
    amy.say "Yeah..."
    amy.say "Whatever you say, [hero.name]..."
    amy.say "I guess I'll see you around."
    show amy sadsmile
    "I'm doing the best I can to keep a smile on my face as I back out of the pub."
    "An effort that's made all the more ridiculous by the way I'm holding onto Kleio."
    "She wriggles and squirms the whole time, kicking her legs in the air."
    "This means that on the way to the exit, she almost injures more than a few drinkers."
    "And I don't feel safe to release her until we're safely on the sidewalk outside."
    "Even when I do so, Kleio instantly makes to rush back into the pub."
    "But I manage to catch hold of her hand, spinning her around to face me."
    show kleio angry
    kleio.say "Hey!"
    kleio.say "What gives, Loverboy?"
    kleio.say "She's still in there, and her ass still wants kicking!"
    show kleio upset
    mike.say "Hmm..."
    mike.say "Maybe I'm beginning to see why she left the band."
    "Despite the fact that she's drunk, Kleio instantly reacts to my comment."
    "She puffs herself up and does the best she can to face me down."
    "Which requires her to stand up on her tip-toes to even attempt."
    show kleio angry
    kleio.say "What's that supposed to mean?!?"
    show kleio upset
    mike.say "Well, you seem to solve problems with your fists, Kleio."
    mike.say "Even when using your mouth might be a better idea!"
    "Much to my surprise, the rebuke actually seems to have an effect."
    show kleio annoyed
    "Kleio looks down at her feet, as if she's genuinely embarrassed."
    show kleio whining
    kleio.say "That's not fair, [hero.name]..."
    kleio.say "You're my date, so you're supposed to stick up for me!"
    show kleio sadsmile
    "No matter how embarrassed I was by Kleio's little performance back there, I'm not made of stone."
    "Almost the same moment I hear her tone become apologetic, my resolve crumbles away to nothing."
    mike.say "Ah..."
    mike.say "I know, Kleio, I know."
    mike.say "I just didn't want you to do something you'd regret in the morning."
    "Kleio leans herself against me as we start to walk off down the street."
    "And I feel that she's silently accepting my explanation for the sake of making peace."
    show kleio talkative
    kleio.say "But, Loverboy..."
    kleio.say "I never regretted kicking anyone's ass!"
    $ game.room = "map"
    $ game.active_date.stay = False
    $ amy.flags.amydelay = TemporaryFlag(True, 2)
    return


label band_harem_amy_event_02:
    scene bg door pub with fade
    show kleio at center, zoomAt (1.5, (640, 1040))
    with fade
    kleio.say "You can stop worrying, Loverboy..."
    kleio.say "Because I forgive you for the other night."
    show kleio at center, traveling (1.75, 0.5, (640, 1200))
    "Kleio's holding onto my arm as she says all of this, leaning her weight against me."
    play sound punch_hard
    with hpunch
    "But unlike almost any other girl I could mention, she feels the need to jab me in the ribs too."
    "Like that's the normal and accepted means of punctuating what you just said and underlining your point."
    mike.say "Oof..."
    mike.say "Ah...yeah, Kleio..."
    mike.say "Thanks for that!"
    show kleio at center, traveling (1.5, 0.5, (640, 1040))
    "Obviously she's talking about the incident that took place the other night."
    "When Amy just happened to walk into The Winchester in the middle of our date."
    "Kleio was more than a little drunk, she all of the resentment between them came to a head."
    "And I ended up literally carrying her out of the pub before they came to blows!"
    mike.say "But you're sure you want to go back to The Winchester tonight?"
    mike.say "There are no bad memories or anything like that?"
    "Kleio shakes her head at this, totally dismissing my concerns."
    show kleio annoyed
    kleio.say "Nah..."
    show kleio normal
    kleio.say "There's no way that skank Amy would show her face in there again."
    kleio.say "Not when she thinks there's even the slightest chance of me showing up."
    "I force a smile onto my face that I hope looks genuine."
    scene bg pub with fade
    pause 0.1
    show kleio at right with easeinright
    "And then I hold the door of the pub open as we slip inside."
    "The place isn't as busy as it was the last time we were in here."
    "But it's still full enough for us to have to weave our way to the bar."
    "As we get there, I happen to be in the lead, with Kleio behind me."
    "Which is probably why a certain girl at the bar turns straight around to greet me."
    show amy happy at left with easeinleft
    amy.say "Hey, [hero.name]…"
    amy.say "I'm so glad you asked me to come along tonight."
    amy.say "I really think we need to..."
    show amy surprised
    show kleio surprised at right5 with ease
    kleio.say "What the fuck?"
    show kleio angry
    kleio.say "What the actual fuck?!?"
    show amy upset at left5 with ease
    "Wait a minute, I'm getting a genuine feeling of deja vu here."
    "Right down to the fact that I'm in the middle of Kleio and Amy again."
    "But then I remember that this time there's a real difference."
    "This time it's all part of what I hope will prove to be a cunning plan."
    show amy angry
    amy.say "[hero.name]…"
    amy.say "What's she doing here?"
    show kleio angry
    kleio.say "What am I doing here?"
    kleio.say "You've got some nerve, asking that!"
    play sound "<from 0 to 0.6>sd/SFX/doors/door_banging.ogg"
    show kleio surprised
    show kleio surprised
    with vpunch
    "Without warning, I slam my hand down on the bar."
    "The sound is louder than I expected it to be."
    "So loud that it makes almost everyone in the place stop and stare in our direction."
    "And it bloody well hurts my hand too!"
    mike.say "Okay, you two..."
    mike.say "It's about time I came clean."
    mike.say "Kleio, we're here on a date."
    mike.say "But it's a double date."
    mike.say "Amy's invited on it too."
    "For the first time I can remember, Kleio and Amy stop fighting with each other."
    show kleio at center, zoomAt (1.25, (940, 880))
    show amy at center, zoomAt (1.25, (340, 880))
    "But the only problem is that instead, the both of them are now staring straight at me!"
    show kleio angry
    kleio.say "Urgh..."
    kleio.say "Now I have to kick your ass, as well as hers!"
    show amy angry
    amy.say "[hero.name], how could you?"
    amy.say "You lured me here under false pretences!"
    "I shake my head, dismissing both of their protests."
    mike.say "Number one, nobody is kicking anyone's ass."
    mike.say "And two, nobody's keeping you here either."
    mike.say "I just thought that maybe you two could do with spending some quality time together."
    mike.say "You know, see past your differences with the help of some fun and friendship?"
    show kleio annoyed
    show amy annoyed
    "Kleio and Amy exchange one of the frostiest looks I've ever seen."
    amy.say "Well that sounds reasonable to me, [hero.name]."
    amy.say "But you'll never convince her."
    amy.say "All she wants to do is butt her thick head against everything in her path!"
    show amy angry
    kleio.say "Hey!"
    kleio.say "I can too make this thing work."
    kleio.say "Because, unlike you, I don't quit when things get tough!"
    show kleio annoyed
    "I think I'm beginning to see a strategy emerging here."
    "Sure, Kleio and Amy might claim that they hate each other's guts."
    "But they each seem to hate the idea of being shown up by the other even more."
    "Maybe if I can use that to my advantage, we can get somewhere."
    mike.say "Okay then..."
    mike.say "Prove it to me, yeah?"
    mike.say "Show me which of you is really willing to change."
    mike.say "And which one of you's actually a thick-headed, stubborn cow!"
    show kleio normal
    kleio.say "Oh I will!"
    show amy normal
    amy.say "You're on!"
    "I do the best I can to keep from smirking as they both take the bait."
    "Because experience tells me that neither of them would appreciate being manipulated like this."
    mike.say "Okay..."
    mike.say "So let's just relax and have a good time, right?"
    mike.say "As far as the world at large knows, we're all good friends."
    "Kleio and Amy both nod at this."
    show kleio annoyed
    show amy annoyed
    "But I can see that they're shooting each other hard glances."
    "So I do the best I can to put that out of my mind and get on with the date."
    show kleio sad
    kleio.say "So what happens now?"
    show amy sadsmile
    amy.say "I guess you have a plan, [hero.name]?"
    mike.say "Well..."
    mike.say "We've been in a pub for a few minutes now."
    mike.say "And I notice that I still don't have a beer in my hand!"
    mike.say "So what do you say we put that right?"
    show amy normal
    show kleio normal
    "I turn to the bar and start studying the drinks on offer."
    show kleio at center, traveling (1.5, 0.2, (940, 1040))
    "And a moment later, I feel Kleio pushing up against my right side."
    show amy at center, traveling (1.5, 0.2, (340, 1040))
    "Then I feel Amy doing the exact same thing on the left."
    show kleio happy
    kleio.say "So, what are you drinking, Loverboy?"
    kleio.say "First round's on me!"
    show amy angry
    show kleio annoyed
    amy.say "Oh no you don't!"
    amy.say "I'll get these."
    amy.say "And why do you always call him that?"
    amy.say "It's really weird..."
    show amy annoyed
    "Oh great, we're only just getting around to ordering a drink."
    "And here comes the first potential argument."
    "Looks like I'm going to have to step in here."
    $ renpy.dynamic(amy_score=0, kleio_score=0)
    menu:
        "Let the first round to Kleio":
            "I feel like I need to show some loyalty to Kleio here."
            "Even if it is something as small as buying a drink."
            mike.say "You go ahead, Kleio..."
            mike.say "We can take it in turns to buy rounds."
            show kleio happy
            "Kleio's face twists into a victorious smirk."
            show amy upset
            "But Amy looks instantly pissed off."
            kleio.say "Thanks, Loverboy!"
            amy.say "Huh..."
            amy.say "I should have guessed you'd side with her!"
            $ amy_score -= 1
            $ kleio_score += 1
        "Let the first round to Amy":
            "I feel like I need to throw Amy a bone here."
            "Even if it is something as small as buying a drink."
            mike.say "You go ahead, Amy..."
            mike.say "We can take it in turns to buy rounds."
            show amy happy
            "Amy's face twists into a victorious smirk."
            show kleio angry
            "But Kleio looks instantly pissed off."
            kleio.say "Thanks a bunch, you traitor!"
            amy.say "Oh grow up, Kleio!"
            $ amy_score += 1
            $ kleio_score -= 1
        "Handle the first round" if hero.money >= 25 and hero.charm >= 25:
            "I feel like I have to assert a little bit of authority here."
            "Just enough to keep Kleio and Amy from trying to pull shit like this all night."
            mike.say "Since I'm the one that organised tonight, I'll get the drinks."
            mike.say "That way nobody's trying to get one over on anyone else, okay?"
            "I can see that neither of them like it."
            show kleio happy
            show amy happy
            "But they both nod their heads in agreement all the same."
            kleio.say "Okay, Okay."
            amy.say "I guess that's fair."
            $ amy_score += 1
            $ kleio_score += 1
    show kleio normal
    show amy normal
    with fade
    "Once we all have a drink, I spot a table that's free nearby."
    "So I head straight over there without pause or hesitation."
    "Of course Kleio and Amy follow close on my heels."
    "Because neither of them wants to be accused of not being on board for this thing."
    scene drink_room_pub
    show amy a at center, zoomAt(1.65, (340, 1040))
    show kleio a at center, zoomAt(1.65, (940, 1040))
    show drink_table_pub_victor
    show drink_room_fg_pub
    with fade
    "Sitting down, I put on what I hope is a friendly face."
    mike.say "Okay..."
    mike.say "The way I see it is that you two must have gotten on at one point."
    mike.say "Otherwise you wouldn't have been in a band together."
    "I glance at Kleio."
    mike.say "Kleio, how did you end up asking Amy to join the band?"
    show kleio a blush
    "At this, I see Kleio suddenly flush with colour."
    show amy a happy at startle
    "But before I can ask why, Amy lets out a burst of laughter."
    amy.say "Ha!"
    show amy a annoyed
    amy.say "Is that what she told you?"
    amy.say "It was me that asked her to join the band!"
    kleio.say "Hey, I was the one doing you a favour."
    show kleio a angry
    kleio.say "Your old bass-player sucked ass!"
    kleio.say "And it's not my fault I turned out to be a better singer than you too."
    menu:
        "So, Kleio, Amy was actually in the band before you?":
            "I can't help shaking my head as I hear all of this."
            mike.say "Kleio..."
            mike.say "Why'd you never tell me Amy was in the band before you?"
            show kleio a annoyed
            kleio.say "Because it doesn't matter, that's why!"
            mike.say "But doesn't that mean it was, like, Amy's band?"
            "By now Kleio's visibly fuming at me."
            show kleio a angry
            kleio.say "It's not like that..."
            kleio.say "The band's a democracy!"
            show amy a angry
            amy.say "Not from where I'm standing it's not!"
            $ amy_score += 1
            $ kleio_score -= 1
        "Kleio is really a better singer than you Amy?":
            "I can't help shaking my head as I hear all of this."
            mike.say "Wow, Amy..."
            mike.say "You're saying Kleio's more talented than you?"
            "Amy's head snaps around at this."
            "And from the look in her eyes, I can tell she's not happy."
            show amy a annoyed
            amy.say "What do you mean, more talented than me?"
            amy.say "She wormed her way in and then pushed me out!"
            kleio.say "That's not how I remember it."
            show kleio a annoyed
            kleio.say "Us kicking you out was a group decision."
            kleio.say "The band's a democracy!"
            show amy a angry
            amy.say "Not from where I'm standing it's not!"
            $ amy_score -= 1
            $ kleio_score += 1
        "Well, that's a shame!" if hero.has_skill("guitar"):
            "I can't help shaking my head as I hear all of this."
            mike.say "What a waste!"
            show amy a annoyed
            "Amy's head snaps around at this."
            "And from the look in her eyes, I can tell she's not happy."
            show kleio a annoyed
            "Kleio doesn't seem to be pleased with my comment either."
            amy.say "What's that supposed to mean?"
            kleio.say "Talk sense, Loverboy!"
            "I shrug as I try to explain myself."
            mike.say "It's just that I've heard both of you play."
            mike.say "And you're like, so talented."
            mike.say "A band with the pair of you in must have sounded totally amazing."
            show kleio a annoyed blush
            show amy a shy
            "Kleio and Amy seem oddly embarrassed by this comment."
            kleio.say "I...I guess we had our moments."
            amy.say "Yeah..."
            amy.say "It was good, while it lasted."
            $ amy_score += 1
            $ kleio_score += 1
    show kleio a normal
    show amy a normal
    "I can sense that we're not going to make any great strides just sitting around talking."
    "And that's when I notice that the dart-board is free, so I hop up and grab some darts."
    "Kleio and Amy seem to crack onto what I'm doing even before I can say it myself."
    show kleio a happy
    kleio.say "You really want to challenge me to a game of darts, Loverboy?"
    kleio.say "I'm like, the all time Deathless Harpies darts champion!"
    show amy a annoyed
    amy.say "Since when is that?"
    amy.say "Only since I got pushed out of the band!"
    mike.say "That sounds like some big talk from the pair of you."
    mike.say "Why don't you put your money where your mouths are?"
    mike.say "Because I'm going to beat the pair of you!"
    "This seems to be enough to get the girls off their backsides."
    show date pub dart none zorder 1 at center
    show kleio zorder 2 at center, zoomAt(1.1, (1100, 880))
    show amy zorder 3 at center, zoomAt(1.1, (800, 880))
    with fade
    "So hopefully a little spirited competition will help clear the air."
    menu:
        "Play fair" if hero.has_skill("shooting"):
            hide kleio
            hide amy
            show date pub dart kleio zorder 1 at center
            with fade
            "Kleio and Amy seem dead set on beating each other."
            "Both of them desperately wanting to prove a point."
            show date pub dart amy zorder 1 at center
            with fade
            "But that means neither of them is really paying any attention to me."
            "Which makes the game pretty easy pickings for a player of my skill."
            show date pub dart none zorder 1 at center
            show kleio zorder 2 at center, zoomAt(1.1, (1100, 880))
            show amy zorder 3 at center, zoomAt(1.1, (800, 880))
            with fade
            "And before either of them realises it, I have them squarely beaten."
            mike.say "I have to hand something to you, Ladies..."
            mike.say "And it just so happens to be your asses!"
            show kleio surprised
            kleio.say "What the..."
            show amy surprised
            amy.say "No way!"
            mike.say "Sorry, but you were too distracted to even notice."
            mike.say "Too busy trying to beat each other to have a chance against me!"
            show amy normal
            show kleio normal
            "Sure, I feel a little bad rubbing it in like that."
            "But I had an important point to make back there."
            "And from the sheepish looks on their faces, Kleio and Amy know that too."
            "So maybe I actually managed to get through to them this time."
            $ amy_score += 1
            $ kleio_score += 1
        "Help Amy":
            hide kleio
            hide amy
            show date pub dart kleio zorder 1 at center
            with fade
            "It doesn't take long for it to become obvious who's going to win out."
            "I know that I have a great chance of winning, but Amy doesn't."
            "Every throw she makes seems to be worse than the last."
            "And at the same time, Kleio's totally on form."
            "So I resolve to do all I can to change that."
            show date pub dart amy zorder 1 at center
            with fade
            "It's not easy, but somehow I manage to pull gimp my own game."
            "And I do it in just such a way to make sure Amy comes out on top."
            amy.say "Ha..."
            amy.say "Deathless Harpies Darts Champion, my ass!"
            show date pub dart none zorder 1 at center
            show kleio annoyed zorder 2 at center, zoomAt(1.1, (1100, 880))
            show amy happy zorder 3 at center, zoomAt(1.1, (800, 880))
            with fade
            "Kleio doesn't come out and say it, but I can tell she suspects something's up."
            "Because the looks she keeps shooting me are far from friendly right now!"
            $ amy_score += 1
            $ kleio_score -= 1
        "Help Kleio":
            hide kleio
            hide amy
            show date pub dart amy zorder 1 at center
            with fade
            "It doesn't take long for it to become obvious who's going to win out."
            "I know that I have a great chance of winning, but Kleio doesn't."
            "Every throw she makes seems to be worse than the last."
            "And at the same time, Amy's totally on form."
            "So I resolve to do all I can to change that."
            "It's not easy, but somehow I manage to pull gimp my own game."
            show date pub dart kleio zorder 1 at center
            with fade
            "And I do it in just such a way to make sure Kleio comes out on top."
            kleio.say "YES!"
            kleio.say "In your face, Amy!"
            show date pub dart none zorder 1 at center
            show kleio happy zorder 2 at center, zoomAt(1.1, (1100, 880))
            show amy annoyed zorder 3 at center, zoomAt(1.1, (800, 880))
            with fade
            "Amy doesn't come out and say it, but I can tell she suspects something's up."
            "Because the looks she keeps shooting me are far from friendly right now!"
            $ amy_score -= 1
            $ kleio_score += 1
    scene bg pub with fade
    "Once the game of darts is over, I'm ready to move on from it."
    "Maybe go back to the table and order some food or just chat."
    "But when I make a move to walk back to it, I feel hand on my arm."
    "Not just that, I feel one on each of my arms at once!"
    "Looking to one side and then the other, I soon see what the problem is."
    show kleio at center, zoomAt (1.5, (940, 1040))
    show amy at center, zoomAt (1.5, (340, 1040))
    with dissolve
    "Kleio's taken hold of one arm, and Amy's gripping the other!"
    mike.say "Erm..."
    mike.say "What seems to be the problem here?"
    mike.say "I thought we were done playing darts?"
    kleio.say "We are, we are..."
    show kleio normal
    kleio.say "But I'm not done proving myself...I mean playing, yet!"
    amy.say "I can't believe I'm saying this..."
    show amy normal
    amy.say "But Kleio's right - I want to play some more too."
    "I glance over to see that someone else has now started using the dart-board."
    "But when I scan around the pub for an alternative, I see the pool-table is free."
    "So I grab a pair of cues and hand one to each of the girls."
    mike.say "Okay..."
    mike.say "Looks like round two is going to be pool."
    "Still eyeing each other jealously, Kleio and Amy stalk over to the pool-table."
    "Which leaves me to rack up the balls and get things ready."
    show kleio annoyed
    kleio.say "Wait a minute, Loverboy..."
    kleio.say "Who's side are you going to be on?"
    show amy annoyed
    amy.say "She's got a point, [hero.name]..."
    amy.say "We can't have a three-way game of pool!"
    "I nod casually as I stand up and turn to face the girls."
    "But at the same time my mind's racing."
    "Because I need to come up with a solution, and fast!"
    menu:
        "Team up with Kleio":
            "When we were playing darts before, things were different."
            "There was no need to choose sides and we could all play for ourselves."
            "But now I have to choose between Kleio and Amy."
            "And as much as I want to get the two of them talking, I have to choose Kleio."
            "Because otherwise I'm practically turning on her."
            mike.say "I'll team up with you, Kleio."
            show kleio happy
            kleio.say "You know you will, Loverboy!"
            show amy annoyed
            amy.say "Urgh..."
            amy.say "Like I should have expected anything else!"
            "I do the best I can to ignore Kleio's crowing and Amy's complaining alike."
            show pool kleio zorder 5 at center with fade
            "And instead I break, getting the game started."
            "I don't know if it's the numbers advantage that does it."
            show pool amy zorder 5 at center with fade
            "Or if me not choosing Amy put her off."
            "But whatever the reason, she never really seems to get into the game."
            show pool kleio zorder 5 at center with fade
            "Which means that Kleio and I pretty much wipe the floor with her."
            kleio.say "Take that, Amy..."
            kleio.say "The best girl won!"
            amy.say "Yeah, yeah..."
            amy.say "Like I really give a damn!"
            $ amy_score -= 1
            $ kleio_score += 1
        "Team up with Amy":
            "When we were playing darts before, things were different."
            "There was no need to choose sides and we could all play for ourselves."
            "But now I have to choose between Kleio and Amy."
            "And as much as I want to get the two of them talking, I have to choose Amy."
            "Otherwise this thing is going to go nowhere."
            mike.say "I'll team up with you, Amy."
            show kleio angry
            kleio.say "You're going to do what?!?"
            kleio.say "You treacherous rat!"
            show amy happy
            amy.say "Oh grow up, Kleio..."
            amy.say "It's only a game!"
            "I do the best I can to ignore Kleio's complaining and Amy's crowing alike."
            show pool amy zorder 5 at center with fade
            "And instead I break, getting the game started."
            "I don't know if it's the numbers advantage that does it."
            show pool kleio zorder 5 at center with fade
            "Or if me not choosing Kleio put her off."
            "But whatever the reason, she never really seems to get into the game."
            show pool amy zorder 5 at center with fade
            "Which means that Amy and I pretty much wipe the floor with her."
            amy.say "Take that, Kleio..."
            amy.say "The best girl won!"
            kleio.say "Yeah, yeah..."
            kleio.say "Like I really give a damn!"
            $ amy_score += 1
            $ kleio_score -= 1
        "Play against Kleio and Amy" if hero.knowledge >= 50:
            "When we were playing darts before, things were different."
            "There was no need to choose sides and we could all play for ourselves."
            "But now I have to choose between Kleio and Amy."
            "Or do I?"
            "Because a thought just occurred to me."
            "And it might just help me get these two on the same page."
            mike.say "The two of you might as well team up against me."
            mike.say "Because that's the only way either of you stands a chance!"
            show amy surprised
            show kleio surprised
            "For a moment, Kleio and Amy just stand and stare at me."
            "And they look pretty comical with their mouths hanging open too."
            "But of course, them being lost for words doesn't last long."
            show kleio annoyed
            kleio.say "What the hell is that supposed to mean?"
            kleio.say "I'm easily as good at pool as you!"
            show amy annoyed
            amy.say "Hey, I don't need a partner to win this game."
            amy.say "I can do it all on my own!"
            "I put on an arrogant grin and shake my head."
            mike.say "Girls, girls..."
            mike.say "I understand if you want to forfeit the game."
            mike.say "Rather than have me humiliate the both of you at once!"
            kleio.say "Right, that does it!"
            show kleio normal
            kleio.say "Amy, we're teaming up, just this once."
            amy.say "What are you suggesting?"
            show amy normal
            amy.say "A temporary truce, until we beat this jackass?"
            "Kleio nods, and gets another one in return from Amy."
            show pool kleio zorder 5 at center with fade
            "Then it's game on, and I break to get things going."
            "It's all I can do to keep from smiling as the game goes on."
            show pool amy zorder 5 at center with fade
            "Because my plan us working perfectly."
            "Kleio and Amy are incensed and totally focussed on beating me."
            show pool kleio zorder 5 at center with fade
            "Which means that they have to work as a team if they want that to happen."
            "In the end they're on a plain, beating me pretty soundly."
            "They even manage to avoid an argument on who gets to sink the last ball of the game."
            hide pool
            show kleio happy
            with fade
            kleio.say "HA!"
            kleio.say "In your face, Loverboy!"
            show amy happy
            amy.say "What do you say now, huh?"
            amy.say "We really did a number on you!"
            "I cross my arms and nod my head."
            mike.say "Yeah, you did."
            mike.say "The two of you make a pretty good team."
            mike.say "Don't you think?"
            show amy annoyed
            show kleio annoyed
            "Suddenly, Kleio and Amy are exchanging awkward glances."
            "And neither of them seems to want to argue anymore."
            "But I can see that the pair of them have been forced to think about what I just said."
            $ amy_score += 1
            $ kleio_score += 1
    hide pool
    show kleio normal
    show amy normal
    with fade
    "It's only when we walk away from the pool-table that I feel my stomach rumbling."
    "Then I remember that I was intending to eat something at the pub all along."
    "But I got distracted and played all of those games instead, so now I'm starving!"
    mike.say "I don't know about you guys..."
    mike.say "But I could really use some food right about now."
    "This time there's no way for Kleio and Amy to disagree."
    "Because I can see the mere mention of food is making them feel hungry too."
    show kleio happy
    kleio.say "Oh yeah..."
    show amy happy
    amy.say "I'm starving!"
    kleio.say "We have to get some of the burgers they do here!"
    show amy annoyed
    amy.say "No way - I want to grab one of their pizzas!"
    show kleio annoyed
    "Just when I thought that we'd all found some common ground."
    "There they go again, squabbling over the smallest detail!"
    "But there's still one of us to speak up on the subject."
    menu:
        "Let's go get burgers":
            "The moment that Kleio mentioned burgers, my mind was made up."
            mike.say "Burgers sound like a great idea."
            mike.say "Let's order three of those, right now!"
            show kleio happy
            "Kleio nods in agreement."
            "But Amy isn't ready to give up the fight just yet."
            show amy annoyed
            amy.say "Screw you guys."
            amy.say "I'm still ordering pizza."
            kleio.say "You do you, Amy..."
            kleio.say "But that means the food will be turning up at different times."
            kleio.say "So you'll end up eating on your own."
            "Amy's brows furrow and she doesn't look happy."
            "But she grits her teeth and makes a gesture of helpless surrender."
            $ amy_score -= 1
            $ kleio_score += 1
        "Let's go get pizza":
            "The moment that Amy mentioned pizza, my mind was made up."
            mike.say "Pizza sounds like a great idea."
            mike.say "Let's order a couple of those, right now!"
            show amy happy
            "Amy nods in agreement."
            "But Kleio isn't ready to give up the fight just yet."
            show kleio annoyed
            kleio.say "Screw you guys."
            kleio.say "I'm still ordering pizza."
            amy.say "You do you, Kleio..."
            amy.say "But that means the food will be turning up at different times."
            amy.say "So you'll end up eating on your own."
            "Kleio's brows furrow and she doesn't look happy."
            "But she grits her teeth and makes a gesture of helpless surrender."
            $ amy_score += 1
            $ kleio_score -= 1
        "Why choose?" if hero.has_skill("foodie"):
            "Both of those options sound good to me."
            "So good in fact that I don't want to choose."
            mike.say "Why not both?"
            mike.say "Let's order a pizza and a burger each."
            show amy normal
            show kleio normal
            "At first Kleio and Amy seem thrown by the idea."
            "But it doesn't take them long to find an objection."
            kleio.say "But that means the food will be turning up at different times."
            show kleio annoyed
            kleio.say "The pizza will be ready well before the burgers!"
            show amy annoyed
            amy.say "So we'll end up with stuff going cold!"
            "I shrug as I begin thinking out loud."
            mike.say "Not if we all order a pizza we can share."
            mike.say "Then we can eat it while we wait for the burgers."
            show kleio normal
            show amy happy
            "Kleio and Amy seem to think about it for a moment."
            "Then, much to my surprise, they both nod."
            "And the plan works out pretty well too."
            scene drink_room_pub
            show amy a happy at center, zoomAt(1.65, (340, 1040))
            show kleio a happy at center, zoomAt(1.65, (940, 1040))
            show drink_table_pub_victor
            show drink_room_fg_pub
            with fade
            "We share a pizza while we have another round of drinks."
            "Then, when the burgers arrive, we pounce on them like ravenous animals."
            $ amy_score += 1
            $ kleio_score += 1
    scene drink_room_pub
    show amy a at center, zoomAt(1.65, (340, 1040))
    show kleio a at center, zoomAt(1.65, (940, 1040))
    show drink_table_pub_victor
    show drink_room_fg_pub
    with fade
    "By now I'm starting to feel pretty stuffed and tired."
    "And it feels like the night is coming to a natural end."
    "But before I call it quits, I want to see if I achieved my goal."
    "I want to see if I've managed to get Kleio and Amy to bury the hatchet."
    mike.say "So..."
    mike.say "Are we thinking that certain people might not be massive assholes now?"
    mike.say "Maybe ready to agree that we were far too judgemental too?"
    show amy a annoyed
    show kleio a annoyed
    "I watch as Kleio and Amy exchange another glance."
    "And then I hold my breath as I wait to hear the answer."
    if amy_score >= 4 and kleio_score >= 4:
        show kleio normal
        show amy normal
        kleio.say "Okay, I admit it..."
        kleio.say "Amy's not the villain I thought she was."
        "I look Kleio straight in the eye once she's said this."
        mike.say "And?"
        kleio.say "Urgh..."
        kleio.say "And sometimes I can overreact, a little."
        "Okay, that's downplaying it quite a bit."
        "But at least it's a start."
        "I see that Amy's nodding too."
        amy.say "Yeah..."
        amy.say "I think the whole band thing clouded my vision too."
        amy.say "I'd forgotten all the fun we used to have before that."
        show amy a happy at startle
        "At this, she bursts out laughing."
        show kleio a happy at startle
        "And it only take a second for Kleio to join in too."
        mike.say "Wait a minute..."
        mike.say "What am I missing here?"
        amy.say "What do you think, Kleio?"
        amy.say "You want to show him how the Deathless Harpies used to party?"
        kleio.say "Oh man, this is like getting the old band back together!"
        kleio.say "Fuck it, let's show him!"
        scene bg pub with fade
        "The next thing I know, Kleio and Amy are grabbing hold of my hands."
        "Then I'm being dragged out of the pub, with no idea where we're headed."
        "But I'm very interested in finding out what's going to happen when we get there."
        $ amy.flags.peace_with_kleio = True
        call amy_kleio_park_threesome from _call_amy_kleio_park_threesome
    else:
        show kleio sad
        kleio.say "Okay, I admit it..."
        kleio.say "Amy's not the villain I thought she was."
        kleio.say "But..."
        "Urgh..."
        "Why does there always have to be a but!"
        kleio.say "But I'm just not ready to be her best buddy yet."
        "Amy listens to all of this with a remarkably reasonable expression on her face."
        "And when Kleio's done explaining herself, she nods in agreement."
        show amy a sadsmile
        amy.say "I kind of feel the same way."
        amy.say "There's no big pit of anger in my stomach anymore."
        amy.say "But I need time to see how this feels."
        show amy a at center, zoomAt(1.65, (340, 840)) with ease
        pause 0.5
        hide amy with easeoutleft
        "All I can do is watch as Amy gets up and walks out of the pub."
        scene bg street with fade
        "Which leaves Kleio and me to walk home together."
        "I guess I should be pleased with the way things turned out."
        "I might not have built the bridges I wanted to."
        "But at least it's a start, and that has to count for something."
        $ amy.flags.possible_peace_with_kleio = True
    return

label band_harem_amy_event_03:
    scene bg waterpark
    with fade
    show anna b dazed swimsuit at center, zoomAt (0.9, (1180, 720)) with easeinright
    anna.say "[hero.name]…"
    show anna b dazed at center, traveling (1.1, 0.3, (1000, 820))
    anna.say "Hey, [hero.name]…"
    show anna b at startle
    pause 0.2
    show anna b angry at center, traveling (1.2, 0.3, (900, 880))
    anna.say "Wait for me!"
    show anna b annoyed
    "Sneaking a look back over my shoulder, I can't help chuckling to myself."
    show anna b at startle
    pause 0.2
    show anna b at center, traveling (1.3, 0.3, (800, 940))
    "Because I can see Anna running after me, waving a hand in the air."
    "And the fact that she's in her swimming costume means that it's quite a sight."
    "Look, before you say anything, I know that what I'm doing is mean."
    "But it's only small-time mean, okay?"
    "And the way Anna's curvy little body is moving right now..."
    "Well that's got to make the whole thing worthwhile!"
    mike.say "Come on, Anna..."
    mike.say "The water-park is going to be closed at this rate!"
    show anna b blush at center, traveling (1.5, 0.3, (640, 1040))
    "Anna's caught up to me by now, and she's still huffing and puffing."
    "But I get the feeling that has more to do with her being annoyed than exhausted."
    show anna angry
    anna.say "Ooh..."
    anna.say "That was really rotten of you, [hero.name]…"
    show anna at startle
    anna.say "Especially when you know my legs are so much shorter than yours!"
    scene bg waterpark at dark, blur(5)
    show anna b swimsuit annoyed at center, zoomAt(1.5, (640, 1040)), top_to_bottom
    with fade
    "At the mere mention of Anna's legs, I can't help myself."
    "I just have to take a moment to look them up and down."
    "Anna seems to notice the attention I'm paying to her."
    "And it temporarily distracts her from telling me off."
    anna.say "What is it?"
    anna.say "What are you looking at?"
    anna.say "Do I have a label showing or something?"
    anna.say "Or did I put my swimming costume on back to front again?"
    show anna b swimsuit annoyed at center, zoomAt(1.5, (640, 1040)), bottom_to_top
    "I look up from admiring Anna's legs and shake my head."
    scene bg waterpark
    show anna b swimsuit annoyed at center, zoomAt(1.5, (640, 1040))
    with hpunch
    mike.say "What?"
    mike.say "Oh no, Anna..."
    mike.say "I have to admit it - I was just checking out your legs."
    show anna normal
    mike.say "You look super-hot in that swimming costume!"
    show anna blush
    "At this, Anna's mood seems to change completely."
    "She cracks a smile, even showing hints of blushing a little."
    show anna happy
    anna.say "Oh..."
    anna.say "Oh that's okay then..."
    anna.say "When you say things like that, it makes me love you again!"
    anna.say "Even more, in fact!"
    show anna a normal
    with fade
    "Anna holds out a hand for me to take."
    "And together we walk off in search of whatever ride enthrals us first."
    "The only problem is that walking around the water-park is kind of hard for me."
    scene bg waterpark at dark, blur(5)
    show aletta a swimsuit at center, zoomAt(3.0, (2000, 1500))
    show aletta a swimsuit at center, traveling(3.0, 4.0, (-370, 1000))
    with fade
    "I mean, I'm no crazed perv, but the place is literally packed with dynamite bodies."
    "Everywhere I look there's a different example of female perfection."
    show bree b swimsuit at center, zoomAt(3.0, (-370, 1500))
    show bree b swimsuit at center, traveling(3.0, 4.0, (2000, 1000))
    "So many shapes and sizes, it's impossible to see the same thing twice."
    show lavish a swimsuit at center, zoomAt(3.0, (2000, 1500))
    show lavish a swimsuit at center, traveling(3.0, 6.0, (-640, 1000))
    "At first I'm afraid that Anna's going to rumble me and get angry."
    "But then I hear her chuckling at my side."
    scene bg waterpark
    show anna b swimsuit happy at center, zoomAt(1.5, (640, 1040))
    with hpunch
    anna.say "It's okay, [hero.name], you're only human."
    show anna evil
    anna.say "And I'll let you into a little secret too..."
    show fx exclamation
    anna.say "I like checking out the girls as well!"
    show anna normal
    "For a moment, Anna's admission leaves me feeling amazed."
    "But then I remember that she's into girls as well as guys."
    "Something that seems to be providing me with unexpected benefits!"
    "It's just about then that I spot a particular body that captures all of my attention."
    show anna at center, traveling (1.25, 0.3, (320, 900))
    show amy swimsuit at blacker, center, blur(16), zoomAt (1.25, (960, 900)) with easeinright
    "There's a set of curves that are almost as impressive as Anna's."
    "And the girl's a little taller too, meaning there's more of them."
    "But what really fascinates me is the fact that she's so pale."
    "I mean literally, the girl's skin is almost white!"
    "And when I see that her hair is also jet-black, I know she has to be a Goth!"
    mike.say "Wow..."
    mike.say "Check her out, Anna."
    mike.say "I don't think I've ever seen a Goth here before!"
    "Anna follows my gaze eagerly, keen to see what's got me interested."
    "And as soon as she sees the girl in question, she lets out a squeal of delight."
    show anna surprised
    anna.say "Ooh..."
    anna.say "A curvy Goth too!"
    anna.say "That's unusual, as most of them are super-skinny."
    anna.say "Well...or else they're really big girls!"
    anna.say "I guess what I'm trying to say is that there don't seem to be many medium-sized Goths!"
    show anna annoyed
    "Anna squints a little as she studies the girl."
    show amy at dark, blur(16), center, zoomAt (1.25, (960, 900)) with dissolve
    anna.say "Hmm..."
    anna.say "I'm usually pretty good when it comes to remembering asses."
    anna.say "And that one looks familiar..."
    anna.say "But I just can't place it!"
    show amy at dark, blur(8), center, zoomAt (1.25, (960, 900)) with dissolve
    "I keep nodding as the two of us unashamedly size up the girl in question."
    "Luckily she has her back turned to us at the moment."
    "So there's no way she can be aware of us watching her."
    mike.say "You know, I always thought they avoided direct sunlight."
    mike.say "Like they'd burst into flames or something?"
    show anna evil
    anna.say "Oh no, [hero.name]…"
    anna.say "You're thinking of vampires."
    anna.say "But it's pretty easy to get them mixed up with Goths!"
    show amy at dark, blur(1), center, zoomAt (1.25, (960, 900)) with dissolve
    "Suddenly the Goth girl begins to turn around."
    show anna normal at startle
    "This causes Anna and I to fall silent and try to act nonchalant."
    "Hoping that by doing so we can check out her face and not get caught in the act."
    show amy at brighter, blur(2), center, zoomAt (1.25, (960, 900)) with dissolve
    "But the moment that we see it, all of that goes straight out the window."
    show anna surprised
    "Because we both recognise her in the same moment."
    mike.say "Oh wow..."
    show amy at brighter with dissolve
    mike.say "It's Amy!"
    show anna angry
    show fx drop at left
    anna.say "Oh no..."
    anna.say "Now I remember where I've seen that ass before!"
    show anna annoyed
    "Neither of us is making any effort to keep our voices down."
    "Which helps to ensure that Amy notices us a second after we spot her."
    show amy b surprised
    show fx drop zorder 10 at right
    amy.say "Oh fuck..."
    show amy happy
    amy.say "Erm...hi, [hero.name]…"
    amy.say "Hi, Anna..."
    amy.say "Fancy seeing you here!"
    show amy sadsmile
    "Amy seems to be making an effort to be nice, no matter how strained it sounds."
    "But Anna actually stamps her foot on the ground as she frowns in Amy's direction."
    show anna angry
    anna.say "Well that's my day at the water-park ruined..."
    anna.say "Just like you tried to ruin our band!"
    show anna unpleased
    show amy b angry
    show fx anger at right
    amy.say "Oh for god's sake, Anna..."
    amy.say "Are we really going to do this here and now?"
    amy.say "Are you really not over it yet?"
    show amy annoyed
    if amy.flags.told_about_band:
        "I should have seen this coming the moment I recognised Amy."
        "She used to be in the Deathless Harpies, with Anna and the others."
        "But something soured between them, and it ended with her getting the boot."
        "So now the only thing I can do is step in and play peacemaker."
    else:
        "I watch as the two girls begin to square up to each other."
        "And while I'm pretty sure it won't come to a fight, I still feel myself tensing up."
        "But at the same time I really don't have a clue what Anna and Amy are talking about."
        "I know that Amy's a damn good guitar player."
        "And I remember her telling me she was in a band before things went sour."
        "Though what all of that has to do with Anna, I haven't a clue."
        mike.say "Wait..."
        mike.say "You two were in a band together?"
        mike.say "Like, before Anna was in the Deathless Harpies?"
        "My question seems to annoy both of them to an equal degree."
        "Because Anna and Amy turn to glare at me as one."
        show anna angry at startle
        anna.say "That was the Deathless Harpies, [hero.name]!"
        show amy angry at startle
        amy.say "Yeah, and you bitches kicked me out!"
        anna.say "Hey!"
        anna.say "That was a democratic decision, Amy!"
        amy.say "Democracy my ass!"
        show anna annoyed
        show amy annoyed
    "Anna and Amy aren't the tallest pair of girls."
    "And the sight of them squaring up to each other's hardly scary."
    "In fact it might have looked comical in another place or time."
    "But right now I don't want to see a fight between two shorties."
    "Especially in the middle of a crowded water-park."
    "So I do the best I can to step in and separate them."
    mike.say "Okay, okay..."
    mike.say "I get that you two have history."
    mike.say "But do you really want to thrash it out here and now?"
    show anna b normal
    show amy normal
    "This seems to be enough to get through to Anna and Amy."
    "If I'd been dealing with Kleio or Sasha, then things might have been different."
    "But Anna's not as naturally aggressive or confrontational as her bandmates."
    "And I'm relieved to see that the same appears to be true of Amy."
    anna.say "Oops..."
    anna.say "Maybe you're right, [hero.name]."
    anna.say "But that doesn't mean I'm not still mad with you!"
    "Anna wags a finger at Amy, then turns her back on the other girl."
    show anna a
    show amy shy
    amy.say "You're probably right, [hero.name]."
    amy.say "Best we just avoid each other, yeah?"
    "I nod and smile at Amy."
    "Hoping she sees the gratitude in my expression."
    hide amy with easeoutright
    show anna a at center, traveling (1.1, 0.3, (120, 820))
    "But then I hear Anna shouting for me."
    show anna b happy at startle
    anna.say "[hero.name]!"
    anna.say "Stop talking to that pasty bitch..."
    anna.say "And get your peachy butt over here, right now!"
    show anna normal
    mike.say "Ah..."
    mike.say "Sorry, Anna..."
    mike.say "Right away, Anna!"
    "I spin on my heel and hurry after Anna."
    "But as I do so, I can hear Amy chuckling to herself."
    "And I can also feel my cheeks flushing form the embarrassment too."
    return

label band_harem_amy_event_04:
    scene bg waterpark
    with fade
    "It's a pretty good day to be at the water park."
    "The sun is shining in the middle of a cloudless, blue sky."
    "The park has a buzz about it from being busy, but not too busy."
    show anna b normal swimsuit at center, zoomAt (1.25, (320, 900)) with easeinleft
    "And a quick glance around shows me Anna hurry over to my side."
    "Which is a sight that's always sure to put a smile on my face."
    "Especially when she's poured herself into her swimming costume!"
    show anna b happy swimsuit at center, zoomAt (1.25, (640, 900)) with ease
    anna.say "Phew..."
    anna.say "Sorry to take so long getting changed, [hero.name]."
    show anna b talkative
    anna.say "But here I am, all ready to have some soggy fun!"
    show anna b unpleased
    "As soon as the words are out of her mouth, Anna frowns."
    show anna b worried
    anna.say "Oh no..."
    anna.say "That just doesn't sound right, does it?"
    show anna b talkative
    anna.say "Damp fun?"
    anna.say "Moist fun?"
    anna.say "Dripping fun?"
    show anna b embarrassed
    anna.say "Is there any way of saying it that doesn't sound wrong?"
    show anna b unpleased
    "I can't help chuckling at the serious expression on Anna's face."
    mike.say "I don't know, Anna..."
    show anna normal
    mike.say "You're slippery when wet."
    mike.say "And that usually makes you a lot of fun!"
    show anna b happy
    "This seems to cheer Anna up a great deal."
    show anna b at center, traveling (1.5, 0.3, (640, 1040))
    "She takes hold of my hand and makes to lead me out into the park."
    show anna_standing_fg_stage zorder 3
    show anna a zorder 1 at dark
    with fade
    "But the problem is that the sun hits us in the eyes as walk out there."
    "Which means that we can't see the faces of anyone around us."
    show anna a stuned at center, traveling (1.25, 0.3, (320, 900))
    show amy b happy swimsuit zorder 2 at center, zoomAt (1.25, (960, 900)), dark with easeinright
    amy.say "[hero.name]?"
    amy.say "Is that you?"
    amy.say "I think this is the place you said we should meet up."
    show amy b normal
    "I recognise the sound of Amy's voice the second that I hear it."
    "But the plan that I'd cooked up for this moment is now ruined."
    "Not least because Anna seems to have recognised Amy's voice too!"
    show amy b annoyed
    show anna b angry
    anna.say "Are you kidding me?"
    anna.say "This is like deja vu, all over again!"
    anna.say "What's she doing here?!?"
    scene bg waterpark at litedark
    show anna b annoyed swimsuit at center, zoomAt (1.25, (320, 900))
    show amy b annoyed swimsuit at center, zoomAt (1.25, (960, 900))
    with dissolve
    "Of course the sun chooses that exact moment to hide itself."
    "It disappears behind the first cloud I've seen all day."
    "And just like that, Anna, Amy and I can all see each other."
    show amy angry at startle
    amy.say "I'm here because [hero.name] invited me!"
    amy.say "What I want to know is why you're here too?"
    show amy annoyed
    show anna angry at startle
    anna.say "The same reason as you."
    anna.say "He invited me as well."
    show anna annoyed
    show amy angry at startle
    amy.say "Oh, did he now?"
    show amy b mad
    show anna angry at startle
    anna.say "Oh yeah, he did!"
    show anna b unpleased
    "It only takes a few seconds for the inevitable to happen."
    show anna b at center, zoomAt (1.25, (340, 900))
    show amy b at center, zoomAt (1.25, (940, 900))
    with ease
    "For Anna and Amy's attention to turn away from each other."
    "And for it to fall squarely on me instead."
    "Now instead of one puzzled and angry girl on my case, I have two."
    mike.say "Now just wait a minute, guys..."
    mike.say "There's a perfectly rational explanation for all of this."
    mike.say "But if you kill me, then you'll never get to hear it!"
    show amy annoyed
    show anna b annoyed
    "This seems to work, as Anna and Amy relax just a little."
    "Not a lot, but just enough to give me the space I need."
    mike.say "Okay, it's like this..."
    mike.say "The last time we were all here, I figured out two things."
    mike.say "One was that you have a lot of stuff you need to work out."
    mike.say "And the other is that you both really like the water park."
    mike.say "So what better idea could there be than to invite you here together?"
    mike.say "Where you can work on your issues and have fun at the same time!"
    "I feel like a hopeless salesman."
    "Desperately making the pitch he needs to save his career."
    show anna b worried
    anna.say "Ooh..."
    anna.say "I was so looking forward to a date with you at the water park."
    show anna b angry
    anna.say "But now you've gone and turned it into some kind of weird therapy session!"
    show anna b sadsmile
    show amy angry
    amy.say "Can't say that I'm crazy about the idea either, [hero.name]."
    show amy lying
    amy.say "But I'll stay and give it a try - so long as you're here."
    show amy shy
    "There's no way I can fail to pick up on the look Amy just gave me."
    "And I'd be lying if I tried to claim that I wasn't thrilled by it too."
    "But the only problem is Anna seems to have noticed it as well."
    show amy sadsmile
    show anna b angry
    anna.say "I saw that, Amy..."
    show anna b at startle
    anna.say "I know when someone's flirting with my man!"
    anna.say "And I'm not leaving him alone with you, not for a second!"
    show anna b annoyed
    "All I can do is shrug and be thankful for the unexpected turn of events."
    show anna b normal
    show amy normal
    mike.say "Okay then..."
    mike.say "Looks like we're all staying for the date."
    mike.say "Oh, and the chance to build some bridges."
    show bg waterpark at brighter with dissolve
    "This last addition earns me a glares from Anna and Amy alike."
    "So I take a deep breath and try to steel myself for what lies ahead."
    "Because I get the feeling this is going to take a lot out of me."
    "It doesn't take Anna long to regain some of her previous enthusiasm."
    "And before anyone else can speak up, she's already striding off with her head held high."
    show anna evil
    anna.say "If we're going to stay here, then I'm going to have some fun."
    anna.say "You guys can come to the water-slide with me, or not."
    anna.say "Your choice."
    show anna normal
    "Amy and I exchange a helpless look and a shrug."
    "Then we fall in behind Anna, following her to the water-slide."
    with fade
    "But as soon as we get there, Amy's cooperation stops dead."
    show amy happy
    amy.say "We're all going on the top slide, right?"
    amy.say "That's the fastest, so it's obviously the best."
    amy.say "Am I right?"
    show amy normal
    show anna surprised
    "I can see that Anna's looking more than a little intimidated."
    "She's gazing up at the top slide, eyes wide with trepidation."
    show anna annoyed
    anna.say "Erm..."
    show anna talkative
    anna.say "Speed isn't everything, Amy."
    anna.say "The bottom slide is longer, and it has more loops in it too."
    show anna normal
    "It's pretty clear that neither one of the girls is going to convince the other."
    "So obviously the next thing they do is turn to me."
    show anna talkative at startle
    anna.say "Tell her, [hero.name]…"
    anna.say "We should go on the bottom slide."
    show anna annoyed
    show amy whining at startle
    amy.say "She's talking crap, [hero.name]."
    amy.say "The top slide is the one we want."
    show amy annoyed
    $ renpy.dynamic(amy_score=0, anna_score=0)
    menu:
        "Go the top slide":
            "Anna might have a point about the length of the bottom slide."
            "But I keep on looking up at the top slide, and I can't help it."
            "I'm even getting a thrill from just standing here looking at the thing!"
            mike.say "Maybe we can do the bottom slide next, Anna?"
            mike.say "But I do want to go on the top one first."
            mike.say "It just look so much more fun!"
            show amy happy at startle
            "Amy's quick to jump on my enthusiasm."
            "And she makes straight for the top slide, grabbing my hand for good measure."
            amy.say "You know it makes sense, [hero.name]..."
            amy.say "And just wait until you see the view from up there."
            amy.say "It's crazily high!"
            show amy normal
            show anna unpleased
            "I'm eager to get up there as soon as possible."
            "So much so that I ignore the look on Anna's face."
            "Which is one of growing fear and concern."
            show anna worried
            anna.say "Do we really have to?"
            anna.say "I feel dizzy just looking at it!"
            show anna sad
            mike.say "Don't worry, Anna..."
            mike.say "It's going to be totally fine."
            "But when we make it to the top, Anna's not convinced."
            show anna surprised
            anna.say "Oh no..."
            anna.say "No, no, no..."
            show anna worried at stepback
            anna.say "I want to go back down!"
            show anna sad
            mike.say "Erm..."
            mike.say "I don't think we can do that, Anna."
            mike.say "There's kind of a big queue behind us."
            show amy happy
            amy.say "Don't worry, guys..."
            amy.say "I have a plan!"
            show amy at backforth(0.5, -200, 0)
            pause 0.3
            show anna stuned at startle
            "Before anyone else can say a thing, Amy steps forward and shoves Anna."
            play sound woosh_punch
            hide anna with moveoutbottom
            "This catches her totally by surprise, sending her down the slide."
            "I grimace as I stand there, listening to Anna scream all the way down."
            show anna b cry swimsuit at center, zoomAt (1.25, (320, 900))
            with fade
            "And when we all get to the bottom, she's standing in the water."
            "Anna looks to be in one piece, but she's pale and shaking."
            "So maybe that wasn't the best decision I could have made."
            $ amy_score += 1
            $ anna_score -= 1
        "Go the bottom slide":
            "Amy might have a point about the height of the top slide."
            "But I keep on looking up at the bottom slide, and I can't help it."
            "I'm even getting a thrill from just standing here looking at the thing!"
            mike.say "Maybe we can do the top slide next, Amy?"
            mike.say "But I do want to go on the bottom one first."
            mike.say "It just look so much more fun!"
            show anna happy at startle
            "Anna's quick to jump on my enthusiasm."
            "And she makes straight for the top slide, grabbing my hand for good measure."
            anna.say "You know it makes sense, [hero.name]..."
            anna.say "And just wait until you see the twists and turns."
            anna.say "It's like a roller-coaster!"
            show anna normal
            "I'm eager to get over there as soon as possible."
            "So much so that I ignore the look on Amy's face."
            "Which is one of growing fear and concern."
            show amy annoyed
            amy.say "Do we really have to?"
            amy.say "I don't do well with being tossed around!"
            mike.say "Don't worry, Amy..."
            mike.say "It's going to be totally fine."
            "But when we make it over there, Amy's not convinced."
            show amy surprised
            amy.say "Oh no..."
            amy.say "No, no, no..."
            show anna happy
            anna.say "I want to out!"
            show amy annoyed
            mike.say "Erm..."
            mike.say "I don't think we can do that, Amy."
            mike.say "There's kind of a big queue behind us."
            anna.say "Don't worry, guys..."
            anna.say "I have a plan!"
            show anna at backforth(0.5, 200, 0)
            pause 0.3
            show amy surprised at startle
            "Before anyone else can say a thing, Anna steps forward and shoves Amy."
            play sound woosh_punch
            hide amy with moveoutbottom
            "This catches her totally by surprise, sending her down the slide."
            "I grimace as I stand there, listening to Amy scream all the way down."
            show amy b sad swimsuit at center, zoomAt (1.25, (960, 900))
            with fade
            "And when we all get to the bottom, she's standing up in the water."
            "Amy looks to be in one piece, but she's pale and shaking."
            "Well, you know, paler than usual..."
            "So maybe that wasn't the best decision I could have made."
            $ anna_score += 1
            $ amy_score -= 1
        "Choose both" if hero.charm >= 60:
            "This is one of those times when I can't help feeling the girls are missing the point."
            "Like both of them have total target-fixation and can't see the bigger picture."
            mike.say "What's the deal with arguing over it?"
            mike.say "It's not like we can only go on the slides once."
            mike.say "Let's do one and then the other."
            show anna normal
            show amy normal
            "To me it sounds like the simplest suggestion in the world."
            "But Anna and Amy look almost gobsmacked."
            show anna surprised
            anna.say "Well..."
            anna.say "I suppose so."
            show amy surprised
            amy.say "You do have a point."
            show anna normal
            show amy normal
            "I nod and then turn my back to begin walking towards the slides."
            with fade
            "Because I plan to capitalise on my success by not letting them dwell on things."
            "And just as I expected, Anna and Amy are soon following, close on my heels."
            "Unfortunately there's no way I can avoid choosing which slide we do first."
            "So I just choose the top one and hope that the girls can keep on being mature."
            "Luckily for me, the gamble seems to pay off."
            "Though Anna doesn't look too happy."
            show anna surprised
            anna.say "No, no, no..."
            anna.say "I want to go back down!"
            mike.say "Erm..."
            mike.say "I don't think we can do that, Anna."
            mike.say "There's kind of a big queue behind us."
            show amy happy
            amy.say "Don't worry, guys..."
            amy.say "I have a plan!"
            amy.say "Just keep your eyes on your feet, Anna."
            amy.say "That always helps me."
            show amy normal
            show anna normal at startle
            "Anna nods and finally gets on the slide."
            "And when we see her at the bottom, she looks fine."
            show anna happy
            anna.say "Thanks, Amy..."
            anna.say "That really worked!"
            show anna normal
            "Next we hurry over to the bottom slide."
            "But this time it's Amy's turn to look nervous."
            amy.say "Do we really have to?"
            amy.say "I don't do well with being tossed around!"
            mike.say "Don't worry, Amy..."
            mike.say "It's going to be totally fine."
            show amy surprised
            amy.say "Oh no..."
            amy.say "No, no, no..."
            anna.say "I want to out!"
            mike.say "Erm..."
            mike.say "I don't think we can do that, Amy."
            mike.say "There's kind of a big queue behind us."
            anna.say "Don't worry, Amy..."
            anna.say "You helped me, now I want to do the same for you."
            show amy annoyed
            anna.say "Just close your eyes and think happy thoughts!"
            "Amy doesn't look convinced, but she nods and gets into position anyway."
            show amy normal at startle
            with fade
            "And when we all make it to the bottom, she looks fine too."
            "Plus I feel relieved to have seen that the two of them can actually coexist."
            $ anna_score += 1
            $ amy_score += 1
    show anna normal
    show amy normal
    "After we've been on the slides, I feel the need to do some actual swimming."
    "So I head over to one of the deeper pools and lower myself into the water."
    "Anna hurries over to the side of the pool, looking concerned."
    show anna annoyed
    anna.say "Are you sure that's a good idea, [hero.name]?"
    anna.say "That water looks very deep!"
    "Amy hears what's being said and walks over too."
    show anna happy
    amy.say "What's the problem, Anna?"
    amy.say "The water here's not that deep!"
    "I watch in amazement as the two of them begin to squabble once more."
    "This time seeming to argue over which of them is more concerned for my safety."
    "And I'm amazed that they seem to be able to do this on almost any situation they encounter."
    "But then I do get the feeling that I need to do something about it."
    "It's about that time that I realise Anna and Amy are totally distracted."
    show anna normal
    show amy normal
    "So I could totally pull one of them into the water..."
    menu:
        "Pull Anna into the water":
            "I know that I'll probably regret this."
            "But now the idea's lodged in my head, I can't back out of it."
            "So I reach out and take hold of Anna, then I pull her into the water."
            play sound woosh_punch
            show anna surprised
            anna.say "Waah..."
            show anna at stepback(0.2, 20, -20)
            anna.say "What are you..."
            show anna at startle
            anna.say "I'm going to drown!"
            play sound water_splash
            "Anna thrashes about in the water, crying and wailing."
            "But there's no way her fears can come true."
            "Because I have a firm hold on her the whole time."
            "Eventually she calms down and stops making such a racket."
            show anna annoyed
            "But she's still frowning and giving me dirty looks."
            anna.say "That was so not funny!"
            anna.say "I could have gone under and never come back up!"
            show amy happy
            amy.say "Oh get over it, Anna..."
            amy.say "He had hold of you the whole time."
            $ anna_score -= 1
            $ amy_score += 1
        "Pull Amy into the water":
            "I know that I'll probably regret this."
            "But now the idea's lodged in my head, I can't back out of it."
            "So I reach out and take hold of Amy's, then I pull her into the water."
            play sound woosh_punch
            show amy surprised
            amy.say "Whoa..."
            show amy at stepback(0.2, -20, -20)
            amy.say "What are you..."
            show amy at startle
            amy.say "How dare you..."
            play sound water_splash
            "Amy thrashes about in the water, crying and wailing."
            "But there's no way anything bad can happen to her."
            "Because I have a firm hold on her the whole time."
            "Eventually she calms down and stops making such a racket."
            show amy annoyed
            "But she's still frowning and giving me dirty looks."
            amy.say "That was so not funny!"
            amy.say "I could have gone under and never come back up!"
            show anna happy
            anna.say "You totally deserved that, Amy..."
            anna.say "And it'll teach you to be so mean to me in future too!"
            $ anna_score += 1
            $ amy_score -= 1
        "Pull both into the water" if hero.fitness >= 60:
            "I know that I'll probably regret this."
            "But now the idea's lodged in my head, I can't back out of it."
            "So I reach out and take hold of Anna and Amy."
            "Then I pull them both into the water."
            play sound woosh_punch
            show anna surprised
            pause 0.1
            play sound woosh_punch
            show amy surprised
            amy.say "Whoa..."
            anna.say "Waah..."
            show amy at stepback(0.2, -20, -20)
            pause 0.1
            show anna at stepback(0.2, 20, -20)
            anna.say "What ..."
            amy.say "... are you..."
            show anna at startle
            pause 0.1
            show amy at startle
            anna.say "I'm going to drown!"
            amy.say "How dare you..."
            play sound water_splash
            queue sound water_splash
            "Anna and Amy about in the water, crying and wailing."
            "But there's no way anything bad can happen to them."
            "Because I have a firm hold on them the whole time."
            "Eventually they calm down and stops making such a racket."
            "But they're still frowning and giving me dirty looks."
            show anna annoyed
            anna.say "He's a rotten bastard, Amy!"
            show amy annoyed
            amy.say "Yeah, Anna, a total asshole!"
            show anna angry
            anna.say "Let's get him!"
            show amy angry
            "As one, Anna and Amy leap at me."
            "They splash me, pull me this way and that, even push my head underwater."
            show anna happy
            show amy happy
            "But as I surface, gagging and coughing, I can hear them laughing together."
            "And before too long, we're all splashing around in the water."
            "Any hint of conflict seemingly forgotten."
            $ anna_score += 1
            $ amy_score += 1
    "By now I'm beginning to feel like the atmosphere's pretty good between the three of us."
    show anna normal
    show amy normal
    "Anna, Amy and I have been getting on well-enough for me to think we're making real progress."
    "So as we sit on the edge of the pool, I decide to pump them for more details about the past."
    "Because I'm more than a little curious about how someone as sweet and fun as Anna can be so bitter."
    "It just doesn't feel like the Anna I know and love."
    mike.say "So..."
    mike.say "About when you guys were all in the band together?"
    mike.say "Like, what actually happened back then?"
    mike.say "What made it all go sour?"
    if amy_score >= 2 and anna_score >= 2:
        show anna happy
        anna.say "Oh, that's no great mystery, [hero.name]…"
        anna.say "Amy and I fucked, and that ruined the whole band!"
        show amy surprised at startle
        "As soon as the words are out of Anna's mouth, Amy starts shaking her head."
        amy.say "That's totally not why it happened!"
        show amy annoyed
        amy.say "It's pretty simple, [hero.name]…"
        amy.say "I left because of Sasha and Kleio's shitty attitudes!"
        show anna blush
        "Now it's Anna's turn to look shocked and shake her head."
        anna.say "But, Amy..."
        anna.say "That's not what Sasha and Kleio told me!"
        show amy angry
        amy.say "Well of course not, Anna."
        amy.say "I bet they wanted to make me look like the bad guy!"
        show amy annoyed
        show anna surprised
        anna.say "Ooh..."
        anna.say "I'm so mad at those two right now!"
        "I'm more than a little fascinated myself."
        "And I'd love to know more about what happened between Anna and Amy."
        "But that'll have to wait for another time."
        "As they seem to be comparing notes on the whole thing."
        "And I think they're also discovering nothing's a simple as it seemed at the time."
    elif anna_score > 1:
        show anna happy
        anna.say "Oh, that's no great mystery, [hero.name]…"
        anna.say "Amy and I fucked, and that ruined the whole band!"
        show amy surprised at startle
        "As soon as the words are out of Anna's mouth, Amy turns on her."
        "It happens so fast that Anna's totally taken by surprise."
        amy.say "What did you just say?!?"
        amy.say "That's totally not why it happened!"
        show amy normal
        amy.say "Sure, we had an encounter of a sexual nature."
        show amy angry
        amy.say "But I left because of Sasha and Kleio's shitty attitudes!"
        show amy annoyed
        show anna surprised
        "Anna stares at Amy in stunned amazement."
        anna.say "But, but, but..."
        anna.say "That's not what they told me!"
        amy.say "Geez, Anna..."
        amy.say "You are so fucking naïve!"
    elif amy_score > 1:
        amy.say "It's pretty simple, [hero.name]…"
        show amy angry
        amy.say "I left because of Sasha and Kleio's shitty attitudes!"
        show amy annoyed
        show anna surprised
        "As soon as the words are out of Amy's mouth, Anna turns on her."
        "It happens so fast that Amy's taken totally by surprise."
        anna.say "What did you just say?!?"
        anna.say "That's totally not why you left!"
        anna.say "It was because of you fucking me and then dropping me like a bad habit."
        anna.say "And for the record, Amy, you didn't leave - you were kicked out!"
        show amy surprised at startle
        "Amy stares at Anna in stunned amazement."
        amy.say "Is that what they told you?"
        show amy annoyed
        amy.say "Geez, Anna..."
        amy.say "You are so fucking naïve!"
    else:
        show anna annoyed
        anna.say "Yeah..."
        anna.say "I'm not going there today!"
        show amy annoyed
        amy.say "Nice try, [hero.name]…"
        amy.say "But I'm not digging it all up either!"
        "I don't need to be told that they're serious."
        "I can tell as much from the tone of their voices."
        "So I resolve to leave it alone for now."
        "But maybe I can try another time."
        "Perhaps when they're both in a better place."
    show anna normal
    show amy normal
    with fade
    "By now our time at the water-park feels like it's coming to a natural end."
    "So we head back towards the dressing rooms and the lockers where we stowed our stuff."
    "But just before I leave the girls to go into the guy's changing rooms, I feel like I have to ask them something."
    mike.say "So did we all get something out of today?"
    mike.say "Did we tear down some walls and build some bridges?"
    if amy_score >= 2 and anna_score >= 2:
        show anna happy
        anna.say "Sure, [hero.name]…"
        anna.say "I had a great time!"
        show amy happy
        amy.say "I hate to admit it, [hero.name]…"
        amy.say "But this was actually pretty fun!"
        "I feel a sense of relief flood over me."
        "But then I notice that Anna and Amy are still staring at me."
        mike.say "Erm..."
        mike.say "Why are you looking at me like that?"
        show anna b swimsuit at center, zoomAt (1.25, (420, 900))
        show amy b swimsuit at center, zoomAt (1.25, (860, 900))
        with ease
        "By now, Anna and Amy are also leaning in close."
        "And I can see they're whispering to each other too!"
        "But they don't explain themselves to me."
        hide anna
        hide amy
        with easeoutleft
        "Instead they disappear into the women's changing rooms."
        "Still looking at me over their shoulders as they go."
        call amy_anna_waterpark_threesome from _call_amy_anna_waterpark_threesome
        $ amy.flags.peace_with_anna = True
    elif anna_score > 1:
        show anna happy
        anna.say "Sure, [hero.name]…"
        anna.say "I had a great time!"
        show amy annoyed
        amy.say "Speak for yourself."
        amy.say "I'd rather pull out my own teeth with rusty pliers than do this again!"
        hide amy with easeoutleft
        "Anna and I watch as Amy storms off into the women's changing rooms."
        "Which leaves me wondering what in the hell I did wrong."
    elif amy_score > 1:
        show amy happy
        amy.say "I hate to admit it, [hero.name]…"
        amy.say "But this was actually pretty fun!"
        show anna annoyed
        anna.say "Was it hell fun!"
        anna.say "I never want to do this with her again!"
        hide anna with easeoutleft
        "Amy and I watch as Anna storms off into the women's changing rooms."
        "Which leaves me wondering what in the hell I did wrong."
        $ amy.flags.possible_peace_with_anna = True
    else:
        show anna annoyed
        anna.say "I never want to do this with her again!"
        show amy annoyed
        amy.say "I'd rather pull out my own teeth with rusty pliers!"
        hide anna
        hide amy
        with easeoutleft
        "Both Anna and Amy storm off into the women's changing rooms."
        "Which leaves me alone and wondering what in the hell I did wrong."
    return

label amy_anna_waterpark_threesome:
    scene bg black
    show minami_showersex_bg at center, zoomAt(1.25, (640, 900)) with fade
    play sound shower loop
    "I'm still puzzling over the way that Anna and Amy were looking at me as I walk into the showers."
    "And kind of hoping that it might be that they're cooking up a special surprise for me in the future."
    "But it doesn't take long for the feel of the showers to pull my thoughts away from such things."
    "As I step under the nearest showerhead, the enveloping heat and the cascading water overcome my senses."
    "All notion of contemplating what might or might not be seems to become a pointless waste of time."
    "Because there's so much more pleasure to be gained from switching off and enjoying my shower instead."
    "It doesn't take me long to lather-up my body, and then I start to wash my hair."
    "Which is obviously one of my best features, so it requires far more care and attention."
    "As the water washes everything away, I feel like it's carrying off my worries at the same time."
    "I feel more relaxed than I can remember feeling for a long time."
    "And without realising it, I start humming away to myself."
    "But once I have my eyes closed, and I'm letting the water fall on my face, I go one step further."
    "Because I actually start to sing!"
    show chibi shower with dissolve
    mike.say "I'm a Barbie Girl..."
    mike.say "In a Barbie world..."
    mike.say "Life in plastic..."
    mike.say "It's fantastic..."
    "For a moment I think that I hear the sound of the door opening behind me."
    hide chibi shower with dissolve
    "That's more than enough to make me stop singing and try to act natural."
    "Because the last thing I want is for some random guy to hear me crooning away in the shower!"
    "But much to my surprise, I don't see or hear anything more after that."
    "Well, there is one thing, which kind of sounds like someone giggling."
    "But that could have been anything, so I just choose to think it's my imagination."
    "And I get right back to my shower."
    show chibi shower with dissolve
    mike.say "You can cut my hair..."
    mike.say "Undress me everywhere..."
    mike.say "I'm a relation..."
    mike.say "To Frankenstein's creation..."
    mike.say "I'm a...urgh..."
    hide chibi shower
    with vpunch
    "Suddenly I feel a hand covering my mouth."
    "And my eyes pop open, expecting to see the face of the man that's going to kill me."
    show anna b naked at center, zoomAt (1.5, (860, 1040))
    show amy b naked at center, zoomAt (1.5, (420, 1040))
    with easeinleft
    "But instead, I find myself looking down at Anna and Amy!"
    "And I'm almost more shocked to see that they're naked than that they've snuck up on me."
    mike.say "B..."
    mike.say "B...b...b..."
    mike.say "Boobies!"
    show amy annoyed blush
    show anna happy
    "Anna and Amy exchange a mischievous glance and an equally impish giggle."
    show anna evil
    anna.say "Well, there's nothing wrong with his eyes."
    show anna normal
    show amy lying
    amy.say "No, it's just his voice that's fucked!"
    show amy normal
    show anna evil
    anna.say "And now that you mentioned that word..."
    show anna normal
    show amy happy
    amy.say "Oh yeah - that's what we came here for, isn't it?"
    show amy normal
    "By now I've managed to regain enough of my composure to formulate a coherent response."
    "And much as I like what I see before me, I can't escape the fact of where we are right now."
    mike.say "Guys..."
    mike.say "What are you playing at?!?"
    mike.say "This is the guy's showers!"
    mike.say "You can't be in here..."
    mike.say "And you definitely can't be naked!"
    show anna b happy
    show amy b flirt
    "For all of the pleading I'm doing, Anna and Amy don't seem to give a damn."
    "Because all they do is shake their heads and giggle all the more."
    show anna b at center, traveling (1.75, 0.3, (880, 1140))
    show amy b at center, traveling (1.75, 0.3, (400, 1140))
    "They also advance on me as they do so, flanking me on either side."
    "It doesn't take long for them to push me on the floor."
    "And as soon as that happens, they pounce on me like wild dogs."
    "Well...if wild dogs were horny and had astonishing breasts!"
    scene bg black
    show band foreplay amyanna bathroom shower aneyes_ahegao with fade
    anna.say "Don't worry, [hero.name]…"
    anna.say "We'll make it quick."
    show band foreplay amyanna bathroom ameyes_ahegao
    amy.say "We just want to thank you for getting us talking."
    amy.say "What you did today was really nice."
    anna.say "Now we're going to do something nice for you!"
    amy.say "Something very nice indeed!"
    mike.say "Ah..."
    mike.say "What is it?"
    mike.say "What are you going to do?"
    anna.say "Let you choose, of course!"
    amy.say "Choose which one of us you want to fuck!"
    "Suddenly I can feel all of my former reservations disappear."
    "Sure, I'm still terrified of someone walking in on us any moment."
    "But now that fear is being infused with a serious amount of arousal."
    "Because being discovered fucking one of these two little hotties..."
    "Well, that's a totally different prospect!"
    show band foreplay amyanna bathroom aneyes_closed ameyes_closed amy_blush anna_blush
    "Anna and Amy seem to sense the change in my mood."
    "They use it as an excuse to come closer still, and then to press themselves against me."
    "All at once, I have two warm, wet bodies slithering over mine."
    "And it's in that moment I realise the real challenge is going to be picking between them!"
    menu:
        "Fuck Anna":
            "I know that we just made great strides in bringing Amy back into the fold."
            "But I'm not sure that goes as far as granting me the permission to fuck her!"
            show band foreplay amyanna back
            pause 0.2
            show band foreplay amyanna front
            "Even if Anna just said I could choose between the two of them."
            "That still feels like one of those loaded statements girls like to make."
            show band foreplay amyanna back
            pause 0.2
            show band foreplay amyanna front
            "You know, like she says it's up to me..."
            "But I'll still get judged for choosing the other girl over her?"
            show band foreplay amyanna back
            pause 0.2
            show band foreplay amyanna front
            "Of course the massive upside to this paranoia is that fucking Anna's hardly a chore!"
            mike.say "Mmm..."
            mike.say "I think I'm going to choose..."
            mike.say "YOU!"
            scene bg black
            show band threesome amyanna fuckanna bathroom
            with fade
            "I say this as I sweep around and pull Anna into my embrace."
            "She squeals with genuine surprise and alarm at first."
            "But as soon as I pull her closer to me, all of that changes."
            "At first her squeals become sounds of anticipation."
            "And once I start kissing her, the turn into moans of delight."
            "The weird thing is that Anna and Amy were the ones that initiated this thing."
            "But as soon as I have a firm hold on her, Anna's like putty in my hands."
            "She offers no resistance as I press her against my shaft."
            "Simply pushing her butt backwards into me, almost nodding in total surrender."
            "It occurs to me in the space of the very next moment that I never checked if I was ready."
            "I just got straight down to the act of lining Anna up and assumed that I'd be ready when I was done."
            "But as soon as I lean in to get on with things, all of my questions in that area are answered."
            show band threesome amyanna fuckanna anna_pleasure
            "And that's because I feel the tip of my cock touch Anna's buttocks."
            "Or to me more specific, they touch them a good number of inches before my thighs can!"
            "All I have the time to do is chuckle to myself."
            show band threesome amyanna fuckanna anna_normal
            "Well, that and enjoy the way Anna jumps and looks pleased by the sensation."
            "But that's all the warning that she's going to get."
            "Because a moment later I push forwards for all I'm worth."
            "Anna lets out another squeal and begins to squirm in my arms."
            "And that's because my cock is right on target."
            show band threesome amyanna fuckanna anna_pleasure vaginal
            "I feel it sliding over the lips of her pussy for a few mere seconds."
            "Then it begins to sink inside of her without anything to oppose it."
            "The combination of water, heat and Anna's flustered state all work in my favour."
            show band threesome amyanna fuckanna anna_normal
            "And I take full advantage too, pushing into her until I can go no deeper."
            "But I don't stop to enjoy the sensation, because I'm still aware of just where we are right now."
            show band threesome amyanna fuckanna bouncing1 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna bouncing2 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna still
            "Instead I begin to pound away on Anna without any effort to build up slowly."
            "Suddenly she goes from anticipating what's to come to getting fucked for all she's worth!"
            show band threesome amyanna fuckanna bouncing1 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna bouncing2 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna still
            "That's not to say Anna can't handle what I'm giving her."
            "Every thrust gets swallowed up by her sturdy little frame."
            show band threesome amyanna fuckanna anna_pleasure bouncing1 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna bouncing2 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna still
            "And when I catch a glimpse of her face, she's always nodding like she wants more."
            "In my eagerness to get hold of Anna, I'd almost forgotten we're not alone."
            show band threesome amyanna fuckanna bouncing1 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna bouncing2 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna still
            "So when I glance the other way and see Amy, I feel a sense of surprise."
            "Even more so when I see that she's not standing still either."
            show band threesome amyanna fuckanna bouncing1 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna bouncing2 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna still
            "Instead she's leaning over me, her massive chest almost surrounding me."
            "But what really captures my attention is what she's doing with her left hand."
            show band threesome amyanna fuckanna amy_pleasure bouncing1 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna bouncing2 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna still
            "It's down by her waist, desperately stroking her pussy!"
            "I doubt that I could have kept this up for much longer with Anna alone."
            show band threesome amyanna fuckanna bouncing1 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna bouncing2 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna still
            "But now that I'm watching Amy pleasure herself too, I simply can't hold on."
            show band threesome amyanna fuckanna anna_ahegao bouncing1 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna bouncing2 at startle(0.05,-10)
            pause 0.2
            show band threesome amyanna fuckanna still with vpunch
            "With one last thrust, I push all the way into Anna."
            show band threesome amyanna fuckanna anna_ahegao creampie with vpunch
            "And in the next breath I lose it, shooting my load deep inside of her."
            $ anna.sexperience += 1
            $ anna.love += 4
            $ amy.love += 4
        "Fucks Amy":
            "I know that we just made great strides in bringing Amy back into the fold."
            show band foreplay amyanna back
            pause 0.2
            show band foreplay amyanna front
            "And I'm pretty sure that grants me the permission to fuck her!"
            "After all, Anna just said I could choose between the two of them."
            show band foreplay amyanna back
            pause 0.2
            show band foreplay amyanna front
            "So who am I to turn down an offer as good as that?"
            mike.say "Mmm..."
            mike.say "I think I'm going to choose..."
            mike.say "YOU!"
            scene bg black
            show band threesome amyanna fuckamy bathroom
            with fade
            "I say this as I sweep around and push Amy into Anna's embrace."
            "They both squeal with genuine surprise and alarm at first."
            "But as soon as I pull Amy closer to me, all of that changes."
            show band threesome amyanna fuckamy onmike
            "At first her squeals become sounds of anticipation."
            "The weird thing is that Anna and Amy were the ones that initiated this thing."
            "But as soon as I have a firm hold on her, Amy's like putty in my hands."
            "She offers no resistance as press her against me."
            "Simply pushing her butt backwards into me, almost nodding in total surrender."
            "It occurs to me in the space of the very next moment that I never checked if I was ready."
            "I just got straight down to the act of lining Amy up and assumed that I'd be ready when I was done."
            "But as soon as I lean in to get on with things, all of my questions in that area are answered."
            show band threesome amyanna fuckamy pleasure
            "And that's because I feel the tip of my cock touch Amy's buttocks."
            "Or to me more specific, they touch them a good number of inches before my thighs can!"
            "All I have the time to do is chuckle to myself."
            show band threesome amyanna fuckamy onmike
            "Well, that and enjoy the way Amy jumps and looks back over her shoulder at the sensation."
            "But that's all the warning that she's going to get."
            "Because a moment later I push forwards for all I'm worth."
            "Amy lets out another squeal and begins to squirm under me."
            "And that's because my cock is right on target."
            show band threesome amyanna fuckamy pleasure vaginal at stepback(speed=0.1, h=-10, v=0)
            "I feel it sliding over the lips of her pussy for a few mere seconds."
            "Then it begins to sink inside of her without anything to oppose it."
            "The combination of water, heat and Amy's flustered state all work in my favour."
            show band threesome amyanna fuckamy onanna insert at stepback(speed=0.1, h=-10, v=0)
            "And I take full advantage too, pushing into her until I can go no deeper."
            "But I don't stop to enjoy the sensation, because I'm still aware of just where we are right now."
            show band threesome amyanna fuckamy onanna -insert
            pause 0.2
            show band threesome amyanna fuckamy onanna insert at stepback(speed=0.05, h=-10, v=0)
            "Instead I begin to pound away on Amy without any effort to build up slowly."
            "Suddenly she goes from anticipating what's to come to getting fucked for all she's worth!"
            show band threesome amyanna fuckamy onanna -insert
            pause 0.2
            show band threesome amyanna fuckamy onanna insert at stepback(speed=0.05, h=-10, v=0)
            "That's not to say Amy can't handle what I'm giving her."
            "Every thrust gets swallowed up by her sturdy little frame."
            show band threesome amyanna fuckamy onanna -insert
            pause 0.2
            show band threesome amyanna fuckamy pleasure insert at stepback(speed=0.05, h=-10, v=0)
            "And when I catch a glimpse of her face, she's always nodding like she wants more."
            "In my eagerness to get hold of Amy, I'd almost forgotten we're not alone."
            "So when I glance over Amy's shoulder and see Anna, I feel a sense of surprise."
            "Even more so when I see that she's not laying still either."
            show band threesome amyanna fuckamy -insert
            pause 0.2
            show band threesome amyanna fuckamy insert at stepback(speed=0.05, h=-10, v=0)
            "Instead she's pressing against Amy, following each move of her body as I fuck her."
            "But what really captures my attention is what she's doing with her hands."
            show band threesome amyanna fuckamy onmike -insert
            pause 0.2
            show band threesome amyanna fuckamy insert at stepback(speed=0.05, h=-10, v=0)
            "One is on Amy's skin, caressing, squeezing and pinching at her flesh."
            "And the other is down by her waist, desperately stroking her pussy!"
            show band threesome amyanna fuckamy -insert
            pause 0.2
            show band threesome amyanna fuckamy pleasure insert at stepback(speed=0.05, h=-10, v=0)
            "I doubt that I could have kept this up for much longer with Amy alone."
            "But now that I'm watching Anna pleasure herself too, I simply can't hold on."
            show band threesome amyanna fuckamy -insert
            pause 0.2
            show band threesome amyanna fuckamy pleasure insert with hpunch
            "With one last thrust, I push all the way into Amy."
            show band threesome amyanna fuckamy pleasure creampie with hpunch
            "And in the next breath I lose it, shooting my load deep inside of her."
            $ amy.sexperience += 1
            $ anna.love += 4
            $ amy.love += 4
    "Normally there'd be time to make sure everyone's satisfied."
    "But the moment that we're done, the reality of where we are hits us."
    scene bg black
    show minami_showersex_bg at center, zoomAt(1.25, (640, 900))
    show anna b blush naked at center, zoomAt(1.75, (880, 1140))
    show amy b blush naked at center, zoomAt(1.75, (400, 1140))
    with fade
    pause 0.5
    hide anna
    hide amy
    with easeoutleft
    "Anna and Amy turn tail and run out of the showers, heading back to the women's changing rooms."
    "That leaves me to quickly clean myself off for the second time."
    stop sound fadeout 0.5
    "Then I do the same as my companions, retreating hastily into the guy's changing rooms."
    "And all the time hoping that nobody saw what we just got up to."
    $ DONE["amy_anna_waterpark_threesome"] = game.days_played
    return

label band_harem_amy_event_05:
    scene bg street with fade
    "Everything seems to have happened in a blur today."
    "One minute I had no idea what I was going to do with my time."
    "The next Sasha strode into the room and informed me I was taking her on a date."
    "And then we were out of the door, heading off for some serious fun together."
    "It was only after walking her in a random direction for a few minutes that it came to me."
    scene bg amusement with dissolve
    "I could always take her to the amusement park, but make it look like that was my plan all along."
    "And so far it seems to be working."
    show sasha date at center, zoomAt (1.25, (320, 860)) with easeinleft
    "Sasha's ecstatic over being here, and is acting like she wants to ride on everything."
    show sasha date happy at center, zoomAt (1.25, (640, 860)) with ease
    sasha.say "Come on, [hero.name]…"
    show sasha at center, zoomAt (1.25, (740, 860)) with ease
    sasha.say "Keep up!"
    sasha.say "We're going to get separated at this rate!"
    show sasha normal
    mike.say "Okay, okay..."
    mike.say "I'm doing the best I can!"
    "I get the feeling Sasha's about to slow down and actually let me catch up."
    show sasha surprised at center, zoomAt (1.25, (840, 860)) with ease
    "But then she seems to spot something that catches her interest."
    "And then she's off again."
    show sasha happy at startle
    sasha.say "Wow..."
    sasha.say "Look at that!"
    show sasha normal
    "I put on a desperate burst of speed, and somehow manage to keep up with Sasha."
    "But then I almost slam straight into her as she comes to a sudden halt."
    show sasha happy
    sasha.say "That's new..."
    show sasha joke
    sasha.say "And we're riding it!"
    show sasha normal
    "I barely have time to look up and even see what this new ride happens to be."
    "All I can make out is curving metal, flashing lights and cars full of people flashing by."
    show sasha annoyed
    sasha.say "Now where in the hell is the queue?"
    show sasha normal at center, zoomAt (1.25, (740, 860)) with ease
    "Sasha's threading her way through the crowd as she says this."
    "Doing the best she can to locate the elusive line for the ride."
    play sound woosh_punch
    show sasha at center, zoomAt (1.25, (640, 860)) with MoveTransition(0.2)
    pause 0.1
    play sound punch_hard
    show sasha surprised
    show amy b angry at dark, blur(10), center, zoomAt (1.25, (540, 860))
    with hpunch
    show sasha at center, zoomAt (1.25, (740, 860)) with MoveTransition(0.1)
    "And that's about when she almost walks straight into another girl's back!"
    amy.say "Ouch!"
    amy.say "I'll tell you where the queue is, you clumsy mare..."
    amy.say "You just blundered into it!"
    "The girl's voice sounds familiar."
    "But even as I make to apologise, I can't quite place it."
    show sasha at center, zoomAt (1.25, (840, 860))
    show amy b angry at dark, blur(10), center, zoomAt (1.25, (440, 860))
    with ease
    show amy at brighter with dissolve
    "It's only when she turns around to confront Sasha that I realise who it actually is."
    mike.say "Amy?"
    show amy surprised at startle
    show fx question at right
    amy.say "[hero.name]?"
    show sasha surprised at startle
    sasha.say "Amy?!?"
    show amy surprised at startle
    amy.say "Sasha?!?"
    show sasha surprised at startle
    sasha.say "[hero.name]?!?"
    show sasha annoyed
    show amy annoyed
    "The strange roundabout process of everyone naming everyone else finally comes to a natural end."
    "But I can see there's far more to it than Sasha and Amy just being surprised to see each other."
    "Because the two of them are already squaring up to each other."
    "And they're twitching like they're going to come to blows!"
    show sasha angry
    sasha.say "You'd better let me on the ride before you, Amy..."
    sasha.say "Because it's a sure thing you're going to jinx it."
    sasha.say "Just like you did the band!"
    show sasha annoyed
    show amy angry
    amy.say "Oh yeah?"
    amy.say "Well that band sounds like cats screwing now..."
    amy.say "Thanks to how much your guitar-playing sucks!"
    show amy annoyed
    "I glance around, seeing that the argument is starting to get people's attention."
    "So I decide that I need to do something, before the park security get involved."
    if amy.flags.told_about_band:
        mike.say "Okay, okay..."
        mike.say "I get it, trust me, I do."
        mike.say "You were in a band together, it got messy, now you hate each other."
        mike.say "But this isn't the time or the place to thrash it out..."
        mike.say "Am I right?"
    else:
        mike.say "Wait a minute..."
        mike.say "You two know each other?"
        "Before Sasha or Amy can answer the question, I have a brainwave."
        "Suddenly everything seems to make sense."
        mike.say "Wait a minute..."
        mike.say "The band you were in..."
        mike.say "It's the same one?!?"
        "Enough time has passed for Sasha and Amy to look my way by now."
        "And the expressions on their faces don't seem to be very sympathetic."
        show amy angry
        sasha.say "Well, duh!"
        sasha.say "Try to keep up, genius!"
        show sasha annoyed
        show amy angry
        amy.say "That's right, Sasha..."
        amy.say "Piss all over your friends, just like always!"
        show amy annoyed
        mike.say "Okay, okay..."
        mike.say "I get it, trust me, I do."
        mike.say "You were in a band together, it got messy, now you hate each other."
        mike.say "But this isn't the time or the place to thrash it out..."
        mike.say "Am I right?"
    "For a moment, Sasha and Amy seem to stop and actually listen to me."
    "And I allow myself a brief second of relief, thinking I got through to them."
    "But then I see anger flare in their eyes again, and they start hurling insults again."
    show amy angry
    sasha.say "You're lucky someone stepped in to save you, bitch!"
    show sasha annoyed
    show amy angry
    amy.say "Not as lucky as you..."
    amy.say "You talentless sow!"
    show amy annoyed zorder 1 at center, zoomAt (1.25, (340, 860))
    show sasha zorder 2 at center, traveling (1.5, 0.3, (640, 1020))
    "The only thing I can think to do is put an arm around Sasha."
    hide sasha with easeoutleft
    pause 0.3
    scene bg amusement
    show sasha date annoyed at center, zoomAt (1.5, (640, 1020))
    with fade
    "And then I march her away from Amy, not stopping until we're out of the park."
    show sasha angry
    sasha.say "Aah..."
    sasha.say "Why'd you have to go and do that?"
    sasha.say "I could have handled her easily!"
    show sasha annoyed
    mike.say "Whatever, Sasha..."
    mike.say "Whatever..."
    return

label band_harem_amy_event_06:
    scene bg amusement
    show sasha happy at center, zoomAt (1.5, (640, 1040))
    with fade
    sasha.say "You know what, [hero.name]…"
    sasha.say "When you suggested this, I thought you were crazy."
    show sasha normal
    "Sasha and I are walking along, weaving through a crowd of bodies."
    "So it's pretty hard for me to keep up, listen and respond all at once."
    mike.say "You..."
    mike.say "You did?"
    show sasha shout
    sasha.say "Oh yeah..."
    sasha.say "Coming back to the Amusement Park so soon, you know?"
    show sasha joke
    sasha.say "After bumping into that trash-bag of Amy ruined the last time!"
    show sasha normal
    "I'm still ducking and weaving as we make our way through the Amusement Park gates."
    "Which is lucky for me, as it means that Sasha can't see the nervous smile on my face."
    mike.say "But now you don't think that, right?"
    mike.say "Because we wouldn't be back here if you did."
    show sasha happy
    sasha.say "That's right."
    show sasha shout
    sasha.say "I thought to myself..."
    sasha.say "Why should I let Amy ruin this for me?"
    sasha.say "She already almost ruined the band."
    sasha.say "So I'm not going to let her ruin this too!"
    show sasha normal
    "By now we're well and truly inside the park and surrounded by the rides."
    "But all the time I'm trying to hide the fact that I'm looking around with intent."
    "Luckily for me, Sasha seems more interested in checking out what she wants to ride first."
    mike.say "Ah..."
    mike.say "Ha, ha..."
    mike.say "That's the spirit, Sasha..."
    with hpunch
    mike.say "OUCH!"
    "I feel the sudden pain of someone jabbing me in the ribs and can't help crying out."
    "Which of course means that one hundred percent of Sasha's attention is now on me."
    show sasha surprised at startle
    sasha.say "What's the matter, [hero.name]?!?"
    sasha.say "Did someone attack you?"
    show sasha vangry
    sasha.say "If they did, they're gonna have me to reckon with!"
    show sasha annoyed
    "I do the best that I can to keep facing Sasha as she tries to push past me."
    "And this results in a comical situation, with her ducking this way and that."
    mike.say "It's nothing, Sasha..."
    mike.say "Really, I'm fine!"
    show sasha vangry
    sasha.say "What are you doing?"
    sasha.say "Why won't you let me get at the prick that attacked you?"
    show sasha annoyed
    "Sasha and I keep up this farcical dance until someone else steps in."
    "And that's the person that jabbed me in the ribs."
    show sasha surprised at center, traveling (1.25, 0.3, (940, 880))
    show amy annoyed at center, zoomAt (1.25, (340, 880)) with easeinleft
    "They step around me and stand there, arms crossed over their chest."
    "And believe me, it's quite some chest too!"
    show amy angry
    amy.say "Are you planning on telling me what's going on here, [hero.name]?"
    amy.say "Or are you just going to let her make a fool out of you, as usual?"
    show sasha wtf
    "The sight of Amy appearing from behind me is more than enough to stop Sasha in her tracks."
    "I watch as she openly gawps at the presence of the other girl, unable to believe what she's seeing."
    mike.say "Sasha, I can explain, okay?"
    mike.say "And, Amy, I can explain to you too, I promise!"
    "Before I chose to speak up, the animosity was between Sasha and Amy alone."
    "But the merest hint that I might have something to say to both of them..."
    "Well, that's more than enough to turn all of it straight onto me instead."
    show sasha vangry
    sasha.say "This had better be good, [hero.name]..."
    sasha.say "Because if it's not, you'll be walking with a limp for a month!"
    show sasha annoyed
    mike.say "Sasha, you wouldn't?"
    show amy angry
    amy.say "I might not beat you up, [hero.name]..."
    amy.say "But I can still hit you where it hurts."
    amy.say "I'll tell Shawn you think Babylon Five is shit!"
    show amy annoyed
    mike.say "Amy, he'd never speak to me again!"
    show sasha sad
    show amy worried
    "Both of them glare at me, their eyes boring into mine."
    "Which I guess means that my explanation really had better be good."
    mike.say "Okay, I get that you have serious history between you."
    mike.say "But I figured that there must have been some good times."
    mike.say "Because hating someone so much can't just come from nothing."
    mike.say "And maybe if you spend some time together, with a neutral chaperone..."
    "I put on a smile and gesture to myself as I say this."
    "Nodding to be sure that they get who I'm referring to."
    mike.say "Then maybe there's a chance you could mend things between you?"
    mike.say "Or at least learn to coexist without it ending in a fight?"
    show sasha angry
    "Sasha's the first to react to my little speech."
    "She puffs herself up, like she's going to scream in my face."
    "But then much to my surprise, she deflates right before my eyes."
    show sasha sadsmile
    sasha.say "Urgh..."
    sasha.say "If it had been anyone else but you asking, [hero.name]!"
    sasha.say "But you have an annoying habit of being right sometimes."
    show amy surprised
    "Amy's watching Sasha's reaction too, and she looks quite surprised."
    "The words coming out of the other girl's mouth seeming to have an effect on her."
    show amy sadsmile
    amy.say "I suppose that if Sasha can give you a chance, so can I."
    amy.say "But if this doesn't work, you never do anything like it again."
    amy.say "You hear me?"
    "I'm already nodding eagerly, keen to make the most of their agreement."
    mike.say "I totally do, totally..."
    mike.say "We make an effort to have a good time today."
    mike.say "And if we don't, that's the end of it."
    show sasha normal
    show amy normal
    "This time it's Sasha and Amy that nod."
    "But then they each see that the other is nodding too, they stop."
    show sasha annoyed
    show amy annoyed
    "And instead they do the best they can to look less than pleased."
    "As if the one of them that is most into the idea is somehow inferior."
    mike.say "Okay, okay..."
    mike.say "That's great, just great..."
    mike.say "So what do you guys want to do first?"
    "Unlike before, this time it's Amy who speaks up first."
    show amy upset
    amy.say "Well I hurried over here to be on time for the sake of some total doofus."
    amy.say "And that means I had to skip lunch to make it."
    show amy happy
    amy.say "So I say we go grab some food first."
    show amy puzzled
    "I look to Sasha as soon as Amy's finished saying her piece."
    "And I can see that she's trying to cook up a reason to object."
    "The basic stubbornness that defines her character making it hard for her to do anything else."
    "But somehow, Sasha actually manages to conquer it for once."
    show sasha sadsmile
    sasha.say "Ah, fuck it..."
    show sasha joke
    sasha.say "I'm pretty hungry too."
    show sasha normal
    show amy normal
    "I clap my hands together with genuine happiness."
    "Because it actually looks like they managed to agree on something for once."
    mike.say "Okay, that sounds like a plan."
    mike.say "Let's go grab something to eat."
    "Luckily for me this is the Amusement Park."
    "So you're never more than a couple of feet from a stall selling food."
    "Even if most of it is probably made up of sugar or congealed grease."
    "But of course, for every blessing the cosmos must bestow upon me a curse."
    "And in this case that becomes apparent very quickly."
    show sasha joke
    sasha.say "Right, I'm starving..."
    sasha.say "So I say we grab some burgers."
    sasha.say "Or maybe a hot-dog."
    show sasha annoyed
    show amy angry
    amy.say "Urgh!"
    amy.say "I don't want my arteries to clog up before we go on a single ride!"
    show amy flirt
    amy.say "Let's get something sweet instead, like cotton candy."
    show amy annoyed
    "Just like that I find myself back in the middle of a brewing argument."
    "And I know that I'm going to have to be the voice of reason again."
    $ renpy.dynamic(amy_score=0, sasha_score=0)
    menu:
        "Suggest donuts":
            "The only thing I know is that neither option appeals to me."
            "Burgers sound too heavy and cotton candy too sweet."
            "But maybe there's a way to find a compromise?"
            mike.say "Hmm..."
            mike.say "How about we get some donuts instead?"
            mike.say "They're nice and sweet for sure."
            mike.say "But they also have some real weight to them."
            show sasha angry
            show amy angry
            "I can see that both Sasha and Amy are about to object."
            "But then a weird thing happens."
            show sasha normal
            show amy normal
            "They seem to actually stop and think about the suggestion."
            "Rather than just rejecting it and starting to squabble."
            sasha.say "Huh..."
            show sasha joke
            sasha.say "I guess a donut could fill the hole."
            show sasha normal
            show amy happy
            amy.say "And they are coated in sugar."
            amy.say "So that should be sweet enough for me."
            show amy normal
            "I'm almost stunned into silence as we walk over to the donut stand."
            with fade
            "And I watch in amazement as Sasha and Amy order their donuts like civilised people."
            "I even see smiles starting to appear on their faces as they eat the things too."
            $ amy_score += 1
            $ sasha_score += 1
        "Recommend burgers":
            "The only thing I can think to do is be honest about it."
            "And I have to admit that one option appeals to me over the other."
            mike.say "All that whipped up sugar sounds like a little too much, Amy."
            mike.say "Let's get those burgers first."
            mike.say "You know, really lay down a solid foundation in our stomachs?"
            show sasha normal
            "Of course this idea goes down really well with Sasha."
            "But the same can't be said for Amy."
            show sasha happy
            sasha.say "You're right, [hero.name]..."
            sasha.say "You need to have a full belly to build up some stamina!"
            show sasha normal
            show amy upset
            amy.say "You do you."
            amy.say "I'll just wait it out."
            show amy sad
            with fade
            "Sasha's mood improves significantly once she has her burger."
            "And she's almost hanging off my arm as we eat them together."
            "But I can see that Amy's still feeling hungry."
            "And I'm worried about how it's going to affect her mood."
            $ amy_score -= 1
            $ sasha_score += 1
        "Propose cotton candy":
            "The only thing I can think to do is be honest about it."
            "And I have to admit that one option appeals to me over the other."
            mike.say "Greasy meat does sound a little too heavy, Sasha."
            mike.say "Let's get the cotton candy for now."
            mike.say "Then maybe think about something more substantial later."
            show amy normal
            "Of course this idea goes down really well with Amy."
            "But the same can't be said for Sasha."
            show amy happy
            amy.say "You're right, [hero.name]..."
            amy.say "The last thing you want is the meat sweats on a ride!"
            show amy normal
            show sasha vangry
            sasha.say "You do you."
            sasha.say "I'll just wait it out."
            show sasha sad
            with fade
            "Amy's mood improves significantly once she has her cotton candy."
            "And she's almost hanging off my arm as we eat it together."
            "But I can see that Sasha's still feeling hungry."
            "And I'm worried about how it's going to affect her mood."
            $ amy_score += 1
            $ sasha_score -= 1
    show amy normal
    show sasha normal
    with fade
    "While we're eating, we take the chance to wander around the park."
    "There are so many rides that it feels almost overwhelming."
    "And I have no idea how we're ever going to choose."
    show amy happy
    amy.say "Oh man..."
    amy.say "I want to choose a ride so badly!"
    sasha.say "Then what's stopping you?"
    show amy annoyed
    amy.say "Well..."
    amy.say "I don't want to start another argument!"
    show sasha happy
    sasha.say "Then let's have [hero.name] pick a ride instead."
    show amy normal
    show sasha normal
    "At the mention of my name, I turn around and begin paying more attention."
    mike.say "Huh?"
    mike.say "Did someone want me?"
    amy.say "Yeah, we did."
    sasha.say "We want you to choose the next ride."
    "Suddenly I feel that weight of responsibility pressing down on me again."
    "But this whole thing was my idea in the first place."
    "So I can't back out when Sasha and Amy are asking something of me together."
    menu:
        "Love Boat":
            "I take a glance around, surveying the nearby rides."
            "And then I settle on one that looks like it can't cause an argument."
            mike.say "Okay, guys..."
            mike.say "We're going to ride the Love Boat."
            show sasha annoyed
            show amy annoyed
            "As soon as the words are out of my mouth, Sasha and Amy groan as one."
            show sasha shocked
            sasha.say "The Love Boat?!?"
            show sasha sad
            show amy upset
            amy.say "That's so lame!"
            show amy sad
            "I feel an instant pang of annoyance at their reaction."
            "And it makes me instantly want to double down on my choice."
            mike.say "No complaining!"
            mike.say "You said you'd ride whatever I chose, remember?"
            with fade
            "Sasha and Amy continue to groan as we make are way over to the Love Boat."
            "It has a short queue, which means that we're soon climbing into a boat."
            scene bg black
            show love_boat_bg
            show love_boat_npc_amy at center, zoomAt (0.95, (490, 700))
            show love_boat_outfits_amy_casual at center, zoomAt (0.95, (490, 700))
            show love_boat_npc_mike at center, zoomAt (0.90, (590, 705))
            show love_boat_outfits_mike_casual at center, zoomAt (0.90, (590, 705))
            show love_boat_npc_sasha at center, zoomAt (0.95, (680, 710))
            show love_boat_outfits_sasha_casual at center, zoomAt (0.95, (680, 710))
            if sasha.flags.haircut:
                show love_boat_haircuts_sasha_haircut at center, zoomAt (0.95, (680, 710))
            else:
                show love_boat_haircuts_sasha_nohaircut at center, zoomAt (0.95, (680, 710))
            show love_boat_fg
            with fade
            "Then I take a deep breath, hoping that the atmosphere of the ride will do the rest."
            "But it doesn't take me long to realise that's not going to happen."
            "Sasha and Amy spend the whole of the ride avoiding my eye."
            "And it comes to an end, I feel glad to be able to get off again."
            $ amy_score -= 1
            $ sasha_score -= 1
        "Hedge Maze":
            "I take a glance around, surveying the nearby rides."
            "And then I settle on one that looks like it can't cause an argument."
            mike.say "Okay, guys..."
            mike.say "We're going to explore the Hedge Maze."
            show sasha annoyed
            show amy annoyed
            "Sasha and Amy seem prepared to groan as one and piss on my choice."
            "But when they actually hear what I have in mind, they seem surprised."
            show sasha normal
            sasha.say "The maze, huh?"
            show amy normal
            amy.say "That's not what I was expecting to hear."
            "I feel a renewed sense of hope at their apparent curiosity."
            "And so I do the best I can to capitalise on it, hurrying them to towards the line."
            "It has a short queue, which means that we're soon stepping into the maze."
            show sasha happy with fade
            sasha.say "Wow..."
            sasha.say "This is pretty atmospheric."
            show sasha normal
            show amy happy
            amy.say "Kind of like a weird movie, you know?"
            amy.say "Or even a trippy videogame."
            scene bg black
            show hedge_maze_bg
            show hedge_maze_mcbody_mikemc at center, zoomAt (1.0, (470, 720))
            show hedge_maze_mc_outfits_mikemc_mc_casual at center, zoomAt (1.0, (470, 720))
            show hedge_maze_npc_amy at center, zoomAt (1.0, (480, 720))
            show hedge_maze_outfits_nakedbelly_amy_casual at center, zoomAt (1.0, (480, 720))
            show hedge_maze_npc_sasha at center, zoomAt (1.0, (760, 720))
            show hedge_maze_outfits_sasha_casual at center, zoomAt (1.0, (760, 720))
            if sasha.flags.haircut:
                show hedge_maze_haircuts_sasha_haircut at center, zoomAt (1.0, (760, 720))
            else:
                show hedge_maze_haircuts_sasha_nohaircut at center, zoomAt (1.0, (760, 720))
            with fade
            "Soon enough we're all wandering through the maze."
            "Second-guessing ourselves as to where we're going and where we've been."
            "Much to my delight, Sasha and Amy actually seem to forget themselves."
            "As they chat about the route we're taking and help each other out more than once."
            "I decide not to point this out for fear of ruining their progress."
            "But by the time we're out of there, I'm feeling quietly confident."
            "Confident that my plan is starting to work."
            $ amy_score += 1
            $ sasha_score += 1
        "Merry-go-Round":
            "I take a glance around, surveying the nearby rides."
            "And then I settle on one that looks like it can't cause an argument."
            mike.say "Okay, guys..."
            mike.say "We're going to ride the Merry-go-Round."
            show sasha annoyed
            show amy annoyed
            "As soon as the words are out of my mouth, Sasha and Amy groan as one."
            show sasha shocked
            sasha.say "The Carousel?!?"
            show sasha sad
            show amy upset
            amy.say "That's so lame!"
            show amy sad
            "I feel an instant pang of annoyance at their reaction."
            "And it makes me instantly want to double down on my choice."
            mike.say "No complaining!"
            mike.say "You said you'd ride whatever I chose, remember?"
            with fade
            "Sasha and Amy continue to groan as we make are way over to the Merry-go-Round."
            scene bg black
            show merry_go_round_bg
            show merry_go_round_npc_amy at center, zoomAt (0.95, (710, 680))
            show merry_go_round_outfits_amy_casual at center, zoomAt (0.95, (710, 680))
            show merry_go_round_mikemc at center, zoomAt (1.0, (640, 720))
            show merry_go_round_mc_outfits_mikemc_mc_casual at center, zoomAt (1.0, (640, 720))
            show merry_go_round_npc_sasha at center, zoomAt (1.0, (630, 720))
            show merry_go_round_outfits_sasha_casual at center, zoomAt (1.0, (630, 720))
            if sasha.flags.haircut:
                show merry_go_round_haircuts_sasha_haircut at center, zoomAt (1.0, (630, 720))
            else:
                show merry_go_round_haircuts_sasha_nohaircut at center, zoomAt (1.0, (630, 720))
            show merry_go_round_fg
            with fade
            "It has a short queue, which means that we're each soon climbing into a wooden horse of our own."
            "Then I take a deep breath, hoping that the thrill of the ride will do the rest."
            "But it doesn't take me long to realise that's not going to happen."
            show sasha annoyed
            show amy annoyed
            "Sasha and Amy spend the whole of the ride avoiding my eye."
            "And it comes to an end, I feel glad to be able to get off again."
            $ amy_score -= 1
            $ sasha_score -= 1
    scene bg amusement
    show sasha casual normal at center, zoomAt (1.25, (940, 880))
    show amy casual normal at center, zoomAt (1.25, (340, 880))
    with fade
    "Now that we've taken a couple of rides and had some food, I feel my confidence growing."
    "Perhaps this would be a good time to start trying to get to the bottom of the issues here?"
    "To spend a while carefully delving into the root of Sasha and Amy's issues with each other?"
    menu:
        "Ask why Amy was kicked out of the band":
            mike.say "So, Sasha..."
            mike.say "You never actually told me why you kicked Amy out of the band."
            show amy surprised
            "Amy's eyes go wide at this."
            "So wide in fact that I think they're going to pop out."
            "And she jumps in before Sasha can say a word."
            amy.say "Is that what she told you?!?"
            amy.say "I was not kicked out of the band."
            show amy upset
            amy.say "I chose to leave!"
            show amy angry
            show sasha joke
            "I hear Sasha snort with derision."
            "And so I turn my gaze towards her instead."
            sasha.say "Oh wow, Amy..."
            sasha.say "Is that what you go round telling people?"
            show sasha vangry
            sasha.say "You can't call it quitting when everyone else tells you to fuck off!"
            show sasha angry
            "Before I know it, the two of them are at each other's throats."
            "And there's nothing I can do to stop the argument."
            "So it looks like I screwed this one up badly."
            $ amy_score -= 1
            $ sasha_score -= 1
        "Ask why Amy left the band":
            mike.say "So, Amy..."
            mike.say "You never actually told me why you chose to leave the band."
            show sasha shocked
            "Sasha's eyes go wide at this."
            "So wide in fact that I think they're going to pop out."
            "And she jumps in before Amy can say a word."
            show sasha surprised
            sasha.say "Is that what she told you?!?"
            sasha.say "She did not choose to leave the band."
            show sasha vangry
            sasha.say "We fired her ass!"
            show sasha angry
            "I hear Amy snort with derision."
            "And so I turn my gaze towards her instead."
            show amy flirt
            amy.say "Geez, Sasha..."
            amy.say "Is that what you go round telling people?"
            show amy upset
            amy.say "You can't call it firing me when I already decided to walk out!"
            show amy angry
            "Before I know it, the two of them are at each other's throats."
            "And there's nothing I can do to stop the argument."
            "So it looks like I screwed this one up badly."
            $ amy_score -= 1
            $ sasha_score -= 1
        "Ask why Sasha and Amy couldn't coexist in the band":



            mike.say "I think it's a shame you couldn't stay in the band together."
            mike.say "Because you must have been amazing playing alongside each other."
            show amy surprised
            show sasha surprised
            "I can see that both Sasha and Amy are caught off-guard by the compliments."
            "And neither of them seems to want to be the one to be negative right now."
            "Which also means that they can't take shots at each other too."
            show sasha sadsmile
            sasha.say "I..."
            sasha.say "I guess we did sound pretty good together."
            sasha.say "And...you are a fierce player, Amy."
            show amy sadsmile
            amy.say "Yeah..."
            amy.say "I always liked your sound too, Sasha..."
            amy.say "I thought we kind of complimented each other."
            "I let out a sigh and shrug my shoulders."
            mike.say "Ah..."
            mike.say "That's a real shame."
            mike.say "I would have loved to hear you two play together."
            "I watch closely as Sasha and Amy absorb all of this."
            "And though I'm trying to get a certain reaction out of them, I'm not lying either."
            "I really do hope the effect of my words is to make them think about the good times they had together."
            "That and maybe to make them think it's something they could get back."
            $ amy_score += 1
            $ sasha_score += 1
    show amy normal
    show sasha normal
    with fade
    "By now I'm starting to get the feeling that our time at the Amusement Park is coming to an end."
    "It's just one of those natural feelings you get that can't really be explained in words."
    "But I feel like I have to try all the same, so I stop and get Sasha and Amy's attention."
    mike.say "You getting that feeling too?"
    mike.say "Like it's time to be heading home?"
    if amy_score >= 2 and sasha_score >= 2:
        show sasha joke
        sasha.say "Nah..."
        sasha.say "I could stand to stay a little longer."
        show sasha happy
        sasha.say "I had a really great time today."
        show sasha normal
        "I'm quite surprised to hear Sasha being so positive."
        "But I can't help turning to Amy and fearing the worst."
        "Because the two of them always seem to choose opposing sides."
        "Sometimes even simply out of naked spite."
        show amy happy
        amy.say "You know what..."
        amy.say "I'm not ready to call it quits just yet."
        amy.say "I had a pretty fun time today."
        show amy normal
        "For a moment I don't know what to say."
        "It's been so hard trying to get these two on the same page."
        "Now that it seems to be happening I'm kind of lost!"
        mike.say "Erm..."
        mike.say "Okay, guys..."
        mike.say "How about we stay for one more ride?"
        mike.say "We could go on the..."
        "I cast my gaze about, looking for a suitable choice."
        mike.say "The...Ferris Wheel?"
        mike.say "How about we ride the Ferris Wheel?"
        show sasha happy
        show amy happy
        "Much to my relief, this gets a nod from Sasha and Amy."
        show amy normal
        show sasha normal
        "So I start heading over there as quickly as I can."
        "Already afraid that this temporary truce might not last."
        call band_harem_amy_ferris_wheel_threesome from _call_band_harem_amy_ferris_wheel_threesome
        $ amy.flags.peace_with_sasha = True
    elif sasha_score > 1:
        show sasha joke
        sasha.say "Nah..."
        sasha.say "I could stand to stay a little longer."
        show sasha happy
        sasha.say "I had a really great time today."
        show sasha annoyed
        sasha.say "Even with certain people along for the ride!"
        "Sasha makes sure that she's looking straight at Amy as she says this."
        "And for her troubles, she get's a pretty hostile glare in return."
        show amy annoyed
        amy.say "Not me."
        amy.say "In fact I think I'm gonna head home."
        show amy sadsmile
        amy.say "See you around, [hero.name]."
        show amy sad
        "I note that Amy doesn't bother to say goodbye to Sasha."
        hide amy with easeoutleft
        "And as she turns on her heel and walks away, I kind of feel like a failure."
        "I didn't manage to get these two back on the same page."
        "But maybe I'll get another chance to try in the future."
    elif amy_score > 1:
        show amy happy
        amy.say "You know what..."
        amy.say "I'm not ready to call it quits just yet."
        amy.say "I had a pretty fun time today."
        show amy annoyed
        amy.say "Even if I had to put up with some bullshit along the way!"
        "Amy makes sure that she's looking straight at Sasha as she says this."
        show sasha annoyed
        "And for her troubles, she get's a pretty hostile glare in return."
        sasha.say "Speak for yourself."
        sasha.say "I can't wait to get out of here."
        show sasha vangry
        sasha.say "Come on, [hero.name]..."
        sasha.say "Let's go home!"
        show sasha angry
        "I note that Sasha doesn't bother to say goodbye to Amy."
        hide amy with easeoutleft
        "And as she turns on her heel and walks away, pulling me along with her, I kind of feel like a failure."
        "I didn't manage to get these two back on the same page."
        "But maybe I'll get another chance to try in the future."
        $ amy.flags.possible_peace_with_sasha = True
    else:
        show amy upset
        amy.say "You hit the nail on the head, [hero.name]."
        amy.say "In fact I think I'm gonna head home right now."
        show amy sadsmile
        amy.say "See you around, [hero.name]."
        show amy sad
        show sasha vangry
        sasha.say "Me too."
        sasha.say "I can't wait to get out of here."
        sasha.say "Come on, [hero.name]..."
        sasha.say "Let's go home!"
        show sasha sad
        "I note that Sasha doesn't bother to say goodbye to Amy, and vice versa."
        hide amy with easeoutleft
        "And Amy turns on her heel and walks away, pulling me along with Sasha, I kind of feel like a failure."
        "I didn't manage to get these two back on the same page."
        "But maybe I'll get another chance to try in the future."
    return

label band_harem_amy_ferris_wheel_threesome:
    "I have to say that I'm pretty confused as to just why Sasha and Amy want to ride the Ferris Wheel."
    "I mean, we were about to leave the amusement park and start making our way home after a long day here already."
    "But all of a sudden the pair of them seem to have found their second wind, which is fine by me."
    "Yet why in the hell would they want to go to all that trouble for a ride on the Ferris wheel of all things?"
    "It's one of the oldest rides in the park, and it's not exactly the most exciting either."
    "Sure, the view from the top is pretty great, but that's about it!"
    "But I guess the whole point of bringing Sasha and Amy here today was to build bridges between them."
    "So I can't exactly start digging my heels in now, not when they finally seem to be getting on so well."
    mike.say "Okay..."
    mike.say "So here we are, guys..."
    mike.say "Waiting in line for the Ferris Wheel."
    show sasha annoyed
    show amy annoyed
    "This earns me a couple of sideways glances from Sasha and Amy."
    "Though I do note that there's something more in the glances they exchange themselves."
    sasha.say "Yeah, [hero.name]…"
    show sasha shout
    sasha.say "And we're about to get on the damn thing too!"
    show sasha normal
    show amy flirt
    amy.say "So just get in there already!"
    show amy happy
    amy.say "I guarantee you'll love it."
    show amy normal
    "I can't help thinking Amy's overselling the potential of the ride."
    "But I decide to do as I'm told, sliding into the gondola after Sasha."
    "Amy jumps in on the other side of me, pulling down the safety bar as she does so."
    scene ferris lookout amysasha with fade
    amy.say "Here we go!"
    sasha.say "Hold on!"
    mike.say "Erm..."
    mike.say "Yay...I guess!"
    "Sasha and Amy are still chuckling at some private joke as the gondola rises into the air."
    "But I'm doing the best I can to make something out of the ride and so I ignore them."
    "Instead I content myself with looking out at the view from the gondola as we get higher."
    "Enjoying the feeling of the sun on my face, the wind in my hair, the hands on my cock..."
    "Wait a minute..."
    "Hands on my cock?!?"
    scene band handjob amysasha at center, zoomAt(1.6, (640, 1100)) with fade
    "I look down, expecting to see something innocent that will explain the odd sensation."
    "But instead I see exactly what it felt like, two hands eagerly stroking my groin!"
    "One of them belongs to Sasha, the other to Amy, and they're already unzipping my flies!"
    "I look up and turn my head first to the right and then to the left."
    "A knowing smile greets me on each side, along with a flutter of filthy giggles."
    mike.say "Guys..."
    mike.say "What are you..."
    sasha.say "Shh!"
    sasha.say "Don't worry about it, [hero.name]."
    amy.say "You helped us out today."
    amy.say "Now let us return the favour, okay?"
    show band handjob amysasha pleasure
    mike.say "But, but..."
    mike.say "Shouldn't we wait until we're somewhere more..."
    mike.say "I don't know...private?!?"
    show band handjob amysasha at center, traveling (1.0, 0.3, (640, 720))
    "By now they have my cock all the way out of my pants."
    "And they're busy massaging it into life, which doesn't seem to be taking long!"
    "But at the same time, Sasha and Amy are still talking me round to their way of thinking."
    amy.say "Don't worry about a thing."
    amy.say "We'll handle everything."
    sasha.say "And no one can see us up here either."
    sasha.say "So there's nothing to worry about."
    mike.say "Erm..."
    mike.say "Okay, guys..."
    mike.say "If you say so."
    sasha.say "Oh, but there is one thing you have to decide."
    amy.say "And that's which one of us you want to fuck!"
    "I watch as Sasha and Amy start using their free hands to undress."
    "Popping buttons and pulling off their clothes."
    show band handjob amysasha naked with dissolve
    sasha.say "One thing though, [hero.name]…"
    sasha.say "You'd better be quick about it!"
    menu:
        "Fuck Amy":
            "I'm already feeling the adrenaline flowing through my veins."
            "So when I'm told that I have to speed things up, I take it literally."
            "Without a conscious thought, I turn to my left and grab hold of Amy."
            "Even though all of this was the girl's idea, she still seems taken by surprise."
            "Because she lets out a squeal as I pull her ass down and onto my lap."
            scene bg black
            show band threesome fuckamy naked
            with fade
            amy.say "Ooh..."
            amy.say "What are you..."
            "The only problem is that I'm not in the mood to answer questions or explain myself."
            "But what I am is already hard and standing to attention down there."
            "Which means that as Amy sits down, she's also sitting on my cock!"
            amy.say "Oh shit..."
            amy.say "[hero.name], I'm..."
            amy.say "I'm not ready!"
            "I hardly hear a word that Amy's saying, as I'm now on auto-pilot."
            "And all I can think about doing is pulling her down while thrusting up from below."
            "But that's when Sasha steps up to the plate, making sure things go smoothly."
            sasha.say "No time for any fancy stuff, Amy..."
            sasha.say "This is going to be wham, bam, thank you mam!"
            "As if to make her point, Sasha reaches between Amy's legs."
            "And then I feel her begin to massage the lips of the other girl's pussy."
            "Of course this only serves to redouble the pleasure Amy's already feeling."
            "But for me, the effect is even better, as it instantly lowers her resistance."
            show band threesome fuckamy vaginal at stepback(0.1, -10, 0)
            "Within what feels like seconds, I can feel myself begin to sink into her."
            "Amy gasps and moans, sliding ever further down the shaft of my cock."
            "Until I'm all the way in and can go no further."
            show band threesome fuckamy vaginal wet at stepback(0.1, -10, 0)
            "But there's no time to sit around and savour the feeling of it."
            "Because by now we've reached the top of the wheel."
            "That means the ride will probably stop for a while."
            "But it also means that, when we start moving again, we'll be on the way down!"
            show band threesome fuckamy at stepback(0.1, -10, 0)
            "With that in mind, I all but launch myself into Amy."
            "In fact I'm pounding her so hard that she's bouncing up and down on my lap."
            show band threesome fuckamy at stepback(0.1, -10, 0)
            "That and the motion of it all is making the gondola swing back and forth."
            "Normally I'd be worried about the thing breaking under the strain."
            show band threesome fuckamy at stepback(0.1, -10, 0)
            "But the only thing on my mind is fucking Amy, as hard and as fast as I can."
            "Of course she's more than a little out of it right now."
            show band threesome fuckamy at stepback(0.1, -10, 0)
            "Her entire body jiggling up and down as she rides my cock."
            "And even Sasha seems absorbed in the task at hand."
            show band threesome fuckamy at stepback(0.1, -10, 0)
            "Because she keeps on running her hands over Amy the whole time."
            "Pinching, stroking and teasing everything that she can reach."
            amy.say "Mmm..."
            amy.say "I'm going to..."
            amy.say "I'm going to cum!"
            show band threesome fuckamy at stepback(0.1, -10, 0)
            "I feel Amy's pussy clamp down on me as her words come true."
            "And then comes the flood of relief as she takes me along with her."
            show band threesome fuckamy creampie with hpunch
            "I keep on thrusting away as I shoot my load into Amy."
            with hpunch
            "Sasha doing all she can at the same time to keep us upright."
            with hpunch
            "There's no chance to properly recover my senses once it's over."
            "As the ride starts to move almost as soon as we're done."
            "And what follows is a mad scramble to get dressed before it's too late."
            $ amy.sexperience += 1
            $ amy.love += 2
        "Fuck Sasha":
            "I'm already feeling the adrenaline flowing through my veins."
            "So when I'm told that I have to speed things up, I take it literally."
            "Without a conscious thought, I turn to my right and grab hold of Sasha."
            "Even though all of this was the girl's idea, she still seems taken by surprise."
            "Because she lets out a squeal as I pull her ass down and onto my lap."
            sasha.say "Wha..."
            sasha.say "What the hell..."
            scene bg black
            show band threesome fucksasha naked out
            with fade
            "The only problem is that I'm not in the mood to answer questions or explain myself."
            "But what I am is already hard and standing to attention down there."
            "Which means that as Sasha sits down, she's also sitting on my cock!"
            sasha.say "Oh fuck..."
            sasha.say "[hero.name], I'm..."
            sasha.say "I'm not ready!"
            "I hardly hear a word that Sasha's saying, as I'm now on auto-pilot."
            "And all I can think about doing is pulling her down while thrusting up from below."
            "But that's when Amy steps up to the plate, making sure things go smoothly."
            amy.say "No time for any fancy stuff, Sasha..."
            amy.say "This is going to be wham, bam, thank you mam!"
            "As if to make her point, Amy reaches between Sasha's legs."
            "And then I feel her begin to massage the lips of the other girl's pussy."
            "Of course this only serves to redouble the pleasure Sasha's already feeling."
            "But for me, the effect is even better, as it instantly lowers her resistance."
            show band threesome fucksasha vaginal at startle(0.1,-10)
            "Within what feels like seconds, I can feel myself begin to sink into her."
            "Sasha gasps and moans, sliding ever further down the shaft of my cock."
            "Until I'm all the way in and can go no further."
            show band threesome fucksasha at startle(0.1,-10)
            "But there's no time to sit around and savour the feeling of it."
            "Because by now we've reached the top of the wheel."
            "That means the ride will probably stop for a while."
            "But it also means that, when we start moving again, we'll be on the way down!"
            show band threesome fucksasha at startle(0.1,-10)
            "With that in mind, I all but launch myself into Sasha."
            "In fact I'm pounding her so hard that she's bouncing up and down on my lap."
            show band threesome fucksasha at startle(0.1,-10)
            "That and the motion of it all is making the gondola swing back and forth."
            "Normally I'd be worried about the thing breaking under the strain."
            show band threesome fucksasha at startle(0.05,-10)
            "But the only thing on my mind is fucking Sasha, as hard and as fast as I can."
            "Of course she's more than a little out of it right now."
            show band threesome fucksasha at startle(0.05,-10)
            "Her entire body jiggling up and down as she rides my cock."
            "And even Amy seems absorbed in the task at hand."
            show band threesome fucksasha at startle(0.05,-10)
            "Because she keeps on running her hands over Sasha the whole time."
            "Pinching, stroking and teasing everything that she can reach."
            sasha.say "Mmm..."
            sasha.say "I'm going to..."
            sasha.say "I'm going to cum!"
            show band threesome fucksasha at startle(0.05,-10)
            "I feel Sasha's pussy clamp down on me as her words come true."
            "And then comes the flood of relief as she takes me along with her."
            show band threesome fucksasha creampie with vpunch
            "I keep on thrusting away as I shoot my load into Sasha."
            with vpunch
            "Amy doing all she can at the same time to keep us upright."
            with vpunch
            "There's no chance to properly recover my senses once it's over."
            "As the ride starts to move almost as soon as we're done."
            "And what follows is a mad scramble to get dressed before it's too late."
            $ sasha.sexperience += 1
            $ sasha.love += 2
    scene bg amusement
    show amy casual flirt at left4
    show sasha casual flirt at right4
    with fade
    "Once the gondola reaches the ground, we're pretty much dressed."
    "Sure, we might look more than a little dishevelled."
    "But nobody seems to notice as we stagger out off the ride."
    "Then, pretty much holding each other up, we stagger off into the crowds."
    return


label band_harem_amy_event_07:
    "I'm feeling pretty worn out from all of my efforts to mend bridges between Amy and the other girls in the band."
    "And even though I'm starting to regain some of the physical energy I spent doing so, my head's another matter entirely."
    "Juggling all of those memories, passionate feelings and boiling emotions has left me mentally drained."
    "Almost to the degree that I'd half-forgotten just how well everything turned out in the end."
    show amy normal at center, zoomAt (1.25, (640, 880)) with fade
    "Which is why the next time I see Amy, I'm really not on the same page as her mentally."
    show amy happy
    amy.say "There you are, [hero.name]…"
    amy.say "The genius that figured it all out!"
    amy.say "The mediator that negotiated peace between all sides!"
    show amy normal
    mike.say "Huh?"
    mike.say "I did what now, Amy?"
    "For some reason, Amy seems to miss the sheer fatigue in my voice."
    "As well as the partially glazed look in my eyes too."
    "And she obviously thinks that I'm trying to play it down."
    show amy happy
    amy.say "Come on, [hero.name]…"
    amy.say "Don't try to be modest."
    amy.say "I thought there was no way I'd ever get back on speaking terms with those girls."
    amy.say "But you proved me wrong, dead wrong!"
    show amy normal
    "By now I'm starting to wake up a little more."
    "My brain's had the time it needs to get up to speed."
    "So I can actually answer Amy, rather than stumbling over bland mutterings."
    mike.say "I guess it was a pretty big ask."
    mike.say "But if it helped you guys out..."
    mike.say "Then all the effort was well worth it."
    show amy happy
    "Amy nods and smiles at this, keen to agree."
    show amy normal
    "But I feel like there's something more that she wants to say."
    mike.say "This is where you say it, Amy."
    show amy surprised
    amy.say "Huh?"
    amy.say "What are you talking about?"
    show amy puzzled
    mike.say "There's no need to play dumb with me, Amy."
    mike.say "I can tell that there's more you want to say."
    mike.say "So come on and tell me already!"
    "Amy looks like she's going to keep on denying it for a moment."
    "But then she seems to crack and give up on the idea."
    show amy annoyed
    amy.say "Okay, you got me!"
    amy.say "I was going to ask what we do next?"
    show amy shy
    "I blink in momentary confusion."
    "Not really sure what Amy actually means."
    mike.say "Well..."
    mike.say "I suppose we could go celebrate."
    mike.say "If that's what you mean?"
    show amy puzzled
    "Amy shakes her head at this."
    "Which obviously means I've misunderstood her somewhere along the way."
    show amy happy
    amy.say "No, no, no..."
    amy.say "I mean what do we do about the band?"
    show amy normal
    "I give Amy another blink."
    "Because I'm still not sure what she's getting at."
    mike.say "The band?"
    mike.say "Like, The Deathless Harpies?"
    mike.say "I thought you were all friends again?"
    mike.say "What more is there to do?"
    show amy happy
    amy.say "We have to get me back into the band, of course!"
    amy.say "You think I just want to be friends with those guys?"
    amy.say "Uh-uh, [hero.name]..."
    amy.say "I want things back the way they were, as much as possible."
    amy.say "I want to be playing with them again!"
    show amy normal
    menu:
        "Alright, let's make you a member again!":
            "I start nodding my head even before Amy's done explaining herself."
            mike.say "That's a great idea, Amy!"
            mike.say "I'd love to see you guys back together."
            mike.say "It'd make the Deathless Harpies even better than before!"
            "Of course, this is exactly the answer that Amy wanted."
            "And she instantly jumps on my enthusiasm."
            show amy happy
            amy.say "My point exactly!"
            amy.say "It's kind of like destiny, you know?"
            amy.say "Like this was all meant to be."
            amy.say "And I feel like I'm better friends with the girls than ever."
            amy.say "So the music should sound better than ever too!"
            show amy normal
            "I'm nodding eagerly by now."
            "My enthusiasm growing by the second."
            mike.say "So what do we do now?"
            mike.say "You going to talk to them or something?"
            "It's now that I see a smile creeping onto Amy's face."
            "And it's a pretty guilty one too."
            show amy happy
            amy.say "Well..."
            amy.say "That's where you come in."
            amy.say "I was thinking it would sound better coming from you?"
            show amy normal
            mike.say "From me?!?"
            show amy happy
            amy.say "You were the one that managed to get us talking again."
            amy.say "So I figure you can make this happen too."
            show amy normal
            "I'm still more than a little scared of the idea."
            "But what Amy's saying kind of makes sense."
            "And I can't think of a better plan on the spot."
            "So I nod my head."
            mike.say "If that's what you want, Amy..."
            mike.say "I promise that I'll do the best I can."
            show amy flirt at center, traveling(1.5, 0.3, (640, 1040))
            "Amy leans in and plants a kiss on my cheek."
            $ amy.love += 2
            show amy happy
            amy.say "Oh..."
            amy.say "Thank you!"
            amy.say "And I promise that if you pull it off..."
            amy.say "Then there'll be more where that came from!"
            $ amy.flags.help_join_band = True
        "Don't push your luck":
            "I start shaking my head even before Amy's done explaining herself."
            show amy puzzled
            mike.say "I don't think that would be a good idea, Amy."
            mike.say "Trying to patch up your friendships was one thing."
            mike.say "But getting you back into the band feels like too much."
            "Of course, this isn't the answer that Amy wanted."
            "And she instantly starts trying to change my mind."
            show amy upset
            amy.say "No, [hero.name], it's not."
            amy.say "It's just the next stage of the process."
            amy.say "The girls are all cool with me now."
            amy.say "And the last time that was the case, I was in there with them."
            amy.say "Don't you see the logic of that?"
            show amy sadsmile
            mike.say "No, Amy..."
            mike.say "I see how you'd want it to be true though."
            show amy upset
            "Amy opens her mouth to protest."
            show amy puzzled
            "But I cut her off before she can speak."
            mike.say "Look, Amy..."
            mike.say "If they ask you back into the band, that's cool."
            mike.say "Or if you ask and they say yes, equally good."
            mike.say "But The Deathless Harpies have moved on since you left."
            mike.say "You can't manipulate your way back in there."
            show amy annoyed
            "By the time I'm done explaining myself, Amy looks pretty pissed."
            "But I make it clear from my body-language that I'm not going to be swayed."
            $ amy.love -= 5
            show amy angry
            amy.say "Urgh..."
            show amy upset
            amy.say "You can be such a frustrating dick sometimes!"
            amy.say "If you won't help me, then I'll do it myself."
            hide amy with easeoutright
            "Amy turns on her heel and walks away without saying anything more."
            "And the truth is that I wish her all the success in the world."
            "If she can talk her way back into The Deathless Harpies, good for her."
            "But I'm not going to do it for her, and I won't be moved on it either."
            $ amy.flags.help_join_band = False
    scene bg black with dissolve
    return

label band_harem_amy_event_08:
    if 'band_harem_amy_event_09' not in DONE and 'band_harem_amy_event_10' not in DONE:
        "I figure that if I'm going to do this thing, then I have to start at the top and work my way down."
        "Which in the case of The Deathless Harpies, means going for the head of the beast first."
        "And while Sasha and Anna might disagree with me on this, I think that can only be Kleio."
        "So I wait for the next time that I meet up with her, and I prepare myself to ask the question."
    show kleio c annoyed at center, zoomAt (1.25, (640, 880)) with fade
    mike.say "Erm..."
    mike.say "Kleio..."
    show kleio a normal
    "Almost the same moment I begin to say her name, Kleio's head snaps around."
    "And then I'm the centre of her attention, nothing else seeming to distract her."
    "Now that might sound like a good thing."
    "But believe me, with a girl like Kleio, it's pretty fucking scary!"
    kleio.say "Let me guess, Loverboy…"
    kleio.say "You wanna talk to me, right?"
    kleio.say "About something really important?"
    "I feel more than a little unnerved by the way Kleio just kind of pounced on me."
    "Almost like she knew exactly what I was going to say, and was just waiting to hear it."
    mike.say "Whoa..."
    mike.say "That's right, Kleio..."
    mike.say "How did you know?"
    show kleio happy at startle
    "Kleio shakes her head and lets out a filthy laugh."
    show kleio normal
    kleio.say "Oh come on, Loverboy…"
    kleio.say "You just manipulated me into spending a night down the pub with Amy."
    if amy.flags.peace_with_kleio:
        kleio.say "Plus we went from hated enemies to reunited friends in the same night."
    mike.say "Oh yeah..."
    mike.say "There was that..."
    kleio.say "Plus I heard from Sasha and Anna."
    kleio.say "They told me you did pretty much the same to them too!"
    kleio.say "So what am I supposed to think, huh?"
    "I hold my hands up in a gesture of surrender."
    "And at the same time I drop any pretence."
    mike.say "Okay, Kleio..."
    mike.say "You got me!"
    mike.say "Amy came to me the other day and asked me a favour."
    mike.say "She asked me to ask you if she could get back into the band."
    show kleio surprised
    "Suddenly I see a change in Kleio's expression."
    "Where before she was cocky and confident, now she looks genuinely surprised."
    kleio.say "You're serious?"
    kleio.say "Amy wants to re-join The Deathless Harpies?"
    mike.say "That's about the size of it, Kleio."
    mike.say "So what do you say?"
    if amy.flags.peace_with_kleio or kleio.love >= 180 or kleio.sub >= 100:
        show kleio annoyed
        kleio.say "Amy wants back in..."
        kleio.say "You know, just a couple of days ago, I'd have said no way."
        show kleio normal
        kleio.say "But you really changed my mind on her, Loverboy."
        "I'm nodding by now."
        "Keen to capitalise on Kleio's apparent approval."
        if 'band_harem_amy_event_09' not in DONE or 'band_harem_amy_event_10' not in DONE:
            mike.say "So that's agreed then?"
            mike.say "Amy's officially back in the band?"
            mike.say "Sasha and Anna will go along with your decision?"
            "To my surprise, Kleio shakes her head at this."
            show kleio angry
            kleio.say "No way!"
            kleio.say "We're a democracy."
            show kleio normal
            kleio.say "You go ask them and get their answers."
            kleio.say "And whatever they are, the majority wins."
            "Now my nodding becomes more apologetic."
            "Maybe even a little grovelling too."
            mike.say "Oh..."
            mike.say "Sure, Kleio...of course!"
            mike.say "I'll go ask them right away."
        $ kleio.flags.amy_accepted = True
    else:
        show kleio angry
        kleio.say "How could I have been so stupid?!?"
        kleio.say "I should have seen this coming from miles away!"
        show kleio upset
        "Now Kleio's gone from surprised to super-pissed!"
        mike.say "What do you mean?"
        mike.say "Are you going to her in or not?"
        "Kleio shakes her head at this."
        show kleio angry
        kleio.say "She's a snake in goth's clothing, Loverboy!"
        kleio.say "It might not be obvious to someone with a cock."
        kleio.say "But if you've got a cunt, you can always spot another cunt!"
        kleio.say "All she ever wanted was to get back in with us."
        show kleio upset
        "I can't believe what Kleio's saying."
        "Because Amy seemed one hundred percent genuine to me."
        mike.say "So..."
        mike.say "I take it that's a no?"
        show kleio angry
        kleio.say "What do you think, Loverboy?!?"
        show kleio upset
        "I nod, reluctantly accepting Kleio's decision."
        if 'band_harem_amy_event_09' not in DONE and 'band_harem_amy_event_10' not in DONE:
            mike.say "I suppose you're going to tell the others too?"
            "To my surprise, Kleio shakes her head at this."
            show kleio angry
            kleio.say "No way!"
            kleio.say "We're a democracy."
            kleio.say "You go ask them and get their answers."
            kleio.say "And whatever they are, the majority wins."
        $ kleio.flags.amy_accepted = False
    return

label band_harem_amy_event_09:
    if 'band_harem_amy_event_08' in DONE and 'band_harem_amy_event_10' not in DONE:
        "The next target on my list of band-members to question is Anna."
        "Probably because I'm still reeling from speaking to Kleio first."
        "And I'm anticipating that Anna will be a moment of relief."
        "At least until I have to face Sasha, who can be every bit as fierce as Kleio!"
        "But even as I start talking to Anna, there's a nagging worry in the back of my head."
        "A creeping fear that I might be underestimating the shortest member of the band."
    show anna surprised at center, zoomAt (1.25, (640, 880)) with fade
    mike.say "Anna..."
    mike.say "Can I talk to you about something?"
    show anna annoyed
    "Anna's face drops almost as soon as she hears me start talking."
    show anna worried
    anna.say "Ooh..."
    anna.say "I don't like the sound of that, [hero.name]!"
    anna.say "When someone asks to talk to me about something..."
    anna.say "Well, it's never anything good!"
    show anna annoyed
    "I put as big of a smile on my face as I can manage."
    "And then I do the best I can to ignore Anna's reaction."
    "Because if I'm going to do this, then I'm going to get through it."
    "Regardless of what gets thrown in my way."
    mike.say "Oh come on, Anna..."
    mike.say "That's a very negative thing to say."
    mike.say "You don't even know what I want to say to you yet!"
    "Anna keeps on frowning and shaking her head."
    "But seeing as how she doesn't actually say no, I press on."
    "Taking that as silent permission to make my point."
    mike.say "Anyway..."
    mike.say "You remember that great time we had with Amy at the water-park the other day?"
    show anna normal
    "At the mention of this, Anna's mood seems to improve a little."
    "She nods and even cracks a bit of a smile."
    show anna evil
    anna.say "Oh yeah..."
    anna.say "Of course I do!"
    anna.say "That was more fun than I thought it'd be."
    show anna normal
    "The change in Anna's mood makes me feel even more confident."
    "And so I decide to go for broke, telling her what I wanted to ask."
    mike.say "Well, Anna..."
    mike.say "It turns out that Amy had a lot of fun too."
    mike.say "So much fun, in fact, that she wants to reconnect with you guys."
    mike.say "Specifically, she wants you guys to let her back into the band..."
    "I wait for the words to sink in, watching Anna's face the whole time."
    "And for a short while, she seems to be totally dumbfounded by the statement."
    show anna surprised
    "But then her face twists into an expression of surprise."
    anna.say "You mean..."
    anna.say "She wants back into the band?"
    anna.say "Our band?"
    anna.say "I mean...I know she used to be in it...so then it was her band too."
    anna.say "But she's not anymore...so now it's our band!"
    mike.say "Calm down, Anna!"
    mike.say "She just wants a yes or no answer, that's all."
    mike.say "Will you let Amy back into The Deathless Harpies?"
    if amy.flags.peace_with_anna or anna.love >= 180 or anna.sub >= 100:
        show anna normal at center, zoomAt (1.0, (640, 880)), vshake
        "Suddenly Anna's nodding her head up and down."
        "And so violently that I'm worried she's going to injure herself."
        show anna happy
        anna.say "Oh yes..."
        anna.say "That's a great idea!"
        anna.say "Why didn't I think of that?"
        "Anna's enthusiasm comes out of nowhere."
        "But like most of her emotions, it's genuine and powerful."
        "As well as being almost impossible to resist."
        mike.say "So you think it's a good idea?"
        mike.say "You'd be up for letting her back into the band?"
        show anna evil
        anna.say "Of course I would, [hero.name]."
        anna.say "I had such a good time with her at the water-park."
        anna.say "So good that I haven't been able to stop thinking about her!"
        anna.say "Oh, and remembering the time we slept together as well..."
        show anna blush
        "Anna seems to drift off as she recalls that particular incident."
        "And for a moment I want to question her on the specifics of it too."
        "But then I remember the task at hand."
        "And I regretfully try to get her back on the same page as me."
        mike.say "That's great, Anna."
        if 'band_harem_amy_event_08' not in DONE and 'band_harem_amy_event_10' not in DONE:
            mike.say "I have to talk to Kleio and Sasha too."
            mike.say "But I'm sure they'll be on board as well."
        $ anna.flags.amy_accepted = True
    else:
        show anna unpleased at center, zoomAt (1.0, (640, 880)), hshake
        "Suddenly Anna's shaking her head from side to side."
        "And so violently that I'm worried she's going to injure herself."
        show anna angry
        anna.say "Oh no..."
        anna.say "No, no, no..."
        anna.say "I know why she made you ask me!"
        show anna unpleased
        "I can't fathom what Anna could mean by that."
        mike.say "Anna, what are you talking about?"
        show anna angry
        anna.say "This is because I slept with her, isn't it?"
        anna.say "Because I showed that one moment of weakness..."
        anna.say "Amy thinks she can control me for the rest of my miserable life!"
        show anna unpleased
        "I don't really know what I was expecting Anna's reaction to be."
        "But I'm damn sure it wasn't what I'm seeing right now."
        "And I feel like I have to calm her down before she gets hysterical."
        mike.say "Anna..."
        mike.say "Anna, stop it!"
        mike.say "I'm sure that's not the reason."
        "Anna's still shaking her head."
        "And I'm not even sure she's hearing what I have to say."
        show anna angry
        anna.say "You tell her to stop it, [hero.name]."
        anna.say "Tell her that she's not welcome in the band too!"
        show anna unpleased
        "I feel like there's more to be said on the matter."
        "But Anna's just working herself up more by the second."
        "So I decide that the best thing to do is let the matter drop."
        mike.say "Okay, Anna..."
        mike.say "Let's forget about it."
        mike.say "And I'll just mark you down as a no."
        $ anna.flags.amy_accepted = False
    return

label band_harem_amy_event_10:
    "Talking to Sasha about Amy getting back into the bad is a pretty scary prospect."
    "But I figure that this is going to be like pulling a plaster off a wound."
    "Tear it off quickly and endure the pain, rather than going slow and making it last."
    show sasha at center, zoomAt (1.25, (640, 880)) with fade
    "So as soon as I see Sasha, I take a deep breath and prepare to bring up the subject."
    mike.say "Sasha..."
    mike.say "I've got to talk to you about something."
    "Sasha doesn't seem to react to the statement with any immediate suspicion."
    "In fact she looks pretty casual as she looks up in response to my words."
    show sasha shout
    sasha.say "You do?"
    sasha.say "Look, [hero.name]..."
    sasha.say "If this is about what I caught you doing with my underwear..."
    sasha.say "I already told, you it's okay!"
    show sasha normal
    mike.say "Erm..."
    mike.say "Thanks again, Sasha..."
    mike.say "But it's not about that."
    "Now I can see the interest beginning to shine in Sasha's eyes."
    "And she raises her eyebrows as she starts to question me about the matter."
    show sasha shout
    sasha.say "Oh?"
    sasha.say "Then what is it about?"
    show sasha normal
    "I take a deep breath, trying to steel my nerves for what lies ahead."
    "And then I take my life into my hands, broaching the subject."
    mike.say "You remember the other day at the Amusement Park?"
    show sasha joke
    sasha.say "Which day was that?"
    sasha.say "The one where Amy showed up and we nearly had a fight?"
    sasha.say "Or the one where we went back and you invited her along too?"
    show sasha annoyed
    "I can feel myself flushing as Sasha reminds me of what actually happened."
    "And the way I went ahead and tricked her into meeting up with Amy again."
    mike.say "Oh come on, Sasha..."
    mike.say "You know very well why I did that."
    mike.say "And it wasn't as bad as you're making it out to be either!"
    show sasha normal
    "The look on Sasha's face changes, becoming more humble."
    "And she gives me a nod, acknowledging that I'm right."
    show sasha shout
    sasha.say "Alright, [hero.name]..."
    sasha.say "I'll give you that one."
    sasha.say "I was pretty nice to be able to meet Amy on neutral ground."
    sasha.say "To catch up and chat about old times together."
    show sasha normal
    mike.say "Well, you know what, Sasha..."
    mike.say "Amy feels the same way too."
    mike.say "So much so that she wanted to ask you something."
    mike.say "She wanted to ask if she could get back into the band?"
    if amy.flags.peace_with_sasha or sasha.love >= 180 or sasha.sub >= 100:
        "The moment I mention the idea, Sasha's expression changes to one of amazement."
        show sasha surprised at center, zoomAt(1.5, (640, 1040)) with vpunch
        "She almost gapes at me, shaking her head in disbelief."
        sasha.say "Are you fucking with me?!?"
        sasha.say "She actually said that?"
        "I note that Sasha's also taken hold of my shirt."
        "And she's using it to pull me down to her level."
        mike.say "Erm..."
        mike.say "Yeah, Sasha..."
        mike.say "Why would I make something like that up?"
        "Sasha suddenly lets go of me."
        show sasha annoyed at center, zoomAt(1.25, (640, 880)) with vpunch
        "And I stagger backwards, trying to regain my balance."
        mike.say "Urgh..."
        mike.say "She asked me to go round each of you, everyone in the band."
        mike.say "You know, and ask that same question?"
        show sasha normal
        "Now Sasha's nodding, like it's all starting to make sense."
        show sasha shout
        sasha.say "Of course..."
        sasha.say "I should have known she was behind this."
        sasha.say "You need a woman's mind to organise something like this."
        sasha.say "And you're just a guy, no offence, [hero.name]."
        show sasha normal
        mike.say "I...I guess not, Sasha..."
        mike.say "Wait a minute..."
        mike.say "What was all that 'just a guy' stuff?!?"
        "I ask the question, but it doesn't do me any good."
        "Because Sasha's already off on another line of thought entirely."
        show sasha shout
        sasha.say "This'll mean so much new stuff we can do with the band."
        show sasha wink
        sasha.say "Plus it's another girl to party with after gigs!"
        show sasha normal
        mike.say "So I take it that's a yes from you?"
        show sasha happy
        sasha.say "Oh..."
        sasha.say "Yeah, yeah - I'm a yes!"
        $ sasha.flags.amy_accepted = True
    else:
        show sasha angry
        "The moment I mention the idea, Sasha's expression hardens."
        "She frowns at me, shaking her head in disapproval."
        show sasha vangry
        sasha.say "So that's what this was all about?"
        sasha.say "That scheming bitch was just trying to worm her way back in with us!"
        sasha.say "And to think, I nearly fell for it."
        show sasha angry
        "By now I'm shaking my head too."
        "The difference is that I'm trying to change Sasha's mind."
        mike.say "No, Sasha..."
        mike.say "That's not how it is at all."
        mike.say "You think I'd have helped Amy out if it were?"
        show sasha sadsmile
        "Sasha looks at me with something approaching pity in her eyes."
        "Like I don't really understand the meaning of the words I'm using."
        show sasha whining
        sasha.say "Oh, [hero.name]…"
        sasha.say "Of course you'd think that."
        sasha.say "You're just a poor, dumb guy."
        sasha.say "And a girl like Amy can wrap you around her little finger."
        show sasha sad
        mike.say "I..."
        mike.say "Wait...what?"
        mike.say "How could that even happen?"
        show sasha sadsmile
        "Sasha gives me that same pitying look again."
        "Then she places a gentle kiss on my cheek."
        show sasha shout
        sasha.say "It's okay, [hero.name]…"
        sasha.say "It's not your fault that you think with your dick."
        sasha.say "And you leave Amy to me, Kleio and Anna."
        sasha.say "We'll make sure she never exploits you like that again!"
        show sasha sadsmile
        mike.say "Erm..."
        mike.say "Thanks..."
        mike.say "I think..."
        $ sasha.flags.amy_accepted = False
    return

label band_harem_amy_event_11:
    scene bg studio with fade
    "Now that all of the running around is over, I kind of feel too exhausted for it all to really sink in."
    "Somehow I managed to discover that Amy used to be a member of The Deathless Harpies."
    "Then set her and all of the girls up to spend time together and heal their relationships."
    "And even more, I brokered a deal for Amy to get back into the band with them all individually."
    "I kind of feel like I single-handedly changed the course of history within the past few days!"
    with fade
    "But now we're all at the studio, waiting for Amy to turn up."
    "This is going to be her first time back here since she left the band the last time."
    "And it was supposed to be just a kind of casual thing, you know?"
    "Amy moving some of her gear back in here and meeting us all together."
    "Yet that doesn't seem to be the message that the girls have gotten."
    "One by one they troop into the practice-room, carrying stuff that's not music-related."
    show sasha casual at center, zoomAt(1.25, (740, 880)) with easeinright
    "Sasha and I arrived together, with her lugging a slab of beer."
    "And with me shooting her sideways glances the whole time."
    mike.say "Don't we already have beers in the fridge, Sasha?"
    mike.say "I mean, there's never any room for a bottle of water in there!"
    mike.say "It's all either alcohol or energy drinks."
    show sasha shout
    sasha.say "You can never have too much beer, [hero.name]."
    show sasha happy
    sasha.say "That's part of the rockstar lifestyle."
    show sasha normal
    mike.say "If you say so..."
    mike.say "Sometimes I think you're going to start sweating it out of your pores!"
    show sasha happy at center, zoomAt(1.25, (340, 880)) with ease
    "Sasha lets out a derisive laugh as she puts the slab down atop the already full fridge."
    $ renpy.sound.set_pan(1, 0, channel='sound')
    play sound door_open
    show sasha stuned
    "And then she turns at the sound of the door opening, pretty much on our heels."
    kleio.say "You fuckers brought beer?!?"
    kleio.say "Talk about turning up to a gunfight with a knife!"
    show sasha normal
    show kleio casual punk at center, zoomAt(1.25, (1040, 880)) with easeinright
    "At the sound of Kleio's voice, I turn around too."
    "The first thing I notice is that she has a bottle of whiskey in each hand."
    "And she's waving them over her head like a cheerleader waves her pom-poms."
    sasha.say "Shit..."
    sasha.say "I wish I'd thought of that!"
    mike.say "First beer and now whiskey?"
    mike.say "This is getting out of hand before it's even started!"
    show kleio happy at startle
    "Kleio lets out a derisive snort of laughter."
    show kleio normal
    "And she looks me up and down, like she's seeing me for the first time."
    show kleio talkative
    kleio.say "What's the matter, Loverboy?"
    kleio.say "Since when were you a member of the anti-fun police?"
    show kleio normal
    show sasha shout
    sasha.say "Ah, just ignore him."
    sasha.say "He's got his panties in a twist for some reason I can't figure."
    show sasha normal
    mike.say "Hey!"
    mike.say "I just think that..."
    play sound door_slam
    "I'm cut off by the sound of the door slamming against the wall."
    scene bg studio at center, zoomAt(1.5, (330, 1040))
    show anna casual at flip, center, zoomAt(1.5, (1140, 1040))
    with fade
    "And all three of us look around to see Anna in the doorway."
    "Or to be more precise, we see the top of her head."
    "As she's struggling under the weight of ever more booze!"
    "I hurry to help, relieving her of most of it before she keels over."
    scene bg studio
    show anna b worried at center, zoomAt(1.25, (940, 880))
    "But that doesn't seem to do anything to relieve the look of concern on her face."
    mike.say "What's the matter, Anna?"
    mike.say "You look like you have the weight of the world on your shoulders."
    "Anna glances over at the alcohol Sasha and Kleio brought with them."
    "And then she looks back at what she's just hauled into the room herself."
    "All the time she's shaking her head too."
    anna.say "Oh dear..."
    anna.say "It's all of this booze, [hero.name]!"
    mike.say "I know, Anna..."
    mike.say "I think everyone got a little carried away."
    anna.say "Oh no, that's not it at all."
    anna.say "I'm worried there won't be enough!"
    "I stare at Anna open-mouthed, not believing what I just heard."
    "And I'm about to say something in return."
    "But then I realise that everyone else is now staring at the door again."
    "So feeling like I'm being blown by an ever-changing wind, I turn that way too."
    $ renpy.sound.set_pan(0, 0, channel='sound')
    scene bg studio at center, zoomAt(1.5, (330, 1040))
    show amy casual at center, zoomAt(1.5, (640, 1040))
    with fade
    "I'm greeted by the sight of Amy, standing in the doorway with a guitar and amp."
    show amy happy
    amy.say "Raised voices and stacks of booze, huh?"
    amy.say "That's just how I remember it!"
    show amy normal
    hide amy with easeoutleft
    "As one, the girls rush towards Amy, pulling her into the room."
    "There's no way I could get in there, even if I tried."
    "So instead I stand back and watch the whole thing unfold."
    scene bg studio
    show amy at center, zoomAt(1.25, (640, 880))
    show anna at center, zoomAt(1.25, (940, 880))
    show kleio at center, zoomAt(1.25, (440, 880))
    show sasha at center, zoomAt(1.25, (240, 880))
    with fade
    "Everyone seems to be talking at once as they usher her into middle of the floor."
    "And I can see from the look on her face that Amy's more than a little overwhelmed."
    "But at the same time she also has a light in her eyes that tells me she's happy."
    "Which makes sense, as she's coming home to her friends and her band."
    "Being carried along on a smothering, yet comforting river of affection."
    show sasha shout at startle
    sasha.say "Is that a new amp and guitar?"
    sasha.say "You gotta show how they sound?"
    show sasha normal
    show kleio talkative at startle
    kleio.say "That shit looks heavy..."
    kleio.say "Let me help you find a place for it."
    show kleio normal
    show anna talkative at startle
    anna.say "You look thirsty, Amy!"
    anna.say "I'll go get you something to drink..."
    show anna normal
    hide sasha
    hide kleio
    with easeoutleft
    hide anna with easeoutright
    "The three of them hurry off to make good on their promises."
    "Which leaves Amy standing alone for a moment."
    show amy at center, traveling(1.5, 0.3, (640, 1040))
    "So I take the chance to walk over and stand by her side."
    mike.say "This has got to be super-weird, right?"
    show amy happy
    amy.say "You got that right!"
    amy.say "But in a good way, you know?"
    show amy normal
    "I nod, enjoying the positive vibes that are filling up the room right now."
    "Once the girls have made space for Amy, all of her gear is safely stashed in it."
    "And then Anna makes good on her promise, hurrying over with an armful of beers pressed against her chest."
    show anna a sadsmile at center, zoomAt(1.5, (940, 1040)) with easeinright
    anna.say "Brrr..."
    show anna worried
    anna.say "Hurry up and grab these things, you guys..."
    anna.say "They're so cold I'm freezing my tits off!"
    show anna b normal with fade
    "Everyone does as they're told, cracking them open and taking a drink."
    "Which is when I take the chance to hold mine up in the air."
    mike.say "Ahem..."
    mike.say "I'd like to take this opportunity to welcome Amy back into the fold."
    mike.say "And I think I speak for us all..."
    show kleio talkative at center, zoomAt(1.5, (340, 1040)) with easeinleft
    kleio.say "Speak for yourself, Loverboy!"
    show kleio normal
    mike.say "I said, I think I speak for us all when I say..."
    mike.say "We're all thrilled to have you back too!"
    show sasha at center, zoomAt(1.5, (240, 1040))
    show kleio at center, zoomAt(1.5, (520, 1040))
    show anna a sadsmile at center, zoomAt(1.5, (1040, 1040))
    show amy at center, zoomAt(1.5, (760, 1040))
    with easeinleft
    pause 0.2
    with hpunch
    "Everyone slams their beers together to show their support."
    "Which means that the stuff goes everywhere."
    show anna evil
    amy.say "Urgh..."
    amy.say "Covered in wet, sticky shit..."
    amy.say "Just like old times in the band!"
    show anna happy
    show sasha happy
    show kleio happy
    show amy happy
    "Everyone laughs at this, and the atmosphere feels pretty much perfect."
    "After that we find ourselves hanging out in the practice-room."
    "There's no clear plan or direction to any of it."
    "We're just a bunch of friends, drinking and catching up with each other."
    "But even as I float from one person to the next, I know there's one of the girls I want to talk to in particular."
    scene bg studio
    show amy at center, zoomAt(1.25, (640, 880))
    with fade
    "It takes a while for me to be able to get Amy on her own."
    "Because obviously everyone wants to talk to the newly-returned member of the band."
    show amy at center, traveling(1.5, 0.3, (640, 1040))
    "But as soon as I do, I notice that she's hurrying towards me too."
    mike.say "Hey, Amy..."
    mike.say "I've been trying to get to talk to you for what feels like an age!"
    show amy shy
    amy.say "Me too, [hero.name]!"
    amy.say "I've wanted to have some time with you since I walked in here."
    show amy normal
    "I can't help feeling a sense of warmth inside of me as Amy admits as much."
    "That in the middle of all of this, she was thinking of me in particular."
    mike.say "Well, this is kind of for you, Amy."
    mike.say "I guess I should learn to share you!"
    "Amy shakes her head at this."
    show amy happy
    amy.say "Don't be so modest, [hero.name]."
    amy.say "Without you, none of this would have happened."
    amy.say "And I think that means you deserve a reward..."
    show amy normal
    mike.say "I do?"
    mike.say "What did you have in mind?"
    "Before I can say anything more, Amy gives me her answer."
    hide amy
    show amy kiss
    with hpunch
    "Which is to pull me in and plant her lips squarely on mine."
    "For a moment, my eyes are wide-open in sheer amazement."
    "But then I feel myself melting into the kiss."
    "And before I know it, Amy and I are wrapped up in each other's arms."
    kleio.say "Way to go, Loverboy!"
    sasha.say "You go, Amy - ride that stud!"
    anna.say "Oh yeah, just like old times!"
    "Amy and I stop for a moment, tongues still stuck deep in each other's mouths."
    "Our eyes looking this way and that as we see that the other's are surrounding us."
    hide amy kiss
    show anna at mostleft4
    show amy at left4
    show kleio at right4
    show sasha at mostright4
    "For a moment I think that we're just going to get cheered on by the three of them."
    "But then they come closer still, and I feel their hands on my body."
    "Are they..."
    "They are!"
    "Anna, Kleio and Sasha are actually pulling off my clothes!"
    "I'm about to protest, when I see they're doing the same thing to Amy."
    "Our eyes meet, and I see her kind of shrug, like it doesn't really bother her."
    show amy naked
    "I have to admit that by this time I've had more than a couple of drinks."
    "And I can feel the effect they're having on me too."
    "Because all I need to see is that nonchalant shrug from Amy."
    "From that point on I decide that I don't really give a fuck either."
    "So as the others efficiently strip-off our clothes, we get right on with it."
    "Soon enough I can feel Amy's warm, naked skin against my own."
    "And the fact that we're not alone doesn't matter one bit."
    "After all, we're bandmates."
    "And we have nothing to hide from each other."
    "As soon as we're both naked, I reach down and pick Amy up."
    scene bg black
    show fivesome amyannakleiosasha noanna nokleiosasha
    with fade
    "Hands under her ass, I carry her over to the nearest speaker."
    "Then I deposit her on top of it."
    "Amy obliges by wrapping her ample thighs around me."
    "But she takes me by surprise, pulling me close with unexpected strength."
    show fivesome amyannakleiosasha -nokleiosasha
    "I don't have time to make a sound before I'm pressed up against her."
    "Again, Amy clamps her lips over mine and thrusts her tongue in there."
    "At the same time, I feel the urge to do a similar thing to her."
    "So I pull her towards me as I thrust myself forwards."
    show fivesome amyannakleiosasha -noanna
    "There's nowhere else for my now extremely hard cock to go."
    "And Amy moans as I rub the head against the lips of her pussy."
    show fivesome amyannakleiosasha vaginal at startle(0.05,-10)
    "Soon enough they part, just like the lips of her mouth."
    "As soon as they do, I begin to thrust with renewed strength."
    show fivesome amyannakleiosasha at startle(0.05,-10)
    "I must make it all the way into her in no more than two movements."
    show fivesome amyannakleiosasha closed pleasure
    "Amy keeps on kissing me the whole time, gasping and moaning around my tongue."
    show fivesome amyannakleiosasha at startle(0.05,-10)
    "And that only makes me all the more determined to pound her harder than ever."
    "I can vaguely hear the others, making lewd comments and cheering us on."
    show fivesome amyannakleiosasha at startle(0.05,-10)
    "But Amy's the centre of my attention, consuming all of my energies."
    "Her legs are wrapped around my waist, her buttocks cupped in my hands."
    show fivesome amyannakleiosasha at startle(0.05,-10)
    "And I know that I'm not going to be able to stop until we both cum."
    show fivesome amyannakleiosasha opened pleasure
    amy.say "Oh fuck..."
    amy.say "I...I can't..."
    show fivesome amyannakleiosasha ahegao creampie with vpunch
    "I feel Amy start to lose it the moment before I do."
    with vpunch
    "She clings onto me as if her life depends on it, nails scraping my back."
    with vpunch
    "And she takes everything that I have to give before it's over."
    "Slumping forwards onto me once I'm done, her body suddenly going limp."
    $ amy.sexperience += 1
    $ amy.love += 2
    $ anna.love += 2
    $ kleio.love += 2
    $ sasha.love += 2





































































































































































































































    "The sensation of coming around afterwards is almost like waking from a dream."
    "Suddenly I'm cold, uncomfortable and aware of the fact there are quite a few eyes on me."
    "But as I scramble to get dressed, I soon realise that nobody is looking at me with disapproval."
    "In fact everyone else seems to be more than a little dishevelled and lacking certain items of clothing too."
    "So it seems that I wasn't the only one who indulged themselves here today!"
    scene bg studio
    show anna at mostleft4
    show amy at left4
    show kleio at right4
    show sasha at mostright4
    with fade
    "The party goes on for a little longer, with more booze being consumed along the way."
    "There are even some seriously crazy moments with dares and challenges between all of us."
    "I just hope that I remember all of them when I wake up in the morning."
    "Because I get the sense my head's going to feel like there's a roadie living in it!"
    return

label amy_anna_kleio_sasha_male_ending:


    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding
    with fade
    "The feeling as I'm standing there in the chapel is pretty hard to explain."
    "At least hard to explain to anyone that can't see inside of my head right now."
    "Because the past few months have been like a roller-coaster for me."
    "Both in terms of my personal and professional lives, and all because of the band."
    "But then I guess it's long overdue time that I admitted those are both the same thing!"
    "After all, I am waiting on the arrival of four girls right now."
    "All of whom I'm going to be marrying."
    "And all of whom are in the band with me too!"
    "Since I convinced the girls to let Amy back into the band, everything's fallen into place."
    "The Deathless Harpies have got a new energy about them, with which we won the Battle of the Bands."
    show bus_tour
    show fg dreamy as foreground
    with dissolve
    "And from that we landed ourselves a world tour, just as we were blowing up online too."
    show concert solo anna
    show fg dreamy as foreground
    with wipeup
    "Since then we've been around the globe, playing in front of ever bigger crowds of adoring fans."
    show concert solo amy
    show fg dreamy as foreground
    with wiperight
    "In fact, I'm amazed we've been able to find the time to arrange what's happening today."
    show concert solo sasha
    show fg dreamy as foreground
    with wipedown
    "The chapel is crammed full of the band's closest friends and family."
    show concert solo mike
    show fg dreamy as foreground
    with wipeleft
    "Which is crazy, when you consider that there's five of us!"
    show concert solo kleio
    show fg dreamy as foreground
    with irisin
    "Part of me thinks that we could have made more out of this."
    scene concert
    show concert anna kleio sasha amy
    show fg dreamy as foreground
    with dissolve
    "Like, booked an entire bloody stadium and sold tickets to fans."
    "But we're doing this in the short amount of time we have open to us."
    show studio with dissolve
    "We just got off the world tour, and next we have to be in the studio to record a new album."
    "So this is all that we were able to organise in that narrow window available to us."
    "But that doesn't mean we weren't able to make it our own."
    scene bg church wedding
    with fade
    "Let me explain..."
    "It might seem quite old-fashioned that I'm the one standing here at the altar."
    "But we all agreed that I was the one that kind of served as the catalyst for all of this."
    "My joining the band was the first shot in the arm that started our inevitable rise."
    "And on top of that, I was the one that got the others to take Amy back into the band."
    "But all that really did was get me top billing at the start of the ceremony."
    "Each of the girls is going to get their own entrance, their own moment in the spotlight."
    "And it's not like they're all just marrying me."
    "Every member of the band is getting wed to the others."
    "We're more than a band, we're more like a romantic collective."
    "And we come as a package deal - you get one of us and the other four are included in the deal."
    "But before you go thinking that I'm the ringmaster of this whole show..."
    play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
    "Let me tell you that I have no idea what order the girls are coming out in!"
    "And just like that, I hear the sound of raucous punk music filling the air."
    "I turn to look at the chapel doors, knowing just who to expect."
    show kleio wedding
    "Kleio struts in a moment later, as cocky and confident as ever."
    "And my eyes are on her the whole time as she swaggers down the aisle."
    if kleio.is_visibly_pregnant:
        "I'm also in love with the way she makes no effort to hide her pregnant belly too!"
        "In fact, Kleio almost shoves it in the faces of the guests as she walks past them."
        "And I'm so proud of how she turns everything into a show of defiance."
    else:
        "I'm so proud of the way Kleio turns everything into a show of defiance."
        "Almost like she's going to start giving everyone the middle-finger next!"
    show kleio at mostleft4 with move
    "Once she reaches my side, Kleio nods in my direction."
    "Almost like she's now challenging me too!"
    mike.say "Hey, Kleio..."
    mike.say "You look awesome!"
    show kleio happy
    kleio.say "Of course I do, Loverboy!"
    kleio.say "And you scrub up pretty well yourself."
    "I'm about to fire off another smart-ass remark in Kleio's direction."
    "But then I hear an exquisite guitar solo begin to play."
    show sasha wedding
    "And we both look back to see Sasha walking down the aisle."
    "If Kleio's walk was a protest, then Sasha's is one of triumph."
    "Like the true lead guitarist she is, Sasha makes sure all attention is on her."
    if sasha.is_visibly_pregnant:
        "The cut of her dress perfectly accommodates the curve of her pregnant belly."
        "And if that draws any disapproving looks from the guests, then I don't see them myself."
        "Because I'm far too busy admiring Sasha as she walks towards me."
    else:
        "And it stays that way all the time Sasha is walking the aisle."
        "In that space of time, all eyes are on her alone."
    "As she gets to the altar, I finally recognise the music playing."
    show sasha at mostright4 with move
    mike.say "Sasha..."
    mike.say "Is that...is that you?!?"
    show sasha happy
    "Sasha smiles and nods her head."
    sasha.say "Who else is good enough to play me down the aisle?"
    kleio.say "Typical guitarist!"
    "My mouth is open to say something else."
    "But then a far more bouncy, lively tune starts to play."
    "It's still metal for sure, but this is full of fun."
    "Which means that it can only be Anna's choice of music."
    show anna wedding
    "A moment later my suspicions are confirmed, as she hurries into view."
    "Where Kleio and Sasha strutted, Anna almost dashes down the aisle."
    "And she's waving to us the whole time too, a total ball of energy."
    if anna.is_visibly_pregnant:
        "I'm relieved to see that Anna's holding onto her belly."
        "Because she's really starting to show now."
        "And I'm always worried about keeping her and the baby as safe as possible."
    else:
        "In fact Anna's moving so quickly that I'm worried she's going to trip and fall."
        "She seems to be rushing in an effort to get here as fast as she possibly can!"
    show anna happy at right4 with move
    anna.say "Hey, guys!"
    anna.say "I am SO pumped for this!"
    "Sasha and Kleio share an amused look."
    "But Anna doesn't seem to notice."
    "And I only see it out of the corner of my eye."
    "Because I'm too busy beaming back at Anna to pay much attention."
    "But before I can say a word to Anna, I hear more music beginning to play."
    "This time it's distinctly goth in nature, which can only mean one thing."
    show amy wedding
    "All four of us turn in time to see Amy stride into the chapel."
    "And we all watch as the Goth princess of the band makes her entrance."
    if amy.is_visibly_pregnant:
        "For once I'm relieved that Amy's made concessions in terms of what she's wearing."
        "Because there's no corset or tight clothing around her visibly pregnant belly."
        "But apart from that she looks amazing, a vision of Gothic beauty."
    else:
        "I always love the fact that Amy's the one Goth in the band."
        "A fact that makes her unique even amongst a bunch of weirdos like us."
    show amy at left4 with move
    kleio.say "You too your time, Goth Barbie!"
    show amy happy
    amy.say "That's because I'm worth waiting for!"
    "Anna, Sasha and I are enjoying the verbal jousting going on in front of us."
    "And I'm sure there's a line or two that the other girls are waiting to drop."
    "But then we get a firm reminder of just where we are right now."
    "Priest" "Ahem..."
    show kleio normal
    show anna normal
    show sasha normal
    show amy normal
    "As one, the entire band snaps to attention."
    "And we all turn to face the priest."
    "Priest" "Sometimes I think I'm in the crowd control business..."
    "Priest" "Rather than the one of marrying people!"
    "Priest" "Now if you wouldn't mind getting into your allotted places?"
    "Anna, Amy, Kleio, Sasha and I all scurry here and there."
    "Only stopping once we're in the positions that we've practiced."
    "Then the priest begins the ceremony in earnest."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join the members of..."
    "Priest" "I can't believe I'm saying this..."
    "Priest" "The members of The Deathless Harpies, in the bonds of holy matrimony."
    "I have to say that I'm impressed by the priest's memory."
    "He's marrying five people today, but he's totally on the ball."
    "Priest" "Do you, Amy..."
    "Priest" "Take Anna, Kleio, Sasha and [hero.name]..."
    "Priest" "To be your lawful, wedded partners?"
    show amy happy at startle(0.2, 5)
    amy.say "I do."
    show amy normal
    "Priest" "Do you, Anna..."
    "Priest" "Take Amy, Kleio, Sasha and [hero.name]..."
    "Priest" "To be your lawful, wedded partners?"
    show anna happy at startle(0.2, 5)
    anna.say "Of course I do!"
    show anna normal
    "Priest" "Do you, Kleio..."
    "Priest" "Take Amy, Anna, Sasha and [hero.name]..."
    "Priest" "To be your lawful, wedded partners?"
    show kleio happy at startle(0.2, 5)
    kleio.say "You're damn right I do!"
    show kleio normal
    "Priest" "Do you, Sasha..."
    "Priest" "Take Amy, Anna, Kleio and [hero.name]..."
    "Priest" "To be your lawful, wedded partners?"
    show sasha happy at startle(0.2, 5)
    sasha.say "I do."
    show sasha normal
    "When the priest turns to me, I can see he's already flagging."
    "The exertion of a five-person ceremony clearly telling on him."
    "Priest" "And finally, do you, [hero.name]..."
    "Priest" "Take Amy, Anna, Kleio and Sasha..."
    "Priest" "To be your lawful, wedded partners?"
    mike.say "I do."
    show amy happy at startle(0.05, -10)
    show anna happy at startle(0.03, -8)
    show kleio happy at startle(0.07, -4)
    show sasha happy at startle(0.04, -11)
    "The priest nods and then turns to face the assembled guests."
    "Priest" "I call upon those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "Why these people may not be joined in matrimony..."
    "Priest" "Speak now, or forever hold you peace!"
    show amy normal
    show anna normal
    show kleio normal
    show sasha normal
    "There's the usual pause and ripple of nervous laughter from the guests."
    "But for me this is actually a pretty tense moment of waiting it out."
    "Because there are five of us up here right now."
    "And each of us has a colourful story to tell as to how we got here."
    "Even thinking about it for the briefest of moments causes me to recall scenes and incidents."
    "Enough to send me on a short and sweet trip down memory lane as I remember our collective past."
    "But thankfully, none of the skeletons in our collective closet come popping out."
    "Priest" "Very well..."
    "Priest" "By the power vested in me..."
    "Priest" "I pronounce you all married to each other."
    "Priest" "Normally I'd tell you to kiss your partner."
    "Priest" "But in this case, I'll just leave you to your own devices!"
    show amy happy
    show anna happy
    show kleio happy
    show sasha happy
    "It's not like any of us really needed the guy to tell us what to do anyway."
    "Without a word, everyone throws their arms around everyone else."
    "This results in a chaotic, five-way hug that shows no signs of stopping."
    "Within it, kisses are exchanged every which way possible."
    "And it's hard to tell who's saying what to who and if they're being heard."
    "But that's kind of how we roll, you know?"
    "To anyone on the outside, it looks like sheer chaos."
    "Yet from the inside looking out, it's all about that chaotic energy."
    "That's what makes us a world-famous band, and a loving collective too."
    "Nothing's going to change that."
    "And the world's going to have to accept us for who we are."
    "Or else everyone else in it can kiss our asses and go to hell."
    "Because we're The Deathless Harpies, baby..."
    "And we're the incarnation of Rock and Roll!"

    scene bg black
    show band amy ending
    kleio.say "You guys can just relax and leave this to me."
    kleio.say "After all, I am the lead singer of the band."
    anna.say "Hey, Kleio..."
    anna.say "That's not fair!"
    sasha.say "She's right, Kleio..."
    sasha.say "There are four of us in the band, apart from [hero.name]."
    sasha.say "And we all have something to say too!"
    amy.say "And some of have mouths almost as big as yours, Kleio..."
    amy.say "So you just try to keep us quiet, and see how far that gets you!"
    kleio.say "Urgh..."
    kleio.say "You guys are as bad as Loverboy himself..."
    kleio.say "Always trying to shut me up!"
    anna.say "That's not fair, Kleio!"
    anna.say "If it wasn't for [hero.name], then we wouldn't be where we are today!"
    kleio.say "What are you talking about, Anna?"
    kleio.say "The Deathless Harpies were around before he came along."
    kleio.say "And it's not like he taught any of you guys to play either!"
    sasha.say "Cut the bullshit, Kleio..."
    sasha.say "You know what she means as well as I do."
    sasha.say "We were good before [hero.name] joined the band."
    sasha.say "But after he did, we all got a lot better."
    kleio.say "What about Amy, yeah?"
    kleio.say "We knew her long before we knew him."
    amy.say "And what about me, huh?"
    amy.say "I'd been in the band and got my ass kicked out."
    amy.say "[hero.name] was the one that mended all of our bridges."
    amy.say "He got us all back on the same page."
    kleio.say "Okay, okay..."
    kleio.say "Maybe I was being a little hard on him just now."
    kleio.say "But you know how guys are - you got to keep them on their toes!"
    sasha.say "What, just like we have to with you?"
    sasha.say "But you've got to admit, [hero.name]'s the thing that holds it all together."
    anna.say "Yeah, Sasha..."
    anna.say "Like, he's the gum stuck to the sole of your shoe!"
    amy.say "I think she means more like he's the glue that holds up together, Anna!"
    anna.say "Oh..."
    anna.say "Oh yeah - that is a better way of saying it!"
    kleio.say "Alright, so I admit it, we need him."
    kleio.say "But he needs us too!"
    sasha.say "[hero.name]'s brought us all together as more than a band too."
    sasha.say "Like, we're a unit too - almost a commune, you know?"
    sasha.say "And I think that's what made us able to win the Battle of the Bands."
    sasha.say "What made us go way beyond that too."
    anna.say "I know what you mean, Sasha..."
    anna.say "We've like, played on every continent and in almost every country!"
    anna.say "Lots of them I'd never even heard of before too."
    amy.say "Yet somehow we've still managed to keep it together as a family."
    if amy.pregnant:
        amy.say "Raising my girl on the road is hard."
        amy.say "But Raven's got so many people to help with that."
    if anna.pregnant:
        anna.say "Tommy's always running me in crazy circles."
        anna.say "And I know he does the same to you guys too!"
    if kleio.pregnant:
        kleio.say "I know that this is where I want Kurt to grow up."
        kleio.say "Surrounded by kick-ass female role-models."
    if sasha.pregnant:
        sasha.say "Veronica doesn't see our lives as anything unusual."
        sasha.say "And that's the way I want it to stay."
    kleio.say "Geez..."
    kleio.say "We're like a musical version of the Manson Family!"
    anna.say "Oooh..."
    anna.say "I remember that band from back in the day!"
    amy.say "She's talking about a different Manson, Anna."
    anna.say "Really?"
    anna.say "Did they make music too?"
    sasha.say "Yeah..."
    sasha.say "But trust me, you wouldn't like it."
    kleio.say "Where is Loverboy anyway?"
    kleio.say "Slacking off as usual?"
    anna.say "I think he's looking after the little ones."
    kleio.say "Does that include you, Anna?"
    anna.say "Hey!"
    sasha.say "Can't you two stop bickering for five minutes?"
    sasha.say "We're supposed to be rock stars, talking about our glamorous lifestyles!"
    amy.say "Nah..."
    amy.say "Leave them to it, Sasha."
    amy.say "That way people get an idea of what [hero.name] has to put up with!"
    kleio.say "I heard that!"
    kleio.say "Loverboy should be counting his blessings every day."
    kleio.say "Because from where I'm standing, he's the luckiest son-of-a-bitch alive!"
    sasha.say "I think we're all lucky, Kleio..."
    sasha.say "All five of us."
    amy.say "We're getting to live out our dreams."
    amy.say "Paid a fortune to make the music we love."
    anna.say "And we all have each other too..."
    anna.say "Which is worth more than all the money in the world!"
    anna.say "Right guys?"
    kleio.say "I dunno about that, Anna!"
    sasha.say "I think the money and the fame definitely help."
    amy.say "It certainly beats working at the electronics shop!"
    anna.say "Ah, screw you guys..."
    anna.say "I know [hero.name] would agree with me if he was here."
    anna.say "Not be a massive bread-head, like all of you!"
    scene bg black with dissolve
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label amy_kleio_park_threesome:
    scene bg street
    show kleio a casual at center, zoomAt (1.25, (840, 880))
    show amy a casual at center, zoomAt (1.25, (440, 880))
    with fade
    "I do the best I can to make it look like the three of us are just walking home from the pub."
    "But all the time I'm looking this way and that, tyring to spot a likely place for us to stop."
    "Because Kleio and Amy have made it pretty clear to me that they're in the mood for some action."
    "Not that they're exactly helping to maintain the illusion of innocence right now."
    "Or even helping to find a conveniently secluded spot either."
    show kleio a casual at center, traveling (1.5, 0.3, (840, 1040))
    show amy a casual at center, traveling (1.5, 0.3, (440, 1040))
    "In fact they seem more intent on making what we're up to totally obvious to anyone that see us."
    show kleio seductive
    kleio.say "Seriously, Amy..."
    kleio.say "You have to squeeze his ass - it's so fucking peachy!"
    show kleio normal
    show amy flirt
    amy.say "Hmm..."
    amy.say "Let me see..."
    show amy normal
    "Suddenly I feel someone pinching one of my buttocks."
    "And it's pretty hard too!"
    mike.say "OUCH!"
    mike.say "Hey!"
    mike.say "What do you think you're doing back there?!?"
    "For all of my protests, all I get in return is a wave of dismissal from Kleio."
    "And Amy seems to be far too enthralled with my butt to even notice."
    show kleio happy
    kleio.say "Ah, you just keep looking for somewhere we can do it, Loverboy."
    kleio.say "Amy here's only getting acquainted with the merchandise!"
    show kleio normal
    show amy happy
    amy.say "Ooh..."
    amy.say "You're right, Kleio..."
    amy.say "We never got asses this good when I was in the band!"
    show amy normal
    "I make a point of turning around, which leaves Amy bent over and looking puzzled."
    "As she was in the middle of making another grab for my, apparently, peachy ass."
    mike.say "Will you guys stop that?"
    mike.say "And maybe help me find a place we can..."
    mike.say "Well...somewhere we can..."
    show kleio annoyed
    "Kleio rolls her eyes, like I'm being totally unreasonable."
    show kleio talkative
    kleio.say "Don't be such a drama-queen!"
    kleio.say "The park's right over there, you know?"
    show kleio normal
    show amy happy
    amy.say "Agreed..."
    amy.say "That's a great place to fuck!"
    show amy normal
    "I find myself staring at the pair of them for a moment."
    "And all the while I'm wondering if there could be two less delicate girls in the entire world!"
    "But then that is one of the things that makes me want to be with them both."
    "So I just shrug my shoulders and begin walking towards the park gates."
    scene bg park with fade
    pause 0.5
    show kleio a casual at center, zoomAt(1.5, (840, 1040))
    show amy a casual at center, zoomAt(1.5, (440, 1040))
    with easeinleft
    "Kleio and Amy follow close on my heels as we go through them."
    "And it's only now that the reality of the place starts to hit me."
    "In the daytime, the park is a great spot to spend time relaxing."
    "But at night, all of those trees and shaded pathways..."
    "Well, they kind of start to look more than a little creepy!"
    "So much so that I find my pace starting to slow down."
    "This means that Kleio and Amy are soon passing me."
    "But as they do so, I feel them taking hold of my arms and speeding me up again."
    mike.say "Erm..."
    mike.say "On second thoughts, this place is very dark."
    mike.say "And it's totally full of spots where someone could hide."
    mike.say "You know, to jump out on us?"
    show kleio happy
    kleio.say "Aw..."
    kleio.say "Did you hear that, Amy?"
    kleio.say "Loverboy's scared!"
    show kleio normal
    show amy happy
    amy.say "Don't worry about it."
    amy.say "I know all of those hiding spots, every last one."
    amy.say "And we're going to be hidden away in one of them too!"
    show amy normal
    "It doesn't look like I'm going to be given any choice in the matter."
    "So I decide that there's no point in even trying to protest."
    "Instead I allow myself to be lead down one of the many paths in the park."
    "And soon enough, we're stepping off it onto one of those hidden spots."
    "The clearing that we end up in actually serves to ease my concerns."
    "As it seems like Amy was right, and there's little chance of us being seen."
    "But before I can open my mouth and say as much, I'm suddenly seized from both sides."
    with hpunch
    mike.say "Wha..."
    mike.say "Argh..."
    "It doesn't take me long to realise that it's actually Kleio and Amy manhandling me."
    "And that all they're really doing is eagerly trying to get me down onto the ground."
    show kleio talkative
    kleio.say "Geez, Loverboy..."
    kleio.say "Weren't you the one that wanted to keep from being discovered?"
    show kleio normal
    show amy happy
    amy.say "She's not wrong, you know!"
    amy.say "Now stop struggling and let us get on with it."
    show amy normal
    "There's really nothing I can do in response to that."
    "So I resign myself to lying back and letting them have their way."
    scene bg park
    show kleio a casual at center, zoomAt (1.0, (840, 720))
    show amy a casual at center, zoomAt (1.0, (440, 720))
    with fade
    "Pretty soon I find myself stripped of my clothes and sitting on the bench."
    "Which makes me thankful that it's a fairly warm and dry night."
    "But I find myself forgetting about such things as I look up."
    "Because Kleio and Amy have now started stripping off their own clothes too!"
    show amy topless with dissolve
    "And for all of the good tonight's done for their relationship, I feel the urge to compete creeping into them."
    "The girls begin undressing pretty simply, just pulling stuff off and tossing it aside."
    show kleio topless with dissolve
    "But as soon as they realise I'm watching, it seem to become a contest for attention."
    "Kleio and Amy are now both doing all they can to make it look sultry and provocative."
    show kleio naked with dissolve
    "A far better man than me would be able to think of a means to defuse the situation."
    show amy naked with dissolve
    "But as I'm only me, I find myself hypnotised by the show they're putting on."
    "All I can do is sit there, totally entranced as they crawl towards me."
    scene bg black
    show band blowjob amykleio park
    with fade
    "Kleio approaches me on the left, Amy on the right."
    "And part of me can't help thinking they look like female big cats on the prowl."
    "Like they're hunting for their next meal and I'm going to be their prey!"
    "But luckily for me, Kleio and Amy seem to have something more gentle in mind."
    "Because they lean in on either side of my cock, smiling sweetly."
    "Of course by now it's standing straight up, even still rising a little."
    "And I can see their eyes following it's every motion too."
    "The girls look like they're kind of fascinated by it."
    "Almost like they're not sure what they should do next."
    "But then I see something flash in Kleio's eyes, something wicked."
    "And when I look over at Amy, I see it reflected in her eyes too!"
    "All of a sudden the sweetness is gone, just totally vanished."
    "Now they're right back to looking like a couple of hungry carnivores."
    "And it's my meat that they're eyeing up!"
    show band blowjob amykleio kleiolick amylick
    "As one, Kleio and Amy make their move."
    "By which I mean that they pretty much pounce on me."
    show band blowjob amykleio kleiosuck -amylick insert
    "Kleio goes for the head of my cock, wrapping her lips around it."
    show band blowjob amykleio amylick
    "And at the same time, Amy begins licking at the base with her tongue."
    "I can't help flinching and letting out a small squeal of alarm."
    mike.say "Argh!"
    "But of course this only seems to amuse the girls."
    "They chuckle and exchange a knowing glance, not stopping as they do so."
    "And I just stay right where I am, almost frozen to the spot."
    "But it's not like the thing keeping me there is actual fear."
    "Because the sensation of their attentions is really taking hold."
    "Kleio and Amy seem to know exactly what they're doing at either end of my cock."
    "And I could sit here until they're all done, just enjoying the ride."
    "But it seems like they have something else in mind before then."
    "Because I see that Amy's starting to move upwards."
    "And at the same time, Kleio's beginning to go down."
    show band blowjob amykleio kleiolick
    "I watch in total fascination as they approach each other."
    "Almost meeting in the middle of my shaft, they deftly pass each other."
    "And just like that, the two of them have swapped positions."
    show band blowjob amykleio amysuck
    "Now Amy is taking the head of my cock into her mouth."
    "While down below, Kleio begins to suck on my balls!"
    "It goes without saying that everything they're doing it intensely pleasurable."
    "And the attentions of either alone would be enough to blow my mind."
    "So together it's all that I can do to hold on while they work me over."
    show band blowjob amykleio amylick kleiolick
    "In fact they're working so well together that I can't help wondering..."
    "Have the girls in the band done things like this before?"
    "And if so, could they be talked into doing it again?"
    "All of this is whirling around inside of my head as it's reeling."
    "Vague thoughts that I might recall afterwards or totally forget."
    "Because the pleasure I'm feeling is almost flooding my brain right now."
    "In a perfect world, I'd like Kleio and Amy to just keep right on going."
    "But I can already feel that I'm getting close to my limits."
    "I'm going to lose it any second, and I need to decide where, as well as how!"
    menu:
        "Make Amy swallow":
            "I don't know what it is that makes me want to choose Amy."
            "Or what makes me want to have her swallow my load."
            "Maybe it's the fact that she's the newest addition to the mix."
            "That and the feeling I have that I need to mark my territory somehow?"
            "Not that I'm trying to claim either of the girls as my property!"
            "Just kind of wanting to make my mark in terms of our sexual relations."
            show band blowjob amykleio amysuck
            "That's why I make sure to hold on until Amy has my cock in her mouth."
            "And then I kind of raise myself up while reaching out ton hold her head."
            "Luckily for me, Amy seems to know exactly what this means."
            show band blowjob amykleio amysuck cumshot with hpunch
            "She relaxes the muscles in her throat, letting me go deeper."
            with hpunch
            "And by the time I actually lose it, she's more than ready."
            with hpunch
            "All of which means she can swallow it all without incident."
        "Make Kleio swallow":
            "I don't know what it is that makes me want to choose Kleio."
            "Or what makes me want to have her swallow my load."
            "Maybe it's the fact that she's obviously got history with Amy."
            "That and the feeling I have that I need to remind her of our own connection?"
            "Not that I'm trying to claim either of the girls as belonging to me!"
            "Just kind of wanting to make my mark in terms of our sexual relations."
            show band blowjob amykleio kleiosuck
            "That's why I make sure to hold on until Kleio has my cock in her mouth."
            "And then I kind of raise myself up while reaching out ton hold her head."
            "Luckily for me, Kleio seems to know exactly what this means."
            show band blowjob amykleio kleiosuck cumshot with hpunch
            "She relaxes the muscles in her throat, letting me go deeper."
            with hpunch
            "And by the time I actually lose it, she's more than ready."
            with hpunch
            "All of which means she can swallow it all without incident."
        "Stop thinking":
            "I don't want to be forced to choose between Kleio and Amy at this point."
            "Because it seems important to me that both of them are included, even now."
            "So I make a point of backing off a little as I feel myself starting to cum."
            "At first this seems to throw the girls, making them frown."
            "But one look at my face is all it takes for them to realise what's happening."
            "And as soon as they do, Kleio and Amy lean in closer, almost cheek to cheek."
            "Which means that they're in the perfect position to take it as I shoot my load."
            show band blowjob amykleio kleiolick amylick cumshot with vpunch
            "Stripes of hot, white cum shoot the short distance between us."
            with vpunch
            "And then I watch as they paint Kleio and Amy's features."
            with vpunch
            "Brows, noses and cheeks are all striped from left to right."
            show band blowjob amykleio kleiolick amylick -cumshot dickcum
            "The strings even stretch from one face to the other, they're so close."
            "All the time the girls smile and giggle with delight."
            "And once I'm done, they happily lick their lips too."
    "Panting and gasping from my efforts, I fall backwards."
    "But Kleio and Amy are there to catch me, hands grabbing hold."
    "Though I instantly get the feeling there's an ulterior motive here."
    "Because they don't look like they're about to let me rest!"
    scene bg park
    show kleio happy naked at center, zoomAt(1.5, (440, 1040))
    show amy normal naked at center, zoomAt(1.5, (840, 1040))
    with easeinbottom
    kleio.say "That was a really great show you just put on, Loverboy..."
    kleio.say "But you're one of the Deathless Harpies now."
    show kleio normal
    show amy happy
    amy.say "That means we always do an encore."
    amy.say "And we never leave the audience wanting more!"
    show amy normal
    show kleio seductive
    kleio.say "So you're gonna have to make a choice."
    show amy flirt
    amy.say "Which one of us is going to get it?"
    "My gaze keeps flitting from one of them to the other."
    "Because it really does feel impossible to choose between them!"
    show kleio happy
    kleio.say "You just sit back and watch me handle him, Amy..."
    kleio.say "I already know how to get his engine going!"
    show kleio normal
    show amy happy
    amy.say "Then you can tell me how to do it as I ride him, Kleio..."
    amy.say "No need for me to be the one sitting it out!"
    show amy normal
    "I can tell that there's no way either of them is going to back down."
    "And I feel that I need to step in and settle the argument before it's too late."
    "But which one of them am I supposed to choose?"
    menu:
        "Fuck Kleio":
            "I kind of feel like I've already done enough good work for one evening."
            "And now I want to do some very bad things with Kleio instead."
            "I know that this might sound like I'm going back on all I've achieved tonight."
            "But surely Amy's not going to renege on it all just because I won't fuck her?"
            "And if she does, then maybe she was never worth the effort anyway!"
            mike.say "Hey, Kleio, get over here..."
            mike.say "I have something for you!"
            "Kleio can't seem to contain the delight at being the one to get picked."
            "She reaches out to take hold of my hands as I hold them up for her."
            "And she also can't resist taking a little jab at Amy too."
            show kleio happy
            kleio.say "You might be back in with me, Amy..."
            kleio.say "But I'm the one that's getting one in me tonight!"
            show kleio normal
            "Luckily for everyone involved, Amy seems to take this in good spirits."
            "Because she simply chuckles and shakes her head at Kleio's words."
            show amy happy
            amy.say "Yeah, yeah..."
            amy.say "Enjoy it while it lasts, Kleio."
            amy.say "Because I'll get some of that action, sooner or later!"
            show amy normal
            "I'm watching them verbally sparring this whole time."
            "Thinking that this could be a way of them getting on."
            "But with my attention elsewhere, I'm not aware of what's happening down below."
            scene bg black
            show band threesome amykleio fuckkleio park
            with fade
            "So it comes as a shock to feel Kleio grab hold of my cock."
            "And that sensation is doubled when she shoves it hard against her pussy!"
            show band threesome amykleio fuckkleio vaginal kleiopleasure kleioclose
            mike.say "Urgh..."
            mike.say "Be careful, Kleio..."
            mike.say "I don't want you to snap it in half!"
            kleio.say "Ah, quit complaining..."
            show band threesome amykleio fuckkleio vaginal kleionormal kleioopen
            kleio.say "There's folks that'd pay to be put in hospital by me!"
            "By now Kleio's straddling me, pushing her weight down at the same time."
            "And it doesn't take long for all of this to begin having an effect."
            "I can feel that my cock can't get any harder."
            "But in contrast, I can also feel her getting softer by the moment."
            "All of a sudden, the muscles down there seem to melt."
            "Their resistance just vanishes, and there's nothing keeping me out."
            show band threesome amykleio fuckkleio vaginal kleioclose at stepback(speed=0.1, h=-10, v=0)
            "Kleio sinks down and onto me, my cock sinking into her."
            "And as soon as it does, all of her swagger disappears too."
            "I watch in amazement as Kleio seems to surrender to the sensations."
            "Where before she was cocky and confident, now she's helpless to resist."
            "All I have to do is thrust up from below, gentle and smooth."
            show band threesome amykleio fuckkleio at stepback(speed=0.1, h=-10, v=0)
            "And every time I do, she becomes more passive and helpless in my grasp."
            show band threesome amykleio fuckkleio vaginal kleiopleasure
            "Soon enough, Kleio is reduced to moaning and gasping."
            "Using all of her strength to hold herself upright."
            show band threesome amykleio fuckkleio at stepback(speed=0.1, h=-10, v=0)
            "My efforts are going into the act of penetrating as deep and hard as possible."
            "So at first I fail to notice what Amy's hands are doing."
            "It's only when I see fingers playing with Kleio's nipples that I realise."
            "Because at first I'm puzzled as to why I can't feel them myself."
            show band threesome amykleio fuckkleio at stepback(speed=0.1, h=-10, v=0)
            "Suddenly I realise that Amy is the one playing with Kleio, not me."
            "In fact she seems to be stimulating the other girl in multiple places at once."
            "While I'm nailing Kleio from below the waist, Amy's teasing her above it."
            show band threesome amykleio fuckkleio at stepback(speed=0.05, h=-10, v=0)
            "And there's nothing that Kleio can do to resist!"
            "I can feel her body begin to quake as she's pushed over the edge."
            show band threesome amykleio fuckkleio at stepback(speed=0.05, h=-10, v=0)
            "The contractions of her muscles making sure I soon join her."
            show band threesome amykleio fuckkleio at stepback(speed=0.05, h=-10, v=0)
            "Knowing that there's no way for me to stop it, I just let go."
            show band threesome amykleio fuckkleio creampie with hpunch
            "And a moment later, I shoot my load deep into Kleio."
            $ kleio.sexperience += 1
            $ kleio.love += 4
        "Fuck Amy":
            "I really wish there was another way to do this."
            "Some way that I didn't have to choose between them."
            "But up to now, tonight's been all about building bridges."
            "I just guess it's now going to be about laying some pipe instead!"
            "And I have to hope that Kleio understands why I feel the need to do this..."
            mike.say "Hey, Amy..."
            mike.say "I've got something for you!"
            "I leave the bench and hold out my hands to Amy."
            "And I beckon for her to come to me."
            "At first she seems a little surprised."
            "And she looks at Kleio, as if for approval."
            show kleio happy
            kleio.say "What are you looking at me for?"
            kleio.say "I'm not selling rides on that thing!"
            kleio.say "You wanna fuck him or not?"
            show kleio normal
            "Amy nods at this, and almost hops onto me."
            scene bg black
            show band threesome amykleio fuckamy park
            with fade
            "I manage to catch her as she straddles my thighs."
            "And as she does so, I note how much studier she is than Kleio."
            "I can't help putting my hands on Amy's body, appreciating the weight of her."
            kleio.say "Alright, Loverboy..."
            kleio.say "Just fuck her already!"
            kleio.say "It's not like you never felt up a girl before!"
            kleio.say "But I think of better use of this hanging mouth of yours."
            "Amy seems a little surprised as Kleio sits on me."
            "But she chooses to look around at almost the same moment my brain gets into gear."
            "This means that she only notices when I grab hold of her by the haunches."
            show band threesome amykleio fuckamy vaginal at startle(0.05,-10)
            "And all she has time to do is gasp before I pull her down and onto me."
            amy.say "Wha..."
            amy.say "Oh..."
            amy.say "Oh fuck!"
            "I can only guess that Amy must have already been very excited."
            "Because as I pull her down, I don't feel enough resistance to stop me."
            "Normally I'd expect to be forced to put in some work to get inside."
            "Even if it was only a matter of teasing her lips open down there."
            "But I swear that Amy slides straight onto me."
            show band threesome amykleio fuckamy vaginal at startle(0.05,-10)
            "And that let's me sink all the way into her too."
            "She keeps on going down, swallowing every inch of my cock."
            show band threesome amykleio fuckamy insert with vpunch
            "This only stops when I can't possibly go any deeper."
            "But that doesn't mean that I come to a halt as well."
            show band threesome amykleio fuckamy at startle(0.05,-10)
            "Instead I begin to thrust up and down, in and out."
            show band threesome amykleio fuckamy onmike
            kleio.say "Hey! Beyond... Do something!"
            "After this delightful reminder, I begin to work on the wet slit in front of me."
            show band threesome amykleio fuckamy lick
            "But it doesn't mean that I'm not focused on my main task."
            show band threesome amykleio fuckamy at startle(0.05,-10)
            pause 0.2
            show band threesome amykleio fuckamy at startle(0.05,-10)
            "Using the grip I already have on Amy, I pound away at her without mercy."
            "The effect is instant and impressive, as she begins to gasp with pleasure."
            show band threesome amykleio fuckamy at startle(0.05,-10)
            pause 0.2
            show band threesome amykleio fuckamy at startle(0.05,-10)
            "At the same time, Amy's impressive breasts bounce and jiggle above me."
            "In fact they're so large that I often can't see her face for them!"
            "I'm almost totally absorbed in the act of watching Amy."
            show band threesome amykleio fuckamy onamy
            "So at first I fail to notice what Kleio's hands are doing."
            "It's only when I see fingers playing with Amy's nipples that I realise."
            "Because at first I'm puzzled as to why I can't feel them myself."
            "Suddenly I realise that Kleio is the one playing with Amy, not me."
            "In fact she seems to be stimulating the other girl in multiple places at once."
            "While I'm nailing Amy from below the waist, Kleio's teasing her above it."
            "And there's nothing that Amy can do to resist!"
            show band threesome amykleio fuckamy at startle(0.05,-10)
            pause 0.2
            show band threesome amykleio fuckamy at startle(0.05,-10)
            "I can feel her body begin to quake as she's pushed over the edge."
            show band threesome amykleio fuckamy at startle(0.05,-10)
            pause 0.2
            show band threesome amykleio fuckamy at startle(0.05,-10)
            "The contractions of her muscles making sure I soon join her."
            show band threesome amykleio fuckamy at startle(0.05,-10)
            pause 0.2
            show band threesome amykleio fuckamy at startle(0.05,-10)
            "Knowing that there's no way for me to stop it, I just let go."
            show band threesome amykleio fuckamy at startle(0.05,-10)
            pause 0.2
            show band threesome amykleio fuckamy creampie squirt with vpunch
            "And a moment later, I shoot my load deep into Amy."
            $ amy.sexperience += 1
            $ amy.love += 4
    "Afterwards there's no time for a romantic exchange of words."
    "Because we all become instantly aware of the fact we're still in the park."
    "So what follows is a mad scramble to get dressed and sneak out again."
    scene bg street
    show kleio a casual at center, zoomAt (1.25, (840, 880))
    show amy a casual at center, zoomAt (1.25, (440, 880))
    with fade
    "On the walk home, there's little chatting going on thanks to us all being tired."
    "That allows me to take time to silently congratulate myself on a job well done."
    "Not long ago, Kleio and Amy couldn't be in the same room without trying to kill each other."
    "But now, largely thanks to me, they're getting on like a house on fire."
    "Maybe I have a talent for this kind of thing?"
    "Maybe mediation could be a potential career for me in the future?"
    return

label amy_concert_naked:
    show amy puzzled at center, zoomAt(1.25, (640, 880))
    "I've been wanting to pitch an idea of mine to the girls in the band for a while now."
    "But it's such a crazy, out there kind of idea that I can't just ask them as a group."
    "So instead I've decided to approach each of them individually and make my pitch."
    "Kind of divide and conquer, or at least not look like a fool in front of them all at once!"
    "Out of all of them, I figure that I might have the most success with Amy."
    "As I've always thought that she has a hidden side to her."
    "One that runs deeply into all things kinky and risqué."
    show amy at center, traveling(1.5, 1.0, (640, 1040))
    "So when I come to ask her, I figure it's best to be pretty frank."
    mike.say "Amy..."
    mike.say "You're a pretty broad-minded kind of girl, right?"
    show amy normal
    "Amy looks up as I say this."
    "And I can see that she has a look of amused intrigue on her face."
    show amy flirt
    amy.say "Well, I have been known to put up with your bullshit, [hero.name]..."
    amy.say "And that takes a bit of an effort, I can tell you!"
    show amy normal
    mike.say "Touche, Amy..."
    mike.say "But seriously, there's something I wanted to ask you."
    mike.say "And it's kind of out there, you know?"
    show amy puzzled
    "Amy shrugs at this."
    show amy happy
    amy.say "Well I won't know until you tell me, will I?"
    amy.say "So why don't you stop beating about the bush and ask me already?"
    show amy normal
    "I nod, hurrying to do as Amy says."
    mike.say "Okay, Amy..."
    mike.say "It's about the band, the thing I wanted to ask."
    mike.say "I've been thinking about how we can get more attention."
    mike.say "Get more eyes on us, yeah?"
    show amy puzzled
    "Amy nods, but I can see she's still waiting for something."
    "So I do the best I can to get to the point."
    mike.say "Well..."
    mike.say "That's when it hit me - nudity, Amy..."
    mike.say "Nudity gets eyes on you, and it's something we can do for free!"
    show amy happy at startle
    "Amy surprises me by beginning to laugh."
    show amy at startle
    "She's shaking her head too, like I just told her a joke."
    show amy surprised
    "But then she seems to notice the puzzled look on my face."
    amy.say "Oh..."
    amy.say "Oh wow..."
    amy.say "You're serious, aren't you?"
    mike.say "Yeah, Amy..."
    mike.say "I'm totally serious!"
    mike.say "What's the matter?"
    mike.say "Don't you think it'd work?"
    if amy.love >= 185 and amy.sub >= 85:
        show amy shy
        "I see the confusion on Amy's face finally clear."
        show amy normal
        "And much to my relief, the next thing she does is start nodding."
        show amy happy
        amy.say "[hero.name]..."
        amy.say "That's such a great idea!"
        show amy normal
        "Of course that's the response that I'd hoped to get."
        "But I was still expecting to have to talk Amy round to my way of thinking."
        "So that fact that she's already agreeing with me is a little confusing."
        mike.say "Are you sure, Amy?"
        mike.say "You'd be up for performing naked?"
        show amy happy
        amy.say "Oh yeah, totally!"
        amy.say "I wish I'd thought of that myself."
        amy.say "It'd make us different from every other band out there!"
        show amy normal
        "I feel a flood of relief pass over me as Amy says all of this."
        "And I make a mental note that I have at least one band member on board."
        show amy flirt
        amy.say "In fact, this is the kind of thing we should have been doing before..."
        amy.say "You know, back when I was in the band the first time?"
        amy.say "Something this unique could have been the making of us."
        show amy normal
        mike.say "That's great news, Amy!"
        mike.say "I'm sure you're right and this will be nothing but good for The Deathless Harpies."
        mike.say "But how about you let me ask the others about the idea, yeah?"
        show amy surprised
        "Amy looks a little surprised at this."
        amy.say "Are you sure?"
        show amy happy
        amy.say "I'd be more than happy to help."
        show amy annoyed
        amy.say "And couldn't the both of us make a better argument?"
        show amy puzzled
        "I shake my head."
        mike.say "No, Amy..."
        mike.say "I think they need to hear it on their own."
        mike.say "That way it's not like we're ganging up on them or anything."
        show amy normal
        "Amy nods and seems to be happy to let the matter drop."
        "So I can start planning my strategy for the next member of the band."
        $ amy.flags.agree_concert_naked = True
    else:
        show amy mad
        "I see the confusion on Amy's face finally clear."
        "But much to my dismay, the next thing she does is start shaking her head."
        show amy upset
        amy.say "No way, [hero.name]…"
        amy.say "I'm not getting naked on stage!"
        show amy angry
        "Of course that's not the response I was hoping for."
        "And so I'm all set to argue my point."
        mike.say "Oh come on, Amy..."
        mike.say "I thought you were the liberated one in the band?"
        mike.say "The resident free-thinker?"
        mike.say "This isn't ordinary nudity..."
        mike.say "This is all for the sake of a higher art!"
        show amy annoyed
        "Despite my best efforts, Amy shakes her head again."
        show amy upset
        amy.say "I'm a liberated kind of girl, sure."
        $ amy.love -= 2
        $ amy.sub -= 2
        amy.say "But I'm not into showing off what I've got in public like that."
        amy.say "And I like to keep my more provocative acts private too."
        show amy mad
        "I open my mouth to try arguing from another angle."
        show amy b
        "But Amy stops me in my tracks by holding up a hand."
        show amy upset
        amy.say "Uh-uh..."
        amy.say "No more of your silver-tongued charming!"
        amy.say "You've had an answer out of me already."
        amy.say "As well as an explanation of my reasons."
        amy.say "And that's all you're getting."
        show amy mad
        "I close my mouth slowly."
        "Feeling a sense of defeat flow over me as I do so."
        $ amy.flags.agree_concert_naked = False
    scene bg black with dissolve
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
