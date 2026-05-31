init python:
    Event(**{
    "name": "anna_start",
    "label": "anna_start",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Or(
                MinFlag("performance", 2),
                MinFlag("band", 2),
                )
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "anna_event_01",
    "label": "anna_event_01",
    "priority": 500,
    "duration": 4,
    "conditions": [
        Or(
            IsDone("anna_start"),
            IsDone("anna_start2"),
        ),
        IsHour(20, 21),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            Not(OnDate()),
            ),
        PersonTarget(anna,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("love", 40),
            ),
        ],
    "clothes": "date",
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "anna_event_02",
    "label": "anna_event_02",
    "priority": 500,
    "duration": 4,
    "conditions": [
        IsDone("anna_event_01"),
        IsHour(19, 22),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            HasRoomTag("home"),
            ),
        PersonTarget(anna,
            Not(IsPresent()),
            Not(IsHidden()),
            IsFlag("horrorMovieDate", True),
            MinStat("love", 60),
            ),
        ],
    "clothes": "casual",
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "anna_event_03",
    "label": "anna_event_03",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("anna_event_02"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_pub")),
        MinDateScore(50),
        PersonTarget(anna,
            OnDate(),
            MinStat("love", 80),
            ),
        ],
    "clothes": "casual",
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "anna_event_04",
    "label": "anna_event_04",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("anna_event_03"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_pub")),
        MinDateScore(50),
        PersonTarget(anna,
            OnDate(),
            MinStat("love", 100),
            ),
        ],
    "clothes": "casual",
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "anna_event_05",
    "label": "anna_event_05",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("anna_event_04"),
        HeroTarget(
            Not(HasRoomTag("home")),
            Not(IsRoom("studio")),
            ),
        PersonTarget(anna,
            IsActive(),
            MinStat("love", 120),
            ),
        ],
    "clothes": "casual",
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "anna_event_06",
    "label": "anna_event_06",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("anna_event_05"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_restaurant")),
        MinDateScore(50),
        PersonTarget(anna,
            OnDate(),
            MinStat("love", 130),
            ),
        ],
    "music": "music/roa_music/innocence.ogg",
    "clothes": "date",
    "do_once": True,
    })

    Event(**{
    "name": "anna_event_07",
    "label": "anna_event_07",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("anna_talk_kleio", "kleio_talk_anna"),
        IsHour(10, 18),
        HeroTarget(IsGender("male")),
        PersonTarget(anna,
            Not(IsPresent()),
            Not(IsHidden()),
            MinStat("love", 140),
            ),
        PersonTarget(kleio,
            Not(IsPresent()),
            Not(IsHidden()),
            ),
        ],
    "clothes": "casual",
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    AfterDateEvent(**{
    "name": "anna_event_08",
    "label": "anna_event_08",
    "priority": 500,
    "conditions": [
        IsDone("anna_event_07"),
        HeroTarget(IsGender("male")),
        MinDateScore(90),
        PersonTarget(anna,
            OnDate(),
            MinStat("love", 150),
            ),
        ],
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "anna_event_09",
    "label": "anna_event_09",
    "priority": 500,
    "conditions": [
        IsDone("anna_event_08"),
        HeroTarget(IsGender("male")),
        PersonTarget(anna,
            IsActive(),
            MinStat("love", 160),
            ),
        ],
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    AfterDateEvent(**{
    "name": "anna_event_10",
    "label": "anna_event_10",
    "priority": 500,
    "conditions": [
        IsDone("anna_event_09"),
        HeroTarget(IsGender("male")),
        MinDateScore(90),
        PersonTarget(anna,
            OnDate(),
            MinStat("love", 170),
            ),
        ],
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "anna_event_11",
    "label": "anna_event_11",
    "priority": 500,
    "conditions": [
        IsDone("anna_event_10"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_livingroom")
            ),
        PersonTarget(anna,
            OnDate(),
            MinStat("love", 180),
            ),
        ],
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "anna_event_12",
    "label": "anna_event_12",
    "priority": 500,
    "conditions": [
        IsDone("anna_event_11"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_pub")
            ),
        PersonTarget(anna,
            OnDate(),
            MinStat("love", 190),
            ),
        ],
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "anna_event_13",
    "label": "anna_event_13",
    "priority": 500,
    "conditions": [
        IsDone("anna_event_12"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),
            Not(OnDate()),
            ),
        PersonTarget(anna,
            IsActive(),
            MinStat("love", 200),
            ),
        ],
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "anna_sub_event_01",
    "priority": 500,
    "label": "anna_sub_event_01",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_bakery"),
            IsRoom("date_mall1"),
            ),
        PersonTarget(anna,
            OnDate(),
            MinStat("sub", 40),
            ),
        ],
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "anna_sub_event_02",
    "priority": 500,
    "label": "anna_sub_event_02",
    "conditions": [
        IsDone("anna_sub_event_01"),
        HeroTarget(
            IsGender("male"),
            IsActivity("date_watch_tv"),
            IsRoom("date_livingroom"),
            ),
        PersonTarget(anna,
            OnDate(),
            MinStat("sub", 80),
            ),
        ],
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    InteractEvent(**{
    "name": "anna_event_talk_murder",
    "label": "anna_event_talk_murder",
    "priority": 500,
    "conditions": [
        PersonTarget(anna,
            IsActive(),
            ),
        PersonTarget(kylie,
            IsFlag("killed", "sasha"),
            ),
        ],
    "clothes": "casual",
    "music": "music/roa_music/innocence.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "anna_practice_01",
    "priority": 500,
    "label": "anna_practice_01",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("practice_band"),
            MinFlag("bandpractice", 25),
            ),
        PersonTarget(anna,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 50),
            ),
        PersonTarget(kleio,
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "anna_kiss_me",
    "label": "anna_kiss_me",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(anna,
            IsPresent(),
            Not(IsHidden()),
            MinFlag("kiss", 1),
            MinStat("love", 150),
            ),
        ],
    "music": "music/roa_music/innocence.ogg",
    "chances": 20,
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "anna_preg_talk",
    "label": "anna_preg_talk",
    "do_once": False,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(anna,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinCounter("pregnant", 6),
            ),
        ],
    "music": "music/roa_music/innocence.ogg",
    })

label anna_start:
    if anna.love.max < 40:
        $ anna.love.max = 40
    $ anna.unhide()
    return

label anna_event_01:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Anna")
    if not result:
        $ hero.cancel_event()
        $ anna.love -= 5
        return
    if anna.love.max < 60:
        $ anna.love.max = 60
    mike.say "Hello?"
    "There is so much noise in the background that it's hard for me to hear. When I finally make out a voice, I'm shocked to hear that it's Anna."
    "She's slurring, and she sounds like she's very drunk."
    anna.say "Hellooooooo, [hero.name], how are you?"
    "I stifle a laugh, amused by the sound of her high-pitched voice mumbling up letters."
    mike.say "I'm doing pretty well, Anna, how are you?"
    anna.say "Oh, I'm fantastic!"
    mike.say "I'm glad to hear that, dear. What are you up to?"
    anna.say "You know, the usual. Getting drunk, getting high, taking the downtown."
    mike.say "Sounds like a super fun time."
    anna.say "Oh, it so totally is. Downtown is my favorite place ever! Everything is soooo great over here."
    menu:
        "Can I join you?":
            mike.say "Really? Well, would you mind if I came and joined you?"
            "Anna gasps."
            anna.say "Oh my god, that would be AMAZING! Here, I'll text you the address of the bar."
            anna.say "You'd better hurry and get here though!"
            "Quicker than I thought someone who was drunk could, she texted me a flawlessly typed address."
            "I realize with a start that this bar is only a few blocks down the street from my house."
            "It must be why Anna called me—even in her alcohol filled stupor, she must have realized I was close."
            mike.say "Alrighty, Anna, I'll be there in a few minutes. Keep an eye out for me!"
            anna.say "I will, I totally will! See you soon!"
            "Before I have a chance to say goodbye, she hangs up on me, leaving the ghost of a laugh still hanging on my lips."
            $ anna.love += 1
            $ HELP = False
        "Where are you?":
            mike.say "Where are you, Anna?"
            "The background noise gets louder again, and I realize that she must be asking her friends where she is. Yikes. She must be more drunk than I realized."
            "Finally, she returns to the phone, yelling the address in my ear. I pull the phone back slight, her tinny voice grating on my nerves."
            "I realize the bar she's at is only a few blocks down from me."
            "Whether or not I want to admit it, I am concerned about her, and I don't want to leave her struggling alone with whoever else she's with, especially if they're drunk too."
            "So, against my better judgement, I grab my coat."
            mike.say "I'm glad you're having fun, Anna! Just to be sure you're okay, I'm gonna come check in on you, alright?"
            "I can hear her pout through the phone. She starts whining, loud and annoyed."
            anna.say "You're not my Dad, [hero.name], I can take care of myself."
            "I roll my eyes, starting to make my way out my door anyway."
            mike.say "I know, I know you can. I'm just being a friend, okay? If nothing else, we can party together now instead of separate, yeah?"
            "She sighs."
            anna.say "I guess sooooo."
            mike.say "Alright then, don't go anywhere. I'll see you in a minute."
            "Before I get a chance to say goodbye, the line goes dead. Holding back laughter and slight worry, I make my way out into the cool night."
            $ anna.sub += 1
            $ HELP = True
    scene bg street with fade
    "I make my way brusquely down the street, and I realize that it isn't going to take me that long to find the bar Anna was at."
    "The bass is thumping so loud, I could hear it at the bottom of my street, the howling laughter of drunks and the flashing party lights so obvious that I'm shocked the police haven't shut it down yet."
    "As I get closer, I see a clump of people who look familiar partying in the outside patio area, downing more tequila shots and laughing about a joke I was too far away to hear."
    show anna casual happy at left4, dark with dissolve
    "When I scan the crowd, I finally see Anna, laughing with the rest, and I let out a breath I didn't realize I was holding."
    show anna at right4 with move
    "Swinging my leg over the short patio fence, I approach her, tapping her on the shoulder."
    show anna happy at center with move
    hide anna
    show anna casual with dissolve
    "She swings around drunkenly, stumbling over her own two feet and directly into my arms. Once she got her bearings, she gazes up at me, and then, the biggest smile crosses her face."
    show anna happy
    anna.say "[hero.name]! You're here!"
    "I smile at her, helping her steady herself."
    if not HELP:
        mike.say "What can I say, who could resist a night out with you?"
        show anna blush
        "Anna goes into a fit of giggles, a blush rising up on her cheeks as she struggles to contain herself."
        anna.say "Aw, [hero.name]., you're so fucking sweet. I'm glad you're here!"
        mike.say "Me too, Anna."
        "I order a beer from the bartender, hoping it would loosen me up a little bit, but I don't spend long at the bar, instead immediately returning to Anna's side."
        $ anna.love += 1
    else:
        mike.say "Yeah, I am."
        show anna annoyed
        "Anna rolled her eyes at me, leaning away, trying to grab her shot glass."
        anna.say "Wow, you sound like quite the party pooper tonight. Have a drink or something, it'll loosen you up."
        "Against my better judgement, I listen to her, ordering a beer from the bartender before returning to her side."
        $ anna.love += 1
    show anna happy
    "Anna sways as she struggles to talk, her words getting more and more garbled."
    "Although I can't help but laugh as she tries to say 'Battle of the Bands' for about the eighth time, my concern for her well-being can't help but grow."
    "She's wasted, beyond wasted, and her friends didn't really care that much. They're drunk too, and more than happy to simply leave her to her own devices."
    "I can't say the same for myself."
    if not HELP:
        mike.say "Hey, Anna, are you feeling okay?"
        show anna dazed at center, zoomAt (1, (600, 720)) with ease
        pause 0.1
        show anna at center, zoomAt (1, (675, 720)) with ease
        "Anna twists her face up, rocking back and forth in her struggle to remain conscious."
        show anna at center, zoomAt (1, (610, 720)) with ease
        pause 0.1
        show anna happy at center, zoomAt (1, (665, 720)) with ease
        anna.say "I'm fineeeeee!"
        mike.say "Are you sure, dear? You seem really out of it. Let me get you a water, at least."
        "For a moment, I'm afraid that she's going to reject my care, her eyes narrowing as she finally righted herself."
        show anna at center, zoomAt (1, (640, 850)), vshake
        "Then, she collapses down into the chair that I had vacated for her, waving her hand."
        anna.say "A water sounds like a good idea, actually. Thank you, [hero.name]."
        "Happy to oblige, I quickly walk off, going to get Anna a water."
        $ anna.love += 1
    else:
        mike.say "Anna, I think we should get out of here."
        show anna annoyed
        "Anna narrowed her eyes, glaring at me, digging her nails into her glass beer bottle."
        anna.say "What are you trying to do, [hero.name]? Are you trying to take advantage of me?"
        mike.say "No! No, goddamn, Anna, I would never do anything like that. I'm just worried about you. You seem really drunk."
        "Anna shuffles her feet, standing down but still defensive."
        anna.say "I'm really not that bad, [hero.name], I don't know what you're going on and on about."
        mike.say "I just—I'm just—oh, whatever, Anna. Just sit down, and let me get you a water, at least. Please."
        show anna at center, zoomAt (1, (640, 850)), vshake
        "Anna huffs, crossing her legs and taking my seat."
        anna.say "Whatever."
    scene bg pub with dissolve
    "The bartender obliges my request quickly, giving me a large, icy glass of water."
    scene bg street
    show anna normal casual at center, zoomAt (1, (640, 850))
    with dissolve
    "When I turn, I see Anna, seated, talking with a man who is leaning over her small frame, far too close for my comfort."
    "For a moment, I just hang back and watch, so stunned that I can't find the energy to pick up my feet."
    "The man leans closer to her, dragging his hand down her jawline, grinning at her, looking like an animal hunting his prey."
    show anna annoyed
    "Anna stiffens, clearly uncomfortable by his advances, but too drunk to realize what is truly going on."
    menu:
        "Interrupt them":
            "Having enough of his behavior, I storm over to her side."
            "Despite the blood boiling underneath the surface, I struggle to maintain calmness in my voice. I don't want to scare Anna."
            mike.say "Hey, dear. I brought you some water. Who is this?"
            "Anna clings onto my arm, holding me tightly as I carefully hand her her water. She struggles to introduce me, her words slurring together so much I can't even catch his name."
            "Shady guy" "I'm just a friend of Anna's."
            mike.say "Well, maybe I'm reading into things too much, but she didn't seem all too happy to see you back there."
            "The Strange Man looks uncomfortable to be called out, and leans away from the two of us."
            "Shady guy" "I guess so. I just thought she was hot. My bad, buddy."
            "With one last glance at Anna, he spoke over his shoulder as he walked away."
            "Shady guy" "See you later, Anna. Sorry again, dude."
            show anna happy
            "Turning back to Anna, she wasn't able to say much, but she simply looked at me, and gave me a hug, eyes speaking more than words ever could."
            "I hug her back, enjoying the moment, before once again helping her drink her water."
            $ anna.love += 1
        "Do nothing":
            "I hang back still, finding myself flipping through any conversations I'd had with Anna to see if she had a boyfriend I didn't know about."
            "After all, I didn't want to be that guy, especially if she had a boyfriend."
            "The man gets closer to Anna, dragging his hand along her thigh, fingers splayed and grabbing at every empty patch of her skin."
            "His mouth is nearly watering, his eyes hungry, taking every inch of her in. Some small part of me agreed, not blaming him—Anna's as hot as they come—but something about this situation felt off."
            "I couldn't quite place the feeling, but something within me left me planted to the floor, unable to tear my eyes away, but unable to drag myself forwards."
            "The Man gets ever closer to Anna, lips nearly brushing hers as she struggles to keep her eyes open."
            "Finally, someone else noticed Anna, one of her friends, her face twisted in the same confusion I felt."
            "However, this time, she decides to step in."
            "She approaches the man with enough drunken swagger to drive him off."
            "The man looks sheepish, ashamed, as though he knew what he was doing was wrong, and I realized with a start that I could've done more."
            "I could have helped her, but instead, all I could do was watch, afraid."
            "Ashamed, I quietly make my way to Anna's side, making sure to give her an extra big hug when I made it to her side."
    show anna normal
    "Anna, seemingly subdued by the water, gently leaned her head into my shoulder."
    show anna dazed
    anna.say "I'm tired, [hero.name]."
    mike.say "I know, Anna. Do you want to go home?"
    "Anna cries out, upset, sounding almost on the verge of tears."
    anna.say "I live all the way across town, and we can't drive now. I'll never be able to get home."
    "Shit, she's right. We can't drive, especially not her."
    "I don't want to be that guy, but I know I can take her home. Or at least help her get home safely."
    menu:
        "Invite her home":
            mike.say "Anna, I promise I don't mean this to be weird, but I live right up the street."
            mike.say "Do you want to come home with me?"
            mike.say "Sasha and [bree.name] should be home, and we have a couch in the living room too."
            "Anna's eyes shimmer, and, wordlessly, she nods, nearly collapsing into my arms."
            "Tossing a few dollars onto the table to cover her tab, and giving a brief goodbye to her friends, I slowly begin to help her back towards my home."
            scene bg street
            show anna dazed casual
            with fade
            "It's a long, quiet walk home, with only the brief sounds from the busy street to punctuate our walk."
            "Anna is silent, stumbling, barely coherent. I did my best to help her walk, praying that my house door would be there soon enough."
            scene bg house
            show anna dazed casual
            with fade
            "Finally, right when I think Anna can't make it any farther, we finally reach my door. Walking as quietly as I can, I let her into my home."
            scene bg livingroom
            show anna dazed casual
            with fade
            pause 0.5
            scene bg livingroom at dark
            show anna happy casual at center, rotation (58), zoomAt (1.75, (600, 1450)), vshake
            "Almost immediately, she collapsed onto my couch, falling asleep quicker than I thought possible."
            "Stifling a grin, I do my best to put her to bed, placing a blanket over her body and giving her a trash can in case she feels sick later."
            "She looks so peaceful, asleep on the couch, that, for a moment, I simply watch her, cuddled up to the blanket, chest rising and falling, indicative of her deep sleep."
            "She was so beautiful, so unaware, as she slept."
            hide anna with dissolve
            "Finally, satisfied that she was safe and comfortable, I turn to go to my own room, suddenly aware of the deep exhaustion permeating my bones."
            $ anna.love += 1
            $ game.room = "bedroom1"
        "Call a cab":
            mike.say "Do you want me to call you a taxi? I can ride it with you so I know you're okay."
            "Anna looks up at me, eyes exhausted. Without a word, she nods before leaning back against my body."
            "I do my best to hail a cab, dialing as many numbers as I can find for cab companies until I find one willing to take us both in the order I need."
            "I wince at the expense, knowing it will take a serious bite out of my wallet, but I know that Anna needs it. In good conscience, I can't leave her here."
            scene bg taxi with fade
            "She dozes off as we wait for the taxi, and it seems as though it can't come soon enough."
            show bg taxi car with dissolve
            pause 0.5
            show anna dazed casual with dissolve
            "Finally, I saw the car pull up to the curve, and I slowly help Anna to her feet, guiding her into the backseat."
            scene bg taxi at blur(8), dark with dissolve
            "She was silent as the drive goes, the lights from the street flashing in and out of the windows."
            "Finally, we got back to her apartment, and, as best as I could, I steady her outside her door."
            scene bg taxi
            show anna dazed casual
            with dissolve
            mike.say "Are you going to be okay, Anna?"
            "Anna nods, struggling to keep her bearings. With a soft smile, she slowly made her way towards her complex, leaving me biting my lip, watching her stumble towards her home."
            scene bg taxi car with dissolve
            "Hesitantly, I turn back to the cab, leaving the bit in my stomach to grow bigger and bigger as the cabbie slowly takes me away, stealing my wallet and leaving my heart at the curb."
            $ game.room = "map"
    return

