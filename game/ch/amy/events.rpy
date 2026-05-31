init python:
    Event(**{
    "name": "amy_teaser",
    "label": "amy_teaser",
    "priority": 500,
    "duration": 1,
    "conditions": [
        MinDaysPlayed(33),
        IsDayOfWeek("135"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("electronic"),
            MinStat("knowledge", 50),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "amy_teaser_kiss",
    "label": "amy_teaser_kiss",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDayOfWeek("24"),
        Or(
            And(
                "'fafow' not in DLCS",
                IsDone("amy_teaser")
                ),
            And(
                "'fafow' in DLCS",
                IsDone("amy_event_01"),
                PersonTarget("amy",
                    MinStat("love", 40),
                    IsFlag("amydelay", False)
                    )
                )
            ),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("electronic"),
            MinStat("charm", 50),
            ),
        GameTarget(
            IsFlag("amyStart", True),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "amy_teaser_sex",
    "label": "amy_teaser_sex",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDayOfWeek("135"),
        Or(
            And(
                "'fafow' not in DLCS",
                IsDone("amy_teaser_kiss")
                ),
            And(
                "'fafow' in DLCS",
                IsDone("amy_event_04"),
                PersonTarget("amy",
                     MinStat("love", 100),
                     IsFlag("amydelay", False)
                     )
                )
            ),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("electronic"),
            MinStat("fitness", 50),
            ),
        GameTarget(
            IsFlag("amyStart", True),
            ),
        ],
    "do_once": True,
    })


