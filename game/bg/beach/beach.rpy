init python:
    Room(**{
    "name": "beach",
    "display_name": "Beach",
    "exits": ["map", "ramenshop", "masterhouse"],
    "conditions": [
        IsSeason(0, 1),
        HasVehicle(),
        InInventory("swimsuit"),
        ],
    "travel_time": 2,
    "music": "music/roa_music/summer_air.ogg",
    "ambience": "sd/SFX/ambiences/nature/beach.ogg",
    "outfit": "swimsuit",
    "tags": ["beach"],
    })

    Activity(**{
    "name": "swim_beach",
    "label": "swim",
    "fun": 1,
    "fitness": 1,
    "duration": 2,
    "rooms": "beach",
    "conditions": [
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 3),
            ),
        ],
    "display_name": "Swim",
    "icon": "swim",
    })

    Activity(**{
    "name": "train_beach",
    "label": "train_beach",
    "fun": -5,
    "energy": -5,
    "hunger": -5,
    "grooming": -5,
    "fitness": 1,
    "duration": 6,
    "rooms": "beach",
    "conditions": [
        IsHour(10, 16),
        HeroTarget(
            IsGender("male"),
            Not(HasSkill("martial_arts")),  
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("grooming", 3),
            MinStat("fun", 3),
            MinFlag("masterStory", 1),
            MaxFlag("masterStory", 5),
            ),
        ],
    "display_name": "Train",
    "icon": "martialart",
    })

    InteractActivity(**{
    "name": "beach_suntan",
    "energy": 2,
    "icon": "tan",
    "conditions": [
        IsHour(9, 19),
        HeroTarget(IsRoom("beach")),
        InInventory("lotion"),
        ],
    "display_name": "Apply sunscreen",
    "label": "apply_sunscreen",
    "once_day": "ACTIVE",
    })

    Event(**{
    "name": "mike_meet_the_master",
    "label": "meet_the_master_male",
    "duration": 1,
    "conditions": [
        IsDayOfWeek("246"),
        IsHour(10, 16),
        HeroTarget(
            IsGender("male"),
            IsRoom("beach")),
        Not(HasSkill("martial_arts")),
        ],
    "chances": 50,
    "do_once": True,
    })

    Event(**{
    "name": "beach_graduation",
    "label": "beach_graduation",
    "duration": 1,
    "conditions": [
        IsDayOfWeek("246"),
        IsHour(10, 16),
        HeroTarget(
            IsGender("male"),
            IsRoom("beach"),
            Not(HasSkill("martial_arts")),  
            IsFlag("masterStory", 6),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "shark_attack_male",
    "label": "shark_attack_male",
    "conditions": [
        IsHour(22, 6),
        HeroTarget(
            IsGender("male"),
            IsActivity("swim_beach"),
            IsRoom("beach"),
            Not(InInventory("shark_training")),
            Or(
                And(
                    HasSkill("animalhated"),
                    MaxStat("energy", 6)
                    ),
                MaxStat("energy", 3),
                ),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "shark_chan_pet",
    "label": "shark_chan_pet",
    "conditions": [
        IsHour(22, 6),
        HeroTarget(
            IsGender("male"),
            IsActivity("swim_beach"),
            IsRoom("beach"),
            InInventory("shark_training"),
            Or(
                And(
                    HasSkill("animalhated"),
                    MaxStat("energy", 6)
                    ),
                MaxStat("energy", 3),
                ),
            ),
        ],
    "do_once": True,
    })


    Event(**{
    "name": "bird_attack_male",
    "label": "bird_attack_male",
    "conditions": [
        IsHour(6, 20),
        HeroTarget(
            IsGender("male"),
            IsRoom("beach"),
            Or(
                HasSkill("animalhated"),
                MaxStat("energy", 3),
                ),
            ),
        ],
    "chances": 10,
    "once_week": True,
    })

    Activity(**{
    "name": "bear_shark_ending",
    "label": "bear_shark_ending",
    "conditions": [
        IsDone("bear_chan_pet", "shark_chan_pet"),
        IsTimeOfDay("afternoon", "evening"),
        HeroTarget(
            IsGender("male"),
            IsRoom("beach"),
            ),
        "hero.sexperience == 0"
        ],
    "display_name": "Surf in the sunset",
    "icon": "sunsetsurf",
    "do_once": True,
    })

label bird_attack_male:
    show bg beach
    "I'm just walking along the beach, minding my own business when it happens."
    "I'm attacked by something swooping down out of the clear, blue skies."
    $ renpy.sound.set_pan(1, 0, channel='sound')
    $ renpy.sound.set_pan(0, 2.0, channel='sound')
    play sound seagull
    $ renpy.sound.set_pan(1, 0, channel='audio')
    $ renpy.sound.set_pan(0, 2.0, channel='audio')
    play sound dove
    "All I know at first is that there's a flapping of wings and a horrible cawing."
    show bird attack
    $ persistent.bird_attack = True
    "And then I realise I'm being attacked by a damn seagull!"
    mike.say "Aargh!"
    mike.say "Piss off, you vicious, feathered bastard!"
    mike.say "What did I ever do to you?!?"
    play sound seagull
    "I wave my hands desperately in the air, trying to fend off my attacker."
    "And my reward for doing so is to have my fingers scratched and pecked."
    call injured from _call_injured
    "But at least it's better than my face suffering the same fate."
    "I must have landed at least one serious blow in self-defence."
    $ renpy.sound.set_pan(0, 0, channel='sound')
    $ renpy.sound.set_pan(-1, 2.0, channel='sound')
    play sound seagull
    scene bg beach
    "As the seagull lets out another horrid cawing cry and suddenly flaps away."
    "Or maybe it spots an easier target that's made the mistake of eating an ice-cream."
    "Either way I hurry off before it decides to return."
    "But not before I discover that it also managed to take a shit on my head too!"
    $ hero.grooming -= 10
    return

label shark_attack_male:
    scene bg beach
    if persistent.shark_attack:
        "I love it when a trip to the beach comes together like this one has."
        "The sun is high in a clear, blue sky and it's beating down on golden sands."
        "Sands that I'm strolling along in my best pair of trunks, looking good."
        "And don't just take my word for it - look at all the admiring glances I'm getting."
        "More than a few guys are visibly fuming right now."
        "Because of the fact their girlfriends are checking me out in front of them!"
        "But I'm just strolling on past them, a huge grin on my face."
        "Sorry guys, it's not my fault your girls all want a piece of this action!"
        "Wow, this must be what guys like Dwayne feel like every day of their lives."
        "And yeah, I know that this isn't going to last, okay."
        "But I'm going to milk it for every single second that it does."
        "Though there is a slight problem with that."
        "Because I can't just keep walking up and down the beach all day."
        "If I do, everyone's going to figure out that I'm posing it'll all be over."
        "Glancing around, I start trying to come up with a solution."
        "I need to be visible to everyone at the beach, and yet still keep moving."
        "But then my eyes fall on the shimmering waters of the sea."
        "And I realise that swimming is the perfect solution."
        "Not only does it mean that people will be able to see me."
        "But they'll also be able to check out my body as I do it!"
        "So wasting no time, I turn towards the water and start to walk into the shallows."
        "Playing it cool, I walk out as the waves begin to lap around my feet and ankles."
        "After only a couple of feet it's reached halfway up my calves and is going higher."
        "By now I'm beginning to wade into the water, rather than walk, so my pace slows."
        "And as the depth exceeds my knees, I start preparing to actually swim."
        "Once my legs are totally underwater, I lean forwards and stretch out my arms."
        "Because a mere moment later I'm deep enough to lift my legs off of the bottom."
        "Then all it takes is a push, and I feel myself being supported by the water."
        "Instinct kicks in and I begin to stroke with my arms while kicking with my legs."
        show swimmingrace_bg_02 at flip
        show swimmingrace_mikemc_02 at flip
        show swimmingrace_outfit_mikemc_normal_02 at flip
        show swimmingrace_water_mikemc_02 at flip
        show swimmingrace_water_fg_mikemc_02 at flip
        with fade
        "And just like that I'm swimming through the cool water like it's nothing."
        "I'm a pretty strong swimmer, so I don't hesitate to head out a little way."
        "Already I can feel my muscles working hard as I plough through the water."
        "Which means that I'm getting a free workout into the bargain too!"
        "Bather" "Oh my god!"
        "Bather" "Is that..."
        "Bather" "Yeah, it is!"
        "I'm only half listening to the hubbub that's happening back on dry land."
        "And I can't help chuckling to myself as I hear people crying out in amazement."
        "I mean yeah, I know that I must look good out here as I part the water."
        "But there are actually people starting to yell and scream back there."
        "And even I think that's a little bit over the top!"
        "Bather" "SHARK!"
        "Bather" "There's a shark!"
        "Bather" "Everyone out of the water!"
        "I turn my head, not wanting to believe what I'm hearing."
        "But as soon as I do, I'm treated to the sight of a shark's fin in the water."
        show shark_attack_bg at center, zoomAt(1.0, (640, 720))
        show shark_attack_shark at center, zoomAt(1.0, (340, 720))
        show shark_attack_shark at center, traveling(1.2, 5.0, (680, 800))
        show shark_attack_water at center, zoomAt(1.0, (640, 720))
        show shark_attack_mikemc
        show shark_attack_fg at center, zoomAt(1.0, (640, 720))
        with fade
        "That and a mouth filled with multiple rows or razor-sharp teeth!"
        "I put all of my effort into trying to swim as fast as I can for the shore."
        "But for some reason I seem to be going slower, rather than faster."
        "Maybe the panic is making me flounder in the water, rather than swim."
        "Which is kind of a shame, because the shark is having no such problems."
        "Perhaps the one mercy I get is that everything happens so damn fast."
        show shark_attack_bg at center, traveling(1.2, 5.0, (680, 800))
        show shark_attack_shark at center, traveling(1.2, 5.0, (680, 800))
        show shark_attack_water at center, traveling(1.2, 5.0, (680, 800))
        show shark_attack_fg at center, traveling(1.2, 5.0, (680, 800))
        show shark_attack_mikemc at hshake
        pause 0.3
        hide shark_attack_mikemc with easeoutbottom
        "Before I can even feel the pain, it's jaws clamp down on me."
        show shark_attack_water at blood
        show shark_attack_fg at blood
        with dissolve
        "And after that I'm no longer swimming at all, just being dragged through the water."
        show shark_attack_shark at center, traveling(1.75, 5.0, (780, 800))
        show shark_attack_water at center, traveling(2.0, 5.0, (680, 720))
        show shark_attack_fg at center, traveling(2.0, 5.0, (680, 720))
        "The sounds of the other bathers on the beach are getting fainter with every passing moment."
        "And all of my senses are being overwhelmed at once, making everything a blur."
        scene bg black with dissolve
        "So when it all goes black, at first that seems to be just another aspect of the confusion."
        "It's only when none of my senses return that I even have an inkling something is wrong."
        "And by that time it's too late, as I'm already sinking into an ocean of blankness."
        "One from which there's no chance of returning."
        if not game.flags.cheat and renpy.has_label("shark_achievement_1"):
            call shark_achievement_1 from _call_shark_achievement_1_2
        if not game.flags.cheat and renpy.has_label("shark_achievement_2"):
            call shark_achievement_2 from _call_shark_achievement_2
    else:
        "I've almost made it to the point where the waves are crashing onto the sand, when I hear the sound of a vague and distant cry."
        "Glancing over my shoulder, I can see what looks like a lifeguard as she runs towards me down the beach in slow motion."
        "I groan and shake my head, thinking that I really don't have the time or patience for being lectured by some extra from Baywatch."
        "A quick look at how far away she is from me in comparison to the sea convinces me that I can be in the water long before she's even close."
        "I can always claim ignorance afterwards, say that she was just too far away for me to hear what she was trying to say."
        "My mind made up, I trot the last couple of feet into the lapping waves and then dive in as soon as the water becomes deep enough to do so."
        "Being a pretty strong swimmer, it doesn't take me long to get pretty far out, even before the lifeguard arrives at the edge of the water herself."
        show swimmingrace_bg_02 at flip
        show swimmingrace_mikemc_02 at flip
        show swimmingrace_outfit_mikemc_normal_02 at flip
        show swimmingrace_water_mikemc_02 at flip
        show swimmingrace_water_fg_mikemc_02 at flip
        with fade
        "Now I have the sound of the waves to drown her out as well, and I make a point of not looking back over my shoulder as I swim further out."
        "But it's not long before I can make out a new sound that's loud enough to heard even over that of the waves."
        "It sounds like something big ploughing its way through the water behind me, and it's catching up fast."
        "Thinking that it's most likely more lifeguards, maybe on jet-skis or some kind of small boat, I decide that the game's up."
        show shark_attack_bg at center, zoomAt(1.0, (640, 720))
        show shark_attack_shark at center, zoomAt(1.0, (340, 720))
        show shark_attack_shark at center, traveling(1.2, 5.0, (680, 800))
        show shark_attack_water at center, zoomAt(1.0, (640, 720))
        show shark_attack_mikemc
        show shark_attack_fg at center, zoomAt(1.0, (640, 720))
        with fade
        $ persistent.shark_attack = True
        if not game.flags.cheat and renpy.has_label("shark_achievement_1"):
            call shark_achievement_1 from _call_shark_achievement_1
        "I glance back over my shoulder, ready to give myself up and claim ignorance."
        "And it's then that I see something that instantly makes me pollute the small part of the sea in which I'm currently floating."
        "It's a shark. Huge, ugly and like something out of cinematic nightmare."
        "And it's bearing down on me with its mouth wide open."
        "Beady black eyes stare at me over the gaping red maw and row after row of jagged, razor-sharp teeth."
        "I'm not frozen in place by the fear, but it does make me panic and reduce my strokes to a pathetic doggy-paddle."
        "I try with all of my might to push myself faster through the water, but everything happens so fast."
        "The shape of the shark looms over me, it's jaws closing faster than I ever thought it was possible for something that large to move."
        show shark_attack_bg at center, traveling(1.2, 5.0, (680, 800))
        show shark_attack_shark at center, traveling(1.2, 5.0, (680, 800))
        show shark_attack_water at center, traveling(1.2, 5.0, (680, 800))
        show shark_attack_fg at center, traveling(1.2, 5.0, (680, 800))
        show shark_attack_mikemc at hshake
        pause 0.3
        hide shark_attack_mikemc with easeoutbottom
        "There's no pain, but only because there isn't time for me to make sense of what's happening."
        show shark_attack_water at blood
        show shark_attack_fg at blood
        with dissolve
        "Everything is churning, white water and a red that isn't the shark's gaping mouth."
        show shark_attack_shark at center, traveling(1.75, 1.0, (780, 800))
        show shark_attack_water at center, traveling(2.0, 1.0, (680, 720))
        show shark_attack_fg at center, traveling(2.0, 1.0, (680, 720))
        "And then there's nothing but black..."
    if not game.flags.cheat and renpy.has_label("mike_achievement_0") and (game.days_played == 0 or (game.days_played == 1 and game.hour <= 10)):
        call mike_achievement_0 from _call_mike_achievement_0_1
    scene bg black with dissolve
    pause 1.0
    $ renpy.mark_image_seen("shark attack")
    $ renpy.full_restart()
    return

label shark_chan_pet:
    scene bg beach
    "I love it when a trip to the beach comes together like this one has."
    "The sun is high in a clear, blue sky and it's beating down on golden sands."
    "Sands that I'm strolling along in my best pair of trunks, looking good."
    "And don't just take my word for it - look at all the admiring glances I'm getting."
    "More than a few guys are visibly fuming right now."
    "Because of the fact their girlfriends are checking me out in front of them!"
    "But I'm just strolling on past them, a huge grin on my face."
    "Sorry guys, it's not my fault your girls all want a piece of this action!"
    "Wow, this must be what guys like Dwayne feel like every day of their lives."
    "And yeah, I know that this isn't going to last, okay."
    "But I'm going to milk it for every single second that it does."
    "Though there is a slight problem with that."
    "Because I can't just keep walking up and down the beach all day."
    "If I do, everyone's going to figure out that I'm posing it'll all be over."
    "Glancing around, I start trying to come up with a solution."
    "I need to be visible to everyone at the beach, and yet still keep moving."
    "But then my eyes fall on the shimmering waters of the sea."
    "And I realise that swimming is the perfect solution."
    "Not only does it mean that people will be able to see me."
    "But they'll also be able to check out my bod as I do it!"
    "So wasting no time, I turn towards the water and start to walk into the shallows."
    "Playing it cool, I walk out as the waves begin to lap around my feet and ankles."
    "After only a couple of feet it's reached halfway up my calves and is going higher."
    "By now I'm beginning to wade into the water, rather than walk, so my pace slows."
    "And as the depth exceeds my knees, I start preparing to actually swim."
    "Once my legs are totally underwater, I lean forwards and stretch out my arms."
    "Because a mere moment later I'm deep enough to lift my legs off of the bottom."
    scene swimmingrace_bg_03
    show swimmingrace_mikemc_03
    show swimmingrace_outfit_mikemc_normal_03
    show swimmingrace_water_mikemc_03
    show swimmingrace_water_fg_mikemc_03
    show swimmingrace_shark
    with fade
    "Then all it takes is a push, and I feel myself being supported by the water."
    "Instinct kicks in and I begin to stroke with my arms while kicking with my legs."
    "And just like that I'm swimming through the cool water like it's nothing."
    "I'm a pretty strong swimmer, so I don't hesitate to head out a little way."
    "Already I can feel my muscles working hard as I plough through the water."
    "Which means that I'm getting a free workout into the bargain too!"
    "Bather" "Oh my god!"
    "Bather" "Is that..."
    "Bather" "Yeah, it is!"
    "I'm only half listening to the hubbub that's happening back on dry land."
    "And I can't help chuckling to myself as I hear people crying out in amazement."
    "I mean yeah, I know that I must look good out here as I part the water."
    "But there are actually people starting to yell and scream back there."
    "And even I think that's a little bit over the top!"
    "Bather" "SHARK!"
    "Bather" "There's a shark!"
    "Bather" "Everyone out of the water!"
    "I turn my head, not wanting to believe what I'm hearing."
    "But as soon as I do, I'm treated to the sight of a shark's fin in the water."
    "That and a mouth filled with multiple rows or razor-sharp teeth!"
    "I'm just about start making a desperate attempt to swim for shore."
    "But then it hits me that just read a book that could help me out here."
    "Now, what did 'How to Train Your Shark' say about this kind of thing?"
    "Oh yeah, apparently it's all about how you position yourself in the water."
    "So as the shark bears down on me, I adjust my stance just so."
    "There are still people screaming on the beach."
    "No doubt some of them wondering what the hell I'm doing."
    "But I don't think I could outswim the shark if I tried."
    "And so I just have to hope that this works."
    "Wincing and closing my eyes, I hold out a hand in front of me."
    "Honestly I'm expecting to open them again and be presented with a bloody stump."
    "But instead I feel something rubbing itself against the palm of my hand."
    "Something really large and with skin that feels like bloody sandpaper!"
    "Opening one eye and then the other, I can't help staring at what I see."
    "Because there's the shark, floating in the water right in front of me."
    "And it's rubbing it's snout against me like a dog desperately wanting attention!"
    "Without thinking, I start rubbing away and patting the shark's nose."
    "Which only seems to make it more friendly than before."
    "Eventually I manage to wade back to the shore and the safety of dry land."
    "But the shark follows me all the way, harassing me like a needy dog."
    scene bg beach with fade
    "And as I walk back onto the beach, everyone is staring at me again."
    "Although this time it's more out of sheer amazement and disbelief."
    "But I can't say that I blame them, as I feel the exact same way."
    return


label bear_shark_ending:
    menu:
        "To the sunset and beyond !!! (leads to an ending)":
            pass
        "Not yet":
            $ hero.cancel_activity()
    "I used to think that my life was totally mundane and boring, like nothing interesting ever happened to me."
    "My job was boring, my friends were a bunch of complete nerds and my love-life was dead on arrival."
    "But then things just started to change for me."
    "I think it was around the time Sam and Ryan were moving out."
    "And it was definitely happening to me when [bree.name] and Sasha had finished moving in."
    "I don't know how to explain it, at least not without sounding like I'm crazy."
    "But it was just like I felt an outside force was suddenly playing a part in my life."
    "I was meeting new people all the time - and I mean HOT new people!"
    "But I suddenly had the confidence to talk to them too."
    "Like, I'd see a new girl at work, or in one of the local stores."
    "And before I knew it, I'd be striking up a conversation, joking with her."
    "Sometimes I'd even pluck up the courage to ask her out on a date."
    "Hell, there were even times when the girl actually said yes!"
    "After that, things just seemed to build from there."
    "My life was getting crazier and more exciting all the time."
    scene bg black
    show bear shark ending
    with fade
    "And I guess that's how I got to be here, sitting on the back of a fully-grown shark."
    "I'm straddling the back of the planet's most feared apex predator."
    "My hands are holding tight to the fin in the middle of it's back."
    "And I'm riding the damn thing towards the horizon, into the setting sun."
    "It's times like now that I tend to look down a feel the need to pinch myself."
    "Just to check that I'm actually awake and not dreaming."
    "Because the way that my life's gotten crazier by degrees means that I sometimes don't notice."
    "And when that happens to me, I feel the need to just take a step back and take stock."
    "So much so that I'm in real danger of losing my grip and falling off the back of the shark."
    "But that's the very moment when I feel a pair of strong arms wrapping themselves around me."
    "And when I say strong, I mean it - crazily strong!"
    "As well as very furry and ending in paws with claws bigger than my head."
    "I can already feel myself relaxing and letting my back rest against my fellow shark-rider."
    "Because I know that they're more than capable of supporting my weight."
    mike.say "Phew..."
    mike.say "I almost fell off just now!"
    mike.say "Thanks, Bear Chan..."
    mike.say "I don't know what I'd do without you."
    "Bear Chan" "UUURRRGH!"
    "Bear Chan" "AAARRRGH!"
    "Bear Chan" "RUUUURGH!"
    "I can't help nodding my head as Bear Chan lets me know just what she's thinking."
    "And as usual, I really appreciate the fact that she's not holding back at all."
    "Which is why I raise a hand in the air, tipping my palm backwards over my shoulder."
    "As soon as I feel one of her massive paws slap down on my own, I start nodding."
    mike.say "You know it's the truth, buddy!"
    mike.say "You and me against the world."
    mike.say "Just like always."
    "I'm not sure just where this damn shark is headed."
    "Or come to think of that, how the hell we're ever going to get off of it."
    "But that's one of the perks that comes with having Bear Chan in tow."
    "She's one of those people that always seems to tip the scale in your favour."
    "And why in the hell would I worry about a small detail like that anyway?"
    "So far this has been the craziest ride imaginable, and I've had a wild time."
    "Whatever's waiting for us over the horizon, I'm sure it'll be just as wild too."
    "And I know that all I've learnt on the journey has prepared me for any challenge."
    "So for now, I'm just going to lean back."
    "I'm going to chill with my erstwhile ursine buddy."
    "And I'm going to watch the sun setting on the distant horizon."
    "I already made it to second base."
    "So there's at least two more to go, right?"
    scene bg black with dissolve
    pause 0.5
    if not game.flags.cheat and renpy.has_label("bear_shark_achievement_1"):
        call bear_shark_achievement_1 from _call_bear_shark_achievement_1
    $ game.set_new_game_plus()
    $ renpy.full_restart()


label beach_graduation:
    "When I arrive at the beach and start looking for the Master, my head is already filled with guesses at what today's humiliating task might be."
    show master happy noglasses with dissolve
    "But when I find him standing on the sand, hands behind his back and a huge grin on his face at the sight of me, I get the impression something's up."
    "It's not the fact that he's smiling that does it, as he must be pleased with himself for having pocketed a couple hundred dollars of my money for his dodgy lessons."
    "I'm more intrigued by the way that he just stands there, making no move to beckon me this way or that, or else proffer the instrument of my daily torture."
    mike.say "Shall we get started, Master?"
    mike.say "I'm ready for today's lesson!"
    "Yeah, because that hundred dollars is just burning a hole in my pocket!"
    show master wink at startle
    "The Master lets out a chuckle and gives me an approving nod."
    master.say "I am heartened by you enthusiasm, my boy."
    master.say "But there will be no lesson today, nor tomorrow, nor the day after that either."
    show master normal
    "Although I'm glad to hear that he won't be draining the contents of my bank account any longer, I'm still quite taken aback by the finality of the statement."
    "I honestly don't feel as though I've learnt that much from his lessons, let alone enough for them to come to an abrupt end."
    mike.say "Really, master?"
    show master at startle(0.05,-10)
    "He nods curtly."
    master.say "I have taught you all that I can...well, all that I can be bothered to."
    master.say "There's actually quite a lot more that I could teach you, but something's come up, and I have to attend to it."
    master.say "So I'm fast-tracking you to graduation - I'm pretty sure I've taught you all that you need to know...probably."
    "I guess that all I can do is shrug and go along with what he's saying."
    mike.say "Yes, Master - thank you."
    show master normal at startle(0.05,-10)
    pause 0.2
    play sound woosh_punch
    show master angry noglasses at center, zoomAt(1.5, (640, 1040))
    "The Master nods for a moment, and then suddenly adopts what looks rather like one of the stances guys use in martial arts movies."
    mike.say "Erm, Master...what are you doing?"
    master.say "Now your skills are complete, my pupil - it is time for you to show me what you have learned!"
    "Is he serious?"
    "Oh god, he really does look serious!"
    "Licking my lips and gritting my teeth, I try to copy his stance."
    "I'm paying him for this shit, so he has to go easy on me, right?"
    play sound woosh_punch
    show master angry noglasses at hshake, center, zoomAt(1.5, (840, 1040))
    "The Master makes some kind of whooping cry and comes at me with that uncanny speed and agility he shows on occasions."
    play sound woosh_punch
    with hpunch
    "I only just have time to see his fist coming from the left, and duck out of the way..."
    play sound woosh_punch
    show master at center, zoomAt (1.5, (640, 1040)) with MoveTransition(0.1)
    queue sound punch_hard
    pause 0.1
    with hpunch
    "Which allows him to neatly kick me straight in the groin."
    play sound body_fall
    scene bg beach at center, zoomAt(1.5, (640, 720))
    show master normal noglasses at center, zoomAt(1.5, (640, 720))
    with vpunch
    "Instantly I collapse onto the sand, curling up into a ball as I try to keep from vomiting."
    mike.say "You...you just kicked me in the balls...what kind of a martial art is that?!?"
    show bg beach at center, zoomAt(1.5, (640, 1080))
    show master wink at center, zoomAt(1.5, (640, 1040))
    with move
    "The Master smiles down at me as I roll around in agony."
    master.say "When I said there were no more lessons, I lied."
    master.say "This is the last lesson I will teach you, my boy."
    show master happy
    master.say "No amount of fancy martial arts is a match for a good, hard kick to the balls."
    master.say "Goodbye, and good luck, my pupil!"
    hide master with easeoutright
    "And with that, he walks off, chuckling to himself at my expense, in every possible sense of the word."
    "All I can do is lie there, clutching my groin and trying not to puke."
    $ hero.gain_skill("martial_arts")
    return

label train_beach:
    if hero.money >= 100:
        $ training_random = randint(1, 5)
        if training_random == 1:
            scene bg beach
            show master at center, zoomAt(1.5, (640, 1040))
            master.say "There you are, my pupil!"
            "I swear that there was no one in sight for as far as the eye can see when I turned my back a moment ago."
            "And that's how I justify jumping out of my skin and screaming like a little girl at the sound of the Master's voice."
            with vpunch
            mike.say "Arrggh!"
            show master wink
            "He smiles in amusement at my being taken completely by surprise, unable to hide the fact that he's pleased with himself at getting such a reaction."
            master.say "First things first!"
            "He holds out his hand in silence, waiting until I pull out a wad of notes and press it into his palm."
            play sound woosh_punch
            $ hero.money -= 100
            master.say "Very good - now the doors of the spiritual temple are open!"
            "I shake my head as I watch him pocket my money, wondering again if I've made a big mistake in trusting the old goat."
            master.say "Today, will work on your balance."
            hide master
            show chibi martialarts with fade
            "He turns and points to some of the pilings that run down the beach and into the sea."
            "Now this is something that I can relate to - everyone's seen the famous movie scene, haven't they?"
            "The one where the bullied kid learns that explosive kick by balancing on a piling just like those ones?"
            "The Master seems to notice my enthusiasm, and nods in approval."
            master.say "Shoes off, climb up - quickly now!"
            "Suddenly feeling a surge of excitement that comes mostly from retro eighties movies, I hurry to do as I'm told."
            "It's only when I actually get up there that I see the sheer amount of rough and splintered wood that I'm about to stand on with bare feet."
            mike.say "Erm...are you sure about this?"
            master.say "No questions - do as I say!"
            "At an honest guess, I'd say I manage to stay up there for all of five or six seconds before I simply can't take the pain any longer."
            hide chibi martialarts
            with vpunch
            "Falling off and rolling in the sand whilst wailing in agony, I hear the Master laughing at my expense for a second time."
            show master at center, zoomAt(1.25, (640, 880)) with fade
            master.say "Congratulations, boy - you have learned the TRUE subject of today's lesson."
            master.say "If someone tells you to do something stupid - don't do it!"
            hide master with easeoutright
            "He wanders off, still chuckling to himself as he leaves me to walk back to the car on all fours, cursing him for all I'm worth."
        elif training_random == 2:
            show master with dissolve
            "I find the Master already standing on the beach as I trudge towards him, his back turned as he stares out to sea."
            show master at center, zoomAt(1.5, (640, 1040)) with fade
            master.say "Good morning, my boy."
            "Without turning around, his hand reaches out and he rubs his fingers together in anticipation."
            "I let out a resigned sigh and pull out the roll of notes to pay for today's lesson."
            "The Master gives a gleeful little laugh at the feel of the money in the palm of his hand and then nods."
            play sound woosh_punch
            $ hero.money -= 100
            master.say "Today, you will learn all about endurance and patience."
            hide master
            show chibi martialarts
            with fade
            "From somewhere unseen, he produces a shovel and hands it to me."
            master.say "First of all - dig a hole, right here, five feet deep!"
            "He points to the sand by his feet, clearly meaning for me to literally dig the hole he just described."
            "I nod to show that I'm on the same page as him, and begin to dig as quickly as I can."
            "As soon as I have the hole dug, he points to the bottom with a bony finger."
            master.say "Now, get in the hole."
            "I look at him for a moment, just in case I heard him wrong."
            master.say "In the hole - NOW!"
            "The sudden yell makes me jump and hurry to obey as I scuttle into the hole."
            "As soon as I'm in there and looking up at him, the Master grabs to shovel and starts to drop the sand back into the hole."
            "I start to protest, but he silences he with a raised hand, and I so keep silent while he buries me up to my neck."
            master.say "Now, as the tide comes in, you will learn to be as enduring as the sea itself!"
            mike.say "Wait... what?!?"
            "Already I can see the tide fast approaching, rushing towards me as I'm trapped beneath the sand."
            "The first couple of waves don't quite reach my mouth, meaning that I can still shout for help."
            mike.say "Get me out of here!"
            master.say "If you truly believe that you can endure, then you will!"
            "The next waves are higher, almost filling my mouth with salt water as I yell at the Master for help."
            mike.say "Ack...gah...help me!"
            master.say "Mind over matter - endure!"
            mike.say "Endure my ass - get me out of here you crazy old bastard!"
            "I don't know if the reality of the situation dawns on the Master, or if he simply sees the chance of another hundred dollars slipping beneath the waves."
            "Either way, he scurries over and starts to dig my arms out of the sand."
            hide chibi martialarts
            with vpunch
            "With them free, I can finally drag myself out of the sand, still coughing and panting."
            show master at center, zoomAt(1.5, (640, 1040)) with fade
            master.say "Well, I think that was a lesson well learnt!"
            "In that moment, it's all I can do to keep from grabbing the shovel and swinging it at his head."
        elif training_random == 3:
            show master at center, zoomAt(1.5, (640, 1140)) with dissolve
            "I find the Master sitting cross-legged on the sand, apparently awaiting my arrival."
            "He has nothing at all with him, save for a gaudily-coloured bucket and spade, the kind a kid would bring to the beach."
            "I look at him expectantly, waiting for him to enlighten me either as to what today's lesson will be, or at least why he has the bucket and spade at his side."
            show master wink
            "The old man looks up at me with a grin on his face, and then holds up the palm of one hand, pointing to it with the index finger of his other."
            "I roll my eyes and produce the crumpled wad of bills to pay for the lesson, placing it in his eager hand."
            play sound woosh_punch
            $ hero.money -= 100
            "Once the money has been stashed away about his person, the Master leaps to his feet in one spry motion."
            show master happy
            master.say "Good morning, my young pupil."
            master.say "Today's lesson will teach you how, by focusing on the smallest of details, one can come to understand the world at large!"
            master.say "In the time of the Samurai, those legendary Japanese warriors would arrange flowers for the very same reason and to the very same end."
            hide master
            show chibi martialarts with fade
            "I glance around the beach, seeing nothing in any direction save for sand and sea."
            mike.say "But, there are no flowers around here!"
            "At this, the Master grins and thrusts out a hand holding the bucket and spade."
            master.say "That, my boy, is why you will be making sand-castles instead!"
            "As much as I protest, the Master silences my objections and insists."
            master.say "Arranging flowers, building sand-castles - there is no difference."
            master.say "Now do as you are bid!"
            "Resentfully, I set about filling the bucket with sand and tipping it upside down onto the ground."
            "My first attempts all crumble and disintegrate without exception, at which the Master lambastes my efforts."
            "Things get better when I hit a vein of wetter sand, the my next series of castles hold together almost completely."
            "By the time I'm feeling like I've got the hang of it, the Master is grudging in his praise, but seems proud of the progress I've made in such a short time."
            "It's only when I finally stand up and work the kinks out of my back that the sense of achievement drains away."
            hide chibi martialarts with fade
            "Now I can see the steady stream of surfers, joggers and dog-walkers passing by and hardly trying to hide the signs of their amusement at what they see."
            "A grown man, making sand-castles at the behest of a crazy-looking old coot!"
        elif training_random == 4:
            show master with dissolve
            "The Master meets me on the beach, but then waves for me to follow him as he makes his way towards the rockier portion of its length."
            show master at left with ease
            "Picking his way over the uneven terrain, he leads me by perhaps a dozen or so rock-pools, gazing into each as he passes them."
            scene bg beach at center, zoomAt(1.5, (640, 1080))
            show master at center, zoomAt(1.5, (640, 1040))
            with fade
            "Suddenly, he stops and becomes utterly fixated on one that, to me at least, looks little different to any of the previous ones."
            "I manage to catch his eye, and cock my head towards the pool that has him so fascinated, hoping to be enlightened as to just why."
            "He gives me a characteristic grin, and shakes his head as he holds out his hand."
            play sound woosh_punch
            $ hero.money -= 100
            "I grudgingly hand over the money for the lesson, and watch as his smile grows broader still."
            hide master
            show chibi martialarts with fade
            master.say "Look deep into the rock-pool, my boy - tell me what you see."
            "Wanting to get value for money, I do as I'm told."
            mike.say "All I see are a couple of crabs, Master."
            mike.say "Nothing special, really..."
            master.say "Nothing special, nothing special!"
            "The Master splutters in exasperation at my answer."
            master.say "A crab is nature's most perfect analogy of the armoured warrior, boy!"
            "He squats down on his haunches and holds his hands up in the air, then starts to scuttle left and right around the edge of the rock-pool."
            "For a moment I honestly think that he's finally succumbed to creeping senility."
            "But as he starts to snap his fingers and thumbs together, I realise that he's trying to imitate a crab."
            master.say "The crab moves with cunning and speed, and his armour is matched in potency by the snip-snapping of his claws!"
            master.say "To understand his method of fighting, you must spar with him, take him prisoner - you must capture him!"
            "The Master points at the rock-pool, and I find myself fishing around in the water a few moments later."
            "But the crabs are elusive and in their natural element, so they have little trouble evading my clumsy grasp."
            "Most that I catch are unlucky enough to pinch one of my fingers and be flung out of the water when I yelp in pain."
            "I wonder where these unfortunate crustaceans are ending up, and stop to look around for them."
            "It's then that I see the Master, a bucket in his hand into which he's dropping the crabs that he plucks off of the rocks."
            "He sees me watching him with a frown on my face, and he gives me a shrug and a grin in response."
            master.say "As well as being nature's answer to the armoured warrior, they're also very tasty in a soup or stew!"
            hide chibi martialarts
            show master at center, zoomAt(1.5, (640, 1040))
            with vpunch
            "Before I can say something suitably waspish in return, I yelp as yet another crab latches onto my finger."
            hide master with easeoutright
            "At this, the Master runs over, eagerly holding out his bucket before him."
        else:
            "I've walked up and down the beach a good few times before I finally manage to hear the sound of someone hissing at me from the dunes."
            show master at center, zoomAt(1.0, (1040, 740)) with dissolve
            "A quick scan of the closest of them shows me the face of the Master, leering at me from between two clumps of tall grass."
            "He waves me over, and I oblige him, stepping up my pace when I realise that he's urging me to come as quickly as I can."
            show master at center, zoomAt(1.5, (640, 1040)) with fade
            "Once I'm in amongst the dunes and squatting down next to him, I open my mouth to ask him just why we're hiding in here."
            "But he holds up a hand to silence my question even before I manage to get the words out."
            "Then I'm greeted by the familiar gesture of the hand reaching out for his money before he'll let us go any further."
            play sound woosh_punch
            $ hero.money -= 100
            "Resentfully, I hand over another portion of my hard-earned cash, and watch it disappear into his shirt pocket, never to be seen again."
            master.say "Today, our lesson will be one of stealth and evasion."
            hide master
            show chibi martialarts with fade
            "He reaches down into the grass at his feet and retrieves a camera that had apparently been there the whole time."
            master.say "Your task will be to emulate the mythical skills of the ninja."
            master.say "Specifically by taking this camera and capturing images of the unsuspecting bathers on the beach."
            "I narrow my eyes at this, wondering if I has more to do with sleaze than stealth."
            mike.say "Should I be looking for any type of bather in particular?"
            "The Master doesn't seem to see the obvious snare I've set for him, and nods intently."
            master.say "You should try to get the best shots you can of the young ladies in their bikinis."
            master.say "It's a scientific fact that a woman between the ages of eighteen and twenty-five possesses the most acute hearing of any human being."
            master.say "So they should prove the most challenging of all!"
            "Muttering under my breath about frauds and dirty old perverts, I crawl off through the dunes."
            "If I make it back from this one without being arrested as a Peeping Tom, I vow to test the Master's own hearing too."
            "Specifically by trying to sneak up on him and crack his skull with his own camera."
        $ game.set_flag("masterStory", 1, mod="+")
        $ NOTIFICATIONS.append(["{size=20}Martial arts " + str((game.flags.masterStory - 1) * 20) + "%{/size}", 2])
    else:
        "I don't have enough money for Master's lesson."
        $ hero.cancel_activity()
    return

label mike_meet_the_master:
label meet_the_master_male:
    "I don't normally spend much of my free time at the beach, but the weather was just so good today that I couldn't resist the temptation to pay a visit."
    "Of course, the great conditions mean that it's crawling with people by the time I arrive and try to weave my way to within at least a hundred feet of the water."
    "I spend most of my time twisting this way and that as I avoid a person coming one way and then have to dodge one coming in the opposite direction a moment later."
    "By my own estimation, I'm doing quite well up until the point that fate conspires to humiliate me in front of the beach-going crowds."
    "It's really nobody's fault, I just happen to be stepping aside for a couple of real beefcakes, when I slip on something underfoot and sprawl flat on my face."
    with vpunch
    "The beefy guys don't even see me go down, and consequently one of them accidentally kicks sand in my face as he walks past where I'm laid out."
    "As I splutter and cough with a mouthful of sand, the little knot of girls sitting closest to me can't help but burst out in laughter at my predicament."
    "Picking myself up and dusting off as much of the sand as I can manage, I see that they're shrugging in sympathy at the same time too."
    "Hey, I can understand that - I guess it was pretty funny, even if it did happen to me."
    "I shrug back and set off on my way again, trying to put the whole incident behind me and just get on with my day at the beach."
    "But as I draw near the dunes that border the beach itself, I hear a voice calling out to me."
    "Old pervert" "Psst...hey, you!"
    show master at center, zoomAt(1.0, (1040, 720)) with easeinright
    "I stop and survey the nearest dunes, and for my trouble I'm rewarded with the sight of a bald-headed old guy staring intently out at me from behind them."
    "He's wearing sunglasses and beach clothes, and is otherwise unremarkable save for his long, white goatee beard and moustaches."
    "Looking left and right first to make sure there's no one else around, I point to myself."
    "Old pervert" "Yeah, I mean you, kid - come over here!"
    "Intrigued enough to see what the strange old man has to say for himself, I oblige him."
    show master at center, zoomAt(1.25, (640, 880)) with fade
    "As soon as I'm within a few feet of him, the old man scuttles out of the dunes and begins to look me up and down."
    "Old pervert" "I saw what happened back there, son - I was watching the whole time!"
    "I'm about to ask him what he means by that, and why he was hidden in the dunes in the first place."
    "But then without warning, he jabs me in the chest with a bony finger."
    "Old pervert" "That's right, I saw those muscle-bound bullies shove you onto your ass in the sand."
    mike.say "Well, I actually kind of fell..."
    "The old man brushes my explanation aside with a shake of his hand."
    "Old pervert" "It's time you stopped making excuses, son!"
    "Old pervert" "I saw those girls laughing at you too!"
    "Old pervert" "The ones with the strappy bikinis and the huge...sunglasses sitting on the red towels!"
    mike.say "I was having a chuckle right along with them..."
    "Again, he waves me to silence."
    "Old pervert" "What you need, my boy, is someone to teach you how to defend yourself!"
    mike.say "I have taken some self-defense classes at the gym..."
    "Old pervert" "I'm talking about the ancient martial arts, son!"
    "Old pervert" "I am known as 'The Master' - you need to learn, and I can teach you!"
    show master happy at startle
    "He pauses and gives a little cough before continuing on."
    show master normal
    master.say "For the very reasonable sum of one hundred dollars per lesson..."
    menu:
        "Refuse":
            mike.say "A hundred dollars per lesson - that's daylight robbery, you silly old fart!"
            show master surprised
            "The old man seems genuinely taken aback, probably because he's used to gullible morons falling for his patter."
            master.say "Don't be foolish, my boy - this is a once-in-a-lifetime opportunity!"
            hide master
            show master surprised
            "I shake my head at his persistence, but start to walk away all the same."
            mike.say "Pardon me for saying so, but I always thought you found masters of martial arts in impressive dojos."
            mike.say "Not squatting in the dunes by the beach where they can see young skin on show and still toss themselves off without being seen!"
            hide master with dissolve
            "I can still hear him protesting as I round the curve of the beach and begin to leave him behind."
            "Chuckling to myself at the guy's audacity, I try to turn my attention to relaxing like I always intended to."
        "Accept":
            "Part of me is skeptical about his claims, but then aren't the movies full of martial arts masters that lead pretty normal, boring lives?"
            "I mean, that Miyagi guy was a plumber, wasn't he?"
            "Dismissing the old man's claims out of hand might be a big mistake."
            mike.say "Okay, 'Master', or whatever you say people call you - I'll give you a shot."
            show master happy
            "At this, a smile spreads across the old man's wrinkled face."
            master.say "Ah, trust me, son - you won't regret this!"
            "I look at him sideways, still not totally willing to trust him."
            mike.say "I'd better not, because if this all turns out to be a crock of shit, I'll want my money back!"
            show master wink at startle
            "The old man cackles and shakes his head at my words."
            show master normal
            master.say "That's good, boy - I'll teach you to stand up for yourself, just like that!"
            master.say "But don't worry about the money, this is more important than such petty material concerns."
            master.say "When I'm through with you, your mind and body will have been honed into a deadly weapon!"
            master.say "No one will ever kick sand in your face again!"
            "I give this declaration the best smile that I can summon, which is still pretty nervous."
            mike.say "Okay, great...when do we get started?"
            master.say "Meet me here when you are ready, my boy - and we will begin!"
            hide master with easeoutright
            "With that, he turns on his heel and disappears back into the dunes once more."
            "As I watch him go, I can't help wondering just what I'm getting into here!"
            $ game.flags.masterStory = 1
    "Most people just go to the beach to relax, but it's just my luck that I go along there and attract every nut job within a two-mile radius."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