label anna_event_02:
    if anna.love.max < 80:
        $ anna.love.max = 80
    scene bg bedroom1
    "One thing that Anna's been pretty keen on telling me since we started spending time together is just how much she loves horror movies."
    "If there had been something new and particularly gruesome showing at the local cinema, then I wouldn't have hesitated to take her along to see it."
    "Even better would have been one of those festivals of horror, where the independent cinema shows obscure, cult classics of the genre."
    "But as neither of those things are an option, I have to settle for inviting Anna round to my place to watch some films with me there."
    "Before the appointed hour arrives, I send her a list of the titles in my collection, asking her to choose her pick."
    "Unfortunately for me, she soon lets me know that she's seen all of them, and on multiple occasions too."
    "Just then I remember that [bree.name] actually has a couple of horror movies amongst her collection that I've honestly never even heard of before."
    scene bg bedroom2 with fade
    "So I fire off a quick message to Anna, telling her not to worry, and then ask [bree.name]'s permission to rummage through her video nasties."
    "I soon find that the only problem with this is that, while [bree.name] does indeed have a number of horror movies to choose from, they seem to be from a kind of strange sub-genre."
    "All of them are filled with high-school kids that turn into werewolves on the basketball court and cheerleaders that slay vampires."
    "It's like someone mashed together the tropes of horror and teen movies from the eighties, creating a baffling mixture of the two."
    "All of the vampires are troubled pretty-boys that just need to be understood by the rebellious girls that they inevitably fall in love with."
    "Well, that is the ones that don't turn out to be once-in-a-generation chosen ones, and drive a stake through their hearts."
    "In the end, I just grab one that looks like it's about vampires and more recent than the others."
    "I mean, just how bad can it be?"
    play sound door_knock
    "Almost the same moment that I have the DVD in my hand, I hear a knock at the front door."
    "I hurry out of [bree.name]'s room and down the stairs into the hallway, eager to let Anna in and get the evening started."
    scene bg black with dissolve
    pause 0.1
    scene bg house
    show anna casual
    with wiperight
    "But when I open the door, she simply stands there, not making any effort to enter."
    anna.say "Well, aren't you going to invite me in?"
    mike.say "Erm, I thought that was kind of implied by my opening the door with a smile on my face?"
    "Anna rolls her eyes and chuckles at this."
    show anna happy with dissolve
    anna.say "Oh, [hero.name] - you're so cute when you're clueless!"
    anna.say "We're watching horror films, right?"
    show anna normal
    mike.say "Yeah...at least that was the plan."
    anna.say "So, you should invite me in, you know - like a vampire?"
    mike.say "What, so that you can bite me on the neck and suck my blood?"
    show anna wink with dissolve
    "Anna giggles wickedly and winks at this, bearing her teeth a little at the same time."
    anna.say "Well, that might not be all that I suck..."
    mike.say "Ah...I suppose you'd better come in then!"
    scene bg livingroom
    show anna casual
    with fade
    "Anna steps over the threshold and into the house, winking evilly at me as she does so."
    "Still feeling a little flustered, I hastily show her into the sitting room and gesture to the couch in front of the TV."
    mike.say "I'm just going to grab some snacks and drinks from the kitchen."
    mike.say "The movie I chose is in the case on the coffee table, so take a look."
    "When I return a couple of moments later, burdened with supplies for the evening's viewing, I see Anna's smiling in an ironic manner."
    mike.say "What's the matter, Anna?"
    mike.say "You look like I just walked in with my flies undone..."
    "Anna answers this by holding up the DVD case so that I can see the cover."
    anna.say "You actually chose this specific film?"
    mike.say "Yeah, so what?"
    mike.say "It's about vampires, isn't it?"
    anna.say "Sure it is!"
    "Anna seems reluctant to say any more, and so I'm left to sit down beside her and take the DVD like its going to explode at any given moment."
    "I could get pissy and demand that she tell me exactly what's up with my choice film."
    "But I'm worried that could kill the evening off before it's even gotten started."
    "So I put the disc in and dim the lights, all the time trying to ignore the smirk on Anna's face."
    "Let's just say that once the titles have scrolled past and we're into the thing, it doesn't take me long to realise what's up."
    "I manage to watch for perhaps twenty minutes before I simply can't take it any more."
    show anna surprised at startle
    "Unable to keep it bottled for another second, I burst out laughing, loud enough to make Anna jump a little."
    show anna happy
    "And then she instantly joins in, secure in the knowledge that I finally understand what she was hinting at."
    mike.say "This is like...like...the worst thing I've ever seen!"
    anna.say "I know, tell me about it!"
    mike.say "What's up with the girl playing the heroine?"
    mike.say "She's got a face like a slapped arse the whole time!"
    show anna normal
    anna.say "But what about the vampire?"
    anna.say "What a whining pussy, right?!?"
    "I shake my head as more of the same nonsense plays out on the screen before us."
    mike.say "Why's he out in the daytime?"
    mike.say "Don't vampires turn into dust in direct sunlight?"
    show anna happy
    anna.say "Oh no, not this special snowflake - he just sparkles, like he's covered in glitter!"
    "This revelation sets me off laughing again, almost doubling me over when I see it actually happen on the screen."
    mike.say "I don't think he's really a vampire, Anna."
    show anna normal
    anna.say "Huh...why's that?"
    mike.say "Sure, he put a dent in that van, but so could someone on drugs!"
    mike.say "He's walking around in the daylight, doing shit like that and sparkling the whole time."
    mike.say "I think he's just been doing PCP in a gay nightclub before this, that's all!"
    show anna happy at vshake
    "Anna literally spits out the mouthful of snacks that she's chewing on."
    show anna happy at vshake
    "She's laughing so much at this point that we're not actually watching the film for its own sake any more."
    "Having ruined our chances of sitting through the rest of it with a straight face, we just spend the rest of the time pissing all over it instead."
    "By the end of the night, we've enjoyed that more than we ever could have the act of watching the film itself."
    mike.say "Oh god...that was bloody awful!"
    mike.say "I suppose they only made the one and then it died off?"
    show anna normal
    anna.say "Oh no, they've made a whole series of them - and they just get worse!"
    mike.say "You're joking!"
    "Anna shakes her head, still trying to keep from laughing as she does so."
    anna.say "I'm not - we could make a regular thing of this, sitting down to slag them off!"
    "Now it's my turn to shake my head in disbelief and horror."
    mike.say "I don't think I could take even the thought of that, Anna!"
    mike.say "Next time, I think you should pick the film..."
    return

label anna_event_03:
    if anna.love.max < 100:
        $ anna.love.max = 100
    show anna surprised at center, vshake
    "Anna sees them before I do, and the only reason I know anything's up is the fact that she seems to go a little pale as I'm looking straight at her."
    "But when I look around, hunting for what the cause of her distress could be, I end up drawing a complete blank."
    mike.say "Anna, you're pale as fuck!"
    mike.say "What's the matter?"
    show anna annoyed at left4 with move
    "Anna's already backing away and trying to duck behind whatever cover she can find when I ask her this."
    "And she grabs me by the hand, pulling me with her, rather than answering the question."
    anna.say "Get down and follow me, right now!"
    anna.say "And whatever you do, don't look behind you..."
    "But of course, the very moment she says this, my head begins to turn in that very same direction."
    "I can't help myself - it's as though I have no control as my body does the exact opposite of what Anna told me to."
    "Even then I'm none the wiser, as all I can see is a couple of guys and a girl that seem to be making their way towards us."
    "Surely they can't be what's got Anna so worked up, can they?"
    "They look like nothing more than typical metal-heads, with long hair and band T-shirts, perfectly harmless."
    "I don't recognise the name printed on their shirts, and so I strain to see what it could be."
    "Who knows, maybe Anna just has a pathological aversion to that band, their music, and their fanbase too."
    with hpunch
    "But then I finally manage to make out the words, and I instantly stop letting Anna pull me away."
    mike.say "Hey, Anna - those guys are all wearing Deathless Harpies T-shirts!"
    mike.say "That's so cool - I didn't even know we had T-shirts!"
    show anna angry
    anna.say "That's because we don't!"
    show anna annoyed
    "My face twists into a confused expression."
    mike.say "Huh - but then how come they have them?"
    mike.say "Did someone else steal the name?"
    "Still battling to pull me after her and having no success thanks to my weight advantage, Anna shakes her head."
    anna.say "No, they had them printed themselves."
    mike.say "Wow - they must REALLY like us!"
    anna.say "Yeah, they do."
    show anna angry
    anna.say "But that's the problem - they like us TOO much!"
    show anna annoyed
    mike.say "What...I don't get it!"
    mike.say "How can they like us too much?"
    anna.say "Don't worry, [hero.name] - you're about to find out for yourself!"
    "I look round at this, following Anna's gaze and seeing almost instantly that, despite her best efforts, we've been spotted."
    "One of the guys points at us while slapping the shoulders and arms of his companions."
    "And a moment later, they're crowding towards us."
    "Male fan" "Hey, hey, hey - it's like fifty percent of the Deathless Harpies!"
    "Male fan" "Even better, it's the hottest drummer in all the world of metal!"
    "Though they looked harmless from a way off, all of them are getting in our personal space, faces mere inches from our own."
    with hpunch
    "I can see and feel them begin to touch me without a thought of asking if it's cool to do so."
    "That makes me want to punch one of them in the face, or at least shove them a good few feet back."
    "And if that's how it makes me feel, it must be much worse for Anna, thanks to her diminutive stature."
    with hpunch
    anna.say "Erm...hey...hey there, guys..."
    "Female fan" "Hey, who are you calling a guy?!?"
    show anna normal
    "Anna smiles nervously at the girl's challenge, clearly intimidated by her pushiness."
    "Female fan" "Don't worry, Anna - I know that most of you girls like us girls in the audience too!"
    show anna annoyed
    menu:
        "Step in to save Anna" if hero.charm >= 25:
            "As the girl reaches out to touch Anna, I can't help but instinctively step into her path."
            with vpunch
            "And I don't hesitate to slap away the hand that she's extending towards my bandmate."
            "Female fan" "Oww - hey, man!"
            "Male fan" "Yeah, dude - what in the hell are you doing?!?"
            "Male fan" "That's not cool - The Deathless Harpies are SO against violence to women!"
            "Wait a minute - these arseholes are getting in our faces and trying to put their unwelcome hands on Anna."
            "And yet they're lecturing me on being out of touch with the band's moral stance for stopping them from basically assaulting her?"
            "Fuck these guys!"
            $ anna.sub += 10
            mike.say "What do you pricks think - that because you had T-shirts printed, you own a piece of us now?"
            "I hadn't noticed it before now, but I'm quite a bit taller than most of the guys in the group."
            "This means that they're a little intimidated by me standing over them and taking them to task."
            "I just hope that they don't realise they're younger than me and outnumber me significantly any time soon!"
            "Male fan" "What...no...we'd never..."
            "Female fan" "Hey, stop trying to twist this on us, man!"
            mike.say "And another fucking thing - when did we get the royalties on those shirts, huh?"
            "Now they're starting to back off a little, looking at each other in confusion."
            "Male fan" "What are you talking about?"
            "Female fan" "We're like serious fans of yours - we had these made to show that!"
            mike.say "What kind of a fan takes money out of our pockets?"
            mike.say "Those shirts are stealing our intellectual property."
            mike.say "You're lucky we don't sue you for theft!"
            "Male fan" "You wouldn't..."
            mike.say "Try me, asshole!"
            "I honestly don't know whether I'm actually intimidating them, or just making them confused."
            "But either way, it seems to have the desired effect, as they start to look worried and back off."
            "Male fan" "Look, we don't want any trouble!"
            "Female fan" "Yeah...we're just fans, honestly, we are!"
            "They make a hasty and cringing exit, leaving Anna and I alone and unmolested once more."
            show anna at center
            mike.say "Are you okay, Anna?"
            "She nods, looking at me a little strangely and causing me to worry that she's suffering from shock."
            mike.say "I had no idea fans could be like that..."
            show anna happy
            "Anna shakes her head, dismissing my attempt at an apology."
            anna.say "You know what it's like when you have a small but dedicated following..."
            "I nod, not needing to say anything more."
            anna.say "No, what really sticks in my head is you talking about suing them."
            anna.say "I've never seen anyone use the threat of legal action to make a bunch of guys back down before!"
            "All I can do is laugh nervously, thankful that it didn't escalate any further."
            "After all, it's not like I keep a team of hot-shot lawyers on speed-dial!"
        "Stand back and watch":
            "I know that I should be stepping in and standing up for Anna here."
            "But there's just something so fascinating about the whole scenario."
            "I can't help watching in silence as the girl's hand reaches out to touch Anna."
            show anna surprised at center, vshake
            "Or to be more precise - reaches out and grabs a sizeable handful of her left breast!"
            $ anna.love -= 25
            show anna angry
            anna.say "HEY THAT'S MY GODDAMN TIT!"
            "To be fair to all concerned, the female fan instantly jumps away at the sound of Anna's sudden outburst."
            "He hand couldn't have been on Anna's actual breast for more than a couple of seconds."
            "But it looks like it was still enough for the damage to be done, emboldening the two guys with her."
            "Male fan" "Whoa, you got a squeeze of the drummer's tit!"
            "Male fan" "No fair - The Deathless Harpies are all about sexual equality!"
            show anna dazed
            "Before Anna can as much as say another word, two more pairs of hands are all over her."
            show anna at vshake
            "The guys indulge themselves by mashing at her breasts without mercy, laughing in delight the whole time."
            "Female fan" "Hey - I only got to touch them for like a second!"
            "And with that, she joins in the action, groping Anna's chest for a second time in mere moments."
            show anna at hshake
            "The whole time they're manhandling her, Anna wails pitifully and tries in vain to beat them off."
            "She looks at me in desperation, her eyes pleading with me to save her from their unwanted attentions."
            anna.say "Ah...ouch!"
            anna.say "[hero.name]...help me...please!"
            "The same way I know I shouldn't have let this happen, I also know that it's high time I stepped in now."
            "But still I find myself hesitating, fascinated and more than a little turned on by the sight of Anna being abused in this way."
            "Her cheeks are bright red, and I swear I can see the beginnings of tears in her eyes as she tries to defend herself."
            "Finally I can't delay acting any longer, and reach out to grab one of Anna's hands."
            "She yelps as I physically drag her out of there, ignoring the protests of the so-called fans as I do so."
            "Once we're outside and I'm sure they're not following, we stop and both take time to catch our breath."
            show anna cry
            anna.say "Thanks, [hero.name]."
            anna.say "If you hadn't pulled me out of there when you did, they might have stripped me naked back there!"
            "I nod, trying to hide the fact that the mental image that statement just summoned is making me hard right now."
            mike.say "It's okay, Anna."
            mike.say "I should have stopped them sooner..."
            "Anna greets this with an expression of sympathy, which is not at all what I expected my actions to earn from her."
            show anna normal
            anna.say "Don't worry, [hero.name], it's only natural."
            anna.say "I froze up like that the very first time I was face-to-face with fans like that."
            show anna happy
            anna.say "You'll get used to it, trust me!"
            "I nod weakly, relieved to have seemingly gotten away with my failure to step up to the mark."
            "But the fact that Anna's totally misinterpreted my actions does make me feel kind of guilty..."
            "Trying to bury the unpleasant feelings this is causing me, I follow Anna as she begins to walk away from the scene of the crime."
    return

label anna_event_04:
    if anna.love.max < 120:
        $ anna.love.max = 120
    show anna annoyed
    mike.say "What's the matter, Anna?"
    show anna dazed at vshake
    "I hand her drink over, surprised to see her immediately down more than half of it in one go."
    anna.say "Erm, nothing...I just didn't realise how thirsty I was!"
    mike.say "Anna, you're a pretty terrible liar - you know that, right?"
    "Anna looks awkward, unable to keep from blushing intensely at being found out so easily."
    anna.say "Okay, okay...I just saw someone I didn't want to bump into, that's all."
    show anna normal
    mike.say "From that reaction, it had to be either one of your parents, or an ex!"
    "Anna visibly flinches at the latter, giving herself away again."
    mike.say "Don't worry about some ex showing up."
    mike.say "I'll tell him where to get off, no worries on that score."
    show anna annoyed
    anna.say "What about telling HER to get lost?"
    "Of course, Anna already told me that I was the first guy she'd been out with for a while."
    "I should have guessed the chances were any ex of hers we bumped into would be female."
    if hero.charm >= 25:
        "I shrug at the news that I'm about to meet Anna's previous female lover."
        mike.say "No problem, Anna - you never hid from me that you liked guys and girls."
        mike.say "It's no different from meeting a guy that used to date you back in the day."
        show anna happy
        "Anna laughs nervously, but looks visibly relieved."
        anna.say "Yeah, I guess you're right."
        anna.say "I just wish Gwendoline was as cool with stuff as you are!"
    else:
        $ anna.love -= 5
        "My groan is so obvious that Anna's face falls in response."
        anna.say "What's up, [hero.name]?"
        anna.say "I already told you I was into girls too, didn't I?"
        mike.say "Yeah, yeah, whatever - but I never thought I'd actually have to deal with any of that shit!"
        show anna annoyed
        "Anna looks upset and gazes down at her feet rather than meet my eye."
        anna.say "Oh, okay...sorry...I guess."
    show anna normal
    "I'm about to ask Anna to point the woman out, when I see someone staring straight at me that just has to be her."
    "Her brown hair framing her sneering features and a hard look in her narrowing black eyes."
    show anna at left with move
    show gwen teaser at right with moveinright
    anna.say "Erm...hi, Gwendoline."
    show anna happy
    anna.say "Imagine seeing you here - what are the chances of that!"
    "Gwendoline almost ignores Anna until she speaks."
    "Instead glaring at me like something she found smeared on the sole of her size twelve boots."
    "Gwendoline" "Don't talk shit, Anna - this is my local, we used to be in here every night of the fucking week."
    show anna dazed
    "Anna visibly flinches at the harsh way in which Gwendoline speaks to her, as if by force of habit."
    "I can immediately see why she was so unhappy to have bumped into the woman."
    "Gwendoline" "So this is the asshole you're letting screw you now, is it?"
    "Gwendoline" "Shit, Anna - looks to me like he'd be a step below a shit-smeared dildo you found in a toilet bowl."
    "Anna still won't look up at Gwendoline, but she shoots me a desperate sideways glance."
    "It's clear that she's waiting for me to say something in response."
    if hero.fitness < 25:
        $ anna.love -= 5
        "I don't know if it's her size or the insults she's flinging, but I can't muster a coherent response."
        "Instead I just stand there, my mouth flapping like a slapped fish."
        "Gwendoline" "What is this guy, some kind of fucking mute or something?"
        show anna annoyed
        anna.say "[hero.name]...are you really gonna let her talk to you like that?"
        "I keep silent, feeling a sudden warmth spreading around my groin."
        "Gwendoline" "I think he is going to let me talk to him like that!"
        "Gwendoline" "Or maybe he's waiting until he's done pissing himself!"
    elif hero.charm < 25:
        "I've dealt with Gwendoline's type before, and male or female, they're all alike."
        "They only respect someone who's prepared to give as good as they get."
        mike.say "Wow, I never knew you could stack shit so high!"
        show anna surprised
        show gwen teaser at right4 with move
        "Anna's eyes widen and Gwendoline leans forward to sneer at me."
        "Gwendoline" "What did you say, you glorified sperm-bank?"
        mike.say "Jesus, whatever crawled up your ass and died must have needed climbing gear."
        show anna happy
        "Anna suddenly realises what I'm doing and bursts out laughing."
        "Gwendoline" "Hey, wait a minute!"
        "Gwendoline backs off visibly, now starting to look unsure of herself."
    else:
        "I've met so many bullies like Gwendoline in the past that I'm not intimidated by her in the least."
        $ anna.love += 5
        $ game.flags.gwenStart = True
        mike.say "Why'd you break up with this prize pig, Anna?"
        mike.say "You just not turned on enough by the prospect of fucking a cold hearted bitch up the ass?"
        show anna surprised
        show gwen teaser at vshake
        "Anna gasps in genuine surprise and Gwendoline almost growls in rage at the insult."
        "Gwendoline" "You shut your mouth, prick - or I'll..."
        mike.say "Or you'll what?...Huh?...Grind my bones to make your bread?"
        mike.say "Before you answer that one, let me tell you that I'm a very, VERY modern guy, bitch."
        mike.say "Don't think that I'll hold back if you come at me swinging those big gorilla arms of yours!"
        "Gwendoline backs off visibly, now starting to look unsure of herself."
    hide gwen with moveoutright
    "As soon as Gwendoline's gone and I'm alone with Anna again, I realise that my heart's pounding in my chest."
    show anna normal at center with move
    anna.say "[hero.name], are you gonna be okay?"
    mike.say "Yeah, don't worry about me - I'll be fine in a minute or so."
    "I'm not sure that Anna's convinced by my brush off, but she says nothing more on the matter."
    "Whatever she thinks, as we settle back down to watch the band, I notice that she's looking at me in a different way to normal."
    "Glancing away, I happen to catch Gwendoline looking at me too, from the other side of the room."
    "I can't hope to tell what either of them are actually thinking as they both look in my direction."
    "But I have the definite feeling that I haven't heard the last of the unfinished business between the two of them just yet."
    hide anna
    return