label amy_teaser:
    show bg electronic
    "I happen to be in the mall and killing time, so I swing by the electronics store."
    "I'm not looking for anything in particular, but it's a pretty cool place to hang out."
    "There's usually something shiny and new on offer to check out too."
    "And today's no exception, apart from the fact it's not a new gadget that catches my eye."
    show amy work at right with dissolve
    "It's a new member of staff, specifically a female member of staff."
    "She's cute girl that, I think, looks to be of Chinese descent."
    show amy at left with move
    "And even better, she's clearly a goth, despite her uniform!"
    if "palla_event_10" in DONE:
        hide amy
        show shawn at center, zoomAt(1.5, (840, 1040)) with vpunch
        shawn.say "Hey, [hero.name]!"
        shawn.say "See anything that takes your fancy?!?"
        "I can't help jumping in surprise as Shawn pops up beside me."
        "He must have spotted me coming in and crept up on me."
        "And all the while I was checking out the hot new girl."
        mike.say "Ah..."
        mike.say "Shit, Shawn - you scared me to death!"
        show shawn happy at center with move
        "Shawn laughs off my concerns, shaking his head."
        "Then he nods towards the new girl, who's busy stacking shelves."
        shawn.say "Couldn't help but see you staring at Amy just now."
        shawn.say "Not that I can blame you, dude!"
        mike.say "Yeah..."
        mike.say "She's quite something, Shawn!"
        show shawn nice
        "Shawn nods, turning to look at Amy too."
        shawn.say "She just started a couple of days ago."
        shawn.say "She's still on her probation period."
        shawn.say "But she's a fast learner."
        shawn.say "And with me training her, she'll do great."
        mike.say "Whatever you say, Shawn."
        mike.say "I'm just going to browse around, okay?"
        hide shawn
        "Shawn nods again and walks off, leaving me alone."
        menu:
            "Flirt with Amy":
                show amy work
                "I try to look casual as I wait for Shawn to disappear."
                "I hurry over there, trying to look as casual as I can."
                mike.say "Ah..."
                mike.say "Hi there..."
                "At the sound of my voice, the Amy looks up from what she's doing."
                "I hear myself swallow as she does so and I get a closer look at her."
                "Because she's even hotter up close than she was across the store!"
                amy.say "Hey, man!"
                amy.say "Welcome to the store."
                amy.say "Is there anything I can help you with today?"
                "I must have heard that rehearsed line a hundred times before now."
                "But coming from her smiling lips, it sounds like the words of an angel!"
                mike.say "Erm..."
                mike.say "Not really, Amy..."
                mike.say "I just wanted to say hi and introduce myself."
                mike.say "I'm [hero.name]."
                "Amy seems to realise that I'm not here to buy anything."
                show amy work blush
                "And she changes gear accordingly, her smile becoming more genuine."
                "Which also means that she becomes that much cuter at the same time!"
                amy.say "Oh really?"
                amy.say "Nice to meet you, [hero.name]."
                if hero.charm >= 30 and hero.fitness >= 30 and hero.knowledge >= 30:
                    show amy work flirt
                    "Amy leans in a little closer."
                    amy.say "Actually, I'm kinda glad you came over here."
                    mike.say "Y...you are?"
                    amy.say "Yeah, because it means I didn't have to come over to you."
                    amy.say "I spotted you coming in just now and wanted to say hi."
                    amy.say "But Shawn's watching me like a hawk!"
                    "I roll my eyes, realising how full of crap Shawn actually is."
                    "And then I shake my head, trying to concentrate on Amy instead."
                    mike.say "Is he giving you a hard time?"
                    mike.say "Because I know that guy, and he can be a real prick!"
                    "Amy chuckles at this."
                    "And the sound is wonderfully naughty."
                    amy.say "Oh, he's not that bad."
                    amy.say "He just likes to pretend he's my boss."
                    amy.say "He's just been working here forever."
                    amy.say "So he kinda thinks he's in charge!"
                    amy.say "Anyway, forget about him."
                    amy.say "It's you I wanted to talk to..."
                    mike.say "You did?!?"
                    show amy
                    "Amy chuckles again, amused at my being caught out."
                    amy.say "Aw, [hero.name]!"
                    amy.say "You're funny and cute."
                    amy.say "I wonder what else you're good at?"
                    mike.say "I don't know, Amy."
                    mike.say "Maybe if we met up some time you might find out?"
                    "Amy nods and gives me a super cute smile."
                    amy.say "Maybe we'll do that, [hero.name]!"
                    "Amy and I exchange goodbyes."
                    hide amy with dissolve
                    "Then I stride out of the place, feeling like I'm walking on air."
                    show shawn angry at center, zoomAt(1.5, (640, 1040)) with vpunch
                    "But before I can make it out the door, Shawn pops up again."
                    "And he looks pretty pissed at me."
                    shawn.say "Hey, man!"
                    shawn.say "What do you think you're doing?!?"
                    "I take a step backwards from Shawn."
                    "He's getting in my face and I don't even know why."
                    mike.say "Whoa, Shawn - calm the hell down!"
                    mike.say "What did I do to make you so mad?"
                    "Shawn plants his hands on his hips."
                    "And he looks me dead in the eye."
                    shawn.say "Don't act the innocent with me, [hero.name]."
                    shawn.say "I saw you putting the moves on Amy just now!"
                    mike.say "What?!?"
                    mike.say "I was just talking to her, that's all!"
                    shawn.say "Bullshit - I saw you swapping numbers!"
                    shawn.say "You'd better back off, because I saw her first!"
                    menu:
                        "Don't back off":
                            "What does Shawn think he's doing?"
                            "He can't just decide that Amy belongs to him."
                            mike.say "Ah, grow up, Shawn."
                            mike.say "Amy's not something you can just call dibs on!"
                            mike.say "So if you want her, then you're going to have to fight for her!"
                            "Shawn's eyes narrow as he glares at me."
                            "And he nods his head grimly."
                            shawn.say "Okay, [hero.name]."
                            shawn.say "If that's the way you want it."
                            shawn.say "This means war!"
                            hide shawn with moveoutright
                            "With that, he turns and strides back into the store."
                            "All I can do is shake my head and walk away."
                            "But even as I do so, I'm sure Amy's going to be worth it."
                            "And I'm more than ready to fight for her myself!"
                            $ game.flags.amyStart = True
                        "Back off (Never meet Amy again)":
                            "Shawn sounds pretty childish right now."
                            "I mean, he can't just decide that Amy belongs to him."
                            "But I don't want her to see me arguing with him either."
                            "That was she might think I'm as big of a prick as him!"
                            mike.say "Whatever, Shawn, whatever."
                            mike.say "I came here to look at the stuff you're selling."
                            mike.say "Not to get into a pissing contest over a girl!"
                            "Shawn's eyes narrow as he glares at me."
                            "And he nods his head grimly."
                            shawn.say "You'd better mean that, [hero.name]."
                            shawn.say "Because I have a good feeling about Amy and me."
                            shawn.say "And I don't want you to screw it up for me!"
                            hide shawn with moveoutright
                            "With that, he turns and strides back into the store."
                            "All I can do is shake my head and walk away."
                            "Shawn's right, he doesn't need me to screw things up."
                            "Because he's more than likely going to do that himself."
                            "I don't know if I'll keep my promise to him or not."
                            "But I'm definitely going to keep an eye on Amy."
                else:
                    show amy work normal
                    amy.say "But if you're not looking for help, I have to get back to work!"
                    "The way Amy suddenly flips the conversation takes me by surprise."
                    "I thought we were getting somewhere, but she just closed me down!"
                    mike.say "O...okay...sorry!"
                    mike.say "I'll just...I'll just go somewhere else then?"
                    "Amy nods and smiles, then turns away to resume her work."
                    "All I can do is shuffle off, feeling utterly deflated."
                    "As I leave the store, I see Shawn watching me go."
                    "And he looks like he's pretty pleased with the way that just played out for me too."
            "Don't flirt with Amy (Never meet Amy again)":
                "More than once I try to pluck up the courage to go over there."
                "To just casually walk up the same aisle as Amy and strike up a conversation."
                "But every time I glance up, she seems to be busy with something else."
                "Either she's showing another customer where to find whatever they want."
                "Or else Shawn is hovering over her while she works."
                "In the end I just give up, and so I shuffle off, feeling utterly deflated."
    else:
        "I keep watching her, trying to look like I'm just browsing."
        "The geeky guy that works here is talking to her for a while."
        "I guess he's the one that's training her up to work in the store."
        "But eventually he wanders off to attend to something else."
        "Now the girl's alone, still stacking the shelves."
        "This would be the perfect chance to go over there and introduce myself."
        menu:
            "Flirt with the girl":
                "I hurry over there, trying to look as casual as I can."
                mike.say "Ah..."
                mike.say "Hi there..."
                "At the sound of my voice, the girl looks up from what she's doing."
                "I hear myself swallow as she does so and I get a closer look at her."
                "Because she's even hotter up close than she was across the store!"
                "Girl" "Hey, man!"
                "Girl" "Welcome to the store."
                "Girl" "Is there anything I can help you with today?"
                "I must have heard that rehearsed line a hundred times before now."
                "But coming from her smiling lips, it sounds like the words of an angel!"
                mike.say "Erm..."
                mike.say "Not really..."
                "I pause to glance down at her nametag."
                "And I try not to stare at her chest as I do so!"
                mike.say "Not really, Amy..."
                mike.say "I just wanted to say hi and introduce myself."
                mike.say "I'm [hero.name]."
                "Amy seems to realise that I'm not here to buy anything."
                show amy work blush
                "And she changes gear accordingly, her smile becoming more genuine."
                "Which also means that she becomes that much cuter at the same time!"
                amy.say "Oh really?"
                amy.say "Nice to meet you, [hero.name]."
                if hero.charm >= 30 and hero.fitness >= 30 and hero.knowledge >= 30:
                    show amy work flirt
                    "Amy leans in a little closer."
                    amy.say "Actually, I'm kinda glad you came over here."
                    mike.say "Y...you are?"
                    amy.say "Yeah, because it means I didn't have to come over to you."
                    amy.say "I spotted you coming in just now and wanted to say hi."
                    amy.say "But Shawn's watching me like a hawk!"
                    "I frown and glance over in the direction of the regular guy who works here."
                    mike.say "Your boss is giving you a hard time?"
                    "Amy chuckles at this."
                    "And the sound is wonderfully naughty."
                    amy.say "Oh, he's not my boss."
                    amy.say "He's just been working here forever."
                    amy.say "So he kinda thinks he's in charge!"
                    amy.say "Anyway, forget about him."
                    amy.say "It's you I wanted to talk to..."
                    mike.say "You did?!?"
                    show amy
                    "Amy chuckles again, amused at my being caught out."
                    amy.say "Aw, [hero.name]!"
                    amy.say "You're funny and cute."
                    amy.say "I wonder what else you're good at?"
                    mike.say "I don't know, Amy."
                    mike.say "Maybe if we met up some time you might find out?"
                    "Amy nods and gives me a super cute smile."
                    amy.say "Maybe we'll do that, [hero.name]!"
                    "Amy and I exchange goodbyes."
                    "And then I stride out of the place, feeling like I'm walking on air."
                    "Her male colleague glares at me on the way out."
                    "But who cares what that guy thinks."
                    "Especially after I got the hot new girl's number!"
                    $ game.flags.amyStart = True
                else:
                    show amy work normal
                    amy.say "But if you're not looking for help, I have to get back to work!"
                    "The way Amy suddenly flips the conversation takes me by surprise."
                    "I thought we were getting somewhere, but she just closed me down!"
                    mike.say "O...okay...sorry!"
                    mike.say "I'll just...I'll just go somewhere else then?"
                    "Amy nods and smiles, then turns away to resume her work."
                    "And all I can do is shuffle off, feeling utterly deflated."
            "Don't flirt with her (Never meet Amy again)":
                "More than once I try to pluck up the courage to go over there."
                "To just casually walk up the same aisle as the new girl and strike up a conversation."
                "But every time I glance up, she seems to be busy with something else."
                "Either she's showing another customer where to find whatever they want."
                "Or else the male member of staff is hovering over her while she works."
                "In the end I just give up, and so I shuffle off, feeling utterly deflated."
    if Person.find("amy"):
        $ amy.flags.amydelay = TemporaryFlag(True, 1)
    return


