init python:
    Event(**{
    "name": "metal_harem_event_01_a",
    "label": "metal_harem_event_01_a",
    "priority": 500,
    "conditions": [
        IsDone("scottie_female_event_01"),
        IsHour(7, 11),
        HeroTarget(
            IsGender("female"),
            IsRoom("bedroom4")),
        PersonTarget(scottie,
            Not(IsHidden())
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            MinStat("love", 20),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "metal_harem_event_01_b",
    "label": "metal_harem_event_01_b",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("metal_harem_event_01_a"),
        IsHour(17, 19),
        HeroTarget(
            IsGender("female"),
            IsRoom("bedroom4")),
        PersonTarget(scottie,
            Not(IsHidden())
            ),
        PersonTarget(sasha,
            Not(IsHidden())
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "metal_harem_event_02",
    "label": "metal_harem_event_02",
    "priority": 500,
    "duration": 2,
    "hunger": 10,
    "conditions": [
        IsDone("metal_harem_event_01_b"),
        TogetherInHarem('metal', 'sasha', 'scottie'),
        IsHour(17, 19),
        HeroTarget(
            IsGender("female"),
            IsRoom("bedroom4")),
        PersonTarget(scottie,
            Not(IsHidden()),
            MinStat("love", 40),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            MinStat("love", 40),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "metal_harem_event_03",
    "label": "metal_harem_event_03",
    "priority": 500,
    "duration": 2,
    "hunger": 10,
    "conditions": [
        IsDone("metal_harem_event_02"),
        IsTimeOfDay("afternoon", "evening"),
        HeroTarget(
            IsGender("female"),
            IsRoom("kitchen")),
        PersonTarget(scottie,
            Not(IsHidden()),
            MinStat("love", 60),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 60),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "metal_harem_event_04",
    "label": "metal_harem_event_04",
    "priority": 500,
    "duration": 3,
    "conditions": [
        IsDone("metal_harem_event_03"),
        IsHour(22, 0),
        HeroTarget(
            IsGender("female"),
            IsRoom("bedroom3")),
        InInventory("fancy_dress"),
        PersonTarget(scottie,
            Not(IsHidden()),
            MinStat("love", 80),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 80),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "metal_harem_event_05",
    "label": "metal_harem_event_05",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("metal_harem_event_04"),
        IsHour(8, 11),
        HeroTarget(
            IsGender("female"),
            IsRoom("kitchen")),
        PersonTarget(scottie,
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "metal_harem_event_06",
    "label": "metal_harem_event_06",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("metal_harem_event_05"),
        IsSeason(0, 1),
        IsHour(10, 18),
        HeroTarget(
            IsGender("female"),
            IsRoom("pool")),
        InInventory("swimsuit"),
        PersonTarget(scottie,
            Not(IsHidden()),
            MinStat("love", 120),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            MinStat("love", 120),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "metal_harem_event_07",
    "label": "metal_harem_event_07",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("metal_harem_event_06"),
        IsHour(9, 18),
        HeroTarget(
            IsGender("female"),
            HasRoomTag("home")),
        PersonTarget(scottie,
            Not(IsHidden()),
            MinStat("love", 140),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            MinStat("love", 140),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "metal_harem_event_08",
    "label": "metal_harem_event_08",
    "priority": 500,
    "duration": 2,
    "conditions": [
        IsDone("metal_harem_event_07"),
        IsHour(15, 18),
        HeroTarget(
            IsGender("female"),
            HasRoomTag("uni")),
        PersonTarget(scottie,
            Not(IsHidden()),
            MinStat("love", 160),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            MinStat("love", 160),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "metal_harem_event_09_a",
    "label": "metal_harem_event_09_a",
    "priority": 500,
    "conditions": [
        IsDone("metal_harem_event_08"),
        IsHour(9, 18),
        HeroTarget(
            IsGender("female"),
            IsRoom("bedroom4")),
        PersonTarget(scottie,
            Not(IsHidden()),
            MinStat("love", 180),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            MinStat("love", 180),
            ),
        ],
    "quit": False,
    })

    Event(**{
    "name": "metal_harem_event_09_b",
    "label": "metal_harem_event_09_b",
    "priority": 500,
    "duration": 2,
    "conditions": [
        IsDone("metal_harem_event_09_a"),
        IsHour(19, 22),
        HeroTarget(
            IsGender("female"),
            HasRoomTag("home")),
        PersonTarget(scottie,
            Not(IsHidden())
            ),
        PersonTarget(sasha,
            Not(IsHidden())
            ),
        ],
    "quit": False,
    })

label metal_harem_event_01_a:

    play sound door_knock
    "I hear knocking at the door."
    "Not too long ago, Scottie came over and almost gave me a wallop."
    "Sasha and Scottie exchanged some harsh words to each other over... I think Sasha dumping him."
    "...Because she got bored."
    "I roll out of bed and put on a quick outfit to make myself presentable enough to open a door. I don't really want to open it in pajamas."
    scene bg house
    show scottie embarrassed
    with wiperight
    "I rush downstairs and open the door to see Scottie. Figures."
    scottie.say "I- hey, I..."
    bree.say "What do you want, Scottie? I'm not too happy to see you after last time. You really gave me a scare, you know?"
    bree.say "It's some jerk move to do that to someone."
    show scottie sad
    "Scottie looks down and rubs the back of his head."
    scottie.say "Yeah... I know. I wanted to come make it up to both of you and show you how charming I can be."
    bree.say "I'm not sure Sasha will agree to that. How did you two manage to get that upset over nothing, anyways?"
    show scottie normal
    scottie.say "I'm sure you noticed we both have quite the temper."
    bree.say "Oh, right. Yeah. Sasha does get mad at weird things. Sometimes she throws stuff."
    show scottie sad
    scottie.say "Ugh, I know..."
    "I didn't hear it, but Scottie murmured something after that. It sounded something like ‘so sexy'."
    "Whatever. I don't judge anyone."
    "Sasha comes downstairs while Scottie ponders."
    show scottie at right
    show sasha annoyed at left
    with fade
    sasha.say "What's going on? Scottie? I thought you said you weren't as stupid as you looked?"
    show scottie angry
    scottie.say "Sasha. Don't you dare."
    sasha.say "Oh? And why not?"
    show scottie normal
    scottie.say "Coffee? Us three? You can't resist me."
    sasha.say "Not a chance."
    scottie.say "I'll pick you two hotties up this evening."
    scene bg black with dissolve
    pause 0.1
    scene bg livingroom
    show sasha annoyed at right
    with wipeleft
    "Sasha tries to protest, but Scottie shuts the door and leaves. We can hear him still."
    scottie.say "I'll win you two over!"
    "I look at Sasha."
    bree.say "What? Just happened?"
    sasha.say "He- he just... came over and is basically making us go to have coffee or other... beverages?"
    bree.say "I know. I just don't know what happened anyways. It feels weird."
    sasha.say "You're telling me. Well. Hopefully it's not as boring as it's been for a while."
    "What's Sasha's idea of ‘fun', anyways?"
    hide sasha with easeoutright
    "She leaves and I'm left mostly alone until later. I catch up on some biology things in the meantime."
    return

label metal_harem_event_01_b:
    play sound door_knock
    "Someone comes and knocks on my door."
    bree.say "Yes? Come in!"
    show sasha at right with easeinright
    "Sasha opens the door. She sheepishly comes in."
    sasha.say "So... are we going? What are you going to wear?"
    "I gape at her."
    bree.say "I thought you weren't interested?"
    sasha.say "Listen, we all have... changing tastes sometimes, okay?"
    bree.say "But this wasn't even ten hour ag-"
    show sasha annoyed
    "Sasha covers her ears."
    sasha.say "I don't want to hear it! Are you coming or not?"
    menu:
        "No":
            bree.say "No, thank you."
            bree.say "It was nice of him to apologize but I need more time before I really trust him."
            show sasha normal
            sasha.say "Okay, I can understand you. So, see you later."
            hide sasha with easeoutright
            "Sasha leaves as I get lost in my thoughts."
            if scottie.love.max < 180:
                $ scottie.love.max = 180
        "Okay":
            "I think for a second. Scottie doesn't... seem like the brightest guy, but he seems exciting to be around."
            bree.say "I don't see why not, I guess. I'll wear something pretty standard. I'm not going to see the queen, haha."
            show sasha happy at startle
            "Sasha snorts."
            show sasha normal
            sasha.say "Yeah. yeah. Very funny. Alright. Be out soon, then."
            hide sasha with easeoutright
            "I nod at her and she shuts the door behind her. I quickly get dressed and freshen up."
            scene bg coffeeshop
            show scottie at right
            show sasha at left
            with fade
            "I come meet up with Sasha and leave with her to see Scottie and head to a small coffee shop."
            "The shop is charming. The decor is coffee shoppy. Nothing out of the ordinary."
            "We each ask for our coffee of choice and Scottie pays for us like he said he would, as his apology treat."
            "Sasha and I go find a table while Scottie asks the barista for something else."
            scene bg coffeeshop
            show sasha at center, zoomAt(1.5, (340, 1040))
            with fade
            pause 0.5
            show sasha at center, zoomAt(1.5, (340, 1140)) with ease
            "We sit down and get comfy."
            bree.say "This is cute."
            sasha.say "I'll say. This place has good coffee, too. You'll like it."
            show scottie at center, zoomAt(1.5, (940, 1040)) with easeinright
            pause 0.5
            show scottie at center, zoomAt(1.5, (940, 1140)) with ease
            "Scottie pulls up a chair and sits down, setting a few baked goods in front of us."
            show scottie sad
            scottie.say "I don't know what any of these dumb things are besides the muffin."
            show sasha happy with vpunch
            "We laugh at his cluelessness. It's a bit hard to believe a guy like him doesn't know anything about small baked items."
            "But a little cute, I guess? Maybe?"
            bree.say "Alright. Well, this one is a scone. They're usually triangles, I think, but they can be circles too."
            bree.say "I've only ever had dry ones, but you're supposed to eat them with your tea or coffee. The fruity ones are the best."
            show sasha normal
            sasha.say "And this one, knucklehead, is just an apple turnover."
            sasha.say "You put some apples in a square and you turn the dough flap over the apples and you get a warm little pie pocket."
            show scottie annoyed
            scottie.say "Why do you know any of this? This is pointless."
            show sasha happy with vpunch
            "Sasha and I look at each other and laugh."
            bree.say "Haven't you ever seen Food Channel? They had good stuff like, all the time!"
            show sasha normal
            sasha.say "Yeah, I'd have it on while writing stuff for the band or when I was just doing school homework."
            show scottie normal
            scottie.say "My ma would watch that. I didn't know it would be interesting. Or useful. It sounded like a waste of time."
            sasha.say "They have a really cool program named Slashneck Kitchen and you're supposed to sabotage other chefs."
            bree.say "Oh I watched that one! Yeah! You could give another chef an anti-boon, like only being able to use one multitool instead of knives and other stuff."
            show scottie surprised
            "This got Scottie's attention."
            scottie.say "How do you cook with a multitool?"
            bree.say "Very carefully."
            show sasha happy at startle
            "Sasha barks out a laugh."
            show scottie normal
            "Scottie doesn't seem too impressed."
            scottie.say "Alright, fine. We'll watch some next time. Which one do I eat?"
            show sasha normal
            sasha.say "How picky are you?"
            show scottie joke
            scottie.say "Uhh... not overly."
            bree.say "Have the scone, honestly. It's a bit hard to get into but it's pretty yummy."
            show scottie normal
            "Scottie takes the scone while I am speaking and takes a big bite out of it."
            show scottie embarrassed
            "His nose crunches up. I did tell him it was dry!"
            "He tries to talk, but there's too much dry scone. He drinks some of his coffee to try and wash it down."
            scottie.say "It'th goof buh I biht too much."
            sasha.say "It's... good, but you had too much?"
            bree.say "Bit."
            show scottie happy
            "Scottie gives me a fingergun."
            scottie.say "It's good. Fruity."
            bree.say "Good. I am glad you liked it."
            sasha.say "Heh."
            show scottie normal
            "We keep chatting amongst ourselves about how good the pastries are and about how full-bodied the coffee is."
            "Eventually, we have to break. I had a nice time and got to see another angle to how Scottie and Sasha interact."
            "I think Scottie's redeemed himself a lot for me."
            "We'll see soon."
            scene bg black with dissolve
            if sasha.love.max < 40:
                $ sasha.love.max = 40
            if scottie.love.max < 40:
                $ scottie.love.max = 40
            $ Harem.join_by_name("metal", "sasha", "scottie")
    return

label metal_harem_event_02:
    "I mind my business studying when Sasha calls me downstairs."
    "Huffing, I put away some of my books and papers and tidy up."
    scene bg secondfloor
    show sasha
    with hpunch
    "I make my way down the stairs and bump into Sasha."
    bree.say "Oh! Sorry about that!"
    sasha.say "I was heading up because you hadn't replied!"
    bree.say "Haha... sorry about that... was in the middle of studying and then I got called down so I sort of got cranky about it in the moment..."
    bree.say "...and forgot to reply."
    show sasha annoyed
    sasha.say "God. You're impossible sometimes."
    bree.say "I apologized! What is it?"
    show sasha normal
    sasha.say "I just... I wanted to know if you wanted to watch a film. With me. Maybe someone else too."
    "She sort of... did she mean to say it like that?"
    "I mean, if I could see italic font, that would be it. Like, that would be what the document has in italics."
    bree.say "Who? Scottie? Are you giving into his..."
    "I wave my hands around."
    bree.say "...charms?"
    show sasha annoyed
    sasha.say "No way. You're being silly. He's cute and all... but I don't know."
    bree.say "Yeah, I mean, you are just a bundle of unstoppable edgy energy."
    show sasha normal
    sasha.say "Exactly. I need someone that can keep it going."
    "Oh, she didn't notice I was joking. Haha. Cute."
    "I chuckle a bit."
    bree.say "It sounds kind of nice. Are we ordering in? I don't really want to do anything tonight for food."
    bree.say "I'm totally winded after some exams this week."
    sasha.say "I'm winded hearing you talk about them and complain about the bullshit on the damn things."
    bree.say "Oh, heck, am I that loud?"
    show sasha happy
    sasha.say "Yep."
    "Yikes. Maybe I have a temper just like Sasha and Scottie do. Haha."
    bree.say "Your temper is rubbing off on me then, Sasha."
    sasha.say "Hey, hey. Don't go blaming me for that weird stuff they make you read. That ain't my fault."
    show sasha normal
    "I huff."
    bree.say "Fine, fine. What time are we doing the movie?"
    bree.say "We can do dinner beforehand and try making some popcorn or some other stuff."
    sasha.say "Uhh... after dinner? It's not really set, it's just whenever."
    bree.say "Alright! See y'all soon for that, then."
    "Sasha and I order some takeout and have dinner."
    scene bg black with timelaps
    scene bg livingroom
    show sasha at left
    show scottie at right
    with timelaps
    "Scottie comes by not long after."
    show scottie joke
    scottie.say "SOMEBODY told me we were making popcorn. I'm a popcorn FIEND."
    bree.say "Knock yourself out. I always burn it, and Sasha just sets it on fire."
    sasha.say "I do not!"
    bree.say "Yes you do. The fire alarm went off last time. I managed to open enough windows for my accident, but you set the bag on fire."
    sasha.say "Do you believe [hero.name]???"
    show scottie happy at startle
    "Scottie is busy laughing, but he nods in between his cackles."
    show sasha embarrassed
    "Sasha pouts."
    sasha.say "Fine. YOU make the popcorn. I'll wait and pick a film."
    scene bg kitchen with fade
    show scottie with easeinright
    "Scottie beckons me over to the kitchen."
    scottie.say "Okay, so I watched that stupid Food Channel stuff you two were talking about."
    scottie.say "I saw some weird guy talking about how to make popcorn instead of anything else. Anything fancy."
    scottie.say "I think his name was Eldon Grey."
    bree.say "The science dude? Looks like he could be a laboratory guy?"
    show scottie happy
    scottie.say "Yeah, that one. He used a mixing bowl for it. Let's try it."
    show scottie annoyed
    scottie.say "Full disclosure, I tried using a plastic bowl at my place and it didn't go well."
    bree.say "No... no shit? Stupid? Oh my god. Why did you- nevermind."
    bree.say "This sounds like it might burn the place down, but I'm also down to do it. We're not using plastic, though."
    show scottie normal
    "We take a stainless steel bowl and put some foil over it. Through a little hole, we put some butter in it."
    "After it melts, we take a Scottie-sized handful of kernels and toss it in."
    "The kernels start popping quickly and we end up having to dump the popcorn out in a minute or two."
    "None of them look burned."
    "Nice."
    bree.say "Nice. Good."
    show scottie happy
    "Scottie smiles. He seems proud."
    scottie.say "Thank you, Food Channel."
    sasha.say "Oh, that smells good. You didn't burn anything? Put some butter on it!"
    show scottie joke at startle
    "Scottie and I look at each other and laugh. She's bossy, but charming."
    scottie.say "Oh, we should get something to drink."
    show scottie at right5 with ease
    "Scottie pivots and starts pushing stuff everywhere in the fridge. No shame, either."
    "Scottie pulls out some... juice, water, and beer."
    scottie.say "I would like the water."
    bree.say "That's flat Sprit. The soda."
    show scottie surprised
    scottie.say "Why the hell is this in here?"
    bree.say "Beats me. All I know is that the water comes from the fancy pitcher you managed to miss. Want a cup?"
    show scottie annoyed
    "Scottie pulls the pitcher out, pouting."
    bree.say "Goofball. Give the beer to Sasha."
    scene bg livingroom
    show sasha at left
    show scottie at right
    with fade
    "After we settle the drinks and we figure out what bowl the popcorn should go in, we watch The King's New Schmoove."
    scottie.say "Oh, man, I haven't seen this movie in forever."
    sasha.say "I haven't either... I remember it being one of my childhood favorites though?"
    bree.say "I saw this pretty recently! Sasha is the alpaca."
    sasha.say "Yeah, well, Scottie is the himbo. He's stupid but strong, so it fits."
    show scottie surprised
    scottie.say "What? No? Hello? I have more game than he does."
    bree.say "Scottie, bud, I'm not going to lie to you, I don't think anyone has more charm than him."
    show scottie joke
    scottie.say "Just watch. I'll prove you two bimbos wrong one day."
    "We keep bantering on who the evil witch is or which character matches who."
    "The movie is nice and everyone enjoys it."
    "The popcorn is delicious and it's not burned. It's very important that we understand this."
    "It's NOT. BURNED."
    show scottie annoyed
    scottie.say "Yep. Definitely the himbo."
    show sasha annoyed
    sasha.say "Totally not the alpaca."
    bree.say "Definitely the alpaca, absolutely the himbo. I'm just the poor little farmer that gets roped into everything."
    sasha.say "VERY funny, [hero.name]."
    show scottie happy at startle
    "Scottie laughs."
    "I don't think they think I'm right."
    scottie.say "You're one of the farmer's little kids that just argues every time we see them on screen."
    bree.say "I-"
    show sasha happy at startle
    "Sasha cackles."
    sasha.say "Oh man, oh man, he got you there."
    show scottie normal
    scottie.say "Alright, well, movie, drinks, and popcorn are done. I like this relaxing stuff. It's different."
    bree.say "Do you want to do another calm thing next time?"
    scottie.say "Yeah. I'll call."
    sasha.say "We'll look forward to it."
    scene bg livingroom with fade
    "And with that, Scottie cleans up after himself, washes the steel drum of a dish he used, and starts heading home."
    show sasha with dissolve
    sasha.say "That was... nice."
    bree.say "I liked it."
    sasha.say "Maybe... well, maybe not. Nevermind. See you tomorrow, [hero.name]. I'm off to bed."
    hide sasha with easeoutright
    "And with that, Sasha went upstairs."
    "Was she getting feelings for Scottie again, or was she just wondering about something else?"
    "Hmm."
    "It's late. I should go to bed too."
    "I turn off the lights and go up to brush, and head to sleep."
    scene bg bedroom4
    if sasha.love.max < 60:
        $ sasha.love.max = 60
    if scottie.love.max < 60:
        $ scottie.love.max = 60
    return

label metal_harem_event_03:
    "I'm busy making lunch when I hear Sasha on the phone with Scottie."
    sasha.say "[hero.name]? She's uhh..."
    show sasha at top_mostright with easeinright
    "Sasha peeks to see me."
    sasha.say "She's making lunch."
    "She covers the phone and yells out to me."
    sasha.say "Are you making me some?"
    bree.say "Gosh, Sasha, you're such a potato. Why don't you come make any?"
    sasha.say "Next time!"
    bree.say "Fine, fine."
    "I start making another omelet for the potato. I place diced potatoes on the side in the shape of a potato."
    show sasha at center with ease
    "Sasha comes over."
    sasha.say "Is that for m- hey, wait a minute..."
    show sasha surprised
    "I laugh a little."
    bree.say "Yes."
    show sasha annoyed
    "Sasha pouts at me."
    sasha.say "Huff. See if I invite you to go out with us later, then."
    bree.say "Wait, Sasha, no, please, I'm sorry."
    "I bat my eyelashes at her."
    bree.say "Pleaseee? I'm too precious."
    show sasha normal
    sasha.say "Rgh... fine. We're just planning on going to the park."
    bree.say "But I just made us lunch, Sasha!"
    sasha.say "Who said we had to eat there?"
    sasha.say "Let's make some snacks and see if we can find some ice cream there."
    bree.say "Fine. You make the snacks. I'm going to go upstairs and get dressed."
    scene bg bedroom4 with fade
    "I hear a clamor in the kitchen while I get ready to go."
    "I grab one of my blankets to sit on and a few dollar bills so we can get some ice cream."
    "I don't really know where my wallet went, but I'll find it later. My study stuff is a mess. I'm not digging through that."
    "Thankfully, I'm smart enough to keep extra money just hanging out."
    "(Or is that silly? Heh.)"
    "I hear Sasha yell from the kitchen."
    sasha.say "Alright! Time to leave!"
    "I carry my blanket with me and offer to help Sasha with her snacks. She pouts and just pulls me along instead, closing the door behind me."
    scene bg park
    show sasha casual
    with fade
    "We arrive at the park and Scottie isn't there yet."
    "There is a small event, something like a small music festival?"
    "There's a couple of groups lined up to play on a little stage near a fountain."
    sasha.say "I can't believe they didn't ask my group to play!"
    bree.say "None of these look like big titty goth girlfriend bands, Sasha."
    show sasha joke
    sasha.say "You think I have big titties?"
    bree.say "Wait, I didn't say tha-"
    show sasha embarrassed
    "Sasha shushes me."
    show sasha shy
    sasha.say "I think you're cute, [hero.name]."
    "I blush. I can't really believe how I got myself into this position."
    show sasha normal
    sasha.say "Honestly, if you wanted to, we could... maybe..."
    "Scottie waves from afar and yells our names out, interrupting Sasha."
    "I'm a little upset he had the audacity to do that, but he didn't know. Poor himbo."
    scottie.say "Sasha! [hero.name]!"
    show sasha at right5
    show scottie at left
    with easeinleft
    "We wave back, though Sasha makes sure to give me a wink before she turns towards Scottie."
    show scottie at left5 with ease
    scottie.say "Did you pick a spot? What's going on today? It's busy here."
    sasha.say "It looks like a music festival that my band didn't get invited to."
    show sasha joke
    sasha.say "After we found that out, you interrupted my heavy flirting with [hero.name]."
    show scottie surprised
    scottie.say "What?"
    "Scottie turns to look at me and then looks back at Sasha."
    scottie.say "You're going to flirt without me?"
    show sasha annoyed
    "Sasha's brows furrow. She didn't seem to like that."
    sasha.say "Sorry? Am I supposed to get your permission or something?"
    "Scottie shakes his head."
    show scottie normal
    scottie.say "Oh, no. No, no, no. I'm just saying that she ought to have someone else here too, you know. For comparison."
    show scottie joke
    scottie.say "Since I'm infinitely better at it than you are."
    show sasha wtf
    sasha.say "Excuse me? You think you can swoop in and cockblock me?"
    scottie.say "Tsk, tsk, Sasha. Your mind is closed. Imagine how red [hero.name] would get if two people made her blush instead?"
    show sasha surprised at right5, startle
    "Sasha's eyes light up."
    show sasha embarrassed
    sasha.say "You terrible goblin of a man."
    show scottie happy
    "Scottie beams."
    "They both turn towards me. Maybe if I don't move they won't see me. Are they like raptors at this point?"
    "They sure feel like raptors. Hunting in a pack and all."
    bree.say "L-listen, y'all, you don't have to go to such drastic measures, you know?"
    bree.say "How about we just lay my blanket out and we listen to the bands?"
    "I'm extremely embarrassed and I'm blushing. I feel like a beet."
    "I'm also... very flattered. They're both very cute, but I just don't know them very well enough to return the favor. I feel shy."
    "They both smirk at me. I think they probably get the idea, but I don't think it's out of their minds."
    "Somehow, I look forward to it."
    scene bg park at center, zoomAt(1.75, (180, 740))
    show sasha at center, zoomAt(1.5, (940, 940))
    show scottie at center, zoomAt(1.5, (340, 940))
    with fade
    pause 0.5
    show sasha at center, zoomAt(1.5, (940, 1140))
    show scottie at center, zoomAt(1.5, (340, 1140))
    with ease
    "We sit down on my blanket and Sasha starts playing with my hair."
    show sasha shy
    sasha.say "So soft..."
    show sasha normal
    sasha.say "Scottie can you get the snacks? I brought a whole bunch of stuff."
    show scottie happy
    scottie.say "Yeah, alright."
    show scottie normal at startle
    "I watch Scottie pull out... fruit cubes, water bottles of the reusable variety, sandwiches, and carved... fruit?"
    bree.say "Wow, Sasha, did you...?"
    show scottie happy
    scottie.say "Ah yes, the carved fruit. You always did remind me that you could ‘figure out how to do this to someone'."
    show sasha joke
    sasha.say "[hero.name] called me edgy. And goth. And big titty girlfriend. You should know this by now."
    with vpunch
    bree.say "Sasha!!"
    show scottie joke
    scottie.say "She's right, but you don't have to carve someone like you would a turkey or a fruit. Damn. Fucking alpaca."
    sasha.say "Himbo."
    bree.say "Now, now, children."
    show sasha normal
    show scottie normal
    with fade
    "A few bands begin to play right after the other and we talk in between them."
    "We like some of them a lot, but Sasha always comments that her group is way better than anything we're seeing."
    "We munch on the snacks cozily on the blanket together."
    "It's pleasant and calm."
    "When the show ends, the sun is low on the horizon, and our snacks are all gone."
    show scottie happy with fade
    scottie.say "I like these chill outings, but I kind of want to do something else next time."
    sasha.say "We could go out to the night club next time?"
    bree.say "I guess we can't always have relaxing dates."
    "Wait. Did I say that? Oops."
    bree.say "Wait, no, I didn't mean-"
    show scottie joke
    scottie.say "Dates, huh?"
    show sasha joke
    sasha.say "[hero.name] is adorable, isn't she?"
    scottie.say "I didn't think my charms worked that fast, but hey, I even surprise myself."
    show scottie at center, zoomAt(1.5, (340, 940)) with ease
    "Scottie stands up."
    scottie.say "Well, sunset's here. Time to go, eh?"
    scene bg park with fade
    "We head home, making a plan for next time. The night club!"
    scene bg livingroom
    if sasha.love.max < 80:
        $ sasha.love.max = 80
    if scottie.love.max < 80:
        $ scottie.love.max = 80
    return

label metal_harem_event_04:
    show bg door bedroom3 at center, zoomAt(1.5, (640, 1040))
    pause 0.3
    play sound door_knock
    "I go rap on Sasha's door."
    bree.say "Party night, party night!"
    sasha.say "PARTY NIGHT, PARTY NIGHT!"
    scene bg black with dissolve
    pause 0.5
    scene bg bedroom3
    show sasha surprised at center, zoomAt(1.5, (640, 1040))
    with hpunch
    "Sasha flings her door open and almost whacks herself with it."
    show sasha joke
    sasha.say "Ah! Oh, the door. I should... chill."
    bree.say "Chill."
    show sasha happy at vshake
    sasha.say "PARTY!"
    bree.say "How much do you drink, Sasha?"
    show sasha joke
    sasha.say "[hero.name], you will find out tonight!"
    "I do not get a good feeling from this. Not a single good one."
    "We both go get ready while Scottie pops on over. We had agreed on going together during our last outing."
    "Since Sasha and I live together, it just makes more sense for Scottie to come over first."
    "I am ready last and head downstairs."
    scene bg livingroom
    show sasha date at left5
    show scottie joke date at right5
    with fade
    scottie.say "[hero.name]. Pregame?"
    bree.say "Oh man, I hardly drink already. I'll be a wreck."
    sasha.say "It's alright. You'll have some either way, it's up to you when, right?"
    bree.say "Wait who is our designated driver if you're both drinking and I'm supposed to drink too?"
    sasha.say "Oh, I asked [mike.name] if he'd do it. We're sort of just waiting on him at this point."
    show scottie normal
    scottie.say "He said he'd be fine with it as long as we didn't mess his car up."
    "We hear a horn beeping outside."
    show sasha happy
    sasha.say "Speak of the devil and he shall appear, eh?"
    bree.say "Gosh, I hope I don't get absolutely blasted."
    show sasha normal
    sasha.say "Are you really that bad with your alcohol?"
    bree.say "Yes. Probably. I don't know."
    play music "music/darren_curtis/feel_it_in_your_feet.ogg" loop
    scene bg nightclub
    show sasha date at left5
    show scottie date at right5
    with fade
    "The club is loud and it's hard to hear Scottie and Sasha."
    "It's.. not unpleasant, though. Everyone looks nice and the atmosphere is upbeat and exciting."
    "Scottie and Sasha take me by the hands and lead me to get a drink."
    sasha.say "What do you want? What do you like? Scottie and I know all of these drinks and can help you out."
    scottie.say "Do you like fruity stuff like that crumpet?"
    bree.say "Th-the scone? The SCONE?"
    scottie.say "Isn't that what I said?"
    show sasha annoyed
    sasha.say "No, you dumb bimboy. You said crumpet."
    scottie.say "What's a crumpet?"
    bree.say "Nevermind! Give me something fruity!"
    show sasha happy
    sasha.say "Ahh, I know what to get her. What's that pineapple thing called?"
    scottie.say "I think it's the Tart Freshspress?"
    show sasha normal
    sasha.say "I want two Tart Freshspresses and a shot of whatever you got on hand!"
    "We drink."
    "The pineapple thing had some blended berry mix, pineapple, strong liquor of some kind, and some fizzy juice."
    "It was sweet. Those are the dangerous ones, I think. It's because you can't taste how much alcohol is in it."
    "Sasha finished hers about four times as fast as I finished mine, so the two had to wait for me to go dance."
    "We chatted for a bit."
    scottie.say "Alright, make sure you have a lot of water."
    sasha.say "It gets warm in these places when you're drunk and doing exercise, so drink PLENTY."
    sasha.say "Of water. Alcohol too, if you want."
    bree.say "I'm not blasted yet, but I think I'm up to dance."
    scottie.say "It'll probably hit you over there, honestly."
    show sasha happy
    sasha.say "Alright! PARTY TIME!"
    bree.say "Party time, party time!"
    show sasha normal
    "We head over to the dance floor together after having some water."
    "Why is everyone so hot?"
    "We get together in our little pod and dance. Sasha's totally on the beat, but that's expected of her."
    "Scottie... not so much."
    show sasha joke
    sasha.say "Scottie, you need us to teach you how to dance? What's up with your two left feet? Can't you feel the beat?"
    bree.say "Are you trying to write something while drunk or was that an accident?"
    show sasha wink
    "Sasha winks at me."
    scottie.say "I don't know what you're talking about! I feel fine!"
    show sasha happy
    sasha.say "Come on, [hero.name]. We gotta teach him how it's done."
    scene bg nightclub
    show sasha date zorder 2 at center, zoomAt(1.5, (640, 1040))
    "Sasha takes my elbow and turns me around to stand next to her."
    "The music gets a bit louder and the lights start to flicker to the beat on the dance floor."
    show sasha at center, zoomAt(1.65, (640, 1080))
    "Sasha presses the side of her hips against mine and we dip in sync to the rhythm."
    show sasha at center, zoomAt(1.65, (840, 1080))
    show scottie date zorder 1 at center, zoomAt(1.5, (440, 1040))
    with easeinleft
    "We move Scottie's hands to our hips, and he presses his hips against ours."
    "He's... very off rhythm. How is he this bad?"
    bree.say "You're like, weirdly slow? Go a little faster!"
    show scottie annoyed
    scottie.say "That doesn't make any sense!"
    show scottie embarrassed
    "I turn around and put my hands on his hips and try to direct how he should rock them to let his feet move along."
    "Sasha sees this and moves his shoulders the other way, since that's how bodies that know how to dance usually do it."
    "Something something contrapposto? It's an art thing someone told me a while ago."
    show scottie normal
    "Scottie eventually gets it and we have fun looking like a group that knows how to dance instead of a little awkward group."
    show sasha joke
    sasha.say "After how bad you were, I can't believe you're actually managing to pull out some moves."
    show scottie joke
    scottie.say "I've told you both this for a while now. I may have some walls to cross, but the charm knows no bounds."
    show sasha happy at startle
    show scottie at startle
    "We laugh and enjoy our time."
    "We tire eventually and need more water. I decide to get another drink, but it wasn't the best idea in the end."
    "I sort of... got too tipsy. We still danced some more, but I was a bit of a wreck by the end of it."
    "It's those fruity drinks. They're dangerous!"
    scene bg nightclub
    show sasha date at center, zoomAt(1.5, (940, 1040))
    show scottie date at center, zoomAt(1.5, (340, 1040))
    with fade
    sasha.say "Whew! I had fun. I think [hero.name] is out for the night though, look at her!"
    scottie.say "Oh, shit. Should I.. do I carry her? What do I do? I don't want to look weird."
    sasha.say "I'm here so it'll be fine. Let's get out slowly and call [mike.name]."
    scene bg street
    show sasha date at center, zoomAt(1.5, (940, 1040))
    show scottie date at center, zoomAt(1.5, (340, 1040))
    with fade
    "Scottie makes sure I don't tip myself over on accident while we leave and wait."
    "..."
    "[mike.name] arrives soon after and we head back home."
    "The car ride makes me feel a bit sick, but I hold everything in like a champ."
    scene bg bedroom4
    show sasha date at center, zoomAt(1.5, (940, 1040))
    show scottie date at center, zoomAt(1.5, (340, 1040))
    with fade
    "It feels like a really long time, but we get home."
    show sasha annoyed
    sasha.say "I jinxed her. I can't believe I jinxed her. She really is that shit at holding her alcohol. I'm not even that drunk!"
    scottie.say "You had more than I did, I think."
    show sasha joke
    sasha.say "Of course I did. I've always been able to drink you under the table."
    show sasha normal
    sasha.say "Alright, kiddo, let's get you to brush your teeth and get more water."
    scottie.say "I can keep holding her up."
    scene bg bathroom
    show sasha date at center, zoomAt(1.5, (940, 1040))
    show scottie date at center, zoomAt(1.5, (340, 1040))
    with fade
    "I can't help but feel like they're babysitting me."
    "I clean up, wipe my makeup off, brush, all that good stuff."
    scene bg bedroom4
    show sasha date at center, zoomAt(1.5, (940, 1040))
    show scottie date at center, zoomAt(1.5, (340, 1040))
    with fade
    "Scottie and Sasha both put me to bed and roll me onto my side."
    show scottie shy
    scottie.say "She's really cute while sleepy."
    show sasha shy
    sasha.say "I'll say. Let's let her rest up. We'll check up on her in the morning."
    scene bg bedroom4 at dark, dark with dissolve
    "..."
    "They did, and I was alright. I had a headache, but it wasn't there for long."
    "I thought about the night before and felt nothing but warmth towards them."
    "I hope next time is that nice, too."
    if sasha.love.max < 100:
        $ sasha.love.max = 100
    if scottie.love.max < 100:
        $ scottie.love.max = 100
    call sleep from _call_sleep_74
    $ game.room = "bedroom4"
    return

label metal_harem_event_05:
    "I wake up, change into some clothes, and make some breakfast for myself."
    "The place is empty and it's pretty quiet. I like it."
    "I hear some birds outside while I make some eggs and toast."
    show sasha at right
    with easeinright
    "My nice silence is interrupted by Sasha nearly throwing the front door off of its hinges."
    show sasha at center
    show scottie annoyed at right
    with easeinright
    "She is followed by Scottie."
    scottie.say "...after the night club night AND dinner? Sasha, no, I-"
    show sasha at left5
    show scottie annoyed at right5
    with ease
    "Scottie sees me."
    show scottie surprised at right5, startle
    scottie.say "...will shut up! I will shut up. Sorry, WE will shut up."
    show sasha annoyed
    sasha.say "You know what, Scottie? I don't think so. You can't keep this from her while I'm around."
    show sasha normal
    sasha.say "[hero.name], I like you. I think you're cute and I want to date you."
    show scottie embarrassed
    "Scottie looks like he's about to sweat some bullets."
    show scottie blush
    scottie.say "I liked taking care of you on the night of the night club. And I liked dinner. I think I like you too. But I like Sasha, too."
    show scottie shy
    show sasha surprised
    "Sasha gapes at him."
    sasha.say "What? I-"
    show scottie blush
    scottie.say "I'm good at cooking and I think recent dates have been pretty exciting."
    scottie.say "Maybe what you need is another pair of hands in a relationship."
    show scottie shy
    show sasha normal
    bree.say "I- I... yes, I... I share these feelings."
    bree.say "I like both of you and I'd been starting to think about the two of you very often."
    bree.say "It's been hard to study because I was afraid I might have to pick."
    show sasha happy
    sasha.say "Oh, [hero.name]... you won't have to do that."
    show sasha normal
    sasha.say "I think Scottie is right."
    bree.say "Is it really okay with you two?"
    show scottie happy
    scottie.say "More than okay."
    sasha.say "I'm willing to try anything once and... I get a really good feeling from this."
    show sasha happy
    sasha.say "Maybe I really did just need another pair of hands."
    bree.say "I'm gonna cry... let's head over to the arcade and have a fun day before I start to sob."
    show sasha normal
    sasha.say "Of course, you pumpkin. Let's go get you all those tickets."
    scene bg arcade
    show sasha at left5
    show scottie at right5
    with fade
    "We run off to the arcade together and agree on a somewhat short outing to get the nerves out."
    "We play a bit of air hockey and Scottie easily plays both of us."
    show sasha surprised
    sasha.say "How?? HOW??"
    bree.say "It's the Chad energy, Sasha. The himbo energy."
    show sasha normal
    show scottie a joke
    scottie.say "Four arms can't compare to a pair of guns, dolls."
    show scottie b
    "He flexes."
    bree.say "Yummy."
    show sasha blush
    sasha.say "Meee-ow."
    "Scottie winks."
    show sasha normal
    show scottie normal
    with fade
    "We also find a few luck-based games, like one where you try and pick a lock with a random set of numbers to pick from."
    sasha.say "How did you manage... to get the top prize... on your first try?"
    bree.say "Sometimes I get lucky. I've gotten lucky twice today!"
    show sasha at center, zoomAt(1.5, (340, 1040))
    show scottie at center, zoomAt(1.5, (940, 1040))
    "I grab both of their arms and pull them close."
    bree.say "See?"
    show scottie shy
    show sasha blush
    "I spot both of them blush, even in the arcade's dim lighting."
    bree.say "Do you two want to check out the rest of the place really quickly for some last minute games?"
    bree.say "My nerves are all gone. We could... maybe...spend some time together in private?"
    show sasha joke
    sasha.say "Let's spend the tickets first. THEN we can... have other kinds of fun."
    show scottie blush
    show sasha normal
    scottie.say "I think they had a little picture frame. They take your photo, too."
    bree.say "That sounds so perfect... let's get it!"
    scene bg black with dissolve
    scene bg photostudio at center, zoomAt(1.5, (540, 1040)), dark
    show bree happy zorder 3 at center, zoomAt(1.5, (640, 1040))
    show sasha joke zorder 2 at center, zoomAt(1.5, (940, 1040))
    show scottie happy zorder 1 at center, zoomAt(1.5, (340, 1040))
    with screenshot
    play sound cameraclick
    "We get a little photo of us three taken and it's placed into the frame."
    scene bg kitchen
    show sasha at left5
    show scottie at right5
    with fade
    "We bring it home and set it on the kitchen bar, since we really like to cook together."
    sasha.say "Alright. We should probably... well, I should probably tell you two that I like it sort of rough."
    sasha.say "Not just on me. On both of you too."
    show scottie joke
    scottie.say "Aaaand that's another reason we got along pretty well."
    bree.say "I, uh, wasn't expecting anything this forward!"
    bree.say "I like... most things, though. As long as everyone is having fun."
    show sasha happy at center, zoomAt(1.5, (640, 1040))
    sasha.say "That's very cute, sweetie."
    show sasha casual normal at center, zoomAt(2.5, (640, 1040))
    "Sasha kisses my forehead."
    show sasha at center, zoomAt(1.5, (640, 1040))
    bree.say "Huh?"
    sasha.say "We'll break you in, don't worry honey."
    sasha.say "Well, [hero.name]? Do you want to come upstairs? Scottie?"
    show scottie blush
    scottie.say "Only if [hero.name] wants to."
    bree.say "In that case... It's time to try some stuff out. Let's go."
    show scottie shy
    show sasha happy
    sasha.say "Great! Oh, and I like toys, too."
    bree.say "What kind?"
    show sasha joke
    sasha.say "You'll see next time. I don't want to overwhelm you yet."
    sasha.say "Everything is sanitized properly, don't worry. I have a chemist friend that taught me how to do it a while ago."
    show sasha blush
    sasha.say "For... next time. I have to clean some stuff still. Buuut we're both too excited, so."
    scene bg bedroom3
    show sasha at left5
    show scottie at right5
    with fade
    "Scottie picks me up from behind."
    bree.say "Whaa!"
    scottie.say "Aaaand bed!"
    "He flings me."
    with vpunch
    "I land on the bed, bounce a little, and my blood pressure skyrockets."
    sasha.say "I won't torture you too much tonight with pleasure, but I'll promise to make you feel good."
    scottie.say "And, for the most important part, it's totally about you."
    "Sasha starts to pull at my pants and Scottie runs his hands up my shirt, unhooking my bra."
    "He massages my skin, making sure to cup my breasts and circle the nipples, hardening them and making me shiver."
    "Sasha, quick at work, pulls my pants and panties down and starts to rub at my clit."
    "I squirm a bit under their touch, overwhelmed by their warm hands."
    sasha.say "Squirm a little more, I promise it makes it feel better."
    "Scottie gets close to my ear and whispers to me."
    scottie.say "Do you want me to hold you down a bit?"
    "I exhale and nod to him. I'm horny and just want his hands on me more."
    "Scottie straddles a little above my chest and holds my hands above my head."
    "His bulge is in front of my face... I can't... handle seeing the twitching through the cloth and Sasha's touching of me."

    "Sasha spreads my legs and sucks on my clit, moving her hand down to finger me instead."
    "The waves of warmth and pleasure are too much and I am pushed over the edge by the pressure from Scottie and Sasha's hands."
    "I whine out in my orgasm and squirm under Scottie and Sasha."
    "I hear them giggle and their grips soften on me. They both caress me instead and come closer to me and lay down with me."
    "We soon... fall asleep together."
    if sasha.love.max < 120:
        $ sasha.love.max = 120
    if scottie.love.max < 120:
        $ scottie.love.max = 120
    return

label metal_harem_event_06:
    "I wake up early to go do a little bit of groceries. I pick up some ice cream and some oranges and some other fruit."
    "I also add some sunscreen into the shopping cart."
    "It's swim day today, fellas."
    "I tell Scottie and Sasha to bring a towel down to the pool and their swimsuits."
    show bg kitchen with fade
    show sasha at left5
    show scottie at right5
    with easeinright
    "Sasha and Scottie arrive alongside me when I'm back from the store."
    bree.say "Hey you two darlings! Can you pretty please help me out with cutting fruit since you're both so ready to go?"
    sasha.say "Scottie will do it. I'll come help you into your swimsuit."
    bree.say "Oh! Sasha..."
    show sasha wink
    "She gives me a wink. Scottie pouts."
    scene bg bedroom3
    show sasha
    "Surprisingly enough, Sasha doesn't make any passes in the bedroom."
    "She just straightens my straps and helps me look my best."
    sasha.say "There you go. Killer."
    "I smooch her."
    bree.say "Thanks honey."
    show bg pool
    "We pull Scottie out with us and munch on the food in the shade."
    bree.say "Alright, you two. Go on and lay down. I'm going to sunscreen both of you."
    scottie.say "Wait, no, one or two of us will be in the sun."
    sasha.say "Yeah, we should get someone first."
    "They both look at me."
    "Wait, no not again."
    bree.say "Haha, why don't we get Scottie first?"
    sasha.say "Nice try! You're setting this up for us, so you get pampered first."
    "Sasha comes up to me and kisses me before putting some sunscreen on my back and hips."
    "Scottie cheats and puts some sunscreen on her shoulders."
    scottie.say "I will be the honorable sacrifice and offer myself to you two."
    "He puts one hand on each of our backs and rubs the sunscreen in."
    bree.say "Big hands."
    scottie.say "Big feet, too. You know what th-"
    sasha.say "I never want to hear that joke again!"
    "I understood what he meant."
    bree.say "Could you put a little more pressure on my back? A mini massage?"
    "Scottie grunts and presses down on my shoulders."
    "Mmm."
    scottie.say "Oh! Your back popped."
    bree.say "Yeahhhh... I feel betterrrrr..."
    "He turns some of his attention to Sasha right after he finishes quickly rubbing me down."
    "Sasha mumbles non-words while Scottie spreads the sunscreen across her skin."
    "I dump some sunscreen into my hands and approach Scottie as he also finishes with Sasha."
    "I lead him into sitting down and straddle his lap, rubbing the cream into his chest and arms."
    "His swim shorts do not protect me from feeling any of his bulge."
    "He's clearly very excited."
    scottie.say "Mm, I'm not letting you go."
    "Scottie holds onto my waist and starts to grind his hips against mine."
    bree.say "Do you want me that badly?"
    scottie.say "Mmm-hmmm."
    "I push him back into the chair. He lays down."
    bree.say "Hmm... how do I do this..."
    bree.say "I know."
    "I pull Scottie's swim shorts down and let his cock spring up."
    bree.say "Sasha... come sit."
    "Sasha cock an eyebrow at me."
    sasha.say "I'll play along, [hero.name]. This'll be entertaining."

    "Sasha envelops Scottie's cock and starts to work her way down to sit on it."
    "Scottie's head rolls back and he exhales sharply."
    "I straddle his face while he tries to get his bearings together."
    "I face Sasha, who then holds onto me for support instead of Scottie's hips."
    "Her hands run up and down my body, stopping to rub my tits and squeeze my nipples."
    "I pull her close to me while Scottie's hips buck into her, and move her mouth over my nipples."
    "Her tongue obediently circles one and she moves to kiss the other."
    bree.say "Mm, Sasha, good girl..."
    "I pat Scottie on his side."
    bree.say "Scottie, I hardly feel your tongue... you don't want me to climb off, do you?"
    "I hear a muffled noise that sounds like a ‘no' and I grind into his face."
    "The ‘no' turns into a few moans while Sasha adds to them by bouncing on him."
    "Sasha keeps stimulating me with Scottie and she starts to feel herself up, too."
    "Scottie's hips move faster and his mouth's movements get messier and messier."
    "My breathing gets faster and I feel Scottie's hot breath, lungs trying to keep up with the two of us on top of him."
    "Sasha nips at me, asking for some attention, and I give it to her."
    "I cup her face with my hands and kiss her, parting her lips and entwining my tongue with hers."
    "She starts to moan and I swallow up the noises she makes."
    "They're for me now."
    "Scottie notices Sasha's orgasm and he slows a little, kindly, to not finish before me."
    "Sasha must have taught him well when they were together."
    "Scottie grabs my ass and pulls me, putting more pressure on his face, letting him put more pressure on my clit with his mouth."
    "Sasha can't keep her hands off of me, and soon it becomes too much for me."
    "I whine and cry out, cumming on Scottie's tongue."
    "He licks up my cum and kisses my lower lips."
    bree.say "Scottie... did Sasha get your cum?"
    "I move off of Scottie's face."
    "He shakes his head slowly."
    "I look at his chest, his hips, his cock... and it's still hard."
    "I straddle his hips and sit on it with ease, and Scottie tries to sit up."
    "Sasha pushes him back down and kneels next to him and kisses his arms and begins to move around his upper body."
    "Carefully, I put one hand on Scottie's hip and one on his thigh and I slam my hips down on him."
    "Scottie can't take two girls on him for much longer and he bursts inside of me."
    bree.say "Good boy! Was that so hard?"
    "I wink."
    scottie.say "Huff... haaa... [hero.name]... dastardly..."
    sasha.say "I never thought you had it in you, [hero.name]..."
    bree.say "I surprised myself, don't worry."
    "I giggle."
    "We don't swim after all. We're too tired, but it was a nice afternoon regardless."
    if sasha.love.max < 140:
        $ sasha.love.max = 140
    if scottie.love.max < 140:
        $ scottie.love.max = 140
    return

label metal_harem_event_07:
    "Scottie calls us really early today."
    "On the phone, Scottie sounds a little muffled."
    scottie.say "Hey ladies! You're both getting spoiled today. I have a few plans. They're... mostly surprises."
    scottie.say "It's nothing big, but I just want to spend some time with my two honies today."
    bree.say "I'll let Sasha know! Are you going to come get us or should we meet you somewhere?"
    scottie.say "Meet me at the mall!"
    "Scottie hangs up."
    "Hmm. Sounds fun!"
    "I let Sasha know with a quick call and tell her to be ready sort of soon."
    scene bg livingroom with fade
    "I wait around for Sasha in the living room."
    show sasha at center, zoomAt(1.25, (640, 880)) with easeinright
    "She eventually comes out of her room after enough prodding from me."
    bree.say "Finally!"
    show sasha shout
    sasha.say "We can't always look perfect, you know!"
    show sasha normal
    bree.say "Alpaca! Let's go meet up with Scottie, yeah?"
    show sasha shout
    sasha.say "Yeah, let's just hurry up. I know I've made us late."
    scene bg mall1
    show sasha at left5
    show scottie at right5
    with fade
    "Scottie waves at us from the front of the florist's store in the mall."
    show scottie angry
    scottie.say "I was hoping you'd get here soon. You two are beyond late!"
    show scottie annoyed
    bree.say "It's Sasha's fault. It's totally her fault. She took twelve years to get ready!"
    show sasha joke
    sasha.say "That's! That's not entirely true!"
    show sasha normal
    show scottie happy
    scottie.say "Shut up and let's go pick some flowers for you two. What colors do you want?"
    show bg flowershop
    show scottie normal
    show sasha shout
    with fade
    sasha.say "I want black ones..."
    show sasha normal
    bree.say "Goth tidy girlfriend speaks in the only way she knows how!"
    bree.say "Jokes aside... I want the orange ones, I think."
    show scottie annoyed
    scottie.say "I didn't expect the black pick, I'm gonna level with you."
    scottie.say "I really expected blue or purple."
    show sasha happy
    sasha.say "The heart wants what the heart wants."
    show sasha normal
    bree.say "Sometimes I'm surprised you don't sleep upside down in a coffin."
    "Scottie asks for the flowers we liked and gives us each a little bouquet."
    bree.say "Thank you, Scottie, I love them."
    show sasha shout
    sasha.say "A fitting tribute to your queen, Scottie. I shall accept them."
    show sasha normal
    show scottie happy
    scottie.say "Anything for my two goblins. It's nice to have one of you on each side of me."
    scottie.say "Feels sort of like one of those really bad pornos, but there's more feeling here."
    show scottie normal
    bree.say "I mean... I'd hope so, right?"
    show sasha whining
    sasha.say "You say that shit one more time and I won't talk to you for a week."
    sasha.say "I'm not some cheap porn whore."
    show sasha annoyed
    "Sasha pouts. I think she's joking?"
    "I think?"
    show scottie happy
    scottie.say "Good, because we're going to the funny little bakery near here and we're getting some of that good stuff."
    show scottie normal
    show sasha stuned
    "Sasha stops a moment and lights up."
    show sasha surprised
    sasha.say "Th-the yummy one with the little fruit tarts?"
    show sasha stuned
    show scottie happy
    scottie.say "You think I didn't remember your dumb tastes?"
    show scottie normal
    show sasha annoyed blush
    "Sasha pouts again, but she's blushing while she does it."
    show sasha whining
    sasha.say "Maybe."
    show sasha annoyed
    show scottie happy
    scottie.say "What about you, [hero.name]?"
    show scottie normal
    bree.say "I uh... I like fruity stuff. I also really like dry stuff for coffee and tea."
    show scottie happy
    scottie.say "I guess we'll pick some up and head back to the adobe."
    show scottie normal
    show sasha stuned
    bree.say "The abode. ABODE."
    show sasha surprised
    sasha.say "Did you read a dictionary upside down?"
    show sasha stuned
    show scottie angry
    scottie.say "Sometimes the himbo tries, ok? Be thankful and shut up."
    show sasha normal -blush
    show scottie normal
    show bg bakery
    with fade
    "We stop by the bakery and we each get a few pieces of bread."
    "I pick up a loaf of bread with thick slices. Might make for really good toast."
    "We wait in line and pay and leave right after."
    show bg mall1
    show scottie happy
    with fade
    scottie.say "We have one more stop."
    scottie.say "Sometimes people get bored of the same thing... so we're going to a sex shop."
    show scottie normal
    show sasha shout
    sasha.say "Oh, good. I forgot to tell both of you that I like toys a lot. At least, I think I forgot."
    show sasha normal
    bree.say "No, you totally told us. At least you told me. After the arcade."
    show sasha shout
    sasha.say "Right, right. I remember. It's because we didn't use any that I forgot."
    sasha.say "But that changes... soon..."
    show sasha normal
    scottie.say "Scottie is gonna spoil himself this time a little with stuff he's gonna use on both of you."
    show scottie normal
    bree.say "Why are you talking in third person?"
    show scottie happy
    scottie.say "We'll be quick."
    show scottie normal
    show bg sexshop
    with fade
    "Scottie buys some... vibrators, I think? Sasha also gets a new strap-on."
    "I'm not really familiar with advanced sex items so I let them have their fun."
    "..."
    play sound "sd/SFX/vehicles/car_door.ogg"
    scene bg street at center, zoomAt(1.25, (640, 530)), dark
    show car_inside_sit at center, zoomAt(1.5, (940, 1080))
    show sasha a casual at flip, center, zoomAt(2.0, (640, 1340))
    with fade
    "Once in the vehicle, Sasha unboxes one of the little vibrator things."
    show sasha a casual shout
    sasha.say "Put this in, [hero.name]."
    show sasha normal
    "In. In? Me?"
    bree.say "What?"
    show sasha shout
    sasha.say "I'll even lube it up for you!"
    show sasha normal
    bree.say "How do I use it?"
    show sasha shout
    sasha.say "It just vibrates... and we can connect to it with an app on the phone."
    sasha.say "It's just to get you started a little before we have some fun tonight."
    show sasha normal
    "While the car moves, Sasha opens a little bottle of lube and rubs it over the toy."
    "She moves my clothing aside and fucks my entrance with it a little to get me we and ready, and then slips it in."
    "She messes with her phone, and then I feel the toy vibrate."
    bree.say "Hnnn... that's... good..."
    "It's not long before we get back home."
    "My legs feel like jelly when I try to climb out of the car."
    "Sasha takes my things and Scottie picks me up and carries me off to my room."
    scene bg bedroom4
    show sasha at right5
    show scottie at left5
    with vpunch
    "Scottie tosses me onto the bed and Sasha comes up with the strap on already... well, on."
    show sasha shout
    sasha.say "Could you roll her over?"
    show sasha normal
    "I roll onto my stomach on my own."
    show sasha shout blush
    sasha.say "Oh, even better. Good girl."
    show sasha normal
    bree.say "Hnn... I'm... needy, hurry up!"
    show scottie happy naked with dissolve
    scottie.say "Mm, you don't have to tell me more than once."
    scene bg black
    show metal harem doggy vibrator off nosasha
    with fade
    "Scottie kneels in front of me. I'm laying down, so I'm at about his crotch level."
    "He wastes no time in putting his hand through my hair and pulling my face onto his bulge."
    "He grinds it against my face."
    "Sasha moves my knees apart and rubs her lubed up strap on against my holes."
    play sfx1 "sd/moans/bree/bree_moans_pained_low.ogg" loop
    show metal harem doggy strapanal -nosasha at stepback(speed=0.1, h=-10, v=0)
    "She pushes into my ass and fucks me gently to get me used to her toy."
    "Scottie rubs his tip on my lips and I take it in gingerly."
    play sfx1 "sd/moans/bree/bree_moans_blowjob_low.ogg" loop
    show metal harem doggy mouth at stepback(speed=0.1, h=10, v=0)
    "He groans and slowly pushes in."
    "I feel delicate, here."
    show metal harem doggy at stepback(speed=0.1, h=-10, v=0)
    "They're gentle. It's so different than what they're usually like."
    show metal harem doggy at stepback(speed=0.05, h=10, v=0)
    "I rock my body back and forth between them."
    scottie.say "Ohh, [hero.name], you're very good at this..."
    play sfx1 "sd/moans/bree/bree_moans_blowjob_medium.ogg" loop
    show metal harem doggy at stepback(speed=0.5, h=-10, v=0)
    "Sasha rubs my clit."
    show metal harem doggy at stepback(speed=0.05, h=10, v=0)
    "It doesn't take a long time before I hear her moan."
    show metal harem doggy sashaahegao
    sasha.say "It's hot seeing you so vulnerable... I can't help but-"
    play sfx1 "sd/moans/bree/bree_moans_blowjob_high.ogg" loop
    show metal harem doggy at stepback(speed=0.05, h=-10, v=0)
    "Sasha gasps."
    show metal harem doggy sashahappy sashapleasure
    sasha.say "...touch both of us to the thought."
    play sfx2 "sd/moans/sasha/sasha_moans_discreet_low.ogg" loop
    show metal harem doggy at stepback(speed=0.05, h=10, v=0)
    "Scottie can't handle it and he forces himself into my throat. He thrusts a few times before I feel his cock twitch."
    show metal harem doggy creampie breepleasure with hpunch
    "Hot cream fills my throat and I struggle to swallow it all."
    with hpunch
    "Sasha's hand moves faster and she bucks her hips to fuck me with the strap on."
    play sfx1 "sd/moans/bree/bree_moans_gagged.ogg" loop
    play sfx2 "sd/moans/sasha/sasha_moans_discreet_medium.ogg" loop
    with hpunch
    "I raise my ass a little higher towards her, fully presenting myself so she can help me cum."
    with hpunch
    "She, her toy, and the vibrator together are too much for me for any length of time, and I cry out and shiver during my orgasm."
    show metal harem doggy -creampie breepleasure
    scottie.say "Huff... you got a real good mouth..."
    play sfx2 "sd/moans/sasha/sasha_panting.ogg" loop
    play sfx1 "sd/moans/bree/bree_moans_discreet_low.ogg" loop
    show metal harem doggy out
    scottie.say "I'm... really tired... I'm gonna stay here with you two..."
    stop sfx2
    sasha.say "What a workout... you're so easy to make orgasm sometimes, [hero.name]. Did you like the toys?"
    stop sfx1
    bree.say "I see why you like them so much."
    scene bg bedroom4
    show sasha naked strapon at right5
    show scottie naked at left5
    with fade
    "I politely pull away from her strap on and sit up."
    bree.say "I get sleepy after I cum..."
    show sasha happy
    sasha.say "Let's put you to bed, then."
    show sasha normal
    "And so she did."
    if sasha.love.max < 160:
        $ sasha.love.max = 160
    if scottie.love.max < 160:
        $ scottie.love.max = 160
    call sleep from _call_sleep_10
    return

label metal_harem_event_08:
    if sasha.love.max < 180:
        $ sasha.love.max = 180
    if scottie.love.max < 180:
        $ scottie.love.max = 180
    "I feel tired... how long have I been at this?"
    "I go ahead and text Sasha and Scottie in our group text and let them know I'm not feeling well from some stress."
    "I'm usually pretty good at running well on insufficient sleep, but some exams are coming up and I don't feel great about them."
    "I wonder how I can relieve stress. Maybe a jog? A yoga class? Dance class? Maybe I'll check online later."
    "For now, though, I had to do a little more studying."
    "About an hour later, Scottie and Sasha show up in the library waving at me."
    show sasha talkative at left
    show scottie at right
    with fade
    sasha.say "Hey! We were getting worried... you work really hard... maybe you need a breather."
    show sasha normal
    show scottie talkative
    scottie.say "We can always help out with that, too."
    scottie.say "Food, takeout, a walk, you name it."
    show scottie normal
    show sasha talkative
    sasha.say "We can always have time for us too, you know."
    show sasha normal
    bree.say "Thank you... that means a lot to me. I've been so stressed over exams..."
    bree.say "...and I haven't wanted to disappoint any of you in our little trio."
    show sasha talkative
    sasha.say "The important thing while you're chasing an education is to try your best."
    sasha.say "Can you do that while you're tired?"
    show sasha normal
    show scottie talkative
    scottie.say "You don't have to accept, but it's probably best for you to take a night off for once."
    scottie.say "You've been here daily for a bit. Let's take your mind off of this and have a free night."
    show scottie normal
    bree.say "I think you're both right. Will it be a fun night?"
    show sasha talkative
    sasha.say "We'll spoil you again, [hero.name]."
    show sasha normal
    hide sasha
    hide scottie
    scene bg livingroom
    show sasha at left5
    show scottie at right5
    with fade
    "We make it back quickly. Scottie and Sasha both seem to be in a bit of a rush."
    "I'm actually really flattered."
    show sasha talkative
    sasha.say "We had a little snack pack ready for you... but we forgot to take it."
    sasha.say "Have some now while we set some stuff up?"
    show sasha normal
    bree.say "Alright. I'll have some of the classic fruit treats we like so much."
    bree.say "Let me know when I can come up!"
    "But I think they were too distracted to hear me."
    "I munch quietly and get a little nap in, or so I think. It couldn't have been more than ten minutes."
    "The lights are turned off and someone taps on my shoulder."
    "It's Sasha, but Scottie is down here too."
    "They both take my hands and lead me upstairs."
    hide sasha
    hide scottie
    scene bg bedroom3
    show sasha at left4
    show scottie at center, zoomAt(1.0, (840, 740))
    with fade
    "There's a dim light in Sasha's bedroom."
    "Some candles are around the bed. There's little petals and Sasha's room smells really nice."
    "I think they just cleaned her room up, ha ha."
    "And dolled it up a bit, of course."
    show scottie talkative
    scottie.say "It's not the... most thought out thing in the world, but we tried!"
    show scottie normal
    show sasha talkative
    sasha.say "Yeah. We're taking care of you tonight and we're gonna make you forget about school for a bit."
    show sasha normal
    bree.say "Alright... I'll let myself relax. But only for you two!"
    show sasha talkative
    sasha.say "That's what we like to hear, [hero.name]."
    sasha.say "Come on and get on the bed."
    show sasha normal
    "I obey Sasha and lay down."
    show sasha talkative
    sasha.say "Close your eyes."
    show sasha normal
    bree.say "Can't you just blindfold me? I'm not very good at just closing my eyes."
    show sasha joke
    sasha.say "Really? REALLY? Fine. Scottie, do you know where...?"
    show sasha shy
    show scottie talkative
    scottie.say "Yeah, one second."
    show scottie talkative at center, traveling(2.0, 0.5, (740, 1380))
    pause 1.0
    scene bg black with wipedown
    "Some soft cloth covers my closed eyes."
    scottie.say "Comfy?"
    bree.say "Mhmm..."
    play sfx1 "sd/moans/bree/bree_moans_happy_low.ogg" loop
    play sfx2 "sd/moans/sasha/sasha_moans_discreet_low.ogg" loop
    "I feel the bed dip to one of my sides and it feels like Scottie climbs on."
    "Scottie's rough hands pick me up and he shimmies underneath me."
    show metal harem reverse cowgirl blindfold at center, zoomAt(2.0, (1200, 1040)) with fade
    "He lays down and pulls me back onto his chest."
    "I hear some rustling from the other side of the room alongside some metal clinking."
    "Some buzzing also makes its way to my ears, but it's very short lived."
    "I feel another dip in the bed. They're both very quiet."
    show metal harem reverse cowgirl blindfold at center, traveling(1.0, 5.0,(640, 720))
    "Scottie reaches forward and rubs my clit and Sasha softly starts to slip into my pussy with her strap on."
    "I think she has the vibrator in her."
    "Scottie pumps his dick with lube in his hands, probably, and starts to poke at my ass."
    "He eventually finds my hole with some help from Sasha."
    "I hear them quietly whisper a few insults at each other and they count down very, very quietly from three."
    play sfx1 "sd/moans/bree/bree_moans_happy_medium.ogg" loop
    "They both push the full girth of their real and/or fake members into me."
    "I feel very, very full and I can't keep the same quiet they are trying to keep."
    "I moan and melt."
    stop sfx1
    show metal harem reverse cowgirl breehurt
    bree.say "Guys... huff... this feels really good, but you don't have to stop making noise."
    play sfx1 "sd/moans/bree/bree_moans_happy_medium.ogg" loop
    sasha.say "It's a relaxing night to get you de-stressed, [hero.name]."
    play sfx2 "sd/moans/sasha/sasha_moans_discreet_low.ogg" loop
    scottie.say "I'd think about us instead of all that stress you have floating around. Just for a bit."
    stop sfx1
    show metal harem reverse cowgirl breehappy
    bree.say "Mmmm..."
    bree.say "I don't think we should take too lon-"
    play sfx1 "sd/moans/bree/bree_moans_happy_medium.ogg" loop
    "Scottie's free hand shushes me and keeps my mouth quiet."
    scottie.say "Shh, melt into us, [hero.name]. You're ours for the night."
    "I close my eyes underneath blindfold and think I understand how to close my eyes and sink into something like this now."
    "Sasha gets a little more forceful and pulls my legs up, putting my knees over her shoulders."
    play sfx2 "sd/moans/sasha/sasha_moans_discreet_medium.ogg" loop
    play sfx1 "sd/moans/bree/bree_moans_happy_high.ogg" loop
    show metal harem reverse cowgirl sashahappy
    "She thrusts into me when Scottie pulls away and I never get a moment of peace."
    "Scottie's lips kiss my neck and he nips and sucks at it."
    "He moves to my ears and Sasha caresses my thighs."
    "My mind focuses on their touch, their breathing, their heat..."
    "Exams aren't even on my mind anymore."
    "Nothing is really on my mind except Sasha and Scottie..."
    "They play my body like an instrument, toying with me and making me moan for them."
    play sfx1 "sd/moans/bree/bree_moans_happy_orgasm_1.ogg"
    queue sfx1 "sd/moans/bree/bree_moans_discreet_low.ogg" loop
    play sfx2 "sd/moans/sasha/sasha_panting.ogg" loop
    show metal harem reverse cowgirl breeahegao with vpunch
    "I feel the heat building up in me."
    with vpunch
    "It bubbles slowly but quickly boils over and I groan and hold onto them, trying not to topple the little tower of us."
    stop sfx1
    with vpunch
    bree.say "Okay... huff. Okay, okay... I've relaxed..."
    stop sfx2
    show metal harem reverse cowgirl breeahegao sashaahegao
    sasha.say "Nuh uh. It's not study time anymore. It's either nap time or shower time."
    bree.say "Cleaning off sounds nice..."
    scottie.say "Off you go, sweet slut. Unless you want us to go with you?"
    bree.say "Next time... I need to... to unwind a tiny bit... bubble bath..."
    "And so I rest up a little more and refresh a lot."
    "Thanks to them."
    scene bg bedroom4
    $ sasha.sexperience += 1
    $ scottie.sexperience += 1
    return

label metal_harem_event_09_a:
    show sasha shy with easeinright
    "Sasha blasts into my room."
    show sasha shout
    sasha.say "Allllright, [hero.name]. It's MY TURN to make a fun little event."
    show sasha shy
    "Oh no."
    show sasha happy
    sasha.say "We're doing strrrrip poker!"
    show sasha shy
    "Oh NO."
    show sasha shout
    sasha.say "You've got until tonight to practice your poker face. Bye!"
    hide sasha with easeoutright
    "She leaves as quickly as she came in."
    "Oh no."
    "Well. Okay. I can do this, I can do this."
    "I can't lie to save my life."
    "I can just hope that Scottie saves me by being worse than I am, I guess."
    return

label metal_harem_event_09_b:
    show sasha at right5
    show scottie at left5
    "Night comes."
    "Sasha probably is coming for both of us during this game."
    "I get settled down with the two. There's a couple of things I spot around the living room."
    "I see... toys. Lube. Cards."
    "Sasha is already shuffling cards when Scottie and I settle into our seats around the little coffee table."
    show sasha talkative
    sasha.say "We're going to put the toys we got to use again. I can't wait!"
    show sasha normal
    show scottie talkative
    scottie.say "Maybe taking you shopping was a terrible idea."
    show scottie normal
    bree.say "Scottie. I'm afraid."
    show scottie talkative
    scottie.say "You have no idea what you're in for. This bitch is insane."
    show scottie normal
    bree.say "Is your poker face worse than mine?"
    show scottie talkative
    scottie.say "Oh... sucks to be you, doesn't it?"
    show scottie joke
    "I gulp."
    "Sasha deals cards."
    bree.say "Is there a specific type of poker that this is?"
    show scottie normal
    show sasha embarrassed
    "Sasha and Scottie look at each other and smirk."
    show scottie talkative
    scottie.say "Yeah. Poker."
    show scottie normal
    bree.say "I mean. Ask stupid questions, right?"
    play sfx1 "sd/moans/bree/bree_laughs_medium_1.ogg"
    with vpunch
    "I laugh."
    show sasha happy at startle
    show scottie happy at startle
    "They laugh after trying to understand my Scottie-level question."
    show sasha talkative
    sasha.say "Alright, this is how it works. The worst hand takes off an article of clothing."
    sasha.say "In the case of junk or a one pair, the winner of the round picks who strips off a piece of covering."
    show sasha normal
    bree.say "I have a feeling you're going to be fully clothed by the end of this."
    show sasha talkative
    sasha.say "If someone folds, they have to leave the premises and never return."
    show sasha normal
    bree.say "Wait, what if we up the ante?"
    show sasha talkative
    sasha.say "Huh? How?"
    show sasha normal
    bree.say "We can bet a clothing amount to take off, like... two or three pieces or something."
    show scottie talkative
    scottie.say "No, the witch Sasha would raise it instantly and make you strip."
    show scottie normal
    show sasha talkative
    sasha.say "I mean..."
    show sasha normal
    bree.say "Point taken!"
    show sasha talkative
    sasha.say "Alright. Let's start?"
    show sasha normal
    bree.say "Hoo... okay. Calm down, calm down."
    "Sasha wins the first round. Scottie has a worse hand than I do."
    "Sasha wins the second round. And the third. And the fourth."
    "Scottie wins the fifth... the sixth..."
    "And the seventh..."
    "I don't win any."
    "This game is rigged."
    "I'm totally naked by the end and Sasha's fully clothed. Scottie and I had junk for some rounds..."
    "But he's not naked yet."
    show sasha talkative
    sasha.say "We'll have Scottie take your place? If he's okay with sacrificing himself for you, that is."
    sasha.say "I'm suuure he wouldn't mind, [hero.name]."
    show sasha normal
    show scottie talkative
    scottie.say "I sure do. A stroke of bad luck for her is a stroke to my cock for me."
    show scottie normal
    "Sasha brushes the cards off of the table and sits me down on it."
    show sasha talkative
    sasha.say "This is a tough little coffee table so this is exactly where I'm going to get off on you."
    scene bg black
    show metal harem missionary sasha livingroom
    with fade
    "Sasha throws her pants and panties off and sits on my face."
    play sfx1 "sd/moans/bree/bree_moans_blowjob_low.ogg" loop
    play sfx2 "sd/moans/sasha/sasha_moans_light_low.ogg" loop
    show metal harem missionary breelick
    "I know my job, so I lick her."
    "I lap at her and try to get at her sweet taste."
    show metal harem missionary sashahurt
    "Every little squirm from her lets me know I'm pleasing her like I should be."
    "She's so hot..."
    "And she's so wet, too."
    "Her fluid and my saliva mix and it covers my chin and neck in not much time."
    show metal harem missionary scottie with dissolve
    "Scottie spreads my legs and starts fucking me."
    show metal harem missionary vaginal at stepback(speed=0.1, h=10, v=-5)
    "Seeing me naked for so long with Sasha on my face must have pent him up."
    show metal harem missionary near at stepback(speed=0.1, h=10, v=-5)
    "He slams against my hips and the tablet doesn't even move."
    "Sasha grinds against my face."
    stop sfx2
    show metal harem missionary far sashapleasure at stepback(speed=0.1, h=10, v=-5)
    sasha.say "Why haven't I been riding your face more? You're perfect for this."
    sasha.say "Scottie... why didn't you tell me she was good with her tongue?"
    show metal harem missionary near at stepback(speed=0.1, h=10, v=-5)
    scottie.say "I wanted it to myself!"
    sasha.say "Ugh, knucklehead."
    show metal harem missionary far sashawide at stepback(speed=0.1, h=10, v=-5)
    sasha.say "Mmmf, keep going, keep going, I'm already close, [hero.name]."
    show metal harem missionary near at stepback(speed=0.1, h=10, v=-5)
    scottie.say "This pussy doesn't quit either."
    scottie.say "[hero.name] was made to be fucked."
    show metal harem missionary far at stepback(speed=0.1, h=10, v=-5)
    bree.say "Mmmf!"
    sasha.say "She can't say anything about it, her lips are a little busy kissing mine."
    play sfx2 "sd/moans/sasha/sasha_moans_light_low.ogg" loop
    "Sasha cackles at her terrible crack."
    "I suck on Sasha's clit to try and interrupt her and make her cum."
    stop sfx2
    show metal harem missionary near sashapleasure sashaahegao at stepback(speed=0.1, h=10, v=-5)
    sasha.say "Hahah- ah! Oh, gosh, wait, [hero.name]!"
    play sfx2 "sd/moans/sasha/sasha_moans_light_medium.ogg" loop
    "I twirl my tongue around it."
    "Sasha almost falls over – she barely manages to hold onto my shoulder and the edge of the table."
    "She moans out loudly and shudders above me, dousing me in more wetness."
    show metal harem missionary far sashahappy sashapleasure at stepback(speed=0.1, h=10, v=-5)
    bree.say "Mmmf, hmmm?"
    stop sfx2
    sasha.say "You make a good point."
    play sfx2 "sd/moans/sasha/sasha_moans_light_medium.ogg" loop
    "Sasha climbs off of me and sits behind me, propping me up some."
    show metal harem missionary near at stepback(speed=0.1, h=10, v=-5)
    "She pinches and rubs my breasts, nipples, and clit while Scottie keeps pumping into me."
    "I feel like I'm close from the over stimulation."
    show metal harem missionary far at stepback(speed=0.1, h=10, v=-5)
    "Scottie starts to thrust a little erratically, and I know exactly what that means."
    "I pull him in with my legs and he thrusts in deeply."
    show metal harem missionary near at stepback(speed=0.1, h=10, v=-5)
    "He starts hitting exactly where I like it and I let him know before he loses it."
    stop sfx1
    show metal harem missionary breeopen
    bree.say "Scottie! Ah! There! More, please! Please!"
    scottie.say "Your wish is my command!"
    play sfx1 "sd/moans/bree/bree_moans_discreet_high.ogg" loop
    show metal harem missionary far at stepback(speed=0.1, h=10, v=-5)
    "He keeps the same angle and momentum and hits the sweet spot over and over again."
    "Each thrust is a wave crashing over me."
    show metal harem missionary near at stepback(speed=0.1, h=10, v=-5)
    "Again, again, and again."
    "Sasha's hands send jolts up and down my naked body."
    show metal harem missionary far at stepback(speed=0.1, h=10, v=-5)
    "She leans in to suck on neck, intending to give me a hickie."
    sasha.say "Mmm, [hero.name]... don't... mind me, I'm making sure you remember how mine you are."
    show metal harem missionary near at stepback(speed=0.1, h=10, v=-5)
    "Out of breath, Scottie speaks up."
    scottie.say "Give her one from me too, Sasha."
    stop sfx2
    show metal harem missionary far at stepback(speed=0.1, h=10, v=-5)
    sasha.say "Make her cum and you can come give her a few yourself!"
    play sfx2 "sd/moans/sasha/sasha_moans_light_high.ogg" loop
    "But they didn't have to wait at all."
    play sfx1 "sd/moans/bree/bree_moans_discreet_orgasm_1.ogg"
    play sfx2 "sd/moans/sasha/sasha_moans_light_orgasm.ogg"
    queue sfx1 "sd/moans/bree/bree_moans_discreet_low.ogg" loop
    queue sfx2 "sd/moans/sasha/sasha_panting.ogg" loop
    show metal harem missionary near breeahegao with hpunch
    "Scottie had hit one too many times and the waves pulled me under, into bliss."
    show metal harem missionary cum with hpunch
    "Scottie follows me closely and erupts inside of me, filling and claiming my pussy."
    show metal harem missionary far out with hpunch
    "He doesn't waste much time and pulls out, panting."
    "Kneeling next to me, he sucks on me and gives me a couple of hickies with Sasha."
    stop sfx1
    stop sfx2
    scottie.say "And we get to do this shit every night if we wanted to."
    sasha.say "Shush, you're ruining the moment."
    bree.say "He's right though!"
    "And we're gonna keep fucking. Maybe not every night, but... I look forward to it."
    "As long as they're both there."
    scene bg bedroom4 with fade
    if sasha.love.max < 200:
        $ sasha.love.max = 200
    if scottie.love.max < 200:
        $ scottie.love.max = 200
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