label anna_event_05:
    if anna.love.max < 130:
        $ anna.love.max = 130
    show anna
    "I don't normally tend to be the one to spot a potential problem on the horizon, but on this occasion I have the edge on my companion."
    "Anna's not exactly the tallest of people, so she's hampered as much by objects of any significant height, as much as the crowds around us."
    "And in addition to that, the problem that I've managed to spot is pretty much the exact opposite, towering as she does above most heads."
    mike.say "Shit - isn't that Gwen over there, Anna?"
    mike.say "Your obnoxious ex-girlfriend?"
    show anna annoyed
    "Anna looks at me with disbelief written all over her face, as well as a measure of annoyance as well."
    "As if she's pissed both at the idea of her ex and the fact that I can see what she can't right now."
    show anna angry
    anna.say "Well how the hell am I supposed to know, [hero.name]?"
    anna.say "Climb up on your shoulders for a look?"
    show anna at left with move
    show gwen teaser at right with moveinright
    "Gwendoline" "Hello, Anna - I didn't see you all the way down there!"
    show anna annoyed
    "In the time that we've wasted bickering over her, Gwen must have seen me and made her way over."
    "Now she's standing there, arms crossed and looking for all the world like she'd going to enjoy the chance to insult us both."
    show anna dazed
    "Instantly I see Anna begin to fold in on herself, just as she always seems to do in Gwen's presence."
    "I still have no idea just what the woman did to her while they were together, as Anna won't tell me."
    "But the sight of her cowering away from her ex again makes me all the more determined to defend her."
    mike.say "This is a private conversation, Gwen."
    mike.say "Nothing intended for your ears."
    mike.say "And neither of us has got anything to say to you either."
    show gwen teaser at right4 with move
    "Gwen rounds on me, trying to use the fact that she has almost a full head in height over me to her advantage."
    "She smiles in a patronising manner, pretending not to have noticed me before I spoke up just now."
    "Gwendoline" "Oh, there you are!"
    "Gwendoline" "[hero.name], isn't it?"
    "Gwendoline" "Sorry, I don't make a habit of noticing the rats that come along for my leftovers!"
    mike.say "Funny, you call Anna something like that, sure."
    mike.say "But you don't seem to be able to keep away yourself, do you?"
    "At this, Gwen makes a disdainful snorting sound and curls her lip at me."
    "She's not about to admit as much, but she knows that I've got her on that point."
    "Try as she might, there's no way she can keep on pretending that she's moved on from Anna."
    "Not if she can't keep herself from seeking her out at every given opportunity."
    "Gwendoline" "Huh...whatever!"
    "Gwendoline" "So this guy's speaking for you now, Anna?"
    "Gwendoline" "When did you lose your tongue?"
    "Clever move - regrouping and taking Anna to task on her silence as a cover for her own loss of the last round."
    "Also trying to drive a wedge between the two of us by suggesting that I'm not letting her stand up for herself."
    "This girl must have been a proper headfuck to be around on a regular basis!"
    mike.say "I'm not speaking for her, Gwen."
    mike.say "I'm speaking for myself."
    mike.say "And I'm still speaking for myself when I say this - fuck off, or I'll put you on your arse!"
    show gwen teaser at right5 with move
    "For the first time since she appeared, Gwen actually looks concerned, taking a step backwards."
    "I follow her, closing the space between us, yet being careful not to stand in front of Anna as I do so."
    "I want Gwen to get that I'm fronting up to her for my own reasons, not to be Anna's knight in shining armour."
    "Gwendoline" "You...you can't be serious!"
    "Gwendoline" "Are you actually...threatening me?!?"
    "I shake my head as I continue to advance on her slowly."
    mike.say "No, Gwen."
    mike.say "A threat would be me saying I'll do one thing unless you do another."
    mike.say "I, on the other hand, just made a statement of fact."
    mike.say "I am going to kick your ass, and the only thing you can do about it is to make it impossible by running away."
    show gwen teaser at right with move
    "Gwen betrays her doubt and fear by looking over her shoulder for a means of escape, and then quickly back again."
    "Gwendoline" "You're bluffing...you're not really going to fight me!"
    mike.say "Because you're a woman?"
    mike.say "Please, Gwen - this is the twenty-first century, and you're more than big enough to look after yourself."
    mike.say "Unless you're only into picking on people smaller than you, huh?"
    mike.say "In which case, you're a bully, and that's reason alone to teach you a lesson..."
    "For all my talk, I'm pretty damn scared of what I'm doing right now."
    "I don't want to fight anyone, man or woman, let alone someone of Gwen's size and build!"
    "She could be a black-belt in something, or knock me the fuck out!"
    "My only hope is that I can call her bluff."
    "Gwendoline" "Seriously, man - you have some fucked up issues going on there!"
    hide gwen teaser with moveoutright
    show anna blush at center with move
    "And with that, she turns her back on me and disappears into the crowd."
    "Once I'm sure she's well out of sight, I let myself sag as though the air is draining out of my entire body."
    anna.say "Wow, [hero.name]!"
    anna.say "Would you really have beaten her up...for me?"
    mike.say "Sure, Anna - that's what friends are for, right?"
    "But even as I'm saying this, the look of gratitude in Anna's large eyes is making me want to be much more."
    return

label anna_event_06:
    if anna.love.max < 140:
        $ anna.love.max = 140
    "I know that Anna can be distracted, even a little ditzy at times, it's something I find cute and endearing about her."
    "But there are times when she takes it a bit too far, and then it tends to get annoying really quickly."
    "Tonight's a perfect example - we're supposed to be enjoying a nice meal in an even nicer restaurant."
    "It's not like I'm laying on the champagne and caviar, but I am trying my best to make it special."
    "Anna, on the other hand, is acting like she's here in body alone, her mind off on another planet."
    "She's hardly touched her food, and the best I can get out of her are yes and no answers."
    "I cough, and then resort to making even more obvious sounds of annoyance, but to no avail."
    show anna b annoyed at center, zoomAt(1.5, (640, 1040))
    mike.say "How do you like the food, Anna?"
    anna.say "Hmm...Oh yeah, that's right."
    mike.say "Mine tastes like burnt rubber - how about yours?"
    anna.say "Mmm...it's so romantic."
    mike.say "I asked the waiter to serve you roasted dog."
    mike.say "I know you're really into eating man's best friend."
    anna.say "Yeah..."
    show anna surprised
    anna.say "Wait...what?!?"
    "For the first time since we sat down to eat, Anna looks like she's actually back in the room with me."
    show anna normal
    "I shake my head, at least thankful that I didn't have to get up and do some kind of dance to snap her out of it."
    mike.say "I think I should be the one asking that, Anna."
    mike.say "What's up with you tonight?"
    mike.say "It's like you're off with the fairies or something."
    show anna blush
    "Anna's cheeks colour a little as she realises what she's done."
    "Which tells me that she's been even more preoccupied than I thought."
    "And the fact that she had no idea she was doing it serves to soften my mood."
    "After all, if there's something that serious on her mind, then the last thing she needs is me making it worse."
    anna.say "Oh, [hero.name]..."
    anna.say "I'm sorry - I've ruined our date!"
    mike.say "Hey, hey - it's okay, Anna."
    mike.say "You haven't ruined anything."
    mike.say "I'm just worried about you, that's all."
    show anna happy
    "Anna manages to give me a weak smile, beginning to open up a little."
    show anna normal
    mike.say "You can tell me what's up, Anna."
    mike.say "A problem shared, you know..."
    anna.say "O..okay, [hero.name], if you say so."
    anna.say "I kind of had a falling out...with Kleio."
    if Harem.together(anna, kleio):
        "So that explains why Kleio didn't want to come along with us tonight."
        "Come to think of it, she didn't even bother to come up with a halfway believable excuse either."
        "So this must have been quite a clash between the two of them!"
        "All the more reason for me to play the role of peacemaker."
        "The last thing I want is for them to fall out so badly that it breaks the three of us up!"
    else:
        "That'd make sense - I've seen and heard what it's like to get both barrels when it comes to Kleio!"
        "And Anna's never been the most assertive of girls either."
        "It's hard to imagine her being able to hold her own in an argument between the two of them."
        "I guess what I'm getting here is the fallout of the ear-bashing she must have taken."
    mike.say "Well, it's not exactly hard to butt heads with someone like Kleio, is it?"
    mike.say "What did you argue about?"
    show anna annoyed
    "Only now do I see a hint of anger and irritation creep onto Anna's face."
    "At first I wonder if I've said the wrong thing."
    "But then I realise that she must be getting mad at the memory of the argument."
    show anna angry
    anna.say "You won't believe this, [hero.name]."
    anna.say "But the bitch actually said that I was too meek...too meek and shy!"
    "It's all that I can do to keep from stating the obvious and agreeing with Kleio."
    "But instead I bite down on my lip, nodding my head in agreement and sympathy."
    anna.say "I mean...can you believe she even said that?!?"
    menu:
        "Agree with Kleio":
            $ anna.sub += 5
            show anna annoyed
            "What I say next might end up with me getting a prized part of my anatomy hacked off."
            "But there's a big part of me that thinks this isn't a time to avoid a painful truth."
            mike.say "Ah, Anna..."
            mike.say "Have you ever thought that Kleio might have a point?"
            "It takes a couple of seconds for what I just said to fully sink in."
            "And when it does, I see Anna's eyes go wide with surprise."
            show anna surprised
            anna.say "Wha...what?"
            anna.say "You...you think she's right?"
            "I hold up my hands, hoping to stop Anna from careering off a cliff of despair before the cheque arrives."
            show anna annoyed
            "If I get this next part just right, I'm sure I can save this thing from disaster."
            mike.say "No, Anna, no - that's not what I mean."
            mike.say "You know how Kleio is, right?"
            mike.say "She has to make everything she says dramatic as fuck."
            show anna angry
            anna.say "Yeah, but you said she was right!"
            show anna annoyed
            mike.say "No, Anna - I said she might have a point."
            mike.say "You can be a bit quiet at times, you know?"
            anna.say "You think I'm like a little mouse, or something?"
            mike.say "Again, no - just that you're a tiny bit shy, that's all."
            "I reach across the table and take her hand in mine."
            mike.say "All I'm trying to say, Anna, is that you do have a voice."
            mike.say "And I don't think it'd be a bad thing for you to use it."
            "Though she doesn't look one hundred percent convinced, Anna still nods at this."
            anna.say "I...um...I don't know, [hero.name]."
        "Agree with Anna":
            $ anna.love += 5
            show anna annoyed
            "I know that Kleio has a point, as Anna can be like a shy little mouse at her worst."
            "But that doesn't give her the right to beat Anna into submission with her opinions."
            mike.say "Jesus, Anna..."
            mike.say "That mouth of hers is going to get Kleio into trouble one day."
            show anna normal
            "I see hope flare in Anna's eyes as I can't help shaking my head."
            "It's pretty obvious that she's been looking for an ally against Kleio in this matter."
            anna.say "I know, right!"
            anna.say "Where does she get off talking to me like that?"
            "I stop shaking my head at this and start nodding instead."
            "But part of me can't help wondering why Anna can't be this irate with someone like Kleio too."
            mike.say "That's Kleio through and through, Anna."
            mike.say "She doesn't get that not everyone's like her."
            mike.say "Sure, she's confident, forthright and knows her own mind."
            mike.say "But that's not how you are, Anna."
            anna.say "Erm...yeah...I guess so."
            mike.say "Some people just don't like confrontation."
            mike.say "They don't need to be the centre of attention, you know?"
            "Anna looks down at her lap, and I realise that I might have been underselling her unique qualities."
            mike.say "They're deeper than that, you understand?"
            mike.say "Not the kind of empty vessel that makes all of the noise."
            show anna happy
            anna.say "Ah...my drums are pretty loud, though..."
            mike.say "I don't mean literally, Anna!"
            show anna surprised
            anna.say "Oh...sorry, [hero.name]!"
    show anna normal
    "Both Anna and I try to forget about the subject for the rest of the meal."
    "But even though we're both making a real effort, it still hangs over us."
    "And part of me thinks that no amount of words between the two of us is going to settle the matter."
    return

label anna_event_07:
    if anna.love.max < 150:
        $ anna.love.max = 150
    "I'll admit that I spent some time waiting for the explosion to hit me from Anna and Kleio getting together to talk it out."
    "For a while I felt like I was going around like a guy with his fingers in his ears, fearing the inevitable bang."
    "So when I finally get a call from Anna, I answer it with understandable feelings of trepidation."
    mike.say "Erm...hey, Anna."
    mike.say "What's up?"
    anna.say "Aw, [hero.name] - you sound all shaken up!"
    anna.say "Are you okay?"
    mike.say "Yeah, Anna - I'm fine."
    mike.say "So...how did it go with Kleio?"
    "I'd been expecting a long silence, and then perhaps another round of drama."
    "But then Anna surprises me by starting to babble in a happy tone."
    anna.say "Oh, that!"
    "Christ, she says it like the argument was nothing at all!"
    anna.say "That's all done with now."
    anna.say "Kleio's here right now, with me!"
    kleio.say "Hey there, Loverboy!"
    "I can hear Kleio's voice as she leans in close to Anna."
    anna.say "We want to meet up with you, [hero.name]."
    anna.say "So that we can thank you in person!"
    mike.say "Okay, Anna - I guess that's not a problem."
    show bg street with dissolve
    "So that's how I end up waiting at the agreed spot, watching for a sight of Anna and Kleio."
    show anna b casual at left4
    show kleio casual at right4
    with dissolve
    "And to my great relief, they turn up late, but walking along arm in arm."
    "In fact, I haven't seen them looking this laid back together in some time."
    "As soon as she lays eyes on me, Anna waves eagerly."
    show anna happy
    anna.say "Hey, [hero.name]!"
    show anna normal
    show kleio seductive
    kleio.say "What's up - your dick go limp while you were waiting?"
    if not Harem.together(anna, kleio):
        mike.say "Ha, ha, Kleio, very funny."
        mike.say "I was actually more worried about the pair of you."
        show kleio normal
        "Kleio smirks at this, dismissing my concern in characteristic fashion."
        "But Anna's quick to come to my rescue, slapping her friend on the arm."
        anna.say "Hey, Kleio - don't be mean!"
        anna.say "If it wasn't for [hero.name], we'd still be fighting!"
        "Kleio waves her words away too."
        "But I know the taller girl well enough to sense a softening of mood."
        kleio.say "Geez, Anna, don't shit yourself!"
        kleio.say "I'm only yanking his chain."
        anna.say "Well you could actually show it, Kleio."
        show kleio surprised
        "Kleio looks at her for a moment, almost as if she's surprised at Anna's insistence."
        show kleio normal
        kleio.say "Thanks, [hero.name]."
        show kleio annoyed
        kleio.say "There, Anna - happy now?"
        "I'm more than a little surprised myself."
        show kleio normal
        show anna happy
        "Is this my first glimpse of a more assertive version of Anna?"
        anna.say "It's a start, Kleio."
        show anna normal
        mike.say "It's okay, guys - you don't have to thank me."
        mike.say "All I ever wanted was for you to bury the hatchet."
        "Anna nods at this, and even Kleio shrugs in agreement."
        anna.say "And the really great thing is that if we ever fall out again - we can just call you, [hero.name]!"
        with hpunch
        "Anna underlines this statement by suddenly wrapping her arms around me."
        "As she pulls me into a pretty ferocious hug, I look up at Kleio in quiet desperation."
        "But all I get from her in response is a face that seems to say 'you break it, you bought it'."
    else:
        mike.say "If it did, seeing you two cured that straight away!"
        show kleio blush
        show anna surprised
        "The comment gets a pretty filthy chuckle from Kleio as she walks up."
        "Anna gasps with surprise, but I can see a similar reaction in her eyes."
        show anna blush
        kleio.say "Yeah, well, you're not the only one, Loverboy."
        kleio.say "I'm getting so wet right now, it feels like I pissed my panties!"
        show kleio kiss
        $ kleio.flags.kiss += 1
        "And with that, she wraps her arms around my neck and plants a kiss on my lips."
        "Even as she does so, I can feel Anna worming her way into the embrace too."
        show kleio annoyed with hpunch
        anna.say "Hey, you guys - don't forget about me!"
        anna.say "If there's make-up sex on offer - my ass wants some of that action too!"
        show kleio angry
        kleio.say "Fuck sake, Anna - you dirty little bitch!"
        show anna happy
        show kleio happy
        "As hard as it is to do, I force myself to pull back from them just a little."
        mike.say "Whoa, hold on for a minute, guys."
        mike.say "Do I take it from all of this suppressed libido that you're both cool with each other now?"
        show anna blush
        show kleio seductive
        "Anna and Kleio glance at each other for a moment, both looking just a little sheepish."
        anna.say "Yeah, [hero.name], we sorted it."
        kleio.say "Sure thing - once Anna admitted it was all her fault!"
        show anna angry
        anna.say "KLEIO!!!"
        show kleio happy
        show anna normal
        kleio.say "Alright, alright..."
        kleio.say "Don't shit yourself!"
        show kleio normal
        kleio.say "Yeah, we sorted it out, sure we did."
        "It's all I can do to keep from sagging with a sigh of relief at hearing that."
        mike.say "That's great, guys - really it is."
        mike.say "Now what was that I heard about make-up sex?"
    hide bg street
    hide anna
    hide kleio
    return

