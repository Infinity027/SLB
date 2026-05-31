init python:
    Event(**{
    "name": "science_project_01",
    "label": "science_project_01",
    "duration": 1,
    "music": "music/roa_music/juice.ogg",
    "conditions": [
        IsHour(7, 10),
        HeroTarget(
            IsGender("male"),
            IsRoom("kitchen")),
        PersonTarget(anna,
            Not(IsHidden()),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            IsRoom("kitchen"),
            ),
        "Person.showdown(anna, bree)",
        ],
    })

    Event(**{
    "name": "science_project_02",
    "label": "science_project_02",
    "duration": 1,
    "music": "music/roa_music/juice.ogg",
    "conditions": [
        IsDone("science_project_01"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("uni")
            ),
        PersonTarget(anna,
            Not(IsHidden()),
            HasRoomTag("uni"),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            HasRoomTag("uni"),
            ),
        ],
    })

    Event(**{
    "name": "science_project_03",
    "label": "science_project_03",
    "duration": 1,
    "music": "music/roa_music/juice.ogg",
    "conditions": [
        IsDone("science_project_02"),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        PersonTarget(bree,
            Not(IsHidden()),
            IsRoom("bedroom2"),
            Not(IsActivity("sleep")),
            ),
        ],
    })

    Event(**{
    "name": "science_project_04",
    "label": "science_project_04",
    "duration": 1,
    "music": "music/roa_music/juice.ogg",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsFlag("sciencehelper"),
            HasRoomTag("uni"),
            ),
        PersonTarget(anna,
            Not(IsHidden()),
            HasRoomTag("uni"),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            HasRoomTag("uni"),
            ),
        "not bree.is_visibly_pregnant"
        ],
    })


label science_project_01:
    scene bg kitchen
    "It's that time of the morning when I need yet another dose of coffee to keep me functioning."
    "And so I'm headed to the kitchen in order to dose myself up on caffeine, like a man on a mission."
    "But then I see [bree.name] sitting at the table, surrounded by piles of books and paper."
    "I stop to stare at this odd sight, wondering what the hell could be going on."
    "Don't get me wrong - [bree.name]'s not some kind of idiot that struggles with her studies."
    "It's just that I've never seen her buried this deep in her books before."
    mike.say "Ah..."
    mike.say "Hey, [bree.name]..."
    mike.say "Is everything okay?"
    show bree sleep surprised at center, vshake
    "[bree.name] almost jumps in her chair, clearly surprised to hear the sound of my voice."
    "Her eyes dart in my direction, and I can see that she must have been miles away just now."
    bree.say "Huh..."
    bree.say "What..."
    show bree happy
    bree.say "Oh...it's only you, [hero.name]!"
    "What does she mean 'only me'?!?"
    show bree normal
    "I guess I'll just have to chalk that one up to [bree.name] being out of it."
    mike.say "I said is everything okay, [bree.name]?"
    mike.say "It's the first time I've seen you study like this!"
    "As she starts to regain her senses, [bree.name] pays more attention to what I just said."
    show bree annoyed
    "And she looks more than a little insulted by it too!"
    bree.say "The first time you've seen me study?!?"
    bree.say "Ouch, [hero.name]!"
    bree.say "I DO take classes too you know!"
    "I hold up my hands in a gesture of surrender and shake my head."
    "[bree.name] must still be a little groggy, as she's not hearing what I actually said."
    mike.say "No, [bree.name]..."
    mike.say "I said it's the first time I've seen you study like THIS!"
    "I gesture to the piles of books and papers covering the table."
    mike.say "I always thought that you studied in your room or something, that's all."
    show bree normal
    "[bree.name] nods at this and lets out a weary sigh."
    bree.say "I'm sorry, [hero.name]."
    bree.say "It's the stress talking, you know?"
    bree.say "I thought a change of scene might help me study better."
    "Well, it doesn't seem to have worked out the way she planned."
    "But I keep the negative observations to myself and just nod."
    "No point in piling more woe onto [bree.name] when she's clearly feeling the pressure."
    "So instead I try to get to the bottom of what's got her so stressed-out."
    mike.say "Anything I can help you with, [bree.name]?"
    mike.say "You know, some people have accused me of being pretty smart!"
    show bree happy
    "[bree.name] cracks a smile at this."
    "Then she shakes her head and chuckles."
    "It's good to hear her laughing, rather than sighing."
    show bree normal
    bree.say "It's the Sci-Fi club at uni, yeah?"
    bree.say "The have this competition they call 'The Mad Scientist's Convention'."
    mike.say "Hmm...that sounds interesting!"
    bree.say "Yeah, it's pretty cool."
    bree.say "You have to come up with a science project that's legit."
    bree.say "But the twist is it has to be...well, quirky too."
    bree.say "Like in a kind of fun and scary way."
    "I wrinkle my nose as I think about what [bree.name]'s saying."
    "And then I start nodding as it all begins to make sense."
    mike.say "Oh...I get it!"
    mike.say "Like in a campy, science fiction way?"
    mike.say "Taking over the world with killer robots and psychic ray-guns?"
    show bree happy
    bree.say "You got it!"
    mike.say "Why didn't you just say that, [bree.name]?"
    mike.say "I've always wanted to plot world domination!"
    "[bree.name] shakes her head, still chuckling at my enthusiasm."
    bree.say "I don't know if taking over the world is going to happen, [hero.name]!"
    bree.say "But the winner gets a really cool prize, one that's nice and geeky."
    bree.say "Like, it's been videogames or books and stuff in the past."
    mike.say "Sounds perfect, [bree.name]!"
    mike.say "So what's the problem?"
    "[bree.name] lets out another long sigh."
    show bree sad
    bree.say "I don't know what to do, that's the problem!"
    bree.say "I'm totally out of ideas."
    "Now it's my turn to frown and shake my head."
    "Obviously I want to help [bree.name] out all I can."
    "Sure, I'm a massive sci-fi nerd."
    "But I'm clueless when it comes to the actual science part!"
    "What [bree.name] needs is someone that's got sci-fi and science smarts."
    "Then it hits me - I know the perfect person to help."
    mike.say "I know who could help you out, [bree.name]."
    show bree normal
    mike.say "There's a girl at uni called 'Anna'."
    mike.say "She's a biology major and a massive sci-fi geek too."
    mike.say "In fact, you might have seen her around?"
    mike.say "She's pretty hard to miss - pink hair, cute butt and great breasts..."
    "I trail off as I see the way that [bree.name]'s looking at me right now."
    show bree annoyed
    "Perhaps I should have stuck to listing Anna's academic and fan girl credentials?"
    show fx drop
    bree.say "Thanks for describing her as an object, [hero.name]!"
    hide fx
    bree.say "Feminism still isn't your strong suit, yeah?"
    "I can't help blushing a little."
    show bree normal
    "But I press on, trying to change the subject."
    mike.say "Whatever, [bree.name], whatever..."
    mike.say "I'm sure you and Anna will make a great team."
    mike.say "I'll introduce you when we're at uni, okay?"
    "[bree.name] nods slowly, still looking like she doesn't quite trust me."
    bree.say "Okay, [hero.name]."
    bree.say "But just remember that I'm looking for a partner to work on my science project."
    bree.say "Not for someone to star in whatever dirty little fantasy you're cooking up inside of your head!"
    return

