init python:
    Event(**{
    "name": "kylie_attack_ayesha",
    "label": "kylie_attack_ayesha",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasRoomTag("gym")),
        PersonTarget(ayesha,
            IsPresent(),
            Not(IsHidden()),
            MaxStat("sub", 75),
            MinStat("sexperience", 1),
            ),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("target", "ayesha"),
            MinStat("sub", 25),
            MinStat("yandere", 25),
            MaxStat("sexperience", 0),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": True,
    "quit": False,
    })

    InteractActivity(**{
    "name": "taming_date_ayesha",
    "label": "taming_date_restaurant",
    "money_cost": 200,
    "conditions": [
        "Harem.together(kylie, ayesha)",
        IsHour(18, 21),
        HeroTarget(
            MinStat("money", 200),
            HasStamina(),
            ),
        PersonTarget(ayesha,
            IsActive(),
            ),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            MinStat("sub", 35),
            Not(IsFlag("schedule", "jail")),
            ),
    ],
    "once_day": True,
    "icon": "kylie",
    "display_name": "Go on a date with Kylie and Ayesha",
    })

    InteractActivity(**{
    "name": "taming_date_kylie",
    "label": "taming_date_restaurant",
    "money_cost": 200,
    "conditions": [
        "Harem.together(kylie, ayesha)",
        IsHour(18, 21),
        HeroTarget(
            MinStat("money", 200),
            HasStamina(),
            ),
        PersonTarget(ayesha,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(kylie,
            IsActive(),
            MinStat("sub", 35),
            Not(IsFlag("schedule", "jail")),
            ),
    ],
    "once_day": True,
    "icon": "ayesha",
    "display_name": "Go on a date with Kylie and Ayesha",
    })

    InteractActivity(**{
    "name": "taming_event_03_a",
    "label": "taming_event_03_a",
    "conditions": [
        "Harem.together(kylie, ayesha)",
        IsTimeOfDay("afternoon"),
        HeroTarget(
            IsGender("male"),
            MinFlag("tamingDatesNumber", 2)),
        Or(
            IsDone("taming_date_kylie"),
            IsDone("taming_date_ayesha")
            ),
        Or(
            PersonTarget(ayesha,
                IsActive(),
                ),
            PersonTarget(kylie,
                IsActive(),
                )
            ),
        PersonTarget(ayesha,
            Not(IsHidden()),
            ),
        PersonTarget(kylie,
            Not(IsHidden()),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "icon": "date",
    "display_name": "Aquarium date with Kylie and Ayesha",
    "do_once": True,
    })

    InteractActivity(**{
    "name": "taming_event_04",
    "label": "taming_event_04",
    "conditions": [
        IsDone("taming_event_03_a"),
        IsTimeOfDay("afternoon", "evening"),
        "Harem.together(kylie, ayesha)",
        GameTarget(
            IsFlag("taming_harem_event_03", True),
            IsFlag("taming_delay", False),
            MinFlag("tamingDatesNumber", 3)
            ),
        HeroTarget(IsGender("male"),),
        Or(
            PersonTarget(ayesha,
                IsActive(),
                ),
            PersonTarget(kylie,
                IsActive(),
                )
            ),
        PersonTarget(ayesha,
            Not(IsHidden()),
            ),
        PersonTarget(kylie,
            Not(IsHidden()),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "duration": 2,
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "icon": "date",
    "display_name": "Home date with Kylie and Ayesha",
    "do_once": True,
    })

    InteractActivity(**{
    "name": "taming_event_05",
    "label": "taming_event_05",
    "conditions": [
        IsDone("taming_event_04"),
        IsTimeOfDay("afternoon", "evening"),
        "Harem.together(kylie, ayesha)",
        HeroTarget(
            IsGender("male"),
            MinFlag("tamingDatesNumber", 4),
            IsFlag("taming_delay", False)
            ),
        Or(
            PersonTarget(ayesha,
                IsActive(),
                ),
            PersonTarget(kylie,
                IsActive(),
                )
            ),
        PersonTarget(ayesha,
            Not(IsHidden()),
            ),
        PersonTarget(kylie,
            Not(IsHidden()),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "duration": 2,
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "icon": "date",
    "display_name": "Meet Kylie and Ayesha at home",
    "do_once": True,
    })

label kylie_attack_ayesha:
    scene bg gym
    "It might sound like I'm flattering myself here, but I'm pretty much religiously regular in attending the gym these days."
    "And even then, there are some days that are better than others, when you feel like you were just in the zone the whole time."
    "Today's certainly been one of those days for me, when I swear that I can already feel the physical benefits of my workout."
    "I can also put my hand on my heart and swear that I'm not getting high off of being so close to Hanna either."
    show ayesha b with dissolve
    "But then, maybe it's more on account of Ayesha's presence than that of the boss's daughter..."
    show ayesha b close at top_to_bottom
    "Even when she's not coaching me one-on-one, the sight of my favourite Amazon always seems to spur me on."
    "All that Ayesha needs to do is be glancing in my direction, and I feel like I could workout from dawn to dusk without stopping once!"
    "And it's weird, because before I met her, I never thought that a woman that buff could catch my eye."
    show ayesha b at bottom_to_top
    "But just the sight of in that skin-tight latex and I can feel my..."
    "Oops - I'm about to step into the shower, so I need to keep a lid on that!"
    "Otherwise I'd be better off taking a cold shower instead..."
    hide ayesha with dissolve
    "So with all of that in mind, I walk towards the male locker-room."
    "And the whole time I'm trying to think of something other than Ayesha's body."
    "Just as I duck in through the door, I see something that catches my eye."
    "It's nothing more than a flash of blonde hair, glimpsed in passing."
    "But it reminds me of something that I just can't place, bugging me as I get ready for a shower."
    "Once I'm in there and standing under the cascading water, I soon forget all about it anyway."
    "And that should have been the last of it, a passing thought that never springs to mind again."
    "I'm well on the way to forgetting all about it when I hear the first scream."
    "My head snaps around, and suddenly there's no room in my head for anything else."
    "Although I can't see where it's coming from, I can tell that it's at least a room away."
    "And as I follow my instincts and try to hurry towards the source, I start to hear raised voices too."
    kylie.say "I'm gonna fix you, bitch!"
    kylie.say "I'll slice you open - from one set of lips to the other!"
    ayesha.say "Oh yeah?"
    ayesha.say "Well all you've done so far is talk about it!"
    "Those are definitely female voices, and they're coming from the women's showers!"
    "I arrive in there a few moments later, almost skidding and falling on the wet tiles as I do so."
    show shower fight with fade
    "And instantly I recognise the blonde hair that I glimpsed on my way into the locker-room."
    "It's Kylie, and she's writhing around, naked on the floor!"
    "But more than that, she's struggling to escape the clutches of another, much larger woman too."
    "Even with the confusion of what's going on and the steam rising from the hot water, it's impossible to mistake her for anyone else."
    "The woman that's currently engaged in the task of grappling Kylie to the floor is none other then Ayesha."
    "And it has to be said that she's doing a pretty good job of it too!"
    "Ayesha has her legs wrapped around Kylie's middle like a pair of pincers."
    "Her arms are just as securely encircling the other girl's throat too."
    "Kylie struggles ineffectually against the larger girl's professional wrestling hold."
    show shower fight press pain with dissolve
    "But even as I watch, her face is turning red, and her eyes are starting to roll back into her head."
    $ love = min(ayesha.love, kylie.love)
    if love < 100:
        if ayesha.love <= kylie.love:
            mike.say "Ayesha - what in the hell are you doing?!?"
            "At the sound of my voice, Ayesha's eyes fix upon me."
            "For a moment I actually think she's too far gone to answer me."
            "But then she lets out an explosive lungful of breath."
            ayesha.say "Just...urgh...taking out some...argh...trash!"
            "The effort it's taken for Ayesha to answer me means she's had to loosen her grip a little."
            "I hear Kylie suck in a ragged gasp, and the she starts to plead her own case."
            kylie.say "Help me...[hero.name]...she's choking...me!"
            "In the confusion of the moment, all I can see is Kylie on the brink of passing out."
            mike.say "Ayesha, let her go - NOW!"
            "Ayesha looks at me in disbelief, but she starts to do it all the same."
            ayesha.say "You weren't here when we got started, [hero.name]."
            ayesha.say "She's crazy - she tried to kill me!"
            mike.say "So what?"
            mike.say "You're going to kill her now?"
            mike.say "Is that how it is, Ayesha?!?"
            $ ayesha.love -= 50
            hide shower fight
            show ayesha naked sad at right4
            show kylie naked at top_mostleft
            with fade
            "Ayesha finally lets Kylie go, and she scuttles away to the opposite side of the showers."
            "Once there, she sits with her back against the wall and one hand on her bruised throat."
            show ayesha at startle
            ayesha.say "NO!"
            ayesha.say "Of course not..."
            mike.say "Well that's how it looked from where I was standing!"
            "Ayesha climbs slowly to her feet, opening her mouth to say something in reply."
            "But then she looks away from me and shakes her head, clearly thinking better of it."
            hide ayesha with moveoutleft
            "She wastes no time in stalking out of the showers, leaving me alone with Kylie."
            "I turn around, thinking to comfort Kylie, only to have her literally throw herself into my arms!"
            hide kylie
            show kylie naked happy at center, zoomAt(2.0, (640, 1340)) with hpunch
            $ kylie.love += 10
            kylie.say "Oh, [hero.name], you saved my life!"
            kylie.say "I was SO scared!"
            mike.say "There, there, Kylie."
            mike.say "You're safe now - I won't let her hurt you anymore..."
            "It's only as I'm stroking Kylie's hair and patting her back that I notice something out of place."
            "A box-cutter on the floor of the showers."
            "Make a mental note to ask Kylie where it came from once she's calmed down."
            "I just hope that I don't forget between now and then..."
        else:
            "I can see what's happened here, as clearly as if I'd been in the room when it went down."
            "And I don't need to be walked through it to know what role the box-cutter in the corner played either!"
            mike.say "Ayesha - are you okay?!?"
            $ ayesha.love += 10
            "At the sound of my voice, Ayesha's eyes fix upon me."
            "For a moment I actually think she's too far gone to answer me."
            "But then she lets out an explosive lungful of breath."
            ayesha.say "Just...urgh...taking out some...argh...trash!"
            "The effort it's taken for Ayesha to answer me means she's had to loosen her grip a little."
            "I hear Kylie suck in a ragged gasp, and then she starts to plead her own case."
            kylie.say "Help me...[hero.name]...she's choking...me!"
            mike.say "Ah, shut up, Kylie!"
            mike.say "Or maybe don't - pass out and do us all a favour!"
            "Kylie looks at me in disbelief, her eyes wider than I've ever seen them."
            kylie.say "She's crazy, [hero.name] - she's trying to kill me!"
            mike.say "Sure thing, Kylie, yeah."
            $ kylie.yandere += 25
            mike.say "And I guess you just happened to be in here with a blade in your hand?"
            "Kylie starts to protest again, but I can already see that her eyes are becoming dull."
            "And it doesn't take long for Ayesha's iron grip to put her to sleep."
            "As the larger girl releases her hold and Kylie's unconscious body flops onto the floor, I rush over to her."
            hide shower fight
            show ayesha naked at center, zoomAt(2.0, (640, 1340))
            with fade
            mike.say "Ayesha - are you okay?"
            "She's panting from the exertion of it all."
            show ayesha happy
            "But there's still a wry smile on Ayesha's face as she turns towards me."
            ayesha.say "Yeah, I'm fine, [hero.name]."
            ayesha.say "I never let her get any use out of the blade."
            mike.say "Ayesha, you can NEVER do anything like that again."
            mike.say "Do you understand me?"
            "Ayesha looks at me, clearly unprepared for the intensity of my words."
            show ayesha blush
            ayesha.say "W...why, [hero.name]?"
            ayesha.say "Are you pissed at me for hurting her?"
            mike.say "No, Ayesha - nothing like that."
            mike.say "I just can't stand the thought of anyone hurting you!"
            $ ayesha.love += 10
            "Now she looks genuinely shocked, her eyes wide with surprise."
            "Gently, she leans her forehead against mine, and we stand together under the cascading water of the showers..."
    else:
        "I have no idea what's going on here, or what could have lead to this crazy situation."
        "All I can do is shake my head in disbelief and demand an explanation."
        mike.say "Shit - what in the hell's going on here?"
        "At the sound of my voice, Ayesha's eyes fix upon me."
        "For a moment I actually think she's too far gone to answer me."
        "But then she lets out an explosive lungful of breath."
        ayesha.say "Just...urgh...taking out some...argh...trash!"
        "The effort it's taken for Ayesha to answer me means she's had to loosen her grip a little."
        "I hear Kylie suck in a ragged gasp, and the she starts to plead her own case."
        kylie.say "Help me...[hero.name]...she's choking...me!"
        "I shake my head in frustration, not fully believing either of them."
        mike.say "Ayesha, let her go - now!"
        mike.say "And Kylie, you shut your mouth too!"
        "Ayesha relents, letting Kylie out of the hold in which she had her pinned."
        hide shower fight
        show ayesha naked at right4
        show kylie naked sad at top_mostleft
        with fade
        "As soon as she's free, Kylie crawls hastily to the far side of the showers."
        "She presses her back to the wall, clutching at her bruised throat."
        mike.say "Now would one of you mind telling me what REALLY happened?"
        show kylie at left with move
        kylie.say "I had to do it, [hero.name]."
        kylie.say "She's trying to take you away from me!"
        "Kylie all but wails the words, pleading with me to see it from her side."
        "Ayesha shakes her head, clearly less than impressed with this explanation."
        ayesha.say "If you need to fight off the competition with a blade, you've already lost, bitch!"
        mike.say "Wait a minute..."
        mike.say "Are you two fighting over me?"
        show kylie at startle
        kylie.say "YES!"
        show ayesha at startle
        ayesha.say "NO!"
        ayesha.say "Well, kind of...I guess..."
        mike.say "The two of you do know that they just made polygamy legal in this country, don't you?"
        show kylie normal
        kylie.say "Well...yeah..."
        ayesha.say "What's that got to do with it?"
        mike.say "You can always share me - learn to get along together."
        "As if sensing a chance to gain the upper hand, Kylie all but leaps on my suggestion."
        show kylie happy
        kylie.say "I can do that, [hero.name], you'll see!"
        ayesha.say "What...now you just wait a damn minute!"
        mike.say "So that's decided then?"
        show kylie normal
        mike.say "No more crazy from you, Kylie."
        mike.say "And no more violence from you, Ayesha."
        mike.say "From now on, we're one happy threesome!"
        mike.say "Because caring is sharing - say it!"
        show kylie happy
        "Kylie smiles at this, eagerly nodding and clapping her hands."
        kylie.say "Sure thing, [hero.name] - caring is sharing!"
        "Ayesha shakes her head in confusion, as if she's not sure exactly what just went down."
        ayesha.say "Uh...sharing is caring...I guess..."
        "But all the same, I note that she doesn't come out and shoot the idea down either..."
        $ Harem.join_by_name("taming", "ayesha", "kylie")
    return

label taming_date_restaurant:
    if not game.flags.tamingDatesNumber:
        call taming_event_1 from _call_taming_event_1
    elif game.flags.tamingDatesNumber:
        call taming_event_1_repeated from _call_taming_event_1_repeated
    $ game.flags.tamingDatesNumber += 1
    $ game.pass_time(4)
    return

label taming_event_1:
    scene bg door restaurant with fade
    "After the way our relationship got started, I sense that there might be a bit of lingering tension between Ayesha and Kylie."
    "But even with such a dramatic introduction to each other, there's no reason that they can't learn to get along."
    "And that's why I decide that what the three of us really need is to start behaving like a regular trio as soon as possible."
    "To this end, I take it upon myself to book us a table at one of the nicer restaurants in the city."
    "And as far as Ayesha and Kylie are concerned, I don't take no for an answer from either of them..."
    "On the actual day, I arrange to meet the pair of them at the actual restaurant."
    "This way I figure that we'll all be arriving on equal terms and there's less chance of an argument developing."
    "But the thought hits me that this could be the perfect chance for Ayesha and Kylie to spend a little time together."
    "And so I take care to ensure that I get there just a little later than the time that we actually agreed upon."
    scene bg restaurant with fade
    "When I finally do arrive what greets me is the sight of both girls sitting at the table in the middle of a pretty chilly silence."
    "Kylie has her hands planted firmly on her hips and Ayesha her hands crossed over her chest."
    "And though neither of them is saying a word now, I can't help feeling they've just had a fiery exchange of some sort."
    "If I were less worldly wise than I am, I'd have instantly asked what was up."
    show kylie date angry at Transform(ypos=0.2, xpos=-0.15, zoom=1.5)
    show ayesha a date annoyed at Transform(ypos=0.2, xpos=0.45, zoom=1.5)
    with dissolve
    "But as neither of them seems to be about to enlighten me, that's all the permission I need to ignore it completely."
    mike.say "Hey, girls!"
    "Note that I'm referring to them in the plural?"
    "That way there's no chance for one of them to assume that they rank higher in my estimation than the other."
    "Just sign me up as a diplomat and have done with it!"
    show ayesha normal
    show kylie happy
    ayesha.say "Hey, [hero.name]."
    kylie.say "Oh, hi there, [hero.name]."
    kylie.say "You're here at last!"
    "Well, no prizes for guessing who the award for putting on a show of sweetness and light goes to today!"
    mike.say "Sorry I'm a little late."
    mike.say "I was just on my way out the door when something came up!"
    show kylie normal
    "Kylie frowns and pouts a little, looking disappointed to have come second to something in my life."
    show kylie happy
    kylie.say "Aww, that's okay, [hero.name]."
    kylie.say "You're here now, and that's what matters!"
    show kylie normal
    "As if sensing that she's being outdone by the other girl, Ayesha gives me a weak smile."
    ayesha.say "I'm glad to see you too, [hero.name]."
    ayesha.say "But you already knew that, right?"
    "I nod and smile, knowing full well that Ayesha means what she says."
    mike.say "I feel like I should be the one thanking you girls."
    mike.say "You both look so good tonight, I feel like the luckiest guy in the world!"
    show kylie happy
    show ayesha blush
    "Kylie, being more used to this kind of compliment, instantly laps it up."
    "But I see that Ayesha looks bashful, averting her eyes as she smiles."
    "All the same, she seems to be deeply affected by the praise, liking it despite her evident embarrassment."
    mike.say "Anyway..."
    mike.say "My throat's getting dry from singing your praises."
    mike.say "So let's order some drinks, okay?"
    show ayesha normal
    show kylie normal
    "At the mention of alcohol, Kylie claps her hands together in glee."
    "Ayesha nods in agreement, and I sense that she could use a drink to ease her nerves."
    "Casting my gaze around the restaurant, I manage to catch the attention of a nearby waitress."
    "She nods without pause or hesitation, knowing from experience what's being asked of her."
    "I swear that I didn't notice this when she was all the way over on the other side of the room."
    "But the moment the waitress gets close to the table, it's obvious that she's pretty damn cute."
    "Don't get me wrong, I'm not interested in any girls other than Ayesha and Kylie right now."
    "I'm just not going to deny the obvious either."
    "Waitress" "Good evening, Sir...and ladies..."
    "Waitress" "Would you like to see the drinks menu?"
    show kylie angry
    show ayesha annoyed
    "I see both Ayesha and Kylie bristle at the way the waitress mentions them almost as an afterthought."
    "A mistake that she only makes worse by handing me a wine-list and dropping the others on the table for them to pick up."
    "Waitress" "If I may, Sir?"
    "Waitress" "We have some rather nice choices on offer tonight..."
    "The waitress then proceeds to lean in pretty close as she points to the drinks in question."
    "She's so near to me that I can smell her perfume, almost feel her hair brushing my face..."
    kylie.say "Urgh..."
    kylie.say "Why don't you just offer yourself up as the main course!"
    kylie.say "Or doesn't this place serve half-baked tarts?!?"
    "The waitress suddenly reels back, clearly stung by Kylie's unexpected outburst."
    "I see that she's already clutching at her purse, and I wonder if there's a box-cutter in there tonight..."
    menu:
        "Let Kylie rage at the waitress":
            $ kylie.flags.dateHandled = "kylie"
            ayesha.say "Hey, you better calm the hell d..."
            "Ayesha's head spins around and she looks art me in surprise."
            "But I keep a hold of her wrist, having just grabbed it under the table."
            "And then I shake my head quickly, letting her know that I want her to leave it alone."
            "Ayesha looks like she's going to wrench her hand free and ignore me."
            show ayesha normal
            "But then she nods, and I feel her entire body begin to relax."
            "Meanwhile, the show is just getting started."
            "Waitress" "I...I..."
            $ kylie.sub -= 4
            $ kylie.yandere += 2
            kylie.say "What's the matter, bitch?"
            kylie.say "You had no trouble talking to my man a second ago!"
            show kylie date angry zorder 1 at Transform(ypos=0.05, xpos=0.05, zoom=1.7) with move
            "Kylie rises from her seat and leans in as close to the waitress as she did to me."
            "And then she hisses right into the poor, trembling girl's ear."
            kylie.say "Now you listen to me, you little slut."
            kylie.say "You use that tongue of yours to say yes and no."
            kylie.say "You speak when you're spoken to - or else I'll cut it out!"
            "The waitress practically jumps in fear, nodding and cowering at the threat."
            show kylie normal
            "Suddenly, the hatred and bile just seems to drain from Kylie's face."
            show kylie happy at Transform(ypos=0.2, xpos=-0.15, zoom=1.5) with move
            "By the time she's back in her seat, she's all smiles again, like nothing happened."
            "Ayesha looks at me, her eyes wide with amazement."
            "But all I can do is shrug it off and turn my attention back to the wine list."
        "Let Ayesha put Kylie in her place":
            $ kylie.flags.dateHandled = "ayesha"
            ayesha.say "Hey, you better calm the hell down, Kylie!"
            "Suddenly, all of Kylie's attention is off of the waitress and focused on Ayesha instead."
            "The poor girl almost seems to stumble backwards, as if released from a physical force."
            "But my attention is solely on the confrontation that's about to go down right in front of me."
            kylie.say "What, and let this little slut flirt with [hero.name]?"
            kylie.say "She's doing it right under our noses, Ayesha!"
            kylie.say "And she needs to be put in her place..."
            "I see Kylie's hand reach for her purse, pretty much confirming my fears about the box-cutter."
            show kylie date angry
            "But luckily for everyone concerned, Ayesha sees it too."
            show ayesha date annoyed behind kylie at Transform(xpos=0.05) with move
            "Before Kylie knows what she's doing, the larger girl's hand shoots out and seizes her wrist."
            show kylie date angry at hshake
            kylie.say "HEY!"
            kylie.say "GET THE F..."
            $ ayesha.sub -= 8
            $ kylie.sub += 4
            show ayesha normal
            "Her words are cut off as Ayesha uses her other hand to cover Kylie's mouth."
            "Kylie struggles and makes muffled sounds that are probably supposed to be the foulest curses imaginable."
            "But none of it seems to bother Ayesha in the slightest, who merely smiles back at her the whole time."
            ayesha.say "I'm sorry, Miss."
            ayesha.say "But my companion here is somewhat lacking in the social graces."
            "The waitress herself doesn't seem to know what to make of the scene playing out before her."
            "She smiles nervously and lets out a peal of laughter."
            "But the look in her eyes tells me that Ayesha's probably made even more afraid then she was before!"
            mike.say "Maybe it's best if you give us a couple of minutes to peruse this?"
            "I hold up the wine-list and give the waitress the best smile I can manage."
            show ayesha a date at Transform(ypos=0.2, xpos=0.45) with move
            "She nods and hurries away, careful to be far away when Ayesha finally lets Kylie go."
        "Take control of the situation":
            $ kylie.flags.dateHandled = "hero"
            with hpunch
            "My hand shoots out and grabs Kylie's arm at the wrist."
            "And then I pull it under the table and keeping her from digging into her purse."
            "But a second later, I see Ayesha move towards the other girl, and I grab her wrist too."
            "Now I have them both held down and their undivided attention, I glare at them over across the table."
            show kylie sad
            show ayesha sad
            $ kylie.sub += 2
            $ ayesha.sub += 2
            kylie.say "Hey!"
            ayesha.say "[hero.name], what gives?!?"
            mike.say "I'm sorry, Miss."
            mike.say "But it seems that my companions have forgotten their table manners."
            mike.say "Would you mind excusing us for a couple of minutes?"
            mike.say "I'm sure we'll be ready to order our drinks by then."
            "The waitress nods and smiles at this."
            "But I can see in her eyes that she's more than eager to leave us well enough alone."
            "As soon as she's gone, I let go of Ayesha and Kylie's hands."
            mike.say "You mind telling me what the fuck that was about, huh?"
            show kylie normal
            kylie.say "She was flirting with you!"
            "Kylie whines as she makes a point of rubbing her wrist."
            ayesha.say "And SHE was going to cut her for it!"
            "For her own part, Ayesha looks like she's ready to kill Kylie, box-cutter or no box-cutter!"
            "I hate to have to play the man in charge."
            "But what other choice have they left me here?"
            mike.say "I thought we agreed that there's be no more crazy, Kylie?"
            kylie.say "Yeah, but..."
            mike.say "No - no buts!"
            mike.say "I'm not getting caught out in public with Jack the Ripper in panties!"
            $ kylie.sub += 2
            "I hear Ayesha snigger at this, and instantly turn my attentions to her next."
            mike.say "And just what were you planning on doing to her, Ayesha?"
            mike.say "Powerslam her through the goddamn table?!?"
            mike.say "Save that stuff for the wrestling ring, okay?"
            $ ayesha.sub += 2
            "I look from one to the other, not happy until I get a grudging nod from each."
    show ayesha normal
    show kylie normal
    "Once the scene is over and done with, the still nervous waitress returns to finally take our orders."
    "And while there are some harsh glances shot across the table between Ayesha and Kylie, it seems the hostilities are at an end."
    $ kylie.love += 2
    $ ayesha.love += 2
    "The rest of the night goes pretty well, all things considered, almost like we're a perfectly normal trio."
    "I'm compelled to leave a large tip out of guilt, but I take heart from making Ayesha and Kylie chip in too."
    $ hero.money -= 200
    call taming_threesome_fuck from _call_taming_threesome_fuck
    return

label taming_event_1_repeated:
    show bg restaurant
    "After the way the last date went down, I must admit I was a little nervous about a repeat performance from Kylie and Ayesha."
    "But regardless of what went down during the evening, the night ended well, so it was decided we'd give it another go."
    "And that's how I found myself once again making my way towards our local restaurant."
    "I hope to any powers that be that Ayesha and Kylie behave themselves this time."
    if kylie.flags.dateHandled == "kylie":
        "Goodness knows I don't need Kylie blowing up like that again. Perhaps I need to reconsider how best to curb her \"enthusiasm\"..."
    elif kylie.flags.dateHandled == "ayesha":
        "Although the way Ayesha handled Kylie last time was rather impressive. Perhaps I should let her reign Kylie in more often."
    elif kylie.flags.dateHandled == "hero":
        "If I'm to keep a firm hand on the situation like last time, I'll need to keep my wits about me."
    "As the restaurant comes into view, I'm greeted by the view of Ayesha and Kylie looking less than pleased, although, I must admit, better than last time."
    "Fingers crossed that they don't come to blows this time, and hopefully learn to enjoy one another's company."
    show kylie date angry at center, zoomAt(1.5, (340, 1140))
    show ayesha date at center, zoomAt(1.5, (940, 1140))
    with dissolve
    "When I finally do arrive what greets me is the sight of both girls sitting at the table talking quietly, which honestly surprises me a bit."
    "Perhaps they're beginning to feel comfortable with each other. You'd hope so with how well things ended last time."
    mike.say "Hey, girls!"
    show ayesha happy
    show kylie happy
    ayesha.say "Hey, [hero.name]."
    kylie.say "[hero.name]!"
    if hero.charm >= 50:
        mike.say "You two are looking particularly gorgeous this evening!"
        $ kylie.love += 1
        $ ayesha.love += 2
    else:
        mike.say "I hope I didn't make you two wait too long."
        "Waving me off, they assure me that they weren't."
    show kylie normal
    "Grinning while I take a moment to admire them, I speak up."
    mike.say "Have you guys had the opportunity to take a look at the menu? Any ideas on what you're thinking of having for dinner?"
    show ayesha normal
    "Ayesha chuckles, and mentions something about steak."
    ayesha.say "Although, I'm more looking forward to dessert."
    "Now if you've never seen a tiger hunting, I don't know how I could explain the experience."
    "The look in Ayesha's eyes and the way she licks her lips leaves me gulping, worried if I'll survive what is to come."
    "Kylie pouts cutely, watching the by-play with invested interest."
    "So of course this is when a waitress shows up at our table. Honestly, I'm just grateful it isn't the same one from last time."
    "Already, I can see Kylie stiffen, and I reach over and pre-emptively given her leg a reassuring squeeze."
    "Waitress" "Good evening, Sir...and ladies..."
    "Waitress" "Would you like to see the drinks menu?"
    show kylie angry at startle
    show ayesha annoyed
    "I see both Ayesha and Kylie bristle at the way the waitress mentions them almost as an afterthought."
    "A mistake that she only makes worse by handing me a wine-list and dropping the others on the table for them to pick up."
    "I'm honestly just concerned. How is it even possible to get a similarly behaving waitress as last time?"
    "Waitress" "If I may, Sir?"
    "Waitress" "We have some rather nice choices on offer tonight..."
    "The waitress then proceeds to lean in pretty close as she points to the drinks in question."
    "She's so near to me that I can smell her perfume, almost feel her hair brushing my face..."
    kylie.say "Urgh..."
    kylie.say "Why don't you just offer yourself up as the main course!"
    kylie.say "Or doesn't this place serve half-baked tarts?!?"
    "The waitress suddenly reels back, clearly stung by Kylie's unexpected outburst."
    "I see that she's already clutching at her purse, and I wonder if there's a box-cutter in there tonight..."
    menu:
        "Let Kylie rage at the waitress":
            ayesha.say "Hey, you better calm the hell d..."
            "Ayesha's head spins around and she looks art me in surprise."
            "But I keep a hold of her wrist, having just grabbed it under the table."
            "And then I shake my head quickly, letting her know that I want her to leave it alone."
            "Ayesha looks like she's going to wrench her hand free and ignore me."
            show ayesha normal
            "But then she nods, and I feel her entire body begin to relax."
            show kylie angry
            "Meanwhile, the show is just getting started."
            "Waitress" "I...I..."
            $ kylie.sub -= 4
            $ kylie.yandere += 2
            kylie.say "What's the matter, bitch?"
            kylie.say "You had no trouble talking to my man a second ago!"
            show kylie angry at center, zoomAt(1.5, (340, 1040)) with move
            "Kylie rises from her seat and leans in as close to the waitress as she did to me."
            "And then she hisses right into the poor, trembling girl's ear."
            kylie.say "Now you listen to me, you little slut."
            kylie.say "You use that tongue of yours to say yes and no."
            kylie.say "You speak when you're spoken to - or else I'll cut it out!"
            "The waitress practically jumps in fear, nodding and cowering at the threat."
            show kylie normal
            "Suddenly, the hatred and bile just seems to drain from Kylie's face."
            show kylie happy
            "By the time she's back in her seat, she's all smiles again, like nothing happened."
            "Ayesha looks at me, her eyes wide with amazement."
            "But all I can do is shrug it off and turn my attention back to the wine list."
        "Let Ayesha put Kylie in her place":
            ayesha.say "Hey, you better calm the hell down, Kylie!"
            "Suddenly, all of Kylie's attention is off of the waitress and focused on Ayesha instead."
            "The poor girl almost seems to stumble backwards, as if released from a physical force."
            "But my attention is solely on the confrontation that's about to go down right in front of me."
            kylie.say "What, and let this little slut flirt with [hero.name]?"
            kylie.say "She's doing it right under our noses, Ayesha!"
            kylie.say "And she needs to be put in her place..."
            "I see Kylie's hand reach for her purse, pretty much confirming my fears about the box-cutter."
            "But luckily for everyone concerned, Ayesha sees it too."
            show ayesha date annoyed at center, zoomAt(1.5, (900, 1140)) with move
            "Before Kylie knows what she's doing, the larger girl's hand shoots out and seizes her wrist."
            show kylie at startle
            kylie.say "HEY!"
            kylie.say "GET THE F..."
            $ ayesha.sub -= 8
            $ kylie.sub += 4
            show ayesha normal
            "Her words are cut off as Ayesha uses her other hand to cover Kylie's mouth."
            "Kylie struggles and makes muffled sounds that are probably supposed to be the foulest curses imaginable."
            "But none of it seems to bother Ayesha in the slightest, who merely smiles back at her the whole time."
            ayesha.say "I'm sorry, Miss."
            ayesha.say "But my companion here is somewhat lacking in the social graces."
            "The waitress herself doesn't seem to know what to make of the scene playing out before her."
            "She smiles nervously and lets out a peal of laughter."
            "But the look in her eyes tells me that Ayesha's probably made even more afraid then she was before!"
            mike.say "Maybe it's best if you give us a couple of minutes to peruse this?"
            "I hold up the wine-list and give the waitress the best smile I can manage."
            "She nods and hurries away, careful to be far away when Ayesha finally lets Kylie go."
        "Take control of the situation":
            with hpunch
            "My hand shoots out and grabs Kylie's arm at the wrist."
            "And then I pull it under the table and keeping her from digging into her purse."
            "But a second later, I see Ayesha move towards the other girl, and I grab her wrist too."
            "Now I have them both held down and their undivided attention, I glare at them over across the table."
            $ kylie.sub += 2
            $ ayesha.sub += 2
            kylie.say "Hey!"
            ayesha.say "[hero.name], what gives?!?"
            mike.say "I'm sorry, Miss."
            mike.say "But it seems that my companions have forgotten their table manners."
            mike.say "Would you mind excusing us for a couple of minutes?"
            mike.say "I'm sure we'll be ready to order our drinks by then."
            "The waitress nods and smiles at this."
            "But I can see in her eyes that she's more than eager to leave us well enough alone."
            "As soon as she's gone, I let go of Ayesha and Kylie's hands."
            mike.say "You mind telling me what the fuck that was about, huh?"
            show kylie sad
            kylie.say "She was flirting with you!"
            "Kylie whines as she makes a point of rubbing her wrist."
            show ayesha annoyed
            ayesha.say "And SHE was going to cut her for it!"
            "For her own part, Ayesha looks like she's ready to kill Kylie, box-cutter or no box-cutter!"
            "I hate to have to play the man in charge."
            "But what other choice have they left me here?"
            mike.say "I thought we agreed that there's be no more crazy, Kylie?"
            kylie.say "Yeah, but..."
            mike.say "No - no buts!"
            mike.say "I'm not getting caught out in public with Jack the Ripper in panties!"
            $ kylie.sub += 2
            "I hear Ayesha snigger at this, and instantly turn my attentions to her next."
            mike.say "And just what were you planning on doing to her, Ayesha?"
            mike.say "Powerslam her through the goddamn table?!?"
            mike.say "Save that stuff for the wrestling ring, okay?"
            $ ayesha.sub += 2
            "I look from one to the other, not happy until I get a grudging nod from each."
    show ayesha normal
    show kylie normal
    "Once the scene is over and done with, the still nervous waitress returns to finally take our orders."
    "And while there are some harsh glances shot across the table between Ayesha and Kylie, it seems the hostilities are at an end."
    $ kylie.love += 2
    $ ayesha.love += 2
    "The rest of the night goes pretty well, all things considered, almost like we're a perfectly normal trio."
    "I'm compelled to leave a large tip out of guilt, but I take heart from making Ayesha and Kylie chip in too."
    $ hero.money -= 200
    scene bg street
    show ayesha date at right5
    show kylie date at left5
    with fade
    menu:
        "Go home":
            call taming_threesome_fuck from _call_taming_threesome_fuck_1
        "Go to the night club" if game.flags.tamingDatesNumber and hero.money >= 200:
            $ hero.money -= 200
            call taming_event_2 from _call_taming_event_2
    return

label taming_event_2:
    scene bg street
    show ayesha date at right5
    show kylie date at left5
    "Being seen on a date with Ayesha and Kylie is a pretty crazy experience, for more than the obvious reasons too!"
    "I mean sure, polygamy's only just become legal over here, and so it's still unusual to see threesomes out in public."
    "And they make a pretty striking pair of girls, there's no way of denying that fact."
    "But then I know something that other people don't - that their personalities are an explosive combination as well!"
    "That's one of the reasons that I insisted on choosing the nightclub that we're going to hit tonight."
    "My hope is that if they're both on neutral ground there's less chance of them clashing with one another."
    "And it seems to be paying off as we stand in the queue and wait to get into the place."
    "Neither Ayesha nor Kylie seems to be wanting to pick a fight."
    "Which means I get to simply bask in the reflected glory of having them both on my arm."
    show bg nightclub with fade
    "But almost the moment that we get inside, the first potential problem rears it's ugly head."
    ayesha.say "Ah..."
    ayesha.say "Could we grab a drink, [hero.name]?"
    ayesha.say "My throat's feeling kind of dry..."
    mike.say "Sure thing, Ayesha."
    mike.say "The bar's just over..."
    show kylie happy at startle
    show fx exclamation at left5
    kylie.say "WOW - this is like my favourite song EVER!"
    kylie.say "We HAVE to dance to it - right now!"
    show ayesha annoyed
    "Ayesha rolls her eyes at this, clearly not pleased with Kylie's demand."
    "And I have to admit, I find it a little suspect myself."
    "Kylie's never mentioned this song before now."
    "But then she does look super keen to get onto the dance floor."
    mike.say "Well, the bar doesn't look too busy."
    mike.say "And the song only just started too."
    menu:
        "Go to the bar":
            mike.say "Why don't you find us a place on the dance floor, Kylie?"
            ayesha.say "Yeah, Kylie - we can grab you a drink too."
            "Ayesha's tone doesn't sound nearly as conciliatory as my own."
            "And for a moment, I honestly think that Kylie's going to stamp her foot and refuse."
            "But then I see a forced smile appear on her face, and she nods."
            kylie.say "Okay...okay, fine."
            kylie.say "Just be quick about it, yeah?"
            "Kylie turns around and makes for the dance floor."
            $ ayesha.love += 1
            hide kylie
            hide ayesha
            show ayesha date happy
            with dissolve
            "Which leaves Ayesha and I alone as we walk over to the bar."
            ayesha.say "Thanks for that, [hero.name]."
            mike.say "Huh..."
            mike.say "Thanks for what, Ayesha?"
            ayesha.say "For understanding that I needed a moment to gather myself."
            ayesha.say "I always get nervous when I'm out somewhere like this."
            ayesha.say "I need to acclimatise myself before I can go with it."
            mike.say "Oh, sure thing, Ayesha."
            mike.say "I understand completely."
        "Go to the dance floor":
            mike.say "Why don't you grab us all some drinks from the bar, Ayesha?"
            kylie.say "Yeah, Ayesha - we can save a place for us on the dance floor."
            "Kylie's tone doesn't sound nearly as conciliatory as my own."
            "And for a moment, I honestly think that Ayesha's going to flat out refuse."
            "But then I see a forced smile appear on her face, and she nods."
            ayesha.say "Yeah, sure thing."
            ayesha.say "I guess that makes sense."
            "Ayesha turns around and walks towards the bar."
            $ kylie.love += 1
            hide kylie
            hide ayesha
            show kylie date happy
            with dissolve
            "Which leaves Kylie free to grab me by the wrist and haul me onto the dance floor."
            kylie.say "I just knew you'd understand, [hero.name]."
            mike.say "Huh..."
            mike.say "Understand what, Kylie?"
            kylie.say "That I needed to have you all to myself."
            kylie.say "Even if it is for just a little while!"
            mike.say "Ah...okay, Kylie."
            mike.say "I guess..."
    hide kylie
    hide ayesha
    show kylie date happy at left5
    show ayesha date happy at right5
    with fade
    "Pretty soon we're all on the dance floor with a drink in our hands."
    "And as far as I'm concerned, the disagreement is a fast becoming a distant memory."
    "I mean, it's easy to forget something like that when you're dancing with Ayesha and Kylie."
    "Each way I turn, there's a seriously hot girl doing her best to get close to me."
    "Before too long, I'm literally sandwiched between the two of them."
    "I can feel the eyes of the other club-goers on me, almost sense their jealousy!"
    "But then I start to feel that there's some jealousy far closer to home as well."
    "With Ayesha dancing on one side of me and Kylie on the other, they begin trying to outdo each other."
    "Soon enough the glances that they're shooting as almost sharp enough to cut yourself on."
    "I need to do something before this gets out of hand."
    "Giving one of them my undivided attention is the only solution that springs to mind."
    "But which one of them should I give it to?"
    menu:
        "Dance with Ayesha":
            "Sure, she's the more physically imposing of the pair."
            "But that doesn't mean Ayesha's the toughest when it comes to her emotions."
            hide ayesha
            hide kylie
            show dance ayesha date
            with fade
            $ ayesha.love += 1
            "And that's why I wrap my arms around her waist, pulling her into an embrace."
            "Ayesha doesn't resist for a moment, and I feel her firm muscles press against me."
            "Before I know it, she slips her tongue between my lips, kissing me passionately."
            "I don't know if she can feel it, but my cock becomes as stiff as a board in response."
            "My intention had been to say something to Kylie."
            "Something that I hoped would explain my choice to her."
            "But now all I can think of doing is pulling Ayesha as close to me as possible."
            "In that moment, she's literally all that I can think about."
        "Dance with Kylie":
            "Ayesha's a big girl, she can look after herself for a couple of minutes."
            "And I already know how emotionally fragile Kylie can be in a situation like this."
            hide ayesha
            hide kylie
            show dance kylie date
            with fade
            $ kylie.love += 1
            "Which is why I put my hands on her hips and pull her towards me."
            "But it's not like Kylie needs any encouragement either."
            "What I had intended to be me embracing her quickly turns into her almost grabbing me."
            "Kylie presses her lips against mine, forcing me to return her kiss."
            "And then her tongue darts between them, probing my mouth."
            "Don't get the impression that I'm complaining for a moment."
            "I get hard almost as soon as Kylie's body is pressed against mine."
            "And the whole time that it is, I can't spare as much as a thought for Ayesha."
    hide dance
    show ayesha date at left5
    show kylie date at right5
    "But it's not like one of the girls can have me to herself the whole night."
    "And almost as soon as the kiss comes to an end, we're back dancing as a threesome."
    "I have no idea of just how long we've been on the dance floor."
    "Just that I'm starting to feel the effects of all this dancing."
    "My throat feels pretty parched too, like I could do with a drink."
    "So I make a time-out gesture and lead the girls off of the dance-floor."
    mike.say "Sorry, ladies."
    mike.say "But I need to rehydrate or I'll drop!"
    show kylie happy
    "Kylie nods with enthusiasm."
    "But I can tell that she's eager to get back to it."
    kylie.say "Well hurry up and grab a drink then, [hero.name]."
    kylie.say "We've still got a couple of hours before this place closes!"
    show ayesha annoyed
    "Ayesha shakes her head."
    "She looks shocked at the very idea of getting back on the dance floor."
    ayesha.say "You've got to be joking!"
    ayesha.say "I'm feeling fit to drop."
    ayesha.say "Couldn't we get a taxi and go back to your place, [hero.name]?"
    menu:
        "Stay longer":
            mike.say "I just wanted to take a break, Ayesha."
            mike.say "Once I've had a drink, I'll be good to go for another hour or more!"
            mike.say "If you're feeling tired, how about you sit out for a while?"
            kylie.say "Yeah, Ayesha."
            kylie.say "Or you could jump in that taxi you mentioned."
            kylie.say "Don't worry - I'll make sure [hero.name] gets home safe and sound!"
            $ ayesha.love -= 1
            show ayesha sad
            "For a moment I think that Ayesha's going to rise to the bait."
            "Either that or she's actually going to punch Kylie in the teeth!"
            ayesha.say "No, it's fine."
            ayesha.say "I can keep up with you guys."
            "And she's as good as her word too."
            "We stay perhaps another hour or two in the club, dancing the whole time."
            "I can't be sure, but I think Kylie looks bummed Ayesha didn't go home early."
            "But whatever..."
            "All it means is that we're all exhausted by the time we actually leave."
            "So much so that it's a battle to stay awake in the taxi back to my place."
        "Call it a night":
            mike.say "Maybe you're right, Ayesha."
            mike.say "I am feeling pretty beat."
            mike.say "And I want to leave some energy for when we get back to my place!"
            show kylie sad
            $ kylie.love -= 1
            kylie.say "Aww...boring!"
            kylie.say "I'm still in the mood for dancing!"
            show ayesha normal
            ayesha.say "You could stay here, Kylie."
            ayesha.say "Don't worry - I'll make sure [hero.name] gets home safe and sound!"
            "Kylie narrows her eyes, suddenly aware of the fact she's being played."
            show kylie normal
            "She curls her lip and then shakes her head, not willing to be duped."
            kylie.say "Nah, it's okay."
            kylie.say "I'm tired too."
            kylie.say "I was just gonna stay because [hero.name] wanted to."
            scene bg taxi with fade
            pause 0.5
            show bg taxi car with dissolve
            "That decided, we head outside and hail a taxi."
            "Leaving a little earlier than planned means we're wide awake on the ride home."
            "And there's no need to fight to stay awake before we reach my place!"
    call taming_threesome_fuck from _call_taming_threesome_fuck_2
    return

label taming_threesome_fuck(appointment=None):
    scene bg house
    if game.week_day % 2 == 0:
        show ayesha date at right5
        show kylie date at left5
        with fade
        if not appointment:
            "The memory of what just went down at the restaurant is still fresh in my mind when we get back to my place."
            "And to be honest, I don't know whether to be embarrassed, pissed off or just plain turned on by the way the girls behaved."
            "But in the end, the sight of them pretty much fighting to be the one leading me to the bedroom makes up my mind."
            "How can I be anything other than turned on at the prospect?"
        kylie.say "Come on, [hero.name]."
        kylie.say "I know the way!"
        show ayesha annoyed
        ayesha.say "Hey - I'm standing right here!"
        ayesha.say "And how come you know the way to [hero.name]'s bedroom, huh?"
        kylie.say "Ah..."
        kylie.say "I mean I don't..."
        kylie.say "I'm just guessing, that's all."
        kylie.say "Why would I know my way around [hero.name]'s house?!?"
        show kylie blush
        kylie.say "It's not like I've wandered around the place when he was out!"
        ayesha.say "Wait...what?!?"
        kylie.say "Never mind - here's the bedroom now!"
        "Before I can even say a word, Kylie pushes open my bedroom door."
        scene bg bedroom1 with fade
        show kylie date at right4
        show ayesha date at top_mostright
        with moveinright
        "Ayesha stops talking too, the sight of my bed seeming to snap her out of it."
        "I know that she pretends to be above the kind of games Kylie likes to play."
        "But she looks determined not to let herself be outdone on this occasion."
        ayesha.say "Enough talking already."
        ayesha.say "Time for some action."
        show ayesha at right5
        show kylie date at left5
        with move
        "With that, Ayesha strides into the middle of the room."
        "She makes no effort to drag me in her wake."
        show ayesha sport topless
        "Instead she kicks off her shoes and then begins to strip off her clothes."
        "Now I've seen Ayesha working out in skin-tight spandex - more times than I care to confess."
        "And yet somehow it just doesn't compare to the sight of what she's doing right now."
        "Seeing that lithe, powerful and yet undeniably feminine form revealed so slowly, so teasingly..."
        "I can almost feel myself shivering with desire for her!"
        kylie.say "Humph!"
        "I barely hear the sound of Kylie harrumphing next to me."
        "But it makes sense - Ayesha's show of effortless confidence, how powerful she seems in her femininity..."
        "Well, it kind of makes Kylie's antics seem more than a little childish in comparison!"
        kylie.say "Wait up, Ayesha."
        kylie.say "Maybe [hero.name] wants to see what a girl looks like naked too!"
        show ayesha blush
        "Kylie giggles with wicked delight as Ayesha's cheeks flush at the insult."
        show ayesha normal
        show kylie underwear
        "But by the time she might have been able to fire back, the other Kylie's already stripping off too."
        "And from there it becomes a far more pleasurable experience for me, as they compete for my attention!"
        "It's all I can do to remember that I need to strip off my clothes too."
        show ayesha naked
        show kylie naked
        "My attention is all on the sight of Ayesha and Kylie's naked forms."
        "They make such a striking contrast to one another it's a turn-on in of itself."
        "Ayesha's all athletic muscle and alluring strength."
        "Kylie's so voluptuous and soft to the touch."
        "It's like there's nothing more I could want in a girl that one of them doesn't have!"
        "But it looks like there's something that both Ayesha and Kylie want for themselves right now."
    else:
        if not appointment:
            "Any feeling of tiredness and fatigue is soon forgotten as the taxi drops Ayesha, Kylie and I at my place."
            "It's like all of the competition that exists between the two girls suddenly becomes a positive thing."
            "And that's because the pair of them are now completely devoted to showing me a good time."
            "By which I mean a REALLY good time!"
            "We practically fall through the front door as I try to open it."
            scene bg livingroom
            "That's because I have Ayesha leaning on one side of me and Kylie on the other."
            "Both of them are alternating between using their mouths to whisper promises to me and kiss my neck."
        show ayesha date at right5 with dissolve
        ayesha.say "Hurry up, [hero.name]."
        ayesha.say "Or else I'm gonna drag you up those stairs!"
        show kylie date at left5 with dissolve
        kylie.say "Not without me you're not!"
        kylie.say "I'm going to hold him so close - never let him go..."
        mike.say "Hey..."
        mike.say "Hey!"
        "Reluctantly they both stop long enough for me to catch my breath."
        mike.say "Keep it down until we're in my room."
        mike.say "We can wake my housemates up once we're behind a closed door."
        mike.say "But if they catch us at it on the stairs..."
        mike.say "Well...I'd never live it down!"
        "I can see that the possibility is at least on their minds."
        "And for a moment I think that they might actually do it."
        "That they might actually jump me on the stairs and to hell with the consequences."
        "But then they both nod, and we hurry upstairs to my bedroom."
        scene bg bedroom1 with fade
        show kylie date at right4
        show ayesha date at top_mostright
        with moveinright
        "I close the door and finally breathe a sigh of relief."
        mike.say "Okay..."
        mike.say "How are we going to do this?"
        "I say this as I turn around."
        show ayesha at right5
        show kylie date at left5
        with move
        "But before I'm even facing them, I feel two pairs of hands seize me."
        "Without as much as a second of hesitation, Ayesha and Kylie begin to manhandle me."
        "Together they strip off every shred of clothing that I'm wearing."
        "Tossing it aside without a care, they don't stop until I'm completely naked."
        ayesha.say "Take the weight off, [hero.name]."
        "And with that, she shoves me backwards..."
        "Luckily for me, they've backed me across the room without my noticing."
        "This means that I land on the bed, rather than the floor."
        "All I can do is lie there and watch as Ayesha and Kylie begin to strip off themselves."
        "My eyes dart between them as it becomes apparent this is a battle for my attention."
        "Both of them try to remove each and every item of clothing as suggestively as possible."
        "And the result is that I think I'm going to lose control of my eyes!"
        show ayesha sport topless
        show kylie underwear
        "By the time they're down to their underwear, my cock is rock hard."
        "I can almost feel their own eyes focus on it."
        "I can sense the hunger that the sight is causing them."
        "And I see them both begin to lick their lips as they advance on me from either side."
        "Without as much as a word, Ayesha and Kylie kneel down at the side of the bed."
        show ayesha naked
        show kylie naked
    menu:
        "Ask for a blowjob" if ayesha.sub >= 50 and kylie.sub >= 50:
            call taming_blowjob from _call_taming_blowjob
        "Just fuck them" if ayesha.sub >= 50 and kylie.sub >= 50:
            pass
    show taming threesome with fade
    if renpy.has_label("taming_harem_achievement_2") and not game.flags.cheat:
        call taming_harem_achievement_2 from _call_taming_harem_achievement_2
    "I watch as both of them climb onto the bed and try to beckon me towards them."
    "Looks like it's time that I made a choice."
    "But which one of them is going to get what they both want?"
    menu:
        "Fuck Ayesha":
            $ first = "ayesha"
            "Ayesha and Kylie are both sitting up on their haunches as I walk over to the bed."
            "But there's something in Ayesha's eyes that makes me veer towards her at the last moment."
            "I hear Kylie moan in disappointment, but I can't tear my gaze away from Ayesha."
            "She watches me in silence the entire time, turning her head as I crawl around behind her."
            "It's like she knows what's coming, what's on my mind to do to her right now."
            "And I can see from the expression on her face that she wants it - badly!"
            "My cock's hard even before my hands touch Ayesha's firm buttocks."
            "But the shiver that goes through her when I do seals the deal."
            show taming threesome left
            "I guide her gently up and onto all fours, lining myself up at the same time."
            call taming_threesome_ayesha_fuck from _call_taming_threesome_ayesha_fuck_1
        "Fuck Kylie":
            $ first = "kylie"
            "Ayesha and Kylie are both sitting up on their haunches as I walk over to the bed."
            "But there's something in Kylie's eyes that makes me veer towards her at the last moment."
            "I hear Ayesha moan in disappointment, but I can't tear my gaze away from Kylie."
            "It's just that wicked, almost crazy look she gets in her eyes at times like this."
            "Part of me just knows that it always means trouble."
            "And yet I want to feed it all the same!"
            "Kylie's eyes follow me as I move around behind her."
            "I can hear her almost panting in anticipation as I push her up and onto all-fours."
            show taming threesome right
            "She doesn't need to say a word - I already know just how much she wants this!"
            call taming_threesome_kylie_fuck from _call_taming_threesome_kylie_fuck_1
    "I'm feeling exhausted, almost too tired to keep myself from closing my eyes."
    if first == "ayesha":
        "But then I see the way that Kylie's looking at me right now."
        "She looks disappointed and hurt, but mainly horny as hell!"
        "And I feel guilty for having ignored her in favour of Ayesha."
        menu:
            "Fuck Kylie too" if hero.stamina:
                call taming_threesome_kylie_fuck from _call_taming_threesome_kylie_fuck_2
            "I'm too tired":
                "But I'm just too spent to do anything about it."
                "So she'll have to wait her turn."
            "Deny her tonight" if kylie.sub >= 50:
                "Call me cruel if you want, but I kinda like the idea of curbing Kylie's \"passion\" in a healthier direction"
                mike.say "Did you enjoy watching that Kylie?"
                "She simply licks her lips, and swallows audibly. I think I can even see some of her juices leaking in response, despite her hurt at not being satisfied tonight."
                $ kylie.love -= 4
                $ kylie.sub += 6
    elif first == "kylie":
        "But then I see the way that Ayesha's looking at me right now."
        "She looks disappointed and hurt, which makes that much hotter!"
        "And I feel guilty for having ignored her in favour of Kylie."
        menu:
            "Fuck Ayesha too" if hero.stamina:
                call taming_threesome_ayesha_fuck from _call_taming_threesome_ayesha_fuck_2
            "I'm too tired":
                "But I'm just too spent to do anything about it."
                "So she'll have to wait her turn."
            "Deny her tonight" if ayesha.sub >= 50:
                "Deciding I want to try messing with our relationship dynamic a bit, I smirk in her direction."
                mike.say "I think that concludes tonight's festivities. Don't you think Ayesha?"
                "Looking down sadly, Ayesha just quietly nods her head."
                $ ayesha.love -= 10
                $ ayesha.sub += 6
    return

label taming_threesome_ayesha_fuck:
    if first == "ayesha":
        $ ayesha.love += 4
    else:
        show taming threesome left
    menu:
        "Fuck her ass" if hero.sexperience >= 20:
            "Everything feels so firm and tight back here."
            "So much so that I ignore the promise of softness that Ayesha's pussy offers."
            "And instead I pull her buttocks further apart, exposing her ass in the process."
            ayesha.say "Ah..."
            ayesha.say "[hero.name], what are you doing?"
            "I'm surprised at Ayesha's surprise."
            "I expected something like this to be no sweat for an Amazon and a pro-wrestler!"
            "But rather than stopping, I begin to push the head of my cock into her ass."
            ayesha.say "Oh, [hero.name]..."
            ayesha.say "I don't know about this..."
            mike.say "Don't worry, Ayesha - I'll be gentle."
            "I mean what I'm saying, but I'm also buying myself time."
            "Because I can feel that I'm reaching that sweet spot in Ayesha's ass."
            "The point where resistance turns into acceptance and pain into pleasure."
            ayesha.say "Oh..."
            $ ayesha.sub += 2
            ayesha.say "Oh, [hero.name]..."
            "And there it is."
            "The point where Ayesha's muscles stop pushing back and begin to pull me in."
            "I feel her tremble as her entire body begins to melt under the pressure."
            "And only now do I start to move inside of her."
            "I go slowly at first, letting her get used to the sensation."
            "But then I begin to move faster, thrusting in and out with ever greater speed."
            show taming threesome ayesha_moan
            "By now, Ayesha's totally enthralled, taken over by the experience."
            "I'm riding her like she was some kind of thoroughbred racehorse."
            "And it's not like she's trying to throw me off either!"
            "Now that she's accepted what I'm doing to her, Ayesha seems to be loving it too."
            "In fact, her entire body is quivering from the sensation of my cock in her ass."
            "The muscles around it are already squeezing it like a fist."
            "And I can feel myself fast approaching my limit..."
            menu:
                "Cum inside":
                    "But the fact that I'm so deep into Ayesha's ass is no reason to stop."
                    with vpunch
                    "In fact, it means that I can redouble my efforts as I reach my climax."
                    show taming threesome ayesha_ahegao with vpunch
                    "And by the time I let go, filling her with all I have, Ayesha's is gasping for mercy."
                    with vpunch
                    "The cum is already seeping out of her as I pull my cock out too."
                    $ ayesha.love += 2
                    "It slips out with a satisfying sound, accompanied by Ayesha's exhausted moans."
                "Pull out":
                    "It seems a waste to just shoot my load inside of Ayesha's ass."
                    "And so I slide my cock out of her with a satisfying sound."
                    "Ayesha moans in disappointment, turning to look at me over her shoulder."
                    $ ayesha.sub += 2
                    with vpunch
                    "Which is the very same moment that I shoot my load, catching her square in the face."
                    with vpunch
                    "She yelps in surprise as the cum spatters across her nose and cheeks."
                    "And then it runs down her face, dripping into her open mouth and off of her chin."
            $ ayesha.flags.anal += 1
        "Fuck her pussy":
            "Everything about Ayesha is just so firm and tight."
            "So can you really blame me for seeking out her pussy?"
            "The moment that the head of my cock rubs against it, I know it's what I want."
            "And the moan that Ayesha let's out in the same moment doesn't do any harm either!"
            "I pause only for a moment, considering if I can be bothered sheathing myself before sinking into her."
            $ CONDOM = False
            if hero.has_condom():
                menu:
                    "Use protection" if hero.has_condom():
                        $ CONDOM = hero.use_condom()
                    "Don't use protection":
                        pass
            ayesha.say "Mmm..."
            mike.say "What was that, Ayesha?"
            ayesha.say "Hmm..."
            ayesha.say "That feels good..."
            ayesha.say "Please, [hero.name]..."
            "I don't need any more encouragement than that."
            "And as soon as I begin to push my cock into her, I know I made the right choice."
            if not CONDOM and ayesha.love < 150:
                "Gasping a bit, she looks back at me with a little worry in her eyes, but says nothing."
            "Unlike the rest of her body, Ayesha's pussy feels like it's melting around me."
            "Sure, she's firm and I can feel the muscles inside of her squeezing me the whole time."
            "With any other girl, this would feel incredible."
            "But with Ayesha, it's like discovering a whole new side to her."
            "Her true femininity is so plain to see."
            "The undeniable beauty of her body too."
            "Her strength and stature only seem to add to that too."
            "She's like a thoroughbred mare, perfect in every way possible."
            "All of this inspires me to take an even firmer hold of Ayesha's haunches."
            "And before too long, I'm thrusting in and out of her with all my might."
            "She takes everything that I have to give her without a moment's hesitation."
            "Her strong body absorbing the pounding that I'm giving her effortlessly."
            "But it's not like what she takes is simply lost either."
            "Instead I can feel every thrust I make translated into the reactions of Ayesha's body."
            "She quivers and trembles on the end of my cock, threatening to cum before I do."
            "Which makes it all the more inevitable that I'm going to lose it myself..."
            menu:
                "Cum inside":
                    "But the fact that I'm so deep into Ayesha's pussy means all I want is to stay there to the end."
                    "In fact, it means that I redouble my efforts as I reach my climax."
                    with vpunch
                    "And by the time I let go, filling her with all I have, Ayesha's is gasping for mercy."
                    with vpunch
                    if not CONDOM:
                        $ ayesha.impregnate()
                        if ayesha.love >= 150 or ayesha.sub >= 50:
                            $ ayesha.love += 2
                            "She groans with satisfaction at the sensations travelling through body."
                        else:
                            $ ayesha.love -= 2
                            "The worried look is back, but is assuaged with a reassuring squeeze of her rump."
                    with vpunch
                    "The cum is already seeping out of her as I pull my cock out too."
                    "It slips out with a satisfying sound, accompanied by Ayesha's exhausted moans."
                "Pull out":
                    "It seems a waste to just shoot my load inside of Ayesha's pussy."
                    if CONDOM:
                        "And so I slide my cock out of her with a satisfying sound, whipping off the condom in a follow-up motion."
                    else:
                        "And so I slide my cock out of her with a satisfying sound."
                    "Ayesha moans in disappointment, turning to look at me over her shoulder."
                    with vpunch
                    "Which is the very same moment that I shoot my load, catching her square in the face."
                    $ ayesha.sub += 2
                    with vpunch
                    "She yelps in surprise as the cum spatters across her nose and cheeks."
                    "And then it runs down her face, dripping into her open mouth and off of her chin."
        "Use the rope" if "bondage_ropes" in hero.inventory and hero.has_skill("shibari") and kylie.sub >= 75:
            call taming_bondage_ayesha_fuck from _call_taming_bondage_ayesha_fuck
            $ kylie.sub += 3
            $ ayesha.love += 4
    $ ayesha.sexperience += 1
    return

label taming_threesome_kylie_fuck:
    if first == "kylie":
        $ kylie.love += 4
    else:
        show taming threesome right
    menu:
        "Fuck her ass" if hero.sexperience >= 20:
            "But it's not only Kylie that can act on the spur of the moment."
            "You know, get a crazy impulse and follow it through, consequences be damned?"
            "Which is why I don't hesitate to part her buttocks and push my cock between them."
            kylie.say "Whoa..."
            kylie.say "So that's where this thing is going?!?"
            mike.say "Is that a problem, Kylie?"
            "She looks back over her shoulder at me, that same crazy look in her eyes."
            kylie.say "No problem, [hero.name]."
            $ kylie.sub += 2
            kylie.say "You can have me ANY way you want me!"
            "It's just as Kylie says this that my cock sinks into her ass."
            show taming threesome kylie_moan
            "And the look of surprised delight that appears on her face seals the deal."
            "Despite the natural resistance of her muscles, I push on with all my strength."
            "Kylie moans a little at first."
            "But then she begins to almost yelp with enthusiasm at my efforts."
            kylie.say "Ah..."
            kylie.say "Ooh..."
            kylie.say "Yeah, [hero.name]..."
            kylie.say "Just...like...that!"
            "I was keen on fucking Kylie up the ass to begin with."
            "But the sounds that she's making and the way she seems to want it..."
            "I can't help getting swept up in the moment!"
            "Pretty soon this means that I'm pounding away at Kylie without mercy."
            "Her ass and thighs are ample enough to take this kind of treatment."
            "And the more I give her, the more eagerly she seems to soak it up."
            mike.say "Oh shit..."
            mike.say "Kylie..."
            kylie.say "Mmm..."
            kylie.say "Are you gonna cum, [hero.name]?"
            kylie.say "Are you gonna cum in my ass, huh?"
            "Whatever I was going to do before she said that doesn't matter anymore."
            "Because now all I know is that my body's about to answer Kylie's question..."
            menu:
                "Cum inside":
                    "Kylie's right on the money, as she finds out a couple of seconds later."
                    "With one final thrust, I shove my cock as deep into her ass as it'll go."
                    with vpunch
                    "And before I can take another breath, I shoot my load."
                    show taming threesome kylie_ahegao with vpunch
                    kylie.say "Oh...oh fuck!"
                    with vpunch
                    $ kylie.love += 2
                    kylie.say "That feels good...so good!"
                "Pull out":
                    "Wanting to surprise her, I pull my cock out of Kylie's ass a second before I cum."
                    show taming threesome kylie_blush with vpunch
                    "She looks over her shoulder, wondering what the hell just happened."
                    with vpunch
                    "Just in time to get a the whole thing straight in the face."
                    kylie.say "Hey, what gives..."
                    with vpunch
                    kylie.say "Oooo..."
                    $ kylie.sub += 2
                    "With her mouth open, Kylie can't help but swallow the largest part of it."
                    "She coughs while the rest of it spatters her cheeks and drips from her chin."
            $ kylie.flags.anal += 1
        "Fuck her pussy":
            "Maybe what Kylie really needs is to be grounded for a moment."
            "To be reminded of the simple pleasures that come from keeping things straight-up and natural."
            "Which is why I aim the head of my cock straight for her pussy."
            kylie.say "Mmm..."
            kylie.say "Come on in, [hero.name]."
            kylie.say "You don't even have to knock!"
            "As much as I know where her opinions lie, I pause for a moment to consider my actions."
            $ CONDOM = False
            if hero.has_condom():
                menu:
                    "Use protection":
                        $ CONDOM = hero.use_condom()
                    "Don't use protection":
                        pass
            "The moment past, I line myself up against her opening."
            "And she's not kidding either."
            "Almost the same moment the head of my cock presses against the lips of Kylie's pussy, it slips inside."
            "She's just so wet and willing that there's no need to do more than push a little and I'm in deep."
            "But that's not to say that I find her loose either."
            "The muscles in Kylie's pussy begin to squeeze against me as soon as I'm all the way in her."
            $ kylie.love += 2
            kylie.say "Ooh..."
            kylie.say "Now that feels GOOD!"
            "It feels pretty damn good from my end too."
            "But somehow hearing Kylie say it makes the feeling all the more intense."
            "The sound of her voice spurs me on to begin thrusting in and out faster than ever."
            "And the way this makes her moan with pleasure only serves to encourage me more."
            "Soon enough it's like we're both feeding the fire more with each second that passes."
            "Kylie's ass and thighs are ample enough to take this kind of treatment."
            "And the more I give her, the more eagerly she seems to soak it up."
            mike.say "Oh fuck..."
            mike.say "Kylie..."
            kylie.say "Hmm..."
            kylie.say "What...up..."
            kylie.say "You...gonna...cum...[hero.name]?"
            kylie.say "Gonna...cum...inside...me?"
            "Whatever I was going to do before she said that doesn't matter anymore."
            "Because now all I know is that my body's about to answer Kylie's question..."
            menu:
                "Cum inside":
                    "Kylie's right on the money, as she finds out a couple of seconds later."
                    "With one final thrust, I shove my cock as deep into her folds as it'll go."
                    with vpunch
                    "And before I can take another breath, I shoot my load."
                    if not CONDOM:
                        $ kylie.impregnate()
                    $ kylie.love += 2
                    show taming threesome kylie_ahegao with vpunch
                    kylie.say "Oh...oh fuck!"
                    with vpunch
                    kylie.say "That feels good...so good!"
                "Pull out":
                    "Wanting to surprise her, I pull my cock out of Kylie's pussy a second before I cum."
                    "She looks over her shoulder, wondering what the hell just happened."
                    with vpunch
                    "Just in time to get a the whole thing straight in the face."
                    kylie.say "Hey, what gives..."
                    $ kylie.sub += 2
                    with vpunch
                    kylie.say "Oooo..."
                    with vpunch
                    "With her mouth open, Kylie can't help but swallow the largest part of it."
                    "She coughs while the rest of it spatters her cheeks and drips from her chin."
    $ kylie.sexperience += 1





    return

label taming_blowjob:
    scene taming blowjob with fade
    if renpy.has_label("taming_harem_achievement_2") and not game.flags.cheat:
        call taming_harem_achievement_2 from _call_taming_harem_achievement_2_1
    "Eyes still fixed on my cock, they lean in until they're close enough to touch it."
    "Ayesha reaches out and puts a hand on my balls, stroking them gently."
    "Kylie is quick to copy the move, but she squeezes with more force."
    show taming blowjob ayeshaopen kylieopen
    "And then, almost as one, they start to lick at the base of the shaft."
    show taming blowjob ayeshaclosed
    "Neither of them actually touches the other as they do this."
    "But the whole time their tongues are so close it feels like they're working as one."
    show taming blowjob kylieclosed
    "Ayesha and Kylie begin to work their way higher."
    "Their tongues climb my cock at an achingly slow pace."
    show taming blowjob ayeshasurprised kyliesurprised ayeshasmile kyliesmile
    "I see them lock eyes."
    "And for a moment I think that their rivalry might ruin the whole thing."
    "But then they return to licking away at my cock without incident."
    show taming blowjob ayeshaclosed kylieclosed ayeshaopen kylieopen
    "I suppose that neither of them wants to be the one that spoiled the blowjob for me!"
    "Instead they seem to be intent on outdoing the other and earning my praise."
    "So all I can really do is sit back and appreciate their efforts."
    "Ah, life can be so hard sometimes!"
    "It almost feels like Ayesha and Kylie have settled into a rhythm."
    "Their tongues feel so good as they caress my cock."
    "And by the time they make it all the way to the head, I can feel the blood pounding in my ears."
    show taming blowjob ayeshaclosed kylieopened ayeshasuck
    "At the very tip, Ayesha and Kylie begin to use their lips almost as much as their tongues."
    show taming blowjob kylieclosed ayeshaopened kyliesuck
    "They're kissing the head now, trying to get as much of it in their mouths as they can."
    show taming blowjob ayeshaclosed kylieopened ayeshasuck
    "This means that they're also close enough for their lips to touch."
    show taming blowjob kylieclosed ayeshaopened kyliesuck
    "And they do, making it feel like my cock is right in the middle of a passionate kiss."
    "My breathing is hard and heavy by now."
    show taming blowjob ayeshaclosed kylieclosed ayeshaopen kylieopen -kyliesuck
    "I can feel that there's not much I can do to hang on..."
    show taming blowjob cumshot ayeshaopened kylieopened with vpunch
    "When I cum a few moments later, droplets hit Ayesha and Kylie on the nose and cheeks."
    show taming blowjob dickcum ayeshaonmouth kylieonmouth -cumshot with vpunch
    "But some weird chance means that the majority of it runs down the shaft of my cock."
    "It flows like wax down a candle, and the girls hurry to lap up as much as they can."
    "Their tongues work tirelessly, so very little actually is left to reach the base."
    "Afterwards, Ayesha and Kylie recline on the bed."
    "They lick the last of the cum from their lips and fingertips."
    "And they remind me of nothing so much as a pair of satisfied cats."
    "Their appetites sated bye the starters, but waiting for the main course."
    return

label taming_bondage_ayesha_fuck:
    hide taming threesome
    show ayesha naked stuned at right5
    show kylie naked stuned at left5
    with fade
    "Ayesha and Kylie both stop and stare at the ropes that I've spread out on the bed to make tonight that little bit more interesting."
    "But I can also see just how different their individual reactions are, and it reminds me of the stark contrast in their characters."
    "Ayesha, for all that she's physically imposing, seems almost shocked to see ropes and imagine the uses we might put them to."
    "Kylie, on the other hand, has a light in her eyes that speaks of intrigue and even excitement at the possibilities they represent."
    show ayesha surprised
    ayesha.say "Ah, [hero.name]..."
    ayesha.say "What's all of this stuff for?"
    show ayesha surprised
    kylie.say "Are you for real, Ayesha?"
    show kylie talkative
    kylie.say "Don't tell me you've never heard of bondage?!?"
    show kylie annoyed
    show ayesha angry
    ayesha.say "Of course I have!"
    show ayesha whining
    ayesha.say "I just...I just never got involved in it before."
    show ayesha sadsmile
    "I offer Ayesha what I hope is a reassuring smile."
    "I don't want to scare her off before we even get started."
    mike.say "Don't worry, Ayesha."
    mike.say "We'll take it slow, okay?"
    show ayesha blush
    ayesha.say "I...I don't know..."
    mike.say "You don't have to do anything that feels uncomfortable."
    mike.say "And we can stop at any time, as it's all about trust."
    show kylie talkative
    kylie.say "Geez, Ayesha - aren't you a wrestler?"
    show kylie happy
    kylie.say "You guys are always choking people out and making them submit!"
    show kylie normal
    show ayesha talkative
    ayesha.say "This is a little different."
    ayesha.say "I never got off on that kind of stuff in the ring!"
    show ayesha sadsmile
    show kylie shout
    kylie.say "Yeah, so you say..."
    show kylie normal
    "I don't want this thing to degenerate into an argument between Ayesha and Kylie."
    "So I step in, sensing a chance to alter the dynamic of the discussion just a little."
    mike.say "Maybe you should be the one to get tied up, Kylie?"
    show kylie surprised
    show fx exclamation at left5
    kylie.say "Huh?!?"
    show kylie stuned
    mike.say "You sound like you're pretty cool with the whole bondage thing."
    mike.say "Why not put your money where your mouth is?"
    mike.say "Show Ayesha there's nothing to be scared of?"
    show kylie talkative
    "Kylie's lips move for a moment, but no words come out."
    "And that's when I know that I've got her backed into a metaphorical corner."
    show kylie annoyed
    "How can she chicken out when she's just laid into Ayesha for the very same reason?"
    show kylie talkative
    kylie.say "Y...yeah, okay...whatever."
    show kylie sadhappy
    kylie.say "I was gonna say it should be me anyway."
    kylie.say "It'd be a waste to tie someone up that didn't appreciate it!"
    show kylie normal
    mike.say "Okay, that's decided then!"
    mike.say "Kylie, you're taking position while I show Ayesha the ropes!"
    "I'm kind of ashamed by the fact that I stooped to making such an obvious and lame joke."
    "But it seems to go straight over Ayesha and Kylie's heads."
    "Instead they pounce on the implications of what I just said, ignoring everything else as they do so."
    show ayesha surprised
    show fx exclamation at right5
    ayesha.say "You want ME to tie her up?!?"
    show ayesha stuned
    show kylie surprised
    kylie.say "You want HER to tie me up?!?"
    show kylie stuned
    mike.say "What's the difference?"
    mike.say "It'll still be me telling Ayesha what to do!"
    "The girls look at me in silence for a moment, then at each other."
    "And I honestly think that they're about to tell me where I can shove it..."
    show ayesha joke
    ayesha.say "Okay, okay - just take it slowly, yeah?"
    show ayesha normal
    show kylie shout
    kylie.say "Fine - just make sure Queen Kong doesn't screw up!"
    show kylie annoyed
    "I honestly expect Ayesha to fire back as Kylie begins to strip off."
    "But when she doesn't, I realise just how nervous she must be."
    mike.say "Just follow my instructions, Ayesha."
    mike.say "It'll be fine, trust me."
    "Ayesha nods as Kylie climbs onto the bed."
    show taming bondage with fade
    "I take things slowly, talking her through every step of the process."
    "And pretty soon Kylie's well and truly trussed up."
    "Her calves are bound to her thighs and her legs pulled apart to reveal her pussy."
    show taming bondage ropes
    "The ropes then tie her legs to her waist and separate her breasts."
    "Her arms are restrained in the same manner as her legs, meaning that she's helpless on the bed."
    "And she knows it too!"
    "I stare down at Kylie as she watches me watching her."
    "She licks her lips in anticipation of what's coming next."
    "Her eyes dart down towards her pussy, and then back up at me."
    scene bg bedroom1
    show ayesha kiss naked
    with fade
    $ ayesha.flags.kiss += 1
    "And it's at this exact moment I choose to pull Ayesha into an embrace and kiss her passionately."
    "The move takes her by surprise, but she soon melts into the kiss, wrapping her arms around me."
    scene bg black
    show taming bondage ropes angry
    with fade
    kylie.say "Hey, what the hell?!?"
    "I break the kiss and look down at Kylie for a moment."
    "But I don't speak a word, and only offer her an ironic smile."
    "And then I begin to run my hands over Ayesha's body and she does the same to me."
    "And it's not a chaste or gentle caress either, as we enjoy the chance to stroke and squeeze."
    "All the time we're aware of Kylie's eyes upon us, making it feel that much hotter!"
    "I take hold of Ayesha's hand, leading her on the bed."
    "Almost instantly, the sound of Kylie struggling to see what we're doing can be heard."
    kylie.say "Hey, what are you doing?"
    "I push Ayesha on the bad to make her stands there on her hands and knees."
    "From here I know that Kylie won't miss anything from what will follow."
    "And then I waste no time in grasping Ayesha's haunches and pulling her onto me."
    scene bg black
    show ayesha doggy
    with fade
    ayesha.say "Ooh..."
    ayesha.say "Hello there!"
    ayesha.say "Does someone want to come inside?"
    "I can't tell you how exciting it is to see Ayesha warming up to the notion of doing this."
    "Her nerves seem to have melted away as she gets off on what we're doing to Kylie right now."
    "Just the thought of her being turned on as the other girl fumes on the bed behind us is so hot!"
    "All of this means that I'm hard as a rock when my cock begins to slide against Ayesha's lips."
    "And I find that she's every bit as slick as I am stiff!"
    "I push against her for no more than a second before she lets me in."
    show ayesha doggy vaginal
    ayesha.say "Mmm..."
    ayesha.say "That's it..."
    ayesha.say "All the way in...I want every inch you got inside of me!"
    "I do my best to give Ayesha exactly what she wants, and more besides."
    "It's not as if the chance to fuck her like this isn't a joy in of itself either."
    "She's squeezing me like a fist every second that I'm in her, and it feels incredible."
    "But the fact is that I can hear her own moans mixing with the noises that Kylie's making near us too!"
    "I know that she can see what we're doing from back there."
    "So the grunts I hear can only be on account of her frustration."
    "All of that pent up jealousy she must be feeling as she's forced to watch."
    "Not to mention the fact that none of her own itch is being scratched either."
    "And knowing that she's wishing she was the one getting my cock makes it so much sweeter!"
    "Ayesha glances back at me, looking over her shoulder."
    "I can see in her eyes that she feels the same way I do, that she's loving it too."
    ayesha.say "[hero.name]..."
    show ayesha doggy vaginal pleasure
    ayesha.say "You cock feels SO good inside of me!"
    ayesha.say "My pussy's going to be aching for days!"
    "Sure, I know full well that Ayesha's laying it on thick for Kylie's benefit."
    "But that doesn't stop it being super hot to hear her talk like that!"
    mike.say "Oh fuck..."
    mike.say "Ayesha..."
    mike.say "I'm gonna cum!"
    ayesha.say "Oh yeah..."
    ayesha.say "Do it, [hero.name]..."
    ayesha.say "Cum inside of me - please!"
    with hpunch
    "A moment later I do just that, shooting everything that I have deep inside Ayesha."
    with hpunch
    "I let out a moan of release and satisfaction, but she actually cries out as she cums too."
    with hpunch
    "Ayesha grabs the frame of the mirror, as though she'll collapse without the support."
    "Even before I think of pulling out, I can already feel the cum seeping out of her pussy and down our legs."
    show ayesha doggy creampie ahegao
    "Still breathing heavily, I move over to where Kylie's tied up on the bed."
    scene bg black
    show taming bondage ropes
    with fade
    "She stares at my cock as it begins to go limp, and then looks me in the eye."
    "There's a strange mixture of anger and what looks like flustered desire in them."
    "And it's then that I realise Kylie must have been turned on by what we just did to her too!"
    kylie.say "Untie me, [hero.name]!"
    kylie.say "I think my butt went to sleep..."
    mike.say "I'll untie you, Kylie."
    mike.say "But on one condition."
    "Kylie looks up at me."
    "And is that actually concern I see flash in her eyes?"
    "Ayesha comes close too, intrigued to hear what I have to say next."
    mike.say "You have to clean up the mess I just made."
    mike.say "And you need to use your tongue too."
    kylie.say "Wha...I..."
    show taming bondage ropes surprised
    kylie.say "Okay, okay..."
    kylie.say "Just untie me and I'll do it!"
    "I keep my end of the deal, untying Kylie as quickly as I can."
    show taming bondage -ropes
    "Ayesha watches the whole time, biting her lip in anticipation of what's to follow."
    "Once free, Kylie sits up on the edge of the bed, rubbing the life back into her wrists."
    scene bg black
    show taming cunnilingus cum
    with fade
    "But true to her word, she then kneels on the floor in front of Ayesha."
    "She licks the inside of the thigh first, following the rivulets of cum upwards."
    "And then she works her way to Ayesha's lips."
    "The Amazon shivers as Kylie's tongue traces the lines of her pussy."
    "But both girls have a look of unmistakable pleasure on their faces the whole time."
    show taming cunnilingus -cum
    "Kylie does a thorough job, chasing down and lapping up every drop of cum she can find."
    scene bg bedroom1
    show kylie naked happy at left4
    show ayesha naked normal at right4
    with fade
    kylie.say "There you go - clean as a whistle!"
    show ayesha blush
    ayesha.say "Th...thank you, Kylie."
    ayesha.say "That felt amazing!"
    "I can see that Ayesha's blushing as she says this."
    "And then Kylie's cheeks flush too."
    kylie.say "D...don't mention it, Ayesha."
    "Am I hearing things?"
    "Did these two just thank each other in an almost civil manner?!?"
    "Maybe there is hope for Ayesha, Kylie and myself as a threesome after all!"
    return

label taming_event_03_a:
    scene bg aquarium with fade
    "Despite the fact that they're pretty different, I'm still sure Ayesha and Kylie can learn to get along."
    "All they really need is the chance to get to know each other, you know?"
    "That's how you turn what were once annoying habits into endearing little quirks."
    "So the first chance that presents itself, I take Ayesha and Kylie out on a date."
    "I tell them both to meet me at aquarium on the same day and at the same time."
    "Only I don't bother to tell them that the other one is going to be there too."
    "That way I figure that neither of them is going to use that as an excuse not to come."
    "I know, I know - I'm a genius, right?"
    "That's how I come to be standing in the lobby of the aquarium, a big smile on my face."
    "I spot Ayesha first, striding into the place and glancing around as she does so."
    show ayesha casual with dissolve
    "I guess she must be looking for me, because her face lights up when she spots me!"
    mike.say "Ayesha..."
    mike.say "Over here!"
    ayesha.say "Hi, [hero.name]!"
    ayesha.say "I got here as soon as I could."
    show ayesha happy
    ayesha.say "This is SUCH a great idea."
    ayesha.say "Just you and me spending some quality time together for once!"
    mike.say "Ah, well..."
    mike.say "About that..."
    kylie.say "Aha!"
    show kylie casual angry at right5
    show ayesha at left5
    with moveinleft
    kylie.say "I knew it, I just knew it!"
    show ayesha mindless at startle
    "Ayesha and I both jump almost out of our skins."
    "Kylie seems to have appeared out of nowhere."
    show ayesha annoyed
    "And now she's pointing an accusatory finger at Ayesha."
    kylie.say "You're stalking him, aren't you?"
    kylie.say "How else would you know he was meeting me here?!?"
    mike.say "Now wait a minute..."
    mike.say "Kylie, it's not like that..."
    "Not to be outdone, Ayesha squares up to Kylie."
    show ayesha a
    "She crosses her arms over her chest and looks down at the other girl."
    ayesha.say "You're crazy, Kylie."
    show ayesha normal
    show kylie sad
    ayesha.say "[hero.name] was meeting me here, not you!"
    mike.say "Well..."
    mike.say "I was kind of meeting you both..."
    mike.say "So...surprise!"
    show ayesha mindless
    show kylie surprised
    "Both of the girls round on me as one, glaring in disbelief."
    "And I don't honestly know which one of them is more scary!"
    ayesha.say "Why in the hell would you do that?!?"
    show ayesha angry
    ayesha.say "She's a crazy woman, and you know it!"
    kylie.say "I am not crazy!"
    show kylie angry
    kylie.say "Okay...maybe a little..."
    kylie.say "But I'm not some violent thug like you, Ayesha!"
    "This is starting to get out of hand."
    "If I don't do something soon, there won't be any date at all."
    "It'll just degenerate into a brawl, right here and now!"
    "Maybe if I can make them see my reasoning?"
    "That might convince them this is a good idea..."
    menu:
        "Explain yourself" if hero.charm < 75:
            mike.say "Well, I figured that you two didn't settle your differences the last time."
            mike.say "So I thought that I'd arrange for you to meet up and have it out again."
            mike.say "And do me a favour this time, sort it out before we leave the aquarium, yeah?"
            mike.say "Because this is really starting to get old!"
            show ayesha normal
            show kylie normal
            "Ayesha and Kylie both glare at me once I'm finished talking."
            "And for a moment I think they're going to slap me senseless."
            "But then they turn away from me and stalk into the aquarium."
            "That must mean I explained myself pretty well, right?"
            "Because they actually going in there together."
            $ taming_events = -1
            $ ayesha.love -= 5
            $ kylie.love -= 5
        "Explain yourself" if hero.charm >= 75:
            mike.say "Look, I'm sorry that I lied to you both, okay?"
            mike.say "I should have been up front and told each of you the other was coming."
            mike.say "But I was worried you'd both refuse to come otherwise."
            mike.say "I know you have your issues."
            mike.say "But I had such a great time when we were last out together."
            mike.say "I wanted to see if we could do it again, that's all."
            "Once I'm done talking, Ayesha and Kylie share a long, hard look."
            show ayesha normal
            show kylie normal
            "Then slowly, they both shrug and nod."
            ayesha.say "Okay, [hero.name], okay."
            ayesha.say "I guess we can give it a try."
            kylie.say "Fine, fine, fine..."
            kylie.say "But this is a trial, yeah?"
            "I nod, willing to accept whatever I'm given right now."
            "And together we walk into the aquarium."
            $ taming_events = 1
        "Kylie's crazy":
            mike.say "Ayesha's right, Kylie."
            show ayesha normal
            show kylie sad
            mike.say "You are pretty crazy."
            mike.say "I mean, I invite you both here on a date."
            mike.say "And I find you lurking in the shadows, ready to jump out on us!"
            "Kylie glares at me once I'm finished talking."
            show kylie annoyed
            "And for a moment I think she's going to slap me senseless."
            "But then she turns on her heel and stalks into the aquarium."
            "I look to Ayesha for help, and see that she's smiling at me."
            "Without needing to be asked, she takes hold of my hand."
            "And then she almost pulls me inside after Kylie."
            $ taming_events = 0
            $ kylie.love -= 5
        "Ayesha needs to cool down":
            mike.say "Kylie's right, Ayesha."
            show ayesha sad
            show kylie normal
            mike.say "You need to chill out, okay?"
            mike.say "I mean, I invite you both here on a date."
            mike.say "And the moment Kylie shows up, you start throwing your weight around!"
            "Ayesha glares at me once I'm finished talking."
            show ayesha annoyed
            "And for a moment I think she's going to slap me senseless."
            "But then she turns on her heel and stalks into the aquarium."
            "I look to Kylie for help, and see that she's smiling at me."
            "Without needing to be asked, she takes hold of my hand."
            "And then she almost pulls me inside after Ayesha."
            $ taming_events = 0
            $ ayesha.love -= 5
    "Once we're inside the place, things do seem to pick up a little."
    show ayesha normal
    show kylie normal
    "Maybe Ayesha and Kylie are really going to try to get along today."
    "Or maybe it's more on account of subdued lighting and the rippling water."
    "Either way I make a conscious effort to get the most out of this temporary truce."
    "Whenever one of the girls shows an interest, I'm there like a flash."
    "I read out all the information around the tanks, even ask the staff questions."
    "And somehow I seem to be able to divide my attention between Ayesha and Kylie."
    "By the time we get to one of the biggest tanks in the place, they seem quite chilled."
    kylie.say "Hmm..."
    kylie.say "I wonder what it'd be like to swim around in there?"
    ayesha.say "What, in that tank?"
    ayesha.say "With all those fish?"
    "This is the first time that I've heard Ayesha and Kylie talking together."
    "Well, talking without arguing, at least!"
    "So I sneak a little closer, hoping to listen in on the conversation."
    kylie.say "Oh, come on, Ayesha."
    kylie.say "Don't tell me you never wanted to be a mermaid!"
    kylie.say "I used to dream about being one all the time."
    ayesha.say "Well...yeah."
    show ayesha blush
    ayesha.say "I guess I kind of did!"
    kylie.say "Then again, Ayesha..."
    kylie.say "Maybe you'd make more sense as something bigger?"
    kylie.say "Something like a killer whale?"
    "I can feel my mood take a nose-dive as the conversation turns nasty."
    "And I take a deep breath, preparing myself to step in and break it up."
    show ayesha normal
    show fx question at left5
    ayesha.say "Oh yeah?"
    ayesha.say "Well you remind me of one of those sharks back there, Kylie."
    ayesha.say "Cold-blooded and mean, with beady little eyes!"
    mike.say "Hey, hey, hey..."
    mike.say "What's going on here?"
    mike.say "I thought we were having a good time?"
    ayesha.say "Kylie started it!"
    show ayesha annoyed
    ayesha.say "I was just trying to be nice!"
    kylie.say "It's not my fault Ayesha can't take a joke!"
    show kylie annoyed
    kylie.say "She needs to stop being so sensitive!"
    "Here we go again!"
    "Looks like I'm going to have to settle this..."
    menu:
        "Shut up! Both of you" if hero.charm < 75:
            mike.say "Will the two of you at least try to grow up a little?"
            mike.say "I heard every word of what you were saying to each other just now."
            mike.say "And just to settle the argument, you'd both look ridiculous as mermaids!"
            mike.say "I can't stand the thought of you flopping around like beached seals!"
            "I watch as Ayesha and Kylie's jaws drop almost in unison."
            show ayesha angry
            show kylie angry
            "But I don't stop to apologise or hear what they have to say in response."
            "I feel like I've already made my point, so I just turn and walk away."
            $ taming_events -= 1
            $ ayesha.love -= 5
            $ kylie.love -= 5
        "Shut up! Both of you" if hero.charm >= 75:
            mike.say "Will you two stop talking about being mermaids?"
            mike.say "All I can think of now is you with tails!"
            mike.say "And...well...seashell bras too!"
            "Suddenly I see a change in Ayesha and Kylie."
            show kylie normal
            show ayesha normal
            "And it's on account of them smelling weakness in me!"
            kylie.say "Oh really, [hero.name]?"
            kylie.say "Does that really turn you on, huh?"
            kylie.say "Thinking of Ayesha and me as mermaids?"
            ayesha.say "I...think I like it too!"
            ayesha.say "Having a strong, powerful tail!"
            ayesha.say "Pulling men down into the water and to their doom!"
            kylie.say "Yeah, Ayesha - but think what we'd do to them first!"
            mike.say "Will you guys please quit it?"
            mike.say "Or else I'm going to have to go to the bathroom for some release!"
            "Ayesha and Kylie share a genuine laugh together, even if it is at my expense."
            "I breathe a sigh of relief, but then remember what's going on in my shorts."
            "Maybe if I stare at some really ugly fish for while I'll be okay..."
            $ taming_events += 1
        "Shut Kylie up":
            mike.say "You shouldn't be teasing Ayesha about her size, Kylie."
            show ayesha normal
            mike.say "All of that is muscle, she got it from working out at the gym."
            mike.say "And your butt is far bigger than hers anyway!"
            mike.say "I don't know how a mermaid could stay afloat with as ass like that!"
            show kylie angry
            "Kylie's jaw drops open in shock and her eyes go wide."
            "But I don't stop to apologise or hear what she has to say in response."
            "I feel like I've already made my point, so I just turn and walk away."
            $ kylie.love -= 5
        "Ayesha, it's just a joke":
            mike.say "She's got a point, Ayesha - you'd look pretty freaky with a tail!"
            show kylie normal
            mike.say "And all those muscles too, I don't see how that would even work."
            mike.say "Mermaids are supposed to have a more feminine figure, yeah?"
            mike.say "Sexy and curvy, like Kylie here!"
            "Ayesha's jaw drops open in shock and her eyes go wide."
            show ayesha angry
            "But I don't stop to apologise or hear what she has to say in response."
            "I feel like I've already made my point, so I just turn and walk away."
            $ ayesha.love -= 5
    "We make it round the rest of the aquarium pretty much without incident."
    "Ayesha and Kylie finally seem more interested in the fish than fighting."
    show kylie normal
    show ayesha normal
    "And the whole thing pans out to be really enjoyable for me as a result."
    "More than once I even catch them both gasping and smiling at the same things."
    "By the time we make it to the gift shop by the exit, I'm in a pretty good mood."
    "And that's when I get to thinking that my dates deserve a reward for behaving themselves."
    "So while Ayesha and Kylie are distracted, I sneak off to buy them something."
    "Luckily for me, I manage to get them both something before they notice I'm gone."
    kylie.say "Wait a minute..."
    kylie.say "Where did [hero.name] go?"
    ayesha.say "Hmm..."
    ayesha.say "Oh...there he is!"
    mike.say "Hey, guys..."
    mike.say "I got you a little something!"
    show ayesha happy
    ayesha.say "Aw, thank you!"
    show kylie happy
    kylie.say "That's so sweet!"
    "I hand over my purchases and watch as the girls pull them out of the bags."
    show ayesha normal
    show kylie normal
    menu:
        "A whale for Ayesha and a shark for Kylie" if hero.charm < 75:
            show ayesha angry at startle
            ayesha.say "What on earth?!?"
            show kylie angry at startle
            kylie.say "Are you kidding me?!?"
            "Ayesha's staring at the plush whale in her hand."
            "And Kylie's already waving a plush shark in my face."
            "I do the best I can to force a grin."
            "And I try to explain myself as best I can."
            mike.say "Well..."
            mike.say "You were comparing each other to a whale and a shark earlier."
            mike.say "So I thought this would be a funny reminder of that, yeah?"
            mike.say "An amusing memory to remind you of our trip to the aquarium together?"
            "My words don't seem to be having the desired effect."
            "As I can feel Ayesha and Kylie's eyes burning into me."
            $ taming_events -= 1
            $ ayesha.love -= 5
            $ kylie.love -= 5
        "A mermaid for Ayesha and a mermaid for Kylie" if hero.charm >= 75:
            ayesha.say "Aww..."
            show ayesha happy
            ayesha.say "That's so sweet!"
            kylie.say "Oh my god!"
            show kylie happy
            kylie.say "I can't believe it!"
            "Ayesha and Kylie are staring down fondly at the plush mermaids in their hands."
            "I couldn't believe my luck when I found two that looked so much like them."
            "Almost as one they look up at me, beaming happily as they clutch their gifts."
            mike.say "Well..."
            mike.say "I thought about getting you a whale and a shark."
            mike.say "But then I saw the mermaids and thought they'd be a better choice."
            mike.say "Something to remind you both of our trip to the aquarium together."
            "My words seem to be having the desired effect."
            "Ayesha and Kylie both nod in agreement."
            $ taming_events += 1
        "A mermaid for Ayesha and a shark for Kylie":
            ayesha.say "Aww..."
            show ayesha happy
            ayesha.say "That's so sweet!"
            show kylie angry at startle
            kylie.say "What in the hell?!?"
            kylie.say "Are you kidding me?!?"
            "Ayesha's staring down fondly at the plush mermaid in her hand."
            "I couldn't believe my luck in finding one that looked so much like her."
            "But Kylie's already waving a plush shark in my face."
            mike.say "Well..."
            mike.say "You were comparing each other to a whale and a shark earlier."
            mike.say "And you were talking about mermaids too."
            mike.say "But I could only find a mermaid that looked like Ayesha."
            mike.say "So I thought this would be a funny reminder of that, yeah?"
            mike.say "An amusing memory to remind you of our trip to the aquarium together?"
            "My words don't seem to be having the desired effect."
            "As I can feel Kylie's eyes burning into me."
            $ kylie.love -= 5
        "A mermaid for Kylie and a whale for Ayesha":
            kylie.say "Aww..."
            show kylie happy
            kylie.say "That's so sweet!"
            show ayesha angry at startle
            ayesha.say "What in the hell?!?"
            ayesha.say "Are you kidding me?!?"
            "Kylie's staring down fondly at the plush mermaid in her hand."
            "I couldn't believe my luck in finding one that looked so much like her."
            "But Ayesha's already waving a plush whale in my face."
            mike.say "Well..."
            mike.say "You were comparing each other to a whale and a shark earlier."
            mike.say "And you were talking about mermaids too."
            mike.say "But I could only find a mermaid that looked like Kylie."
            mike.say "So I thought this would be a funny reminder of that, yeah?"
            mike.say "An amusing memory to remind you of our trip to the aquarium together?"
            "My words don't seem to be having the desired effect."
            "As I can feel Ayesha's eyes burning into me."
            $ ayesha.love -= 5
    "Once we're out of the aquarium, I try to gauge the mood."
    "I thought the date went pretty well, all things considered."
    "And I'm not quite ready for it to end just yet."
    mike.say "So..."
    mike.say "How was that for you guys?"
    mike.say "I had a really great time!"
    show ayesha normal
    show kylie normal
    if taming_events <= -2:
        ayesha.say "Wake up, [hero.name]!"
        show ayesha annoyed
        ayesha.say "This was a disaster from start to finish!"
        kylie.say "She's right, it was awful!"
        show kylie annoyed
        kylie.say "I'm going to need time to recover!"
        "I watch as Ayesha and Kylie walk away, leaving me standing all alone."
        hide kylie
        hide ayesha
        with dissolve
        "Did things really go that badly wrong?"
        "And if they did, how come I didn't notice?"
        "I'm really going to have to try harder next time."
        "I need to step my game up to the next level!"
        $ game.pass_time(2)
    elif taming_events >= 2:
        ayesha.say "I've had a great time, [hero.name]."
        show ayesha happy
        ayesha.say "In fact, I wish it didn't have to end yet."
        kylie.say "Same here, [hero.name]."
        show kylie happy
        kylie.say "I don't want the fun to end either!"
        mike.say "Well..."
        mike.say "How about a dinner?"
        ayesha.say "That sounds great!"
        kylie.say "Yeah, count me in!"
        "I'm grinning like crazy as I set off for the restaurant."
        "I have Ayesha on one side and Kylie on the other."
        "And my mind's already racing as I think of what we're going to get up to!"
        $ kylie.love += 5
        $ ayesha.love += 5
        call taming_event_03_b from _call_taming_event_03_b
    else:
        ayesha.say "I had a pretty good time today."
        ayesha.say "We should do it again soon."
        kylie.say "Yeah, I had fun too."
        kylie.say "Let me know when the next one's happening."
        "I smile as I watch Ayesha and Kylie walk away."
        hide kylie
        hide ayesha
        with dissolve
        "Sure, the date's over for now and I'm going home alone."
        "But there's the next date with them to think about."
        "And I'm determined to make that one even better!"
        if 'do_event' in locals() and do_event:
            $ hero.cancel_event()
        $ game.pass_time(2)
    return

label taming_event_03_b:
    $ DONE["taming_event_03_b"] = game.days_played
    $ game.hour = 20
    scene bg door restaurant
    show ayesha date at left5
    show kylie date at right5
    with fade
    "I make a point of holding the door open for Ayesha and Kylie when we arrive at the restaurant."
    "And the whole time I'm just praying that they both like this place, as it was my choice to come here."
    "But now you're thinking that I'm some kind of old-fashioned chauvinist, right?"
    "That I've insisted on picking the place where the three of us go out for a meal?"
    "Well let me tell you something - I HAD to pick the place myself."
    "It was either that or the whole date get scrapped before it even started!"
    "So this is how it went down..."
    "Ayesha wanted to try the new Japanese restaurant in town."
    "Kylie, on the other hand, insisted we eat at her favourite steak house."
    "I'd happily have gone for either of those, as it's the company that's important to me."
    "But the two of them would apparently rather starve in complete isolation than compromise!"
    scene bg restaurant
    show kylie date angry at center, zoomAt(1.5, (940, 1140))
    show ayesha a date annoyed at center, zoomAt(1.5, (340, 1140))
    with fade
    "And so here we are, sitting down in a restaurant that's pretty much an old reliable for me."
    "I have a smile plastered on my face, trying to make sure that everybody plays nicely together."
    "But I can already see that Ayesha and Kylie are glaring at each other across the table."
    "Which is a crying shame, because everyone else in the place is staring at them."
    "I mean, who wouldn't?"
    "I have an Amazon to one side of me and a blonde bombshell to the other!"
    "It's just that the former could go feral at any moment."
    "And the latter looks like she's ready to explode!"
    mike.say "So..."
    mike.say "This is a pretty nice place, right?"
    mike.say "And this table - they're really spoiling us!"
    ayesha.say "Huh..."
    show ayesha annoyed
    ayesha.say "I'd still have preferred the sushi joint!"
    kylie.say "Don't forget the steakhouse!"
    show kylie annoyed
    kylie.say "They serve the steaks extra bloody there!"
    "Desperate to broker peace, I hold up a menu."
    mike.say "Well..."
    mike.say "They have some pretty impressive steaks on the menu here, Kylie."
    mike.say "Seafood too, Ayesha - even if it isn't exactly sushi!"
    "I can't help cringing back into my seat as they both look at me."
    "Suddenly all of that suppressed hostility is focused in my direction!"
    "And I know that I have to do something to defuse the situation."
    "Waiter" "Sir..."
    "Waiter" "Are you ready to order?"
    "I almost jump at the unexpected sound of the waiter's voice."
    "But then I realise that he could be my ticket out of this mess."
    "Surely Ayesha and Kylie have to behave around this guy, right?"
    mike.say "Ah...yeah..."
    mike.say "I think we are!"
    mike.say "No, wait a minute..."
    mike.say "What are the specials?"
    "Waiter" "Tonight we have hand-pulled, stone-baked pizza."
    "Waiter" "We also have grilled king prawns in garlic butter."
    "Waiter" "There's a sirloin steak with seasonal vegetables."
    "Waiter" "Oh..."
    "Waiter" "And we also have gammon - extra salty!"
    menu:
        "Order something for everyone" if hero.charm < 75:
            mike.say "Mmm..."
            show ayesha normal
            show kylie normal
            mike.say "Extra salty, eh?"
            mike.say "In that case, make it three orders of gammon!"
            "The waiter nods and smiles as he takes back the menus."
            "I know it's not what either of the girls wanted to eat."
            "But surely they can see I needed to make a compromise?"
            "I smile at them, hoping to see them smile back."
            show ayesha angry
            show kylie angry
            "Instead I find Ayesha and Kylie glaring at me across the table."
            $ taming_events = -1
            $ ayesha.love -= 5
            $ kylie.love -= 5
        "Order something for everyone" if hero.charm >= 75:
            mike.say "I think we should all go for the pizza."
            mike.say "Because everyone likes pizza, right?"
            ayesha.say "I..."
            show ayesha normal
            ayesha.say "I could actually go for pizza."
            kylie.say "You know what..."
            show kylie normal
            kylie.say "That doesn't sound too bad."
            "The waiter nods and smiles as he takes back the menus."
            "I know it's not what either of the girls wanted to eat."
            "But thankfully it sounds like they're willing to compromise!"
            $ taming_events = 1
        "Order seafood":
            mike.say "We'll all have the prawns, yeah?"
            mike.say "Because everyone likes prawns."
            show ayesha normal
            show kylie normal
            mike.say "And it might not be sushi."
            mike.say "But it's still seafood."
            mike.say "Right, Ayesha?"
            show ayesha happy
            "Ayesha smiles and nods, looking pleased with my decision."
            "But Kylie practically glares at me across the table."
            show kylie angry
            "Ah well, I guess you can't please everyone."
            $ taming_events = 0
            $ kylie.love -= 5
        "Order steak":
            mike.say "We'll all have the steak, yeah?"
            mike.say "Because everyone likes steak."
            show ayesha normal
            show kylie normal
            mike.say "And it might not be from a fancy steakhouse."
            mike.say "But it's the next best thing."
            mike.say "Right, Kylie?"
            show kylie happy
            "Kylie smiles and nods, looking pleased with my decision."
            "But Ayesha practically glares at me across the table."
            show ayesha angry
            "Ah well, I guess you can't please everyone."
            $ taming_events = 0
            $ ayesha.love -= 5
    "With the food ordered, I figure that we can finally get on with the date."
    show ayesha normal
    show kylie normal
    "And as soon as it arrives, I make a point of looking happy and tucking in."
    "But after no more than a mouthful, I look up to see Ayesha and Kylie staring at me."
    "I freeze, my eyes darting this way and that as my brain tries to figure out what's wrong."
    mike.say "Ah..."
    mike.say "Why are you looking at me like that?"
    mike.say "Were you expecting me to say grace or something?"
    "Both Ayesha and Kylie look exasperated at the question."
    show ayesha annoyed
    show kylie annoyed
    "They tut and shake their heads at me in disbelief."
    ayesha.say "You have to be kidding, [hero.name]!"
    kylie.say "How can you say you didn't see that?"
    mike.say "See what?"
    mike.say "I can't say what I didn't see if I don't know what I'm supposed to have seen!"
    ayesha.say "The waiter, [hero.name]!"
    ayesha.say "When he was putting the food on the table just now?"
    kylie.say "You mean you didn't see what he was doing?"
    kylie.say "He was staring down our tops!"
    ayesha.say "Yeah, [hero.name] - he was checking out our chests!"
    "I can't keep my eyes from going wide at this statement."
    "If what the girls are saying is right, that's not cool."
    "But how in the hell did I manage to miss something like that?"
    "Was I so engrossed in getting started eating my meal?"
    "Whatever the case, I need to do something about this."
    menu:
        "Deal with it" if hero.charm < 75:
            "I can't just go accusing the waiter of staring at my date's chests."
            "He'll just flat out deny it and make me look like a complete fool."
            "Better to play the whole thing down in the hope of it blowing over."
            "So pardon me while I indulge in a little bit of gas lighting..."
            show ayesha normal
            show kylie normal
            mike.say "Are you sure that's what was happening?"
            mike.say "I mean, the guy's standing up and you're sitting down."
            mike.say "So it's always going to look like he's staring at your chest, isn't it?"
            ayesha.say "Are...are you siding with the waiter?!?"
            show ayesha angry
            kylie.say "Why would you do that, [hero.name]?"
            show kylie angry
            kylie.say "That guy was being a total creep!"
            ayesha.say "He was totally staring at us!"
            mike.say "Then why didn't you say something yourselves?"
            mike.say "Aren't you supposed to be modern women?"
            mike.say "Since when did you need me to fight your battles for you?"
            "Ayesha and Kylie both open their mouths to speak."
            "But then what I just said seems to sink in."
            "And they both look away, shaking their heads in defeat."
            "Yeah, it was a cheap trick on my part."
            "But it got me off the hook, so what the hell!"
            $ taming_events -= 1
            $ ayesha.love -= 5
            $ kylie.love -= 5
        "Deal with it" if hero.charm >= 75:
            "And I need to do it fast too."
            "Or else I'm going to look like an asshole."
            "The kind of asshole that lets his dates be taken advantage of!"
            mike.say "Okay, okay..."
            mike.say "Leave this to me!"
            show ayesha normal
            show kylie normal
            "I get up and walk over to the nearest member of staff."
            mike.say "Get me the manager."
            "Waiter" "Wha...what?!?"
            mike.say "I said, get me the manager - right now!"
            "The poor hapless employee hurries off to do as they're told."
            "And a few moments later, the manager appears as requested."
            "They nod and shake their head alternately as I make my complaint."
            "Then I stand and watch as the waiter is dragged in front of the manager."
            "I can't hear what's being said."
            "But the guy actually seems to be flinching from the words being spat at him!"
            "After that, I nod my head and return to the table."
            mike.say "There you go."
            mike.say "That's him told!"
            ayesha.say "Oh...okay, [hero.name]."
            ayesha.say "I hope the waiter doesn't get fired over this."
            kylie.say "I...I'm sure he'll just get a telling off, that's all!"
            mike.say "Don't feel sorry for that creep!"
            mike.say "He's getting exactly what he deserves."
            "Ayesha and Kylie nod at this."
            "And I catch them both glancing at me when they think I'm not looking."
            "Call me crazy, but I'm almost sure they're regarding me with renewed admiration!"
            $ taming_events += 1
        "Blame Kylie":
            "I can't just go accusing the waiter of staring at my date's chests."
            "He'll just flat out deny it and make me look like a complete fool."
            "Better to play the whole thing down in the hope of it blowing over."
            "So pardon me while I indulge in a little bit of gaslighting..."
            show ayesha normal
            show kylie normal
            mike.say "Well..."
            mike.say "Of course he was staring at you, Kylie."
            mike.say "It's not like you don't flaunt yourself, is it?"
            "Suddenly the united from the girls have been presenting is gone."
            show kylie angry
            "Kylie leans forwards, glaring at me across the table."
            show ayesha happy
            "But Ayesha leans back, laughing at the implications of what I just said."
            kylie.say "What the hell is that supposed to mean?!?"
            ayesha.say "It means you dress like a cheap prostitute, Kylie!"
            ayesha.say "Leave nothing to the imagination, and everyone's going to look!"
            "I can't help smiling and leaning back in my chair as they start to argue."
            "It doesn't solve the problem of the ogling waiter."
            "But it sure as hell takes the pressure off me!"
            $ kylie.love -= 5
        "Blame Ayesha":
            "I can't just go accusing the waiter of staring at my date's chests."
            "He'll just flat out deny it and make me look like a complete fool."
            "Better to play the whole thing down in the hope of it blowing over."
            "So pardon me while I indulge in a little bit of gaslighting..."
            show ayesha normal
            show kylie normal
            mike.say "Well..."
            mike.say "He might have been staring at Kylie like that."
            mike.say "But I think you're safe, Ayesha!"
            "Suddenly the united from the girls have been presenting is gone."
            show ayesha angry
            "Ayesha leans forwards, glaring at me across the table."
            show kylie happy
            "But Kylie leans back, laughing at the implications of what I just said."
            ayesha.say "What the hell is that supposed to mean?!?"
            kylie.say "It means the guy's into women, Ayesha."
            kylie.say "Not big, muscly guys that just happen to have boobs!"
            "I can't help smiling and leaning back in my chair as they start to argue."
            "It doesn't solve the problem of the ogling waiter."
            "But it sure as hell takes the pressure off me!"
            $ ayesha.love -= 5
    "Once the drama with the waiter is over, everything seems to settle down."
    "Ayesha and Kylie are either out of things to argue about right now."
    show kylie normal
    show ayesha normal
    "Or else they're actually having a good time in each other's company."
    "I mean the former is more likely than the latter."
    "But I'm not about to go asking them why and have it all blow up in my face!"
    "In fact, we make it through the rest of the meal without incident."
    "That is until the bill turns up and we see what the damage is going to be..."
    ayesha.say "Ooh..."
    show ayesha annoyed
    ayesha.say "Now I remember why I don't eat out too often!"
    kylie.say "You can say that again!"
    show kylie annoyed
    kylie.say "Did they charge us for breathing the air in here too?!?"
    mike.say "Ah, it's not that bad really!"
    mike.say "There are three of us, after all."
    "So far, nobody's even mentioned how we're going to pay for the meal."
    "And it looks like the responsibility is going to fall on me."
    menu:
        "Pick up the bill":
            mike.say "Hey, don't worry about it."
            mike.say "What kind of a gentleman would I be if I didn't pick up the tab, huh?"
            ayesha.say "Erm..."
            show ayesha angry
            ayesha.say "Maybe one that lives in the twenty-first century?"
            kylie.say "Yeah, [hero.name]!"
            show kylie angry
            kylie.say "That is kind of presumptuous."
            "I feel my heckles stand up at their reaction."
            "And I suddenly have the desperate need to double down on my promise to pay."
            mike.say "Well call me old-fashioned then!"
            mike.say "Geez...you try to do something nice."
            mike.say "And all you get is abuse!"
            $ taming_events -= 1
            $ ayesha.love -= 10
            $ kylie.love -= 10
            $ ayesha.sub += 5
            $ kylie.sub += 5
        "Split the bill" if hero.charm >= 75:
            mike.say "And it won't be too much once we've split it three ways."
            mike.say "Are you both okay with that?"
            show ayesha normal
            show kylie normal
            "Ayesha and Kylie exchange a shrug and a nod."
            ayesha.say "Okay, [hero.name]."
            ayesha.say "That sounds fair."
            kylie.say "Fine by me."
            kylie.say "Let's do that."
            "I breathe a sigh of relief as they both agree."
            "Looks like we managed to avoid making a scene!"
            $ taming_events += 1
        "Let Ayesha pick up the tab":
            mike.say "Why don't you get this one, Ayesha?"
            mike.say "After all, you're the one with a job."
            mike.say "Kylie here's just a broke student!"
            show ayesha angry
            "Ayesha stares at me in open amazement."
            "It's like she can't quite believe what I just said."
            show kylie happy
            "But Kylie can't help laughing as she nods in agreement."
            $ ayesha.love -= 5
        "Let Kylie pick up the tab":
            mike.say "Why don't you get this one, Kylie?"
            mike.say "I know for a fact you just got your student loan for this semester."
            mike.say "So you can spend some of it on us, rather than wasting it on books!"
            show kylie angry
            "Kylie stares at me in open amazement."
            "It's like she can't quite believe what I just said."
            show ayesha happy
            "But Ayesha can't help laughing as she nods in agreement."
            $ kylie.love -= 5
    "Once we're out of the restaurant, I try to gauge the mood."
    "I thought the date went pretty well, all things considered."
    "And I'm not quite ready for it to end just yet."
    show ayesha normal
    show kylie normal
    mike.say "So..."
    mike.say "How was that for you guys?"
    mike.say "I had a really great time!"
    if taming_events <= -2:
        ayesha.say "Wake up, [hero.name]!"
        show ayesha annoyed
        ayesha.say "This was a disaster from start to finish!"
        kylie.say "She's right, it was awful!"
        show kylie annoyed
        kylie.say "I'm going to need time to recover!"
        "I watch as Ayesha and Kylie walk away, leaving me standing all alone."
        hide kylie
        hide ayesha
        "Did things really go that badly wrong?"
        "And if they did, how come I didn't notice?"
        "I'm really going to have to try harder next time."
        "I need to step my game up to the next level!"
        $ game.pass_time(2)
    elif taming_events >= 2:
        ayesha.say "I've had a great time, [hero.name]."
        show ayesha happy
        ayesha.say "In fact, I wish it didn't have to end yet."
        kylie.say "Same here, [hero.name]."
        show kylie happy
        kylie.say "I don't want the fun to end either!"
        mike.say "Well..."
        mike.say "What do you say we end this at the beach?"
        ayesha.say "That sounds great!"
        kylie.say "Yeah, count me in!"
        "I'm grinning like crazy as I set off for the beach."
        "I have Ayesha on one side and Kylie on the other."
        "And my mind's already racing as I think of what we're going to get up to!"
        $ kylie.love += 5
        $ ayesha.love += 5
        call taming_event_03_c from _call_taming_event_03_c
    else:
        ayesha.say "I had a pretty good time tonight."
        ayesha.say "We should do it again soon."
        kylie.say "Yeah, I had fun too."
        kylie.say "Let me know when the next one's happening."
        "I smile as I watch Ayesha and Kylie walk away."
        hide kylie
        hide ayesha
        "Sure, the date's over for now and I'm going home alone."
        "But there's the next date with them to think about."
        "And I'm determined to make that one even better!"
        if 'do_event' in locals() and do_event:
            $ hero.cancel_event()
        $ game.pass_time(2)
    return

label taming_event_03_c:
    $ game.hour = 22
    $ DONE["taming_event_03_c"] = game.days_played
    scene bg beach with fade
    "I've been racking my brains for the past few days, trying to figure out where to take Ayesha and Kylie on a date."
    "Any other girls I'd just have thought up something that sounded like fun and sprung it on them as a surprise."
    "But Ayesha and Kylie are exactly any other girls, they're both present unique challenges all of their own."
    "And what's worse is that they seem to take pleasure in instantly hating anything the other wants to do."
    "So instead of thinking up something fun, I have to think up something that nobody could possibly object to."
    "What I need is something so simple, so fundamentally uncomplicated that there's nothing they can disagree on."
    "And that's when it hits me - what about a walk on the beach by moonlight?"
    "It's simple, classic and completely devoid of complications."
    "What could possibly go wrong?"
    "Yeah, I know, I know!"
    "I probably just jinxed the whole thing right there!"
    "But here goes nothing..."
    show ayesha date at left5
    show kylie date at right5
    with dissolve
    ayesha.say "Does anybody else think this is..."
    ayesha.say "I don't know...maybe a little weird?"
    "We've only been walking on the sand for a couple of minutes."
    "And so far everyone's been quiet, nobody speaking a word."
    "This means that Ayesha's question catches me off-guard."
    "It also takes me a moment to get my head around what she actually said."
    mike.say "You..."
    mike.say "You mean you think this is weird?"
    mike.say "Taking a stroll on the beach at night?"
    "I can't help shaking my head in surprise."
    mike.say "This is like a classic romantic thing to do, Ayesha!"
    show ayesha sad
    "Ayesha frowns at my response, looking this way and that."
    "There's something else going on here."
    "But I can't tell just what it is."
    "Though it seems like Kylie's quicker on the uptake than me."
    kylie.say "Oh my god..."
    kylie.say "Ayesha, are you...are you scared?"
    show kylie happy
    kylie.say "How can someone as big as you be afraid of the dark?!?"
    show ayesha a annoyed
    "Ayesha instantly becomes defensive, crossing her arms over her chest."
    "But at the same time I see that she doesn't stop looking around."
    "Maybe Kylie's onto something here - maybe Ayesha is scared."
    ayesha.say "I'm not scared of something jumping out of the shadows, Kylie!"
    ayesha.say "Like I said, it's weird - like uncanny, you know?"
    show ayesha normal
    show kylie normal
    ayesha.say "I'm used to being here in the daytime, when it's busy."
    ayesha.say "Take away all of the people and it's creepy!"
    menu:
        "Shut up! Both of you" if hero.charm < 75:
            "Urgh..."
            "I knew it was going to turn out like this!"
            "We've only walked a couple of steps onto the sand."
            "And already these two are bickering!"
            mike.say "Will the two of you shut up?"
            mike.say "Ayesha, there's nothing out here that can hurt you."
            mike.say "So stop acting like a scared little girl."
            mike.say "And as for you, Kylie..."
            mike.say "Stop jumping in every chance you get."
            mike.say "All that does is make things worse!"
            show ayesha annoyed
            show kylie annoyed
            "Ayesha and Kylie both look annoyed at my chewing them out."
            "And for a moment I think that they're going to give me a mouthful in return."
            "But in the end all I get is a couple of irritated huffs."
            "And with that, I choose to consider the matter closed."
            $ taming_events = -1
            $ ayesha.love -= 5
            $ kylie.love -= 5
        "Shut up! Both of you" if hero.charm >= 75:
            "I hold my hands up, appealing for calm."
            mike.say "Hey, hey, hey!"
            mike.say "This is supposed to be a date!"
            mike.say "Why in the hell are we starting to fight?"
            show ayesha angry
            ayesha.say "Because Kylie was being mean to me!"
            show kylie angry
            kylie.say "I was only mad because you were going to ruin the date before it got started!"
            "I shake my head and wave away their protests."
            mike.say "You need to chill out, the pair of you!"
            mike.say "I get what you're saying, Ayesha."
            show ayesha normal
            mike.say "It's weird there being no people here."
            mike.say "But Kylie and I are here, so you're not alone."
            mike.say "And Kylie, if you think that Ayesha's going to want to leave, why not reassure her?"
            show kylie normal
            mike.say "You might actually be able to convince her that she's safe with us!"
            "Ayesha and Kylie both look like they're going to argue with me."
            "But then they seem to think better of it."
            "They nod one after the other, and then we start walking again."
            "A quick glance to either side shows me that they both seem satisfied."
            "Maybe not one hundred percent happy."
            "But at least they're not fighting anymore."
            $ taming_events = 1
        "Ayesha! Shut up!":
            "I roll my eyes at Ayesha and let out a weary sigh."
            mike.say "Kylie's right, Ayesha."
            show ayesha normal
            show kylie normal
            mike.say "This place is as safe right now as it is in the middle of the day."
            mike.say "I think you're being a little childish letting it get to you!"
            ayesha.say "What?!?"
            show ayesha angry
            ayesha.say "I already said I wasn't scared!"
            ayesha.say "Kylie was the one that said that!"
            "I shake my head, brushing aside Ayesha's explanation."
            mike.say "Look, let's forget about it, okay?"
            mike.say "I'll hold your hand extra tight if that'll help!"
            "Ayesha opens her mouth to protest."
            "But then she seems to think better of it."
            "We start to walk down the beach again."
            "A quick glance confirms that I have Ayesha glaring on one side of me."
            "And a look in the other direction lets me know Kylie's gloating on the other."
            $ taming_events = 0
            $ ayesha.love -= 5
        "Kylie! Shut up!":
            "I turn on Kylie without warning, staring her straight in the eye."
            mike.say "Oh shut up, Kylie!"
            show kylie sad
            mike.say "Ayesha never said she was scared of anything - that was you!"
            mike.say "She said this place was weird in the darkness, and she's right."
            show kylie surprised
            kylie.say "Wh..."
            show kylie angry
            kylie.say "Why are you getting mad at me?!?"
            kylie.say "I wasn't the one complaining!"
            "I shake my head, brushing aside Kylie's excuses."
            mike.say "Yeah, Kylie, I know that."
            mike.say "But you didn't have to weigh in and make things worse!"
            "Kylie opens her mouth to protest."
            show kylie sad
            "But then she seems to think better of it."
            "We start to walk down the beach again."
            "A quick glance confirms that I have Kylie glaring on one side of me."
            "And a look in the other direction lets me know Ayesha's gloating on the other."
            $ taming_events = 0
            $ kylie.love -= 5
    "Once we're actually walking along the beach, things seem to get better."
    "The gentle sound of the ocean waves lapping forms a natural background noise."
    show ayesha normal
    show kylie normal
    "The soft sand beneath our feet feels just as good as it does in the daytime."
    "And that's not to mention the sight of the moon and stars reflecting off the water."
    "It's fast becoming one of those picture perfect nights."
    "You know what I mean - the kind you see in the movies?"
    show kylie angry at startle
    kylie.say "Ouch!"
    kylie.say "Goddammit!"
    show kylie sad
    kylie.say "I think I broke my fucking toe!"
    "Well that never happened in any movie that I saw!"
    "And it pretty much kills the mood too."
    "Ayesha and I glance round to see what's the matter with Kylie."
    "We're just in time to see her reach down and grab a rock off the sand."
    "I guess that must be what caused her outburst a few seconds ago."
    show kylie at startle
    "And that's confirmed when she winds up and throws the offending rock into the sea."
    "All three of us end up watching at it sails towards the water."
    "But it comes as some surprise to see the rock skip across the surface before it sinks."
    mike.say "Wow, Kylie!"
    mike.say "You skimmed that thing pretty far!"
    show kylie angry
    kylie.say "Hurmph..."
    kylie.say "Not as far as it deserved!"
    kylie.say "Who put that thing there?!?"
    kylie.say "Anyone could have tripped over it!"
    show kylie normal
    "Ayesha doesn't add anything to the conversation at first."
    "Instead she just stands there like she's deep in thought."
    ayesha.say "Hmm..."
    ayesha.say "You could have got it much further."
    ayesha.say "It's all in the wrist action."
    kylie.say "Yeah, well..."
    kylie.say "I wasn't thinking about breaking a world record just now!"
    "Ayesha seems to ignore Kylie, stooping to pick up another rock."
    show ayesha at startle
    "Then she sends it skipping out to sea with a flick of her wrist."
    "I watch as Ayesha's proven right, her stone going much further than Kylie's."
    show ayesha happy
    ayesha.say "There you go!"
    ayesha.say "That's how you skim a stone, Kylie."
    kylie.say "What are you talking about, Ayesha?"
    kylie.say "I don't want a lesson in skimming stones!"
    show kylie angry
    kylie.say "I was just mad that I stubbed my toe, that's all!"
    "Here we go again!"
    "Is there nothing these two can't turn into an argument?"
    menu:
        "Show them a real stone skim" if hero.charm < 75:
            "Maybe it's time somebody put the pair of them in their places?"
            "With that in mind, I bend down and pick up a rock of my own."
            "Then I shoulder my way between Ayesha and Kylie."
            show ayesha normal
            show kylie normal
            ayesha.say "Hey!"
            kylie.say "What the..."
            mike.say "Okay, amateur hour's over!"
            mike.say "Stand back and let me show you how it's done."
            "I hear groans and snorts from the girls."
            "But I put them out of my mind as I prepare myself."
            "And then I cast my stone out onto the water."
            "It sails through the air and then hits the waves."
            "Where it skips over the surface like a dream!"
            mike.say "What did I tell you!"
            mike.say "That's how you skim a damn stone!"
            ayesha.say "Geez..."
            ayesha.say "What a show-off!"
            kylie.say "What do I care, [hero.name]?"
            kylie.say "I was never trying to skim a stone in the first place!"
            $ taming_events -= 1
            $ ayesha.love -= 5
            $ kylie.love -= 5
        "Play peacemaker" if hero.charm >= 75:
            "Maybe I can be the one to defuse it?"
            "With that in mind, I bend down and pick up a rock of my own."
            "Then I shoulder my way between Ayesha and Kylie."
            show ayesha normal
            show kylie normal
            ayesha.say "Hey!"
            kylie.say "What the..."
            mike.say "Okay, amateur hour's over!"
            mike.say "Stand back and let me show you how it's done."
            "I hear groans and snorts from the girls."
            "But I put them out of my mind as I prepare myself."
            "And then I cast my stone out onto the water."
            "It sails through the air and then hits the waves."
            "Whereupon it sinks like, well...like a stone."
            ayesha.say "Oh wow..."
            show ayesha annoyed
            ayesha.say "This is kind of embarrassing!"
            kylie.say "Oh my god, [hero.name]!"
            show kylie annoyed
            kylie.say "Mine went further than that."
            kylie.say "And I wasn't even trying!"
            mike.say "I..."
            mike.say "I wasn't ready!"
            mike.say "Let me just find another stone..."
            show ayesha normal
            show kylie normal
            ayesha.say "I think one was enough, [hero.name]!"
            kylie.say "Yeah, let's leave it alone!"
            "I nod reluctantly and follow as the girls start to walk on."
            "But I wait until they have their backs turned to treat myself to a sly smile."
            "Sure, you have to be good to skim a stone any great distance."
            "But you have to be really good to fake a throw that bad!"
            "And back home, I was the undisputed champion when it came to stone-skimming!"
            $ taming_events += 1
        "Praise Ayesha's performance":
            "Maybe I should be worried about the state of Kylie's toe right now."
            show ayesha normal
            show kylie normal
            "But I used to love skimming stones as a kid, and so I'm entranced."
            "Ayesha's throw was really good, and I want to know how she did it."
            mike.say "That's the best throw I've seen in ages, Ayesha!"
            mike.say "You're a natural!"
            mike.say "You've got to teach me how to do that!"
            ayesha.say "Sure thing, [hero.name]."
            show ayesha happy
            ayesha.say "It's not that hard really."
            ayesha.say "You just need to know when to let go..."
            "I lean in close as Ayesha shows me her technique."
            "And I'm so engrossed that I forget all about Kylie."
            kylie.say "Ahem..."
            show kylie angry
            kylie.say "Ah, hello?"
            kylie.say "Did I just turn invisible or something?!?"
            "Ayesha and I look up to see Kylie glaring daggers in our direction."
            "She has her arms crossed over her chest."
            "But the pain in her toe seems to have subsided a little."
            "At least enough for Kylie to stamp her foot and storm off down the beach."
            $ kylie.love -= 5
        "Sympathise with Kylie":
            "I'm actually worried about the state of Kylie's toe right now."
            show ayesha normal
            show kylie normal
            "What if she's broken it and I have to carry her back to the car?"
            mike.say "Geez, Ayesha!"
            mike.say "Do you have to turn everything into a competition?"
            ayesha.say "I..."
            show ayesha annoyed
            ayesha.say "I'm sorry, [hero.name]..."
            ayesha.say "I didn't think!"
            "Kylie doesn't miss the chance to milk my sympathy."
            "Or an opportunity to pile on Ayesha!"
            show kylie sad
            kylie.say "Ow, ow, ow!"
            kylie.say "It still hurts, [hero.name]!"
            show kylie normal
            kylie.say "But I think I'll be able to walk."
            show kylie happy
            "Kylie narrows her eyes and smiles at Ayesha as I fuss over her."
            "So much so that I begin to wonder if she's as badly hurt as she claims."
            "For her part, Ayesha furrows her brows and looks away."
            $ ayesha.love -= 5
    "We've been walking a while by now, covering most of the length of the beach."
    "I guess that it'll soon be time to call it a night and head for home."
    show ayesha normal
    show kylie normal
    "The conversation has been meandering for a while as well."
    "In fact, I'm not even sure exactly what we're talking about anymore."
    "And I lose all interest in it anyway, as soon as I look up at the moon."
    mike.say "Whoa..."
    mike.say "How did we not notice that before now?"
    ayesha.say "Notice what, [hero.name]?"
    kylie.say "Yeah, what are you talking about?"
    mike.say "The moon, you guys!"
    mike.say "It's one hundred percent full!"
    mike.say "I mean, just look at it!"
    "Ayesha and Kylie do as I say, gazing up at the sky."
    ayesha.say "You're right, it's huge!"
    kylie.say "I don't remember it ever being that big!"
    mike.say "You know what..."
    mike.say "We should make a wish!"
    show ayesha happy
    show kylie happy
    "Ayesha and Kylie turn their attention from the moon to me."
    "Both of them look amused by my suggestion, smirking and giggling."
    kylie.say "What are you even talking about, [hero.name]?"
    show kylie normal
    kylie.say "Nobody wishes on the moon!"
    ayesha.say "She's right, [hero.name]."
    show ayesha normal
    ayesha.say "You're thinking of stars!"
    show ayesha happy
    show kylie happy
    "I can feel myself starting to frown as they laugh at me."
    "Maybe it's not the done thing to wish on the full moon."
    "But I thought it sounded romantic, you know?"
    "A prefect way to bring the date to an end!"
    menu:
        "Make a wish" if hero.charm < 75:
            mike.say "Aren't women always dumping on guys for not being romantic enough?"
            mike.say "Well look what happens when one of us gives it a try!"
            mike.say "You throw it back in his face!"
            show ayesha normal
            show kylie normal
            "I shake my head as I walk a little way from them."
            mike.say "Well screw the pair of you."
            mike.say "I'm going to do it on my own!"
            ayesha.say "You do you, [hero.name]."
            ayesha.say "Whatever makes you feel better about yourself!"
            kylie.say "Don't take too long about it though."
            kylie.say "There's a seashell over here you can wish on next."
            kylie.say "Or maybe you want to wish on one of the trash-cans in the car park?"
            "I try as best I can to tune Ayesha and Kylie out."
            "But no matter how hard I try, I still feel like a fool the whole time."
            $ taming_events = -1
            $ ayesha.love -= 5
            $ kylie.love -= 5
        "Don't make a wish" if hero.charm >= 75:
            mike.say "Yeah..."
            mike.say "Now you mention it, the idea is kind of lame!"
            show ayesha normal
            show kylie normal
            "Ayesha and Kylie nod, smiling as I admit defeat."
            "They each take one of my arms and lead me off down the beach."
            "Sure, I feel disappointed that they both dumped on my idea."
            "But I'm a big enough guy to be able to take it on the chin."
            "Especially if it ends up making them think they got one over on me."
            "I even allow myself a little grin as I note the lack of arguing as we walk."
            "It doesn't matter what Ayesha and Kylie think."
            "I know that I chose to back down and they didn't really score a victory back there."
            $ taming_events += 1
        "Ayesha, I'm disappointed":
            show ayesha normal
            show kylie normal
            mike.say "I could have guessed Kylie would dump on the idea."
            mike.say "But I expected better of you, Ayesha!"
            show ayesha mindless
            ayesha.say "H...huh?!?"
            show ayesha annoyed
            ayesha.say "What do you mean?"
            mike.say "You're the one that's always going on about how I need to be more sensitive."
            mike.say "Telling me how I need to be more in touch with my feelings."
            mike.say "So why don't you back it up and support me for once, huh?!?"
            "I start to stride off down the beach."
            "And Ayesha follows on my heels."
            ayesha.say "Wait..."
            show ayesha sad
            ayesha.say "I didn't mean to..."
            ayesha.say "I can explain!"
            "Kylie follows at a slower pace."
            "Perhaps she's hoping that it'll look like she's being respectful."
            "But I know all to well that she's eager to watch the fireworks between Ayesha and me."
            $ ayesha.love -= 5
        "Kylie, I'm disappointed":
            mike.say "I could have guessed Ayesha would dump on the idea."
            show ayesha normal
            show kylie normal
            mike.say "But I expected better of you, Kylie!"
            show kylie surprised
            kylie.say "H...huh?!?"
            kylie.say "What do you mean?"
            mike.say "You're the one that's always going on about how much you care for me."
            mike.say "Telling me how I'm the man of your dreams and we're supposed to be together."
            mike.say "So why don't you act like it and support me for once, huh?!?"
            "I start to stride off down the beach."
            "And Kylie follows on my heels."
            kylie.say "Wait..."
            show kylie sad
            kylie.say "I didn't mean to..."
            kylie.say "I can explain!"
            "Ayesha follows at a slower pace."
            "Perhaps she's hoping that it'll look like she's being respectful."
            "But I know all to well that she's eager to watch the fireworks between Kylie and me."
            $ kylie.love -= 5
    "Once we're back at the car, I try to gauge the mood."
    show ayesha normal
    show kylie normal
    "I thought the date went pretty well, all things considered."
    "And I'm not quite ready for it to end just yet."
    mike.say "So..."
    mike.say "How was that for you guys?"
    mike.say "I had a really great time!"
    if taming_events <= -2:
        ayesha.say "Wake up, [hero.name]!"
        show ayesha annoyed
        ayesha.say "This was a disaster from start to finish!"
        kylie.say "She's right, it was awful!"
        show kylie annoyed
        kylie.say "I'm going to need time to recover!"
        hide ayesha
        hide kylie
        with dissolve
        pause 0.2
        play sound car_door
        pause 0.4
        play sound car_door
        "I watch as Ayesha and Kylie clamber into the car."
        "Which leaves me to ponder things alone for a moment."
        "Did things really go that badly wrong?"
        "And if they did, how come I didn't notice?"
        "I'm really going to have to try harder next time."
        "I need to step my game up to the next level!"
        $ game.pass_time(2)
    elif taming_events >= 2:
        ayesha.say "I've had a great time, [hero.name]."
        show ayesha happy
        ayesha.say "In fact, I wish it didn't have to end yet."
        kylie.say "Same here, [hero.name]."
        show kylie happy
        kylie.say "I don't want the fun to end either!"
        mike.say "Well..."
        mike.say "You could always come back to my place?"
        ayesha.say "That sounds great!"
        kylie.say "Yeah, count me in!"
        "I'm grinning like crazy as I set off for home."
        "I have Ayesha and Kylie in the car with me."
        "And my mind's already racing as I think of what we're going to get up to!"
        $ kylie.love += 5
        $ ayesha.love += 5
        $ game.flags.taming_harem_event_03 = True
        $ game.flags.taming_delay = TemporaryFlag(True, 1)
        call taming_threesome_fuck from _call_taming_threesome_fuck_3
    else:
        ayesha.say "I had a pretty good time tonight."
        ayesha.say "We should do it again soon."
        kylie.say "Yeah, I had fun too."
        kylie.say "Let me know when the next one's happening."
        hide ayesha
        hide kylie
        with dissolve
        pause 0.2
        play sound car_door
        pause 0.4
        play sound car_door
        "I smile as I watch Ayesha and Kylie climb into the car."
        "Sure, the date's over for now and I'm going home alone after I drop them off."
        "But there's the next date with them to think about."
        "And I'm determined to make that one even better!"
        if 'do_event' in locals() and do_event:
            $ hero.cancel_event()
        $ game.pass_time(2)
    return

label taming_event_04:
    scene bg bedroom1
    show ayesha date
    with fade
    "Normally I'd be waiting eagerly for Kylie to turn up for a little fun in my bedroom."
    "Doubly so because Ayesha's here already and we're supposed to be doing it as a threesome too."
    "But right now I can practically feel the anxiety that Ayesha's going through as we wait."
    "And I can't say that I really blame her, because Kylie made it clear she has a 'surprise' in store."
    "Anybody else and we'd be speculating like crazy, eager to see just what it was."
    "But Kylie can be a little kooky at the best of times, you know?"
    "Part of me is worried that she'll turn up carrying a box with a severed head in it!"
    "Well, maybe not anything that crazy!"
    "I mean, she's not a psychopath, right?"
    mike.say "Don't worry, Ayesha."
    mike.say "I'm sure it'll be fine."
    "Ayesha looks up at me from where she's sitting on the bed."
    show ayesha annoyed
    "There's genuine concern in her eyes as she does so."
    "And it's weird to see someone so physically strong put on edge."
    ayesha.say "I...I guess you're right, [hero.name]."
    ayesha.say "Kylie's been a lot less crazy lately."
    ayesha.say "Just...promise you'll keep me safe, okay?"
    mike.say "I promise, Ayesha."
    mike.say "You're safe with me, okay?"
    show ayesha normal
    "Ayesha nods, beginning to look a little more hopeful."
    show kylie happy date at top_mostright with moveinright
    "But then the door bursts open and Kylie strides into the room."
    show kylie at right with move
    kylie.say "Hey guys..."
    kylie.say "Sorry I'm a little late."
    kylie.say "Took me a while to dig this stuff out of my closet!"
    show ayesha at left5
    show kylie at right4
    with move
    "As if to make her point, Kylie empties the bag she's carrying onto the bed."
    "Ayesha scoots aside out of instinct as the contents tumble out beside her."
    "I see what looks like a blindfold and even a pretty impressive dildo in there."
    "But most of what tumbles out seems to be rope."
    "And by that I mean fine quality rope, with an expensive look about it."
    "I can see the way that Ayesha's looking at it as well."
    "Suffice to say that it's done nothing to calm her fears."
    "So I try to step in and clear up what's going on here."
    mike.say "What's all of this stuff for, Kylie?"
    mike.say "Are you going to teach us to tie knots?"
    mike.say "I think we're a little old to be playing boy scouts!"
    show kylie annoyed
    "Kylie rolls her eyes at this."
    "She chuckles and shakes her head."
    kylie.say "We're going to be playing with knots."
    show kylie happy
    kylie.say "But these ones are strictly for adults."
    kylie.say "I'm going to teach you two all about bondage!"
    ayesha.say "Oh no!"
    show ayesha angry
    ayesha.say "No way are you tying me up!"
    kylie.say "Geez, Ayesha - calm down!"
    show kylie annoyed
    kylie.say "The idea's for you guys to tie me up, not the other way around."
    show kylie normal
    kylie.say "There's no way I'd do this with an amateur in the actual ropes!"
    mike.say "That sounds pretty good to me, Ayesha."
    mike.say "Kylie's going to show us something fun and new."
    mike.say "Plus we get to do it to her - so what's not to like?"
    "I'm still trying to sell the idea to Ayesha and reassure her."
    show ayesha annoyed
    "But now I'm putting in more effort on account of my own interest too."
    "The idea of tying Kylie up and having my way with her sounds great."
    "And I don't want to miss out just because Ayesha's got butterflies."
    ayesha.say "Okay, okay..."
    show ayesha normal
    ayesha.say "If she's the one getting tied up."
    ayesha.say "But I get to call it quits if things get weird!"
    "Kylie and I both nod in agreement, eager to get things moving."
    "But part of me does wonder just what Ayesha means by weird."
    "I mean, Kylie's already agreed to be tied up by a veritable Amazon."
    "How much stranger are things going to get?"
    kylie.say "Well?"
    show kylie happy
    kylie.say "What are you waiting for?"
    kylie.say "Let's get this show on the road!"
    show kylie underwear
    "Kylie sets an example by starting to strip off her clothes a moment later."
    "Ayesha and I share a meaningful glance, which I hope serves to reassure her."
    show kylie naked
    "Then I begin to take off my clothes as well, trying to inspire her to do the same."
    "Ayesha does just that, but she still lags behind Kylie and I as we all strip."
    show ayesha naked
    "Kylie hops onto the bed and immediately starts giving our instructions."
    show taming bondage with fade
    "Most of the work falls to me, as Ayesha hangs back as much as possible."
    "But there are several points where I need to make use of her strength."
    "Little by little and following Kylie's instructions to the letter, we make progress."
    "Left to my own devices, I'd have been utterly lost."
    "Yet soon enough, Kylie's trussed up in a compromising position."
    "Her wrists are bound together and held up above her head."
    show taming bondage ropes
    "Her ankles are likewise held up, but stretched wide apart."
    "But what strikes me most of all is that Kylie's completely helpless right now."
    "She's putting a hell of a lot of trust in Ayesha and I."
    "Though I guess that's a large part of what she's getting out of all this."
    kylie.say "There you go - I'm totally at your mercy!"
    kylie.say "So, what are you going to do with me?"
    "I look over to where Ayesha's standing."
    "She's beginning to look a little more confident."
    "Like the reality of the situation is finally sinking in."
    "I hold up the blindfold for her to see."
    mike.say "First things first, Ayesha."
    mike.say "You think we need this?"
    menu:
        "Use blindfold":
            "Ayesha glances down at Kylie, gazing at her for a moment."
            "Then she seems to see something in the other girl's eyes."
            "And whatever it is, seems to make up her mind."
            ayesha.say "Yeah, [hero.name]."
            ayesha.say "I think we could use it."
            ayesha.say "All the better to keep Kylie in the dark!"
            "I could argue the point with Ayesha."
            "But the truth is that I want her to be as comfortable as possible."
            "So I decide that deferring to her on this matter is the best thing."
            mike.say "Whatever you say, Ayesha..."
            "I lean forwards and slip the blindfold over Kylie's eyes."
            show taming bondage blindfold
            "She keeps still as I do so, playing along without protest."
            $ blindfolded = True
        "Do not use blindfold":
            "Ayesha glances down at Kylie, gazing at her for a moment."
            "Then she seems to see something in the other girl's eyes."
            "And whatever it is, seems to make up her mind."
            ayesha.say "No, [hero.name]."
            ayesha.say "I think she needs to see this for herself."
            ayesha.say "So we're not using that thing tonight."
            "I could argue the point with Ayesha."
            "But the truth is that I want her to be as comfortable as possible."
            "So I decide that deferring to her on this matter is the best thing."
            mike.say "Whatever you say, Ayesha..."
            "I toss the blindfold aside with a smile."
            $ blindfolded = False
    "But even with that little matter sorted, we still have another to tackle."
    "I stoop down and pick up the dildo that came out of Kylie's bag."
    "Only now do I see that it has straps attached to it."
    "Obviously this thing wasn't brought along with me in mind."
    "But it'd fit Ayesha perfectly."
    "I see her eyeing it, and then she looks up at me."
    mike.say "Okay, Ayesha..."
    mike.say "How are we going to do this?"
    "Ayesha hurries over to where I'm standing."
    "Than she leans in close, preventing Kylie from overhearing what she has to say."
    menu:
        "Fuck Kylie":
            "I can see that Ayesha's a lot more confident than she was to begin with."
            "But there's still a lot of anxiety in the way she's moving and speaking."
            "So much so that I feel like I need to step in and take the lead here."
            mike.say "You leave this to me, Ayesha."
            mike.say "I'll do the deed, itself."
            mike.say "Just jump in where you're comfortable, okay?"
            "Ayesha looks at the strap-on like she's creeped out by it."
            "And I can hear the relief in her voice when she answers me."
            ayesha.say "Okay, [hero.name]."
            ayesha.say "I can handle that."
            ayesha.say "Thanks for looking out for me!"
            "I smile and nod, then turn to face Kylie on the bed."
            show taming bondage mike
            if blindfolded:
                "Kylie feels someone climbing onto the mattress."
                "And she casts her head this way and that."
                kylie.say "Who's there?"
                kylie.say "Who's that creeping towards me?"
            else:
                "Kylie smiles as I climb onto the mattress."
                kylie.say "Oh, I see how it is."
                kylie.say "I'm getting the all natural treatment!"
            ayesha.say "You just wait and see, Kylie."
            ayesha.say "You're going to get what you're given."
            ayesha.say "And you're going to like it!"
            "I don't know if Ayesha was really trying to intimidate Kylie with that last line."
            "But the effect it has is the exact opposite, making her giggle in anticipation."
            "Kylie makes a show of wriggling and writhing as I get ever closer to her."
            "She pulls on the ropes that bind her, the knots holding firm as she does so."
            "Kylie knows very well that the knots she had me tie will hold."
            "She's just putting on a show, pretending to be a damsel in distress."
            "Well, let's see if she can keep the act up when things really get started around here!"
            menu:
                "Fuck her pussy":
                    "I could get really creative in a situation like this."
                    "But maybe all of the ropes make that a little too much?"
                    "Maybe what's really needed here is something simple."
                    "That's why I start using my cock to trace the outline of Kylie's pussy."
                    "I don't have to do anything more than tease her to make the most of the ropes."
                    "Because there's nothing she can do to escape what I'm doing to her."
                    kylie.say "Mmm..."
                    kylie.say "That feels good!"
                    if blindfolded:
                        kylie.say "But is it the real thing?"
                    else:
                        kylie.say "There's nothing like a real one!"
                    "I smile, enjoying the expression on Kylie's face."
                    "I can see her trying her best to keep from showing it."
                    "But the helplessness is making her feel everything with more intensity than usual."
                    "Out of curiosity and more than a little desire, I push harder against her lips."
                    "Kylie moans as nature takes its course and they begin to part before me."
                    "Her head falls back onto the pillow as my cock inches its way inside her."
                    show taming bondage vaginal
                    "Taking full advantage of the situation, I begin to move straight away."
                    "Kylie's wide open and begging for all that I have to give."
                    "And by now her pussy is surrendering to me, warm, wet and welcoming."
                    "I hardly notice Ayesha watching me as I thrust in and out of Kylie."
                    "But she's there alright, watching intently as I have my way."
                    "Slowly I become more aware of just what she's doing too."
                    "Ayesha's hands are straying to certain parts of her body as she watches."
                    "I don't know if she's doing it on purpose, or if she's even aware."
                    "But soon enough, one hand is at her breast."
                    "And the other is slipping between her thighs."
                    "Ayesha's stroking herself as she watches us."
                    "Her breath coming in ragged gasps as she gets ever more excited."
                    "Trust me when I say this."
                    "I'm not forgetting that I'm balls-deep in Kylie right now."
                    "But Ayesha's getting a good deal of my attention as she plays with herself too!"
                    "I try as best I can to tear my eyes away from her, to concentrate on Kylie."
                    "But Ayesha begins to lean over the other girl, reaching out with one hand."
                    "She uses it to trace the lines of Kylie's helpless body."
                    "And she lingers longest over the other girl's exposed breasts."
                    "Ayesha still has one hand between her legs, working her own pussy."
                    "The other explores Kylie's chest, squeezing her breasts and pinching her nipples."
                    "Kylie's head is still buried in the pillows."
                    "But now it's thrashing from side to side as well."
                    "It's as if Kylie's fast approaching her limits."
                    "Like her body just can't take any more of what we're giving it."
                    "She's gasping and moaning like crazy too, sounding like an animal on heat."
                    "I feel like I should have kept on going for longer."
                    "But adding Ayesha's antics into the mix, I just can't hold on!"
                    menu:
                        "Cum inside":
                            "The fact that Kylie's tied up and helpless means that I'm the one in charge here."
                            "So there's nothing to stop me keeping right on until I lose it inside of her."
                            with vpunch
                            "And that's just what I do, putting the very last of my energy into it too."
                            show taming bondage creampie ahegao with vpunch
                            $ kylie.love += 2
                            "Kylie pulls on her bindings as I shoot my load into her, muscles twitching the whole time."
                            with vpunch
                            "She gaps and moans, her own orgasm taking hold of her as well."
                            "When she's done, her head sags down onto the pillow and her entire body goes limp."
                        "Pull out":
                            "The fact that Kylie's tied up and helpless means that I'm the one in charge here."
                            "So there's nothing to stop me adding a little more exquisite torture by pulling out."
                            "And I'm sure to do so before the end, sliding my cock out of Kylie's pussy just in time."
                            show taming bondage -vaginal
                            "Kylie pulls on her bindings in vain, making vague animalistic sounds as way of protest."
                            with vpunch
                            "But by then it's too late, and I shoot my load over her helpless body."
                            show taming bondage cumshot ahegao with vpunch
                            $ kylie.sub += 2
                            "She gaps and moans, her own orgasm taking hold of her as well."
                            with vpunch
                            "When she's done, her head sags down onto the pillow and her entire body goes limp."
                "Fuck her ass":
                    "I could get really creative in a situation like this."
                    "And what better time to take advantage of all these ropes?"
                    "That's why I take aim for something a little unusual."
                    "I start pushing my cock between Kylie's ample buttocks."
                    "I don't have to do anything more than tease her to make the most of the ropes."
                    "Because there's nothing she can do to escape what I'm doing to her."
                    kylie.say "Mmm..."
                    kylie.say "That feels good!"
                    kylie.say "You can have my ass if you want it!"
                    if blindfolded:
                        kylie.say "But is it the real thing?"
                    else:
                        kylie.say "There's nothing like a real one!"
                    "I smile, enjoying the expression on Kylie's face."
                    "I can see her trying her best to keep from showing it."
                    "But the helplessness is making her feel everything with more intensity than usual."
                    "Out of curiosity and more than a little desire, I push harder against her hole."
                    show taming bondage anal surprised
                    "Kylie moans as nature takes its course and they begin to part before me."
                    "Her head falls back onto the pillow as my cock inches its way inside her."
                    "Taking full advantage of the situation, I begin to move straight away."
                    show taming bondage anal shy
                    "Kylie's wide open and begging for all that I have to give."
                    "And by now her ass is surrendering to me, her muscles relaxing just enough."
                    "I hardly notice Ayesha watching me as I thrust in and out of Kylie."
                    "But she's there alright, watching intently as I have my way."
                    "Slowly I become more aware of just what she's doing too."
                    "Ayesha's hands are straying to certain parts of her body as she watches."
                    "I don't know if she's doing it on purpose, or if she's even aware."
                    "But soon enough, one hand is at her breast."
                    "And the other is slipping between her thighs."
                    "Ayesha's stroking herself as she watches us."
                    "Her breath coming in ragged gasps as she gets ever more excited."
                    "Trust me when I say this."
                    "I'm not forgetting that I'm balls-deep in Kylie right now."
                    "But Ayesha's getting a good deal of my attention as she plays with herself too!"
                    "I try as best I can to tear my eyes away from her, to concentrate on Kylie."
                    "But Ayesha begins to lean over the other girl, reaching out with one hand."
                    "She uses it to trace the lines of Kylie's helpless body."
                    "And she lingers longest over the other girl's exposed breasts."
                    "Ayesha still has one hand between her legs, working her own pussy."
                    "The other explores Kylie's chest, squeezing her breasts and pinching her nipples."
                    "Kylie's head is still buried in the pillows."
                    "But now it's thrashing from side to side as well."
                    "It's as if Kylie's fast approaching her limits."
                    "Like her body just can't take any more of what we're giving it."
                    "She's gasping and moaning like crazy too, sounding like an animal on heat."
                    "I feel like I should have kept on going for longer."
                    "But adding Ayesha's antics into the mix, I just can't hold on!"
                    menu:
                        "Cum inside":
                            "The fact that Kylie's tied up and helpless means that I'm the one in charge here."
                            "So there's nothing to stop me keeping right on until I lose it inside of her."
                            with vpunch
                            "And that's just what I do, putting the very last of my energy into it too."
                            show taming bondage creampie ahegao with vpunch
                            $ kylie.love += 2
                            "Kylie pulls on her bindings as I shoot my load into her, muscles twitching the whole time."
                            with vpunch
                            "She gaps and moans, her own orgasm taking hold of her as well."
                            "When she's done, her head sags down onto the pillow and her entire body goes limp."
                        "Pull out":
                            "The fact that Kylie's tied up and helpless means that I'm the one in charge here."
                            "So there's nothing to stop me adding a little more exquisite torture by pulling out."
                            "And I'm sure to do so before the end, sliding my cock out of Kylie's ass just in time."
                            show taming bondage -anal
                            "Kylie pulls on her bindings in vain, making vague animalistic sounds as way of protest."
                            with vpunch
                            "But by then it's too late, and I shoot my load over her helpless body."
                            show taming bondage cumshot ahegao with vpunch
                            $ kylie.sub += 2
                            "She gaps and moans, her own orgasm taking hold of her as well."
                            with vpunch
                            "When she's done, her head sags down onto the pillow and her entire body goes limp."
                    $ kylie.flags.anal += 1
        "Let Ayesha use Kylie":
            "Ayesha seems to shake off a lot of the anxiety she was suffering from just now."
            "In fact, she looks like she does just before going out to wrestle a match in the ring!"
            "She has that expression on her face that lets me know she means business."
            mike.say "You don't have to do anything you don't want to, Ayesha."
            mike.say "I can handle this myself."
            mike.say "Just sit back and watch if that's what you want."
            "Ayesha shakes her head at this."
            "And I watch as she picks up the strap-on."
            ayesha.say "Thanks, but no thanks, [hero.name]."
            ayesha.say "I think this is one of those times I have to face my fears."
            ayesha.say "Just be there to back me up, okay?"
            "I nod as I help Ayesha to secure the strap-on."
            "That done, we turn to face Kylie on the bed."
            show taming bondage ayesha
            if blindfolded:
                "Kylie feels someone climbing onto the mattress."
                "And she casts her head this way and that."
                kylie.say "Who's there?"
                kylie.say "Who's that creeping towards me?"
            else:
                "Kylie smiles as Ayesha climbs onto the mattress."
                kylie.say "Oh, I see how it is."
                kylie.say "I'm getting the chick with a dick!"
            ayesha.say "You just wait and see, Kylie."
            ayesha.say "You're going to get what you're given."
            ayesha.say "And you're going to like it!"
            "I don't know if Ayesha was really trying to intimidate Kylie with that last line."
            "But the effect it has is the exact opposite, making her giggle in anticipation."
            "Kylie makes a show of wriggling and writhing as Ayesha gets closer to her."
            "She pulls on the ropes that bind her, the knots holding firm as she does so."
            "Kylie knows very well that the knots she had me tie will hold."
            "She's just putting on a show, pretending to be a damsel in distress."
            "Well, let's see if she can keep the act up when things really get started around here!"
            menu:
                "Ayesha fucks Kylie's pussy":
                    "It's strange for me to watch as Ayesha gets ever closer to Kylie."
                    "Firstly because I'm not used to watching other people get it on."
                    "And secondly because I can't help thinking what I'd do differently."
                    "Then there's the way that Ayesha's confidence seems to be growing by the second."
                    "Before we got started she was unsure about even getting involved in all of this."
                    "But now she's wearing the strap-on like it's empowering her!"
                    "I watch as she lowers herself over Kylie's helpless form."
                    "And I can't help leaning in closer to watch where the dildo's going."
                    "For a moment I honestly think that Ayesha's going to go for the ass."
                    "But then the head of the dildo slides along Kylie's lips."
                    "She's trying to hold back, to make this tougher for Ayesha."
                    "Yet she can't help letting out a long, low moan of pleasure."
                    kylie.say "Mmm..."
                    kylie.say "That feels good!"
                    if blindfolded:
                        kylie.say "But is it the real thing?"
                    else:
                        kylie.say "There's nothing like a real one!"
                    "I see a wry grin spread across Ayesha's face."
                    "She seems to be taking Kylie's words as a challenge."
                    "All it takes is a little more pressure from Ayesha."
                    show taming bondage vaginal
                    "As she leans into it, Kylie's lips begin to surrender."
                    "She moans again as her body submits, her lips parting."
                    "And I watch in fascination as the dildo sinks into her."
                    "Ayesha stays silent as she begins to fuck Kylie."
                    "All of her concentration is focused on the task at hand."
                    "The lithe, powerful muscles of her body begin to move."
                    "And all of that motion in turn moves the dildo inside of Kylie."
                    "Ayesha's not just going through the motions either."
                    "I can see that she's doing all she can to emulate the real thing."
                    "Her body moves in a way that's startlingly familiar to me."
                    "It's almost the exact same way I'd be moving were I the one doing the fucking!"
                    "Has Ayesha been watching me that closely when we're made love in the past?"
                    "Because she's doing an amazing job on Kylie right now!"
                    "And she looks like she's enjoying herself too."
                    "I know that Ayesha has a deep mistrust of Kylie."
                    "Sure, it's faded since we started this threesome thing up."
                    "But I can't help thinking what she's doing to Kylie is helping Ayesha to cope."
                    "It's like she's finally able to assert herself over the other girl."
                    "Able to dominate her in an acceptable manner."
                    "And the whole thing is incredibly hot from my point of view too!"
                    "I don't honestly remember how my cock ended up in my hand."
                    "But it's hard and I just can't keep from stroking it as I watch."
                    "I lean in close, taking the chance to play with Kylie's helpless form."
                    "I squeeze her breasts, pinch her nipples and whatever else takes my fancy."
                    "After all, there's nothing she can do to stop me."
                    "Caressed, stroked and penetrated from all angles, Kylie writhes on the bed."
                    "She tugs in vain at the bonds that she had us tie, helpless to resist."
                    "And all she achieves is to heighten the effect of all we're doing to her."
                    kylie.say "Ah..."
                    kylie.say "Oh god..."
                    kylie.say "Please...I'm going to..."
                    "Kylie hardly needs to finish what she was going to say."
                    "Ayesha and I know exactly what's about to happen."
                    menu:
                        "Ayesha stays inside":
                            "Even so, Ayesha doesn't stop or even slow down."
                            "She seems determined to pound Kylie to the last."
                            "So that's exactly how it happens."
                            "Kylie bucks and wriggles on the end of the dildo."
                            show taming bondage ahegao
                            $ kylie.love += 2
                            $ ayesha.love += 2
                            "And I feel myself losing it too."
                            with vpunch
                            "Without asking permission, I shoot my load over Kylie's belly."
                            with vpunch
                            "Warm, sticky white cum stripes her stomach."
                            "When she's done, her head sags down onto the pillow and her entire body goes limp."
                        "Ayesha pulls out":
                            "All of a sudden, Ayesha yanks the dildo out of Kylie."
                            show taming bondage -vaginal
                            "The other girl bucks and wriggles as it slides out of her."
                            "And I feel myself losing it too."
                            show taming bondage ahegao with vpunch
                            $ kylie.sub += 2
                            $ ayesha.sub += 2
                            "Without asking permission, I shoot my load over Kylie's belly."
                            with vpunch
                            "Warm, sticky white cum stripes her stomach."
                            "When she's done, her head sags down onto the pillow and her entire body goes limp."
                "Ayesha fucks Kylie's ass":
                    "It's strange for me to watch as Ayesha gets ever closer to Kylie."
                    "Firstly because I'm not used to watching other people get it on."
                    "And secondly because I can't help thinking what I'd do differently."
                    "Then there's the way that Ayesha's confidence seems to be growing by the second."
                    "Before we got started she was unsure about even getting involved in all of this."
                    "But now she's wearing the strap-on like it's empowering her!"
                    "I watch as she lowers herself over Kylie's helpless form."
                    "And I can't help leaning in closer to watch where the dildo's going."
                    "For a moment I honestly think that Ayesha's going to go for the pussy."
                    "But then the head of the dildo slides between kylie's buttocks."
                    "She's trying to hold back, to make this tougher for Ayesha."
                    "Yet she can't help letting out a long, low moan of pleasure."
                    kylie.say "Mmm..."
                    kylie.say "That feels good!"
                    kylie.say "You can have my ass if you want it!"
                    if blindfolded:
                        kylie.say "But is it the real thing?"
                    else:
                        kylie.say "There's nothing like a real one!"
                    "I see a wry grin spread across Ayesha's face."
                    "She seems to be taking Kylie's words as a challenge."
                    "All it takes is a little more pressure from Ayesha."
                    "As she leans into it, Kylie's buttocks begin to part."
                    show taming bondage anal
                    "She moans again as her body submits, muscles slacking off."
                    "And I watch in fascination as the dildo sinks into her."
                    "Ayesha stays silent as she begins to fuck Kylie."
                    "All of her concentration is focused on the task at hand."
                    "The lithe, powerful muscles of her body begin to move."
                    "And all of that motion in turn moves the dildo inside of Kylie."
                    "Ayesha's not just going through the motions either."
                    "I can see that she's doing all she can to emulate the real thing."
                    "Her body moves in a way that's startlingly familiar to me."
                    "It's almost the exact same way I'd be moving were I the one doing the fucking!"
                    "Has Ayesha been watching me that closely when we're made love in the past?"
                    "Because she's doing an amazing job on Kylie right now!"
                    "And she looks like she's enjoying herself too."
                    "I know that Ayesha has a deep mistrust of Kylie."
                    "Sure, it's faded since we started this threesome thing up."
                    "But I can't help thinking what she's doing to Kylie is helping Ayesha to cope."
                    "It's like she's finally able to assert herself over the other girl."
                    "Able to dominate her in an acceptable manner."
                    "And the whole thing is incredibly hot from my point of view too!"
                    "I don't honestly remember how my cock ended up in my hand."
                    "But it's hard and I just can't keep from stroking it as I watch."
                    "I lean in close, taking the chance to play with Kylie's helpless form."
                    "I squeeze her breasts, pinch her nipples and whatever else takes my fancy."
                    "After all, there's nothing she can do to stop me."
                    "Caressed, stroked and penetrated from all angles, Kylie writhes on the bed."
                    "She tugs in vain at the bonds that she had us tie, helpless to resist."
                    "And all she achieves is to heighten the effect of all we're doing to her."
                    kylie.say "Ah..."
                    kylie.say "Oh god..."
                    kylie.say "Please...I'm going to..."
                    "Kylie hardly needs to finish what she was going to say."
                    "Ayesha and I know exactly what's about to happen."
                    menu:
                        "Ayesha stays inside":
                            "Even so, Ayesha doesn't stop or even slow down."
                            "She seems determined to pound Kylie to the last."
                            "So that's exactly how it happens."
                            "Kylie bucks and wriggles on the end of the dildo."
                            show taming bondage ahegao
                            $ kylie.love += 2
                            $ ayesha.love += 2
                            "And I feel myself losing it too."
                            with vpunch
                            "Without asking permission, I shoot my load over Kylie's belly."
                            with vpunch
                            "Warm, sticky white cum stripes her stomach."
                            "When she's done, her head sags down onto the pillow and her entire body goes limp."
                        "Ayesha pulls out":
                            "All of a sudden, Ayesha yanks the dildo out of Kylie."
                            show taming bondage -anal
                            "The other girl bucks and wriggles as it slides out of her."
                            "And I feel myself losing it too."
                            show taming bondage ahegao with vpunch
                            $ kylie.sub += 2
                            $ ayesha.sub += 2
                            "Without asking permission, I shoot my load over Kylie's belly."
                            with vpunch
                            "Warm, sticky white cum stripes her stomach."
                            "When she's done, her head sags down onto the pillow and her entire body goes limp."
            $ ayesha.sexperience += 1
    show taming bondage -mike -ayesha
    "Afterwards, Ayesha and I are pretty much slumped on the bed."
    "We're both breathing heavily and slick with sweat."
    "But I can see from the look on Ayesha's face that she got something out of this."
    "She was afraid when we started out, yet now she looks calm and confident."
    "We exchange a smile, not needing to say or do anything more."
    kylie.say "Ah..."
    kylie.say "Hello?"
    show taming bondage surprised
    kylie.say "Aren't you forgetting something?"
    "Ayesha and I glance over to where Kylie's still tied up at the other end of the bed."
    "She fixes us with a meaningful glare and then motions to her bonds."
    mike.say "I guess we should untie her, Ayesha."
    ayesha.say "Yeah, yeah..."
    ayesha.say "But we don't have to be quick about it!"
    $ kylie.sexperience += 1
    $ game.flags.taming_delay = TemporaryFlag(True, 1)
    return

label taming_event_05:
    scene bg bedroom1 with fade
    "I'd never have thought it possible when the three of us started out down this road."
    "But they way things have been going recently between Ayesha, Kylie and I..."
    "Well, I think it's actually starting to turn into a real relationship, you know?"
    "A partnership between three equal parties, where everyone contributes something unique."
    "Ayesha's the one with a hard exterior and tender depths hidden beneath it."
    "Kylie's the one that looks like a porcelain doll, but has red-blooded passion inside of her."
    "And me...well...I guess you'd have to ask Ayesha and Kylie to describe my unique qualities!"
    "But I know for sure that one of them is knowing how to have fun in the bedroom!"
    "Right now I have the perfect chance to remind them of that too."
    show ayesha date at right5
    show kylie date at left5
    with dissolve
    "Because Ayesha and Kylie are standing right here in my room."
    "And they're stripping off their clothes too!"
    show ayesha naked annoyed
    show kylie naked
    ayesha.say "Hurry up, [hero.name]!"
    ayesha.say "What are you waiting for?"
    ayesha.say "You need to get undressed too!"
    "Ayesha sounds genuinely exasperated at my lagging behind."
    show kylie happy
    "But Kylie just sniggers and shakes her head."
    kylie.say "Don't be so naive, Ayesha."
    kylie.say "He knows exactly what he's doing."
    show kylie blush
    kylie.say "The perv's getting off on watching us strip!"
    "I frown at Kylie as I begin to pull off my own clothes."
    mike.say "How can I be a pervert, Kylie?"
    mike.say "I'm watching my girlfriends take off their clothes before we have sex!"
    mike.say "In a few minutes, we're all going to be naked."
    mike.say "Then I'll have all of that exposed flesh shoved in my face!"
    show ayesha sad
    "Ayesha shakes her head and gives Kylie a despairing look."
    show kylie happy
    "And in response, Kylie just sniggers again."
    kylie.say "Oh, you're still a perv, [hero.name], trust me."
    kylie.say "You're just lucky that perverts really turn me on!"
    show ayesha normal
    show kylie normal
    "For her part, Ayesha lets out a derisive snort."
    "Then she looks admiringly as I pull down my shorts."
    ayesha.say "I don't know about any of that."
    ayesha.say "But I do know that I want some of that!"
    show ayesha blush
    ayesha.say "I can already feel it inside of me!"
    kylie.say "Hey, look, Ayesha..."
    show kylie happy
    kylie.say "I think it heard you!"
    "Ayesha and Kylie giggle at the sight of my cock beginning to get hard."
    "Myself, I don't know whether to be flattered or embarrassed."
    mike.say "Hey!"
    mike.say "It's not like I can help it, you know!"
    mike.say "I'm naked in the company of two hot girls."
    mike.say "And you'd be the first to complain if this wasn't happening right now!"
    show ayesha normal
    ayesha.say "The man has got a point, Kylie."
    show kylie normal
    kylie.say "And we need it pointing somewhere useful, Ayesha!"
    "A moment later, I find myself flanked by Ayesha and Kylie."
    "They take an arm each and lead me towards the bed."
    mike.say "Hey, there's no need to march me there!"
    mike.say "That's where I was headed for anyway."
    "Once we're there, the girls shove me down onto the bed."
    "I lie there looking up at them, liking where this is going."
    "But so far, I kind of feel like they've had all the say."
    "And it's time I asserted myself a little..."
    menu:
        "Fuck Ayesha":
            "Ayesha looks full of confidence as she stands over me."
            "She has her hands planted on her hips like she's firmly in charge."
            "So maybe the easiest way to take control would be to tackle the alpha female first?"
            "Without a word of warning, I sit up and grab Ayesha by the haunches."
            "She's solid as a rock and strong as a bull."
            "But I still manage to take her by surprise and pull her down onto me."
            scene taming threesome ayeshafuck with fade
            ayesha.say "Wha..."
            ayesha.say "What are you..."
            kylie.say "Looks like you're it, Ayesha."
            kylie.say "Have fun!"
            "Before Ayesha can resist, Kylie pounces on her from behind."
            "And together we drawn her down onto the bed."
            "Though from my angle, I can decide just where my cock goes..."
            menu:
                "Fuck her pussy":
                    "While Ayesha's muscles are hard, her pussy definitely isn't."
                    "And the sound that she makes as my cock rubs against it is softer still."
                    "I know that Ayesha has a tiger tattooed on her arm."
                    "But right now she's almost purring like a contented kitten!"
                    kylie.say "Oh..."
                    kylie.say "I think she likes that!"
                    "I try to ignore Kylie's barbed comments."
                    show taming threesome ayeshafuck vaginal
                    "Instead guiding Ayesha gently down and onto my cock."
                    "But there's something intriguing about the expression on her face."
                    "And I feel like I have to ask the question myself, just out of genuine curiosity."
                    mike.say "Is she right, Ayesha?"
                    mike.say "Are you having a good time?"
                    ayesha.say "Mmm..."
                    ayesha.say "Yeah, I'm having a good time..."
                    ayesha.say "The best time!"
                    kylie.say "Told you!"
                    "I shoot Kylie a warning glance."
                    "Nothing serious, just enough to let her know she's on thin ice."
                    "And she seems to get the message, holding her hands up and backing off."
                    "That means, for the moment at least, I'm left to concentrate on Ayesha."
                    "I gaze up at her as she rides my cock, moving slowly up and down."
                    "She has her eyes closed, as though she's savouring every moment."
                    "The muscles of her body are like moving coils of rope under her skin."
                    "But the expression on her face is gentle, almost innocent."
                    "And it betrays the side of Ayesha that she tries so hard to keep hidden."
                    "I'm watching her with fascination, when something obscures my vision."
                    kylie.say "Hey, big girl..."
                    kylie.say "Make yourself useful!"
                    show taming threesome ayeshafuck kylie
                    "I look up to see Kylie standing over me."
                    "And she has Ayesha's head just below her waist."
                    show taming threesome ayeshafuck kyliehand
                    "Without asking for permission, Kylie thrusts herself forwards."
                    "Ayesha has no choice as the other girl's pussy meets her mouth."
                    "But she nods all the same, already parting her lips."
                    show taming threesome ayeshafuck lick down
                    "I keep on thrusting in and out of Ayesha at the same time."
                    "And I'm watching her as she goes to work on Kylie's pussy."
                    show taming threesome ayeshafuck lick middle kyliepleasure
                    "Soon enough, both of them are moaning."
                    "As for me, well, I'm sweating away underneath them both!"
                    show taming threesome ayeshafuck lick up
                    "And it looks like my efforts are about to pay off too!"
                    mike.say "I..."
                    show taming threesome ayeshafuck lick middle
                    mike.say "I'm gonna cum!"
                    menu:
                        "Cum inside":
                            "I love the sensation of Ayesha's weight above me."
                            show taming threesome ayeshafuck lick down
                            "It's so reassuring that I don't want to lose that feeling."
                            with vpunch
                            "So I make one last thrust into her as I cum."
                            show taming threesome ayeshafuck -lick creampie with vpunch
                            "Ayesha tears her lips away from Kylie's pussy and cries out as I do so."
                            show taming threesome ayeshafuck ayeshaahegao with vpunch
                            $ ayesha.love += 2
                            "Her muscles squeeze me tightly, making the sensation that much more intense."
                            "And then Ayesha's head droops, and she pants like she's run a marathon."
                        "Pull out":
                            "I love the sensation of Ayesha's weight above me."
                            "It's so reassuring that I don't want to lose that feeling."
                            show taming threesome ayeshafuck lick down
                            "But I want to shoot my load somewhere else instead."
                            "So I drag my cock out of Ayesha's pussy at the last possible moment."
                            show taming threesome ayeshafuck -vaginal
                            "Ayesha tears her lips away from Kylie's pussy and cries out as I do so."
                            show taming threesome ayeshafuck ayeshaahegao cumshot with vpunch
                            $ ayesha.sub += 2
                            "I shoot my load up her back and over her buttocks."
                            show taming threesome ayeshafuck cum onbody with vpunch
                            "And then Ayesha's head droops, and she pants like she's run a marathon."
                "Fuck her ass":
                    "While Ayesha's muscles are hard, even the ones in her ass."
                    "I can feel just how tight they are as my cock slips between her buttocks."
                    "I know that Ayesha has a tiger tattooed on her arm."
                    "But right now she's almost purring like a contented kitten!"
                    ayesha.say "Mmm..."
                    ayesha.say "You want my ass, huh?"
                    ayesha.say "Well you can have it, babe!"
                    kylie.say "Oh..."
                    kylie.say "I think she likes that!"
                    "I try to ignore Kylie's barbed comments."
                    show taming threesome ayeshafuck anal
                    "Instead guiding Ayesha gently down and onto my cock."
                    "But there's something intriguing about the expression on her face."
                    "And I feel like I have to ask the question myself, just out of genuine curiosity."
                    mike.say "Is she right, Ayesha?"
                    mike.say "Are you having a good time?"
                    ayesha.say "Mmm..."
                    ayesha.say "Yeah, I'm having a good time..."
                    ayesha.say "The best time!"
                    kylie.say "Told you!"
                    "I shoot Kylie a warning glance."
                    "Nothing serious, just enough to let her know she's on thin ice."
                    "And she seems to get the message, holding her hands up and backing off."
                    "That means, for the moment at least, I'm left to concentrate on Ayesha."
                    "I gaze up at her as she rides my cock, moving slowly up and down."
                    "Her ass is tight, but it feels incredible to be buried inside of it."
                    "She has her eyes closed, as though she's savouring every moment."
                    "The muscles of her body are like moving coils of rope under her skin."
                    "But the expression on her face is gentle, almost innocent."
                    "And it betrays the side of Ayesha that she tries so hard to keep hidden."
                    "I'm watching her with fascination, when something obscures my vision."
                    kylie.say "Hey, big girl..."
                    kylie.say "Make yourself useful!"
                    show taming threesome ayeshafuck kylie
                    "I look up to see Kylie standing over me."
                    "And she has Ayesha's head just below her waist."
                    show taming threesome ayeshafuck kyliehand
                    "Without asking for permission, Kylie thrusts herself forwards."
                    "Ayesha has no choice as the other girl's pussy meets her mouth."
                    "But she nods all the same, already parting her lips."
                    show taming threesome ayeshafuck lick down
                    "I keep on thrusting in and out of Ayesha at the same time."
                    "And I'm watching her as she goes to work on Kylie's pussy."
                    show taming threesome ayeshafuck lick middle kyliepleasure
                    "Soon enough, both of them are moaning."
                    "As for me, well, I'm sweating away underneath them both!"
                    show taming threesome ayeshafuck lick up
                    "And it looks like my efforts are about to pay off too!"
                    mike.say "I..."
                    show taming threesome ayeshafuck lick middle
                    mike.say "I'm gonna cum!"
                    menu:
                        "Cum inside":
                            "I love the sensation of Ayesha's weight above me."
                            show taming threesome ayeshafuck lick down
                            "It's so reassuring that I don't want to lose that feeling."
                            with vpunch
                            "So I make one last thrust into her as I cum."
                            show taming threesome ayeshafuck -lick creampie with vpunch
                            "Ayesha tears her lips away from Kylie's pussy and cries out as I do so."
                            show taming threesome ayeshafuck ayeshaahegao with vpunch
                            $ ayesha.love += 2
                            "Her muscles squeeze me tightly, making the sensation that much more intense."
                            "And then Ayesha's head droops, and she pants like she's run a marathon."
                        "Pull out":
                            "I love the sensation of Ayesha's weight above me."
                            "It's so reassuring that I don't want to lose that feeling."
                            show taming threesome ayeshafuck lick down
                            "But I want to shoot my load somewhere else instead."
                            "So I drag my cock out of Ayesha's ass at the last possible moment."
                            show taming threesome ayeshafuck -anal
                            "Ayesha tears her lips away from Kylie's pussy and cries out as I do so."
                            show taming threesome ayeshafuck ayeshaahegao cumshot with vpunch
                            $ ayesha.sub += 2
                            "I shoot my load up her back and over her buttocks."
                            show taming threesome ayeshafuck cum onbody with vpunch
                            "And then Ayesha's head droops, and she pants like she's run a marathon."
                    $ ayesha.flags.anal += 1
            $ ayesha.sexperience += 1
        "Fuck Kylie":
            "Maybe the best way to do that is to wipe the smile off Kylie's face?"
            "And by that I don't mean make her frown, I'm not a mean bastard!"
            "I just plan to put a very different kind of smile in it's place, that's all!"
            "That's why I grab hold of Kylie's haunches with both hands."
            "She yelps in surprise and tries to wriggle free."
            kylie.say "Hey!"
            kylie.say "What are you doing?!?"
            scene taming threesome kyliefuck
            show taming threesome kyliefuck mike
            "But it's not like Kylie's thighs are anything but generous in their proportions."
            "So I have plenty to hold onto as I pull her down onto the bed beside me."
            "Perhaps sensing a chance to gain a measure of revenge, Ayesha hurries to help."
            "Before Kylie can even try to escape, the other girl pounces on her like a big cat."
            "And together we make sure Kylie is pinned down on the bed."
            menu:
                "Fuck her pussy":
                    "Lifting Kylie's right leg in the air, I take aim with my cock."
                    "Everything between her legs is now laid open to me."
                    "And I can already see something that I like the look of."
                    "Already slick and glistening in the light, her pussy looks so inviting."
                    kylie.say "You see something you want, huh?"
                    kylie.say "Well, what are you waiting for?"
                    kylie.say "Hurry up and take it already!"
                    "Well, it'd be rude not to do as the lady says!"
                    "So I rub the head of my cock along Kylie's lips."
                    show taming threesome kyliefuck vaginal
                    "And instantly I hear the tone of her voice change."
                    "Just as her entire body begins to quiver at the same time."
                    kylie.say "Mmm..."
                    kylie.say "Oh...oh yeah..."
                    kylie.say "Please...give it to me?"
                    "I can't help smiling at the sudden change in Kylie's demeanour."
                    "A moment before she was all defiance, almost challenging my manhood."
                    "And now she's practically begging for me to take her!"
                    "Without pausing to think, I begin to push my cock into her."
                    show taming threesome kyliefuck kyliepleasure
                    "Kylie pants as I do so, nodding almost in desperation."
                    "Is this all down to me?"
                    "Am I really this damn good?"
                    "It's at that moment I chance to look down and see Ayesha."
                    "She's down on her belly, crawling over the bed."
                    "But she's also crawling over Kylie too!"
                    show taming threesome kyliefuck ayesha kylienormal
                    "As my cock sinks deeper into Kylie's pussy, I watch Ayesha's progress."
                    "She's using her hands, lips and tongue."
                    "Caressing every sensitive part of Kylie's body."
                    "So it's not just me that's got her in such a state."
                    "Ayesha's been lending a helping hand too!"
                    "I smile and quicken my pace as Ayesha's hands reach Kylie's breasts."
                    "I don't resent the effect Ayesha's having on Kylie."
                    "Quite the opposite, I love watching her play with the other girl."
                    "My cock feels good inside of Kylie's pussy, thrusting in and out."
                    "But there's no way I could reach the parts of her that Ayesha can."
                    show taming threesome kyliefuck lick closed
                    "And together we work to overwhelm Kylie."
                    "Together we can push her further than we ever could alone."
                    "Kylie nods her head desperately, moaning with pleasure."
                    "Neither of us needs to be urged on though."
                    "Ayesha and I are on a mission, working towards a higher goal."
                    "Just how far can we push Kylie before she can't take any more?"
                    kylie.say "Oh..."
                    kylie.say "Oh my..."
                    show taming threesome kyliefuck kyliepleasure
                    kylie.say "I don't think I can take any more!"
                    "Whoa..."
                    "Now that's an uncanny coincidence!"
                    "And as it happens, neither can I!"
                    mike.say "Me too, Kylie!"
                    mike.say "Here it comes!"
                    menu:
                        "Cum inside":
                            "The only way I can see this ending is with me losing it inside of Kylie."
                            show taming threesome kyliefuck opened
                            "So I don't pause or hesitate for even a moment, I just keep right on going."
                            "It doesn't take long for me to reach my climax after that."
                            show taming threesome kyliefuck creampie with hpunch
                            $ kylie.love += 2
                            "And I'm as deep inside of her as possible when it happens."
                            show taming threesome kyliefuck kylieahegao with hpunch
                            "Kylie moans and quivers, taking everything I have to give."
                            "And then she collapses against me, utterly spent."
                        "Pull out":
                            "Still holding onto Kylie's haunches, I pull my cock out of her."
                            show taming threesome kyliefuck opened -vaginal
                            "She moans at the sensation, already beginning to cum herself."
                            "And she's well into the throes of her orgasm when mine hits too."
                            show taming threesome kyliefuck cumshot with hpunch
                            $ kylie.sub += 2
                            "Warm, sticky cum rains down on the small of Kylie's back."
                            show taming threesome kyliefuck cum with hpunch
                            "Then it runs down her legs, and I feel it as she squirms against me."
                            "And then she collapses against me, utterly spent."
                "Fuck her ass":
                    "Lifting Kylie's right leg in the air, I take aim with my cock."
                    "Everything between her legs is now laid open to me."
                    "And I can already see something that I like the look of."
                    "So neat and tight as it nestles between her buttocks."
                    "I feel like Kylie's ass is calling to me!"
                    kylie.say "You see something you want, huh?"
                    kylie.say "Well, what are you waiting for?"
                    kylie.say "Hurry up and take it already!"
                    "Well, it'd be rude not to do as the lady says!"
                    "So I rub the head of my cock between Kylie's buttocks."
                    show taming threesome kyliefuck anal
                    "And instantly I hear the tone of her voice change."
                    "Just as her entire body begins to quiver at the same time."
                    kylie.say "M...my ass?!?"
                    kylie.say "I mean...sure...of course!"
                    kylie.say "Oh...oh yeah..."
                    kylie.say "Please...give it to me?"
                    "I can't help smiling at the sudden change in Kylie's demeanour."
                    "A moment before she was all defiance, almost challenging my manhood."
                    "And now she's practically begging for me to take her!"
                    "Without pausing to think, I begin to push my cock into her."
                    show taming threesome kyliefuck kyliepleasure
                    "Kylie pants as I do so, nodding almost in desperation."
                    "The muscles of her ass are tight as hell."
                    "But they soon begin to yield to me as I push inside of her."
                    "Is this all down to me?"
                    "Am I really this damn good?"
                    "It's at that moment I chance to look down and see Ayesha."
                    "She's down on her belly, crawling over the bed."
                    "But she's also crawling over Kylie too!"
                    show taming threesome kyliefuck ayesha kylienormal
                    "As my cock sinks deeper into Kylie's ass, I watch Ayesha's progress."
                    "She's using her hands, lips and tongue."
                    "Caressing every sensitive part of Kylie's body."
                    "So it's not just me that's got her in such a state."
                    "Ayesha's been lending a helping hand too!"
                    "I smile and quicken my pace as Ayesha's hands reach Kylie's breasts."
                    "I don't resent the effect Ayesha's having on Kylie."
                    "Quite the opposite, I love watching her play with the other girl."
                    "My cock feels good inside of Kylie's ass, thrusting in and out."
                    "But there's no way I could reach the parts of her that Ayesha can."
                    show taming threesome kyliefuck lick closed
                    "And together we work to overwhelm Kylie."
                    "Together we can push her further than we ever could alone."
                    "Kylie nods her head desperately, moaning with pleasure."
                    "Neither of us needs to be urged on though."
                    "Ayesha and I are on a mission, working towards a higher goal."
                    "Just how far can we push Kylie before she can't take any more?"
                    kylie.say "Oh..."
                    kylie.say "Oh my..."
                    show taming threesome kyliefuck kyliepleasure
                    kylie.say "I don't think I can take any more!"
                    "Whoa..."
                    "Now that's an uncanny coincidence!"
                    "And as it happens, neither can I!"
                    mike.say "Me too, Kylie!"
                    mike.say "Here it comes!"
                    menu:
                        "Cum inside":
                            "The only way I can see this ending is with me losing it inside of Kylie."
                            show taming threesome kyliefuck opened
                            "So I don't pause or hesitate for even a moment, I just keep right on going."
                            "It doesn't take long for me to reach my climax after that."
                            show taming threesome kyliefuck creampie with hpunch
                            "And I'm as deep inside of her as possible when it happens."
                            show taming threesome kyliefuck kylieahegao with hpunch
                            $ kylie.love += 2
                            "Kylie moans and quivers, taking everything I have to give."
                            "And then she collapses against me, utterly spent."
                        "Pull out of Kylie's ass":
                            "Still holding onto Kylie's haunches, I pull my cock out of her."
                            show taming threesome kyliefuck opened -anal
                            "She moans at the sensation, already beginning to cum herself."
                            "And she's well into the throes of her orgasm when mine hits too."
                            show taming threesome kyliefuck cumshot with hpunch
                            $ kylie.sub += 2
                            "Warm, sticky cum rains down on the small of Kylie's back."
                            show taming threesome kyliefuck cum with hpunch
                            "Then it runs down her legs, and I feel it as she squirms against me."
                            "And then she collapses against me, utterly spent."
                    $ kylie.flags.anal += 1
            $ kylie.sexperience += 1
    scene bg bedroom1
    show ayesha b naked happy at center, zoomAt(2, (360, 1380))
    show kylie b naked smile at center, zoomAt(2, (920, 1380))
    with fade
    "Afterwards, I lie back and try to catch my breath."
    "I'm exhausted and physically satisfied."
    "But I'm waiting for the inevitable squabbling to begin."
    "Yet, much to my surprise, both Ayesha and Kylie are silent."
    "Neither of them seems in the mood to start an argument."
    "Is this the answer to making them get along?"
    "Do I just have to wear them out in the bedroom to make peace?"
    "I mean, that sounds like a really fun way to get the job done."
    "But I just don't know if I have the stamina to do this all the damn time!"
    $ game.flags.taming_delay = TemporaryFlag(True, 1)
    return

label ayesha_kylie_propose_male:
    "Do you ever feel like everything in life is a balancing act?"
    "Like nothing ever works out until one thing is equal to another?"
    "Well, I didn't have that feeling until pretty recently."
    "To be more specific, until the time I started dating Ayesha and Kylie."
    "Before that, it was all about the crazy extremes those two represent."
    show ayesha casual at left with dissolve
    "On the one hand, there was Ayesha."
    "An Amazonian goddess on the outside, but sensitive and vulnerable on the inside."
    show kylie casual at right with dissolve
    "On the other, there was Kylie."
    "Sweet and innocent on the outside, but intense and sometimes even crazy on the inside!"
    "And when they came together, all they seemed to do was bring out the worst in each other."
    show kylie angry
    "Kylie became possessive and tried to do everything she could to drive Ayesha off."
    show ayesha annoyed
    "In turn, Ayesha used her superior strength to put the other girl in her place!"
    "I thought that them coming into contact with each other was the end of it all."
    "That the two of them could never learn to get along."
    "But somehow I was wrong."
    show ayesha at left4 with ease
    "Ayesha put the breaks on Kylie's craziness."
    show kylie at right4 with ease
    "And Kylie managed to get beyond Ayesha's barriers too."
    show ayesha happy
    show kylie happy
    "In fact, we're getting on so well as a trio that I want to take things to the next level."
    "Which is why I choose my moment carefully."
    "And then I drop down onto one knee..."
    ayesha.say "That's the whole point, Kylie."
    ayesha.say "You make the moves LOOK painful."
    show ayesha annoyed
    ayesha.say "But you're not really trying to hurt the other girl, yeah?"
    kylie.say "I know, I know..."
    kylie.say "But some of that stuff you do is real - it has to be!"
    show kylie annoyed
    kylie.say "Like the choke-holds?"
    kylie.say "They work for real, don't they?"
    show ayesha normal
    ayesha.say "Well...yeah, I guess..."
    ayesha.say "But that's not the point, Kylie..."
    ayesha.say "Erm...[hero.name]..."
    show kylie normal
    kylie.say "What are you doing?"
    "I can't help looking more than a little puzzled by the question."
    mike.say "Really?"
    mike.say "I'm kneeling down here."
    mike.say "And I've got a pair of matching rings in my hand!"
    mike.say "I know it's a surprise guys."
    mike.say "But I'd have thought it was pretty obvious!"
    ayesha.say "Oh..."
    show ayesha mindless
    ayesha.say "Oh god!"
    kylie.say "You..."
    show kylie surprised
    kylie.say "You're..."
    mike.say "That's right - I'm asking you to marry me."
    mike.say "So what do you say?"
    show ayesha normal
    show kylie normal
    if ayesha.love >= 195 and kylie.love >= 195:
        "For a moment I think that I've totally misjudged the situation."
        "Ayesha and Kylie are totally silent as they stare at me."
        "Then I see them slowly exchange a meaningful glance."
        "And I can feel myself swallowing in anticipation."
        show kylie happy at right4, vshake
        show fx exclamation at right4
        kylie.say "OF COURSE WE WILL!"
        show kylie crazyhappy
        kylie.say "Oh, [hero.name] - this is just perfect!"
        ayesha.say "Yeah, [hero.name]."
        show ayesha happy
        ayesha.say "It's a yes from me too!"
        "I can feel the sense of relief as it passes through me."
        "Like a surge of adrenaline that leaves me shaking."
        "And all I can think to do is hurry and put on the rings."
        "As if the deal isn't done until they're on the girl's fingers."
        mike.say "I...I..."
        mike.say "I can't believe this is actually happening!"
        "Ayesha and Kylie look up from admiring their rings as one."
        ayesha.say "Well it is."
        ayesha.say "So you'd better get used to having two wives!"
        kylie.say "Yeah, [hero.name]."
        show kylie smile
        kylie.say "You've got the both of us to keep happy now!"
        $ ayesha.set_fiance()
        $ kylie.set_fiance()
    elif ayesha.love >= 195 and kylie.love < 195:
        "For a moment I think that I've totally misjudged the situation."
        "Ayesha and Kylie are totally silent as they stare at me."
        "Then I see them slowly exchange a meaningful glance."
        "And I can feel myself swallowing in anticipation."
        ayesha.say "Wow..."
        ayesha.say "That kind of came out of nowhere!"
        show ayesha happy
        ayesha.say "But yeah, I will!"
        show kylie sad at right4, vshake
        kylie.say "NO WAY!"
        show kylie crazysad
        kylie.say "I want to marry you, [hero.name]!"
        show kylie at right5 with move
        kylie.say "Not her!"
        "I'm feeling a bizarre mix of emotions as all of this takes place."
        "On the one hand I'm delighted that Ayesha said yes."
        "But on the other I don't know what to make of Kylie's answer."
        ayesha.say "Wait a minute..."
        show ayesha angry at left5 with move
        ayesha.say "You're saying you don't want to marry ME?!?"
        kylie.say "No, I don't."
        show kylie angry
        kylie.say "It's supposed to be me and [hero.name]!"
        kylie.say "That's the way I always imagined it!"
        kylie.say "And if I can't have him to myself..."
        kylie.say "Well, then nobody can have him!"
        show ayesha happy
        "Ayesha clings to me as something seems to change in Kylie."
        show kylie yandere
        "There's suddenly a darkness in her eyes."
        "One that I haven't seen in a long while."
        hide kylie with moveoutright
        "And she storms off before either of us can say another word."
        $ ayesha.set_fiance()
        $ kylie.love -= 25
        $ kylie.sub -= 25
    elif ayesha.love < 195 and kylie.love >= 195:
        "For a moment I think that I've totally misjudged the situation."
        "Ayesha and Kylie are totally silent as they stare at me."
        "Then I see them slowly exchange a meaningful glance."
        "And I can feel myself swallowing in anticipation."
        kylie.say "OF COURSE WE WILL!"
        show kylie crazyhappy
        kylie.say "Oh, [hero.name] - this is just perfect!"
        ayesha.say "I..."
        ayesha.say "I can't marry you both."
        show ayesha sad at left5 with move
        ayesha.say "That's just not how I want my life to go!"
        "I'm feeling a bizarre mix of emotions as all of this takes place."
        "On the one hand I'm delighted that kylie said yes."
        "But on the other I don't know what to make of Ayesha's answer."
        show kylie surprised at right5 with move
        kylie.say "Wait a minute..."
        show kylie angry
        kylie.say "You're saying you don't want to marry ME?!?"
        ayesha.say "No, I don't."
        ayesha.say "I could settle down with [hero.name]."
        ayesha.say "But you don't fit into that picture, Kylie."
        mike.say "Ayesha..."
        mike.say "Don't be like this - we can work it out!"
        "Kylie clings to me as I say all of this."
        show kylie crazyhappy
        "Like she's letting Ayesha know we come as a package."
        "But it doesn't seem to have the desired effect."
        ayesha.say "It was fun fooling around with this crazy bitch, [hero.name]."
        ayesha.say "But I'm not getting hitched to her - no way!"
        hide ayesha with moveoutleft
        "That said, Ayesha storms off before either of us can say another word."
        $ kylie.set_fiance()
        $ ayesha.love -= 25
        $ ayesha.sub -= 25
    elif ayesha.love < 195 and kylie.love < 195:
        "For a moment I just kneel there, staring at the pair of them."
        "Willing Ayesha and Kylie to give me the answer I want."
        "Then I see them slowly exchange a meaningful glance."
        "And I can feel myself swallowing in anticipation."
        ayesha.say "I..."
        ayesha.say "I can't marry you both."
        show ayesha sad at left5 with move
        ayesha.say "That's just not how I want my life to go!"
        show kylie sad at right4, vshake
        kylie.say "NO WAY!"
        show kylie crazysad
        kylie.say "I want to marry you, [hero.name]!"
        show kylie at right5 with move
        kylie.say "Not her!"
        "I feel like I've been dealt a crushing blow."
        "Both of them have turned me down flat."
        "But then I notice them turning their attention upon each other."
        ayesha.say "Wait a minute..."
        show ayesha angry
        ayesha.say "You're saying you don't want to marry ME?!?"
        kylie.say "Well...yeah, Ayesha!"
        show kylie angry
        kylie.say "But didn't you just say the same thing?"
        "I'm getting to my feet as this exchange is taking place."
        "Sheepishly putting away the rejected rings."
        "So all I can do is watch on as they begin to squabble."
        "By the time I manage to open my mouth, it's already too late."
        show kylie at top_mostright
        show ayesha at top_mostleft
        with move
        "Ayesha and Kylie storm off in opposite directions."
        hide kylie with moveoutright
        hide ayesha with moveoutleft
        "Leaving me standing alone and feeling more than a little confused."
        $ ayesha.love -= 25
        $ ayesha.sub -= 25
        $ kylie.love -= 25
        $ kylie.sub -= 25
    return

label ayesha_kylie_male_ending:

    if renpy.has_label("taming_harem_achievement_3") and not game.flags.cheat:
        call taming_harem_achievement_3 from _call_taming_harem_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "I'm one of those guys that never really sat down and planned out his life."
    "I know a lot of girls have their entire life planned out down to the smallest detail."
    "And often their wedding day is the thing they've spent the most time thinking about."
    "But in the rush and confusion of the past few months, I never thought to ask Ayesha and Kylie."
    "You know, ask them if this was anything like what they imagined their wedding days would be like?"
    "Because even though I never imagined mine, I know that I couldn't have dreamed this up in a thousand years!"
    "Right now I'm standing at the altar, waiting for Ayesha and Kylie to come walking down the aisle."
    "A quick look over my shoulder shows the chapel filled with my own friends and families."
    "I can pick out some of Kylie's guests too, like Alexis, her sister and my ex."
    "And I'm pretty sure all the people that look like bodybuilders are here for Ayesha."
    "Some of them being from the gym and others probably her fellow pro-wrestlers."
    "All in all it makes for a colourful crowd."
    "Which is kind of appropriate, as the three of us do too!"
    "But all of my mental musings come to an end a few moments later."
    "Because that's when the sound of music fills the chapel."
    "As one, everyone in the place looks over their shoulders."
    "And we're treated to the sight of Ayesha and Kylie sweeping into view."
    "Neither of them would let me see their dresses before the big day."
    "Which means that I'm hit twice as hard by the sight of them as they come down the aisle."
    "My eyes shift from one to the other, as I can't hope to settle on either for too long."
    show ayesha wedding happy at left5 with dissolve
    "Ayesha strides confidently towards the altar, head held high."
    "For all the world she looks like nothing could ever shake her."
    "But I can see just how tightly she's gripping her bouquet."
    "God, I love that girl!"
    if ayesha.is_visibly_pregnant:
        "And I couldn't be prouder to see the cut of her dress."
        "Which has been tastefully made to accommodate her pregnant belly."
    show kylie wedding happy at right5 with dissolve
    "Kylie might not be as statuesque as Ayesha, but she still keeps up the pace."
    "And she makes up for what she lacks in height thanks to her sheer audacity."
    "Kylie's figure and smouldering looks can't be hidden my a wedding dress."
    "And she makes me hard just looking at her!"
    if kylie.is_visibly_pregnant:
        "Which would help to explain how she ended up pregnant too!"
        "And that only serves to add to the glow that she has today."
    kylie.say "Hey, [hero.name]!"
    show kylie normal
    kylie.say "Can you believe we're actually doing this?"
    ayesha.say "Keep it down, Kylie!"
    show ayesha normal
    ayesha.say "We need to stick to the plan."
    ayesha.say "Do things how we did them in the rehearsal!"
    mike.say "Ayesha's right, Kylie."
    mike.say "We can talk all we want later!"
    "Priest" "Ahem..."
    "Somehow the sound of the priest's cough snaps us out of it."
    "Even Kylie seems to be jumping to attention!"
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join together these three people..."
    "Priest" "In the bonds of holy matrimony..."
    "You know what comes next, even when there are three people involved."
    "The priest goes through the motions, saying this and that."
    "But nothing interesting happens."
    "Not until it's time for us to exchange vows."
    "Priest" "Do you, Ayesha..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    show ayesha happy
    ayesha.say "Yes, I do."
    "Priest" "And do you, Kylie..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    show kylie smile
    kylie.say "Yes, yes I do!"
    "Priest" "And finally, do you, [hero.name]..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    mike.say "I do."
    "The priest nods."
    "And he looks relieved to have gotten through all of our vows too!"
    "Priest" "I now call upon those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "That these three may not be wed..."
    "Priest" "Speak now, or forever hold your peace!"
    "Ayesha, Kylie and I share a few smirks and chuckles."
    "And part of me wonders if one of Ayesha's wrestling friends might object."
    "Because they're all about making fake drama for the sake of entertainment."
    "But I do feel a sense of relief when the moment passes without incident."
    "Priest" "Very good."
    "Priest" "It is therefore my pleasure to pronounce you married."
    "Priest" "You may show your emotions in a way that you judge fitting."
    show ayesha at center, zoomAt(2, (360, 1380))
    show kylie at center, zoomAt(2, (920, 1380))
    with hpunch
    "Ayesha and Kylie almost pounce on me."
    "Four arms wrap around my body and pull me close."
    "And the kisses that follow are passionate and unrestrained."
    "We did it."
    "We actually did it."
    "We're married!"

    if ayesha.flags.manager:
        scene taming harem wrestling ending
    else:
        scene taming harem beach ending
    with fade
    kylie.say "I guess you'll want me to do most of the talking?"
    kylie.say "Right, Ayesha?"
    ayesha.say "Wait...what?"
    ayesha.say "No way, Kylie!"
    ayesha.say "What makes you think that?!?"
    kylie.say "Oh come on, Ayesha!"
    kylie.say "You're only loud and funny when you're in the wrestling ring!"
    kylie.say "Outside of it, I'm the one that everyone thinks is fun!"
    ayesha.say "That is not true, Kylie!"
    ayesha.say "I'm just not as big of a show-off as you."
    ayesha.say "And [hero.name] likes that about me too!"
    kylie.say "Okay, okay..."
    kylie.say "You're right, Ayesha."
    kylie.say "[hero.name] likes you for who you really are."
    kylie.say "And he's cool with the real me too."
    ayesha.say "Which is a miracle in and of itself!"
    kylie.say "HEY!"
    ayesha.say "Oh come on, Kylie - you know I'm right!"
    kylie.say "Yeah, yeah..."
    kylie.say "I definitely know that this couldn't work without him."
    kylie.say "He's kind of like the glue that holds it all together."
    ayesha.say "He sure is the most understanding guy I know."
    ayesha.say "The most tolerant too."
    if ayesha.flags.manager:
        kylie.say "Yeah, Ayesha."
        kylie.say "Like the way he was cool with you keeping on wrestling."
        ayesha.say "Just for the record - that was my decision, not his!"
        ayesha.say "But yeah, some guys would have been against that."
        kylie.say "I've got to say, I like coming to your matches."
        kylie.say "Sitting in the front row with, [hero.name]."
        kylie.say "Wearing your T-shirts and cheering you on!"
        ayesha.say "Ah...stop it, Kylie!"
        ayesha.say "You know I get embarrassed about all that!"
    else:
        kylie.say "Yeah, Ayesha."
        kylie.say "Like the way he was cool with you quitting the wrestling."
        ayesha.say "Just for the record - that was my decision, not his!"
        ayesha.say "But yeah, some guys would have been against that."
        ayesha.say "It's like a modern man can't cope with his wife wanting to stay home!"
        kylie.say "Yeah, Ayesha!"
        kylie.say "What's up with that?"
    kylie.say "You know, what..."
    kylie.say "I always knew that he was the perfect man."
    kylie.say "The perfect husband material too."
    kylie.say "Ever since that first time I met him as a kid!"
    ayesha.say "Yeah..."
    ayesha.say "You remember when I told you that was weird?"
    ayesha.say "And I asked you not to mention it?"
    kylie.say "Erm...yeah."
    ayesha.say "Well it's still weird."
    ayesha.say "And I still don't want you to mention it!"
    kylie.say "Ah, lighten up, Ayesha!"
    if (ayesha.is_visibly_pregnant or ayesha.flags.mikeBabies >= 1) and (kylie.is_visibly_pregnant or kylie.flags.mikeBabies >= 1):
        kylie.say "Because we're all family now!"
        if ayesha.flags.manager:
            kylie.say "Especially since little Alexis came along."
        else:
            kylie.say "Especially since little Hector came along."
        ayesha.say "I know that I couldn't have predicted being a mom!"
        ayesha.say "And I never thought my kid would be as perfect as Bruce is."
        kylie.say "They're both so great!"
        ayesha.say "And we make a pretty cute family."
    elif ayesha.is_visibly_pregnant or ayesha.flags.mikeBabies >= 1:
        kylie.say "Because we're all family now!"
        ayesha.say "I know that I couldn't have predicted being a mom!"
        ayesha.say "And I never thought my kid would be as perfect as Bruce is."
        kylie.say "You can say that again, Ayesha."
        kylie.say "He's so great!"
    elif kylie.is_visibly_pregnant or kylie.flags.mikeBabies >= 1:
        kylie.say "Because we're all family now!"
        if ayesha.flags.manager:
            kylie.say "Especially since little Alexis came along."
            ayesha.say "You do have a point, Kylie."
            ayesha.say "She's a total darling!"
        else:
            kylie.say "Especially since little Hector came along."
            ayesha.say "You do have a point, Kylie."
            ayesha.say "He's a total cutie!"
    else:
        kylie.say "Because we're all family now!"
        kylie.say "And our family may be getting bigger soon."
        ayesha.say "You know what, Kylie..."
        ayesha.say "That's not nearly as scary as I thought it'd be!"
    kylie.say "I don't think any of us could have predicted how things would turn out."
    kylie.say "But maybe that's why it feels like this works?"
    ayesha.say "You might be onto something there, Kylie."
    ayesha.say "I know I'm excited to see where we go from here."
    kylie.say "Me too, Ayesha."
    kylie.say "It's gonna be a wild ride for sure!"
    scene bg black with dissolve
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