label anna_getting_serious_01:
label anna_event_08:
    show bg street
    show anna
    "It's weird, you know, the way that you never actually take a step back and realize that something is going well."
    "I guess that at the time it's happening, you're too wrapped up in the moment to be able to step back."
    "Only later do you have the chance to think about how much you enjoyed yourself, all the time you spent laughing."
    "But then the flip side of that is the way you always notice when something seems to be even a little amiss."
    "And I get that second feeling almost as soon as Anna and I are walking home from our date."
    "It really is weird, as everything went well tonight, all I remember being fun and laughter."
    "It's only now that I notice Anna's gone quiet, letting me do most of the talking."
    "Now that's strange, as she's usually an unstoppable source of chatter."
    "Instead she seems to be content merely to cling to my arm, staring up at me the whole time."
    "If she was pissed off with something that I said, then I'd have been able to read it in her mood."
    "But this is different, more like her whole attitude towards me has undergone a subtle change."
    mike.say "Anna?"
    anna.say "Hmm..."
    mike.say "Anna, are you okay?"
    show anna surprised at hshake
    anna.say "Wha...oh, sorry, [hero.name]."
    anna.say "I was miles away!"
    mike.say "Yeah, I kind of noticed that."
    show anna blush
    "Anna blushes a little, her cheeks flushing with color."
    "She looks away, clearly embarrassed at being called out on her ditziness."
    "But I can't help smiling at her reaction, as her quirks have never been something that annoyed me."
    "In fact, they're one of the things about her that I can't help but find endearing."
    mike.say "You want to tell me what's on your mind, Anna?"
    mike.say "Maybe that way we can get on the same wavelength!"
    anna.say "I...well..."
    mike.say "It's okay, Anna."
    mike.say "I'm not mad or anything - just curious, that's all."
    show anna normal
    "She nods at this, almost visibly drawing strength from my words."
    anna.say "Well, [hero.name]..."
    anna.say "What's on my mind is...you!"
    mike.say "Me?!?"
    anna.say "Yeah, [hero.name]."
    anna.say "I was thinking about how much I like spending time with you."
    anna.say "How much I like us hanging out together."
    anna.say "How much I like it being just you and me!"
    "For a moment, her words leave me staring at her in silence."
    "Because it's at that moment my brain finally wakes up to just what's happening here."
    "Something just changed between Anna and me."
    "Something too subtle for my poor brain to notice on its own."
    "We're not a couple of friends hanging out anymore."
    "We're not even a couple of friends hanging out as a lame cover for really liking each other."
    "We just crossed over into being a couple that are actually dating!"
    "I expect to feel a wave of panic overtake me, that typical fear of commitment."
    "But it doesn't materialize, and instead I feel a warm sensation rising in my chest."
    "It's weird, but it makes me want to gaze at Anna in the exact same way she's looking at me..."
    mike.say "Me too, Anna."
    mike.say "It's great to do fun stuff with you."
    mike.say "But the best part is just being with you."
    show anna b happy at center, zoomAt (1.65, (650, 1140))
    "Anna's face breaks into a delighted smile, and she hugs me tightly."
    "I can feel every inch of her petite body as she presses herself against me."
    show anna normal
    anna.say "Then let's spend lots more time together, [hero.name]!"
    anna.say "As much time as we can possibly spare!"
    "I nod happily, already looking forward to taking Anna up on her offer."
    if anna.love.max < 160:
        $ anna.love.max = 160
    return

label anna_confession:
label anna_event_09:
    "Normally I'd hardly notice Anna being scatter-brained and ditzy in general."
    "As that's pretty much how she is most of the time, give or take the occasional moment of clarity."
    "But just recently she's been even more confused and indecisive than usual."
    "It's almost as though something's happened to make her brain go on the fritz."
    "What makes it even more strange is the fact that no one else seems to notice it either."
    "Sasha never makes as much as a comment about it when the subject of Anna comes up at home."
    "And beyond the usual verbal sparring between them, Kleio's the exact same story."
    "You can call me slow if you like, but it takes me a while to realize what the common element is here."
    "It's me - Anna's acting normal around everyone else and yet tying herself in a knot whenever we're together."
    "Of course, I react to this in a level-headed and perfectly rational manner."
    "Weighing up all of the possibilities, I examine each one in terms of merit and practicality."
    "And only then do I panic and jump to the conclusion that Anna's contemplating how to dump me."
    "No matter how much I try, I just can't shake the conviction."
    show anna
    "Which means that by the next time we meet up, I'm a quaking bag of nerves."
    "I can't look Anna in the eye without fear of her using that as the chance she's waiting for."
    "Any moment I expect the words to come out of her mouth that'll end it all between us."
    "And so, in the end, the only thing I can do is face it head on..."
    mike.say "Anna..."
    anna.say "Huh?"
    mike.say "Is there anything wrong?"
    mike.say "You know, anything you'd like to talk about?"
    anna.say "Erm...like what, [hero.name]?"
    mike.say "Anything about...us?"
    "The question seems to snap Anna out of her usual state of mild distraction."
    show anna surprised
    "I see her eyes go wide and her cheeks flush, which makes me fear the worst."
    mike.say "Please, Anna - tell me what's up."
    mike.say "You've been on another planet for days now."
    mike.say "And I need to know what's bugging you."
    show anna blush
    "Anna looks away for a moment, and then back again."
    "Right now she reminds me of a deer in the headlights."
    "Like she wants to bolt, but is afraid of the consequences."
    anna.say "I...I want to, [hero.name]."
    anna.say "But I don't know if I should!"
    "I take a deep breath, steeling myself for what lies ahead."
    "Whatever Anna's keeping bottled up, I really need to know."
    "We just can't go on like this any longer."
    "If we do, it's sure to kill off what we have simply by hanging over us the whole time."
    mike.say "Anna, it's okay."
    mike.say "I won't get mad - I promise you that."
    show anna normal
    "I take hold of Anna's hands as I say this, wrapping them in mine."
    "She glances down as I do this, her eyes still fearful."
    "And it's only now that I notice that she's actually trembling."
    anna.say "Okay, if you promise you won't be mad..."
    anna.say "I think..."
    show anna blush
    anna.say "I think I've fallen in love with you..."
    "It takes a good couple of seconds for me to actually realize what Anna just said."
    "I'd been so prepared for a verbal and emotional punch to the gut."
    "But she just floored me with something entirely different."
    mike.say "Anna..."
    mike.say "Are you serious?!?"
    anna.say "I am...really."
    anna.say "Oh shit - I knew you'd be mad!"
    mike.say "No, Anna, no!"
    mike.say "I thought you were going to dump me!"
    show anna b at center, zoomAt (1.65, (650, 1140))
    with hpunch
    "At this, Anna literally throws herself at me."
    "Wrapping her arms around my waist, she pulls me into a surprisingly fierce embrace."
    anna.say "No, no, no!"
    anna.say "[hero.name], how could you even think that?!?"
    anna.say "I LOVE YOU!"
    "For the second time in as many minutes, Anna manages to leave me stunned."
    "All I can do is return her embrace, struggling to comprehend her confession."
    mike.say "I..."
    mike.say "I love you too, Anna."
    "This time it's Anna's turn to remain silent, simply hugging me as tightly as possible."
    "I can feel my heart racing in my chest, beating like it's going to explode any second."
    "But I don't know if it's on account of the adrenaline still coursing through my body."
    "Or whether it's because I just realized that Anna and I are actually in love with one another..."
    if anna.love.max < 170:
        $ anna.love.max = 170
    return

label anna_getting_serious_02:
label anna_event_10:
    show bg street
    show anna
    "It's that time again, the time when the night is over and I have to say goodbye to Anna until we can meet up again."
    "Up until now, the date we've been on was just great, one of the best yet."
    "But suddenly I feel my mood changing at the thought of the long walk home and the empty bed waiting for me there."
    "I must have said goodbye to Anna more than a dozen times before, just like this."
    "And yet now I find that I want to do anything I can to delay the moment when I have to do so."
    "Anna doesn't seem to have picked up on my sudden change of mood, and keeps on talking away regardless."
    show anna angry
    anna.say "...and so I said to Kleio that she was DEAD wrong."
    anna.say "But then Sasha weighed in, totally without asking if she could, I should mention."
    anna.say "And she took Kleio's side against me - can you actually believe that?!?"
    "Anna throws up her hands to emphasize her outrage, clearly expecting me to echo the sentiment."
    "But my mind is still caught up on the strange feeling of trepidation at the night ending."
    show anna annoyed
    anna.say "[hero.name]!"
    anna.say "Are you even listening to me?"
    "I shake my head, trying as best I can to break out of the funk into which I've sunk."
    mike.say "Sorry, Anna..."
    mike.say "I just got distracted, you know?"
    mike.say "I guess I have something on my mind."
    show anna normal
    "Almost as soon as she detects the genuine ennui in my voice, Anna's mood softens."
    anna.say "Hey, [hero.name] - don't be sad, please!"
    anna.say "I thought we had a pretty good time tonight?"
    anna.say "I don't like it when you're upset - it makes me scared that you're growing tired of me!"
    "I've just about stopped shaking my head by the time Anna bursts out with this."
    "But her words set me off again, this time shaking it with much more speed and drama."
    mike.say "Oh shit..."
    mike.say "No, Anna...no way!"
    mike.say "That's not it at all."
    "Anna looks up at me, starting to pout a little as she digs for an answer."
    "I know that look well, that it means she's looking to me to allay her fears."
    "And that's exactly what I want to do right now too."
    anna.say "Then what is it, [hero.name]?"
    anna.say "Huh?"
    mike.say "Ah...it's weird, Anna."
    mike.say "I just...don't want to go home alone."
    mike.say "I guess I'm a little scared of being lonely, that's all."
    show anna happy
    "Suddenly, I see a light go on behind Anna's eyes."
    "She smiles like a Cheshire cat, practically beaming up at me."
    anna.say "You really mean that, [hero.name]?"
    anna.say "You miss me that much when we're apart?"
    "All I can do is nod slowly, afraid of being overwhelmed by Anna's enthusiasm."
    "Well, that and the fact that I don't feel like I could lie about this, even if I tried."
    "She's put into words what I was struggling to - that I'm afraid of being without her."
    mike.say "Yeah, Anna, that's right."
    mike.say "I don't want my time with you to end."
    show anna b blush at center, zoomAt (1.65, (650, 1140))
    "Anna wraps her arms around my waist, gently pulling me into her embrace."
    "I respond in kind wrapping her in my arms too."
    "For once, she doesn't say a word."
    "But then I guess she doesn't need to."
    "As I hold Anna close to me, I begin to weigh up the evidence."
    "I get a funny feeling in my gut when she's around."
    "I'm almost afraid to think of her not being around."
    "And we're starting to communicate without the need for words."
    "I don't think that I can deny it any longer."
    "I'm falling for Anna."
    "And I'm falling fast!"
    $ anna.set_girlfriend()
    if anna.love.max < 180:
        $ anna.love.max = 180
    return

label anna_event_11:
    show bg livingroom
    if anna.love.max < 190:
        $ anna.love.max = 190
    "I guess in a way I'm pretty lucky to have found a girl the likes of Anna, and I should be thankful for that."
    show anna b blush at center, zoomAt (2, (650, 1050)) with dissolve
    "And I don't mean simply because of the fact that she's got the most amazing chest imaginable."
    "But also because she knows it and is pretty proud of the effect that it has on me as well!"
    "Like right now, for example - I just can't take my eyes off of them."
    "And is Anna rolling her eyes, cursing me for being a typical guy with a one-track mind?"
    show anna happy at center, zoomAt (2, (650, 1250)) with move
    "Hell no - she's smiling at the attention and loving the fact that I'm so into her!"
    show anna normal
    anna.say "Hey, [hero.name], you've been staring at them for ages."
    anna.say "Are you gonna ask to play with them, or what?"
    mike.say "Huh...are you serious?"
    show anna wink
    "Anna giggles and winks at me, squeezing her breasts between her arms."
    show anna normal
    anna.say "Sure I am!"
    anna.say "I see the way you're looking at me."
    anna.say "And it'd be a shame for all of that lust to just go to waste!"
    anna.say "So, what do you say?"
    "Before I can give what should be the easiest answer imaginable, I suddenly remember something."
    "Feeling like a complete loser, I glance at my watch and then slap myself in the forehead."
    mike.say "Damn it!"
    mike.say "I have to be somewhere in like half an hour!"
    mike.say "I'm sorry, Anna - can we do this another time?"
    "Anna shakes her head and waves away my concerns as though they're nothing."
    anna.say "Don't worry about it, [hero.name]."
    anna.say "I can get you off in less than that!"
    show anna blush
    anna.say "You just stick your cock right in there."
    "She looks down at the space between her breasts in the most suggestive way possible."
    anna.say "And leave the rest to me!"
    menu:
        "Accept":
            $ videotape = False
            "What, like you think there's any chance I was about to say no to an offer like that?!?"
            mike.say "Y...yeah, Anna!"
            mike.say "Sure thing!"
            show anna happy
            "Anna's smile becomes even wider as she takes my hand."
            anna.say "I had a feeling that you couldn't say no!"
            anna.say "Come on, let's go somewhere a little more private!"
        "Say you wanna record it":
            $ videotape = True
            $ anna.love -= 10
            $ anna.sub += 10
            "What, like you think there's any chance I was about to say no to an offer like that?!?"
            mike.say "Y...yeah, Anna!"
            mike.say "Sure thing!"
            show anna happy
            "Anna's smile becomes even wider as she takes my hand."
            anna.say "I had a feeling that you couldn't say no!"
            anna.say "Come on, let's go somewhere a little more private!"
            "But then a thought occurs to me, and I motion for Anna to stop."
            show anna surprised
            show fx exclamation
            anna.say "Huh...what's up?"
            mike.say "I was wondering if we could...maybe film it?"
            "Anna looks a little surprised at first, but then I see the idea start to sink in."
            show anna happy
            "Her smile returns and she looks at me sideways, clearly intrigued by the possibilities."
            anna.say "Sure, we could do that."
            anna.say "But where'd you get that idea?"
            show anna normal
            menu:
                "Say you want it for yourself":
                    mike.say "Well, you're going to be out of town in a week or so, right?"
                    "Anna nods."
                    anna.say "Sure, just for a couple of days."
                    anna.say "But I already told you about that."
                    anna.say "And you were okay with it."
                    mike.say "Oh, I am."
                    mike.say "I just...wanted something...to remind me of you."
                    mike.say "You know...until you're back."
                    "I find myself shrugging and even blushing a little at the admission."
                    show anna happy
                    "Anna smiles at me, clasping her hands together as if enchanted by the thought of it."
                    anna.say "Aww, [hero.name] - that's so sweet!"
                    anna.say "Of course you can film it."
                    anna.say "But first you have to promise me something."
                    mike.say "Erm, okay, Anna - what's that?"
                    anna.say "You have to promise me that you'll masturbate to it."
                    anna.say "Every single night until I get back and you can have the real thing, yeah?"
                    "I laugh and nod eagerly, which makes Anna do the same."
                "Say you want revenge on Gwen and Alexis":
                    mike.say "I thinking we could use it to get some revenge."
                    show anna surprised
                    "Anna looks quizzical at this, cocking her head on one side."
                    anna.say "Revenge?"
                    anna.say "On who?"
                    anna.say "For what?"
                    mike.say "Okay, Anna, hear me out."
                    mike.say "Your ex, Gwen - she treated you really shitty, right?"
                    show anna evil
                    "Anna's lip curls in distaste at the mere mention of her towering former girlfriend."
                    anna.say "Yeah, I really hate that lanky bitch!"
                    mike.say "I know exactly how you feel."
                    anna.say "You do?"
                    mike.say "Sure I do."
                    mike.say "One of my old girlfriends, Alexis - she cheated on me, broke my heart."
                    anna.say "So, we film ourselves having fun, and then send it to them?"
                    mike.say "That's it - kind of like a big 'fuck you' to them both!"
                    "Anna giggles evilly, shaking her head in disbelief at what I'm proposing."
                    anna.say "[hero.name], that sounds wicked!"
                    anna.say "We should so do it!"
    scene bg bedroom1
    show anna naked blush
    "Anna peels off the last of her clothes and hurries over to the bed, beckoning for me to follow."
    show anna naked b blush
    "I try to shed the last of my own at the same time, almost tripping over as I do so."
    "She chuckles as she clambers backwards onto the mattress, not stopping until her head hits the pillows."
    anna.say "Don't hit your head, [hero.name]."
    show anna wink
    anna.say "You're a guy - you're not supposed to fall unconscious until AFTER you cum!"
    show anna blush
    "As if the sight of her naked body before me wasn't enough, Anna's giggles are driving me mad too."
    "For a moment I'm actually afraid that I will knock myself out in my desperation to reach her."
    show anna at center, zoomAt (1.75, (650, 1050))
    "She beckons me closer as I climb onto the bed and crawl towards her, smiling over her breasts in approval."
    "By the time I've made it and I'm straddling Anna's belly, my cock is already painfully stiff."
    "It sways and bobs above her breasts, and she eyes it with a hunger that gets me even hotter than before."
    scene anna tittyfuck
    anna.say "Well hello there, big boy!"
    anna.say "I've got a couple of friends that are just dying to meet you..."
    "And with that, Anna wastes no more time on innuendo and foreplay."
    "Instead she pushes her breasts together, lightly at first."
    "Their heavy, rounded shapes completely cover the head and perhaps half the length the shaft."
    "The feeling is instantly incredible, like my cock's been wrapped in warm dough."
    if videotape:
        show anna tittyfuck phone movie
        "In my rush to catch up to Anna, I almost forgot that we'd agreed that I'd film this."
        "Luckily I can see my phone on the floor, where it must have tumbled from my pocket as I stripped off."
        "I strain and just manage to reach it, hurriedly setting it to record and getting Anna fully in frame."
        "She grins wickedly, clearly recalling just what we're going to use the video for."
    else:
        "Anna grins wickedly, clearly ready to go and relishing the thought of what we're about to do."
    show anna tittyfuck concentrate
    "Slowly, she begins to massage my cock with her breasts, kneading them as though they actually were dough."
    show anna tittyfuck down
    "It doesn't take long for the head to emerge from between them, swollen and red from the pressure."
    show anna tittyfuck up
    "Which in turn means that all of the sensations are now concentrated in the shaft instead."
    show anna tittyfuck down
    "I can't fully describe how it feels to have Anna doing this to me right now."
    show anna tittyfuck up
    "The only thing I can compare it to would be a regular hand-job."
    show anna tittyfuck down
    "But then where could you find a hand so big and so soft?"
    show anna tittyfuck up
    "The focus of the pressure might be moving up and down the whole time."
    show anna tittyfuck down
    "Yet Anna's breasts are so large that almost all of my cock is caught between them just the same."
    show anna tittyfuck up
    "And while the feeling of what she's doing to me is simply amazing, there's also the look on her face too."
    show anna tittyfuck down
    "Anna divides her attention between looking down at what she's doing and up at me."
    show anna tittyfuck up
    "One moment she's staring at the sight of my cock, jutting through her breasts."
    show anna tittyfuck down
    "And the next she looks up and catches my eye, grinning at reactions she sees written across my face."
    show anna tittyfuck speed up at startle(0.05,-10)
    "Suddenly I can feel a spasm travelling through my entire body."
    show anna tittyfuck speed down at startle(0.05,-10)
    "I've been so caught up in watching Anna's face that I totally fail to notice how much she's sped up."
    show anna tittyfuck speed up at startle(0.05,-10)
    "By now she's practically working her breasts into a lather around my cock."
    show anna tittyfuck speed down at startle(0.05,-10)
    "And the spasm that I just felt is the first hint that I'm about to cum."
    show anna tittyfuck speed up at startle(0.05,-10)
    "Before I can speak a single word to warn Anna, I realise that it's already too late."
    show anna tittyfuck -speed cum cumshot surprise with vpunch
    "I thrust my cock forward, sending a surge of cum straight into her face."
    show anna tittyfuck cum -cumshot face with vpunch
    "Anna's expression goes from intense to shocked in the blink of an eye."
    with vpunch
    "And blinking might have been a good idea for her in the same moment."
    "Not to mention keeping her mouth shut as well."
    show anna tittyfuck cum body
    "Instead she lays there, wide-eyed and with an open mouth as the streamers splatter over her."
    "But then her surprise seems to fade, and she smiles broadly before bursting into a fit of giggles."
    mike.say "Ah..."
    mike.say "Sorry, Anna!"
    show anna tittyfuck cum normal
    "Anna cocks her head on one side, still grinning up at me through a mask of cum."
    "She's still working away at my cock as she does so, as if determined to milk it dry."
    anna.say "You ever see those skits where someone looks down a hose-pipe for the water?"
    anna.say "I think I knew what I was gonna get when I agreed to this!"
    return