label amy_teaser_kiss:
    if Person.find("amy"):
        if amy.love.max < 60:
            $ amy.love.max = 60
    scene bg electronic
    "I'm passing the electronics store where Shawn and Amy work, so I make a detour to pop in."
    "It's always worth browsing around the place to see what they have on offer and what's new."
    "And in the past there was the chance to catch up with Shawn too."
    "But I've got to admit that recently, it's been more about getting to hang-out with Amy!"
    "I walk into the place with a big, dumb smile on my face at the thought of seeing her."
    "But that turns into a confused and disappointed frown when I hear and see what's going on inside."
    show shawn angry at center, zoomAt(1.0, (1140, 740)) with dissolve
    shawn.say "How many time do I have to tell you this stuff, Amy?"
    shawn.say "How many damn times?!?"
    show amy work angry at right4 with dissolve
    amy.say "Urgh!"
    amy.say "I already said I was sorry, Shawn!"
    amy.say "I promise it won't happen again."
    amy.say "What more do you want?"
    amy.say "Actual fucking blood?!?"
    show shawn at center, zoomAt(1.0, (1140, 740)), startle
    shawn.say "How about actually listening to me for once, huh?"
    shawn.say "How about retaining some information in that empty head of yours?"
    show amy at right4, startle
    amy.say "I don't have to stand here and take this from you!"
    amy.say "You can shove it up your..."
    show amy normal at center with move
    "It's at that moment Amy turns on her heel a towards the door."
    "And in doing so, she sees me standing there behind her."
    show shawn normal at center, zoomAt(1.0, (1140, 740)), startle
    "The move lets Shawn see me too, cutting off his next retort."
    "Suddenly both of them are silently staring at me."
    "And I can't help feeling more than a little awkward."
    mike.say "Ah..."
    mike.say "Hey, Shawn!"
    mike.say "Hey, Amy!"
    mike.say "Did I catch you at a bad time?"
    "I can feel the muscles of my face straining as I smile at them."
    "And part of me wants to just walk backwards out of the place."
    "No matter how weird that would look right now."
    "Amy seems to be able to regain control of herself first."
    "I see her expression become one of resolute determination."
    "She shoots a defiant look at Shawn."
    show amy at center, zoomAt(1.5, (640, 1040))
    "And then she strides straight over to where I'm standing."
    "I open my mouth to say something."
    "But that's when Amy reaches up and grabs me by the front of my shirt."
    "Taken by surprise, she easily jerks me forwards."
    hide shawn
    hide amy
    show amy kiss teaser
    with hpunch
    "And then she plants a kiss squarely on my lips."
    "Well, when I say kiss, I don't mean like a little affectionate peck."
    "Amy literally pushes her tongue straight into my mouth."
    "Then it explores in there like a snake hunting for prey!"
    "In that moment I'm totally stunned and unable to move."
    "It's like being transported from the most awkward situation imaginable."
    "And ending up in a place of sheer indulgent paradise!"
    "I find myself returning the kiss with mounting enthusiasm."
    "Amy doesn't hesitate to press herself against me either."
    "And the sensation of her body meeting mine makes me instantly hard."
    "I'm forgetting where we are and who's watching us right now."
    "I swear that if she put her hand in my pants I wouldn't be able to stop her."
    "That if she offered me herself that I'd fuck her on the spot!"
    "But then Amy breaks off the kiss."
    hide amy
    show amy work blush at center, zoomAt(1.5, (640, 1040))
    "And just like that I'm jolted back to reality."
    hide amy
    show amy work blush at center
    "Which really sucks, as it means I'm standing with an awkward erection."
    show shawn at center, zoomAt(1.0, (1140, 740)) with dissolve
    "And I have Shawn glaring at me from the other side of the store."
    "I look at Amy, hoping that she'll come to my rescue."
    hide amy with moveoutright
    "But it looks like she's already slipped away into the back of the store."
    show shawn at center with move
    "Shawn comes stalking over now that she's gone."
    "And he doesn't look at all pleased with me!"
    shawn.say "You mind telling me what that was all about?"
    mike.say "What?"
    mike.say "I was going to ask you the same thing!"
    mike.say "Does she normally behave like that with customers?"
    show shawn sad
    shawn.say "She doesn't even behave like that with me!"
    shawn.say "More's the pity..."
    "Shaking off the effects of Amy's unexpected kiss, I make my excuses and leave."
    scene bg mall1 with fade
    "I get the impression that I'm not Shawn's favourite person after what just happened."
    "Plus I feel the need to make sense of why Amy chose to do what she did too."
    "Maybe I need to talk to her alone, without Shawn there to listen in?"
    "That way I can finally ask her what the hell's going on between us."
    $ game.room = "mall1"
    if Person.find("amy"):
        $ amy.flags.amydelay = TemporaryFlag(True, 2)
        $ amy.flags.kiss += 1
    return