label science_project_02:
    scene bg university
    "The first chance I get, I arrange for Anna to meet up with [bree.name] and myself on the uni campus."
    "Sure, it feels a little awkward, like I'm playing match-maker for the two of them or something."
    "But I just need to keep my mind on the actual reason we're doing this, which is [bree.name]'s science project."
    "And I have to stop my thoughts wandering towards images of [bree.name] and Anna together..."
    "Both of them working hard into the night..."
    "Sweating over the science project until they're glistening with perspiration..."
    "Maybe one of them volunteering to give the other a massage to relieve the strain..."
    show bree with dissolve
    show fx question
    bree.say "[hero.name]?"
    bree.say "Hey, will you snap out of it already?!?"
    hide fx
    "At the sound of [bree.name]'s voice the fantasy in my mind pops like a bubble."
    "Or to be honest, the tone of her voice makes me stop fantasizing."
    mike.say "Oh...oh yeah..."
    mike.say "Sorry, [bree.name]!"
    mike.say "Where's Anna gotten to?"
    mike.say "She was supposed to be here by now!"
    "[bree.name] shakes her head at me, still not convinced I'm back in reality."
    "But then she seems to spot something that distracts her."
    bree.say "You said short, right?"
    bree.say "With pink hair?"
    "I look in the direction that [bree.name]'s pointing and nod."
    mike.say "Yeah, that's Anna."
    mike.say "How did you spot her so easily?"
    "I know I said that Anna had bright pink hair."
    "But this is a uni campus, and students like to experiment with their image."
    "A lot of them have dyed hair, and it's not like pink is a rare choice of colour."
    show bree blush
    "[bree.name]'s cheeks flush at the question, and I can't help wondering why."
    bree.say "Well..."
    bree.say "You said she was short too."
    bree.say "And...and...well-endowed!"
    "It's all I can do to keep myself from sniggering at [bree.name]'s embarrassment."
    "But she's not wrong, as anyone watching Anna walk over to us would agree."
    "Anna's smiling as she walks over, having already spotted me."
    "And her hips roll with every step, as well as her breasts bouncing too!"
    show bree -blush at left5 with move
    show anna at right5 with moveinright
    anna.say "Hey, [hero.name]!"
    anna.say "What's up?"
    mike.say "Hey, Anna!"
    mike.say "This is [bree.name]."
    mike.say "[bree.name], this is Anna."
    "Anna beams up at [bree.name], clearly pleased to be introduced to her."
    "And even though she's much shorter, her enthusiasm seems to make up for that."
    "In every way she seems to be a match for [bree.name], a perfect partner."
    "For the science project, of course!"
    bree.say "Hi, Anna."
    bree.say "It's great to finally meet you."
    bree.say "[hero.name]'s told me so much about you!"
    show anna surprised
    anna.say "Wow..."
    anna.say "You're SO pretty, [bree.name]!"
    anna.say "Sasha was right - you are like a big, sexy blonde doll!"
    show bree blush
    "Up until that moment, it looked like [bree.name] was getting over her embarrassment."
    "But Anna just comes out with that line, and she's turning red in an instant."
    "All I can do is smile awkwardly and try to laugh it off."
    "I really should have warned [bree.name] that Anna seldom thinks anything she doesn't then say!"
    show anna blush
    anna.say "Oh...oh dear..."
    anna.say "I'm so sorry, [bree.name]!"
    anna.say "I tend to say things without thinking sometimes."
    anna.say "And please don't be mad at Sasha either!"
    anna.say "We're in a band together and well...well, you know how she can be, right?"
    "For a moment I think that I'm going to have to step in to save the situation."
    show bree -blush
    "But then [bree.name] seems to steel herself and push her embarrassment aside."
    bree.say "It's okay, Anna."
    bree.say "I've lived with Sasha long enough to get used to her."
    bree.say "She can be very...uncomplicated...straight-forward, yeah?"
    show anna normal
    "Anna nods eagerly, clearly relieved to be offered a means of escape."
    anna.say "Oh yeah, yeah..."
    anna.say "Sasha can be a tough cookie sometimes!"
    anna.say "Well, most of the time really..."
    anna.say "But she's a good person under it all!"
    "I sense that this would be a good time for me to interject myself."
    "Just for the sake of steering the conversation back in the right direction."
    mike.say "So, [bree.name]..."
    mike.say "You were thinking of entering this 'Mad Scientist's Convention'?"
    bree.say "Oh...oh yeah!"
    bree.say "Have you heard of it, Anna?"
    show anna happy
    "Anna smiles and makes a kind of snorting sound."
    anna.say "Of course I have!"
    anna.say "I always wanted to enter myself."
    show anna normal
    anna.say "I just never seem to get round to it!"
    bree.say "Thing is, Anna - I don't know what to actually DO!"
    "Anna cocks her head on one side for a moment, looking thoughtful."
    "I know the look, it means that she's racking her brains for an idea."
    "It's just a bonus that it also makes her look super cute at the same time!"
    anna.say "Why don't we use the title for inspiration?"
    anna.say "Doctor Frankenstein was the original mad scientist, right?"
    show bree surprised
    "[bree.name] looks at me and then back to Anna, surprise written all over her face."
    "But I'm not really shocked to hear that kind of a suggestion from Anna."
    "Because I know how seriously she takes her horror films, both modern and classic."
    mike.say "Hear Anna out, [bree.name]!"
    show fx drop at left5
    bree.say "B...but we can't sew bits of dead bodies together!"
    hide fx
    show anna happy
    "Anna bursts out laughing at this, covering her mouth with a hand."
    "She shakes her head and rolls her eyes at [bree.name]'s comment."
    show anna normal
    show bree normal
    "And I can see that [bree.name] bristles a little at this too."
    "But Anna soon seems to smooth that over with her innocent enthusiasm."
    anna.say "No, [bree.name] - of course not!"
    anna.say "But you remember that Mary Shelley was inspired by Galvanism, right?"
    anna.say "She was thinking about that when she wrote the book."
    "I scratch the back of my head at the unfamiliar term."
    "Anna's starting to make me feel pretty dumb right now!"
    mike.say "Erm...sorry to sound like the exposition guy."
    mike.say "But what's Galvanism?"
    anna.say "It's a branch of science pioneered by Luigi Galvani."
    anna.say "He studied the generation of electric currents in biological organisms."
    anna.say "Stuff like the way muscles contort and contract when in contact with an electric current."
    "[bree.name] seems to be taking in everything that Anna's saying."
    "But I can already feel my own head starting to spin."
    "Luckily for me, that's when I remember that this is nothing to do with me!"
    mike.say "Okay, Ladies..."
    mike.say "It sounds like you're already on the way to plotting world domination."
    mike.say "So I'll leave you to it, okay?"
    bree.say "Huh..."
    bree.say "Oh...are you still here, [hero.name]?"
    anna.say "Don't worry, [hero.name]."
    anna.say "We can handle it from here!"
    "I shake my head as I walk away from [bree.name] and Anna."
    scene bg university with fade
    "I can't help feeling like I just got shooed away like an annoying child!"
    "But I put that thought out of my head and congratulate myself instead."
    "Looks like I did well to team the two of them up for this project."
    "Their level of enthusiasm and the goriness of their ideas is a little worrying."
    "But I'm sure it'll all work out well in the end."
    return