label anna_event_12:
    scene bg pub at dark
    show anna
    if anna.love.max < 200:
        $ anna.love.max = 200
    "It feels like a hell of a long time since I've been in the crowd at a really decent gig."
    if game.flags.band >= 2:
        "Sure, I've been on the stage with Anna and the rest of the Deathless Harpies a lot recently."
        "But that's not the same as being one of the fans in the crowd."
    "And there's nothing like being out there, soaking up the atmosphere!"
    "Apart maybe from doing all of that with Anna by my side."
    "She's been squeezing my hand and beaming up at me since we walked in through the doors!"
    show anna close happy with dissolve
    anna.say "Oh...my...fucking...god, [hero.name]."
    anna.say "I still can't believe you managed to score Metallikea tickets!"
    anna.say "They always sell out super-quick."
    "I try to keep a tight hold of Anna as we start to weave through the crowd."
    "We've been inside the venue for what feels like less than ten minutes by now."
    "But it's already getting so busy we're having to elbow a path between the bodies."
    mike.say "I guess it was just plain, dumb luck, Anna."
    mike.say "Must have been that I got in there before everyone else!"
    "I'm not about to admit the countless hours I spent on hold calling the ticket-line."
    "Or the fleecing that I had to endure from a scalper when the first plan failed."
    "All that matters is the look of sheer delight on Anna's face right now."
    show anna blush
    "Well, that and the way she's looking at me too."
    "Like I'm the one thing she loves almost as much as the band we're here to see."
    "In my state of bliss at Anna's obvious delight, I'm not paying attention to just where we're going."
    "And before I know it, she's burrowed her way through most of the crowd."
    "Anna keeps on elbowing and squeezing forwards until we reach the barriers at the very front."
    "It's no problem for me, as I can easily see over the heads or shoulders of the people before me."
    "Anna, on the other hand, is already struggling to glimpse anything at all from here."
    "She tries standing on her tip-toes, then jumping up and down on the spot."
    "But it's no good, she can't hope to see the stage without a box to stand on or stilts!"
    mike.say "Erm, Anna..."
    mike.say "Maybe we'd have a better view from the back?"

    show anna surprised
    show fx exclamation
    anna.say "Are you mad?!?"
    anna.say "This is a Metallikea gig, [hero.name]."
    anna.say "Who wants to miss out on being as close as possible?!?"
    hide fx
    show layer master at lparty
    "Just then the lights go up and the crowd roars in anticipation."
    "Even worse, they rush forwards in the hope of getting the best view possible too."
    play music "music/TeknoAXE/simple_metal.ogg" loop fadeout .5 fadein .5
    with vpunch
    "Anna and I are almost swept off our feet, even before the start of the first song!"
    "I struggle to stay on my feet and hold her up at the same time."
    "But things only get worse once the opening chords thunder through the PA system."
    "Holding onto Anna for dear life, I recognise the song that they're opening up with."
    "It's a super-heavy number that almost always whips the crowd up into a frenzy."
    "And that means only one thing - MOSH PIT!!!"
    with vpunch
    "The first body slams into me from behind a second later."
    show anna dazed at hshake
    "I hear Anna let out a scream that could be of terror or delight."
    "Only just managing to keep upright, I know now that I'm the only thing that can save her!"
    if hero.fitness >= 50:
        "It's a damn good job that I'm a mosh-pit veteran with the scars to prove it!"
        "Even before second body hits me, I'm already moving and taking Anna with me."
        "I roll with the blows as they start to come from all sides."
        with hpunch
        "But at the same time, I'm trying to use them to my advantage, bouncing here and there."
        show anna at hshake
        anna.say "[hero.name]!"
        anna.say "Help me!"
        "I could stop and ask Anna what the hell she thinks I'm trying to do right now!"
        "But I doubt that she'd hear a word of it if I did so."
        "Instead I keep us moving, making sure that I take any blow that looks like it might hit her."
        "The fact that I'm actively looking for Anna means that I can't defend myself too."
        with hpunch
        "Heads butt against mine, elbows slam into my ribs and more than one knee connects with my groin."
        "At one point, I even bite down on my tongue and taste blood."
        "And then, just when I think I might be on the verge of passing out, it's all over."
        "Battered and bruised, I finally stagger out of the crowd when the song ends."
        "I honestly think I'd have collapsed, were it not for Anna holding me up."
        show anna close normal with dissolve
        anna.say "[hero.name] - are you okay?"
        "There's genuine concern in her voice as she looks up at me."
        "I shake my head, trying to dismiss her worries."
        mike.say "Don't worry about me, Anna..."
        "The impression is kind of ruined as I break off in pain for a second."
        mike.say "Seriously - how are you?"
        show anna happy
        anna.say "I'm fine, [hero.name] - thanks to you."
        show anna blush
        anna.say "You saved me from getting trampled back there!"
        hide anna
        show anna kiss with fade
        $ anna.flags.kiss += 1
        "She pulls me down to her level, planting a kiss on my lips."
        "It's full-on, genuine and filled with passion."
        hide anna
        show anna close blush
        with fade
        "But Anna breaks it off when I wince and cry out in pain."
        anna.say "Oh, goodness."
        anna.say "My poor, wounded hero!"
        anna.say "Come on - let's get you up to the balcony."
        show anna happy
        anna.say "Nurse Anna prescribes a beer and all of her attention!"
        "I nod and do my best to follow as Anna leads me away from the crowd."
        "And if she wants to dote on me for the rest of the night, who am I to argue?"
        "After all, she did say that I was her hero!"
    else:
        "Though I manage to roll with the first body that hits me, the second is a different story."
        with hpunch
        "Still staggering from the first, this one winds me and I lose my grip on Anna."
        "Before I can even see which way I've been pushed, she's snatched away from me."
        hide anna at vshake with moveoutright
        "Being so short, it's not even like I can pick her out in the sea of bobbing heads either."
        anna.say "[hero.name]!"
        anna.say "Help me!"
        "Turning towards what I think is the direction of her voice, I plunge into the fray."
        with hpunch
        "But no matter how hard I push, shove and barge at the mass of bodies, it does no good."
        "And the fact that I'm actively looking for Anna means that I can't defend myself too."
        with vpunch
        "Heads butt against mine, elbows slam into my ribs and more than one knee connects with my groin."
        "At one point, I even bite down on my tongue and taste blood."
        "Battered and bruised, I finally stagger out of the crowd when the song ends."
        "Gasping for breath, I scan the crowd, desperately searching for a sign of Anna."
        anna.say "There you are!"
        "Stunned to hear the sound of her voice, I spin around to face Anna."
        show anna annoyed with dissolve
        "She's standing there, arms crossed over her chest and tapping her foot on the floor."
        "Sure, she looks a little dishevelled."
        "But it's nothing compared to the mess I must be in right now!"
        mike.say "Anna..."
        mike.say "How did you..."
        show anna normal
        anna.say "One of the security guys pulled me out after a few seconds."
        show anna angry
        anna.say "No thanks to you!"
        anna.say "Did you push me in there on purpose so that'd happen, huh?"
        show anna annoyed
        "I stare at her for a moment."
        "My mouth moving and no words coming out."
        $ anna.love -= 15
        anna.say "Oh don't be such a big baby, [hero.name]!"
        show anna normal
        anna.say "Let's go find a spot on the balcony - just like you wanted!"
        "Anna grabs my wrist and drags me painfully after her."
        "I spend the rest of the gig sulking and in pain from my many wounds."
        "All the time marvelling at her assumption that I got my ass kicked on purpose!"
    return

label anna_event_13:
    scene bg pub
    "I love doing exciting stuff with Anna, the kind of things that will make great memories that we'll never forget."
    "But it's also nice to have the chance to actually sit down and spend some quality time with her."
    "You know - just chat and laugh together, enjoy each other's company."
    show drink anna with dissolve
    "Like right now, we're sitting in the Winchester, having a drink and talking about whatever springs to mind."
    "It reminds me of just how sweet and funny Anna actually is, as well as being so damn hot!"
    "And it also reminds me of how much of a lucky guy I am to be with her too."
    "I watch as Anna drains the last of her beer and then places the empty glass on the table."
    "She can't help letting out a little belch a second later, blushing as she does so."
    anna.say "Oops..."
    anna.say "Sorry, [hero.name]!"
    mike.say "It's okay, Anna."
    mike.say "Do you want me to get you another?"
    "Anna giggles at the offer, cocking her head on one side in an exaggerated motion."
    "And it's only now that I see she's flushed from the alcohol as well as the embarrassment."
    anna.say "Hey..."
    anna.say "Are you trying to get me drunk?!?"
    "I feel like pointing out that that ship's already sailed."
    "But instead I bite my tongue and laugh along with Anna."
    mike.say "What if I am, huh?"
    mike.say "You're pretty cute when you're drunk, Anna!"
    mike.say "And I know that you like me taking advantage of you..."
    "At this, Anna practically explodes into a flood of tittering laughter."
    "She slaps me playfully on the chest, but I can already see the look in her eyes."
    "It's the look that I know means she's imagining the possibilities for later tonight..."
    hide drink
    show gwen teaser at left with moveinleft
    "Gwendoline" "Urgh!"
    "Gwendoline" "Get a damn room!"
    show gwen teaser at right with move
    "The voice belongs to someone walking by our table on the way to the bar."
    "It's pretty deep and belongs to a tall person that I at first take for a guy."
    show anna b annoyed at left
    "But then I see Anna's face turn dark with anger, and I realise it's not a guy at all."
    "In fact, it's far worse than that!"
    show anna angry
    anna.say "GWEN!"
    anna.say "What did you just say?!?"
    show anna annoyed
    show gwen teaser at right4 with move
    "Before I can say a word, Anna's former girlfriend spins on her heel."
    "Gwen glowers down at us, using every inch of height that she possesses to her advantage."
    "Gwendoline" "You heard what I said, Anna."
    "Gwendoline" "Bad enough you lowered your standards after what we had."
    "Gwendoline" "But do you really have to slobber over that loser in public?"
    mike.say "Hey - who are you calling a loser?!?"
    "Almost as one, Anna and Gwen both round on me."
    "Gwendoline" "Ah, shut up."
    "Gwendoline" "I didn't ask her talking dildo for its opinion!"
    show anna angry
    anna.say "Don't you talk to him like that, you bitch!"
    show anna annoyed
    anna.say "But seriously, [hero.name], shut up."
    anna.say "This is my fight."
    anna.say "It's time that I stood up to her, once and for all!"
    "Gwen bursts out laughing at Anna's proclamation, crossing her arms over her chest."
    "From where I'm sitting, it only serves to make her look all the more like a fairy-tale ogre."
    "In fact, I wouldn't be surprised to hear her fire back with a threat to grind my bones to make her bread!"
    "Gwendoline" "Don't make me laugh any louder, Anna."
    "Gwendoline" "What are you gonna do, huh?"
    "Gwendoline" "Punch me in the kneecaps?"
    "Gwendoline" "Nip at my heels?"
    show anna angry
    "I can see the rage building in Anna by the second."
    "And now the red in her cheeks is on account of sheer hatred for Gwen!"
    "Before I can stop her, she's hopped onto the seat of her chair."
    show anna at left4 with move
    "Anna squats like a cat for a moment, then launches herself at Gwen."
    "Taken as much by surprise as me, the taller girl has no time to defend herself."
    play sound punch_hard
    pause 0.2
    show gwen teaser at vshake
    show gwen teaser at right, onknees with move
    "Which means that when Anna's clenched fist connects with her chin, she collapses like a house of cards."
    show anna a at flip, right5 with move
    "Gwen lands in a heap on the floor of the pub, and Anna lands atop her."
    "She grabs a handful of Gwen's collar and raises her other fist for a second blow."
    "Gwendoline" "No..."
    "Gwendoline" "No, Anna - please!"
    hide gwen
    hide anna
    with moveoutbottom
    menu:
        "Watch":
            "I should be telling Anna to stop right now."
            "But part of me knows that she needs to do this thing."
            "Gwen looks utterly shocked at what's happening."
            "I guess that she never thought Anna had it in her!"
            anna.say "Don't you cry off on me now, bitch!"
            "Anna's fist descends."
            play sound punch_hard
            pause 0.2
            with vpunch
            "And there's the sickening sound of snapping cartilage."
            "Gwendoline" "Aaah..."
            "Gwendoline" "Shit, shit, shit!"
            "Gwendoline" "You broke my fucking nose!"
            show anna evil at right5 with moveinbottom
            "Anna climbs off of the taller girl."
            "She dusts off her hands with a satisfied grin on her face."
            anna.say "You asked for it, Gwen."
            anna.say "I should have done that a LONG time ago!"
            "It's only now that Anna actually looks at me."
            "And instantly I can see the confidence in her waver."
            "It's obvious to me that she's looking for my approval of her actions."
            hide anna
            show anna normal close a
            mike.say "Wow, Anna - you're my hero!"
            mike.say "Next time someone picks on me, I'll give you a call!"
            show anna happy
            "Anna smiles at this, blushing for real this time."
            "She walks over to where I'm sitting and hauls me onto my feet."
            show anna blush
            anna.say "Come on, [hero.name]."
            anna.say "You get to take me home now!"
            mike.say "Whoa...okay, okay!"
            mike.say "Whatever you say, Anna."
            mike.say "Just promise you won't lay one on me too - unless it's a kiss!"
            show anna happy
            "Anna giggles as she wraps her arms in mine and we walk towards the door."
            "I can't keep my eyes off of her, not looking back at Gwen even once."
        "Protect Gwen":
            "I know that I should be cheering Anna on right now."
            "But the look on Gwen's face is one of genuine fear."
            "She's not even trying to fight back either."
            "What kind of guy would I be if I let her get beaten up like this?"
            mike.say "Anna - what in the hell are you doing?!?"
            "At the sound of my voice, Anna's fist freezes in mid-air."
            "Both she and Gwen stare up at me from the floor."
            "I think I can see relief and gratitude in Gwen's eyes."
            "But Anna just looks confused, like she can't understand what's happening."
            show anna normal at right5, onknees with moveinbottom
            anna.say "W...what do you mean?"
            anna.say "You heard what she said, [hero.name]!"
            mike.say "Sure I did, Anna."
            mike.say "But you were the one that threw the first punch!"
            mike.say "How does that make you any better than her?"
            show anna at right5 with move
            "Anna clambers off of Gwen, looking shameful and embarrassed."
            $ anna.love -= 20
            $ anna.sub += 10
            show anna cry
            anna.say "I...I'm sorry, [hero.name]."
            anna.say "I just saw red!"
            show anna at center with move
            "I shake my head as I get up and walk over to where Gwen is still sprawled on the floor."
            show gwen teaser at right, onknees with moveinbottom
            "Kneeling down, I help the taller girl to her feet without looking in Anna's direction."
            mike.say "Are you okay, Gwen?"
            "She looks at me in what seems to be sheer shock for a moment."
            show gwen teaser at right with move
            "But then she nods hastily, pulling away from me as she does so."
            "Gwendoline" "Y..yeah..."
            "Gwendoline" "I'm fine..."
            "And with that, she shoulders her way through the crowd and out of the pub."
            hide gwen with moveoutright
            "I sit back down and Anna follows me a moment later."
            "I can tell that she wants to ask me about what I just did, why I helped Gwen."
            "But the sting of being shown up in front of the entire pub is still weighing on her."
            "And so she sits there in silence, alone with her own thoughts."
    return

