init python:
    Event(**{
    "name": "emma_dream_01",
    "label": "emma_dream_01",
    "priority": 1000,
    "conditions": [
        MinDaysPlayed(10),
        HeroTarget(
            IsGender("male"),
            IsActivity("sleep"),
            MinStat("fun", 10),
            ),
        ],
    "chances": 20,
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_dream_02",
    "label": "emma_dream_02",
    "priority": 1000,
    "conditions": [
        IsDone("emma_dream_01"),
        HeroTarget(
            IsActivity("sleep"),
            MinStat("fun", 10),
            MaxStat("luck"),
            ),
        PersonTarget(emma,
            IsFlag("emmadelay", False)
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_01",
    "label": "emma_event_01",
    "priority": 1000,
    "conditions": [
        IsDone("emma_dream_02"),
        IsHour(10, 15),
        HeroTarget(HasRoomTag("park")),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Activity(**{
    "name": "look_for_emma_park",
    "label": "look_for_emma_park",
    "conditions": [
        IsDone("emma_event_01"),
        HeroTarget(
            HasRoomTag("park"),
            MinStat("energy", 2),
            MinStat("hunger", 1),
            MinStat("grooming", 1),
            MinStat("fun", 1),
            ),
        PersonTarget(emma,
            IsFlag("search")
            ),
        ],
    "icon": "emma",
    "display_name": "Look for the dream girl",
    "do_once": True
    })

    Activity(**{
    "name": "look_for_emma_mall",
    "label": "look_for_emma_mall",
    "rooms": ("mall1", "mall2"),
    "conditions": [
        IsDone("emma_event_01"),
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 1),
            MinStat("grooming", 1),
            MinStat("fun", 1),
            ),
        PersonTarget(emma,
            IsFlag("search")
            ),
        ],
    "icon": "emma",
    "display_name": "Look for the dream girl",
    "do_once": True
    })

    Activity(**{
    "name": "look_for_emma_gym",
    "label": "look_for_emma_gym",
    "rooms": ("gym", "gymmachine", "gymlockers", "gymreception"),
    "conditions": [
        IsDone("emma_event_01"),
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 1),
            MinStat("grooming", 1),
            MinStat("fun", 1),
            ),
        PersonTarget(emma,
            IsFlag("search")
            ),
        ],
    "icon": "emma",
    "display_name": "Look for the dream girl",
    "do_once": True
    })

    Activity(**{
    "name": "look_for_emma_university",
    "label": "look_for_emma_university",
    "rooms": "university",
    "conditions": [
        IsDone("emma_event_01"),
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 1),
            MinStat("grooming", 1),
            MinStat("fun", 1),
            ),
        PersonTarget(emma,
            IsFlag("search")
            ),
        ],
    "icon": "emma",
    "display_name": "Look for the dream girl",
    "do_once": True
    })

    Event(**{
    "name": "emma_event_02",
    "label": "emma_event_02",
    "priority": 1000,
    "conditions": [
        IsDone("look_for_emma_park"),
        IsDone("look_for_emma_mall"),
        IsDone("look_for_emma_gym"),
        IsDone("look_for_emma_university"),
        Or(
            IsDone("samantha_event_A01"),
            IsDone("samantha_event_B01"),
            ),
        IsHour(10, 15),
        HeroTarget(IsRoom("bakery")),
        PersonTarget(emma,
            IsFlag("search"),
            ),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_03",
    "label": "emma_event_03",
    "priority": 1000,
    "conditions": [
        IsDone("emma_event_02"),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("emmadelay", False),
            ),
        ],
    "do_once": True,
    })

    InteractEvent(**{
    "name": "emma_event_04",
    "label": "emma_event_04",
    "priority": 1000,
    "conditions": [
        IsDone("emma_event_03_appointment"),
        PersonTarget(emma,
            IsActive(),
            MinStat("love", 20),
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "emma_event_05",
    "label": "emma_event_05",
    "priority": 1000,
    "conditions": [
        IsDone("emma_event_04"),
        HeroTarget(IsRoom("coffeeshop")),
        PersonTarget(emma,
            IsActive(),
            MinStat("love", 30),
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_06",
    "label": "emma_event_06",
    "priority": 1000,
    "conditions": [
        'not Room.find("electronic").hidden',
        IsDone("emma_event_05"),
        IsHour(10, 20),
        PersonTarget(emma,
            Not(IsPresent()),
            MinStat("love", 40),
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_07",
    "label": "emma_event_07",
    "priority": 1000,
    "conditions": [
        IsDone("emma_event_06_finish"),
        HeroTarget(IsActivity("offer_a_drink")),
        PersonTarget(emma,
            IsActive(),
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_08",
    "label": "emma_event_08",
    "priority": 1000,
    "conditions": [
        IsDone("emma_event_07"),
        IsHour(21, 0),
        HeroTarget(
            Not(OnDate()),
            IsRoom("livingroom"),
            ),
        PersonTarget(emma,
            MinStat("love", 80)
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_09",
    "label": "emma_event_09",
    "priority": 1000,
    "conditions": [
        IsDone("emma_event_08"),
        PersonTarget(emma,
            IsPresent(),
            Not(IsHidden()),
            Not(IsFlag("delay")),
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_09_sam",
    "label": "emma_event_09_sam",
    "conditions": [
        PersonTarget(samantha,
            IsFlag("friendzone", False)
            ),
        PersonTarget(emma,
            IsFlag("talktosam"),
            MinStat("love", 120),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_09_betrayed",
    "label": "emma_event_09_betrayed",
    "conditions": [
        PersonTarget(samantha,
            IsFlag("friendzone")
            ),
        PersonTarget(emma,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("samgirlfriend"),
            IsFlag("samok", False),
            IsFlag("samresolved", False),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_09_okayed",
    "label": "emma_event_09_okayed",
    "conditions": [
        PersonTarget(samantha,
            IsFlag("friendzone")
            ),
        PersonTarget(emma,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("samgirlfriend"),
            IsFlag("samok"),
            IsFlag("samresolved", False),
            MinStat("love", 120),
            ),
    ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_10_cinema",
    "label": "emma_event_10_cinema",
    "priority": 500,
    "conditions": [
        IsDone("emma_fuck_date_second"),
        HeroTarget(IsActivity("date_watch_a_movie")),
        PersonTarget(emma,
            IsRoom("date_cinema")
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_10_bree",
    "label": "emma_event_10_bree",
    "priority": 500,
    "conditions": [
        IsDone("emma_fuck_date_second"),
        HeroTarget(IsRoom("classroom")),
        PersonTarget(emma,
            IsRoom("classroom")
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            IsRoom("classroom")
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_10_gfs",
    "label": "emma_event_10_gfs",
    "priority": 500,
    "conditions": [
        IsDone("emma_fuck_date_second"),
        HeroTarget(Or(IsActivity("date_picnic"), IsActivity("date_make_snowman"))),
        PersonTarget(emma,
            IsRoom("date_park")
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_10",
    "label": "emma_event_10",
    "priority": 500,
    "conditions": [
        IsDone("emma_event_10_gfs", "emma_event_10_bree", "emma_event_10_cinema"),
        PersonTarget(emma,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("event10delay", False),
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "emma_event_11",
    "label": "emma_event_11",
    "priority": 500,
    "conditions": [
        IsDone("emma_fuck_date_third"),
        PersonTarget(emma,
            IsActive(),
            MinStat("love", 160),
            IsFlag("emmadelay", False),
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_event_12",
    "label": "emma_event_12",
    "priority": 500,
    "conditions": [
        IsDone("emma_event_11"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_beach")),
        PersonTarget(emma,
            OnDate(),
            MinStat("love", 180),
            IsFlag("emmadelay", False),
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "emma_preg_talk",
    "label": "emma_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(emma,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/tiny_love.ogg",
    })

label emma_dream_01:
    scene bg bedroom1 at blur(16), dark, dark with dissolve
    $ emma.flags.emmadelay = TemporaryFlag(True, 7)
    "I don't know where this begins, just that I'm here and the time is now."
    "I'm walking through one of those hedge mazes, the kind they have in the grounds of stately homes and such."
    "I have no idea how I got here or exactly why I might have chosen to wander into a maze."
    "But as this is a dream, I guess none of that stuff is really relevant."
    "The one thing that I do know is that I'm hopelessly lost, although I don't know why I should know that and almost nothing else at all."
    "Standing well above the height of my own head, the hedges of the maze keep me from being able to see anything outside of it."
    "My only options are to either go forwards or back, and it seems as though the former is the choice I keep making."
    "In the back of my mind, I can vaguely recall that to navigate a maze, you either need to always turn left or right."
    "But the frustrating thing is that I can't actually remember which of the two it is."
    "This means that I keep making turns that seem to be completely random and without a shred of reason to them."
    "More than once I find myself thinking that the maze surely can't be so big as to keep me lost like this forever."
    "If I keep wandering for long enough, there must be a way out."
    "It's then that I catch sight of something as it flits around the corner just ahead of me."
    show emma at center, zoomAt(1.5, (640, 1040)), blur(5) with dissolve
    pause 0.1
    hide emma with dissolve
    "The slightest flicker of auburn hair and the last lingering notes of musical laughter, like the essence of a human being upon the air itself."
    "At this, my memory sparks and I remember for a second why I'm here at all."
    "I'm following on her heels, trying to catch even the most fleeting glimpse of the girl."
    show emma at center, zoomAt(1.5, (640, 1040)), blur(5) with dissolve
    pause 1
    hide emma with moveoutright
    "But thus far, she's always eluded me, and this only compels me to hurry on in the hope of catching her."
    "How I know the person ahead of me is a girl and just why I must follow her are things that, in the manner of a dream, don't seem to matter at all."
    "All that matters is that she keeps on slipping away around the corners that loom ahead of me and the fact that I have to catch her."
    "What I can see of her comes in snatched glimpses and what I can see out of the corner of my eye."
    show emma at center, blur(5) with dissolve
    "I perceive pale skin, eyes of blue, or green, or hazel that flit here and there in a round, laughing face."
    show emma at left with ease
    "Legs that disappear with the shimmer of tights catching the late sunlight of the afternoon as they do so."
    hide emma with moveoutleft
    "But even as I grasp at these few elements of the whole which still eludes me, I see that she quickens her pace yet more."
    "I'm forced almost to run now, even to keep the barest glimpse of her heels ahead of me as I genuinely chase her through the endless maze."
    "Somehow the fact that we're running fills me with the impression that an end of some sort is fast approaching."
    "For a moment, I lose sight of her completely, and I can feel my heart begin to pound with a rising sense of panic at doing so."
    "And then I round one last corner, and come to a sudden halt."
    show emma with dissolve
    "There she is, standing with her back to me, no more than a couple of metres ahead."
    "I hold my hand up to her, wanting to close that last short distance that still lies between us."
    "But as I do so, she turns at the waist and regards me with one large eye, as her hair covers the other."
    "Now that I can see her this close and still as a statue, I notice that she's relatively short and quite delicate in appearance."
    "Her slender limbs and pale skin almost give her the look of a child's doll that's been scaled up in size and somehow given the spark of life."
    "She looks at me in a manner that suggests familiarity, not at all surprised at my having followed her with such determination."
    "Girl" "Well - are you ready for our date?"
    "And that's it - with the sound of her voice still ringing in my ear, I wake up."
    "But the image of her face and those few words are as real to me as if she were standing in front of me, right here and now."
    hide emma with dissolve
    return

label emma_dream_02:
    scene bg bedroom1 at blur(16), dark, dark with dissolve
    "I can feel the leather of the leash wrapped around my hand as her weight strains against it, pulling it tighter."
    "It's an effort to keep the whole thing taut, what with the collar around her neck being how she's attached to it."
    show emma doggy ahegao saliva bounce speed squirt at blur(10) with dissolve
    pause 0.1
    hide emma with dissolve
    "But I feel that I've done this many times before, and so has she, so I'm not particularly worried about her being choked."
    "Well, any more than she likes to be, that is..."
    "If anything, she seems to be more eager to struggle and strain than I am to pull hard on the leash so that it chafes at her."
    show emma doggy smile with dissolve
    "She's crouched down in front of me, on all fours and completely naked save for the collar and leash."
    "The only sound apart from the straining of the leather is the jingling of the bell that hangs around her neck."
    hide emma with dissolve
    "That and the sound of our own breathing, coming heated and heavy as we build up to what comes next."
    "She glances over her shoulder at me, pale cheeks flushed with excitement and anticipation."
    "I can see that she's keen for me to begin, wanting to feel the sensation of me inside her with a true sense of urgency."
    "And thanks to the angle that she's crouched at, I don't even need to part her buttocks to find her pussy."
    "Instead I can already see it's pink lips as they glisten invitingly before me, letting me know that she's already slick in anticipation."
    "I could easily place my hands on her buttocks and push inside of her without her moving as much as an inch."
    "But with the leash still held firmly in my hand, I have other ideas as I begin to wrap ever more of it around my clenched fist."
    "I hear her breathing quicken as the shortening of the leash means she's forced to move backwards an inch at a time."
    "All it takes is for me to make sure that my stiff cock is poised at just the right height as she does so."
    show emma doggy pleasure with dissolve
    "Soon she feels the sensation of the head, pressing against the lips of her pussy."
    "But I'm not about to allow her the luxury of pausing to prepare herself - not that she'd want me to either."
    "And so instead I keep winding in the leash still further, making her keep on going."
    "I hear her gasp in reaction to the way she's being forced to take me in at a pace she cannot predict."
    "There's little need to be anything other than gentle with her in order to push inside, as she's already plenty wet enough."
    "But the uncertainty and lack of control is making her excitable, which in turn is making me all the more determined."
    "Keeping as still as I can manage, I savour the sensation of feeling her as she's pulled onto my cock."
    "Her body twitches as the feelings her body is experiencing come upon her without preamble or warning."
    show emma doggy ahegao saliva bounce speed squirt with dissolve
    "At the same time she moans and cries out from the pleasure she's feeling, her motions making the bell hung from her collar tinkle away almost constantly."
    "Once I'm in as far as I can go, I hold myself rigid inside of her, simply enjoying the prolonged feeling of excitement this gives me."
    "The effect is only made that much better by the sight of her limbs beginning to twitch and her backside shaking as I do so."
    "Feeling just a little merciful, I begin to thrust in and out of her a few moments later."
    "She lets out a deep, throaty groan in relief and begins to move in sympathy, her cheeks becoming even more red with the enjoyment of it all."
    "Her auburn hair is plastered to her head, darkened by the sweat that soaks it."
    "She casts her head around, almost like an animal lowing for relief as she receives satisfaction for her desires."
    "And then she throws it back so that her hair is tossed aside and slaps heavily against her shoulders and the nape of her neck."
    "I feel her sweat splash against my naked chest, wondering at the fact that she could be so drenched thanks to what we're doing together."
    "The only response that I can even think of making is to try and fuck her yet harder, feeling my balls slap against her backside as I do so."
    "I see her reach up for the collar at her throat in response, holding onto it for a moment as if to seek release."
    "If she had a bit in her mouth right now, I have no doubt that she'd be champing at it."
    "But she seems to realise swiftly that none will come from doing so, and her hand falls quickly to one of her heavy breasts."
    "Her fingers are squeezing and tugging almost desperately at her own erect nipple."
    "I see that she's trying to add yet more intensity to the act, hoping to bring about her climax as she does so."
    "Giving her one last yank on the leash, I feel myself letting go too."
    "I have no fear of thrusting forwards for a final time as I cum inside of her, sure in the knowledge that she's already pregnant."
    "Utterly exhausted, I expect to collapse at her side..."
    hide emma with dissolve
    "And it's then that I suddenly wake up, bathed in sweat, wrapped in sheets and with the sensation of my own fast-cooling cum running down the inside of my thigh."
    return

label emma_event_01:
    "While casually walking around the park, I stop short when I see someone familiar in the distance."
    "I can't put my finger on who she is, but whoever it is, seeing her caused a shiver to run down the back of my neck."
    "With such a strong reaction, I can't help but go toward her to figure out what's going on."
    "And then it hits me, without warning. The most intense memory I've ever had."
    show emma doggy ahegao saliva bounce speed squirt with dissolve
    "The memory of that dream is so powerful I stumble, but that's not enough to banish the dream from my mind."
    "It's almost as though I'm experiencing the dream while awake; on one hand, my cock is definitely still in my pants."
    "But on the other hand, I can feel it sliding in and out of her wet pussy. I can hear her moaning. I can feel her sweat!"
    hide emma with dissolve
    "With all the concentration I can muster, I bring myself back to the present. I can't very well just suddenly come in the middle of the park!"
    "And when I look around, the girl is gone."
    "Did I imagine her? Am I going crazy?"
    menu:
        "She's not real, it's just a dream (Never meet Emma again)":
            "There's no way she was real. I must have imagined her. Maybe I'm overly tired and seeing things."
            "Maybe I should see a doctor."
            $ emma.set_gone_forever()
        "She's real. I have to find her":
            "I know what I saw was real. I have to find her again."
            "She was there, she must have just gone elsewhere while I was ... whatever was going on with me."
            $ emma.flags.search = True
    return

label look_for_emma_park:
    "I look all over the park for any sign of the dream girl, but nothing."
    return

label look_for_emma_mall:
    "I look all over the mall for any sign of the dream girl, but nothing."
    return

label look_for_emma_gym:
    "I look all over the gym for any sign of the dream girl, but nothing."
    return

label look_for_emma_university:
    "I look all over the university for any sign of the dream girl, but nothing."
    return

label emma_event_02:
    $ emma.flags.search = False
    "Samantha walks up to me with a shorter girl a little bit behind her. I don't really see her because Samantha has a great big smile on her face."
    "And that's very distracting."
    show samantha happy zorder 2 at center
    show emma zorder 1 at left4, dark
    with dissolve
    samantha.say "Hey [hero.name]!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey Cupcake! How you doing?"
    else:
        mike.say "Hey Sam! How you doing?"
    samantha.say "Great! Listen, I want you to meet a friend of mine."
    show samantha at right5
    show emma at left5
    with move
    samantha.say "[hero.name], I'd like you to meet Emma! I met her through school and she's one of the good ones."
    if samantha.flags.mikeNickname in nickname_master:
        $ emma.flags.samgirlfriend = True
        samantha.say "And Emma, this is my Master, [heroname]!"
    elif not samantha.flags.friendzone and not samantha.flags.breakup and ("samantha_event_A01" in DONE or "samantha_event_E01" in DONE):
        $ emma.flags.samgirlfriend = True
        samantha.say "And Emma, this is my boyfriend, [heroname]!"
    else:
        samantha.say "And Emma, this is my best friend, [heroname]!"
    hide emma
    show emma at left5
    with dissolve
    "I'm going to be honest right now, I'm not sure what Sam just said, because the girl she's introducing is my dream girl!"
    "And just like the last time I saw her, I have an incredibly intense image of the dream I had. It completely overpowers me, and I can't even talk."
    hide emma
    show emma doggy ahegao saliva bounce speed squirt
    with dissolve
    "It is through sheer will alone that I force myself to ignore it and pay attention to the girls in front of me."
    hide emma
    show samantha happy at right5
    show emma blush at left5
    with dissolve
    mike.say "H-h. Hi, um. I'm sorry I was, um. What was your name again?"
    "The girl makes a little squeaking sound."
    show samantha surprised
    samantha.say "What in the world is up with you two?"
    emma.say "Oh uh. Hi, [hero.name]. Emma, my name is Emma."
    show samantha normal
    "Get it together, [hero.name]! It was just a dream!"
    mike.say "Hi, Emma. How is it you know Sam again?"
    emma.say "Oh, Sam and I met in an internship program at the university. I just graduated and um we're both..."
    "Emma trails off; it seems like she meant to finish the sentence, but got lost in her own words."
    mike.say "Both what?"
    "Emma looks extremely uncomfortable."
    emma.say "Oh um we're both looking at the same, um, stuff and I was, um."
    show samantha annoyed at right4 with move
    "Samantha shouts loud enough that Emma and I are both startled."
    samantha.say "[hero.name]!"
    show emma normal at left4 with move
    mike.say "What?"
    samantha.say "Why are you staring at her like that?"
    mike.say "Like what?"
    samantha.say "Like you're going to eat her or something!"
    mike.say "Oh? Oh! Oh my gosh, I'm so sorry. I just...sorry, Emma looks so familiar, like someone I know, but don't know. Like Deja Vu or something! You know what I mean?"
    emma.say "Yes."
    samantha.say "Yes what?"
    emma.say "I mean, yes, I know what you mean. I f--I, ah, I've felt..that kind of thing before."
    emma.say "Look I've got to go! I have, um, papers to work on. For work."
    hide emma with moveoutleft
    "And before I can even say anything, or ask her number (damn it, I really should have asked for her number) she runs out."
    show samantha angry at center with move
    "Then Samantha turns and gives me the \"What the hell are you doing?\" look."
    samantha.say "Good job, scaring her off like that! What's going {b}on{/b} with you?"
    mike.say "Oh, nothing, I just...I'm sorry, I guess I've got a lot on my mind and she looks so familiar and..."
    show samantha annoyed
    samantha.say "Ugh. You'd better be nice! I think she's going to be a really good friend and I wanted you two to be friends. Because, you know."
    if "samantha_event_A02" in DONE:
        "Wait a minute. Suddenly I remember how she introduced me."
        if samantha.flags.mikeNickname in nickname_master:
            mike.say "Did you just tell her I'm your Master?"
        elif not samantha.flags.friendzone and not samantha.flags.breakup and ("samantha_event_A01" in DONE or "samantha_event_E01" in DONE):
            mike.say "Did you just tell her I'm your boyfriend?"
        else:
            mike.say "Did you just tell her I'm your best friend?"
        samantha.say "Yep!"
        mike.say "I, uh, we didn't talk about that."
        samantha.say "We didn't? I, um. Did I assume too much?"
        menu:
            "Yes":
                $ samantha.love -= 5
                $ samantha.sub -= 5
                mike.say "Yeah, I mean, just that hit me out of nowhere, and I wasn't ready for it."
                show samantha sad
                samantha.say "Oh. I...I thought..."
                mike.say "No, wait! I'm not saying I don't want that, I just...not by surprise, okay? Let's talk about it later, okay?"
                samantha.say "Yeah, sure, I guess..."
                return
            "No it's fine!":
                mike.say "No no, it was a surprise, but I like it!"
                samantha.say "So you're my boyfriend, then? And I'm your girlfriend?"
                mike.say "Yes!"
                show samantha happy
                samantha.say "See! I knew I picked the right guy after all."
                $ samantha.set_girlfriend()
    else:
        mike.say "Because what?"
        samantha.say "Because you're my best friend and I think all my friends should get along!"
        show samantha normal
        samantha.say "Besides, she's cute and I thought you'd like her."
        mike.say "Are you trying to set me up with her?"
        samantha.say "Well, yeah, if you don't blow it. Like you nearly did just now!"
        samantha.say "I'll talk to her and smooth it over. Unless you think she's not your type..."
        mike.say "No! I mean, yes. Yes she's my type!"
        samantha.say "That's what I thought!"
    samantha.say "I gotta get back to work."
    $ samantha.flags.emmadelay = TemporaryFlag(True, 2)
    return

label emma_event_03:
    play music "music/roa_music/the_one.ogg" loop fadeout .5 fadein .5
    show samantha
    samantha.say "Hi [hero.name]!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey Cupcake!"
    else:
        mike.say "Hey Sam!"
    samantha.say "I still want to set something up with you me and Emma, even after last time was weird. Coffee maybe?"
    "The dream girl!"
    menu:
        "Not interested (Never meet Emma again)":
            if samantha.flags.nickname == "cupcake":
                mike.say "Sorry, Cupcake, I'm not really all that interested."
            else:
                mike.say "Sorry, Sam, I'm not really all that interested."
            samantha.say "Oh. That's disappointing. I really thought you and she would hit it off. But I guess I don't want to force it if you don't want."
            mike.say "Thanks for understanding."
            $ samantha.love -= 10
            $ emma.set_gone_forever()
        "Sure":
            mike.say "Sure, I'll try again."
            samantha.say "And try not to be such a creep this time!"
            "I can only laugh at that."
            if samantha.flags.nickname == "cupcake":
                mike.say "Sure, Cupcake."
            else:
                mike.say "Sure, Sam."
            samantha.say "When is good for you?"
            $ day, week_day = day_chooser()
            $ hero.calendar.add(day, LabelAppointment(16, ["samantha"], "Meet with Sam and Emma", "emma_event_03_appointment", "emma_event_03_appointment_missed"))
            samantha.say "Great! I get off work at 16:00 that day. Meet us at 16:00?"
            mike.say "It's a date!"
            if emma.flags.samgirlfriend or "samantha_event_B01" not in DONE or game.flags.ryandead or (Harem.find_by_name("home") and Harem.find_by_name("home").is_active(samantha)):
                samantha.say "Don't be silly, I didn't say you were dating us!"
                menu:
                    "Aw, why not?":
                        mike.say "Aw, why not?"
                        $ samantha.lesbian += 1
                        samantha.say "Well, we haven't talked about that kind of thing, for one!"
                    "A friend date, then":
                        pass
            else:
                samantha.say "Don't be silly, I'm married!"
            mike.say "Fine, a friend date, then."
    return

label emma_event_03_appointment_missed:
    "Shit I missed my date with Samantha and Emma."
    $ samantha.love -= 10
    $ emma.love -= 10
    $ hero.calendar.add(game.days_played + 6, LabelAppointment(16, ["emma", "samantha"], "Meet with Sam and Emma", "emma_event_03_appointment", "emma_event_03_appointment_missed"))
    return

label emma_event_03_appointment(appointment=None):
    $ DONE["emma_event_03_appointment"] = game.days_played
    play music "music/roa_music/tiny_love.ogg" loop fadeout .5 fadein .5
    scene bg coffeeshop
    show samantha casual zorder 2 at left5
    show emma casual zorder 1 at right5
    samantha.say "Hi, [hero.name]!"
    show samantha zorder 2 at left, zoomAt(1.5, (640, 1040))
    "Samantha steps up and wraps her arms around me in a tight hug."
    samantha.say "Thanks for coming!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Hi Cupcake!"
    else:
        mike.say "Hi Sam!"
    samantha.say "I hope you're less distracted today, [hero.name]!"
    hide samantha
    show samantha casual zorder 2 at left5
    "I take a quick peek at Emma and the memory of the dream threatens to invade my vision again. I do my best to brush it aside."
    mike.say "Jury's out, I'm afraid, but I'll do my best."
    "Emma giggles a little bit at that."
    samantha.say "And you, Emma, what was your excuse?"
    show emma blush
    emma.say "Oh, um. I, er, had...something on my mind, I guess."
    emma.say "I'm better now, I promise."
    show emma normal
    samantha.say "Coffee? My treat!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Sure, Cupcake. You know my order already."
    else:
        mike.say "Sure, Sam. You know my order already."
    samantha.say "Emma?"
    emma.say "Ah, um, a caramel frappe I guess?"
    samantha.say "Coming right up."
    hide samantha
    show emma at center
    with moveoutleft
    "After Sam walks toward the counter to get the drinks, there's an awkward silence. I do my best to try to fill it."
    if samantha.flags.nickname == "cupcake":
        mike.say "So, how long have you known my Cupcake?"
    else:
        mike.say "So, how long have you known Sam?"
    emma.say "Um, a few months I guess? We met at one of the seminars and she seemed nice. And when we met up again she needed someone to study with, so I helped her out."
    mike.say "So you're a student then?"
    emma.say "Not anymore. I just started my first internship!"
    mike.say "Doing what?"
    emma.say "Teaching second graders. Mostly I sit and watch and help grade papers but an hour or so a day I get to run a lecture or a group project."
    emma.say "And I can help the kids during Q&A time too."
    mike.say "Oh, that's great!"
    emma.say "What do you do?"
    if hero.flags.promoted >= 5:
        mike.say "I manage a small team at a small company. We do a lot of IT stuff."
    else:
        mike.say "I do IT stuff at a small company."
    emma.say "Oh. Is it interesting?"
    "I shrug."
    mike.say "I guess? I mean it's a living, right?"
    emma.say "But is it something you love?"
    menu:
        "Yeah":
            mike.say "Yeah, actually, I guess I do love my job. At least I don't hate going to work every day, but sometimes it can be stressful."
            $ emma.love += 3
        "No":
            mike.say "Not really, I guess. It's just what I do to get by."
    emma.say "Oh, okay. I guess I've always wanted to make sure I'm doing something I love, even if doesn't pay well."
    mike.say "And do you?"
    emma.say "Well I've only just gotten started, but helping kids grow? Yeah I've always loved that. I think I always will."
    show emma at right5
    show samantha casual at left5
    with moveinleft
    samantha.say "I'm back! Here's your drinks!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Thanks, Cupcake!"
    else:
        mike.say "Thanks, Sam!"
    $ hero.energy += 2
    samantha.say "You two getting along this time?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake... I had a moment! Are you going to hold it against me forever?"
    else:
        mike.say "Sam! I had a moment! Are you going to hold it against me forever?"
    show samantha happy
    samantha.say "Yep! You're never going to live that one down. Weirdo [hero.name], that's who you are now."
    mike.say "Oh, don't make me come up with a nickname for you!"
    samantha.say "Such as?"
    mike.say "Give me some time to think about it."
    show emma happy
    "Emma laughs, and it's kind of a sudden, unexpectedly loud laugh."
    emma.say "You two are funny. It's cute."
    samantha.say "See? I knew you two would get along."
    show samantha normal
    show emma normal
    "We spend the next half hour or so making small-talk. Nothing consequential, really. It's me describing the office a bit, and Emma and Sam sharing stories about school."
    emma.say "Well, I'd better go. I have a lot of papers to grade."
    mike.say "It was good to really get to meet you, Emma."
    show emma blush ahoge
    emma.say "Oh, I uh...yeah it was good to meet you too, [hero.name]!"
    "We all start to go, and Emma has even gotten most of the way out of the coffee shop. But then she turns and practically runs back to us."
    "Wordlessly, she shoves a small slip of paper into my hands, then giggles a little bit and runs away again."
    "When I look at it, it's her phone number."
    $ hero.smartphone_contacts.append("emma")
    hide emma
    show samantha happy at center
    with moveoutright
    if samantha.flags.samgirlfriend:
        samantha.say "Oh! [hero.name], be careful with that! Don't make me all jealous, now!"
        mike.say "If I do, you have only yourself to blame."
        "She narrows her eyes at me."
        samantha.say "You'd {b}better{/b} be good!"
        "I offer her a wink before walking away."
    else:
        samantha.say "Oh, I think she likes you! Maybe you should ask her out!"
        mike.say "After just one meeting? That's a bit premature."
        samantha.say "You two will be an amazing couple!"
        mike.say "Oh I get it, you think I'm still madly in love with you and just looking to help me move on, is that it?"
        samantha.say "Maybe! I'll never tell!"
        mike.say "Ugh, women!"
        samantha.say "You love it!"
        "She offers me a wink before walking away."
    $ game.room = "coffeeshop"
    $ game.pass_time(1, needs=True)
    $ emma.unhide()
    return

label emma_event_04:
    show emma
    if emma.love.max < 30:
        $ emma.love.max = 30
    emma.say "Hi, [hero.name]!"
    mike.say "Nice to see you, Emma!"
    emma.say "How is everything?"
    mike.say "Good! How about you?"
    show emma sad
    emma.say "Good for me. Honestly I'm a little worried about Samantha, though."
    mike.say "How do you mean?"
    if "samantha_event_B01" in DONE and not samantha.flags.divorced:
        emma.say "I don't think she's happy in her marriage."
        mike.say "Yeah."
        emma.say "What do you know about them?"
        mike.say "Well, Ryan used to be my best friend. He and Samantha and I all shared the house, and then the two of them got together."
        mike.say "But...Ryan isn't always the most upright guy."
        emma.say "Do you think he's cheating on her?"
        menu:
            "I know he is" if hero.flags.knows_ryancheats:
                mike.say "He is."
                emma.say "You seem certain of that."
                mike.say "I am."
                emma.say "Oh. Have you told her?"
                if samantha.flags.knows_ryancheats:
                    $ emma.love += 1
                    mike.say "I have."
                    show emma annoyed
                    emma.say "And she's still with him?!"
                    mike.say "She's trying to make the best of it, I guess?"
                    show emma normal
                    emma.say "I don't understand."
                    mike.say "I don't either, really, but...she knows what's going on and she's dealing with it."
                    emma.say "That doesn't sound healthy."
                    mike.say "It may not be."
                else:
                    $ emma.love -= 2
                    mike.say "I...no, I didn't want to hurt her."
                    emma.say "What? But you know her husband is cheating on her, she's getting hurt every second of every day!"
                    mike.say "I, uh, ah. Um."
                    show emma angry
                    emma.say "Some friend you are! You have to tell her!"
                    menu:
                        "I can't!":
                            mike.say "I can't! I know it sounds bad, but every time I try, I see the look on her face and I can't do it."
                        "Okay":
                            mike.say "Okay. You're right. I just have to get over myself and rip the bandage off."
                        "Ryan, Sam and I have an arrangement" if game.flags.sam_ryan_threesome:
                            mike.say "I...um, Ryan, Sam and I have an arrangement."
                            emma.say "What does that mean?"
                            mike.say "It's not my place to say."
                            "Emma's eyebrows go up in shock."
                            emma.say "You mean, the three of you?!"
                            mike.say "It's...not my place to say."
                            emma.say "Oh. Um, oh wow."
                            emma.say "I need some time to process this!"
                            hide emma
                            return
            "I think he is":
                mike.say "I think he is, but...it's hard to be sure."
                show emma angry
                emma.say "Yeah. We should do something about it."
                mike.say "Like what?"
                emma.say "Like tell her!"
                show emma annoyed
                mike.say "I don't know, telling her about suspicions when we're not sure might create more trouble. That wouldn't be helping."
                emma.say "Then...then I guess we need to find out."
                mike.say "I guess? How do we do that?"
                show emma normal
                emma.say "I'll think of something."
            "I don't think so":
                mike.say "I don't think he's cheating on her."
                show emma annoyed
                emma.say "So you think I'm imagining it?"
                mike.say "That's not what I said!"
                emma.say "Then what do you mean?"
                mike.say "That...I just haven't seen anything that makes me say that."
                show emma angry
                emma.say "Well. I think he's cheating on her."
                emma.say "And I think we should tell her."
                mike.say "That sounds like a bad idea without more proof."
                show emma annoyed
                emma.say "Maybe you're right. I guess we need to find out."
                mike.say "I guess? How do we do that?"
                emma.say "I'll think of something."
        emma.say "Wait. Do you think she's cheating on {b}him?{/b}"
        menu:
            "Yeah, she is" if samantha.sexperience > 0:
                mike.say "Yeah, I know she is."
                emma.say "You seem awfully sure."
                mike.say "Yeah, I know 100%%."
                emma.say "Oh. Oh! You?"
                "I shrug."
                $ emma.love -= 2
                show emma annoyed
                emma.say "That's...disappointing."
                mike.say "She knows what she's doing, and Ryan doesn't deserve her."
                emma.say "Yeah, but..."
                "She shakes her head."
                emma.say "I really don't know what to think of you two now. Can I trust you at all?"
                mike.say "What, I'm not a serial cheater or anything."
                emma.say "Do you love her?"
                menu:
                    "Yes":
                        mike.say "Yes, of course I do."
                        $ emma.flags.samgirlfriend = True
                        emma.say "Okay, that's good I guess."
                    "No":
                        mike.say "No, this is just...it helps her. Her marriage sucks, this helps her get through it."
                emma.say "She shouldn't be with him."
                mike.say "That may be true."
            "I don't think so":
                mike.say "I don't think she'd do that. She's not like that."
                emma.say "Yeah, I don't think so either."
    else:
        emma.say "That whole thing with you, and then Ryan. And now you again."
        show emma normal
        emma.say "She doesn't think things through very well, does she?"
        mike.say "She might...have a tendency to leap before she looks, yeah."
        emma.say "You're going to take care of her, right?"
        mike.say "Of course."
        show emma happy
        emma.say "Good. She needs someone strong to guide her. You're a good man, [hero.name]!"
    hide emma
    return

label emma_event_05:
    show emma
    if emma.love.max < 40:
        $ emma.love.max = 40
    emma.say "[hero.name]! I was just thinking about you!"
    mike.say "Oh? Good thoughts, I hope?"
    emma.say "I...um, yeah. Hey, you got time for a quick coffee?"
    mike.say "Sure, that's why I'm here!"
    "Emma and I both buy coffees, and we sit."
    mike.say "So is something up?"
    show emma fear
    emma.say "I, um. I want to. I mean."
    mike.say "Relax, Emma! You seem very flustered. Is everything okay?"
    emma.say "Yes, I mean, everything's fine!"
    "She quickly takes a sip of her coffee."
    mike.say "Okay. Take a deep breath, maybe close your eyes, and just say what it is you want to say?"
    show emma normal
    "Emma does this, wrapping her fingers around her hot cup of coffee and closing her eyes."
    emma.say "Before we met, I, um, you. I mean, I saw you."
    mike.say "Saw me? Like in the park?"
    show emma fear
    "Her eyes widen."
    emma.say "In the park? How'd you know?"
    mike.say "Oh, I saw you too."
    emma.say "What?! How? How could you, no no no that doesn't make any sense."
    mike.say "What doesn't?"
    emma.say "How could you see me? You didn't know me!"
    mike.say "You didn't know me either, Emma."
    show emma annoyed
    emma.say "I know, but. I mean I kind of did."
    mike.say "Now you're confusing me."
    emma.say "I know. I'm sorry, I'm flu--look this is weird, but."
    show emma normal
    "Emma's squeezes her eyes shut, and her speaking pace quickens."
    emma.say "I'm trying to say I dreamed about you. Before we met. I know it's weird and maybe I'm crazy. I hope you don't think I'm crazy?"
    "I don't immediately have an answer, because I'm too stunned by this. She dreamed about me too?"
    show emma sad
    "Her eyes open back up, and she looks deflated."
    emma.say "You do think I'm crazy, don't you?"
    mike.say "No! No! Not at all, not even a little bit."
    emma.say "Oh. You will when I tell you...what kind of dream."
    mike.say "I...it was a sex dream."
    show emma normal
    emma.say "How? I mean was it that obvious?"
    mike.say "Did it involve, um. Me behind you? Holding onto you with...um."
    emma.say "...a leash. What...how did you?"
    mike.say "Yeah. I had that same dream."
    show emma fear
    emma.say "Impossible!"
    mike.say "I know! It should be impossible!"
    show emma normal
    "She looks down at her coffee, staring at it as though it were the most important thing in the world just now."
    emma.say "What does this mean?"
    mike.say "I don't know. Fate? Destiny?"
    if emma.flags.samgirlfriend:
        show emma sad
        emma.say "But...you're with my best friend! That's...is fate really that awful to people?"
        emma.say "Sam deserves better than that."
    else:
        emma.say "I've never really believed in anything like that. I can't believe in that. How awful would that be if...Krissa."
    mike.say "I don't know. I've never really thought about it at all. I guess...maybe it doesn't mean anything. Maybe it means something."
    show emma normal
    emma.say "How will we know?"
    mike.say "I don't know. I guess we'll have to think about it and see."
    "She nods and then finishes her coffee."
    emma.say "Let me think about it."
    mike.say "Just don't...overthink it, okay?"
    emma.say "Sure, yeah. I'll do my best."
    return

label emma_event_06:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Emma")
    if not result:
        $ hero.cancel_event()
        $ emma.love -= 5
        return
    if emma.love.max < 50:
        $ emma.love.max = 50
    emma.say "Hi, [hero.name]!"
    mike.say "Heya!"
    if not emma.flags.huntmissed:
        emma.say "I have a weird question for you."
        mike.say "Another one?"
        emma.say "It probably won't be the only one. Anyway, I got this cool scavenger hunt app, and I want to do it but I don't think I want to do it alone."
        mike.say "What is it?"
        emma.say "It's an app with some clues and you go around town and find the items. If you get a high enough score you get a prize, though it's just a free cup of coffee."
        emma.say "But the prize isn't the point. Do you think that sounds like fun?"
        emma.say "Will you go with me?"
    else:
        emma.say "You didn't show for the scavenger hunt, but I thought maybe you'd like to try again?"
    menu:
        "Not interested":
            mike.say "Sorry, Emma. That doesn't sound very interesting."
            emma.say "Oh. I--I'm sorry, I thought it would...never mind me I'm just being silly."
            "And then she disconnects."
            return
        "Sure!":
            pass

    mike.say "Sure, that sounds like fun!"
    emma.say "When are you free?"
    $ renpy.dynamic("day", "week_day")
    $ day, week_day = day_chooser()
    $ hero.calendar.add(day, ScavengerHuntAppointment(16, "emma", "emma_event_06", name="Scavenger hunt (Emma)", fail_label="emma_event_06_missed"))
    emma.say "Great! I look forward to it!"
    return

label emma_event_06_start:
    scene bg coffeeshop
    show emma happy
    emma.say "Hi [hero.name]! So glad you could make it!"
    mike.say "Sure! Okay so how does this work?"
    emma.say "There are three clues to an item, somewhere in the city. We'll get the clue, decide where to go, and tap the guess button on my phone here."
    emma.say "If we're in the right location, then we just have to guess the item."
    show emma normal
    if Room.find("electronic").hidden:
        call emma_event_06_canceled from _call_emma_event_06_canceled
        $ date.stay = False
        return
    emma.say "BUT! We only get three chances. And the fewer tries we use, the higher our score."
    mike.say "What does the score mean?"
    emma.say "I think it's just a leaderboard with other people playing the app. See, it says here that someone named Nut Buster 2167 is in the lead with 97 points."
    mike.say "Okay. So I guess what's the first clue?"
    return

label emma_event_06_clue_1:
    show emma
    emma.say "What has keys but unlocks nothing?"
    mike.say "What is that supposed to mean?"
    emma.say "No idea. Where should we go?"
    hide emma
    return

label emma_event_06_guess_1:
    if game.room != "electronic":


        return False
    emma.say "Yes, this is the right place! Now what could it be?"
    menu:
        "Telephone" if not "telephone" in game.active_date.tried:
            $ game.active_date.tried.add("telephone")
            return False
        "Speaker" if not "speaker" in game.active_date.tried:
            $ game.active_date.tried.add("speaker")
            return False
        "Game console" if not "gameconsole" in game.active_date.tried:
            $ game.active_date.tried.add("gameconsole")
            return False
        "Computer":
            return True
        "Television" if not "tv" in game.active_date.tried:
            $ game.active_date.tried.add("tv")
            return False
        "Sim card" if not "simcard" in game.active_date.tried:
            $ game.active_date.tried.add("simcard")
            return False

label emma_event_06_clue_2:
    show emma
    emma.say "It sits high glowing and watches the world go by, without it everything would seem dark and dangerous."
    mike.say "What watches the world go by?"
    emma.say "I don't know. Maybe a reference to mythology? I'm not sure."
    hide emma
    return

label emma_event_06_guess_2:
    if game.room != "park":
        return False
    emma.say "Yes, this is the right place! Now what could it be?"
    menu:
        "Lamp":
            return True
        "Bench" if not "Bench" in game.active_date.tried:
            $ game.active_date.tried.add("Bench")
            return False
        "Cobblestone" if not "Cobblestone" in game.active_date.tried:
            $ game.active_date.tried.add("Cobblestone")
            return False
        "Tree" if not "Tree" in game.active_date.tried:
            $ game.active_date.tried.add("Tree")
            return False
        "Office window" if not "Office window" in game.active_date.tried:
            $ game.active_date.tried.add("Office window")
            return False

label emma_event_06_clue_3:
    show emma
    emma.say "Elegant in public, a sign of power. Constricting in private, a sign of submission."
    mike.say "Right. No idea what that means."
    show emma annoyed
    emma.say "It sounds kind of dirty."
    hide emma
    return

label emma_event_06_guess_3:
    if game.room != "sexshop":
        return False
    emma.say "Yes, this is the right place! Now what could it be?"
    menu:
        "Dildo" if not "Dildo" in game.active_date.tried:
            $ game.active_date.tried.add("Dildo")
            return False
        "Vibrator" if not "Vibrator" in game.active_date.tried:
            $ game.active_date.tried.add("Vibrator")
            return False
        "Rope" if not "Rope" in game.active_date.tried:
            $ game.active_date.tried.add("Rope")
            return False
        "Whip" if not "Whip" in game.active_date.tried:
            $ game.active_date.tried.add("Whip")
            return False
        "Lingerie" if not "Lingerie" in game.active_date.tried:
            $ game.active_date.tried.add("Lingerie")
            return False
        "Collar":
            return True
        "Butt plug" if not "Butt plug" in game.active_date.tried:
            $ game.active_date.tried.add("Butt plug")
            return False

label emma_event_06_finish:
    if emma.love.max < 60:
        $ emma.love.max = 60
    scene bg street
    $ DONE["emma_event_06_finish"] = game.days_played
    show emma
    if game.active_date.total < 30:
        emma.say "Well, we didn't do very well, but I had a good time!"
        mike.say "Me too."
        emma.say "Do you want to do another one of these sometime?"
        mike.say "Um, not really."
        show emma happy
        "Emma laughs."
        emma.say "Me either!"
        mike.say "Something else then?"
        emma.say "Sure!"
    elif game.active_date.total < 70:
        emma.say "I'd say we did okay, though maybe not great."
        mike.say "Yeah, we could use some work on this."
        emma.say "Think we should try it again?"
        mike.say "Maybe!"
    else:
        show emma happy
        emma.say "Wow, [hero.name]! We kicked butt at that! I should say you kicked butt at that, all the good ideas were yours!"
        mike.say "Oh nonsense, you helped!"
        emma.say "As if! It was all you!"
        mike.say "You're sweet, but that's not true! It was a team effort. {b}We{/b} won!"
        if game.active_date.score >= 100:
            "Without warning, Emma practically throws herself at me."
            hide emma
            show emma kiss casual
            $ emma.flags.kiss += 1
            "As a kiss, it's more like a tight hug with lips involved."
            "Emma presses herself against me, creating contact entirely up the length of our bodies."
            "And then as quickly as she started it, she pushes herself away."
            hide emma kiss casual
            show emma blush ahoge
            emma.say "Oh! Oh my gosh, I'm so--I'm so sorry that--I didn't mean--I shouldn't! Augh!"
            mike.say "No! It's okay!"
            if emma.flags.samgirlfriend:
                emma.say "No! No it's not! I'd never do that to a friend like Samantha! I'm a horrible, awful person!"
                mike.say "You are none of those things. Maybe you're a little impulsive. It's okay! I forgive you."
                emma.say "{b}You're{/b} not the one that has to forgive me. It's Samantha!"
                emma.say "I have to tell her...right away!"
            else:
                emma.say "No, I mean, I um. Crap, I wasn't...I don't want, I mean, I'm not...not ready! I don't!"
                emma.say "I'm sorry, I always get so flustered when I...please, I have to go!"
            "And without waiting for me to respond, she runs off."
            "Well, this should be interesting!"
    hide emma
    $ game.room = "street"
    return

label emma_event_06_missed:
    "Shit, I missed the scavenger hunt with Emma!"
    $ emma.love -= 20
    $ DONE.pop("emma_event_06", None)
    $ emma.flags.huntmissed += 1
    return

label emma_event_06_canceled:
    mike.say "Sorry Emma, I don't have access to all locations. We'll have to postpone."
    $ DONE.pop("emma_event_06", None)
    return

label emma_event_07:
    show emma
    $ emma.flags.nodrink = False
    if emma.love.max < 80:
        $ emma.love.max = 80
    mike.say "Emma, would you like a drink?"
    emma.say "I do--you know maybe I will."
    mike.say "What do you drink?"
    show emma annoyed
    emma.say "Oh geez, I don't know."
    mike.say "Let's go with something mild and...hm. Do you prefer mint or pineapple?"
    show emma normal
    emma.say "Oh, I think pineapple."
    mike.say "Great! Bartender, get this young woman a Malibu! Go a little easy on the rum, okay?"
    "After a moment, the bartender delivers Emma's red-and-yellow drink."
    "She eyes it dubiously, but she takes a taste."
    emma.say "Huh, this isn't bad. I thought it'd be more...I don't know. Harsh?"
    mike.say "It's mostly fruit juice, really. There's a bit of rum still though so, you know, go slow."
    show emma happy
    "Emma smiles at me."
    emma.say "You're so thoughtful!"
    mike.say "I try."
    show emma normal
    "Emma takes another sip or two of her drink, and she definitely seems to like it."
    emma.say "You know, [hero.name], I've been thinking about you a lot lately."
    mike.say "Oh yeah? Should I be flattered or worried?"
    show emma happy
    emma.say "Let's go with flattered."
    mike.say "Should I be {b}really{/b} flattered?"
    show emma blush
    emma.say "Oh! I, um. I mean kind of, yes it was...I mean the dreams. I can't get them out of my head!"
    mike.say "Yeah, me either."
    show emma normal
    emma.say "So you know, I've been wondering if they mean something. Like fate. Or destiny. Or if they're just some weird random coincidence."
    menu:
        "I don't believe in fate":
            mike.say "I don't believe in fate, or destiny. We make our own fates. We're strong people and we make our marks on the world."
            $ emma.love -= 3
            emma.say "Sure, but there's so many...outside factors we can't control. Yeah you're good at your job, but what if your boss was miserable and hated you?"
            mike.say "I guess I'd find a new job?"
            emma.say "That easy, huh?"
            mike.say "I guess, no, maybe not quite that easy."
        "I don't believe in coincidence":
            mike.say "I don't believe in coincidence. Somehow, some way, it has to be connected. It has to mean something."
            mike.say "I don't want to live in a world where there isn't any meaning."
            $ emma.love += 3
            show emma happy ahoge
            emma.say "I don't either! There's so much more to this world than we can ever understand."
            emma.say "What if it touched us?"
            mike.say "I don't know. There's no way to know!"
            $ emma.flags.believesfate = True
    show emma normal
    emma.say "So I had an idea about the dreams. What if we could test it?"
    mike.say "Test it how?"
    emma.say "What if we slept w--well, near each other. Like, maybe just a room apart."
    mike.say "Huh. You think that would show anything? I mean, what if nothing happens?"
    emma.say "If nothing happens then it was probably just coincidence. I mean, think about it."
    emma.say "If we go to sleep at the same time, thinking about each other, then maybe, just maybe..."
    mike.say "And what if I have a...really nice dream about you because you're close and you're attractive and I'm thinking about. You know, that!"
    show emma blush ahoge
    emma.say "But it only counts if we have the same dream again!"
    mike.say "Oh, I see. I mean, it would be pretty unlikely that we'd have the same dream by chance."
    emma.say "Right?"
    mike.say "But what if nothing happens?"
    show emma normal
    emma.say "Then I guess nothing happens and it didn't mean anything, and we're just two people with big dreams."
    mike.say "Okay, I'm game, I guess. When and where?"
    emma.say "It'd have to be a weekend, I have to get up and go to school right away and I'd rather not try to teach kids like...that."
    mike.say "Okay. So Saturday, then?"
    emma.say "Sure. I'll call you!"
    mike.say "It's a date!"
    show emma blush
    if emma.flags.samgirlfriend:
        emma.say "No! Not a date! I would never do that to Samantha!"
    else:
        emma.say "No! Not a date!"
    emma.say "It's...just a sleepover!"
    "I can't help but laugh. Honestly she's so cute when she gets a little flustered."
    mike.say "Okay, a sleepover, then. I'll wait for your call!"
    hide emma
    return

label emma_event_08:
    if emma.love.max < 100:
        $ emma.love.max = 100
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Emma")
    if not result:
        $ hero.cancel_event()
        $ emma.love -= 5
        return
    mike.say "Hey, Emma!"
    emma.say "Hi, [hero.name]!"
    mike.say "Is it time for that sleepover we talked about?"
    emma.say "Yeah! Sorry it took me awhile to work myself up to it. Is that weird?"
    mike.say "Honestly? Maybe a little, but it's also adorable."
    "I swear I can hear her blushing through the phone."
    emma.say "So um anyway, should I come over?"
    mike.say "Yes!"
    emma.say "I'll be there shortly!"
    scene bg black with timelaps
    $ game.pass_time(1, needs=True)
    scene bg livingroom
    show emma casual blazer hat
    with timelaps
    "When Emma arrives, it's clear from her general demeanor that she's nervous, and understandably so."
    emma.say "Hi, [hero.name]!"
    mike.say "Do you want me to take your coat?"
    emma.say "Oh yes, I guess I don't need this in here!"
    "I take Emma's hat and coat and set them safely aside."
    show emma casual -blazer -hat with dissolve
    "I try to put her at ease with a little friendly banter."
    mike.say "I haven't done anything like this since middle school. So what should we do?"
    emma.say "Well, I'm not really ready to go to sleep just yet."
    mike.say "I imagine making out on the couch is out of the question."
    show emma blush
    if emma.flags.samgirlfriend:
        emma.say "That's--no that's not what this is! Sam would kill me!"
    else:
        emma.say "Ugh, I just want to have--no!"
    "I laugh, good-naturedly."
    mike.say "I'm just kidding! It's okay, this is just two friends, trying an experiment."
    mike.say "How about this. Are you hungry?"
    emma.say "Yeah, I haven't actually had dinner yet."
    if hero.has_skill("cooking"):
        mike.say "I'm pretty decent in the kitchen. How about I whip something up?"
        emma.say "Um, sure, I guess that sounds good!"
        $ game.room = "kitchen"
        scene bg kitchen
        show emma casual
        with fade
        mike.say "Let's see what's in the refrigerator. Oh! I've got some chicken. Do you like garlic?"
        emma.say "Oh I guess maybe, but it can be a bit strong."
        mike.say "This dish gives it a nice braise, so there's a lot of it but it gets really mild. You can spread it on the bread like butter."
        emma.say "That sounds interesting, I've never had it."
        "I set about to work while Emma watches, first browning the chicken in a pan, then adding a whole lot of peeled garlic and some oil."
        "The whole thing goes into the oven."
        show emma happy
        emma.say "That looked a lot easier than it sounded like it was going to be."
        mike.say "Oh yeah, this one isn't hard, it's just peeling all the garlic that's annoying."
        show emma annoyed
        emma.say "Huh. When I cook it's all really simple stuff. Lots of pasta and rice. I don't eat a lot of meat, actually."
        mike.say "As long as you get your vegetables!"
        show emma normal
        "After a short while, the dish is ready to come out of the oven. I separate it into two plates, serve it with some mashed potatoes and vegetables."
        show emma ahoge
        "When Emma takes a bit, her eyes grow wide."
        emma.say "This is delicious! It's like eating at a fancy restaurant!"
        mike.say "Oh, I wish I were that good of a chef! But thank you anyway."
        emma.say "Oh, don't be modest, this is amazing!"
        $ emma.love += 3
        "We eat, and I notice that we're both carefully not discussing the dreams. I think she's just not ready for that."
        "When we're done, we go back to the living room."
        $ game.room = "livingroom"
        scene bg black with timelaps
        scene bg livingroom
        show emma casual normal at center
        with timelaps
    else:
        mike.say "I'm not much of a cook, unfortunately. Maybe we can order pizza?"
        show emma happy
        emma.say "Sure, I like pizza."
        mike.say "What do you like on yours?"
        show emma normal
        emma.say "Olives, mushrooms and artichoke hearts are my favorite."
        mike.say "Oh! I'm kind of a pepperoni lover. Maybe we can get one half-and-half?"
        emma.say "That sounds good. And I'll try a bite of yours if you try a bite of mine?"
        mike.say "I, uh. Well okay, sure, I'll give it a try. Why not!"
        "I put in an order for the pizza. I make a little small talk while we wait for it to arrive."
        mike.say "So, how's work? Everything good with the kids?"
        emma.say "Oh! Well, you know, um. Kids are...I mean some of them are amazing little things, watching them learn and soak up what you have to say."
        emma.say "They see everything even if you think they don't, and it's amazing to watch a child figure something out."
        emma.say "But some of them just don't care. I wish I knew what to with those kids. But what can you do?"
        mike.say "Mm, yeah. I guess a long time ago people tried to beat sense into them, but we don't do that anymore."
        emma.say "It doesn't really work, it just makes kids who're scared of you. And then they grow up thinking they have to beat on others to get what they want."
        mike.say "Huh, I never thought of it that--"
        play sound door_bell
        "I'm interrupted by the doorbell. Pizza's here!"
        "When it arrives, Emma and I both take our respective pieces and munch away."
        scene bg black with timelaps
        scene bg livingroom
        show emma casual normal at center
        with timelaps
    $ hero.hunger += 8
    $ game.pass_time(1, needs=True)
    if bree.hidden:
        mike.say "So. Emma, do you maybe want to watch a movie?"
        emma.say "Sure! That'll be just about perfect."
        "We sit on the couch together, and turn on the TV."
        emma.say "Do you have any anime?"
        mike.say "I think we've got a few. What do you like?"
        emma.say "My favorite is probably {i}No need for Benji{/i}!"
        mike.say "You're in luck, we've got the whole series!"
        show emma happy
        "I start up the TV, and we sit on the couch."
        "While we watch, Emma scoots closer to me, and eventually is practically leaning against me. After a little while, I put my arm around her shoulder."
        show emma blush
        emma.say "I hope it's okay. I like to, you know. Sit right next to people. I like the warmth!"
        mike.say "It's great, Emma!"
        scene bg black with timelaps
        $ game.pass_time(2, needs=True)
        scene bg livingroom
        show emma casual
        with timelaps
        "We watch the next two episodes in silence, cuddling on the couch. While the credits are rolling, Emma yawns and stretches, pulling a little away from me."
        emma.say "I think...I think I'm ready to try to go to sleep now."
        mike.say "That sounds good."
        emma.say "Am I sleeping on the couch?"
        mike.say "Yeah, that'll work."
        mike.say "Let me get you a blanket and a pillow."
        scene bg bedroom1 with fade
        $ game.room = "bedroom1"
    else:
        show emma casual at left5
        show bree at right5
        with moveinright
        bree.say "Hi, [hero.name]! Who's this?"
        mike.say "Oh! Emma, this is my roommate [bree.name]. [bree.name], this is Emma!"
        bree.say "Oh. Is this a date or something?"
        mike.say "Oh no! She's going to sleep on the couch tonight. This is just a...we're testing something."
        bree.say "Testing what?"
        mike.say "Oh just, um. It's weird and I don't think I can explain it right now."
        if bree.love > 120 or bree.sexperience > 3:
            bree.say "Okay well I'm glad it's not a date, or I'd be really jealous!"
            mike.say "Relax! We're just friends, right Emma?"
            emma.say "That's right. Just friends!"
        mike.say "So. Emma, do you maybe want to watch a movie?"
        emma.say "Sure! That'll be just about perfect."
        "We sit on the couch together, and turn on the TV."
        emma.say "Do you have any anime?"
        show bree happy
        bree.say "Oh! Yeah we've got a few. What do you like?"
        emma.say "My favorite is probably {i}No need for Benji{/i}!"
        bree.say "You're in luck, we've got the whole series!"
        show emma happy
        emma.say "Yes! I can see we're going to get along just fine!"
        "[bree.name] starts up the TV, and all three of us sit on the couch, with me between the two girls."
        "While we watch, Emma scoots closer to me, and eventually is practically leaning against me. After a little while, I put my arm around her shoulder."
        show emma blush
        emma.say "I hope it's okay. I like to, you know. Sit right next to people. I like the warmth!"
        mike.say "It's great, Emma!"
        if bree.love > 120:
            show bree happy
            "[bree.name] laughs at that."
            bree.say "Oh! Can I get some of those snuggles too?"
            emma.say "Let's have a [hero.name] pile!"
            "And then the two of them both squish into me."
        scene bg black with timelaps
        $ game.pass_time(2, needs=True)
        scene bg livingroom
        show emma casual at left5
        show bree at right5
        with timelaps
        "We watch the next two episodes in silence, cuddling on the couch. While the credits are rolling, Emma yawns and stretches, pulling a little away from me."
        emma.say "I think...I think I'm ready to try to go to sleep now."
        mike.say "That sounds good."
        emma.say "Am I sleeping on the couch?"
        mike.say "Yeah, that'll work."
        bree.say "Let me get you a blanket and a pillow."
        "[bree.name] looks at me. You. Go. I've got this."
        mike.say "Yes, ma'am!"
        scene bg bedroom1 with fade
        $ game.room = "bedroom1"
        "Off in my bedroom, while I get ready for bed, I can hear the two girls giggle from time to time."
        "I can't decide if it's a good thing or not that [bree.name] and Emma immediately started getting along. But they seem happy."
    "I lay down and try to go to sleep. My mind whirls, thinking about the dreams we've had together. Will there be another one tonight?"
    "And it takes awhile. But eventually I do fall asleep."
    scene bg bedroom1 at blur(16), dark, dark with dissolve
    "To sleep, perchance to dream."
    "Where am I? Am I on a beach?"
    "I open my eyes and all I see is pale flesh and a beautiful pussy with soft, fuzzy brown pubic hair all over it."
    show emma lick pleasure with fade
    $ emma.flags.loose += 1
    "Her legs are spread wide for me, and her vulva is wide open. I can see her clit. I put one finger between her labia, and I can hear her sharp intake of breath."
    "I move that finger up, then down, and that breath releases with a high pitched, squeal, like a balloon that's just let the air out."
    emma.say "Oh, [hero.name]!"
    "She puts her hand on the back of my head and pulls me toward her. My face dives in and I don't think, I just act."
    "I use my tongue, I use my fingers. She responds to everything, breathing faster with every touch, moaning aloud."
    "After what seems like both forever and at the same time only seconds, she has a powerful orgasm right in my face."
    "Her thighs clench me tightly, squeezing my cheeks. I can't move without hurting her, so I don't."
    "I just let her hips buck against my face, relishing the sweet, sweet orgasm she's having."
    "After a few moments it subsides, and everything about her relaxes."
    "I pull myself up, moving up to look down at her."
    "She smiles at me and opens her mouth."
    emma.say "[hero.name]?"
    "Her voice is almost lethargic, that tone you get when you're drifting away on a cloud after perfect sex."
    mike.say "Yes, my love?"
    "And then her face goes impish."
    emma.say "Wake up!"
    hide emma lick
    call sleep from _emma_event_08
    scene bg bedroom1
    with dissolve
    "I wake up with a jolt, suddenly back in my bedroom."
    "I have the biggest, hardest boner I think I've ever had in my life."
    "It won't go down, either, and I can't very well go out into the rest of the house with that. So I have to jerk it off."
    "It doesn't take long, though, and the sweet, sweet release is like heaven."
    "When I'm done, I quickly get dressed. And then I run out to the living room."
    scene bg livingroom
    $ game.room = "livingroom"
    "But she's gone!"
    "Well. Now what?"
    $ emma.flags.delay = TemporaryFlag(True, 1)
    return

label emma_event_09:
    show emma happy
    emma.say "Hi, [hero.name]!"
    "I expected Emma to be upset or weird after disappearing, but she seems cheerful and happy to see me."
    mike.say "Hi, Emma. Is everything okay?"
    emma.say "Sure, everything's fine. Why wouldn't it be?"
    mike.say "Well, when I woke up, you were already gone."
    show emma normal
    emma.say "Oh! I'm sorry! I'm kind of an early riser, and I didn't want to wake you. So I got up and then I went for a bit of a walk."
    mike.say "I see."
    show emma annoyed
    emma.say "I needed to...clear my head."
    mike.say "Yeah?"
    emma.say "So...did you have any, um. Dreams?"
    menu:
        "Admit it":
            mike.say "Yeah, I had one heck of a dream."
            show emma blush
            emma.say "Did it involve...you know. Um. Down...there?"
            mike.say "Yes!"
            emma.say "Oh my God. So it's...I mean did you, um. What did you do?"
            mike.say "I was going down on you, and you squirted all over my face. It was--"
            show emma blush ahoge
            "Emma was already blushing, but somehow the shade of red on her cheeks got even brighter!"
            emma.say "Stop talking about it! I get the idea!"
            mike.say "Okay, fine."
            emma.say "You seem pretty, um. Blasé about the whole thing."
            mike.say "Well, it's just a dream, right?"
            emma.say "Oh. Do you have a lot of, um. Dreams like that?"
            mike.say "Sure, though I prefer the real thing!"
            if emma.flags.samgirlfriend:
                emma.say "I hope you mean with Sam!"
            else:
                emma.say "Oh! I, um!"
            emma.say "I guess you've, um. Done that kind of thing a lot?"
            mike.say "I guess, sure!"
            show emma normal
            emma.say "So what do you think it means?"
            if emma.flags.believesfate:
                mike.say "I don't know. I guess it's fate! Or destiny? Something is telling us something."
            else:
                mike.say "I don't know. We're two attractive people who are drawn to each other and our libidos tell us at night."
            call emma_event_09_do_what from _emma_event_09_admit
        "Lie and say no":
            mike.say "No, I didn't have any dreams. Did you?"
            show emma sad
            "The look of disappointment on Emma's face is absolutely palpable."
            emma.say "Oh. Um. No I didn't either, really."
            "She's lying, it's completely transparent. She's also upset."
            menu:
                "Relent":
                    mike.say "I...okay look I didn't really want to admit this, but I did, actually. Have a dream about you."
                    emma.say "What kind of dream?"
                    mike.say "A very, very naughty dream."
                    show emma blush
                    emma.say "Oh!"
                    mike.say "I guess you had one too?"
                    emma.say "I, um. I might...maybe, kind of."
                    mike.say "It's okay."
                    emma.say "Why did you say you didn't, then?"
                    mike.say "I, uh. It's kind of embarrassing to tell someone you had a dream so naughty that you had a giant orgasm in bed, I guess."
                    show emma blush ahoge
                    emma.say "Oh! Oh um. I guess I see what you mean."
                    call emma_event_09_do_what from _emma_event_09_lie
                "It's better this way":
                    mike.say "Look, it's better this way, right? We know the dreams were just a weird coincidence."
                    mike.say "None of it means anything. We can just be friends."
                    "Emma nods, her expression a little bit numb, like she's having trouble focusing on me or really anything."
                    emma.say "Um. Yeah. I guess you're right."
    $ emma.unhide()
    hide emma
    return

label emma_event_09_do_what:
    emma.say "But um...what should we do about it?"
    menu:
        "We should explore it":
            if emma.love.max < 120:
                $ emma.love.max = 120
            mike.say "We should explore it, and see where it goes."
            if emma.flags.samgirlfriend:
                show emma angry
                emma.say "We can't! You're with Sam! I could never hurt her."
                mike.say "What if I wasn't?"
                emma.say "If you hurt her, so help me, fate or destiny or whatever, I will never forgive you."
                mike.say "I like that about you. Don't worry."
                $ emma.flags.talktosam = True
            else:
                emma.say "I guess we could, maybe. A little. One step at a time, right? Take it slow and see what, um. What happens, I guess?"
                mike.say "Okay!"
                $ emma.flags.nodate = False
                $ emma.flags.nokiss = False
        "Nothing":
            mike.say "Look, we shouldn't do anything about it."
            show emma sad
            "Emma looks disappointed, but at the same time, almost kind of relieved."
            emma.say "Yeah, I guess you're right. We really should just...pretend this never happened."
            mike.say "It's a deal."
    return

label emma_event_09_sam:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Samantha")
    if not result:
        $ hero.cancel_event()
        $ samantha.love -= 5
        return

    if samantha.flags.nickname == "cupcake":
        mike.say "Hi, Cupcake!"
    else:
        mike.say "Hi, Sam!"
    samantha.say "Hi, [hero.name]. You got a sec to talk?"
    mike.say "Sure, I always have time for you!"
    samantha.say "Yeah, thanks. I guess, I..."
    "Her voice trails off, and for a second I start to think that the call got cut off somehow."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake? You still there?"
    else:
        mike.say "Sam? You still there?"
    samantha.say "Yeah, [hero.name], I'm still here. So, um. I had a nice chat with Emma."
    mike.say "Oh?"
    samantha.say "I..."
    if samantha.is_girlfriend:
        samantha.say "Do you love me?"
        "The tone of her voice is incredibly insecure. She's upset. And she needs reassurance. Of course, there could be an opportunity to get something going with Emma here, too."
        menu:
            "Of course":
                mike.say "Of course I do!"
                samantha.say "You do? Because...I just...I mean, you and Emma."
            "I don't, really":
                if samantha.flags.nickname == "cupcake":
                    mike.say "Cupcake, I...I'm sorry, but I don't think I do."
                else:
                    mike.say "Sam, I...I'm sorry, but I don't think I do."
                "Sam bursts into tears on the other side of the phone."
                if samantha.flags.nickname == "cupcake":
                    mike.say "Hey! Cupcake, don't do that!"
                else:
                    mike.say "Hey! Sam, don't do that!"
                samantha.say "Fuck you, [hero.name]! And stupid Emma and your stupid roommates and all of you!"
                samantha.say "I never want to see you again!"
                $ samantha.breakup()
                "And then the connection drops."
                return
    else:
        samantha.say "Look, I know that I sprang that boyfriend thing on you, and you didn't actually agree to it."
        mike.say "I guess...is that what this is about?"
        samantha.say "I just want clarity about you and me. Especially with what's going on between you and Emma."
    mike.say "What do you think is between me and Emma?"
    samantha.say "She's clearly in love with you."
    "I take a deep breath before answering that."
    mike.say "Look, yes. There's this weird connection with us."
    samantha.say "I see."
    mike.say "No, you don't, it's not what you think."
    samantha.say "Uh huh."
    mike.say "Seriously! Okay look, when you introduced me to Emma, I already kind of knew her. Except I didn't. Because I'd had multiple dreams about her."
    mike.say "Except I'd never seen her before in my life."
    mike.say "And then I found out she also was dreaming about me, but had never seen me before either."
    mike.say "So we decided to test it. And we had the same dream. About each other."
    mike.say "I don't know what it means!"
    samantha.say "Yeah. That's what she told me, too."
    mike.say "So."
    samantha.say "Are you in love with her?"
    mike.say "I don't know! I don't think so. I mean, I barely know her. We've chatted a bit, and watched some anime together, and it was fun."
    samantha.say "Do you need me to...get out of the way?"
    menu:
        "No!":
            mike.say "No, absolutely not. This isn't about you and me."
            samantha.say "But it's going to get in the way of us."
            "I let out a long sigh. It's not like she's wrong."
            mike.say "What do {b}you{/b} want to do?"
            samantha.say "I want to eat a pound of chocolate and cry myself to sleep."
            mike.say "What? No! That's not okay!"
            "Now it's her turn to let out a long sigh."
            if samantha.is_girlfriend:
                samantha.say "I don't want to lose you."
                mike.say "You won't."
                samantha.say "But Emma's a sweet girl, too."
                mike.say "She is."
            else:
                samantha.say "I guess I was wrong about us."
                mike.say "No!"
                samantha.say "Then why didn't you agree I was your girlfriend?"
                mike.say "You took me by surprise!"
                samantha.say "I gave you time to think about it, but you still haven't said it."
                mike.say "Hey, I've just been a little scared, that's all."
                samantha.say "Mmm."
                mike.say "I'm ready to say it now."
                samantha.say "Really? Are you sure?"
                mike.say "Yes."
                samantha.say "But what about Emma?"
                mike.say "I honestly don't know."
            samantha.say "Let's talk more about this. Meet us both tomorrow in the bakery. Say around 14:00?"
            mike.say "Sure. I'll be there."
            $ hero.calendar.add(game.days_played + 1, LabelAppointment((14, 18), ["emma", "samantha"], "Meet with Sam and Emma", "emma_event_09_appointment", "emma_event_09_appointment_missed"))
            samantha.say "Ok."
            "There's a brief pause."
            samantha.say "Ok, bye."
            $ emma.flags.event09 = "appointment"
        "I want to explore with Emma":
            if samantha.flags.nickname == "cupcake":
                mike.say "I...I hate to say this, Cupcake, but I want to explore this more with her. I can't ignore it."
            else:
                mike.say "I...I hate to say this, Sam, but I want to explore this more with her. I can't ignore it."
            samantha.say "I see."
            mike.say "I don't want to hurt you."
            if samantha.is_girlfriend:
                samantha.say "But you did."
                if samantha.flags.nickname == "cupcake":
                    mike.say "I...I'm sorry, Cupcake. I didn't mean to."
                else:
                    mike.say "I...I'm sorry, Sam. I didn't mean to."
                samantha.say "So am I."
                $ emma.flags.samok = False
            else:
                samantha.say "That must be why you didn't...we didn't..."
                mike.say "Maybe it was some kind of destiny?"
                samantha.say "Do you believe in fate?"
                mike.say "Before, I would've said no. But now? I'm seriously thinking about it."
                samantha.say "Mmm."
                mike.say "Look. What do {b}you{/b} want?"
                "Sam lets out a long, defeated sigh."
                samantha.say "I just want you to be happy, [hero.name]. I guess that isn't with me."
                "Oof."
                samantha.say "I...I'll tell her. I'll make sure it's okay."
                $ emma.flags.samok = True
                samantha.say "I'll see you around, right?"
                mike.say "Absolutely."
                samantha.say "Ok. Okay. Take care of yourself."
            $ emma.flags.event09 = "emma"
            $ samantha.breakup()
    "And then she disconnects."
    return

label emma_event_09_betrayed:
    show emma angry
    "Emma comes up to me -- no, {b}stomps{/b} up to me with murder in her eyes."
    emma.say "{b}What{/b} did you do to Sam?"
    mike.say "What do you mean?"
    emma.say "Don't play games with me!"
    mike.say "I...well, I guess I wanted to have a chance to explore what we have--"
    emma.say "You dumped her! You dumped her for me?! I fucking told you that if you hurt her I'd never forgive you!"
    mike.say "Emma! I just--"
    emma.say "Fuck off, [hero.name]! I wasn't kidding about that."
    "She turns and storms away. I may have nightmares about that encounter for awhile."
    $ emma.set_gone_forever()
    hide emma
    return

label emma_event_09_okayed:
    show emma angry
    "Emma comes up to me -- no, {b}stomps{/b} up to me with murder in her eyes."
    emma.say "{b}What{/b} did you do to Sam?"
    mike.say "What do you mean?"
    emma.say "Don't play games with me!"
    mike.say "I didn't do anything! We had a talk about the two of us."
    "Her eyes narrow, but her expression softens a bit."
    emma.say "You didn't dump her?"
    mike.say "Did she tell you I dumped her?!"
    emma.say "No, but...she was upset and trying to hide it."
    mike.say "Yeah. We decided together it wasn't going to work out."
    show emma annoyed
    emma.say "You did? Why? Was it me?"
    mike.say "No! It wasn't going to work out. Whether or not you were involved."
    "Emma scowls a little bit, then relaxes."
    show emma normal
    emma.say "I...damn it, I should have trusted her."
    mike.say "What do you mean?"
    emma.say "I really thought she was lying when she said she dumped you."
    mike.say "Well, you're not entirely wrong. It was more mutual than her."
    emma.say "What do you mean?"
    mike.say "Okay, look. When she introduced me as her boyfriend, that was her assuming. It wasn't actually true, we hadn't talked about it, and...we talked about it afterward and I was uncomfortable."
    mike.say "I had to think about it for a long time, and I just...I wasn't sure it was right."
    mike.say "And when she figured that out, she was mad. But, see, that happened before we had any idea what was going on between us. This was going to happen whether you were here or not."
    emma.say "I see."
    mike.say "And it would've been much worse if I'd agreed with her and then changed my mind. So I waited, and...it just wasn't there."
    emma.say "I guess. I mean. I guess I owe you both an apology."
    mike.say "Never. You're doing your best to be an amazing, caring and loving friend. I couldn't ask for more."
    emma.say "Really?"
    mike.say "Really."
    emma.say "Okay. I guess...I think...I mean yeah, I guess everything's okay then."
    $ emma.flags.samresolved = True
    $ emma.flags.nodate = False
    $ emma.flags.nokiss = False
    $ emma.flags.samgirlfriend = False
    hide emma
    return

label emma_event_09_appointment(appointment=None):
    scene bg coffeeshop
    show samantha normal casual at left5
    show emma normal casual blazer at right5
    samantha.say "Hi, [hero.name]! Glad you made it!"
    mike.say "Of course! Anything for you."
    "Emma waves, almost shyly, while Sam and I chat."
    if samantha.is_girlfriend:
        samantha.say "So, my love, what do we want to do about this Emma naughty dream thing?"
    else:
        samantha.say "So, what do we want to do about this Emma naughty dream thing?"
    show emma blush
    mike.say "Direct and to the point, I see!"
    samantha.say "Well, we've got to just rip the bandage off, I think."
    mike.say "Fine. The answer is -- I don't know."
    samantha.say "Emma, what would {b}you{/b} like to do?"
    emma.say "I, uh. I mean, I kind of...but I don't...look, Sam. I love you dearly. I will never, {b}ever{/b} intentionally do anything to hurt you."
    samantha.say "I understand that. And I believe you. That's why we're having this conversation at all!"
    show emma sad
    emma.say "Which means we probably shouldn't do anything about it. We shouldn't have done anything, even. I just, I wanted to, I mean..."
    samantha.say "Hey, Emma! Emma! You haven't done {b}anything{/b} wrong."
    "I feel like I should say something here, but I don't know what to add."
    emma.say "Not yet, anyway."
    emma.say "I think I should go. I'm really sorry about all this!"
    hide emma with moveoutright
    samantha.say "Emma! Wait, don't be--"
    "But Emma has already left."
    samantha.say "Crap, [hero.name], now I feel bad."
    mike.say "Yeah, me too."
    samantha.say "Do you like her?"
    mike.say "Of course!"
    samantha.say "I mean...do you {b}like{/b} her!"
    mike.say "Oh! Um. Yeah, I guess. I mean, she's really cute, and sweet, and..."
    samantha.say "Should I--"
    mike.say "I already told you no!"
    samantha.say "Well, I guess that's that?"
    mike.say "Yeah. I just feel so bad about her. Like, there's this destiny thing and it's really important to her."
















    hide samantha
    $ DONE["emma_event_09_appointment"] = game.days_played
    $ emma.set_gone_forever()
    return

label emma_event_09_appointment_missed:
    play sound cell_vibrate
    pause 1.0
    "It's a text from Samantha."
    samantha.say "[hero.name], you missed our meetup. But this is important, let's try again tomorrow."
    $ hero.calendar.add(game.days_played + 1, LabelAppointment((14, 18), ["emma", "samantha"], "Meet with Sam and Emma", "emma_event_09_appointment", "emma_event_09_appointment_missed"))
    return

label emma_event_10_cinema:
    $ emma.flags.event10delay = TemporaryFlag(True, 1)
    show emma
    emma.say "Hey, [hero.name]! There's an obscure anime festival going on right now! Should we see that?"
    mike.say "Well, how can I possibly say no to that when I'm here with the biggest tiny anime fan I know?"
    emma.say "Right you are!"
    "We go into the theater. They put this into the smallest screen they have, it barely fits forty people, and it's mostly empty."
    $ game.room = "date_cinemaroom"
    "Apparently the movie is called {i}No yasashii kisu{/i}, whatever that means."
    "We sit down with our popcorn and the movie starts."
    "I'm going to be honest. It's a fairly dull romance. The characters aren't very interesting, and the clueless boy who is the main character just never seems to learn a thing."
    "But Emma seems to enjoy it; only a few minutes into the film, she grabs my arm and snuggles close to me. So I settle in to enjoy that part, even if not the film."
    "Halfway through it surprises me when the boy's best friend hooks up with the girl's brother. And the two boys share a long, sensual kiss while the main characters watch."
    "It's then that I notice Emma's watching {b}me{/b}, not the film."
    menu:
        "I'm disgusted by the kiss":
            "I can't help myself. If it had just been quick, fine, but this one takes so long, I can't hold it in."
            "I groan and look away."
            "Emma seems extremely disappointed in me."
            $ emma.love -= 5
        "I don't like the kiss, but I don't show it":
            "I guess it's not that bad, it's just two cartoon boys kissing. If it were girls I'd love it; this I don't really care for, but with a little patience, it'll be gone."
            "And it is."
            "When it's over, Emma closes her eyes and rests her cheek on my shoulder."
            $ emma.flags.lovepoints += 1
            $ game.active_date.score += 15
        "I like the kiss":
            "It's easy to imagine it's two girls kissing. Those boys were both drawn so fem anyway, that maybe with longer hair and different clothes, they'd just be girls."
            "That's probably what the point of the movie is anyway."
            "So I kick back and enjoy the kiss. Emma giggles at me when I smile, and squeezes me tight."
            $ emma.flags.lovepoints += 1
            $ game.active_date.score += 20
    $ hero.replace_activity()
    return


label emma_event_10_bree:
    $ emma.flags.event10delay = TemporaryFlag(True, 1)
    show emma happy at left5
    show bree happy at right5
    "When I see [bree.name] and Emma, they are already in conversation together."

    if 'bree_event_04' not in DONE and 'bree_event_05' not in DONE:
        bree.say "...don't really know him all that well. I mean we live together, but I guess we don't talk a whole lot."
        bree.say "But that's just fine with me!"
        emma.say "Yeah but someone like you? I'd have thought he'd be all into you!"
        bree.say "I guess not!"
        emma.say "Well, great talking to you! I gotta go! I'll see you at the movie?"
        bree.say "Yeah! See you then!"
        $ emma.set_counter("breeMovieDelay")

        hide bree
        hide emma
        return

    if bree.pregnant:
        bree.say "...is the father!"
        show emma annoyed
        emma.say "Oh. Oh wow. I didn't...that's um. Oh my gosh I may have made a huge mistake!"
        bree.say "What do you mean?"
        emma.say "I just...there were these dreams with me and [hero.name] and I thought maybe there was something, but..."
        emma.say "He's going to be a father! With you!"
        emma.say "I can't get in the way of that!"
        if bree.lesbian >= 9:
            bree.say "What makes you say you'd get in the way?"
            show emma blush
            emma.say "Wha! Hmph I just I um."
            bree.say "Promise me you'd never do anything to hurt me."
            emma.say "I pr--what, but why?"
            bree.say "Because you I'd trust."
            emma.say "I promise I'd never do anything to hurt you."
            $ emma.flags.lovepoints += 1
            $ emma.flags.breeok = True
            bree.say "Great! See, that was easy!"
            "Emma continues to blush furiously as she walks away from [bree.name]."
            return

    if 'bree_event_04' in DONE:
        if bree.flags.debt:
            bree.say "...and when I had money trouble, he helped me out with the rent."
        else:
            bree.say "...and when money trouble, he didn't make a big deal about it until I caught up on the rent."
    else:
        if not bree.flags.stayedoutkat:
            bree.say "...and when this bitch was hogging the game at the arcade, he stood up for me!"
        else:
            if hero.has_skill("video_games"):
                bree.say "...and he's one of the only guys who can beat me at video games!"
            else:
                bree.say "...and we play video games all the time. He's so cute when he thinks he can win."

    emma.say "So he really is as sweet as he seems?"
    bree.say "Most of the time!"
    "Huh. They're talking about me! I decide to hang back and listen. I know, it's not nice to eavesdrop, but..."
    emma.say "So have you ever, I mean. You know. With him?"
    bree.say "What, you mean fucked him?"
    show emma blush
    emma.say "Oh! Um, yeah. I mean I wouldn't say it like that I guess, but um, yeah. I know I shouldn't ask but..."
    if bree.is_sex_slave:
        "[bree.name]'s fingers lift to touch the collar at her neck."
        bree.say "Oh, honey, every which way I can. I'll...do anything for him."
        show emma fear
        "Emma's eyes grow wide and she stammers her reply."
        emma.say "But, you. Oh! Did he put that, um. That collar around your neck?"
        bree.say "Yes he did!"
        show emma annoyed
        emma.say "And you like it?"
        bree.say "I fucking love it."
        emma.say "Oh, that's weird. How did you...why did you? Oh I mean, that's so..."
        if Harem.together(bree, sasha):
            bree.say "Me and Sasha both!"
            show emma fear with vpunch
            emma.say "What?!?!"
            bree.say "I know! When I found out he was screwing both of us, I was pretty mad at first, but then I thought about it more, and I got so hot and bothered."
            bree.say "And so I dunno. She's kind of hot too! It turned out to be the best thing I ever did."
            show emma annoyed
            "Emma stammers an incoherent reply."
            bree.say "Why, do you want in?"
            show emma blush
            emma.say "No! No no no no!"
            bree.say "Oh, that's good, because I think we keep [hero.name] pretty busy."
            "Emma is still blushing furiously as she walks away from [bree.name]."
        else:
            bree.say "I know, I never would've thought about it. But there's something about him. I just want to do stuff for him."
            emma.say "Yeah, I get that part."
            bree.say "But?"
            show emma normal
            emma.say "I just don't get the collar thing."
            bree.say "What can I say? He likes it to see me with it, and I love to please him."
            emma.say "I, huh, okay."
        hide emma
        hide bree
        return

    if bree.sexperience > 0:
        bree.say "I shouldn't say, but...um, yeah, we have!"
        emma.say "What's he like?"
        bree.say "Well, he knows what he wants, that's for sure. And he's fun! He never fails to make me cum!"
        show emma blush
        bree.say "Why are you asking?"
        emma.say "I, uh. I mean, I can't stop thinking...um."
        bree.say "Is that what your little experiment was about the other night? When you slept on the couch? Were you really hoping to sleep in his room!"
        emma.say "No! I mean, no I wasn't, but I did...dream about it. And um. I can't stop thinking about that dream."
        bree.say "Ohhh! Are you going to?"
        emma.say "Not if you're sleeping with him!"
        bree.say "Well that's very nice of you!"
        if bree.lesbian >= 9:
            $ emma.flags.lovepoints += 1
            bree.say "What if...what if I said it was okay?"
            emma.say "What? Why would you..."
            bree.say "Well. For one, we had fun that night you came by. For two, you're cute. And for three, you asked first."
            emma.say "I wasn't asking permission!"
            bree.say "Well, not directly, no, but close enough."
            $ emma.flags.breeok = True
        else:
            bree.say "I'm not that inclined to share, but thanks for asking!"
            emma.say "Oh, I wasn't actually asking, I mean. Oh gosh."
            $ emma.flags.maybecheating = True
        "Emma continues to blush furiously as she walks away from [bree.name]."
        hide bree
        hide emma
        return

    $ emma.flags.lovepoints += 1
    bree.say "No, we haven't!"
    emma.say "Yeah but someone like you? I'd have thought he'd be all into you!"
    bree.say "I guess not!"
    emma.say "Well, great talking to you! I gotta go! I'll see you at the movie?"
    $ emma.set_counter("breeMovieDelay")
    bree.say "Yeah! See you then!"
    hide emma
    hide bree
    return

label emma_event_10_gfs:
    $ emma.flags.event10delay = TemporaryFlag(True, 1)
    $ renpy.dynamic("girlfriends", "pregs", "ignore")
    $ ignore = ["emma", "samantha"]
    if emma.flags.breeok:
        $ ignore.append("bree")
    $ girlfriends = hero.get_girlfriends(ignore=ignore)
    $ pregs = hero.get_pregs(ignore=ignore)

    show emma
    if game.season == 3:
        mike.say "Let's make a snowman."
    else:
        mike.say "Let's have a picnic."
    emma.say "I'd love to!"
    if game.season == 3:
        "We sit down to make a snowman. The first half of it is just normal small-talk and chit chat, nothing too special."
    else:
        "We sit down to have a picnic. The first half of it is just normal small-talk and chit chat, nothing too special."
    "But then the conversation takes a turn."
    if len(girlfriends) == 0 and len(pregs) == 0 and not emma.flags.admittedgirlfriend:
        emma.say "Hey, you know how you said you didn't have a girlfriend, back when we, uh. You know."
        mike.say "Sure."
        emma.say "Is that still true?"
        mike.say "It is."
        show emma annoyed
        emma.say "I was wondering. Do you think you'd..."
        mike.say "I'd what?"
        emma.say "Well that...no, never mind. Not now. Maybe...no not now."
        mike.say "What? Tell me!"
        emma.say "No it's not the right time. But you'll see! I promise!"
        $ emma.flags.lovepoints += 1
        $ game.active_date.score += 20
    else:
        emma.say "Hey, um."
        if len(girlfriends) != 0 and len(girlfriends.difference({'palla', 'lexi', 'audrey'})) == 0:
            emma.say "Do you remember we talked about you having a girlfriend, and your relationship is...open?"
            mike.say "I do."
            emma.say "How does that work?"
            mike.say "Well, it's..."
            if 'palla' in girlfriends:
                mike.say "Palla thinks it's hot when I'm with other women. So as long as I have time for her, it really gets her going."
                mike.say "Of course other women might not see it the same way."
            elif 'audrey' in girlfriends:
                mike.say "Audrey is weird. She's a have it both ways girl, and so she gets jealous, but then she likes the feeling of being jealous."
                mike.say "It's a little weird but I think it works out."
            else:
                mike.say "Lexi just isn't all that possessive. If I do right by her, she doesn't care what else I do or who else I see."
            mike.say "Which leads to the question...would something like that work for you?"
            emma.say "It's...you know I've never really thought about something like that. I mean, what do you do when someone gets jealous, or isn't getting enough attention?"
            mike.say "It's like any relationship. You talk through it, I guess. Sometimes there's yelling, sometimes there's crying, and you figure out what people need and if you can do it."
            mike.say "And maybe you can and maybe you can't, but you do your best."
            emma.say "Huh."
            $ emma.flags.lovepoints += 1
            $ game.active_date.score += 20
            emma.say "I...might be willing to try."
            mike.say "That'd be great!"
            emma.say "Might be! Don't get your hopes up too high."
            "I can only laugh at that."
        else:
            emma.say "Do you remember when I asked if you had a girlfriend?"
            if len(girlfriends) == 0:
                mike.say "I don't anymore."
                emma.say "What happened?"
                mike.say "That's...between me and her. I hope you understand."
                emma.say "Was it because of me?"

                mike.say "No."
                emma.say "You better not be lying."
                mike.say "I'm not!"
                $ emma.flags.lovepoints += 1
                $ game.active_date.score += 20
                emma.say "Okay. Because just the idea of you hurting someone else for my sake fills me with deep, dark rage."
                mike.say "I promise!"
                emma.say "Good!"
            else:
                mike.say "Yes, I remember."
                if emma.flags.admittedgirlfriend:
                    emma.say "You still do, don't you?"
                else:
                    emma.say "Do you have one?"
                mike.say "I, ah. Yes."
                emma.say "Mmm."
                mike.say "What is it?"
                emma.say "I just...I hate to be the other girl, the one someone is cheating with."
                mike.say "It's not--"
                emma.say "Don't!"
                mike.say "But--"
                emma.say "No buts, Mister!"
                mike.say "Fine."
                emma.say "It's not fair to me, or to her."
                mike.say "What would you like me to say?"
                emma.say "Just...don't say anything. There's nothing you can say."
                mike.say "Okay."
                $ emma.flags.maybecheating = True
                $ game.active_date.score += 5
    hide emma
    return

label emma_event_10:
    if emma.flags.lovepoints > 2:
        show emma happy
    else:
        show emma
    emma.say "Hi, [hero.name]!"
    mike.say "Hi Emma? How're you doing?"
    if emma.flags.lovepoints > 2:
        emma.say "I'm doing {b}great{/b}! I look forward to our next date!"
        if emma.love.max < 140:
            $ emma.love.max = 140
        $ emma.love += 4
    elif (emma.flags.lovepoints > 0 and not emma.flags.maybecheating) or emma.flags.lovepoints > 1:
        emma.say "I wanted to talk to you..."
        mike.say "What about?"
        emma.say "About us."
        mike.say "Oh?"
        show emma annoyed
        emma.say "There are...I have questions. But. But I think...I might be..."
        "She pauses. I stay quiet to let her talk."
        emma.say "I just want to know if you can..."
        show emma normal
        emma.say "Oh, ugh. [hero.name], you know I'm kind of falling for you, right?"
        mike.say "I do."
        emma.say "Are you falling for me too?"
        mike.say "I think I am."
        show emma happy
        emma.say "Oh. Oh whew! I'm so glad to hear that!"
        if emma.love.max < 140:
            $ emma.love.max = 140
        $ emma.love += 2
    else:
        show emma sad
        emma.say "So, hey, [hero.name]. I've been thinking about you. A lot."
        "I'm not sure I like the expression on her face as she says she's been thinking about me a lot."
        mike.say "Oh really?"
        emma.say "Um. Yeah. Look. I know we decided that, you know, with the dreams and whatnot, that we should..."
        emma.say "Well. I, um. I've thought a lot about it. And I just don't think we're compatible."
        mike.say "What?!"
        emma.say "You just...and...I don't know. I'm sorry. Look. Can we just be friends?"
        mike.say "But, Emma!"
        emma.say "No buts, [hero.name]. I thought about it a lot, and I've already made up my mind."
        "I sigh."
        mike.say "So that's it?"
        emma.say "That's it."
        mike.say "Okay, I guess."
        emma.say "Thanks for...well, not making a big deal out of it."
        hide emma with dissolve
        "Well. That sucks!"
        $ emma.set_gone_forever()
    hide emma
    return

label emma_event_11:
    if emma.love.max < 180:
        $ emma.love.max = 180
    "Sometimes a girl will really catch you off-guard when they come out with something unexpected."
    "It's like they've been hiding what they have to say with expert skill, waiting to spring it on you."
    "And then, at the other extreme, there are those girls that give the game away the moment you see them."
    "They look like a bag of nerves, like they're bursting at the seams to tell you, but afraid of actually doing it."
    show emma normal with dissolve
    "Emma, for example, falls very much into the latter category."
    "And she's been tripping over herself ever since we met up today."
    "I keep thinking that she's going to say something deep and meaningful."
    "But then she seems to lose her nerve and start babbling about something irrelevant."
    "In the end, I feel like I have to step in and offer her a helping hand."
    mike.say "Ah, Emma..."
    mike.say "Is there something the matter with you?"
    mike.say "You know, like something on your mind?"
    "I can see that I'm right the moment Emma hears what I have to say."
    "Her eyes go wide and her cheeks flush red at the same time."
    "All of which makes being proven right feel a little hollow."
    show emma fear
    emma.say "What?!?"
    show emma annoyed
    emma.say "I...I don't know what you mean!"
    emma.say "Why would you think that?!?"
    "Trying as best I can to look nonchalant, I offer her a casual shrug."
    mike.say "I dunno, Emma."
    mike.say "You just seem a little...distracted, that's all."
    show emma normal
    "Emma sets her face into a more determined expression."
    "And I can see that she's resolved to say whatever she has to say."
    emma.say "You're right, [hero.name]."
    emma.say "There is something the matter with me."
    emma.say "I'm nervous because I have something I need to say to you!"
    "Oh, here we go!"
    "Show me a guy that hasn't been here before."
    "I force a smile onto my face and nod, urging Emma to keep going."
    "But inside I'm already tensing up, preparing for the blow I'm expecting to land any moment."
    "I'm a big boy, I've been dumped like this before."
    "Sure, it never gets any easier, but I can handle it."
    emma.say "I..."
    emma.say "I just wanted to say..."
    emma.say "Since we've been together..."
    emma.say "I've never been happier before - not in my entire life!"
    show emma blush at center, zoomAt(1.5, (640, 1040))
    emma.say "And I want it to stay that way - I want us to be together forever!"
    "Once Emma's finished saying her piece, I'm left speechless."
    "But not for the reason I expected to be when she started speaking."
    "I was totally expecting her to tell me that it was over."
    "I was getting ready for the old 'it's not you, it's me' speech!"
    "Instead she's left me reeling for the exact opposite reason."
    "Apparently she never wants to leave my side again!"
    menu:
        "I feel the same way":
            "I don't have to hesitate for a moment."
            "As soon as the power of speech returns, I blurt out the words."
            mike.say "Emma..."
            mike.say "Me too!"
            mike.say "I feel the exact same way!"
            show emma happy
            "I didn't think that Emma's eyes could get any bigger."
            "But there they go, growing to the size of saucers!"
            emma.say "Do you really mean that, [hero.name]?"
            emma.say "You wouldn't joke about something that serious, right?!?"
            mike.say "Of course not, Emma!"
            mike.say "I'm one hundred percent serious right now!"
            "Without pausing for a second, Emma leaps towards me."
            "Throwing her arms out, she almost jumps into my embrace."
            "I return the gesture, but she's hugging me tighter than I can manage."
            "In fact I swear that my eyes are in danger of popping out of their sockets!"
            emma.say "Oh, [hero.name]..."
            emma.say "I never want to let you go!"
            mike.say "Emma..."
            mike.say "If this is a dream, I don't ever want to wake up!"
            $ hero.fun += 4
            $ emma.love += 10
            $ emma.set_girlfriend()
        "I like you, but not in the same way":
            "Whoa...this is intense."
            "In fact, this is a little too intense for me!"
            "I have to get Emma to slow down a little."
            "I'm just not ready for that level of commitment yet!"
            mike.say "Wow, Emma..."
            mike.say "That's kind of hit me like a bolt out of the blue!"
            show emma normal
            "Instantly Emma looks concerned."
            "She fixes me with an intense gaze."
            "And she looks for all the world like a puppy I just kicked."
            emma.say "Wha...what do you mean?!?"
            emma.say "I'm baring my soul to you, [hero.name]!"
            emma.say "Telling you exactly how I feel!"
            show emma sad
            emma.say "Don't you feel the same way?"
            emma.say "Don't you love me too?!?"
            "I wave my hands in the air desperately as Emma says all of this."
            "She's getting more worked up by the second, and I can't seem to calm her down."
            "And the worst thing is that I do feel the same way that she does."
            "About everything but the whole committing forever thing!"
            mike.say "No, no, no, Emma!"
            mike.say "That's not what I mean at all!"
            mike.say "I love you too, honestly I do!"
            mike.say "But I just don't think we're at that stage in our relationship just yet."
            show emma normal
            "This seems to have the desired effect, as it calms Emma down."
            "But I can tell that she still seems hurt by my words."
            "Which makes sense, as she just laid herself open to me."
            "It's not perfect, but at least it's a start."
            emma.say "But...we will be one day soon, right?"
            mike.say "Of course we will, Emma, of course!"
            "Mollified by my words, Emma nods."
            "She leans her head against my shoulder and we drop the subject."
            "But I'm left hoping that what I said was right."
            "I don't want to be made a liar by the way my own feelings turn out!"
            $ emma.love += 2
    $ emma.flags.emmadelay = TemporaryFlag(True, 1)
    return

label emma_event_12:
    scene bg beach
    if emma.love.max < 200:
        $ emma.love.max = 200
    "The weather's finally decent enough for us to head to the beach"
    "So that's exactly where Emma and I head for our next date."
    "I make sure that we get there nice and early so we can get a decent spot on the sand."
    "But even so, I'm surprised to find that the car-park is already almost full."
    "Once we're out of the car, I glance around, still a little puzzled."
    emma.say "[hero.name]..."
    emma.say "Is there something wrong?"
    show emma with dissolve
    "I turn around at the sound of Emma's voice."
    "And suddenly my interest in all of the cars seems pretty silly."
    "I smile and rub the back of my neck as I try to pass it off as nothing."
    mike.say "What?"
    mike.say "Oh...no, Emma, there's nothing wrong."
    mike.say "I just didn't expect the place to be this busy already, that's all."
    "Emma shrugs and shakes her head."
    show emma happy
    emma.say "Well...it IS a really nice day."
    emma.say "In fact, it's the first decent weather we've had in ages."
    emma.say "Maybe everyone just had the same idea we did?"
    mike.say "You're probably right, Emma."
    mike.say "In which case we need to get down to the beach as quickly as we can!"
    mike.say "Otherwise all the good spots will have been taken!"
    "Emma shakes her head again."
    "And I don't think she shares my sense of urgency."
    "But she indulges me by picking up the pace a little."
    scene bg beach with fade
    "A few minutes later we're on our way down to the sand."
    "And at first sight, it seems like I was right about the number of people already there."
    "But I was wrong about them taking up all of the good spots on the beach."
    mike.say "Huh!"
    mike.say "Will you look at all those people over there."
    mike.say "I wonder what they're doing."
    show emma at mostright5 with easeinright
    "Emma drops all of the stuff she's carrying onto the sand."
    "Which I guess means that we're claiming this spot as our own for the day."
    show emma at right4 with ease
    emma.say "They look like they're all together."
    emma.say "Like they're one big group."
    mike.say "Yeah, I see that..."
    mike.say "But they're not exactly dressed for the beach, are they?"
    mike.say "I mean, most of the guys are in suits."
    mike.say "And the girls are all in expensive dresses too!"
    "Emma looks at me in a strange way for a moment."
    show emma happy
    "And then she laughs, shaking her head."
    emma.say "It's a wedding party, you dummy!"
    emma.say "Somebody's getting married on the beach."
    "I take a closer look and see that Emma's right."
    "The crowd of people are roughly divided into two groups."
    "So one must be the groom's guests and the other the bride's."
    "And between them I can see the happy couple themselves."
    "Then I notice something else too."
    mike.say "Wait a minute..."
    mike.say "Are they..."
    mike.say "They are - they're standing in the sea!"
    "At this, Emma strains to get a better look at what's going on."
    "And I can tell from the look on her face that she approves."
    emma.say "Oh, [hero.name]..."
    emma.say "That's so original!"
    emma.say "And it's SO romantic too!"
    hide emma
    show emma happy at center, zoomAt (2, (650, 1250))
    "Now she turns to face me, her eyes wide with delight."
    emma.say "Don't you think so?"
    emma.say "If someone did something like that for me..."
    show emma blush
    emma.say "Well...I'd know that he loved me more than anything in the entire world!"
    "Emma keeps on looking me in the eye as she says all of this."
    "And she even holds my gaze once she's finished too."
    "Which means I get the distinct feeling she's expecting a response from me!"
    menu:
        "You're right, it's unique.":
            mike.say "I've got to hand it to them, Emma..."
            mike.say "I never saw anyone get married here at the beach before!"
            mike.say "I suppose they chose this place for that reason."
            mike.say "Because nobody here's ever going to forget their wedding day."
            show emma happy
            $ emma.love += 5
            "Emma's eyes light up with approval."
            "And she nods with enthusiasm."
            emma.say "That's right, [hero.name]..."
            emma.say "A girl wants her wedding day to be special, to be unique!"
            emma.say "I'm so glad you understand."
            emma.say "Because most guys just don't get it!"
        "Yeah, I guess it's different...":
            mike.say "Aah..."
            mike.say "It's different, I'll give them that!"
            mike.say "But don't you think it's kind of pretentious?"
            mike.say "And what if the weather turns bad all of a sudden?"
            show emma sad
            $ emma.love -= 5
            "Emma's expression turns to one of disappointment."
            show emma angry -close
            "And then her face darkens as she seems to get annoyed with me."
            emma.say "Urgh..."
            emma.say "That's such a typical guy thing to say, [hero.name]!"
            emma.say "A girl wants her wedding day to be special, to be unique!"
            emma.say "If it were up to most guys, you'd do it at one of those drive-thru chapels!"
            emma.say "And the reception afterwards would be in the car-park."
            emma.say "Just you and your buddies drinking a keg of beer!"
    hide emma with fade
    "We settle down on the sand, still watching the wedding ceremony."
    "And at the same time I'm starting to ponder Emma's interest in it too."
    "I mean yeah, it's kind of a cliche for a girl to be into it."
    "Even a modern girl can get carried away thinking about weddings."
    "But I can't help feeling there's more going on here."
    "Emma keeps looking over at me and smiling."
    "It's like she's picturing something in her head."
    "Is she..."
    "Oh god..."
    "Is she imagining that being the two of us up there?"
    "Is she thinking about what it'd be like for us to tie the knot?"
    "I have no idea if my suspicions are anything more than that."
    "But as I offer Emma a smile, she seems to beam back twice as intensely."
    "Perhaps she is making plans in her head for me popping the question."
    "And if she is, I really don't know how that makes me feel."
    "All I do know is that I need to get my head straight before it's too late."
    "I can't let myself get pressured into making the wrong decision."
    "Asking Emma to marry me would definitely make her happy."
    "But if it's not the right choice, we'll regret it in the future."
    return

label emma_preg_talk:
    $ emma.flags.toldpreg = True
    show emma fear
    "From the first moment I set eyes on Emma, I know that there's something wrong."
    "Her face is pale, her eyes huge and I swear that she's actually shaking too!"
    show emma fear at center, zoomAt (1.5, (640, 1040))
    "The second I realise the state that she's in, I hurry over, consumed with worry."
    "I have my hands on her shoulders before either of us can speak a single word."
    mike.say "Emma..."
    mike.say "Are you okay?"
    mike.say "You look as white as a sheet!"
    "Emma gazes up at me as I say all of this, looking straight into my eyes."
    "But even so there's something not quite right about the way she does this."
    "It's almost like she sees me and yet she doesn't see me at the same time."
    mike.say "Emma, please!"
    mike.say "Snap out of it already..."
    mike.say "You're scaring me!"
    "For some reason this last statement seems to get through to Emma."
    "She shakes her head a little, starting to come back to her senses."
    "And I finally see the fog clearing from her eyes as she does so."
    emma.say "[hero.name]..."
    emma.say "Oh...I'm sorry!"
    emma.say "I feel like I'm in a daze!"
    emma.say "Like everything's unreal, you know?"
    "I nod eagerly, hanging on every word that Emma says."
    "But pretty soon I realise that she's not actually saying that much."
    "Sure, she's explaining how she feels."
    "But she's not telling my why."
    "Taking Emma's hands gently in mine, I press her for an answer."
    mike.say "Emma..."
    mike.say "I want to help you."
    mike.say "But to do that, I need to know what's wrong."
    mike.say "Can you do that?"
    show emma sad
    "Emma nods at this."
    "But I can see that she's still scared."
    "And I can feel her trembling as I hold her hands."
    emma.say "I...I have to tell you something, [hero.name]."
    emma.say "I took a test this morning..."
    show emma fear
    emma.say "And it was positive!"
    "The moment that Emma comes out with those words, I know exactly what she means."
    "There's no need for her to say what kind of test it was, because that's obvious."
    mike.say "You mean...you're pregnant?"
    "Emma nods, biting her lip."
    "I can see tears welling in her eyes too."
    emma.say "Oh, [hero.name]..."
    emma.say "I'm so scared!"
    emma.say "I...I can't have a baby - I just can't!"
    "I shake my head, feeling more than a little puzzled."
    "I'd have expected a girl to be delighted at the news."
    "Either that or mad at me for getting her pregnant."
    "But Emma seems to be genuinely terrified by the idea."
    mike.say "Don't worry, Emma..."
    mike.say "I'm right here, and I'm not going anywhere!"
    mike.say "Whatever decision we come to, we'll do it together, okay?"
    "Emma looks at me in what could almost be described as desperation."
    emma.say "No, [hero.name], you don't understand!"
    emma.say "I'm not scared of being a mother."
    emma.say "I'm scared that I won't survive giving birth!"
    emma.say "I...I've always been weak, had bad health since I was a child."
    emma.say "The doctors told me that it would be dangerous for me to have a baby!"
    "That confession almost hits me harder than the actual news Emma's pregnant."
    "I was all set to step up to the challenge, to shoulder the responsibility."
    "But now the there's not one life on the line, but two!"
    "And Emma's clearly waiting for me to tell her what she should do about it."
    menu:
        "Tell Emma to keep it":
            "I take a deep breath as I prepare to say my piece."
            "And I already know that this is going to be a hard thing to sell."
            "But I feel that I owe it to Emma and myself to be honest."
            "So here goes nothing..."
            mike.say "Emma..."
            mike.say "I think you should keep the baby."
            show fx exclamation
            "Emma's eyes go wider still."
            "And I can see the shock written all over her face."
            hide fx
            emma.say "B...but, [hero.name]..."
            emma.say "Didn't you hear what I just said?"
            emma.say "What the doctors said could happen to me?"
            mike.say "I know, Emma, I know."
            mike.say "Obviously it's your decision to make, not mine."
            mike.say "And I'll support whatever choice you do make."
            mike.say "But at least hear me out, okay?"
            show emma sad
            "Emma nods slowly."
            "And I do the best I can to make my case."
            mike.say "When was the last time you actually saw someone about your condition?"
            emma.say "Erm..."
            emma.say "I guess it's been a while..."
            mike.say "And you're healthy now, right?"
            mike.say "You're doing fine, aren't you?"
            show emma normal
            "Emma nods again."
            mike.say "So what I'm saying is, things might have gotten better."
            mike.say "If you think about keeping the baby, we can go see your doctors."
            mike.say "We'll have them find out what the chances are, okay?"
            "I can see the idea starting to take root in Emma's head."
            "She's been ruled by the advice the doctors gave her in the past."
            "So why not seek their advice on this matter too?"
            emma.say "I...I suppose we could try that."
            emma.say "It would be reassuring."
            "I nod at this."
            mike.say "Then that's what we'll do, Emma."
            mike.say "We'll keep the baby - but get the doctors involved too!"
        "Tell Emma to get rid of it":
            "I take a deep breath, preparing myself for what I'm about to say."
            "There's no easy answer to a question like this."
            "But after what Emma's told me, I have to be honest."
            mike.say "Emma..."
            mike.say "If what you say about your health is true..."
            mike.say "Then I think that you should have a termination."
            mike.say "Obviously it's your decision to make, not mine."
            mike.say "And I'll support whatever choice you do make."
            mike.say "But that's my honest opinion."
            show emma cry
            "Emma finally bursts into tears, unable to hold back her emotions any longer."
            "She falls into my arms and I do the best I can to hold her gently yet firmly."
            hide emma
            show emma close cry
            emma.say "Oh, [hero.name]..."
            emma.say "I feel like the worst person in the world!"
            emma.say "But I'm so scared of dying!"
            mike.say "That's nothing to be ashamed of, Emma."
            mike.say "This was just an accident, that's all."
            mike.say "And you caught it early, which is a good thing."
            mike.say "You shouldn't have to risk your life for an accident!"
            "Emma buries her head into my shoulder, still sobbing."
            "And I do the best I can to comfort her."
            "I know it hurts, but I honestly think she's making the right choice."
            $ emma.love -= 20
            $ emma.unpreg()
    return

label emma_male_ending:
    $ game.hour = 16




    if renpy.has_label("emma_achievement_3") and not game.flags.cheat:
        call emma_achievement_3 from _call_emma_achievement_3
    $ game.room = "church"
    scene bg church wedding with fade
    "I thought that by now things would have started to feel like they were real and solid."
    "I mean, I know that I saw Emma in a dream before I actually met her in the flesh and all that."
    "But it's just one of those things that becomes an interesting story after a while, right?"
    "Like it'll be something that we tell people at parties and throw into conversation."
    "I'm sure that it's not going to be the thing that comes to define our relationship."
    "But right now I kind of feel like I'm right back there in the dream where it all started."
    "I keep glancing around the chapel as I wait for the service to get started."
    "And as I do so, everything seems unreal to me."
    "None of the planning that went into all of this comes to mind."
    "None of the discussions and debates that Emma and I had on the smallest of details."
    "Instead everything seems to have happened all at once."
    "It's almost like I was proposing to her one moment."
    "And the next I'm standing here at the altar, waiting to marry her."
    "So you see, it still feels like some kind of crazy dream!"
    "Maybe that's something that I'm just going to have to accept."
    "Maybe my life with Emma is always going to feel a little like a dream."
    "The people filling the pews are definitely real though."
    "I recognise the faces of my own friends and family sitting on one side."
    "And I even manage to spot a few of the guests on Emma's side that I recognise too."
    "Surely I can't be imagining all of those people at once?"
    "Just to be sure, I stick a hand into one of my trouser pockets."
    "And then I give myself a firm pinch on the flesh of my thigh."
    "Sure enough, I feel the pain and it confirms that I am indeed awake."
    "The proof comes just in time too, as the chapel suddenly fills with music."
    "Instantly I recognise the tune that Emma chose to come down the aisle to."
    "Turning my head, I see the doors of the chapel swing open."
    show emma wedding blush at center, zoomAt (1.0, (640, 730)) with dissolve
    "And then Emma sweeps through them."
    "I'm going to run the dream analogy straight into the ground here."
    "But I can't think of any other way to explain how Emma looks right now."
    "Somehow, a girl that I've always seen as beautiful, looks even better today!"
    "Everything seems perfect - the dress, the hair, the flowers."
    "All of them come together to make Emma look sensational."
    show emma at center, traveling(1.5, 5.0,(640, 1000))
    "To me it's like she's walking down the aisle in slow-motion."
    "Like it's one of those scenes in a movie with the soft-focus, you know?"
    "I feel like I'm the only person here and Emma's looking only at me."
    if emma.is_visibly_pregnant:
        "I steal a second to glance at the curve of Emma's belly."
        "Her dress is cut to be sympathetic to the fact she's pregnant."
        "But at the same time it doesn't try to hide the fact at all."
        "That was a choice that we made together, because why should we hide it?"
        "We're proud of the fact that we're going to be parents."
        "Proud of the fact that we're going to be a family."
    else:
        "I honestly never thought this moment would come."
        "I never thought that I'd actually be standing here."
        "And in just a few moments time, we're going to be married!"
    show emma happy at center, traveling(1.5, 5.0, (640, 1000))
    emma.say "[hero.name]?"
    show fx question
    emma.say "Are you feeling okay?"
    show emma blush
    "Suddenly Emma's standing right by my side."
    "And I snap back to reality in that moment."
    hide fx
    mike.say "Huh..."
    mike.say "Oh...yeah, yeah..."
    mike.say "I'm okay, Emma."
    mike.say "Just nerves, I guess!"
    show emma happy
    show wedding emma with fade
    "Emma nods and smiles, clutching her bouquet tightly."
    "I can see from the look on her face that she's nervous too."
    "So I open my mouth to say something that I hope is reassuring..."
    "Priest" "Ahem..."
    show wedding emma priest with dissolve
    "As one, Emma and I look in the direction of the priest."
    "He's smiling as he looks from one of us to the other."
    "But it's clear from the expression on his face that he wants to get things moving."
    "Emma and I turn to face him, trying to look like we're ready for what comes next."
    "The priest nods and then launches into it."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these two people in the bonds of holy matrimony."
    "We must have rehearsed this whole thing maybe a dozen times."
    "We went through the motions so many times I could have done it in my sleep."
    "But somehow everything now seems to become a blur."
    "It's hard for me to keep up with what the priest is saying."
    "And his words aren't making sense to me like they should."
    "By the time we get to the important part, I feel like I need a slap in the face."
    "Either that or a bucket of water tipped over my head to snap me out of it!"
    "Priest" "Do you, Emma..."
    "Priest" "Take this man, [hero.name]..."
    "Priest" "To be your lawful, wedded husband?"
    emma.say "I do."
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take this woman, Emma..."
    "Priest" "To be your lawful, wedded wife?"
    mike.say "I do."
    "The priest nods with satisfaction."
    "Priest" "These two people have exchanged their vows."
    "Priest" "And so I now call on those here present..."
    "Priest" "That if you know of any lawful reason that they may not be joined in holy matrimony..."
    "Priest" "Speak now, or forever hold your peace!"
    "There's the traditional pause for effect and ripple of nervous laughter."
    "And then the priest nods for a second time."
    "Priest" "Very well."
    "Priest" "By the power vested in me..."
    "Priest" "I hereby pronounce you husband and wife."
    "Priest" "You may kiss the bride!"
    show wedding emma -priest with dissolve
    "Emma takes hold of my hands, squeezing them tightly."
    "She looks up at me, her eyes beaming with happiness."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show emma kiss wedding
    with fade
    $ emma.flags.kiss += 1
    "We kiss, gently at first as she slides into my arms."
    "And then with a little more intensity as reality dawns on us."
    "We did it - we're actually married!"
    "And now we get to spend the rest of our lives together!"
    scene emma ending with fade
    emma.say "Are you sure that you want me to do this?"
    emma.say "Because I'm not the best when it comes to this kind of thing!"
    emma.say "And who's going to hear it anyway?"
    emma.say "I don't want to say anything that's going to get me in trouble!"
    emma.say "Okay, okay...if you say so."
    emma.say "I'll do my best, I promise!"
    emma.say "Oh, but where am I supposed to even start?"
    emma.say "I mean, I don't even know where [hero.name] and I first met - not really!"
    emma.say "Was it when we saw each other in that strange dream?"
    emma.say "Or was it when we recognised each other on the street a few days later?"
    emma.say "It was so confusing at the time all of that happened, and a little scary too."
    emma.say "Even now I really don't know what to make of it all."
    emma.say "Was it all some crazy coincidence?"
    emma.say "Or were we always supposed to meet like that?"
    emma.say "Oh dear..."
    emma.say "Maybe I should try to focus on the things that happened in the real world?"
    emma.say "At least with those I can be pretty sure I'm talking about stuff that really happened!"
    emma.say "Well...after [hero.name] and I first met, it took a while to get over the dream thing."
    emma.say "As if dating somebody new wasn't enough of a challenge!"
    emma.say "One of us was always mentioning it when we were together."
    emma.say "Bringing it up in the middle of a date when something occurred to us."
    emma.say "I guess I was as bad as [hero.name] when it came to that kind of thing."
    emma.say "Both of us were second-guessing ourselves when a little thing went wrong."
    emma.say "We were kind of hung up on the idea that this was all meant to be."
    emma.say "But at the same time we were also kicking against it, you know?"
    emma.say "Because who wants to think that their lives are already decided for them?"
    emma.say "You might like the idea of there being a handsome prince for you when you're a little girl."
    emma.say "But by the time you've grown up, you realise there are always people trying to control you."
    emma.say "So you're like, screw that!"
    emma.say "Luckily for me, [hero.name] turned out to be a great guy in his own right."
    emma.say "And I can certainly say that he's no handsome prince out of a fairy tale!"
    emma.say "Oh no...that sounded so mean!"
    emma.say "What I meant to say was that he's a wonderful guy."
    emma.say "But he's just a guy, yeah?"
    emma.say "Once I actually got to know him, the whole dream thing didn't seem to matter anymore."
    emma.say "And I felt like we were starting to date just because we liked each other so much."
    emma.say "Before I knew it, we were getting pretty serious too!"
    emma.say "I never thought the man of my dreams would be so goofy and make me laugh so much!"
    emma.say "When [hero.name] asked me to marry him, I was afraid that it was because of the dream thing."
    emma.say "But all it took was one look into his eyes to know that he understood what I was feeling."
    emma.say "And I know that he'd never have popped the question because he thought he had to - only because he wanted to."
    emma.say "Likewise I would never have said yes for the same reason, only because I knew we were really in love!"
    if emma.is_visibly_pregnant or emma.flags.mikeBabies >= 1:
        emma.say "And when we found out that I was pregnant with Emily, it was just perfect."
        emma.say "The fact that we were going to become a family made everything seem real."
        emma.say "At last we were forging bonds in the physical world and building something solid."
        emma.say "[hero.name]'s not the perfect dad, but he tries his best to be just that."
        emma.say "And in the end, that's what makes him a great father."
    else:
        emma.say "And now we're building something solid together in the real world."
        emma.say "I really feel like we're laying down the foundations of a future together."
        emma.say "[hero.name] and I keep talking about the possibility of starting a family."
        emma.say "And I'm sure that it's going to happen sooner, rather than later."
        emma.say "When that happens, I'm sure he'll prove to be a great father."
        emma.say "Not a perfect one, of course, but the best he can possibly be."
    emma.say "And before anyone asks me about it, let's talk about the elephant in the room."
    emma.say "Before I met [hero.name], I had no idea what I wanted in terms of a career."
    emma.say "But what with all of the dream girl nonsense...well, I started reading around."
    emma.say "I guess you could say that I got kind of obsessed with the subject of dreams."
    emma.say "Pretty soon I was studying them whenever the chance arose, even taking courses."
    emma.say "In the end, I became a fully qualified dream-therapist."
    emma.say "Not that I'm into dream-catchers, crystals and all that kind of nonsense."
    emma.say "What I do is rooted in proper psychology!"
    emma.say "But yeah, I kind of turned that weird way we met into a career!"
    emma.say "Of course [hero.name] hates it when I analyse his dreams."
    emma.say "But that's just because his are so obvious and easy to read!"
    emma.say "And I love to tease him about the deeper meanings of his nightly flights of fantasy!"
    emma.say "Plus, it's a great way to keep him in check."
    emma.say "Because if he steps out of line, I'm not going to be the girl of his dreams."
    emma.say "I'll make sure to be a thing of his darkest nightmares!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not emma.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_8
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_8
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