label science_project_03:
    scene bg livingroom
    "It's been a short while since I hooked [bree.name] up with Anna to work on her science project."
    "And since then, I have to admit that I haven't seem either of them all that much."
    "I just assume that they're hard at work on their effort to win 'The Mad Scientist's Convention'."
    "That us until I hear the sound of screaming coming from [bree.name]'s bedroom!"
    show bg secondfloor
    "Dropping what I was doing, I hurry to the bedroom door."
    "That sounded like [bree.name] alright - like she was in pain."
    menu:
        "Barge into the room":
            "I don't hesitate for a moment."
            "I shoulder the door open and barrel into the room."
            show bg bedroom2 with hpunch
            "But as soon as I see what's going on inside, I stop dead."
            show bree surprised underwear at left5
            show anna surprised a at right5
            "There's [bree.name] and Anna, both looking back at me in surprise."
            "But what's really weird is their state of dress."
            "While Anna's fully dressed, [bree.name] only has on her underwear."
            "Well, technically she's covered with what look like electrodes."
            "But the only actual clothes she has on are her bra and panties!"
            mike.say "Oh..."
            mike.say "I..."
            mike.say "Sorry!"
            "I point helplessly at the open door behind me."
            "As if it's some kind of explanation for what's going on here."
            mike.say "I heard [bree.name] screaming just now."
            mike.say "And I thought you might need some help?"
            $ anna.love += 2
            $ anna.sub += 1
            $ bree.love += 6
            $ bree.sub += 1
        "Knock on the door":
            "Maybe I should just barge straight into the room?"
            "But the sound seems to have stopped for the moment."
            "Surely if it were that bad, [bree.name] would still be screaming?"
            "Unsure of what to do next, I choose to knock on the door."
            "Almost instantly, I hear the sound of Anna's voice on the other side."
            anna.say "Hey!"
            anna.say "Come on in!"
            show bg bedroom2
            bree.say "NO!"
            bree.say "Wait!"
            "I'm already following Anna's instructions as [bree.name] speaks."
            "And so, for better or worse, I already have the door open."
            "But as soon as I see what's going on inside, I stop dead."
            show bree surprised blush underwear at left5
            show anna at right5
            "There's [bree.name] and Anna, both looking back at me in surprise."
            "But what's really weird is their state of dress."
            "While Anna's fully dressed, [bree.name] only has on her underwear."
            "Well, technically she's covered with what look like electrodes."
            "But the only actual clothes she has on are her bra and panties!"
            mike.say "Oh..."
            mike.say "I..."
            mike.say "Sorry!"
            "I point helplessly at the open door behind me."
            "As if it's some kind of explanation for what's going on here."
            mike.say "I heard [bree.name] screaming just now."
            mike.say "And I thought you might need some help?"
            mike.say "Sorry for interrupting this..."
            mike.say "Well...whatever this is!"
            $ anna.love += 4
            $ bree.sub += 2
        "Listen at the door":
            "Maybe I should just barge straight into the room?"
            "But the sound seems to have stopped for the moment."
            "Surely if it were that bad, [bree.name] would still be screaming?"
            "Unsure of what to do next, I put my ear to the door."
            "I can definitely hear two voices in there."
            "Both of them sound female, so it's probably [bree.name] and Anna."
            "They're arguing about something I can't make out."
            "Something to do with electric currents and test subjects."
            "I struggle to hear more."
            show bg bedroom2
            show anna
            "But then the door swings open, and I'm face-to-face with Anna!"
            "And as soon as I see what's going on inside, I stop dead."
            show anna at right5 with move
            "There's [bree.name], looking back at me in surprise."
            "But what's really weird is her state of dress."
            show bree surprised underwear at left5 with dissolve
            "While Anna's fully dressed, [bree.name] only has on her underwear."
            "Well, technically she's covered with what look like electrodes."
            "But the only actual clothes she has on are her bra and panties!"
            mike.say "Oh..."
            mike.say "I..."
            mike.say "Sorry!"
            "I point helplessly at the open door behind me."
            "As if it's some kind of explanation for what's going on here."
            show bree annoyed
            mike.say "I was just going around the doors on this floor of the house."
            mike.say "You know, seeing if they needed to be cleaned?"
            mike.say "I don't think we clean them enough to be sanitary!"
            "Both [bree.name] and Anna shake their heads."
            $ anna.love -= 2
            $ anna.sub -= 1
            $ bree.love -= 6
            $ bree.sub -= 1
            "Clearly my excuse isn't good enough for them!"
    show bree annoyed blush
    show anna annoyed
    if bree.sexperience < 2:
        "[bree.name], still clad in only her underwear, looks like she wants me to leave."
        "But Anna, typically being a little ditzy, seems to miss this fact completely."
        "Instead she launches into an explanation of what's going on."
    anna.say "[hero.name], you can't just barge in here like that!"
    anna.say "We're conducting sensitive scientific research."
    anna.say "This is a prototype for a suit to control a person's every movement!"
    mike.say "Erm..."
    mike.say "That's amazing, Anna."
    mike.say "But why would you want to do that?"
    "Somehow the act of questioning their research seems to cause a change in [bree.name] and Anna."
    show anna normal
    show bree -blush normal
    "Anna looks almost shocked at the question, like it was the dumbest thing I could have asked."
    "And [bree.name] seems to forget the fact that she's still standing there in only her underwear."
    anna.say "What couldn't we use it for, [hero.name]?!?"
    bree.say "Yeah, [hero.name], the possibilities are endless!"
    bree.say "You could...well, you could have a surgeon control somebody from miles away."
    bree.say "Operate on a patient using another person's body!"
    anna.say "A musician could perform like that too."
    bree.say "Or a Kung Fu master fight with someone else's body!"
    mike.say "Well, when you put it like that..."
    show bree happy
    bree.say "So you agree - it'd be amazing?"
    show anna happy
    anna.say "And you want to help us make it happen, right?"
    mike.say "I...I suppose..."
    show bree normal
    bree.say "That's great - now take your clothes off!"
    mike.say "Wh...what the hell?!?"
    show anna normal
    anna.say "Isn't it obvious - [bree.name] and I are the scientists here."
    show anna annoyed
    anna.say "We can't keep experimenting on ourselves, it's unprofessional!"
    show bree annoyed
    bree.say "It's also undermining our objectivity too."
    bree.say "Plus we can't ask Sasha, because we know what her answer would be!"
    show bree normal
    show anna normal
    anna.say "So that makes you..."
    mike.say "The last resort!"
    anna.say "No, no, no!"
    show anna happy
    anna.say "It makes you a scientific pioneer!"
    show anna normal
    "I look into Anna's huge, innocent eyes as she smile up at me."
    "Damn it - why does she have to be so irresistibly cute?"
    "I tear my gaze away from Anna, only to have it fall on [bree.name] instead."
    "Who's still standing there in her underwear, smiling at me too."
    "Smiling at me with her sexy body on show!"
    "I take a deep breath and then let it out, feeling utterly defeated."
    mike.say "Okay, okay..."
    mike.say "Let's get it over with!"
    "[bree.name] and Anna clap their hands together in delight."
    "And then they begin to tug the electrodes off of [bree.name]'s body."
    "At the same time I start to strip off my own clothes."
    "It doesn't take long for them to be ready to start experimenting on me."
    show bree b at center, zoomAt(1.5, (340, 1040))
    show anna b at center, zoomAt(1.5, (940, 1040))
    with dissolve
    "I stand still, eyeing [bree.name] and Anna nervously as they advance, holding the electrodes..."
    if hero.fitness > 50:
        "The girls fuss around me, attaching the things to various parts of my body."
        show bree b at center, zoomAt(1.5, (240, 1040))
        show anna b at center, zoomAt(1.5, (1040, 1040))
        with dissolve
        "More than once I think I catch them stopping to poke me in the firmer parts."
        "I can feel their fingers lingering for far longer than they need to as well."
        show bree b at center, zoomAt(1.5, (140, 1040))
        show anna b at center, zoomAt(1.5, (840, 1040))
        with dissolve
        "Wherever [bree.name] and Anna stick the electrodes, they seem to want to take their time."
        "And it feels more like I'm getting a massage than being prepared for an experiment!"
        $ anna.love += 2
        $ bree.love += 2
    else:
        "The girls fuss around me, attaching the things to various parts of my body."
        show bree b at center, zoomAt(1.5, (240, 1040))
        show anna b at center, zoomAt(1.5, (1040, 1040))
        with dissolve
        "More than once I think I catch them stopping to poke me in softer parts."
        "And I'm convinced they're giggling at how pudgy I've let myself become recently."
        show bree b at center, zoomAt(1.5, (140, 1040))
        show anna b at center, zoomAt(1.5, (840, 1040))
        with dissolve
        "But I do the best I can to ignore it and wait for them to complete the task."
    "I should have seen this coming, a perfectly natural reaction to what's going on."
    "After all, I'm standing here in only my underwear, two hot girls touching me all over."
    "Of course I was going to get hard before too long, as hard as I can possibly get."
    show bree b zorder 1 at center, zoomAt(1.5, (-340, 1040))
    show anna b zorder 2 at center, zoomAt(1.65, (640, 1380))
    with dissolve
    "And I might have been able to get away with it if Anna wasn't kneeling down in front of me too!"
    show anna surprised
    anna.say "Oh..."
    anna.say "Oh my!"
    show anna blush
    anna.say "Maybe you should try to relax, [hero.name]?"
    "I can't help blushing as Anna giggles away."
    mike.say "Anna!"
    mike.say "I can't help it, okay?!?"
    "I hear [bree.name] tutting from where she's standing behind me."
    bree.say "She's right, [hero.name]."
    bree.say "It's cute that you're nervous."
    show bree b at center, zoomAt(1.5, (340, 1040)) with ease
    bree.say "But..."
    hide bree
    show bree underwear surprised b zorder 1 at center, zoomAt(1.5, (340, 1040)), vshake
    "[bree.name] trails off as she walks around to my front and see's what the problem is."
    show bree b blush at zoomAt(1.5, (440, 1040)) with ease
    "She leans in close to Anna, looking like she's deep in thought."
    bree.say "Ah, Anna..."
    bree.say "Can I have a word with you?"
    show anna happy -blush
    "Anna smiles and nods."
    anna.say "Sure, [bree.name]!"
    anna.say "What's up?"
    show bree annoyed
    "[bree.name] looks a little exasperated and nods towards the corner of the room."
    hide anna
    show anna b surprised at center, zoomAt(1.5, (840, 1040))
    "Anna's eyes go wide as she realises that the other girl wants to speak in private."
    hide bree
    hide anna
    with moveoutright
    "I watch as they hurry into the corner, turning their backs on me."

    mike.say "Erm..."
    mike.say "Maybe this isn't such a great idea after all?"
    mike.say "I mean, we can forget all about it if you want?"
    mike.say "That's fine by me!"
    show bree underwear at left4
    show anna at right4
    with moveinright
    "Suddenly [bree.name] and Anna emerge from the corner."
    "And they waste no time in dismissing my offer."
    show bree annoyed blush
    bree.say "No way, [hero.name]!"
    bree.say "We already hooked you up with the electrodes."
    show anna happy
    anna.say "And we figured out a solution for you little problem too!"
    "As Anna says this, a smile spreads across her face."
    "But I can see that [bree.name] looks more than a little embarrassed."
    show anna b at center, zoomAt(1.5, (740, 1040))
    "Perhaps that's why it's Anna who walks over and takes hold of my shorts."
    "Before I can say a word, she pulls them down, exposing my cock."
    mike.say "H...hey!"
    mike.say "What are you..."
    hide bree
    hide anna
    show college oral
    with fade
    if renpy.has_label("college_harem_achievement_2") and not game.flags.cheat:
        call college_harem_achievement_2 from _call_college_harem_achievement_2
    "My protests trail off as [bree.name] and Anna both kneel in front of me."
    "Together they reach out and begin to gently caress my cock."
    anna.say "Chill out, [hero.name]."
    anna.say "We need you relaxed for our experiments to work."
    bree.say "She's right, [hero.name]."
    bree.say "This is all in the name of science...I guess."
    show college oral ahandjob annatongue
    "[bree.name] and Anna waste no time in working away at my cock."
    "Their touch starts out gentle, but soon becomes firmer."
    "And I gasp at the sensation of them squeezing my balls."
    show college oral -ahandjob bhandjob
    "[bree.name] seems to take care of working around the edges."
    show college oral handonbree breeclose
    "She tickles and teases, adding a subtle undertone to the proceedings."
    show college oral ahandjob bhandjob annaclose
    "But Anna's the one that really puts the effort in when it come to the shaft."
    "Her hand moves up and down constantly, never still for a moment."
    show college oral handonanna bhandonleg
    "And somehow she seems to know exactly how light or heavy to make her touch."
    "I feel myself gasping and groaning the whole time."
    if anna.sub > 50 and bree.sub > 50:
        "[bree.name] and Anna suddenly kick things up a level."
        "I gasp in anticipation as they both lean in and open their mouths."
        show college oral bj ahandbj breeopen
        "And the feeling a moment later is almost beyond words."
        "[bree.name]'s still working her way around the edges."
        "She still tickles and teases, but this time it's with her tongue and lips."
        "I can feel her licking and sucking on my balls, paying close attention to her task."
        "Anna, on the other hand, makes my cock the centre of her attention."
        "She slowly licks her way from the bottom to the top."
        "And she punctuates her progress with loud kisses followed by wicked giggles."
        "Tongue moves constantly, dexterous and lithe."
        "I'm almost panting by now, my heart pounding."
        "The volume goes up as soon as she reaches the head."
        "That's when Anna swallows it without hesitation."
        "My breathing becomes heavy and laboured in response."
        "Looking down, I see Anna's head moving back and forth."
    "More than once I swear that Anna's going to make me cum."
    "But all that happens is the intensity of my sensations increasing."
    show college oral hj ahandjob
    "All the time she's casting glances up at me as she works away."
    show college oral annaopen
    "I can see the mischief in her eyes, the delight at what she's doing."
    "Anna's loving the fact that I'm so exposed and helpless right now."
    "She's got me right where she wants me."
    show college oral annatongue pleasure
    "And I can see something else in her eyes too."
    "It's the knowledge that she's about to make me cum!"
    show college oral hj ahandjob cumshot with vpunch
    "[bree.name] and Anna are kneeling right in front of me when it happens."
    with vpunch
    "So there's no way they can escape getting showered with cum."
    show college oral hj -cumshot cum face breeclose annaclose
    if anna.lesbian > 5 and bree.lesbian > 5:
        "The sticky, white streamers paint their faces a moment later."
        "And both girls gasp in surprise, then begin to laugh."
        show college oral hand breeopen annaopen neutral
        "Anna's head darts forwards and she licks the drops from [bree.name]'s lips."
        "This seems to trigger something between them, as [bree.name] returns the favour."
        "A moment later, [bree.name] and Anna are kissing as though their lives depended on it!"
        "Their lips press together, tongues in and out of each other's mouths."
        "All I can do is watch in amazement, enjoying what's happening before me."
        $ anna.lesbian += 1
        $ bree.lesbian += 1
    else:
        "The sticky, white streamers paint their faces a moment later."
        "And both girls gasp in surprise as the cum starts to run down their cheeks."
        show college oral hand breeopen annaopen neutral
        "Then Anna breaks the silence, bursting out in a peal of laughter."
        "Soon [bree.name] can't help joining in too, and then I relent as well."
    anna.say "I think we blew-off his tension!"
    bree.say "Is that the scientific term, Anna?"
    mike.say "It was a practical experiment, at least..."
    hide college
    show bree underwear at left5
    show anna b at right5
    with fade
    bree.say "Right, I'll connect the electrodes to the power source."
    bree.say "You get the subject into position, Anna!"
    anna.say "Okay, [hero.name]!"
    anna.say "We're going to need you laid on the bed!"
    "And just like that the fun's over."
    "It's back to the prospect of being [bree.name] and Anna's human Guinea Pig for me!"
    menu:
        "I have a bad feeling about this":
            "By now I've had enough time to let the reality of this sink in."
            "And all I can think of is the fact that these guys are rank amateurs."
            "That and the vivid memory of [bree.name] screeching like a banshee just now!"
            "I begin to shake my head, already pulling the electrodes off my skin."
            mike.say "I changed my mind, guys."
            mike.say "I want out!"
            show anna surprised
            anna.say "HEY!"
            anna.say "What are you doing?!?"
            show bree surprised
            bree.say "[hero.name], you can't be serious?!?"
            bree.say "We REALLY need your help here!"
            "Once I have the last of the electrodes off, I scoop up my clothes."
            "Even the prospect of pleasing two hot girls isn't worth the risk."
            mike.say "Nope, no way, not going to happen."
            mike.say "My mind's made up - find yourselves another victim!"
            show anna angry
            anna.say "Oooh...you jerk!"
            show bree angry
            bree.say "Yeah, thanks for nothing, [hero.name]!"
            "I try as best I can to ignore their protests as I stride out of [bree.name]'s room."
            "And I tell myself that they'll get over it soon enough."
            $ anna.love -= 6
            $ anna.sub -= 1
            $ bree.love -= 6
            $ bree.sub -= 1
            return
        "Go easy on me" if hero.knowledge > 60:
            mike.say "Okay, I'm ready!"
            mike.say "Just go easy on me, okay?"
            "I nod, trying to look as confident as I possibly can."
            "But I think [bree.name] and Anna can sense how nervous I am."
            "They try to make out like they don't, which is kind of them."
            show anna happy
            anna.say "Don't worry, [hero.name]."
            anna.say "We'll be as gentle as we can with you."
            show bree happy
            bree.say "Trust us, you're in safe hands!"
            mike.say "Ah...okay, guys."
            mike.say "Should we agree on a safe-word or something?"
            "[bree.name] and Anna exchange glances at this, giggling at my nerves."
            show anna normal
            show bree normal
            "I let Anna show me over to the bed and lie me down in top of the covers."
            "And in the background I hear [bree.name] fiddling with various dials and switches."
            anna.say "All ready over here, [bree.name]!"
            bree.say "Same here, Anna - let's do this!"
            $ anna.love += 6
            $ anna.sub -= 1
            $ bree.love += 6
            $ bree.sub -= 1
        "I'm ready" if hero.fitness > 60:
            mike.say "Okay, I'm ready!"
            mike.say "Electrify me!"
            "I see [bree.name] and Anna's eyes go wide at the tone of my voice."
            show bree surprised
            show anna surprised
            "They exchange glances, and I swear I see a thrill pass between them."
            "I guess they weren't prepared for me to be this eager."
            bree.say "Calm down, [hero.name]!"
            show bree normal
            bree.say "We're supposed to be the mad scientists here!"
            anna.say "Yeah, [hero.name]...what [bree.name] said!"
            "But as she leads me over to the bed, Anna leans in close."
            "She whispers in my ear, clearly not wanting [bree.name] to hear her."
            show anna blush
            anna.say "This is going to be SO cool, [hero.name]!"
            anna.say "When you said that just now..."
            anna.say "Well...it felt like you were electrifying me...downstairs!"
            "I let Anna show me over to the bed and lie me down in top of the covers."
            show anna normal
            "And in the background I hear [bree.name] fiddling with various dials and switches."
            anna.say "All ready over here, [bree.name]!"
            bree.say "Same here, Anna - let's do this!"
            $ anna.love += 2
            $ anna.sub += 3
            $ bree.love += 2
            $ bree.sub += 3
    $ game.flags.sciencehelper = True
    "All I can do now is take a deep breath, steeling myself for what lies ahead."
    "But part of me can't help wondering about what happens if something does go wrong."
    "If they kill me, does my body get donated to science by default?"
    if anna.sub < 50 and bree.sub < 50:
        "What follows is an unnerving experience to say the least."
        "As soon as [bree.name]'s powered-up the equipment, my body is not my own!"
        "I'm forced to lie there, helpless on [bree.name]'s and at their whims."
        "[bree.name] and Anna don't seem to be in a hurry either."
        "They take their time in making my limbs jerk this way and that."
        "And it seems like they're as interested in keeping me paralysed as they are controlling my movements too!"
        "All the time they're standing over me, making notes and chatting to each other."
        "Sure, they try to keep it all sounding like it's a scientific experiment."
        "But I can see the way the corners of their mouths keep turning up."
        "They're enjoying every moment that they have me at their mercy!"
        "And I swear that I can see them realising the possibilities of this situation too!"
        "So as soon as they declare the experiment over, I hop off the bed and begin to pull off the electrodes."
        show anna surprised
        anna.say "Aw..."
        anna.say "Going so soon, [hero.name]?"
        show bree sad
        bree.say "Yeah, we've only just gotten started!"
        "Once I have the last of the electrodes off, I scoop up my clothes."
        show anna normal
        show bree normal
        "Even the prospect of pleasing two hot girls isn't worth another round of electrical torture."
        mike.say "Oh no, no way!"
        mike.say "I made my contribution to science for one day!"
        mike.say "Good luck with the contest, okay?"
        "[bree.name] and Anna look a little disappointed."
        "But they force themselves to nod and smile all the same."
        "After all, I did do what they asked."
    else:
        "But all such thoughts vanish from my mind a moment later."
        "And that's because I see [bree.name] walking over to the bed, unhooking her bra!"
        "She nods to Anna as she drops it on the floor."
        "And then she begins to pull down her panties too!"
        show bree naked
        "Anna doesn't seem at all concerned by this rather unscientific development."
        "In fact she's smiling the whole time, like she knew this was going to happen."
        mike.say "Ah, guys..."
        mike.say "What exactly is happening here?"
        mike.say "I mean, do you normally perform experiments naked?!?"
        bree.say "Do you normally fuck with all your clothes on?"
        "[bree.name] raises an eyebrow as she climbs onto the bed."
        hide bree
        hide anna
        show college cowgirl bedroom2 dickout
        with fade
        "I don't think the electrodes are keeping me from moving right now."
        "But still I can't move a single muscle as [bree.name] straddles me."
        mike.say "Y...you're going to have sex with me?"
        mike.say "While I'm hooked up to your experiment?!?"
        "[bree.name] waggles a finger in my face to shut me up."
        "And then she nods to Anna, who busies herself with the equipment."
        bree.say "It's perfectly safe, [hero.name], trust me."
        bree.say "So long as we keep the current low enough."
        bree.say "All we'll feel is a pleasant tingle the whole time!"
        anna.say "There you go, [bree.name]."
        anna.say "That should be enough to get him stiff!"
        "Now I can definitely feel the electrodes working on my body."
        "And it's reassuringly close to what the girls claimed I'd feel."
        "A tingling in my muscles that, while weird, isn't actually unpleasant."
        "I smile at [bree.name], trying to show her that I'm not afraid."
        "But then my eyes widen as I see what effect it's having on a certain part of my anatomy."
        "My cock is swiftly stiffening, rising upwards in a manner that reminds me of something."
        "And then it hits me - it's like Frankenstein's monster, rising from the slab!"
        bree.say "Mmm..."
        bree.say "We have lift off!"
        bree.say "Now let's put that thing to good use!"
        "Without asking for permission, [bree.name] reaches out and grabs my cock."
        show college cowgirl -dickout vaginal
        "She rubs it hard against the lips of her pussy."
        "And the effect is instant, making her moan with pleasure."
        show college cowgirl close
        bree.say "Oh fuck..."
        bree.say "Oh yeah..."
        anna.say "What's it like, [bree.name]?"
        anna.say "Can you actually feel it?"
        show college cowgirl normal
        bree.say "You bet I can!"
        bree.say "It's like we turned him into a human vibrator!"
        "I open my mouth to protest, not liking the mental image that term creates."
        "But I guess I'm still being used as an experimental subject, not getting a say."
        "Because [bree.name] presses my cock even harder against her slick pussy."
        "And her lips yield to the pressure, letting her slide down and onto me."
        "It's now that I begin to feel a subtle change in the electrical current."
        "I mean, that's obviously not ALL that I feel!"
        "The sensation of my cock sinking into [bree.name] is breath-taking."
        show college cowgirl anna electremote
        "But Anna must have done something to the equipment."
        show college cowgirl turnon
        "Because the electricity starts to pulse, coming in short bursts."
        "This makes me tense and then relax under [bree.name]."
        "And of course, it drives my cock into her at the same time too!"
        "The experience is pretty weird, feeling my body being used like this."
        "I get all of the normal sensations of making love."
        "But I'm simply not in control, like Anna's using a remote control on me!"
        "All I can do is lie back on the bed and watch what's happening."
        show college cowgirl -anna -electremote
        "This makes what I'm feeling that much more intense too."
        "I have nothing to distract me from the sensations of fucking [bree.name]."
        "Nothing to keep me from watching the way she twitches from the thrusts."
        show college cowgirl close
        "[bree.name] is yelping and panting with each jolt of electricity."
        "And I guess that means some of the current is flowing into her too!"
        "I confess that I'd almost forgotten all about Anna."
        show college cowgirl anna fingering normal
        "But then she appears over [bree.name]'s shoulder."
        "She has something in her hand that she waves from side to side."
        "It's a pink egg vibrator, specifically [bree.name]'s vibrator!"
        "I can't see what Anna's doing back there, but I can guess."
        show college cowgirl anna vibremote analvib evil close
        "And my suspicions are confirmed a moment later when I see [bree.name] stiffen."
        "I swear I can feel the egg as Anna sticks it into [bree.name]'s ass."
        "Her muscles put up a token resistance, but then even this melts away to nothing."
        "With Anna working [bree.name] from one side and me the other, she can't hold on too long."
        show college cowgirl ahegao lust
        "Already sweating and panting, [bree.name]'s cheeks turn bright red."
        bree.say "I...I'm gonna..."
        bree.say "I'm gonna cum..."
        bree.say "Right now...here I go!"
        "[bree.name] grinds herself down and into me as she loses it."
        "I haven't been in control of my body this whole time."
        "And so there's no way I can keep myself from cumming too."
        show college cowgirl cum with vpunch
        "I shoot my load into [bree.name], making her wail even louder than before."
        "She squeezes her breasts, pinching her nipples desperately."
        show college cowgirl -vaginal dickout grab close -turnon surprised
        "Then she collapses atop me, her face an inch from my own."
        mike.say "D...did we do well, [bree.name]?"
        mike.say "Was the experiment...a success?"
        show college cowgirl normal
        bree.say "I...I definitely broke new ground..."
        bree.say "Discovered new things..."
        anna.say "That was SO great, you guys!"
        anna.say "With an experiment like this, we're gonna win first prize for sure!"
    scene bg black with dissolve
    $ Harem.join_by_name("college", "anna", "bree")
    return