label anna_male_ending:

    if renpy.has_label("anna_achievement_3") and not game.flags.cheat:
        call anna_achievement_3 from _call_anna_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding
    "I guess that you never really know someone as well as you think you do, even when you're actually marrying them."
    "But I was sure that I'd gotten the measure of Anna in the time that we'd known each other as friends and bandmates."
    "Even more so in the time that we've actually been dating and getting steadily more serious about each other."
    "I mean, getting to know Anna and all of her little quirks was what made me want to marry her in the first place!"
    "And based on the fact that she's not the most normal of girls, I'd assumed that she'd want the big day to be wild and crazy."
    "I don't know what I had envisioned exactly, maybe tying the knot while bungee-jumping or something like that."
    "Which is why it took me by surprise when Anna started talking about churches and white dresses."
    "You know, all of the stuff that you'd associate with a traditional wedding ceremony!"
    "At first I wasn't sure if she was being honest with me, if she was just saying what she thought I wanted to hear."
    "But pretty soon I was convinced that this was actually what Anna wanted for the day we said 'I do'."
    "And so I simply shrugged my shoulders and got on with it."
    "Obviously, I didn't actually shrug my shoulders in front of her - I'm not that stupid."
    "I just went along with the notion of keeping things simple and traditional, because that's what she wanted."
    "But while I agreed to all of it, I was never totally convinced that it was the right thing for us."
    "And I felt that way right up until a second ago."
    "The moment I hear the music Anna chose to come down the aisle to."
    "Instantly I stop fiddling with the awkward tie that I've had to wear for the occasion."
    "And I'm glancing eagerly back over my shoulder."
    "At first, I can't actually see her as she makes her way into the church."
    "Anna's just so short that, as the assembled guests stand, she's lost from view."
    "But then she turns to walk down the aisle, and I catch my first glimpse of her."
    show anna a wedding at center, zoomAt( 0.9, (640, 740)) with dissolve
    "In that moment, I feel all of my doubts disappear."
    "My anxieties fall away into nothingness."
    "This is right, I just know it."
    "And it's all because of her."
    "Because of Anna."
    "Look, I know this should be all soft and fluffy."
    show anna b
    "But fuck me, she looks so good in that floaty, white dress!"
    "Whoever made it tried their best to hold it all in."
    show anna happy
    "Yet every curve of Anna's hot little body moves beneath it, like poetry in motion."
    show anna normal
    "And then there's the look on her face, the smile and the way that her eyes are shining right now."
    "That's almost as much of a turn on as the sight of her chest, bobbing along in the corset of her dress."
    if not anna.is_visibly_pregnant:
        "By sheer force of habit, I find myself mentally undressing her."
        "But I can only imagine what the underwear she's chosen might look like!"
    else:
        "I can also see that the seamstress made an effort to hide Anna's swollen belly."
        "But if anything, the sight of it makes me happier than ever."
        "There's no shame for either of us in the fact that we're expecting a child."
        "Only the proof of our love and the promise of our future together."
    show anna wedding blush at traveling (1.75, 3.0, (650, 1150))
    "Clutching a bouquet in her hands as she comes to stand beside me, Anna looks fit to burst."
    "When the priest calls for everyone to be seated, it's all that I can do to tear my eyes away from her."
    "Priest" "Dearly beloved, we are gathered here today to witness the union of these two souls."
    "Priest" "Their joining together in the sacred bonds of holy matrimony..."
    "The rest of the ceremony passes as a blur for me."
    "Words that I should recall and pay attention to, but don't reach my ears."
    show wedding anna with fade
    "All I can do is stare at Anna, and I see that she's in the same predicament too."
    "In the end, it's only when the priest coughs loudly that we both jump and snap back to reality."
    "Priest" "Ahem..."
    show wedding anna priest with dissolve
    "Priest" "Pardon me, must have had a frog in my throat."
    "Priest" "I believe I was saying - do you, Anna, take this man to be your lawful, wedded husband?"
    anna.say "Sure thing - you bet I do!"
    "The priest raises his eyebrows at this, a faint smile curling the edges of his lips."
    "Who knows, maybe he's not quite as straight-laced as he seems?"
    "Priest" "A simple 'yes' would have sufficed, my dear."
    "Anna looks bashful at his gentle reproach, looking down at her feet for a moment."
    "But then she looks back up at me, blushing in the cutest way possible."
    "Priest" "And you, [hero.name]."
    "Priest" "Do you take this woman to be your lawful, wedded wife?"
    mike.say "Yeah, what she said!"
    "The priest looks stunned for a moment, but then shakes his head."
    "Priest" "Then I see no reason not to pronounce you husband and wife."
    "Priest" "You may kiss the bride."
    "Priest" "Preferably before she says something else just as colourful..."
    show wedding anna -priest with dissolve
    "I turn to face Anna, bending down to do as the priest told us."
    "But before I can get even halfway down to her height, Anna all but leaps up at me."
    "Tossing her bouquet over one shoulder and into the congregation, and hops straight into my arms."
    "I hardly hear the sound of our guests scrabbling to catch the flowers as she wraps her legs around me."
    "And I can honestly say that I don't care who ends up with it, or if they break bones along the way."
    scene wedding_bg_04 at center, zoomAt(1.2, (640, 800)), blur(5)
    show anna kiss wedding
    with hpunch
    $ anna.flags.kiss += 1
    "She plants her lips on mine, and the kiss that follows is hardly suitable for the interior of a church!"
    "When it ends, Anna doesn't even ask to be put down, simply clinging to me the whole time."
    "She looks deep into my eyes, ignoring the scene of chaos playing out behind us."
    hide anna
    show anna wedding happy at center, zoomAt (1.75, (650, 1150))
    with fade
    anna.say "[hero.name], we did it - we got married!"
    "She may be stating the obvious - but what the hell do I care?"
    mike.say "We did, Anna..."
    mike.say "We sure did!"
    scene bg street
    show anna at center, zoomAt (1.75, (650, 1150))
    with fade
    anna.say "Ooh, [hero.name], should I start talking now?"
    anna.say "Or is someone gonna tell me when?"
    anna.say "Huh...what?"
    anna.say "People can hear me right now?"
    show anna surprised at vshake
    anna.say "Whaaa...I've been blabbing this whole time!"
    anna.say "And you didn't even tell me?!?"
    anna.say "Whadda ya mean you're telling me now?!?"
    show anna annoyed
    anna.say "Now's too late!"
    anna.say "They're gonna think I'm some dumb, ditzy air-head!"
    anna.say "Ah well, maybe I can talk them back round with my winning personality?"
    show anna angry
    show fx exclamation
    anna.say "WHAT?!?"
    anna.say "[hero.name], that's such a MEAN thing to say!"
    show anna normal
    anna.say "Okay...okay..."
    anna.say "Where was I..."
    anna.say "Oh yeah, it's me - Anna!"
    anna.say "And this is the bit where I get to tell the story, and not [hero.name]."
    show anna annoyed
    anna.say "Who's being a real jerk to me right now, by the way!"
    show anna evil
    anna.say "So I should be mean to him too!"
    show anna normal
    anna.say "But...aww, who am I kidding."
    anna.say "Just look at that face!"
    anna.say "I can't stay mad at him for too long."
    if anna.flags.mikeBabies >= 1 or anna.is_visibly_pregnant:
        anna.say "Not when it comes to my precious little Tommy's daddy!"
    else:
        anna.say "Not when it comes to my fantastic husband!"
    anna.say "Ah, it's so weird to think what might have happened if we hadn't met, you know?"
    anna.say "Like if our paths had never crossed at all."
    anna.say "If Sasha hadn't brought him along to band practice that one time."
    anna.say "If I hadn't said yes when the big lug asked me out the first time too!"
    anna.say "And if I didn't let him do those things that he does to me in bed..."
    show anna blush
    anna.say "Mmm..."
    anna.say "Just the thought of it's making me go all funny..."
    anna.say "I can picture it right now!"
    anna.say "I can almost feel him..."
    anna.say "Doing that thing the he does with his..."
    anna.say "To my..."
    anna.say "Oops..."
    show anna wink
    anna.say "Sorry about that - got a little distracted for a moment there!"
    anna.say "But you guys don't want to know about that, do you?"
    anna.say "Who cares about what I'm imagining [hero.name] doing to me right now."
    anna.say "You all want to hear about how we lived happily ever after, yeah?"
    show anna happy
    anna.say "I thought so!"
    show anna normal
    anna.say "So, anyway..."
    anna.say "We went on tour with the rest of the band pretty soon after we tied the knot."
    anna.say "Our first time headlining, so it was a really big deal!"
    anna.say "We played all these clubs in all of these different cities."
    anna.say "And that was all kind of a blur, you know?"
    scene anna ending
    anna.say "So we only just got back off of it, and we realised we were married!"
    anna.say "Well...not that we forgot or anything, you know?"
    anna.say "We just had a lot on our minds at the time."
    anna.say "And that we needed to think about what we were going to do next."
    anna.say "Right now [hero.name]'s still spending half of his time at my place and half at Sasha's."
    anna.say "But that's going to change as soon as we find a place of our own that's big enough."
    anna.say "And having [hero.name] around the whole time is great too."
    anna.say "It means I have him all to myself, and I don't have to share him with anyone!"
    anna.say "I'm still not sure if guys are always better than girls in that department."
    anna.say "But I do know that [hero.name]'s the best of all!"
    anna.say "It's not all about the sex though, oh no!"
    anna.say "We're so good together too, laughing at each other's jokes, even finishing the other's sentences."
    anna.say "Sometimes I think it's like we both have half of the same brain!"
    anna.say "Huh..."
    anna.say "What's up, [hero.name]?"
    anna.say "Why are you laughing at me?"
    anna.say "Yeah, well...just ignore him, okay?"
    anna.say "Oh, dammit - how long have I got left?"
    anna.say "Eek...that's only a couple more seconds!"
    anna.say "I just wanna say that we're madly in love, and he's the best."
    anna.say "Even though I already said that."
    anna.say "But he is, so I can say it as many times as I like."
    anna.say "So there!"

    if not game.flags.cheat:
        if renpy.has_label("sexperience_achievement_2") and not anna.sexperience:
            call sexperience_achievement_2 from _call_sexperience_achievement_2_2
            if renpy.has_label("sexperience_achievement_3") and sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False)]) <= 0:
                call sexperience_achievement_3 from _call_sexperience_achievement_3_2
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label anna_sub_event_01:
    show anna a normal
    "It's been one of those average trips to the mall with Anna today."
    "Nothing to complain about, but nothing that sticks in the memory either."
    "We wander from one end of the mall to the other a couple of times."
    "And we fill the time with window shopping for the most part."
    "We just hit a couple of shops for random stuff that we need along the way."
    "After a while I'm thinking of suggesting that we head home."
    "But I can see that Anna's starting to get a little tetchy."
    show anna annoyed
    "She's curling her lip and frowning as we walk along."
    mike.say "Anna..."
    mike.say "What's the matter?"
    mike.say "Did I say something to piss you off?"
    "I'm not prepared for what happens next."
    show anna b at hshake
    "Anna stops dead and spins on her heel."
    "Hands planted on her hips, she glares at me."
    anna.say "What's that supposed to mean?"
    show anna angry
    anna.say "Can't I have a change of mood?"
    anna.say "Not everything I do is because of you, [hero.name]!"
    show anna annoyed
    "I instinctively back off, giving Anna some space."
    "But rather than advancing on me, she clutches her stomach."
    "And I swear that I can hear it rumble from six feet away!"
    show anna surprised
    anna.say "Ooh..."
    show anna normal
    anna.say "I'm sorry, [hero.name]."
    anna.say "I think I'm a little hungry!"
    anna.say "I skipped lunch today and now it's catching up with me!"
    "I nod, suddenly understanding what the problem is."
    "And I start glancing around for the nearest place we can get something to eat."
    "A moment later I spot a possibility."
    mike.say "How about we grab something over there, Anna?"
    mike.say "I hear good things about that patisserie."
    "Anna's gaze follows the direction in which I'm pointing."
    "And as soon as she spots the place, she nods eagerly."
    show anna happy
    anna.say "Mmm..."
    anna.say "That sounds really good!"
    anna.say "I LOVE donuts!"
    show anna a with hpunch
    "She grabs hold of my hand and then sets off at a pace."
    "I find myself dragged after her, unable to resist."
    scene bg bakery
    show anna a normal
    "We join the queue at the patisserie, and wait in line."
    "And before too long we're getting served."
    "Anna seems to get ever more ravenous with each moment that passes."
    "Perhaps that's why she ends up ordering an entire box of ring donuts."
    "I'm feeling less hungry, so I just make do with a single chocolate eclair."
    show anna b at center, zoomAt(1.5, (640, 1040))
    "We wander over to a table and sit down to eat our purchases."
    "And I watch in amazement as Anna tears into the box of donuts."
    "She's eaten two or three before I've taken a single bite."
    "But then she catches me watching her intently as she licks at the next donut."
    "Anna's tongue was trying to strip it of sugar, but now she's stopped dead."
    anna.say "[hero.name]!"
    show anna annoyed
    anna.say "What are you staring at?!?"
    mike.say "Oh, come on, Anna!"
    mike.say "You're literally licking a ring in front of me!"
    anna.say "Ah!"
    show anna evil
    anna.say "You have such a filthy mind!"
    "I watch as Anna's eyes settle on my uneaten eclair."
    anna.say "I bet I can guess why you bought that!"
    anna.say "The longest pastry they had?"
    anna.say "One filled with cream too!"
    mike.say "Are you saying that my choice of pastry is somehow phallic?"
    "Anna doesn't answer my question."
    show anna blush
    "She just smiles as she leans forwards."
    "Then she pushes her donut onto the end of my eclair."
    show anna happy
    "Anna giggles uncontrollably as she works it up and down."
    "And I have to say that she's making a pretty good job of it."
    show anna blush
    "If these weren't items of pastry, I'd be rather aroused!"
    "In fact, I'm watching her so intently that I don't see her other hand move."
    "Quick as a flash, she squeezes my hand with it, the same hand that's holding the eclair."
    "The pressure makes the cream spurt out of the other end, the one pointing towards Anna."
    "She sticks her tongue out and catches it in her mouth."
    "Then she licks her lips and swallows it in one go."
    anna.say "Why are you looking at me like that, [hero.name]?"
    show anna wink
    anna.say "I was just hungry, that's all!"
    "Anna flutters her eyelids at me, trying to look innocent."
    mike.say "Yeah, well..."
    mike.say "I think you just gave me an appetite for something else entirely!"
    if anna.sub.max < 80:
        $ anna.sub.max = 80
    $ game.active_date.score += 10
    $ hero.replace_activity()
    return

label anna_sub_event_02:
    show anna normal
    "Anna and I genuinely tried to come up with something to do for our date tonight."
    "I know that I racked my brain to think of an idea and she suggested some stuff too."
    "But neither of us could agree on anything the other came up with."
    "And so we've fallen back on the last resort of sitting down and watching a film at my place."
    "Yeah, I know - it's not like that's the worst thing in the world to have to endure."
    "But there's a whole world full of things to do out there!"
    "And I can sit on my ass watching the TV when I'm not on a date too."
    "I kind of get the feeling that Anna feels the same way too."
    "She doesn't come out and say as much, probably to save my feelings."
    "But she's pretty quiet and not her usual outgoing self tonight."
    "All the same she nestles down beside me on the sofa."
    "And feeling her so close to me does begin to make me feel a little better."
    anna.say "So..."
    anna.say "What are we watching tonight?"
    "She chuckles and playfully elbows me in the ribs."
    show anna wink
    anna.say "Knowing you, it'll be some cult sci-fi film!"
    anna.say "Or a horror flick that somebody made for like no money at all, right?"
    mike.say "Actually it's a film that Sasha recommended we should watch."
    show anna normal
    mike.say "It's called 'Sixty-Nine Shades of Grey' or something."
    mike.say "Must be an artsy kind of thing, like that one 'Three Colours Red', I guess!"
    anna.say "Ooh..."
    anna.say "That sounds pretty high-brow!"
    anna.say "Promise me you'll explain what's happening if it goes over my head?"
    mike.say "I promise, Anna."
    mike.say "I'll pay extra attention just for you."
    "We both sit back and relax as the opening credits roll."
    "And to begin with it seems like pretty familiar stuff."
    "There's a cute young girl that's out to prove herself."
    "Then there's a rich guy that comes off as arrogant and aloof."
    mike.say "I bet you they hate each other at first."
    mike.say "Then they'll get all angry and passionate."
    mike.say "Which will make them realise they can't resist each other."
    mike.say "You just wait and see, Anna!"
    anna.say "[hero.name]!"
    show anna annoyed
    anna.say "Will you just shut up and watch the film already?"
    "Chastened by Anna's words, I do as I'm told."
    show anna normal
    "But as the film plays out, I see my predictions coming true."
    "I'm all set to point at the screen and claim that I was right."
    "And that's when things take an unexpected turn."
    show anna surprised
    anna.say "Oh..."
    show anna blush
    anna.say "Oh my..."
    anna.say "Is that even possible in real life?!?"
    mike.say "I have no idea, Anna!"
    mike.say "It can't be without a harness, vaseline and being born double-jointed!"
    "What we both thought was going to be an arty film turns into a parade of debauchery."
    "Right before our eyes, things play out that I thought were the stuff of porn films."
    "Not that I'm saying it shocks me, you understand?"
    "I'm one hundred percent okay with the ropes, rubber and whips they employ."
    "It's just that I wasn't prepared to see it tonight."
    show anna dazed
    "Anna seems to be spell-bound too, pressing herself into me the whole time."
    "I can hear her gasping and sighing as things play out on the TV screen."
    "At one point I swear that I can even feel her heart pounding in her chest!"
    "Finally the end credits roll and the film ends."
    show anna normal
    "We sit there in silence for a while, neither of us speaking."
    "It's like that strange, unreal feeling when you walk out of the cinema."
    "But in this case it's also charged with sexual tension too."
    show anna evil
    anna.say "[hero.name]..."
    mike.say "Yeah, Anna?"
    anna.say "I'm feeling a little funny."
    anna.say "Are you feeling a little funny too?"
    mike.say "Yeah, Anna."
    anna.say "I think the film affected me."
    mike.say "Me too, Anna, me too."
    anna.say "All I know is that I want to try that."
    show anna blush
    anna.say "I want to try some of the stuff they were doing."
    anna.say "Do you think, maybe, we could do some of that too?"
    menu:
        "We can try":
            "I nod my head, agreeing without a moment of hesitation."
            mike.say "Anna, I don't think some of that stuff is actually possible."
            mike.say "Some of it I think you need a license to practice in this country."
            mike.say "And a little of it I think is still punishable by death in some parts of the world!"
            mike.say "But I'm willing to try it, or die in the attempt!"
            "Anna claps her hands together and then hugs me tightly."
            anna.say "Ooh..."
            show anna happy
            anna.say "This is going to be so much fun!"
            anna.say "We can swing by the hardware store and get all the stuff we're going to need..."
            "I swallow at the mere mention of shopping for sensual pleasure in such a place."
            "But I nod along all the same, already thinking about the possibilities."
            "I guess that I should thank Sasha for recommending the film."
            "And also for not bothering to tell me what the hell it was about too!"
            $ game.active_date.score += 5
            if anna.sub.max < 100:
                $ anna.sub.max = 100
        "I'm not sure":
            "I shake my head firmly, dismissing the idea."
            mike.say "Anna, I don't think some of that stuff is actually possible."
            mike.say "Some of it I think you need a license to practice in this country."
            mike.say "And a little of it I think is still punishable by death in some parts of the world!"
            show anna annoyed
            "Anna makes a disappointed sound and turns away from me."
            anna.say "Huh..."
            anna.say "I never thought you were such a prude!"
            "I shake my head in sheer disbelief at the accusation."
            mike.say "Anna, what are you talking about?"
            mike.say "That film made what rockstars did back in the day look like kindergarten!"
            mike.say "By those standards, ninety-nine percent of the world's population are prudes!"
            "Anna keeps on sulking, regardless of what I have to say."
            anna.say "I'm just trying to keep things fresh, [hero.name]!"
            anna.say "Don't complain to me if you get bored in bed anytime soon!"
            $ game.active_date.score += 2
    $ hero.replace_activity()
    return

