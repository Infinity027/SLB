init python:
    InteractActivity(**{
    "name": "fuck_kat",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            ),
        PersonTarget(kat,
            IsActive(),
            MinStat("love", 100),
            MinStat("sub", 25),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    Event(**{
    "name": "kat_hottub_sex_male",
    "label": "kat_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            IsActivity("date_hot_tub_home")),
        PersonTarget(kat,
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


label kat_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    scene bg pool with fade
    "I still can't believe that I had to try so hard to talk cat into coming over to use the hot-tub."
    "Normally girls jump at the chance to spend some time relaxing in a warm pool of bubbling water."
    "But with Kat I had to throw in the offer of letting her play some of my collection of retro videogames too."
    "She's been itching to get her hands on them since I told her that I had them."
    "And it's pretty obvious she's more interested in them than taking a dip in the hot-tub with me!"
    "Nevertheless, I've decided that the best idea is to go all-out with the presentation."
    "Mood-lighting, candles borrowed from around the house, a really nice bottle of wine too."
    "Once Kat gets here, I'm hoping that it'll hit her right between the eyes."
    "Well...in a good way, obviously!"
    "Like she'll realise how great of an idea this is."
    "So once everything is ready, all I can do is wait."
    "I'm already in my trunks, hovering around the side of the hot-tub."
    "At a moment's notice I'm ready to leap into action, open the wine and hit the bubbles."
    "In fact I'm so poised and ready for action that when Kat arrives, it catches me totally off-guard."
    show kat smile swimsuit with easeinleft
    kat.say "Hey, [hero.name]!"
    kat.say "Ready for some retro action?"
    "At the sound of Kat's voice, I almost leap out of my skin."
    "And my sudden cry of alarm earns the same response from her."
    with vpunch
    mike.say "Aargh!"
    show kat shocked at vshake
    kat.say "Aargh!"
    mike.say "What the..."
    mike.say "Don't...don't sneak up on me like that!"
    show kat confused
    kat.say "I...I didn't mean to!"
    show kat normal
    kat.say "I..."
    show kat surprised
    kat.say "Oooh!"
    "Kat seems to lose interest in explaining herself as she finally sees the space around the hot-tub."
    "And I can see that her eyes are going wide as she takes it all in, like it's a massive surprise."
    mike.say "What's the matter, Kat?"
    mike.say "Have you never seen a hot-tub before?"
    "Kat shakes her head, which also seems to snap her out of it."
    "Then she turns to look at me with a wry smile on her face."
    show kat angry
    kat.say "Well, duh!"
    kat.say "Of course I have."
    show kat smile
    kat.say "I just didn't think you were going to all this trouble just for me!"
    kat.say "It looks really...nice."
    "I can't help feeling a little puzzled at Kat's reaction."
    mike.say "How else would I make it look?"
    mike.say "This is supposed to be a chance for us to do something romantic."
    mike.say "You know - enjoy the warm water and the bubbles?"
    mike.say "A glass of wine of two?"
    show kat annoyed
    "Kat slaps her forehead with her own hand."
    "Then she shakes her head."
    kat.say "Urgh..."
    kat.say "What is the matter with me?"
    kat.say "I got it into my head this was going to be more like going swimming."
    kat.say "You know, like at a public pool?"
    show kat sadsmile
    kat.say "I was even thinking your housemates might be in there with us too!"
    mike.say "Erm..."
    mike.say "No, Kat..."
    mike.say "It's going to be just us."
    show kat smile
    kat.say "That's good..."
    show kat blush
    kat.say "Because the hot-tub isn't the only thing that looks good right now!"
    "I look around, wondering what Kat could be talking about."
    "But a moment later she clues me in by walking over and leaning against me."
    "Kat makes a pleasant purring sound as she strokes the muscles of my chest."
    mike.say "Oh..."
    mike.say "Oh, I get it!"
    mike.say "You were talking about me!"
    mike.say "You...you were talking about me, right?"
    show kat happy -blush
    "Kat chuckles and pushes herself away from me, shaking her head."
    kat.say "Of course I was, dumbass!"
    show kat smile
    kat.say "Now how about you pour us some of that wine?"
    "Kat's still shaking her head as she turns her back on me and starts getting undressed."
    "And I struggle to keep on watching her as I try to pour the wine at the same time."
    "Kat has her swimming costume on under her clothes, so changing doesn't take her long."
    "But my arm's still shaking a little as she turns round and I hand her a glass of wine."
    mike.say "You're looking good too, Kat."
    mike.say "I mean great...you're looking great!"
    show kat shy blush
    "Kat can't help blushing as she accepts the glass."
    "And I note too that she takes a step over to the edge of the tub."
    show hottub kat with fade
    "Dipping an experimental toe into the water, she begins to lower herself in."
    "It seems like all the flattery has had the desired effect."
    "Because Kat's not mentioned my game collection once since she got here!"
    kat.say "Oh wow..."
    kat.say "The water's really warm!"
    "I nod and smile, trying to play it cool."
    "Because as Kat's saying this, I'm getting ready to play my ace."
    "Which involves leaning over and hitting the switch to activate the water jets."
    "As soon as I do, the water begins to churn and bubbles appear on the surface."
    kat.say "Wha..."
    kat.say "Whoa!"
    kat.say "That feels even better!"
    "I hurry to get into the tub, settling down beside Kat."
    "She wastes no time in sliding closer, pressing herself against me."
    mike.say "So..."
    mike.say "What do you think, Kat?"
    mike.say "You like it?"
    "Kat nods as she takes a sip of her wine."
    "And I can't help noting too that it's a long sip."
    "Or that the glass is already close to being empty too!"
    kat.say "Oh yeah..."
    kat.say "This is really great!"
    kat.say "Do you ever..."
    kat.say "You know...do stuff in here?"
    "It's just now that I notice where Kat's free hand is."
    "That she's put in on my thigh under the water."
    "And that it's creeping higher by the moment."
    "By way of an answer, I reach up and pull down the straps of her swimming costume."
    "Kat gasps and I see that her cheeks are beginning to flush with colour."
    "But she doesn't try to stop me, even helping out by shouldering out of her costume too."
    "Pretty soon I've managed to pull it all the way down."
    "Then Kat kicks it off, and it floats away, forgotten atop the water."
    "She returns the favour, pulling down my shorts so that I can be rid of them too."
    "And from that moment on, the pair of us seem to be on some kind of autopilot."
    show hottub sex male kat outside with fade
    "Kat leans herself up against the wall, letting it take her weight."
    "That means I can get the perfect angle as I loom over her."
    "She's nodding as I take aim, almost desperately for what comes next."
    "But I'm not as quick to get down to it as she might have liked."
    "Because first I take the time to tease her with the tip of my cock."
    "As it slides up and down the lips of her pussy, Kat's moans get ever louder."
    "And at the same time I can feel things getting ever more slippery down there."
    "But when the resistance I'm feeling finally fades, it takes me by surprise."
    show hottub sex male kat inside
    "All of a sudden I feel myself surging forwards, pushing into Kat."
    "And though it's her body that's making this happen, it seems to surprise her too."
    "In a matter of mere seconds we go from teasing each other to full-on doing it!"
    "I feel myself slide all the way into Kat, meeting next to no resistance."
    "And once I'm all the way in, I only pause for a second."
    "Because that same automatic urge takes over."
    "Without pause or hesitation, I start to thrust in and out of her."
    "Kat responds in kind, clinging on to me and nodding her approval."
    "But all I know is that I need to go harder and faster."
    "So I put a hand under each of her thighs, and lift her higher."
    "This give me a better angle, more space to work with."
    "And the effects are clear to see on Kat's face."
    "Her mouth hangs open and her eyes are glazed over, almost rolling back into her head."
    "The force of my thrusts is making Kat's breasts jiggle and bounce."
    "She seems to be trying to hold onto them, maybe even play with her nipples."
    "But all she can manage is to wave them vaguely in the air without success."
    kat.say "Oh..."
    kat.say "Oh yeah..."
    kat.say "Fuck me...harder!"
    "I can hear the way Kat's voice is starting to crack."
    "Like she's on the brink of something she can't control."
    "And I know that she's on the brink of losing it."
    "The knowledge excites me so much that I feel it happening to me too."
    show hottub cumshot with hpunch
    $ kat.impregnate()
    "A moment later I can't hold it in, and I have no choice but to let it happen."
    $ kat.love += 1
    show hottub sex male ahegao with hpunch
    "I shoot my load into Kat, holding nothing back."
    with hpunch
    "And that's enough to push her over the edge."
    "She cums, the sensation of her muscles making my own climax all the more intense."
    "Afterwards I hold Kat up in the water, waiting for the strength to return to her limbs."
    mike.say "So, Kat..."
    mike.say "You want to go play those sweet, retro games?"
    kat.say "Huh..."
    kat.say "What?"
    kat.say "What games?"
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ kat.sexperience += 1
    $ game.active_date.clothes = None
    return

label kat_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg street
    show kat

    call kat_fuck_date_intro_male (location) from _call_kat_fuck_date_intro


    call kat_dick_reactions from _call_kat_dick_reactions


    call kat_fuck_date_foreplay_male from _call_kat_fuck_date_foreplay_male


    call kat_fuck_date_choices_male from _call_kat_fuck_date_choices_male


    call handle_npc_leaving (kat, _return) from _call_handle_npc_leaving_28
    if _return:
        return


    hide kat
    call kat_fuck_date_sleep (location="hero") from _call_kat_fuck_date_sleep
    return

label kat_fuck_date_intro_male(location="hero"):
    $ rand_intro = randint(0, 4)
    if rand_intro == 0:
        scene bg house
        show kat happy
        with fade
        "Kat and I have just made it back to my place in a taxi, all laughs and smiles."
        "And that's because the date we just went on was a good one, an all-round success."
        "After having had so much fun together, neither of us is in the mood to call it quits."
        "So it just feels like the natural thing to slip quietly in through the front-door."
        scene bg livingroom
        show kat smile
        with fade
        "And then hurry through the house to my bedroom, praying not to meet anyone on the way."
        "Sure, we could probably handle it if [bree.name] or Sasha happened to cross our path."
        "But this is one of those times when it just feels like there's a certain buzz between us."
        "A kind of unspoken connection that means we don't need to exchange words."
        "Each of us just knows what the other wants on pure instinct alone."
        scene bg bedroom1 with fade
        show kat normal blush at right with easeinright
        "This means that the moment we're through the door and alone in my room, it's on."
        show kat smile topless at center with ease
        "I close the door and turn around to the sight of Kat already pulling off her top."
        "Again, without a single word, I start to do the same."
        show kat shy naked -topless with dissolve
        "Pretty soon there's a trail of discarded clothes all the way to the side of my bed."
    elif rand_intro == 1:
        scene bg house
        show kat smile
        with fade
        "My curiosity is getting harder to ignore as Kat and I get out of the taxi."
        "It's not on account of anything she's said, rather something she keeps doing."
        "Our date went really well tonight, and Kat jumped at the chance to come back to my place."
        "So I'm not worried for a moment that she's going to refuse to come to my bedroom too."
        "It's just that she keeps shooting me these glances as we walk up to the front door."
        show kat shy blush at startle
        "Every time I try to turn my own head and make eye-contact, Kat turns away from me."
        "And more than once, I swear that she's about to say something."
        "But she always stops before a single word comes out of her mouth."
        "So by the time I have the front door open and we're inside, it's driving me crazy!"
        scene bg bedroom1
        show kat normal
        with fade
        "I just about manage to keep a lid on it as I lead Kat to my room."
        show kat shy blush
        "But as soon as I close it behind us, I catch her doing it again."
        "And now that we're on our own, I feel like it's the perfect time to call her out on it."
        mike.say "Kat..."
        mike.say "Are you going to tell me what's up?"
        mike.say "Or are you just going to keep looking at me like that?"
        show kat surprised -blush at startle
        kat.say "Huh?"
        kat.say "Looking at you?"
        show kat shy
        kat.say "I don't know what you're talking about!"
        "I can't help rolling my eyes at Kat's obvious attempts to hide the truth."
        "Not only because she's a pretty terrible liar."
        "But also because she can't even look me in the eye as she's saying it."
        mike.say "Come on, Kat..."
        mike.say "If you don't tell me, then it's going to be on my mind all night."
        mike.say "And that kind of thing can seriously affect a guy's performance!"
        "This does seem to be enough to get through to Kat."
        "And she nods, letting me know that I'm going to get my way."
        show kat confused blush
        kat.say "Okay, okay..."
        kat.say "But this isn't an easy thing for me to ask."
        show kat shy
        kat.say "I...I want to...to go on top!"
        "I look at Kat in a kind of stunned silence for a moment."
        "Because I'm honestly expecting her to add something else."
        "But there's nothing more added to the request."
        "And so I'm forced to offer up an answer all the same."
        mike.say "Erm..."
        mike.say "Is that it?"
        show kat sad
        kat.say "Yes, that's it."
        mike.say "Of course you can go on top, Kat."
        mike.say "But I don't get why you think that's hard to ask?"
        show kat shy
        "Kat's starting to look more than a little embarrassed by now."
        "And she's finding it hard to meet my eye again."
        show kat -blush
        kat.say "Well, I..."
        kat.say "I thought guys always wanted to go on top?"
        show kat sad
        kat.say "Most of the guys I've dated insisted on it."
        kat.say "Like they didn't enjoy it unless they were the one on top."
        "I shake my head, feeling pretty surprised by Kat's explanation."
        mike.say "They didn't do that because they were guys, Kat."
        mike.say "They did it because they were jerks!"
        show kat surprised
        "Kat's eyes go wide as she's surprised in turn."
        "But then she puts a hand in front of her mouth."
        show kat smile at startle
        "And she giggles, the sound filled with mischief."
        "As soon as she stops giggling, both of her hands begin another task."
        show kat topless with dissolve
        "Specifically, they start to strip off her clothes!"
        "I take this as meaning that the discussion is over."
        "And so I start doing the same thing too."
        show kat naked -topless with dissolve
        "Soon enough, we're both naked and walking over to the bed."
    elif rand_intro == 2:
        scene bg house
        show kat blush
        with fade
        "Once we're out of the taxi and through the front door, Kat and I don't waste a second."
        scene bg livingroom
        show kat blush
        with fade
        "We hurry straight past the sitting room and the kitchen, hoping not to see anyone on the way."
        "And we don't stop until we make it all the way to the door of my bedroom."
        "I hold it open for Kat and she slips inside with me following on her heels."
        scene bg bedroom1
        show kat blush
        with fade
        "The moment the door closes, it feels like we both breath out in the same motion."
        "Because we're finally alone and there shouldn't be anything to get in the way."
        show kat defiant
        "Only now can we get down to what we've wanted to do all night."
        "Which is play a long and complicated game of chess!"
        "Kidding!"
        "I'm only kidding!"
        "We want to fuck like rabbits on speed, of course we do!"
        show kat close
        "That's why Kat pounces on me the moment the door is closed."
        "Sure, she takes me by surprise at first, sending me staggering backwards."
        "But it's not enough to make me lose my footing, and I soon recover."
        hide kat
        show kat kiss date
        with fade
        $ kat.flags.kiss += 1
        "And once I do, I'm all over Kat in the same way she's all over me!"
        "Neither of us says a single word while all of this is happening."
        "Mainly because we have our lips pressed together the whole time."
        "We end up staggering around the room, locked together."
        "And I guess the unspoken idea is that we're trying to make it to the bed."
        "But more than once I feel my leg brush against it."
        "Then I find that I can't do a thing about it and we're off in a different direction again."
        "When we finally make it there, the only reason is thanks to the fact that we literally fall over it."
        "The back of my legs hit the bed, and I stop moving."
        "But there's no way for Kat to get the message."
        "So she keeps right on going, pushing me over so that I fall onto the bed."
        "Kat's still wrapped in my arms with her arms around me too."
        "Which means that she's dragged along for the ride."
        hide kat
        with vpunch
        mike.say "Whoa..."
        mike.say "Ah shit!"
        show kat close date surprised
        kat.say "Wha..."
        kat.say "What the hell?"
        with vpunch
        "We land in a heap on the mattress, bouncing as the springs groan under our weight."
        "At the same time I try to sit up and Kat tries to roll to the side."
        show kat smile with hpunch
        "But as we're still entangled, all this does is make use turn over on the bed."
        "I come up on top, with Kat now pretty much pinned beneath me."
        "And while all of this might be confusing, it's not enough to kill the mood."
        show kat topless -close with dissolve
        "Kat pulls of her top, tossing it aside."
        "Then she starts to wriggle around under me, trying to pull off her shorts too."
        "Any other time I'd have been doing all I could to help her get naked."
        "But the problem is that I'm struggling to do that too!"
        "One item at a time and with an incredible amount of effort, we eventually manage it."
        show kat naked -topless with dissolve
        "We're both naked and now there's nothing to stop us finally getting it on."
    elif rand_intro == 3:
        scene bg street
        show kat
        with fade
        "Tonight's been one of those times when everything just seems to fall into place."
        "The date that Kat and I have been on was great, and I enjoyed it from start to finish."
        "Even better, I know that Kat feels the same way about it too."
        scene bg taxi
        show kat
        with fade
        pause 0.5
        show bg taxi car with dissolve
        pause 0.2
        show bg taxi car open
        hide kat
        with dissolve
        pause 0.2
        show bg taxi car closed
        "Because she eagerly jumps into a taxi with me afterwards and we head back to my place."
        "The only problem is that I can't keep from yawning the entire way back."
        scene bg livingroom with fade
        "Kat manages to ignore it in the taxi and most of the way into the house."
        scene bg bedroom1
        show kat
        with fade
        "But by the time we make it to my room, it's getting too loud and frequent for that."
        show kat sad
        kat.say "[hero.name]..."
        kat.say "Are you okay?"
        show kat sadsmile
        kat.say "Because you haven't stopped yawning for like twenty minutes straight!"
        mike.say "Oooh..."
        mike.say "I'm sorry, Kat..."
        mike.say "It's nothing personal."
        mike.say "I've just been working really hard the past couple of days."
        mike.say "And I guess it's catching up to me!"
        show kat smile
        "Kat nods, and I can see that she's definitely not mad at me for being tired."
        show kat sadsmile
        "But there's also a hint of disappointment in her eyes that she can't hide."
        kat.say "That's okay."
        kat.say "We don't have to do anything strenuous."
        kat.say "Not if you're to tired..."
        mike.say "No!"
        mike.say "No way!"
        mike.say "I've still got enough left in the tank..."
        "I start pulling off my clothes and making for the bed."
        show kat at center, zoomAt(1.5, (640, 1040)) with hpunch
        "But Kat puts a hand on my chest, stopping me in my tracks."
        show kat smile
        kat.say "Cut the bravado, [hero.name]."
        kat.say "At this rate, you'll be asleep before we're halfway done!"
        show kat defiant
        kat.say "And I know a great way to compromise..."
        hide kat
        show kat defiant
        with fade
        "Kat takes hold of my hand, and then she leads me to the edge of the bed."
        "Once there, she helps me out of the last of my clothes."
        show kat naked
        "Then she makes a show of stripping off her own."
    elif rand_intro == 4:
        scene bg house
        show kat smile
        with fade
        "The night out that I just treated Kat to went really well, almost perfectly - even if I do say so myself."
        "And that's not just me patting myself on the back either, because Kat's got a huge smile on her face too."
        "In fact she's the one pulling me in through the front door now that we're back at my place."
        scene bg livingroom
        show kat normal
        with fade
        "Though I do wonder if Kat's had a little too much fun tonight, as she looks more than a little tired."
        "And as we make it to my bedroom, she can't help letting out a pretty impressive yawn."
        scene bg bedroom1
        show kat yawn at right
        with fade
        kat.say "Oooh..."
        show kat sadsmile
        kat.say "Oh, sorry, [hero.name]..."
        show kat normal at right5 with ease
        kat.say "I don't know where that came from!"
        "I shake my head as I turn to close the door behind us."
        mike.say "No need to apologise, Kat."
        mike.say "It is getting a little late."
        mike.say "No shame in being tired."
        show kat at center with ease
        "I turn to see Kat walking towards the bed."
        show kat underwear with dissolve
        "She's already stripping off her clothes."
        "So it's no mystery what she's wanting us to do next."
        hide kat with dissolve
        "By the time I make it over there too, she's almost naked."
        "But when I get up close, I realise that Kat's not moving."
        "Instantly concerned, I lean in closer, trying to see what the problem is."
        show kat yawn naked at center, zoomAt (1.5, (640, 1040)) with dissolve
        "And that's when I notice her eyes are closed, also that she's making a soft sound."
        "It's snoring!"
        "Kat's fallen asleep and she's actually snoring right now!"
        "I'm already half undressed myself."
        "So I pull off the last of my clothes before I do anything else."
        "And then I put what I hope is a gentle hand on Kat's shoulder."
        mike.say "Ah..."
        mike.say "Kat?"
        mike.say "You mind, like, waking up?"
        show kat sadclosed
        kat.say "Urgh..."
        kat.say "Wha..."
        show kat surprised at center, zoomAt (1.0, (640, 1040)), startle
        show fx exclamation
        kat.say "Aargh!"
        hide fx
        hide kat
        show kat naked surprised
        with vpunch
        "I leap backwards as Kat flails her arms around."
        "Her eyes have popped open and she looks totally out of it!"
        mike.say "It's okay!"
        mike.say "It's okay..."
        mike.say "You just feel asleep, that's all."
        "Kat frowns and makes a vague grousing noise at first."
        "Then she seems to come round enough to think straight."
        show kat confused
        kat.say "No way..."
        kat.say "I never do that!"
        mike.say "Well, you were definitely snoring."
        mike.say "And I don't know how else explain the fact you're drooling!"
        "Kat moans and wipes her mouth with the back of her hand."
        kat.say "What?"
        show kat afraid
        kat.say "Oh no!"
        kat.say "That's SO embarrassing."
        show kat sad
        kat.say "And I don't want to fall asleep either."
        kat.say "I wanted to have some fun - you know?"
        "I nod, doing the best I can to look sympathetic."
        "And it's about then that an idea comes to me."
        mike.say "You can still have fun without using any energy, Kat."
        mike.say "Just leave it to me, okay?"
        show kat confused
        show fx question
        "Kat's forehead wrinkles and her eyes show her interest."
        "But when she speaks, she doesn't sound convinced."
        hide fx
        kat.say "But I'll just fall asleep again, [hero.name]!"
        kat.say "I won't be able to stay awake to enjoy whatever you're going to do!"
        mike.say "Oh, don't worry about that."
        show kat defiant
        mike.say "You'll stay awake, Kat."
        mike.say "I guarantee it!"
    $ game.room = "bedroom1"
    return

label kat_fuck_date_foreplay_male:
    menu:
        "Suggest a blowjob" if kat.sub >= 10:
            call kat_fuck_date_blowjob from _call_kat_fuck_date_blowjob
        "Eat her pussy" if hero.sexperience >= 5:
            call kat_fuck_date_cunnilingus from _call_kat_fuck_date_cunnilingus
        "Fuck her right now":
            pass
    call stop_all_sfx from _call_stop_all_sfx_45

    return _return

label kat_fuck_date_choices_male:
    menu:
        "Missionary":
            call kat_fuck_date_missionary (0) from _call_kat_fuck_date_missionary
        "Cowgirl" if hero.sexperience >= 5:
            call kat_fuck_date_cowgirl (5) from _call_kat_fuck_date_cowgirl
        "Doggy" if hero.sexperience >= 10:
            call kat_fuck_date_doggy (10) from _call_kat_fuck_date_doggy
    call stop_all_sfx from _call_stop_all_sfx_46

    return _return

label kat_fuck_date_sleep(location="hero"):
    scene bg bedroom1
    if game.hour > 19 or game.hour < 6:
        show kat naked
        if kat.is_sex_slave:
            kat.say "May I share your bed tonight, Master?"
        else:
            kat.say "Mmm...you cool with me spending the night here?"
        menu:
            "No":
                mike.say "No...I have to be up really early in the morning."
                "The sex was beyond incredible, but now I want to be alone."
                "Kat frowns in disappointment, clearly trying to shrug off the sense of rejection."
                kat.say "Okay...sleep well, I guess."
                "She shakes her head as she collects her things and leaves my bedroom."
                $ kat.love -= 3
                call sleep from _call_sleep_97
            "Yes":
                mike.say "YES...I mean, yes...if you want to!"
                "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                show cuddle kat
                "Kat curling up against me beneath the covers is almost as good as the sex - almost..."
                if kat.is_sex_slave:
                    kat.say "Sweet dreams, Master..."
                else:
                    kat.say "Sweet dreams, [hero.name]..."
                mike.say "You too, Kat..."
                $ kat.love += 3
                call sleep ("kat") from _call_sleep_98
    return

label kat_fuck_date_blowjob:
    "Right from the start I seems like there's a change in Kat's demeanour."
    "Before she was still in a playful mood, buzzing from out date."
    "But as soon as she reaches out to take hold of my cock, that changes."
    show kat blowjob naked handjob with fade
    "Now she appears to be more focused, like she's blocking out everything else."
    "And as she starts to stoke it into life, I think I recognise what I'm seeing."
    show kat blowjob forth
    pause 0.35
    show kat blowjob back
    pause 0.35
    show kat blowjob forth
    pause 0.35
    show kat blowjob back
    pause 0.35
    show kat blowjob forth
    pause 0.35
    show kat blowjob back
    "The way that Kat's solely concerned with the task at hand, I've noticed it before."
    "Because it's the exact change that comes over her when she's playing videogames too!"
    "Not casually messing around on the Z-Box with the likes of me."
    "But more like the single-minded way she plays in a serious competition."
    "It takes no time at all for Kat to have my cock hard and standing to attention."
    show kat blowjob eyes_closed mouth_lick
    "Then she leans forward and closes her eyes, parting her lips at the same time."
    "I realise that I've been holding my breath up to this moment."
    "But the sensation of the head passing between Kat's lips changes that."
    show kat blowjob blow
    "The feeling is so intense, the sense of anticipation so powerful."
    "All of that means I let out a gasp of sheer amazement as she gets going."
    "Not that the sounds I'm making seem to affect her in the slightest."
    "Kat doesn't miss a beat, smoothly taking more of my cock into her mouth."
    "She's not just swallowing it either, but licking and caressing with her lips."
    "I don't get the first feel of her teeth until it's a good way in there."
    "And even then she's sparing in her use of them, nibbling on infrequent occasions."
    "Just enough to punctuate the softer actions that are going on at the same time."
    "Slowly and surely, Kat begins to build up what she's doing."
    "Her movements are almost achingly slow at first."
    "But when she begins to pick up speed, it's with infinite care."
    "Everything seems to be thought out in advance, with a clear plan."
    "And things only change and progress at the precise moment they're intended to."
    "This means that everything builds at the same time and rate."
    "The things that Kat's doing to me on the one hand."
    "And the pleasure that it's building up in me on the other."
    "She has her hands braced against my thighs."
    "And she's squatting in front of me, rather than kneeling."
    "All of which means that she's bobbing up and down as she moves."
    "This seems to give Kat a greater range and more fluidity to her motions."
    "Which is something I'm definitely feeling the benefit of right now."
    "Because she's finally built up her speed to what feels like the limit."
    "And it's ramped up the pleasure I'm feeling too!"
    "In fact, it's starting to feel like it's too much to handle."
    mike.say "Oh fuck..."
    mike.say "Kat..."
    mike.say "I'm going to cum!"
    menu:
        "Cum in her mouth":
            show sexinserts head kat zorder 1 at center, zoomAt(1.0, (680, 870))
            "Even though I'm unable to stop myself from losing it, I still have one choice."
            "And that's to leave my cock right where it is when the time comes."
            show sexinserts head kat cum at center, zoomAt(1.0, (680, 870))
            show kat blowjob cum
            with hpunch
            $ kat.love += 3
            $ kat.sub += 1
            "Luckily for me, Kat seems to be well aware of the choice that I'm making."
            with hpunch
            "And she handles it smoothly, swallowing everything that I have to give."
            show sexinserts head kat -cum at center, zoomAt(1.0, (680, 870))
            show kat blowjob out breath eyes_open
            with hpunch
            "Once she's done, I feel the strength drain out of my limbs all at once."
            "And I collapse backwards onto the bed."
        "Cum on her face":
            "Even though I'm unable to stop myself from losing it, I still have one choice."
            show kat blowjob out eyes_surprised breath -handjob
            "And that's to pull my cock out of Kat's mouth when the time comes."
            show kat blowjob eyes_open
            "She lets out a gasp as I slide free, and waits patiently for what comes next."
            show kat blowjob eyes_closed cum with hpunch
            $ kat.love += 1
            $ kat.sub += 2
            "A second later, I shoot my load straight into her face."
            with hpunch
            "Lines of hot, white cum stripe Kat's cheeks, running downwards to her chin."
            show kat blowjob eyes_open tongue2 handjob with hpunch
            "Once it's done, I feel the strength drain out of my limbs all at once."
            "And I collapse backwards onto the bed."
    return

label kat_fuck_date_cunnilingus:
    show kat cunnilingus naked mike eyes_open mouth_close with fade
    "I lower myself slowly down in front of Kat until I'm kneeling on the floor."
    "At the same time I reach out with both hands, placing them upon her knees."
    "Kat watches with evident interest as I pull them apart a moment later."
    "And I note that she makes no effort to stop me or else ask what I'm doing."
    show sexinserts bottom kat at center, zoomAt(0.75, (740, 580)) with dissolve
    "But then I lean in closer still, putting my head between her thighs."
    "And my guess is that it's not hard for her to figure out what I have in mind."
    "That's one of the main reasons I choose not to linger too long before getting started."
    "Because what other intentions could I have down here?"
    "Other than to part my lips and begin using my tongue."
    hide sexinserts with dissolve
    "I close my eyes as I do so, relying on what the tip touches to guide me."
    "And the first thing that it does touch is soft, yet uneven folds."
    show kat cunnilingus tongue2 eyes_close
    pause 0.2
    show kat cunnilingus tongue3
    pause 0.2
    show kat cunnilingus tongue1
    pause 0.2
    show kat cunnilingus tongue2
    pause 0.2
    show kat cunnilingus tongue3
    pause 0.2
    show kat cunnilingus tongue1
    "That alone would have been enough to tell me that I was in the right place."
    "But the sound that I hear at the same time confirms it."
    kat.say "Mmm..."
    kat.say "Oh..."
    kat.say "Oh god!"
    "Kat's gasped words let me know that I'm on the right track."
    "But it's not like I pause while she's uttering them."
    "Instead I'm already moving my tongue, using it to trace those folds."
    show kat cunnilingus tongue2
    pause 0.2
    show kat cunnilingus tongue3
    pause 0.2
    show kat cunnilingus tongue1
    pause 0.2
    show kat cunnilingus tongue2
    pause 0.2
    show kat cunnilingus tongue3
    pause 0.2
    show kat cunnilingus tongue1 eyes_open mouth_open
    "I go clockwise, working my way around the very edge of her pussy."
    "And with each trip around, I go a little closer to the centre too."
    "All the while I'm doing this, I know that it's working in the way I want."
    "Because I can feel the heat coming off of Kat as I'm doing it."
    "That and the fact that her pussy is getting slicker by the second."
    show kat cunnilingus tongue2 eyes_close
    pause 0.175
    show kat cunnilingus tongue3
    pause 0.175
    show kat cunnilingus tongue1
    pause 0.175
    show kat cunnilingus tongue2
    pause 0.175
    show kat cunnilingus tongue3 hold at center, startle(0.05,-10)
    pause 0.175
    show kat cunnilingus tongue1
    pause 0.175
    show kat cunnilingus tongue2
    pause 0.175
    show kat cunnilingus tongue3
    pause 0.175
    show kat cunnilingus tongue1
    "By now my tongue isn't so much travelling around the edge either."
    "It's actually beginning to sink downwards and into the centre."
    "I almost feel like there's a force pulling me in that direction too."
    "Though the more rational part of my mind is sure that's just imagination."
    "Nothing more than a compulsion to do all I can to please Kat."
    "And thus the need to get as close to her most sensitive parts as possible."
    "But whatever the reason, I know that it's working."
    show kat cunnilingus tongue2
    pause 0.15
    show kat cunnilingus tongue3 at startle(0.05,-10)
    pause 0.15
    show kat cunnilingus tongue1
    pause 0.15
    show kat cunnilingus tongue2
    pause 0.15
    show kat cunnilingus tongue3 at startle(0.05,-10)
    pause 0.15
    show kat cunnilingus tongue1
    pause 0.15
    show kat cunnilingus tongue2 mouth_close
    pause 0.15
    show kat cunnilingus tongue3 at startle(0.05,-10)
    pause 0.15
    show kat cunnilingus tongue1
    pause 0.15
    show kat cunnilingus tongue2
    pause 0.15
    show kat cunnilingus tongue3 at startle(0.05,-10)
    pause 0.15
    show kat cunnilingus tongue1
    "Kat's quivering and quaking from what I'm doing to her now."
    "And the grip that I have on her thighs is tightening as a result."
    "Before I was just making sure that was in the best position I could be."
    "But now I'm beginning to have to hold Kat down in order to keep it up."
    "More than once I almost find myself thrown off as she jerks beneath me."
    "And in response I find that I can't help sticking my tongue even deeper into her."
    show kat cunnilingus tongue2
    pause 0.15
    show kat cunnilingus tongue3 at startle(0.05,-10)
    pause 0.15
    show kat cunnilingus tongue1
    pause 0.15
    show kat cunnilingus tongue2
    pause 0.15
    show kat cunnilingus tongue3 at startle(0.05,-10)
    pause 0.15
    show kat cunnilingus tongue1
    pause 0.15
    show kat cunnilingus tongue2 mouth_hurt
    pause 0.15
    show kat cunnilingus tongue3 at startle(0.05,-10)
    pause 0.15
    show kat cunnilingus tongue1
    pause 0.15
    show kat cunnilingus tongue2
    pause 0.15
    show kat cunnilingus tongue3 at startle(0.05,-10)
    pause 0.15
    show kat cunnilingus tongue1
    "By now my head is turned on it's side, just so I can push my tongue in further still."
    "Every time I move it, I feel like that's going to be the moment that seals the deal."
    "Like it'll be the tiniest of movements that'll finally push her over the edge."
    "But when it actually happens, I'm not prepared for it at all."
    show kat cunnilingus tongue2
    pause 0.125
    show kat cunnilingus tongue3 at startle(0.05,-10)
    pause 0.125
    show kat cunnilingus tongue1
    pause 0.125
    show kat cunnilingus tongue2
    pause 0.125
    show kat cunnilingus tongue3 at startle(0.05,-10)
    pause 0.125
    show kat cunnilingus tongue1
    pause 0.125
    show kat cunnilingus tongue2
    pause 0.125
    show kat cunnilingus tongue3 at startle(0.05,-10)
    pause 0.125
    show kat cunnilingus tongue1
    pause 0.125
    show kat cunnilingus tongue2 eyes_up
    pause 0.125
    show kat cunnilingus tongue3 at startle(0.05,-10)
    pause 0.125
    show kat cunnilingus tongue1
    pause 0.125
    show kat cunnilingus tongue2
    pause 0.125
    show kat cunnilingus tongue3 at startle(0.05,-10)
    pause 0.125
    show kat cunnilingus tongue1 mouth_open with vpunch
    $ kat.love += 4
    "Suddenly Kat lets out a cry."
    "And by that, I don't mean a moan or a groan."
    "I mean she genuinely makes a sound so loud that anyone in the house could hear it!"
    "Normally I'd have been quick to ask her to keep it down, to stop being so noisy."
    with hpunch
    "But at the same time she clenches her thighs together like a fleshy vice."
    "And that effectively pins me down, muffling my lips against her pussy."
    with hpunch
    "So I'm stuck there, listening to Kat wake the entire house as she cums."
    show kat cunnilingus eyes_close
    "Only when it subsides and her muscles slacken can I start to free myself."
    "But as I raise my head, I see there's no longer any point in telling her to stop."
    "Because I'm greeted with the sight of Kat laid flat out on the mattress."
    return

label kat_fuck_date_missionary(sexperience_min):
    scene bg black
    show kat missionary mouth_pleasure
    with fade
    kat.say "Well?"
    kat.say "What are you waiting for?"
    mike.say "Nothing, Kat..."
    mike.say "Nothing at all..."
    show kat missionary mike
    mike.say "I'm totally on it, you'll see!"
    menu:
        "Fuck her pussy":
            "Actually I'm not totally on it."
            "I'm still trying to decide where to put it!"
            "But a moment later, I feel something that decides it for me."
            "The head of my cock is down between Kat's thighs."
            "And I catch the slightest sensation of it rubbing against her pussy."
            "That's all it takes to make up my mind."
            "From that point on, I'm almost on auto-pilot."
            call check_condom_usage (kat) from _call_check_condom_usage_133
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show kat missionary condom
            "Without a conscious thought, my hands reach out and take hold of Kat's thighs."
            "Then I part them, making sure that they're spread wide enough for me to get right in there."
            "With all that done, there's nothing to stop me from finally getting down to it."
            "But for all of Kat's demands, I still decide to take things a little slowly."
            "Sure, it might frustrate her in the short term."
            "But it'll allow me to build up the intensity of what I'm doing a lot more."
            show kat missionary vaginal eyes_pleasure
            "This means that I begin to stroke the head of my cock against the lips of Kat's pussy."
            "As soon as I do this, I can feel the whole of her body start to quake and quiver."
            "And the sensation is enough to make me start to move a little faster than before."
            show kat missionary eyes_normal mouth_normal
            "With each pass I make, Kat becomes more animated and her pussy gets wetter too."
            "So that pretty soon I can feel her lips starting to open up for me."
            show kat missionary eyes_normal mouth_pleasure
            "At first I can only push my way perhaps an inch inside."
            "But that tiny foothold is more than enough to spur me on to try harder."
            "Every time I push, Kat's resistance weakens a little more."
            show kat missionary eyes_pleasure mouth_normal full
            "Until, with one final effort, I manage to get all the way inside."
            "Kat's head rolls backwards as I sink into her, going as deep as I can."
            "Her eyes close and she lets out a confused, murmuring stream of nonsense sounds."
            "All of which I choose to interpret as signs that I'm giving her what she wants."
            show kat missionary eyes_normal speed with hpunch
            "And so I push onwards, redoubling my efforts to pleasure Kat."
            "Now I'm totally up to speed and setting a comfortable pace."
            "Or at least one that's comfortable for me."
            "The effect it seems to be having on Kat is something quite different."
            "I watch as she begins to twist and thrash on the mattress before me."
            "There's even a moment when I wonder if I shouldn't slow down, or even stop."
            "Because I'm worried that she might not be able to handle it."
            "But then I remember all the demands that Kat made of me before we began."
            "And on balance, I think it'd be better to overwhelm her with my performance."
            "As opposed to being told off for not putting in the work afterwards."
            "The plan certainly seems to be paying off too."
            show kat missionary eyes_pleasure
            "I can see Kat's hands beginning to roam all over her body."
            "At first I think it's just part of the way she's moving in general."
            "But then I see them reach the most sensual parts of her body."
            show kat missionary mouth_pleasure
            "Where they begin to caress and massage with uncanny skill."
            "Though it's when they arrive at Kat's petite breasts that I'm really drawn into watching."
            "Thus far, they've been jiggling around in sympathy with the rest of Kat's body."
            "But now I stare in amazement as her hands massage and squeeze them."
            show kat missionary eyes_normal
            "Kat's fingers pinch and roll her nipples too, making them stiffer then ever."
            "I can feel my own hands tensing and clenching in sympathy."
            "Because I want to be doing that so badly myself!"
            show kat missionary eyes_pleasure mouth_hurt
            "The effect is only made more intense by the sound Kat begins to make at the same time."
            "She's moaning again, vocalising the sense of release that it's providing to her."
            "And the sound is more than enough to begin pushing me over the edge."
            show kat missionary eyes_ahegao
            "Because it tells me that Kat's starting to cum too!"
            call cum_reaction (kat, 'vaginal', sexperience_min) from _call_cum_reaction_245
            if _return == "vaginal_outside":
                "I don't want to do it, but I have to pull out before the end."
                if not CONDOM:
                    "That's just the inevitable consequences of not using a condom."
                    show sexinserts chest kat zorder 1 at center, zoomAt(1, (710, 820))
                    show sexinserts belly kat as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                show kat missionary eyes_pleasure out -speed
                with hpunch
                "I do it as quickly and smoothly as I can, pulling out in the blink of an eye."
                "But the sensation is still enough to make Kat gasp."
                "And it seems trigger her orgasm too."
                $ kat.love += 1
                show kat missionary eyes_normal mouth_normal cum
                if CONDOM:
                    with hpunch
                    "She shakes and moans as I shoot my load."
                else:
                    show sexinserts chest kat cum zorder 1 at center, zoomAt(1, (710, 820))
                    show sexinserts belly kat cum as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                    with hpunch
                    "She shakes and moans as I shoot my load over her."
                    show kat missionary bodycum -cum with hpunch
                    "Seeming not to notice as it spatters her buttocks and thighs."
                    hide sexinserts
                    hide bellycum
            elif _return == "vaginal_condom":
                "I feel a great sense of relief that we chose to use a condom."
                "As it means that I can simply keep on going until the inevitable happens."
                "And when it does, I can feel Kat being swept along with me."
                show kat missionary eyes_pleasure mouth_normal -speed with hpunch
                "I freeze as we cum within seconds of each other, unable to move."
                "But the sensation is more than worth the sacrifice."
                with hpunch
                "A moment of almost perfect unity between us."
                show kat missionary eyes_normal mouth_pleasure out cum with hpunch
                "Made all the more precious by the very fact that it's so fleeting."
            elif _return == "vaginal_inside_pregnant":
                kat.say "Don't stop..."
                show kat missionary eyes_normal
                kat.say "It's...okay..."
                "I feel a great sense of relief as Kat reminds me that she's already pregnant."
                "As it means that I can simply keep on going until the inevitable happens."
                "And when it does, I can feel Kat being swept along with me."
                $ kat.love += 2
                show kat missionary eyes_ahegao mouth_normal tongueout cum -speed with hpunch
                "I freeze as we cum within seconds of each other, unable to move."
                "But the sensation is more than worth the sacrifice."
                with hpunch
                "A moment of almost perfect unity between us."
                show kat missionary eyes_normal mouth_pleasure out vaginaldrip -cum with hpunch
                "Made all the more precious by the very fact that it's so fleeting."
            elif _return == "vaginal_inside_pill":
                kat.say "Don't stop..."
                show kat missionary eyes_normal
                kat.say "I'm...on the...pill..."
                "I feel a great sense of relief as Kat reminds me that she's taking the pill."
                "As it means that I can simply keep on going until the inevitable happens."
                "And when it does, I can feel Kat being swept along with me."
                $ kat.love += 2
                show kat missionary eyes_ahegao mouth_normal tongueout cum -speed with hpunch
                "I freeze as we cum within seconds of each other, unable to move."
                "But the sensation is more than worth the sacrifice."
                with hpunch
                "A moment of almost perfect unity between us."
                show kat missionary eyes_normal mouth_pleasure out vaginaldrip -cum with hpunch
                "Made all the more precious by the very fact that it's so fleeting."
            elif _return == "vaginal_inside_happy":
                kat.say "Don't stop..."
                show kat missionary mouth_pleasure
                kat.say "Keep...going..."
                "At first I don't understand what Kat's asking me to do."
                "And that confusion is what causes me to lose my concentration."
                with hpunch
                "A moment later I feel myself starting to cum."
                $ kat.love += 5
                $ kat.impregnate()
                show kat missionary eyes_ahegao mouth_normal tongueout cum -speed with hpunch
                "I freeze, unable to move as I shoot my load into Kat."
                with hpunch
                "And just then I remember that we didn't use a condom!"
                show kat missionary eyes_pleasure mouth_pleasure out vaginaldrip -cum
                "The cold touch of fear runs down my spine."
                "And I can't believe what just happened."
                "But much to my surprise, Kat seems delighted!"
            elif _return == "vaginal_inside_mad":
                kat.say "Stop!"
                show kat missionary eyes_normal mouth_normal
                kat.say "You have to...stop..."
                "At first I don't understand what Kat's asking me to do."
                "And that confusion is what causes me to lose my concentration."
                $ kat.love -= 5
                $ kat.impregnate()
                show kat missionary eyes_pleasure mouth_hurt cum -speed with hpunch
                "A moment later I feel myself starting to cum."
                with hpunch
                "I freeze, unable to move as I shoot my load into Kat."
                with hpunch
                "And just then I remember that we didn't use a condom!"
                show kat missionary eyes_normal out vaginaldrip -cum
                "The cold touch of fear runs down my spine."
                "And I can't believe what just happened."
                "Kat turns her head back to stare at me, horror visible in her eyes."
                "Neither of us seems able to speak, only to gaze at the other with disbelief and dread."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Actually I'm not totally on it."
            "I'm still trying to decide where to put it!"
            "But a moment later, I feel something that decides it for me."
            "The head of my cock is down between Kat's thighs."
            "And I catch the slightest sensation of it rubbing against her buttocks."
            "That's all it takes to make up my mind."
            "From that point on, I'm almost on auto-pilot."
            "Without a conscious thought, my hands reach out and take hold of Kat's thighs."
            "Then I part them, making sure that they're spread wide enough for me to get right in there."
            "With all that done, there's nothing to stop me from finally getting down to it."
            "But for all of Kat's demands, I still decide to take things a little slowly."
            "Sure, it might frustrate her in the short term."
            "But it'll allow me to build up the intensity of what I'm doing a lot more."
            show kat missionary anal eyes_pleasure
            "This means that I begin to stroke the head of my cock around the edge of Kat's hole."
            "As soon as I do this, I can feel the whole of her body start to quake and quiver."
            "And the sensation is enough to make me start to move a little faster than before."
            show kat missionary eyes_normal mouth_normal
            "With each pass I make, Kat becomes more animated and her ass gets slicker too."
            "So that pretty soon I can feel her muscles starting to relax and open up for me."
            show kat missionary eyes_normal mouth_pleasure
            "At first I can only push my way perhaps an inch inside."
            "But that tiny foothold is more than enough to spur me on to try harder."
            "Every time I push, Kat's resistance weakens a little more."
            show kat missionary eyes_pleasure mouth_normal full
            "Until, with one final effort, I manage to get all the way inside."
            "Kat's head rolls backwards as I sink into her, going as deep as I can."
            "Her eyes close and she lets out a confused, murmuring stream of nonsense sounds."
            "All of which I choose to interpret as signs that I'm giving her what she wants."
            show kat missionary eyes_normal speed with hpunch
            "And so I push onwards, redoubling my efforts to pleasure Kat."
            "Now I'm totally up to speed and setting a comfortable pace."
            "Or at least one that's comfortable for me."
            "The effect it seems to be having on Kat is something quite different."
            "I watch as she begins to twist and thrash on the mattress before me."
            "There's even a moment when I wonder if I shouldn't slow down, or even stop."
            "Because I'm worried that she might not be able to handle it."
            "But then I remember all the demands that Kat made of me before we began."
            "And on balance, I think it'd be better to overwhelm her with my performance."
            "As opposed to being told off for not putting in the work afterwards."
            "The plan certainly seems to be paying off too."
            show kat missionary eyes_pleasure
            "I can see Kat's hands beginning to roam all over her body."
            "At first I think it's just part of the way she's moving in general."
            "But then I see them reach the most sensual parts of her body."
            show kat missionary mouth_pleasure
            "Where they begin to caress and massage with uncanny skill."
            "Though it's when they arrive at Kat's petite breasts that I'm really drawn into watching."
            "Thus far, they've been jiggling around in sympathy with the rest of Kat's body."
            "But now I stare in amazement as her hands massage and squeeze them."
            show kat missionary eyes_normal
            "Kat's fingers pinch and roll her nipples too, making them stiffer then ever."
            "I can feel my own hands tensing and clenching in sympathy."
            "Because I want to be doing that so badly myself!"
            show kat missionary eyes_pleasure mouth_hurt
            "The effect is only made more intense by the sound Kat begins to make at the same time."
            "She's moaning again, vocalising the sense of release that it's providing to her."
            "And the sound is more than enough to begin pushing me over the edge."
            show kat missionary eyes_ahegao
            "Because it tells me that Kat's starting to cum too!"
            call cum_reaction (kat, 'anal', sexperience_min) from _call_cum_reaction_246
            if _return == 'anal_inside':
                "I feel a great sense of relief that I chose to use the back door."
                "As it means that I can simply keep on going until the inevitable happens."
                show kat missionary cum with hpunch
                "And when it does, I can feel Kat being swept along with me."
                $ kat.sub += 2
                show kat missionary eyes_ahegao mouth_normal tongueout -speed with hpunch
                "I freeze as we cum within seconds of each other, unable to move."
                with hpunch
                "But the sensation is more than worth the sacrifice."
                "A moment of almost perfect unity between us."
                show kat missionary eyes_normal mouth_pleasure out analdrip -cum
                "Made all the more precious by the very fact that it's so fleeting."
            elif _return == 'anal_outside':
                "I don't know why I want to do it."
                "But I feel the need to pull out before the end."
                "It's just one of those sudden urges that sometimes takes a hold of me."
                "And I know that I have to give in to it."
                show kat missionary eyes_pleasure out -speed
                show sexinserts chest kat zorder 1 at center, zoomAt(1, (710, 820))
                show sexinserts belly kat as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                "I do it as quickly and smoothly as I can, pulling out in the blink of an eye."
                "But the sensation is still enough to make Kat gasp."
                "And it seems trigger her orgasm too."
                $ kat.sub += 1
                show sexinserts chest kat cum zorder 1 at center, zoomAt(1, (710, 820))
                show sexinserts belly kat cum as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                show kat missionary eyes_normal mouth_normal cum
                with hpunch
                "She shakes and moans as I shoot my load over her."
                show kat missionary bodycum -cum with hpunch
                "Seeming not to notice as it spatters her buttocks and thighs."
                hide sexinserts
                hide bellycum
    return

label kat_fuck_date_doggy(sexperience_min):
    scene bg black
    show kat doggy mouth_pleasure naked
    with fade
    "Kat makes it there first, and she quickly climbs onto the mattress."
    "And once she's on all fours, she actually feels the need to speak."
    show kat doggy mouth_open
    kat.say "No fooling around tonight, [hero.name], okay?"
    kat.say "I'm going to tell you what I want once, and only once."
    kat.say "Then I want you to do it to me until I cum, right?"
    show kat doggy mouth_pleasure
    "My eyes go wide as Kat makes her demands of me."
    "But I hurry to nod in agreement all the same."
    mike.say "Y...yeah, Kat..."
    mike.say "Whatever you want!"
    "Kat nods."
    "And then she lays out her demands."
    show kat doggy mouth_open
    kat.say "I want you to get up behind me."
    kat.say "And then I want you to fuck, [hero.name]."
    kat.say "I want you to fuck me like I'm an animal!"
    kat.say "You think you can do that?"
    "I can already feel myself getting hard as Kat says all of this."
    "And my head is still nodding away like it's going to tumble off my shoulders."
    "I hurry to clamber onto the bed, getting into the position that Kat wanted."
    show kat doggy eyes_close mouth_pleasure mike
    "My hands reach out and take hold of her around the waist."
    "But for a moment, I find that I can't do anything other than stare forwards."
    "The shape of Kat's body is laid out before me, and it just looks so good!"
    show kat doggy eyes_open mouth_open
    kat.say "[hero.name]!"
    kat.say "What are you waiting for?!?"
    "I almost leap out of my skin as Kat turns her head to look back at me."
    "In reality, she didn't seriously scold me or anything like that."
    "She's just wanting to know that I'm on the same page as she is."
    "But it's still enough to make me jump to do as she says."
    mike.say "I'm on it!"
    mike.say "I'm totally on it!"
    "At the same time as I'm saying this, I pull Kat sharply backwards."
    "This means that her ass is pressed hard against my groin."
    "And my cock pushes its way between her thighs at the same time."
    show kat doggy mouth_pleasure
    kat.say "Oh!"
    kat.say "Oh yeah..."
    kat.say "That's more like it!"
    "I feel a surge of relief as Kat lets me know that she approves."
    "But now that I have her literally in my hands, there's another problem."
    "Because now I have to decide what I'm going to do with her!"
    menu:
        "Fuck her pussy":
            "Since Kat's champing at the bit to get going, I need to act fast."
            "And that makes the pussy the obvious choice out of the two options."
            "So I make sure that I'm at the correct angle."
            "And then I get ready to make my first move."
            call check_condom_usage (kat) from _call_check_condom_usage_134
            if _return == False:
                return "leave_without_gain"
            "All it takes is one experimental move forwards for my eyes to pop open."
            "And that's because all at once, I know what kind of a state Kat's in."
            "No wonder she came right out and asked me to fuck her like an animal."
            "From what I can feel down there, she's on heat like one right now!"
            "Everything my cock touches is hot, slick and ready to go."
            "Even after hearing Kat's demands, I was sure I'd have to do some preparing."
            "Foreplay and teasing were what I had in mind."
            "But I don't think that I'm going to need any of that now!"
            "I feel the head of my cock slide along the lips of Kat's pussy."
            "And the sensation is like sliding across a slippery floor."
            show kat doggy eyes_close
            "At the same time, the contact makes her moan too."
            "The sound is deep and sensual, filled with need."
            "And it's more than enough to spur me on as well!"
            "As soon as I feel her lips parting, I begin to pile on the pressure."
            show kat doggy mouth_open
            "Kat's moans deepen as I do this, becoming almost desperate."
            "She lowers herself down too, trying to make my task easier."
            "I don't know if the move works, or if I was about to succeed anyway."
            "But whatever the true cause, the result is the same."
            show kat doggy eyes_up
            "Kat opens to me like a flower, and my cock sinks deep into her body."
            "And from that moment on there's nothing like conscious thought involved."
            "Sheer animal instinct seems to take over, guiding all of my actions."
            "So it seems like Kat's going to get what she wants."
            "Because the primitive that's grabbed the controls in me wants the same thing."
            show kat doggy eyes_open
            "Instantly I push all the way into Kat, going as deep as I possibly can."
            "But once I'm there, I don't stop to enjoy the sensation."
            show kat doggy eyes_close speed with hpunch
            "Instead I begin to thrust in and out of her without pause."
            "The effect this has on her is instant and dramatic."
            "Kat moans, her head swaying at the same time as her body quivers."
            "It's hard to tell if the motion is her own."
            "Because I'm slamming into her so hard that it's got to be having an effect."
            "In fact, Kat's moving so much that I can even see her breasts bouncing."
            "Which is quite something, as they're pretty petite!"
            "The sound of my thighs slapping against Kat's is pretty loud by now."
            "But it's in danger of being drowned out by the cries she's letting out."
            kat.say "Ah..."
            show kat doggy mouth_pleasure
            kat.say "Oh..."
            kat.say "Oh god..."
            kat.say "Harder..."
            show kat doggy eyes_up mouth_open
            kat.say "Fuck me...harder!"
            "I'm already doing all I can to make that happen."
            "And I don't know if there's any way I could be doing more."
            "But all the same, I find myself striving to meet Kat's demands."
            show kat doggy up
            "I push harder and move faster, putting all of my energy into it."
            "And it doesn't take long for me to reap the rewards of my efforts."
            show kat doggy mouth_hurt eyes_close
            kat.say "Y...yeah..."
            kat.say "That's it..."
            kat.say "Gonna cum!"
            "I hold on tight as Kat's body succumbs to her orgasm."
            with hpunch
            "Muscles clench and squeeze, making me gasp at the sensation."
            "And then I feel her pulling me into it too, making me join her."
            call cum_reaction (kat, 'vaginal', sexperience_min) from _call_cum_reaction_247
            if _return == "vaginal_outside":
                "Suddenly I'm the one making all the noise."
                show kat doggy down -speed
                "I'm grunting and panting as I pull out of Kat."
                with hpunch
                "And I only just manage it before I shoot my load."
                $ kat.love += 1
                show kat doggy eyes_up mouth_open tongueout with hpunch
                "Kat gasps as my cock pops out of her."
                with hpunch
                "And I swear that the result is her coming a second time."
                show kat doggy eyes_close mouth_pleasure
                "Afterwards she slides off of me and collapses onto the bed."
                "I do the same, falling backwards in a state of complete exhaustion."
            else:
                "Suddenly I'm the one making all the noise."
                $ kat.love += 3
                show kat doggy eyes_up mouth_open tongueout -speed
                if not CONDOM:
                    show kat doggy cum
                    $ kat.impregnate()
                with hpunch
                "I'm grunting and panting as I shoot my load."
                with hpunch
                "And I do that when I'm as deep as I can go."
                with hpunch
                "This means Kat takes all of it without a thing held back."
                with hpunch
                "And I swear that the result is her coming a second time."
                show kat doggy eyes_close mouth_pleasure
                "Afterwards she slides off of me and collapses onto the bed."
                "I do the same, falling backwards in a state of complete exhaustion."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Since Kat's champing at the bit to get going, I need to act fast."
            "But I also get the feeling that she's going to want to get rough along the way."
            "Which means that using the back door would be the better choice."
            "So I make sure that I'm at the correct angle."
            "And then I get ready to make my first move."
            "All it takes is one experimental move forwards for my eyes to pop open."
            "And that's because all at once, I know what kind of a state Kat's in."
            "No wonder she came right out and asked me to fuck her like an animal."
            "From what I can feel down there, she's on heat like one right now!"
            "Everything my cock touches is hot, slick and ready to go."
            "Even after hearing Kat's demands, I was sure I'd have to do some preparing."
            "Foreplay and teasing were what I had in mind."
            "But I don't think that I'm going to need any of that now!"
            "I feel the head of my cock slide between Kat's buttocks."
            "And the sensation is like sliding across a slippery floor."
            show kat doggy eyes_close
            "At the same time, the contact makes her moan too."
            "The sound is deep and sensual, filled with need."
            "And it's more than enough to spur me on as well!"
            "As soon as I feel her muscles relaxing, I begin to pile on the pressure."
            show kat doggy mouth_open
            "Kat's moans deepen as I do this, becoming almost desperate."
            "She lowers herself down too, trying to make my task easier."
            "I don't know if the move works, or if I was about to succeed anyway."
            "But whatever the true cause, the result is the same."
            show kat doggy eyes_up
            "Kat opens to me like a flower, and my cock sinks deep into her body."
            "And from that moment on there's nothing like conscious thought involved."
            "Sheer animal instinct seems to take over, guiding all of my actions."
            "So it seems like Kat's going to get what she wants."
            "Because the primitive that's grabbed the controls in me wants the same thing."
            show kat doggy eyes_open
            "Instantly I push all the way into Kat, going as deep as I possibly can."
            "But once I'm there, I don't stop to enjoy the sensation."
            show kat doggy eyes_close speed with hpunch
            "Instead I begin to thrust in and out of her without pause."
            "The effect this has on her is instant and dramatic."
            "Kat moans, her head swaying at the same time as her body quivers."
            "It's hard to tell if the motion is her own."
            "Because I'm slamming into her so hard that it's got to be having an effect."
            "In fact, Kat's moving so much that I can even see her breasts bouncing."
            "Which is quite something, as they're pretty petite!"
            "The sound of my thighs slapping against Kat's is pretty loud by now."
            "But it's in danger of being drowned out by the cries she's letting out."
            kat.say "Ah..."
            show kat doggy mouth_pleasure
            kat.say "Oh..."
            kat.say "Oh god..."
            kat.say "Harder..."
            show kat doggy eyes_up mouth_open
            kat.say "Fuck me...harder!"
            "I'm already doing all I can to make that happen."
            "And I don't know if there's any way I could be doing more."
            "But all the same, I find myself striving to meet Kat's demands."
            show kat doggy up
            "I push harder and move faster, putting all of my energy into it."
            "And it doesn't take long for me to reap the rewards of my efforts."
            show kat doggy mouth_hurt eyes_close
            kat.say "Y...yeah..."
            kat.say "That's it..."
            kat.say "Gonna cum!"
            "I hold on tight as Kat's body succumbs to her orgasm."
            with hpunch
            "Muscles clench and squeeze, making me gasp at the sensation."
            "And then I feel her pulling me into it too, making me join her."
            call cum_reaction (kat, 'anal', sexperience_min) from _call_cum_reaction_248
            if _return == 'anal_inside':
                "Suddenly I'm the one making all the noise."
                $ kat.sub += 2
                show kat doggy eyes_up mouth_open tongueout cum -speed with hpunch
                "I'm grunting and panting as I shoot my load."
                with hpunch
                "And I do that when I'm as deep as I can go."
                with hpunch
                "This means Kat takes all of it without a thing held back."
                with hpunch
                "And I swear that the result is her coming a second time."
                show kat doggy eyes_close mouth_pleasure
                "Afterwards she slides off of me and collapses onto the bed."
                "I do the same, falling backwards in a state of complete exhaustion."
            elif _return == 'anal_outside':
                "Suddenly I'm the one making all the noise."
                show kat doggy down -speed
                "I'm grunting and panting as I pull out of Kat."
                with hpunch
                "And I only just manage it before I shoot my load."
                $ kat.sub += 1
                show kat doggy eyes_up mouth_open tongueout with hpunch
                "Kat gasps as my cock pops out of her."
                with hpunch
                "And I swear that the result is her coming a second time."
                show kat doggy eyes_close mouth_pleasure
                "Afterwards she slides off of me and collapses onto the bed."
                "I do the same, falling backwards in a state of complete exhaustion."
    return

label kat_fuck_date_cowgirl(sexperience_min):
    "Once we're there, I lie down on my back and beckon to Kat."
    mike.say "Come on, Kat..."
    mike.say "Climb aboard!"
    scene bg black
    show kat cowgirl mouth_pleasure
    with fade
    "I notice that Kat can't help smiling as she climbs onto the bed."
    "And she seems genuinely excited as she straddles my thighs too."
    "But that surprise turns into a knowing anticipation when she looks down."
    "Because that's the moment that she sees just how hard my cocks getting."
    "Kat watches intently as it begins to rise up in front of her."
    "And I have to try hard not to laugh at the look of amazement on her face."
    kat.say "Is...is that because of me?"
    kat.say "Did I do that?!?"
    mike.say "It's all because of you, Kat."
    mike.say "Now how about we find somewhere to put it?"
    menu:
        "Fuck her pussy":
            "Kat nods and reaches down to take a firm hold of my cock."
            mike.say "How about right there, Kat?"
            call check_condom_usage (kat) from _call_check_condom_usage_135
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show kat cowgirl condom
            "Kat's still got hold of my cock as we finally get down to it."
            "And now that we are, she doesn't seem inclined to let go of it either."
            "Instead I watch as she presses the head against the lips of her pussy."
            "At the same time I reach up and place my hand gently on her haunches."
            "Then I begin to manoeuvre her into position, guiding her into raising herself upwards."
            "Kat doesn't say a word, but at the same time she seems to be paying close attention."
            "I can see her interpreting what I need her to do next and reacting in kind."
            show kat cowgirl vaginal mouth_open
            "This means that when I start to pull her downwards, Kat's right there with me."
            "We're moving together, maybe not in perfectly synchronised motions."
            "But it's more than enough to stroke the head of my cock down the length of her pussy."
            "For me the sensation is incredible, and I can already see Kat's cheeks flushing."
            "Plus the look she has on her face tells me that she's enjoying it too."
            show kat cowgirl eyes_close mouth_pleasure
            "A moment later I look up to see a change in her expression."
            "It's nothing dramatic, more the fact that her eyes are closing."
            "And at the same time her lips slowly part too."
            "What really catches me off-guard is the way that's mirrored elsewhere too."
            "Watching Kat's face, I almost fail to notice that the lips of her pussy are parting too!"
            "This means that by the time she's opened her mouth, she's opened down there as well."
            "The first thing I know about it is when Kat suddenly begins to sink downwards."
            "And in the split-second after that, I feel her swallowing me whole."
            "Now it's my turn to close my eyes and be overwhelmed."
            "I'm supposed to be holding onto Kat right now, to be guiding her motions."
            "But all I can do is lie back as she keeps on sinking down."
            "To me it feels like it takes an eternity for me to fill her."
            "Though in truth it can't have been much more than a few short seconds."
            show kat cowgirl mouth_open eyes_open
            "And what brings me round is the sensation of Kat riding me hard."
            "My eyes pop open to the sight of her bouncing up and down atop me."
            "Her petite breasts are jiggling, her tight little buttocks swaying."
            "And she has a look of sheer determination on her face too."
            "Part of me feels like telling her that cowgirl is just the name of the position."
            "That she doesn't have to actually ride me for real."
            "But I'm not about to put a stop to what she's doing."
            "Not when it feels this good."
            "So instead I resolve to give Kat the ride of her life."
            show kat cowgirl eyes_up mouth_pleasure
            "Tightening my grip on her waist, I start to move in earnest."
            "The effort that Kat's putting into riding me means there's no point starting out slow."
            "So instead I simply leap into it, thrusting up from below in time with her own movements."
            "The second I do so, Kat begins to gasp and moan."
            "But I can see from the look on her face that she's into it."
            "And I hardly need to see her begin nodding her head too."
            show kat cowgirl eyes_close mouth_hurt
            "Now that we're both fully committed, things begin to get seriously intense."
            "Kat's getting hot and sweaty, her skin becoming slick to the touch."
            "This means I have to hold onto her more tightly than ever."
            "But she seems to interpret this as me wanting her to go faster and harder still."
            "Pretty soon I'm battling to keep hold of Kat's slippery, slithering thighs."
            show kat cowgirl eyes_up
            "In fact, she's wriggling about so much that it's almost too much for me."
            "And I can feel that I'm about to lose it!"
            call cum_reaction (kat, 'vaginal', sexperience_min) from _call_cum_reaction_249
            if _return == "vaginal_outside":
                "The sensation of being inside Kat without a condom is truly amazing."
                "But this is the point where I have to pay the price for that thrill."
                "So before I become totally rigid and unable to move, I have to pull out."
                show kat cowgirl out eyes_close mouth_pleasure
                "Lifting Kat upwards, I make sure not to stop until my cock slides free."
                "The move seems to be more than enough to push her over the edge."
                show kat cowgirl eyes_up mouth_open
                "Kat lets out an almost animal moan, tossing back her head and arching her back."
                with vpunch
                "Every muscle in her body seems to be tight and clenched."
                $ kat.love += 1
                show kat cowgirl cum eyes_close with vpunch
                "At the same time I shoot my load, spattering it over her belly and thighs."
            elif _return == "vaginal_condom":
                "Thankfully we chose to use a condom, so losing it is the least of my worries."
                "Because a moment later I feel myself stiffening and holding Kat as still as possible."
                show kat cowgirl eyes_close mouth_open cum with vpunch
                "Then I shoot my load while I'm as deep inside of her as I can get."
                with vpunch
                "Almost as soon as it happens, I can feel her orgasm hit too."
                with vpunch
                "Kat lets out an almost animal moan, tossing back her head and arching her back."
                "Every muscle in our bodies seems to be tight and clenched."
                show kat cowgirl eyes_open mouth_pleasure out
                "Then as one, everything goes limp and Kat slumps down on top of me."
            elif _return == "vaginal_inside_pregnant":
                "I've been protecting Kat's pregnant belly this whole time."
                "So losing it inside of her is the least of my worries."
                "And sure enough, I feel myself stiffening and holding Kat as still as possible."
                $ kat.love += 2
                show kat cowgirl mouth_open tongueout cum with vpunch
                "Then I shoot my load while I'm as deep inside of her as I can get."
                with vpunch
                "Almost as soon as it happens, I can feel her orgasm hit too."
                with vpunch
                "Kat lets out an almost animal moan, tossing back her head and arching her back."
                "Every muscle in our bodies seems to be tight and clenched."
                show kat cowgirl eyes_close mouth_pleasure dickcum_pussy out -cum
                "Then as one, everything goes limp and Kat slumps down on top of me."
            elif _return == "vaginal_inside_pill":
                "I'm still with it enough to remember that Kat's on the pill."
                "So losing it inside of her is the least of my worries."
                "And sure enough, I feel myself stiffening and holding Kat as still as possible."
                $ kat.love += 2
                show kat cowgirl mouth_open tongueout cum with vpunch
                "Then I shoot my load while I'm as deep inside of her as I can get."
                with vpunch
                "Almost as soon as it happens, I can feel her orgasm hit too."
                with vpunch
                "Kat lets out an almost animal moan, tossing back her head and arching her back."
                "Every muscle in our bodies seems to be tight and clenched."
                show kat cowgirl eyes_close mouth_pleasure dickcum_pussy out -cum
                "Then as one, everything goes limp and Kat slumps down on top of me."
            elif _return == "vaginal_inside_happy":
                "The sensation of being inside Kat without a condom is truly amazing."
                "But this is the point where I have to pay the price for that thrill."
                "So before I become totally rigid and unable to move, I have to pull out."
                "But the moment I make my move, Kat begins shaking her head."
                show kat cowgirl mouth_open eyes_open
                kat.say "No..."
                kat.say "Don't do it!"
                kat.say "Don't you dare!"
                "Kat's demands catch me totally off-guard."
                $ kat.love += 5
                $ kat.impregnate()
                show kat cowgirl eyes_up tongueout cum with vpunch
                "Which means that I shoot my load while I'm as deep inside of her as I can get."
                with vpunch
                "Almost as soon as it happens, I can feel her orgasm hit too."
                with vpunch
                "Kat lets out an almost animal moan, tossing back her head and arching her back."
                "Every muscle in our bodies seems to be tight and clenched."
                show kat cowgirl eyes_close mouth_pleasure
                "Then as one, everything goes limp and Kat slumps down on top of me."
                "She seems totally delighted with what just happened."
                "Whereas the awful reality of the situation is already starting to dawn on me."
            elif _return == "vaginal_inside_mad":
                show kat cowgirl eyes_open
                kat.say "No..."
                kat.say "Don't do it!"
                kat.say "Don't you dare!"
                kat.say "Pull out - NOW!"
                "Kat's demands catch me totally off-guard."
                $ kat.love -= 5
                $ kat.impregnate()
                show kat cowgirl eyes_up cum with vpunch
                "Which means that I shoot my load while I'm as deep inside of her as I can get."
                with vpunch
                "Almost as soon as it happens, I can feel her orgasm hit too."
                with vpunch
                "Kat lets out an almost animal moan, tossing back her head and arching her back."
                "Every muscle in our bodies seems to be tight and clenched."
                show kat cowgirl eyes_close
                "Then as one, everything goes limp and Kat slumps down on top of me."
                "But even as she does that, I can hear her beginning to moan as realisation sinks in."
                "And the awful reality of the situation is already starting to dawn on me too."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Kat nods and reaches down to take a firm hold of my cock."
            mike.say "How about right there, Kat?"
            "Kat's still got hold of my cock as we finally get down to it."
            "And now that we are, she doesn't seem inclined to let go of it either."
            "Instead I watch as she presses the head between her buttocks."
            "At the same time I reach up and place my hand gently on her haunches."
            "Then I begin to manoeuvre her into position, guiding her into raising herself upwards."
            "Kat doesn't say a word, but at the same time she seems to be paying close attention."
            "I can see her interpreting what I need her to do next and reacting in kind."
            show kat cowgirl anal mouth_open
            "This means that when I start to pull her downwards, Kat's right there with me."
            "We're moving together, maybe not in perfectly synchronised motions."
            "But it's more than enough to stroke the head of my cock around her hole."
            "For me the sensation is incredible, and I can already see Kat's cheeks flushing."
            "Plus the look she has on her face tells me that she's enjoying it too."
            show kat cowgirl eyes_close mouth_pleasure
            "A moment later I look up to see a change in her expression."
            "It's nothing dramatic, more the fact that her eyes are closing."
            "And at the same time her lips slowly part too."
            "What really catches me off-guard is the way that's mirrored elsewhere too."
            "Watching Kat's face, I almost fail to notice that the muscles of her ass are relaxing!"
            "This means that by the time she's opened her mouth, she's opened down there as well."
            "The first thing I know about it is when Kat suddenly begins to sink downwards."
            "And in the split-second after that, I feel her swallowing me whole."
            "Now it's my turn to close my eyes and be overwhelmed."
            "I'm supposed to be holding onto Kat right now, to be guiding her motions."
            "But all I can do is lie back as she keeps on sinking down."
            "To me it feels like it takes an eternity for me to fill her."
            "Though in truth it can't have been much more than a few short seconds."
            show kat cowgirl mouth_open eyes_open
            "And what brings me round is the sensation of Kat riding me hard."
            "My eyes pop open to the sight of her bouncing up and down atop me."
            "Her petite breasts are jiggling, her tight little buttocks swaying."
            "And she has a look of sheer determination on her face too."
            "Part of me feels like telling her that cowgirl is just the name of the position."
            "That she doesn't have to actually ride me for real."
            "But I'm not about to put a stop to what she's doing."
            "Not when it feels this good."
            "So instead I resolve to give Kat the ride of her life."
            show kat cowgirl eyes_up mouth_pleasure
            "Tightening my grip on her waist, I start to move in earnest."
            "The effort that Kat's putting into riding me means there's no point starting out slow."
            "So instead I simply leap into it, thrusting up from below in time with her own movements."
            "The second I do so, Kat begins to gasp and moan."
            "But I can see from the look on her face that she's into it."
            "And I hardly need to see her begin nodding her head too."
            show kat cowgirl eyes_close mouth_hurt
            "Now that we're both fully committed, things begin to get seriously intense."
            "Kat's getting hot and sweaty, her skin becoming slick to the touch."
            "This means I have to hold onto her more tightly than ever."
            "But she seems to interpret this as me wanting her to go faster and harder still."
            "Pretty soon I'm battling to keep hold of Kat's slippery, slithering thighs."
            show kat cowgirl eyes_up
            "In fact, she's wriggling about so much that it's almost too much for me."
            "And I can feel that I'm about to lose it!"
            call cum_reaction (kat, 'anal', sexperience_min) from _call_cum_reaction_250
            if _return == 'anal_inside':
                "Thankfully we chose to use the back door, so losing it is the least of my worries."
                "Because a moment later I feel myself stiffening and holding Kat as still as possible."
                $ kat.sub += 2
                show kat cowgirl mouth_open tongueout cum with vpunch
                "Then I shoot my load while I'm as deep inside of her as I can get."
                with vpunch
                "Almost as soon as it happens, I can feel her orgasm hit too."
                with vpunch
                "Kat lets out an almost animal moan, tossing back her head and arching her back."
                "Every muscle in our bodies seems to be tight and clenched."
                show kat cowgirl eyes_close mouth_pleasure dickcum_ass out -cum
                "Then as one, everything goes limp and Kat slumps down on top of me."
            elif _return == 'anal_outside':
                "The sensation of being inside Kat's ass is truly amazing."
                "But for some reason I want to pull out of there before the end."
                "Don't ask me to explain it, that's just the way I feel it's going."
                "So before I become totally rigid and unable to move, I have to pull out."
                show kat cowgirl out eyes_close mouth_pleasure
                "Lifting Kat upwards, I make sure not to stop until my cock slides free."
                "The move seems to be more than enough to push her over the edge."
                show kat cowgirl eyes_up mouth_open
                "Kat lets out an almost animal moan, tossing back her head and arching her back."
                with vpunch
                "Every muscle in her body seems to be tight and clenched."
                $ kat.sub += 1
                show kat cowgirl cum eyes_close with vpunch
                "At the same time I shoot my load, spattering it over her belly and thighs."
    return

label kat_fuck_date_arcade:
label kat_fuck_arcade:
    scene bg arcade
    show kat normal casual
    with fade
    mike.say "Wow, Kat..."
    mike.say "Looks like we have this place almost to ourselves."
    mike.say "So, what are we going to play first?"
    show kat annoyed
    kat.say "Hmm..."
    show kat normal
    kat.say "I've kind of burnt myself out on new stuff recently."
    show kat smile
    kat.say "Now I'm in the mood for something a little more old-school."
    "I nod, realising that I'm in the same mood as Kat myself."
    mike.say "They keep all the retro classics over there."
    mike.say "Near the back of the arcade."
    show kat defiant
    kat.say "You think I don't know that?!?"
    kat.say "I come to this place all the time!"
    hide kat with easeoutleft
    "And just like that, Kat's off again."
    "I follow close on her heels until we reach our destination."
    show game arcade kat with fade
    "Then we're pumping in coins, hammering away at joysticks and buttons."
    "We play one classic game after another."
    "Monkey Kong, Snackman and even Adolescent Anthropoid Assassin Alligators."
    "And in all the time we're playing, I don't notice another person around us."
    mike.say "Kat..."
    mike.say "Are we like, the only people in here right now?"
    "Kat doesn't look away from the game she's playing."
    "But I note that she's nodding in agreement."
    kat.say "Oh yeah..."
    kat.say "Or at least nobody else is coming back here."
    kat.say "I bet they're just playing the more modern games at the front of the place."
    mike.say "Huh..."
    mike.say "I always used to dream about this when I was a kid."
    mike.say "You know, having an entire arcade to myself?"
    "Kat's still nodding."
    kat.say "Me too!"
    kat.say "In fact it's one of my biggest fantasies!"
    kat.say "You get me?"
    mike.say "Oh yeah - like it's on your bucket list?"
    hide game arcade with fade
    show kat casual happy at center, zoomAt(1.5, (640, 1040)), startle
    "Kat laughs and grabs hold of my hand."
    hide kat
    show kat a casual defiant blush at center, zoomAt(2.0, (640, 1340)) with vpunch
    "And before I know what's happening, she shoves it into her shorts!"
    kat.say "No, dumbass..."
    kat.say "I mean it really turns me on!"
    "I can feel what Kat means now."
    "And she's not and she's serious as hell."
    "Because I can already feel just how hot and wet her pussy is!"
    "I can't help moving my fingers around down there."
    "Letting them slide over the slick, sensitive folds."
    show kat afraid
    pause 0.2
    show kat happy at startle
    "Kat lets out an appreciative moan, and then a playful giggle."
    show kat defiant
    kat.say "What are you waiting for?"
    kat.say "Pull my shorts down, [hero.name]..."
    kat.say "Then stick it in me!"
    mike.say "Are you sure, Kat?"
    mike.say "You think we'll get away with it?"
    show kat smile
    kat.say "Of course we will."
    kat.say "No one's coming back here, are they?"
    kat.say "And even if they do, just lean in real close."
    kat.say "Then they won't be able to see what we're really doing!"
    "I don't need any more selling on the idea."
    "My cock is already straining against the elastic of my underwear!"
    hide kat
    show kat doggy arcade
    with fade
    "And my heart's starting to beat faster too."
    "I hurry to do as Kat says, pulling her shorts down with one hand."
    "The other I use to hastily unzip my flies."
    show kat doggy arcade mouth_pleasure mike with fade
    "Then with one last look over my shoulder, I get ready to do it."
    menu:
        "Fuck her pussy":
            "Normally I'd be sure to take my time at this point."
            "You know, engage in a little foreplay and teasing."
            "All in order to make sure that Kat's ready for me."
            "But the truth is that I'm pretty paranoid about getting caught."
            "So all of that goes out the window in favour of saving time."
            "Luckily for me, Kat wasn't lying when she said that she was ready for it."
            "As soon as I have my cock out, I shove it roughly between her thighs."
            "And I swear that I can feel the heat coming off of her pussy already!"
            "That's enough to override the fear in my mind."
            "Enough for the base desire I'm feeling to come to the fore."
            "And the next thing I know, it's taking me over."
            "I don't even bother to aim my cock with a hand."
            "Instead I grab hold of Kat by the haunches."
            "And then I pull her backwards and onto me."
            "At the same time I thrust myself forwards."
            "This means that the head of my cock pushes hard against the lips of her pussy."
            show kat doggy eyes_close mouth_pleasure
            "I hear Kat gasp at the sensation, as her body puts up a token resistance."
            "But that only makes me all the more determined to push on."
            "So I redouble my efforts, and I'm rewarded almost instantly."
            "The muscles that were holding Kat's pussy closed begin to weaken."
            "Then little by little, I feel myself starting to sink into her."
            show kat doggy eyes_up
            "I'm still pushing as hard as ever, straining to get all the way inside."
            "And with each second that passes, the balance seems to shift in my favour."
            "Before it was a case of me expending ever more energy and effort."
            show kat doggy eyes_open
            "Which only saw me creeping forward at an agonisingly slow pace."
            "But now the opposite is happening as Kat's body surrenders to me."
            show kat doggy eyes_close speed with hpunch
            "I can feel myself moving ever faster, and getting deeper still."
            "As soon as I manage to get all the way in, I think about pausing."
            "Just talking a few seconds to savour the sensation."
            "But when I remember where we are, I almost leap back into action."
            show kat doggy mouth_open
            "Now I'm thrusting in and out of Kat with feverish intent."
            "I know that I don't want to rush things here."
            "That could ruin the experience for us both."
            "But no matter what I do, I can't seem to make myself slow down!"
            "If it's even something that Kat notices, she doesn't let it show."
            "Though I still feel like I should be doing more."
            show kat doggy eyes_up
            "And that's about the time I see Kat's breast, bobbing up and down."
            "They're pretty petite, so that's about all they can do."
            "But they're still guaranteed to make me even hotter for her."
            "Without thinking, my hands slide up her sides and over her belly."
            "I pull her shirt up at the same time, exposing her bra."
            "Then I pull it down, spilling her breasts into my hands."
            show kat doggy eyes_open
            "Kat's moaning becomes even more intense as I begin to play with them."
            "Each one is big enough to fill the palm of one hand."
            "So I can easily squeeze and massage them to my heart's content."
            "I feel the sensation of Kat's nipples stiffening between my fingers."
            "And I respond by pinching them without mercy."
            kat.say "Mmm..."
            show kat doggy mouth_pleasure
            kat.say "Oh...oh god..."
            show kat doggy eyes_up mouth_open
            kat.say "I'm...I'm going to cum!"
            show kat doggy up
            "Kay underlines the point by pushing her ass into me."
            show kat doggy mouth_hurt eyes_close
            "She grinds it so hard that the inevitable happens."
            "And I feel myself starting to cum too!"
            menu:
                "Cum inside pussy":
                    "One last thrust is all it takes."
                    "Then I feel a surge of release."
                    show kat doggy eyes_up mouth_open tongueout cum -speed with hpunch
                    "And I shoot my entire load into Kat."
                    with hpunch
                    "She gasps at the sensation, slumping against the arcade cabinet."
                    show kat doggy eyes_close mouth_pleasure with hpunch
                    "Without it, I'm sure she would have collapsed into the ground."
                "Pull out of pussy":
                    "One last backwards pull is all it takes."
                    show kat doggy down -speed
                    "And I feel my cock pop out of Kat's pussy."
                    show kat doggy eyes_up mouth_open tongueout with hpunch
                    "She gasps at the sensation, slumping against the arcade cabinet."
                    "Without it, I'm sure she would have collapsed into the ground."
                    "Then I feel a surge of release."
                    show kat doggy eyes_close mouth_pleasure with hpunch
                    pause 0.2
                    with hpunch
                    pause 0.2
                    with hpunch
                    "And I shoot my entire load over Kat's exposed ass."
        "Fuck her ass":
            "Normally I'd be sure to take my time at this point."
            "You know, engage in a little foreplay and teasing."
            "All in order to make sure that Kat's ready for me."
            "But the truth is that I'm pretty paranoid about getting caught."
            "So all of that goes out the window in favour of saving time."
            "Luckily for me, Kat wasn't lying when she said that she was ready for it."
            "As soon as I have my cock out, I shove it roughly between her thighs."
            "And I swear that I can feel the heat coming off of her pussy already!"
            "That's enough to override the fear in my mind."
            "Enough for the base desire I'm feeling to come to the fore."
            "And the next thing I know, it's taking me over."
            "I don't even bother to aim my cock with a hand."
            "Instead I grab hold of Kat by the haunches."
            "And then I pull her backwards and onto me."
            "At the same time I thrust myself forwards."
            "But she gets the surprise of her life a moment later."
            "Because I'm not aiming for her pussy, but rather for her ass!"
            "This means that the head of my cock pushes hard against her hole."
            show kat doggy eyes_close mouth_pleasure
            "I hear Kat gasp at the sensation, as her body puts up a token resistance."
            "But that only makes me all the more determined to push on."
            "So I redouble my efforts, and I'm rewarded almost instantly."
            "The muscles that were holding Kat's ass closed begin to weaken."
            "Then little by little, I feel myself starting to sink into her."
            show kat doggy eyes_up
            "I'm still pushing as hard as ever, straining to get all the way inside."
            "And with each second that passes, the balance seems to shift in my favour."
            "Before it was a case of me expending ever more energy and effort."
            show kat doggy eyes_open
            "Which only saw me creeping forward at an agonisingly slow pace."
            "But now the opposite is happening as Kat's body surrenders to me."
            show kat doggy eyes_close speed with hpunch
            "I can feel myself moving ever faster, and getting deeper still."
            "As soon as I manage to get all the way in, I think about pausing."
            "Just talking a few seconds to savour the sensation."
            "But when I remember where we are, I almost leap back into action."
            show kat doggy mouth_open
            "Now I'm thrusting in and out of Kat with feverish intent."
            "I know that I don't want to rush things here."
            "That could ruin the experience for us both."
            "But no matter what I do, I can't seem to make myself slow down!"
            "If it's even something that Kat notices, she doesn't let it show."
            "Though I still feel like I should be doing more."
            show kat doggy eyes_up
            "And that's about the time I see Kat's breast, bobbing up and down."
            "They're pretty petite, so that's about all they can do."
            "But they're still guaranteed to make me even hotter for her."
            "Without thinking, my hands slide up her sides and over her belly."
            "I pull her shirt up at the same time, exposing her bra."
            "Then I pull it down, spilling her breasts into my hands."
            show kat doggy eyes_open
            "Kat's moaning becomes even more intense as I begin to play with them."
            "Each one is big enough to fill the palm of one hand."
            "So I can easily squeeze and massage them to my heart's content."
            "I feel the sensation of Kat's nipples stiffening between my fingers."
            "And I respond by pinching them without mercy."
            kat.say "Mmm..."
            show kat doggy mouth_pleasure
            kat.say "Oh...oh god..."
            show kat doggy eyes_up mouth_open
            kat.say "I'm...I'm going to cum!"
            show kat doggy up
            "Kay underlines the point by pushing her ass into me."
            show kat doggy mouth_hurt eyes_close
            "She grinds it so hard that the inevitable happens."
            "And I feel myself starting to cum too!"
            menu:
                "Cum inside ass":
                    "One last thrust is all it takes."
                    "Then I feel a surge of release."
                    show kat doggy eyes_up mouth_open tongueout cum -speed with hpunch
                    "And I shoot my entire load into Kat."
                    with hpunch
                    "She gasps at the sensation, slumping against the arcade cabinet."
                    show kat doggy eyes_close mouth_pleasure with hpunch
                    "Without it, I'm sure she would have collapsed into the ground."
                "Pull out of ass":
                    "One last backwards pull is all it takes."
                    show kat doggy down -speed
                    "And I feel my cock pop out of Kat's ass."
                    show kat doggy eyes_up mouth_open tongueout with hpunch
                    "She gasps at the sensation, slumping against the arcade cabinet."
                    "Without it, I'm sure she would have collapsed into the ground."
                    "Then I feel a surge of release."
                    show kat doggy eyes_close mouth_pleasure with hpunch
                    pause 0.2
                    with hpunch
                    pause 0.2
                    with hpunch
                    "And I shoot my entire load over Kat's exposed buttocks."
    "Without saying a word, Kat pulls up her shorts."
    "Then she pulls down her shirt and gets back to her game."
    hide kat
    show kat casual shy blush
    with fade
    "Neither of us says a word about what we just did."
    "Not until we get out of the arcade a short while later."
    "We just keep quiet, each of us enjoying the afterglow."
    "And keeping it a secret between the two of us."
    $ kat.sexperience += 1
    return

label kat_fuck_date_mall1:
    scene bg mall1
    show kat casual smile
    with fade
    if not kat.flags.photobooth_blowjob:
        $ kat.flags.photobooth_blowjob = True
        "Kat and I had a date in the diary for today, and I think we were supposed to agree on somewhere to go."
        "But it looks like somewhere along the line, we both kind of forgot about the last part."
        "And so actually deciding where we were going to go and what we were going to do there never happened."
        "But we're still determined to have the date that we didn't plan for, and to have a good time too."
        "The solution comes in the form of that great temple of modern culture - the local mall!"
        "Soon enough we're wandering around the place, window-shopping and talking about totally random stuff."
        "And that's totally fine with me."
        "All I really wanted was to spend some time with Kat."
        "Just chatting and chilling out, with no pressure whatsoever."
        show kat smile at center, zoomAt (1.5, (640, 1040))
        "And much to my relief, that seems to be how Kat's feeling too."
        show kat surprised
        kat.say "Ooh..."
        show kat at center, zoomAt (1.5, (540, 1040)) with ease
        kat.say "What's that thing over there?"
        "I turn my head in the direction that Kat's pointing."
        "And I frown as I stare at the object that's aroused her interest."
        mike.say "That thing right there?"
        mike.say "That's one of those old-fashioned photo booths."
        show kat confused at center, zoomAt (1.5, (640, 1040)) with ease
        "Kat turns round and frowns at me, a puzzled look on her face."
        show fx question
        kat.say "Huh?"
        kat.say "Why would you need to go in there to take a photo?"
        kat.say "Wouldn't it be easier just to use your phone?"
        hide fx
        "I shake my head, trying to explain the thing to Kat."
        mike.say "It's from way back in the past, Kat."
        mike.say "Back when there weren't even mobile phones that didn't take pictures."
        show kat surprised
        "Kat nods slowly, a look of amazement now spreading across her face."
        "And I can guess that she's trying in vain to imagine a time without mobile phones."
        show kat normal
        kat.say "So, like..."
        kat.say "If you wanted to take a selfie..."
        kat.say "You had to go sit in one of those?"
        mike.say "Uh-huh..."
        mike.say "And then you had to wait for the photos to come out of that slot."
        mike.say "That one right there."
        "Kat leans in a little closer to look at the offending slot."
        kat.say "So..."
        kat.say "It prints the photos and they come out..."
        kat.say "What...like a couple of seconds later?"
        mike.say "Oh no, Kat..."
        mike.say "It takes almost ten minutes!"
        mike.say "It actually takes the photos with a physical camera."
        mike.say "Then it develops them from the negatives."
        show kat shocked
        "By now Kat's staring at me like I'm speaking a foreign language."
        kat.say "It does what with the what-now?"
        "I think about trying to explain old-fashioned methods of developing photos."
        "But I'm not sure that I really understand how it works myself."
        "So what chance do I have of explaining it to Kat?"
        show kat normal
        mike.say "Never mind..."
        mike.say "It's just something people do for fun now."
        mike.say "For the novelty of having real photos, yeah?"
        hide kat smile with easeoutleft
        scene bg black
        show kat blowjob casual photobooth no_people curtain at zoomAt (1.35, (-185, 0))
        with fade
        show kat as katsprite at center, zoomAt (2.0, (940, 740)) with easeinright
        "Kat nods and takes hold of my hand."
        show kat blowjob casual photobooth no_people -curtain at zoomAt (1.35, (-185, 0))
        "Then she pulls me towards the booth."
        kat.say "Then we should totally do it too!"
        show kat as katsprite at center, zoomAt (2.0, (840, 740)) with ease
        "I shrug and let her pull me inside."
        "Because after all, I did just say it was fun."
        "So I don't mind dropping a couple of bucks to make it happen."
        show kat as katsprite at center, zoomAt (2.0, (740, 740)) with ease
        pause 0.5
        hide katsprite
        show kat blowjob casual photobooth curtain at zoomAt (1.35, (-185, 0))
        "Kat steps inside the booth and pulls back the curtain and ."
        "I follow her lead, turning to pull it closed behind us."
        "But when I turn around, I get a surprise."
        scene bg black
        show kat blowjob casual photobooth no_people at zoomAt (1.45, (-250, 0))
        show kat kiss as katkiss
        with fade
        $ kat.flags.kiss += 1
        "Because Kat pulls me down onto the seat and presses her lips against mine."
        "The kiss is as intense as it was unexpected."
        "But that doesn't stop me enjoying it."
        "Afterwards I point to the coin slot."
        hide katkiss
        show kat smile close as katsprite
        with fade
        mike.say "Okay, Kat..."
        mike.say "Are you ready for the photos now?"
        show kat defiant close as katsprite
        "Kat lets out a mischievous giggle as she shakes her head."
        kat.say "You didn't actually believe all that BS, did you?"
        kat.say "That I had no idea what one of these thing is for?"
        mike.say "Erm..."
        mike.say "Yeah, Kat - I kinda did!"
        kat.say "Well it was BS!"
        kat.say "Just an excuse to get you in here."
        mike.say "But why, Kat?"
        mike.say "What's wrong with kissing me in public all of a sudden?"
        show kat defiant close as katsprite at center, zoomAt (1, (640, 1600)) with ease
        "Kat giggles again as she starts to slide onto the floor of the booth."
        kat.say "That was just for starters."
        kat.say "This is what I really had in mind..."
    else:
        "As Kat and I walk through the mall together, something catches my eye."
        "It's the old photo booth that Kat dragged me into one time."
        "I can't help but remember it on account of the legendary blow-job she gave me in there!"
        "So, while trying to sound as nonchalant as possible, I point it out."
        mike.say "Erm..."
        mike.say "Hey, Kat..."
        show fx question
        kat.say "What is it?"
        mike.say "You remember that photo booth over there?"
        hide fx
        "Kat looks in the direction that I'm pointing."
        "And then she looks back at me with a raised eyebrow."
        show kat smile
        kat.say "How could I forget?"
        show kat surprised
        kat.say "Wait a minute..."
        kat.say "Do you want to go again?"
        "I wanted to answer in the affirmative, but in a smooth manner."
        "Instead I can't help nodding my head and grinning like a fool."
        show kat defiant
        "But none of that seems to discourage Kat."
        "As she nods too, then grabs hold of my hand."
        hide kat with easeoutleft
        scene bg mall1 at blur(16), dark with dissolve
        "Together we hurry over to the booth and slip inside."
        show kat blowjob casual photobooth handjob curtain with fade
        "And once I close the curtain I turn around to find Kat already on her knees."
        "I guess she's keen on getting straight down to business!"
    scene bg black
    show kat blowjob casual photobooth handjob curtain
    with fade
    "I watch as Kat reaches out and begins to unzip my flies."
    "And for a moment I think about objecting to what she's doing."
    "But then I stop myself, wondering why I'd even think of it?"
    "What am I - some kind of prude?"
    "So I just stand still and let her get on with it."
    "And as she reaches inside my pants, I can feel the excitement building in me."
    scene bg black
    show kat blowjob casual photobooth handjob
    with fade
    "The kiss we just shared was pretty hot, but not enough to get me totally hard."
    "Though the sensation of Kat pulling my cock out of my pants is a whole different story."
    "Almost before she's managed it, I can feel myself getting bigger."
    "And once she has it out, there's hardly anything left for her to do in that department."
    "But that doesn't stop Kat stroking and squeezing it."
    show kat blowjob forth
    pause 0.35
    show kat blowjob back
    pause 0.35
    show kat blowjob forth
    pause 0.35
    show kat blowjob back
    pause 0.35
    show kat blowjob forth
    pause 0.35
    show kat blowjob back
    "Her fingers move up and down the shaft, making sure it's as hard as can be."
    "And only when that's done does she start to pay attention to other things."
    "Kat give me one last look before she leans in close."
    show kat blowjob eyes_closed
    "She closes her eyes as she does so, concentrating on the task ahead."
    "And it's only now that I realise I've been holding my breath."
    "I keep on doing so while I watch Kat's lips part."
    show kat blowjob mouth_lick
    pause 0.15
    show kat blowjob tongue2
    pause 0.15
    show kat blowjob tongue3
    pause 0.15
    show kat blowjob tongue1
    "Only when the tip of her tongue emerges and touches the head of my cock..."
    "Only then do I finally feel that I can start to breath again."
    show kat blowjob -handjob
    "But it's not as simple as that, or as subtle."
    "Because I let the air out of my lungs in a loud gasp."
    show kat blowjob blow curtain shadows with dissolve
    "A huge sigh of relief as Kat actually starts using her mouth on me."
    "Thankfully the sound seems to do nothing to deter her."
    "Though as soon as she takes more of it into her mouth, I gasp again."
    "Because I have no idea what she's doing inside of there!"
    "Seriously, I've had a few blow-jobs in my time."
    "Some of them good and some of them bad."
    "And if I'm honest, most of them forgettable."
    "But this is something unexpected and totally different."
    "The way that Kat's moving her tongue around my cock is baffling."
    show kat blowjob -curtain with dissolve
    "I had no idea you could do that kind of thing with one."
    "And the sensation of it is almost impossible to describe."
    "It's not just the tongue either."
    "I can feel her teeth nibbling here and there."
    "Her lips sucking and pouting too."
    "It has to have something to do with how Kat's moving her head as well."
    show kat blowjob eyes_open
    "She doesn't just move it back and forth, but from side to side too."
    "It's constantly changing angles, rolling around on her shoulders."
    "I find myself bracing my arms against the sides of the booth."
    "Doing all that I can to keep myself upright and standing."
    "And that's because Kat's beginning to make me go weak at the knees!"
    "All of this means that, for a moment at least, I don't notice what Kat's actually doing."
    "Which is kind of ironic, because that's the very thing that snaps me out of it."
    show kat blowjob eyes_closed
    "In the time I was distracted, Kat seems to have decided things needed kicking up a gear."
    "And so she's taken me even deeper into her mouth than before."
    "I come round to the sensation of my cock going down her throat."
    "It feels more intense than anything that came before."
    "And yet Kat still manages to handle it like the whole thing is a breeze."
    "She doesn't miss a beat, doesn't gag for a second."
    "It's smoother than I could have ever imagined."
    "But it's not something that she's going to be able to keep up for too long."
    "Because I can already feel myself starting to lose it."
    "I have no idea if Kat's aware of what's happening to me."
    "So I assume that I have to make the decision as to what happens next."
    menu:
        "Cum in her mouth":
            "I don't know what would happen if I were to pull out now."
            show sexinserts head kat zorder 1
            "My cock is so deep in Kat's mouth I'm scared that she might choke!"
            "So I stay right where I am, hoping that she realises what's about to happen."
            show kat blowjob eyes_open
            "Luckily for me, her eyes pop open a few moments before it does."
            show sexinserts head kat cum zorder 1
            show kat blowjob eyes_closed cum
            with hpunch
            $ kat.sub += 2
            "And she visibly braces herself as I shoot my load."
            with hpunch
            "Kat takes it all in one go, swallowing everything with practised ease."
            hide sexinserts
        "Cum on her face" if kat.sub >= 50:
            "I don't know what would happen if I just stayed where I am."
            "My worry is Kat not realising what's going to happen before it does."
            "That could lead to her choking!"
            show kat blowjob eyes_surprised out mouth_normal
            "So I lurch backwards, pulling my cock out of her mouth."
            "Kat coughs and gasps in surprise, but only for a couple of seconds."
            show kat blowjob eyes_closed mouth_open facecum with hpunch
            $ kat.love += 2
            "Because it doesn't take long for me to shoot my load into her face."
            with hpunch
            "Painting it with stripes of sticky, white cum."
    show kat blowjob out cum eyes_open mouth_lick breath
    "Afterwards, Kat cleans herself up as quickly as she can."
    "And I shove my cock back into my pants just as hastily."
    scene bg mall1
    show kat smile casual
    with fade
    "Then we slip out of the photo booth as if nothing happened."
    "Pretty soon we're back to just strolling around the mall."
    "Safe in the knowledge that we're the only people here who know what just went down."
    "Or to be more precise, who went down on whom."
    $ game.active_date.score += 40
    return

label kat_fuck_date_restaurant:
    scene bg restaurant with fade
    "Getting a table at the restaurant was pretty much a last-minute deal."
    "So about an hour ago, neither Kat nor I knew we were going to be coming here."
    "But it's a great place with food that always leaves you wanting more."
    "So as soon as I knew we could get in, I called her up and we hurried down here."
    "Part of me is still thinking that we're going to find out it was a mistake."
    "That when I give the guy on the door my name, he won't find it in the reservation book."
    "But to my surprise, he looks down and nods."
    "Waiter" "Ah yes..."
    "Waiter" "I have you right here."
    "Waiter" "Follow me please."
    "I can't help letting out a sigh of relief as we're shown to our table."
    "Something that seems to cause Kat a great deal of amusement."
    show restaurant meal kat date nomeals
    show restaurant_meal_waiter_pose01 as waiter zorder 1
    with fade
    "As the waiter seats us and takes our drinks order, she's smiling at me the whole time."
    hide restaurant_meal_waiter_pose01 as waiter with easeoutleft
    "And once he's gone, she leans over the table towards me."
    kat.say "What was all that about, [hero.name]?"
    kat.say "You looked like you were sweating bullets back there!"
    mike.say "I was just nervous, that's all!"
    mike.say "This is a pretty nice place, Kat."
    mike.say "I didn't want him to say they'd lost the booking."
    mike.say "They sometimes do stuff like that, you know?"
    mike.say "If they don't like the look of you, that is."
    "Kat chuckles and shakes her head."
    kat.say "You really need to lighten up a little."
    kat.say "So what if some stuffy waiter sniffs at you?"
    kat.say "That doesn't mean you're a bad person."
    mike.say "You're right, Kat - of course you are."
    mike.say "But I just find it hard not to worry what people think of me."
    mike.say "I don't really know how it's so easy for you."
    "Kat raises her eyebrows at this."
    show restaurant meal kat date happy nomeals
    kat.say "You want to know my secret?"
    kat.say "What I do to not give a fuck?"
    mike.say "Are you kidding?!?"
    mike.say "Of course I do!"
    show restaurant meal kat date nomeals normal
    "Kat nods and takes a quick glance around, as if to check nobody's listening in on us."
    "Then she leans in even closer, gesturing for me to do the same."
    "I do as she says, eager to hear what she has to say to me."
    "But as I do so, Kat sweeps her hand across the top of the table."
    "And in doing so, she sends her napkin tumbling into the floor."
    show restaurant meal kat date bored nomeals
    kat.say "Oh shit!"
    kat.say "I'm so clumsy..."
    show restaurant meal kat date happy nomeals
    kat.say "Would you get that for me?"
    "I look at Kat for a second, trying to scrutinise her expression."
    "Because I could have sworn she actually did that on purpose."
    "But nevertheless, I nod and get out of my seat."
    "Though as I get down on my knees, Kat's foot appears from under the table."
    "And then it pushes the napkin under there as it disappears again!"
    "Part of me wants to look up and ask Kat just what's going on here."
    "But instead I push the thought aside and crawl under the table."
    hide restaurant meal
    show kat cunnilingus restaurant date mouth_close
    with fade
    "Which is when I find myself face-to-face with something unexpected."
    "Kat's sitting with her legs spread apart, which shouldn't be noteworthy."
    "But what makes it so is the fact that she's also exposing herself!"
    "Well...I don't know if it really counts as exposing herself totally."
    "Because you'd have to be under the table like me in order to actually see it."
    "But that's a technicality at best."
    "What's important is that I'm literally staring at her pussy right now!"
    "For a moment I don't know what to do."
    "The most obvious thing seems to be to get up."
    "And then to ask Kat in a polite manner what in the hell she's playing at."


    "Is this what Kat meant when she talked about not giving a fuck?"
    "The only thing I can think is that she wants me to..."
    "Well, to get to work on her down there!"
    "Because that certainly would require me not to give a fuck!"
    "Wait a minute...what am I even thinking here?"
    "Do I want to be the guy that runs away from a chance like this?"
    "Or do I want to be the guy that grabs it with both hands and won't let go?"
    "I know the answer to that question."
    "And it's the reason I begin to crawl closer to Kat."
    show kat cunnilingus mike eyes_close
    "Pretty soon I have my head between her thighs."
    "And I'm almost pressing my face into her groin."
    "I don't know how much time I have to do this thing."
    "And I'm guessing that Kat's going to cover for me up there while I do it."
    "So I make an effort to put everything else out of my mind."
    "Then I close my eyes and open my mouth."
    "Normally I'd be careful about taking my time, making sure Kat's in the right mood."
    "But right now, time is going to be of the essence, so I get straight down to business."
    "Luckily for me, I can already catch the unmistakable scent of Kat's pussy."
    "It's musky and sweet."
    "Which lets me know that she's already excited at the prospect of what lies ahead."
    "And when I extend the tip of my tongue, I get the bittersweet taste of it too."
    show kat cunnilingus tongue2 eyes_open
    pause 0.15
    show kat cunnilingus tongue3
    pause 0.15
    show kat cunnilingus tongue1
    "That's more than enough to spur me on, to make me want this as much as Kat seems to."
    "Instantly my reserve vanishes and I stop holding back."
    "I don't bother lingering around the edges of Kat's pussy either."
    "Instead I dip my tongue straight in there."
    show kat cunnilingus tongue2 mouth_open
    pause 0.15
    show kat cunnilingus tongue3
    pause 0.15
    show kat cunnilingus tongue1
    pause 0.15
    show kat cunnilingus tongue2
    pause 0.15
    show kat cunnilingus tongue3
    pause 0.15
    show kat cunnilingus tongue1
    "I push it in with all the strength I can muster."
    "And my reward is to feel Kat's entire body quiver at my efforts."
    "Her pussy is still resisting, as I'd expect it to."
    "But with each pass that my tongue makes, I feel it loosen a little."
    "And as it does, my tongue pushes in further still."
    show kat cunnilingus tongue2 eyes_close
    pause 0.15
    show kat cunnilingus tongue3
    pause 0.15
    show kat cunnilingus tongue1
    pause 0.15
    show kat cunnilingus tongue2
    pause 0.15
    show kat cunnilingus tongue3
    pause 0.15
    show kat cunnilingus tongue1
    "Soon enough the roles are reversed between us."
    "Before it was me trying to push inside and Kat's pussy keeping me out."
    show kat cunnilingus hold mouth_close eyes_open
    "Now it feels like she's trying to pull me inside."
    "And I'm the one fighting to keep from being in head first!"
    "Kat's squirming in her chair, muscles twitching as I work on her."
    "I can only imagine what it must look like from above the table."
    "The thought makes me feel oddly conflicted."
    "On the one hand I fear us being caught in the act."
    "But on the other I'm seriously excited at the danger we've put ourselves in."
    "And that's what keeps me going, pushing my tongue ever deeper into her."
    show kat cunnilingus tongue2 eyes_up
    pause 0.115
    show kat cunnilingus tongue3
    pause 0.115
    show kat cunnilingus tongue1
    pause 0.115
    show kat cunnilingus tongue2
    pause 0.115
    show kat cunnilingus tongue3
    pause 0.115
    show kat cunnilingus tongue1
    pause 0.115
    show kat cunnilingus tongue2
    pause 0.115
    show kat cunnilingus tongue3
    pause 0.115
    show kat cunnilingus tongue1
    pause 0.115
    show kat cunnilingus tongue2
    pause 0.115
    show kat cunnilingus tongue3
    pause 0.115
    show kat cunnilingus tongue1
    "Normally I'd be listening out for any sign that Kat was reaching the end."
    "Looking up to read the expression on her face to see if she was about to cum."
    "But down here all I can do is keep on going at it."
    "I just have to hope that when the time comes, spot the more subtle cues."
    "Then, as if I'm being punished for being so lax, it happens."
    show kat cunnilingus tongue2 eyes_close
    pause 0.115
    show kat cunnilingus tongue3
    pause 0.115
    show kat cunnilingus tongue1
    pause 0.115
    show kat cunnilingus tongue2
    pause 0.115
    show kat cunnilingus tongue3
    pause 0.115
    show kat cunnilingus tongue1
    pause 0.115
    show kat cunnilingus tongue2
    pause 0.115
    show kat cunnilingus tongue3
    pause 0.115
    show kat cunnilingus tongue1
    pause 0.115
    show kat cunnilingus tongue2
    pause 0.115
    show kat cunnilingus tongue3
    pause 0.115
    show kat cunnilingus tongue1 mouth_hurt
    pause 0.075
    show kat cunnilingus tongue2
    pause 0.075
    show kat cunnilingus tongue3
    pause 0.075
    show kat cunnilingus tongue1
    pause 0.075
    show kat cunnilingus tongue2
    pause 0.075
    show kat cunnilingus tongue3
    pause 0.075
    show kat cunnilingus tongue1 mouth_open eyes_up
    $ kat.love += 2
    $ kat.sub += 1
    "Kat seems to try curling herself into a ball."
    "She must be about to hit her climax, it's the only explanation."
    "The only problem is that my head's right in her lap."
    "This means that it's pulled up as her thighs rise."
    "And then the back of my head hits the underside of the table." with vpunch
    "Luckily for me, the cry of pain I let out is muffled."
    "Because my face is still buried in Kat's pussy!"
    "In the confusion that follows, I crawl backwards."
    show kat cunnilingus normal eyes_close -mike
    "And as sneakily as possible, I climb back into my seat."
    hide kat
    show restaurant meal kat blush date nomeals
    with fade
    "When I finally collect myself and look across the table, I have to cover my mouth again."
    "Because Kat's sitting there, slumped in her chair and looking like she's exhausted."
    "Her eyes are glazed over and her cheeks are bright red."
    "Plus she looks like she's lost the power of speech!"
    show restaurant_meal_waiter_pose01 as waiter zorder 1 at top_mostleft with easeinleft
    "Waiter" "Excuse me..."
    "Waiter" "Are you ready to order?"
    "I see the waiter staring at Kat in confusion."
    "So I make a point of grabbing the menus."
    show restaurant meal kat blush date nomeals order
    mike.say "Don't worry about my companion."
    mike.say "She's just chilling out over there, you know?"
    mike.say "Kind of like meditating..."
    mike.say "So I'll be ordering for the both of us."
    show restaurant meal kat blush date nomeals -order
    "The waiter looks like he's about to say something."
    "Then he just nods and smiles, obviously concluding it's not worth his time."
    "So I end up ordering for Kat too."
    hide restaurant_meal_waiter_pose01 as waiter zorder 1 with easeoutleft
    "And then sitting there in silence, waiting for her to recover."
    "Something that takes quite some time too."
    $ game.active_date.score += 40
    return

label kat_fuck_date_nudistbeach:
label kat_fuck_date_beach:
label kat_fuck_beach:
    scene bg beach
    show kat swimsuit
    if game.active_date and game.active_date.on_date(kat):
        show kat annoyed
        "It's not usually hard to pitch a day at the beach to most girls."
        "They normally love the idea of sea, sand and sunshine."
        "But the girl I've been trying to sell on the idea this time is Kat."
        "And she's definitely not the average girl, not by any measure."
        "Which means that I had to practically beg her to come to the beach with me."
        "And even when she finally agreed, it's not like she cheered up about it."
        "Because there's no requirement for her to pretend like she wants to be here!"
        "So the experience is kind of like being at the beach with a sulky teenager."
    show kat normal
    kat.say "Have you got any more of that sun-screen?"
    if hero.activity.flags.date_suntan:
        kat.say "I think you missed a spot here!"
    else:
        kat.say "I think I missed a spot here!"
    "I shake my head as I reach into my bag and grab the sun-screen."
    "Then I hand it over to Kat, biting my tongue as I respond."
    mike.say "Are you sure, Kat?"
    if hero.activity.flags.date_suntan:
        mike.say "I feel like I got everything covered already."
        mike.say "I did kind of put on three lots of the stuff!"
    else:
        mike.say "I feel like you got everything covered already."
        mike.say "You did kind of put on three lots of the stuff!"
    "Kat shakes her head, effectively dismissing my comments."
    "And she begins to rub yet more sun-screen into her skin as she replies."
    kat.say "That's easy for you to say, [hero.name]!"
    kat.say "You have naturally high levels of melanin."
    kat.say "So you don't burn so easy."
    show kat sadsmile
    kat.say "Whereas I have almost none."
    kat.say "I only have to step outside for a minute and I start to cook!"
    "I'm still a little peeved at Kat as she says all of this."
    "But as I think about it, one or two things do start to click."
    mike.say "Huh..."
    mike.say "So I bet your parents kept you out of the sun?"
    show kat annoyed
    kat.say "Oh yeah, you bet!"
    kat.say "They were really strict about it too."
    "I nod, feeling my suspicions are being confirmed."
    mike.say "So you must have spent a lot of time inside as a kid, right?"
    mike.say "Never really getting into stuff like sports and the like?"
    show kat normal
    "Now Kat's the one nodding."
    kat.say "Well how could I?"
    kat.say "Can't do that stuff inside."
    mike.say "So you naturally started gravitating towards video-games."
    mike.say "That you can play inside and alone."
    show kat confused
    "Kat looks up at me as I say this, a quizzical look on her face."
    kat.say "I guess so..."
    kat.say "But what are you trying to say?"
    mike.say "It's pretty obvious, Kat..."
    mike.say "You only ended up getting into video-games because you're so pale!"
    show kat angry
    "Kat frowns and looks like she's about to argue with me."
    "But then she seems to actually think about it for a moment."
    show kat normal
    kat.say "Hmm..."
    kat.say "I never thought of it that way around!"
    mike.say "Yeah..."
    if game.active_date and game.active_date.on_date(kat):
        mike.say "And maybe if I'd known how easily you burn..."
        mike.say "I might have thought twice before making you come to the beach with me!"
    "I glance around, looking for something that might help the situation."
    "And then my eyes fall on a more secluded part of the beach."
    "One where the rocks are casting shade on the sand."
    mike.say "Come on, Kat..."
    mike.say "Let's move over there."
    mike.say "The sun's moved since we got here."
    mike.say "And now that part of the beach is in the shade."
    "Kat looks in the direction I'm pointing."
    "And it doesn't take long for her to start nodding her head."
    kat.say "That looks good..."
    show kat smile
    kat.say "Come on, [hero.name], let's go!"
    hide kat with easeoutleft
    "Not wanting to pass up the chance to improve Kat's mood, I spring into action."
    scene beach_cream_bg_01 as bg
    show kat smile swimsuit at dark, center, zoomAt(1.5, (640, 1040))
    with fade
    "Within mere seconds I've managed to gather up all of our stuff."
    "And then we hot-foot it over to the more shady spot."
    "As soon as we're settled down again, Kat's whole mood seems to change for the better."
    "She lets out a long sigh of relief and shakes her head."
    kat.say "Phew!"
    kat.say "That's better..."
    show kat shy
    kat.say "Sorry for being a grouch."
    kat.say "You just get that way when you've been dodging the sun all your life!"
    "I wave away the apology with a casual gesture of my hand."
    mike.say "No worries, Kat..."
    mike.say "I'm just glad you're okay."
    show kat smile blush
    "It's about now that I notice the way Kat's looking at me."
    "Kind of like a hungry dog staring into the window of a butcher's shop."
    kat.say "Oh, I'm feeling better than okay!"
    kat.say "So..."
    kat.say "I'm guessing nobody can see us here, right?"
    "I look around and then nod."
    mike.say "Sure looks that way..."
    "But I don't get to finish what I'm saying."
    show kat at center, zoomAt(2.0, (640, 1340)) with hpunch
    "As when I turn my head back towards Kat, she literally pounces on me!"
    with vpunch
    "Taken by surprise, I end up rolling in the sand with her."
    "And by mere chance I come up on top."
    show kat shy
    kat.say "Urgh..."
    kat.say "It's all the heat I absorbed already..."
    show kat defiant
    kat.say "It's making me super horny!"
    mike.say "I..."
    mike.say "I'm not sure that's how it works!"
    "But even as I'm saying this, I can feel Kat pulling down my trunks."
    "And the whole situation is making me harder by the second!"
    "So am I really going to argue the point with her?"
    "Instead of saying more, I return the favour."
    show kat naked with dissolve
    "I begin pulling at Kat's swimming costume."
    "And she helps me by wriggling out of it too."
    "Pretty soon we're both naked, and Kat has hold of my cock."
    hide kat
    show kat missionary beach mouth_pleasure mike
    with fade
    kat.say "Hurry up, [hero.name]!"
    kat.say "I need this thing inside of me!"
    "I nod eagerly, wanting more than anything to do as Kat says."
    "But first I have to decide just where I'm going to put it!"
    menu:
        "Fuck her pussy":
            "I kinda feel like this is one of those spur-of-the-moment situations."
            "So taking my time isn't really an option or in the spirit of things."
            "Likewise trying to get fancy doesn't feel right either."
            "So I decide to keep things simple and just head straight for the pussy!"
            "I'm already pretty much lined up for that, so all I need do is lean forwards."
            "Kat spreads herself out beneath me as I do so, making things that much easier."
            show kat missionary vaginal eyes_pleasure
            "And she welcomes me with literal open arms as I aim my cock between her thighs."
            "From this angle, I'm the one doing most of the work."
            "But that's not an issue for me, as it means I'm in almost total control as well."
            "I use this to slowly and deliberately tease Kat with the tip of my cock."
            "I trace the outer edge of her lips, making a full circuit of them."
            "And only when that's complete do I even begin to move inwards."
            show kat missionary mouth_normal
            "All the time I can hear gat gasping and even panting at my efforts."
            "Which kind of amazes me, as I'm not even inside of her yet!"
            "But all of that's about to change, because now I'm making serious inroads."
            "Every pass my cock makes, it gets closer to the middle."
            "And I swear that every time I feel Kat's resistance ebb away a little more."
            "I feel like I'm in total control, like I can almost pick my moment."
            "Which means it comes as a total surprise a few seconds later when it happens."
            "Suddenly all trace of resistance is gone, and there's nothing to hold me back."
            "That means all the force I was putting into teasing Kat has to go somewhere else."
            "And in this case, that's plunging me straight into her!"
            show kat missionary full mouth_pleasure eyes_ahegao
            "All of my weight is behind me as this happens."
            "So I keep right on going until I can't go any further."
            show kat missionary eyes_pleasure
            "Now I find myself as deep into Kat as it's possible to get."
            "I'm totally unprepared, and I find myself gasping and panting just like Kat."
            "But it doesn't take long for the animal part of my brain to take over."
            "And that gives me a mental kick up the arse."
            "It seems to demand to know why I'm balls deep in a girl and not doing anything."
            show kat missionary mouth_normal
            "And sure enough, I begin to move without really thinking about it."
            "I start off slowly, going back and forth with a careful rhythm."
            show kat missionary speed with vpunch
            "But it doesn't take long for me to begin to pick up speed."
            "Every thrust is a little faster than the last."
            "And it seems to affect Kat a little more too."
            "Soon enough I'm moving as fast as I possibly can."
            "Going in and out of her without pause or hesitation."
            show kat missionary mouth_hurt
            "Kat leans back as far as she can go, improving the angle of my thrusts."
            "And when she can't go any further, she raises her legs into the air too."
            "This means I can pound away even harder, and so I take full advantage."
            kat.say "Oh fuck..."
            show kat missionary eyes_ahegao
            kat.say "Can't take...any more..."
            "As soon as the words are out of Kat's mouth, I know she's not kidding."
            "I can feel her muscles beginning to squeeze my cock."
            "And I know that means she's going to cum any moment."
            "The pressure has a similar effect on me too."
            "And I guess I have seconds at best to decide how I want to finish this thing!"
            menu:
                "Cum inside":
                    "By now I'm almost bending Kat in half."
                    "So the only solution is to keep right on going."
                    "With one final thrust, I make sure I'm as deep as I can go."
                    show kat missionary mouth_normal tongueout cum with hpunch
                    $ kat.love += 2
                    "Then I shoot my load into her without holding back."
                    with hpunch
                    "Pinned down under my weight, Kat writhes and wriggles."
                    with hpunch
                    "Taking everything that I have to give until the very end."
                    show kat missionary out vaginaldrip -cum
                "Pull out":
                    "I have Kat pinned down under my weight."
                    "So it's no challenge for me to pull out."
                    show kat missionary out eyes_pleasure mouth_normal tongueout
                    "She moans as it happens, her orgasm increasing in intensity."
                    show kat missionary cum with vpunch
                    "And then I let go, shooting my load over her stomach."
                    with vpunch
                    "Unable to escape, Kat writhes and wriggles."
                    show kat missionary mouth_pleasure bodycum -cum -tongueout with vpunch
                    $ kat.sub += 1
                    "Being showered by all I have to give until the very end."
        "Fuck her ass":
            "I kinda feel like this is one of those spur-of-the-moment situations."
            "So taking my time isn't really an option or in the spirit of things."
            "But I do feel like there's a need for me to mix it up a little."
            "So I make a point of heading straight for the ass!"
            "I'm already pretty much lined up for that, so all I need do is lean forwards."
            "Kat spreads herself out beneath me as I do so, making things that much easier."
            show kat missionary anal eyes_pleasure
            "And she welcomes me with literal open arms as I aim my cock between her buttocks."
            "From this angle, I'm the one doing most of the work."
            "But that's not an issue for me, as it means I'm in almost total control as well."
            "I use this to slowly and deliberately tease Kat with the tip of my cock."
            "I trace the outer edge of her ass, making a full circuit of it."
            "And only when that's complete do I even begin to move inwards."
            show kat missionary mouth_normal
            "All the time I can hear gat gasping and even panting at my efforts."
            "Which kind of amazes me, as I'm not even inside of her yet!"
            "But all of that's about to change, because now I'm making serious inroads."
            "Every pass my cock makes, it gets closer to the middle."
            "And I swear that every time I feel Kat's resistance ebb away a little more."
            "I feel like I'm in total control, like I can almost pick my moment."
            "Which means it comes as a total surprise a few seconds later when it happens."
            "Suddenly all trace of resistance is gone, and there's nothing to hold me back."
            "That means all the force I was putting into teasing Kat has to go somewhere else."
            "And in this case, that's plunging me straight into her!"
            show kat missionary full mouth_pleasure eyes_ahegao
            "All of my weight is behind me as this happens."
            "So I keep right on going until I can't go any further."
            show kat missionary eyes_pleasure
            "Now I find myself as deep into Kat as it's possible to get."
            "I'm totally unprepared, and I find myself gasping and panting just like Kat."
            "But it doesn't take long for the animal part of my brain to take over."
            "And that gives me a mental kick up the arse."
            "It seems to demand to know why I'm balls deep in a girl and not doing anything."
            show kat missionary mouth_normal
            "And sure enough, I begin to move without really thinking about it."
            "I start off slowly, going back and forth with a careful rhythm."
            show kat missionary speed
            "But it doesn't take long for me to begin to pick up speed."
            "Every thrust is a little faster than the last."
            "And it seems to affect Kat a little more too."
            "Soon enough I'm moving as fast as I possibly can."
            "Going in and out of her without pause or hesitation."
            show kat missionary mouth_hurt
            "Kat leans back as far as she can go, improving the angle of my thrusts."
            "And when she can't go any further, she raises her legs into the air too."
            "This means I can pound away even harder, and so I take full advantage."
            kat.say "Oh fuck..."
            show kat missionary eyes_ahegao
            kat.say "Can't take...any more..."
            "As soon as the words are out of Kat's mouth, I know she's not kidding."
            "I can feel her muscles beginning to squeeze my cock."
            "And I know that means she's going to cum any moment."
            "The pressure has a similar effect on me too."
            "And I guess I have seconds at best to decide how I want to finish this thing!"
            menu:
                "Cum inside":
                    "By now I'm almost bending Kat in half."
                    "So the only solution is to keep right on going."
                    "With one final thrust, I make sure I'm as deep as I can go."
                    show kat missionary mouth_normal tongueout cum with hpunch
                    $ kat.sub += 1
                    "Then I shoot my load into her without holding back."
                    with hpunch
                    "Pinned down under my weight, Kat writhes and wriggles."
                    with hpunch
                    "Taking everything that I have to give until the very end."
                    show kat missionary out analdrip -cum
                "Pull out":
                    "I have Kat pinned down under my weight."
                    "So it's no challenge for me to pull out."
                    show kat missionary out eyes_pleasure mouth_normal tongueout
                    "She moans as it happens, her orgasm increasing in intensity."
                    show kat missionary cum with vpunch
                    "And then I let go, shooting my load over her stomach."
                    with vpunch
                    "Unable to escape, Kat writhes and wriggles."
                    show kat missionary mouth_pleasure bodycum -cum -tongueout with vpunch
                    $ kat.love += 2
                    "Being showered by all I have to give until the very end."
    show kat missionary eyes_pleasure mouth_pleasure -speed
    "Afterwards, Kat lies down on the sand, still panting and moaning."
    "I open my mouth to ask if she's okay, but then I see that her eyes are closed."
    "And it seems that she's actually fallen asleep!"
    "So I forget all about it and lie back down myself."
    "Because my job is done, and now I can relax."
    $ kat.sexperience += 1
    return

label kat_fuck_date_home:
    scene bg black
    show play console kat
    with fade
    "We've played almost every game that we can lay our hands on."
    "And we've smashed the high scores on all of them, every last one!"
    mike.say "Oh man..."
    mike.say "[bree.name] is going to be super mad!"
    "Kat pauses the game we're playing."
    "And then she gives me a sideways glance."
    scene bg livingroom
    show kat casual at center, zoomAt(1.5, (640, 1040))
    show fx question
    kat.say "Huh?"
    kat.say "What's she got to be mad about?"
    kat.say "It's not like we erased her saved games or anything!"
    kat.say "All we did was set new high scores."
    hide fx
    "I shake my head at this."
    mike.say "You don't understand, Kat..."
    mike.say "[bree.name]'s super competitive about that kind of thing!"
    mike.say "Like, once I beat her high score on Super Latino Stereotype Brothers."
    mike.say "And she couldn't let it stand."
    mike.say "She stayed up for three days until she beat my score!"
    show kat defiant
    "As I'm telling Kat all of this, I can see that she's smiling."
    "In fact, by the time I'm done, she's grinning like a Cheshire cat!"
    mike.say "Why are you smiling, Kat?"
    mike.say "This isn't a good thing!"
    kat.say "Well it sounds like a good thing to me, [hero.name]."
    kat.say "It sounds like [bree.name]'s got a real ego problem."
    kat.say "And I kind of feel good for sticking it to her!"
    "I can't help letting out a sigh of frustration."
    mike.say "That's easy for you to say, Kat."
    mike.say "But you're not the one that has to live with [bree.name]!"
    mike.say "And trust me..."
    mike.say "If she can't take it out on you, then she'll take it out on me instead!"
    show kat normal
    kat.say "Okay, okay..."
    kat.say "I get what you're saying."
    kat.say "Beat [bree.name] high score, make [bree.name] mad - then [bree.name] smash!"
    show kat defiant blush
    kat.say "So I'll just have to do something to make it up to you..."
    "I can't help wondering what Kat could mean by that."
    "So I keep a close eye on her as she puts down her joypad."
    "But all the same, I'm not ready for what she does next."
    "And that's because Kat literally turns and pounces on me!"
    mike.say "Wha..."
    mike.say "What are you..."
    hide kat
    show kat kiss
    with fade
    $ kat.flags.kiss += 1
    "By way of answer, Kat leans in closer and presses her lips against mine."
    "The kiss that follows is made all the more intense and exciting thanks to it being unexpected."
    "Kat makes it long and passionate too, her tongue exploring the inside of my mouth."
    "Only when she finally breaks it off do I get to finish what I was saying."
    hide kat
    show kat smile blush at center, zoomAt(1.5, (640, 1040))
    with fade
    mike.say "Oh..."
    mike.say "I think I see what you're doing now!"
    show kat defiant -blush
    kat.say "He finally gets it!"
    kat.say "It's a fucking miracle!"
    mike.say "Oh, ha ha..."
    mike.say "Very funny!"
    "Kat shakes her head as she starts to pull off her top."
    kat.say "Seriously though, [hero.name]..."
    show kat topless with dissolve
    show kat smile
    kat.say "You can be pretty slow on the uptake sometimes!"
    "I do the best I can to ignore the statement."
    "And instead I devote my attention to getting undressed."
    scene bg black
    show kat cowgirl livingroom mouth_pleasure
    with fade
    "Which proves to be harder than I expected."
    "Mainly because I have Kat sitting on top of me."
    "But with a truly massive amount of effort on my part, I eventually manage it."
    "Once we're both naked, Kat's still sitting astride my thighs, pinning me down."
    mike.say "Erm..."
    mike.say "Are you planning on moving any time soon?"
    "Kat cocks her head on one side, a thoughtful look on her face."
    kat.say "You know what..."
    kat.say "I think I'm good right here."
    "As if to underline her point, Kat takes hold of my cock."
    kat.say "So..."
    kat.say "Where do you want me to put this thing?"
    menu:
        "Fuck her pussy":
            "Part of me is still stinging from that last little jibe aimed in my direction."
            "So I'm not about to just lie back and let Kat take charge."
            "No, now that we're actually doing it, I feel the need to be the one in control."
            "Which is why my hands shoot up and grab her around the waist."
            mike.say "I've got a better idea, Kat..."
            mike.say "How about I show you?"
            "With that, I pull Kat downwards and onto me."
            kat.say "Wha..."
            kat.say "What are you..."
            show kat cowgirl eyes_close mouth_open vaginal
            "I don't even need to look downwards as I do it."
            "Because I already know where all the moving parts involved are."
            "And I also know exactly where I want them to go as well."
            "Kat's words are replaced by incoherent moans within seconds."
            "And the sounds that she's making only become louder as I begin to move."
            "All I'm doing is raising my groin and then lowering it again."
            "But that has the effect of rubbing my cock against the lips of her pussy."
            "And each time I do so, I can feel a shudder run through Kat."
            "This seems to affect the whole of her body without exception."
            "Yet the one place I feel things begin to change is between her legs."
            "Down there, things are getting hotter by the second."
            "Not only that, they're getting wetter at the same time too."
            "And I can feel the head of my cock beginning to slide around."
            "That should be making things easier for me, helping me get inside."
            "But instead it means that I need to redouble my efforts."
            "That is if I want to keep it from veering off target!"
            show kat cowgirl eyes_open mouth_pleasure
            kat.say "Mmm..."
            kat.say "That feels good!"
            kat.say "Keep doing whatever you're doing!"
            "I feel a small surge of frustration at Kat's demand."
            "Because what I'm doing right now is trying to get inside of her!"
            "So the last thing I want is to be stuck doing that until I lose it."
            "Making an effort to ignore her demands, I push on regardless."
            "And a moment later I'm rewarded by the sensation of something giving way."
            "It's not the feeling of Kay opening up to me totally."
            "Just the first inkling of her lips parting thanks to my efforts."
            "And it's enough for the head of my cock to begin sliding in there too."
            "Now that I have the foothold I need, I don't hold back."
            "I put all of my efforts into getting further inside."
            "Luckily for me it seems that the sensation is just as intense for Kat too."
            "Because she soon begins to nod and cling to me anew."
            "Spurred on by her approval, I throw myself into it."
            show kat cowgirl eyes_up mouth_hurt
            "And as soon as I begin to move inside her, my efforts are rewarded."
            "All it takes is the slightest movement on my part to inspire the same in Kat."
            "She moves in sympathy to me, perfectly matching her motions to mine."
            "This means that as I'm pleasuring her, she's doing the same to me."
            "And the sensation is one of total and utter release."
            "My speed picks up without my even noticing it."
            "The first time I become aware of my pace is when I'm going all out."
            "Kat's writhing and wriggling under me the whole time."
            "After all that build up, things feel like they're going crazily fast."
            "But there's no sense of disappointment in me on that account."
            "Instead I feel totally lost in the moment, absorbed in what we're doing."
            show kat cowgirl mouth_open
            "And when I look up at Kat, panting and massaging her own body..."
            "Well, how in the hell am I going to be able to keep this up much longer?"
            "Already I can feel the sensation welling up inside of me."
            "The feeling that let's me know I'm about to lose it."
            "Kat's moaning now too, as if she can sense it as clearly as I can."
            "And I'm going to need to decide how I want this to end."
            menu:
                "Cum inside":
                    "Still going at the same break-neck pace, I don't stop for a second."
                    show kat cowgirl cum mouth_pleasure with vpunch
                    $ kat.love += 4
                    "I just keep right on going until the moment that I shoot my load."
                    with vpunch
                    "And it just so happens that I'm deep inside Kat when it happens."
                    with vpunch
                    "This means that she takes all of it at point-blank range."
                    with vpunch
                    "As soon as she does, her own orgasm hits, rendering her helpless."
                    with vpunch
                    "And squeezing me as I ride out the last waves of my own."
                "Pull out":
                    show kat cowgirl out
                    "I change direction and pull out of Kat without warning."
                    "All of this happens at the same speed I've been keeping up."
                    "The result is that the sensations Kat feels push her over the edge."
                    with vpunch
                    "She's left helpless and in the grips of her own orgasm."
                    show kat cowgirl cum mouth_pleasure with vpunch
                    $ kat.sub += 1
                    "And it happens just as mine hits too."
                    show kat cowgirl bodycum with vpunch
                    "Which means she's helpless to escape as I shoot my load over her."
        "Fuck ass":
            "Part of me is still stinging from that last little jibe aimed in my direction."
            "So I'm not about to just lie back and let Kat take charge."
            "No, now that we're actually doing it, I feel the need to be the one in control."
            "Which is why my hands shoot up and grab her around the waist."
            mike.say "I've got a better idea, Kat..."
            mike.say "How about I show you?"
            "With that, I pull Kat downwards and onto me."
            kat.say "Wha..."
            kat.say "What are you..."
            show kat cowgirl eyes_close mouth_open anal
            "I don't even need to look downwards as I do it."
            "Because I already know where all the moving parts involved are."
            "And I also know exactly where I want them to go as well."
            "Kat's words are replaced by incoherent moans within seconds."
            "And the sounds that she's making only become louder as I begin to move."
            "All I'm doing is raising my groin and then lowering it again."
            "But that has the effect of rubbing my cock between the cheeks of her ass."
            "And each time I do so, I can feel a shudder run through Kat."
            "This seems to affect the whole of her body without exception."
            "Yet the one place I feel things begin to change is between her buttocks."
            "Down there, things are getting hotter by the second."
            "Not only that, they're getting wetter at the same time too."
            "And I can feel the head of my cock beginning to slide around."
            "That should be making things easier for me, helping me get inside."
            "But instead it means that I need to redouble my efforts."
            "That is if I want to keep it from veering off target!"
            show kat cowgirl eyes_open mouth_pleasure
            kat.say "Mmm..."
            kat.say "That feels good!"
            kat.say "Keep doing whatever you're doing!"
            "I feel a small surge of frustration at Kat's demand."
            "Because what I'm doing right now is trying to get inside of her!"
            "So the last thing I want is to be stuck doing that until I lose it."
            "Making an effort to ignore her demands, I push on regardless."
            "And a moment later I'm rewarded by the sensation of something giving way."
            "It's not the feeling of Kat opening up to me totally."
            "Just the first inkling of her muscles relaxing thanks to my efforts."
            "And it's enough for the head of my cock to begin sliding in there too."
            "Now that I have the foothold I need, I don't hold back."
            "I put all of my efforts into getting further inside."
            "Luckily for me it seems that the sensation is just as intense for Kat too."
            "Because she soon begins to nod and cling to me anew."
            "Spurred on by her approval, I throw myself into it."
            show kat cowgirl eyes_up mouth_hurt
            "And as soon as I begin to move inside her, my efforts are rewarded."
            "All it takes is the slightest movement on my part to inspire the same in Kat."
            "She moves in sympathy to me, perfectly matching her motions to mine."
            "This means that as I'm pleasuring her, she's doing the same to me."
            "And the sensation is one of total and utter release."
            "My speed picks up without my even noticing it."
            "The first time I become aware of my pace is when I'm going all out."
            "Kat's writhing and wriggling under me the whole time."
            "After all that build up, things feel like they're going crazily fast."
            "But there's no sense of disappointment in me on that account."
            "Instead I feel totally lost in the moment, absorbed in what we're doing."
            show kat cowgirl mouth_open
            "And when I look up at Kat, panting and massaging her own body..."
            "Well, how in the hell am I going to be able to keep this up much longer?"
            "Already I can feel the sensation welling up inside of me."
            "The feeling that let's me know I'm about to lose it."
            "Kat's moaning now too, as if she can sense it as clearly as I can."
            "And I'm going to need to decide how I want this to end."
            menu:
                "Cum inside":
                    "Still going at the same break-neck pace, I don't stop for a second."
                    show kat cowgirl cum mouth_pleasure with vpunch
                    $ kat.sub += 2
                    "I just keep right on going until the moment that I shoot my load."
                    with vpunch
                    "And it just so happens that I'm deep inside Kat when it happens."
                    with vpunch
                    "This means that she takes all of it at point-blank range."
                    with vpunch
                    "As soon as she does, her own orgasm hits, rendering her helpless."
                    with vpunch
                    "And squeezing me as I ride out the last waves of my own."
                "Pull out":
                    show kat cowgirl out
                    "I change direction and pull out of Kat without warning."
                    "All of this happens at the same speed I've been keeping up."
                    "The result is that the sensations Kat feels push her over the edge."
                    with vpunch
                    "She's left helpless and in the grips of her own orgasm."
                    show kat cowgirl cum mouth_pleasure with vpunch
                    $ kat.love += 2
                    "And it happens just as mine hits too."
                    show kat cowgirl bodycum with vpunch
                    "Which means she's helpless to escape as I shoot my load over her."
    $ kat.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