label science_project_04:
    scene bg university
    "When I next see [bree.name] and Anna together, I can't help wincing a little."
    "The memory of becoming part of their science project is still quite fresh."
    "But I try my best to ignore all of that and give the pair a friendly smile."
    show bree at left5
    show anna at right5
    with dissolve
    "As it looks like they're in good spirits as they hurry up to speak to me."
    show anna happy
    anna.say "Hey, [hero.name]!"
    anna.say "We really want to thank you for all your help!"
    bree.say "Yeah, [hero.name], Anna's right."
    bree.say "Without you, we'd never have teamed up for the contest."
    mike.say "Does that mean what I think it means?"
    show anna normal
    "Anna nods, almost jumping up and down on the spot."
    "But [bree.name]'s a little more reserved, just nodding and smiling."
    bree.say "If you think it means we won, then yeah!"
    show anna happy
    anna.say "We won, we won, we won!"
    "I can't help smiling at the news."
    "And it feels great knowing I had a hand in it too."
    mike.say "That's great news, guys."
    mike.say "So all you have to do now is enjoy your prize, right?"
    show bree blush
    "At this, I see [bree.name]'s cheeks flush red."
    show bree annoyed
    "She looks down at the floor, suddenly unable to meet my eye."
    show anna normal
    anna.say "Oh no, that's not it, [hero.name]!"
    anna.say "We're an internet sensation as well!"
    mike.say "Huh?"
    mike.say "What do you mean, Anna?"
    show bree angry
    bree.say "Anna!"
    bree.say "He doesn't need to see that!"
    "But all of [bree.name]'s pleading is in vain."
    "Because Anna's already too carried away to hear a word she's saying."
    "Instead she eagerly explains herself to me, oblivious to [bree.name]'s objections."
    anna.say "It's the video of the experiment, [hero.name]."
    anna.say "It's gone viral!"
    "Before [bree.name] can say another word, I already have my phone out."
    "And it doesn't take me long to find the video in question either."
    show bree dazed
    bree.say "Anna, he doesn't need to see that!"
    anna.say "Aw...why not, [bree.name]?"
    anna.say "I think it's pretty cool that we're trending online!"
    mike.say "Yeah, [bree.name] - what's the big deal?"
    mike.say "If you guys are getting a fanbase, I want to be a part of it too!"
    "As soon as the video starts to play, I recognise the amphitheatre at the university."
    hide anna
    hide bree
    show college experiment look
    with fade
    "[bree.name] and Anna are on the stage in front of a pretty impressive audience."
    "[bree.name] reclined in a chair and Anna standing by her side."
    "I chuckle and shake my head at the sight of Anna, wearing a white lab-coat."
    show college experiment nervous
    "In contrast, [bree.name] has on only a lycra bodysuit that leaves little to the imagination."
    "It's patterned to look like something a mecha pilot might wear."
    show college experiment look
    "And she looks amazingly hot in it too!"
    mike.say "Love the outfit, [bree.name] - very anime!"
    bree.say "You're supposed to be watching the experiment, [hero.name]."
    bree.say "Not staring at what I have on!"
    anna.say "Hey - what about me?!?"
    mike.say "Okay, Anna, okay."
    show college experiment wink thumb
    mike.say "You look cute too!"
    "I turn my attention back to the video as the experiment gets underway."
    show college experiment nervous -thumb
    "At first the results are less than spectacular and the crowd remains quiet."
    "Anna fiddles with the controls and [bree.name] begins to move in a jerky fashion."
    show college experiment rtense
    "Everything seems to be going according to plan at first."
    "[bree.name]'s arms and legs lurch up and down as Anna works the controls."
    show college experiment -rtense ltense
    "And [bree.name] seems as surprised as anyone to see them moving of their own accord."
    show college experiment -ltense confused lup with hpunch
    "But then there's a burst of sparks from the remote control and an audible bang."
    show college experiment panic rup
    "Anna yelps and drops the malfunctioning device on the stage."
    show college experiment electrofx pleasure
    "Meanwhile, [bree.name] seems to be experiencing a similar malfunction herself."
    "She seems to lose control of her body below the waist."
    "It twitches and spasms as the electrodes spark and fizzle."
    show college experiment blush
    "All the time, [bree.name] keeps letting out yelping squeaks."
    "The sound is vaguely familiar at first, but I just can't place it."
    show college experiment legup
    "Then, as I watch her jerk more and more, it dawns on me."
    show college experiment wet
    "[bree.name]'s acting like she's being stimulated - stimulated down there!"
    "The entire audience seems to have been on the same wavelength as me."
    show college experiment -legup confused
    "Because as [bree.name]'s pleasure becomes more obvious, they begin to react."
    "There are gasps of astonishment as they realise what's happening."
    "And then spontaneous applause can be heard beginning to spread."
    show college experiment climax legup normal
    "Pretty soon there's cheering too, loud and genuine."
    "It almost drowns out the sound of [bree.name] as she loses it on stage!"
    hide college
    show bree annoyed blush at left5
    show anna happy at right5
    with fade
    "When the video ends, I can't help grinning at [bree.name]."
    "Her cheeks are burning with shame by now."
    "But Anna seems oblivious to the other girl's embarrassment."
    "So I choose to keep all the comments that spring to mind to myself."
    "[bree.name] and Anna won the competition."
    "And that's what really matters."
    "Even if it wasn't in a way they were expecting..."
    return