label anna_birthday_date_male:
    $ DONE["anna_birthday_date_male"] = game.days_played
    $ game.active_date.clothes = "sport"
    scene bg forest with fade
    "Ah...it sure feels good to get away from the hustle and bustle of the city."
    "To swap all that noise and pollution for the clean air and the sounds of nature."
    "Why, all I've heard since we got to the forest is the sound of birds in the trees."
    "The sound of crystal clear water cascading down over the rocks."
    "And the sound of..."
    play sound hitting_bushes
    anna.say "OUCH!"
    anna.say "Ow, ow, ow!"
    anna.say "[hero.name], help me!"
    anna.say "I got hurt real bad!"
    "Suddenly the spell of being lost in nature is shattered."
    "And I find myself glancing back over my shoulder, looking for Anna."
    "At first I can't see her at all, but then I rush back down the track."
    show anna a sport embarrassed at center, zoomAt (1.2, (1040, 900))
    "And I soon find her around the last corner, sitting on a tree-stump."
    "Not good, as we're supposed to be out here camping."
    "Worse still, we're supposed to be doing it to celebrate Anna's birthday!"
    mike.say "Anna..."
    mike.say "Are you okay?"
    show anna a cry at startle
    "At the sound of my voice, Anna looks up."
    "And I can see that she's got a serious pout on right now."
    anna.say "[hero.name]!"
    anna.say "Where did you go?!?"
    anna.say "I thought you'd abandoned me!"
    "I shake my head as I walk over and kneel down by Anna."
    show anna b at center, zoomAt (1.65, (640, 1100)) with dissolve
    if anna.sub >= 50:
        show anna pat
    mike.say "Don't be silly, Anna."
    mike.say "I was just a little way down the trail, that's all."
    mike.say "Now what's wrong?"
    show anna b at center, zoomAt(1.5, (640, 1040)) with hpunch
    "At this, Anna shoves her foot into my lap."
    "And she points at it, her eyes wide as she does so."
    anna.say "My foot, [hero.name]!"
    anna.say "I think I broke it!"
    anna.say "I fell over, and it was all I could do to hobble over here!"
    mike.say "Well then, let's have a look at it..."
    show anna b embarrassed at startle
    "Anna yelps and flinches as I take off her boot."
    "And she keeps it up as I examine her foot too."
    "I can see that there's nothing broken."
    "Most likely Anna just twisted her ankle a little."
    "But how am I going to explain that to her?"
    menu:
        "Tell her that she'll be okay":
            "I gently put Anna's sock back on and begin to slip her foot back into her boot."
            "And that earns me a cry of surprise, but not pain, from Anna."
            show anna b cry
            anna.say "[hero.name], what are you doing?"
            anna.say "Shouldn't you be calling an ambulance?"
            anna.say "Or maybe even a helicopter?"
            "I look up at Anna and smile, shaking my head."
            mike.say "No need for that, Anna."
            mike.say "You haven't actually broken any bones."
            mike.say "Your ankle's just a little sore."
            mike.say "Putting your boot back on will stop it swelling up."
            mike.say "Walking it off will help too."
            show anna b normal
            "Anna looks less than pleased with this diagnosis."
            "So I make a point of helping her up and taking her backpack too."
            mike.say "It's not too far to the spot where we're camping now."
            mike.say "And I'll carry this for you too, okay?"
            $ game.active_date.score += 15
            show anna happy
            "Anna nods, beginning to look a little happier."
            "And she takes my arm as we start to walk again."
        "Quickly put her to her feet":
            "I immediately start shoving Anna's foot back into her boot."
            "A course of action that earns me more cries and protests from her."
            show anna b angry
            anna.say "Ouch!"
            anna.say "[hero.name], what are you doing?"
            anna.say "Shouldn't you be calling an ambulance?"
            anna.say "Or maybe even a helicopter?"
            mike.say "Don't be so dramatic, Anna."
            mike.say "You haven't actually broken any bones."
            mike.say "Your ankle's just a little sore."
            mike.say "Putting your boot back on will stop it swelling up."
            mike.say "Walking it off will help too."
            $ game.active_date.score -= 10
            show anna b unpleased
            "Anna looks less than pleased with this diagnosis."
            "But she seems to realise that there's no use arguing."
            "So she gets up and shoulders her backpack."
            "Though I see she makes a point of limping as we start to walk again."
        "Massage her swollen foot":
            "I take Anna's bare foot in my hands and start to massage the swollen parts."
            "And that earns me a cry of surprise, but not pain, from Anna."
            anna.say "[hero.name], what are you doing?"
            anna.say "Shouldn't you be calling an ambulance?"
            anna.say "Or maybe even a helicopter?"
            show anna b cry
            "I look up at Anna and smile, shaking my head."
            mike.say "No need for that, Anna."
            mike.say "You haven't actually broken any bones."
            mike.say "Your ankle's just a little sore."
            mike.say "This massage will help to keep it from swelling up."
            show anna b dazed
            $ anna.sub += 2
            "Anna nods and watches on as I massage her foot."
            "And before too long, she looks like she's quite enjoying it!"
            anna.say "Ooh..."
            show anna b normal
            anna.say "That does feel a bit better!"
            "I gently put Anna's sock back on and begin to slip her foot back into her boot."
            mike.say "Putting your boot back on will stop it swelling up."
            mike.say "Walking it off will help too."
            show anna b annoyed
            "Anna looks less than pleased with this diagnosis."
            "So I make a point of helping her up and taking her backpack too."
            mike.say "It's not too far to the spot where we're camping now."
            mike.say "And I'll carry this for you too, okay?"
            show anna b normal
            $ game.active_date.score += 15
            "Anna nods, beginning to look a little happier."
            "And she takes my arm as we start to walk again."
    hide anna
    show anna sport
    with fade
    "It doesn't take us long to get to the spot I picked out for us to spend the night."
    "And as soon as we get there, I take off my backpack, wanting to get down to pitching camp."
    show anna annoyed
    show fx question
    "But when I look up from what I'm doing, I see Anna giving me a questioning look."
    mike.say "Ah..."
    mike.say "What's the matter, Anna?"
    anna.say "Why are we stopping here, [hero.name]?"
    anna.say "This doesn't look like a campsite."
    hide fx
    anna.say "It's just somewhere in the middle of the woods!"
    mike.say "Well this is it, Anna."
    mike.say "Think you could help me put up the tent?"
    "Anna shakes her head."
    show anna normal
    anna.say "Nuh-uh!"
    anna.say "I went camping all the time with my folks as a kid."
    anna.say "So I think I know what a campsite looks like!"
    anna.say "There's no way my dad could have gotten his RV up here."
    "I think I'm starting to see the source of the confusion."
    mike.say "No, Anna..."
    mike.say "We're wild camping - staying in the forest."
    show anna surprised
    anna.say "But, but, but..."
    anna.say "Where are the nearest bathrooms!"
    menu:
        "Change subject":
            mike.say "Trust me, Anna."
            mike.say "This is much better."
            show anna angry
            "Anna shakes her head the instant I say this."
            anna.say "How could going to the bathroom in the woods be better?!?"
            mike.say "We're away from other people out here, Anna."
            mike.say "Nobody else making noise."
            mike.say "Or telling us not to make noise either."
            mike.say "We can do what we like!"
            show anna annoyed
            "Anna thinks about this for a moment."
            "And she seems to come round a little."
            anna.say "What kind of things are you talking about?"
            "I offer Anna a sly wink."
            mike.say "Just you wait and see, Anna!"
            show anna blush
            $ game.active_date.score += 15
            "This seems to take Anna's mind off the less comfortable aspects of the night ahead."
            "And she sets to helping me pitch camp."
        "Tell her how it's gonna be":
            mike.say "Well, I'm planning on digging a hole."
            "I point to the nearby tree-line."
            mike.say "About a hundred yards over that way."
            mike.say "And I'll be using that while we're here."
            mike.say "You're welcome to use my hole too."
            mike.say "Or you can dig one of your own."
            "I hold out the folding shovel I've brought along to make my point."
            show anna angry
            "But Anna doesn't seem pleased at the prospect."
            $ game.active_date.score -= 10
            show fx anger
            anna.say "You mean we have to do our business into a hole in the ground?"
            anna.say "Like animals?!?"
            hide fx
            show anna embarrassed
            anna.say "Oh no - this is like one of those movies where society's broken down."
            anna.say "And nothing works anymore - or maybe even worse than that!"
    "I soon have the components that make up the tent spread out on the ground."
    show anna unpleased
    "But I also have Anna standing next to me, looking at them in sheer bafflement."
    mike.say "What's wrong, Anna?"
    mike.say "You never seen a tent before?"
    "Anna frowns at me."
    show anna angry
    anna.say "Sure I have."
    anna.say "I've just never seen one in so many pieces before!"
    show anna annoyed
    anna.say "Are you sure it's all there?"
    "I shrug my shoulders and bend down to pick up some of the pieces."
    mike.say "Only one way to find out..."
    show anna normal
    "With that, we set about pitching the tent."
    "Pretty soon we're making real progress."
    "The frame is up and we're ready to put the waterproof fabric over it."
    mike.say "Anna..."
    mike.say "Throw it over the top."
    mike.say "I'll go inside and stretch it over the top."
    scene bg forest at blur(8) with dissolve
    "Anna nods and I hurry inside the frame."
    "Everything seems to be going to plan."
    "But then I hear the frame collapsing."
    play sound body_fall
    scene bg forest at blur(16), dark with vpunch
    "And everything comes down on top of me."
    "Trapped under the whole of the tent, I struggle to get free."
    "And the situation isn't helped by the fact I can hear Anna laughing."
    scene bg forest
    show anna sport happy
    with dissolve
    "As soon as my head pops out, she points at me and laughs again."
    anna.say "See, I know how to put a tent up."
    anna.say "And pull one down too!"
    "So all of this was Anna's doing!"
    menu:
        "Apologize for earlier":
            mike.say "Okay, Anna, okay..."
            mike.say "Sorry for being such a jerk."
            "Anna smiles and nods, accepting my apology."
            "Then she hurries over to help me out from under the tent."
            show anna normal
            "Once we set about the task a second time, things go much better."
            "With the two of us working together, we have the tent up in no time."
            "To finish it off, we unroll our sleeping bags."
            "And then we throw out backpacks in there too."
        "Chastise her":
            mike.say "Anna!"
            mike.say "You're not helping!"
            "Anna doesn't seem in the least bit concerned as I try to chastise her."
            show anna at startle
            "In fact she keeps right on laughing as I crawl out from under the collapsed tent."
            "Once I've freed myself, I feel the need to stamp off and regain some composure."
            "But when I come back, I'm surprised to see that Anna's got the tent up on her own."
            show anna normal
            anna.say "Don't worry, [hero.name]."
            show anna evil
            anna.say "I've got this!"
            "And just like that, she's humiliated me for a second time!"
    $ game.active_date.score += 15
    show anna happy
    "Anna pops her head out of the tent, smiling at me sweetly."
    "Which is a relief, as it shows she's actually starting to enjoy herself."
    show anna normal
    anna.say "Okay, [hero.name]..."
    anna.say "What are we going to do now?"
    "I look up from the fire I've been building."
    "And I have to admit, that's a pretty good question."
    menu:
        "Play guitar":
            "I choose this as the perfect moment to whip out my guitar."
            "And I give it a casual strum as Anna walks over and sits by the fire."
            mike.say "I thought we might have a sing-along, Anna."
            mike.say "You know, kind of like you always hear about?"
            "Anna nods eagerly, leaning closer to me as I start to play."
            show anna happy
            anna.say "Oh yeah!"
            anna.say "I remember my mom and dad singing by the campfire when I was a kid!"
            if hero.has_skill("guitar"):
                "It seems like playing in the bosom of nature agrees with me."
                "Because from the first time I strum the guitar, everything goes great."
                "The instrument is perfectly in tune."
                "My fingers dance over the strings with poise and grace."
                "And the smoke from the fire even seems to add some timbre to my voice."
                "It doesn't seem to matter what I play either."
                "As Anna joins in, singing along the whole time."
                show anna close normal
                "Afterwards she leans her head against my shoulder."
                anna.say "Aww..."
                anna.say "That was really great, [hero.name]!"
                show anna happy
                $ game.active_date.score += 15
                anna.say "It totally reminded me of camping as a kid."
            else:
                "I don't know what the problem is."
                "But things start to go wrong almost from the start."
                show anna embarrassed
                "My guitar sounds like it's out of tune, even though I know it can't be."
                "And I'm all fingers and thumbs, probably from chopping up the firewood."
                "Worst of all, my voice is hoarse and cracked when I try to sing."
                "But when I try to take a deep breath and clear it, I inhale smoke from the fire."
                mike.say "Urgh..."
                mike.say "Aargh!"
                $ game.active_date.score -= 10
                show anna angry
                "Anna puts her hands over her ears and shakes her head."
                anna.say "Oh no!"
                anna.say "Please stop it, [hero.name]!"
                anna.say "You're making my ears hurt!"
                "Ah well, so much for that idea."
        "Cook something":
            mike.say "Aren't you starting to feel a little hungry, Anna?"
            mike.say "After all, we walked for a while to get here."
            mike.say "And putting up the tent took some serious effort too."
            show anna surprised
            "Anna seems surprised by the question at first, like it never crossed her mind."
            "But then she puts a hand on her stomach, and I can almost hear it growling!"
            show fx exclamation
            anna.say "Oh wow!"
            anna.say "Now that you mention it - I do feel hungry!"
            hide fx
            mike.say "Good thing I started a fire then, isn't it?"
            "I hold up a pot and then show Anna frame I've set up to hang it over the fire."
            show anna normal
            mike.say "Don't worry."
            mike.say "Dinner will be ready soon!"
            if hero.has_skill("cooking"):
                "Anna watches eagerly as I tend the pot."
                show anna happy
                "And she positively beams as I spoon out a portion for us both."
                mike.say "There you go, Anna."
                mike.say "Tuck in!"
                "Anna inhales deeply over her steaming bowl."
                "And then her eyes light up with sheer delight."
                anna.say "Mmm!"
                anna.say "This smells amazing!"
                mike.say "Never mind how it smells, Anna."
                mike.say "How does it taste?"
                "Anna nods as she eagerly spoons some of the food into her mouth."
                show anna surprised
                pause 1.5
                show anna happy
                $ game.active_date.score += 15
                "Then she starts to shovel spoon after spoon in there."
                mike.say "Erm..."
                mike.say "Anna?"
                mike.say "Are you okay?"
                "I reach out towards Anna, but then I leap backwards."
                show anna angry
                "Because she looks up from her bowl, and I swear she actually growls at me!"
                anna.say "Back off, buddy!"
                anna.say "This is my bowl!"
                show anna surprised
                "Almost as soon as she says this, Anna snaps out of it."
                show anna embarrassed
                "She looks embarrassed and shakes her head."
                anna.say "Oops...sorry, [hero.name]!"
                show anna normal
                anna.say "I don't know what came over me."
                anna.say "I guess I was hungrier than I thought!"
                mike.say "Ah...it's okay, Anna."
                mike.say "At least I know it tastes good..."
            else:
                "Anna watches eagerly as I tend the pot."
                show anna happy
                "And she positively beams as I spoon out a portion for us both."
                mike.say "There you go, Anna."
                mike.say "Tuck in!"
                "Anna inhales deeply over her steaming bowl."
                show anna angry
                "But then she makes a face and frowns."
                anna.say "Eww!"
                show anna annoyed
                anna.say "Is it supposed to smell like that?"
                anna.say "Like boiled sweat-socks and crap?"
                "Now it's my turn to frown back at Anna."
                mike.say "Hey!"
                mike.say "Don't insult my cooking!"
                mike.say "It's fine, and I'll prove it..."
                "I spoon some of the food into my mouth."
                "And I spit it out a moment later."
                mike.say "Urgh!"
                mike.say "It really tastes of sweat-socks and crap too!"
                "I watch as Anna pours hers onto the ground and shakes her head."
                $ game.active_date.score -= 10
                anna.say "Don't worry, [hero.name]..."
                anna.say "I have some snacks and potato-chips in my bag."
        "Look for wild animals":
            play sound hitting_bushes
            "There's a rustling sound over by the treeline."
            "And when Anna and I look up, we see some small animals hopping around."
            "It's hard to make out what they are at first."
            "But then Anna seems to get a better view of them than me."
            show anna happy
            anna.say "Aww!"
            anna.say "Look, [hero.name] - it's a family of badgers."
            anna.say "Aren't they cute?"
            "I half-grimace as I get a better look at the animals."
            "To me they look pretty big and potentially dangerous."
            mike.say "I don't know about that, Anna..."
            mike.say "We don't want them getting into our supplies while we're asleep."
            "But it looks like Anna's not listening to a word I'm saying."
            "As she's already walking towards the badgers with some food in her hand."
            anna.say "Hey little guys!"
            anna.say "Are you hungry?"
            mike.say "Anna!"
            mike.say "No!"
            "I charge over, trying to put myself between Anna and the badgers."
            show anna surprised at startle
            "Of course this means that both she and the animals see me and freeze."
            if hero.has_skill("animalhated"):
                anna.say "[hero.name]..."
                anna.say "What's the matter?"
                mike.say "Be careful, Anna!"
                mike.say "Badgers can be vicious, yeah?"
                "Just as I'm saying this, I see the badgers make their move."
                "As one, they leap into the air, showing their sharp teeth."
                "And I watch in horror, convinced Anna's about to be attacked."
                "Which means it's quite a surprise when the whole lot of them land on me!"
                with hpunch
                play sound [badger, badger]
                "All of a sudden I have badgers climbing all over me."
                "Badgers hanging off of me by their teeth and claws."
                play sound badger
                "And badgers snarling an inch from my face."
                with hpunch
                mike.say "AAARGH!"
                mike.say "Get them off me!"
                mike.say "Get them off me!"
                "Anna does all that she can to help."
                "But in the end I have to physically tear the badgers off of myself."
                "And one by one, I hurl the little fuckers as far as I can."
                show anna normal
                "After wards, Anna does the best she can with the first-aid kit we brought."
                "But I'm still scratched and bitten to hell."
            else:
                anna.say "[hero.name]..."
                anna.say "What's the matter?"
                mike.say "Be careful, Anna!"
                mike.say "Badgers can be vicious, yeah?"
                "Just as I'm saying this, I see the badgers coming closer."
                "I wince and close my eyes, waiting to feel the first one bite me."
                "But instead I feel it licking my hand."
                "Opening my eyes, I see a scene like something out of a fairy-tale."
                "All of the badgers are gathered around us."
                "And Anna's feeding them like an enchanted princess!"
                show anna happy
                $ game.active_date.score += 15
                anna.say "One for you."
                anna.say "One for you."
                anna.say "And I can't forget you - because you're SO cute!"
                "All I can do is shake my head as the badgers take the food without incident."
                "Then they all scurry back into the woods and leave us alone by the fire."
                show anna normal
                anna.say "Aww!"
                anna.say "That was amazing!"
                anna.say "I wonder if you can keep those things as pets?"
    scene bg forest
    show anna sport
    with fade
    "As evening starts to fall, so does the temperature."
    "And it's now that we're really glad of the fire."
    show anna at center, zoomAt(1.5, (640, 1040))
    "It's an added bonus for me that Anna huddles close to me too."
    "I've brought a blanket for just this kind of occasion."
    "And I love the feeling of her arms wrapped around me beneath it."
    anna.say "[hero.name]..."
    mike.say "Yes, Anna?"
    anna.say "You remember you said you were taking me camping for my birthday?"
    mike.say "Yes, I do."
    anna.say "Well..."
    anna.say "Does that mean the trip is like...my birthday present?"
    if not hero.has_gifts:
        "Damn it - I knew there was something I was supposed to do!"
        "What with all the preparation for the trip, I forgot Anna's birthday present!"
        "Looks like I'm going to have to improvise."
        mike.say "Yeah, Anna..."
        mike.say "That's really perceptive of you."
        mike.say "I thought rather than buy you something..."
        mike.say "I'd get you memories that'd last forever!"
        "Anna seems to think about it for a moment."
        "And then she nods."
        $ game.active_date.score -= 20
        $ anna.love -= 10
        anna.say "Okay..."
        anna.say "That's what I thought too."
        show anna annoyed
        "I can tell from the tone of her voice that she's a little disappointed."
        "But at least she accepted my excuse."
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_2
        if _return != "done":
            if _return not in ["None", "exit"]:
                "I shake my head at this."
                mike.say "I do hope that the memories from today will be special, Anna."
                mike.say "But that's not the only thing I got you for your birthday."
                "I pull out the gift I brought along and hand it to Anna."
                mike.say "Happy birthday, Anna!"
                show anna happy
                anna.say "Aww..."
                anna.say "Thank you so much!"
                play sound [paper_ripping_2, paper_ripping_1]
                "Anna smiles as she tears off the wrapping paper."
                if _return:
                    "But when she sees what's inside, her jaw drops open."
                    show anna surprised
                    anna.say "Oh wow!"
                    anna.say "I always wanted one of these!"
                    anna.say "How did you know?"
                    "I shrug and smile, enjoying Anna's amazement."
                    mike.say "Well, you did keep dropping hints, Anna!"
                    mike.say "And now you have proof that I do listen to you."
                    $ game.active_date.score += 15
                    hide anna
                    show anna close happy
                    "Anna hugs me even tighter under the blanket."
                    anna.say "It's great, [hero.name]."
                    anna.say "And it's so much better because it came from you!"
                    hide anna close
                else:
                    "But when she sees what's inside, I notice her face falls."
                    show anna normal
                    anna.say "Oh..."
                    anna.say "Thanks, [hero.name]."
                    $ game.active_date.score -= 10
                    anna.say "That's...really thoughtful."
                    "I can tell that Anna's disappointed with my gift."
                    "But she also seems to be doing the best she can to hide it."
                    "So all I can do is smile and do the same."
                    "All the time cursing my inability to pick out a decent gift for her."
            else:
                "Damn it - I knew there was something I was supposed to do!"
                "What with all the preparation for the trip, I forgot Anna's birthday present!"
                "Looks like I'm going to have to improvise."
                mike.say "Yeah, Anna..."
                mike.say "That's really perceptive of you."
                mike.say "I thought rather than buy you something..."
                mike.say "I'd get you memories that'd last forever!"
                "Anna seems to think about it for a moment."
                "And then she nods."
                $ game.active_date.score -= 20
                $ anna.love -= 10
                anna.say "Okay..."
                anna.say "That's what I thought too."
                "I can tell from the tone of her voice that she's a little disappointed."
                "But at least she accepted my excuse."
    show anna surprised at startle
    anna.say "Ooh!"
    anna.say "I just remembered..."
    show anna normal
    anna.say "I brought marshmallows!"
    show anna sport at center, traveling (1.2, 0.5, (640, 800))
    "Anna slips out from under the blanket and begins to rummage in her bag."
    "A few moments later, she returns with a bag of marshmallows and two sticks."
    show anna happy at center, traveling (1.5, 0.3, (640, 1040))
    anna.say "Let's roast these bad boys!"
    show anna normal
    "Soon enough we have them on the end of the sticks."
    "And we're toasting them over the flames."
    "But then Anna seems to hold hers too close to the fire."
    "Because the marshmallow bursts into flames."
    "The sugary substance burning with an intense light."
    show anna surprised
    anna.say "Oh no!"
    anna.say "What do I do?!?"
    show anna cry
    anna.say "[hero.name], help me!"
    menu:
        "Help her out":
            show anna surprised with hpunch
            "Tossing my own stick into the fire, I grab Anna's from her."
            "And I throw that into the flames a moment later."
            "Then I turn my attention to Anna herself."
            mike.say "Are you okay, Anna?"
            mike.say "Did you get burned?"
            show anna blush
            "Anna shakes her head."
            "But she still clings to me all the same."
            $ game.active_date.score += 15
            anna.say "No, [hero.name] - I'm okay."
            anna.say "It was just scary, that's all."
            "I nod and return the embrace."
            "Doing all I can to calm Anna's nerves."
        "Laugh at the situation":
            "I can't help laughing at Anna as she wails for help."
            show anna at center, hshake
            "And her waving the stick around only makes things worse."
            "As it helps to fan the flames even more."
            mike.say "Ha ha!"
            mike.say "For fuck's sake, Anna!"
            show anna at startle
            "Eventually Anna drops the whole thing into the fire."
            "Where it burns up in a mere matter of seconds."
            "Then she shoots an annoyed glare in my direction."
            $ game.active_date.score -= 10
            show anna angry
            anna.say "That wasn't funny, [hero.name]!"
            anna.say "I was really scared!"
            mike.say "I don't know, Anna..."
            mike.say "It looked pretty funny to me!"
    "Once night has fallen for real, the sky slowly fills with stars."
    "Anna and I spend a little time gazing up at them."
    show anna embarrassed at center, traveling (1.55, 0.6, (640, 1060))
    "But then she lets out a pretty huge yawn."
    anna.say "Oooh..."
    show anna normal at center, traveling (1.5, 0.3, (640, 1040))
    anna.say "I'm bushed!"
    mike.say "Maybe we should turn in for the night?"
    mike.say "I know I could use some sleep too."
    "Anna nods and we crawl into the tent, and then into our sleeping-bags."
    if game.active_date.score >= 80 and anna.sexperience >= 1:
        "Almost as soon as she's zipped up, Anna snuggles herself against me."
        "Even thought we're both tired, the sensation begins to wake me up."
        "And I mean that in a physical sense, if you follow me..."
        "Oh yeah, Anna's definitely rubbing her ass against me."
        "And in the most obvious way imaginable too!"
        show anna blush
        anna.say "[hero.name]..."
        mike.say "Yeah, Anna?"
        anna.say "I might not be quite as tired as I thought."
        mike.say "Me too, Anna."
        anna.say "I think I have just a little bit of energy left..."
        "I don't know who starts to unzip their sleeping-bag first."
        "But a moment later, we're both wriggling towards each other..."
        call anna_birthday_sex from _call_anna_birthday_sex
    else:
        hide anna with dissolve
        "Almost as soon as she's zipped up, Anna turns her back to me."
        "And a few moments later I hear her start to snore."
        "That's a little disappointing, as I was hoping to fool around."
        "And if not, even just cuddle a little."
        "But I suppose we are both tired at the end of a long day."
        "So I just turn over and try to get some much needed rest too."
    return