label amy_teaser_sex:
    if Person.find("amy"):
        if amy.love.max < 120:
            $ amy.love.max = 120
    scene bg electronic
    "I just happen to be passing the electronics store where my friend Shawn works."
    "It's getting towards closing time, and that usually means the place is pretty quiet."
    "So I decide to stick my head around the door and see how Shawn's doing today."
    "Walking into the store, I soon see that I'm the only potential customer in the place."
    "I cast my gaze around, looking for Shawn amongst the aisles."
    show shawn at right with moveinleft
    "But when I finally see him, it's only a passing glimpse."
    mike.say "Ah..."
    mike.say "Hey, Shawn!"
    show shawn at left with move
    "I see his head travelling along one of the aisles at high speed."
    "And I have to wave just to make sure that he's actually seen me."
    show shawn at startle
    shawn.say "Oh..."
    show shawn happy at center with move
    shawn.say "Hey, [hero.name]!"
    show shawn normal
    shawn.say "Sorry, man - I'm rushing to finish something in the back!"
    shawn.say "Did you need me for anything?"
    "I shrug, starting to feel more than a little embarrassed."
    mike.say "Erm...no, not really!"
    mike.say "I was kinda just browsing, yeah?"
    "Shawn nods, still looking pretty harassed."
    shawn.say "Okay, man..."
    shawn.say "Look, just call Amy over if you want anything, yeah?"
    show shawn at startle
    shawn.say "HEY, AMY!"
    "I almost jump at the mere mention of his colleague's name."
    "And I try my best to wave Shawn down as he calls to her."
    amy.say "HUH?"
    amy.say "WHAT'S UP, SHAWN?"
    shawn.say "You okay to take care of [hero.name]?"
    shawn.say "I gotta go in the back."
    show amy work at right with moveinright
    "Before I can object, I see the top of Amy's head approaching."
    "Her blue hair bobs up and down as she walks the short distance to where I'm standing."
    "Then she round the end of the aisle, a huge smile on her face at the sight of me."
    amy.say "Hey, [hero.name]!"
    amy.say "Great to see you again!"
    "She turns to Shawn and shoos him away."
    amy.say "Off you go, Shawn."
    amy.say "I can handle [hero.name] on my own!"
    show amy at center
    show shawn at right
    with move
    "Shawn rolls his eyes and turns to walk into the back."
    shawn.say "Whatever you say, Amy..."
    hide shawn with moveoutright
    "As soon as we're alone together, I feel a surge of relief."
    mike.say "It's great to see you too, Amy!"
    mike.say "You're looking great too!"
    "And I really mean that."
    "Okay, okay...cards on the table here."
    "I was kind of hoping that Amy would be around when I decided to go into the shop."
    "Don't get me wrong, Shawn's a pretty nice guy."
    "But he doesn't have the same effect on me as Amy does."
    "The same effect she's having on me right now!"
    show amy flirt
    amy.say "Aww..."
    amy.say "Thanks, [hero.name]!"
    "Amy grins at me as she twirls her blue hair in one hand."
    "She's leaning against a basket full of discounted games."
    "And her head is tilted towards me."
    amy.say "You too, by the way!"
    amy.say "You're looking good, I mean..."
    "I look down at myself, more than a little surprised."
    mike.say "I do?"
    mike.say "Oh...you really think so?"
    "Amy nods and lets out a cute little chuckle."
    amy.say "Of course I do, [hero.name]!"
    amy.say "Don't you know how to take a compliment?"
    show amy angry
    amy.say "Anyway, you're a lot more fun than Shawn's being right now!"
    mike.say "Huh?"
    mike.say "Is he working you too hard or something?"
    "Amy casts a glance at the door to backroom, as if she's afraid of Shawn reappearing."
    "But when he doesn't show up at the mere mention of his name, she seems satisfied."
    amy.say "Urgh..."
    show amy normal
    amy.say "It's not that, [hero.name]."
    amy.say "Shawn's a pretty easy-going boss, you know?"
    amy.say "It's just...I kinda feel he wants more from me!"
    amy.say "And I'm just not into him, yeah?"
    mike.say "Yeah..."
    mike.say "I see how that could be awkward!"
    mike.say "You're sure Shawn's not dating material?"
    mike.say "Sure, he's a little anal at times."
    mike.say "But he's really a nice guy!"
    "Amy shakes her head, dismissing the case I'm making for Shawn."
    show amy work flirt at center, zoomAt(1.5, (640, 1040))
    "At the same time she reaches out and caresses my cheek."
    amy.say "No way, [hero.name]!"
    amy.say "You see...there's another guy I like!"
    amy.say "And he's WAY hotter than Shawn..."
    hide amy
    show amy kiss with dissolve
    "My eyes go wide as Amy leans forward and puts her lips against mine."
    "And her tongue slips into my mouth before I even know what's happening!"
    "But it's not like this is an unpleasant surprise, and I soon recover."
    "Then I'm returning the kiss with as much passion as Amy is able to handle."
    hide amy
    show amy work blush at center, zoomAt(1.5, (640, 1040))
    with dissolve
    "In the end, I'm a little disappointed when it comes to an end."
    "But the mischievous grin on Amy's face makes up for that disappointment."
    amy.say "Mmm..."
    amy.say "I've been waiting to do that for SO long!"
    amy.say "But you know what - I want more!"
    "It's about now that I realise Amy's stroking me below the waist."
    "Specifically she's rubbing my cock through my pants!"
    mike.say "Y...you're serious, Amy?"
    mike.say "You want to get it on?"
    mike.say "Here and now?!?"
    "I glance around the shop."
    mike.say "What if someone walks in on us?"
    mike.say "What if Shawn catches us?"
    show amy flirt
    amy.say "Don't worry, [hero.name]."
    amy.say "I closed the shutters before I came over here."
    amy.say "Nobody's getting in and Shawn'll be too busy to bother us."
    show amy blush
    "I glance at Amy, realising that she must have planned this from the start."
    "Why else would she have closed the shutters and ushered Shawn off like that?"
    mike.say "You're sure, Amy?"
    mike.say "Because I REALLY want to take you up on the offer!"
    "Amy nods and giggles, clearly delighted to have caught me in her trap."
    show amy flirt
    amy.say "I promise, [hero.name]."
    amy.say "It'll be just you and me - having fun!"
    "I look away from Amy for a moment, turning my head towards the back of the shop."
    "But then I look back at her, and I know what my answer is going to be."
    mike.say "I can't say no, Amy."
    mike.say "In fact, you've been on my mind ever since I first saw you!"
    "Amy's grin tells me all that I need to know."
    "She looks delighted by my admission that I like her."
    "And now she seems all the more determined to have her way with me too!"
    amy.say "I kind of have a fantasy, [hero.name]..."
    amy.say "About being fucked in the store by a customer."
    amy.say "You see I imagine I'm bending over...like this."
    "Amy turns and leans over the basket in front of her."
    "And she's sure to stick her ass out towards me as she does so."
    amy.say "The guy keeps on asking me to reach for stuff."
    amy.say "Stuff right at the back of the basket."
    amy.say "So I have to stretch, like this..."
    "I watch as Amy reaches for the back of the basket."
    "She's already standing on her tip-toes."
    "And her skirt is riding up dangerously too!"
    amy.say "Then you know what the perv does?"
    amy.say "He lifts up my skirt!"
    "Suddenly it dawns on me what Amy's doing."
    "She's not just showing me her fantasy."
    "She's trying to draw me into it, to get me role playing!"
    hide amy
    show amy fuck electronic with fade
    "I step up behind her, pushing my groin into her ass."
    "Amy's pushed forwards, but she giggles and nods all the same."
    "And her laughter becomes even more eager when I lift up her skirt."
    amy.say "Yeah, [hero.name], just like that!"
    amy.say "Then the creep pulls down my panties, can you believe that?!?"
    "I'm nodding even as I hook my fingers into the elastic of Amy's knickers."
    "And then I pull them down, exposing the pale cheeks of her backside."
    amy.say "Can you guess what he does next?"
    "As Amy asks the question, I'm already unzipping my flies."
    "She seems to hear the sound, giggling again."
    amy.say "Yeah, that's right!"
    amy.say "He gets his cock out."
    amy.say "And then he sticks it in me!"
    show amy fuck electronic insert
    "Amy's got me pretty aroused by now, as you can probably imagine."
    "And my cock's as hard as rock at the mere thought of fucking her."
    "There's nothing to stop me from getting what I want."
    "And giving Amy exactly what she wants too!"
    menu:
        "Fuck her pussy":
            "I hastily take hold of Amy's haunches, gripping them tightly."
            "She almost purrs at the sensation, pushing her ass harder against me."
            "I still feel like we might get caught at any moment."
            "So I don't waste any time in getting down to it."
            "Luckily for me, I soon discover that Amy's more then ready for it."
            "The head of my cock slides along the lips of her pussy."
            "And that's because she's already slick and slippery down there."
            "Amy must have been getting wet almost from the moment she saw me!"
            amy.say "Oh god..."
            amy.say "I NEED this..."
            show amy fuck electronic insert vaginal
            "It doesn't take much for my cock to start inching into Amy."
            "She moans and sighs as it enters her, clearly loving every moment."
            amy.say "Mmm..."
            amy.say "Oh fuck, [hero.name]..."
            amy.say "I never thought you'd be so BIG!"
            "And I never thought I'd be fucking Amy like this!"
            "I'm already picking up speed, thrusting in and out of her."
            "In fact, I'm almost lifting her off the ground!"
            "The basket rattles underneath Amy as I furiously pound her."
            "She feels so good around my cock, I want this to last longer."
            "Trying to think of something to prolong the experience, I glance around the store."
            "And that's when I see something in the doorway to the backroom."
            mike.say "Ah..."
            mike.say "Amy..."
            mike.say "Shawn's...watching!"
            amy.say "Ah, fuck him, [hero.name]!"
            amy.say "Who the fuck cares?"
            "Well, I might, for one!"
            "I can't say I like the idea of Shawn watching me fuck Amy!"
            "But then I'm already balls deep in her by now."
            "And I don't feel like stopping to have it out with him."
            "Because I'm sure that'd be the end of what we're doing right now."
            "That's why I give a silent nod and redouble my efforts."
            "And Amy seems to instantly appreciate the work I'm putting in."
            amy.say "Oh yeah..."
            amy.say "That's more like it!"
            "I'm so excited at the chance to fuck Amy like this."
            "And at the same time I'm on edge thanks to the knowledge we're being watched."
            "The combination of the two is what I blame for the thing that happens next."
            "Which is me starting to cum!"
            "I estimate I have no more than a few seconds to decide where this is going..."
            menu:
                "Cum inside":
                    "Amy starts to squeal as I push as far into her as possible."
                    if Person.find("amy"):
                        $ amy.love += 2
                    show amy fuck electronic insert vaginal cum with hpunch
                    "Then she begins to wail as I finally lose it and shoot my load."
                    with hpunch
                    "I don't hold anything back, letting her take everything I have to give."
                    show amy fuck electronic insert vaginal creampie with hpunch
                    "And it's a good job she's leaning over the basket while all of this is happening."
                    "Because otherwise I'm pretty sure Amy would have collapsed into a heap on the floor by now!"
                "Pull out":
                    "Amy squeals as I pull my cock out of her pussy in one smooth motion."
                    if Person.find("amy"):
                        $ amy.love += 1
                    show amy fuck electronic -insert with hpunch
                    "And then she begins to moan as I shoot my load over her ass."
                    with hpunch
                    "White lines of cum stripe her pale skin and soak into her skirt."
                    with hpunch
                    "And it's a good job she's leaning over the basket while all of this is happening."
                    "Because otherwise I'm pretty sure Amy would have collapsed into a heap on the floor by now!"
        "Fuck her ass":
            "But then she never specifically said WHERE she wanted it, did she?"
            amy.say "Oh god..."
            amy.say "I NEED this..."
            "I nod and smile, eager to get into it with Amy."
            "But also because I have a surprise in mind for her."
            "Aiming my cock higher than her pussy, I target her neat little ass."
            amy.say "Wha..."
            amy.say "What are you..."
            amy.say "Oh shit..."
            show amy fuck electronic insert anal
            "I push as hard as I dare, sinking the head of my cock into Amy's hole."
            "It's tight and her muscles squeeze me the whole time, trying to keep me out."
            "None of that stops me, and slowly my cock starts inching into Amy."
            "She moans and sighs as it enters her, clearly loving every moment."
            amy.say "Mmm..."
            amy.say "Oh fuck, [hero.name]..."
            amy.say "I never thought you'd be so BIG!"
            "And I never thought I'd be fucking Amy like this!"
            "I'm already picking up speed, thrusting in and out of her."
            "In fact, I'm almost lifting her off the ground!"
            "The basket rattles underneath Amy as I furiously pound her."
            "She feels so good around my cock, I want this to last longer."
            "Trying to think of something to prolong the experience, I glance around the store."
            "And that's when I see something in the doorway to the backroom."
            mike.say "Ah..."
            mike.say "Amy..."
            mike.say "Shawn's...watching!"
            amy.say "Ah, fuck him, [hero.name]!"
            amy.say "Who the fuck cares?"
            "Well, I might, for one!"
            "I can't say I like the idea of Shawn watching me fuck Amy!"
            "But then I'm already balls deep in her by now."
            "And I don't feel like stopping to have it out with him."
            "Because I'm sure that'd be the end of what we're doing right now."
            "That's why I give a silent nod and redouble my efforts."
            "And Amy seems to instantly appreciate the work I'm putting in."
            amy.say "Oh yeah..."
            amy.say "That's more like it!"
            "I'm so excited at the chance to fuck Amy like this."
            "And at the same time I'm on edge thanks to the knowledge we're being watched."
            "The combination of the two is what I blame for the thing that happens next."
            "Which is me starting to cum!"
            "I estimate I have no more than a few seconds to decide where this is going..."
            menu:
                "Cum inside":
                    "Amy starts to squeal as I push as far into her as possible."
                    if Person.find("amy"):
                        $ amy.sub += 2
                    show amy fuck electronic insert anal cum with hpunch
                    "Then she begins to wail as I finally lose it and shoot my load."
                    with hpunch
                    "I don't hold anything back, letting her take everything I have to give."
                    show amy fuck electronic insert anal creampie with hpunch
                    "And it's a good job she's leaning over the basket while all of this is happening."
                    "Because otherwise I'm pretty sure Amy would have collapsed into a heap on the floor by now!"
                "Pull out":
                    "Amy squeals as I pull my cock out of her ass in one smooth motion."
                    if Person.find("amy"):
                        $ amy.sub += 1
                    show amy fuck electronic -insert with hpunch
                    "And then she begins to moan as I shoot my load over her buttocks."
                    with hpunch
                    "White lines of cum stripe her pale skin and soak into her skirt."
                    with hpunch
                    "And it's a good job she's leaning over the basket while all of this is happening."
                    "Because otherwise I'm pretty sure Amy would have collapsed into a heap on the floor by now!"
    "Almost as soon as she gets her breath back, Amy starts to pull up her panties."
    hide amy
    show amy work blush at center, zoomAt(1.5, (640, 1040))
    with fade
    "Sensing that I need to beat a hasty retreat, I stuff my cock back into my own pants."
    "Then she hustles me towards the door, looking back over her shoulder the whole time."
    "Amy half-opens the shutters and almost shoves me out of the store."
    "But as she does so, she shouts after me."
    show amy flirt
    amy.say "That was some serious fun, [hero.name]!"
    amy.say "Call me, okay?"
    "Amy puts her hand up to the side of her head to make the 'phone' sign."
    scene bg mall1 with fade
    "And then the shutters clatter down again, leaving me alone outside the store."
    "I shrug and turn to start walking away."
    "And I'm wondering what the hell Shawn must have made of all that."
    "But I soon forget about him and start thinking about Amy instead."
    "I wonder how long I should wait before I call her."
    "And if we can get up to something like that when I do."
    $ game.room = "mall1"
    if Person.find("amy"):
        $ amy.flags.amydelay = TemporaryFlag(True, 2)
        $ amy.flags.kiss += 1
        $ amy.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