label anna_bree_propose_male:
    show anna a normal at right5
    show bree normal at left5
    "All I have in my pocket right now is a couple of little boxes."
    "And inside of them are two rings that weigh next to nothing."
    "Which is kind of galling, when I remember what they actually cost!"
    "But somehow they feel like a couple of bowling balls weighing me down."
    "I keep looking at Anna and [bree.name] as they stroll along."
    "They're chatting away like they don't have a care in the world."
    "And here I am, sweating from the stress of waiting."
    "Waiting for just the right moment to go down on one knee."
    "Oh fuck!"
    "There it is - the perfect moment!"
    "Fumbling for the boxes that contain the rings, I start to kneel down."
    "It's [bree.name] that sees what I'm doing first."
    "She falls silent, staring at me in surprise."
    "But Anna seems to be oblivious, and she keeps on babbling away."
    anna.say "Anyway..."
    anna.say "I told her that, but she wasn't having any of it!"
    anna.say "And then..."
    show anna a annoyed
    anna.say "[bree.name], are you even listening to me?!?"
    bree.say "[hero.name]..."
    bree.say "What are you doing?"
    "Anna follows [bree.name]'s gaze down to where I'm kneeling."
    "Then her eyes go wide with surprise too."
    show anna b surprised at startle
    show bree surprised
    anna.say "Ooh!"
    show anna annoyed b
    anna.say "Are you making fun of me again?"
    anna.say "I already told you, [hero.name]..."
    show anna angry b
    anna.say "Mocking short people isn't cool!"
    "It's about then the pair of them seem to notice the rings in my hand."
    show anna surprised b
    "And then they look more surprised than ever!"
    mike.say "Anna..."
    mike.say "[bree.name]..."
    mike.say "You've made me so happy."
    mike.say "In fact, you've made my life complete."
    mike.say "Will you marry me?"
    show anna blush b
    show bree normal blush
    "Anna and [bree.name] both look like they're on the brink of something big."
    "Like they're about to explode, but I don't know in what way."
    "Will it be the answer that I want to hear?"
    "Or am I about to get my heart broken?"
    if anna.love >= 195 and bree.love >= 195:
        "It's Anna that starts jumping up and down first."
        "And she's squealing like a teenage girl at a boy-band concert too!"
        show anna happy b at startle
        anna.say "Oh god!"
        anna.say "Oh fuck!"
        anna.say "Yes, yes I will!"
        "[bree.name] seems more than a little shocked at Anna's reaction."
        "But she soon warms up to the idea herself."
        show bree happy
        bree.say "Wow, [hero.name]!"
        bree.say "You kind of caught me on the hop there."
        bree.say "Yes, of course I'll marry you!"
        "Part of me can't believe what's happening right now."
        "They both said yes!"
        "Which leaves me in a daze as I get to my feet."
        "Anna and [bree.name] hold out their hands for me."
        "And I slide the rings onto their fingers."
        mike.say "It's really happening!"
        mike.say "Were getting married!"
        anna.say "And it'd gonna be the best, [hero.name]!"
        bree.say "You got that right, Anna!"
        $ anna.set_fiance()
        $ bree.set_fiance()
    elif anna.love < 195 and bree.love < 195:
        "It's Anna that starts shaking her head first."
        "And she's backing away like she's afraid of the rings too."
        show anna b annoyed at startle
        anna.say "Ooh..."
        anna.say "Oh no!"
        show anna b cry
        anna.say "I don't want to get married!"
        anna.say "And you can't make me!"
        show bree -blush
        "[bree.name] seems more than a little shocked at Anna's reaction."
        "But she doesn't look too happy about the idea herself."
        show bree annoyed
        bree.say "Don't be silly, Anna."
        bree.say "Nobody's going to make you get married."
        bree.say "You can just choose not to do it - like me!"
        "Part of me can't believe what's happening right now."
        "They both said no!"
        "Which leaves me in a daze as I get to my feet."
        mike.say "I..."
        mike.say "I don't know what to say, guys!"
        mike.say "I thought we were pretty solid, you know?"
        mike.say "That we were definite marriage material."
        "Anna and [bree.name] both seem to show me some sympathy."
        "But all the same, I can see they're not about to change their minds."
        show anna b normal
        anna.say "I don't wanna get married, [hero.name]!"
        anna.say "I'm too young for that!"
        show bree normal
        bree.say "I just don't think it's the right time."
        bree.say "Sorry, but that's just how I feel."
        "All I can do is shrug and put the rings away again."
        "Now I don't know if I should return them in the hope of getting a refund."
        "Or if I should hang onto them in the hope of Anna and [bree.name] changing their minds."
        $ anna.love -= 25
        $ anna.sub -= 25
        $ bree.love -= 25
        $ bree.sub -= 25
    elif bree.love < 195:
        "It's Anna that starts jumping up and down first."
        "And she's squealing like a teenage girl at a boy-band concert too!"
        show anna b happy at startle
        anna.say "Oh god!"
        anna.say "Oh fuck!"
        anna.say "Yes, yes I will!"
        show bree -blush
        "[bree.name] seems more than a little shocked at Anna's reaction."
        "But she doesn't look too happy about the idea herself."
        show bree annoyed
        bree.say "Don't be silly, Anna."
        bree.say "Getting married is a big decision."
        bree.say "You can just choose not to do it - like me!"
        "Part of me can't believe what's happening right now."
        "One said yes and the other said no!"
        "Which leaves me in a daze as I get to my feet."
        mike.say "I..."
        mike.say "I don't know what to say, guys!"
        mike.say "I thought we were pretty solid, you know?"
        mike.say "That we were definite marriage material."
        "Anna and [bree.name] both seem to show me some sympathy."
        "But neither of them is about to change their answer to please the other."
        show bree normal
        bree.say "I just don't think it's the right time."
        bree.say "Sorry, but that's just how I feel."
        anna.say "But, but..."
        anna.say "We can still get married, right?"
        mike.say "I guess so, Anna."
        show anna b happy
        "That leaves me with no idea of what should happen next."
        "Sure, I want to marry Anna, but what about [bree.name]?"
        "Can we still be a threesome if she's not involved in the marriage?"
        $ bree.love -= 25
        $ bree.sub -= 25
        $ anna.set_fiance()
    elif anna.love < 195:
        "It's Anna that starts shaking her head first."
        "And she's backing away like she's afraid of the rings too."
        show anna b annoyed at startle
        anna.say "Ooh..."
        anna.say "Oh no!"
        show anna b cry
        anna.say "I don't want to get married!"
        anna.say "And you can't make me!"
        "[bree.name] seems more than a little shocked at Anna's reaction."
        "But her own answer is totally different."
        show bree happy
        bree.say "Wow, [hero.name]!"
        bree.say "You kind of caught me on the hop there."
        bree.say "Yes, of course I'll marry you!"
        "Part of me can't believe what's happening right now."
        "One said yes and the other said no!"
        "Which leaves me in a daze as I get to my feet."
        mike.say "I..."
        mike.say "I don't know what to say, guys!"
        mike.say "I thought we were pretty solid, you know?"
        mike.say "That we were definite marriage material."
        "Anna and [bree.name] both seem to show me some sympathy."
        "But neither of them is about to change their answer to please the other."
        anna.say "I don't wanna get married, [hero.name]!"
        show anna b annoyed
        anna.say "I'm too young for that!"
        bree.say "I'd still like to marry you, [hero.name]."
        bree.say "We can do that, right?"
        mike.say "I guess so, [bree.name]."
        show bree happy
        "That leaves me with no idea of what should happen next."
        "Sure, I want to marry [bree.name], but what about Anna?"
        "Can we still be a threesome if she's not involved in the marriage?"
        $ anna.love -= 25
        $ anna.sub -= 25
        $ bree.set_fiance()
    return