label anna_birthday_sex:
    "Anna wastes no time in wriggling out of her sleeping-bag and into mine."
    show anna b underwear with dissolve
    "She's stripped down to her underwear, and her skin feels warm against me."
    "It's a tight squeeze in a sleeping-bag meant to accommodate one."
    "But Anna's a petite girl, and she snuggles herself into me, her back to my belly."
    anna.say "Mmm..."
    anna.say "I'm cold, [hero.name]."
    show anna a
    anna.say "You think you know a way to warm me up?"
    "Anna pushes her ass hard against my groin as she says this."
    "And I can already feel my cock getting hard with the anticipation."
    "As I wrap my arms around her, Anna takes hold of my wrists."
    "Then she guides one hand to her breasts."
    "The other she slides into her panties."
    "And far be it from me to argue when she knows what she wants!"
    "I begin to kiss Anna's neck at the same time as using my hands."
    "She sighs with satisfaction as I do so, letting me know she approves."
    "The hand on her breasts is inside of her bra by now."
    show anna a embarrassed grope
    "And I use it to cup one of her breasts, squeezing gently."
    "Anna nods, moaning as the tips of my fingers find her nipple."
    "It stiffens under my touch, just like my cock down below."
    "Meanwhile my other hand is gently teasing the edges of her pussy."
    "I can already feel the folds down there getting slick."
    "The tips of my fingers slipping and sliding over them."
    "Slowly they start to gravitate towards the centre."
    "The slippery folds guiding them without me having to do a thing."
    "They begin to push inside of Anna, making her moan."
    "But then I feel her reach down and grab my hand."
    anna.say "Ah..."
    show anna a blush
    anna.say "I...I don't want them..."
    show anna b -grope
    anna.say "I want this!"
    "Now it's my turn to moan and gasp as Anna's hand moves to my groin."
    "And she squeezes my cock pretty hard, as if to make her point clear."
    "I nod, eager to do whatever Anna wants."
    mike.say "Yeah..."
    mike.say "Of course..."
    "At once Anna starts yanking down my short, trying to free my cock."
    "And I begin doing the same to her panties to be sure we're ready."
    "It's awkward doing all of that inside a sleeping-bag."
    "But somehow we manage it, kicking them off with our feet once they're below our knees."
    "That done, Anna doesn't waste any more time."
    "She takes a firm hold of my manhood."
    hide anna
    show anna missionary nightforest lookup
    with fade
    "And then she presses it hard against the lips of her pussy."
    "But it's not like I need any serious encouragement either."
    "My hands back on her body, I push forwards with the same enthusiasm."
    "The fact that we're both on the same page, body and mind makes things flow together."
    "And I feel the sensation of Anna's lips opening to let me inside."
    "She wriggles her ass backwards at the same time."
    show anna missionary vaginal pleasure
    "Which means that I'm as deep as I can go within seconds."
    "After that, neither of us need to be told what to do next."
    "Everything happens naturally and builds in the same manner."
    "Somehow we manage to writhe and wriggle together in the one sleeping-bag."
    "And perhaps the cramped confines make things that much more intense."
    "But all I know right now is that I want Anna more than anything I can imagine."
    "I can hear the sound of my thighs slapping against hers."
    "That and the cries of pleasure she's letting out as I pound away at her."
    anna.say "Oh yeah..."
    anna.say "Just like that..."
    show anna missionary lookup
    anna.say "Fuck me harder, [hero.name]..."
    anna.say "Make me cum!"
    "Like I said before, I hardly need to be told what to do at this point!"
    "And based on where I seem to be going, Anna doesn't have anything to worry about either."
    "In fact, I can feel the sleeping-bag straining at the seams."
    "Making me think that we might be about to tear the thing apart!"
    show anna missionary pleasure
    "But just then I feel myself stiffen, and I grab hold of Anna."
    "She gasps as I make one final thrust into her."
    show anna missionary ahegao creampie with hpunch
    "Then I shoot my load, clinging onto her as I do so."
    with hpunch
    "Anna can't resist the sensation, and she begins to cum too."
    with hpunch
    "She almost curls into a ball, pressing herself into me."
    show anna missionary pleasure with hpunch
    "And I hold onto her like that, both of us riding out our climax."
    "Afterwards there are no words exchanged between us."
    "There doesn't seem to be any need for them."
    "Before we might have been lying when we said that we were tired."
    "But now we're both exhausted for real."
    "And sleep soon comes to claim us, still huddled together in my sleeping-bag."
    $ anna.sexperience += 1

    scene bg black with dissolve
    python:
        duration = 6 if hero.has_skill("no_sleep") else 8
        energy_recovery = 1.25 if hero.has_skill("no_sleep") else 1.0
        is_hungry = False
        energy_gained = hunger_decay = grooming_decay = 0.0
        for slept_hours in range(1, duration + 1):
            game.pass_time()
            energy_gained += energy_recovery
            hunger_decay += 0.5
            grooming_decay += 0.3
            if hero.hunger <= hunger_decay:
                is_hungry = True
                break
        if slept_hours == duration:
            energy_gained += 1.0
            hero.fun += 1
        hero.energy += energy_gained
        hero.hunger -= hunger_decay
        hero.grooming -= grooming_decay
    $ game.room = "forest"
    pause 1
    return

label anna_preg_talk:
    $ anna.flags.toldpreg = True
    show anna
    "I can tell that there's something on Anna's mind as soon as I see her."
    "With a girl as honest and open as Anna, it's almost impossible for her to hide what she's actually thinking."
    "The sheer amount of effort that she's putting into trying to act normal is the biggest give away of all."
    "Not wanting to make her life any harder than it already is, I play along, acting like everything's normal and I don't suspect a thing."
    show anna kiss
    $ anna.flags.kiss += 1
    "She reacts well when I give her a pretty passionate kiss and squeeze her ass in the middle of it."
    hide anna
    show anna
    "Anna giggles in a typically dirty fashion, and for a moment it's like she's back to normal again."
    mike.say "Anna, for God's sake - what's the matter?"
    anna.say "Huh...oh...nothing, I guess."
    mike.say "It's either nothing or else it's something."
    mike.say "How about you put the guessing aside and just tell me?"
    show anna cry
    "Anna looks at me, her eyes massive and staring, making her look more like an innocent puppy than ever."
    anna.say "Well, I was wondering...can we do anal tonight?"
    "I burst out laughing, I just can't help it."
    mike.say "Anna, we almost always do it that way!"
    mike.say "You like it, and I like that you like it so much."
    mike.say "Plus it saves on condoms and keeps us from having a little accident."
    "At the last few words, she instantly colours and deliberately looks away from me."
    mike.say "Anna...have you got something that you need to tell me?"
    mike.say "Something like, I don't know, you having missed a certain female monthly event?"
    "Anna still won't turn around and look me in the face."
    "But finally she nods, confirming my suspicions."
    mike.say "But how?"
    mike.say "We almost never do it anywhere but up the ass!"
    mike.say "Jesus, what are the odds!"
    show anna close cry
    "Anna finally turns round to face me."
    "Her eyes are puffy and red, as if she's on the brink of tears."
    anna.say "Well, we never bothered with precautions when we did...did we?"
    "I have to nod in agreement."
    "She's bang right - we got into such a habit of doing it anally I guess we just got lazy on the few other occasions."
    "We assumed that we'd be safe just because we were dabbling, and we got caught out."
    anna.say "[hero.name], please don't be mad at me?"
    mike.say "It's as much my fault as your's, Anna - why would I be mad with you?"
    anna.say "Well, you see...I want to keep it."
    "Saying the words out loud seems to somehow strengthen her will on the matter."
    anna.say "That is...I'm going to keep it."
    "She looks suddenly resolute and immovable."
    "It's then I realise she's waiting for me to react to what she just said."
    menu:
        "Dump her ass":
            mike.say "It's your decision, Anna - your body, your choice."
            mike.say "But this is the twenty-first century, and I'm a modern kind of guy."
            mike.say "I'm not going to be held down by any old-fashioned notions of 'doing what's right'."
            anna.say "What...what are you saying?"
            mike.say "I'm saying, Anna, that you can have the kid with my blessing."
            mike.say "But you'll be doing it on your own."
            "Anna's eyes widen even further, and she finally starts to actually shed tears."
            anna.say "You mean it's...it's over between us?"
            mike.say "Yeah, I guess that's exactly what I'm saying."
            $ sasha.set_gone_forever()
            $ kleio.set_gone_forever()
            $ anna.set_gone_forever()
            $ Room.find("bedroom3").hide()
            $ Room.find("studio").hide()
        "Beg her to abort":
            mike.say "Anna, have you really thought this through?"
            mike.say "I mean REALLY thought it through?"
            anna.say "Well, I haven't known for all that long."
            anna.say "I just know that I want to keep it."
            anna.say "That feels right and getting rid of it doesn't."
            "I sigh in frustration, wanting to keep Anna, but not being in the slightest bit ready to be a father."
            anna.say "I want this baby, [hero.name] - with you or without you!"
            "All I can do is shrug unhappily and look away from her."
            anna.say "I guess it's without you then..."
            $ anna.set_gone_forever()
        "Take responsibility":
            "For a moment I don't say a word, but the smile on my face begins to elicit one of Anna's own."
            show anna normal
            anna.say "What are you grinning like a fool for, [hero.name]?"
            mike.say "I was just picturing you with a massive baby-belly!"
            show anna angry
            anna.say "Hey!"
            show anna normal
            mike.say "No, you're getting it all wrong - I think you'll look great pregnant."
            mike.say "I also think you'll make a great mother too."
            "Anna looks at me expectantly, knowing that I haven't yet said the words she's wanting to hear."
            mike.say "Okay, I'll say it - I want to be with you, and the baby too."
            show anna happy
            "I don't need to say any more, as the look of happiness in Anna's eyes as she suddenly hugs me says it all."
    "There must have been more to the evening, more words spoken and things done."
    "But all I can recall, even after Anna's left, is the bombshell she dropped on me and what it means for our relationship."
    "Everything changes from here, for better or worse."
    return

label anna_kiss_me:
    call anna_greet from _call_anna_greet_5
    show anna b blush at center, zoomAt (1.75, (650, 1150))
    with vpunch
    "When Anna practically jumps up and grabs me by the collar, I can't help thinking something must have startled her."
    "But then I see her eyes, a mere couple of inches from mine as she hangs on to me."
    "There's no trace of surprise or fear in them, just an intense look of desire."
    hide anna
    show anna kiss
    $ anna.flags.kiss += 1
    "And then she presses her lips to mine, kissing me without a moment of hesitation."
    "Without thinking, I wrap my arms around her, plucking her from the ground."
    "Anna clings to me like an amorous little monkey, simply refusing to let go for as much as a second."
    hide anna kiss
    return

label anna_practice_01:
    "With the Battle of the Bands almost here, it feels like I've been shut in the practice room with the girls every spare moment for the past few days."
    "The stress is building, and being in such close confines means you can almost feel the tension as we go over stuff again and again."
    show sasha annoyed at left
    show kleio annoyed at center
    "Sasha is blunter than usual, and it's hard to get anything but grunts and acid glares out of Kleio."
    show anna at right
    "But Anna seems unaffected, blithly hammering away at her drumkit and casting me adoring glances whenever she gets the chance."
    show sasha angry
    sasha.say "Anna, what the fuck?!?"
    show anna surprised at vshake
    anna.say "Huh!"
    sasha.say "You're not keeping time right, it's ruining our sound."
    show kleio angry
    kleio.say "She's right, Anna - I could hear it too."
    "Anna looks surprised and more than a little downcast at the accusation."
    show sasha annoyed
    show kleio annoyed
    "I realise that, unlike Sasha and Kleio, I hadn't noticed Anna's mistake."
    "And then I also realise that was because of the attention she was paying me, and that this probably what made her screw up as well."
    "There's an awkward silence, as the girls are waiting for me to add my opinion as a fellow band member."
    menu:
        "Try to play peacemaker":
            $ a = 1
            mike.say "I didn't hear it, for what it's worth."
            show anna blush
            "Anna's eyes show her thanks for the support, and she seems to cheer up a little."
            show kleio angry
            kleio.say "Jesus, man - I knew you were tuneless, but you'd have to be stone deaf to miss something like that!"
            mike.say "Back up a bit, Kleio...we're all frazzled and strung out right now, and fighting each other'll only make it worse."
            show sasha normal
            sasha.say "He's got a point, Kleio - yeah, Anna fucked up, but we are all feeling the strain - let's take a break while we still can."
            $ anna.love += 5
        "Try to stay neutral":
            $ a = 2
            mike.say "Maybe you were a little off, Anna - but not by too much."
            show anna blush
            "Anna's eyes widen as all three of us basically agree she made a mistake, and she looks down at the drumsticks in her hands sadly."
            anna.say "I'm really sorry, guys...I guess I just wasn't trying hard enough."
            show sasha normal
            sasha.say "Ahh, we're all feeling it, Anna...but we're a team and we can get through this - let's take five and get our heads straight."
        "Side with Sasha and Kleio against Anna":
            $ a = 3
            mike.say "They're right, Anna - you're fucking up your part, and it's screwing with all of us."
            show anna cry
            "Anna's eyes are instantly filled with self-doubt, her lips quivering a little, and I can tell she expected me to defend her."
            show kleio normal
            kleio.say "He's not wrong, Anna - but don't get suicidal over it!"
            show sasha normal
            sasha.say "Yeah, Anna, we can fix the problem before the contest - but right now, we need to take a breather from this."
            $ anna.love -= 5
    hide kleio
    hide sasha
    hide anna
    with dissolve
    "Everyone downs their instruments, and there's an almost palpable sense of relief, as if a weight has been lifted off all four of us."
    "I slip out into the corridor, where there's an open window and the chance of some fresh air."
    "I've only been out there perhaps half a minute, when I hear the door open and see Anna has followed on my heels."
    if a == 1:
        show anna blush
        anna.say "Hey, thanks for sticking up for me back there."
        mike.say "No problem...look, I know you were off because you were into me."
        anna.say "Am I really that obvious?"
        mike.say "Don't feel bad, maybe it's the stress getting to you, that's all."
        mike.say "For what it matters, I'm not mad...actually, I'm flattered."
        show anna happy
        "Anna's mood changes suddenly for the better, and she hugs me tightly."
        "Her petite frame means that she barely comes up to my chest, but her grip is intense."
        mike.say "I just want you to know, Anna...you're more important than winning this contest."
    elif a == 2:
        show anna cry
        anna.say "Did you really think I screwed the song up just now?"
        "I take a deep breath and scrub my hand across my face, trying to slough off some of my fatigue."
        mike.say "Look, Anna - I'm sorry for ganging up on you like that, but you were off by a bit."
        mike.say "But I think we all were, if we're honest...you just got both barrels because Sasha spotted it first and we all jumped in."
        "Anna nods, still looking sad, but perhaps a little reassured that she's not the weak link in the band."
        anna.say "Okay, I guess that's something."
        show anna blush
        "She hugs me gently, more for the sake of reassuring herself than anything more amorous, and I hug her back weakly."
    else:
        show anna cry
        anna.say "I'm sorry...please don't be mad with me!"
        "I'd expected her to be angry that I'd torn a strip off of her in front of the others."
        "But Anna's clearly more concerned that she's upset me than made a mess of the song we were playing."
        mike.say "God's sake, Anna - I'm not mad at you, I'm mad that the song got fucked up."
        mike.say "The contest's so damn close that we can't afford to miss a beat right now."
        "Anna's silent for a moment, then she sniffles and visibly tries to look stronger, reminding me of a kid trying to look tough and failing."
        anna.say "Okay, got it...I'll keep focused on the contest, I promise."
    hide anna
    "Anna goes back into the practice room ahead of me, and I can hear her begin to bash the drums."
    "She's tentative at first, but I can hear her confidence slowly growing with each stroke of her drumsticks."
    "I take a deep breath and prepare to follow her in, hoping that my words have had the desired effect."
    return

label guitar_practice_book:
    "I practice some guitar with Anna's book."
    $ game.pass_time(2)
    $ game.set_flag("bandpractice", 10, mod="+")
    return

label anna_event_talk_murder:
    show anna cry
    anna.say "I can't believe it, [hero.name]."
    anna.say "None of this seems real."
    mike.say "I feel the same way, Anna."
    mike.say "And I was in the damn room when it all happened!"
    mike.say "I just wanted to say that I'm sorry, you know?"
    mike.say "Maybe if I'd done something differently..."
    "Anna raises her head from my chest and looks me in the eye."
    "Her own eyes are a little red and puffy from crying."
    "But the look in them is resolute and she shakes her head."
    anna.say "No, no, no..."
    anna.say "This isn't your fault!"
    if kylie.flags.rape == True:
        anna.say "You're as much a victim as poor Sasha!"
        anna.say "What that horrid girl did to you..."
        anna.say "Ooh...I'll never forgive her for that!"
    else:
        anna.say "This is all that horrid girl's fault!"
        anna.say "She's the one that deserves to be punished."
        anna.say "Not you, [hero.name]!"
    "I nod my head, trying my best to agree with Anna's take on events."
    "I can't say that she manages to convince me totally."
    "But it feels reassuring to hear someone defending me like that."
    mike.say "Maybe you're right, Anna."
    mike.say "But I'd give anything to have Sasha back!"
    $ anna.love += 10
    show anna b cry at center, zoomAt (1.75, (650, 1150))
    anna.say "Of course you would!"
    anna.say "And that's because you're the good guy!"
    anna.say "Bad people always do bad things."
    anna.say "Good people always do good things."
    anna.say "You just need to be around more good people!"
    show anna b cry at zoomAt (1.95, (650, 1250))
    "I can't help pulling Anna closer to me as she says this."
    "I need positive energy in my life right now."
    "And she's giving it out like crazy."
    mike.say "Thanks for being a friend, Anna."
    anna.say "I'm here for you, [hero.name]."
    anna.say "We gotta stick together now, all of us!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
