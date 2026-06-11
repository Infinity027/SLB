init python:
    Event(**{
    "name": "morgan_event_01",
    "label": "morgan_event_01",
    "priority": 500,
    "conditions": [
        IsNotDone("kleio_event_01"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_cinemaroom", "cinemaroom", "date_cinema", "cinema")),
        ],
    "music": "music/roa_music/underwater.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "morgan_event_02",
    "label": "morgan_event_02",
    "priority": 500,
    "conditions": [
        IsDone("morgan_event_01"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),),
        ],
    "do_once": True,
    "music": "music/roa_music/underwater.ogg",
    })

    SpecificTalkSubject(**{
    "name": "morgan_event_03",
    "display_name": "Apologize",
    "label": "morgan_event_03",
    "duration": 0,
    "icon": "button_morgan",
    "conditions": [
        IsDone("morgan_event_02"),
        HeroTarget(IsGender("male")),
        PersonTarget(morgan,
            IsActive(),
            MinStat("love", 20),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "morgan_event_04",
    "label": "morgan_event_04",
    "priority": 750,
    "conditions": [
        IsDone("morgan_event_03"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_pub")),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 50),
            ),
        ],
    "music": "music/roa_music/underwater.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "morgan_event_05",
    "label": "morgan_event_05",
    "priority": 750,
    "conditions": [
        IsDone("morgan_event_04"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_restaurant")),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 60),
            ),
        ],
    "music": "music/roa_music/underwater.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "morgan_event_06",
    "label": "morgan_event_06",
    "priority": 500,
    "conditions": [
        IsDone("morgan_event_05"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_cinema")),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 80),
            ),
        ],
    "music": "music/roa_music/underwater.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "morgan_event_07",
    "label": "morgan_event_07",
    "priority": 500,
    "conditions": [
        IsDone("morgan_event_06"),
        Not(IsDone("morgan_event_07b")),
        IsSeason(0, 1),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_waterpark")),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        ],
    "music": "music/roa_music/underwater.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "morgan_event_07b",
    "label": "morgan_event_07b",
    "priority": 500,
    "conditions": [
        IsDone("morgan_event_06"),
        Not(IsDone("morgan_event_07")),
        IsSeason(3),
        "18 <= game.day < 25",
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1")),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        ],
    "music": "music/roa_music/underwater.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "morgan_event_08",
    "label": "morgan_event_08",
    "priority": 500,
    "conditions": [
        Or(
            IsDone("morgan_event_07"),
            IsDone("morgan_event_07b"),
            ),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_cinema", "date_cinemaroom")),
        MinDateScore(90),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/underwater.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "morgan_event_09",
    "label": "morgan_event_09",
    "priority": 500,
    "conditions": [
        IsDone("morgan_event_08"),
        IsTimeOfDay("afternoon"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        PersonTarget(morgan,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("love", 140),
            IsRoom("aquarium"),
            ),
        ],
    "music": "music/roa_music/underwater.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "morgan_event_10",
    "label": "morgan_event_10",
    "priority": 500,
    "conditions": [
        IsDone("morgan_event_09"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(morgan,
            IsActive(),
            MinStat("love", 160),
            Or(
                IsRoom("date_pub"),
                HasRoomTag("pub"),
                ),
            ),
        ],
    "music": "music/roa_music/underwater.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "morgan_event_11",
    "label": "morgan_event_11",
    "priority": 500,
    "conditions": [
        IsDone("morgan_event_10"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(morgan,
            IsActive(),
            MinStat("love", 180),
            IsFlag("LoveDelay", False)
            ),
        ],
    "music": "music/roa_music/underwater.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "morgan_preg_talk",
    "label": "morgan_preg_talk",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/underwater.ogg",
    "once_day": True,
    "do_once": False,
    "quit": False,
    })








    InteractEvent(**{
    "name": "morgan_male_90",
    "label": "morgan_male_90",
    "conditions": [
        PersonTarget(morgan,
            IsActive(),
            MaxStat("male", 90),
            MinStat("male", 81),  
            ),
        ],
    "priority": 1000,
    "music": "music/roa_music/underwater.ogg",
    "do_once": True,
    "quit": False,
    })

    InteractEvent(**{
    "name": "morgan_male_80",
    "label": "morgan_male_80",
    "conditions": [
        PersonTarget(morgan,
            IsActive(),
            MaxStat("male", 80),
            MinStat("male", 71),  
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "music": "music/roa_music/underwater.ogg",
    "quit": False,
    })

    InteractEvent(**{
    "name": "morgan_male_60",
    "label": "morgan_male_60",
    "conditions": [
        PersonTarget(morgan,
            IsActive(),
            MaxStat("male", 60),
            MinStat("male", 51),  
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "music": "music/roa_music/underwater.ogg",
    "quit": False,
    })

    InteractEvent(**{
    "name": "morgan_male_50",
    "label": "morgan_male_50",
    "conditions": [
        PersonTarget(morgan,
            IsActive(),
            MaxStat("male", 50),
            MinStat("male", 41),  
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "music": "music/roa_music/underwater.ogg",
    "quit": False,
    })

    InteractEvent(**{
    "name": "morgan_male_40",
    "label": "morgan_male_40",
    "conditions": [
        PersonTarget(morgan,
            IsActive(),
            MaxStat("male", 40),
            MinStat("male", 31),  
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "music": "music/roa_music/underwater.ogg",
    "quit": False,
    })

    InteractEvent(**{
    "name": "morgan_male_20",
    "label": "morgan_male_20",
    "conditions": [
        PersonTarget(morgan,
            IsActive(),
            MaxStat("male", 20),
            ),
        ],
    "priority": 1000,
    "music": "music/roa_music/underwater.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "morgan_react_kylie_sentence",
    "priority": 1500,
    "label": "morgan_react_kylie_sentence",
    "conditions": [
        IsDone("morgan_event_03"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "morgan_loose_not_girly",
    "label": ("loose_trait", "morgan", "not_girly"),
    "priority": 1500,
    "conditions": [
        PersonTarget(morgan,
            HasTrait("not_girly"),
            MaxStat("male", 89),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "morgan_gain_not_girly",
    "label": ("gain_trait", "morgan", "not_girly"),
    "priority": 1500,
    "conditions": [
        PersonTarget(morgan,
            Not(HasTrait("not_girly")),
            MinStat("male", 90),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "morgan_loose_tomboy",
    "label": ("loose_trait", "morgan", "tomboy"),
    "priority": 1500,
    "conditions": [
        PersonTarget(morgan,
            HasTrait("tomboy"),
            MaxStat("male", 69),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "morgan_gain_tomboy",
    "label": ("gain_trait", "morgan", "tomboy"),
    "priority": 1500,
    "conditions": [
        PersonTarget(morgan,
            Not(HasTrait("tomboy")),
            MinStat("male", 70),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "morgan_gain_girly",
    "label": ("gain_trait", "morgan", "girly"),
    "priority": 1500,
    "conditions": [
        PersonTarget(morgan,
            Not(HasTrait("girly")),
            MaxStat("male", 30),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "morgan_loose_girly",
    "label": ("loose_trait", "morgan", "girly"),
    "priority": 1500,
    "conditions": [
        PersonTarget(morgan,
            HasTrait("girly"),
            MinStat("male", 31),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "morgan_gain_not_tomboy",
    "label": ("gain_trait", "morgan", "not_tomboy"),
    "priority": 1500,
    "conditions": [
        PersonTarget(morgan,
            Not(HasTrait("not_tomboy")),
            MaxStat("male", 10),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "morgan_loose_not_tomboy",
    "label": ("loose_trait", "morgan", "not_tomboy"),
    "priority": 1500,
    "conditions": [
        PersonTarget(morgan,
            HasTrait("not_tomboy"),
            MinStat("male", 11),
            ),
        ],
    "quit": False,
    }
    )

    Event(**{
    "name": "morgan_date_play_arcade_clawmachine_male",
    "label": "morgan_date_play_arcade_clawmachine_male",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1"),
            IsActivity("date_play_arcade"),
            MinStat("money", 100),
            ),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        ],
    "music": "music/roa_music/underwater.ogg",
    "do_once": True,
    })

label morgan_murder_talk:
    "I can't help feeling like people are kind of avoiding me at the moment."
    "Which, considering what happened, I guess is perfectly understandable."
    "Maybe because they can't deal with the severity of the whole thing."
    "Or perhaps because they think that I need the space to start my recovery."
    "But the truth is that, either way, it still makes me feel like a pariah."
    show morgan sad at center, zoomAt(1.0, (640, 720)) with dissolve
    "So when I look up to see that there's someone standing in front of me, it comes as a real surprise."
    mike.say "Oh..."
    mike.say "Hi, Morgan."
    "Morgan looks awkward as she tries to meet my eye."
    "At first I think it's because of what happened to me."
    "But then I begin to see that it's more like she's ashamed of something."
    show morgan sadsmile at center, traveling(1.5, 1.0, (640, 1040))
    morgan.say "Hi, [hero.name]…"
    morgan.say "I was just..."
    morgan.say "I wanted to..."
    morgan.say "But I..."
    "Morgan tries again and again to say something."
    "But every time she ends up stumbling over her words."
    show morgan sad
    "In fact, she looks like she's about to burst from sheer frustration."
    "That is until she seems to give up entirely, and hurries over to me."
    "Without another word, Morgan throws her arms around me, hugging me tightly."
    "I hesitate for a few seconds, kind of stunned at her spontaneous show of affection."
    "Then I return the gesture, pulling her closer still."
    "And I have to admit, that does make me feel a lot better."
    "Though maybe not in the way a hug from a hot girl normally would."
    "This is more the comfort that comes from embracing a true and valued friend."
    "It's Morgan that breaks the hug up, backing away from me a little."
    "Enough that I can see she's red-cheeked and flustered."
    if morgan.male >= 66:
        morgan.say "Urm…"
        morgan.say "Sorry, man - I just kinda lost it a little back there!"
    elif morgan.male >= 33:
        morgan.say "Sorry, [hero.name]…"
        morgan.say "I've just been so worried about you!"
    else:
        morgan.say "Oh, [hero.name]…"
        morgan.say "I'm so glad that you're safe now!"
    mike.say "It's fine, Morgan..."
    mike.say "I mean, I'm not back to one hundred percent yet."
    mike.say "But I'm getting there, one step at a time."
    
    show morgan normal
    "The sensation of her doing so feels almost as good as the hug did."
    "And I can't resist putting my head atop hers a few seconds later."
    morgan.say "All of this proves one thing, [hero.name]…"
    mike.say "What's that?"
    morgan.say "It proves that I need to keep a closer eye on you!"
    morgan.say "So you won't be able to lose contact with me, not like before."
    morgan.say "Because I just won't let that happen!"
    "Morgan says this with such conviction that I feel a twinge in the core of my being."
    "And suddenly I feel like I'm going to be the one to start crying instead of her!"
    "Maybe I hadn't realised how deeply all of this wounded me until now."
    "Or maybe I never knew how much I valued Morgan's friendship."
    "But either way, from now on I'll be holding onto her as tightly as she just promised to hold onto me."
    scene bg black with dissolve
    return

label morgan_event_11:
    if morgan.love.max < 200:
        $ morgan.love.max = 200
    show morgan sad
    mike.say "Morgan..."
    mike.say "Looks like you've got the weight of the world on your shoulders!"
    mike.say "What's the matter?"
    show morgan surprised
    "Morgan looks surprised for a moment."
    show morgan annoyed
    "But then she lets out a tired sigh."
    if morgan.male >= 66:
        morgan.say "Ah, shit..."
        morgan.say "I thought I was better at hiding stuff than that!"
    elif morgan.male >= 33:
        morgan.say "Y...you noticed?"
        morgan.say "I guess I'm easier to read than I thought!"
    else:
        morgan.say "Oh dear..."
        morgan.say "I hoped it wouldn't be so obvious!"
    "Now I'm starting to worry - who wouldn't?"
    "I thought we were getting on great as a couple."
    "But now there could be something wrong - something I failed to notice."
    mike.say "What is it, Morgan?"
    mike.say "You seemed so happy the last time I saw you."
    mike.say "Was it all that dragging up old memories?"
    mike.say "I...I'm sorry if that brought up past trauma."
    mike.say "I had no idea..."
    show morgan blush
    "Morgan shakes her head at this, stopping me before I can finish."
    morgan.say "No, [hero.name]..."
    morgan.say "It's not something you or Jack said."
    morgan.say "It was something I said."
    morgan.say "I haven't been honest with you..."
    "Confused and still more than a little worried, I don't know what Morgan's about to say."
    "So I guess that what comes out of my mouth is just the first thing I can think of."
    mike.say "What do you mean, Morgan?"
    mike.say "Is it about me thinking you were a guy?"
    mike.say "Were you actually a guy and you had the surgery to become a girl?"
    mike.say "Because if that's what it is, then I'm still cool with that!"
    mike.say "What matters is how you choose to define yourself - not societal labels!"
    "Morgan stares at me in stunned silence for a few seconds."
    show morgan happy at center, vshake
    "Then she surprises me by bursting into peals of laughter."
    if morgan.male >= 66:
        morgan.say "What?!?"
        morgan.say "You actually think I used to have a dick?"
    elif morgan.male >= 33:
        morgan.say "Oh, [hero.name]..."
        morgan.say "Your head must be really messed up right now!"
    else:
        morgan.say "Oh, you silly boy!"
        morgan.say "That's the craziest thing I ever heard!"
    hide morgan
    show morgan normal close
    "But then she stops and looks at me in a more serious way."
    morgan.say "But it does make what I have to say next easier."
    morgan.say "Because it proves how devoted you are to me."
    morgan.say "Ah...here goes nothing..."
    morgan.say "[hero.name], the other night...when I said I loved you."
    morgan.say "I meant it - I love you."
    morgan.say "I always have, and now I know that I always will!"
    "I can feel my heart beating like a drum in my chest."
    "And it's like my brain can't process what Morgan's saying."
    hide morgan
    show morgan kiss
    with fade
    $ morgan.flags.kiss += 1
    "So it's up to my body to react."
    "I throw my arms around her, picking her up off the ground."
    "And I plant my lips on hers, kissing her like my life depends on it."
    "Morgan squeals in surprise, but then I feel her melt into my embrace."
    "She returns the kiss, clinging to me with just as much desperation."
    "When I finally release her and lower her to the ground, she doesn't let go."
    "I can hear her panting in my ear, like her heart's pounding too."
    hide morgan
    show morgan blush close
    with fade
    mike.say "I love you too, Morgan."
    mike.say "I can't imagine ever being without you again."
    "Morgan lays her head against my chest, closing her eyes as she does so."
    morgan.say "Oh, [hero.name]..."
    morgan.say "I used to dream about this happening to me, back when we were just kids."
    morgan.say "And now it seems like those dreams are actually coming true!"
    return

label morgan_event_10:
    if morgan.love.max < 180:
        $ morgan.love.max = 180
    $ morgan.flags.LoveDelay = TemporaryFlag(True, 3)
    "I've been wanting to get Morgan alone ever since she treated me to a private show at the aquarium."
    "Seeing her swimming around in a mermaid costume was something that I could never have imagined."
    "Not in a thousand years did I ever think I'd see Morgan doing something like that!"
    "But ever since I haven't been able to get the image of her with a tail out of my mind."
    "Sure, I'd love to have gotten Morgan alone somewhere intimate like my bedroom at home."
    "But what I end up with instead is a chance for us to grab a drink at the local pub."
    "So I guess that'll just have to do, and I'll have to control myself as best I can."
    show morgan casual at center with easeinright
    pause 1.0
    show morgan at center, zoomAt(1.5, (640, 1140))
    "When she arrives and takes a seat, I can see that Morgan's a little embarrassed."
    "And so I decide that it's best to confront the elephant in the room."
    "Or more specifically, the mermaid under the table..."
    mike.say "I'm still buzzing from the aquarium, Morgan!"
    mike.say "I can't believe my girlfriend moonlights as a mermaid!"
    show morgan blushhappy
    "Morgan instantly begins to blush."
    "But she has a smile on her face all the same."
    "Which means that she likes the compliments I'm giving her."
    if morgan.male >= 66:
        morgan.say "Yeah, I think I look good in that thing too."
        morgan.say "And it's a damn good workout too, swimming in it!"
    elif morgan.male >= 33:
        morgan.say "I'm really glad you liked it, [hero.name]."
        morgan.say "I feel kinda sexy in the tail, you know?"
        morgan.say "Like I'm another person when I wear it."
    else:
        morgan.say "I know what you mean, [hero.name]."
        morgan.say "It's super cute, right?"
    "I nod, eager to encourage Morgan to talk about the subject."
    "Anything for a chance to see her in that costume again!"
    mike.say "Do they make you keep the costume at work?"
    mike.say "Because I was looking at how much they cost online..."
    show morgan blush
    "Morgan's eyes go wide at this."
    "And she chuckles at my awkward hints."
    morgan.say "You're really into this whole mermaid thing, aren't you?"
    mike.say "I...I just thought it was cute, Morgan!"
    mike.say "And...well...kinda sexy..."
    show morgan happy
    morgan.say "You know once I'd have found that pretty weird."
    morgan.say "The idea of a guy wanting me to dress up as a mermaid for him?"
    show morgan normal
    morgan.say "But since we started dating, nothing seems nearly so strange to me!"
    "I frown and cock my head on one side."
    "Because I'm not sure what Morgan means."
    mike.say "What's strange about us dating, Morgan?"
    mike.say "I'm a guy and you're a girl."
    mike.say "Plus we really like each other."
    mike.say "I'm all for diversity and people shaking things up."
    mike.say "But on paper, there's nothing weird about us."
    mike.say "At least nothing that I can see."
    show morgan annoyed
    morgan.say "That's not what I mean, [hero.name]!"
    show morgan normal
    morgan.say "It's just that I never expected us to meet up again."
    morgan.say "And us actually dating..."
    show morgan blush
    morgan.say "I mean...wow!"
    morgan.say "I never thought that was gonna happen!"
    morgan.say "But I'm SO glad that it did..."
    hide morgan
    show morgan kiss
    with fade
    $ morgan.flags.kiss += 1
    "As Morgan's words trail away, neither of us needs any other cue."
    "As one we lean in towards each other, and then our lips meet."
    "The kiss is electric, and I can feel it rippling through my whole body."
    "The sensation sums up everything neither of us could ever put into words."
    "And I feel a desire for her like nothing I've ever felt before."
    hide morgan
    show jack
    with vpunch
    jack.say "BY THE POWER OF GRAYSKULL!"
    "In an instant our eyes snap open."
    hide jack
    show morgan kiss
    with dissolve
    $ morgan.flags.kiss += 1
    "Neither of us breaks off the kiss."
    "But we both glance in the direction of the voice."
    "And we both see Jack standing there, his mouth hanging open."
    "His eyes dart between Morgan and myself, like he can't believe what he's seeing."
    "Slowly, Morgan and I pull our lips apart and sit back into our seats."
    show morgan blush zorder 2 at center, zoomAt(1.5, (440, 1140))
    show jack zorder 1 at right5
    with fade
    morgan.say "Erm..."
    morgan.say "Hi, Jack!"
    mike.say "Yeah...hi, man!"
    mike.say "Fancy us running into you here - what are the chances?"
    "Suddenly Jack seems to snap out of it."
    "He points at us, almost quivering with shock."
    jack.say "You two..."
    jack.say "You were kissing..."
    jack.say "You were kissing each other!"
    mike.say "Ah...yeah, Jack..."
    mike.say "Morgan and I are kind of a thing now!"
    show morgan normal
    morgan.say "We were going to tell you, honest!"
    morgan.say "But there never seemed to be a good time..."
    show morgan blush at center, zoomAt(1.5, (340, 1140))
    show jack at center, zoomAt(1.5, (940, 1140))
    with vpunch
    "Jack hurries over and sits down at the table with us."
    "His eyes are almost popping out of his head."
    "And I'm actually worried he's going to have some kind of mental episode."
    jack.say "Two of my best friends..."
    jack.say "Seeing each other behind my back..."
    show jack happy
    jack.say "That's...that's GREAT!"
    jack.say "That's like the best thing ever!"
    show morgan normal
    "Morgan and I exchange a look of genuine relief."
    mike.say "You really mean that, Jack?"
    morgan.say "We were worried you might think we were betraying you!"
    show jack normal
    jack.say "Nah, of course not."
    jack.say "I think it's pretty cool - like a secretive romance!"
    jack.say "And plus you always had a thing for [hero.name]."
    jack.say "Didn't you, Morgan?"
    "I turn to look Morgan in the eye."
    show morgan blush
    "And I can see that she's caught off-guard by the question."
    if morgan.male >= 66:
        morgan.say "Well...yeah, I kinda liked him..."
        morgan.say "But it was more like a crush, you know?"
    elif morgan.male >= 33:
        morgan.say "I...I guess I did, Jack."
        morgan.say "We were all kids back then - full of hormones, you know?"
    else:
        morgan.say "I...I know that I did, Jack."
        morgan.say "But didn't we all have crushes on each other back then?"
    "I can sense that this is going somewhere that Morgan doesn't like."
    "I mean, it's flattering to know that she had feelings for me back in the day."
    "But I don't want to see her embarrassed about things like that here and now."
    show morgan normal
    mike.say "What about you, Jack?"
    mike.say "You used to have a crush on a different girl every day!"
    mike.say "Sometimes they were really weird too."
    mike.say "You remember when you fell in love with that chick?"
    mike.say "What was her name now..."
    show morgan happy
    morgan.say "Reona?"
    mike.say "Yeah, that was it!"
    morgan.say "Oh yeah, I remember her now."
    morgan.say "She was pretty short and frumpy, wasn't she?"
    mike.say "Yeah, and she had a big ass too!"
    jack.say "Hey!"
    jack.say "She was sweet and homely!"
    jack.say "And at least I knew she was a woman!"
    show morgan annoyed
    "Morgan and I both groan at the mere mention of that old chestnut."
    mike.say "Oh come on, Jack!"
    mike.say "When are you going to let that one drop?"
    show morgan normal
    morgan.say "Yeah, Jack."
    morgan.say "[hero.name]'s more than made up for that now."
    mike.say "Yeah - I totally know who Morgan is now."
    mike.say "And I totally love who she is too!"
    show morgan blush
    morgan.say "Aww..."
    show morgan blushhappy
    morgan.say "And I love you too!"
    "I blink as what Morgan just said actually starts to sink in."
    mike.say "Wait...what..."
    mike.say "You love me?"
    show morgan surprised
    morgan.say "Well...you just said you loved me!"
    mike.say "Ah...no, Morgan."
    mike.say "I said I loved who you are."
    mike.say "I mean...I'm crazy about you, for sure."
    mike.say "But I never actually said that I loved you!"
    show morgan blush
    "We stare at each other in silence for what feels like forever."
    "I don't think either of us knows what we really mean."
    "And we're not sure of the consequences of what we just said either."
    jack.say "Geez..."
    jack.say "You two need to lighten up a bit!"
    "Jack's nonchalant words cut through the tension."
    jack.say "I'm surprised either of you know what the other means."
    jack.say "First you thought she was a guy, [hero.name]."
    jack.say "And you were hiding a secret crush on him, Morgan."
    jack.say "Now you're back together and dating!"
    jack.say "That's enough to make anyone confused."
    jack.say "So give yourselves a break before you give yourselves a brain haemorrhage!"
    "Morgan and I share one more gaze into each other's eyes."
    show morgan happy
    with vpunch
    "And then we both burst out laughing."
    mike.say "He's right, Morgan."
    mike.say "Maybe we shouldn't sweat the small things?"
    show morgan normal
    morgan.say "Okay, okay..."
    morgan.say "For now, let's just agree that we like each other - a hell of a lot!"
    "After that the tension seems very much reduced."
    "We keep on laughing and joking, remembering old times."
    "And it feels good to know that our secret is out."
    "That and the fact that Jack's cool with it too."
    return

label morgan_event_09:
    play sound cell_vibrate loop
    "My phone buzzes. It's Morgan... I wonder what's up..."
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Morgan")
    if not result:
        $ hero.cancel_event()
        $ morgan.love -= 5
        return
    mike.say "Hey, Morgan!"
    mike.say "What's up?"
    morgan.say "Ah..."
    morgan.say "I am at work right now, thinking about you, that's all."
    mike.say "So what are you saying?"
    morgan.say "Hmm..."
    morgan.say "Why don't you come meet me at work?"
    morgan.say "I'll tell whoever's on the door to let you in on the quiet."
    mike.say "The aquarium?!?"
    mike.say "I don't know..."
    morgan.say "Trust me, you won't be waiting too long to see me, I promise!"
    mike.say "Okay, Morgan."
    mike.say "I'll be there as soon as I can."
    show bg street with fade
    "As soon as the call ends I head straight for the aquarium."
    "It doesn't take me long to make it there."
    show bg aquarium
    show victor at left4, blacker
    with fade
    "And just as Morgan promised, the guy on the door sneaks me in for free."
    "I make to walk into the place, but he stops me before I can leave."
    "Guy" "Ah, hey man..."
    "Guy" "Morgan said to wait for her in the theatre, okay?"
    mike.say "Oh..."
    mike.say "Okay, I guess."
    mike.say "Thanks, man."
    "Guy" "Oh, you will, my dude!"
    "Guy" "You will!"
    hide victor with dissolve
    "I nod again and walk away, not sure what the guy's talking about."
    "But the odd comment is soon forgotten as I wander through the aquarium."
    "Soon enough I find my way to the theatre the guy mentioned."
    "It's actually a massive tank with rows of benches for seating."
    "I guess they put on educational shows in here."
    "But right now it's totally deserted as closing time is near."
    "Taking a seat on the front bench, I prepare to wait for Morgan."
    "I try to keep myself occupied by watching the tank before me."
    "But then I notice that there are hardly any fish in there at all."
    "This makes me frown, and it's then that I hear music playing."
    "It's an upbeat melody, kind of a Caribbean type of tune."
    "And I think I remember hearing it on a cartoon when I was a kid."
    "Wasn't this one sung by a talking crab or something?"
    "Suddenly there's a flood of bubbles inside the tank."
    "I lurch backwards as they obscure everything inside."
    "And when they clear, the tank is no longer empty."
    "Inside I can see what looks like a huge fish swimming around."
    "The bubbles are still clearing, meaning I can't see it clearly."
    "I catch glimpses of fins and a tail."
    "Large coppery scales glisten as they catch the light."
    "But then I swear that I see a hand through the bubbles too!"
    "I leap up and get closer to the glass, struggling to see more."
    "Then I see a pair of huge blue eyes looking back at me."
    "I gasp at what I'm seeing, unable to believe it's real."
    show morgan mermaidcg with fade
    "That's Morgan in there!"
    "My eyes wander downwards, studying her as she hangs in the water."
    "She seems to have on a strange bra - one that's made of seashells!"
    "My gaze move downwards to her waist, seeing a sash tied around her middle."
    "But below it, I again see those shimmering copper scales!"
    "They're covering a tail, one that's taken the place of Morgan's legs!"
    "Below the waist, Morgan has a swaying, glistening tail!"
    "It ends in a broad fin that looks both elegant and powerful."
    "She's...she's a mermaid!"
    "My hands are pressed against the glass."
    "And the look on my face must be quite something."
    "Because Morgan's smiling with obvious delight at my reaction."
    "She raises her hands and forms them into a heart shape."
    "And then she extends it out to me!"
    "I can feel my heart pounding in my chest."
    "Not to mention my cock stiffening in my pants!"
    "Morgan puts her hands against the glass, mirroring mine."
    "She opens her mouth, letting our a stream of bubbles."
    "And I'm sure she mouths the words 'I love you' as she does so!"
    "I watch, totally spellbound, as she starts to swim around inside the tank."
    "She must have done this a thousand times before."
    "Because she moves like the tail is actually a part of her."
    "Morgan flicks her tail and moves her fins."
    "This sends her shooting through the water like an actual fish."
    "But the way she moves is graceful, almost like an underwater ballet."
    "Morgan keeps the show going for longer than I thought possible."
    "She sneaks gulps of air from a concealed tube to keep going."
    "And there's a part of me that doesn't want her to ever stop."
    "But finally her show has to come to an end."
    "Morgan gives me a wave to say goodbye."
    "And then she swims up in another flood of bubbles."
    hide morgan mermaidcg with fade
    "After that she's gone, and I sit back down on the bench."
    "As I wait, my mind is filled with images of her in that damn tail."
    "I always thought mermaids were kid's stuff."
    "But now I can't get Morgan as a mermaid out of my head!"
    morgan.say "Hello, sailor!"
    show morgan mermaid with dissolve
    "At the sound of Morgan's voice, I shoot up and spin around."
    "She hurries over to me, and I can see that her hair's still damp from the tank."
    morgan.say "So..."
    morgan.say "What did you think of my performance?"
    morgan.say "Do I make a good fish, huh?"
    mike.say "Wow, Morgan..."
    mike.say "That was...amazing!"
    mike.say "Why didn't you tell me you did that for a living?!?"
    show morgan blush
    "Morgan looks a little embarrassed at my enthusiasm."
    morgan.say "It's not all I do around here, [hero.name]!"
    morgan.say "And all the girls take turns in the mermaid show."
    morgan.say "Even some of the guys too!"
    "She looks away for a moment."
    "Then she half meets my gaze."
    morgan.say "So you liked it?"
    morgan.say "You thought I was good?"
    morgan.say "I was worried it might freak you out."
    mike.say "Morgan, it was the hottest thing I've ever seen!"
    mike.say "You're the sexiest mermaid I can imagine!"
    show morgan close blushhappy
    "Morgan's cheeks are getting reader by the moment."
    "But she does the best she can to ignore that fact."
    morgan.say "Oh, stop it!"
    morgan.say "Actually...don't stop it!"
    morgan.say "Just wait until we get somewhere more fun to start again!"
    if morgan.love.max < 160:
        $ morgan.love.max = 160
    return

label morgan_event_08:
    if morgan.love.max < 140:
        $ morgan.love.max = 140
    $ game.active_date.stay = False
    show bg cinema
    "I'm not one for having to be the first out of the cinema after the credits roll, like it's a race or something crazy like that."
    "But at the same time, I never want to hang around until the very end either."
    "Unless, that is, I have it on good authority there's a sweet extra scene tagged on for the benefit of the particularly devoted fan."
    "Normally I just grab my stuff and leave when I'm good and ready."
    "Which is why I'm surprised when Morgan doesn't make to get up out of her seat when I do."
    "At first I think she's just not ready yet, and so I sit straight back down to wait for her."
    "But then I see that she's got her jacket on and has all of her things ready to go."
    "My brow furrows at this, as there's nothing I can think of to keep Morgan in her seat."
    "We only came to the cinema in the first place as a kind of default choice for our date."
    "It was somewhere we could be together and yet chill out, not needing to deal with other people or be expected to make conversation."
    "I don't think either of us was desperate to see the film we just sat through."
    "I mean, the plot's already fading from my memory and the damn credits haven't even finished yet!"
    "Did Morgan really get that into the past two hours of utterly forgettable cinematic trash?"
    show morgan with dissolve
    mike.say "Hey, Earth to Morgan!"
    show morgan surprised
    morgan.say "Wha...huh..."
    morgan.say "Oh, sorry, [hero.name] - I was miles away!"
    show morgan annoyed
    mike.say "Yeah, I kinda noticed!"
    mike.say "What's with you anyway?"
    mike.say "You heard about something we need to see after the credits?"
    mike.say "Is there a secret scene?"
    show morgan normal
    "At this, Morgan gives me a little smile as she waves her hand in a dismissive gesture."
    morgan.say "No...no!"
    morgan.say "Just ignore me...it's nothing."
    morgan.say "I'm just a bit slow coming back to reality - you know what I mean?"
    "I nod and offer her a smile of my own, appearing to be happy to leave it at that."
    "But as we finally do get up and leave, my mind's already racing as to just what the matter could actually be."
    "If there's one thing that I've learned about women, it's that it's never 'nothing'."
    "And usually the something that it really is just so happens to be you."
    "Or else it's so closely related to you that it makes no real difference."
    show morgan at center, zoomAt(1.5, (640, 1040))
    "I try not to look too pained or worried as we walk out of the lobby and Morgan takes my hand."
    "The smile on her face still looks pretty genuine."
    "God knows how forced mine must look by now!"
    "Once we're out on the street, Morgan stops and turns to face me."
    "Still holding my hand like before, she now clasps the other and gazes up at me almost sweetly."
    morgan.say "[hero.name]?"
    mike.say "Ah...yeah, Morgan?"
    morgan.say "You know just now...when you asked me what was up?"
    "I nod slowly, waiting for the inevitable gut punch I'm sure will follow."
    morgan.say "Well, you caught me off guard, you know?"
    show morgan annoyed
    morgan.say "I've had something on my mind for a while now."
    morgan.say "And I was waiting for the right moment to say something."
    morgan.say "I thought I was better at hiding it - but if it's that obvious..."
    morgan.say "Maybe there won't be a right moment, and I should just come straight out and say it?"
    mike.say "If you think that's best, Morgan..."
    show morgan normal
    "She nods, taking a deep breath as she prepares to drop her bombshell."
    "My instinct is to close my eyes and maybe even hold my own breath."
    "But I keep right on grinning inanely, the smile on my face threatening to become a rictus."
    show morgan blush
    morgan.say "I think...I think I'm...falling for you, [hero.name]!"
    morgan.say "There, I said it!"
    morgan.say "I actually came out and said it!"
    "I shake my head in disbelief, still bracing myself for being told that my ass was single again."
    mike.say "What?"
    mike.say "You mean you don't want to dump me?!?"
    hide morgan
    show morgan surprised at center, zoomAt(1.5, (640, 1040)), vshake
    show fx exclamation
    morgan.say "NO...shit, no!"
    morgan.say "Is that what you thought I was going to say?"
    hide fx
    "I can already feel myself turning red with embarrassment at having so badly misread the situation."
    "But at the same time, I also feel a flood of relief at the fact I've been proven wrong."
    mike.say "Maybe a little...yeah."
    mike.say "Sorry?"
    show morgan normal
    morgan.say "Don't apologise, you dope!"
    morgan.say "Just tell me you're happy I said that...and maybe that you feel the same way!"
    mike.say "Oh...yeah, of course!"
    mike.say "I am...and...and I do!"
    "Morgan shakes her head with an amused look on her face, chuckling at my stumbling words."
    morgan.say "Okay, I guess that'll do - for now!"
    "And with that, she stands on the tips of her toes to plant a kiss on my lips."
    show morgan happy
    morgan.say "Now, maybe you should make good on that monosyllabic declaration of affection - and walk me home?"
    return

label morgan_event_07b:
    if morgan.love.max < 120:
        $ morgan.love.max = 120
    show morgan
    "I don't like coming to the mall when I actually have a whole load of shopping to get done."
    "And yeah, I know how crazy that might sound - because what else is a shopping mall for, right?"
    "But I prefer to shop online, so that I don't actually have to deal with real people."
    "And I like a trip to the mall to be more of a social event, like a nice stroll in the park."
    "All the better if you can go window-shopping with a hot girl in tow as well!"
    "But right now I only have one of those things ticked off on my list."
    "And the girl in question is getting more ticked off with every passing minute."
    show morgan annoyed
    if morgan.male <= 33:
        morgan.say "Oh...oh no..."
        morgan.say "I think somebody's going to trample me to death!"
    elif morgan.male <= 66:
        morgan.say "Geez..."
        morgan.say "I've never seen this place so packed with people!"
    else:
        show morgan angry
        morgan.say "Urgh..."
        morgan.say "I told you this was a dumb idea!"
    "I turn my head to give Morgan what's meant to be a reassuring smile."
    "But it probably ends up looking more like a pained grimace."
    "She's holding onto my hand for dear life as I drag her through the crowd of bodies."
    mike.say "Just hold on, Morgan..."
    mike.say "The store I need is right up ahead!"
    morgan.say "You're sure that you can't order it online?"
    morgan.say "Can't you order anything online these days?!?"
    mike.say "Apparently not!"
    mike.say "Otherwise you think I'd be at the mall before Christmas?!?"
    show morgan annoyed
    morgan.say "Yeah..."
    morgan.say "But that still doesn't explain why I'm here!"
    "I'm about to say something about wishing that she wasn't."
    "But instead I bite my tongue and push on until we reach the store I want."
    scene bg mall2 with fade
    "Once we're there, I hurry to find what I'm looking for."
    "Part of this is because I'm genuinely desperate to get my hands on it."
    "But a smaller part of it is so that I can ignore Morgan's complaints."
    "It's only when I have what I want and manage to pay for it that I'm satisfied."
    "Then I stop tuning her out and finally start paying attention to her again."
    mike.say "Got it!"
    mike.say "We can the hell out of here..."
    mike.say "Erm...what the matter, Morgan?"
    show morgan a sad with dissolve
    "My concern is on account of the way Morgan looks right now."
    "She's hugging herself tightly and she even seems to be shaking a little."
    "The sight makes me feel more than a little guilty for ignoring her."
    if morgan.male <= 33:
        morgan.say "It's all the people, [hero.name]!"
        morgan.say "There's just too many of them for me to handle it!"
    elif morgan.male <= 66:
        morgan.say "Ah...it sounds crazy..."
        morgan.say "But all these people..."
        morgan.say "It's kinda freaking me out!"
    else:
        morgan.say "It...it's nothing!"
        morgan.say "I...I just don't like big crowds, okay?"
    "I can see that Morgan's not putting on a performance here."
    "She genuinely looks like she can't handle being here right now."
    "I need to step up and do something about it too."
    "But what?"
    "To leave the mall we'd have to fight our way through those same crowds."
    "And if we stay at the mall, we're still surrounded by them."
    menu:
        "Calm Morgan down":
            "Wait a minute - I think I just had an idea!"
            "Maybe there's a way we can stay at the mall and calm Morgan down at the same time."
            mike.say "Don't worry, Morgan."
            mike.say "Christmas shopping can wait."
            mike.say "I know something that'll help."
            mike.say "It always helps me to relax!"
            show morgan surprised at center, zoomAt(1.5, (640, 1040))
            "Without waiting for an answer, I grab hold of Morgan's hand."
            "And then I lead her out of the store."
            "Well, at least that's what I intend to do."
            "Morgan's unaware of my plans and in the middle of freaking out."
            "Which means that she almost gets yanked off her feet by my efforts."
            if morgan.male <= 33:
                morgan.say "Oh no..."
                morgan.say "Where are we going?!?"
            elif morgan.male <= 66:
                morgan.say "Wha..."
                morgan.say "What are you doing?!?"
            else:
                morgan.say "Hey..."
                morgan.say "What the hell?!?"
            "I don't stop to offer an answer."
            show bg mall1 with fade
            "I'm already out of the store and elbowing through the crowds."
            "Shoppers scatter this way and that as I push my way past."
            "And Morgan's pulled along in the wake of my progress."
            "It doesn't take long for me to find the nearest restroom."
            show bg publicbathroom with fade
            "And then I open the door, dragging Morgan inside."
            "Before she can protest, I usher her into an empty cubicle."
            play sound door_slam
            "The door slams shut behind us."
            "And I hold the door just to be sure we're not disturbed."
            show morgan annoyed
            if morgan.male <= 33:
                morgan.say "This is the men's bathroom!"
                morgan.say "I can't be in here!"
            elif morgan.male <= 66:
                morgan.say "Ah, [hero.name]..."
                morgan.say "You mind telling me what's going on?"
            else:
                show morgan angry
                morgan.say "Okay, buddy, that's far enough!"
                morgan.say "What's going on here?!?"
            mike.say "Don't worry, Morgan."
            mike.say "Nobody's going to walk in on us in here."
            mike.say "And this won't take too long either."
            show morgan annoyed
            morgan.say "What do you mean?"
            morgan.say "What are we even in here for?!?"
            mike.say "We're in here so I can do something to help, Morgan."
            mike.say "Something that I just know will help you chill out."
            "I'm already getting down on my knees as I'm saying this."
            "I'm reaching out to undo Morgan's pants too."
            show morgan normal
            "She's no innocent, and it doesn't take her long to catch on."
            "I see Morgan's hands reach out, as if she's about to stop me."
            show morgan blush
            "But then they stop, and begin to retreat."
            "Which I take as permission to keep right on going."
            "I can hear Morgan's breathing become more intense with each passing second."
            "And she gasps as I gently pull down her panties a moment later."
            hide morgan
            show morgan cunnilingus restroom
            with fade
            "My head is level with her neat little pussy now."
            "I can just see it, nestled between her thighs."
            "Using my hands to part them, I lean forwards and open my mouth."
            "Morgan's body smells clean and inviting, like she just showered."
            "But the closer I get to her pussy, the more I can smell it's musky scent."
            "It's like the scent gets stronger all the time too, as Morgan gets excited."
            show morgan cunnilingus mikemid pleasure
            "And when I slide my tongue between her lips, I can taste it as well."
            "Morgan whimpers softly as I begin to lick at her."
            "Even exploring the outer folds seems to make her body quiver."
            show morgan cunnilingus mikeup closed
            "Those sounds and movement only spur me on to go further still."
            "I turn my head sideways and push my tongue in deeper than ever."
            "There's the sound of something hitting the walls of the cubicle."
            show morgan cunnilingus mikemid
            pause .4
            show morgan cunnilingus mikeup
            pause .4
            show morgan cunnilingus mikedown
            pause .4
            show morgan cunnilingus mikemid
            pause .4
            show morgan cunnilingus mikeup
            "But as nothing happens to stop me, I assume it's Morgan herself."
            "She must be bracing herself against the walls to keep upright."
            "I could believe it too, as her legs are turning to jelly right now!"
            show morgan cunnilingus mikemid
            pause .4
            show morgan cunnilingus mikeup
            pause .4
            show morgan cunnilingus mikedown
            pause .4
            show morgan cunnilingus mikemid
            pause .4
            show morgan cunnilingus mikeup
            "It seems like every movement of my tongue pushes her further over the edge."
            "And her whimpering is muffled, like she's biting her lip to keep from screaming."
            "I sense that I don't have much time before Morgan can't hold on."
            show morgan cunnilingus mikemid
            pause .4
            show morgan cunnilingus mikeup
            pause .4
            show morgan cunnilingus mikedown
            pause .4
            show morgan cunnilingus mikemid
            pause .4
            show morgan cunnilingus mikeup
            "So I redouble my efforts, probing as deep as I can into her pussy."
            "My tongue is getting numb from the demands I make of it."
            show morgan cunnilingus opened
            if morgan.male <= 33:
                morgan.say "Oh god...oh god...oh god..."
                morgan.say "You're making me cum!"
            elif morgan.male <= 66:
                morgan.say "Ah...what are you doing to me?!?"
                morgan.say "You're gonna make me cum!"
            else:
                morgan.say "Oh fuck...oh fuck...oh fuck..."
                morgan.say "I'm gonna cum, you wicked bastard!"
            show morgan cunnilingus closed
            "A moment later, Morgan falls silent as she bites down on her lip."
            show morgan cunnilingus mikedown pleasure
            pause .2
            show morgan cunnilingus mikemid
            pause .2
            show morgan cunnilingus mikeup
            pause .2
            show morgan cunnilingus mikedown
            pause .2
            show morgan cunnilingus mikemid
            pause .2
            show morgan cunnilingus mikeup
            pause .2
            show morgan cunnilingus mikedown
            pause .2
            show morgan cunnilingus mikemid
            pause .2
            show morgan cunnilingus mikeup
            pause .2
            show morgan cunnilingus mikedown
            pause .2
            show morgan cunnilingus mikemid
            pause .2
            show morgan cunnilingus mikeup
            "Her hands slap the walls of the cubicle, and I'm afraid she'll give us away."
            "But our luck seems to hold."
            "Nobody demands to know what's going on or tries to break down the door!"
            show morgan cunnilingus embarrassed squirt mikeup with hpunch
            $ morgan.love += 2
            $ morgan.sub += 2
            "Morgan grabs handfuls of my hair as she cums, almost tearing it out in clumps."
            "And she almost succeeds in smothering me by pressing my head into her pussy."
            "Once it's over, she gingerly pulls up her panties."
            show morgan cunnilingus closed smile -squirt mikedown blush
            "Then she sits down on the toilet, panting and exhausted."
            morgan.say "It...it worked..."
            show morgan cunnilingus opened
            morgan.say "I'm WAY more chill now!"
            morgan.say "I just hope you're there the next time I have a panic attack..."
            $ game.active_date.score += 20
        "Leave the mall":
            "There's no way around it, Morgan needs to get out of here."
            "Even if it freaks her out a little getting to the exit."
            "All that'll happen if she stays put is that she'll get worse."
            mike.say "Don't worry, Morgan."
            mike.say "Christmas shopping can wait."
            mike.say "Let's get you out of here!"
            show morgan surprised at center, zoomAt(1.5, (640, 1040))
            "Without waiting for an answer, I grab hold of Morgan's hand."
            "And then I lead her out of the store and towards the exit."
            "Well, at least that's what I intend to do."
            "Morgan's unaware of my plans and in the middle of freaking out."
            "Which means that she almost gets yanked off her feet by my efforts."
            with hpunch
            if morgan.male <= 33:
                morgan.say "Oh no..."
                morgan.say "Where are we going?!?"
            elif morgan.male <= 66:
                morgan.say "Wha..."
                morgan.say "What are you doing?!?"
            else:
                show morgan angry
                morgan.say "Hey..."
                morgan.say "What the hell?!?"
            "I don't stop to offer an answer."
            show bg mall1
            show morgan annoyed
            with fade
            "I'm already out of the store and elbowing through the crowds."
            "Shoppers scatter this way and that as I push my way past."
            with hpunch
            "And Morgan's pulled along in the wake of my progress."
            "I think I can hear her saying something on the way."
            "But I ignore her words in favour of ploughing ahead."
            scene bg street with fade
            "It's only when we reach the exit to the mall that I finally stop."
            mike.say "Phew..."
            mike.say "There...you...go..."
            mike.say "We're out of the mall, Morgan."
            mike.say "No need to thank me!"
            show morgan angry with dissolve
            "Morgan looks at me through narrowed eyes."
            "And she has a massive frown on her face too."
            "It's only now that I see what a state she's in."
            "Her clothes are in disarray and her hair's a crazy mess."
            "She looks like she's been dragged through a hedge backwards."
            "Or more accurately, protesting through a crowd of shoppers..."
            morgan.say "Next time, maybe let me breathe into a paper-bag, huh?"
            morgan.say "That normally does the trick, [hero.name]!"
            "All I can do is offer up a weak smile."
            "That and hope Morgan doesn't hold it against me for too long."
            $ morgan.love -= 5
            $ hero.cancel_activity()
    return

label morgan_event_07:
    if morgan.love.max < 120:
        $ morgan.love.max = 120
    show morgan
    morgan.say "Come on, [hero.name] - we need to get to the biggest of the slides before the line gets too long!"
    "Pulled into the water after her and almost losing my footing at the same time, I try my best to do as she asks."
    mike.say "Whoa, Morgan!"
    mike.say "Careful there, or you'll drag me the whole damn way on my face!"
    show morgan happy
    "Morgan laughs at my protests, letting up on the urgency with which she's pulling me, but not slowing down at all."
    "We make it to the queue that she was talking about and find that it's still short enough to see us on in less than ten minutes at the most."
    show morgan b normal at left4, vshake with ease
    "As Morgan jumps up and down, then does a little victory dance, I have to shake my head in amazement."
    "I can't quite believe that this is the same tough little tomboy that I grew up with."
    show morgan a normal at center, vshake with ease
    "Even now that I know she was never a guy, this side to her personality was totally hidden from me back then."
    "She's almost effortlessly feminine in moments like this, but yet not any the less herself a the same time."
    show morgan b normal at right4, flip, vshake with ease
    "It would have been easy to assume that she might go from one extreme to the other in these circumstances."
    "To imagine her feminine side coming out as a shy, fragile persona that recoiled from the world at large."
    show morgan a normal at center, flip, vshake with ease
    "But when she lets herself go and becomes like this, Morgan seems every bit as strong and confident as she ever did."
    "The big difference is how much more aware of her female nature and it's effect on others she seems to be."
    "Like right now, as she notes me staring at her a little too long as she hops on the spot."
    hide morgan
    show morgan
    "I look away quickly, hoping to minimise the damage done."
    mike.say "Sorry, Morgan - I didn't mean to stare like that."
    "She keeps on looking at me, cocking her head on one side and smiling sweetly."
    show fx exclamation
    morgan.say "Don't be silly, [hero.name] - of course you did!"
    "I start blustering, trying to make my excuses and yet not knowing what on earth I should be saying."
    show morgan happy
    "But Morgan cuts me off with a shake of her head and an impish giggle at my expense."
    morgan.say "It's okay, you can look at me if you like."
    show morgan close with dissolve
    "She crooks an finger at me, so that I lean in closer, letting her whisper into my ear."
    show morgan blush
    morgan.say "I'll tell you a little secret, [hero.name]."
    morgan.say "I kinda like it when you look at me like that!"
    hide morgan with easeoutright
    "And with that, she trots up the last few steps ahead of her and down the slide, disappearing in a cascade of water."
    "I stand still and silent for a moment, struck dumb by what Morgan just told me."
    "But then a series of shouts and complaints from the queue behind me snaps me back into reality."
    "I clamber after Morgan, shooting down the slide in the hope that I can catch her at the bottom."
    with hpunch
    play sound water_splash
    pause 0.2
    with vpunch
    "When I find her a few minutes later, she's sitting on the edge of the shallow pool."
    show morgan a at center, zoomAt(1.5, (640, 1040)) with dissolve
    "Morgan has one leg crossed over the other and leans backwards on the palms of her hands as she watches me approach."
    "The look on her face tells me just how calculated what she said to me back there was, and how much she enjoyed the effect that it had on me."
    "She almost seems to be sitting there, reclining and showing off her body as a kind of a challenge."
    show morgan a happy
    show fx exclamation
    morgan.say "Oh, [hero.name] - your face...your fucking face!"
    "I sit down next to her, trying as best I can to ignore the curve of her chest and the flat plane of her stomach."
    morgan.say "You looked like you'd been slapped with a wet fish!"
    mike.say "I'm glad you're amused, Morgan."
    "I try to sound like I'm not too butt-hurt, like I'm not some disapproving prude."
    "If I'm honest, the true implications of just what she said are only now occurring to me."
    "And maybe that's why I'm almost afraid to turn my head and look at her."
    show morgan a normal
    morgan.say "I do, by the way."
    mike.say "Huh...you do what?"
    morgan.say "Like it when you look at me."
    morgan.say "It makes me sure that you don't think I'm a guy any more."
    morgan.say "It might not be very feminist or woke, but it makes me feel like a real woman."
    mike.say "Erm...thanks, I guess..."
    mike.say "I'll be honest, Morgan - nobody ever thanked me for eyeing them up before now!"
    show morgan a happy
    morgan.say "Well, no one ever spent years thinking that I was a guy either."
    morgan.say "So I think we're about equal in the weirdo stakes."
    show morgan a normal at center, zoomAt(1.75, (640, 1200))
    "Morgan takes me by surprise again by leaning into me and wrapping her arms around my waist."
    morgan.say "Seriously though, [hero.name] - you've helped me to rediscover the woman in me."
    morgan.say "And I'm really grateful for that."
    morgan.say "It's like because you never saw me as female before now, you had no expectations of me in that way."
    morgan.say "You gave me the room to find out what kind of a woman I wanted to be."
    mike.say "One that likes me staring at her semi-naked body, apparently!"
    show morgan a happy with hpunch
    "Morgan cries out in mock offence at my comment, digging me in the ribs and making me groan."
    "But she's smiling the whole time as she does so, and she wraps her arms around me again as soon as she's done."
    "I finally feel that I can return the gesture, holding her against me and enjoying the sensation of her body being pressed against mine."
    return

label morgan_event_06:
    if morgan.love.max < 100:
        $ morgan.love.max = 100
    show morgan sad
    "From the moment that I meet up with Morgan, I can tell that there's something up with her."
    "She seems preoccupied, like she's trying to be all upbeat and into whatever we're chatting about."
    "But there's always something that she seems almost about to drop into the conversation."
    "Yet whenever the chance arises to change the subject, she always backs off again."
    "In the end, I feel like I have to broach it myself, just to stop it looming over us both."
    mike.say "Morgan, what's up?"
    show morgan surprised
    "She looks at me with a surprised expression on her face, still trying to deny that there's anything wrong."
    morgan.say "Huh...what do you mean?"
    mike.say "Come on, Morgan - you're miles away."
    show morgan annoyed
    "At this, she holds my eye for a couple of seconds and then looks away with a resigned sigh."
    morgan.say "Okay...okay, you got me!"
    morgan.say "There's something that's been bugging me...since we met at the cinema the other day."
    "Oh great, so not only were my suspicions correct, but what's up also has a lot to do with me too!"
    mike.say "Well, if it's bothering you that much, I suppose that you'd better tell me all about it."
    show morgan normal
    "Morgan nods, smiling a little sadly as she does so."
    "And I brace myself to hear something that I'd probably rather not."
    show morgan sad
    morgan.say "So...you remember that I was with another girl when we saw each other?"
    "I nod quickly, recalling the moment clearly in my mind."
    mike.say "Um, yeah - I guessed that must have been your girlfriend, right?"
    show morgan blush
    "I'm taken by surprise as Morgan's cheeks instantly flush at my suggestion."
    mike.say "I'm sorry, that was dumb of me to say."
    mike.say "I just assumed she was!"
    show morgan normal
    "Morgan shakes her head, even letting out an ironic little chuckle as she does so."
    morgan.say "She wasn't, [hero.name] - but you weren't to know that."
    show morgan annoyed
    morgan.say "No, what I meant was that I was out with ANOTHER girl!"
    "It takes a couple of moments for Morgan's words to rattle around inside of my head."
    "But then I finally understand the implications of what she's saying."
    mike.say "You mean that you were seeing the cinema girl on the side?"
    mike.say "I can see why you'd feel guilty, Morgan - but you don't need to explain yourself to me!"
    mike.say "Really it's just between you and your girlfriend."
    mike.say "But don't worry about Jack or me, as we won't tell anyone."
    show morgan normal
    "All this time, I'm trying to come over as the concerned friend that's cool with her being into both guys and girls."
    "But at the same time, I can't help feeling jealous of the girls that I've seen her with and know she's been dating."
    "I still don't know why Morgan seems to have become so insanely hot after I found out that she's actually a girl herself!"
    morgan.say "Thanks, [hero.name], you're a good friend."
    show morgan sad
    morgan.say "But that's not all of it..."
    "Wait - there's still more?"
    mike.say "It's not?"
    show morgan annoyed
    morgan.say "No, it's not!"
    morgan.say "Let's just say that you don't have to be worried about the girlfriend that I was kinda cheating on."
    morgan.say "Because I went and sent her a text afterwards, telling her all about it and..."
    morgan.say "And, well...pretty much telling her that I wasn't into her any more and it was over!"
    "There was a lot to take in there."
    "Do I need to be sympathetic that Morgan's just broken up with her girlfriend?"
    "Should I be relieved that there's no jealous partner hovering in the background, wanting revenge?"
    "Or am I just going to be a selfish prick and see this as an opportunity to move in on her now that she's single and vulnerable?"
    "In the end, I think that being a friend is the safest option right now."
    mike.say "So you feel bad about dumping your girlfriend by text?"
    mike.say "Sure, it's a bit impersonal, Morgan."
    mike.say "But there's no law against it, is there?"
    mike.say "Sometimes you just realise that a person's not the one, that's all."
    show morgan sad
    "Morgan nods, but still seems less than convinced."
    mike.say "I mean, what was it - that the new girl was better in bed, or something like that?"
    "I cringe the very second after I've uttered the words, knowing how insensitive they must sound."
    "Luckily for me, it seems that Morgan's just too wrapped up in her own predicament to properly notice."
    show morgan normal
    morgan.say "What...oh, no... I never slept with the girl you saw at the cinema, it never went that far."
    mike.say "Huh, well, that's another point in your favour then, isn't it?"
    morgan.say "How so?"
    mike.say "You went out with this other girl, and she made you realise there was no future with your girlfriend."
    mike.say "It's a lot better than sleeping with her and that being what opened your eyes to the fact, isn't it?"
    "Morgan shakes her head at this, and then nods."
    morgan.say "I suppose so."
    show fx heart
    show morgan blush
    morgan.say "That and seeing you again, [hero.name]!"
    "That last comment hits me like a slap in the face, and I can't get my head together in time to ask what it means."
    "By then it's far too late to start fishing for the finer details."
    "After that Morgan seems to cheer up quite noticeably, and the conversation moves on to a new subject entirely."
    "But now I feel like I'm the one that's becoming preoccupied."
    "The whole time I'm trying to guess why seeing me would make Morgan turn round and dump her girlfriend..."
    return

label morgan_event_05:
    if morgan.love.max < 80:
        $ morgan.love.max = 80
    "I wasn't sure about asking Morgan out for a meal at a restaurant, what with her being pretty masculine in her tastes and how she behaves."
    "I guess I figured that she'd be more interested in grabbing a burger on the way to a movie or something similarly uncomplicated."
    "But then I started to get worried that I was falling into the trap of stereotyping her and assuming that she might embarrass herself in polite company."
    "Which is crazy, as Morgan's not an animal - she doesn't drool when she talks or scratch herself below the waist in public."
    "Surely she can handle sitting down at a table and eating a meal with a knife and fork?"
    "Sure enough, when I suggest it to Morgan, she's pretty enthusiastic and agrees straight away."
    "And so I find myself sitting at the table in the restaurant, waiting for her to arrive."
    "I'm nervous as I wait, but I can't tell if it's more for Morgan's sake or my own."
    show morgan at center with easeinright
    "So when she walks in and gets shown over to the table, I'm flooded with relief that she's actually shown up."
    "And I make no effort whatsoever to judge what she's wearing or how she reacts to the surroundings either."
    mike.say "Hey, Morgan - I was starting to get worried you weren't going to make it tonight!"
    show fx question
    show morgan at center, zoomAt(1.5, (640, 1040)) with dissolve
    "Though she was smiling as she sat down, a look of confusion appears on her face at my comment."
    morgan.say "Huh...why's that?"
    morgan.say "You gave me the right address for this place."
    morgan.say "And this is just about the time you said the table was booked for two."
    "Morgan cocks her head on one side as she pulls her chair further under the table."
    morgan.say "Plus I'd have called or sent a text if I was running late or needed to cancel."
    morgan.say "So why would you think I wouldn't show up?"
    "The comment was, of course, fuelled by my paranoia at Morgan's masculine side screwing things up."
    "But I can't just come out and admit that, can I!"
    mike.say "Ah, well...I just never ate here before myself."
    mike.say "It's pretty fancy, so I was always scared off by it before now, that's all."
    morgan.say "Oh, so what...you thought I might stand you up over how posh the place is?"
    "I manage a halfway convincing laugh and throw my hands in the air helplessly."
    mike.say "I know - how dumb can I be, right?"
    mike.say "I guess that I still think of us as a bunch of kids that only want to eat junk food and play videogames!"
    mike.say "But we're adults now, and you must eat at places like this all the time."
    show morgan sad
    "At this, I see Morgan suddenly look sad and perhaps even a little melancholy."
    "Have I misjudged the situation here, said something that's upset her?"
    mike.say "What's wrong, Morgan?"
    mike.say "Are you feeling okay?"
    "Morgan shakes her head, but can't seem to make her expression convey the same message."
    "Concerned for her, I call a waiter over and ask for some water."
    morgan.say "I'll be okay, [hero.name], really I will."
    morgan.say "You just hit a little closer to home with that last comment than you realise."
    mike.say "What do you mean, Morgan?"
    "She laughs a little before answering."
    morgan.say "I was putting on a front just now."
    morgan.say "I never have been in a restaurant as fancy as this before."
    "I'm about to jump to the obvious conclusion and ask if she's upset that no one's ever taken her to a nice restaurant before."
    "But then, at the last minute, I somehow manage to save myself from making such a fundamentally dumb error."
    "Of course it's not something so simple that's upsetting Morgan - it's something much deeper and more far-reaching than that."
    mike.say "Morgan, what is it?"
    mike.say "You can tell me..."
    "For a moment, Morgan holds my eye in silence, and I genuinely think that she's not going to open up to me."
    "But then, slowly, she begins to talk."
    morgan.say "Sometimes, [hero.name], I feel like I never stopped being one of those kids that you mentioned."
    morgan.say "Sure, I grew up and I started to look more like a grown woman, even started dating and screwing around."
    morgan.say "But inside, deep down inside, I still felt like that little tomboy that I always was back then."
    "I can see genuine pain in Morgan's eyes, making me want desperately to help relieve it."
    mike.say "Morgan, is this all because I..."
    show morgan surprised
    show fx exclamation
    "She looks at me with wide eyes, seemingly surprised by the suggestion I just made."
    morgan.say "No, [hero.name] - all of this is not because you used to think I was a guy!"
    show fx drop
    morgan.say "That you'd even think that is very sweet...or very egotistical...or maybe both at once, I'm not sure."
    morgan.say "But no - you just made a mistake, I was the one that chose to behave like a boy to deal with it."
    show morgan sad
    "She sighs heavily before going on."
    morgan.say "It's too late now to change all of that."
    morgan.say "But I can't help wondering what would have been different if I'd been more in touch with my feminine side."
    morgan.say "Would life have been easier?"
    morgan.say "Would I have been a better, more rounded person?"
    "I have no idea what to say to that, so I decide to just be as honest as I can be."
    mike.say "It's lame, Morgan, and it probably doesn't help right now - but I like the person that you grew up to be a whole lot."
    mike.say "I like her so much that I asked her to a fancy restaurant."
    mike.say "One where the waiters probably look at me like something they scraped off of the soles of their shoes."
    mike.say "Learn to be more feminine if that'll make you happy - but don't stop being who you are, Morgan."
    show morgan happy
    "She smiles at this and gives me a grudging laugh."
    morgan.say "You're right, [hero.name] - that was pretty lame!"
    morgan.say "But maybe you can teach me to be lame enough to like myself too?"
    "Happy to see her in lighter spirits, I hand Morgan a menu and click my fingers for the waiter's attention."
    "I know they hate it when you do that, but I can't bring myself to care."
    show morgan normal
    "As all of my attention is now focused on making the meal an enjoyable experience for Morgan's sake alone."
    return

label morgan_event_04:
    if morgan.love.max < 60:
        $ morgan.love.max = 60
    show morgan
    "I have that feeling almost anything I could suggest Morgan and I do together could turn into a potential minefield for me."
    "So after spending some serious time pondering the matter, I settle on us doing the most down-to-earth thing that comes to mind."
    "Maybe if the demands that everything else places on me aren't all that strenuous, I can concentrate on making a good impression?"
    "And that's how we come to be sitting in a local pub, looking at each other over a couple of drinks and making pleasantly awkward smiles."
    "All I want out of this is for it to go well, and to have Morgan come away from it thinking that I'm someone she wants to spend more time with."
    "So in order to do that, I've already decided that I need to keep conversation well away from the issue of my thinking she was a guy."
    "Which is harder than it might sound, as my brain has developed a habit of leaping straight to that very subject."
    mike.say "Wow, Morgan - you drink just like a guy!"
    show morgan angry
    show fx anger
    "I watch in horror as Morgan's eyes shoot up from her drink and fix on mine."
    "Well, so much for me being smooth and keeping conversation away from that one subject that I wanted to avoid."
    "And here come the consequences!"
    morgan.say "And what, pray tell, is that supposed to mean?"
    "She raises an eyebrow and frowns, clearly waiting for an answer."
    "I can only manage to open and close my mouth, like a suffocating fish."
    "But then I find the will to start babbling a stream of desperate excuses."
    mike.say "I...I just meant that...that you drink pints!"
    mike.say "Like a guy drinks pints...you know?"
    mike.say "Not that it means you ARE a guy...or that girls can't drink pints!"
    "Morgan manages to keep her face straight and the disapproving expression together for another few seconds."
    show morgan happy at center, vshake
    "And then she finally cracks, bursting into laughter and grinning like a Cheshire Cat at my expense."
    morgan.say "Oh, [hero.name] - you're so easy to wind up!"
    morgan.say "It's one of the things that I always liked about you."
    "My sense of panic is only just starting to show signs of fading, and I can still feel my heart pounding a little."
    "All the same I force myself to smile back at Morgan, and nod as though I think it's just as funny as she does."
    "Honestly, I don't know which is more worrying right now."
    "The thought that I'm still so paranoid about thinking she was a guy, or that she's able to joke about it so easily."
    show morgan normal
    mike.say "Sorry, Morgan - I guess I'm still a little jumpy around that particular subject."
    morgan.say "Well don't be."
    morgan.say "As far as I'm concerned, it's ancient history."
    "I nod hastily, hoping that we can move on and start to talk about something else."
    "And to my relief, as time passes and the drinks begin to flow, we do just that."
    "We do what pretty much all old friends to when they haven't seen each other for a while and finally get to meet up again."
    "We keep on drinking and reminiscing about old times, chatting about people and places that we both remember."
    "But the difference is that I now get to revisit all of those memories with the knowledge that Morgan was actually a girl the whole time."
    "Suddenly things that had always seemed weird or to not quite make sense are revealed for what they actually were."
    "And yet it's not only me that gets frequent surprises and revelations about our shared past."
    "Morgan herself gets an education on the way that my mistaking her for a guy coloured my reactions to her back then too."
    show morgan happy
    "Thankfully we end up laughing at ourselves more than having quiet and contemplative moments."
    "When I finally shake off some of the effects of the beer and look around, I'm amazed at the number of empty glasses on the table in front of us."
    "I suppose time flies when you're having fun, and shoots past when you're making up for lost time."
    "And that's how it feels to me, like I'm running to make up for all of the years that I lost through not knowing the real Morgan."
    mike.say "I wish we could have done this a lot sooner, Morgan."
    show morgan normal
    "The suddenly serious tone of my voice makes her snap out of the pleasantly drunken haze into which we'd both fallen."
    morgan.say "Huh...done what?"
    mike.say "This - sat down and shot the shit with everything out in the open."
    morgan.say "Ah, [hero.name] - don't be so negative!"
    morgan.say "Maybe we should have, but we've got plenty of time to do it again."
    morgan.say "But I'd like to think that we're gonna make the most of now, rather than trying to make up for stuff from the past!"
    "I raise my glass and offer Morgan a toast."
    mike.say "Okay - here's to new stuff!"
    show morgan happy
    morgan.say "To new stuff!"
    with hpunch
    "Morgan smashes her glass against mine with a little too much enthusiasm."
    show morgan surprised
    "She lets out a squeal of alarm as some of the contents splash over her."
    "And I can't help but smile at just how cute she looks as she does so."
    return

label morgan_event_03:
    if morgan.love.max < 50:
        $ morgan.love.max = 50
    show morgan
    "I'm still nervous as hell when I even think about broaching the subject that's been playing on my mind with Morgan."
    "But it's fast becoming an obsession, and I'm seriously worried that it'll soon make it impossible for me to be comfortable around her."
    "So as soon as the chance presents itself, I take a deep breath and force myself to speak up."
    mike.say "Morgan, I...I need to get something off of my chest."
    show fx question
    "Morgan looks at me with raised eyebrows, as if she's not expecting my question, but perfectly open to answering it all the same."
    "Though this does nothing to settle my nerves, as I'm convinced that she knows what I'm about to say."
    mike.say "I just wanted to apologise...for, you know..."
    show fx exclamation
    "Morgan smiles at me, a look of slight embarrassment crossing her impish features as she does so."
    morgan.say "For spending all those years thinking I was a guy?"
    morgan.say "Oh, [hero.name] - you should really let it go."
    morgan.say "We were just kids back then, and none of that stuff really mattered!"
    "I rub the back of my neck nervously, trying to summon the courage to go on."
    mike.say "Yeah, but that's not totally true - is it, Morgan?"
    "Now she's looking at me with the raised eyebrows again."
    "Perhaps she's starting to realise that there's a little bit more to this than she thought."
    mike.say "What I mean is, we were kids, yeah."
    mike.say "But we knew each other when we were on the brink of all that changing, you know?"
    mike.say "The time in our lives when all of that stuff really was going to start to matter."
    "Morgan puts her hand atop mine and nods."
    morgan.say "I think you should say what you need to say, [hero.name]."
    morgan.say "And we can worry about how it makes me feel later, okay?"
    "Now it's my turn to nod, before I clear my throat and continue."
    mike.say "I suppose what's eating at me isn't just that I thought you were a guy, Morgan."
    mike.say "That I could just slap myself for and think that I was an ass for being that way."
    mike.say "What really bothers me is that I thought you were into me when I also thought you were a guy."
    mike.say "And...well, it freaked me out at the time."
    morgan.say "You mean that you're ashamed you were scared of a guy being attracted to you?"
    mike.say "I guess so...yeah."
    "Morgan looks at me for a couple of seconds in contemplative silence."
    show morgan happy at center, vshake
    "And then she surprises me by bursting into peals of laughter."
    morgan.say "Oh, [hero.name] - that's so sweet."
    morgan.say "Stupid, but sweet all the same!"
    "For a moment I'm utterly lost for words, unable to think of just what I should say to that."
    "Eventually, I manage to stammer a reply."
    mike.say "I...I was being homophobic..."
    mike.say "That's not a good thing, Morgan!"
    show morgan normal
    morgan.say "No, [hero.name], you were being a dumb kid, that's all!"
    morgan.say "Everyone gets to be dumb when they're a kid and they don't know who or what they are yet."
    morgan.say "What really matters is the kind of person you grow up to be."
    morgan.say "Trust me, [hero.name], I've dated girls that weren't as sensitive and self-aware as you on this very subject!"
    mike.say "So you forgive me?"
    show morgan happy
    "Morgan laughs again, shaking her head at me in exasperation."
    morgan.say "There's nothing to forgive."
    show morgan normal
    morgan.say "But if it'll make you feel better, then yes - I forgive you!"
    "Now it's my turn to smile back at her, as I can feel the weight of my guilt finally starting to lift from my shoulders."
    return

label morgan_event_02:
    "I guess it's down to the law of attraction, or something similarly weird and unknowable working away silently behind the scenes."
    "But when I bump into Jack in the pub a day or so later, my equally random encounter with Morgan is still very much on my mind."
    "Jack looks his usual self, upbeat and untroubled as he smiles at the sight of me and stops in his tracks."
    show jack normal with dissolve
    jack.say "Hey, [hero.name] - how you doing, man?"
    mike.say "Not too bad - and you?"
    "Jack gives me one of his characteristic nonchalant shrugs and snorts a little."
    jack.say "You know me...as good as I can be, right?"
    "We chat about everything and nothing for a couple of minutes, and then I drop my titbit of nostalgic news."
    mike.say "Hey, you'll never guess who I bumped into at the cinema the other night!"
    show jack happy
    jack.say "Don't tell me...it was Ozzy Osbourne?"
    "I give Jack a withering look, and he holds up his hands in surrender."
    show jack -happy
    jack.say "Okay, okay, Captain Serious - who did you see at the cinema the other night?"
    mike.say "Morgan - you remember the dude, right?"
    "Jack looks at me a little oddly as he nods."
    jack.say "Yeah, of course I remember Morgan."
    jack.say "Little younger than us, used to follow you around like your shadow at school."
    mike.say "That's the guy."
    mike.say "I bumped into him on a date a couple of nights ago."
    "Jack keeps nodding as I go on, but now he's kind of looking at me with narrowing eyes."
    "It's as though something's puzzling him more and more as I speak."
    "Whatever it is, I try to ignore it and press on with my account of the trip to the cinema."
    mike.say "Anyway, he's looking good - had a girl with him that was really pretty hot too!"
    "Jack realises that I've finished delivering my story and it's now time for him to offer a response."
    "He tilts his head to one side, clearly considering his words carefully before speaking."
    jack.say "Dude, seriously - we're adults now, so you need to drop all that stuff we used to joke about back when we were kids!"
    "Of all the responses I could have imagined, that might just be one of the most unexpected."
    "I look at him blankly, genuinely not knowing what he's talking about."
    jack.say "It was funny when we were messing around in the playground, man."
    jack.say "But you really should let it go now!"
    mike.say "Jack...seriously, what in the hell are you even talking about?"
    "Jack looks at me like he's having to explain why I should wash my hands after using the bathroom."
    jack.say "Calling Morgan a dude...dude!"
    jack.say "I know she was always a tomboy when we were kids."
    jack.say "But if she's gay or bi or something like that now, you need to respect that."
    jack.say "Keeping on calling her a guy just isn't cool."
    "My expression is still blank, and I feel like I've just stepped into a strange, alternate reality."
    mike.say "Jack...Morgan's a guy, he's always been a guy for as long as we've known him!"
    mike.say "Are you telling me he had a sex-change or something?"
    jack.say "Erm, no, [hero.name]...Morgan's always been a girl - well, now I guess she's technically a woman."
    "I feel like I've been staring at one of those magic eye pictures for years, always thinking that I knew what it depicted."
    "But now someone's told me to take a step forwards and to the left, revealing that I'd been looking at it from the wrong angle the whole time."
    with vpunch
    mike.say "Morgan's a girl?!?"
    "Jack's expression is showing genuine concern now, and he leans forward to put a steadying hand on my shoulder."
    jack.say "Dude, please tell me that you haven't just realised, this very moment, that Morgan was always a girl?"
    "I'm genuinely stunned, left with nothing to say."
    "All I can do is nod slowly."
    show jack happy at center, vshake
    "Jack laughs uproariously, not really helping the situation all that much."
    "But how can I blame him?"
    "If the roles were reversed, I'd no doubt find it as amusing as he does."
    jack.say "Wait a minute...didn't you...yes, yes you did!"
    "Oh god, what's he remembered now?"
    jack.say "You remember when we all thought Morgan had that crush on you, back in high school?"
    "I can feel my stomach already beginning to churn at the mention of the subject he's about to dredge up from our collective past."
    jack.say "We all thought it was pretty cool, but you...you were all weirded out by the idea."
    mike.say "Jack..."
    jack.say "Yeah, everyone thought you were creeped out at the idea because she was a friend or because of the age difference."
    mike.say "Jack, please..."
    jack.say "It never made sense before now."
    mike.say "Jack, please don't say it..."
    jack.say "No, no...it was because you thought she was a guy, wasn't it?"
    jack.say "Oh, dude - that's so funny!"
    jack.say "After all this time...I finally know what that was all about!"
    "Well, there's an episode from my youth that I thought was pretty much buried and forgotten about."
    "Now it looks like the whole thing's been dug up, had a bolt of lighting run through it and reanimated like Frankenstein's Monster!"
    "Jack and I talk for a little while longer, but despite my best efforts, I simply can't change the subject."
    hide jack with moveoutright
    "In the end we say goodbye and go our separate ways, with him still chuckling away at my expense."
    "Jack quips that he hopes to see Morgan before me, just so that he can tell her the whole embarrassing story and see her reaction for himself."
    "While I nod and laugh as best I can manage, I sincerely hope that I'm the one to see her first."
    "But I have no idea what I'm actually going to say to her, if and when I actually do see her again."
    if morgan.love.max < 20:
        $ morgan.love.max = 20
    $ morgan.unhide()
    $ morgan.flags.nodate = False
    $ morgan.flags.nokiss = False
    return

label morgan_event_01:
    "It was supposed to be nothing more than an evening out at the local multi-plex cinema, watching the latest big-budget superhero movie."
    if game.active_date:
        "The whole decision process must have taken [date_girl.name] and I less than a couple of minutes to chew over and agree to."
        "Tickets bought on my phone, Uber booked the same way to take us there and back again - nothing more to it."
        "And all seemed to be going to plan, until we walked into the cavernous lobby and I saw something that instantly caught my eye."
    else:
        "And all seemed good and well, until I walked into the cavernous lobby and I saw something that instantly caught my eye."
    show morgan casual at left with dissolve
    "I've always been one to notice dyed hair, even in passing, and want to take a second glance."
    "It's not a massive thing for me, like a fetish or anything that serious."
    "But I do think it's one of those little things that can get your attention and add an element of interest to a person's appearance."
    "Though the exact reason that this person caught my attention wasn't just because they had dyed hair."
    "It was actually more on account of the fact that I was sure I'd seen that exact shade of electric blue somewhere before."
    if game.active_date:
        if date_girl == kleio:
            hide morgan
            show kleio at center, zoomAt(1.25, (640, 880))
            with dissolve
            kleio.say "Hey, Loverboy..."
            kleio.say "What's bugging you out?"
            show kleio normal
            mike.say "I thought I just recognised someone...over there."
            mike.say "Yeah, that's them alright!"
            show kleio annoyed
            kleio.say "Yeah, yeah, yeah..."
            kleio.say "I gotta go use the little girl's room."
            show kleio happy
            kleio.say "So you go ruin their day without me, okay?"
            hide kleio with easeoutright
            "I make to weave through the crowd and towards the person in question as Kleio rushes off to the bathroom."
        else:
            hide morgan
            $ renpy.show(date_girl.id, at_list=[center, zoomAt(1.25, (640, 880))])
            with dissolve
            date_girl.say "Hey, [hero.name], what's up?"
            mike.say "I thought I just recognised someone...over there."
            mike.say "Yeah, that's them alright!"
            "I make to weave through the crowd and towards the person in question, [date_girl.name] following close behind me."
            $ renpy.hide(date_girl.id)
            with dissolve
    else:
        "I make to weave through the crowd and towards the person in question."
    mike.say "Hey...hey, Morgan!"
    show morgan casual at left with dissolve
    "At first the familiar figure hears me calling, but doesn't seem to see me for the bodies still between us."
    "They turn around, looking this way and that for the person calling their name."
    show morgan stuned at center with ease
    "Just as they turn to face my general direction, the crowd parts enough for them to pick me out."
    show morgan surprised
    show fx question
    morgan.say "[hero.name]...is that you?"
    show morgan normal
    mike.say "Yeah, you bet it is!"
    mike.say "How are you, man?"
    hide fx
    show morgan annoyed
    "For all that I'm happy to see Morgan, I'm not sure the same is true in reverse."
    "Morgan's face looks more confused and uneasy than pleased to have bumped into an old school friend at random."
    morgan.say "Oh, I'm good...I guess!"
    if game.active_date:
        if date_girl == Person.find("amy"):
            "Morgan shifts uncomfortably, even more so when Amy steps up to my side and nudges me in the elbow."
            mike.say "Oh, right - Morgan, this is Amy."
            mike.say "Amy, this is Morgan - he's one of the guys I used to hang out with at school."
            show morgan casual blush
            "For some odd reason, this statement seems to embarrass Morgan, who flushes red and begins to say something."
            "The words are drowned out, however, as a girl hovering close by (who I now realise must be Morgan's own date) suddenly starts chuckling loudly."
            "I can't help staring at her for a moment, as I'm not sure either why she's laughing or why Morgan's blushing."
            show amy happy
            amy.say "Oh, don't worry, [hero.name]..."
            amy.say "We already kind of know each other."
            amy.say "Friend of a friend, yeah?"
            show amy normal
            "I wait for Amy to say more, but it doesn't seem like she's going to oblige me."
        elif date_girl == anna:
            "Morgan shifts uncomfortably, even more so when Anna steps up to my side and nudges me in the elbow."
            mike.say "Oh, right - Morgan, this is Anna."
            mike.say "Anna, this is Morgan - he's one of the guys I used to hang out with at school."
            show morgan casual blush
            "For some odd reason, this statement seems to embarrass Morgan, who flushes red and begins to say something."
            "The words are drowned out, however, as a girl hovering close by (who I now realise must be Morgan's own date) suddenly starts chuckling loudly."
            "I can't help staring at her for a moment, as I'm not sure either why she's laughing or why Morgan's blushing."
            show anna happy
            anna.say "Oh, hi Morgan!"
            anna.say "Yeah...we already kind of know each other."
            anna.say "Friend of a friend, that sort of thing."
            show anna normal
            "I wait for Anna to say more, but it doesn't seem like she's going to oblige me."
        elif date_girl == sasha:
            "Morgan shifts uncomfortably, even more so when Sasha steps up to my side and nudges me in the elbow."
            mike.say "Oh, right - Morgan, this is Sasha."
            mike.say "Sasha, this is Morgan - he's one of the guys I used to hang out with at school."
            show morgan casual blush
            "For some odd reason, this statement seems to embarrass Morgan, who flushes red and begins to say something."
            "The words are drowned out, however, as a girl hovering close by (who I now realise must be Morgan's own date) suddenly starts chuckling loudly."
            "I can't help staring at her for a moment, as I'm not sure either why she's laughing or why Morgan's blushing."
            show sasha shout
            sasha.say "Oh, don't worry, [hero.name]..."
            sasha.say "Morgan already knows who I am."
            show sasha happy
            sasha.say "Friend of a friend, yeah?"
            show sasha normal
            "I wait for Sasha to say more, but it doesn't seem like she's going to oblige me."
        elif date_girl == minami:
            "Morgan shifts uncomfortably, even more so when Minami steps up to my side and nudges me in the elbow."
            show minami happy
            minami.say "Hi there!"
            show minami normal
            mike.say "Oh, right - Morgan, you remember Minami?"
            mike.say "My sister...I mean my ADOPTED sister!"
            mike.say "Minami, you remember Morgan, don't you?"
            mike.say "He's one of the guys I used to hang out with at school."
            show morgan casual blush
            "For some odd reason, this statement seems to embarrass Morgan, who flushes red and begins to say something."
            "The words are drowned out, however, as a girl hovering close by (who I now realise must be Morgan's own date) suddenly starts chuckling loudly."
            "I can't help staring at her for a moment, as I'm not sure either why she's laughing or why Morgan's blushing."
            "I look at Minami, hoping for some help."
            "But I see that she's looking at me in an odd way too."
        elif date_girl == alexis:
            "Morgan shifts uncomfortably, even more so when Alexis steps up to my side and nudges me in the elbow."
            show alexis happy
            alexis.say "Oh...hi."
            show alexis normal
            mike.say "Oh, right - Morgan, you remember Alexis?"
            mike.say "We dated back in high-school, and we just got back together."
            mike.say "Alexis, you remember Morgan, don't you?"
            mike.say "He's one of the guys I used to hang out with at school."
            show morgan casual blush
            "For some odd reason, this statement seems to embarrass Morgan, who flushes red and begins to say something."
            "The words are drowned out, however, as a girl hovering close by (who I now realise must be Morgan's own date) suddenly starts chuckling loudly."
            "I can't help staring at her for a moment, as I'm not sure either why she's laughing or why Morgan's blushing."
            "I look at Alexis, hoping for some help."
            "But I see that she's looking at me in an odd way too."
        else:
            "Morgan shifts uncomfortably, even more so when [date_girl.name] steps up to my side and nudges me in the elbow."
            mike.say "Oh, right - Morgan, this is [date_girl.name]."
            mike.say "[date_girl.name], this is Morgan - he's one of the guys I used to hang out with at school."
            show morgan casual blush
            "For some odd reason, this statement seems to embarrass Morgan, who flushes red and begins to say something."
            "The words are drowned out, however, as a girl hovering close by (who I now realise must be Morgan's own date) suddenly starts chuckling loudly."
            "I can't help staring at her for a moment, as I'm not sure either why she's laughing or why Morgan's blushing."
    else:
        "Morgan shifts uncomfortably and a girl hovers close by (who I now realise must be Morgan's date) and suddenly starts chuckling loudly."
        "I can't help staring at her for a moment, as I'm not sure either why she's laughing or why Morgan's blushing."
    "Morgan seems to regain enough composure to introduce the chuckling girl, but her name doesn't lodge in my memory for as much as a second."
    "I'm more concerned with the odd way in which Morgan is behaving, wondering if there was any reason I could recall for it."
    "Had I done or said something back in the day that I'd forgotten all about?"
    "What could be so bad that Morgan would still be nursing a grudge over it?"
    "Especially if had no memory of it whatsoever!"
    "Whatever the case, I can sense the mood becoming ever more awkward, and so I make my apologies and claim our film is about to start."
    morgan.say "Oh, yeah...ours too!"
    mike.say "Good to see you again, Morgan."
    mike.say "We should meet up for a drink or something, man."
    mike.say "You know, catch up with each other - make it a guy's night out?"
    morgan.say "Uh, okay...I guess we could do that."
    hide morgan with easeoutleft
    if game.active_date:
        "Weirdly, I see Morgan's date, giggling away at us again."
    else:
        "Weirdly, I see Morgan's date, giggling away at me again."
    "I can't quite put my finger on it, but I'm sure that the girl knows what's making Morgan edgy and bugging me at the same time."
    "Try as I might, I can't figure it out, or stop myself from taking an instinctive dislike to her because of that same reason."
    if game.active_date:
        if date_girl == Person.find("amy"):
            scene bg cinemaroom
            with fade
            show amy at center, zoomAt(1.25, (640, 880)) with easeinleft
            "As we walk off and find the screen where our film is being shown, I find myself talking about Morgan to Amy."
            "Most likely I'm unconsciously trying to distance myself from the memory of his annoying date with more agreeable ones about Morgan instead."
            mike.say "I can't believe we just bumped into that guy at random."
            mike.say "It's been years since I saw him last."
            show amy stuned
            "Every time I make a statement about Morgan, Amy seems to look at me in a strange manner."
            "It's almost like I think that I'm speaking in English, but something is a little off when she hears it come out of my mouth."
            mike.say "Hey, look...what's up?"
            show amy surprised
            amy.say "What do you mean?"
            show amy sadsmile
            mike.say "Every time I mention Morgan or something about the guy, you look at me like I have steaming turds hanging out of my mouth!"
            mike.say "Plus you never explained the whole 'friend of a friend' thing either!"
            show amy lying
            amy.say "Look, it's just pretty complicated, that's all."
            show amy normal
            "I shrug my shoulders and shake my head, not knowing what she means."
            "But it doesn't look like I'm going to be able to ask any more questions."
            show bg cinemaroom at dark
            show amy at dark
            with dissolve
            "Because with that, the lights in the theatre go down and the film begins."
        elif date_girl == anna:
            scene bg cinemaroom
            with fade
            show anna b at center, zoomAt(1.25, (640, 880)) with easeinleft
            "As we walk off and find the screen where our film is being shown, I find myself talking about Morgan to Anna."
            "Most likely I'm unconsciously trying to distance myself from the memory of his annoying date with more agreeable ones about Morgan instead."
            mike.say "I can't believe we just bumped into that guy at random."
            mike.say "It's been years since I saw him last."
            show anna stuned
            "Every time I make a statement about Morgan, Anna seems to look at me in a strange manner."
            "It's almost like I think that I'm speaking in English, but something is a little off when she hears it come out of my mouth."
            mike.say "Hey, look...what's up?"
            show anna surprised
            anna.say "What do you mean?"
            show anna sadsmile
            mike.say "Every time I mention Morgan or something about the guy, you look at me like I have steaming turds hanging out of my mouth!"
            mike.say "Plus you never explained the whole 'friend of a friend' thing either!"
            show anna talkative
            anna.say "Look, it's just pretty complicated, that's all."
            show anna normal
            "I shrug my shoulders and shake my head, not knowing what she means."
            "But it doesn't look like I'm going to be able to ask any more questions."
            show bg cinemaroom at dark
            show anna at dark
            with dissolve
            "Because with that, the lights in the theatre go down and the film begins."
        elif date_girl == sasha:
            scene bg cinemaroom
            with fade
            show sasha at center, zoomAt(1.25, (640, 880)) with easeinleft
            "As we walk off and find the screen where our film is being shown, I find myself talking about Morgan to Sasha."
            "Most likely I'm unconsciously trying to distance myself from the memory of his annoying date with more agreeable ones about Morgan instead."
            mike.say "I can't believe we just bumped into that guy at random."
            mike.say "It's been years since I saw him last."
            show sasha stuned
            "Every time I make a statement about Morgan, Sasha seems to look at me in a strange manner."
            "It's almost like I think that I'm speaking in English, but something is a little off when she hears it come out of my mouth."
            mike.say "Hey, look...what's up?"
            show sasha surprised
            sasha.say "What do you mean?"
            show sasha sadsmile
            mike.say "Every time I mention Morgan or something about the guy, you look at me like I have steaming turds hanging out of my mouth!"
            mike.say "Plus you never explained the whole 'friend of a friend' thing either!"
            show sasha shout
            sasha.say "Look, it's just pretty complicated, that's all."
            show sasha normal
            "I shrug my shoulders and shake my head, not knowing what she means."
            "But it doesn't look like I'm going to be able to ask any more questions."
            show bg cinemaroom at dark
            show sasha at dark
            with dissolve
            "Because with that, the lights in the theatre go down and the film begins."
        elif date_girl == minami:
            scene bg cinemaroom
            with fade
            show minami at center, zoomAt(1.25, (640, 880)) with easeinleft
            "As we walk off and find the screen where our film is being shown, I find myself talking about Morgan to Minami."
            "Most likely I'm unconsciously trying to distance myself from the memory of his annoying date with more agreeable ones about Morgan instead."
            mike.say "I can't believe we just bumped into that guy at random."
            mike.say "It's been years since I saw him last."
            show minami stuned
            "Every time I make a statement about Morgan, Minami seems to look at me in a strange manner."
            "It's almost like I think that I'm speaking in English, but something is a little off when she hears it come out of my mouth."
            mike.say "Hey, look...what's up?"
            show minami surprised
            minami.say "What do you mean, big bro?"
            show minami sadsmile
            mike.say "Every time I mention Morgan or something about the guy, you look at me like I have steaming turds hanging out of my mouth!"
            show minami happy
            minami.say "Oh, big bro..."
            minami.say "Even after all this time, you still don't see it?"
            show minami normal
            "I shrug my shoulders and shake my head, not knowing what she means."
            show minami happy
            minami.say "Oh no, I'm not going to get into all of that!"
            show minami normal
            show bg cinemaroom at dark
            show minami at dark
            with dissolve
            "With that, the lights in the theatre go down and the film begins."
        elif date_girl == alexis:
            scene bg cinemaroom
            with fade
            show alexis at center, zoomAt(1.25, (640, 880)) with easeinleft
            "As we walk off and find the screen where our film is being shown, I find myself talking about Morgan to Alexis."
            "Most likely I'm unconsciously trying to distance myself from the memory of his annoying date with more agreeable ones about Morgan instead."
            mike.say "I can't believe we just bumped into that guy at random."
            mike.say "It's been years since I saw him last."
            show alexis stuned
            "Every time I make a statement about Morgan, Alexis seems to look at me in a strange manner."
            "It's almost like I think that I'm speaking in English, but something is a little off when she hears it come out of my mouth."
            mike.say "Hey, look...what's up?"
            show alexis surprised
            alexis.say "What do you mean?"
            show alexis normal
            mike.say "Every time I mention Morgan or something about the guy, you look at me like I have steaming turds hanging out of my mouth!"
            alexis.say "Are you actually serious?"
            alexis.say "You haven't figured it out yet?!?"
            show alexis normal
            "I shrug my shoulders and shake my head, not knowing what she means."
            show alexis happy
            alexis.say "Oh boy!"
            alexis.say "I do not have the energy to get into that tonight."
            show alexis normal
            show bg cinemaroom at dark
            show alexis at dark
            with dissolve
            "With that, the lights in the theatre go down and the film begins."

        elif date_girl == kleio:
            show kleio at center, zoomAt(1.25, (640, 880)) with easeinright
            "I'm still shaking my head when Kleio appears by my side."
            show kleio happy
            kleio.say "So..."
            kleio.say "Was it who you thought it was?"
            show kleio normal
            mike.say "Yeah..."
            mike.say "Yeah, it was."
            mike.say "I can't believe we just bumped into that guy at random."
            mike.say "It's been years since I saw him last."
            scene bg cinemaroom
            with fade
            show kleio at center, zoomAt(1.25, (640, 880)) with easeinleft
            "By now we're in the cinema and looking for our seats."
            "Kleio shrugs as we sit down and get comfortable."
            show kleio talkative
            kleio.say "I know what you mean."
            kleio.say "It's a small, weird world, right?"
            show bg cinemaroom at dark
            show kleio normal at dark
            with dissolve
            "With that, the lights in the theatre go down and the film begins."
        else:
            scene bg cinemaroom
            with fade
            $ renpy.show(date_girl.id, at_list=[center, zoomAt(1.25, (640, 880))])
            with easeinleft
            "As we walk off and find the screen where our film is being shown, I find myself talking about Morgan to [date_girl.name]."
            "Most likely I'm unconsciously trying to distance myself from the memory of his annoying date with more agreeable ones about Morgan instead."
            mike.say "I can't believe we just bumped into that guy at random."
            mike.say "It's been years since I saw him last."
            "Every time I make a statement about Morgan, [date_girl.name] seems to look at me in a strange manner."
            "It's almost like I think that I'm speaking in English, but something is a little off when she hears it come out of my mouth."
            mike.say "Hey, look...what's up?"
            date_girl.say "What do you mean?"
            mike.say "Every time I mention Morgan or something about the guy, you look at me like I have steaming turds hanging out of my mouth!"
            date_girl.say "Isn't it obvious?"
            "I shrug my shoulders and shake my head, not knowing what she means."
            date_girl.say "If you need someone to spell it out for you, then I'm not going to be the one that does!"
            show bg cinemaroom at dark
            $ renpy.show(date_girl.id, at_list=[dark])
            with dissolve
            "With that, the lights in the theatre go down and the film begins."
        "But all I can think about is the weird encounter with Morgan and the way everyone seems to know something I don't."
        menu:
            "It's nothing...":
                "As the trailers roll by and the movie begins, I just can't concentrate on what's happening on the screen."
                "It still bugs me that what should have been a good chance to reconnect with an old friend ended up feeling so awkward."
                "But then I find myself thinking back to my memories of Morgan from when we were kids."
                "Always a little younger than the rest of us, Morgan never quite fitted in as well as most of us did."
                "I guess that all that time that passed since we last met must have added to that, maybe even made it more pronounced."
                "Most likely that was what lay at the root of my worries, and we could always iron that out when we met up in the near future."
            "Something's up":
                "I don't take anything in, from either the trailers or the first part of the film."
                "All I can think about is how oddly Morgan came across and how I was the only one that missed the reason why."
                "Maybe there really were things from our past that I'd assumed didn't amount to anything."
                "Maybe they were still bugging Morgan, even after all this time had passed?"
                "But I realised I was just ruminating on things and getting nowhere."
                "We'd agreed to meet up soon enough, and I could always get to the bottom of the mystery then."
        "Even though I tried, there was no way I could tune back into the movie now."
        "And so I spent the rest of the time in my seat just trying to keep my mind occupied until the time came to leave for home."
        $ renpy.hide(date_girl.id)
    return

label morgan_male_ending:




    if renpy.has_label("morgan_achievement_3") and not game.flags.cheat:
        call morgan_achievement_3 from _call_morgan_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding

    if morgan.male > 66:
        show morgan wedding happy
        with fade
        "When Morgan and I sat down to thrash out the details for the wedding, I really had no idea what she would want."
        "Part of me was sure that it'd be the most unconventional thing imaginable, something that broke all of the rules."
        "Which is why it was a huge surprise to find that we were both thinking of a traditional service in a small church."
        "I guess that when it came down to it, all we wanted was to be marrying each other, and that's all that mattered."
        "But that's not to say everything we came up with was slavishly traditional either."
        "We threw some of the bigger traditions straight to the wind and without hesitation too."
        "That's why there's nobody but the priest standing at the altar right now."
        show morgan at center, zoomAt(1.5, (640, 1040))
        "And why Morgan and I are walking down the aisle to the music we chose together."
        "Before you say it, we're not doing it this way because I'm some kind of submissive pussy either!"
        "It's just that I could never have taken Morgan seriously if she did it the traditional way."
        "Not that there's anything wrong with that - but it's just not her."
        "This way we're doing the whole thing as equals, as partners."
        "Nobody's being given away to anyone or agreeing to obey them like a slave either."
        "We were partners when we were dating, so why should that change once we're married?"
        "And if walking up the aisle together isn't enough of a hint, then maybe Morgan's outfit will do the trick instead."
        "She chose to forego the dress altogether, replacing it with a black suit and white shirt."
        if morgan.is_visibly_pregnant:
            "The cut has been made specifically to accommodate the curve of Morgan's belly, but not to hide it."
            "And she cradles it unconsciously with one hand as her other arm is wrapped in mine."
        else:
            "The colour's perfect, making her electric blue hair all the more striking."
            "And I have to admit that she's making me feel pretty hot right now!"
        "As we approach the altar, I take the chance to lean over and whisper to Morgan."
        mike.say "This is your last chance, Morgan."
        mike.say "They'll be shutting the doors in a second."
        mike.say "If you want to do a runner, now's the time!"
        "Morgan looks up at me, cocking her head on one side as she does so."
        "Her face remains almost perfectly neutral, but I see her lips curl just a little."
        morgan.say "Funny, I was just about to say the same thing to you!"
        morgan.say "But then, you already saw the goods, didn't you?"
        morgan.say "No need to lift my skirt to check I don't have something I shouldn't!"
        morgan.say "You just think about what's in my panties and what we're gonna do when we're all alone..."
        "I want to hear more and I'm about to ask her just what she means when we come to a halt."
        "Glancing up, I see that we're finally standing in front of the altar."
        "Morgan shoots me a wicked smile and then turns her head to look at the priest."
        "The sneaky little minx!"
        "She knew exactly what she was doing just then."
        "Now I'm going to have that image of her panties and their contents on my mind through the whole ceremony!"
        "Priest" "Please be seated."
        "Priest" "Dearly beloved, we are gathered here today to witness the union of these two souls."
        "Priest" "Their joining together in the sacred bonds of holy matrimony."
        "You can pretty much imagine how the rest of it goes."
        "Only the vows are pretty different from the ones that you'd normally hear."
        "Priest" "Do you, Morgan, take [hero.name] to be your lawful partner?"
        "Priest" "Will you love him and keep him as your companion for as long as you both shall live?"
        show morgan blush at startle
        morgan.say "I will."
        "Priest" "Do you, [hero.name], take Morgan to be your lawful partner?"
        "Priest" "Will you love her and keep her as your companion for as long as you both shall live?"
        mike.say "I will."
        "Priest" "Then it is my great pleasure to pronounce you husband and wife."
        "Priest" "You may kiss each other."

        "Yeah, I know, I know."
        "We tried to keep it as equal and equitable as possible, no obeying or cow-towing to anyone."
        "It's all very modern and woke, but it's what we want, and that's all that matters."
        scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
        show morgan kiss wedding
        with fade
        $ morgan.flags.kiss += 1
        "And believe me, the kiss that Morgan plants on me a moment later reminds me why it's worth the effort."
        "I still can't believe that I'm standing here right now."
        "Married to Morgan and looking forward to spending the rest of my life with her."
        "It's crazy to think that I thought I knew her back in the day, but had no idea."
        "And just as insane to realise that I've only really come to understand her so recently."
        "No, just knowing her doesn't even cover the half of it."
        "Come to love her would be closer to the truth."
        "That and come to feel like I can't imagine life without her by my side."
        "Who'd have thought it - the boy I thought I knew turned out to be the girl I love."
        "I don't think I've ever been so happy to be wrong!"

    elif morgan.male > 33:
        "I was kind of worried that planning for the actual wedding might be a little tricky for Morgan and me."
        "You know, what with her having been such a tomboy back in the day and still being so outspoken and feisty in nature."
        "I really had no idea if she was even going to be into any of the more traditional things that come along with a wedding."
        "And I have to admit, a part of me was eager to see what kind of crazy, alternative stuff she might have in mind!"
        "So it came as a surprise to find that Morgan was open to doing things in a pretty conventional way."
        "I might have actually been disappointed were it not for the fact that she made sure to sneak in enough quirk along the way."
        "But in the end, we managed to come up with something that would keep the most fossilised of our elderly relatives happy."
        "And yet we also made sure to add those little touches that made the both of us smile at each other."
        "Those private jokes that you always share as a couple and never let anyone else in on either."
        "You know, like having an instrumental version of 'Dude Looks like a Lady' playing as the guests shuffle into their seats."
        "Yeah, it might sound pretty lame to you."
        "But it's our big day - and all I care about is making sure that Morgan's happy."
        "And while I'm hoping that she's happy right now, I'm starting to feel the nerves setting in."
        "That's because one of the concessions we made towards tradition was to have me standing alone at the altar."
        "Trust me, there's only so many times that you can look a priest in the eye and exchange an awkward smile."
        "And before too long, I'm even beginning to believe that the guy's getting pretty annoyed with me!"
        "But it's just then that a change in the music comes to the rescue."
        "I turn my head just as the entire congregation seems to do the same."
        "The strains of the wedding march are already filling the inside of the church."
        "Now everyone is waiting for the exact same thing."
        "We're all waiting for our first glimpse of Morgan."
        show morgan wedding normal at center, zoomAt(1.0, (640, 740)) with dissolve
        "And when she appears at the far end of the aisle, everyone gets another surprise."
        "Because there she is, looking nothing short of stunning in a pure, white dress."
        "Sorry if you were expecting Morgan to be wearing something radical and outrageous."
        "The truth is that we chose this very dress to make a statement that some might not understand."
        "But I can see the message that it sends in how it shows off each and every inch of Morgan's perfect body."
        "Remember that I started out thinking that she was a guy."
        "And then I found out just how wrong I'd been when she came back into my life."
        "So for us, showing off the fact that she's very much a woman is a pretty important statement!"
        show morgan at center, traveling(1.5, 5.0, (640, 1040))
        if morgan.is_visibly_pregnant:
            "Not to mention the way that the dress can't hope to conceal Morgan's rounded belly."
            "As if there were any better testament to her femininity than that."
            "And I can't begin to express how proud I am to be the father of her child."
        else:
            "And with every move she makes, it seems all the more incredible to me that I ever mistook her for a boy."
            "I can't ever imagine there being a bigger mistake in my life."
            "Or one that I was so happy to be corrected on either."
        show morgan at center, zoomAt(1.5, (640, 1040)) with fade
        "As she finally reaches the altar, I lean and whisper into Morgan's ear."
        mike.say "I can't believe this is actually happening."
        mike.say "You look stunning, Morgan."
        show morgan happy
        morgan.say "Are you sure, [hero.name]?"
        morgan.say "This is kind of the last chance to check under my dress?"
        morgan.say "You know, check I wasn't fooling you this whole time?"
        show wedding morgan with fade
        "I shake my head and chuckle at the gentle ribbing that she's giving me."
        "As far as we've come, I don't know if I'll ever live that one down."
        "Priest" "Ahem..."
        show wedding morgan priest with dissolve
        "The sound of the priest clearing his throat makes the pair of us snap to attention."
        "But even as we turn to face him, I catch sight of Morgan's expression in the corner of my eye."
        "And I see that the grin on her face is a perfect match for the one on mine too."
        "Priest" "Please be seated."
        "Priest" "Dearly beloved, we are gathered here today to witness the union of these two souls."
        "Priest" "Their joining together in the sacred bonds of holy matrimony."
        "After we went through the rehearsal a couple of times, I was sure that I had this whole thing memorised."
        "But the rest of the ceremony soon turns into a blur of half-forgotten words and overwhelming emotions."
        "It's only with the prompting of the priest and the occasional prod from Morgan that I manage to get through it all."
        "Priest" "Do you, Morgan, take this man to be your lawful, wedded husband?"
        "Priest" "Will you honour and obey him, comfort and support him?"
        "Priest" "Comfort him, and, forsaking all others, be faithful to him as long as you both shall live?"
        morgan.say "I will."
        "Priest" "Do you, [hero.name], take this woman to be your lawful, wedded wife?"
        "Priest" "Will you honour and obey her, comfort and support her?"
        "Priest" "Comfort her, and, forsaking all others, be faithful to her as long as you both shall live?"
        mike.say "I...I will."
        "Priest" "And so, it is now my great pleasure to pronounce you husband and wife."
        "Priest" "You may kiss the bride."
        show wedding morgan -priest with dissolve
        "I must have kissed Morgan going on for a hundred times by now."
        scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
        show morgan kiss wedding
        with fade
        $ morgan.flags.kiss += 1
        "But none of them, even the very first one that we shared, ever felt like this one."
        "This one feels like the very first kiss where Morgan and I are equals."
        "It feels like a new beginning."
        "As if all the problems and misunderstandings of the past are behind us now."
        "I never thought of marriage in that way before."
        "As a new start, a different chapter in our lives."
        "But that's what this is."
        "And I feel like I truly know Morgan for the very first time too."
    else:

        "At first I thought that planning the wedding was going to be a real pain in the ass."
        "I mean, don't they say it's as stressful as having a kid or something like that?"
        "But as soon as we actually sat down to thrash it out, Morgan came to the rescue."
        "Turns out that she'd already thought of everything we needed for the wedding beforehand."
        "In fact, she'd planned the entire thing in her head, right down to the smallest detail."
        "So I didn't have to do a thing, as she insisted that I leave almost all of the planning to her."
        "Which I guess is how I come to find myself standing at the altar, staring at the decor in amazement."
        "It's not that I don't like what I'm seeing, or that I'm pretty sure I'd never have picked it in a million years."
        "I just never thought there were actually that many different shades of pink in existence."
        "The entire church is decked out in the colour."
        "There are pink streamers, bows and flowers everywhere."
        "I can hardly see an inch of the place that isn't splashed with it."
        "Going all the way from pastel shades to almost neon tones too."
        "Perhaps the only things that aren't pink are the clothes that the priest is wearing and my own suit."
        "Though I can't help glancing down at the thought."
        "And I note my pink tie and handkerchief that's stuffed in my breast pocket."
        "Another thing I never knew was that Morgan had such a liking for the colour."
        "It seems like an oddly strange thing to discover on your wedding day as well..."
        "Before I can ponder the thought any further, I hear the sound of the organ winding up."
        "And then the church is filled with the strains of the wedding march."
        "Okay, here we go."
        "This is it!"
        "I glance back over my shoulder, straining for catch my first glimpse of Morgan."
        "You might find it strange that I'm so keen to set eyes on a girl I've known for so long."
        "But she was pretty keen on keeping things as traditional as possible."
        "And that includes the groom not allowed to see the dress or the bride before the big day."
        "So I have absolutely no idea what to expect when I do see Morgan walking down the aisle."
        "At first I thought she's definitely go for the more conservative and traditional white."
        "Then it entered my head that all of this tradition might be a front for something else."
        "And maybe she was planning on doing something outrageous when it came to the actual dress."
        "But neither of those notions could have prepared me for what comes striding down the aisle a second later."
        show morgan wedding normal at center, zoomAt(1.0, (640, 740)) with dissolve
        "At first I can't quite make out whether Morgan is actually in the middle of it all."
        "There's so much fluffy, puffed up pink material on show that I have to search to spot her head atop it."
        show morgan at center, traveling(1.5, 5.0, (640, 1040))
        if morgan.is_visibly_pregnant:
            "In fact, the effect is so much, that it's impossible to see the shape of her body."
            "Something which completely hides the fact that she's getting dangerously close to being due."
            "Still, I'm pretty sure our baby's still under there somewhere!"
        else:
            "I watch in amazement as the pink mass that's my bride to be comes ever closer."
            "Still not quite able to believe that she's somewhere in there!"
        "But the very moment that my eyes meet Morgan's, all thoughts of the dress simply disappear."
        "And that's because of the smile that she has on her face."
        "One that lets me know that she's blissfully happy right now."
        "Which is all that matters to me."
        "Any doubts that I might have had about Morgan's choices just don't matter anymore."
        "All of that is just minor details, the things that will be soonest to be forgotten."
        "But the memory of seeing her like this, on the day that we got married."
        "Well, that'll last for a lifetime."
        show wedding morgan with fade
        "Once she's finally made it to the altar, I steal another glance in her direction."
        "Our eyes meet for a second time, and I realise that she was doing the same thing."
        "We gaze at each other for a moment, but then Morgan flushes with colour and looks away."
        show wedding morgan priest with dissolve
        "And it's only the sound of the priest's voice that snaps me back to reality."
        "Priest" "Please be seated."
        "Priest" "Dearly beloved, we are gathered here today to witness the union of these two souls."
        "Priest" "Their joining together in the sacred bonds of holy matrimony."
        "We did talk about writing our own vows, you know?"
        "Going for something that would be personal and unique to us."
        "But in the end, Morgan convinced me that the tried and tested ones were timeless."
        "So those are the ones we went with."
        "And they come around far sooner than I was expecting too!"
        "Priest" "Do you, Morgan, take this man to be your lawful, wedded husband?"
        "Priest" "Will you honour and obey him, comfort and support him?"
        "Priest" "Comfort him, and, forsaking all others, be faithful to him as long as you both shall live?"
        "Morgan nods solemnly, her eyes facing straight forwards and full of determination."
        "Before this moment, I don't know that I'd ever truly appreciated her commitment to this thing."
        "As old-fashioned and cheesy as it sounds, my heart almost skips a beat as I watch her in silence."
        morgan.say "I do."
        "Priest" "And you, [hero.name] - do you take this woman to be your lawful, wedded wife?"
        "Priest" "Will you honour and obey her, comfort and support her?"
        "Priest" "Comfort her, and, forsaking all others, be faithful to her as long as you both shall live?"
        mike.say "I...I do."
        "It's not the pressure of saying the words in front of the congregation that makes me stumble."
        "Nor is it the thought of what being married to Morgan means in terms of responsibility."
        "What's behind it is the fact that she's looking me in the eye as I say them."
        "I don't think I've ever seen another human being look at me quite like that."
        "Like they see their entire future embodied by one person and one person alone."
        "Priest" "And so, it is now my great pleasure to pronounce you husband and wife."
        "Priest" "You may kiss the bride."
        show wedding morgan -priest with dissolve
        "For all of the pleasant traditions associated with marriage, it's not like I need to be told."
        scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
        show morgan kiss wedding
        with fade
        $ morgan.flags.kiss += 1
        "I lean down and kiss Morgan full on the lips, feeling her return the gesture with an equal amount of passion."
        "No matter how many times I say it, I'll still never believe that I once thought she was a boy."
        "Or be able to convey just how glad I am to have been given a chance to discover the truth."


    if morgan.male > 66 and morgan.sub < 33:
        scene morgan househusband ending with fade
        morgan.say "Whew, where should I even start?!?"
        morgan.say "You think it was hard for [hero.name] to get his head around all of this?"
        morgan.say "Where we started from and where we ended up?"
        morgan.say "Never mind all the time in between too!"
        morgan.say "Well, let's just say that you should have seen it from MY side!"
        morgan.say "For the longest time, [hero.name] was just one of those guys from back in the day."
        morgan.say "You know, they were always in there, at the back of your mind."
        morgan.say "But you told yourself that was then and this is now."
        morgan.say "You told yourself that the world had moved on, and so you should too."
        morgan.say "I guess it was only when he walked back into my life that I realised I hadn't done that."
        morgan.say "But it was kinda worse for me, you know?"
        morgan.say "Because it made me question things about myself that I thought I knew for a fact."
        morgan.say "Like, yeah, I always knew that he thought I was one of the guys."
        morgan.say "And yeah, I wanted him to realise he was wrong and..."
        morgan.say "And well...to notice me for what I was!"
        morgan.say "I really though that he'd have wised up since then, to know I was actually a girl."
        morgan.say "So when he had to have Jack take him aside and smarten him up..."
        morgan.say "That really got me thinking about what happened back in the day."
        morgan.say "It made me realise some things about myself too."
        morgan.say "And some of them were pretty uncomfortable."
        morgan.say "I realised that [hero.name] couldn't see me as a girl, even now."
        morgan.say "Which must have meant that it wasn't just inside of his head."
        morgan.say "I always thought that I was sort of...well, a tough chick."
        morgan.say "But the truth was that I'd been putting on a show of being masculine all these years."
        morgan.say "And who else could I be trying to please, other than someone who thought I was a guy?"
        morgan.say "It was pretty scary to realise that I'd spent so long doing that."
        morgan.say "Unconsciously trying to live up to his mental image of me."
        morgan.say "And it was even scarier to think about it and come to the inevitable conclusion."
        morgan.say "Which was that I still loved him, despite all the time we'd been apart."
        morgan.say "That meant it was hard to say yes when he asked me to hang out with him for the first time."
        morgan.say "Sure, he was full of apologies for the mistake he made back in the day."
        morgan.say "But for me, that was kind of a dead issue by now."
        morgan.say "What worried me more was that I couldn't handle his attention, no matter how much I wanted it."
        morgan.say "It's terrifying, to realise that you've had an emotion that strong buried deep inside of you for so long."
        morgan.say "Makes you afraid of what else is lurking inside of your head."
        morgan.say "Could it be like it was when we were younger?"
        morgan.say "Did I even want that, now that he knew the truth about me?"
        morgan.say "Worse was the fear that [hero.name] wouldn't like the boyish girl I'd become."
        morgan.say "But I was determined not to change who I was in the hope of winning him over."
        morgan.say "Because then I would have been doing the same damn thing all over again."
        morgan.say "No, I wanted him to want me for the person I am now, not a fantasy that didn't even exist back then."
        morgan.say "And...well..."
        morgan.say "It was touch and go for a while there, with all of the usual snafus on his part."
        morgan.say "And if I'm honest...probably a couple from me too!"
        morgan.say "But the whole time that we were doing the dating thing, it just felt right."
        morgan.say "Like we were getting to know each other all over again, and for real this time round."
        morgan.say "And [hero.name], he liked what he found in me!"
        morgan.say "Ah, why am I STILL trying to be all tough and macho about this?!?"
        morgan.say "[hero.name] loved what he found in me - there, I said it."
        morgan.say "And I found the same in him."
        morgan.say "I got the guy I always wanted back in high school."
        morgan.say "The one that never saw me in that way even once!"
        morgan.say "But he sees me now - I know that every single time he looks at me."
        morgan.say "And that makes me feel all gooey and girly inside!"
        morgan.say "So what else is there to say?"
        if morgan.is_visibly_pregnant or morgan.flags.mikeBabies >= 1:
            morgan.say "We're looking for a place to settle down."
            morgan.say "Preferably BEFORE the baby arrives!"
            morgan.say "So if you know of anywhere that's decent, let me know real quick."
            morgan.say "Because I feel like I'm going to burst any time soon!"
        else:
            morgan.say "[hero.name] still lives with his housemates, [bree.name] and Sasha."
            morgan.say "But I practically live there too most of the time."
            morgan.say "He keeps saying we have to move out, find a place of our own."
            morgan.say "I don't know though - they look like pretty broad-minded girls to me..."
        morgan.say "Other than that, it's the promise of what's to come that's the best thing in life."
        morgan.say "Knowing that I have the chance to spend it with someone that I always held a candle for."
        morgan.say "As well as the knowledge that they turned out to be so much more than I ever imagined them to be!"

    elif morgan.male <= 33 and morgan.sub >= 66:
        scene morgan housewife ending with fade
        morgan.say "You want me to do this bit?"
        morgan.say "Really?!?"
        morgan.say "Well...okay...if I have to..."
        morgan.say "But if nobody likes what I've got to say..."
        morgan.say "Let's just say that I'm gonna blame you, okay?"
        morgan.say "Right, here goes nothing!"
        morgan.say "Yeah, yeah, I know that you know I'm kinda putting on an act here."
        morgan.say "And I know that you know that I know too."
        morgan.say "But hear me out before you judge me, yeah?"
        morgan.say "[hero.name] and I were never anything but complicated, even when we were just a couple of kids."
        morgan.say "And when I figured out that he thought I was a guy..."
        morgan.say "Well, I'd have punched anyone else right in the gut!"
        morgan.say "But not him."
        morgan.say "I...I never knew why at first, but I just couldn't imagine ever hurting him."
        morgan.say "It'd have felt like I was hitting myself too."
        morgan.say "Looking back, I realise that I was probably in love with him, even then."
        morgan.say "And so I kind of went along with it, because I knew it'd please him."
        morgan.say "Sure, I never came out and said that I was a guy."
        morgan.say "But I never put him right either."
        morgan.say "And I played up to that tomboy image whenever the chance arose."
        morgan.say "Before too long, it became second nature to me."
        morgan.say "Then it just got to be so easy to keep up that it sort of took over."
        morgan.say "Without realising it, the act I was putting on for [hero.name] became the real me."
        morgan.say "After school, when we drifted apart, I was in so deep that even I bought the act."
        morgan.say "And I don't think that I ever wised up to the fact that I was still pretending either."
        morgan.say "At least not until [hero.name] came walking back into my life."
        morgan.say "And when I felt all of those old feelings resurfacing after so long..."
        morgan.say "I guess it was inevitable that everything was gonna get dragged up along with them."
        morgan.say "The elephant in the room was always going to be the big one."
        morgan.say "Of course, he was falling over himself to say how sorry he was."
        morgan.say "And, of course, I told him that it wasn't a big deal, that it was water under the bridge."
        morgan.say "Obviously it wasn't, but that's just what you're expected to say to a guy."
        morgan.say "Also there was the fact that I was getting super interested in reconnecting with him too."
        morgan.say "I mean, I'm only human!"
        morgan.say "I thought that maybe now [hero.name] would see me for who I really was."
        morgan.say "But who in the hell was that anyway?"
        morgan.say "If [hero.name] had never really known the real me, he couldn't know what to expect."
        morgan.say "And that's when the thought hit me."
        morgan.say "What if I tried to show him that I could be as feminine as the next girl?"
        morgan.say "And so I tried it out, dressing and acting as cutesy as I could stomach for him."
        morgan.say "It was hard at first, fighting the instincts that I'd build up over the years."
        morgan.say "But each and every time that [hero.name] seemed to like what I did, it became that much easier."
        morgan.say "Pretty soon he seemed to be sure that I was a sweet, flighty little thing."
        morgan.say "That all I wanted to do was look pretty as I hung off of his arm on a date."
        morgan.say "And the weird thing was that I found myself enjoying it too."
        morgan.say "For the first time in my life, I had [hero.name] doting on me, giving me all of his attention."
        morgan.say "All the while he was falling for a version of me that I'd made up myself too."
        morgan.say "This time I wasn't trying to appeal to his image of me."
        morgan.say "I was making my own image, and he liked it all on his own!"
        morgan.say "I know some of you are gonna get all pissy at me for admitting that."
        morgan.say "And I know that it's not very woke or feminist of me to be acting all girly."
        morgan.say "But it sure is fun!"
        morgan.say "And [hero.name] likes it too!"
        morgan.say "So maybe one day it'll be time to dial it down a little."
        morgan.say "But for now, being all bubblegum and giggles is too good to pass up!"
        if morgan.is_visibly_pregnant or morgan.flags.mikeBabies >= 1:
            morgan.say "Oh, and I mustn't forget that I get to be a mommy too!"
            morgan.say "Mmm...just the thought of pushing a stroller through the park with [hero.name]..."
            morgan.say "It makes me go all weak in the knees!"
        else:
            morgan.say "In fact, [hero.name] and I are thinking of moving in together."
            morgan.say "And I'm SO looking forward to playing the perfect little wife for him too!"
        morgan.say "It's weird, how I always used to think that I was the strong, independent type of girl."
        morgan.say "I spent so long acting like a boy that it became a habit."
        morgan.say "So maybe all I'm doing now is swinging to the other extreme before I can balance out."
        morgan.say "And if that's the case, then I'm gonna enjoy every single moment along the way."
        morgan.say "Because I missed the chance to be with [hero.name] once."
        morgan.say "And pretending to be something I'm not played a big part in that."
        morgan.say "So now I've found a version of me that he loves, why wouldn't I love it too?"
        morgan.say "Because I love him - I know that above everything else."
    else:

        scene morgan ending with fade
        morgan.say "Urrgh..."
        morgan.say "I've been dreading this!"
        morgan.say "And do you know why that is?"
        morgan.say "It's because I know just what everyone's expecting me to come out and say."
        morgan.say "But I'm gonna have to go off-script here."
        morgan.say "You know - be really honest."
        morgan.say "The modern girl in me wants to be all radical feminist, say women can do it on their own."
        morgan.say "And I still believe that, I honestly do."
        morgan.say "The problem is that I've got to come clean when I'm talking about [hero.name] and me."
        morgan.say "When I'm talking about what he means to me and what we mean to each other."
        morgan.say "It all began back when we were kids."
        morgan.say "Specifically with me slowly realising that he thought I was a boy."
        morgan.say "You see, the problem was that it happened at that particular time in life."
        morgan.say "You know what I mean - the time when I started to first notice boys myself."
        morgan.say "To be more clear, when I started to notice [hero.name] in particular."
        morgan.say "I guess that I wanted his attention even back then."
        morgan.say "And the easiest way to get it was to play up to what he expected of me."
        morgan.say "But he never seemed to get the hint, no matter how hard I tried."
        morgan.say "There's an irony there, I think."
        morgan.say "Me trying to be what he wanted me to be."
        morgan.say "And that making me into something he'd never want in that special way!"
        morgan.say "For years it bothered me."
        morgan.say "The fact that I couldn't say for certain if I was meant to turn out that way."
        morgan.say "I mean, I'll always feel an attraction to guys and girls alike."
        morgan.say "But I can never say if I was the person I was for any other reason than trying to please [hero.name]."
        morgan.say "So yeah, when we bumped into each other after all that time, it was a shock."
        morgan.say "I still kind of resented him for what happened back when we were kids."
        morgan.say "But the problem was that I also remembered how he used to make me feel."
        morgan.say "And I found out pretty quickly that he still had that effect on me too!"
        morgan.say "So I decided to give him another chance."
        morgan.say "The apologies were what I expected, nothing special or out of the ordinary."
        morgan.say "But it was the actual process of getting to know him again that made all the difference."
        morgan.say "That was what actually changed my mind, what made me want to see more of him."
        morgan.say "[hero.name] didn't treat me like one of the guys anymore."
        morgan.say "Yet he wasn't turned off when I behaved a little bit like one of them either."
        morgan.say "It felt like he was finally beginning to discover the real me."
        morgan.say "And...well..."
        morgan.say "Let's just say that it makes a girl feel special, yeah?"
        morgan.say "Having a guy that you've always held a torch for paying you that much attention."
        morgan.say "Watching him kind of fall for you..."
        morgan.say "Ah...shit!"
        morgan.say "I'm getting all emotional."
        morgan.say "But so what - are you gonna shoot me for that?"
        morgan.say "So yeah, maybe [hero.name] had a lot to do with the direction that my life took."
        morgan.say "Yet I'd like to think that's not really a negative thing, you know?"
        morgan.say "I'm not the kind of girl to believe in destiny, soul-mates and all that crap."
        morgan.say "But I do believe that you sometimes meet a person that has a kind of pull on your life."
        morgan.say "And for me, [hero.name] was that person."
        morgan.say "Let's not say it was written in the stars."
        morgan.say "Just that we had a second chance and took it."
        morgan.say "It's still early days, maybe too early to be talking about growing old together."
        if morgan.is_visibly_pregnant or morgan.flags.mikeBabies >= 1:
            morgan.say "All we really have time for right now is getting ready for the baby's arrival anyway."
            morgan.say "There's so much to think of, but we've deliberately decided not to find out if it's a boy or a girl."
            morgan.say "Because, with our track record, we're going to be easy and take things as they come!"
        else:
            morgan.say "For now, it's enough to be making plans to find a place to live together."
            morgan.say "Maybe even think about whether or not we want to start a family of our own."
            morgan.say "And with our track record, neither of us is worried about having boys or girls!"
        morgan.say "Whatever happens, I think that, between us, we're strong enough to handle it."
        morgan.say "After all, we waited so long to be together in the first place."
        morgan.say "And I'm not about to allow anything save for an end-of-the-world scenario end it now!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not morgan.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_16
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_16
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label morgan_preg_talk:
    show morgan casual
    mike.say "Morgan...hey there."
    mike.say "Are you okay?"
    if morgan.male >= 75:
        "She looks at me whilst shaking her head and making a resigned sighing sound."
        morgan.say "There's no easy way to say this, [hero.name], so I'm just going to come out and say it."
        morgan.say "I'm pregnant, and it's yours."
        morgan.say "And...and, well...you're just gonna have to man up!"
        "There are times when Morgan's blunt nature makes things so much easier than they might otherwise be."
        "But suffice to say, this isn't one of those time."
        "The bald nature of the statement leaves me feeling like I've been punched in the gut."
        morgan.say "[hero.name]...you're supposed to say something!"
        mike.say "Sorry, Morgan - you just kind of took me by surprise..."
    elif morgan.male >= 25:
        "Now that she's looking me straight in the eye, I can see a measure of fear that wasn't apparent beforehand."
        morgan.say "[hero.name]...I was late this month, so I took a pregnancy test, just to be sure..."
        "I wait for her to go on, feeling my mouth go dry as the silence stretches by seconds to a minute."
        mike.say "And...what did it say?"
        morgan.say "It was...it was positive - I'm pregnant!"
        "All that I can do at first is puff out my cheeks and then blow the air out of my lungs in a long sigh."
        "I want to say something that will reassure Morgan and make everything alright."
        "But the news is so monumental that I'm having enough trouble processing it myself right now."
        mike.say "Morgan...I...I don't know what to say!"
    else:
        show morgan sad
        "Morgan lays her head on my shoulder, and I can feel that she's scared of something."
        morgan.say "Oh, [hero.name]...I have to tell you something."
        morgan.say "You're going to be a daddy!"
        "It takes me a moment to get my head around what she just said."
        "But then the truth of what she's saying dawns on me."
        mike.say "Morgan, are you saying that you're pregnant?!?"
        "At this, she looks up from my shoulder, her eyes wide and seductive."
        morgan.say "Uhuh, [hero.name] - I'm pregnant, and you're the father!"
    show morgan normal
    "I want to come over as the strong, masculine type, really I do."
    "But after all that I've been through with Morgan already, the emotional roller-coaster it's been, discovering there's another time around the loops is really making that almost impossible to manage."
    mike.say "What...what do you want to do, Morgan?"
    "Morgan looks at me hard for a moment, but then her expression softens by a couple of degrees."
    "I think that she was expecting me to step up and take control, but now realises the enormity of it all has hit me hard too."
    if morgan.love >= 150:
        morgan.say "I think that I want to keep the baby, [hero.name]."
        morgan.say "But I can't do it on my own..."
        "There's no need for Morgan to complete that last statement."
        "I already know what she meant to say and just what it means for me."
        menu:
            "Refuse":
                $ morgan.set_gone_forever()
                mike.say "Morgan...I can't be a father right now."
                mike.say "I'm not prepared for that kind of responsibility..."
                "I hate myself even as I say the words, but I have to be brutally honest."
                if morgan.male >= 75:
                    show morgan angry
                    "Morgan looks at me as though she's disgusted at first."
                    "But then she looks away and shakes her head, emotion seeming to get the better of her."
                    morgan.say "I...I thought you'd be a man about this, [hero.name]."
                    morgan.say "But I guess I'll have to be man enough for both of us!"
                    "She shakes her head again and turns her back on me as she does so."
                    morgan.say "I'm not sure I know where this leaves me...or us!"
                elif morgan.male >= 25:
                    "There's the slightest hint of tears in Morgan's eyes as she nods, her lip quivering just a little."
                    morgan.say "Well, I guess that's that..."
                    morgan.say "We should have been more careful and used a..."
                    "She stops before she can speak the last few words, something seeming to break inside of her."
                    morgan.say "Fucking hell, [hero.name] - I really thought there was more to us than this!"
                    "She shakes her head and looks away, as though she can't bring herself to as much as look at me right now."
                else:
                    "Morgan looks up at me with tears in her eyes."
                    "I can see that she's doing her best not to cry."
                    morgan.say "How could you, [hero.name]?"
                    morgan.say "I'm not just a toy for you to play with and toss away like garbage!"
                    "She spins on her heel and refuses to look me in the eye any longer."
                    morgan.say "How could I have been so wrong about you?"
            "Accept":
                $ morgan.flags.toldpreg = True
                mike.say "Morgan...of course I'll be there, for you and the baby!"
                mike.say "How could you even think that I wouldn't want that?"
                $ morgan.love += 10
                "I haven't had time to really think about what I'm saying or practise the lines."
                "I'm just saying what comes naturally to me on the spur of the moment."
                if morgan.male >= 75:
                    "Morgan's eyes widen a little, almost as though she's surprised at my enthusiasm."
                    "I see her relax just enough to let the worry and weariness that must have been eating at her show through."
                    morgan.say "You...you really mean that?"
                    morgan.say "You want the baby...and me?"
                    mike.say "Of course I mean it, Morgan."
                    mike.say "How could you even think that I'd not be serious about something like this?"
                    "Morgan wraps her arms around me suddenly, pulling me into a tight embrace."
                    "It feels to me like she's accepted something deep inside, something that means she doesn't need to act so tough anymore."
                elif morgan.male >= 25:
                    "Morgan's eyes show her emotions, small tears forming in the corners that she wipes away quickly."
                    morgan.say "Is that the truth - do you really want to make a go of this with me?"
                    mike.say "Morgan, of course I do."
                    mike.say "I don't think we should see this as an accident, but a chance to do something amazing together."
                    "Morgan wraps her arms loosely around my waist and leans her head into my shoulder."
                    morgan.say "I don't know how you do it, [hero.name] - but you make this whole thing sound simply wonderful."
                    mike.say "Don't worry, it will be - because we'll make it wonderful together."
                else:
                    "I watch as Morgan clasps her hands together and smiles."
                    morgan.say "Oh, [hero.name] - sometimes, you really are my hero!"
                    morgan.say "I know we're going to make a great little family."
                    "Morgan reaches up and wraps her arms around my neck, pulling me down to her level."
                    "Her lips are right next to my ear as she whispers to me."
                    morgan.say "I'm gonna make you so happy that you'll never want to let me go [hero.name] - just you wait and see!"
    else:
        morgan.say "I don't know about you, [hero.name], but I'm just not ready to be a parent, not right now."
        morgan.say "I've thought long and hard about this before I told you, and I think that I want to have a termination."
        "Things seem to be happening so fast, I feel as though I can't keep up."
        "First Morgan tells me she's pregnant, and now she hits me with the fact that she wants to get rid of it!"
        menu:
            "Agree":
                $ morgan.unpreg()
                mike.say "I...I suppose that it's your decision, Morgan."
                mike.say "I can't tell you what to do when it comes to your own body..."
                "I feel like I'm taking the easy way out by not challenging her on this one."
                "But do I really want a fight on my hands over something like this?"
                if morgan.male >= 75:
                    "Morgan's expression hardens, and she nods a little whilst looking away from me for a moment."
                    "I get the distinct feeling that she was preparing herself for a fight on this one."
                    morgan.say "Y...yeah, it is...of course it is!"
                    morgan.say "I just wanted to level with you, yeah?"
                    morgan.say "I feel better knowing that we're both on the same page."
                    "She clasps my hand, and I return the gesture."
                    "Neither of us speaks, but that's a relief as, under the circumstances, I have no idea what to say."
                elif morgan.male >= 25:
                    "Morgan gives me a smile at this, but it's a hard one and I can see that it's concealing her deeper emotions."
                    "She almost starts to break down, and then fights back the urge and wipes a tear from the corner of her eye."
                    morgan.say "I...I really think it's for the best, don't you?"
                    mike.say "Yeah...I mean, yes - yes it is, Morgan."
                    mike.say "We can't just sleepwalk into something like this."
                    "Morgan looks up at me, and I can't keep the emotion out of my own face either."
                    "At the sight of this, she clasps both of my hands in her own and offers me a fragile, but somehow more bitter-sweet smile."
                else:
                    "Morgan leans against me, and I take her in my arms on instinct."
                    "Her head rests upon my chest, and I can hear her fighting off tears."
                    mike.say "It's okay, Morgan."
                    mike.say "Whatever happens, I'm here for you."
                    "Morgan looks up at this, catching my eye."
                    "She smiles weakly, and I feel my heart almost break for her."
                    "She's trying the best she can to be strong, but her heart must be breaking too."
            "Protest":
                $ morgan.flags.toldpreg = True
                mike.say "Morgan, no - you can't do that...I won't let you!"
                mike.say "The child that you're talking about is a part of me too."
                "I don't know where this will to fight for the life of an unborn child is coming from."
                "All I do know is that it feels totally wrong to end a life before it's even begun."
                if morgan.male >= 75:
                    morgan.say "Well...well..."
                    morgan.say "Maybe you should have thought about all of this."
                    morgan.say "You know - BEFORE you went and knocked me up, huh?"
                    "The aggression and anger with which Morgan spits her initial response soon drains out of her face once the words are spoken."
                    morgan.say "Urrggh...I'm sorry, [hero.name] - but this is such a fucking mess!"
                    mike.say "You're right, Morgan - but we both made that mess."
                    mike.say "What kind of people are we if we just turn tail and run from it?"
                    morgan.say "I...I hear what you're saying..."
                    "I take hold of her hand and squeeze it, trying to show that even though I don't have an answer, I'm not going anywhere."
                elif morgan.male >= 25:
                    "Morgan regards me with what looks like surprise at my sudden outburst against her plan to have a termination."
                    morgan.say "I...I suppose you're right, [hero.name]."
                    morgan.say "I guess I just assumed that you'd be a typical guy and freak out at the idea."
                    morgan.say "I'm sorry...I should have asked you first."
                    "I nod my head slowly."
                    mike.say "It's okay, Morgan, I understand - you're scared, and so am I."
                    mike.say "Can we just talk this over before we make such a massive decision?"
                else:
                    "Morgan leans against me, and I take her in my arms on instinct."
                    "Her head rests upon my chest, and I can hear her fighting off tears."
                    morgan.say "I...I'm more than a little scared, [hero.name]!"
                    morgan.say "Scared of the operation - but more scared of being a mother!"
                    "I pull her closer to me, trying to reassure her with the warmth of my body."
                    mike.say "It's...it's going to be okay, Morgan."
                    mike.say "Don't worry about anything...I'll make sure that you're alright."
    "There's a part of me that wonders if any of this would have come to pass had my relationship with Morgan been different back in the day."
    "Was it the years of her holding a candle for me and my own thinking that she was a guy cause us to be this emotionally volatile when we finally came together?"
    return

label morgan_male_90:
    show morgan
    morgan.say "Does it bother you that you thought I was a boy for, what, fifteen years or something?"
    mike.say "In my defense there was at least a five year gap where I didn't see you at all in there."
    morgan.say "You're dodging the question."
    mike.say "Fine. A little, yes, it makes me feel...dense at best, idiotic at worst."
    mike.say "Does it bother you that I thought you were a boy?"
    morgan.say "Well. No. And yes. And no."
    mike.say "That's a very clear answer."
    morgan.say "It didn't bother me that you thought I was a boy. It bothered me that {b}you{/b} thought I was a boy."
    mike.say "Less clear."
    morgan.say "That's all I got."
    hide morgan
    return

label morgan_male_80:
    show morgan
    morgan.say "I'm not gay, you know."
    mike.say "What?"
    morgan.say "Look, I know you thought I was a boy so I could ask girls out."
    mike.say "I did?"
    morgan.say "You did."
    mike.say "I...think maybe you're projecting."
    morgan.say "Fine, I did actually want to ask ... a couple of girls out."
    if 'morgan_kleio_event_01' in DONE:
        mike.say "And you dated Kleio."
    morgan.say "Yes, I like girls. But I like boys too. So I'm not gay."
    mike.say "But..."
    morgan.say "I prefer queer. Or pan. Bi if you must, but I dunno, I don't like the sound of it."
    mike.say "Okay, sure."
    morgan.say "Glad we cleared that up."
    hide morgan
    return

label morgan_male_60:
    show morgan
    morgan.say "What do you think it means that I act like a boy?"
    mike.say "Do you act like a boy? I mean you dress like one, sure, but I don't think it's necessarily the same thing."
    morgan.say "When we were kids I absolutely acted like a boy. Not so much now, maybe."
    mike.say "Are you sure?"
    morgan.say "Well. Maybe I acted like what I thought boys acted like."
    mike.say "Okay, I'll buy that."
    morgan.say "But..."
    mike.say "Yes?"
    morgan.say "This might sound weird, but I didn't ever actually want to be a boy."
    mike.say "What?"
    morgan.say "I tried to be tough, I wanted to hang with you and Jack, and maybe go make out with Alexis."
    mike.say "Hey! She was my girlfriend!"
    morgan.say "She wasn't always your girlfriend!"
    mike.say "I didn't realize I was competing with you."
    morgan.say "Well that's the thing, I was hardly competition. I didn't want to be a boy..."
    mike.say "But?"
    morgan.say "I didn't really want to be a girl, either."
    mike.say "Then what?"
    morgan.say "I don't know. Something in between?"
    mike.say "Ahh. A confusing place to be."
    morgan.say "Now you're getting it."
    hide morgan
    return

label morgan_male_50:
    show morgan
    morgan.say "I've been thinking a lot about something."
    mike.say "What's that?"
    morgan.say "Well, it's that I don't want to be a boy. I know that now, for sure."
    morgan.say "But I don't want to be a girl, either."
    mike.say "Why not?"
    morgan.say "See, that's what I've been trying to figure out. I don't actually know."
    menu:
        "You should be a girl":
            mike.say "The more I've gotten to know you, the more I like the idea that you're a girl, you know?"
            morgan.say "But I don't want to be that."
            mike.say "Well. Maybe when you figure out why it'll be different."
            $ morgan.love -= 2
            $ morgan.sub += 2
            morgan.say "Maybe."
        "You should be whatever you want to be":
            mike.say "You can be whatever you want to be. You know that, right?"
            morgan.say "Yeah. Yeah, I can. And I do know that."
            morgan.say "But it's good to hear that."
            $ morgan.love += 2
            $ morgan.sub -= 2
    hide morgan
    return

label morgan_male_40:
    show morgan
    morgan.say "How do you like my new wardrobe?"
    mike.say "It's really cute on you."
    if morgan.sexperience > 1:
        mike.say "It's really cute off of you, too!"
    morgan.say "Yeah, you like it? Thanks to you, I thought I'd start mixing it up a little. I'm trying out makeup too."
    mike.say "What changed? You didn't want to be a girl, but you're really starting to dress like one!"
    morgan.say "I have an idea, but I'm not sure."
    mike.say "Care to tell me?"
    morgan.say "No, not yet."
    mike.say "Whenever you're ready."
    morgan.say "Thanks, [hero.name], I appreciate that."
    hide morgan
    return

label morgan_male_20:
    show morgan
    morgan.say "I figured it out."
    mike.say "Figured what out?"
    morgan.say "Why I didn't want to be a girl. And it's so stupid."
    mike.say "What is it?"
    morgan.say "It's my dad. And Jack, too actually, but mostly my dad."
    mike.say "What did he do?"
    morgan.say "When I was little, I was...really clumsy, and I broke something of my dad's. And he got {b}really{/b} mad."
    morgan.say "And...God I didn't even really remember this until recently, but he was screaming at me, and my mom stepped between us."
    morgan.say "And I remember him shouting that girls fuck everything up."
    morgan.say "My mom and he got divorced a few years later, and I kind of forgot about it. Except I didn't."
    morgan.say "I always remembered that girls fuck everything up. And I fucked everything up. And I thought it was because I was a girl."
    mike.say "That's harsh."
    morgan.say "Yeah, right? But it's not. It's not because I'm a girl, and I feel so stupid for pretending for all those years."
    mike.say "Don't feel stupid, Morgan. Maybe you've changed your mind, but it made you what you are."
    mike.say "You just wanted to make yourself a better person. It sucks that you didn't know the right way to do it."
    mike.say "But no one can fault you for trying."
    morgan.say "That's so sweet of you to say, [hero.name]. Thank you!"
    hide morgan
    return

label morgan_react_kylie_sentence:
    "I've kind of been dreading bumping into people since the news of Kylie's sentence got out."
    "It's bad enough trying to come to terms with the fact she's been given the death sentence."
    "But on top of that I now have to listen to everyone that I know giving me their take on it too!"
    "So when I see Morgan hurrying towards me, all I can do is take a deep breath and prepare myself."
    "Hell, I even manage to force a smile onto my face too."
    show morgan sad
    morgan.say "[hero.name]…"
    morgan.say "I'm so glad I managed to find you."
    mike.say "Hey, Morgan..."
    mike.say "That can't have been too easy for you."
    mike.say "I've kind of been keeping my head down recently."
    "The moment that she sees me up close, Morgan's expression becomes one of concern."
    "Most likely because she can now see how pained I look and how fake my smile is."
    "But rather than feeling vindicated by that, I find that it just makes me feel dejected."
    "Because what I can see on Morgan's face is the genuine concern of a friend."
    "And that makes me regret trying to avoid the people that actually care for me."
    show morgan annoyed
    if morgan.male <= 33:
        morgan.say "I was gonna say that it was good news..."
        morgan.say "That the psycho bitch is getting what she deserves."
    elif morgan.male <= 66:
        morgan.say "I was going to say that at least it's all over."
        morgan.say "That now you can draw a line under all of this."
    else:
        morgan.say "I was going to say that I was sad to hear the news."
        morgan.say "That I felt safer knowing that she'll be gone."
    "Morgan pauses to take a deep breath."
    "And in that moment she takes a step forward, putting a hand on mine."
    show morgan sad
    morgan.say "But now I can see that none of that's really important."
    morgan.say "I shouldn't be talking about how this is making me feel."
    show morgan sadsmile
    morgan.say "I should be asking how it makes you feel, [hero.name]!"
    "All I can do is shake my head, trying to hold my emotions in check."
    "I thought that I was dealing with all of this pretty well."
    "That I could just keep my head down and tough my way through it."
    "But Morgan's presence somehow makes me want to just let it all out."
    "So I take hold of her hand, squeezing it tightly."
    mike.say "I..."
    show morgan sad
    mike.say "I don't know, Morgan."
    mike.say "Part of me feels like I should be happy with the sentence."
    mike.say "Kylie did a horrific thing, and she's being punished for it."
    mike.say "But somehow it still doesn't make me feel any better."
    mike.say "Sure, she won't be able to do anything to harm me or anyone else."
    mike.say "But it still doesn't undo what happened."
    mike.say "It's not like killing one person brings another back from the dead!"
    "Now I can feel Morgan squeezing my hand in return."
    "She's nodding as I try to explain myself too."
    morgan.say "I know, [hero.name], I know..."
    morgan.say "Kylie will be gone."
    morgan.say "And her victims are still here."
    show morgan sadsmile
    morgan.say "But so am I!"
    morgan.say "And so are all the people that love you."
    "Looking into Morgan's eyes, I start to feel something that I haven't in a long time."
    "It's an odd little feeling, right down in the core of my being that seems to be growing."
    "And when I finally figure it out, I realise that it can only be hope."
    "Sure, it's small and it feels kind of like a tiny little flame."
    "But if I can nurture it, keep it from being extinguished."
    "Then it might start to grow."
    mike.say "You know what, Morgan..."
    show morgan surprised
    mike.say "You're right!"
    morgan.say "I am?"
    show morgan normal
    morgan.say "I mean...of course I am!"
    mike.say "Maybe I can beat this thing."
    mike.say "So long as I have you to help me."
    "Morgan nods her head eagerly."
    "Keen to do all that she can to make it happen."
    show morgan wink
    morgan.say "Whatever you need, [hero.name]…"
    morgan.say "I'm here for you!"
    return

label morgan_birthday_date_male:
    $ DONE["morgan_birthday_date_male"] = game.days_played
    if morgan.male >= 50:
        call morgan_birthday_date_tomboy from _call_morgan_birthday_date_tomboy
    else:
        call morgan_birthday_date_feminine from _call_morgan_birthday_date_feminine
    return

label morgan_birthday_date_tomboy:
    $ game.active_date.clothes = "casual"
    scene bg street with fade
    "Sometimes it can be pretty hard to figure out what will win Morgan over."
    "And even harder to know what will land me in deep trouble with her too."
    "But as her birthday has been fast approaching, I've spent time wracking my brains."
    "And I feel pretty confident that I've managed to arrange something special."
    "So when the big day comes around, I'm feeling pretty confident in my plans."
    "But that confidence begins to feel like it's being slowly eroded."
    "Because I keep looking at the time, noting that it's past when we agreed to meet."
    "Morgan's officially late, and she hasn't even bothered to call ahead and tell me."
    "Which means that when she finally shows up, I'm feeling more than a little flustered."
    show morgan at center, zoomAt(1.5, (940, 1040)) with easeinright
    morgan.say "Hey, [hero.name]..."
    morgan.say "How's it hanging?"
    "Morgan looks me in the face for a moment."
    "And then she seems to realise what's wrong."
    show morgan surprised at center, zoomAt(1.5, (640, 1040)) with ease
    morgan.say "Ah, shit..."
    morgan.say "What time was I supposed to be here again?"
    morgan.say "Am I late?"
    menu:
        "I laugh off Morgan being late":
            "I put a smile on my face, hoping that it looks genuine."
            "And then I add a casual shrug, waving away her concerns."
            mike.say "Oh, it's no problem, Morgan..."
            mike.say "It's only a couple of minutes really."
            mike.say "Nothing to worry about."
            show morgan angry
            "Morgan frowns as she listens to my response."
            "And then she shakes her head."
            morgan.say "You do know that you can be pissed off with me, right?"
            morgan.say "Like, I won't instantly dump you for telling me off!"
            "I blink a couple of times, not really knowing what to say."
            "I'm not used to a girl giving me permission to be mad at her."
            mike.say "I...I guess so, Morgan..."
            mike.say "I just didn't want to start the date on a bad note, that's all!"
            morgan.say "Yeah, yeah..."
            morgan.say "Whatever, [hero.name]."
            morgan.say "I just never remembered you being this much of a doormat!"
            $ game.active_date.score -= 30
        "Lets Morgan know im upset at her being late":
            "I can't help frowning a little and cocking my head on one side."
            "Because I'm not sure I'm comfortable with just glossing over it."
            mike.say "Yeah, Morgan..."
            mike.say "You kind of are!"
            mike.say "Not enough to screw things up though."
            "Morgan nods as she listens to my answer."
            "And she looks like she's taking it pretty well."
            show morgan sad
            morgan.say "I'm sorry, okay?"
            morgan.say "I can be a little slack when it comes to time-keeping."
            morgan.say "But thanks for telling it how it is, yeah?"
            morgan.say "I just hate it when people try to coddle me."
            "I blink a couple of times, not really knowing what to say."
            "I'm not used to a girl thanking me for telling her off."
            mike.say "I do kind of feel like a jerk complaining, Morgan."
            mike.say "But if you prefer things that way..."
            mike.say "Then I'll try to keep it in mind."
            show morgan normal
            morgan.say "I'd like that, [hero.name]..."
            morgan.say "You know, I never had you down as a door-mat kind of guy!"
            $ game.active_date.score += 30
    "Morgan claps her hands together, making me jump a little."
    "Then she looks around, turning on her heels as she does so."
    show morgan normal
    morgan.say "So..."
    morgan.say "What the fuck are we here for?"
    "As Morgan turns around, I wait for her to be facing in the right direction."
    "And then I put my hands on her shoulders, gently holding her in place."
    mike.say "Ta da!"
    mike.say "There you go, Morgan..."
    show morgan surprised at startle
    morgan.say "NO WAY!"
    morgan.say "Are you for real?"
    morgan.say "We're going go-karting?!?"
    mike.say "Oh yeah, you bet we are!"
    show morgan happy
    morgan.say "Yes!"
    morgan.say "I am SO going to kick your ass!"
    "I'm seriously delighted with the enthusiasm Morgan's showing."
    "Though maybe just a little worried that she wants to beat me so badly."
    "But I do the best I can to put that thought out of my head."
    "And instead I lead her inside so that we can get down to some actual racing."
    scene bg kart with fade
    "As we walk through the doors, I see that there's a queue to get served."
    "Not a massive one, but we'll still probably be waiting a couple of minutes."
    show morgan sad at center, zoomAt(1.5, (640, 1040))
    morgan.say "Urgh..."
    morgan.say "Why is there always a damn queue?"
    "I happen to be looking back over my shoulder as Morgan says this."
    "And I see a large group of people walking in behind us."
    mike.say "Maybe it's not so bad, Morgan..."
    mike.say "At least we made it in before they did!"
    "Morgan looks behind her too, and so she sees what I mean."
    "A moment later, the lobby behind us fills up with bodies."
    "Most seem to be parents with small children in tow."
    "And in the confusion, they all seem to be stepping in and out of the queue."
    "I see one kid that seems to be doing it on purpose."
    "Weaving around the other adults without being seen."
    "And then his parents are following on his heels."
    morgan.say "You see that too, right?"
    show morgan angry
    morgan.say "They're using their kid to jump the queue!"
    "Soon enough they reach our point in the queue."
    "And it looks like they're going to try the same thing."
    "Morgan's about to say something to the family in question."
    menu:
        "Stop Morgan from confronting the family":
            "Quick as a flash, I reach out and pull Morgan aside."
            "This means that she's distracted as the family get to us."
            "And also that their little scam goes off without a hitch."
            morgan.say "What the..."
            morgan.say "Why did you do that?"
            morgan.say "Now they're going to get in before us!"
            "I shake my head and roll my eyes."
            mike.say "Don't you think you're being a little petty, Morgan?"
            mike.say "Sure, it's annoying and those guys are jerks."
            mike.say "But you can rise above them, rather than sinking to their level."
            "Morgan mutters and mumbles under her breath."
            "And I can tell that she's far from pleased."
            "But her being pissed for a short while is something I can handle."
            "And far easier to deal with than her making a scene in public."
            $ game.active_date.score -= 20
        "Stick my foot out in front of the kid":
            "At just the moment the kid tries to sneak past, I stick out my foot."
            "And with perfect timing, he trips over it, landing in a heap on the floor."
            "Luckily for me, the lobby is too crowded for anyone to have seen me do it."
            "So everyone just seems to assume the kid tripped over his own feet."
            "Of course the parents hurry to comfort the little brat."
            "But as they do so, people in the queue start to notice they're cutting in line."
            "Morgan and I step forwards and up to the desk as an argument breaks out behind us."
            morgan.say "Don't try to act all casual with me."
            morgan.say "I saw what you did back there!"
            "I shrug, trying to act like it was nothing."
            mike.say "They were fucking with us."
            mike.say "So I fucked with them."
            mike.say "Fair payback, if you ask me."
            "Morgan nods, clearly agreeing with the sentiment."
            show morgan happy
            morgan.say "Well said!"
            morgan.say "Let's just hope they learn their lesson."
            $ game.active_date.score += 30
    "Once we're at the front of the queue, it doesn't take long to get sorted."
    "In no time at all we're putting on crash helmets and choosing our carts."
    "Morgan practically leaps into hers, champing at the bit to get going."
    morgan.say "Come on, [hero.name]..."
    show morgan happy
    morgan.say "Let's go already!"
    mike.say "What's the hurry, Morgan?"
    mike.say "Are you that keen to get beaten?"
    morgan.say "Oooh..."
    morgan.say "Those are fighting words!"
    "As soon as both of us are strapped in, I stamp down on the accelerator."
    "But Morgan must be doing the same thing at the same time."
    "Because we both screech onto the circuit at the same time."
    hide morgan with easeoutright
    if hero.has_skill("racing") or hero.has_skill("sneaky") or hero.has_skill("video_games"):
        menu:
            "Race like a pro" if hero.has_skill("racing"):
                "I deliberately neglected to tell Morgan that I've been go-karting before."
                "Well, it'd be more honest to say that I've been go-karting a hell of a lot."
                "Far more than the average person and almost to the point where I'm as good as a pro."
                "So I guess that she's just going to have to deal with learning that on the track!"
                "I play up to Morgan by not going in for the kill from the start."
                "And this seems to do the trick, lulling her into a false sense of security."
                "But the truth is that I have her just where I want her the whole time."
                "So all I need to do is choose the right moment to flip the race."
                "Luckily for me, Morgan seems to be totally engrossed in trying to win."
                "Which means that she doesn't even notice that I'm holding back."
                "Suddenly I see the perfect opportunity present itself."
                "And when that happens, I go in for the kill!"
                "Just before the last corner of the final lap, I swing into action."
                "Then I catapult myself past Morgan and into first place."
                "My kart shoots over the finishing line, leaving her in a distant second."
                "As soon as we stop, Morgan hurries over, pulling off her helmet."
                show morgan surprised
                morgan.say "Whoa..."
                morgan.say "Where did you learn to drive like that?"
                mike.say "Now that would be telling."
                mike.say "And I like to maintain an air of mystery!"
                $ game.active_date.score += 20
            "Wait for an opening to pass" if hero.has_skill("sneaky"):
                "The honest truth is that I've only been go-karting a couple of times."
                "And I'm probably only as good as any other amateur behind the wheel."
                "So that means I'm going to have too get creative out there on the track."
                "And the best way I know to do that is using my wits and outsmarting Morgan."
                "When Morgan and I first pull out onto the track, things are pretty much even."
                "We're fighting to get around each other, and there's really nothing in it."
                "But I already have my eye out for any potential chance to change all of that."
                "And the moment I see one, I don't hesitate to take it."
                "Unfortunately for her, Morgan doesn't seem to be thinking the same way."
                "So she's taken by complete surprise when I do something sneaky."
                "And what's more, the shock of it only seems to make things worse."
                "Morgan's thrown off balance and starts to fall behind."
                "Of course I don't even think of showing mercy, not for a second."
                "And I take whatever short-cuts I can to keep ahead for the rest of the race."
                "Morgan does the best she can to catch up to me."
                "But it's just not enough, and I pass the finish-line in first place."
                "Leaving Morgan a distant second."
                "As soon as we stop, Morgan hurries over, pulling off her helmet."
                show morgan angry
                morgan.say "You sneaky bastard!"
                morgan.say "Where did you learn so many dirty tricks?"
                mike.say "Now that would be telling."
                mike.say "And I like to maintain an air of mystery!"
                $ game.active_date.score += 20
            "I am a pro on arcade this should not be more complicated" if hero.has_skill("video_games"):
                "The honest truth is that I've only been go-karting a couple of times."
                "And I'm probably only as good as any other amateur behind the wheel."
                "But one advantage I do have is hours and hours spent playing racing games."
                "So I figure that I can use that experience to my advantage here, right?"
                "When Morgan and I first pull out onto the track, things are pretty much even."
                "We're fighting to get around each other, and there's really nothing in it."
                "But my brain is already gearing up to spot potential uses of my gaming knowledge."
                "I'm trying to recall racing around the track in all those videogames."
                "And the moment I think I see a familiar situation, I leap into action."
                "On a sharp corner, I feel my kart drifting, just like in a game."
                "So I throw the wheel into it and try to drift the way I would when playing."
                "And much to my delight, it seems to work!"
                "I go sailing past Morgan and out of the bend in the lead."
                "After that the chances seem to be come easier to spot."
                "The real simulated experience of the games matching up to reality."
                "Which means I can take full advantage and keep ahead of Morgan."
                "Most of the time she's still breathing down my neck."
                "And Morgan does the best she can to catch up to me."
                "But it's just not enough, and I pass the finish-line in first place."
                "Leaving Morgan a distant second."
                "As soon as we stop, Morgan hurries over, pulling off her helmet."
                show morgan surprised
                morgan.say "How did you do that?"
                morgan.say "You have to teach me those tricks!"
                mike.say "Now that would be telling."
                mike.say "And I like to maintain an air of mystery!"
                $ game.active_date.score += 20
    else:
        "The honest truth is that I've only been go-karting a couple of times."
        "And I'm probably only as good as any other amateur behind the wheel."
        "So that means I'm going to have to rely on my own wits to beat Morgan."
        "But that can't be too hard, right?"
        "I mean, I'm not saying that I'm smarter than her."
        "But I'm not a dumb guy, am I?"
        menu:
            "I try hard and try to beat Morgan":
                "When Morgan and I first pull out onto the track, things are pretty much even."
                "We're fighting to get around each other, and there's really nothing in it."
                "But the whole time I'm trying to remember all the times I played a racing game."
                "Hell, I'm even trying to remember if I ever watched a race of any kind on the TV."
                "Cars, motorbikes, hell I'd even settle for an insight from watching a three-legged race right now!"
                "In the end though, it all comes down to the two of us slugging it out the whole way."
                "Every lap we complete, morgan and I are twisting this way and that."
                "I lose track of how many times we swap places as we wind around the track."
                "And then, just as we're getting into the last lap, I see it."
                "Everything seems to come together, and I think I know how I can win."
                "Without hesitating, I make my move."
                "I put my foot down on the accelerator and throw caution to the wind."
                "And the crazy thing is that it works!"
                "Just before the last corner, I swing into action."
                "Then I catapult myself past Morgan and into first place."
                "My kart shoots over the finishing line, leaving her in a distant second."
                "As soon as we stop, Morgan hurries over, pulling off her helmet."
                show morgan surprised
                morgan.say "Whoa..."
                morgan.say "Where did you learn to drive like that?"
                mike.say "I have no idea, Morgan."
                mike.say "I guess I just got lucky."
                "I'm smiling as I say all of this, and not because I won."
                "But rather because Morgan looks like she had the time of her life."
                $ game.active_date.score += 20
            "I try hard but decide to let Morgan win":
                "When Morgan and I first pull out onto the track, things are pretty much even."
                "We're fighting to get around each other, and there's really nothing in it."
                "But the whole time I'm trying to remember all the times I played a racing game."
                "Hell, I'm even trying to remember if I ever watched a race of any kind on the TV."
                "Cars, motorbikes, hell I'd even settle for an insight from watching a three-legged race right now!"
                "In the end though, it all comes down to the two of us slugging it out the whole way."
                "Every lap we complete, morgan and I are twisting this way and that."
                "I lose track of how many times we swap places as we wind around the track."
                "And then, just as we're getting into the last lap, I see it."
                "Everything seems to come together, and I think I know how I can win."
                "But at the critical moment, I hesitate, wondering if I'm doing the right thing."
                "This is Morgan's birthday date, so is beating her really going to go down well?"
                "The pause effectively decides it for me, as I lose the chance to take advantage."
                "And after that, I don't get another opportunity of the same kind."
                "Morgan's kart shoots over the finishing line."
                "And she leaves me to finish a distant second."
                "As soon as we stop, Morgan hurries over, pulling off her helmet."
                show morgan surprised
                morgan.say "[hero.name], what happened back there?"
                morgan.say "I was sure you were going to pass me!"
                mike.say "Are you sure, Morgan?"
                mike.say "That's not the way I remember it."
                morgan.say "Wait a minute..."
                show morgan angry
                morgan.say "You didn't let me win, did you?"
                mike.say "No, of course not!"
                "Morgan nods at this, but I can see that she's still eyeing me with suspicion."
                "So I'd probably better change the subject pretty fast if I want to get away with it."
                $ game.active_date.score -= 30
    "Once we're done racing, Morgan and I regroup and try to catch our breath."
    "The go-karting arena has an obligatory kind of cafe where you can chill-out."
    "So we end up hanging around there for a moment while we decide what to do next."
    show morgan normal
    morgan.say "Okay, [hero.name]..."
    morgan.say "Time to fess up."
    morgan.say "Did you get me a present, or did you forget?"
    if not hero.has_gifts:
        "Seeing as how Morgan's being so upfront and open, I feel the need to be the same."
        "So I just shrug and come right out with it."
        mike.say "Yeah..."
        mike.say "Sorry about that, Morgan."
        mike.say "I was so busy organising the go-karting that I forgot!"
        "Morgan just shrugs it off and shakes her head."
        show morgan sad
        morgan.say "Whatever..."
        morgan.say "This was a pretty cool idea."
        morgan.say "So it kind of makes up for it."
        $ game.active_date.score -= 20
        $ morgan.love -= 10
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_29
        if _return != "done":
            if _return not in ["None", "exit"]:
                "I can't help chuckling, amused by Morgan's frankness."
                "But I pull out her present and hand it over all the same."
                mike.say "No, Morgan - I didn't forget."
                mike.say "Here you go."
                mike.say "And I hope you like it."
                "Morgan gives me an ironic grin as she accepts the gift."
                play sound [paper_ripping_2, paper_ripping_1]
                "And then she stats to tear into it, ripping off the wrapping paper."
                if _return:
                    show morgan happy
                    "But as soon as she sees what's inside, Morgan's expression changes."
                    mike.say "What's the matter?"
                    mike.say "Is everything okay?"
                    morgan.say "Are you kidding?!?"
                    morgan.say "This is awesome!"
                    morgan.say "Best present ever!"
                    $ game.active_date.score += 30
                else:
                    show morgan sadsmile
                    "But as soon as she sees what's inside, Morgan's expression changes."
                    mike.say "What's the matter?"
                    mike.say "Is everything okay?"
                    show morgan annoyed
                    morgan.say "You need to try harder next time."
                    morgan.say "Or else just don't bother."
                    morgan.say "Lamest present ever!"
                    $ game.active_date.score -= 10
            else:
                "Seeing as how Morgan's being so upfront and open, I feel the need to be the same."
                "So I just shrug and come right out with it."
                mike.say "Yeah..."
                mike.say "Sorry about that, Morgan."
                mike.say "I was so busy organising the go-karting that I forgot!"
                show morgan sadsmile
                "Morgan just shrugs it off and shakes her head."
                morgan.say "Whatever..."
                morgan.say "This was a pretty cool idea."
                morgan.say "So it kind of makes up for it."
                $ game.active_date.score -= 20
                $ morgan.love -= 10
    "I glance around at all of the other people in the little cafe."
    "And I notice that we seem to be the only ones without a drink."
    mike.say "You thirsty, Morgan?"
    mike.say "Want to grab a drink?"
    show morgan normal
    "Morgan looks around and nods."
    morgan.say "Sure thing..."
    morgan.say "Looks like they sell beers here!"
    mike.say "Oh..."
    mike.say "I was thinking more of a coffee."
    show morgan annoyed
    "Morgan gives me that look."
    "The one that lets me know she thinks I'm being lame."
    menu:
        "Insist on getting a coffee":
            "What am I, some kind of teenager being influenced by his peers?"
            "A kid giving in to pressure in the hope of looking cool?"
            "No, I'm a grown man that wants to have a damn coffee!"
            mike.say "You grab a beer if you want one, Morgan."
            mike.say "I'm going to get a coffee."
            mike.say "Maybe I'll have something stronger later in the day."
            "Morgan shakes her head and rolls her eyes."
            morgan.say "Whatever, [hero.name]."
            morgan.say "Go ahead and be a boring arse."
            morgan.say "I'm going to have a beer."
            "I nod and shrug my shoulders."
            "Because I'm determined not to be made to feel guilty."
            mike.say "Like I said, Morgan..."
            mike.say "That's fine."
            "With that we walk over to the bar and order."
            "Morgan getting her beer and me getting my coffee."
            $ game.active_date.score -= 20
        "Lets get a beer instead of a coffee":
            "Why am I being so rigid in wanting a coffee?"
            "And what difference will having a beer a little early make?"
            mike.say "You know what, Morgan..."
            mike.say "I think I will have a beer after all."
            show morgan happy
            "Morgan nods her head and slaps me on the back."
            "In fact, she slaps me pretty damn hard."
            "So much so that I can't help staggering forwards."
            morgan.say "Great idea!"
            morgan.say "Come on then - let's grab a couple of cold ones!"
            "Morgan eagerly leads the way to the bar."
            "And pretty soon we both have a beer in our hands."
            "Morgan puts hers to her lips."
            "Then she drains off almost half of it in one go!"
            morgan.say "Ahh..."
            morgan.say "That's more like it."
            morgan.say "Now we can really start to celebrate!"
            $ game.active_date.score += 30
    "It doesn't take long for us to finish our drinks."
    scene bg street
    show morgan normal at center, zoomAt (1.5, (640, 1040))
    with fade
    "And once we do, it's time to decide what happens next."
    mike.say "So..."
    mike.say "Are you ready to call it quits, Morgan?"
    mike.say "Because we don't have to if you don't want to."
    mike.say "We could maybe...do something else?"
    if game.active_date.score >= 80 and morgan.sexperience >= 1:
        show morgan happy
        "Morgan nods her head with visible enthusiasm."
        morgan.say "We should definitely do something else."
        morgan.say "Because I'm having a good time, you know?"
        morgan.say "And I'm not ready to quit just yet!"
        "Now it's my turn to nod."
        "I have no idea where we're going or what we'll do when we get there."
        "But what matters is that we're doing it together."
        call morgan_birthday_sex_tomboy from _call_morgan_birthday_sex_tomboy
    else:
        "Morgan shakes her head, causing my mood to plummet."
        show morgan annoyed
        morgan.say "Nah..."
        morgan.say "I think I've had enough fun for one day."
        morgan.say "I should head home and get some rest."
        "I don't want to agree with Morgan, but I have no choice."
        "So I nod and walk outside with her, looking for a taxi."
        "Maybe she's telling the truth and she really is just tired."
        "I hold onto that thought as she leaves me to go home alone."
    return

label morgan_birthday_sex_tomboy:
    show morgan normal at center, zoomAt (1.5, (640, 1040)) with fade
    "I can tell that Morgan's still feeling the rush from riding the go-karts."
    "She's clutching my hand harder than ever as we walk out of the karting circuit."
    "And the looks she keeps on shooting me the whole time are pretty intense too."
    "So perhaps I should have been expecting her to do something spontaneous any moment."
    "But somehow it still comes as a surprise to me when Morgan looks to the left and right."
    scene bg alley
    show morgan at center, zoomAt (1.5, (640, 1040))
    with fade
    "Then she pulls me down the nearest alleyway without any kind of warning."
    mike.say "Whoa..."
    mike.say "Morgan..."
    mike.say "What are you..."
    "No matter what I say, Morgan doesn't seem inclined to stop and answer me."
    "Instead she just keeps right on dragging me further down the alleyway."
    "Or at least that's what she does until we're out of sight of the street."
    "And then she finally stops dragging me along."
    "Though it's only a temporary reprieve."
    "As the next thing I know, Morgan pushes me hard against the nearest wall."
    with hpunch
    mike.say "Urgh..."
    mike.say "Morgan!"
    mike.say "Will you please tell me what's going on?!?"
    "I notice that Morgan has her hands on my top as she looks up at me."
    "And from the expression on her face, I can tell that I've caught her by surprise."
    "Like she was dead set on doing something until I spoke up."
    show morgan blush
    morgan.say "Oh..."
    morgan.say "I was...just..."
    morgan.say "Just going to initiate things, you know?"
    morgan.say "I thought you liked it when I'm assertive?"
    "Suddenly all of this makes sense."
    "And I can't help chuckling as I shake my head."
    mike.say "Okay, okay..."
    mike.say "I get it now!"
    mike.say "I thought you were trying to take a shortcut or something!"
    "Morgan seems to realise what's happened all of a sudden."
    "And she let's go of my top, taking an unconscious step backwards."
    "I can see that she's beginning to blush too."
    morgan.say "Oh shit..."
    morgan.say "I thought...I thought that..."
    morgan.say "Ah shit..."
    morgan.say "Now I look like some kind of nympho psycho slut!"
    "I shake my head, reaching out to put my hands on Morgan's shoulders."
    "And then I pull her back towards me again."
    mike.say "Don't sweat it, Morgan!"
    mike.say "It was just a little miscommunication, that's all."
    mike.say "Actually...a nympho psycho slut sounds pretty hot!"
    mike.say "How about you show me what one's like?"
    "Morgan's still blushing a little as I say all of this."
    "But I note that she's smiling too, and finding it hard to meet my eye."
    "So I can be pretty sure that my efforts to diffuse the situation have worked."
    morgan.say "You're a massive doofus, you know that?"
    morgan.say "But then I always kind of liked that about you."
    morgan.say "I always thought it was cute, you know?"
    "Morgan reaches up to wrap her hands around my neck as I pull her closer."
    "And her lips are ready to meet mine as I lean down towards her too."
    hide morgan
    show morgan kiss
    with fade
    $ morgan.flags.kiss += 1
    "Almost as soon as they meet, they part and her tongue begins to move."
    "I can feel it exploring my mouth with a genuine hunger."
    "And the sensation reminds me of just how much I want Morgan too."
    "All thought of where we are vanishes from my mind in an instant."
    "And now all I want is to be as close to Morgan as possible."
    "Hell, who am I trying to kid?"
    "What I want is to be inside of Morgan."
    "As hard and deep as I can possibly get!"
    "That's why it's me who's picking her up and turning her around."
    "Me who's pinning her against the wall this time."
    "And me that's trying to take off her clothes without looking."
    "But when it was Morgan doing the same to me, I was surprised."
    show morgan kiss naked with dissolve
    "The same can't be said of her, as she seems to take it in her stride."
    "I feel Morgan wrap her legs around my middle, clinging onto me."
    "That leaves her hands free to make a second attempt at undressing me."
    "The difference is that this time we're both on the same page."
    "We both want the same thing and there's nothing stopping us."
    "I don't know which one of us gets the other undressed first."
    "All I do know is that Morgan's the one that grabs hold of me."
    "I feel her hand on my cock, fingers closing on the shaft."
    "And once she has a hold of it, she pushes it hard between her legs."
    "At the same time I push myself upwards and pull her down."
    "This means that we're both trying to get it inside of her at once."
    "And while she seems to want it badly, Morgan's body has other ideas."
    scene bg black
    show morgan standing alley
    with fade
    morgan.say "Mmm..."
    morgan.say "Push harder, [hero.name]!"
    morgan.say "I want it...inside of me!"
    mike.say "I'm trying, Morgan..."
    mike.say "Urgnh..."
    mike.say "I'm trying!"
    "Now I really am pinning Morgan against the wall."
    "Pushing her against it as I rub the head of my cock against her pussy."
    "I can already feel her getting wetter with each pass."
    "And the way she's moaning makes me think it won't be much longer."
    "All the time Morgan's pushing herself downwards too."
    "Doing all she can think of to speed things up."
    "This means that when it happens, we're both distracted."
    "So fixated on doing it that we don't notice change in the tide."
    "I push up as Morgan pushes down...and then it's gone."
    "Just like that the last of the resistance vanishes."
    "Instead of sliding over the lips of her pussy, my cock slides inside."
    "And all the force we're putting in means it doesn't stop either."
    show morgan standing vaginal
    "Suddenly I'm as deep into Morgan as I can go!"
    "She gasps, clinging to me more tightly than ever."
    "And I feel like I'm choking on my own breath."
    "But the sensation only lasts for a few seconds."
    "Because that's when sheer instinct takes over for us both."
    "Animal desire means that we're no longer stunned."
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    "Almost without a conscious thought, our bodies start to move again."
    "Morgan's still pressed against the wall, just like before."
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    "But now it's because of the way I'm thrusting into her from below."
    "She nods and makes almost desperate noises as she clings to me."
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    "And they make me all the more determined to keep right on going."
    show morgan standing half
    morgan.say "Oh..."
    morgan.say "Oh yeah..."
    morgan.say "Don't stop, please - don't stop!"
    "I guess Morgan could well interpret what I do next as me obeying her."
    "But the truth is that I'd have been doing the same thing if she said nothing at all."
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    "Virtually pinning her against the wall, I keep right on going."
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    pause 0.1
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    "And somehow I also manage to pick up speed and go harder too."
    "I honestly think that I could let go of Morgan right now."
    "And she'd stay pretty much exactly where she is."
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    pause 0.1
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    "It's at times like this I'm glad for something as solid as a wall."
    "If we were doing it against anything more delicate, I don't think it'd hold up."
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    pause 0.1
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    "And I don't think that I'd have the presence of mind to move if we weren't."
    "Everything around me seems to be fading out of my perception."
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    pause 0.1
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    "The only thing that matters to me is Morgan and what I'm doing to her."
    "Luckily for us, the sound of the traffic on the street is pretty loud."
    show morgan standing closed pleasure at stepback(speed=0.1, h=-20, v=-10)
    pause 0.1
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    "Which means that when she starts to cry out, nobody hears it."
    "But before Morgan was still uttering actual words."
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    pause 0.1
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    "Now all that she seems to be capable of are primitive grunts and moans."
    "And I can tell from the sensations down below why that is."
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    pause 0.1
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    "Morgan's muscles are squeezing me without mercy."
    "Every moment we go on, I feel like I'm trapped in a vice."
    show morgan standing down at stepback(speed=0.1, h=-20, v=-10)
    pause 0.1
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    "Which can only mean that she's in the throes of her climax."
    "I don't know if it's the knowledge of that or the sensations themselves that do it."
    show morgan standing down at stepback(speed=0.1, h=-20, v=-10)
    pause 0.1
    show morgan standing at stepback(speed=0.1, h=-20, v=-10)
    "And in the end it doesn't really make a difference."
    "Because either way, Morgan's doing enough to take me along with her."
    show morgan cumshot with hpunch
    "With one final thrust, I bury myself in her and then I let go."
    with hpunch
    "The sense of release is enough to make me go weak at the knees."
    with hpunch
    "Now I'm pinning Morgan to the wall by leaning on her, not supporting her."
    "And it's a minor miracle that I don't sink down onto my knees in the alleyway."
    scene bg alley
    show morgan blush at center, zoomAt (1.5, (640, 1040))
    with fade
    "Once it's over, Morgan and I hurry to find our clothes and get dressed."
    "Then we slip back out of the alleyway and down the street."
    show bg street with fade
    "Neither of us says a word about what we just did."
    "Instead we hold hands tightly, and exchange knowing glances."
    "Which makes the whole thing seem that much more exciting."
    "Like a scandalous secret that we're always going to keep to ourselves."
    $ morgan.sexperience += 1
    return

label morgan_birthday_date_feminine:
    $ game.active_date.clothes = "casual"
    scene bg street with fade
    "Sometimes it can be pretty hard to figure out what will win Morgan over."
    "And even harder to know what will go down like a lead balloon with her too."
    "But as her birthday has been fast approaching, I've spent time racking my brains."
    "And I think that I've managed to arrange something special."
    "So when the big day comes around, I'm feeling pretty confident in my plans."
    "But that confidence begins to feel like it's being slowly eroded."
    "Because I keep looking at the time, noting that it's past when we agreed to meet."
    "I'm standing at the entrance to the mall, right on the chosen spot."
    "But Morgan's officially late, and she hasn't even bothered to call ahead and tell me."
    "Which means that when she finally shows up, I'm feeling more than a little flustered."
    show morgan happy at center, zoomAt(1.0, (640, 720)) with easeinright
    morgan.say "Hi, [hero.name]..."
    morgan.say "Are you glad to see me?"
    show morgan normal
    "Morgan looks me in the face for a moment."
    "And then she seems to realise what's wrong."
    show morgan sad
    morgan.say "Oh no..."
    morgan.say "What time was I supposed to be here again?"
    morgan.say "Am I late?"
    menu:
        "Laugh off Morgan being late":
            "I put a smile on my face, hoping that it looks genuine."
            "And then I add a casual shrug, waving away her concerns."
            mike.say "Oh, it's no problem, Morgan..."
            mike.say "It's only a couple of minutes really."
            mike.say "Nothing to worry about."
            "At first, Morgan looks worried as she listens to my response."
            "But as she hears me dismissing her concerns, her expression changes."
            show morgan happy at center, traveling(1.5, 0.5, (640, 1040))
            morgan.say "Oh thank goodness!"
            morgan.say "You had me worried for a moment there."
            "I can't help smiling as a wave of relief washes over me."
            "Because I feel like we just managed to avert a disastrous start to the date."
            mike.say "Like I said, Morgan..."
            mike.say "It's no big deal."
            mike.say "Let's just forget about it and start our date, okay?"
            "Morgan nods eagerly, wrapping her arm in mine."
            $ game.active_date.score += 20
        "Let Morgan know I am upset at her being late":
            "I can't help frowning a little and cocking my head on one side."
            "Because I'm not sure I'm comfortable with just glossing over it."
            mike.say "Yeah, Morgan..."
            mike.say "You kind of are!"
            mike.say "Not enough to screw things up though."
            show morgan sad
            "Morgan looks visibly upset as I share my feelings."
            "In fact, she can't even bring herself to look me in the eye."
            "Instead she stares down at the ground the whole time."
            show morgan annoyed
            morgan.say "I...I'm sorry, [hero.name]..."
            morgan.say "I guess I just lost track of the time."
            morgan.say "You know I can be a little scatter-brained, right?"
            show morgan sad
            "I shake my head, not really knowing what to say."
            "I kind of feel like a bit of a bully now."
            mike.say "Urgh..."
            mike.say "Now I feel like a jerk for complaining."
            mike.say "Let's just forget about it and start our date, okay?"
            show morgan annoyed
            morgan.say "Okay. [hero.name]..."
            show morgan sad
            "Morgan's still looking at the ground as I say this."
            "And she doesn't look up even as we walk into the mall."
            $ game.active_date.score -= 20
    scene bg mall1
    show morgan normal
    with fade
    "Morgan summons up the courage to ask a question as we enter the mall."
    "I can see her starting to look this way and that with growing interest."
    morgan.say "So, [hero.name]..."
    morgan.say "What are we here for?"
    "This is the moment I've been waiting for."
    "The chance to make my pitch to Morgan."
    "So I spread my arms wide."
    "Gesturing for Morgan to take in the mall in all of it's glory."
    mike.say "We're here for the complete mall experience, Morgan."
    mike.say "Everything you could possibly want to do on your birthday."
    mike.say "It's all here, and it's all under one roof!"
    "It seems to take a moment for what I'm saying to sink in."
    show morgan happy
    "But then I see a look of amazement spreading over Morgan's face."
    morgan.say "Seriously?"
    morgan.say "You mean we can do whatever I want?"
    mike.say "Erm..."
    mike.say "Well, within reason, Morgan."
    mike.say "We can't like, go on a spending spree in the jewellers, you know?"
    mike.say "Nothing that crazy!"
    show morgan flirt
    "Morgan rolls her eyes at this."
    "And she gives me a playful shove on the shoulder too."
    show morgan wink
    morgan.say "I know that, silly!"
    show morgan normal
    morgan.say "Okay..."
    morgan.say "Let's get started!"
    menu:
        "Passing a crowd to take it to a famous store":
            show morgan normal zorder 7 at center
            show emma zorder 1 at left4, blacker
            show alexis zorder 2 at right5, blacker
            show scottie zorder 3 at flip, left, blacker
            show palla zorder 4 at flip, mostright5, blacker
            show sasha zorder 5 at flip, mostleft5, blacker
            show jack zorder 6 at center, blacker
            with fade
            "Wanting to make the most of Morgan's enthusiasm, I dive straight into the crowds."
            "But it doesn't take long for me to find myself fighting against the tide."
            "The place is literally packed full of shoppers going from one store to the next."
            "Morgan and I are in danger of being swept along with them too!"
            show morgan sad at left with ease
            morgan.say "Ah..."
            morgan.say "[hero.name]..."
            morgan.say "I'm...kinda scared!"
            "Glancing at Morgan, I can see that she's not kidding."
            "She keeps getting shoved this way and that in the crowd."
            "And I'm having to make a serious effort to hold onto her too!"
            if hero.fitness >= 50:
                "Before I was just holding onto Morgan's hand."
                show morgan sad at center, zoomAt(1.0, (420, 720)) with ease
                "But now I start making a serious effort to pull her towards me."
                "At the same time I'm also trying to fight against the flow of the crowd."
                "It's times like this that all those sessions at the gym really pay off."
                "Because without them, I don't think I'd have been able to keep hold of Morgan."
                show morgan sad at center, zoomAt(1.0, (520, 720)) with ease
                "Doing the best I can to shield her from the crowd, I press onwards."
                "I feel like I'm paddling a canoe upstream the whole time."
                "But in the end my perseverance pays off and we make it through."
                "Up ahead the crowds seem to thin out a little."
                show morgan sad at right4 with ease
                "At least enough for us to be able to walk at our own pace again."
                "So I take this as a chance to check up on Morgan."
                mike.say "Phew..."
                mike.say "That was a little intense!"
                mike.say "Are you feeling okay, Morgan?"
                morgan.say "Oh..."
                show morgan blush
                morgan.say "I am now, [hero.name]!"
                morgan.say "Thanks for saving me back there."
                morgan.say "I thought I was going to get trampled for sure!"
                $ game.active_date.score += 20
            else:
                "Before I was just holding onto Morgan's hand."
                show morgan sad at center, zoomAt(1.0, (420, 720)) with ease
                "But now I start making a serious effort to pull her towards me."
                "At the same time I'm also trying to fight against the flow of the crowd."
                show morgan sad at center, zoomAt(1.0, (520, 720)) with ease
                "And I know that I'm giving it everything I've got."
                "Yet it still doesn't seem to be enough."
                "Suddenly there's a surge of movement from behind."
                show morgan sad at center, zoomAt(1.0, (420, 720)) with ease
                "And it pulls me in the opposite direction to Morgan."
                morgan.say "[hero.name]!"
                morgan.say "Help!"
                mike.say "Hold on, Morgan..."
                mike.say "Just hold on!"
                show morgan sad at center, zoomAt(1.0, (220, 720)) with ease
                "I know it all sounds a bit dramatic."
                "But Morgan really is being pulled away from me."
                show morgan sad at center, zoomAt(1.0, (-200, 720)) with ease
                "Finally my hand is torn away from hers and I lose sight of her."
                "Eventually I manage to fight my way after her."
                show morgan sad at right4 with ease
                "And I find Morgan huddled against one of the store windows."
                mike.say "Are you okay, Morgan?"
                morgan.say "Y...yeah..."
                morgan.say "I think so."
                "I take Morgan at her word and decide to leave it alone."
                "But part of me still feels like a failure for not being able to keep hold of her."
                $ game.active_date.score -= 20
        "Take morgan to a store I saw last time":
            show morgan normal zorder 7 at center
            show emma zorder 1 at left4, blacker
            show alexis zorder 2 at right5, blacker
            show scottie zorder 3 at flip, left, blacker
            show palla zorder 4 at flip, mostright5, blacker
            show sasha zorder 5 at flip, mostleft5, blacker
            show jack zorder 6 at center, blacker
            with fade
            "Wanting to make the most of Morgan's enthusiasm, I dive straight into the crowds."
            "But it doesn't take long for me to find myself wondering where we're going."
            "I keep looking around for a familiar sight to orient myself by."
            "But at first it just seems like everything looks the same."
            morgan.say "[hero.name]..."
            morgan.say "You know where we're going, right?"
            morgan.say "Because it kind of looks like you're lost!"
            mike.say "Don't worry, Morgan..."
            mike.say "I know exactly where we are."
            mike.say "Just leave it to me..."
            if hero.knowledge >= 50:
                "I turn my attention back to figuring out where in the hell we are."
                "And this time I don't bother trying to look for landmarks at all."
                "Instead I concentrate on remembering the layout of the mall."
                "In fact I manage to recall a rough map of what it looks like in my head."
                "Once that's done, everything starts to fall into place."
                mike.say "Come on, Morgan..."
                mike.say "I figured it out."
                "I don't wait for an answer as I lead the way."
                "And there must have been some genuine confidence in my voice too."
                "Because Morgan simply follows in my wake without question."
                "It doesn't take long for me to be proven right either."
                "Soon enough I see that we're right where we need to be."
                $ game.active_date.score += 20
            else:
                "I turn my attention back to figuring out where in the hell we are."
                "And I genuinely try to remember the layout of the mall inside of my head."
                "But nothing seems to do the trick, and I just can't get my bearings."
                "All the time I'm doing this, Morgan is watching me like a hawk."
                "No doubt waiting for me to make good on my promise."
                "But soon enough it becomes clear that's not going to happen."
                "And so she decides to take matters into her own hands."
                "Morgan yanks me out of the steady flow of shoppers."
                "Then marches me to the nearest map of the mall."
                show morgan angry
                morgan.say "Stop trying to show-off, [hero.name]."
                morgan.say "Use the map already."
                morgan.say "Before they have to send out a search party to look for us!"
                mike.say "Okay, Morgan..."
                mike.say "Point taken."
                $ game.active_date.score -= 20
        "Try something else":
            show morgan normal zorder 7 at center
            show emma zorder 1 at left4, blacker
            show alexis zorder 2 at right5, blacker
            show scottie zorder 3 at flip, left, blacker
            show palla zorder 4 at flip, mostright5, blacker
            show sasha zorder 5 at flip, mostleft5, blacker
            show jack zorder 6 at center, blacker
            with fade
            "Wanting to make the most of Morgan's enthusiasm, I dive straight into the crowds."
            show morgan normal at center, zoomAt(1.0, (420, 720)) with ease
            "But it doesn't take long for me to find myself fighting against the tide."
            "The place is literally packed full of shoppers going from one store to the next."
            show morgan normal at center, zoomAt(1.0, (520, 720)) with ease
            "Morgan and I aren't going anywhere fast in all of this!"
            morgan.say "Erm..."
            morgan.say "[hero.name]..."
            morgan.say "This kind of sucks!"
            mike.say "Yeah, Morgan..."
            mike.say "It sure does."
            mike.say "But leave it to me..."
            "I glance around, looking for a way to get around the crowds."
            "And then I see it."
            if hero.knowledge >= 30 and hero.fitness >= 30:
                "My eyes settle on a pair of plain, double doors up ahead."
                "And as soon as we reach them, I push one of the doors open."
                show morgan surprised at right with ease
                "Then I pull Morgan inside with me."
                morgan.say "Wha..."
                morgan.say "What are you..."
                mike.say "Relax, Morgan..."
                mike.say "This is just one of the service corridors."
                mike.say "Most malls have them for moving stuff around."
                mike.say "Safely out of the way of the herds of shoppers!"
                show morgan normal
                "Morgan looks around at the featureless, concrete walls."
                morgan.say "Aren't we trespassing, or something?"
                mike.say "Only if we get caught."
                mike.say "And even then we just say we got lost."
                morgan.say "Fine, fine..."
                morgan.say "But this looks like a maze."
                morgan.say "Won't we get lost?"
                mike.say "Nah."
                mike.say "I used to work here when I was younger."
                mike.say "I know these corridors like the back of my hand."
                "Leading the way, Morgan and I walk quickly through the corridors."
                "Right until we arrive at the door I'm looking for."
                "Then we duck right back into the public part of the mall."
                "Popping up at exactly the point I was trying to reach."
                $ game.active_date.score += 20
            else:
                "My eyes settle on the nearest fire alarm."
                "It's just at the right height for me to smash it with my elbow."
                "And we're fast approaching it too."
                "Maybe if I hit it as I walk past, that could do the trick?"
                "I'm just about to put my plan into action."
                "And that's when I feel something pulling on my arm."
                "A quick glance shows me that it's Morgan's hand."
                "And when I look up at her face, she doesn't seem pleased."
                show morgan sad
                morgan.say "Please tell me you weren't going to set off the fire alarm?!?"
                mike.say "Erm..."
                mike.say "Well..."
                mike.say "The thought had crossed my mind!"
                "Morgan shakes her head at me."
                "The disapproval in her eyes plain to see."
                show morgan angry
                morgan.say "[hero.name]!"
                morgan.say "That is SO irresponsible."
                morgan.say "Someone could have got hurt!"
                mike.say "Okay, Morgan, okay..."
                mike.say "I only said I was thinking about it."
                mike.say "Not that I was going to do it!"
                $ game.active_date.score -= 20
    "Morgan looks around, seeming to recognise where we are."
    show morgan happy at center with ease
    morgan.say "Oh, the food hall!"
    morgan.say "Are we getting something to eat?"
    show morgan normal
    mike.say "I was thinking more of a drink."
    mike.say "You know, like a coffee?"
    mike.say "But if you're hungry, we can grab a bite as well."
    mike.say "How about the coffee shop right there?"
    "Morgan follows my gaze, but she doesn't seem that enthusiastic."
    "Then she turns her gaze to another one of the units nearby."
    morgan.say "I kinda wanted to try the Maid Cafe."
    morgan.say "I've never been in there before."
    morgan.say "And it looks like fun!"
    menu:
        "Agree to the Maid Cafe":
            mike.say "It's your birthday, Morgan."
            mike.say "So let's do the Maid Cafe, yeah?"
            morgan.say "Hurray!"
            morgan.say "This is going to be so great!"
            scene bg maidcafe
            show morgan happy at center
            with fade
            "I don't have the same level of enthusiasm as Morgan does."
            "And one glance at the menu shows me the choice is much smaller in here."
            "Plus I have a loyalty card for the other place that's almost full!"
            "But I push all of that aside in favour of making things special for Morgan."
            "Once we're sat down at a table, the waitress hurries over."
            if bree.hidden:
                "Waitress" "Welcome! What can I get you?"
                mike.say "I would like some coffee please."
                morgan.say "Let see... I'll take a double mokachiatto with conutoa powder and a lot of whipped cream please."
                "Once served, we sink back into childhood memories."
            else:
                "And of course it's Bree!"
                "One day I'll come in here when she's not on shift, I swear it."
                show morgan happy at right with ease
                show bree happy maid at left with moveinleft
                bree.say "Hi, [hero.name]!"
                bree.say "Hi, [hero.name]'s date!"
                mike.say "Bree, this is Morgan."
                mike.say "Morgan, this is Bree - one of my housemates."
                morgan.say "Lovely to meet you, Bree."
                bree.say "Likewise, Morgan!"
                "As soon as we've ordered, the inevitable happens."
                "Bree hangs around to chat, rather than getting back to work."
                "And of course, she finds out that Morgan is one of my childhood friends."
                "She then proceeds to pump her for all of the embarrassing stories she can."
                "All the while I sit there with a smile on my face."
                "Telling myself that at least Morgan seems to be enjoying herself."
            $ game.active_date.score += 30
        "Insist on the Coffee Shop":
            mike.say "I think we do the coffee shop, Morgan."
            mike.say "They have a far better selection of beans."
            mike.say "Plus my loyalty card is almost full."
            mike.say "If I buy a coffee there, I'll get one free!"
            show morgan sad
            morgan.say "Okay, [hero.name]..."
            morgan.say "If you say so."
            scene bg coffeeshop with fade
            show morgan sad at center
            "Morgan doesn't seem to share my enthusiasm for this money-saving move."
            "But I guess she'll change her tune once we're inside the place."
            "Plus it means that I can spend more money on her choice of beverage too."
            "So everyone's a winner, right?"
            "At least that's what I hope will happen as we order and sit down."
            "But no matter what I do, Morgan just doesn't seem to get it."
            "Instead she spends most of the time just staring out of the window."
            "In fact she hardly touches her coffee the whole time."
            "But keeps on staring longingly at the Maid Cafe."
            "Which is kind of ungrateful, if you ask me!"
            $ game.active_date.score -= 20
    scene bg mall2
    show morgan normal
    with fade
    "Once we're done rehydrating ourselves, Morgan and I walk back out into the mall."
    "Thankfully the crowds seem to have died down a little by now."
    "So we can actually enjoy the experience of strolling around."
    "We've only gone so far when I start to hear a commotion up ahead."
    "It sounds like an alarm going off in one of the stores."
    "Morgan must hear it to, as she holds onto my arm more tightly than ever."
    "But all the same, she's still straining to see what's happening."
    "Following her gaze, I see a guy running towards us from that direction."
    "He looks pretty dodgy, and I can already see he has a bunch of stuff in his arms."
    "It seems to be T-shirt and pants, that kind of thing."
    "And there's a couple of mall security guards close on his tail."
    show morgan surprised
    morgan.say "Oh my..."
    morgan.say "Is that..."
    mike.say "A shoplifter?"
    mike.say "Looks like it to me, Morgan."
    "A moment later I realise that the guy's going to run straight past us."
    "All it would take is for me to move a little way, and I'd be in his path."
    "But when I move forwards, I instantly feel Morgan pull me back again."
    menu:
        "Let Morgan keep me where I am":
            "The macho wannabe inside of me wants to resist."
            "But the mature guy in there is the one that wins in the end."
            "And so I let Morgan hold me by her side as the shoplifter runs past."
            "It doesn't take long for the security guards to catch up to him."
            "They pounce no more than a few metres away, all piling on top of the guy."
            "Morgan and I watch in silence as he's hauled roughly to his feet."
            "Then the security guards march him off, presumably to face justice."
            "Curious about Morgan's motives, I turn to face her."
            mike.say "You were holding me back there, right?"
            mike.say "What did you think I was going to do?"
            show morgan normal
            "Morgan blushes, and for a moment I think she's not going to answer."
            "But then she looks me in the eye, and I can see genuine emotion in them."
            show morgan sad
            morgan.say "Oh, I don't know, [hero.name]!"
            morgan.say "I guess I just panicked."
            morgan.say "I thought you might get hurt."
            morgan.say "And...well..."
            morgan.say "I waited this long to be with you."
            morgan.say "I can't stand the idea of losing you again!"
            "That admission leaves me kind of gob-smacked."
            "As I had no idea Morgan felt so strongly about me."
            $ game.active_date.score += 20
        "Pull away and do something about the shoplifter":
            "I resist Morgan's efforts to keep me back."
            "It's not that I shove her off me or anything like that."
            "I just take a step forward, dragging her with me a way."
            "Just enough to be able to stick out one foot."
            "And that's all it takes."
            "The shoplifter trips right over it."
            "He drops all of his loot as he goes sprawling on the ground."
            "Then the security guards are all over him before he can blink."
            "I honestly don't think he even sees what he tripped over."
            "And he's manhandled away in the opposite direction."
            "So he certainly doesn't get to see one of the security guards thank me either."
            "Officer" "Much obliged, buddy."
            mike.say "No worries."
            show morgan angry
            morgan.say "[hero.name]!"
            morgan.say "Have you gone crazy?!?"
            mike.say "Settle down, Morgan..."
            mike.say "He never even saw me."
            morgan.say "That's not the point!"
            morgan.say "I can't stand the thought of you being in danger like that."
            "The bravado that came from stopping the thief quickly melts away."
            "And instead of feeling manly, I'm left more than a little ashamed."
            "Making Morgan worry about me like that isn't really worth it."
            $ game.active_date.score += 20
    show morgan normal with fade
    "Now that we've been strolling a while, I feel like a change."
    "So when I spot a convenient bench up ahead, I make straight for it."
    "Morgan follows close on my heels, sitting down beside me."
    "And I can see that there's a look of genuine interest in her eyes."
    morgan.say "So..."
    morgan.say "Are we sitting on this bench for any particular reason?"
    show morgan happy
    "Morgan smiles as she asks the question."
    "And it's not hard for me to tell what she's hinting at."
    if not hero.has_gifts:
        "Morgan's waiting for me to whip out a birthday gift."
        "But the problem is that I totally forgot to get her one!"
        "So it looks like I'm going to have to improvise."
        mike.say "Ah..."
        mike.say "I just wanted the chance to sit down with you, Morgan."
        mike.say "And to tell you how much I love spending time with you."
        show morgan sad
        "Morgan waits a moment longer, giving me the chance to say more."
        "But when I just keep on grinning at her, she finally gets the message."
        show morgan annoyed
        morgan.say "Oh..."
        morgan.say "Okay then..."
        morgan.say "That's great...really great."
        $ game.active_date.score -= 20
        $ morgan.love -= 10
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_30
        if _return != "done":
            if _return not in ["None", "exit"]:
                mike.say "You can stop dropping hints, Morgan..."
                mike.say "Because I didn't forget!"
                "I choose that exact moment to pull out the gift I got Morgan."
                "She beams with happiness, giving me a tight hug."
                play sound [paper_ripping_2, paper_ripping_1]
                "And then she accepts the gift, tearing at the paper."
                "But once it's open, I see her expression change."
                mike.say "What's the matter, Morgan?"
                mike.say "Is there a problem with the gift?"
                if _return:
                    show morgan surprised
                    "Morgan shakes her head as soon as I ask the question."
                    morgan.say "No..."
                    morgan.say "It's just that..."
                    show morgan happy at startle
                    morgan.say "This is totally amazing!"
                    morgan.say "I never expected anything like this."
                    "I can't help smiling as Morgan gapes at her gift."
                    "I had high hopes that it was something she really wanted."
                    "But her reaction is more than I could have dreamed of."
                    $ game.active_date.score += 30
                else:
                    show morgan sad
                    "Morgan shakes her head as soon as I ask the question."
                    show morgan sadsmile
                    morgan.say "Erm..."
                    morgan.say "No..."
                    morgan.say "Of course not!"
                    morgan.say "I'm just bowled over, that's all."
                    "I nod and smile, trying to keep up appearances."
                    "But I know for sure that Morgan's just trying to protect my feelings."
                    "Because it's plain to see that she's less than impressed with the gift."
                    $ game.active_date.score -= 10
            else:
                "Morgan's waiting for me to whip out a birthday gift."
                "But the problem is that I totally forgot to get her one!"
                "So it looks like I'm going to have to improvise."
                mike.say "Ah..."
                mike.say "I just wanted the chance to sit down with you, Morgan."
                mike.say "And to tell you how much I love spending time with you."
                show morgan sad
                "Morgan waits a moment longer, giving me the chance to say more."
                "But when I just keep on grinning at her, she finally gets the message."
                show morgan annoyed
                morgan.say "Oh..."
                morgan.say "Okay then..."
                morgan.say "That's great...really great."
                $ game.active_date.score -= 20
                $ morgan.love -= 10
    show morgan normal with fade
    "I kind of feel like the date is coming to a natural end."
    "Morgan and I have visited most parts of the mall."
    "And we've managed to squeeze in plenty of stuff along the way."
    "But one of the last parts we pass through has stalls as well as stores."
    "They're in the space between the units, kind of like a little market inside the mall."
    "It's about then that I realise I haven't spent enough to leave me broke just yet."
    "So I can probably afford to buy Morgan a little something before we leave."
    menu:
        "Buy Morgan a bunch of flowers":
            show bg flowershop
            show morgan normal
            with fade
            "One of the stalls is a florists, selling bunches of flowers."
            "And all girls like flowers, right?"
            "So I take the chance to sneak away from Morgan for a moment."
            "And I hand over the cash for one of the biggest bouquets on the stall."
            "Once I get back to her, Morgan is curious as to where I've been."
            morgan.say "There you are!"
            morgan.say "I thought I lost you, [hero.name]."
            mike.say "I was just over there, Morgan..."
            mike.say "Getting you a little surprise!"
            "I present Morgan with the flowers, a huge smile on my face."
            show morgan happy
            "And it only takes a second for an equally large one to appear on hers too."
            morgan.say "Oh, [hero.name]..."
            morgan.say "Are those for me?"
            mike.say "Of course, Morgan..."
            mike.say "Who else would they be for?"
            "Morgan accepts the flowers."
            "Then she holds them under her nose, inhaling their scent."
            show morgan flirt
            morgan.say "Mmm..."
            morgan.say "You know, I always dreamed about moments like this."
            morgan.say "Romantic things like getting flowers from you!"
            morgan.say "So you kind of just made one of my dreams come true!"
            $ game.active_date.score += 30
        "Buy Morgan a cookie":
            show bg bakery
            show morgan normal
            with fade
            "One of the stalls sells cakes and other sweet baked goods."
            "And everyone likes cookies, right?"
            "So I take the chance to sneak away from Morgan for a moment."
            "And I hand over the cash for one of the biggest cookies on the stall."
            "Once I get back to her, Morgan is curious as to where I've been."
            morgan.say "There you are!"
            morgan.say "I thought I lost you, [hero.name]."
            mike.say "I was just over there, Morgan..."
            mike.say "Getting you a little surprise!"
            "I present Morgan with the cookie, a huge smile on my face."
            show morgan sad
            "But she seems a tad underwhelmed when she sees what it is."
            morgan.say "Oh...thanks..."
            morgan.say "I guess..."
            mike.say "What's the matter, Morgan?"
            mike.say "Don't tell me you hate cookies!"
            morgan.say "Of course not!"
            morgan.say "I just had a snack back at the cafe."
            morgan.say "So I'm feeling pretty full."
            mike.say "Erm..."
            mike.say "Maybe save it for later then?"
            $ game.active_date.score -= 20
    show bg street
    show morgan normal
    with fade
    "As Morgan and I are finally leaving the mall, I suppose it's time to head home."
    "But I kind of feel like there's a chance things aren't actually over quite yet."
    "Maybe, if she's enjoying herself enough, Morgan might want to do more stuff with me?"
    "So I decide that it's worth asking the question, even if I don't get the answer I want."
    mike.say "Morgan..."
    mike.say "Are you ready to call it a day?"
    mike.say "Because I can hang-out a little longer, you know?"
    mike.say "But only if you want to..."
    if game.active_date.score >= 80 and morgan.sexperience >= 1:
        show morgan happy at startle
        "Morgan doesn't hesitate to nod, almost jumping at the chance."
        morgan.say "Me too, [hero.name]!"
        morgan.say "I'd love to keep hanging-out!"
        morgan.say "What did you have in mind?"
        "Morgan's enthusiasm kind of takes me by surprise."
        "And it's only now that I realise I hadn't thought that far ahead!"
        mike.say "Let's just walk and talk for now, Morgan."
        mike.say "I'm sure we can think of lots to do together."
        "Morgan wraps her arms in mine."
        "And we do just as I suggested."
        "It doesn't take me long to think of something after all."
        "But the tough part is going to be finding somewhere to do it!"
        call morgan_birthday_sex_feminine from _call_morgan_birthday_sex_feminine
    else:
        "Morgan doesn't hesitate to stretch and let out a huge yawn."
        show morgan sadsmile
        "Then she gives me a sleepy smile and shakes her head."
        morgan.say "I'd love to, [hero.name]."
        morgan.say "But I have an early start at the aquarium tomorrow."
        morgan.say "So I need to get some rest, okay?"
        "I'm pretty sure Morgan wasn't so tired a moment ago."
        "But I'm not about to call her on it."
        "Because that would make me look a total jerk."
        "So I just nod and go along with her."
        mike.say "Oh, I know that feeling!"
        mike.say "But we'll do this again, yeah?"
        mike.say "And soon?"
        show morgan happy
        morgan.say "I'll call you."
        "With that, Morgan gives me a wave."
        hide morgan with easeoutright
        "Then she turns on her heel and walks away."
        "Leaving me hoping that she really means it."
    return

label morgan_birthday_sex_feminine:
    "There are times when you want to get it on with a girl and you just throw down wherever."
    "I mean, like you might find the first safe place to do it and then just fuck like animals."
    "You might even choose to do it in a precarious place, the danger of discovery adding some spice."
    "But then there are some girls that you know that kind of stuff is never going to fly with."
    "And Morgan's one of those girls, I just know it."
    "When we leave the mall and decide to do something after the official date is over, we're only going one place."
    scene bg bedroom1
    show morgan at center, zoomAt(1.0, (640, 720))
    with fade
    "Which is straight back to my place and to the door of my bedroom."
    "Because there's no way I want anyone or anything interrupting us and upsetting Morgan."
    "I know that I'm getting into her pants if I play this right."
    "The mischievous look in her eyes as I lead her into my room tell me as much."
    "And Morgan makes it certain when she holds a finger to her lips."
    "Letting me know that she's totally into the whole thing of sneaking around."
    "It's only when the door is finally closed and locked that she makes a sound."
    show morgan flirt
    morgan.say "You think anyone saw us come in here, [hero.name]?"
    "I shrug, taking a moment to look back over my shoulder at the door."
    mike.say "I don't think so, Morgan..."
    mike.say "If anyone's in the house, we don't have to worry about them."
    mike.say "Bree and Sasha are usually pretty tied up in their own stuff anyway..."
    "I stop talking almost as soon as I turn around."
    "Stunned into silence by the sight that's presented to me."
    "Morgan's taken full advantage of my attention being elsewhere."
    show morgan topless with dissolve
    "And now she's standing there, totally naked above the waist!"
    mike.say "Wha..."
    mike.say "I..."
    mike.say "Whoa..."
    "Morgan lets out a giggle of pure delight at my reaction."
    show morgan at center, traveling(1.25, 1.0, (640, 900))
    "Then she leans forwards and shakes her chest at me."
    "Which of course means that her perfect, petite breasts sway and bounce."
    morgan.say "Like what you see?"
    "I nod desperately."
    morgan.say "Want to see more?"
    "I nod like my head is going to come off my shoulders."
    morgan.say "Well you took me on such a great date for my birthday..."
    morgan.say "I figure you deserve a reward!"
    show morgan at center, traveling(1.5, 1.0, (640, 1040))
    "Morgan reaches out and takes hold of my hand."
    "And then she leads me over to the side of my bed."
    "I offer no resistance as she does so."
    "All it takes is the sensation of her hands on my shoulders to make me sit down."
    "Then I find myself staring up at her from the bed, waiting to see what happens next."
    show morgan naked at center, traveling(1.25, 1.0, (640, 900)) with dissolve
    "Which is that Morgan slowly strips off the rest of her clothes, kicking them away."
    "So now she's standing in front of me, totally naked."
    morgan.say "You might want to take your clothes off now, [hero.name]."
    morgan.say "What I have in mind will be much easier if you do!"
    "That's all it takes for me to begin tearing off my clothes."
    "I pull them off and toss them aside as fast as I can."
    "Morgan watches me the whole time, waiting patiently."
    "But as soon as I'm done, she makes her next move."
    show morgan naked at center, traveling(1.5, 1.0, (640, 1140))
    "Morgan puts one hand on my shoulder, pushing me down onto the bed."
    "At the same time she climbs onto it herself, straddling my thighs."
    "Morgan keeps the one hand on my shoulder, pinning me in place."
    "And with the other, she reaches down below my waist."
    "I strain to lift my head, trying to see what she's doing."
    "But I get my answer soon enough, as I feel Morgan take hold of my cock."
    "Needless to say, it's already pretty hard from her previous antics."
    "Yet the moment she starts handling it, I feel it growing again."
    "Morgan looks me in the eye as she strokes the shaft up and down."
    "She can clearly see the effect this is having on me."
    "Because her smile becomes ever wider and more wicked."
    "But I can see that she's not unaffected herself."
    "There's a flush spreading across Morgan's cheeks."
    "And her breathing seems to be getting faster as she plays with me."
    "For all that she's trying to be the one in control, I feel like she's about to lose it."
    "I'm prove right a few seconds later, when something inside of Morgan just snaps."
    "All of a sudden she lets out a gasp of sheer desperation."
    "And then she pushes herself downwards without warning."
    scene bg black
    show morgan reverse cowgirl
    with fade
    "I feel the head of my cock pushed hard against the lips of her pussy."
    show morgan reverse cowgirl vaginal pleasure
    "It's hot and wet, slippery to the touch."
    "And it only takes a couple of pushes from Morgan."
    "Then her lips part, just enough for nature to take it's course."
    "As that happens, I feel the irresistible urge to take over."
    "My arms shoot up, hands clasping Morgan around the waist."
    show morgan reverse cowgirl pleasure at startle(0.05,-10)
    "Then I thrust upwards all at once, sinking almost the whole way into her."
    "All semblance of control simply vanishes as Morgan wriggles and writhes."
    "Instead she becomes helpless in my arms, letting me have my way with her."
    show morgan reverse cowgirl at startle(0.05,-10)
    "I don't hesitate to take full advantage, now moving up and down."
    show morgan reverse cowgirl ahegao at startle(0.05,-10)
    "Morgan braces herself against me, hands spread on my chest."
    "All the time she's nodding in sheer desperation, urging me on."
    "My hands move around to grasp Morgan's buttocks."
    "And my fingers sink into the soft, white flesh."
    "Morgan moans, nodding as I massage her cheeks."
    show morgan reverse cowgirl at startle(0.05,-10)
    "Then she begins to grind herself down on me too."
    show morgan reverse cowgirl at startle(0.05,-10)
    "My thrusts are becoming faster and more forceful by the second."
    "I can see them making Morgan's breasts jiggle and dance."
    "Her small nipples are hard as they can be, standing up before me."
    show morgan reverse cowgirl pleasure at startle(0.05,-10)
    "And then she throws her head back, starting to cry out."
    morgan.say "Oh..."
    morgan.say "[hero.name]..."
    morgan.say "You're gonna..."
    show morgan reverse cowgirl ahegao at startle(0.05,-10)
    morgan.say "Gonna make me...make me cum!"
    show morgan reverse cowgirl at startle(0.05,-10)
    "I don't know if it's Morgan's desperate words that do it."
    show morgan reverse cowgirl at startle(0.05,-10)
    "Or if the time was just right for me to reach my climax."
    with vpunch
    "But either way I feel myself starting to cum a moment later."
    show morgan cum vaginal with vpunch
    "And the second I do, Morgan is swept along with me."
    with vpunch
    "Morgan's arms fold under her, and she collapses atop me."
    "Then she clings on, riding it out as she wraps herself around me."
    $ morgan.sexperience += 1
    return

label morgan_date_play_arcade_clawmachine_male:
    scene bg arcade
    show chibi clawmachine
    with fade
    mike.say "Argh..."
    mike.say "Dammit..."
    mike.say "Almost...I almost had it!"
    "I can see that people walking past are starting to glance in my direction."
    "Hell, some of them are even stopping to stand and stare at me as I rant and race."
    "But none of that is going to come between me and my current, all-consuming obsession."
    if hero.is_lucky:
        $ hero.money -= 10
    else:
        $ hero.money -= 10 * randint(2, 10)
    $ hero.gain_item("cute_plushie")
    "So I dig into my pockets for more change, and then I jam the coins into the claw machine."
    "Seizing the controls, I sent the claw swaying towards my intended target once again."
    "And as it drops onto the plushie atop the pile, I can't help holding my breath."
    "I swear I feel my heart skip a beat as the claw closes around the soft-toy."
    "And I almost go weak at the knees as it actually gets hoisted into the air."
    "Time seems to slow down as the claw approaches the hole into which it should drop the plushie."
    "More than once it starts to slip, and I'm sure that disaster is going to strike."
    "But then it drops for real, right into the hole!"
    "And in that moment, time suddenly returns to normal."
    mike.say "Yes, yes...YES!"
    hide chibi with fade
    "I pounce on the machine, shoving my hand inside to grab the plushie."
    "And then I clutch it to my chest."
    "As though I'm afraid someone will try to steal it away from me."
    show morgan with easeinright
    "Then I turn around and see Morgan walking towards where I'm standing."
    show morgan stuned
    "But before she can say a word, I thrust the plushie at her."
    mike.say "Hey, Morgan..."
    mike.say "Look what I won for you."
    mike.say "Pretty cool, huh?"
    $ hero.lose_item("cute_plushie")
    if morgan.male >= 66:
        show morgan sadsmile
        "Morgan shakes her head and chuckles."
        hide morgan
        show morgan clawmachine
        with fade
        "But she takes the plushie all the same."
        "And then she thanks me in a distinctly sarcastic tone."
        morgan.say "Thanks, [hero.name]."
        morgan.say "I promise to love him, and cuddle him and keep him warm!"
        $ morgan.love += 1
        $ game.active_date.score += 5
    elif morgan.male >= 33:
        show morgan normal
        "Morgan smiles and shakes her head."
        hide morgan
        show morgan clawmachine
        with fade
        "But she seems genuinely happy to accept my gift."
        morgan.say "Aww..."
        morgan.say "That's really cute, [hero.name]!"
        morgan.say "Thank you."
        $ morgan.love += 2
        $ game.active_date.score += 10
    else:
        show morgan happy
        "Morgan's grin is as wide as her face."
        hide morgan
        show morgan clawmachine
        with fade
        "And she hugs the plushie against her chest as soon as she takes it from me."
        morgan.say "Thank you so much, [hero.name]!"
        morgan.say "It's the cutest thing ever."
        morgan.say "I'll sleep with it every night from now on!"
        $ morgan.love += 3
        $ game.active_date.score += 15
    "I feel more than a little vindicated thanks to Morgan's reaction."
    "Almost enough not to regret having dropped so much money on the claw machine."
    "Almost, but not quite!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