label anna_bree_male_ending:

    if renpy.has_label("college_harem_achievement_3") and not game.flags.cheat:
        call college_harem_achievement_3 from _call_college_harem_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "The chapel is packed with guests here to support the two brides and the groom."
    "Looking around, I can see my own friends and family out there."
    "But I also recognise some of the faces that are here for Anna and [bree.name] too."
    "Of course Sasha's sitting right there, front and centre."
    "I mean, she lives with [bree.name] and myself, obviously."
    "But she's also in the same band as Anna too, so they're good friends."
    "And sitting right beside her is Kleio, the spikey vocalist from the band too."
    "The two of them catch my eye as I scan the crowd."
    "Sasha smiles and gives me a wave, while Kleio sticks out her tongue and two fingers."
    "But I know her well enough not to be offended, that's just her way of being friendly!"
    "I'm thinking about returning the gesture when the chapel fills with music."
    "Instantly my attention is drawn to the doors, as they open to admit my brides."
    show anna b wedding zorder 4 at center, zoomAt (1.0, (880, 740))
    show bree wedding zorder 5 at center, zoomAt (1.0, (400, 740))
    with fade
    "Anna and [bree.name] walk in together, coming down the aisle side by side."
    show anna b at center, traveling (1.25, 5.0, (860, 900))
    show bree at center, traveling (1.25, 5.0, (420, 900))
    "Naturally my eyes are drawn to [bree.name] first, simply because of her height."
    "Her blonde hair bounces as she walks and her blue eyes are sparkling."
    "And the cut of her dress is perfect."
    "It manages to show off her figure while remaining elegant."
    if bree.is_visibly_pregnant:
        "Even the curve of her belly is taken into account."
        "Celebrating, rather than trying to hide the fact she's pregnant."
    "Then my eyes turn to Anna, and I'm reminded of how much I adore her."
    "Petite and full of life, she's impossible to ignore."
    "And that dress makes her look better than ever!"
    if anna.is_visibly_pregnant:
        "Plus it shows off her belly as well."
        "And I love the sight of Anna carrying my baby."
        "It add a womanly aspect to her normally girlish character."
    show anna b at center, traveling (1.75, 5.0, (840, 1200))
    show bree at center, traveling (1.75, 5.0, (440, 1200))
    "My chance to observe them comes to an end as they reach the altar."
    "Then it's all about smiles and blushes as we get ready to do this thing."
    "Priest" "Ahem..."
    show anna normal
    show bree normal
    "At the sound of the priest's cough, the whole chapel stands to attention."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these three people..."
    "Priest" "In the bonds of holy matrimony."
    "You know what happens next."
    "The priest goes through all the usual lines."
    "And nothing really happens until it comes to the vows."
    "So let's skip ahead a little..."
    "Priest" "Do you, Anna..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    show anna happy at startle
    anna.say "You bet I do!"
    "Priest" "Erm..."
    "Priest" "Yes, yes - very good."
    "Priest" "Do you, [bree.name]..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    show bree happy at startle
    bree.say "I do."
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    mike.say "I do."
    "Priest" "I call upon all those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "Why these three may not be married..."
    "Priest" "Speak now, or forever hold your peace!"
    "Anna, [bree.name] and I exchange nervous glances and a few chuckles."
    "But luckily for us, nobody chooses that moment to speak up."
    "Priest" "Very well."
    "Priest" "It is therefore my pleasure to pronounce you married."
    "Priest" "You may celebrate in a way that you find fitting."
    "I understand the choice of words the priest just used."
    "But for us, that's never going to be anything other than a kiss!"
    show anna b happy zorder 4 at center, zoomAt (2.0, (820, 1340))
    show bree happy zorder 5 at center, zoomAt (2.0, (460, 1340))
    with hpunch
    "Anna, [bree.name] and I embrace each other and share one that goes on for quite a while."
    "It's like none of us wants this moment to end, or to be the first one to let go."
    "So it lingers on for a long time, and I enjoy every single second of it too!"

    scene bg park
    show anna happy at right5, startle
    show bree at left5
    with fade
    anna.say "Ooh!"
    anna.say "This is going to be SO cool, [bree.name]!"
    show anna normal
    bree.say "It is?"
    show anna evil
    anna.say "Of course it is!"
    anna.say "We get to do the talking for once."
    show anna normal
    anna.say "Instead of [hero.name] telling everyone how it is!"
    bree.say "Hmm..."
    show bree happy
    bree.say "I guess you've got a point, Anna."
    bree.say "We should get a chance to tell our side of the story."
    show anna normal
    anna.say "And we both know who we need to start out by thanking."
    show bree normal
    bree.say "We do?"
    anna.say "Sure we do!"
    anna.say "And it's Sasha!"
    show bree surprised at startle
    bree.say "SASHA?!?"
    bree.say "What's she got to do with this?"
    anna.say "Oh, come on, [bree.name] - you know better than that!"
    anna.say "If Sasha hadn't moved in with you, she'd never have introduced me to [hero.name]."
    show bree normal
    bree.say "Well that is true."
    bree.say "And if she hadn't been around the house..."
    show bree evil
    bree.say "Well, [hero.name] might not have realised how much hotter I am than her!"
    show anna annoyed at vshake
    anna.say "BREE!"
    show bree wink
    bree.say "Kidding!"
    show anna annoyed
    anna.say "Alright, [bree.name] - stop being mean!"
    show anna normal
    show bree normal
    bree.say "I suppose we really do have a lot to talk about."
    bree.say "We're like a threesome that got married, after all."
    anna.say "Oh yeah."
    anna.say "Like, I dated guys before and I dated girls too."
    anna.say "But I never dated both at once."
    show anna happy
    anna.say "And I never thought I'd marry one of each either!"
    show bree happy
    bree.say "I like the way you put it, Anna."
    bree.say "Let you got the complete set!"
    show anna normal
    anna.say "But [hero.name]'s great, isn't he?"
    anna.say "Like, he let me stay in the band after we got married."
    show bree normal
    bree.say "What's that to do with him, Anna?"
    bree.say "You stayed in the band because you wanted to, right?"
    show anna normal
    anna.say "Yeah, but he was cool with it!"
    anna.say "And that counts for something."
    if 'bree_event_04' in DONE:

        bree.say "Yeah, yeah..."
        bree.say "I suppose he supported me when I wanted to keep on working."
        bree.say "Like he didn't dump on me still being a waitress."
        show anna happy
        anna.say "You see, [bree.name] - I told you he was great!"
    elif 'bree_event_05' in DONE:

        bree.say "Yeah, yeah..."
        bree.say "I suppose he supported me when I wanted to keep on working."
        bree.say "Like he didn't dump on me still being a pro gamer."
        show anna happy
        anna.say "You see, [bree.name] - I told you he was great!"

















    bree.say "Family life is actually pretty good too."
    show bree happy
    bree.say "I have to admit that."
    show anna normal
    anna.say "Oh, it's much better since I moved in with you two."
    anna.say "Shame that Sasha had to move out though!"
    show bree normal
    bree.say "I dunno, Anna."
    bree.say "It was getting pretty crowded around here."
    if (anna.is_visibly_pregnant or anna.flags.mikeBabies >= 1) and (bree.is_visibly_pregnant or bree.flags.mikeBabies >= 1):
        anna.say "Hmm..."
        anna.say "I guess so, what with little Tommy running around!"
        bree.say "Yeah, mainly running his daddy ragged!"
        anna.say "What about Brianna?"
        anna.say "She's quite a handful!"
        bree.say "You don't need to remind me!"
    elif anna.is_visibly_pregnant or anna.flags.mikeBabies >= 1:
        anna.say "Hmm..."
        anna.say "I guess so, what with little Tommy running around!"
        bree.say "Yeah, mainly running his daddy ragged!"
    elif bree.is_visibly_pregnant or bree.flags.mikeBabies >= 1:
        anna.say "What about Brianna?"
        anna.say "She's quite a handful!"
        bree.say "You don't need to remind me!"
    else:
        anna.say "Yeah, but it's still big enough for some little additions."
        anna.say "If you know what I mean?"
        bree.say "I sure do, Anna."
        bree.say "And when that happens, [hero.name] won't know what hit him!"
    anna.say "I think things turned out pretty well for us, [bree.name]."
    show bree happy
    bree.say "You know what, Anna - you're right."
    bree.say "I'm certainly looking forward to seeing what the future brings."
    show anna happy
    anna.say "Me too, [bree.name] - it's gonna rock!"
    scene bg black with dissolve
    pause 2.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
