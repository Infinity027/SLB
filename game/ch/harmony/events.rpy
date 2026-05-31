init python:
    Event(**{
    "name": "harmony_kiss_me",
    "label": "harmony_kiss_me",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(harmony,
            IsPresent(),
            Not(IsHidden()),
            MinFlag("kiss", 1),
            MinStat("love", 140),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "chances": 20,
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "harmony_start",
    "label": "harmony_start",
    "conditions": [
        HeroTarget(IsFlag("harmonystart", 2)),
        ],
    "priority": 1000,
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "harmony_fix",
    "label": "harmony_start",
    "conditions": [
        IsDone("harmony_start"),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "harmony_event_03",
    "label": "harmony_event_03",
    "duration": 1,
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("bible_study"),
            IsRoom("church"),
            ),
        PersonTarget(harmony,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "harmony_event_03_fix",
    "label": "harmony_event_03_fix",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_03"),
        IsNotDone("harmony_event_04"),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "harmony_event_04",
    "label": "harmony_event_04",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_03"),
        HeroTarget(
            IsActivity("bible_study"),
            IsRoom("church"),
            ),
        PersonTarget(harmony,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 40),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "harmony_event_05",
    "label": "harmony_event_05",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_04"),
        HeroTarget(
            IsActivity("bible_study"),
            IsRoom("church"),
            ),
        PersonTarget(harmony,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 60),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "harmony_event_06",
    "label": "harmony_event_06",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_05"),
        HeroTarget(
            IsActivity("bible_study"),
            IsRoom("church"),
            ),
        PersonTarget(harmony,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 80),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "harmony_event_07",
    "label": "harmony_event_07",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_06"),
        IsNotDone("harmony_event_08"),
        IsDayOfWeek("123457"),
        HeroTarget(IsActivity("ask_date")),
        PersonTarget(harmony,
            IsActive(),
            MinStat("love", 100),
            Not(IsDatePlanned()),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    })

    Event(**{
    "name": "harmony_event_07_fix",
    "label": "harmony_event_07_fix",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_07"),
        IsNotDone("harmony_event_08"),
        PersonTarget(harmony,
            Not(IsDatePlanned()),
            Not(IsHidden()),
            ),
        ],
    "do_once": False
    })

    Event(**{
    "name": "harmony_event_09",
    "label": "harmony_event_09",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_08"),
        IsNotDone("harmony_event_10"),
        IsDayOfWeek("123457"),
        HeroTarget(IsActivity("ask_date")),
        PersonTarget(harmony,
            IsActive(),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    })

    Event(**{
    "name": "harmony_event_09_fix",
    "label": "harmony_event_09_fix",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_09"),
        IsNotDone("harmony_event_10"),
        PersonTarget(harmony,
            Not(IsDatePlanned()),
            Not(IsHidden()),
            ),
        ],
    "do_once": False
    })

    Event(**{
    "name": "harmony_event_01_vanilla",
    "label": "harmony_event_01_vanilla",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_10"),
        IsNotDone("harmony_event_02_vanilla"),
        IsDayOfWeek("123457"),
        HeroTarget(IsActivity("ask_date")),
        PersonTarget(harmony,
            IsActive(),
            MinStat("love", 140),
            Not(HasTrait("religious")),
            Not(HasTrait("slutty"))
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    })

    Event(**{
    "name": "harmony_event_03_vanilla",
    "label": "harmony_event_03_vanilla",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_02_vanilla"),
        IsNotDone("harmony_event_04_vanilla"),
        IsDayOfWeek("123457"),
        HeroTarget(IsActivity("ask_date")),
        PersonTarget(harmony,
            IsActive(),
            MinStat("love", 150),
            Not(HasTrait("religious")),
            Not(HasTrait("slutty"))
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    })

    Event(**{
    "name": "harmony_event_05_vanilla",
    "label": "harmony_event_05_vanilla",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_04_vanilla"),
        IsNotDone("harmony_event_06_vanilla"),
        IsDayOfWeek("123457"),
        HeroTarget(IsActivity("ask_date")),
        PersonTarget(harmony,
            IsActive(),
            MinStat("love", 170),
            Not(HasTrait("religious")),
            Not(HasTrait("slutty"))
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    })

    Event(**{
    "name": "harmony_event_07_vanilla",
    "label": "harmony_event_07_vanilla",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_06_vanilla"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_park")),
        PersonTarget(harmony,
            OnDate(),
            MinStat("love", 180),
            Not(HasTrait("religious")),
            Not(HasTrait("slutty"))
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "harmony_event_01_religious",
    "label": "harmony_event_01_religious",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_10"),
        IsNotDone("harmony_event_02_religious"),
        IsDayOfWeek("123457"),
        HeroTarget(IsActivity("ask_date")),
        PersonTarget(harmony,
            IsActive(),
            MinStat("love", 140),
            HasTrait("religious")
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    })

    Event(**{
    "name": "harmony_event_03_religious",
    "label": "harmony_event_03_religious",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_02_religious"),
        IsNotDone("harmony_event_04_religious"),
        IsDayOfWeek("123457"),
        HeroTarget(IsActivity("ask_date")),
        PersonTarget(harmony,
            IsActive(),
            MinStat("love", 170),
            HasTrait("religious")
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    })

    InteractEvent(**{
    "name": "harmony_event_05_religious",
    "label": "harmony_event_05_religious",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_04_religious"),
        HeroTarget(
            IsGender("male")),
        PersonTarget(harmony,
            IsActive(),
            MinStat("love", 180),
            HasTrait("religious")
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "harmony_event_06_religious",
    "label": "harmony_event_06_religious",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_05_religious"),
        IsHour(13),
        HeroTarget(
            IsGender("male"),
            Not(HasRoomTag("park"))
            ),
        PersonTarget(harmony,
            Not(IsPresent()),
            Not(IsHidden()),
            HasTrait("religious"),
            MinStat("love", 180),
            Not(IsFlag("storyDelay")),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "harmony_event_07_religious",
    "label": "harmony_event_07_religious",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_06_religious"),
        IsDayOfWeek("7"),
        HeroTarget(
            IsGender("male"),
            Not(IsRoom("church"))
            ),
        PersonTarget(harmony,
            Not(IsHidden()),
            HasTrait("religious"),
            MinStat("love", 190),
            IsRoom("church")
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "harmony_event_01_slutty",
    "label": "harmony_event_01_slutty",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_10"),
        IsNotDone("harmony_event_02_slutty"),
        IsDayOfWeek("123457"),
        HeroTarget(IsActivity("ask_date")),
        PersonTarget(harmony,
            IsActive(),
            MinStat("love", 140),
            HasTrait("slutty")
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    })

    Event(**{
    "name": "harmony_event_03_slutty",
    "label": "harmony_event_03_slutty",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_02_slutty"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_nightclub")),
        PersonTarget(harmony,
            OnDate(),
            MinStat("love", 150),
            MinStat("sub", 70),
            HasTrait("slutty")
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "harmony_event_04_slutty",
    "label": "harmony_event_04_slutty",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_03_slutty"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_nightclub")),
        PersonTarget(harmony,
            OnDate(),
            MinStat("love", 170),
            MinStat("sub", 90),
            HasTrait("slutty")
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "harmony_event_05_slutty",
    "label": "harmony_event_05_slutty",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_04_slutty"),
        IsNotDone("harmony_event_06_slutty"),
        IsDayOfWeek("123457"),
        HeroTarget(IsActivity("ask_date")),
        PersonTarget(harmony,
            IsActive(),
            MinStat("love", 190),
            MinStat("sub", 100),
            HasTrait("slutty")
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    })

    InteractEvent(**{
    "name": "harmony_purity_01",
    "label": "harmony_purity_01",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_06"),
        IsNotDone("harmony_purity_02"),
        IsDayOfWeek("123456"),
        PersonTarget(harmony,
            IsActive(),
            MaxStat("purity", 80),
            Not(IsDatePlanned()),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    })

    Event(**{
    "name": "harmony_purity_01_fix",
    "label": "harmony_purity_01_fix",
    "priority": 500,
    "conditions": [
        IsDone("harmony_purity_01"),
        IsNotDone("harmony_purity_02"),
        PersonTarget(harmony,
            Not(IsDatePlanned()),
            ),
        ],
    "do_once": False
    })

    Event(**{
    "name": "harmony_purity_03",
    "label": "harmony_purity_03",
    "priority": 500,
    "conditions": [
        IsDone("harmony_purity_01"),
        IsNotDone("harmony_purity_04"),
        IsSeason(0, 1, 2),
        IsDayOfWeek("123456"),
        HeroTarget(IsActivity("ask_date")),
        PersonTarget(harmony,
            IsActive(),
            MaxStat("purity", 70),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    })

    Event(**{
    "name": "harmony_purity_03_fix",
    "label": "harmony_purity_03_fix",
    "priority": 500,
    "conditions": [
        IsDone("harmony_purity_03"),
        IsNotDone("harmony_purity_04"),
        PersonTarget(harmony,
            Not(IsDatePlanned()),
            ),
        ],
    "do_once": False
    })

    Event(**{
    "name": "harmony_purity_05",
    "label": "harmony_purity_05",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("harmony_purity_04"),
        IsNotDone("harmony_purity_05"),
        HeroTarget(
            IsGender("male"),
            IsActivity("attend_mass"),
            IsRoom("church"),
            ),
        PersonTarget(harmony,
            IsPresent(),
            Not(IsHidden()),
            MaxStat("purity", 50),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "harmony_purity_06",
    "label": "harmony_purity_06",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("harmony_purity_05"),
        IsNotDone("harmony_purity_06"),
        IsDayOfWeek("67"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_nightclub"),
            HasStamina(),
            ),
        PersonTarget(harmony,
            OnDate(),
            MaxStat("purity", 30),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "harmony_preg_talk",
    "label": "harmony_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(harmony,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    })

    Event(**{
    "name": "harmony_kissable",
    "label": "harmony_kissable",
    "priority": 1500,
    "conditions": [
        PersonTarget(harmony,
            IsFlag("nokiss"),
            MaxStat("purity", 80),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "harmony_lose_religious",
    "label": ("loose_trait", "harmony", "religious"),
    "priority": 1500,
    "conditions": [
        PersonTarget(harmony,
            HasTrait("religious"),
            MaxStat("purity", 70),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "harmony_dateable",
    "label": "harmony_dateable",
    "priority": 1500,
    "conditions": [
        PersonTarget(harmony,
            IsFlag("nodate"),
            MaxStat("purity", 65),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "harmony_danceable",
    "label": "harmony_danceable",
    "priority": 1500,
    "conditions": [
        PersonTarget(harmony,
            IsFlag("nodance"),
            MaxStat("purity", 60),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "harmony_lose_innocent",
    "label": ("loose_trait", "harmony", "innocent"),
    "priority": 1500,
    "conditions": [
        PersonTarget(harmony,
            HasTrait("innocent"),
            MaxStat("purity", 40),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "harmony_fuckable",
    "label": "harmony_fuckable",
    "priority": 1500,
    "conditions": [
        PersonTarget(harmony,
            IsFlag("nosex"),
            MaxStat("purity", 55),
            ),
        ],
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "harmony_gain_flirty",
    "label": ("gain_trait", "harmony", "flirty"),
    "priority": 1500,
    "conditions": [
        PersonTarget(harmony,
            Not(HasTrait("flirty")),
            MaxStat("purity", 30),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "harmony_gain_slutty",
    "label": ("gain_trait", "harmony", "slutty"),
    "priority": 1500,
    "conditions": [
        PersonTarget(harmony,
            Not(HasTrait("slutty")),
            MaxStat("purity", 10),
            ),
        ],
    "quit": False,
    })

    InteractEvent(**{
    "name": "harmony_stripclub_event_01",
    "label": "harmony_stripclub_event_01",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_04_slutty"),
        HeroTarget(IsGender("male")),
        PersonTarget(harmony,
            IsActive(),
            MaxStat("purity", 10),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "harmony_stripclub_event_02",
    "label": "harmony_stripclub_event_02",
    "priority": 500,
    "conditions": [
        IsDone("harmony_event_06_slutty", "harmony_stripclub_event_01"),
        HeroTarget(
            IsGender("male"),
            IsRoom("stripclub")
            ),
        PersonTarget(harmony,
            Not(IsHidden()),
            MaxStat("purity", 5),
            ),
        ],
    "music": "music/roa_music/one_day.ogg",
    "do_once": True,
    })

label harmony_danceable:
    $ harmony.flags.nodance = False
    return

label harmony_fuckable:
    $ harmony.flags.nosex = False
    return

label harmony_dateable:
    $ harmony.flags.nodate = False
    return

label harmony_kissable:
    $ harmony.flags.nokiss = False
    return

label harmony_start:
    if not "harmony_fix" in DONE:
        $ DONE["harmony_fix"] = game.days_played
    $ harmony.unhide()
    return

label harmony_event_03_fix:
    if harmony.love.max < 60:
        $ harmony.love.max = 60
    return

label harmony_event_03:
    if harmony.love.max < 40:
        $ harmony.love.max = 40
    show harmony
    "I'm still worrying and fretting over whether or not I was right to take Harmony up on the offer of bible study classes."
    "And the feeling persists even as I sit down with her for the first of the sessions at church the next Sunday morning."
    "I really should be able to draw some comfort from the fact that Harmony looks pretty pained and awkward too."
    "But then she has the advantage of that positive, upbeat front that the seriously religious always seem to be able to summon."
    harmony.say "Okay, [hero.name], let's see if we can get started."
    show harmony happy
    harmony.say "There's no need to worry - I don't bite!"
    "She giggles at this, and smiles, clearly intending it as an ice-breaker."
    show harmony normal
    "But all I can do is make a grimace in return as the image of her face spattered in my cum returns to haunt me."
    harmony.say "If it's okay with you, I'm going to treat you like a beginner."
    harmony.say "So we'll be starting with Genesis, and working from there."
    "Harmony picks up her well-thumbed bible and opens it at a point towards the start."
    harmony.say "Erm, [hero.name] - you should probably have your bible open too!"
    "My bible?"
    "What does she mean by that?"
    "Shit - was I supposed to bring a copy of my own?"
    "All I can do is offer her a helpless and rather pathetic shrug."
    mike.say "Ah...sorry, Harmony."
    mike.say "I must have left mine at home!"
    "Harmony looks at me askance, probably thinking that I'm even more of a hopeless case than she already suspected."
    show harmony happy
    "But again, she adopts that same upbeat attitude and shakes her head with a forced smile upon her face."
    harmony.say "No, don't worry about it - it's not a problem."
    show harmony normal
    harmony.say "I guess that I should have been more specific, that's all."
    harmony.say "Here - you can use one of my spare bibles."
    "I try to look relieved and pleased as Harmony reaches into her bag and pulls out a second bible."
    "But I can't help wondering at the fact that she carries a spare around with her, in case of emergencies such as this."
    "Also, she said spare bibles, not bible - so just how many of the damn things does she actually have on her at any given time?"
    "Pushing all of these unhelpful thoughts aside, I take the proffered bible and hurriedly find the correct page."
    harmony.say "I thought the story of Adam and Eve and their temptation by the serpent would be appropriate."
    harmony.say "And I don't think you can fail to agree that you're facing some similar issues in your daily life, [hero.name]!"
    "Well, I'm certainly being sorely tempted by something ripe and forbidden that's in a sacred place, that's for sure!"
    "Harmony wastes no time in diving into her subject, seeming to relish the task ahead."
    "She reads out the verses that she thinks are particularly apt with some considerable gusto, as if wanting to drive the words directly into my skull."
    "And then Harmony tries to tease out the deeper meanings that she seems sure are to be found behind those same verses."
    "Finally, after being assaulted by her words for what feels like hours, she pauses and cocks her head on one side."
    harmony.say "So, [hero.name] - what do you think?"
    menu:
        "Agree that the verses have illuminated your own sins":
            "I don't know whether it's because I'm so nervous or still racked with genuine guilt over what happened in the bathroom."
            "But something about what Harmony's reading out to me and the points she's making really do seem to be hitting home."
            "At first I was nodding to keep her from getting annoyed with me."
            "Yet now I can feel the nods actually coming in response to what she's saying."
            $ harmony.love += 5
            mike.say "It's all so clear to me now, Harmony."
            mike.say "I never knew that all of my experiences, thoughts and feelings were right there on the page!"
            show harmony happy
            "If I had any doubt at all about what I'm saying, it vanishes utterly as Harmony smiles in response."
            "The way that her face lights up is enough to make me forget everything we just talked about."
            "Oh God - she's like an angel!"
            "I honestly don't know if I'd be buying all of this from anyone else."
            "And part of me's sure that she could be speaking a foreign language and I'd still be nodding like a fool."
            harmony.say "That's so good to hear, [hero.name]!"
            harmony.say "You just have to remember that all the wisdom you'll ever need is right here."
            "At this, she clutches the bible she's holding to her more than ample chest."
            "I nod again, wondering if she's even aware of the fact that my attention is miles away from the bible itself."
        "Question the verses" if hero.knowledge >= 10:
            "I can't help screwing my face up into a rather puzzled expression as I think about what we just discussed."
            "I've never really sat down and thought about what's actually in the bible like we just did here and now."
            "That it's full of weird stories and impossible tales I already knew."
            "But I always just assumed that they made some kind of sense when you actually read them through."
            "And now I'm not so sure that's the case here..."
            mike.say "Erm, Harmony...I have some questions."
            show harmony happy
            "At this, she smiles and nods, encouraging me to speak up and share what's on my mind."
            mike.say "Okay...for one thing - why did God stick fruit people weren't supposed to eat, right in front of them?"
            harmony.say "Ah, well, [hero.name], you see he wanted to test them."
            mike.say "But I thought the snake did that?"
            harmony.say "No, no...the serpent tempted them."
            mike.say "With something that God had already put there to test them?"
            show harmony normal
            harmony.say "Yes, I suppose so..."
            mike.say "So God wanted the snake to tempt them, right?"
            harmony.say "It was a serpent...and no, I don't think that's what the story says!"
            mike.say "How come - wouldn't God have just gotten rid of the snake if he didn't want that to happen?"
            mike.say "You know, smited it or something?"
            "Harmony's smile is becoming ever more forced as her eyes almost glaze over from my questions."
            $ harmony.purity -= 5
            harmony.say "I...I think that we're in danger of getting distracted here, [hero.name]!"
            harmony.say "Maybe...maybe we should leave it there for now?"
            harmony.say "Pick up where we left off in a couple of days time?"
            harmony.say "When my brain's had time to recover..."
    "We wrap things up there, with Harmony hastily giving me a little reading to do for my homework before our next session."
    "I make to hand the bible back, but she stops me and pushes it towards me instead."
    harmony.say "No, I think that you should keep it - my gift to you."
    harmony.say "I have plenty more where that came from!"
    "I nod hastily, more taken by the warmth of her hands on mine than the gift of the bible."
    return

label harmony_event_04:
    if harmony.love.max < 60:
        $ harmony.love.max = 60
    "For our second session of bible study, I suggested that we have a change of venue and meet in the park."
    "Harmony was quick to shoot this idea down, making me wonder if she's embarrassed to be seen with me in public."
    "But either way I find myself hurrying along to the room in the church where we'd agreed to meet, bible in hand."
    show harmony happy with dissolve
    "Harmony's already there when I arrive, of course she is, smiling and patting a chair beside her."
    "I hardly need any kind of encouragement to hurry over and sit down just where she suggests."
    show harmony normal
    harmony.say "Hello, [hero.name] - isn't it a lovely day?"
    harmony.say "A gift from God to help us as we study the words of wisdom in the pages of the good book!"
    "I nod and retrieve the bible that she gave me at the end of our previous session."
    "While I'm still a bag of nerves around Harmony, I don't feel nearly as embarrassed as I did before."
    "Maybe the shame of what happened in the spare room is finally starting to fade from my memory."
    "Or maybe it's just that being close to her has that effect on me..."
    harmony.say "I thought that we'd skip ahead a little today, if that's okay?"
    mike.say "Erm, okay...I guess so, Harmony."
    show harmony happy
    "She nods and smiles at my assent, clearly happy in the role of teacher with an attentive pupil."
    harmony.say "Not too far ahead though - only to a later point in the Old Testament."
    harmony.say "We're going to be reading through the story of David and Goliath..."
    show harmony normal
    "From there we follow a similar routine to the one we did at the last session."
    "Harmony reads the relevant passages out to me, stopping to make various points along the way."
    "Again, this is one of those bible stories that I've heard of and know the basic shape it takes."
    "But I've never actually gone through it in this kind of painstaking detail."
    "I find myself getting lost in what I think is the narrative and swept along with the tale."
    "Yet when she wraps up her reading and gives me an expectant look, I realise that I was actually enraptured by Harmony herself."
    harmony.say "Well, [hero.name] - what did you think of that?"
    menu:
        "Find a deeper spiritual meaning in the story":
            "It only takes me a couple of seconds to ponder the question before I feel that I can answer."
            "Who knows - maybe I'm actually getting the hang of this bible study thing?"
            mike.say "Well...it's not really about going out and killing giant guys in armour, is it?"
            "Harmony gives me her usual bland smile, but I can see in her eyes that she's eager to hear more."
            harmony.say "Go on, [hero.name] - tell me what you mean by that."
            mike.say "Ah, okay..."
            mike.say "So, all of those bigger guys have refused to fight Goliath and then David says he will."
            mike.say "And he wins because he's got faith and he's not scared."
            "I look into Harmony's eyes for reassurance that I'm getting this right."
            "She remains silent, but nods for me to go on."
            mike.say "I'm kind of like David, aren't I?"
            mike.say "And my...erm...my problem..."
            "I pause long enough to nod down and in the general direction of my groin."
            mike.say "It's like my own Goliath...isn't it?"
            "For a moment I'm actually worried that she's going to shoot me down in flames."
            show harmony happy
            "But then Harmony puts her bible down on her lap and give me a little round of applause."
            harmony.say "That's exactly right, [hero.name]!"
            harmony.say "We're all like David, having to find the courage to stand up to Goliath."
            harmony.say "But the difference is that we have or own version of Goliath inside of us."
            $ harmony.love += 5
            "I smile broadly, feeling a genuine warmth beginning to grow in the pit of my stomach."
            "But for the life of me I still can't tell if I'm happy to have understood the lesson."
            "Or whether I feel this way on account of having made Harmony so delighted with me."
        "Find fault with the moral of the story" if hero.knowledge >= 20:
            mike.say "I don't know..."
            mike.say "But wasn't that David guy a major dick?"
            show harmony annoyed
            "Harmony opens her mouth as if to say something, but then shakes her head in evident surprise."
            harmony.say "A...a dick?"
            harmony.say "I...I don't understand..."
            "I shrug my shoulders and try to explain myself as best I can."
            mike.say "Look, I'm sure there's a moral in there somewhere."
            mike.say "Something like, I don't know, facing your demons and not being a scared little bitch."
            mike.say "But come on - he killed the guy with a damn sling, from miles away."
            mike.say "It's not exactly brave or honourable, is it?"
            "Harmony puts her hand to her lips, looking for all the world like her brain is struggling to make sense of what I just said."
            mike.say "So I take it that the lesson here is...what - that it's good to be a dick?"
            $ harmony.purity -= 5
            harmony.say "I...I never really thought of it in that way."
            harmony.say "Not before you put it like that."
            harmony.say "But I suppose it wasn't very brave of him really..."
            show harmony normal
            "But then Harmony shakes her head."
            harmony.say "But that was in the middle of a war!"
            harmony.say "You can't apply the same moral standards during wartime."
            "I frown at this, but I nod all the same."
            "Harmony has got a point there."
            if hero.knowledge >= 30:
                $ harmony.purity -= 5
                "But then a thought occurs to me."
                mike.say "Wait a minute, Harmony..."
                "I begin flipping through her bible, searching for a particular passage."
                mike.say "There - the book of Samuel..."
                mike.say "David takes Bathsheba as his wife."
                show harmony annoyed
                harmony.say "Erm..."
                harmony.say "What's so wrong about that?"
                mike.say "Read the story for yourself, Harmony."
                mike.say "She was married to another dude at the time!"
                "I see the confusion spread across Harmony's face."
                harmony.say "Oh dear!"
                harmony.say "That's not very nice at all!"
                "Now it's my turn to have a beaming smile plastered across my face."
                mike.say "This is great, Harmony."
                mike.say "I really feel like we're both learning something from this session."
                mike.say "You know, having our assumptions called into question and finding out new things about ourselves!"
                harmony.say "Erm...yeah...I guess so..."
                harmony.say "Look, how about we call it quits for today, [hero.name]?"
                mike.say "Oh, are you feeling tired?"
                harmony.say "Well, let's just say that you've given me a lot to think about..."
    "I wave goodbye to Harmony, feeling like I've really made some serious progress during this session."
    "Even though I can't quite put my finger on just what that progress might be."
    "But whatever it is, I have the added bonus of knowing that it's also brought me that much closer to Harmony too."
    return

label harmony_event_05:
    if harmony.love.max < 80:
        $ harmony.love.max = 80
    show harmony
    "Sitting down in the uncomfortably small room that's been the venue for all of my bible study classes with Harmony thus far, I sense something in the air."
    "And it's something apart from the usual sexual tension and burning sense of shame that I still feel at the memory of her catching me in the bathroom."
    "Sure, she's all smiles and encouragement as she pats the seat next to her and picks up her bible."
    "But there's an edginess about her that makes it all seem somehow forced, as though she's struggling to keep it up."
    mike.say "Erm, Harmony..."
    mike.say "Are you okay?"
    mike.say "You look a little...well, a little tense."
    show harmony happy
    "At this, Harmony's smile becomes even wider and more painfully forced than before."
    "She shakes her head, clearly trying to push away my concerns and press on with her planned agenda."
    harmony.say "Whatever do you mean, [hero.name]?"
    harmony.say "Me, tense - don't be silly!"
    show harmony normal
    "She pauses to let out a small cough, and I notice that her cheeks are flushing right before my eyes."
    mike.say "You sure about that?"
    mike.say "If you're feeling ill, we can always reschedule."
    harmony.say "No, really - I'm fine."
    harmony.say "And anyway, this is a really important lesson."
    harmony.say "We're going to be putting aside the reading of a passage from the bible this week."
    mike.say "How does that work?"
    mike.say "Is it really bible study if we're not actually studying the bible?"
    show harmony happy
    "Harmony's forced smile returns as she dismisses my concerns with a wave of her free hand."
    harmony.say "I feel it's important that we start applying what we've learned to our lives and habits."
    show harmony normal
    harmony.say "Well, specifically to yours, [hero.name]."
    "Ah...I should have known that this was going to come up, sooner or later."
    mike.say "Are you talking about what happened..."
    harmony.say "In the spare room, yes."
    harmony.say "But it's not the specific details that are important."
    harmony.say "Not for the sake of this lesson."
    "From the way Harmony rapidly glosses over the actual gory details, I can tell that the memory still bothers her."
    "So does that account for the atmosphere that I sensed when I first walked into the room?"
    show harmony annoyed
    harmony.say "You must understand that what you were...doing, is not just gross."
    harmony.say "It's also a sin, [hero.name]!"
    "All I can do is shrug in response and answer meekly."
    mike.say "I...I guess so."
    show harmony normal
    harmony.say "God gave you those parts of your body to create new life, [hero.name]."
    harmony.say "But what you were doing meant that gift was wasted."
    harmony.say "Wasted in the pursuit of selfish pleasure!"
    "There's a strange kind of zeal in Harmony's voice as she talks about this most intimate of subjects."
    "One moment she seems to be burning with holy righteousness."
    "But the next there's something almost dark and guilt-ridden as she dwells on the details of sin."
    mike.say "But what if someone wants to have...well, have sex without getting pregnant?"
    mike.say "Doesn't it get wasted then too, if the guy wears a rubber?"
    show harmony annoyed
    harmony.say "Contraception is EVIL - and condoms are the Devil's squishy boots!"
    "I have to lean back a little as Harmony delivers this outburst, which clearly hit a nerve."
    menu:
        "Agree":
            mike.say "I never really thought about it like that, Harmony."
            mike.say "But if God gave us those unmentionable parts of our bodies to make babies, then you're right."
            mike.say "It would be wrong and wicked to use them for the pursuit of earthly pleasures."
            show harmony happy
            "The fanaticism fades from Harmony's eyes to be replaced with a look of almost smug satisfaction."
            harmony.say "There's nothing wrong with a man and a woman using their bodies to worship the Lord, [hero.name]."
            show harmony normal
            harmony.say "So long as they do it within the sanctity of holy wedlock and without things getting...well, weird and ungodly."
            harmony.say "And if they're lucky, their union will be blessed with a new life."
            "Deferred gratification - not the most instantly appealing of philosophies."
            "But maybe it could work?"
            mike.say "That sounds wonderful, Harmony."
            mike.say "But I'm scared that I might be too weak - too tempted by the flesh!"
            show harmony happy
            $ harmony.love += 5
            "Harmony places a hand upon mine, smiling indulgently at my admission of weakness."
            harmony.say "It takes strength to admit weakness, [hero.name]."
            harmony.say "Don't worry - I'm here to help you along the path to righteousness."
            "For some reason, just knowing that Harmony has my back (in a purely spiritual sense) is a great comfort."
            "With her help, I might just be able to make these ideas of abstinence and chastity work."
        "Disagree" if hero.knowledge >= 30:
            mike.say "Sorry, Harmony, but I just don't buy it!"
            show fx question
            show harmony sad at center, vshake
            harmony.say "I...wha...what did you just say?"
            harmony.say "Did you not understand the lesson?"
            "It's now my turn to shake my head, dismissing the question completely."
            mike.say "I understand what you said, Harmony."
            mike.say "I just think that you're wrong, that's all."
            show harmony annoyed
            "Harmony frowns at this, beginning to look annoyed at my disregard for the moral she's trying her best to instill."
            harmony.say "Oh you do, do you?"
            mike.say "Okay, okay - hear me out."
            mike.say "God made you, right?"
            "Harmony nods, still frowning."
            mike.say "And he wants you to be happy, right?"
            "Harmony nods again, now looking confused as to just where I'm going with this."
            mike.say "So why did he make you in a way that means being sinful can make you so happy?"
            mike.say "And if sex is just for making babies, why did he make the first part feel so good?"
            mike.say "Because from what I hear, the bit at the end doesn't seem to be much fun at all!"
            show harmony sad at left4 with ease
            "Harmony looks away from me, shaking her head as if trying to dislodge troubling thoughts from her mind."
            "I know that what I'm saying must be getting to her, or else she'd be preaching back at me, or at least denying the truth of it all."
            $ harmony.purity -= 5
            show harmony annoyed at center with ease
            harmony.say "No, it's...it's wicked!"
            mike.say "It's like what I was getting up to in the spare room, Harmony."
            show harmony sad
            harmony.say "[hero.name], please...no!"
            mike.say "God made you, and he made you beautiful, made you desirable..."
            mike.say "It was your beauty, your God-given beauty that made me do that."
            mike.say "So, in a way, I was celebrating his creation, just like we do in Church..."
            harmony.say "[hero.name], stop...please!"
            "I do as she asks, but I can see just how deeply my words have affected her."
    show harmony normal
    "We wrap up the study session there, with each of us having a great deal to think about and needing privacy to do so."
    "Harmony unusually quiet as we leave the room and go our separate ways."
    hide harmony with dissolve
    "And I wonder if these sessions are having as much of an effect on her as they are on me."
    return

label harmony_event_06:
    if harmony.love.max < 100:
        $ harmony.love.max = 100
    show harmony
    "As the appointed hour for my fourth session of bible study with Harmony comes around, I really shouldn't be as nervous as I am."
    "We've done this a couple of times before, and it's always seemed to go pretty well."
    "Give or take a bit of a rocky start..."
    "So I should be getting used to the idea of spending time alone with her, right?"
    "But then maybe I would be less tense at the prospect if we weren't still meeting in a neutral location."
    "Even after all these sessions, we're still meeting in the same room at the church."
    "I honestly can't remember how the notion came about in the first place, but we've not changed venue since."
    "But I do recall that it was Harmony who said it'd be a good idea for us to get to know each other a little better."
    "Apparently she feels that we're beyond needing to have so many boundaries between us."
    "And getting into deep, meaningful conversations about the word of God should be easier for me in his own house."
    "Because of course, having someone like Harmony sitting so close to me is no sweat whatsoever, especially in church!"
    "If you hadn't guessed, I was being sarcastic just now."
    "I seem to find it hard enough to be close to Harmony when there's a crowd of people around us."
    "Bible studies aside, the only time I've been alone and so close with her was in that bathroom..."
    "But it's probably a bad idea to go dragging that particular memory up right now."
    show harmony happy
    harmony.say "Hey, [hero.name]!"
    harmony.say "I'm sorry we couldn't do this at your place."
    show harmony normal
    harmony.say "I'm sure it's very...nice."
    "What does she mean by that?"
    "Was she expecting me to live in some kind of squat in a bad neighbourhood or something?!?"
    "No...no, that's not it at all - it's just an innocent comment, nothing more."
    mike.say "Ah...thanks, Harmony."
    mike.say "But my housemates normally leave it looking like a bomb's hit it!"
    "At the mention of [bree.name] and Sasha, I can see a definite look of disapproval pass over Harmony's face."
    show harmony annoyed
    harmony.say "Oh yes, I remember you mentioning them - [bree.name] and...Sasha, right?"
    "Although she manages to make it sound light and breezy, Harmony's face twists a little as she says the other girl's names."
    "And for a moment I can't help being put in mind of someone being forced to recall a couple of cockroaches and not liking the experience."
    "I'm about to leap in and say something in their defence when I remember how religious and old-fashioned she really is."
    "No doubt the idea of two young, unmarried women living with a man is sinful in her mind."
    "I wonder for a moment why she doesn't have the same reaction to me."
    "But then I recall that she's actively trying to save my soul from damnation, and so probably wants to rescue me from this terrible fate..."
    show harmony happy
    "Harmony smiles, pulling out her bible and motioning for me to do the same."
    harmony.say "Okay then - let's hope we won't be disturbed while we get into a very important subject."
    show harmony normal
    harmony.say "Now don't be afraid, [hero.name] - but we're going to talk about something closely related to your own particular problems today."
    harmony.say "We'll be reading the story of Samson and Delilah, then discussing the dangers of uncontrolled passion."
    "I nod, trying not to look too worried about the prospect of what she has in mind."
    "While I may not remember many bible stories in great detail, I do know this one."
    "Hell, they even made a movie out of it!"
    "I smile and nod as Harmony recounts the brawny Samson slaughtering the Philistines with his trusty ass's jawbone."
    "But by the time he's been shorn of his locks and betrayed, bringing the place down on everyone, she's really getting into the swing of narrating this shit."
    "Her chest is practically heaving and her breath seems to be coming in gasps as she describes Samson's emotional torment."
    "Jesus, but she's giving me a raging erection right now!"
    menu:
        "Tell Harmony you understand the moral of the story":
            "I have to stop her, or I'm afraid that I'll cum in my pants!"
            mike.say "Harmony, I get it!"
            show harmony happy
            $ harmony.love += 5
            "She stops suddenly, her eyes almost burning with emotion as she stares at me."
            mike.say "Really, I do!"
            mike.say "Samson was given a wondrous gift by God."
            mike.say "And he threw it all away for the sake of tawdry passion, which damned him in the eyes of the almighty!"
            show harmony normal
            "Harmony nods as the words spill out of me, the motion becoming ever more intense as I confess my understanding."
            mike.say "I was on that same path, Harmony - I see it now."
            mike.say "I was about to bring it all tumbling down on myself!"
            mike.say "Well, in a metaphorical sense, anyway..."
            show harmony happy
            "There are actually tears in her eyes as I say this, and she claps in approval."
            harmony.say "Oh, [hero.name] - the scales have finally fallen from your eyes!"
            "She throws her arms around me, and I return the gesture."
            "But for the very first time, I don't feel awkward or consumed by lust."
            "Is it possible?"
            "Has she actually saved my soul?"
        "Offer Harmony an alternate moral to the story" if hero.knowledge >= 40:
            "I have to stop her, as I can't go on like this any longer."
            mike.say "Harmony, I get it!"
            "She stops suddenly, her eyes almost burning with emotion as she stares at me."
            mike.say "Really, I do!"
            mike.say "I see what you've been trying to do all along."
            mike.say "That you've been pretending to save me, but that you really wanted me to save you!"
            "Harmony makes to speak, but the words die in her mouth as she realises what I just said."
            mike.say "You could have chosen any other bible story about love, but you chose this specific one."
            mike.say "I see that you didn't mean I was Samson."
            mike.say "But that you were Delilah!"
            "Harmony starts to shake her head, trying to regain her habitual control of the situation."
            harmony.say "No, [hero.name]...no, you've mistaken what I was trying to..."
            mike.say "No, Harmony - don't lie to yourself any longer."
            mike.say "You know as well as I do that if Delilah had just been honest with herself, admitted that she loved Samson and been faithful to him."
            mike.say "Then none of the terrible things that happened at the end of the story needed to have happened!"
            show harmony sad
            "I see the confusion growing in her eyes as she actually begins to consider my words."
            "Deep down, she knows that what I'm saying makes sense, even if she's never considered it from this new angle before."
            show harmony normal
            mike.say "God made us both, Harmony."
            mike.say "And if two of his children feel a love for each other, who are we to find fault with that?"
            mike.say "Is there really any more natural and beautiful way to celebrate the wonders of his creation?"
            "I lean in as close as I dare, aware that this is the critical moment where I either win big or else lose it all."
            $ harmony.purity -= 5
            hide harmony
            show harmony kiss
            with dissolve
            $ harmony.flags.kiss += 1
            "She makes no effort to stop me as my lips press against her own."
            "For a terrible moment I'm convinced that she's about to pull away and slap me into the middle of next week."
            "But then I feel her resistance falter, and a second later it seems to melt away entirely."
            "Harmony returns the kiss with a passion that grows slowly and yet soon becomes pleasantly intense."
            "Admittedly, she doesn't tear off my clothes or throw herself on the ground before me."
            "But then even a kiss is a huge step for a girl as moral and pure as she is."
            "And more than anything else, it's a good place to start!"
            hide harmony kiss
    return

label harmony_event_07:
    show harmony close
    "It's hard to choose a suitably wholesome thing to do on a date with a girl like Harmony."
    "So in the end, I just go with the first thing that comes into my head without any perverse overtones."
    mike.say "Erm, how about we go roller-skating next saturday, Harmony?"
    "Harmony looks at me with a slightly puzzled expression."
    "Clearly not expecting to have been asked that, of all things."
    harmony.say "Sure, [hero.name]...why not!"
    hide harmony
    $ hero.cancel_activity()
    $ hero.calendar.add(game.calendar.get_next_day_of_week("saturday"), DateAppointment(14, "harmony", "Date at the park (Harmony)", "harmony_event_08", "missed_harmony_event_08"))
    return

label missed_harmony_event_08(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Harmony is going to be mad."
        $ harmony.love -= 10
    $ DONE.pop("harmony_event_07", None)
    $ storytracker.refresh()
    return

label harmony_event_07_fix:
    $ DONE.pop("harmony_event_07", None)
    return

label harmony_event_08(appointment=None):
    $ DONE["harmony_event_08"] = game.days_played
    show bg park with fade
    $ harmony.flags.sexycasual = True
    if harmony.love.max < 120:
        $ harmony.love.max = 120
    "Part of me still can't believe that I asked Harmony to go roller skating me with for a date."
    "And the other half frankly amazed by the fact that she actually said yes!"
    "I was trying to think of something that was fun, but not too obvious."
    "More wholesome than your run of the mill date, yet not completely lame either."
    "And all I could come up with was roller skating."
    "I figured that it'd need me to get close to Harmony without having to make any excuses."
    "Problem is that I haven't been roller skating since I was a kid."
    "But I'm not about to tell Harmony that!"
    "So that's how I find myself waiting for her to turn up in the roller rink entrance hall."
    "I try not to notice that most of the other patrons seem to be kids and their parents."
    "That's just the kind of self-conscious bullshit that can ruin an otherwise fun date."
    "Or at least that's what I tell myself as I look around, searching for a sight of Harmony's arrival."
    "It's not hard to spot her when she actually turns up."
    "For one thing, she's one of the few adults not followed by a gaggle of kids."
    "But there's also the fact that she's undoubtedly the hottest girl in the whole place..."












    show harmony casual with dissolve
    if harmony.purity < VLP:
        "Maybe telling Harmony to wear something loose and short was a mistake."
        "Especially when there are so many innocent pairs of eyes looking her way!"
        "She seems to have chosen the shortest and most revealing skirt imaginable."
        "And the way she walks towards me draws lustful gazes from the dads present, as well as making the mums look daggers in her direction."
        "It's only when she gets closer that I catch a glimpse of something that makes me gasp."
        "Don't quote me on this - but I'm almost certain she's not wearing anything under that skirt!"
    elif harmony.purity < LP:
        "I told Harmony that she might want to wear something loose and short."
        "And she seems to have taken that advice to heart as she sashays towards me."
        "Her skirt is very short indeed, and she makes sure that it bounces and rises with every step she takes."
        "My instant interest doesn't escape her notice either."
        "And Harmony smiles in an almost wicked manner at my obvious approval of her outfit."
    else:
        "Harmony seems to have taken my advice on how to dress for roller skating."
        "I suggested something loose and short, and her skirt certainly fits both those criteria."
        "She seems a little conscious of just how short the skirt is, at least compared to her usual style of dress."
        "But I take the fact that she doesn't spend the whole time yanking it down as a positive."
        "In fact, my smile of approval even seems to make her less uneasy and more confident in what she's wearing."
    "I force a smile onto my face as Harmony finally reaches me, trying to forget my observations about her outfit."
    show harmony happy
    "She returns the gesture, that pretty, innocent face lighting up with what looks like genuine delight at seeing me."
    mike.say "Hey, Harmony."
    mike.say "I'm so glad you decided to turn up!"
    "Ah, shit - why did I have to go and blurt out a lame line like that?"
    "Now it looks like I was worried that she was going to stand me up!"
    show harmony close happy
    "The smile stays on Harmony's face, but she raises her eyebrows in surprise."
    harmony.say "Why, of course I did, [hero.name]!"
    harmony.say "I just LOVE roller skating."
    show harmony normal
    "Harmony underlines the point with an expansive gesture of the hands."
    harmony.say "I used to skate all the time when I was younger."
    harmony.say "Back then I won all sorts of trophies and medals."
    hide harmony
    show harmony casual happy
    "She doesn't seem to notice the fact that my eyes boggle at this admission."
    harmony.say "But don't worry - I'm sure I can remember most of those old moves!"
    show harmony blush
    "She underlines this with a wink, then takes me by the hand and pulls me towards the desk to hire our roller skates."
    show harmony normal
    "No wonder she was so eager to take me up on the offer of a turn around the roller rink."
    "She's some kind of Olympic roller skating champion!"
    "And I'm about to look like a clumsy oaf on wheels..."
    "I keep on worrying about making a fool of myself as we collect our roller skates and put them on."
    "It's only when we get out onto the actual roller rink that my fears are somewhat allayed."
    "Harmony grabs my hand again and eagerly pulls me out onto the floor."
    "Luckily for me she seems so keen to show off her skills that she's not about to let me flail around on my own!"
    show harmony happy
    "She smiles as I travel along in her wake, clearly enjoying being the one in the driving seat."
    "And before too long, I actually feel like I'm getting the hang of it."
    show harmony normal
    "Harmony seems to notice my increased confidence too."
    "She responds by pulling me into ever closer and more complicated moves alongside her."
    menu:
        "Follow her lead":
            "I might be getting more confident with the whole roller skating thing."
            "But I'm still too unsure of myself to even think of taking the lead."
            "And so I decide to sit back and let Harmony take the lead."
            "I figure that I should keep things clean while I'm the rank amateur here."
            "Getting down and dirty on wheels will just have to wait!"
            if harmony.purity >= VHP:
                show harmony roller a with dissolve
                "Harmony seems to almost instantly understand that I want to follow her lead."
                "And she also seems perfectly happy to take me through a complicated routine of her own devising."
                "We spin, twist and turn so quickly that I can't always tell which way I'm headed!"
                "And even though we seldom come close to actually touching, it's pretty exhilarating all the same."
                "When we come to the apparent end of the routine, Harmony seems genuinely pleased with my performance."
                "She smiles like a Cheshire cat as she leads me off of the rink floor, beaming with happiness."
                $ harmony.love += 10
            elif harmony.purity >= HP:
                show harmony roller a with dissolve
                "Harmony seems to almost instantly understand that I want to follow her lead."
                "And she also seems perfectly happy to take me through a complicated routine of her own devising."
                "We spin, twist and turn so quickly that I can't always tell which way I'm headed!"
                "We come close to touching a couple of times, but I make sure we keep our distance from each other."
                "When we come to the apparent end of the routine, Harmony pretty happy with my performance."
                "She smiles, and yet I wonder if she was totally okay with me not contributing more than I did."
                $ harmony.love += 5
            elif harmony.purity < VLP:
                show harmony roller b with dissolve
                "Harmony seems to almost instantly understand that I want to follow her lead."
                "But she also takes this as a clear invitation to indulge herself at the same time."
                "We spin, twist and turn so quickly that I can't always tell which way I'm headed!"
                "She's constantly pressed against me, grinding herself into me the whole time."
                "Harmony does everything in her power to get my hands below her already skimpy skirt."
                "But my constant efforts to avoid her suggestive behaviour means that she ends up frustrated."
                "By the time she leads me off of the rink floor, Harmony looks pretty flustered and annoyed."
                $ harmony.love -= 10
            elif harmony.purity < LP:
                show harmony roller b with dissolve
                "Harmony seems to almost instantly understand that I want to follow her lead."
                "But the way she leads me through the routine that follows makes me aware that she's not best pleased."
                "We spin, twist and turn so quickly that I can't always tell which way I'm headed!"
                "Harmony seems to take every opportunity that presents itself to press herself against me."
                "My response is to evade her efforts and do all I can to keep things clean in front of our youthful audience."
                "This means that by the time she leads me off of the rink floor, Harmony looks pretty frustrated and annoyed."
                $ harmony.love -= 5
            else:
                show harmony roller b with dissolve
                "Harmony seems to almost instantly understand that I want to follow her lead."
                "She makes no complaints about this, taking me through a complex routine of her own devising."
                "We spin, twist and turn so quickly that I can't always tell which way I'm headed!"
                "More than once she presses herself against me, but I try to keep the whole thing clean."
                "When we come to the apparent end of the routine, Harmony smiles at me pleasantly."
                "But I get the instant feeling that she would have been happier if I'd contributed more."
                $ harmony.sub -= 10
        "Make it lewd":
            "I feel like I'm getting ever more confident with the whole roller skating thing."
            "So much so that I don't hesitate to take the lead as soon as we hit the rink."
            "Harmony is taken by surprise, probably thinking that she was going to be the one to take the lead."
            "Well, I'll soon show her that she's not dealing with a rank amateur."
            "I also have no intention of keeping her in the dark as to just what I want..."
            if harmony.purity >= VHP:
                show harmony roller a with dissolve
                "Harmony instantly stiffens, becoming almost rigid as she realises my true intentions."
                "I don't have the chance to lead her through the smallest portion of what I have in mind."
                "It's almost as if she has a sixth sense for sleazy intent and just won't stand for it."
                "What I do manage to pull off is awkward and frustrating in the extreme."
                "And Harmony remains as stiff as a corpse throughout the entire thing."
                "As soon as the chance presents itself, her breaks free of me and storms off of the rink."
                $ harmony.love -= 10
            elif harmony.purity >= HP:
                show harmony roller a with dissolve
                "Harmony goes quite stiff the moment that she realises I'm intent upon taking the lead."
                "And her face becomes a mask of fear when it then dawns on her that I want to get as close as I can."
                "She goes along with it for a little while, but she's glancing this way and that the whole time."
                "It's as if she's convinced that we'll be thrown out at any moment for lewd behaviour."
                "She doesn't relax the entire time we're on the floor of the rink."
                "And when we come off of it, she's dead silent, her eyes fixed on the ground before her."
                $ harmony.love -= 5
            elif harmony.purity < VLP:
                show harmony roller c with dissolve
                "Harmony surrenders herself to me almost the very second that we're out on the ring."
                "If she uses her superior skills as a skater at all, it's to make sure I keep a hold of her the whole time."
                "All I'd intended to do was some seriously dirty dancing as we made our way around the rink."
                "But as soon as the chance presents itself, Harmony grabs my hand and shoves it under her skirt."
                "A moment later I know for sure that she's going commando, as well as that she's slick as hell down there."
                "I hear her moan audibly as I stroke her between the thighs, and she responds by squeezing my cock pretty damn hard too!"
                "That no one seems to see what's going on has to be some kind of minor miracle."
                "And when we finally come off the ice, I'm almost bent double, only able to think about getting into Harmony..."
                $ harmony.love += 10
            elif harmony.purity < LP:
                show harmony roller b with dissolve
                "Harmony doesn't seem at all surprised when I make it clear that I intend to take the lead."
                "And instead of using her superior skills as a skater to avoid my advances, she does the exact opposite."
                "No matter where we go on the roller rink, I can feel the soft warmth of her body against me the whole time."
                "I hardly have to try at all, as Harmony practically attaches herself to me, sticking like glue."
                "She makes it clear that she's getting off on this too, breathing heavily and sighing into my ear."
                "By the time we finally come to leave the floor of the rink, I'm hot, sweaty and exhausted."
                "And I make sure Harmony stays right in front of me, so as to hide the fact that I'm stiff as a board."
                $ harmony.love += 10
            else:
                show harmony roller b with dissolve
                "Harmony stiffens a little when she realises that I want to take the lead and won't take no for an answer."
                "But then, just as quickly, she seems to get to grips with the notion and relax again."
                "Emboldened by this, I make to put some of my most suggestive moves on her."
                "She gasps at this, realising my true intentions, but she doesn't slap my face or storm out of the place."
                "Instead she begins to make a kind of game out of escaping my clutches."
                "She's by far the better skater, so this isn't exactly hard for her."
                "And by the time we're done, I feel exhausted, a little frustrated, but very much aroused by her antics."
                $ harmony.sub += 10
    $ harmony.flags.sexycasual = False
    $ game.pass_time(2, True)
    return

label harmony_event_09:
    show harmony close
    "I've never been to the place with Harmony before, but most girls I know use any excuse to go there."
    mike.say "What about the Mall, Harmony?"
    mike.say "We could go hang out there for a few hours, next saturday, maybe?"
    harmony.say "Hmm..."
    harmony.say "Okay, [hero.name] - that sounds like it could be fun!"
    $ hero.cancel_activity()
    $ hero.calendar.add(game.calendar.get_next_day_of_week("saturday"), DateAppointment(14, "harmony", "Date at the mall (Harmony)", label="harmony_event_10", fail_label="missed_harmony_event_10"))
    hide harmony
    return

label missed_harmony_event_10(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Harmony is going to be mad."
        $ harmony.love -= 10
    $ DONE.pop("harmony_event_09", None)
    $ storytracker.refresh()
    return

label harmony_event_09_fix:
    $ DONE.pop("harmony_event_09", None)
    return

label harmony_event_10(appointment=None):
    $ DONE["harmony_event_10"] = game.days_played
    scene bg mall1
    show harmony casual
    with fade
    if harmony.love.max < 140:
        $ harmony.love.max = 140
    "I have to confess that I was in two minds about asking Harmony out for a walk around the mall."
    "As innocent and ordinary as that sounds, you have to remember that she's pretty keen on Jesus."
    "And seriously religious types can sometimes be seriously down on the whole consumerist culture of such a place."
    "But almost as soon as we walk in through the automatic doors, I feel like I can breathe a metaphorical sigh of relief."
    "Harmony's eyes are just as wide and filled with dreams of the shiny things that fill the stores as the next girl."
    "I can't help smiling as she hangs off of my arm, laughing and chattering about everything and nothing."
    "The conversation is hardly one-sided, but I'm hard-pressed to remember what contributions I've made to it."
    "I'm far more interested in stealing glances at Harmony or checking out her reflection in the windows."
    "And the fact that she's getting more than a few admiring glances from guys in passing is also an ego-polish."
    "More than a couple of girls look at her with jealousy clear to see in their eyes as well."
    "But Harmony doesn't seem to notice the attention that she's attracting from either gender."
    show harmony happy
    "She appears more than happy to bask in the light of my own attention."
    "Which just so happens to be something that I'm more than happy to give her."
    "We've been wandering slowly around the mall for what must be almost an hour by now."
    "And so far the time has passed in a pleasant kind of haze as we flit from one window to the next."
    show harmony normal
    "But then I notice that Harmony's gone quiet beside me."
    "I glance at her, wondering what's up."
    "And then I see that she's staring straight ahead, totally silent."
    "I start to say something, but then I shut up and just follow her gaze."
    "And then I see what's on the other side of the glass and has her temporarily spellbound."
    menu:
        "Go to a Bridal boutique":
            "The window is packed with mannequins, all of which wear bridal dresses."
            "Every shade of white, ivory and pearl, in every style imaginable is arrayed before us."
            "Harmony's eyes flit from one dress to the next."
            "And I swear that I can see her chest rising and falling ever faster."
            if harmony.purity >= VHP:
                show harmony happy
                harmony.say "Oh, [hero.name]!"
                harmony.say "Aren't they beautiful?"
                harmony.say "Pure white - just like the blushing, virgin bride they're made for!"
                "I can hear the passion and intensity in her words."
                "And I swallow nervously before replying."
                mike.say "Yeah, Harmony - they're pretty special!"
                "Lame, I know - but she's so brimming with delight I can't think what else to say!"
                $ harmony.love += 10
            elif harmony.purity >= HP:
                harmony.say "Ah, so many white dresses."
                show harmony sad
                "She shakes her head, as if suddenly disheartened."
                harmony.say "[hero.name] - why do so many girls wear white?"
                harmony.say "Don't they value virginal purity as the gift it truly is?!?"
                "I gulp at the passion of Harmony's tirade against the moral decay of the current age."
                mike.say "I guess they're just not as close to God as you are, Harmony!"
                "She nods, then shakes her head at the depravity of women in general."
                $ harmony.love += 5
            elif harmony.purity < VLP:
                show harmony angry
                harmony.say "Virginal brides, all dressed in white."
                harmony.say "Hah - what a crock of shit!"
                harmony.say "I bet half the girls who buy those dresses end up sucking another dude's cock on the big day!"
                "I can't help letting out a gasp of shock and surprise at hearing what Harmony just said."
                mike.say "Harmony, please - someone'll hear you!"
                show harmony annoyed
                "Harmony curls her lip at me, clearly annoyed at my show of prudishness."
                harmony.say "Jesus, [hero.name] - who yanked on your tampon?"
                "She laughs out loud, and then walks away from me, shaking her head in evident disgust."
                $ harmony.love -= 10
            elif harmony.purity < LP:
                harmony.say "Ooh...so much white!"
                harmony.say "I wonder how many brides are REALLY virgins!"
                "At this, she leans back against me in the most suggestive manner possible."
                show harmony blush
                harmony.say "If they are, then they don't know what they're missing!"
                "Feeling instantly flustered, I shove her off of me and almost push her into the glass of the window."
                show harmony annoyed
                harmony.say "HEY!"
                harmony.say "Geez, [hero.name] - since when did you turn into such a prude?!?"
                $ harmony.love -= 5
            else:
                show harmony happy
                harmony.say "I've always dreamed about my wedding day."
                harmony.say "I imagined every little detail, right down to the colour of the flowers."
                show harmony normal
                "She shakes her head a little ruefully."
                harmony.say "But all of that seems a bit weird to me now."
                harmony.say "Almost like something changed without me noticing it..."
                mike.say "I guess that's just something all little girls do."
                mike.say "Maybe you just grew up a bit?"
                "Harmony nods, but I can see from the look on her face that she's still troubled by the thought."
        "Go to a lingerie store":
            "The window is packed with mannequins, which is nothing out of the ordinary."
            "But every last one of them is clad in nothing but underwear."
            "And when I say underwear, I don't mean support pants and utilitarian bras."
            "All I can see is lace and nylon, in shades of white, black and red."
            "It's only one of those sanitised lingerie shops, nothing extreme or fetishistic in nature."
            "But all the same, Harmony's eyes are as wide as saucers as the gazes through the glass..."
            if harmony.purity >= VHP:
                show harmony angry
                harmony.say "Urrgh!"
                harmony.say "Filth, filth and more filth!"
                harmony.say "What kind of a whore would wear something like that?"
                harmony.say "And what kind of a man would want to see a woman in it?!?"
                show harmony annoyed
                "At this last question, Harmony rounds on me."
                "I feel the weight of her gaze fall on me, and I know she expects me to back her up."
                mike.say "I don't know, Harmony."
                mike.say "We shouldn't judge people on what they do behind closed doors..."
                "For a moment I think that she's actually going to slap me, and I flinch in anticipation of the blow."
                "But then she simply makes a loud harrumphing sound, and storms off alone."
                $ harmony.love -= 10
            elif harmony.purity >= HP:
                show harmony annoyed
                harmony.say "Eww!"
                harmony.say "Aren't they yucky, [hero.name]!"
                harmony.say "You'd never want to see me dressed like that - would you?"
                "Feeling like I've just been asked the most loaded question imaginable, I begin to sweat."
                "I look at the revealing lingerie for a moment, and then at Harmony's incredible figure."
                mike.say "I...I don't know, Harmony..."
                mike.say "Some of them might be nice - that one there looks like it'd give great support."
                "Harmony fires me a disapproving look and shakes her head."
                harmony.say "Oh, [hero.name] - whatever am I going to do with you?"
                harmony.say "We clearly need to step up your bible studies!"
                "And with that, she grabs my hand, pulling me away from the lingerie store."
                $ harmony.love -= 5
            elif harmony.purity < VLP:
                show harmony blush
                harmony.say "Wow...I could REALLY see myself in some of those."
                harmony.say "And I could see you in me at the same time..."
                "It takes a moment for the suggestive nature of what Harmony just said to sink in."
                show harmony close
                "But by then she's already grinding her ass into my groin as hard as she can."
                harmony.say "I'd want value for money."
                harmony.say "I'd want them to be enough to have you make me scream!"
                "It's then that I feel Harmony shove her hand down the front of my pants."
                "She grabs my already stiff cock, rubbing and squeezing without mercy."
                harmony.say "Maybe we could make it even more interesting?"
                harmony.say "Maybe we could add leather...maybe even some rubber?"
                "I can't help myself, and I cum in my shorts a few seconds later."
                "Harmony smiles wickedly, enjoying the sensation and rubbing my cum between her fingers."
                harmony.say "I'll take that as a yes!"
                $ harmony.love += 10
            elif harmony.purity < LP:
                show harmony happy
                harmony.say "Oooh, [hero.name] - come look at some of this stuff!"
                "Harmony presses her hands against the glass of the window, marvelling at what's on the other side."
                harmony.say "I wonder if they have any of it in my size?"
                show harmony normal
                "Suddenly she looks a little self-conscious, looking down at herself."
                harmony.say "I mean...sometimes they don't have plus sizes..."
                show harmony blush
                "But then she looks back up at me, raising her eyebrows in a suggestive manner."
                harmony.say "Imagine that, [hero.name] - you'd just have to enjoy me naked!"
                "Suddenly I feel incredibly hot and bothered, aware of how close I am to all these other human beings."
                "Harmony's suggestive smile is more than enough to make my cock get hard in record time."
                mike.say "We...we could...ask..."
                mike.say "We could always go in and ask!"
                show harmony happy
                "Harmony almost squeals in pleasure, grabbing my hand and pulling me into the lingerie store after her."
                $ harmony.love += 5
            else:
                harmony.say "You know, it's weird."
                harmony.say "Before I met you, something like this would have made me real mad."
                harmony.say "But now...well, it just doesn't seem to be that big of a deal!"
                "I try to laugh the comment off, not wanting to come across as having corrupted Harmony."
                "But I can see from the way she's gazing into the window that she's telling the truth."
                "Back when I first met her, she'd have been in there with a pitchfork and a burning torch!"
                mike.say "You make it sound like I'm leading you astray!"
                show harmony happy
                "Now it's her turn to laugh, as she slaps me playfully on the shoulder."
                harmony.say "I wouldn't go that far!"
                show harmony normal
                harmony.say "I guess you just helped to broaden my horizons, that's all."
                "Harmony smiles, taking my arm and leading me away from the lingerie store."
                "The whole time my mind is filling with images of her in some of the stuff in that window..."
    return

label harmony_event_01_vanilla:
label harmony_event_01_slutty:
    show harmony close
    mike.say "Can I invite you at my place, Harmony?"
    mike.say "We could have a nice time together."
    mike.say "Maybe next week, if you're up to it?"
    harmony.say "Hmm..."
    harmony.say "Okay, [hero.name] - I'll be there!"
    $ hero.cancel_activity()
    if 'slutty' in harmony.traits:
        $ hero.calendar.add(game.calendar.get_next_day_of_week("saturday"), DateAppointment(20, "harmony", "Date at home (Harmony)", label="harmony_event_02_slutty", fail_label="missed_harmony_event_02_slutty"))
    else:
        $ hero.calendar.add(game.calendar.get_next_day_of_week("saturday"), DateAppointment(20, "harmony", "Date at home (Harmony)", label="harmony_event_02_vanilla", fail_label="missed_harmony_event_02_vanilla"))
    hide harmony
    return

label missed_harmony_event_02_vanilla(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Harmony is going to be mad."
        $ harmony.love -= 10
    $ DONE.pop("harmony_event_01_vanilla", None)
    $ storytracker.refresh()
    return

label missed_harmony_event_02_slutty(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Harmony is going to be mad."
        $ harmony.love -= 10
    $ DONE.pop("harmony_event_01_slutty", None)
    $ storytracker.refresh()
    return

label harmony_event_02_vanilla(appointment=None):
    call harmony_event_02_slutty (appointment) from _call_harmony_event_02_slutty
    return

label harmony_event_02_slutty(appointment=None):
    if harmony.love.max < 150:
        $ harmony.love.max = 150
    if bree.is_gone_forever or sasha.is_gone_forever:
        call harmony_event_02_slutty_alt from _call_harmony_event_02_slutty_alt
        return
    scene bg livingroom with fade
    "I'm all ready and prepared for my evening in with Harmony, making sure that the house is clean and tidy."
    "Sure, you might think that the idea of a date at home is pretty lame - but then you'd be so wrong!"
    "Because I'm managed to get [bree.name] and Sasha to haul their butts out of here for the night."
    "Which means that I have the whole house to myself - and Harmony all to myself as well!"
    play sound door_bell
    "I'm just putting the final touches to the place when I hear the sound of the door-bell."
    "Taking one last look around the sitting room, I nod in satisfaction at my efforts."
    "And then I make a dash for the front door."
    "I open it eagerly, already grinning at the mere thought of seeing Harmony in the flesh."
    scene bg house
    show harmony sexycasual
    with wiperight
    "And the sight definitely doesn't disappoint, as she's a genuine feast for the eyes!"
    "Taking in every inch and each individual curve that makes up her body, I almost forget to greet her!"
    mike.say "H...hey, Harmony!"
    mike.say "I'm so glad you're finally here!"
    show harmony happy
    "Harmony smiles and lets out a chuckle of laughter."
    "She cocks her head on one side as she does so, looking a little quizzical."
    show harmony normal
    harmony.say "Oh..."
    show fx question
    harmony.say "I'm not late, am I?"
    harmony.say "I thought we said about this time?"
    "I shake my head at this."
    hide fx
    mike.say "No, Harmony..."
    mike.say "I just meant that I've been looking forward to seeing you, that's all!"
    show harmony happy
    "Harmony's smile becomes wider still."
    "And I can see her starting to blush a little."
    "All of which just serves to make her look that much more adorable."
    harmony.say "Is that so?"
    show harmony blush
    harmony.say "Then you'd better let me come in, hadn't you?"
    "I step aside so that Harmony can walk into the hall."
    "Then I close the door and usher her into the sitting room."
    show bg livingroom
    show harmony sexycasual normal
    with fade
    "Harmony looks around, noting the cleanliness of the room and the subdued lighting."
    harmony.say "Ooh..."
    harmony.say "This place looks so nice, [hero.name]!"
    harmony.say "Somebody really put in a lot of effort, didn't they?"
    "Now it's my turn to blush a little."
    "I even find it hard to look Harmony in the eye."
    mike.say "I...I just wanted things to be nice for you, Harmony."
    mike.say "I even made sure that my housemates are out for the night."
    "At the mention of us being alone, Harmony raises her eyebrows."
    show fx exclamation
    harmony.say "You mean we're going to be alone all night?"
    mike.say "Erm...yeah."
    hide fx
    harmony.say "Just the two of us, with no distractions?"
    mike.say "Oh yeah!"
    show harmony happy
    harmony.say "That's great, [hero.name]!"
    harmony.say "The perfect chance to play the board-game I brought with me!"
    "Harmony whips a box out from behind her back."
    "And I see that she's not kidding - she really has brought a board-game."
    "Suddenly I see all of my amorous hopes fading into nothing."
    mike.say "Sure, Harmony..."
    mike.say "We could play your game."
    mike.say "But first, maybe we could..."
    "Harmony either doesn't hear everything I say."
    "Or else she just stops listening after I say yes."
    "Because she's already kneeling down on the floor and opening the box."
    show harmony normal
    harmony.say "Trust me, [hero.name]..."
    harmony.say "This game is SO much fun."
    harmony.say "You're going to love it!"
    "I slowly sit down on the other side of the board Harmony's unfolded."
    "And I console myself by pouring us both a glass of the wine."
    "I bought it especially for the occasion, and I'm damned if I'm not going to drink it."
    "Harmony busies herself over setting up the board, shuffling cards and arranging playing pieces."
    "And I can't help noting that the game's got some pretty nice artwork to it."
    "Those playing pieces are pretty nice too - like the minis that Jack paints!"
    mike.say "Erm, Harmony..."
    mike.say "Can I be the guy with the cool sword?"
    show harmony happy
    "Harmony looks up with a smile on her face."
    harmony.say "Sir Hector, the crusading knight?"
    harmony.say "Of course you can, [hero.name]."
    show harmony blush
    harmony.say "After all, you're MY knight in shining armour!"
    "I can't help smiling as Harmony winks and hands me the little knight."
    "He looks even better up close."
    "And I can imagine him coming to life, swinging his sword in anger!"
    show harmony normal
    harmony.say "Okay..."
    harmony.say "Everything's ready, [hero.name]."
    harmony.say "Let's play!"
    scene bg black with timelaps
    scene bg livingroom
    show harmony sexycasual zorder 3 at center
    with timelaps
    "I'd been dreading this moment, thinking the evening was ruined."
    "But it doesn't take me long to realise Harmony was right."
    "This game is pretty fun, and I find myself getting really into it."
    "Soon enough we're engrossed, wanting for each roll of the dice."
    if bree.hidden and sasha.hidden:
        "In fact, we're so engrossed that we forgot everything, including the passing hours."
        "By the time it's done, reality kicked back."
        show fx exclamation
        harmony.say "Oh dear..."
        harmony.say "Will you look at the time!"
        hide fx
        harmony.say "I have to get home!"
        mike.say "Erm...maybe we could do this again sometime soon?"
        mike.say "You wanna come over and hang-out again, Harmony?"
        harmony.say "Of course..."
        harmony.say "That sounds like a great idea!"
        hide harmony
        with moveoutright
        "We pack up the game and then I see Harmony out."
    else:
        "In fact, we're so engrossed that we don't even hear the front door open."
        show harmony at left4
        show bree casual zorder 1 at right
        with moveinright
        bree.say "Phew!"
        bree.say "It's okay, Sasha - they're not doing anything gross!"
        bree.say "They're just playing board-games."
        show harmony at left5
        show bree at right4
        show sasha casual angry zorder 2 at mostright4
        with moveinright
        sasha.say "What?"
        sasha.say "He kicked us out of the house for that?!?"
        sasha.say "I'm calling bullshit on this whole deal!"
        "Harmony and I look up to see [bree.name] and Sasha standing over us."
        "And it takes me a moment to pull my head out of the game."
        "But when I do, I point an accusatory finger at them."
        mike.say "What are you guys doing here?"
        mike.say "You were supposed to disappear tonight!"
        mike.say "Harmony and I were supposed to be left alone!"
        show sasha annoyed
        "Sasha rolls her eyes and snorts at this."
        sasha.say "Yeah well..."
        sasha.say "You go tell that to the guys down the pub!"
        show bree angry
        bree.say "Yeah, they kicked us out, [hero.name]!"
        bree.say "Said there was a leak in one of the pipes or something."
        "I'm about to get up and physically throw them out."
        "But then I feel Harmony put a hand on my arm."
        harmony.say "Don't be mad at them, [hero.name]."
        harmony.say "It sounds like it wasn't their fault."
        harmony.say "So why don't we let them join in our game?"
        show bree normal at left
        show sasha normal at right
        show harmony sexycasual at center
        with ease
        "Before I can object, [bree.name] and Sasha are sitting down too."
        "They seem to be just as drawn in by the game as I was."
        sasha.say "This thing has dragons in it?"
        sasha.say "Dragons are cool!"
        bree.say "Ooh..."
        bree.say "Are those fairies or elves?"
        bree.say "They're so pretty!"
        show harmony happy
        "Harmony happily explains the rules of the game to [bree.name] and Sasha."
        "At the same time I sit there in silence, fuming at their joining in."
        "This was supposed to be an intimate night for Harmony and me."
        "But now it's turned into an evening of wholesome family games!"
        "I do the best I can to make my feelings evident."
        "And yet it just doesn't seem to work, no matter how I try."
        scene bg black with timelaps
        scene bg livingroom
        show bree casual normal at left
        show sasha casual normal at right
        show harmony sexycasual at center
        with timelaps
        "For one thing, [bree.name] and Sasha are really into the game."
        "And their enthusiasm begins to rub off on me too."
        "Plus I've been playing for longer, so I have an advantage."
        "The ego-rub of being better at them and offering advice is too much."
        "Which means that pretty soon we're all engrossed in the game."
        "By the time it's done, everyone's getting on like old friends."
        show sasha happy
        sasha.say "That was pretty fun, guys!"
        show bree happy
        bree.say "Yeah, we should totally play another game!"
        show fx exclamation
        harmony.say "Oh dear..."
        harmony.say "Will you look at the time!"
        hide fx
        harmony.say "I have to get home!"
        show bree normal
        show sasha normal
        mike.say "Erm...maybe we could do this again sometime soon?"
        mike.say "You wanna come over and hang-out with us, Harmony?"
        harmony.say "Of course..."
        harmony.say "That sounds like a great idea!"
        show bree normal at left5
        show sasha normal at right5
        hide harmony
        with moveoutright
        "We pack up the game and then I see Harmony out."
        "And when I get back, [bree.name] and Sasha are still talking about her."
        show bree happy
        bree.say "Your date's a lot of fun, [hero.name]!"
        show sasha flirt
        sasha.say "Yeah, and she's hot too!"
        mike.say "Well...I certainly think so!"
        mike.say "I'm glad you guys like her."
        bree.say "Oh yeah - I can't wait to see her again."
        sasha.say "Me too - there's so much we could all do together!"
    return

label harmony_event_02_slutty_alt:
    scene bg livingroom with fade
    "I'm all ready and prepared for my evening in with Harmony, making sure that the house is clean and tidy."
    "Sure, you might think that the idea of a date at home is pretty lame - but then you'd be so wrong!"
    "Because I'm managed to get [bree.name] and Sasha to haul their butts out of here for the night."
    "Which means that I have the whole house to myself - and Harmony all to myself as well!"
    play sound door_bell
    "I'm just putting the final touches to the place when I hear the sound of the door-bell."
    "Taking one last look around the sitting room, I nod in satisfaction at my efforts."
    "And then I make a dash for the front door."
    "I open it eagerly, already grinning at the mere thought of seeing Harmony in the flesh."
    scene bg house
    show harmony sexycasual
    with wiperight
    "And the sight definitely doesn't disappoint, as she's a genuine feast for the eyes!"
    "Taking in every inch and each individual curve that makes up her body, I almost forget to greet her!"
    mike.say "H...hey, Harmony!"
    mike.say "I'm so glad you're finally here!"
    show harmony happy
    "Harmony smiles and lets out a chuckle of laughter."
    "She cocks her head on one side as she does so, looking a little quizzical."
    show harmony normal
    harmony.say "Oh..."
    harmony.say "I'm not late, am I?"
    show fx question
    harmony.say "I thought we said about this time?"
    "I shake my head at this."
    hide fx
    mike.say "No, Harmony..."
    mike.say "I just meant that I've been looking forward to seeing you, that's all!"
    "Harmony's smile becomes wider still."
    "And I can see her starting to blush a little."
    "All of which just serves to make her look that much more adorable."
    harmony.say "Is that so?"
    show harmony blush
    harmony.say "Then you'd better let me come in, hadn't you?"
    "I step aside so that Harmony can walk into the hall."
    "Then I close the door and usher her into the sitting room."
    show bg livingroom
    show harmony sexycasual normal
    with fade
    "Harmony looks around, noting the cleanliness of the room and the subdued lighting."
    harmony.say "Ooh..."
    harmony.say "This place looks so nice, [hero.name]!"
    harmony.say "Somebody really put in a lot of effort, didn't they?"
    "Now it's my turn to blush a little."
    "I even find it hard to look Harmony in the eye."
    mike.say "I...I just wanted things to be nice for you, Harmony."
    mike.say "I even made sure that my housemates are out for the night."
    "At the mention of us being alone, Harmony raises her eyebrows."
    show fx exclamation
    harmony.say "You mean we're going to be alone all night?"
    mike.say "Erm...yeah."
    hide fx
    harmony.say "Just the two of us, with no distractions?"
    mike.say "Oh yeah!"
    show harmony happy
    harmony.say "That's great, [hero.name]!"
    harmony.say "The perfect chance to play the board-game I brought with me!"
    "Harmony whips a box out from behind her back."
    "And I see that she's not kidding - she really has brought a board-game."
    "Suddenly I see all of my amorous hopes fading into nothing."
    mike.say "Sure, Harmony..."
    mike.say "We could play your game."
    mike.say "But first, maybe we could..."
    "Harmony either doesn't hear everything I say."
    "Or else she just stops listening after I say yes."
    "Because she's already kneeling down on the floor and opening the box."
    show harmony normal
    harmony.say "Trust me, [hero.name]..."
    harmony.say "This game is SO much fun."
    harmony.say "You're going to love it!"
    "I slowly sit down on the other side of the board Harmony's unfolded."
    "And I console myself by pouring us both a glass of the wine."
    "I bought it especially for the occasion, and I'm damned if I'm not going to drink it."
    "Harmony busies herself over setting up the board, shuffling cards and arranging playing pieces."
    "And I can't help noting that the game's got some pretty nice artwork to it."
    "Those plying pieces are pretty nice too - like the minis that Jack paints!"
    mike.say "Erm, Harmony..."
    mike.say "Can I be the guy with the cool sword?"
    show harmony happy
    "Harmony looks up with a smile on her face."
    harmony.say "Sir Hector, the crusading knight?"
    harmony.say "Of course you can, [hero.name]."
    show harmony blush
    harmony.say "After all, you're MY knight in shining armour!"
    "I can't help smiling as Harmony winks and hands me the little knight."
    "He looks even better up close."
    "And I can imagine him coming to life, swinging his sword in anger!"
    show harmony normal
    harmony.say "Okay..."
    harmony.say "Everything's ready, [hero.name]."
    harmony.say "Let's play!"
    scene bg black with timelaps
    scene bg livingroom
    show harmony sexycasual zorder 3 at center
    with timelaps
    "I'd been dreading this moment, thinking the evening was ruined."
    "But it doesn't take me long to realise Harmony was right."
    "This game is pretty fun, and I find myself getting really into it."
    "Soon enough we're engrossed, waiting for each roll of the dice."
    "In fact, we're so engrossed that we don't seem to notice the passing of time."
    "Or the fact that the wine in the bottle is steadily going down too."
    "When the game finally comes to an end, I'm amazed to see how late it's gotten."
    mike.say "Whoa..."
    mike.say "Harmony, have you seen the time?"
    "Harmony checks the time too."
    "And her eyes go wide with surprise."
    show fx exclamation
    harmony.say "Oh my goodness..."
    harmony.say "I'd better pack things up and get going."
    harmony.say "I have to get up early in the morning."
    harmony.say "And if I don't get enough sleep, I'll be so grumpy!"
    hide fx
    "I hurry to help Harmony pack the game away and collect her things."
    scene bg house
    with wiperight
    show harmony normal sexycasual with easeinleft
    "Then I walk her to the door."
    mike.say "That was pretty fun, Harmony."
    harmony.say "Oh yes, we should totally play another game!"
    mike.say "Erm...maybe we could make it sometime soon?"
    mike.say "You wanna come over and hang-out with me, Harmony?"
    harmony.say "Of course..."
    harmony.say "That sounds like a great idea!"
    "I'm smiling at the prospect of seeing Harmony again soon."
    "And I'm so distracted that I don't notice what she does next."
    "Which is to lean in and plant a little kiss on my cheek."
    hide harmony with easeoutright
    "Then she turns on her heel and walks off down the street."
    "I've had far more passionate kisses in the past."
    "But for some reason, that little peck leaves me staggered."
    "And I can feel my heart beating faster in my chest too."
    "Yet I have no idea how Harmony's able to have such an effect on me."
    "All I do know is that I want to experience more of that sensation."
    return

label harmony_event_03_vanilla:
label harmony_event_01_religious:
    show harmony normal
    "Harmony's looking at me in a weird way right now, cocking her head on one side and smiling."
    "I mean, there's nothing wrong with her doing that, it's just the way she's doing it - you know?"
    show harmony happy
    "Harmony keep staring and smiling just a little too long for it to be anything but uncomfortable."
    "And I'm starting to think that there's an ulterior motive behind all of this."
    "So the only logical thing I can do is call her out..."
    mike.say "Come on, Harmony..."
    mike.say "Spit it out!"
    show harmony normal
    "Harmony's smile instantly turns into a look of surprise."
    "She shakes her head, putting on a pretty good performance for my benefit."
    show fx question
    harmony.say "Whatever do you mean, [hero.name]?"
    harmony.say "I wasn't doing anything at all!"
    hide fx
    show fx drop
    harmony.say "You must be imagining things!"
    "Not only is Harmony less than convincing, she's also starting to babble."
    "And that's a sure sign she's trying and failing to cover something up."
    hide fx
    mike.say "Nice try, Harmony."
    mike.say "But you're the worst liar I ever met!"
    mike.say "So come on - spit it out!"
    "Harmony opens her mouth to reply."
    "And for a moment it looks like she's going to keep on trying to deny it."
    show harmony sad
    "But then she lets out a sigh and shakes her head, finally admitting defeat."
    harmony.say "Okay, [hero.name]..."
    harmony.say "I guess I'm busted!"
    harmony.say "There was something that I wanted to ask you."
    "I can't help smiling in triumph at calling Harmony out."
    "And I nod at the same time, letting her know I'm cool with that."
    "The least I can do now is actually let her ask the question that's on her mind."
    mike.say "Sure, Harmony..."
    mike.say "Fire away!"
    show harmony happy
    harmony.say "Well..."
    harmony.say "I was thinking..."
    show harmony normal
    harmony.say "We've been dating a while now."
    harmony.say "And my family is always asking me about you."
    harmony.say "So I figured that this would be a good time for them to meet you in person."
    harmony.say "Your family must be just the same - you know how they are!"
    harmony.say "So what do you think?"
    menu:
        "Agree to meet Harmony's family":
            "The moment that Harmony asks the question, it hits me like a slap in the face."
            "Why in the hell haven't I met her family yet?"
            "And why haven't I introduced her to mine either?"
            mike.say "Geez, Harmony..."
            mike.say "You're right - we should totally do that!"
            mike.say "I can't believe we've waited this long to meet each other's families!"
            show harmony happy
            "The smile that appears on Harmony's face is broad and genuine."
            "She nods in delight as I agree with her."
            harmony.say "Oh, [hero.name]..."
            harmony.say "I'm so glad you said that!"
            harmony.say "I was worried you'd say no."
            "I frown at this and shake my head."
            mike.say "Why would you think that, Harmony?"
            mike.say "We're getting on great, aren't we?"
            mike.say "So the next logical step is to meet each other's parents."
            mike.say "I don't know about you, but mine are kind of a big deal to me!"
            "Harmony chuckles and nods her head."
            show harmony normal
            harmony.say "Mine are too - obviously!"
            harmony.say "And I REALLY want them to like you, [hero.name]."
            harmony.say "It's important to me that all the people I love get along!"
            "I nod too, totally agreeing with Harmony."
            mike.say "So it's decided then?"
            mike.say "We talk to our parents and work something out."
            harmony.say "You got it."
            harmony.say "You talk to yours and I'll talk to mine."
            harmony.say "Then we meet up as soon as possible!"
            $ hero.cancel_activity()
            if 'religious' in harmony.traits:
                $ hero.calendar.add(game.calendar.get_next_day_of_week("saturday"), DateAppointment(15, "harmony", "Meet Harmony parents", label="harmony_event_02_religious", fail_label="missed_harmony_event_02_religious"))
            else:
                $ hero.calendar.add(game.calendar.get_next_day_of_week("saturday"), DateAppointment(15, "harmony", "Meet Harmony parents", label="harmony_event_04_vanilla", fail_label="missed_harmony_event_04_vanilla"))
        "Refuse to meet Harmony's family":
            "The moment Harmony asks the question, everything changes."
            "I feel a jolt of genuine fear travel up my spine."
            "And I swear that I break into a cold sweat too."
            mike.say "Y...you want me to meet your parents?"
            mike.say "Not like video-call them or something like that?"
            mike.say "Like be in the same room as them and everything?"
            show harmony annoyed
            "Harmony frowns at my evident discomfort."
            "I don't think this was the reaction that she wanted."
            harmony.say "Well...yeah, [hero.name]!"
            harmony.say "That was kind of the idea."
            harmony.say "I kind of thought you might like to get to know them!"
            mike.say "Ah..."
            mike.say "It's not that I DON'T want to meet them, Harmony."
            mike.say "It's more like I don't want to meet them YET, you know?"
            show harmony angry
            $ harmony.love -= 10
            harmony.say "Erm...no, [hero.name]."
            harmony.say "I don't think that I do!"
            "Harmony's frown is getting pretty intense."
            "She's also crossing her arms over her chest."
            "And neither of those are ever good signs."
            mike.say "Look, Harmony..."
            mike.say "I just don't think I'm there yet."
            mike.say "I'm not at that point where I'm ready to meet your folks."
            mike.say "I really want to like them and for them to like me."
            mike.say "And if I meet them before I'm ready..."
            mike.say "Well...I might screw it up!"
            show harmony annoyed
            "Harmony lets out a pouty snort at this."
            "But she seems to be ready to let the matter drop."
            "At least for now!"
            show harmony sad
            harmony.say "Okay, [hero.name]..."
            harmony.say "We'll forget about it for now."
            harmony.say "But my family are super important to me, you know?"
            show harmony annoyed
            harmony.say "If you want to be a part of my life, you have to accept them sooner or later!"
            $ hero.cancel_event()
    return

label missed_harmony_event_04_vanilla(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Harmony is going to be mad."
        $ harmony.love -= 10
    $ DONE.pop("harmony_event_03_vanilla", None)
    $ storytracker.refresh()
    return

label missed_harmony_event_02_religious(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Harmony is going to be mad."
        $ harmony.love -= 10
    $ DONE.pop("harmony_event_01_religious", None)
    $ storytracker.refresh()
    return

label harmony_event_04_vanilla(appointment=None):
    call harmony_event_02_religious (appointment) from _call_harmony_event_02_religious
    return

label harmony_event_02_religious(appointment=None):
    if harmony.love.max < 170:
        $ harmony.love.max = 170
    scene bg coffeeshop with fade
    "I have to admit that I'm feeling nervous as I walk into the coffee shop and take a look around."
    "Harmony's given me a pretty good description of her mom and shown me a couple of pictures too."
    "And she said that she'd done the same thing with her mom too, so she should also be looking out for me."
    "Pretty soon I spot a woman that looks like she fits the bill well enough."
    "She's half standing up at a table on the other side of the coffee shop right now."
    "And she looks to be checking me out at the same time I'm studying her too!"
    "Eventually she gives me a little wave and beckons me over to her table."
    "I take her up on the invitation, hurrying over and relieved to have spotted her so quickly."

    show harmony a wedding at center, flip, zoomAt(1.1, (640, 500)), blacker with dissolve
    "Harmony's mom" "Hello there..."
    "Harmony's mom" "You must be [hero.name]?"
    "Harmony's mom" "Am I right?"
    mike.say "That's me!"
    mike.say "And that would make you Diane?"
    "Diane nods and smiles as she starts to sit back down in her seat."
    "It's a nice smile too, one that instantly reminds me of Harmony."
    "In fact, Diane looks pretty much like a more mature version of her daughter."
    "I can't help hoping it's true what they say about mothers and daughters."
    "That you can tell how the latter will age by looking at the former."
    "Because Harmony's mom is pretty cute for an older woman!"
    menu:
        "Keep things respectful":
            "But I need to keep things above board here."
            "I have to make a good impression with Harmony's mom."
            "So letting on that she's hot would be a pretty dumb idea!"
            mike.say "It's great to meet you, Diane."
            mike.say "Harmony's told me so much about you."
            "Diane smiles, clearly happy to talk about her daughter."
            "Diane" "Ah, she's such a precious girl!"
            "Diane" "And she's told me all about you too."
            "Diane" "In fact, she never stops talking about you!"
            "I can already feel myself blushing a little at the compliment."
            "But Diane doesn't seem to be too concerned at this."
            "In fact, if anything, it seems to make her smile more genuine."
            mike.say "Sh...she does?"
            mike.say "I had no idea!"
            mike.say "I hope she says good things?"
            "Diane" "Wouldn't you like to know!"
            "For a moment I see a sparkle of mischief in Diane's eyes."
            "Then she seems to take great pleasure in letting me off the hook."
            "Diane" "I'm kidding around, [hero.name]!"
            "Diane" "Harmony seems very taken with you."
            "Diane" "And that's why I wanted to meet you for myself."
        "Flirt a little with Diane":
            mike.say "Wow..."
            mike.say "Now I know where Harmony gets her looks from!"
            "It takes a moment for Diane to realise that I'm complimenting her."
            "But the moment she does, her cheeks flush red."
            "And she looks totally thrown by my words."
            if hero.charm >= 60:
                "Diane" "Oh my..."
                "Diane" "Harmony never told me you were such a charmer!"
                "Diane" "I see that I'm going to have to keep an eye on you, [hero.name]!"
                mike.say "Well, I'll be keeping one eye on you too, Diane!"
                "Harmony's mom lets out a gasp and covers her mouth."
                "Then she bursts out laughing and playfully slaps my hand."
                "Diane" "Oh, stop it, [hero.name]!"
                "Diane" "I'm old enough to be your mother!"
                "Diane" "And we're supposed to be talking about you and Harmony!"
            else:
                "Diane" "Hmm..."
                "Diane" "Would you mind not doing that?"
                "Diane" "It's hardly appropriate, now is it?"
                "Just like that, Harmony's mom turns the tables on me."
                "Now I'm the one staring down at the table and feeling awkward."
                mike.say "I...I'm sorry..."
                mike.say "I shouldn't have said that."
                mike.say "I think the nerves are getting to me!"
                "Diane" "Hmm..."
                "Diane" "Well, we could have gotten off to a better start!"
                "Diane" "But let's put that behind us and move on, shall we?"
    "Diane takes a deep breath, trying to focus on the matter at hand."
    "Diane" "You see Harmony is my only daughter, [hero.name]."
    "Diane" "So her happiness is very important to me."
    "Diane" "I need to know that you understand that."
    "Diane" "And I need to know that you're going to make her happy."
    menu:
        "Play it straight down the line":
            "I don't even have to think before I respond to what Diane just said."
            "It's like the answer just comes straight out of my subconscious."
            mike.say "I know you're Harmony's mom, Diane."
            mike.say "And I respect that."
            mike.say "But don't take it the wrong way when I say I feel the same as you do."
            mike.say "I mean...not exactly, as I'm not her mom - obviously."
            mike.say "But Harmony means the world to me too."
            mike.say "And all I want is to be able to make her happy."
            "Diane listens patiently as I try to explain myself to her."
            "She listens carefully, nodding in all the right places."
            "And when I'm done, she seems to be satisfied."
        "Play it cool":
            "I lean back in my chair, letting out a little chuckle."
            "And I shake my head, a wry smile on my face as I do so."
            mike.say "Oh, don't worry, Diane..."
            mike.say "I know what it takes to make a woman happy!"
            if hero.charm >= 75:
                "Diane lets out a helpless burst of laughter."
                "She's blushing again, finding it hard to meet my eye."
                "Diane" "I already told you to stop that!"
                "Diane" "We're discussing Harmony - I have to remember that!"
                "Diane" "Oh, [hero.name]..."
                "Diane" "You're getting me into such a state!"
            else:
                "Diane raises an eyebrow at this statement."
                "And it isn't hard to tell that she's less than impressed."
                "Diane" "I really do wish that you'd take this more seriously, [hero.name]!"
                "Diane" "I'm not joking when I say that I care for my daughter."
                "Diane" "And I'll never approve of her being with someone that's so...flippant!"
                "I nod, feeling the confidence from before draining away."
                mike.say "Y...yes, Diane..."
                mike.say "I understand completely..."
    "I watch as Harmony's mom collects herself and then nods."
    "Diane" "Well..."
    "Diane" "I think that went as well as can be expected."
    "Diane" "We've met and started to learn a little about each other."
    "Diane" "Maybe we should leave it there and pick up another time?"
    "I nod as I stand up, eager to be leaving the coffee shop."
    "It's not that I didn't like meeting Harmony's mom."
    "Just that I feel like I need some time alone to process it all."
    "And I hope that I was able to make the right impression on her too."
    "Because if not, I'm sure that Harmony will let me know!"
    return

label harmony_event_05_vanilla:
label harmony_event_03_religious:
    show harmony
    "It's been a couple of days now since I met up with Harmony's mom at the coffee shop."
    "And in that time I've been waiting to hear back from her about how the meeting went."
    "Well, I know how I THINK it went, as I was actually there when it happened."
    "What I mean is that I want to know how Harmony and her mom think it went."
    "So when I finally get to meet up with her again, it's all that's on my mind."
    show harmony happy
    harmony.say "Hi, [hero.name]..."
    harmony.say "How are you today?"
    show harmony normal
    mike.say "Don't give me that, Harmony!"
    mike.say "I feel like you're trying to torture me!"
    show harmony sad
    harmony.say "What on earth are you talking about?"
    harmony.say "Are you feeling okay, [hero.name]?"
    "The look on Harmony's face tells me that I'm letting things get to me."
    "I'm so desperate to hear about what her mom thinks it's making me sound crazy!"
    "So I take a deep breath and shake my head, trying to get myself under control."
    mike.say "I'm sorry, Harmony."
    mike.say "It's just that I've been wanting to hear about what your mom told you."
    mike.say "It's kind of been playing on my mind!"
    show harmony normal
    "A look of realisation appears on Harmony's face."
    show harmony happy
    "She smiles and raises her eyebrows."
    show harmony mean
    "Now she's enjoying the sense of power I've handed to her."
    harmony.say "Oh, do you now?"
    harmony.say "Well, let's see..."
    harmony.say "She did say that you were 'an interesting young man'."
    harmony.say "And that you were very different from boyfriends I've had in the past."
    "I nod eagerly as Harmony relates these titbits of information."
    "But it doesn't take me long to realise that it's pretty meagre in nature."
    mike.say "Is...is that all?"
    mike.say "I don't know what to make of that, Harmony."
    mike.say "Is it good or bad?"
    show harmony normal
    "Harmony looks thoughtful for a moment."
    "She cocks her head on one side before she answers."
    harmony.say "Hmm..."
    harmony.say "With my mom it can be hard to tell."
    harmony.say "The best I can say is that it's not really bad."
    harmony.say "And that it's maybe not incredibly good."
    show fx drop
    harmony.say "Sorry - I know that's not very helpful!"
    "If anything, I'm now more clueless and confused than I was before!"
    hide fx
    mike.say "Talk me through that again, Harmony - please?"
    mike.say "It might make sense a second time!"
    "Harmony shakes her head at this."
    harmony.say "Uh-uh..."
    harmony.say "There's something else we need to talk about first."
    mike.say "There is?"
    show harmony sad
    "Harmony shakes her head in disbelief."
    harmony.say "Of course there is!"
    harmony.say "You just got to meet my mom."
    show harmony normal
    harmony.say "So when I do I get to meet yours?"
    menu:
        "Let Harmony meet Angela":
            "I slap a hand against my forehead."
            "How could I have forgotten?"
            mike.say "Of course, Harmony!"
            mike.say "I was supposed to be arranging that, wasn't I?"
            "Harmony shakes her head, smiling at my forgetfulness."
            show harmony happy
            harmony.say "Oh, [hero.name]!"
            harmony.say "Whatever am I going to do with you?"
            mike.say "Don't worry, Harmony."
            mike.say "I'm supposed to be calling my mom tonight."
            mike.say "I'll be sure to talk to her about it when I do."
            "Harmony nods, clearly happy with my promise."
            harmony.say "That's wonderful, [hero.name]."
            harmony.say "But be sure to make it soon, okay?"
            harmony.say "I just can't wait to meet her!"
            $ hero.cancel_activity()
            if 'religious' in harmony.traits:
                $ hero.calendar.add(game.calendar.get_next_day_of_week("saturday"), DateAppointment(21, "harmony", "Harmony meet Angela", label="harmony_event_04_religious", fail_label="missed_harmony_event_04_religious"))
            else:
                $ hero.calendar.add(game.calendar.get_next_day_of_week("saturday"), DateAppointment(21, "harmony", "Harmony meet Angela", label="harmony_event_06_vanilla", fail_label="missed_harmony_event_06_vanilla"))
        "Don't let Harmony meet Angela":
            "The question opens up a bottomless pit of dread right beneath my feet."
            "It was bad enough me agreeing to meet up with Harmony's mom."
            "But the mere thought of her sitting down to talk with mine..."
            "Well, it's almost too much for my brain to handle!"
            mike.say "I...I don't think that's such a good idea, Harmony!"
            mike.say "Besides, I can tell you all about my mom myself."
            mike.say "What is it that you want to know?"
            show harmony angry
            "Harmony crosses her arms over her chest and fixes me with a serious stare."
            "All of which means that she's less than impressed with my efforts at diversion."
            harmony.say "Why are you being like that, [hero.name]?"
            harmony.say "I thought we already agreed this was a good idea?"
            show harmony annoyed
            mike.say "I know, I know..."
            mike.say "Let's just say I've had more time to think it over."
            mike.say "And now I've changed my mind!"
            $ harmony.love -= 20
            "Harmony snorts in shakes her head."
            show harmony angry
            harmony.say "You know what, [hero.name]..."
            harmony.say "That's pretty low of you!"
            show harmony annoyed
            harmony.say "We're in a serious relationship here."
            harmony.say "We're supposed to open, to trust each other!"
            "Before I can answer that, Harmony turns and walks away."
            "I think about following her, but then decide to leave it."
            "Perhaps what she really needs is a chance to cool off."
    return

label missed_harmony_event_06_vanilla(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Harmony is going to be mad."
        $ harmony.love -= 10
    $ DONE.pop("harmony_event_05_vanilla", None)
    $ storytracker.refresh()
    return

label missed_harmony_event_04_religious(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Harmony is going to be mad."
        $ harmony.love -= 10
    $ DONE.pop("harmony_event_03_religious", None)
    $ storytracker.refresh()
    return

label harmony_event_06_vanilla(appointment=None):
    call harmony_event_04_religious (appointment) from _call_harmony_event_04_religious
    return
label harmony_event_04_religious(appointment=None):
    if harmony.love.max < 180:
        $ harmony.love.max = 180
    scene bg livingroom with fade
    "I can't remember the last time I felt this nervous, like my heart is pounding in my chest."
    "And all because my mom is coming over to sit down and have a coffee with the girl I'm dating."
    "It's not like this hasn't happened before - she's met plenty of the girls I dated in the past."
    scene bg kitchen
    show harmony sexycasual
    with dissolve
    "So why am I getting into such a state about her meeting Harmony?"
    "I mean, she's no different to any other girl, is she?"
    "Maybe that's it - maybe Harmony IS different."
    "Maybe my feelings for her are stronger than they were for all the other girls."
    "And I'm worried that my mom will say or do something to sabotage my relationship with her!"
    harmony.say "Hello?"
    show fx question
    harmony.say "[hero.name]?"
    hide fx
    harmony.say "I think I heard a knock at the door!"
    "Suddenly I feel myself snapping back to reality."
    "I see that Harmony is looking me in the eye."
    "She has a sweet smile on her face, but I can see that she's nervous too."
    "I need to get my feelings under control and make sure things go according to plan!"
    mike.say "Ah..."
    mike.say "No worries, Harmony."
    mike.say "It'll probably be my mom."
    mike.say "I'll go let her in, okay?"
    "Harmony nods, sitting down at the kitchen table."
    scene bg livingroom with dissolve
    "Meanwhile I dash to the front door and hastily swing it open."
    scene bg house
    show angela date
    with wiperight
    angela.say "Hi, [hero.name]..."
    angela.say "I hope I'm not too early?"
    "If my mom's at all nervous herself, she's not letting it show."
    "She's practically beaming, straining to see over my shoulder."
    angela.say "So?"
    angela.say "Where is she?"
    angela.say "Where's the girl you're so keen for me to meet?"
    scene bg livingroom
    show angela date
    with hpunch
    "My mom steps into the hallway before I can ask her in."
    "In fact I almost have to leap aside to keep her from barging into me!"
    mike.say "Whoa!"
    mike.say "Slow down, Mom!"
    mike.say "Harmony's just through here, in the kitchen."
    hide angela
    "I hurry to get there ahead of my mom, and only just manage it."
    "It's like she's trying to get in there before Harmony knows she's here."
    "What does she think surprising Harmony's going to achieve anyway?"
    "It's not like she has a habit of torturing puppies when she thinks nobody's looking!"
    scene bg kitchen
    show angela date at left5
    show harmony sexycasual at right5
    with fade
    mike.say "Harmony...this is my Mom."
    mike.say "Mom, this is Harmony."
    "Harmony doesn't miss a beat."
    "The moment we enter the room, she's on her feet."
    "And she hurries over to where my mom's standing."
    show harmony happy at center with move
    harmony.say "Hello!"
    harmony.say "It's so nice to finally meet you!"
    show angela happy
    angela.say "The feeling's mutual, my dear!"
    "They proceed to do that weird thing where they pretend to kiss each other on the cheeks."
    "But in reality they never come within range of touching each other the whole time."
    show harmony normal at right5 with move
    show angela normal
    "And then Harmony returns to her seat and my mom claims one for herself."
    "It's a moment later that I realise they're both staring at me."
    harmony.say "[hero.name].."
    harmony.say "Aren't you going to make your mother a coffee?"
    show angela disappointed
    angela.say "Oh, don't mind him, dear."
    angela.say "He's always off with the fairies like that!"
    mike.say "Oh..."
    mike.say "Oh yeah..."
    mike.say "Coffee...right..."
    "I leap into action making the coffee."
    show angela happy
    show harmony happy
    "While behind me, Harmony and my mom share a conspiratorial chuckle."
    angela.say "He's such a typical man, dear!"
    show angela sadistic
    angela.say "But I think he's trainable."
    show harmony normal
    harmony.say "Oh, please - call me Harmony."
    show angela normal
    angela.say "Of course, Harmony."
    angela.say "And you must call me Angela too!"
    angela.say "No calling me [hero.name]'s mom!"
    "I can already sense that the conversation is beginning to gain pace."
    "And I don't want to be left standing on the side-lines when it gets serious."
    "So I load up the coffees on a tray and hurry to take a seat at the table."
    show angela eww
    show harmony normal
    angela.say "Now what's this I hear about you two meeting at church?"
    angela.say "I was intrigued by that, Harmony."
    show angela sadistic
    angela.say "Because [hero.name] was never one to attend services on a Sunday when he was at home!"
    if "religious" in harmony.traits:
        "At the mere mention of religion, Harmony's face lights up."
        "She takes hold of my hand and gives it an affectionate squeeze."
        harmony.say "I can't believe that was ever the case, Angela!"
        harmony.say "Because [hero.name]'s always there, every Sunday!"
        harmony.say "As soon as I walk into the church, he's right at my side!"
        show angela flirt
        "My mom nods at this, but I see a smile tugging at the corner of her mouth."
        angela.say "Hmm..."
        angela.say "Maybe it's the congregation at your church, Harmony?"
        angela.say "Maybe there's something about the company he's getting to keep there?"
        show angela sadistic
        angela.say "Or perhaps it's just one of them..."
        mike.say "Ahem..."
        mike.say "I...I don't know exactly what it is, Mom!"
        mike.say "But as they say - god moves in mysterious ways!"
    else:
        show harmony happy
        "At the mention of religion, Harmony smiles."
        "But she also shakes her head."
        harmony.say "You're not exactly up to date with your information there, Angela!"
        harmony.say "I used to be a regular at church, and that is where we first met."
        harmony.say "But being with [hero.name]'s made me rethink all of that."
        show angela normal
        "Now my mom seems more intrigued than ever."
        "She leans forwards, nodding for Harmony to go on."
        angela.say "What do you mean, Harmony?"
        show angela annoyed
        angela.say "Did [hero.name] lead you away from god?"
        angela.say "Did he lead you...into temptation?"
        mike.say "MOM!"
        mike.say "You're making me sound like the devil himself!"
        show harmony happy
        show angela normal
        "Harmony just laughs and shakes her head."
        "The sound is so pure and casual."
        "It cuts through everything else and defuses the tension in an instant."
        harmony.say "Oh god, no!"
        harmony.say "[hero.name] might like to think he's devilish!"
        show harmony normal
        harmony.say "But it was really more like he showed me that I was missing out."
        harmony.say "I was letting my faith control my life, rather than guide me when I needed it."
    show angela happy
    show harmony happy
    "My mom nods, seemingly happy with the answers that she's getting."
    "Harmony's smiling too, but I can sense that she's feeling a little tense."
    "She doesn't normally smile so much and for so long."
    "Her face must be starting to ache by now!"
    "We keep on chatting about this and that."
    "For the most part, mom asks questions and we answer them."
    "It's pretty innocent stuff, peppered with jokes and funny stories."
    "And part of me's starting to feel like I was worried about nothing."
    "This is all going well, with mom and Harmony getting on fine."
    "But then she pulls a fast one on me."
    "Mom's been lulling me into a false sense of security!"
    show angela normal
    show harmony normal
    angela.say "[hero.name]'s a big boy now, Harmony."
    angela.say "And he's not got me to keep an eye on him."
    angela.say "I hope he's been taking precautions when you stay over here?"
    show angela flirt
    angela.say "And I don't mean locking the doors and windows at night either!"
    mike.say "MOM!"
    mike.say "What are you doing?!?"
    mike.say "You can't ask about stuff like that!"
    if "religious" in harmony.traits:
        "For a moment I think that we're well and truly screwed."
        show harmony sad
        "A look of horror appears on Harmony's face."
        show harmony normal
        "But then I see her collect herself."
        "And it's replaced by one of serene, almost saintly calm."
        harmony.say "You must be mistaken, Angela."
        harmony.say "[hero.name] and I are not married."
        harmony.say "So that would be a sin in the eyes of god."
        show angela annoyed
        "Mom's eyes narrow at this."
        "And she frowns at Harmony."
        angela.say "Is that so?"
        show angela normal
        angela.say "Well...no need to worry on that score then."
        "She seems to be willing to let the matter drop."
        "But I know my mom pretty well."
        "And I have a feeling that she just judged Harmony on what she said."
    else:
        harmony.say "Oh, [hero.name]!"
        harmony.say "Don't be so old-fashioned!"
        harmony.say "Angela's just looking out for us, that's all."
        "Harmony waves away my concerns like they're nothing."
        "I splutter and gasp a little more."
        "But she cuts me off again."
        harmony.say "I'm not going to go into any details, obviously!"
        show angela normal
        harmony.say "But I can assure you, Angela - we're very careful."
        harmony.say "You won't be getting any grandkids until we're good and ready!"
        "I look this way and that, confused and disoriented."
        "First my mom's talking about my sex-life with Harmony."
        "And now Harmony's talking about kids with my mom!"
        "I can't keep up!"
        "But what I do notice is the look on my mom's face."
        "She looks like she's impressed by what Harmony's saying."
        "Or maybe it's on account of her being so upfront about everything."
        "Either way it's a good omen!"
    "Soon enough we're finishing up the coffee."
    "And the conversation seems to be winding down too."
    show angela disappointed
    "My mom glances at her watch and shakes her head."
    angela.say "Sorry, but I'm going to have to dash."
    show angela happy
    angela.say "But this was nice - we'll have to do it again soon."
    show harmony happy
    harmony.say "I hope so, Angela."
    harmony.say "It was so nice to meet you."
    "We all get up and make for the front door."
    show bg house
    show harmony normal
    hide angela
    with fade
    "Harmony and I see my mom out and then wave until she's out of sight."
    "Then we shut the door and both let out a genuine sigh of relief."
    show bg livingroom
    show harmony at center
    with fade
    harmony.say "I think I need some more coffee, [hero.name]!"
    harmony.say "That was exhausting."
    mike.say "Really?"
    mike.say "I thought you breezed through it!"
    harmony.say "Making it look so easy was half of the struggle!"
    if not "religious" in harmony.traits:
        show harmony blush
        harmony.say "Now let's see about that second round of coffee you mentioned..."
        call harmony_fuck_date_male from _call_harmony_fuck_date
    return

label harmony_event_07_vanilla:
    if harmony.love.max < 200:
        $ harmony.love.max = 200
    show harmony
    "Today's one of those days when it'd be a crime to stay inside."
    "The sun is out and the sky's almost totally clear, a beautiful shade of blue."
    "And that's why Harmony and I have come to the park for our date."
    "What better way to take advantage of all this than a stroll?"
    "Well, that's be a stroll surrounded by nature of course!"
    "It's all very pretty and pleasant, I have to admit."
    "But none of it is as beautiful as Harmony."
    "Yeah, I know I sound like a babbling, romantic idiot right now."
    "But to me she looks like one of those princesses in the animated movies."
    "Like any moment she's going to burst into song and start dancing."
    "And all the animals are going to emerge from the undergrowth."
    "The birds will descend from the trees too and they'll all follow her around!"
    "Okay...okay...I know I'm getting carried away."
    "Let's just say that Harmony looks gorgeous and I'm happy to be seen with her."
    harmony.say "[hero.name]..."
    show fx question
    harmony.say "What's that look on your face, huh?"
    harmony.say "What's going on in that head of yours?"
    hide fx
    mike.say "Huh..."
    mike.say "What..."
    "I stumble over my words only partly because Harmony catches me off-guard."
    "At least part of it is seeing her smiling at me after I've been gushing over her."
    mike.say "Oh...I..."
    mike.say "I'm just having such a great time today, Harmony."
    mike.say "And I was thinking that I'm a pretty lucky guy!"
    hide harmony
    show harmony normal
    harmony.say "Oh, really?"
    harmony.say "And why's that?"
    "Ah shit...I guess I asked for that!"
    "There's no choice but to be honest with her now..."
    mike.say "Well..."
    mike.say "Because I'm here with you, Harmony!"
    show harmony happy
    "As soon as I confess the source of my happiness, Harmony blushes."
    "And I mean she really blushes, her cheeks flushing bright red."
    harmony.say "Oh, [hero.name]..."
    harmony.say "I'm so glad you said that!"
    show harmony close normal
    "Harmony stops and steps directly in front of me."
    "At the same time she clasps both my hands in her own."
    harmony.say "Because there's something I have to tell you too."
    harmony.say "Something that's very important..."
    "Oh no...here we go!"
    "She's going to burst into song, just like I imagined a moment ago!"
    harmony.say "I never thought I'd be saying anything like this to a guy."
    harmony.say "I used to go along to church every Sunday..."
    harmony.say "Well, let's be honest, any chance that I got!"
    harmony.say "And I'd sit there, thinking that I had it all figured out."
    harmony.say "But then you came along..."
    "Harmony takes a deep breath."
    "Then she lets it out as a long sigh."
    harmony.say "And suddenly I was feeling all kinds of emotions."
    harmony.say "Ones that didn't seem to be mentioned in my bible."
    harmony.say "And trust me, I looked in there!"
    harmony.say "I searched it from cover to cover!"
    harmony.say "But nothing explained how you made me feel, [hero.name]."
    "I can't help letting out a nervous laugh."
    "What Harmony's confessing sounds seriously intense!"
    mike.say "Oh, come on, Harmony!"
    mike.say "You make it sound like I caused you to lose your faith!"
    harmony.say "In a way, that's exactly what I mean, [hero.name]!"
    harmony.say "But maybe that does sound a little too dramatic..."
    harmony.say "Let's say you made me start to question for the first time."
    harmony.say "Like I was having so much fun with you, feeling so happy."
    show harmony sad
    harmony.say "And I knew that people would start to disapprove, to say it wasn't what god wanted."
    harmony.say "But how could that be, [hero.name]?"
    harmony.say "How could a loving god not want two people to be happy together?"
    mike.say "I have no idea, Harmony."
    mike.say "I'm no philosopher!"
    show harmony normal
    harmony.say "Well neither am I."
    harmony.say "But I'm still sure that, if he exists, god wants us to be happy!"
    "That last statement makes my eyes pop open."
    "The very fact that Harmony used the word 'if' in relation to god's existence!"
    "There's no way she has even questioned it when I first met her."
    mike.say "I think so too, Harmony."
    mike.say "So...that means I make you happy?"
    "Harmony looks away for a moment."
    show harmony happy
    "And she blushes again."
    harmony.say "Ah...yeah, [hero.name]!"
    harmony.say "In fact, you make me completely happy."
    harmony.say "So much that I want to spend the rest of my life with you!"
    show harmony normal
    harmony.say "Well...that is...if you'll let me?"
    "I don't hesitate to nod at this."
    "In fact it's the easiest question I've ever answered."
    mike.say "Of course I will, Harmony - one hundred percent!"
    hide harmony
    show harmony kiss
    with fade
    $ harmony.flags.kiss += 1
    $ harmony.love += 5
    $ game.active_date.score += 20
    "Harmony lets go of my hands, just to thrown her arms around my neck."
    "And when she kisses me, I can feel the weight of all the emotions she just confessed."
    "That sensation assures me that she was telling the truth more than words ever could."
    return

label harmony_event_05_religious:
    show harmony sad
    "I feel like I'm getting pretty good at reading Harmony, like I know her moods and quirks."
    "So when she seems to be preoccupied, I see it as the perfect chance to put this to the test."
    "And if I can head off a problem before it can become a crisis, even better!"
    mike.say "Harmony..."
    mike.say "Is everything okay with you?"
    "Harmony looks around, surprise written on her face."
    harmony.say "Oh..."
    harmony.say "That's weird, [hero.name]..."
    show harmony normal
    harmony.say "I was just about to talk to you about that!"
    "I can't help smiling at being proven right."
    show fx question
    "But then I see the expression on Harmony's face turn into one of confusion."
    "Oh yeah - she just told me that she needs to talk to me about something."
    hide fx
    "And it's probably something that's pretty serious too!"
    "So I do the best I can to look serious and interested."
    mike.say "Erm...yeah..."
    mike.say "Of course, Harmony."
    mike.say "What's on your mind?"
    show harmony sad
    harmony.say "Well..."
    harmony.say "It's about your living arrangements."
    "I can't help frowning at this."
    "What could possibly be wrong with that area of my life?"
    mike.say "Erm..."
    mike.say "What do you mean, Harmony?"
    mike.say "Don't most people rent at our age?"
    mike.say "Do you think that I should be saving towards the deposit on my own place?"
    show harmony annoyed
    "Harmony shakes her head and frowns a little."
    "All of which lets me know I'm missing her point."
    harmony.say "No, no, no, [hero.name]!"
    harmony.say "I don't mean WHERE you live."
    harmony.say "I mean WHO you live with!"
    "Now I am confused."
    "Is Harmony saying she has a problem with [bree.name] and Sasha?"
    mike.say "Look, Harmony..."
    mike.say "I know that [bree.name]'s a little ditzy at times."
    mike.say "And she REALLY needs to learn to pick up after herself!"
    mike.say "Sasha too - she can be a real pig if you let her!"
    mike.say "But they're a great pair of girls when you really get to know them."
    harmony.say "That's the problem, [hero.name]."
    harmony.say "They're a pair of girls!"
    "For a moment I honestly don't understand what Harmony's getting at."
    "I can't think of a reason that [bree.name] and Sasha being female would be a problem."
    "And then I remember where I first met Harmony."
    "That and where she gets her morality from too!"
    mike.say "Harmony..."
    mike.say "You can't mean..."
    harmony.say "Yes I do, [hero.name]!"
    harmony.say "It's not right for you to be living with two single women!"
    harmony.say "I don't like you being exposed to such...such temptation!"
    "I can't help laughing at Harmony's words."
    "Which is a mistake, because she instantly stiffens."
    harmony.say "This isn't funny!"
    harmony.say "I know what women are like, [hero.name]!"
    harmony.say "They'll pretend to be your friends."
    harmony.say "But underneath it all, they're vile temptresses!"
    mike.say "Harmony, please!"
    mike.say "This is the twenty-first century for goodness sake."
    mike.say "Men and women can just be friends, nothing more than that!"
    show harmony angry
    "Harmony shakes her head and actually stamps her foot at this."
    "Which makes me take a step back in genuine surprise."
    harmony.say "Don't be so naive, [hero.name]!"
    show harmony annoyed
    harmony.say "I can see them now."
    harmony.say "I can see them walking around in their little panties."
    harmony.say "Bending over in front of you so that you get a good look!"
    "Actually, I'm beginning to be able to see what Harmony sees too."
    "And it's kind of making me want to go home and turn up the thermostat!"
    "But I shake off such shameful thoughts."
    "Instead I concentrate on the matter at hand."
    mike.say "Don't be ridiculous, Harmony."
    mike.say "I don't look at [bree.name] and Sasha any differently to the guys I know!"
    mike.say "When I'm around them, sex is the last thing on my mind, okay?"
    "Harmony lets out a snort of derision."
    harmony.say "Well then, you're going to have to find a way to prove it, aren't you?"
    harmony.say "Otherwise you're a sinful, dirty little man - and I won't be seen with you!"
    "Harmony turns her back on me and strides away."
    "Leaving me to mull over her words and try to come up with a solution."
    $ harmony.flags.storyDelay = TemporaryFlag(True, 3)
    return

label harmony_event_06_religious:
    if harmony.love.max < 190:
        $ harmony.love.max = 190
    play sound cell_vibrate loop
    "I feel the sensation of my phone vibrating in my pocket, distracting me from what I'm doing."
    "So I pull it out, feeling more than a little annoyed at whoever's calling me up out of the blue."
    "But when I see that the call is from Harmony, my mood changes for the better."
    stop sound
    "I take the call straight away, eager to hear what she has to say to me."
    mike.say "Hi, Harmony..."
    mike.say "Great to hear from you!"
    "I hear a sigh on the other end of the line, even before she speaks."
    "And my heart sinks with the sound, dreading what I'm about to hear."
    harmony.say "Hello, [hero.name]..."
    harmony.say "I'm calling because we need to talk."
    "Oh no - that's never a good thing to hear!"
    mike.say "S...sure we can talk, Harmony!"
    mike.say "We can talk about anything you like!"
    harmony.say "Good, [hero.name], good..."
    harmony.say "Come meet me and..."
    harmony.say "Well, I guess we'll talk..."
    "After we agree where to meet, Harmony ends the call."
    "She leaves me with nothing but questions running around in my head."
    "So by the time we actually meet up, I've thought up every terrible scenario possible."
    "But even so, I'm not prepared for what Harmony is actually going to say to me."
    scene bg park
    show harmony sad casual
    with fade
    $ game.room = "park"
    "When I first lay eyes on Harmony, she looks pretty grim-faced."
    "She might have been crying before I arrived, as her eyes are a little red."
    "But now she looks like she's prepared herself for what lies ahead."
    "All of which means that, whatever that is, it can't be good."
    mike.say "Harmony..."
    mike.say "I came as fast as I could."
    mike.say "What is it?"
    mike.say "What have you got to tell me?"
    "Harmony takes a deep breath and closes her eyes."
    "She holds it in for a moment, then lets it out again."
    "Then she opens her eyes and starts to talk."
    harmony.say "I...I have to tell you something, [hero.name]."
    harmony.say "But it's going to be hard."
    harmony.say "And you're not going to like it."
    "I do the best I can to put on a brave face."
    "To be truthful, Harmony's scaring me more than a little."
    "But I need to hear her out, so I bite down on my fear."
    mike.say "Go ahead, Harmony."
    mike.say "Say what you have to say."
    mike.say "I can take it, whatever it is."
    show harmony normal
    "Harmony nods."
    harmony.say "I've been doing a lot of thinking recently."
    harmony.say "Deep and serious thinking about where my life is going."
    harmony.say "And I think I've come to a decision."
    "I know that I should be listening to what Harmony has to say."
    "But being scared is also making me selfish."
    "And so I blurt out a question to satisfy my own needs."
    mike.say "You're breaking up with me, aren't you?"
    mike.say "I'm not moral enough, not good enough."
    mike.say "Is that it?"
    harmony.say "Oh no, [hero.name], not at all."
    show harmony sad
    harmony.say "I have to end our relationship, and I'm sorry for that."
    harmony.say "But it's not you that's lacking moral fibre - it's me!"
    "I can't believe what I'm hearing."
    "Sure, I'm devastated that Harmony's calling it quits with me."
    "But how can she say that she's lacking moral fibre?"
    mike.say "But, Harmony..."
    mike.say "You practically live in the church!"
    show harmony normal
    "Harmony smiles and shakes her head."
    harmony.say "Maybe I used to, [hero.name]."
    show harmony sad
    harmony.say "But since you came on the scene I've been slipping."
    harmony.say "You're too much of a distraction for me, too much of a temptation."
    harmony.say "I need to rededicate myself to god."
    show harmony normal
    harmony.say "That's why I've decided to become a nun!"
    "I still can't believe what I'm hearing."
    mike.say "A NUN!"
    mike.say "Harmony, that's crazy!"
    mike.say "I mean, do a penance or something."
    mike.say "Or maybe go on a pilgrimage - a really long one!"
    mike.say "But don't go off and become a nun - I'll never see you again!"
    harmony.say "Oh, you will, [hero.name]."
    harmony.say "But when you do, I'll be married to god!"
    hide harmony with dissolve
    "With that, Harmony turns and walks away."
    "I'm left alone and lost for words."
    "I find a girl."
    "I fall in love with her."
    "Then she ends up leaving me for god!"
    "What does a guy have to do to get a break around here?!?"
    $ harmony.flags.nosex = True
    $ harmony.flags.nodate = True
    $ harmony.flags.nokiss = True
    $ harmony.friendzone()
    $ harmony.flags.breakupDelay = True
    return

label harmony_event_07_religious:
    "It's been a while since Harmony called me up and told me that she'd made the decision to become a nun."
    "And while I've spent a lot of that time trying to come to terms with it, I haven't managed to do so yet."
    "The whole idea is just so strange and old-fashioned, you know?"
    "It feels like the plot of an old book or something you'd read about happening in the past."
    "Not the way a relationship would come to an end in the twenty-first century!"
    "Part of me is hoping that Harmony will at least call me, just to let me know how she is."
    "But I don't know the first thing about training to be a nun."
    "Do you go off to a nun school in the middle of nowhere?"
    "Or can you do it in your spare time, like an online course or something?"
    "Do they even let you make phone calls to the non-nun world?"
    scene bg church with fade
    "I find myself taking long walks in an effort to clear my head."
    "And that's how I end up walking around outside the church where Harmony and I first met."
    "Maybe I walked her on an unconscious impulse, hoping to catch sight of her."
    "Or maybe it's just one of those cruel ironies that seems to happen purely at random."
    "An irony which the cosmos then doubles down on by what I see passing the front of the church."
    "It's nuns - an entire column of nuns!"
    "Fate's really rubbing salt into the wound today."
    "I find myself staring at the backs of the nuns as they file past."
    "And then my eyes settle on one nun in particular."
    "Well...on her backside, if I'm going to be honest!"
    "And what the heck, I'm already miserable as sin."
    "Who cares if I end up going to hell for perving over a nun's arse?!?"
    "But wait a minute...that arse is starting to look very familiar!"
    mike.say "Harmony?"
    mike.say "Is that you?!?"
    "I see the nun in question jump at the sound of my voice."
    show harmony nun at right5 with dissolve
    "She steps out of the column and slowly turns around to face me."
    show harmony nun at center with ease
    show fx question
    with dissolve
    harmony.say "[hero.name]?"
    harmony.say "Wh...what are you doing here?"
    hide fx
    "For a moment I can't make myself answer the question."
    "I was dreading seeing Harmony in a nun's habit."
    "I'd convinced myself that she'd look stern and sexless."
    "But the exact opposite is true - she looks exquisitely beautiful."
    "The simplicity of the habit brings out the qualities of her face."
    "And I can almost see a radiant halo of light illuminating it."
    mike.say "You look so beautiful, Harmony!"
    mike.say "I...I'm sorry..."
    mike.say "I know I'm not supposed to say things like that to you anymore."
    show harmony nun at center, vshake
    "Harmony looks shocked at my admission."
    "Her cheeks flush red and she covers her mouth."
    "All of which only serves to make her look even more beautiful."
    mike.say "I was just out walking, trying to clear my mind."
    mike.say "I guess I must have wandered here by chance, that's all."
    "Harmony nods."
    harmony.say "I see..."
    show harmony sad
    harmony.say "I...I was worried that you might have..."
    harmony.say "Well, that you might have come to try and talk me out of all this!"
    "Harmony gestures to her habit and puts on a weak smile."
    "I can tell that she's trying very hard to sound like she disapproves."
    "But there's a small part of her that seems to be pulling against all of that."
    "A part of that which maybe wishes that I had tried to change her mind."
    mike.say "I won't lie, Harmony."
    mike.say "I do wish we were still together."
    mike.say "But I don't get to tell you what to do."
    mike.say "For a relationship to work, we both have to want the same thing."
    "At this, Harmony hurries over and grabs hold of my hands."
    show harmony normal
    harmony.say "This isn't forever, [hero.name]!"
    harmony.say "It's just what I feel I have to do right now!"
    harmony.say "I could still come find you when things change for me?"
    harmony.say "I just need you to give me something to make sure I remember you!"
    menu:
        "Fuck Harmony one last time":
            if harmony.love.max < 200:
                $ harmony.love.max = 200
            show fx exclamation
            "Without saying another word, I reach out and take hold of Harmony's hand."
            "Then I turn and begin to lead her out of sight around the side of the church."
            hide fx
            "She resists a little at first, glancing back over her shoulder at the other nuns."
            "But she doesn't stop me guiding her away until we're totally hidden from view."
            "Once we're alone, I put my hands on the sides of Harmony's head."
            show harmony kiss with fade
            $ harmony.flags.kiss += 1
            "And I kiss her with unrestrained passion."
            "She wriggles and squirms for a moment."
            "But all too soon Harmony's natural, long suppressed urges win out."
            "She melts into the kiss, her tongue pushing into my mouth."
            "And she presses her body into mine, almost with desperation."
            "Her breathing is starting to sound more like panting right now."
            "And she gasps out pleas between kisses."
            hide harmony
            show harmony close nun
            with fade
            harmony.say "Oh..."
            harmony.say "Oh, [hero.name]..."
            harmony.say "We shouldn't be doing this!"
            harmony.say "It's so wicked of you to tempt me!"
            mike.say "You're going to be a nun, Harmony."
            mike.say "So you need something to atone for, right?"
            hide harmony
            show harmony kiss nun
            with fade
            $ harmony.flags.kiss += 1
            "Harmony gasps even more as I spin her around and wrap my arms around her."
            "I squeeze and caress her body through her habit, making her moan with pleasure."
            "And then I hastily hitch up her skirts, exposing her large, round ass."
            "I use one hand to open my flies and the other to yank down Harmony's panties."
            show harmony missionary church mike nun with dissolve
            harmony.say "Mmm..."
            harmony.say "Oh, you shouldn't..."
            harmony.say "I should make you stop..."
            harmony.say "But...I've missed this SO much!"
            "I grab Harmony by the haunches, loving how her full figure feels."
            "And I don't even hesitate to answer her worries and fears."
            "Because I know what we both want without saying a word."
            "One firm thrust sends the head of my cock sliding over Harmony's lips."
            show harmony missionary orgasm
            "She whimpers at the sensation, then a moment later her gasps and moans."
            show harmony missionary vaginal
            "And that's because her pussy yields to my efforts and I inch inside her."
            show harmony missionary normal
            "Harmony looks back over her shoulder at me, nodding eagerly."
            "I don't know how much time we have, or if we might be discovered."
            show harmony missionary orgasm speed
            "So I waste no time on beginning to thrust in and out of her."
            "Harmony keeps on nodding, every sensation she feels written on her face."
            "For my part, I go at it like a man living his last day on earth."
            "I want this to be something that I'll remember for a long time to come."
            "And I also want to leave Harmony aching for me too!"
            show harmony missionary ahegao
            "But from the look on her face, that's already happening."
            "Harmony's eyes are rolling back into her head right now!"
            "Her entire body is rocking back and forth as I pound her."
            "And the sound of my thighs slapping into hers is pretty loud!"
            show harmony missionary orgasm
            harmony.say "Oh yes..."
            harmony.say "Oh god...yes..."
            harmony.say "Jesus Christ...I'm going to cum!"
            harmony.say "I love you...I love you so much!"
            "Fucking hell - I'm doing it with a blaspheming nun!"
            "The thought of that and the feeling of being inside Harmony is too much."
            show harmony missionary ahegao creampie with hpunch
            $ harmony.love += 2
            $ harmony.sexperience += 1
            "The moment that she starts to cum, I feel myself dragged along with her."
            with hpunch
            "Harmony wriggles and writhes on my cock, squealing as I fill her up."
            show harmony missionary orgasm with hpunch
            "Then she slowly slides herself off me, leaning against my chest for support."
            hide harmony
            show harmony nun
            with fade
            "Harmony pulls up her panties and makes herself look presentable."
            show harmony happy
            "She gives me one last smile."
            hide harmony with dissolve
            "And then she runs after the other nuns."
            "Though I note that she's not able to walk as straight as she did before."
            "Maybe it's better that she leaves without saying another word."
            "That way the last memory we both have is the intimate moment we just shared."
            "Because it was pretty much perfect."
            "And it left me wanting more."
            "But it's only when she's gone that I remember what Harmony said before she came."
            "Did she mean that, or was it just something she said in the heat of the moment?"
            "Damn it - I was supposed to be the one leaving her with a hook in her brain!"
            "Now I'm standing here, wondering if she was telling the truth or not."
        "Kiss Harmony one last time":
            show harmony kiss with fade
            $ harmony.flags.kiss += 1
            "Without saying another word, I lean forwards and kiss Harmony."
            "She freezes for a moment, her body stiffening with surprise."
            "But then I feel the tension slip away and she melts into the kiss."
            "Even so it's still a tender and gentle affair."
            "Our tongues touch, sending a thrill through my body."
            "But neither of us is probing the other's tonsils!"
            "The kiss lasts for a long, lingering moment."
            hide harmony
            show harmony close nun
            with fade
            "Then Harmony lets out a sigh and pulls away."
            "She gives me one last smile."
            hide harmony with dissolve
            "And then she runs after the other nuns."
            "Maybe it's better that she leaves without saying another word."
            "That way the last memory we both have is the kiss we just shared."
            "Because it was pretty much perfect."
            "And it left me wanting more."
    return

label harmony_event_03_slutty:
    if harmony.love.max < 170:
        $ harmony.love.max = 170
    show harmony
    "When I first met Harmony, I was sure that she couldn't have been more straight-laced and righteous."
    "Sure, I wanted to get as close to her as I could, but I thought that would mean being in the friend-zone."
    "And even if we did ever get further than that, I thought she'd want me to prove myself as pious and pure as her."
    "But then I discovered that there was a chink in the armour of her faith, a kernel of repressed desire in her soul."
    "And like the devil whispering in the ear of a saint, I somehow managed to lure her into temptation with me!"
    "Since then, Harmony's never looked back, and now she's even starting to amaze me with what she's capable of."
    "It's like I've unleashed an insatiable succubus from the deepest regions of hell!"
    "Tonight is no exception."
    "After I suggested that we go to a night-club, Harmony jumped at the chance."
    "And when I saw the outfit she'd chosen to wear, I knew I was in for a good time."
    "Before she was almost ashamed of her full, buxom figure and tried to hide it."
    "But now she's wearing something so tight that every curve is accentuated to the maximum."
    "And Harmony seems to be revelling in the attention that her body is attracting."
    "She strides into the night-club on my arm, looking like she owns the place!"
    "Guys and girls alike are looking at her with wanton gazes."
    "Desire and jealousy equally mixed in their eyes as they stare."
    mike.say "Wow, Harmony..."
    mike.say "You're getting some serious attention tonight!"
    mike.say "Just remember you're here with me, please?"
    show harmony happy
    "Harmony regards me with a satisfied smile."
    harmony.say "Don't worry about it, [hero.name]."
    show harmony blush
    harmony.say "I LOVE being the centre of attention."
    harmony.say "But you're the only one I have eyes for!"
    show harmony happy
    "I nod, trying to feel reassured by Harmony's promise."
    "But I can still see all the attention that she's getting."
    "And it's making me feel more than a little paranoid."
    "Back when Harmony was frumpy and pious, I never had to deal with all of this."
    "But I guess that's the trade-off for having her transform into a sex-kitten."
    "Maybe I should just be grateful to have a chance with her like this?"
    "That and keep clinging onto the hope that she won't eventually outgrow me!"
    mike.say "Come on, Harmony..."
    mike.say "Let's grab a drink."
    show harmony normal
    "Harmony gives this an eager nod, following me to the bar."
    "That's another thing that's changed about Harmony since she ditched the religion."
    "Before she'd only drink communion wine - now she practically drinks like a fish!"
    mike.say "Ah...can I get a beer, please?"
    mike.say "What about you, Harmony?"
    mike.say "You want a beer too?"
    show harmony happy
    harmony.say "I'd like a 'Sex on the Beach', please!"
    mike.say "You want what?!?"
    show harmony normal
    harmony.say "A 'Sex on the Beach', [hero.name]."
    harmony.say "It's a cocktail with vodka, peach schnapps and..."
    mike.say "I know what it is, Harmony."
    mike.say "Don't you think it's a bit strong for starters?"
    show harmony happy
    harmony.say "Nope, I don't."
    harmony.say "I want a 'Sex on the Beach', please!"
    "I shrug and order the drink that Harmony wants."
    "Maybe it'll be okay if I just keep an eye on her tonight."
    "And I don't want to blow it by getting sniffy over what she's drinking."
    "Once we have our drinks, we got to stand by the edge of the dance-floor."
    harmony.say "Mmm..."
    harmony.say "That really hit the spot!"
    harmony.say "Can I get another?"
    "At first I don't get what Harmony is talking about."
    "But then I spot the empty glass in her hand."
    mike.say "Y...you drank it already?"
    mike.say "Harmony, we only just walked away from the bar!"
    show harmony normal
    "Harmony pouts a little at this, frowning at me."
    harmony.say "I was thirsty, okay?"
    harmony.say "I promise I'll drink the next one more slowly."
    show harmony blush
    harmony.say "So are you going to get me another one, or what?"
    "Amazed by Harmony's sudden bitchiness, I don't know what else to do."
    hide harmony with dissolve
    "So I nod and hurry off to the bar to do as I'm told."
    "When I get back, I see that Harmony's waving at someone across the dance-floor."
    show harmony
    show fx exclamation
    mike.say "Hey!"
    mike.say "Who's that?!?"
    hide fx
    harmony.say "Oh, nobody in particular."
    harmony.say "They just smiled and waved at me."
    show harmony happy
    harmony.say "So I waved back, that's all."
    "I hand Harmony her second drink while scouring the crowd for the culprit."
    show harmony normal
    "Is she doing this on purpose, trying to make me jealous and paranoid?"
    "Or is Harmony just that innocent she doesn't know what she's doing?"
    "Whatever the truth of the matter, I need to shake off this funk I'm in!"
    "And what's the most natural thing to do in a night-club?"
    "Well, apart from getting wrecked on expensive cocktails!"
    mike.say "Come on, Harmony..."
    mike.say "Let's go dance, yeah?"
    show harmony happy
    "At the mere mention of hitting the dance-floor, Harmony's face lights up."
    harmony.say "Ooh, yeah!"
    harmony.say "I really feel like dancing tonight!"
    harmony.say "I've got so much energy to burn!"
    mike.say "Ah, that'll be the cocktail's, Harmony!"
    show harmony normal
    show fx question
    harmony.say "Huh...what was that?"
    mike.say "Erm...nothing - let's get out there, okay?"
    hide fx
    hide harmony
    show dance harmony date
    with dissolve
    "Harmony takes hold of my hand and leads me onto the dance-floor."
    "It's crowded, but we manage to find a spot that we can occupy."
    "Not that the cramped confines seem to bother Harmony in the slightest."
    "She giggles happily as we're pushed together in the packed crowd."
    "And I have no idea if she can even hear the music that's playing right now."
    "Because all Harmony seems to want to do is press herself against me."
    "Her arms are around me, pulling me closer still."
    "I feel like Harmony's grinding herself on me."
    "Like she's using me to get herself off!"
    "And I'm not complaining either - not in the slightest!"
    "My cock is hard as a rock, and my hands are all over her too."
    hide dance
    show harmony kiss date
    with dissolve
    $ harmony.flags.kiss += 1
    "Harmony kisses me at the same time, hard and full-on."
    "Her tongue is in my mouth, exploring like it has a mind of its own!"
    "I swear that she's actually tugging at my clothes."
    "Like she's forgotten where we are and she's trying to undress me!"
    hide harmony
    show harmony close date
    with dissolve
    "I break off the kiss and gasp for air."
    "And then I try to make myself heard over the sound of the music."
    mike.say "Harmony!"
    mike.say "You need to cool off a little!"
    show fx question
    harmony.say "Huh?"
    harmony.say "What do you mean?"
    hide fx
    mike.say "You can't do that here!"
    mike.say "Not in the middle of the dance-floor!"
    show fx exclamation
    "The light of recognition appears in Harmony's eyes."
    "And she instantly starts pulling me off the dance-floor."
    hide fx
    hide harmony
    show harmony date
    "At first I think she's sobered up a little."
    "At least to the point where my words are getting through to her."
    "But then I see that she's making straight for the nearest bathroom!"
    "I barely have time to follow her through the door."
    "And then she's pushing me into one of the empty cubicles."
    scene bg restroom
    show harmony date
    with fade
    mike.say "Whoa..."
    mike.say "Harmony, I didn't mean we needed to go someplace else!"
    mike.say "We really shouldn't be fucking in here either!"
    "Harmony has her back turned to me as she bolts the door."
    "But I can hear the giggles that my statement earns from her."
    "She turns around slowly, shaking her head at me."
    show harmony blush
    harmony.say "Oh, you WISH I was going to fuck you in here, [hero.name]!"
    harmony.say "I'm a bad girl, but I'm not THAT bad!"
    harmony.say "This is just an innocent little bit of oral, that's all..."
    show harmony bj restroom -blush with fade
    "With that, Harmony lowers herself onto her knees before me."
    "She gazes upwards, holding my eye as she unzips my pants."
    "Sure, I could tell her to stop, even take physical steps to end it."
    "But then why would I do a thing like that?"
    "My fears of Harmony trying to fuck me in here have been laid to rest."
    "And I'm all worked up right now, so what better way to calm myself down?"
    "The moment I feel Harmony's fingers closing around my cock it's settled."
    "I'm letting her have her way with me, and I'm going to enjoy every moment."
    "Harmony doesn't waste any time getting down to it either."
    "Normally it's nice to play around a little, even be teased."
    "But we're already in a compromising position."
    "Plus Harmony looks like she's almost desperate to do the deed."
    show harmony bj suck choke
    "This means that she opens her mouth and takes it in without hesitation."
    "Fully half of its length must go in there in the first few seconds."
    "And Harmony licks, kisses and nibbles the whole time too."
    "I'm pretty sure she hasn't had much experience with this kind of thing."
    "But she seems to be making up for it with sheer enthusiasm."
    show harmony bj surprised
    "As Harmony's head moves back and forth, I find myself gasping at the sensation."
    "I have to brace my arms against the walls of the cubicle to keep myself upright."
    "And yet none of this seems to make her slow down in the slightest."
    "In fact, the louder my moans become, the faster she goes."
    "I'm amazed at the portion of my cock Harmony can fit in her mouth."
    "And whatever isn't in there, she's working with her hand too."
    "Even the sound of what she's doing is turning me on."
    "I can remember hearing that mouth singing hymns in church."
    "But now it's sucking and gulping around my cock instead!"
    "Just as that thought occurs to me, Harmony opens her eyes."
    "She looks straight into mine, delight written all over her face."
    "The thrill of her fall from grace hits me like a jolt of electricity."
    "And I know in that moment that I'm mere seconds from cumming."


    "I don't even have time to warn Harmony that it's about to happen."
    "The sensation just overtakes me, and I lose the power of speech."
    show harmony bj orgasm cum with hpunch
    "This means that she's totally unprepared when I shoot my load in her mouth."
    with hpunch
    "Harmony coughs, splutters and gags, but somehow she holds on in there."
    with hpunch
    "Eyes wide she chokes down the unexpected mouthful as best she can."
    "And once it's all over, I can see that her eyes are actually watering!"










    hide harmony
    show harmony date happy naked
    with fade
    "I lean back against the wall of the cubicle, panting and light-headed."
    "But Harmony seems to recover far more quickly than I do."
    "The surprise disappears from her face, replaced with satisfaction and amusement."
    "She goes about cleaning herself up as I stuff my cock back into my pants."
    show harmony date -naked
    "And soon enough she's looking almost as presentable as she did when we came in here."
    "Harmony gets back to her feet and offers me her hand."
    harmony.say "Come on, [hero.name]..."
    harmony.say "Let's get back on the dance-floor!"
    "As exhausted as I feel right now, I hurry to obey."
    "Even if only for fear of not being able to keep up if I drag my heels."
    return

label harmony_event_04_slutty:
    if harmony.love.max < 190:
        $ harmony.love.max = 190
    scene bg street
    show harmony date
    with fade
    "Tonight is date night for Harmony and me, which usually means a lot of planning on my part."
    "Normally I like to know just where we're going and what we're going to be doing as well."
    "But this time round there was no time for me to think anything up before the big night."
    "So as neither of us wanted to cancel, we've instead decided to simply meet up and wing it."
    "Harmony and I are walking slowly down the street together, arm-in-arm."
    "And we're just waiting for something to jump out at us that we both want to do."
    mike.say "Ah..."
    mike.say "How about we grab something to eat in there, Harmony?"
    mike.say "[bree.name] ate there the other week, and she said it was great!"
    "Harmony looks at the restaurant I'm pointing to."
    show harmony annoyed
    "But then she wrinkles her nose in disapproval."
    harmony.say "Nah..."
    harmony.say "I'm not feeling hungry yet, [hero.name]."
    "She casts her gaze about as she says this."
    show harmony normal
    "And then she points out another possibility."
    harmony.say "The cinema's just around the corner over there."
    harmony.say "How about we go see if there's something neat showing?"
    show harmony blush
    harmony.say "Plus it'll be dark, so we can fool around a little!"
    "Now it's my turn to shake my head and say no."
    mike.say "Sorry, Harmony..."
    mike.say "I don't want to sit in the dark for a couple of hours!"
    mike.say "And if you want to get your hands on me, then we can do that at my place for free."
    show harmony sad
    "Harmony lets out a snort of frustration and curls her lip."
    "I can tell from her body-language that she's not mad at me."
    "But she is getting annoyed that we can't seem to agree on what to do."
    show harmony normal
    show fx exclamation
    "Suddenly her face brightens up and she starts to stride down the street."
    "I shake myself out of my funk and hurry after her a moment later."
    hide fx
    harmony.say "Come on, [hero.name]..."
    harmony.say "I just saw the perfect place!"
    mike.say "What?"
    mike.say "Where is it, Harmony?"
    mike.say "And what is it?"
    scene bg alley
    show harmony date
    with fade
    "I come to a halt a step behind Harmony as she reaches her destination."
    "Then I look up at the sign proclaiming the type of place she's settled upon."
    mike.say "But, Harmony..."
    mike.say "This is a strip-club!"
    show harmony happy
    "Harmony nods with genuine enthusiasm."
    harmony.say "Yeah, I can see that, [hero.name]!"
    show harmony normal
    harmony.say "But this is perfect for our date."
    harmony.say "We can get a drink, maybe even a bite to eat."
    show harmony happy
    harmony.say "And there's entertainment too!"
    show harmony normal
    mike.say "Are you serious, Harmony?"
    mike.say "You do realise that means girls dancing for money, right?"
    mike.say "Dancing with almost nothing on as well?"
    show harmony happy
    "Harmony laughs and shakes her head, like what I just said was crazy."
    harmony.say "Of course I do!"
    harmony.say "And it's fine."
    show harmony blush
    harmony.say "We're both adults, we can handle it!"
    "With that, Harmony grabs me by the hand."
    hide harmony with dissolve
    "And then she drags me into the strip-club."
    "Look, I'm no puritan."
    "I've been in my fair share of these places over the years."
    "But on all of those occasions I was never out with a date!"
    scene bg stripclub
    show harmony date at center, zoomAt(1.5, (980, 1040))
    with fade
    "Even so, Harmony seems to be as cool with it as she promised."
    "We grab a drink and find somewhere to sit with a good view."
    "And as soon as the first dancer takes to the stage, Harmony is entranced."
    "She watches wide-eyed as the girl twists and gyrates, drinking it all in."
    "She doesn't even hit me with any of the usual questions either."
    "Like asking me if any of the girls are prettier than she is."
    "But as the first dancer ends her set and the next gets started, I notice something odd."
    "The girls are good and very easy on the eye, but they're just not what I was expecting."
    "They look like they could have come here from work and gotten changed before dancing."
    "In fact, they look like they'd be more at home in an office or working in a store."
    "Then my eyes settle on the answer."
    "I see a sign on the side of the stage and read the words written on it."
    mike.say "Amateur Night..."
    mike.say "Huh...that explains a lot!"
    show fx question at right
    harmony.say "What do you mean?"
    mike.say "I thought these girls didn't look like regular strippers."
    hide fx
    mike.say "This must be the strip-club equivalent of an open mike night!"
    harmony.say "You mean..."
    show fx question at right
    harmony.say "You mean anyone can get up there and do it?!?"
    mike.say "Yeah, Harmony..."
    mike.say "I guess so..."
    mike.say "Erm...Harmony...where are you going?"
    hide fx
    "Harmony doesn't stop even to acknowledge my words."
    hide harmony
    show harmony date at right5
    "Instead she's up and hurrying across the floor of the club."
    hide harmony with moveoutright
    "I watch in stunned silence as she reaches the DJ booth by the stage."
    "She exchanges words with the DJ himself, and then climbs onto the stage."
    "Is she..."
    "She wouldn't..."
    "She can't be...can she?"
    "DJ" "And next, please welcome to the stage..."
    "DJ" "Harmony the Harlot!"
    "I swallow dryly as I watch what's unfolding before me."
    show harmony sexynun blush noacchead at right with moveinright
    "Raucous music plays as Harmony strides out into the middle of the stage."
    "She hold herself like she owns the place, like a queen holding court."
    "Instantly the crowd pick up on something about the way she's smiling."
    "It's like they just know this is going to be something special."
    "And from the moment she starts to move, Harmony doesn't disappoint."
    hide harmony
    show harmony poledance sexynun
    with fade
    "I was amazed at how little she was wearing when we met up earlier in the night."
    "But now somehow she manages to turn taking it all off into an entire act!"
    "Harmony twists and turns her body, inching her dress off of her shoulders."
    "Little by little, more of her naked flesh is exposed to the watching audience."
    "The weird thing is that I'm every bit as entranced as everyone else."
    "I mean, I've seen Harmony naked more than a few times by now."
    "But somehow seeing her on stage like this makes it all seem new."
    "I'm straining to see all that I can, just like everyone else."
    "And the more I see, the more I crave to see the rest of her."
    "I don't know if Harmony practised this routine beforehand."
    "Maybe the whole thing of dragging me in here was a set-up."
    "Then again, it could all be spontaneous, something she has a natural gift for."
    "Either way she's killing it up there, and I'm getting harder by the second."
    "Harmony's down to her bra and panties by now."
    "And she's wrapping herself around the pole on the stage."
    "I can't believe how easily she's teasing the audience in here."
    "They're following her every move, almost begging for more!"
    "When she finally turns her back and unhooks her bra, the place goes wild."
    "Harmony covers her breasts with both hands, then turns back around."
    "For a moment I think she's going to leave it at that."
    show harmony poledance naked with dissolve
    "But then she reaches out for the pole with her hands."
    "This allows her heavy, round breasts to fall free."
    "Harmony starts to move again, making them sway back and forth."
    "The motion is hypnotic, impossible to ignore."
    "I don't know if I'm being reminded of breast-feeding as a child."
    "Or just seduced by the most perfect pair of breasts imaginable!"
    hide harmony with fade
    "When Harmony stoops down and picks up her clothes, it comes as a genuine shock."
    "She hurries off the side of the stage while the rest of the crowd reacts in the same way."
    show harmony date happy at right with moveinright
    "But as she walks back to our table, Harmony gets a round of applause and cheers for her efforts."
    mike.say "I...I don't know what to say, Harmony!"
    mike.say "That was amazing!"
    show harmony date happy at center, zoomAt(1.5, (980, 1040))
    "Harmony smiles at this, even blushes a little."
    "But I can see that she's delighted with the praise."
    harmony.say "Oh, I don't know..."
    harmony.say "I guess I just got swept up in the moment, that's all!"
    show harmony normal
    harmony.say "I do wonder though...do they do this every week?"
    "I don't know if I should be thrilled or terrified at that prospect."
    "The thought of Harmony dancing like that again is impossible to resist."
    "But can I actually handle the prospect of all those eyes on her a second time?"
    return

label harmony_event_05_slutty:
    show harmony close
    mike.say "Hey Harmony, do you want to go{nw}"
    show harmony close happy
    harmony.say "Yes [hero.name], I'd like to!"
    harmony.say "I really enjoyed the strip club the last time we've go."
    harmony.say "Let's go back there again!"
    mike.say "Su...sure Harmony."
    $ hero.cancel_activity()
    $ hero.calendar.add(game.calendar.get_next_day_of_week("saturday"), DateAppointment(22, "harmony", "Date at the strip club (Harmony)", label="harmony_event_06_slutty", fail_label="missed_harmony_event_06_slutty"))
    hide harmony
    return

label missed_harmony_event_06_slutty(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Harmony is going to be mad."
        $ harmony.love -= 5
        $ harmony.sub -= 5
    $ DONE.pop("harmony_event_05_slutty", None)
    $ storytracker.refresh()
    return

label harmony_event_06_slutty(appointment=None):
    if harmony.love.max < 200:
        $ harmony.love.max = 200
    scene bg alley with fade
    "After the first visit we made to the strip-club, Harmony's still buzzing about it for days."
    "She talks about it constantly, replaying the scene from her memories in minute detail."
    "And she makes me do the same thing from my perspective too, telling her everything I can remember."
    "But no matter how often we do all of this, it just doesn't seem to be enough for her."
    "Harmony kind of reminds me of a junkie when the first hit of their drug is starting to fade."
    "And I know that she's going to have to do something drastic to regain that same high once more."
    "So it's no surprise that we find ourselves going back to the strip-club as soon as we can."
    "Or as soon as we know the amateur night is on again, that is..."
    show harmony date happy with dissolve
    harmony.say "Come on, [hero.name]!"
    harmony.say "Hurry up!"
    mike.say "What's the rush, Harmony?"
    mike.say "The stage isn't going anywhere!"
    "Harmony grabs hold of my wrist and drags me through the door of the strip-club."
    "And I have no choice but to quicken my pace as she does so."
    "It's that or end up falling on my face and being pulled inside."
    show harmony normal
    harmony.say "Don't be such a stick-in-the-mud!"
    harmony.say "We don't want to be the last in line to perform, do we?"
    "I nod in the hope of placating Harmony a little."
    "And in doing so, I almost miss the fact the she said 'we' rather than 'I'."
    "But I just put it down to her being so keen to get in there and onto the stage."
    scene bg stripclub
    show harmony date
    with fade
    "Once we're inside, I grab us some drinks while Harmony puts her name down."
    "And then all we can do is wait for her turn to come up."
    show harmony date at center, zoomAt(1.5, (640, 1040))
    harmony.say "Isn't this a good spot to watch, [hero.name]?"
    harmony.say "We can see everything from here!"
    "I nod, having to admit that Harmony's right."
    "We're sitting at a table right beside the stage."
    mike.say "Yeah, Harmony..."
    mike.say "The view's great!"
    mike.say "From here we won't miss a thing."
    show harmony happy
    "Harmony smiles, evidently pleased with the praise."
    "Just then the first of the amateur acts comes on stage."
    "And a hush settles over the audience as they get into it."
    "Of course the hush is soon replaced with whistling, cheering and clapping."
    "But the point is that the whole atmosphere in the place changes."
    "Before it was conversation and joking, like almost any bar."
    "Now it's all about watching somebody flaunt everything they've got!"
    "I'm seriously enjoying myself by now, getting into the show."
    "But I keep glancing across at Harmony now and then."
    show harmony normal
    "And the look on her face is making me a little concerned."
    "Instead of being into it too, she looks pretty impatient."
    "The only thing I can figure is that she's itching to get up there herself."
    "Which means there's really nothing I can do to alleviate the tension she's feeling."
    "I can only will the time away until her turn on the stage comes around."
    "DJ" "And next up we have..."
    "DJ" "Harmony and her companion!"
    hide harmony
    show harmony date normal
    "Before I can fully grasp what the DJ just said, Harmony's up and on her feet."
    with vpunch
    "At the same time she yanks me out of my seat and towards the stage."
    "There's no time for me to come to my senses, let alone have a hope of resisting."
    "And so I find myself on the stage, blinking at the glare of the lights."
    "Harmony, evidently aware of my confusion, leans in to whisper in my ear."
    show harmony blush
    harmony.say "Don't worry about a thing, [hero.name]."
    harmony.say "I have it all worked out."
    harmony.say "So just sit back and let me handle everything..."
    mike.say "Harmony..."
    mike.say "What are you talking about?"
    mike.say "Why am I on the stage with you?!?"
    "Rather than answering any of my questions, Harmony simply assumes a provocative stance."
    "A moment later music begins to play, and she starts to move in an equally provocative manner."
    show harmony at left4 with ease
    "Harmony circles me slowly, getting closer all the time."
    show harmony at center with ease
    "She moves like a slithering serpent, one ready to strike at any moment."
    show harmony at right4 with ease
    "By contrast, I find myself rooted to the spot in the middle of the stage."
    "The only parts of me that seems to move are my eyeballs."
    show harmony at center with ease
    "These follow Harmony as closely as they possibly can."
    "All the time my heart is pounding in my chest."
    "I barely hear the sounds that the audience are making."
    "And the stage seems to fade out of existence for me too."
    "The only thing I can see for certain is Harmony."
    show harmony naked normal with dissolve
    "I watch transfixed as she begins to strip off her clothes."
    "She does this in that same serpentine fashion, like she's shedding her skin."
    show harmony at right4 with ease
    "With each item of clothing she removes, more pale flesh is revealed."
    "Harmony was wearing an outfit that looked pretty tight and revealing."
    show harmony at center with ease
    "But somehow the sight of her naked body is different, more intense and powerful."
    show harmony at left4 with ease
    "All I can feel is the desire for her that's rising up inside of me right now!"
    show harmony blush at center with ease
    "Maybe that's why I don't do a thing when Harmony starts undressing me too."
    "I'm so swept up in the moment that all I can think of is her."
    "For some reason where we are doesn't seem to matter to me at all."
    "And the fact that there are other people in the room never even occurs to me."
    show harmony at left4 with ease
    "Harmony continues to dance around me, pulling off my clothes as she does so."
    show harmony at center with ease
    "Soon enough we're both naked, and I can't hide the effect she's having on me."
    "My cock is standing proud in front of me."
    "And it's clear that Harmony wants it badly."
    "She strokes it, purring like a hungry cat."
    "Then she bends over in front of me, like she's offering herself up."
    "I swear I'm not in control as all this happens."
    "My brain's on auto-pilot, controlled by animal instinct."
    "Because I don't hesitate to grab hold of Harmony."
    show harmony doggy stripclub pleasure with hpunch
    "She squeals as I take hold of her ample haunches."
    "And then she gasps as I pull her backwards and thrust myself forwards."
    "My cock doesn't hit the target at first."
    show harmony doggy surprised
    "Instead it slips and slides over Harmony's lips."
    "This makes her quiver and quake with unsuppressed desire."
    show harmony doggy pleasure pov
    "She wriggles backwards, desperate to have me inside of her."
    "And with me pushing in the other direction, that's exactly what happens."
    show harmony doggy hurt vaginal
    "My cock pushes between her lips and into Harmony's pussy."
    "She's slick and hot, swallowing me with what feels like desperation."
    "I don't stop pushing into her until I can go no further."
    "And every fraction of an inch makes Harmony moan with pleasure."
    harmony.say "Oh fuck..."
    harmony.say "That feels SO good!"
    harmony.say "Please, [hero.name]...fuck me!"
    harmony.say "Fuck me in front of them all!"
    show harmony doggy normal
    harmony.say "I'm a dirty, horny little bitch, aren't I?"
    "I don't even bother to answer Harmony's questions."
    show harmony doggy pleasure bounce with vpunch
    "Instead I just begin to pound her as hard as I possibly can."
    "She was performing a dance to seduce me when this thing began."
    "But now I'm just fucking her out of pure animal desire."
    "It hardly matters to me that everyone in the place is watching."
    "I'm simply mounting Harmony to possess her, to prove myself."
    "And that animal need seems to translate into her reactions too."
    "Harmony pants and wails, taking everything that I have to give her."
    "Those generous curves make her feel so solid and real."
    "And they mean that she can absorb every thrust I make into her."
    "My thighs slap into Harmony, making her buttocks quake."
    "I can see her heavy, round breasts swinging beneath her."
    show harmony doggy pleasure
    "But when she looks back over her shoulder at me, that's what pushes me over the edge!"
    "Her eyes are wide, but almost dull with surrender and gratitude."
    "Harmony nods, her mouth hanging open as she gaps with pleasure."
    "She looks totally submissive, willing to take anything I give her."
    "But on top of it all, I can see that she's completely happy too!"
    "This is what Harmony wants, to be used for my sexual gratification."
    "All the more so if there's a chance for the act to be made public!"
    mike.say "Ah..."
    mike.say "Fuck, Harmony..."
    mike.say "I'm gonna cum!"
    harmony.say "Cum in me, please!"
    harmony.say "I want you to do it!"
    harmony.say "Fill me up while they all watch!"
    "I don't know if I even have a choice in the matter!"
    show harmony doggy ahegao creampie squirt with hpunch
    $ harmony.love += 2
    $ harmony.sexperience += 1
    "The next thing I know, I'm shooting my load into Harmony."
    with hpunch
    "She practically screams the whole time, wriggling on my cock."
    with hpunch
    "But all the while she's nodding her head, willing me to keep on going."
    "Afterwards, I envision us having to sneak out of the place in shame."
    hide harmony
    show harmony date normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "Yet once we're cleaned up, dressed and back in our seats, that's not the case."
    "Harmony and I get a round of applause and admiring glances."
    "Someone even sends us an anonymous round of drinks too!"
    mike.say "I...I think they liked it, Harmony!"
    show harmony happy
    harmony.say "What did I tell you, [hero.name]?"
    harmony.say "I had it all worked out!"
    mike.say "I guess you did!"
    mike.say "But do me a favour and ask me next time, yeah?"
    show harmony blush
    harmony.say "Oh, but where's the fun in that?"
    harmony.say "And how am I supposed to know you're not just pretending to love it?"
    "I shake my head at Harmony and turn my attention to my free drink instead."
    "But the truth is that I enjoyed that far more than I ever thought possible."
    "And I'm already beginning to wonder what other ideas Harmony has in that head of hers..."
    return

label harmony_purity_01:
    show harmony close
    "Harmony looks at me sideways, as if she has something to say, but can't quite pluck up the courage."
    mike.say "Ah, what's bugging you, Harmony?"
    harmony.say "Well..."
    harmony.say "It's the annual church dance this weekend, you know?"
    "Even though I'm supposed to be an active member of the congregation, I admit that I didn't."
    "But I'm not about to admit as much to Harmony!"
    mike.say "Sure I did, Harmony."
    mike.say "What about it?"
    harmony.say "I was wondering if..."
    harmony.say "You'd like to come along?"
    harmony.say "We could use some help to get the numbers up this year!"
    menu:
        "No way":
            mike.say "Ah, sorry, Harmony."
            mike.say "I have plans this weekend!"
            mike.say "Any other time, and I'd have been there like a shot."
            show harmony sad
            "Harmony looks visibly disappointed, but she nods her head all the same."
            harmony.say "Ah well, I just thought I'd ask."
            $ hero.cancel_event()
        "Ok":
            mike.say "I did have plans for the weekend."
            $ harmony.love += 2
            mike.say "But as it's you asking, I'll cancel them and come to the dance instead."
            show harmony happy
            "Harmony smiles at this, almost clapping her hands together in glee."
            harmony.say "Oh, thank you, [hero.name]!"
            harmony.say "I promise that you won't regret this."
            $ hero.calendar.add(game.calendar.get_next_day_of_week("sunday"), DateAppointment(14, "harmony", "Date (Harmony)", "harmony_purity_02", "missed_harmony_purity_02"))
    hide harmony
    return

label missed_harmony_purity_02(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Harmony is going to be mad."
        $ harmony.love -= 4
    $ DONE.pop("harmony_purity_01", None)
    $ storytracker.refresh()
    return

label harmony_purity_01_fix:
    $ DONE.pop("harmony_purity_01", None)
    return

label harmony_purity_02(appointment=None):
    play music "music/roa_music/one_day.ogg" fadeout .5 fadein .5
    scene bg church
    $ harmony.purity.min = 70
    "Yeah, yeah, yeah - I know that you'd have to try really hard to imagine something more lame than a church dance."
    "And you'd be right too, as this one is all of the cliches that you might expect to see, and then some!"
    "It's full of old folks, annoying kids and the kind of people who are just far too keen on Jesus for their own good."
    "But it's also right where Harmony happens to be too."
    "And so long as she's here, I'm willing to put up with all of the rest."
    show harmony date zorder 2 at center with dissolve
    harmony.say "Hello, [hero.name]."
    harmony.say "I'm so happy that you came!"
    mike.say "Hey, Harmony."
    mike.say "I wouldn't have missed it for the world."
    mike.say "Especially after you asked me to come along!"
    show harmony happy
    "I see Harmony's cheeks flush a little at my enthusiasm for her invite."
    "Sometimes I forget just how innocent she is, and I worry about coming on too strong."
    show harmony normal
    mike.say "But I'd have come along anyway...of course I would!"
    mike.say "We have to do our bit for the church, right?"
    show harmony happy
    "As quickly as she blushed, Harmony recovers and smiles broadly."
    harmony.say "Y...yes...of course!"
    harmony.say "This is all about us being one big Christian congregation!"
    show harmony normal
    "She turns towards the dance-floor, as if trying to change the subject."
    "Even though the hall is pretty full, the same can't be said for the dance-floor."
    mike.say "Not many takers yet, eh?"
    "Harmony greets this observation with a curt nod and a smile."
    "Just like her to see it as an opportunity, rather than a problem..."
    harmony.say "Well, what do you say we do something about that, you and me?"
    mike.say "Erm, okay - what did you have in mind?"
    harmony.say "I think I know a lady that'd love to dance with a big handsome guy like you, [hero.name]!"
    "Of course, my eyes instantly light up at this."
    "I thought it'd take me a while to pluck up the courage to ask Harmony to dance."
    "But here she is, practically offering me the chance almost before I've walked through the door!"
    mike.say "Okay, Harmony - it'd be impolite to turn a lady down, wouldn't it?"

    show emma a casual topless zorder 1 at center, flip, zoomAt(0.9, (640, 500)), blacker
    show harmony happy at right with ease
    "Harmony nods as she steps neatly aside."
    "This reveals a small girl that's been hiding behind her the whole time."
    harmony.say "See, Celeste - I told you [hero.name] would dance with you!"
    "The little girl, who can't be more than six or seven, smiles to reveal a mouthful of braces."
    "She grabs my hand and pulls me towards the dance-floor, as Harmony watches approvingly."
    "Sure, I'm disappointed to have misread the situation."
    "But I'm not a big enough jerk to act like one in front of a sweet little girl!"
    "So I dutifully take her round the dance-floor to a couple of sedate tracks, smiling the whole time."
    scene bg black with timelaps
    scene bg church with timelaps
    $ game.pass_time()
    "As we walk off the dance-floor, I see that Harmony's delighted with my performance."
    show harmony date happy zorder 2 at center
    "I guess I should be thankful of the karma it's earned me in her eyes."
    harmony.say "Aw, that was so sweet of you, [hero.name]."
    mike.say "No worries, Harmony."
    mike.say "I'm happy to make Celeste happy."
    show harmony normal
    harmony.say "Someone was watching you the whole time, you know?"
    mike.say "They were?"
    harmony.say "Sure they were!"
    harmony.say "And they were so impressed that they want to dance with you themselves."
    "Here it comes, my reward for being so kind to a little girl!"
    mike.say "Well, I don't have a partner for the next dance..."

    show sasha b wedding zorder 1 at center, flip, zoomAt(0.9, (640, 500)), blacker
    show harmony happy at right with ease
    "As Harmony steps aside for the second time, I feel a terrible sense of deja vu."
    "My eyes fall on one of the oldest women in the congregation."
    "Imagine a Caucasian Yoda with a blue rinse and thick glasses."
    harmony.say "There you go, Prudence - he's all yours."
    hide harmony with dissolve
    "And so I take to the floor for a second time, carefully walking the fragile old lady through some basic steps."
    "The whole time I keep looking over at Harmony, wondering if I'm ever going to get to dance with her."
    scene bg black with timelaps
    scene bg church with timelaps
    $ game.pass_time()
    "She greets me even more warmly than after the last dance when I return to her side."
    "I do my best to smile back and show willing."
    show harmony date
    "But all the same, Harmony seems to notice that there's something wrong."
    "She puts her hand atop mine, setting my heart racing without even knowing it."
    show harmony sad
    harmony.say "[hero.name] - what's the matter?"
    mike.say "It's nothing, Harmony."
    harmony.say "No, [hero.name], it's not."
    harmony.say "We're friends, aren't we?"
    harmony.say "You can tell me what's bothering you."
    "I shrug and let out a little laugh."
    mike.say "I don't know, Harmony."
    mike.say "It'll sound dumb!"
    harmony.say "No, it won't - you can tell me!"
    mike.say "Ah, okay...here goes..."
    mike.say "I'm kinda bummed that I haven't got to dance with you yet!"
    show harmony close normal at vshake
    show fx exclamation
    "At this, I see Harmony's eyes go wide, and she flushes with colour again."
    show harmony happy
    harmony.say "Oh, [hero.name]..."
    harmony.say "I'm so sorry - I've been such a bad friend!"
    harmony.say "Of course I'll dance with you - I'll dance with you right now!"
    hide fx
    "And with that, she takes my hand and leads me out onto the dance-floor."
    menu:
        "Keep things clean and wholesome":
            hide harmony
            show dance harmony date
            with fade
            $ harmony.love += 5
            "I'm so nervous as I follow Harmony onto the floor that I almost trip over my own feet on the way."
            "The hardest thing of all is to keep my mind on the actual task of dancing."
            "As without an effort in concentration, all I can to is just stare into her eyes."
            "This means that the dance can't be anything but slow and steady."
            "But that's a pace and tempo that seems to suit the both of us very well indeed."
            "As much as I'm physically attracted to Harmony, I now know there's more than that between us."
            "Somehow I feel almost as much of a thrill from not touching her as doing so."
            "It's like there's a building energy between us whenever we come this close."
            "A kind of static electricity that only gets stronger so long as we resist the temptation to discharge it."
            "And still looking into Harmony's eyes, I'm sure that she feels it too."
            "She holds my gaze for the longest time, staring deeply into me."
            "And when she finally looks away, I get the feeling that it's for fear of feeling too much too soon."
            "When the dance comes to a natural end, neither of us says a thing."
            "There's no need, as I'm certain that we just shared a moment of great significance."
        "Pull Harmony close for the dance":
            $ harmony.purity -= 5
            $ harmony.love -= 5
            hide harmony
            show dance harmony date
            with fade
            "I've been waiting for this moment so long, I guess I kind of lose control a little."
            "Almost as soon as we're out there, I reach out and take hold of Harmony's hips."
            "She lets out a little yelp of surprise, instinctively wrapping her arms around my neck."
            "I start to move in a basic, swaying motion, before she has the chance to object."
            "Harmony struggles a little, wriggling against me in the hope of winning back some distance."
            "But all this does is exaggerate the moves that I'm already making."
            "She looks down at how close our bodies are pressed together."
            "And then she looks up at me, her eyes wide with fear."
            "Fear and something else..."
            "And it's that something else that I choose to focus my attention on."
            "Slowly, ever so slowly, I feel the resistance in Harmony begin to fail."
            "She moves more freely with me, no longer trying to pull away."
            "I feel the stiffness in her limbs finally start to melt."
            "Her eyes blink, and then almost fall closed."
            "And I feel the weight of her head as it comes to rest upon my shoulder."
            "And with that, Harmony surrenders herself to the dance, and to me."
            "When the dance comes to a natural end, neither of us says a thing."
            "There's no need, as I'm certain that we just shared a moment of great significance."
    hide dance
    $ game.pass_time(2)
    $ game.room = "church"
    return

label harmony_purity_03:
    show harmony close
    "It's hard to choose a suitably wholesome thing to do on a date with a girl like Harmony."
    "So in the end, I just go with the first thing that comes into my head without any perverse overtones."
    mike.say "Erm, how about we have a picnic next sunday, Harmony?"
    "Harmony looks at me with a slightly puzzled expression."
    "Clearly not expecting to have been asked that, of all things."
    harmony.say "Sure, [hero.name]...why not!"
    hide harmony
    $ hero.cancel_activity()
    $ hero.calendar.add(game.calendar.get_next_day_of_week("sunday"), DateAppointment(12, "harmony", "Date (Harmony)", "harmony_purity_04", "missed_harmony_purity_04"))
    return

label missed_harmony_purity_04(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Harmony is going to be mad."
        $ harmony.love -= 4
    $ DONE.pop("harmony_purity_03", None)
    $ storytracker.refresh()
    return

label harmony_purity_03_fix:
    $ DONE.pop("harmony_purity_03", None)
    return

label harmony_purity_04(appointment=None):
    play music "music/roa_music/one_day.ogg" fadeout .5 fadein .5
    $ harmony.purity.min = 50
    show bg park
    show harmony casual
    with fade
    harmony.say "Hello, [hero.name]."
    mike.say "Uh...hey, Harmony."
    "She giggles at my anxiousness for a second time, clearly finding it endearing."
    show harmony happy
    harmony.say "There's no need to worry, [hero.name]."
    harmony.say "Picnics are really just a chance to eat a meal in the bosom of nature!"
    harmony.say "And I'll be here to teach you all that you need to know..."
    show harmony close casual at cleavage
    "Oh hell - why did she have to use the word 'bosom'?"
    "Now all I can do is stare at her chest!"
    hide harmony
    show harmony casual normal
    "For a girl that's supposedly a good Christian, Harmony sure knows how to tempt me."
    "Right now I feel like I'm Adam and she's the the sexy serpent, rather than the innocent Eve!"
    harmony.say "Maybe we should start with a glass of lemonade?"
    harmony.say "Then we can move on to the cucumber sandwiches!"
    "I know full well that those are nothing more than innocuous items of food and drink."
    "So why do they sound like the filthiest of innuendos when coming from Harmony's lips?"
    "I try my best to banish any and all impure thoughts from my mind and just enjoy the picnic."
    "That's something that I should be able to do, right?"
    show harmony picnic with fade
    "And as we begin to eat the picnic food that Harmony's prepared, I try to do just that."
    "Pretty soon I find myself relaxed by the setting and the pleasant conversation between us."
    "I almost forget the sense of sexual tension that I can feel as it fades into the background."
    "And yet all of that changes as soon as Harmony pulls a punnet of strawberries out of the hamper."
    "The smile that she offers me as she places them on the blanket between us should be just that."
    "But strawberries are a sexy fruit, aren't they?"
    "All ripe, succulent and bursting with flavour..."
    "Wait a minute...am I talking about the strawberries or Harmony here?!?"
    "Anyway - we take it in turns to pluck a strawberry from the punnet and eat them almost shyly."
    "I can't be sure, but I think Harmony's starting to feel a little of my awkwardness too."
    "It's then that our hands touch as we both reach for the last strawberry."
    mike.say "Oh...sorry."
    harmony.say "No, no - I should have looked first."
    mike.say "You should have it, Harmony."
    mike.say "You brought the picnic after all."
    harmony.say "I couldn't do that."
    harmony.say "It'd be so bad of me..."
    mike.say "We could share it?"
    harmony.say "You mean cut it in half?"
    "I can feel the butterflies in my stomach as I find the courage to say the words."
    mike.say "Ah, no..."
    mike.say "I was thinking that we could maybe...take turns at taking a bite?"
    harmony.say "Okay, [hero.name] - that sounds like it might be fun!"
    "I raise the strawberry to Harmony's lips, and she takes a self-consciously small bite."
    "Then she returns the favour, and I feel her fingers lightly brush my lip."
    "Thanks to the strawberry being a large one, there's enough left for one last bite."
    "Then it happens - we both lean in, anticipating that last bite to be for us."
    "And sure, we both get a bit of strawberry for out troubles."
    show harmony kiss casual with fade
    $ harmony.flags.kiss += 1
    "But at the same time we end up with our lips pressed together into the bargain."
    menu:
        "Pull back from the accidental kiss":
            "The moment that our lips come together, I feel like I'm having a kind of epiphany."
            "Suddenly I understand where all of the tension between Harmony and myself is coming from."
            "And it's solely my own fault for letting myself get distracted by her physical beauty."
            "If, God willing, our relationship grows and we become closer, then there'll be a time for that."
            "But right now, I need to keep a close reign on my emotions."
            "What I need to do is focus on my feelings for Harmony as a friend and companion."
            "Not sit here dwelling on her body, but appreciate her mind and personality."
            hide harmony
            show harmony picnic
            with fade
            "So I pull myself away from the accidental kiss, being sure to smile at her as I do so."
            mike.say "I'm sorry, Harmony."
            mike.say "That felt amazing - but I shouldn't have taken such a liberty."
            "Harmony looks away for a moment, which means I can't see her instant reaction to my apology."
            "When she turns her head back to me a moment later, she's wearing a small, modest smile."
            harmony.say "It's okay, [hero.name]."
            harmony.say "I'm as much to blame as you are."
            "She pauses for a moment, and then seems to decide to say something more."
            harmony.say "For the record - I thought it was rather nice too..."
            "I smile and take her hand in mine."
            "It feels so good to know that we understand each other like this."
            "Sure, we might have gone a little too far too fast just now."
            "But I have the feeling that it'll serve as a reminder for us to be more careful in future."
            "Harmony feels so special to me that I don't want to take any chances."
            "Who knows - she might even be the one that I've been waiting for!"
        "Lean into the accidental kiss":
            $ harmony.purity -= 5
            $ harmony.love -= 5
            "The moment that our lips come together, everything just feels right."
            "I've always known where the tension between us is really coming from."
            "And now I'm not going to pass up the chance to blow some of it off."
            "I turn my head, leaning into the previously chaste kiss and applying more pressure as I do so."
            "Harmony makes a surprised squeaking sound as her lips are pressed against my own."
            "But then I hear the sound of it change into a helpless, breathy sigh."
            "No more than a second or two later, she begins to return the kiss with equal amounts of passion."
            "Don't get me wrong - this isn't some tongue-heavy make-out session in the middle of the park."
            "By my normal standards, what we're doing is really pretty tame."
            "But then I'm not stealing one of my first kisses from any normal girl."
            "Harmony's innocence and purity make me feel like I'm educating her at the same time."
            "Maybe even a little like I'm corrupting her too..."
            "And yet it's not like she's being fooled or forced into returning the kiss either."
            "Instead she seems to grow in confidence with every second that passes."
            "More than once I swear that I can actually feel the tip of her tongue as it darts between my open lips."
            "I have no idea just how long the kiss lasts, but eventually it comes to a natural end."
            hide harmony
            show harmony picnic
            with fade
            "Harmony and I stare at each other, cheeks flushed and trying to catch our breath."
            mike.say "I'm sorry, Harmony."
            mike.say "I didn't mean to..."
            "Harmony shakes her head, dismissing my faltering apology as quickly as I make it."
            harmony.say "Don't be silly, [hero.name]."
            harmony.say "That was just as much me as it was you!"
            "I feel a sudden sense of relief at this."
            "Harmony's words making me realise that it was not just me forcing myself upon her."
            "Rather it was something mutual and spontaneous in nature."
            harmony.say "And...well, it was really nice too."
            mike.say "Really?"
            harmony.say "Yeah, silly - of course it was!"
            mike.say "Um...would you like to do it again?"
            "Harmony laughs and shakes her head, then kisses me for a second time."
            "This one lasts a lot longer than the last one."
            "And yes, there are tongues involved..."
    $ game.pass_time(2)
    hide harmony
    return

label harmony_purity_05:
    $ harmony.purity.min = 30
    scene bg church with fade
    "I can remember a time when going to Mass felt like a chore."
    "It was something that I felt I had to do, not something that I wanted to do."
    "But all of that changed when I met Harmony and we struck up a relationship."
    "And now I find myself looking forward to Mass, excited when it comes around."
    "I'd like to say it's because Harmony's pureness and piety is rubbing off on me."
    "But let's be honest, it's really because she's super hot!"
    "And I spend most of the service stealing glances at her."
    "Seriously, the priest might as well be speaking a foreign language."
    "All of my attention's focused on Harmony while we're sat in the pews."
    show harmony with dissolve
    "Like right now, we're sitting side by side and holding hands."
    "Each of us has a bible open in our laps, pretending to listen to the sermon."
    "But the only thing on my mind right now is Harmony."
    "Well, Harmony and how hard she's making me too!"
    "Suddenly I get the urge to show her the effect she's having on me."
    "And so I lift my bible and gently pull her hand underneath."
    show harmony church hj with fade
    "At first she looks over at me with interest."
    "But the moment she feels how hard my cock is, her eyes go wide."
    show harmony church hj lookbook
    "Harmony glances up at the priest for a moment."
    "And I'm almost convinced she's about to pull her hand away."
    show harmony church hj happy
    "Then I see a wicked smile spread slowly across her face."
    "Of course she doesn't say a word, but she doesn't need to."
    "I feel Harmony locate the zipper on my pants."
    "And then she deftly pulls it down, slipping her fingers inside."
    "At first all she does is stroke it through my shorts."
    "Even that's enough to make me go stiff as a board."
    "I want to moan at the sensation, to nod and encourage her."
    "But I can't let on for a moment what's happening."
    "We're sitting in church, surrounded by the congregation."
    "Luckily for me, Harmony doesn't seem to need any prompting."
    "I feel her fingers slide into my shorts, wrapping around my cock."
    "She gives it an unexpectedly hard squeeze a second later."
    "And I have to bite my tongue to keep from crying out."
    "I glance sideways at Harmony, and I can see her smile is wider than ever."
    "She's enjoying herself right now, and it's making her bolder by the second."
    show harmony church hj lookmike
    "Harmony begins to rub her hand up and down the length of the shaft."
    "She doesn't have to apply too much pressure or work very hard."
    "Because the constant fear of being discovered is always there."
    "It's making my heart race, making her every touch fraught with danger."
    show harmony church hj lookbook
    "Harmony grasps me tighter, taking me by complete surprise."
    "I can't help jolting upright in my seat."
    "It's like I'm snapping to attention."
    "But luckily for me, most people seem not to notice."
    "Maybe they think I was just dropping off to sleep and suddenly woke up again."
    "But there's no mistaking the fact that Harmony knows exactly what's going on."
    show harmony church hj dick
    "She giggles under her breath as she pulls my cock out of my pants."
    "I try to stop her, but there's nothing I can do."
    "Well, at least noting that won't cause a scene!"
    "I feel the cold cover of the bible against my cock."
    show harmony church hj speed
    "And then Harmony is at it again, rubbing up and down."
    "She's going faster than ever now, working me hard."
    "Maybe it's the thrill of knowing only the bible is hiding what she's doing."
    "Or maybe Harmony's just that into it that she's getting carried away."
    "Either way, it doesn't really matter what's behind her enthusiasm."
    "I can still feel her pushing me ever closer to losing it."
    "It's then that I see people fumbling for their hymn books."
    "Oh shit - they're getting ready to stand up and sing!"
    show harmony church hj cumshot dickcum lookmike with vpunch
    "A moment later I feel myself shudder as I shoot my load."
    with vpunch
    "Cum shoots out, spattering over Harmony's hand and the cover of the bible."
    show harmony church hj -cumshot lookbook
    "She giggles in my ear as she wipes her hand on a tissue from her purse."
    "And then she picks up her own hymn book as I struggle to make myself decent."
    hide harmony
    show harmony happy
    with fade
    "I only just manage to zip up my flies in time."
    "My cock narrowly avoiding being circumcised in the act!"
    "The cum-spattered bible I toss under the pew to deal with later."
    "Still dishevelled and disoriented, I stand up next to Harmony."
    "But she's already singing away, a smile plastered across her face."
    $ harmony.purity -= 5
    "For all the world, she looks like she just had a revelation."
    "Though perhaps not one of the religious variety."
    return

label harmony_purity_06:
    $ harmony.purity.min = 10
    scene bg nightclub
    show harmony date
    with fade
    "I can sense that something's different about Harmony tonight."
    "It's like she has an itch to scratch or something of that kind."
    "And she's aware of everyone looking her way in the club too."
    "More than once I have to steer her away from another guy."
    "I know that all she's doing is smiling in return for an admiring glance."
    "But there's just something with her tonight that's got me worried."
    "And I don't want to let things get out of hand."
    mike.say "Hey, Harmony..."
    mike.say "How about we head over to the VIP area?"
    show fx exclamation
    "That suggestion gets Harmony's complete attention."
    "She raises her eyebrows and nods her head in agreement."
    harmony.say "You can really get us in there?!?"
    harmony.say "If you can, I'm SO up for that!"
    "Harmony clings onto me as I lead the way over to the VIP area."
    "The guy on the door checks my credentials and then waves us in."
    show bg vip
    show harmony happy
    with fade
    harmony.say "Oh wow..."
    harmony.say "This is so cool, [hero.name]!"
    harmony.say "Everyone in the club is looking at us right now!"
    show harmony normal
    "Harmony seems to shudder as she says all of this."
    "Almost like there's a thrill running through her entire body."
    mike.say "Ah..."
    mike.say "Okay, Harmony..."
    mike.say "You want another drink?"
    show harmony blush
    harmony.say "No, [hero.name] - I want to fuck!"
    "It takes a moment for me to realise what Harmony just said."
    "I understand the meaning of the words that came out of her mouth."
    "But the context doesn't seem to make sense."
    mike.say "You want to do what?"
    harmony.say "I said I want to fuck, [hero.name]!"
    harmony.say "I want us to have sex, right here and right now."
    harmony.say "We can do it over there - in one of those booths!"
    "I look over to the unoccupied booth that Harmony's pointing out."
    "And then I turn my gaze back to her."
    "There's only one possible answer to that question."
    menu:
        "Accept":
            mike.say "You read my mind, Harmony!"
            mike.say "I've always wanted to do it in a place like this."
            mike.say "After all, what's the point of being a VIP if you can't break the rules!"
            $ harmony.purity -= 5
            show harmony happy
            "Harmony's face lights up as I say all of this."
            "She claps her hands together as we hurry over to the booth."
            show harmony blush
            harmony.say "Mmm..."
            harmony.say "I'm so horny right now, [hero.name]!"
            harmony.say "I can't wait to have you inside of me!"
            "I nod eagerly as I start to pull off my clothes."
            "Just the idea of fucking Harmony's got me nice and hard."
            "And the fact that all those eyes are going to be on us the whole time..."
            "Well, it adds a whole new level of thrill on top too!"
            show harmony naked with dissolve
            "Harmony and I both strip off at record speed, tossing our clothes aside."
            "I'm pretty sure that nobody's going to try and stop us doing it."
            "But there's no point in taking a chance like that."
            "And likewise, once we're naked, we don't waste any time getting started."
            show harmony doggy vip with hpunch
            "I just grab a firm hold of Harmony's generous haunches."
            "Then I pull her backwards and onto me in one sudden motion."
            "She wasn't lying when she said that she was ready for me either."
            show harmony doggy pov vaginaltip
            "My cock presses against the lips of Harmony's pussy for a mere second."
            show harmony doggy vaginal surprised
            "And then I'm inside of her, slipping all the way inside."
            harmony.say "Oh..."
            harmony.say "Oh fuck yeah!"
            show harmony doggy pleasure
            harmony.say "That feels so good, [hero.name]!"
            "She's not just saying that to keep me happy either."
            "It feels incredible from my side of things too."
            show harmony doggy bounce hurt -pov with hpunch
            "And I set about hammering away as soon as I can."
            "It actually takes longer for people to see what we're doing than I expected."
            "We're in a nightclub, after all, where the lights are subdued and the music is loud."
            "But soon enough, heads begin to turn in our direction, gazes settling on us."
            "Nobody seems to be inclined to intervene or demand that we stop."
            "Perhaps they would have done if they'd realised earlier."
            "I guess it's that much harder to step in when someone's actually fucking!"
            show harmony doggy pleasure squirt
            "The moment that I'm sure we're the centre of attention, I feel a change in Harmony."
            "It's like the more people staring at her, the more turned-on she becomes."
            "She moans and gasps, riding my cock like her life depends on it."
            "The more she's stared at, the more debauched she behaves."
            "And the more Harmony debases herself, the more aroused I feel in turn."
            "By now her cheeks are red and flushed."
            "Though I can't tell if it's from exertion or embarrassment!"
            harmony.say "Ah..."
            harmony.say "I'm so dirty...so cheap...I'm trash..."
            harmony.say "Use me like a slut, [hero.name]...please?!?"
            "That does it for me, pushes me over the edge."
            show harmony doggy ahegao pov creampie -bounce with hpunch
            $ harmony.love += 4
            "I shoot my load into Harmony."
            with hpunch
            "And she cries out as I do so."
            with hpunch
            "Harmony quivers and shakes."
            "All eyes are still on her as I begin to get dressed."
            "I can hear her panting as I watch cum drip out of her pussy."
            "But I can't help wondering if that was enough for Harmony to scratch the itch."
            $ game.active_date.score += 20
            $ harmony.sexperience += 1
        "Refuse":
            mike.say "You can't be serious, Harmony!"
            mike.say "I'm pretty sure that'd be indecent exposure."
            mike.say "And probably half a dozen other criminal offences too!"
            $ harmony.love -= 5
            show harmony sad
            "Harmony looks shocked and disappointed, frowning at my refusal."
            "She crosses her arms over her chest, like she's pouting."
            harmony.say "It's only a crime if someone reports it."
            show harmony annoyed
            harmony.say "And what's the point of being a VIP anyway?"
            harmony.say "Especially if you don't get to do crazy stuff!"
            "I glance around, seeing that our conversation is drawing attention."
            "And what can you expect when you're discussing sex in a public place?"
            mike.say "Harmony, I really think we need to leave."
            mike.say "If you want sex, we can do it at my place."
            harmony.say "Urgh..."
            harmony.say "We can fuck at your place anytime, [hero.name]."
            harmony.say "I can't believe you're so boring!"
            hide harmony with moveoutleft
            "With that, Harmony turns around and walks off."
            "And I hurry after her, still trying to talk her around."
            $ game.active_date.score -= 20
    $ game.pass_time(1)
    return

label harmony_preg_talk:
    $ harmony.flags.toldpreg = True
    show harmony sad
    "Harmony isn't exactly one of those girls that's good at keeping her emotions under wraps."
    "If she has something on her mind, good or bad, then it tends to be pretty easy to spot."
    "It's either written all over her face or else it's totally taking over her thoughts."
    "So I can usually see when there's something that we need to sit down and discuss."
    "And when she's showing those signs today, I decide to take the initiative."
    mike.say "Hey, Harmony..."
    show fx question
    harmony.say "Hmm..."
    hide fx
    show harmony normal
    harmony.say "Oh...oh, yeah, [hero.name]!"
    harmony.say "Sorry, I was miles away!"
    mike.say "I can see that, Harmony!"
    mike.say "What's on your mind?"
    mike.say "Is there something we should talk about?"
    show harmony sad
    "The moment I suggest that we talk, Harmony's reaction is plain to see."
    "Her cheeks flush red and she tries to keep from looking me in the eye."
    harmony.say "H...how did you know?"
    harmony.say "Oh dear..."
    harmony.say "I thought I was being all secretive and sly too!"
    "I chuckle and shake my head."
    "Harmony can be so cute and endearing sometimes."
    mike.say "Just a hunch, I guess!"
    mike.say "So..."
    mike.say "What was it that you needed to talk about?"
    "Harmony takes a deep breath, preparing herself for the task ahead."
    "Then she finally turns and looks me straight in the eye."
    harmony.say "I'm afraid I have some bad news, [hero.name]."
    harmony.say "We seem to have had a little...accident!"
    mike.say "Harmony..."
    mike.say "You don't mean..."
    "Harmony lets out a sigh."
    harmony.say "Yes, I do."
    harmony.say "I took a test this morning - and it was positive."
    harmony.say "We're pregnant!"
    "I feel like my eyes are going to pop right out of their sockets."
    "A moment ago I was being all smug and superior as I quizzed Harmony."
    "But now it's my turn to be the one that looks shocked."
    mike.say "You're sure?!?"
    mike.say "You did the test right?!?"
    mike.say "Those things can be tricky, you know!"
    show harmony annoyed
    "Harmony frowns at this and pouts a little."
    harmony.say "Of course I'm sure, [hero.name]!"
    harmony.say "I wouldn't joke about something this serious."
    show harmony sad
    harmony.say "Now what are we going to do about it?!?"
    menu:
        "We should keep it":
            "I feel like someone just sucker-punched me - right in the gut!"
            "But Harmony's right, we need to focus and make a decision here."
            "And there's only one honest answer that I can give her."
            mike.say "We have to keep it, Harmony."
            mike.say "We can't end the life of a child we made together!"
            if "religious" in harmony.traits:
                show harmony happy
                $ harmony.love += 10
                "Harmony instantly clasps her hands together like she's praying."
                "They make a clapping sound, and I jump with surprise."
                harmony.say "Praise the Lord!"
                harmony.say "I KNEW you were a good man, [hero.name]!"
                harmony.say "A righteous man with the Holy Spirit in him!"
                hide harmony
                show harmony close happy
                with hpunch
                "Harmony parts her hands and literally pounces on me."
                "She pulls me into an embrace and squeezes me like a boa constrictor!"
                mike.say "H...Harmony..."
                mike.say "I...can't...breathe!"
                show harmony close normal
                harmony.say "Oh...oh dear!"
                hide harmony
                show harmony
                "She releases me and I gasp for breath."
                harmony.say "I'm sorry, [hero.name]."
                show harmony happy
                harmony.say "I'm just so happy that we're going to be a family!"
                harmony.say "Now we can get married, settle down and plan the rest of our lives together!"
                mike.say "Ah...yeah, Harmony..."
                mike.say "That sounds...perfect!"
            elif "slutty" in harmony.traits:
                "Harmony takes a deep breath, and then lets it out as a weary sigh."
                "She nods her head with a grim smile on her face."
                $ harmony.love -= 10
                $ harmony.sub -= 5
                harmony.say "Ah shit..."
                harmony.say "I was kind of hoping you'd say the opposite of that!"
                harmony.say "But if that's what you really want..."
                mike.say "It is, Harmony."
                mike.say "I think we can make a success of this, if we work together."
                "Harmony snorts, beginning to pout a little."
                harmony.say "Well okay then..."
                show harmony annoyed
                harmony.say "But you've got to promise me we'll still have fun!"
                harmony.say "I spent WAY too long fixated on Jesus before I met you."
                harmony.say "If we keep the kid, you'd better not stop doing me, okay?"
                mike.say "Okay, Harmony."
                mike.say "It's a deal."
            else:
                show harmony normal
                "Harmony takes a deep breath, and then lets it out as a weary sigh."
                "She nods her head with a grim smile on her face."
                harmony.say "I didn't know which way you'd go on this one, [hero.name]."
                harmony.say "So I thought that I'd just leave it to chance and go with your choice."
                harmony.say "Okay...I guess this means I'm going to have to grow-up!"
                show harmony annoyed
                "Harmony looks me straight in the eye."
                harmony.say "But the same goes for you too, mister!"
                harmony.say "If we do this, we do it together, you got that?"
                "I nod, still a little surprised at Harmony's intensity."
                mike.say "Of course, Harmony!"
                mike.say "You and me against the world!"
                show harmony happy
                "Harmony smiles at this."
                show harmony normal close
                "Then she throws her arms around me."
                harmony.say "I can do this, [hero.name]."
                harmony.say "So long as I have you, I know I can!"
        "You should have a termination":
            "I feel like someone just sucker-punched me - right in the gut!"
            "But Harmony's right, we need to focus and make a decision here."
            "And there's only one honest answer that I can give her."
            mike.say "We can't keep it, Harmony."
            mike.say "Having a kid by accident is a terrible idea."
            mike.say "I think we need to get a termination."
            if "religious" in harmony.traits:
                show harmony angry
                $ harmony.love -= 100
                "The moment the words leave my mouth, Harmony gasps in horror."
                "It's like she's seeing me as I really am for the very first time."
                "And she's just realised that all this time I've been a hideous monster!"
                harmony.say "Oh no..."
                harmony.say "Oh no, no, no!"
                harmony.say "God save me and saints preserve me!"
                harmony.say "I had no idea I was in a relationship with a child murderer!"
                show harmony annoyed
                "Harmony's already starting to back away from me."
                "I make to reach out for her, trying to explain myself."
                mike.say "Harmony, please!"
                mike.say "Don't you think you're overreacting?"
                "But it's no good, as she leaps backwards to escape."
                show harmony angry
                harmony.say "Don't touch me!"
                harmony.say "I see it now!"
                harmony.say "You have the devil in you!"
                harmony.say "You want to tempt me into sin - to lure me down to hell!"
                harmony.say "But I won't let you, and I'll raise my child in the light of god!"
                hide harmony with dissolve
                "Before I can say another word, Harmony turns and runs away."
                "And as I watch her go, I get the feeling things just came to an end between us."
                $ harmony.set_gone_forever()
            elif "slutty" in harmony.traits:
                show harmony happy
                $ harmony.love += 10
                $ harmony.sub += 5
                harmony.say "Geez, [hero.name]!"
                harmony.say "Am I ever glad to hear that!"
                show harmony normal
                harmony.say "I thought you were gonna want to keep the kid!"
                "I feel an initial wave of relief that Harmony and I are of one mind."
                "But then I ponder the speed with which she seems to be getting over it."
                mike.say "You don't like the idea of being a mom, Harmony?"
                mike.say "Starting a family doesn't appeal - even in the future?"
                show harmony happy
                "Harmony snorts with laughter and shakes her head."
                harmony.say "Nah!"
                show harmony normal
                harmony.say "I used to be into all that stuff."
                harmony.say "You know, back when my head was full of religious crap?"
                harmony.say "But now I'm having too much fun to want to stop and settle down!"
                "I nod, trying to tell myself that's the answer I wanted to hear."
                "Because I feel that way too - I think..."
                $ harmony.unpreg()
            else:
                "Harmony takes a deep breath, and then lets it out as a weary sigh."
                "She nods her head with a grim smile on her face."
                if harmony.love >= 150:
                    harmony.say "You're right, [hero.name], we can't raise a kid together."
                    harmony.say "At least not now - we're not ready for that."
                    harmony.say "I knew that was the only answer."
                    show harmony normal
                    harmony.say "I guess I just needed to hear you say it too."
                    hide harmony
                    show harmony close
                    "Harmony leans against me, her head on my shoulder."
                    "We hold each other in silence for a good long while."
                    "Each of us is lost in our own thoughts."
                    "But we both know that we're making the right choice."
                    "Because it's the only choice that makes sense."
                    "Though that doesn't mean that we have to like it."
                    $ harmony.unpreg()
                else:
                    harmony.say "I knew you were going to say that."
                    harmony.say "You're not ready to be a father yet."
                    harmony.say "I respect that, [hero.name]."
                    harmony.say "But I'm not going to terminate my own child."
                    show harmony normal
                    "Harmony smiles, but it's a weak and tired one."
                    harmony.say "So I'm going to go it alone on this one."
                    mike.say "Harmony..."
                    mike.say "You don't have to..."
                    show harmony sad
                    harmony.say "Yes, [hero.name], I do!"
                    harmony.say "Maybe we can try again when you're in a different place."
                    harmony.say "But for now, I guess this is goodbye!"
                    "Harmony plants a kiss on my cheek."
                    hide harmony with dissolve
                    "Then she waves and walks away."
                    "Which leaves me standing alone and feeling like I've been slapped in the face."
                    $ harmony.set_gone_forever()
    return

label harmony_male_ending:

    if renpy.has_label("harmony_achievement_3") and not game.flags.cheat:
        call harmony_achievement_3 from _call_harmony_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    if "religious" in harmony.traits:
        "I can't remember the last time I saw the chapel this full of people and buzzing with anticipation."
        "The whole place is decked out with flowers and everyone seems to have made an effort to dress well."
        "And I can practically feel the warmth of the affection that the guests are feeling right now."
        "All of that positive emotion is directed at Harmony and myself, which is pretty hard to believe!"
        "I thought I was the only person close to bursting at the prospect of marrying the love of my life."
        "But a quick glance around the chapel proves that everyone here is delighted at the match too."
        "I can see my own family and friends out there, which is reassuring."
        "But I think they're outnumbered almost two-to-one by Harmony's portion of the guests."
        "There's her family, to whom I've already been introduced."
        "And I think I recognise a few of her friends out there too."
        "As well as a large number of faces from the congregation of the church we both attend too!"
        "It makes my heart swell to think of how loved Harmony is."
        "And that's the girl I'm getting to marry!"
        "I'm so wrapped up in thinking about Harmony that I almost don't notice the music."
        "The graceful, traditional music that she chose to come down the aisle fills the chapel."
        "And as everyone stands for the bride's entrance, I finally snap back to reality."
        "But a moment later, it feels like a dream all over again."
        show harmony happy wedding at center, zoomAt(1.0, (640, 730)) with dissolve
        "And that's because Harmony sweeps into the chapel looking like a dream come true!"
        "Her dress is, of course, all white - symbolising her virtue and purity."
        "But it's her face that captures my attention and makes me yearn for her."
        show harmony happy wedding at center, traveling(1.5, 5.0, (640, 1040))
        "Harmony looks positively radiant as she walks down the aisle."
        "And from the very moment she comes into view, she only has eyes for me."
        "With every step she takes towards me, I'm more convinced this is meant to be."
        "The smile on her face and the love that I see in her eyes almost entrance me."
        "And I actually have to reach into my trouser pocket and pinch myself."
        show wedding harmony with fade
        "Just so that, when she arrives at my side, I truly believe all of this is real!"
        "Priest" "Ahem..."
        show wedding harmony priest with dissolve
        "At the sound of the priest's cough, Harmony and I snap to attention."
        "We've rehearsed this moment so many times, until we had everything perfected."
        "So neither of us has to worry about missing a single cue."
        "Priest" "Dearly beloved..."
        "Priest" "We are gathered here today..."
        "Priest" "To join these two people in the bonds of holy matrimony."
        "Of course, Harmony insisted on the most traditional version of the ceremony possible."
        "Which means that there are long readings from the bible by various people."
        "More than a few hymns that everyone in the chapel mumble or wail through."
        "And lots of florid language as the priest goes through the motions."
        "But the important part of the ceremony is still the same."
        "Priest" "Do you, Harmony, take this man..."
        "Priest" "To be your lawful, wedded husband?"
        "Priest" "Do you promise to love, honour and obey him?"
        harmony.say "I do."
        "Priest" "And do you, [hero.name], take this woman..."
        "Priest" "To be your lawful, wedded wife?"
        "Priest" "Do you promise to love, honour and obey her?"
        mike.say "I do."
        "Priest" "Very good."
        "Priest" "I call upon those here present..."
        "Priest" "That if anyone knows of a lawful reason these two may not be married..."
        "Priest" "Speak now, or forever hold your peace!"
        "Of course this is one of those moments where everyone shares a wry laugh."
        "And nobody would ever actually think of standing up and saying a single word."
        "But then who could find a single blemish on Harmony's reputation?"
        "With me there might be some niggles from the past."
        "But not her - she's practically an angel in human form!"
        "Priest" "Very good."
        "Priest" "Then it is my great pleasure to pronounce you husband and wife."
        "Priest" "You may kiss the bride!"
        scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
        show harmony kiss wedding
        with fade
        $ harmony.flags.kiss += 1
        "Harmony and I do as we're told, lips touching a moment later."
        "I fully expect this to be a pretty chaste affair."
        "But Harmony catches me off-guard when she slips her tongue between my lips!"
        "I melt into the kiss on pure instinct alone, enjoying every moment."
        "Yet in the back of my mind I can't help wondering what this means."
        "Is there a new side to Harmony stirring now that we're officially married?"
        "After all, she did hint to me that we can do fun stuff in our marital bed without fear of censure!"
        "Maybe I'm about to be treated to a wedding night that'll set the tone for the future..."
        show harmony ending church with fade
        harmony.say "Hmm...I'm not sure that this is going to work for me."
        harmony.say "You see I'm a very traditional kind of girl - I like to think that I know my place."
        harmony.say "[hero.name] is usually the one that handles this kind of thing for the both of us."
        harmony.say "But I suppose this IS kind of important, and he can get in a bit of a muddle sometimes..."
        harmony.say "Okay, okay...fine, I'll share my thoughts on the two of us and how all of this played out."
        harmony.say "But you'd better not take anything I say out of context, you promise?"
        harmony.say "Okay, here goes..."
        harmony.say "For the longest time I only thought there'd ever be one true love in my life."
        harmony.say "And, of course, that was my love for god!"
        harmony.say "My faith has always been important to me, a guiding light in the darkness."
        harmony.say "And so when [hero.name] turned up at church one Sunday, I accepted him without question."
        harmony.say "To me he was just another poor lost lamb, needing to be guided back to the flock."
        harmony.say "But I soon began to notice that he was becoming much more to me than that."
        harmony.say "I found myself thinking about him all the time, finding excuses to be with him."
        harmony.say "Before too long I was thinking of us as good friends, you know?"
        harmony.say "But it didn't stop there - and soon he was on my mind all the time."
        harmony.say "In fact, I was finding it hard to think about anything else!"
        harmony.say "Even finding the time to pray or study the bible was almost impossible."
        harmony.say "That's then it started to get hard for me."
        harmony.say "I was finding myself drawn towards [hero.name]."
        harmony.say "But he was also distracting me from my faith!"
        harmony.say "So I came to the only logical conclusion possible."
        harmony.say "That he'd been sent by the devil to tempt me!"
        harmony.say "Every time I felt a sinful desire rise up in me for [hero.name], I fought it."
        harmony.say "I couldn't refuse to see him, as that would have been less than Christian of me."
        harmony.say "So I soldiered on, using my faith as a shield against temptation."
        harmony.say "All the time I was expecting [hero.name] to test my resolve."
        harmony.say "I thought that he would try his best to lure me into sin!"
        harmony.say "But, much to my surprise, he did nothing of the sort."
        harmony.say "I mean, he's only human - and a man on top of that!"
        harmony.say "There were times when it was obvious that he found me attractive."
        harmony.say "But somehow he was able to control himself and respect my boundaries."
        harmony.say "Which only served to make me that much more confused."
        harmony.say "If he was supposed to be a tool of the devil, then why was he holding back?"
        harmony.say "Why did he seem willing to respect me and still keep wanting to see me?"
        harmony.say "Then one day it struck me that I was wrong."
        harmony.say "[hero.name] hadn't been sent by the devil to tempt me."
        harmony.say "He had instead been sent by god to test my faith."
        harmony.say "God had sent me a good, loving man that would respect me."
        harmony.say "I was the one that was being tested, to see if I was worthy of him!"
        harmony.say "All my life I had believed that I was a good, Christian woman."
        harmony.say "And now I would have to prove it."
        harmony.say "I would have to prove that I could win this man's love."
        harmony.say "And I would have to do it without resorting to offering him my body."
        harmony.say "It was hard at times, almost too much for me to bear."
        harmony.say "But when he got down on one knee and asked me to marry him..."
        harmony.say "Well, I knew that I had passed the test!"
        harmony.say "And after that...well, everything was like a fairy-tale!"
        harmony.say "[hero.name] and I are all settled down in a little house all of our own."
        harmony.say "He's still working hard at the office every day to pay the bills."
        harmony.say "But I'm working on getting him to give it up and do something more useful with his life."
        harmony.say "You know, like become a pastor in his own right, or even a missionary!"
        harmony.say "And let's just say that I haven't stinted on my duties as a wife either."
        harmony.say "I might have made him restrain his more animal instincts before we married."
        harmony.say "But such things are practically encouraged within the bonds of wedlock!"
        harmony.say "And he's shown me such amazing things - I almost feel like I was missing out before!"
        if not harmony.is_visibly_pregnant or harmony.flags.mikeBabies < 1:
            harmony.say "Oh, and that's another thing..."
            harmony.say "I don't know if [hero.name]'s noticed the fact my belly's getting rounder."
            harmony.say "It's growing a little more each day, so soon he'll know that we're going to be a family!"
            harmony.say "The doctor tells me it's going to be a boy."
            harmony.say "And I know [hero.name] will be delighted when I tell him!"
        harmony.say "So that's my story, all of it."
        harmony.say "I feel that I was rewarded for keeping my faith."
        harmony.say "I got everything that I wanted and more because I remained true."
        if not harmony.is_visibly_pregnant or harmony.flags.mikeBabies < 1:
            harmony.say "So now I'll do the same thing for [hero.name] and our son, when he comes along!"
        if renpy.has_label("harmony_achievement_6") and not game.flags.cheat:
            call harmony_achievement_6 from _call_harmony_achievement_6
    elif "slutty" in harmony.traits:
        "Part of me still can't believe that I'm actually standing at the altar."
        "And that I'm waiting for Harmony to come walking down the aisle."
        "Sure, some of that is the genuine amazement that I'm getting married."
        "But a lot of it has to do with the fact that we almost didn't pull it off!"
        "I know that a lot of girls have been planning their weddings since they were young."
        "But the one that Harmony had in mind couldn't have been a childhood vision."
        "And I think it was more a result of the new and liberated way she lives her life."
        "I don't want to go into details."
        "Let's just say that Harmony wanted to make things pretty outrageous!"
        "Luckily for me, I managed to talk her down on most of it."
        "And by the time things were decided, she compromised."
        "So today we're getting married in a chapel, rather than desecrating one!"
        "A quick glance at the assembled guests lets me know what most of them are here."
        "My side of the chapel is almost full of family and friends."
        "But a glance over to Harmony's side tells a very different story."
        "There are far fewer people sitting there, the pews almost half empty."
        "I guess that's a reflection of just how much Harmony's changed since I met her."
        "Back then she was a member of a church and had many friends there."
        "But since she started to leave all that behind, those people have abandoned her."
        "The mere thought of such things feels like a knife in my gut."
        "And I turn my gaze away from Harmony's side of the chapel."
        "I also make a silent vow to do all I can for my wife-to-be."
        "Those people might have turned their backs on her."
        "But I'll always be there to support her, no matter what!"
        "I'm making myself that promise when the chapel suddenly seems to come alive."
        "Music swells and the guests rise as one, looking back over their shoulders."
        "I'm looking in that direction too, straining to see the same thing."
        show harmony happy wedding with dissolve
        "And there's an appropriate sound of awe when Harmony finally makes her entrance."
        "I have no idea if it's on account of amazement or shock."
        "And that's because one of the things she wouldn't compromise on was the dress."
        "Harmony's wedding dress is daring beyond belief."
        "It shows off every curve and line of her body."
        "Somehow it manages to do all of this while still keeping her decent too!"
        "Another guy might have been shocked at the sight of her in it."
        "But not me - I'm just blown away by how gorgeous my bride looks in it!"
        if harmony.is_visibly_pregnant:
            "My smile becomes even wider when I see Harmony's growing belly."
            "The dress does little if nothing to hide the fact she's pregnant."
            "But then why should it?"
            "There's nothing for either of us to be ashamed about."
            "Our child was conceived out of love, and that's how they'll be raised too."
        else:
            "There's nothing wrong with petite, skinny women."
            "But once you've been with a girl as curvy as Harmony..."
            "Well, I wouldn't say you'd never go back!"
            "But you certainly never forget a girl built like her!"
        "Harmony's grinning by the time she makes it to the altar."
        "And she looks even better up close than she did coming down the aisle."
        hide harmony
        show harmony close wedding
        harmony.say "Well, [hero.name]..."
        harmony.say "How do you like the look of your future wife?"
        mike.say "Wow, Harmony...just, wow!"
        mike.say "You look so great!"
        show harmony close happy
        harmony.say "Thanks, [hero.name]!"
        harmony.say "I feel SO hot too!"
        show harmony close blush
        harmony.say "All these eyes on me - I'm getting SO horny!"
        "Priest" "Ahem..."
        show harmony close normal
        "Harmony and I both jump a little as the priest clears his throat."
        "I have no idea if he was listening in on what we were just saying."
        "But I can feel myself flushing a little all the same."
        "Thankfully he keeps up the pretence that he was just prompting us."
        "Priest" "Shall we begin?"
        "We both nod and try to look like we're ready to do this."
        "Priest" "Very good..."
        "Priest" "Dearly beloved..."
        "Priest" "We are gathered here today..."
        "Priest" "To join these two people in the bonds of holy matrimony."
        show harmony close happy
        "At the mention of the word 'bonds', Harmony lets out a giggle."
        "And she shoots me a lascivious glance that betrays what she's thinking."
        "I can't help smiling and shaking my head, even as I try to keep a straight face."
        show harmony close normal
        "The majority of the ceremony is just what you'd expect."
        "We insisted on it being stripped down to the bare minimum."
        "More on account of Harmony's falling out with religion than anything else."
        "And so it doesn't take long for us to get to the serious part."
        "Priest" "Do you, Harmony..."
        "Priest" "Take this man, [hero.name]..."
        "Priest" "To be your lawful, wedded husband?"
        show harmony close blush
        harmony.say "You bet I do!"
        "Priest" "Erm...yes, very good..."
        show harmony close normal
        "Priest" "And do you, [hero.name]..."
        "Priest" "Take this woman, Harmony..."
        "Priest" "To be your lawful, wedded wife?"
        mike.say "I do!"
        "Priest" "Then god help you!"
        mike.say "Huh?"
        show fx question
        harmony.say "What was that?"
        "Priest" "Oh...nothing...nothing at all!"
        hide fx
        "Priest" "Ahem..."
        "Priest" "Having made their vows before you all..."
        "Priest" "I am now compelled to ask that..."
        "Priest" "If anybody knows of a lawful reason..."
        "Priest" "That these two may not be joined in holy matrimony..."
        "Priest" "Speak now, or forever hold your peace!"
        "There's the usual pregnant pause as the priest looks around the chapel."
        "And of course everyone has a little chuckle as he pretends to wait it out."
        "But I can't help thinking that this is the moment when they might come for Harmony."
        "That the hardcore element of the church she used to attend could come storming in."
        "And then carry her off to be saved from a life of sin!"
        "Thankfully that doesn't happen, and the priest nods with satisfaction."
        "Priest" "Very good!"
        "Priest" "Then by the power vested in me..."
        "Priest" "I pronounce you husband and wife!"
        "Priest" "You may kiss the bride!"
        "I turn to do as he says, but Harmony beats me to it."
        hide harmony
        show harmony kiss wedding
        with vpunch
        $ harmony.flags.kiss += 1
        "She practically pounces on me the moment I turn to face her."
        "Harmony clamps her lips on mine, and her tongue snakes into my mouth."
        "I'm almost holding onto her so that I can keep on my feet right now!"
        "But it doesn't take me long to regain my senses."
        "And when I do, I return the kiss with almost as much passion."
        "Harmony feels so good in my arms, so warm and welcoming."
        "But the best thing is that I know this doesn't have to end."
        "That from this moment on, we have the rest of our lives to spend together."
        show harmony poledance sexynun with fade
        harmony.say "It's easy for you guys to ask me to do something like that."
        harmony.say "Just sit down and tell you all about [hero.name] and me."
        harmony.say "But you've got to look at it from my point of view, you know?"
        harmony.say "[hero.name] isn't like some random guy that I just met and dated."
        harmony.say "Before he came along, I was a totally different person."
        harmony.say "He changed my entire life - changed who I was!"
        harmony.say "What?"
        harmony.say "Oh...okay...I guess I could just explain how all that happened."
        harmony.say "But I don't agree that I'm overthinking it!"
        harmony.say "I think it's you guys that aren't getting it..."
        harmony.say "So yeah, back then I was totally wrapped up in religion."
        harmony.say "It was pretty much my entire social life and all I thought about."
        harmony.say "If it didn't have anything to do with god and Jesus, it wasn't for me."
        harmony.say "I'd hate to meet the me from back then - she was a really boring cow!"
        harmony.say "Always trying to be good, acting all meek and clutching her bible."
        harmony.say "Urgh...it makes me shudder to even think I was ever like that!"
        harmony.say "And, of course, when I first met [hero.name], it was all about god!"
        harmony.say "All I saw when I looked at him was another lost sheep to save."
        harmony.say "He wasn't passionate enough in his belief."
        harmony.say "He wasn't devoted enough to the man upstairs."
        harmony.say "So, like a true religious jerk, I decided that it was up to me to change him."
        harmony.say "It started out the usual way, being friendly yet condescending at the same time."
        harmony.say "Indulging his obvious interest in my feminine qualities."
        harmony.say "Oh yeah, don't think I didn't know I was a hot-looking girl!"
        harmony.say "And don't think that I was above using it to get my way back then either."
        harmony.say "I drew [hero.name] into my little religious web and started to work on him."
        harmony.say "I thought that it wouldn't take too long, that he'd be an easy target."
        harmony.say "But pretty soon I started to get confused, forgetting what I was doing and why."
        harmony.say "And do you know why that was?"
        harmony.say "Because [hero.name] started treating me nicely, showing interest in me."
        harmony.say "Not in the religious bullshit I was trying to sell him."
        harmony.say "And not in using me for his own gratification either."
        harmony.say "Just in being with me!"
        harmony.say "And yeah, I liked that."
        harmony.say "I liked it a lot!"
        harmony.say "Soon I was looking forward to our dates for their own sake."
        harmony.say "And...well...and then he introduced me to the physical side of things!"
        harmony.say "I'd always been told that indulging the pleasures of the flesh was wicked."
        harmony.say "That it could only lead down a path that ended with the flames of Hell!"
        harmony.say "But what I felt when we kissed, and when we made love..."
        harmony.say "I knew almost as soon as it happened that it could never be bad."
        harmony.say "And yeah, [hero.name] lit a fire inside of me."
        harmony.say "It's still burning right now - and I want to keep those flames alive!"
        if harmony.is_visibly_pregnant or harmony.flags.mikeBabies >= 1:
            harmony.say "And sure, we ended up getting pregnant."
            harmony.say "But we're both mature individuals, not dumb kids."
            harmony.say "And together we made the decision to start a family."
            harmony.say "Believe me, [hero.name]'s not the perfect dad!"
            harmony.say "But he's trying his best, and Jamie loves him for it."
        else:
            harmony.say "But for all that he liberated me from sexual oppression, we weren't dumb kids."
            harmony.say "We still played it safe and made sure that we didn't have any accidents."
            harmony.say "So now we're in a good position to think about starting a family of our own."
        harmony.say "[hero.name]'s doing great at his job and he has a perfect home-life too."
        harmony.say "And me?"
        harmony.say "Well...I always used to think that I'd end up becoming a nun."
        harmony.say "Can you believe that?"
        harmony.say "The truth is that I'm thinking of breaking into the adult film industry."
        harmony.say "Or maybe becoming a full-time pole-dancer!"
        harmony.say "Anything's possible when you're a modern, sexually liberated woman!"
    else:
        "It feels kind of weird to be back inside a chapel and waiting for Harmony to appear."
        "After all, we met in a church, back when she was a far more religious kind of person."
        "And since then she's left all that behind, becoming more worldly and open to new things."
        "That fact is reflected starkly in the face that I can see behind me, sitting in the pews."
        "Almost none of them are the people that we used to see at church on a Sunday."
        "But I guess that's more a reflection on them than it is on Harmony and me."
        "If her becoming less religious was a reason to stay away, then they can go to hell."
        "Because that means they were never friends with us for any other reason."
        "Instead I see that those pews are filled with our respective families."
        "Our real friends are there too, happy to bear witness to us tying the knot."
        "I turn back to the altar, and the priest smiles at me."
        "I smile back, relieved by the fact he's almost a complete stranger."
        "So there's no chance of him lecturing us about turning our backs on god!"
        "The priest opens his mouth, like he's about to say something."
        "But at that very moment, music fills the chapel."
        "As one, we all look to the back of the place."
        show harmony wedding with dissolve
        "And then Harmony sweeps in through the doors."
        "I barely notice the wave of admiring comments she receives from the guests."
        "And that's because I'm unable to do anything but stare at my bride as she approaches."
        "Harmony looks radiant, as beautiful as she's ever seemed to my eyes."
        "Her dress is perfect, making the most of her full figure too."
        "I swear that I can feel my heart swelling in my chest!"
        if harmony.is_visibly_pregnant:
            "I had worried that Harmony's belly might be obvious."
            "And now that I see her, you can't avoid spotting it."
            "But somehow it only serves to add to her beauty."
            "I know it's a cliche, but she really is glowing!"
        else:
            "I don't mind admitting that I see many guys checking her out."
            "And I can't blame them for having good taste!"
            "Plus more than a few skinny girls are looking pretty jealous too!"
            "After all, curves like Harmony's are something special."
        hide harmony
        show harmony close wedding
        with fade
        "When she finally reaches the altar, Harmony slyly grabs my hand."
        "She squeezes it, letting me know that she's as excited as I am."
        "But that's all we have time to do before the priest begins his duties."
        "Priest" "Dearly beloved..."
        "Priest" "We are gathered here today..."
        "Priest" "To join these two people in the bonds of holy matrimony."
        "Harmony wasn't bothered in the slightest about sticking to tradition."
        "So the version of the ceremony that we chose was a pretty stripped down affair."
        "We decided that only the essential elements really meant anything to us."
        "Which means that it doesn't take us long to get to the actual vows."
        "Priest" "Do you, Harmony, take this man..."
        "Priest" "To be your lawful, wedded husband?"
        show harmony close happy
        harmony.say "I do."
        "Priest" "And do you, [hero.name], take this woman..."
        "Priest" "To be your lawful, wedded wife?"
        mike.say "I do."
        "Priest" "Very good."
        show harmony close normal
        "Priest" "I call upon those here present..."
        "Priest" "That if anyone knows of a lawful reason these two may not be married..."
        "Priest" "Speak now, or forever hold your peace!"
        "Of course this is one of those moments where everyone shares a wry laugh."
        "And nobody would ever actually think of standing up and saying a single word."
        "But I'm still worried that some bible-thumping nutter is out there."
        "Just waiting to come in here and demand that Harmony come back to god!"
        "Priest" "Very good."
        "Priest" "Then it is my great pleasure to pronounce you husband and wife."
        "Priest" "You may kiss the bride!"
        hide harmony
        show harmony kiss wedding
        with fade
        $ harmony.flags.kiss += 1
        "Harmony and I do as we're told, lips touching a moment later."
        "I fully expect this to be a pretty chaste affair."
        "But Harmony catches me off-guard when she slips her tongue between my lips!"
        "I melt into the kiss on pure instinct alone, enjoying every moment."
        "We did it - we actually tied the knot!"
        "Now all we have to do is figure out what happens next..."
        show harmony ending beach with fade
        harmony.say "It's kind of ironic that you want me to do something like this."
        harmony.say "You know, talking all about [hero.name] and what he means to me?"
        harmony.say "Because before I met the guy, I'd never have been able to do it!"
        harmony.say "I mean, it's not like I was some kind of recluse or a crazy lock-in."
        harmony.say "But he was definitely instrumental in getting me to grow as a person."
        harmony.say "Before he came along, there was nothing but religion in my life."
        harmony.say "In fact, I can't remember a time before I was totally devoted to the church!"
        harmony.say "And I always thought that was the way it would be."
        harmony.say "I was happy too...or at least I thought that I was happy."
        harmony.say "When you're all wrapped up in something so tightly, it's strange."
        harmony.say "You're living inside of a bubble, you just don't know it."
        harmony.say "You can see what's going on outside of the bubble too."
        harmony.say "But the bubble distorts everything, twists it out of its true shape."
        harmony.say "Urgh...this is pretty hard for me to admit!"
        harmony.say "But yeah, I was one of those REALLY annoying religious types!"
        harmony.say "I thought that I had all the answers."
        harmony.say "That the only book I'd ever need was my bible."
        harmony.say "And when [hero.name] showed up at church, I saw a chance."
        harmony.say "To me he looked like someone that needed saving."
        harmony.say "What he needed was someone to show him the way to salvation."
        harmony.say "And, of course, I was sure that person was me!"
        harmony.say "Once I befriended him, I started with all the usual stuff."
        harmony.say "I invited him to study the bible with me."
        harmony.say "I took him along to church social events."
        harmony.say "And at first I was sure that it would only be a matter of time."
        harmony.say "I'd make a better Christian out of him, and prove myself into the bargain."
        harmony.say "But I was as arrogant as usual, so I missed two things."
        harmony.say "One was that he kept asking me questions that I couldn't answer."
        harmony.say "And he often left me questioning myself afterwards too."
        harmony.say "The second thing was that I liked him a lot more than I realised."
        harmony.say "Pretty soon I was more looking forward to seeing him than anything else."
        harmony.say "I almost forgot why we were meeting up in the first place."
        harmony.say "That was about the same time he started asking me out on dates."
        harmony.say "Of course he didn't call them that, and I didn't think of them as that."
        harmony.say "But it was a girl and a boy going places and doing things together."
        harmony.say "So what else could it have been?"
        harmony.say "I was intimidated to do so many things I'd been told were sinful."
        harmony.say "But [hero.name] did them and he was a good guy."
        harmony.say "So how could they be bad?"
        harmony.say "And I soon found out that they weren't bad - they were a lot of fun!"
        harmony.say "Soon enough I realised that I was forgetting all about god."
        harmony.say "When we were out together, [hero.name] was all I thought about."
        harmony.say "I didn't stop going to church or being spiritual."
        harmony.say "I just found something else I loved too."
        harmony.say "That was when I began to realise that things weren't as simple as I'd thought."
        harmony.say "Sometimes the words I read in my bible didn't help me to see things clearly at all."
        harmony.say "And sometimes they even sounded totally wrong!"
        harmony.say "In the past I'd have had a crisis of faith."
        harmony.say "But [hero.name] helped me to see things from another perspective."
        harmony.say "And yeah, let's address the elephant in the room!"
        harmony.say "It was a revelation to discover all the sex I'd been missing out on!"
        harmony.say "That was probably worth it all on it's own."
        if harmony.is_visibly_pregnant or harmony.flags.mikeBabies >= 1:
            harmony.say "And sure, we ended up getting pregnant."
            harmony.say "But we're both mature individuals, not dumb kids."
            harmony.say "And together we made the decision to start a family."
            harmony.say "Believe me, [hero.name]'s not the perfect dad!"
            harmony.say "But he's trying his best, and Jamie loves him for it."
        else:
            harmony.say "But for all that he liberated me from sexual oppression, we weren't dumb kids."
            harmony.say "We still played it safe and made sure that we didn't have any accidents."
            harmony.say "So now we're in a good position to think about starting a family of our own."
        harmony.say "[hero.name]'s career is going from strength to strength."
        harmony.say "And I'm working at a centre that helps out girls fleeing religious persecution."
        harmony.say "It's not the future that I saw for myself when I was a kid."
        harmony.say "But I finally feel like I'm actually doing something positive with my life."
        harmony.say "So yeah, I'm glad [hero.name] walked into the church on that fateful Sunday morning."
        harmony.say "But these days I'd rather Sunday morning in bed with him!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not harmony.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_10
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_10
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label harmony_kiss_me:
    call harmony_greet from _call_harmony_greet
    show harmony
    "Something's up with Harmony, I can sense it the moment that I set eyes on her."
    "She's not the best in the world at hiding her emotions at the best of times."
    "And now it's plain to see from her face that there's something pressing on her thoughts."
    "I try to give her the space that she needs to pluck up the courage and speak."
    "But instead of beginning to open up about what's bothering her, Harmony leans in closer to me."
    hide harmony
    show harmony kiss
    with fade
    $ harmony.flags.kiss += 1
    "Thinking that she wants to be hugged, I oblige and make to embrace her."
    "So it comes as no small surprise when she tilts her head and kisses me full on the lips."
    "I'm stunned for a few seconds, but then my instinct takes over and I return the kiss."
    "It's only later, after it's over, that I realise just how much so forward a gesture must have cost a girl as shy as Harmony..."
    hide harmony kiss with fade
    return

label harmony_stripclub_event_01:
    scene expression f"bg {game.room}"
    show harmony sad
    "Harmony's one of those girls that can't help giving away the fact she has something on her mind."
    "Like, she'll keep quiet about it, not mention a single word all the time she's around you."
    "But she'll be doing something that gives it away, humming a tune or curling hair around her finger."
    "And right now she's doing both, while totally ignoring me too!"
    mike.say "Harmony!"
    mike.say "Are you hearing me right now?"
    mike.say "Like have you gotten a single word I've said?!?"
    "At the raised and rather annoyed tone of my voice, Harmony snaps out of it."
    "She jumps a little and finally seems to become aware of my presence."
    show harmony normal
    harmony.say "Oh!"
    harmony.say "What?"
    harmony.say "What are you talking about?"
    harmony.say "Of course I'm listening to you!"
    "I could demand that Harmony repeat the last thing I told her."
    "But I can already feel my irritation draining away."
    "So instead I just shake my head and decide to be the bigger person."
    mike.say "You seem distracted, Harmony."
    mike.say "Is there something bothering you?"
    "Harmony wrings her hands and looks at the ground."
    "Then she looks back up at me, a serious expression on her face."
    harmony.say "Well, yeah..."
    harmony.say "There was something I wanted to ask you."
    show harmony happy
    harmony.say "I was looking for some career advice."
    "It's all that I can do to keep myself from laughing out loud."
    "Ever since she left the pious life behind, Harmony's been pretty much out of control."
    "It's like she's trying as best she can to make up for all the partying she missed out on."
    "So the idea of her wanting to devote time to furthering her career is kind of hard to believe."
    mike.say "Erm..."
    mike.say "Okay, Harmony..."
    mike.say "Exactly what kind of advice were you wanting?"
    show harmony normal
    "Harmony's face becomes serious as she explains herself."
    harmony.say "Okay, hear me out..."
    harmony.say "You think I'm pretty, right?"
    harmony.say "That I have a sexy body?"
    "I begin to nod my head instantly."
    "How could I not?"
    "Harmony's easily one of the most beautiful girls I've ever met."
    "And her body is composed almost entirely of perfect curves."
    "She's like the total package!"
    mike.say "Of course I do, Harmony!"
    mike.say "You're a goddess!"
    "Harmony blushes a little at the compliment."
    "And I can see that familiar amorous glint creeping into her eyes too!"
    harmony.say "Aw!"
    show harmony blush
    harmony.say "Thank you, [hero.name]!"
    show harmony normal
    harmony.say "So you think I should try out to become a stripper, right?"
    "At the mere mention of the word stripper, my eyes almost pop out of their sockets."
    "Where in the hell did that come from?"
    mike.say "What do you mean, stripper?"
    mike.say "Since when do you want to become a stripper?!?"
    mike.say "Nobody told me that you were going to be a stripper!"
    "Harmony looks more than a little surprised by my reaction."
    harmony.say "Huh?"
    show harmony sad
    harmony.say "You're always telling me I look great, [hero.name]."
    harmony.say "And you like looking at me naked every chance you get too!"
    show harmony normal
    harmony.say "Are you jealous at the idea of other guys seeing me naked aside from you?!?"
    menu:
        "That's a great idea!":
            "I shake my head as soon as Harmony gets through saying all of this."
            "Because I know that I can handle other guys seeing her naked body."
            "Especially if it means I get to see it gyrating on a stage too!"
            mike.say "Of course not, Harmony!"
            mike.say "I'm a thoroughly modern kind of guy."
            mike.say "And I've got no issue with stripping as a profession."
            mike.say "In fact, I'm more than happy to give you my blessing."
            "At first Harmony looks more surprised than anything else."
            "Like she really doesn't know how to react."
            "I guess she was preparing herself for me saying no."
            "But then she smiles again."
            show harmony happy
            harmony.say "You really mean that, [hero.name]?"
            harmony.say "You're okay with dating a stripper?"
            mike.say "Harmony, I'm more than okay with it."
            mike.say "I think it's a really hot idea!"
            "Now I can see Harmony beginning to bite her lip and blush."
            "All things that she does when she's getting turned-on."
            harmony.say "Oh, [hero.name]!"
            harmony.say "You're such a great guy!"
            show harmony blush
            harmony.say "Maybe you'd like to have a preview of my act?"
            $ harmony.purity.min = 0
            $ harmony.purity -= 1
        "I'm not sure...":
            "I shake my head as soon as Harmony gets through saying all of this."
            "She's one hundred percent correct of course."
            "The last thing that I want is have other guys ogling her naked body."
            "But that doesn't mean I have to admit as much."
            mike.say "Of course not, Harmony!"
            mike.say "I'm a thoroughly modern kind of guy."
            mike.say "And I've got no issue with stripping as a profession."
            mike.say "I just think you should be aiming higher, that's all."
            "Harmony frowns, looking less than convinced."
            show harmony annoyed
            harmony.say "Humph..."
            harmony.say "How can I aim higher?"
            harmony.say "Especially when I still want to take my clothes off!"
            "I force a smile onto my face as I rack my brains."
            "And then an idea pops into my head."
            "I don't know if it's a very good one or not."
            "But I don't have time to test it out."
            mike.say "You could..."
            mike.say "Become a life model?"
            mike.say "Yeah, that's it - become a life model!"
            mike.say "They take off all their clothes when they pose for artists!"
            harmony.say "Really, [hero.name]?"
            show harmony angry
            harmony.say "That doesn't sound as much fun as stripping!"
            mike.say "Maybe it's not as lucrative, Harmony."
            mike.say "But it's got much more artistic credibility."
            show harmony normal
            harmony.say "Are you really sure?"
            "I breathe a sigh of relief as we begin to debate the matter."
            "Sure, I might not want Harmony to be a life model either."
            "But that's not the point."
            "Taking her mind off being a stripper's the point."
            "At least I've bought myself some time."
            "Now all I have to do is come up with a better plan."
            $ harmony.love += 2
    return

label harmony_stripclub_event_02:
    scene bg stripclub
    "I can't help feeling more than a little smug as I walk up to the door of the strip club and step inside."
    "I mean, most guys are always sneaking into these places and hoping that their girlfriends won't find out."
    "But here I am, actually strolling in to see if my girlfriend took my advice and got herself a job here."
    "If she did, then I'm obviously here to support her."
    "And if not, then I can say I was only here to see if she had."
    "Either way, I get to sit back and watch some hot acts shaking their stuff in front of me."
    "Sometimes it's good to be me!"
    "Grabbing myself a drink from the bar, I sit as close to the pole as possible."
    "And then I settle in to wait for Harmony to make an appearance."
    "But there's nothing to stop me from appreciating the other acts on before her."
    "From a purely artistic point of view, you understand!"
    "At first I feel like the king of the world as I'm sitting there."
    if shiori.flags.schedule == "stripclub":
        show poledance shiori
    "One girl after another takes to the stage."
    scene bg stripclub
    if hanna.flags.schedule == "stripclub":
        show poledance hanna
    "And I watch as they wrap themselves around the pole before me."
    scene bg stripclub with fade
    "But none of them are Harmony, and so I find myself getting a little frustrated."
    "The drinks here are expensive, draining me of funds at a rapid rate."
    "And I'm worried that if Harmony does come on stage, I'll be totally spent by then!"
    "Taking a swig of what feels like my hundredth drink, I let out a tired sigh."
    "And it's then that I hear the sound of someone giggling close by."
    "In fact, it's a giggle so familiar that I'm sure I know who it belongs to!"
    "Looking up, I see Harmony smiling down at me from above."
    show harmony happy stripper with dissolve
    harmony.say "Hey, [hero.name]!"
    harmony.say "You came to see me dance!"
    harmony.say "That's so sweet of you!"
    mike.say "H...Harmony..."
    mike.say "Wow..."
    mike.say "Is that really you?!?"
    "Harmony towers over me, her spectacular figure on show."
    "She's wearing a tiny skirt and a bra covered in shimmering pink sequins."
    "I can see the strings of a thong emerging from the top of the skirt."
    "And below it, her shapely legs are clad in fishnet stockings."
    "Severe heels finish of the outfit, making Harmony see taller than usual too."
    harmony.say "Oh yeah, [hero.name]."
    show harmony blush
    harmony.say "You're not dreaming."
    harmony.say "It's me alright."
    harmony.say "But I am your dream come true!"
    "With that, Harmony twirls on the spot and grabs hold of the pole."
    hide harmony
    show poledance harmony stripper
    with fade
    "She moves with amazing speed and grace, even on such high heels."
    "And within moments she's making use of the pole to get herself off the ground."
    "My eyes are fixed on Harmony with no possibility of tearing them away even for a second."
    "I have no idea if she's ever done this before."
    "But she looks like a pro to me as she goes to work."
    "The first thing to go is her skirt."
    "Harmony eases it down over her curving ass."
    "Then she shimmies it along her thighs until it drops to the ground."
    "Neatly stepping out of it, she begins to make more use of her legs."
    "Bending and stretching shows off the thong she's wearing."
    "But everyone in there is more interested in her ass."
    "It sways and bounces as she moves, hypnotic in its motions."
    "In fact, I'm so engrossed in watching it that I almost miss what she takes off next."
    "Which would have been a real shame, as Harmony reaches behind her back to unhook her bra!"
    "There's an audible gasp of appreciation from the audience as she does this."
    "And a second when those heavy, full and gorgeous breasts are set free."
    "Now Harmony begins to dance in a manner that makes the most of them."
    "They swing and sway as she moves, leaving me breathless from their motion."
    "Finally she pauses to peel off her stockings and panties."
    show poledance harmony naked
    "Harmony doesn't make the mistake of flaunting what's now revealed."
    "Instead she keeps on moving, making the audience work for it."
    "I have to watch her the whole time to even catch a glimpse."
    "And every time I catch sight of her pussy, it's for a brief second."
    "But even so, it makes my heart beat ever faster."
    "All too soon it seems that the dance is over."
    "Harmony stoops to pick up her things."
    "Then she turns, blows a kiss to the audience and disappears backstage."
    scene bg stripclub with fade
    "I'm left sitting there, trying to catch my breath and get my head in order."
    "I order another drink in the hope of it helping."
    "But I'm still pretty much out of it when Harmony sits down next to me."
    show harmony normal stripper
    harmony.say "Well, [hero.name]..."
    harmony.say "What do you think?"
    show harmony happy
    harmony.say "Did you like the dance?"
    "I shake my head and let out a gasp."
    mike.say "It was..."
    mike.say "It was amazing, Harmony!"
    mike.say "You totally blew me away!"
    "Harmony's face lights up at the praise."
    "And she leans in closer."
    "At the same time, I feel her hand on my lap."
    harmony.say "I'll let you into a little secret, [hero.name]."
    show harmony blush
    harmony.say "All the time I was up there on the stage..."
    harmony.say "I was thinking about you!"
    "Harmony underlines her point by squeezing my cock - pretty hard too!"
    "I gasp at the sensation, but that doesn't seem to do anything to make her stop."
    harmony.say "Mmm..."
    harmony.say "You're still nice and hard!"
    harmony.say "Now I know that you liked it!"
    "I nod desperately, hoping that it might make her let go."
    harmony.say "Don't worry, [hero.name]."
    show harmony blush
    harmony.say "I'll give you an encore performance."
    harmony.say "Just as soon as you take me home!"
    $ harmony.purity -= 2
    $ harmony.love += 2
    $ harmony.flags.schedule = "stripclub"
    return

label harmony_birthday_date_male:
    $ DONE["harmony_birthday_date_male"] = game.days_played
    if "slutty" in harmony.traits:
        call harmony_birthday_date_impure_male from _call_harmony_birthday_date_impure_male
    else:
        call harmony_birthday_date_pure_male from _call_harmony_birthday_date_pure_male
    return

label harmony_birthday_date_pure_male:
    $ game.active_date.clothes = "date"
    show harmony date happy
    "Harmony has a pretty big smile on her face as she greets me."
    "But when she see's the look on mine, that changes rather quickly."
    show harmony normal
    harmony.say "Hello, [hero.name]..."
    show fx question
    harmony.say "Is everything okay?"
    show harmony embarrassed
    harmony.say "I'm not late, am I?"
    hide fx
    harmony.say "The thing is, I sort of got dragged into helping out around the church."
    harmony.say "You know me, I just can't say no to this place!"
    menu:
        "Tell her she's in time":
            mike.say "Oh no, Harmony..."
            mike.say "Don't worry about it."
            mike.say "The time I told you was more of a rough estimate anyway."
            show harmony normal
            "Harmony nods and smiles as she hears this."
            "Then she reaches out her hand for me to take it."
            $ game.active_date.score += 15
            harmony.say "Oh good!"
            harmony.say "So shall we get going?"
            harmony.say "I'm so excited to see where you're taking me!"
            "Okay, okay...I know that lying's not exactly cool."
            "But it was just one of those little white lies."
            "And what's the problem if the result is that it makes Harmony happy?"
            "The reality is that we are going to be running a little later than planned."
            "But I'm sure that I can hustle her along as we make our way there."
            "And I can probably cover up the need to hurry with upbeat enthusiasm."
            "What Harmony doesn't know won't hurt her either."
        "Tell her she's a little late":
            mike.say "Well..."
            mike.say "Yeah, Harmony..."
            mike.say "You are actually a little late!"
            show harmony sad
            "As soon as the words leave my mouth, Harmony begins to blush."
            "She holds a hand up to her mouth and gasps in evident distress."
            harmony.say "Oh no!"
            harmony.say "Oh, I'm so sorry!"
            $ game.active_date.score -= 10
            harmony.say "That was so thoughtless and selfish of me..."
            "I hate the sight of Harmony beating herself up over being late."
            "And it instantly makes me regret even bringing it up with her."
            mike.say "Let's just forget about it, okay?"
            mike.say "I'm sure we can still make it in time."
            mike.say "So long as we hurry, that is!"
            "Harmony nods as I reach out to take her hand."
            "And I hope that the matter's well on the way to being forgotten."
    scene bg door restaurant
    show harmony date embarrassed
    with fade
    "Luckily for us we make really good time in getting to our destination."
    "But as soon as we stop, I see Harmony looking a little nervous."
    "I glance from her to the door of the restaurant and back again."
    mike.say "Are you okay, Harmony?"
    mike.say "Don't you like the look of this restaurant?"
    mike.say "I thought a meal here would be really nice."
    "I can see that Harmony has her hands over her stomach."
    "Almost like she's trying to hide something from sight."
    harmony.say "Erm..."
    harmony.say "Y...yeah, [hero.name]..."
    harmony.say "I guess so..."
    "I rack my brain, trying to figure out what could be bothering Harmony."
    "Then I have a sudden surge of inspiration, and I'm sure I know what's the matter."
    if hero.charm >= 75:
        "It doesn't take a genius to figure out that Harmony's self-conscious."
        "But now I realise it's because of her full-figure."
        "And dumbass here went and brought her to a restaurant!"
        "I open my mouth to reassure Harmony that she doesn't look fat."
        "But then I stop myself, thinking that will only make matters worse."
        "So I need to come at this from a different angle."
        mike.say "I hope you don't mind me bringing you here, Harmony."
        mike.say "I'd have chosen somewhere smaller and more quiet."
        mike.say "But...I kind of wanted to be seen out with you!"
        show harmony surprised
        "Harmony's eyes go wide as she hears this."
        "Her cheeks flush red too."
        show harmony embarrassed
        harmony.say "Wh...what are you talking about?"
        mike.say "I know it's not very humble of me, Harmony."
        mike.say "I just wanted to show-off how beautiful you look."
        mike.say "Because I'm proud of you."
        show harmony normal
        "Harmony smiles and looks at the ground."
        harmony.say "Oh my..."
        $ game.active_date.score += 20
        harmony.say "Well, in that case, I think I can let you off!"
        harmony.say "But just this once - as pride is a sin!"
    else:
        mike.say "Look, Harmony..."
        mike.say "I know this place looks expensive."
        mike.say "But I've got the cash to cover the bill, okay?"
        show harmony sad
        show fx question
        "For a moment, Harmony looks confused."
        "It's almost like she doesn't know what I'm talking about."
        hide fx
        $ game.active_date.score -= 10
        "But then her expression changes, and she looks oddly disappointed."
        "Though she seems to smile all the same."
        harmony.say "If you say so, [hero.name]."
        harmony.say "I'm not feeling very hungry anyway."
        harmony.say "So I'll probably just have something light."
        harmony.say "Like a salad, you know?"
        "I shake my head, not understanding Harmony's concerns."
        mike.say "Whatever you say, Harmony."
        mike.say "Just let me know if you get your appetite back."
    scene bg restaurant
    show ryan at blacker, center
    with fade
    pause 0.1
    show harmony date at right with easeinright
    "I have a nervous moment as the waiter scans down the list in search of my name."
    "And I almost find myself holding my breath, expecting him to say it's not down there."
    "But then he looks up and gives me a well-practiced smile."
    "Waiter" "Here we are, sir..."
    "Waiter" "If you'd like to follow me?"
    show ryan at blacker, left
    show harmony date at center
    with ease
    "Harmony and I do just as he says, following him every step of the way."
    "The waiter leads us across the restaurant and straight to our table."
    "And then he gestures for us to take our seats."
    menu:
        "Help Harmony into her seat":
            "I don't hesitate to gesture towards the nearest seat."
            mike.say "Allow me to help you, Harmony..."
            "Sure, I'm feeling pretty hungry right now."
            "Probably from the nerves of organising all of this."
            "But that's no reason to let my manners slip."
            "And I know it was the right decision from Harmony's reaction too."
            show harmony happy
            $ game.active_date.score += 15
            "She practically beams as I help her into the seat."
            "Smiling up at me like the cat that got the cream."
            "As I turn around and get into my seat, I catch a glance of the waiter's expression."
            "And at first I can't figure out just why he looks so pissed all of a sudden."
            "Then it dawns on me - he must be used to guys not doing stuff like that."
            "I'll bet he was poised to leap in there and do the same thing for Harmony if I didn't!"
            "That makes me feel more than a little smug."
            "Not only because I remembered to do the right thing."
            "But also as I managed to deny the waiter his chance to be an unctuous creep as well!"
        "Sit straight down in your seat":
            "I don't hesitate to sit down in the seat nearest to me."
            "I'm getting hungrier by the moment, probably from the nerves."
            "And so I don't want anything to get between me and the menu!"
            show harmony annoyed
            $ game.active_date.score -= 10
            "It's only when I look up again that I see Harmony staring at me."
            "Then I realise that the waiter is doing the same thing too."
            "What's the matter with them?"
            "Do I have something stuck between my teeth or something?"
            "Waiter" "Excuse me, madam..."
            "Waiter" "Would you like a little help there?"
            harmony.say "Oh!"
            harmony.say "Why yes, that would be very kind of you."
            "The waiter nods as he helps Harmony into her seat."
            "And as she sits down, I get a look that could kill from her."
            "Turning my gaze to the waiter, I get a more smug one from him."
            "It's then that I realise the proper thing to do would have been to do that myself."
            "Or at least it would have been the gentlemanly thing to do."
            "I guess I need to brush up on my etiquette!"
    show restaurant meal harmony date nomeals
    show restaurant_meal_waiter_pose01 as waiter zorder 1 at top_mostleft
    "As soon as we're settled into our seats, the waiter hands us each a menu."
    hide restaurant_meal_waiter_pose01 as waiter zorder 1 at top_mostleft with easeoutleft
    "I don't waste any time in starting to scan what's on offer."
    "And as soon as I see something that I like, my mind's made up."
    "I'm about to announce what I'll be ordering tonight."
    "But then I look up and see Harmony still studying her own menu."
    mike.say "Is everything okay, Harmony?"
    if hero.has_skill("foodie"):
        "At the sound of my voice, Harmony looks up."
        harmony.say "Oh..."
        harmony.say "I was just a little confused..."
        harmony.say "All of these dishes look so complicated."
        harmony.say "I don't think I know what anything actually is!"
        harmony.say "And I wanted to order something...well, something light."
        harmony.say "If you know what I mean?"
        "I nod as I take a second look at the menu."
        "I'm pretty confident that I'll be able to help Harmony out."
        "As I'm usually pretty knowledgeable when it comes to this kind of thing."
        "And it doesn't take me long to get my head around this one either."
        mike.say "No worries, Harmony..."
        mike.say "This thing reads like someone was making it extra-complicated on purpose."
        mike.say "But I don't think they're as clever as they think they are."
        mike.say "Because it's pretty simple once you know that."
        "I explain the dishes to Harmony."
        "Even pointing out the ones that are lower in calories too."
        "It's about then that I get the feeling we're being watched."
        "Waiter" "Ahem..."
        show restaurant_meal_waiter_pose01 as waiter zorder 1 at top_mostleft with easeinleft
        "Harmony and I look around as one to see the waiter leaning over us."
        "Waiter" "If there's a problem..."
        "Waiter" "Perhaps I could be of assistance?"
        mike.say "No need - we got this."
        "The waiter makes a sniffy sound in response."
        "And I get the impression he's pissed at not being able to step in and help."
        hide restaurant_meal_waiter_pose01 as waiter zorder 1 at top_mostleft with easeoutleft
        "Most likely he gets off on doing that for less well-informed diners."
        $ game.active_date.score += 15
        "But not in this case, as Harmony and I both confidently order what we want."
    else:
        "At the sound of my voice, Harmony looks up."
        harmony.say "Oh..."
        harmony.say "I was just wondering..."
        harmony.say "Why is so much of the menu in French?"
        harmony.say "Because I don't understand that language!"
        if hero.knowledge >= 75:
            "I smile and shake my head."
            mike.say "Don't worry, Harmony."
            mike.say "That's just something French people do to show-off."
            mike.say "I can speak the language pretty well."
            mike.say "Let me see that..."
            "I confidently take the menu from Harmony."
            "And then I proceed to reel off all the dishes in plain English."
            "The whole time I can see the waiter trying to conceal his annoyance."
            "I guess he was waiting for the chance to act all superior with us."
            "But now he's having to bite his tongue and keep quiet."
            $ game.active_date.score += 15
            harmony.say "Oh, thank you, [hero.name]..."
            harmony.say "That makes things so much easier!"
            harmony.say "I know what I want to order now."
            "Within a few short minutes, we've ordered our meals."
            "And the waiter stalks off towards the kitchen, leaving us in peace."
            "I guess he's pretty pissed-off at being denied the chance to gloat over us."
        else:
            "I take a quick glance down at the menu."
            "And I see that Harmony's right."
            "What I'm ordering just so happens not to be in French."
            "But almost everything else is literally written in a foreign language!"
            mike.say "Erm..."
            mike.say "Me neither, Harmony!"
            mike.say "I suppose you could always guess?"
            "That's pretty much the best answer I can come up with."
            "But it doesn't seem to go down too well with Harmony."
            $ game.active_date.score -= 10
            harmony.say "Oh never mind."
            harmony.say "I'll just ask the waiter..."
            "I open my mouth to say no, to beg her to stop."
            "But it's already too late."
            harmony.say "Excuse me..."
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at top_mostleft with easeinleft
            harmony.say "But we don't speak French!"
            "The moment the waiter hears this, a superior smile spreads across his face."
            "And for the space of the next few minutes I'm forced to sit, squirming in my seat."
            "Because of course he revels in the chance to look down his nose at the both of us."
            hide restaurant_meal_waiter_pose01 as waiter zorder 1 at top_mostleft with easeoutleft
            "After what feels like an eternity, we've actually managed to order our meals."
            "But the experience leaves us feeling about two feet tall."
    show restaurant meal harmony date -nomeals
    "Pretty soon our food arrives and we're digging into it."
    "And it doesn't take long to find out that it was worth the wait."
    "In fact, it's so good that the meal seems to be over in record time."
    "Once we're done eating, Harmony gives me a smile and knowing glance."
    harmony.say "So..."
    harmony.say "Here we are, celebrating somebody's birthday!"
    if not hero.has_gifts:
        "Oh crap!"
        "I knew there was something that I'd forgotten."
        "Harmony's dropping hints about her birthday present."
        "And I've got nothing to give her!"
        "Looks like I'm going to have to think on my feet."
        mike.say "I know, Harmony."
        mike.say "And isn't it great that we can just enjoy each other's company?"
        mike.say "You know, and not bring material things into it?"
        mike.say "Kind of like how Jesus or one of those religious guys would have done it?"
        "Harmony blinks, looking surprised by the line I'm taking."
        "But she recovers quickly, nodding in agreement."
        $ game.active_date.score -= 20
        $ harmony.love -= 10
        harmony.say "Oh..."
        harmony.say "Of course!"
        harmony.say "Material things just don't need to come into it!"
        "Phew...I think I got away with it."
        "Sure, I feel kind of guilty at exploiting Harmony's beliefs like that."
        "But it's better than admitting that I forgot her present, right?"
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_9
        if _return != "done":
            if _return not in ["None", "exit"]:
                "I nod and smile."
                mike.say "Okay, Harmony..."
                mike.say "You can stop dropping hints."
                "I take out the gift that I brought for Harmony and hand it over."
                harmony.say "Oh, thank you!"
                harmony.say "You didn't have to - but I'm happy you did!"
                play sound [paper_ripping_2, paper_ripping_1]
                if _return:
                    "Harmony grins as she opens the box."
                    "But when she sees what's inside, she looks totally stunned."
                    mike.say "Are you okay, Harmony?"
                    mike.say "Is there something wrong?"
                    harmony.say "What?"
                    harmony.say "Oh...oh no..."
                    $ game.active_date.score += 20
                    harmony.say "This is the greatest thing ever!"
                    harmony.say "Thank you so much!"
                    "I nod and smile, trying to look humble."
                    "But the truth is that I'm swelling up with pride."
                else:
                    "Harmony grins as she opens the box."
                    "But when she sees what's inside, her face falls."
                    mike.say "Are you okay, Harmony?"
                    mike.say "Is there something wrong?"
                    harmony.say "What?"
                    harmony.say "Oh no, nothing's wrong."
                    $ game.active_date.score -= 10
                    harmony.say "It's...very nice."
                    "I nod and smile."
                    "But it doesn't take a genius to know that Harmony's seriously disappointed with my gift."
            else:
                "Oh crap!"
                "I knew there was something that I'd forgotten."
                "Harmony's dropping hints about her birthday present."
                "And I've got nothing to give her!"
                "Looks like I'm going to have to think on my feet."
                mike.say "I know, Harmony."
                mike.say "And isn't it great that we can just enjoy each other's company?"
                mike.say "You know, and not bring material things into it?"
                mike.say "Kind of like how Jesus or one of those religious guys would have done it?"
                "Harmony blinks, looking surprised by the line I'm taking."
                "But she recovers quickly, nodding in agreement."
                $ game.active_date.score -= 20
                $ harmony.love -= 10
                harmony.say "Oh..."
                harmony.say "Of course!"
                harmony.say "Material things just don't need to come into it!"
                "Phew...I think I got away with it."
                "Sure, I feel kind of guilty at exploiting Harmony's beliefs like that."
                "But it's better than admitting that I forgot her present, right?"
    scene bg street
    show harmony date
    with fade
    "Once the meal is over and the bill's been paid, Harmony and I walk outside."
    "There are taxis zipping here and there, plenty looking for a fare."
    "So it seems like now would be the logical time to think about heading home."
    "But first I feel the need to gauge how well Harmony thinks things have gone."
    mike.say "I had a great time tonight, Harmony."
    mike.say "And I'd like to so this again some time."
    mike.say "Some time soon, if you're willing?"
    if game.active_date.score >= 100:
        "Harmony nods as I say all of this."
        "And it seems like she can't wait to answer me too."
        show harmony happy
        harmony.say "Oh yes!"
        harmony.say "I had a great time tonight too."
        harmony.say "And I'd love to do it again soon."
        show harmony embarrassed
        harmony.say "But...ooh!"
        harmony.say "Pardon me - I am feeling a little tired!"
        "Harmony's unexpected yawn is making me feel like doing the same."
        "But at the same time I'm fighting the urge to ask her to go someplace else."
        "I want to keep things going, but I know that Harmony likes to take things slowly."
        mike.say "That sounds great, Harmony."
        mike.say "So you'll call me?"
        show harmony happy
        "Harmony nods and smiles."
        "Then she leans in and plants a kiss on my cheek."
        "It's delicate enough to be totally platonic in nature."
        "But as she walks away, waving goodbye, I choose to take it as otherwise."
        "To me, it's the first step on the road to something much more."
    else:
        "Harmony smiles as I say all of this."
        "But I can see it's one of her special smiles."
        "The kind she wheels out when she's going to say no."
        "But she still wants to give the appearance of being nice about it."
        harmony.say "Me too, [hero.name], me too."
        show harmony embarrassed
        harmony.say "But I don't know when that would be."
        harmony.say "You see I have so many things in my calendar this month!"
        show harmony normal
        harmony.say "How about I let you know when I'm free?"
        "I know for sure that's a brush-off."
        "But there's no way I can call Harmony on it."
        "Not if I want even the remotest chance of seeing her again."
        mike.say "Sure thing, Harmony."
        mike.say "I'll wait to hear from you."
        show harmony happy
        "Harmony nods, smiles and then places a kiss on my cheek."
        "It's the kind of kiss that could be totally platonic in nature."
        "So I choose to think of it as just that, and to try harder next time."
    return

label harmony_birthday_date_impure_male:
    $ game.active_date.clothes = "sexydate"
    scene bg street
    "Going anywhere with Harmony since she got in touch with the carnal side of her nature has been pretty wild."
    "As she seems to have gained the ability to turn anything that happens to her into the chance to be debauched."
    "And don't get me wrong, I'm not complaining about that state of affairs."
    "In fact it's something that I've been enjoying a great deal."
    "The only problem is that it makes picking what to do on a special occasion a little harder than normal."
    "Because when your date's going to practically run riot in a vacuum, how do you choose something really outrageous?"
    "In the end I decide that the only answer is to just go with the flow."
    "So that's what I have in mind when I turn up to collect Harmony on her birthday."
    "Or at least I would, if she'd bothered to turn up on time!"
    "I turn around on the spot, looking this way and that."
    "But I'm sure that this is the place where we agreed to meet up."
    "Then I take out my phone to check the time."
    "And I find that I'm just about bang on for the time we agreed too."
    "This goes on for another couple of minutes, with me getting ever more irritated."
    "Until I hear the sound of someone calling my name."
    harmony.say "[hero.name]!"
    harmony.say "Here I am!"
    harmony.say "Over here!"
    "I turn towards the direction of Harmony's voice."
    show harmony sexydate happy with dissolve
    "And the moment that I see her, I instantly know why she's late."
    "Harmony's almost hobbling towards me thanks to the outfit she's wearing."
    "And it seems to have been designed solely for the sake of showing off her assets."
    "Because it certainly looks less than practical for her to be walking about in!"
    "In fact I have to make a concerted effort not to be entranced by the motions of her body."
    "Because everything seems to be swinging and swaying as Harmony hurries towards me."
    menu:
        "Compliment her outfit":
            mike.say "You're a little late, Harmony..."
            mike.say "But it was worth the wait."
            mike.say "That outfit is amazing!"
            "Harmony shakes her head and waves away my compliments."
            "But it's pretty easy to tell that she's delighted with my reaction."
            $ game.active_date.score += 15
            show harmony normal
            harmony.say "What?"
            harmony.say "This old thing?!?"
            harmony.say "I just threw it on as I was coming out of the door."
            "There's absolutely no way that Harmony can be telling the truth."
            "Because part of me's not convinced she could even get into that outfit on her own!"
            "It's clear she's late on account of the effort that she's gone to getting ready."
            "All of which is fine by me."
            "Because who cares about being late when you're with a girl who looks like that?"
            mike.say "Come on, Harmony..."
            mike.say "We still have to make it to where I'm taking you."
            show harmony happy
            harmony.say "Ooh!"
            harmony.say "I'm so excited!"
            harmony.say "Where are we going?"
            mike.say "It's a surprise, Harmony."
            mike.say "So you'll just have to wait and see!"
            show harmony normal
        "Tell her she's late":
            mike.say "You're a little late, Harmony!"
            mike.say "I've been waiting here for ages."
            show harmony upset
            "The smile on Harmony's face instantly fades as she hears what I have to say."
            "And in it's place I see a defensive expression beginning to take hold."
            harmony.say "Well..."
            harmony.say "I'm sorry, [hero.name]..."
            harmony.say "But I got here as fast as I could."
            harmony.say "I mean...maybe I did take a while getting myself ready."
            "I look Harmony up and down."
            "Noting again the tightness of her outfit."
            mike.say "I don't think putting that stuff on was what caused it."
            mike.say "More like the fact you can hardly walk in it!"
            $ game.active_date.score -= 20
            show harmony angry
            "Harmony frowns at this and shakes her head."
            harmony.say "Hey!"
            harmony.say "I was only trying to look nice for you."
            mike.say "Whatever, Harmony..."
            mike.say "Let's just get going."
            mike.say "We're late enough already."
            show harmony annoyed
    "Now we're effectively walking at the pace Harmony's outfit allows."
    "And I'm soon glad that I chose to meet her so close to our destination."
    "Because it means we only have to head down a couple of streets before we get there."
    scene bg alley
    show harmony sexydate
    with fade
    "And when we do, I can see that I made the right choice to start the date here."
    show harmony surprised
    harmony.say "Oh look, [hero.name]..."
    harmony.say "There's the sex shop!"
    show harmony happy
    harmony.say "I just love all the stuff they sell in there."
    harmony.say "Imagine if you were taking me there for a date!"
    "I can't keep a smile off my face as Harmony says all of this."
    mike.say "Funny you should say that, Harmony!"
    show fx exclamation
    show harmony surprised
    harmony.say "No!"
    harmony.say "No way?"
    harmony.say "You have to be kidding me?!?"
    hide fx
    "I shake my head and keep on smiling as we come to a stop outside the door."
    show harmony happy
    $ game.active_date.score += 5
    harmony.say "No frickin way!"
    harmony.say "This is going to be the best birthday ever!"
    "Harmony proceeds to grab hold of my hand so tightly that it makes me wince."
    "And then she pulls me inside the sex shop so quickly I almost fall on my face."
    scene bg sexshop
    show harmony sexydate happy
    with fade
    "Once we're inside she turns around on the spot, taking the whole place in."
    "An believe me, she really does look like the proverbial kid in the sweet-shop."
    show harmony surprised
    harmony.say "Oh, [hero.name]..."
    harmony.say "How does this work?"
    mike.say "What do you mean, Harmony?"
    show harmony normal
    harmony.say "I mean, like...I could spend a fortune in here."
    harmony.say "But you've got a budget, right?"
    harmony.say "Like how much you want to spend on me?"
    "The question of money is always an awkward one."
    "And it's about now that I realise I should have thought this one through."
    menu:
        "Buy everything she wants" if hero.money >= 500:
            "I think about it for a moment."
            "But then I smile and shake my head."
            mike.say "Don't worry about it, Harmony."
            mike.say "I think I can break the bank, just this once."
            mike.say "After all, it is a special occasion."
            show harmony happy
            $ game.active_date.score += 15
            "Of course my answer is an instant source of delight for Harmony."
            "She practically beams with happiness, clapping her hands together."
            show harmony normal
            "But then she stops and nods her head in a more careful manner."
            harmony.say "That's very kind of you, [hero.name]."
            show harmony blush
            harmony.say "But I promise that I won't take advantage of your generosity."
            harmony.say "I won't go insane and buy the whole place!"
            "I nod and make sure to keep the smile on my face."
            "Because I'm hoping that Harmony's going to be as good as her word."
            "But if not, I'll have to make sure that I step in and take back control."
        "Tell her to moderate herself":
            "I force a smile onto my face and nod."
            mike.say "Yeah, Harmony..."
            mike.say "I kind of do have to set a limit!"
            mike.say "So here's what I was thinking..."
            "I don't want to say the figure out loud, as that seems pretty crass."
            "So instead I pull out my phone and type in the number on the keypad."
            "Harmony watches with interest, waiting for me to be done."
            "And then she leans in closer to be able to read what's on the screen."
            show harmony embarrassed
            harmony.say "Oh!"
            harmony.say "Okay..."
            mike.say "Erm..."
            mike.say "You really mean that?"
            mike.say "You don't think I'm being mean or anything?"
            "Harmony shakes her head."
            harmony.say "No, no..."
            show harmony upset
            $ game.active_date.score -= 10
            harmony.say "If that's what you think I'm worth, then that's fine."
            harmony.say "I just like to know what I've got to work with."
            "I get the distinct feeling that Harmony's not impressed."
            "But things are already awkward enough without more discussions on the subject of money."
            "So I resolve to leave it alone and try to move on."
    scene bg sexshop
    show harmony sexydate
    with fade
    "It really doesn't come as a surprise a moment later when Harmony makes straight for the clothes racks."
    "If there's one thing this place has a lot of, it's outfits that would be called scandalous anywhere else."
    show harmony surprised at right with ease
    "There's everything from underwear to full-length ballgowns on the hangers, a dazzling amount of variety."
    "But all of them are either made out of something like rubber and leather."
    "Or else they have bits missing in strategic places that make the mind boggle."
    show harmony happy at left4 with ease
    "Harmony begins to search through what's on offer, pondering one item after another."
    "And each one of them is more than enough to make my eyes bulge at the mere sight of it."
    "So heaven knows what effect they'd have on me were I to actually see her in them!"
    if hero.has_skill("low_libido"):
        "In fact, most of those outfits are making me feel tired already."
        "And I'm getting more worried about what Harmony will pick by the moment!"
        "Finally she turns around, holding one of the outfits up against herself."
        show harmony normal at center with ease
        harmony.say "What do you think of this one?"
        harmony.say "It's sexy, but understated, right?"
        "I feel like I'm going to faint at the sight of the outfit."
        "But somehow I manage to summon an unexpected reserve of strength."
        "And the smile I force onto my face must be a convincing one too."
        "Because the one on Harmony's own face becomes larger still."
        show harmony blush
        harmony.say "I can see that you like it, [hero.name]!"
        $ game.active_date.score += 15
        harmony.say "And that's good enough for me."
        show harmony happy
        harmony.say "I'll go with this one!"
        "I keep on nodding and smiling as Harmony explains herself."
        "And I manage to hold it all in until she hurries off to the sales desk too."
        "Then I let it all out in one go, groaning and almost bending over double."
        "My god, she's going to look so hot in that outfit."
        "I don't know how I'm going to find the strength to cope."
        "But at least if the sight it does finish me off..."
        "Then I'm going to die happy!"
    elif hero.has_skill("high_libido"):
        "I've been getting harder by the moment since I saw Harmony looking at those outfits."
        "The thought of her in any of them is enough to make me want to do terrible things!"
        show harmony normal at center with ease
        harmony.say "What do you think of this one?"
        harmony.say "It's sexy, but understated, right?"
        "I can already feel my heart beating ever faster in my chest."
        "And now the corners of my vision are going all fuzzy too."
        "But this is hardly my first rodeo."
        "So I know how to control myself when the need arises."
        mike.say "Hmm..."
        mike.say "I don't mind telling you, Harmony..."
        mike.say "The thought of you in that outfit..."
        mike.say "It's all I can do to control myself right now!"
        "I can see that I've just about managed to reign it in enough."
        "Sufficiently so that I can keep myself under control."
        "But not so much that Harmony can't sense my genuine desire for her."
        show harmony blush
        harmony.say "I can see that you like it, [hero.name]!"
        $ game.active_date.score += 15
        harmony.say "And that's good enough for me."
        show harmony happy
        harmony.say "I'll go with this one!"
        "I keep on nodding and smiling as Harmony explains herself."
        "But once she's back amongst the racks, I let out a moan of relief."
        "Because that took almost all the strength I had in me to pull off."
        "And when she finally puts herself in front of me in that thing..."
        "Well, let's just say I won't be held responsible for my actions!"
    else:
        "I'm half intrigued to see what Harmony's going to choose."
        "But at the same time I'm also half scared of finding out."
        "I've never seen her set loose in a place like this before."
        "So heaven knows what she's going to settle on!"
        "Finally she turns around, holding one of the outfits up against herself."
        show harmony normal at center with ease
        harmony.say "What do you think of this one?"
        harmony.say "It's sexy, but understated, right?"
        menu:
            "Finely balanced, as all things should be":
                "A soon as I see the outfit that Harmony's holding up, my eyes bulge in their sockets."
                "And there's nothing I can do to keep myself from beginning to nod my head too."
                mike.say "Whoa..."
                mike.say "You're right, Harmony!"
                mike.say "How could something be so finely balanced?"
                mike.say "That's definitely the outfit you should buy!"
                "Of course I'm lying."
                "Nothing could be further from the truth."
                "But I really want to see Harmony in that outfit."
                "Because it leaves absolutely nothing to the imagination!"
                show harmony blush
                harmony.say "I can see that you like it, [hero.name]!"
                $ game.active_date.score += 15
                harmony.say "And that's good enough for me."
                show harmony happy
                harmony.say "I'll go with this one!"
                "I keep on nodding and smiling as Harmony explains herself."
                "But once she's back amongst the racks, I breathe a sigh of relief."
                "Just thinking about her in that outfit is almost enough to finish me off."
                "So god knows what's going to happen when I actually see wearing it for real."
            "Wow there! You can't be serious about this one!":
                "A soon as I see the outfit that Harmony's holding up, my eyes bulge in their sockets."
                "And there's nothing I can do to keep myself from beginning to shake my head too."
                mike.say "Whoa..."
                mike.say "No way, Harmony!"
                mike.say "I mean, if that's the one you want, that's fine."
                mike.say "But that's the raunchiest thing I've ever seen!"
                show harmony surprised
                "Harmony looks at me in genuine surprise."
                "Then she takes a long, hard look at the outfit she's holding."
                harmony.say "You can't be serious?"
                harmony.say "I deliberately chose this one because it was modest!"
                show harmony sad
                harmony.say "Hmm..."
                harmony.say "I can see that I'm going to have to think about this one."
                harmony.say "Because I thought we were on the same page."
                $ game.active_date.score -= 10
                harmony.say "But it seems like I was wrong."
                "Harmony shakes her head as she turns around."
                "And then she disappears back between the racks."
                "Which leaves me wondering if being honest was the best idea."
                "As it seems to have highlighted a genuine divide between us."
    show harmony sexydate normal
    "Harmony emerges from the racks with the items she wants to buy."
    "Then she hands them over to me, and I duly walk over to the sales desk."
    scene bg sexshop
    show lexi c at blacker, mostright4
    with fade
    "There's a fairly young girl working behind the cash register."
    "And she gives me a pleasant smile as I put down the clothes."
    "Cashier" "Hey there..."
    "Cashier" "Let me get that for you, sir..."
    "As the girl takes the items, I get the feeling I'm being watched."
    "Or more specifically, that someone's staring past me."
    "A quick glance over my shoulder confirms my suspicions."
    show harmony sexydate annoyed at dark, mostleft5 with dissolve
    "Harmony's right there, eyeballing the girl with the intensity of a laser beam!"
    "Luckily for me, she doesn't seem to notice."
    "Or else she's choosing to ignore it."
    "Cashier" "Are these for someone special?"
    "Cashier" "Or for your own use, sir?"
    "The girl winks as she asks the question."
    "And I instantly get that she's joking around with me."
    "They must get guys buying women's clothes in here on account of their kinks."
    "But the insinuation is only being made in jest, and so I laugh along like a good sport."
    mike.say "Oh no..."
    mike.say "They don't come in my size!"
    hide harmony
    show harmony sexydate angry at mostleft5
    show harmony at left4 with ease
    harmony.say "Excuse me!"
    harmony.say "But if you must know, those are for me."
    harmony.say "And MY boyfriend here is treating me on my birthday!"
    "I take a step to the side."
    "More than a little surprised by how rude Harmony's being."
    "But then it hits me that this is just a misunderstanding."
    "And I'm sure that, with a little charm, I can sort it all out."
    if hero.charm >= 60:
        mike.say "Wait a minute, Harmony..."
        show harmony annoyed
        mike.say "I think she might have a point."
        mike.say "I wonder if they do have something like this in my size after all?"
        "The cashier seems to get the joke straight away."
        "Because she chuckles and slips away from the conversation."
        "But Harmony seems to be getting more intrigued by the second."
        show harmony embarrassed
        harmony.say "Are...are you serious?"
        harmony.say "Because, that's...kind of interesting..."
        harmony.say "And it's seriously kinky too!"
        "I'm secure enough in my sexuality to take this as a win."
        "And the important thing is that it's distracted Harmony from the cashier."
        "Because now she's more interested in the possibilities of me cross-dressing."
        mike.say "I could be, Harmony."
        mike.say "We are living in the twenty-first century."
        mike.say "And it pays to keep an open mind..."
    else:
        show harmony annoyed
        mike.say "There's no need to get tetchy, Harmony."
        mike.say "She was just joking around."
        mike.say "No harm done, yeah?"
        "The girl nods and turns to Harmony with a nod."
        "But it doesn't look like Harmony's going to make it that easy."
        show harmony angry
        harmony.say "But she insulted you, [hero.name]!"
        harmony.say "She practically called you a transvestite!"
        mike.say "Oh, come on, Harmony!"
        mike.say "I'm not offended by that."
        mike.say "For that, she'd need to...oh, I don't know..."
        show harmony surprised
        mike.say "Make fun of your weight, or something like that!"
        "As soon as the words are out of my mouth, I see the girl wince."
        "And she almost sinks down under the counter as Harmony rounds on me."
        show harmony angry
        harmony.say "How did you manage to do it, [hero.name]?"
        $ game.active_date.score -= 20
        harmony.say "How did you manage to make this about my weight?!?"
        "Oh balls..."
        "Looks like I actually made things worse."
        "But at least Harmony's forgotten all about the cashier."
        "Even if it does mean that I'm the one in the firing-line instead."
    scene bg sexshop
    show harmony sexydate
    with fade
    "Once she comes back from making her purchase, Harmony gives me a smile and knowing glance."
    harmony.say "So..."
    harmony.say "Here we are, celebrating somebody's birthday!"
    if not hero.has_gifts:
        "Oh crap!"
        "I knew there was something that I'd forgotten."
        "Harmony's dropping hints about her birthday present."
        "And I've got nothing to give her!"
        "Looks like I'm going to have to think on my feet."
        mike.say "I know, Harmony."
        mike.say "And isn't it great that we can just enjoy fun stuff like this place sells?"
        mike.say "You know, and not bring material things into it?"
        mike.say "Kind of like we're really liberated from that kind of thing."
        show harmony surprised
        "Harmony blinks, looking surprised by the line I'm taking."
        "But she recovers quickly, nodding in agreement."
        $ game.active_date.score -= 20
        $ harmony.love -= 10
        show harmony sad
        harmony.say "Oh..."
        harmony.say "Of course!"
        show harmony sadsmile
        harmony.say "Material things just don't need to come into it!"
        "Phew...I think I got away with it."
        "Sure, I feel kind of guilty at exploiting Harmony's emotions like that."
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_10
        if _return != "done":
            if _return not in ["None", "exit"]:
                "I nod and smile."
                mike.say "Okay, Harmony..."
                mike.say "You can stop dropping hints."
                "I take out the gift that I brought for Harmony and hand it over."
                show harmony happy
                harmony.say "Oh, thank you!"
                harmony.say "You didn't have to - but I'm happy you did!"
                if _return:
                    "Harmony grins as she opens the box."
                    show harmony surprised
                    "But when she sees what's inside, she looks totally stunned."
                    mike.say "Are you okay, Harmony?"
                    mike.say "Is there something wrong?"
                    show fx question
                    harmony.say "What?"
                    harmony.say "Oh...oh no..."
                    hide fx
                    $ game.active_date.score += 20
                    show harmony happy
                    harmony.say "This is the greatest thing ever!"
                    harmony.say "Thank you so much!"
                    "I nod and smile, trying to look humble."
                    "But the truth is that I'm swelling up with pride."
                else:
                    "Harmony grins as she opens the box."
                    show harmony sad
                    "But when she sees what's inside, her face falls."
                    mike.say "Are you okay, Harmony?"
                    mike.say "Is there something wrong?"
                    show fx question
                    harmony.say "What?"
                    harmony.say "Oh no, nothing's wrong."
                    hide fx
                    show harmony sadsmile
                    $ game.active_date.score -= 10
                    harmony.say "It's...very nice."
                    "I nod and smile."
                    "But it doesn't take a genius to know that Harmony's seriously disappointed with my gift."
            else:
                "Oh crap!"
                "I knew there was something that I'd forgotten."
                "Harmony's dropping hints about her birthday present."
                "And I've got nothing to give her!"
                "Looks like I'm going to have to think on my feet."
                mike.say "I know, Harmony."
                mike.say "And isn't it great that we can just enjoy fun stuff like this place sells?"
                mike.say "You know, and not bring material things into it?"
                show harmony surprised
                mike.say "Kind of like we're really liberated from that kind of thing."
                "Harmony blinks, looking surprised by the line I'm taking."
                "But she recovers quickly, nodding in agreement."
                $ game.active_date.score -= 20
                $ harmony.love -= 10
                show harmony sad
                harmony.say "Oh..."
                harmony.say "Of course!"
                show harmony sadsmile
                harmony.say "Material things just don't need to come into it!"
                "Phew...I think I got away with it."
                "Sure, I feel kind of guilty at exploiting Harmony's emotions like that."
    scene bg street
    show harmony sexydate
    with fade
    "As we walk out of the sex shop and onto the street, I glance at the time."
    "And I see that it's far earlier than I'd expected it to be right now."
    mike.say "Looks like we've got some time on our hands, Harmony."
    mike.say "You want to go do something else before we call it a day?"
    if game.active_date.score >= 80:
        "Harmony instantly nods her head."
        show harmony happy
        harmony.say "Sure, [hero.name]..."
        harmony.say "I'm having such a great time!"
        show harmony normal
        harmony.say "There's no way I'm ready to go home yet."
        "I nod eagerly, delighted to hear that Harmony's up for it."
        "And then I begin casting my gaze about."
        "Looking for something that we can do next."
        mike.say "Wait a second, Harmony..."
        mike.say "I'll think of something!"
        "It's then that I feel Harmony grab hold of my hand again."
        show harmony blush
        harmony.say "Don't worry..."
        harmony.say "I already did!"
        call harmony_birthday_sex_impure from _call_harmony_birthday_sex_impure
    else:
        "Harmony surprises me by shaking her head."
        show harmony embarrassed
        harmony.say "Oh no!"
        harmony.say "All that shopping seems to have taken it out of me."
        harmony.say "I'm feeling so tired that all I want to do is go home."
        mike.say "Okay, Harmony..."
        mike.say "If that's what you really want."
        hide harmony
        "I make sure to see that Harmony gets safely into a cab."
        "And then I begin to think about how I'm going to get home myself."
        "But as I do so, I find myself distracted as I worry about how the date went."
        "Sure, there were things I could have done better."
        "But I thought most of it was a success."
        "I just hope Harmony's as forgiving in her opinions too."
    return

label harmony_birthday_sex_impure:
    show harmony upset sexydate
    "As soon as Harmony has hold of my hand, her head starts turning this way and that."
    "And I can tell that she's looking for something, casting her gaze about the street."
    show fx exclamation
    show harmony mean
    "A moment later it seems to settle on one spot, as if she's found what she's looking for."
    show harmony at right4 with hpunch
    "That's when I feel her begin to pull on my arm, without warning or explanation."
    hide fx
    "And it's not a gentle pull either, it's a sudden and merciless one that uses all of her strength!"
    "This is also the point where I should mention that Harmony's not a frail little thing."
    "In fact, she's deceptively strong!"
    mike.say "Whoa..."
    mike.say "Harmony..."
    mike.say "What are you doing?"
    show harmony at right5 with ease
    "Harmony obviously hears my protests, as she turns her head towards me as I speak."
    "But all the same, she doesn't stop for even a moment as she drags me along."
    show harmony blush
    harmony.say "No time to explain, [hero.name]..."
    harmony.say "Just come with me..."
    show harmony mean at right with ease
    harmony.say "Over here!"
    "I figure that it's easier to go along with Harmony and find out what she wants."
    "As opposed to fighting her to a standstill and then demanding to know what's going on."
    "So I allow myself to be manhandled down the street."
    scene bg alley
    show harmony sexydate blush
    with fade
    "And then I find myself being dragged off of it and into one of the nearby alleyways."
    "Which lets me make a guess at just what Harmony has in mind."
    "But that doesn't mean that I'm suddenly the one in charge here."
    "Because as soon as we're out of sight down the alley, Harmony grabs me by the collar."
    show harmony mean with hpunch
    "And then she shoves me bodily backwards against the wall."
    "I hit the bricks hard enough to knock the wind out of my lungs too."
    mike.say "Urgh..."
    mike.say "Ouch!"
    mike.say "Harmony..."
    mike.say "What the hell?!?"
    "The response this elicits from Harmony isn't any kind of apology."
    "It's not even a decent explanation of any kind either."
    show harmony close
    harmony.say "Can't stop now..."
    harmony.say "Not before we do it!"
    show harmony blush
    harmony.say "Come on, [hero.name] - what are you waiting for?!?"
    "I feel like saying that I'm waiting for a moment when I'm not being dragged around."
    "But that wouldn't be very productive at a time like this, now would it?"
    "And the truth is that I've kind of started to get over the way Harmony's going about it."
    "I'm actually more interested in where all of this is going."
    "My heartbeat is quickening, and I can feel my cock getting hard too."
    "How could it be any other way?"
    "I have Harmony's body pressed up against mine as she fumbles with my flies."
    "Her breasts are almost pushed into my face."
    "And her thighs are grinding into me at the same time."
    "My first course of action is to reach down and take hold of Harmony's skirt."
    "Then I pull it upwards, exposing the curve of her more than ample buttocks."
    "Next I yank at the elastic of her panties, dragging them downwards."
    "I can feel Harmony nodding and gasping with approval."
    harmony.say "Mmm..."
    harmony.say "Oh yeah..."
    harmony.say "Tear them off me!"
    "I can feel just how warm it is down there as I pull of Harmony's panties."
    "And I'm not at all surprised to find that they're already wet to the touch."
    "She must have been getting wet even before she dragged me into the alley!"
    "I don't need any more motivation than that."
    "From that moment on, I can feel myself rising to the occasion and taking control."
    "My hands have a firm hold on Harmony, and I use it to change our positions."
    "Before she was the one pressing me against the wall."
    "But now I lift her off her feet as I turn the tables."
    scene bg black
    show harmony doggy alley pleasure
    with hpunch
    harmony.say "Ooh!"
    "Harmony lets out a cry of surprise as I'm now pushing her up against the wall."
    "But it soon turns into a moan of pleasure as I slide my cock between her thighs too."
    show harmony doggy normal
    harmony.say "Oh yes..."
    harmony.say "Please..."
    harmony.say "I want it so badly!"
    "There's no need for Harmony to beg for it."
    "I'm already dead set on getting inside of her."
    show harmony doggy pov vaginaltip
    "To that end I get straight down to pushing the head of my cock hard against her pussy."
    "Normally I'd be gentle at this stage, indulging in foreplay and teasing Harmony."
    "But neither of us is in that kind of place right now."
    "All we want is the physical release of fucking."
    "We want it fast."
    "We want it hard."
    "And we want it now!"
    "I keep on pushing and thrusting, not letting up for a second."
    show harmony doggy hurt
    "Harmony nods and clings onto me as I do this, urging me on."
    "It feels like I'm trying to batter down a door, swinging again and again."
    show harmony doggy surprised vaginal
    "But then I hear Harmony let out a deep, helpless cry."
    show harmony doggy ahegao
    harmony.say "Ahh..."
    harmony.say "Oh fuck!"
    "The mixture of pain and pleasure in her voice flips a switch in my head."
    "There's no time for me to stop and think, not even for a second."
    "Instead I redouble my efforts, forcing my way deeper inside."
    show harmony doggy hurt vaginaltip
    pause 0.25
    show harmony doggy vaginal with hpunch
    pause 0.1
    show harmony doggy bounce
    pause 0.3
    show harmony doggy -bounce
    pause 0.15
    show harmony doggy vaginaltip
    pause 0.25
    show harmony doggy vaginal with hpunch
    pause 0.1
    show harmony doggy bounce
    pause 0.3
    show harmony doggy -bounce
    pause 0.15
    show harmony doggy vaginaltip
    pause 0.25
    show harmony doggy vaginal with hpunch
    pause 0.1
    show harmony doggy bounce
    pause 0.3
    show harmony doggy -bounce
    "Even when I'm as deep as I can go, I don't stop."
    "I just back up and do it again, thrusting in and out like a machine."
    "This is one of those times when I'm thankful that Harmony's built like she is."
    "A slighter girl would have made me worry about going to hard and fast."
    "But no matter what I do, Harmony soaks it up and then asks for more."
    "Her body, like that of a voluptuous goddess, bounces and sways."
    "And the weight of it means I feel every movement multiplied a hundredfold."
    show harmony doggy vaginaltip
    pause 0.25
    show harmony doggy vaginal with hpunch
    pause 0.1
    show harmony doggy bounce
    pause 0.3
    show harmony doggy -bounce
    pause 0.15
    show harmony doggy vaginaltip
    pause 0.25
    show harmony doggy vaginal with hpunch
    pause 0.1
    show harmony doggy bounce
    pause 0.3
    show harmony doggy -bounce
    pause 0.15
    show harmony doggy vaginaltip
    pause 0.25
    show harmony doggy vaginal with hpunch
    pause 0.1
    show harmony doggy bounce
    pause 0.15
    show harmony doggy -bounce
    "But there's no way I can keep up this kind of pace forever."
    show harmony doggy vaginaltip
    pause 0.25
    show harmony doggy vaginal creampie with hpunch
    pause 0.1
    show harmony doggy bounce
    pause 0.15
    show harmony doggy -bounce
    "And now it's my turn to cry out as I lose it."
    "Harmony moans with disappointment at first."
    show harmony doggy vaginaltip pleasure
    pause 0.15
    show harmony doggy vaginal ahegao squirt with hpunch
    "Then her tune changes as she begins to feel the effects."
    with hpunch
    harmony.say "Fuck..."
    harmony.say "Fuck yeah..."
    with hpunch
    harmony.say "Do it..."
    harmony.say "Fill me up!"
    with hpunch
    "By the time I'm spent, I'm leaning all of my weight onto Harmony."
    "And I'm sure the wall is the only thing that's keeping us upright."
    show harmony hurt dickcum out -creampie -squirt
    "She gently turns me to one side, propping me against it and freeing herself in the process."
    "I feel my cock slide out of Harmony, and I watch as she starts to tidy herself up."
    "Once she's done, Harmony stuffs my cock back into my pants and zips them up too."
    scene bg alley
    show harmony sexydate happy
    with fade
    harmony.say "Mmm..."
    harmony.say "That was just what I needed!"
    harmony.say "And I didn't even have to put on my nice new outfit either."
    show harmony blush
    harmony.say "Come on, [hero.name] - we can try it out when we get home!"
    "Harmony takes hold of my hand again, dragging me after her."
    "I stumble along in her wake, trying to make sense of what she just said."
    "And hoping to all the gods that she just means putting the damn thing on."
    "Because another session like that within twenty four hours would be enough to finish me off!"
    $ harmony.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
