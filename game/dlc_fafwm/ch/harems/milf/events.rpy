init python:
    
    CallEvent(**{
        "name": "milf_harem_event_01",
        "label": "milf_harem_event_01",
        "conditions": [
            IsDone("claire_event_06", "kiara_event_06"),
            IsTimeOfDay("evening"),
            HeroTarget(
                IsGender("male"),
                HasRoomTag("home"),
                Not(OnDate()),
                ),
            PersonTarget("claire",
                IsActive(),
                ),
            PersonTarget("kiara",
                Not(IsHidden()),
                ),
            "Person.showdown(claire, kiara)",
            ],
        "music": "music/roa_music/focus.ogg",
        "priority": 500,
        "do_once": True,
        })
    
    Event(**{
        "name": "milf_harem_event_02",
        "label": "milf_harem_event_02",
        "conditions": [
            IsDone("cherie_event_06", "claire_event_06"),
            IsHour(11, 14),
            HeroTarget(
                IsGender("male"),
                HasRoomTag("mcoffice"),
                Not(OnDate()),
                IsActivity("work", "workhard", "work_personal", "workhard_personal"),
                ),
            PersonTarget("claire",
                Not(IsHidden()),
                ),
            PersonTarget("cherie",

                Not(IsHidden()),
                ),
            "Person.showdown(cherie, claire)",
            ],
        "music": "music/roa_music/focus.ogg",
        "priority": 500,
        "do_once": True,
        })
    
    Event(**{
        "name": "milf_harem_event_03",
        "label": "milf_harem_event_03",
        "conditions": [
            IsDone("milf_harem_event_01", "milf_harem_event_02"),
            HeroTarget(
                IsGender("male"),
                HasRoomTag("home"),
                Not(OnDate()),
                ),
            PersonTarget("claire",
                Not(IsHidden()),
                IsFlag("clairedelay", False),
                ),
            PersonTarget("cherie",
                Not(IsHidden()),
                IsFlag("cheriedelay", False),
                ),
            PersonTarget("kiara",
                Not(IsHidden()),
                IsFlag("kiaradelay", False),
                ),
            "Person.showdown(cherie, claire, kiara)",
            ],
        "music": "music/roa_music/focus.ogg",
        "priority": 500,
        "do_once": True,
        })
    
    Event(**{
        "name": "milf_harem_event_04",
        "label": "milf_harem_event_04",
        "conditions": [
            IsDone("milf_harem_event_03"),
            TogetherInHarem('milf', 'cherie', 'claire', 'kiara'),
            HeroTarget(
                IsGender("male"),
                HasRoomTag("club"),
                Not(OnDate()),
                ),
            PersonTarget("claire",
                Not(IsHidden()),
                IsFlag("clairedelay", False),
                ),
            PersonTarget("cherie",
                Not(IsHidden()),
                IsFlag("cheriedelay", False),
                ),
            PersonTarget("kiara",
                Not(IsHidden()),
                IsFlag("kiaradelay", False),
                ),
            ],
        "music": "music/roa_music/focus.ogg",
        "priority": 500,
        "do_once": True,
        })
    
    Event(**{
        "name": "milf_harem_event_05",
        "label": "milf_harem_event_05",
        "conditions": [
            IsDone("milf_harem_event_04"),
            TogetherInHarem('milf', 'cherie', 'claire', 'kiara'),
            IsHour(10, 16),
            HeroTarget(
                IsGender("male"),
                HasRoomTag("beach"),
                Not(OnDate()),
                ),
            PersonTarget("claire",
                Not(IsHidden()),
                IsFlag("clairedelay", False),
                ),
            PersonTarget("cherie",
                Not(IsHidden()),
                IsFlag("cheriedelay", False),
                ),
            PersonTarget("kiara",
                Not(IsHidden()),
                IsFlag("kiaradelay", False),
                ),
            ],
        "music": "music/roa_music/focus.ogg",
        "priority": 500,
        "do_once": True,
        })

label milf_harem_event_01:
    "I'm still feeling pretty bad about the way that Hector's been getting on Claire's case recently."
    "And I know that she's not really getting much relief when he's out of the house at work either."
    "Because all that does is leave Claire on her own, wrestling with all of the issues in her life."
    "So I decide that it's time I did something about it, and, with that in mind, I call her up."
    show screen expression "smartphone_calling" pass ("Claire")
    show mikemc p speak casual smile at center, zoomAt (2.0, (840, 1360))
    with fade
    "There's hardly enough time for the phone to ring before it's answered and I hear Claire's voice."
    claire.say "[hero.name]…"
    claire.say "It's so nice to hear from you!"
    show mikemc happy
    mike.say "Hey, Claire - the feeling's mutual."
    mike.say "Look, are you doing anything right now?"
    mike.say "Because if not, I wondered if you wanted to...maybe, come over here?"
    show mikemc smile
    "I'm fully expecting to have to convince Claire that it's a good idea."
    "Maybe even to have to promise to come over and collect her myself."
    "So her response comes as a genuine surprise to me."
    claire.say "Of course I do!"
    claire.say "You just sit tight, [hero.name]…"
    claire.say "I'll be there in two shakes of a lamb's tail!"
    show mikemc happy
    mike.say "Oh..."
    mike.say "Okay, Claire..."
    show mikemc talkative
    mike.say "When should I expect to..."
    mike.say "Huh?"
    hide screen smartphone_calling
    hide mikemc
    with fade
    "I find myself staring at my phone, as Claire just ends the call without warning."
    "So I guess that means she's already on her way over here."
    play sound door_bell
    "And it's not long before I hear the sound of the doorbell ringing too."
    "Which sees me hurrying into the hallway and hastily opening the door."
    "There, standing on the porch and looking a little flustered, is Claire."
    scene bg house
    show claire happy casual
    with dissolve
    show claire talkative
    claire.say "Phew..."
    claire.say "Here I am!"
    claire.say "I came as fast as I could."
    show claire pleased
    "I nod my head as I step aside and gesture for Claire to step inside."
    scene bg livingroom
    show claire pleased casual at center, zoomAt(1.6, (640, 1070))
    with dissolve
    "Eager to get her into the house and out of sight of anyone outside."
    "Not that I'm embarrassed to be seen in her company, you understand?"
    "More that I'm getting paranoid Hector might be spying on the two of us."
    mike.say "Thanks for coming over, Claire."
    mike.say "I know that it's short notice..."
    mike.say "But I don't like the thought of you stuck at home on your own."
    show claire happy
    "Claire pleaseds and waves a hand vaguely in the air, dismissing my concerns."
    show claire talkative
    claire.say "Oh, don't be silly!"
    claire.say "It's my pleasure, really."
    claire.say "And anyway, this place could use a woman's touch."
    show claire normal
    "I'd kind of been expecting to show Claire into the sitting-room."
    show claire c at center, traveling(1, 3, (1040, 720))
    "But I notice that she's headed straight for the kitchen."
    "And none of my efforts to redirect her seem to be having an effect."
    mike.say "Erm..."
    mike.say "I live with a couple of women, remember?"
    show claire startle
    claire.say "No, no, no..."
    claire.say "You live with a couple of young girls."
    claire.say "I'm talking about a real woman - there's a lot of difference!"
    hide claire with easeoutright
    scene bg kitchen
    show claire happy c casual at center, zoomAt(1, (240, 720))
    with pushleft
    "Claire bustles into the kitchen and plucks an apron off the back of the door."
    show claire normal at center, traveling(1, 3, (1040, 720))
    "And once she has it on, she proceeds to open the nearest cupboard and root around inside."
    mike.say "What are you doing going through the cupboards?"
    mike.say "I thought we could watch some TV, maybe even a movie?"
    mike.say "I didn't expect you to start performing domestic chores!"
    show claire happy
    "Claire pulls her head out of the cupboard long enough to shake her head at me."
    "And then she proceeds to dive straight into the next one."
    show claire talkative
    claire.say "You're being silly again, [hero.name]!"
    claire.say "It would be my pleasure to cook for you."
    show claire startle
    claire.say "But your housemates aren't keeping up with the shopping."
    claire.say "Why, I bet you live on takeaways and leftovers!"
    show claire happy
    mike.say "Well, it's not really Bree and Sasha's job to do all of the shopping..."
    show claire startle
    claire.say "Never mind, I'm an expert at making do with what's at hand."
    claire.say "So I'll soon knock you up something delicious."
    show claire normal
    "There really doesn't seem to be any way of me stopping Claire."
    "As she's charging around the kitchen like a domestic tornado."
    "And so I resolve to just stand back and leave her to it."
    "After all, the idea of cooking for me seems to make her happy."
    "Plus if I get a meal out of it, that's a double win."
    "And I can soon see that Claire wasn't exaggerating her prowess in the kitchen either."
    "Because it doesn't take her long to root out the ingredients she needs and toss it all together."
    "The collection of mismatched stuff bubbling away on the stove and starting to smell damn good too."
    "So good that I can't keep myself from leaning in closer and inhaling deeply, much to Claire's delight."
    show claire talkative
    claire.say "You see, [hero.name]?"
    claire.say "I'm a magician in the kitchen!"
    show claire happy
    mike.say "You certainly are, Claire..."
    play sound door_bell
    show claire stuned
    "I'm about to say more, but I get interrupted a second later by the sound of the doorbell."
    mike.say "Huh..."
    mike.say "I wonder who that could be?"
    show claire surprised
    claire.say "You're not expecting anyone, are you?"
    show claire normal
    mike.say "Nope..."
    mike.say "Give me a second to see what they want, okay?"
    show claire happy at startle(0.2, 5)
    "Claire gives me a nod and a smile as she goes back to her cooking."
    "Which leaves me free to answer the door, hoping to get rid of whoever's there."
    "Because now I'm keener than ever to get my hands on a portion of Claire's cooking."
    play sound door_open
    scene bg house at center, zoomAt(1.2, (640, 770))
    show kiara smile casual at center, zoomAt(1, (640, 720))
    with dissolve
    "But when I open the door, I almost freak out at the sight that awaits me."
    show kiara talkative
    kiara.say "Good evening, [hero.name]."
    kiara.say "Apologies for coming over unannounced."
    show kiara flirt at center, traveling(1.6, 1, (640, 1070))
    kiara.say "But I wanted to...check in on my newest investment!"
    show kiara normal
    "Okay, normally I'd be bowled over by the fact that Kiara's on my doorstep."
    "And more than excited at the fact that she seems to be dropping innuendos too."
    "But not while I still have Claire beavering away in the kitchen like a domestic goddess!"
    mike.say "Oh..."
    mike.say "Ah..."
    mike.say "I'm fine, Kiara - as you can see for yourself."
    "I wave a hand up and down in front of myself to make my point."
    show kiara mischievous at startle(0.1, -5)
    "But all that seems to do is make Kiara more suspicious."
    show kiara at center, traveling(2, 1, (640, 1300))
    "As now she's staring at me and narrowing her eyes."
    show kiara irritated
    kiara.say "Tell me, [hero.name]…"
    kiara.say "Why are you being so evasive?"
    kiara.say "And why haven't you invited me in yet?"
    show kiara serious with dissolve
    "As if to make her point, Kiara inhales so that her chest expands."
    show bg house at center, traveling(1.2, 0.7, (640, 720))
    show kiara at center, traveling(2, 0.7, (640, 1170))
    "And I'm treated to the rather impressive sight of her breasts rising and falling too."
    show bg house at center, traveling(1.2, 0.7, (640, 770))
    show kiara at center, traveling(2, 0.7, (640, 1300))
    "But in doing so, Kiara seems to have breathed in through her nose."
    "Because now she's sniffing the air again, and with renewed interest."
    show kiara delicious at startle(0.1, -5)
    kiara.say "Mmm…"
    show kiara stuned at hshake
    pause 1
    show kiara surprised with dissolve
    kiara.say "What is that divine aroma?"
    kiara.say "Are you cooking supper?"
    show kiara stuned
    mike.say "Y...yeah, Kiara..."
    mike.say "Just knocking up a little something for myself, you know?"
    mike.say "Nothing special, just a bunch of leftovers, that's all."
    "Kiara nods as she takes a step into the hallway, despite my efforts to block her path."
    show kiara talkative
    kiara.say "That reminds me of the cooking from the old country!"
    kiara.say "And I haven't yet eaten tonight..."
    kiara.say "Surely you can spare a little for me?"
    show kiara normal
    mike.say "Honestly, it's not up to your high standards!"
    scene bg livingroom
    show kiara casual at center, zoomAt(1.2, (640, 820))
    with dissolve
    show kiara at center, traveling(1, 3, (1040, 720))
    "By now Kiara's made her way into the house and is walking into the kitchen."
    hide kiara with easeoutright
    "And there's nothing I can do to keep her from sweeping straight in there."
    scene bg kitchen
    show bg kitchen at center, zoomAt(1, (640, 720))
    show claire c normal casual at center, zoomAt(1, (960, 720))
    show kiara stuned casual at center, zoomAt(1, (320, 720))
    with pushleft
    "Arriving on her heels as Claire looks up from what she's doing."
    show claire b talkative at startle(0.1, 5)
    claire.say "Oh..."
    claire.say "Hello there - are you one of [hero.name]'s housemates?"
    show kiara annoyed at hshake
    pause 0.7
    show kiara talkative with dissolve
    kiara.say "I most certainly am not!"
    kiara.say "Who are you?"
    show kiara whining
    kiara.say "The house-keeper?"
    show kiara mischievous
    pause 0.3
    show claire angry
    claire.say "Of course I'm not the house-keeper!"
    claire.say "Tell her who I am, [hero.name]!"
    show kiara whining
    kiara.say "Yes, [hero.name] - tell me who this woman is."
    show kiara annoyed
    mike.say "Erm..."
    mike.say "This is Claire..."
    mike.say "She's...my old friend Adam's mom."
    show kiara smile
    show claire angry
    with dissolve
    "This answer seems to please Kiara, who narrows her eyes and smiles knowingly."
    "But it certainly has the opposite effect on Claire, who frowns and crosses her arms over her chest."
    show claire furious at hshake
    claire.say "Am I indeed?!?"
    claire.say "Well, who's this then?"
    show claire disappointed
    "Claire nods towards Kiara."
    mike.say "Okay..."
    mike.say "This is Kiara..."
    mike.say "Who is...my housemate Bree's boss."
    show kiara stuned
    show claire happy
    with dissolve
    "In an instant the roles are reversed, with Kiara's smile turning into a scowl."
    "And Claire sensing that her potential adversary just got humbled in turn."
    "But there's no way those half-arsed explanations are going to cut it."
    show claire upset
    show kiara annoyed
    "Because both of them are now staring at me, waiting for me to say more."
    if kiara.sub <= -25:
        "I'm kind of flinching on the inside, expecting an explosion any moment."
        "So it comes as a genuine surprise when Kiara chuckles and produces a bottle of wine."
        show kiara amused
        kiara.say "I picked this out for the two of us to enjoy, [hero.name]…"
        play sound wine_stopper
        kiara.say "But there's enough for three - wouldn't you agree?"
        show kiara at center, traveling(1, 0.5, (540, 720))
        "I find myself shrugging and blustering as Kiara grabs three wine glasses."
        play sound wine_serving
        mike.say "I..."
        mike.say "I guess..."
        mike.say "I mean...if you say so?"
        "Kiara seems to have managed to mollify me pretty easily, as usual."
        show kiara smile
        "But Claire's totally new to the other woman's charms."
        "And so she's not so easily convinced."
        show claire angry
        claire.say "Excuse me!"
        claire.say "Isn't anyone going to ask me what I think about all of this?"
        "Kiara's lips twist into a languid smile as she hands one of the glasses to Claire."
        show kiara warning at startle(0.1, -5)
        kiara.say "What's to tell, Claire?"
        kiara.say "The whole of your story is written on your face."
        show claire stuned
        kiara.say "You're a frustrated wife and mother, married to a chauvinist pig."
        kiara.say "And you're having an affair with a younger man, because he sees you for who you really are."
        kiara.say "Not a wife, not a mother, but a woman with genuine needs."
        show kiara mischievous
        show claire surprised
        claire.say "I..."
        claire.say "Well..."
        show claire at center, traveling(1, 1, (740, 720))
        claire.say "I suppose you could put it like that."
        play sound wine_serving
        show claire pleased
        show bg kitchen at center, traveling(1.4, 2, (640, 820))
        show kiara at center, traveling(1.8, 2, (440, 1120))
        show claire at center, traveling(1.8, 2, (840, 1120))
        pause 2
        play sfx1 wine_cheers
        pause 0.1
        play sfx2 glass_wine
        "Claire accepts the glass and instantly drains off about half of its contents."
        show claire blush with dissolve
        "I can already see the way that her cheeks are flushing as she looks at Kiara."
        "And I'm sure that not all of it is on account of the effects of the alcohol."
        show kiara flirt
        kiara.say "So what then, is the problem with my being involved too?"
        kiara.say "You've already crossed the line, Claire, already started your affair."
        kiara.say "Why not go one step further and let me in on it too?"
        show kiara normal
        "I can only stand there, taking the occasional sip of wine."
        "As I watch Kiara talking Claire into what I guess would be a threesome!"
        $ claire.sub += 2
        $ kiara.sub -= 2
        if claire.lesbian < 9:
            $ claire.lesbian += 2
    menu:
        "We're just three lonely people":
            "And if this thing is going to blow up in my face, then I'm going to be honest."
            "I'm going to put all of my cards on the table in front of Claire and Kiara."
            mike.say "Alight, ladies..."
            mike.say "It's more like this..."
            "I point to Claire."
            mike.say "Claire's a beautiful woman that's trapped in a loveless marriage to a pig."
            mike.say "I started spending time with her out of genuine friendship and admiration."
            mike.say "And before I knew it, there was a bond between us that gives me goosebumps."
            show claire shy blush with dissolve
            "I look at Claire, seeing that there's genuine emotion in her eye."
            "My confession of how I feel about her seeming to touch her heart."
            show kiara blank
            "Then I risk a glance at Kiara, expecting to see her glaring at me."
            "But instead I see a look of interest in her eyes."
            "Okay, in for a penny, in for a pound."
            mike.say "Kiara is a sophisticated business woman married to her work."
            mike.say "I met her at her café and started coming back just to be around her."
            mike.say "Thrilled to be able to add warmth and affection to her life."
            "Once I'm done talking about Kiara, I look her in the eye again."
            show kiara smile
            "Seeing that she's got the same expression on her face that Claire did just now."
            show claire pleased
            "And sure enough, she's now the one looking over at Kiara in genuine interest."
            "Now I figure that I have to do some explaining for myself too."
            mike.say "And as for me..."
            mike.say "I guess I'm lonely too."
            mike.say "Lonely enough to think that I needed two women's love, rather than just the one."
            $ claire.love += 4
            $ kiara.love += 4
        "You're both mine!" if kiara.sub >= 25 or claire.sub >= 25:
            "Wait a minute - why am I struggling to explain myself and coming out with excuses?"
            "Aren't I the one that's been successfully romancing the pair of them until now?"
            "Hell, even if this is the end of all that, I'm not going to act like I'm ashamed of it!"
            mike.say "This is pretty much what it looks like, girls..."
            mike.say "I've been seeing the both of you at the same time."
            mike.say "And if you hadn't bumped into each other tonight..."
            mike.say "Well, I'd still be dating two seriously hot ladies and doing a damn good job of it too!"
            "There it is, the best swaggering, arrogant prick speech I'll probably ever give."
            "And at first I can see that Claire and Kiara are both glaring at me."
            show claire angry
            show kiara blank
            "But the former is the first to break, a little smile creeping onto her face."
            show claire pleased
            claire.say "Oh, [hero.name]…"
            claire.say "You're the devil himself!"
            "For a moment I think that Kiara's going to object to what Claire's saying."
            "But then she shakes her head and lets out a sigh."
            show kiara normal
            kiara.say "Ah..."
            kiara.say "The heart will have what it desires, I suppose!"
            show kiara smile
            mike.say "So there you have it, ladies..."
            mike.say "As far as I'm concerned, you're both mine."
            mike.say "And I want it to stay that way."
            $ claire.sub += 2
            $ kiara.sub += 2
    mike.say "Okay..."
    mike.say "There you have it, guys."
    mike.say "All the cards are out on the table."
    mike.say "So what happens next?"
    if all([person.love >= 135 and person.lesbian >= 7 for person in [claire, kiara]]) and claire.sub >= 25 and kiara.sub.abs >= 25:
        play sound wine_serving
        queue sound wine_serving
        "I watch in silence as Kiara refills everyone's glasses."
        show kiara smile
        "And at the same time, Claire begins to plate up the food."
        show claire happy
        "It feels totally uncanny, the way they're now working together."
        mike.say "So..."
        mike.say "Does this mean that..."
        "As one, Claire and Kiara turn to face me."
        show claire pleased
        show kiara smile
        "And suddenly I feel like I'm being put on the spot."
        mike.say "I mean..."
        mike.say "Nobody's storming out or throwing stuff..."
        mike.say "So does that mean we're..."
        "Without saying a word, Kiara reaches out and takes hold of my hand."
        "Then Claire does the same, taking hold of the other one."
        "And I note that they're also holding hands with each other at the same time."
        show claire happy
        claire.say "I'm not sure what it means yet, [hero.name]…"
        claire.say "But I think we're going to have a lot of fun finding out!"
        show kiara smile
        kiara.say "Exactly so, Claire - we eat together, we drink together..."
        kiara.say "And we do many more things together too!"
        "I'm nodding as the girls say all of this, trying to appear calm."
        "But the truth is that my heart's racing at the mere thought of it."
        "Claire, Kiara and me - all coming together, in every sense of the word!"
        hide claire
        hide kiara
        with dissolve
        $ Harem.join_by_name("milf", claire, kiara)
    elif claire.love >= kiara.love and claire.love >= 125:
        play sound drinking volume 0.5
        "Kiara makes a point of draining the contents of her glass."
        play sound glass_break
        show kiara disgusted at hshake
        "And then she slams it down as she gathers up her things."
        show kiara angry
        kiara.say "I am not in the habit of sharing what is mine."
        kiara.say "When I want something, I desire to possess it."
        kiara.say "I need for it to be mine completely."
        kiara.say "And my lovers are no exception to that rule!"
        show claire surprised
        mike.say "Kiara..."
        mike.say "Wait..."
        hide kiara with easeoutleft
        "My pleas fall on deaf ears, as Kiara hurries out of the kitchen."
        play sound door_slam
        pause 0.3
        with hpunch
        "And a moment later I hear the sound of the door being slammed behind her."
        show claire happy at center with move
        claire.say "Phew!"
        claire.say "She was SO dramatic, [hero.name]…"
        show claire pleased
        claire.say "You don't need that kind of stress in your life."
        claire.say "No, what you need is someone that's sensible and reliable."
        "I'm still sore at the way Kiara stormed out on me just now."
        "But there is a lot of sense in what Claire's saying."
        "Better to be with one beautiful woman than alone."
        "So I begin to plate up the food she cooked for us."
        "All the time resigning myself to being without Kiara."
        hide claire with dissolve
        $ kiara.set_gone_forever()
    elif kiara.love >= claire.love and kiara.love >= 125:
        play sound drinking volume 0.5
        "Claire makes a point of draining the contents of her glass."
        play sound glass_break
        show claire angry at hshake
        "And then she slams it down as she gathers up her things."
        show claire angry
        claire.say "Your explanations sound all well and good, [hero.name]…"
        claire.say "But I don't need to be getting involved with another woman."
        claire.say "You were all that I needed to be happy."
        claire.say "I'm just sorry that I wasn't enough for you!"
        show kiara mischievous
        mike.say "Claire..."
        mike.say "Wait..."
        hide claire with easeoutleft
        "My pleas fall on deaf ears, as Claire hurries out of the kitchen."
        play sound door_slam
        pause 0.3
        with hpunch
        "And a moment later I hear the sound of the door being slammed behind her."
        show kiara normal at center with move
        kiara.say "Ah, well..."
        kiara.say "I am not planning on going anywhere."
        show kiara smile
        kiara.say "So how about we enjoy the wine and the food together?"
        kiara.say "Because it would be a shame to waste what we have, would it not?"
        "I'm still sore at the way Claire stormed out on me just now."
        "But there is a lot of sense in what Kiara's saying."
        "Better to be with one beautiful woman than alone."
        "So I begin to plate up the food Claire cooked for us."
        "All the time resigning myself to being with Kiara."
        hide kiara with dissolve
        $ claire.set_gone_forever()
    else:
        play sound drinking volume 0.5
        pause 0.2
        play sound drinking volume 0.5
        "Claire and Kiara both drain their glasses in one gulp."
        play sound glass_break
        pause 0.2
        play sound glass_break
        "And then slam them down at almost the exact same moment."
        show claire angry
        claire.say "Your explanations sound all well and good, [hero.name]…"
        claire.say "But I don't need to be getting involved with another woman."
        claire.say "You were all that I needed to be happy."
        claire.say "I'm just sorry that I wasn't enough for you!"
        show kiara angry
        kiara.say "I am not in the habit of sharing what is mine."
        kiara.say "When I want something, I desire to possess it."
        kiara.say "I need for it to be mine completely."
        kiara.say "And my lovers are no exception to that rule!"
        mike.say "Claire..."
        mike.say "Kiara..."
        mike.say "Wait..."
        "My pleas fall on deaf ears, as Claire and Kiara hurry out of the kitchen."
        hide claire
        hide kiara
        with easeoutleft
        pause 2
        play sound door_slam
        "And a moment later I hear the sound of the door being slammed behind them."
        "Feeling utterly dejected, I pour myself another glass of wine."
        "Then I plate myself up an extra large portion of the food Claire made for us."
        "Thinking that I can at least comfort myself that way."
        "Though it feels like the emotional pain from this one is going to last a lot longer."
        $ claire.set_gone_forever()
        $ kiara.set_gone_forever()
    call stop_all_sfx from _call_stop_all_sfx_63
    scene bg black with fade
    return
label milf_harem_event_02:
    cherie.say "[hero.name]…"
    cherie.say "Would you mind stepping into my office for a moment?"
    show cherie a work at center, zoomAt(1.25, (440, 900)) with fade
    "I look up from my desk at the sound of Cherie's voice, my current task instantly forgotten."
    "And there she is, looking as desirable as ever in her perfectly tailored executive suit."
    "Standing in the doorway of my office and gesturing for me to get up and follow her."
    mike.say "Sure thing, Cherie..."
    mike.say "I'll be right there!"
    show cherie a work at center, zoomAt(1.25, (240, 900)) with ease
    "Cherie nods and turns to leave, which is when I realise that I have no idea what she wants."
    mike.say "Erm..."
    mike.say "Cherie?"
    mike.say "What's this about?"
    "Cherie pauses long enough to look back over her shoulder at me."
    show cherie a happy
    cherie.say "Oh, nothing serious, mon ami…"
    show cherie a talkative
    cherie.say "Just a little...strategy meeting!"
    show cherie a wink
    "Cherie's slight pause there is more than enough to set my mind racing."
    pause 0.5
    hide cherie with easeoutleft
    "And the fact that she adds a little wink before walking off seals the deal, at least in my mind."
    "She's got to be giving me hints, right?"
    "You know, like this is a private and very intimate kind of meeting?"
    "Becoming more convinced by the second, I hurry to grab a couple of things from around the office."
    "Just the right amount of files and papers to make it look like I'm off to a very real and serious meeting."
    "All the while hoping that Cherie's pretty much going to pounce on me once the doors to her office are closed!"
    show shiori_stretch_bg zorder 1 at center with fade
    mike.say "Here I am, Cherie..."
    mike.say "What kind of strategy are we talking here?"
    mike.say "I mean, did you have a particular position in mind?"
    mike.say "Because I'm an expert in multiple positions!"
    "I try to make the statement as suggestive as I can."
    show cherie a work annoyed zorder 4 at center, zoomAt(1.25, (440, 900)) with fade
    "But when Cherie turns to face me, I can see she looks totally serious."
    "Dropping an armful of files onto the desk in front of her."
    show cherie a talkative
    cherie.say "Oh, [hero.name]…"
    cherie.say "Your double entendres are so cute!"
    cherie.say "But I am afraid that I am being quite serious this time."
    cherie.say "I really must pick your brains on business matters."
    show cherie a annoyed
    mike.say "Oh..."
    mike.say "Oh, of course..."
    mike.say "I totally get what you're saying."
    "I do the best I can to nod and look professional, hiding my disappointment."
    show cherie a smile at center, traveling(1.5, 1.0, (640, 1040))
    "But it doesn't seem like my efforts have worked, as Cherie smiles and walks over to me."
    "And once she's close enough, I feel her jab me playfully in the ribs with her elbow."
    show cherie a talkative
    cherie.say "But do not worry, mon ami…"
    cherie.say "We will schedule a...comfort break afterwards, no?"
    show cherie a happy
    cherie.say "One where we will compete to see who can make the other the most comfortable!"
    show cherie a normal
    "By now my head is nodding up and down like crazy."
    "And I'm more than determined to earn the reward Cherie's offering me."
    "So I drop my own files onto the desk and we begin the meeting in earnest."
    mike.say "So, Cherie..."
    mike.say "I think the problem is that..."
    play sound door_knock
    "But I've no sooner started talking than there's the sound of a knock at the door."
    show cherie a stuned
    "As one, Cherie and I turn to glance in the direction of the noise."
    show claire casual zorder 3 at center, zoomAt(1.25, (340, 880)) with easeinleft
    "Which means that we're in time to see the door swing open and someone bustle through it."
    show claire talkative
    claire.say "[hero.name]…"
    claire.say "Oh, [hero.name]?"
    claire.say "Where are you, you cheeky little thing?"
    claire.say "I've brought you something nice and tasty!"
    show claire happy
    "I'm more than a little surprised to find myself looking at Claire's smiling face."
    show claire embarrassed
    show cherie a at center, traveling(1.25, 0.3, (840, 880)) with ease
    "And a second later also caught off-guard by Cherie hopping away from me."
    "As I realise that she was in the middle of putting a hand on the curve of my butt!"
    show claire disappointed
    show cherie a talkative
    cherie.say "So, [hero.name]…"
    cherie.say "Aren't you going to introduce me to your visitor?"
    show cherie a normal
    show claire bored
    mike.say "Claire?"
    mike.say "What are you doing here?!?"
    show claire sadsmile blush
    "I can see that Claire's already starting to flush from the embarrassment."
    "And for want of knowing what else to do, she thrusts the basket she's holding towards me."
    show claire talkative
    claire.say "I..."
    claire.say "I just made you a wholesome packed lunch, that's all!"
    claire.say "And the girl at the reception desk told me I could bring it to you."
    show claire whining
    claire.say "I hope I haven't done anything wrong?"
    show claire sadsmile
    "I hastily take the basket from Claire and set it down on the desk."
    "Distracted for a moment by the fact that it really does smell very good indeed."
    mike.say "No, Claire..."
    mike.say "Of course not!"
    mike.say "It's just that Cherie and I were in the middle of a meeting, that's all."
    show claire conceited
    "As soon as I mention Cherie's name, Claire's eyes are on the other woman."
    "And it's pretty obvious that she's being sized up as potential competition."
    "Claire looks Cherie up and down, but it doesn't seem to bother her one bit."
    show claire annoyed
    claire.say "And just who is this Cherie?"
    claire.say "Is she your assistant...or your secretary?"
    show claire normal
    show cherie a smile
    "I can't help showing my shock and concern as Claire assumes Cherie's beneath me."
    mike.say "No, Claire..."
    mike.say "Cherie's my boss...the acting CEO of the whole company!"
    show claire stuned
    "This only seems to serve to make Claire all the more indignant."
    show claire conceited
    "And she keeps on glaring at Cherie like a jealous feline eyeing a rival that's strutted onto its turf."
    "Cherie, on the other hand, seems to find the whole situation increasingly amusing."
    show cherie a talkative
    cherie.say "And who is your little friend here, [hero.name]?"
    cherie.say "So sweet and just as wholesome as her home-cooking..."
    cherie.say "That she comes to bring you whilst you are at work!"
    show cherie a normal
    mike.say "Okay, Cherie..."
    mike.say "Claire's my childhood friend's step-mom."
    mike.say "We've known each other for years."
    show cherie a amused
    "Cherie raises her eyebrows in a show of exaggerated interest."
    show cherie a talkative at center, zoomAt(1.25, (800, 880)) with ease
    cherie.say "The adoptive mother of a friend you had when you were a boy?"
    cherie.say "And yet here she is, being motherly to you now that you are a man!"
    show cherie a amused
    "By now I'm more than used to Cherie's habit of dissecting a situation with cutting humour."
    "Watching her take a person apart one piece at a time until she gets to the core of the matter."
    "But Claire's not had the privilege, and her own nature is pretty much at odds with all of that."
    "She's way more honest and forthright, usually saying what she means and wearing her heart on her sleeve."
    "And right now, she seems to be boiling over with annoyance at Cherie's barbs."
    show claire annoyed at center, traveling(1.25, 1.0, (500, 880))
    claire.say "Now you see here, lady..."
    claire.say "I don't care how much of a fancy, big-shot boss you are around these parts."
    claire.say "[hero.name] has been nothing but kind to me in my time of need."
    claire.say "And I will not have you talking about him like that!"
    show claire pout
    "Claire's leaning towards Cherie as she says all of this."
    "Wagging a finger in her face, just like I remember her doing to Adam when scolding him as a kid."
    "But it's not like Cherie's the kind to be easily intimidated, not after her marriage to Dwayne."
    "And it's not long before she fires back with her own salvo of accusations."
    show cherie a upset at center, zoomAt(1.25, (780, 880)) with ease
    cherie.say "Oh, what a beautiful picture you paint of your relations with him!"
    cherie.say "But I will have you know that [hero.name] is not a little boy for you to mother."
    cherie.say "Oh no, he is a fully-grown man, a rock on which I have rebuilt my life!"
    show cherie a annoyed
    "The two of them are no more than an inch or two apart now."
    "Hands clenched into fists, and faces twisted with suspicion."
    mike.say "Okay..."
    mike.say "Well, thank you for saying such kind things about me, the both of you!"
    mike.say "But maybe this isn't the time or the place to be having this discussion?"
    "All of a sudden the tension between Claire and Cherie seems to break."
    show claire upset
    "As both of them turn their attention to me at the same time."
    "And I almost take a step backwards at the intensity in their eyes."
    show claire angry
    claire.say "Tell her, [hero.name]…"
    claire.say "Tell her that I'm more to you than that!"
    show claire upset
    show cherie a angry
    cherie.say "No, mon ami…"
    cherie.say "Explain to this woman that we have a special relationship."
    show cherie a upset
    "I honestly think about turning on my heel and dashing out of the door."
    "But Claire and Cherie are standing between me and the nearest means of escape."
    "And throwing myself out of the window really seems like too dramatic of an option."
    "So I guess it looks like I'm going to have to come clean."
    if cherie.sub <= -25:
        "I'm kind of flinching on the inside, expecting an explosion any moment."
        show cherie a amused
        "So it comes as a genuine surprise when Cherie sidles towards Claire."
        show cherie a talkative
        cherie.say "So, you desire for [hero.name] to save you, no?"
        cherie.say "You wish for him to be your knight in the shining armour?"
        show cherie a normal
        show claire disappointed
        "Claire's still in the mood to huff and puff."
        "And so she shakes her head at Cherie's questions."
        show claire annoyed
        claire.say "I don't think you know me well enough to make any such judgement!"
        claire.say "I mean...this is the first time that we've met each other."
        show claire disappointed
        show cherie a amused
        "Cherie raises her eyebrows in genuine amusement as Claire fires back at her."
        show cherie a talkative
        cherie.say "There is really nothing to he ashamed of here, Claire..."
        cherie.say "We both know how hard it is to be dominated by a brute of a man."
        cherie.say "And it is only natural that you would want to exchange that for being dominated by a good, loving one instead."
        cherie.say "All I am suggesting is that you go one step further and let more than one person dominate you."
        cherie.say "Wouldn't your life be so much simpler that way?"
        show cherie a normal
        show claire whining
        claire.say "I..."
        claire.say "Well..."
        show claire blush
        claire.say "I suppose you could put it like that."
        show claire conceited
        "Claire's really starting to blush now, her cheeks a bright shade of red."
        "But I can tell that it's from arousal, as well as embarrassment."
        "And I watch in fascination as Cherie, having hooked her prey, proceeds to reel her in."
        show cherie a happy
        cherie.say "You know that it's what you want, Claire..."
        cherie.say "For [hero.name] and I to take charge for you."
        cherie.say "To let us make the decisions that scare you."
        show cherie a smile
        "I can only stand there, shaking my head in amazement."
        "As I watch Cherie talking Claire into what I guess would be a threesome!"
        $ claire.sub += 2
        $ cherie.sub -= 2
        if claire.lesbian < 9:
            $ claire.lesbian += 2
    menu:
        "We're just three vunerable people that need each other":
            "And if this thing is going to blow up in my face, then I'm going to be honest."
            "I'm going to put all of my cards on the table in front of Claire and Cherie."
            mike.say "Okay, okay..."
            mike.say "Here's the situation as I see it..."
            "I point to Claire."
            show claire sad
            mike.say "Claire's trapped in a loveless marriage with Hector, a big, fat slob."
            mike.say "We reconnected and started to have a good time together."
            mike.say "And soon enough, I couldn't imagine being without her."
            show claire sadsmile blush
            "I look at Claire, seeing that there's genuine emotion in her eye."
            "My confession of how I feel about her seeming to touch her heart."
            "Then I risk a glance at Cherie, expecting to see her glaring at me."
            "But instead I see a look of interest in her eyes."
            "Okay, in for a penny, in for a pound."
            show cherie a sad
            mike.say "Cherie was married to Dwayne, who's basically a rich, buff version of Hector."
            mike.say "He was the big boss around here, and he treated her like shit."
            mike.say "Then, when he went missing, I helped her to take the reigns of the company."
            mike.say "And since then, we've gotten ever closer."
            show cherie a sadsmile blush
            "Once I'm done talking about Cherie, I look her in the eye again."
            "Seeing that she's got the same expression on her face that Claire did just now."
            "And sure enough, she's now the one looking over at Claire in genuine interest."
            "Now I figure that I have to do some explaining for myself too."
            mike.say "And as for me..."
            mike.say "I guess I'm vulnerable too."
            mike.say "Lonely enough to think that I needed two women's love, rather than just the one."
            $ claire.love += 2
            $ cherie.love += 2
        "You're both mine and I am not going to apologise for it" if claire.sub >= 25 and cherie.sub >= 25:
            "Wait a minute - why am I struggling to explain myself and coming out with excuses?"
            "I've been juggling a demanding female CEO with a fortune of her own on the one hand."
            "And a drop-dead gorgeous MILF that's begging to be validated on the other."
            "Hell, even if this is the end of all that, I'm not going to act like I'm ashamed of it!"
            mike.say "This is pretty much what it looks like, girls..."
            show cherie a stuned
            show claire stuned
            mike.say "I've been seeing the both of you at the same time."
            mike.say "And if Clare hadn't walked in here just now..."
            mike.say "Well, neither of you would have been any the wiser, and I'd have gotten away with it!"
            "Okay, so I either just talked myself out of this, or else signed my own death warrant."
            "And at first I can see that Claire and Cherie are both glaring at me."
            show claire normal
            "But the former is the first to break, a little smile creeping onto her face."
            show claire talkative
            claire.say "Oh, [hero.name]…"
            claire.say "You're the devil himself!"
            show claire normal
            "For a moment I think that Cherie's going to object to what Claire's saying."
            show cherie a normal
            "But then she shakes her head and lets out a sigh."
            show cherie a talkative
            cherie.say "Ah, she is right, mon ami..."
            cherie.say "You do have a little of the demonic about you!"
            show cherie a normal
            mike.say "So there you have it, ladies..."
            mike.say "As far as I'm concerned, you're both mine."
            mike.say "And that's how things are going to stay."
            $ claire.sub += 2
            $ cherie.sub += 2
    show claire normal
    show cherie a normal
    mike.say "Okay..."
    mike.say "There you have it, guys."
    mike.say "Everything's out in the open now."
    mike.say "So what happens next?"
    if all([person.love >= 135 and person.lesbian >= 7 for person in [claire, cherie]]) and claire.sub >= 25 and cherie.sub.abs >= 25:
        "I watch in silence as Cherie empties the basket onto the desk."
        show eat_snacks_meals_01 as meal1 zorder 2 at center, zoomAt(1.0, (940, 960))
        show eat_snacks_meals_01 as meal2 zorder 2 at center, zoomAt(1.0, (340, 980))
        with fade
        "And then Claire begins to portion out the food between us."
        "It feels totally uncanny, the way they're now working together."
        mike.say "So..."
        mike.say "Does this mean that..."
        show cherie a smile at center, traveling(1.5, 0.5, (840, 1080))
        show claire evil at center, traveling(1.5, 0.5, (440, 1080))
        "As one, Claire and Cherie turn to face me."
        "And suddenly I feel like I'm being put on the spot."
        mike.say "I mean..."
        mike.say "Nobody's storming out or throwing stuff..."
        mike.say "So does that mean we're..."
        "Without saying a word, Cherie places her lips against mine."
        "Then Claire does the same, so that all three of us are united in the kiss."
        "And only once it's over do they answer my question."
        show claire talkative
        claire.say "I'm not sure what it means yet, [hero.name]…"
        claire.say "But I think we're going to have a lot of fun finding out!"
        show claire happy
        show cherie a happy
        cherie.say "Exactly so, Claire - we will do everything together."
        cherie.say "And I do mean everything!"
        show cherie a smile
        show claire normal
        "I'm nodding as the girls say all of this, trying to appear calm."
        "But the truth is that my heart's racing at the mere thought of it."
        "Claire, Cherie and me - all coming together, in every sense of the word!"
        $ Harem.join_by_name("milf", claire, cherie)
    elif claire.love >= cherie.love and claire.love >= 125:
        show cherie a upset at center, traveling(1.25, 0.5, (940, 880))
        "Cherie takes a moment to collect herself and straighten her clothes."
        "And then she looks me straight in the eye, like she means business."
        show cherie a whining
        cherie.say "I have fought long and hard to win control of my life."
        cherie.say "And I need an equal to stand at my side now that I do."
        cherie.say "Someone that I can rely on and is devoted to me."
        show cherie a angry
        cherie.say "And my lovers are no exception to that rule!"
        show cherie a upset
        mike.say "Cherie..."
        mike.say "Wait..."
        "Cherie is totally unaffected by my desperate pleading."
        hide cherie with easeoutleft
        play sound door_slam
        pause 0.3
        with hpunch
        "And she storms out of the office, leaving me alone with Claire."
        show claire whining at center, traveling(1.25, 0.5, (640, 880))
        claire.say "Oh my goodness me!"
        claire.say "These foreign types, they can be so dramatic, can't they?"
        show claire talkative
        claire.say "You don't need that kind of stress in your life."
        claire.say "No, what you need is someone that's sensible and reliable."
        show claire normal
        "I glance at the doors and then back at Claire."
        "Still kind of stunned at how Cherie just stormed out."
        "As well as at how casually Claire seems to be taking it all."
        show claire at center, traveling(1.5, 0.5, (640, 1080))
        show eat_snacks_meals_01 as meal1 zorder 2 at center, zoomAt(1.0, (940, 960))
        show eat_snacks_meals_01 as meal2 zorder 2 at center, zoomAt(1.0, (340, 980))
        with fade
        "Because she's already started unpacking the lunch from the basket."
        "Setting it out on the table for the two of us to enjoy."
        $ cherie.set_gone_forever()
    elif cherie.love >= claire.love and cherie.love >= 125:
        show claire upset at center, traveling(1.25, 0.5, (340, 880))
        "Claire pulls herself up to her full height and shakes her head."
        "Doing all she can to regain her sense of poise and dignity."
        show claire whining
        claire.say "Well, I hope that the two of you are happy, [hero.name]…"
        claire.say "Because you may be a two-woman kind of man..."
        claire.say "But I'm definitely not going to share you with her!"
        claire.say "I'm just sorry that I wasn't enough for you!"
        show claire sad
        mike.say "Claire..."
        mike.say "Wait..."
        "Claire is totally unaffected by my desperate pleading."
        hide claire with easeoutleft
        play sound door_slam
        pause 0.3
        with hpunch
        "And she storms out of the office, leaving me alone with Cherie."
        show cherie a whining at center, traveling(1.25, 0.5, (640, 880))
        cherie.say "Oh dear, mon ami..."
        cherie.say "We seem to have offended the little housewife!"
        show cherie a talkative
        cherie.say "But do not worry, I am far harder to upset."
        cherie.say "And look, she has kindly left us with lunch!"
        show cherie a smile
        "I glance at the doors and then back at Cherie."
        "Still kind of stunned at how Claire just stormed out."
        "As well as at how casually Cherie seems to be taking it all."
        show cherie a at center, traveling(1.5, 0.5, (640, 1080))
        show eat_snacks_meals_01 as meal1 zorder 2 at center, zoomAt(1.0, (940, 960))
        show eat_snacks_meals_01 as meal2 zorder 2 at center, zoomAt(1.0, (340, 980))
        with fade
        "Because she's already started unpacking the lunch from the basket."
        "Setting it out on the table for the two of us to enjoy."
        $ claire.set_gone_forever()
    else:
        show cherie a upset at center, traveling(1.25, 0.5, (940, 880))
        show claire upset at center, traveling(1.25, 0.5, (340, 880))
        "Claire and Cherie both seem to do all that they can to regain their dignity."
        "Standing up straight and smoothing their clothes as best they can."
        show claire whining
        claire.say "Well, I hope that the two of you are happy, [hero.name]…"
        claire.say "Because you may be a two-woman kind of man..."
        claire.say "But I'm definitely not going to share you with her!"
        claire.say "I'm just sorry that I wasn't enough for you!"
        show claire sad
        show cherie a whining
        cherie.say "I have fought long and hard to win control of my life."
        cherie.say "And I need an equal to stand at my side now that I do."
        cherie.say "Someone that I can rely on and is devoted to me."
        show cherie a angry
        cherie.say "And my lovers are no exception to that rule!"
        show cherie a upset
        mike.say "Claire..."
        mike.say "Cherie..."
        mike.say "Wait..."
        hide claire
        hide cherie
        with easeoutleft
        play sound door_slam
        pause 0.3
        with hpunch
        "My pleas fall on deaf ears, as Claire and Cherie storm out of the office."
        "And a moment later I'm left standing there alone."
        "Feeling utterly dejected, I walk over to the desk."
        "And I begin rooting around in the basket containing the lunch that Claire made for me."
        "Thinking that I can at least comfort myself that way."
        "Though it feels like the emotional pain from this one is going to last a lot longer."
        $ claire.set_gone_forever()
        $ cherie.set_gone_forever()
    scene bg black with dissolve
    pause 0.3
    return

label milf_harem_event_03:
    scene bg livingroom with fade
    "I'm feeling pretty good about myself right now, like I finally have a lot of stuff figured out."
    "There's a definite spring in my step, and I keep finding myself whistling happily without even realising it."
    play sound door_knock
    "So when there's a knock at the front-door, I don't hesitate to leap up and stroll leisurely into the hallway."
    "I even do a little kind of shuffling dance as I reach the door and swing it open in a nonchalant manner."
    "Wondering if I should add a witty little quip to whoever I find waiting on the other side."
    mike.say "Hey..."
    mike.say "How's it..."
    scene bg black
    show bg house
    show cherie a annoyed at center, zoomAt(1.0, (640, 720))
    show claire upset at center, zoomAt(1.0, (340, 720))
    show kiara upset at center, zoomAt(1.0, (940, 720))
    with wiperight
    mike.say "OH SHIT!"
    "Everything changes in the blink of an eye, literally as soon as I see who's waiting for me."
    "Or to be more precise, when I see the three people that are standing on the porch."
    "Their arms crossed over their chests and looks of intense irritation on their faces."
    show cherie a angry
    show kiara angry
    show claire angry
    with vpunch
    "Cherie, Claire & Kiara" "WE NEED TO TALK!"
    show kiara upset
    show claire upset
    cherie.say "Merde is the word, mon ami!"
    show cherie a annoyed
    show kiara angry
    kiara.say "Ah, now he sees the predicament he is in!"
    show kiara upset
    show claire angry
    claire.say "Open up, mister - because you've got some explaining to do!"
    show claire upset
    "Okay, so I might have been living dangerously by trying to date three beautiful women all at once."
    "And yes, I did think that I'd dodged a bullet when Claire found out separately about Cherie and Kiara."
    show claire at center, traveling (1.25, 0.3, (340, 900))
    "But the mistake that I made becomes glaringly obvious to me when it's Claire that steps forwards first."
    "Why in the hell did I think she'd keep the two other girls I've been seeing on the side a secret from each other?"
    "She must be the brains behind this surprise raid, the one coordinating their efforts against me!"
    mike.say "I..."
    mike.say "I know this looks bad, okay..."
    mike.say "But I can explain!"
    "Before I can say another word, Claire, Cherie and Kiara surge forwards as one."
    "Alternatively throwing their hands into the air and jabbing at me with their fingers."
    scene bg livingroom with hpunch
    pause 0.3
    show cherie a annoyed at center, zoomAt(1.0, (640, 720))
    show claire upset at center, zoomAt(1.0, (340, 720))
    show kiara upset at center, zoomAt(1.0, (940, 720))
    with easeinright
    "I'm instantly forced backwards down the hallway as they step into the house uninvited."
    "Holding my own hands up in a feeble effort to keep from being swamped, I retreat towards the kitchen."
    show claire at center, traveling (1.25, 0.3, (200, 900))
    "But even as they come on, the three of them seem to be looking here and there as they do so."
    show kiara a at center, traveling(1.25, 0.3, (1080, 900))
    "Opening any doors that they pass and glancing behind pieces of furniture large enough to hide a person."
    show claire angry
    claire.say "Where are you hiding them all?"
    show claire upset
    show cherie a angry at center, traveling(1.25, 0.3, (640, 900))
    cherie.say "Where are those girls you live with?"
    show cherie a annoyed
    show kiara angry
    kiara.say "Yes, where are Bree and Sasha - are they in on this too?!?"
    scene bg kitchen with hpunch
    pause 0.3
    show cherie a annoyed at center, zoomAt(1.0, (640, 720))
    show claire upset at center, zoomAt(1.0, (340, 720))
    show kiara upset at center, zoomAt(1.0, (940, 720))
    with easeinright
    "Now that we're finally in the kitchen, there's nowhere else for me to go."
    "And so I soon find my back pressed against the wall as they converge on me from three sides."
    mike.say "Girls, girls, girls..."
    show claire angry
    claire.say "Exactly, [hero.name]…"
    show claire upset
    show cherie a angry
    cherie.say "Girls, girls and more girls!"
    show cherie a annoyed
    show kiara angry
    kiara.say "Just how many more of them are you hiding from us?"
    show kiara upset
    "Even as harassed and harangued as I feel right now, that question still makes me sit up and pay attention."
    "Because it gives me the beginning of an insight into what's going on here on a deeper level."
    mike.say "Wait, you think I'm seeing more girls than just the three of you?"
    mike.say "Come on, don't you think that sounds just a little crazy?"
    show cherie a annoyed at center, traveling(1.1, 0.2, (640, 780))
    show claire upset at center, traveling(1.1, 0.2, (380, 780))
    show kiara upset at center, traveling(1.1, 0.2, (900, 780))
    "As soon as I say it, I realise that perhaps crazy wasn't the best term to use."
    "Because it soon has the three of them back in my face and pointing fingers."
    show claire furious
    claire.say "Are you trying to gaslight us, or what?"
    claire.say "Because you're not the most trustworthy of people, you know?"
    show claire upset
    show cherie a angry
    cherie.say "Maybe you have the organisational skills to manage more girls, maybe not."
    cherie.say "But if we need to interrogate you to find out, then we will!"
    show cherie a annoyed
    show kiara guilty
    kiara.say "She's right, [hero.name]…"
    show kiara angry
    kiara.say "We have ways of making you talk!"
    show kiara upset
    "I take a deep breath, doing the best I can to collect myself."
    "And then I breath out with a loud sigh, tyring to regain control."
    mike.say "That's what I've been trying to do, Kiara..."
    mike.say "I've been trying to talk."
    mike.say "So let's crack open a bottle of wine, grab a glass each, and then we'll talk - okay?"
    "Yeah, I know that offering women of their age a bottle of wine is kind of a cliché."
    show claire normal
    show cherie a normal
    show kiara normal
    "But the moment they hear the suggestion, their moods do seem to improve just a little."
    "Enough to make them all back off while I grab one of the bottles we keep in the kitchen."
    "Then I pop the cork, putting out four glasses and making sure to fill them all with the same amount."
    play sound glass_wine
    "Claire is the first to take up her glass, sipping and looking quite mollified."
    play sound glass_wine
    "But soon enough the others are taking a drink too."
    show claire talkative
    claire.say "Thank you, [hero.name], the wine is very nice."
    show claire furious
    claire.say "But you're still a big, lying bastard!"
    show claire upset
    show cherie a talkative
    cherie.say "Yes, mon ami…"
    cherie.say "I hope to never have to negotiate a contract with you."
    show cherie a annoyed
    show kiara talkative
    kiara.say "Makes me wonder if you play poker, you know?"
    kiara.say "How good are you at bluffing?"
    show kiara mischievous
    "Somehow the jibes and verbal prodding doesn't seem to land as hard by now."
    "And I'm beginning to feel like I have the room to actually think clearly."
    "Which means it's becoming apparent to me that I need to try and explain myself."
    if cherie.sub <= -25 and kiara.sub <= -25:
        "Before I can even think of what I'm going to say, I'm attacked on two sides."
        "Kiara gets in my face on the right, and Cherie closes in on the left."
        "Each of them herding me like sheepdogs with a confused and terrified ewe."
        show kiara angry
        kiara.say "This is not about emotions and such frivolous things."
        kiara.say "No, this is a matter of supply and logistics."
        show kiara mischievous
        show cherie a angry
        cherie.say "Exactly so, mon ami…"
        cherie.say "We must approach this in the same way as we do a business deal."
        cherie.say "So, [hero.name] - can you deliver the goods?"
        show cherie a annoyed
        show claire stuned
        "I'm relieved to see that Claire seems to be as surprised by all of this as I am."
        "Shaking her head and looking between the two of them like they've gone off-script."
        show claire surprised
        claire.say "Huh?"
        claire.say "Aren't we supposed to be mad at him for dating us all at once?"
        show claire stuned
        show cherie a talkative
        cherie.say "Not if he can actually pull it off."
        show cherie a annoyed
        show kiara talkative
        kiara.say "If he can deliver, then I might be interested in the offer."
        show kiara mischievous
        mike.say "Well, if that's what you guys want..."
        $ claire.sub += 2
        $ cherie.sub -= 2
        $ kiara.sub -= 2
    menu:
        "Explain that you love all of them and they're all special to you":
            "I stand back and shake my head, gesturing to the three of them."
            mike.say "Man..."
            mike.say "Just look at the three of you."
            mike.say "How could any man not want to be with a trio like that?"
            show claire bored
            show cherie a annoyed
            show kiara pout
            "This earns me a round of rolling eyes and shaken heads."
            show claire pissed
            claire.say "Flatterer!"
            show claire bored
            show cherie a angry
            cherie.say "Silver tongued devil!"
            show cherie a annoyed
            show kiara evil
            kiara.say "Oh, such bullshit!"
            show kiara pout
            "I shrug my shoulders helplessly."
            mike.say "I'm being serious, guys!"
            mike.say "Being with any one of you would be a dream come true."
            mike.say "So can you really blame me for wanting to be with all of you at once?"
            mike.say "Seriously, you're all special to me, and I love each of you equally."
            $ claire.love += 1
            $ cherie.love += 1
            $ kiara.love += 1
        "Explain that they're all yours and will just have to follow your rules now" if claire.sub >= 25 and cherie.sub >= 25 and kiara.sub >= 25:
            "I shrug and make a nonchalant gesture."
            mike.say "Oh, come on, ladies..."
            mike.say "You know that you love this, right?"
            mike.say "All three of you being mine?"
            show claire bored
            show cherie a annoyed
            show kiara pout
            "This earns me a round of rolling eyes and shaken heads."
            show claire pissed
            claire.say "Egomaniac!"
            show claire bored
            show cherie a angry
            cherie.say "So full of yourself!"
            show cherie a annoyed
            show kiara evil
            kiara.say "Oh, such a big man!"
            show kiara pout
            "Not letting any of their comments get to me, I press on."
            mike.say "You words say one thing, but your faces say another."
            mike.say "But that's no concern of mine."
            mike.say "The three of you belong to me now."
            mike.say "And it's going to be my way or the highway from now on."
            $ claire.sub += 2
            $ cherie.sub += 2
            $ kiara.sub += 2
    show claire sadsmile
    show cherie a closed
    "Things certainly seem to have calmed down by now, with there being no more pointing and shouting."
    show kiara serious
    show claire disappointed
    "And everything that's come out must be turning over inside of their minds, as they look thoughtful."
    "So the best I can do is keep on sipping my wine and waiting to hear what they have to say for themselves."
    show kiara fantasize
    "Because I certainly don't think my speaking up again is going to help matters."
    show cherie a annoyed
    show kiara blank
    show claire bored
    "Almost at the same moment, all three of them slam down their glasses, as if about to make a pronouncement."
    if all([person.love >= 150 and person.lesbian >= 9 for person in [claire, cherie, kiara]]) and claire.sub >= 25 and cherie.sub.abs >= 25 and kiara.sub.abs >= 25:
        show claire annoyed
        claire.say "I've waited years for [hero.name] to be mine."
        claire.say "And I'm not going to lose him now."
        claire.say "Not because I don't know how to share!"
        show claire disappointed
        show cherie a angry
        cherie.say "I could not have endured the things I have been though without him."
        cherie.say "So I cannot just abandon him in the face of a challenge."
        cherie.say "This will be hard, but no harder than what we have already endured."
        show cherie a annoyed
        show kiara guilty
        kiara.say "[hero.name] is an important part of my organisation, and my life."
        kiara.say "And I will not give him up just because he has too much love to give."
        kiara.say "More than enough for all three of us to share."
        show kiara remorse
        "I can hardly believe what I'm hearing right now."
        show claire normal blush at center, traveling(1.5, 1.0, (400, 1040))
        show cherie a smile at center, traveling(1.5, 1.0, (640, 1040))
        show kiara flirt at center, traveling(1.5, 1.0, (880, 1040))
        "And the only thing I can think to do is throw my arms around the three of them."
        "They respond by doing the same, pulling the four of us into a group embrace."
        mike.say "I want you to know that this is a totally crazy idea."
        mike.say "But I think we can make it work..."
        mike.say "So long as we face whatever comes together."
        $ Harem.join_by_name("milf", claire, cherie, kiara)
    elif claire.love >= kiara.love and cherie.love >= kiara.love and claire.love >= 140 and cherie.love >= 140:
        show claire annoyed
        claire.say "I've waited years for [hero.name] to be mine."
        claire.say "And I'm not going to lose him now."
        claire.say "Not because I don't know how to share!"
        show claire disappointed
        show cherie a angry
        cherie.say "I could not have endured the things I have been though without him."
        cherie.say "So I cannot just abandon him in the face of a challenge."
        cherie.say "This will be hard, but no harder than what we have already endured."
        show cherie a annoyed
        "I turn to look at Kiara, who hasn't spoken yet."
        show kiara whining
        kiara.say "[hero.name] is an important part of my organisation, and my life."
        kiara.say "But in my world, there is no greater thing than loyalty."
        kiara.say "And if I do not have it from him, then there is no hope for us!"
        show kiara sad
        mike.say "No..."
        mike.say "Wait, Kiara..."
        mike.say "Can't we talk about this?"
        hide kiara with easeoutright
        "Without another word, Kiara stands up and walks out."
        play sound door_slam
        pause 0.3
        with hpunch
        "And I look over to Claire and Cherie as I hear the sound of the front-door closing behind her."
        show claire normal blush at center, traveling(1.5, 1.0, (440, 1040))
        show cherie a smile at center, traveling(1.5, 1.0, (800, 1040))
        "The only thing I can think to do is throw my arms around the two of them."
        "They respond by doing the same, pulling the three of us into a group embrace."
        mike.say "I want you to know that this is a totally crazy idea."
        mike.say "But I think we can make it work..."
        mike.say "So long as we face whatever comes together."
        $ kiara.set_gone_forever()
    elif claire.love >= cherie.love and kiara.love >= cherie.love and claire.love >= 140 and kiara.love >= 140:

        show claire annoyed
        claire.say "I've waited years for [hero.name] to be mine."
        claire.say "And I'm not going to lose him now."
        claire.say "Not because I don't know how to share!"
        show claire disappointed
        show kiara guilty
        kiara.say "[hero.name] is an important part of my organisation, and my life."
        kiara.say "And I will not give him up just because he has too much love to give."
        kiara.say "More than enough for all three of us to share."
        show kiara remorse
        "I turn to look at Cherie, who hasn't spoken yet."
        show cherie a whining
        cherie.say "I could not have endured the things I have been though without him."
        cherie.say "But I need to know that I have his undivided attention and affection."
        cherie.say "I cannot do what needs to be done without that."
        show cherie a sad
        mike.say "No..."
        mike.say "Wait, Cherie..."
        mike.say "Can't we talk about this?"
        hide cherie with easeoutright
        "Without another word, Cherie stands up and walks out."
        play sound door_slam
        pause 0.3
        with hpunch
        "And I look over to Claire and Kiara as I hear the sound of the front-door closing behind her."
        show claire normal blush at center, traveling(1.5, 1.0, (440, 1040))
        show kiara flirt at center, traveling(1.5, 1.0, (800, 1040))
        "The only thing I can think to do is throw my arms around the two of them."
        "They respond by doing the same, pulling the three of us into a group embrace."
        mike.say "I want you to know that this is a totally crazy idea."
        mike.say "But I think we can make it work..."
        mike.say "So long as we face whatever comes together."
        $ cherie.set_gone_forever()
    elif cherie.love >= claire.love and kiara.love >= claire.love and cherie.love >= 140 and kiara.love >= 140:

        show cherie a angry
        cherie.say "I could not have endured the things I have been though without him."
        cherie.say "So I cannot just abandon him in the face of a challenge."
        cherie.say "This will be hard, but no harder than what we have already endured."
        show cherie a annoyed
        show kiara guilty
        kiara.say "[hero.name] is an important part of my organisation, and my life."
        kiara.say "And I will not give him up just because he has too much love to give."
        kiara.say "More than enough for all three of us to share."
        show kiara remorse
        "I turn to look at Claire, who hasn't spoken yet."
        show claire whining
        claire.say "I've waited years for [hero.name] to be mine."
        claire.say "And I'm not going to share him with anyone else!"
        claire.say "Either he's mine alone, or I don't want him."
        show claire sad
        mike.say "No..."
        mike.say "Wait, Claire..."
        mike.say "Can't we talk about this?"
        hide claire with easeoutright
        "Without another word, Claire stands up and walks out."
        play sound door_slam
        pause 0.3
        with hpunch
        "And I look over to Cherie and Kiara as I hear the sound of the front-door closing behind her."
        show cherie a smile blush at center, traveling(1.5, 1.0, (440, 1040))
        show kiara flirt at center, traveling(1.5, 1.0, (800, 1040))
        "The only thing I can think to do is throw my arms around the two of them."
        "They respond by doing the same, pulling the three of us into a group embrace."
        mike.say "I want you to know that this is a totally crazy idea."
        mike.say "But I think we can make it work..."
        mike.say "So long as we face whatever comes together."
        $ claire.set_gone_forever()
    elif claire.love >= cherie.love and claire.love >= kiara.love and claire.love >= 140:

        show claire annoyed
        claire.say "I've waited years for [hero.name] to be mine."
        claire.say "And I'm not going to lose him now."
        claire.say "Not because I don't know how to share!"
        show claire disappointed
        "I turn to look at Cherie and Kiara, who haven't spoken yet."
        show cherie a whining
        cherie.say "I could not have endured the things I have been though without him."
        cherie.say "But I need to know that I have his undivided attention and affection."
        cherie.say "I cannot do what needs to be done without that."
        show cherie a sad
        show kiara whining
        kiara.say "[hero.name] is an important part of my organisation, and my life."
        kiara.say "But in my world, there is no greater thing than loyalty."
        kiara.say "And if I do not have it from him, then there is no hope for us!"
        show kiara sad
        mike.say "No..."
        mike.say "Wait, Cherie, Kiara..."
        mike.say "Can't we talk about this?"
        hide cherie
        hide kiara
        with easeoutright
        "Without another word, Cherie and Kiara stand up and walk out."
        play sound door_slam
        pause 0.3
        with hpunch
        "And I look over to Claire as I hear the sound of the front-door closing behind them."
        show claire normal blush at center, traveling(1.5, 1.0, (640, 1040))
        "The only thing I can think to do is throw my arms around her."
        "She responds by doing the same thing, clinging onto me tightly."
        mike.say "I know all of that was pretty crazy."
        mike.say "But I think we can make it work..."
        mike.say "So long as we face whatever comes together."
        $ cherie.set_gone_forever()
        $ kiara.set_gone_forever()
    elif cherie.love >= claire.love and cherie.love >= kiara.love and cherie.love >= 140:

        show cherie a angry
        cherie.say "I could not have endured the things I have been though without him."
        cherie.say "So I cannot just abandon him in the face of a challenge."
        cherie.say "This will be hard, but no harder than what we have already endured."
        show cherie a annoyed
        "I turn to look at Claire and Kiara, who haven't spoken yet."
        show claire whining
        claire.say "I've waited years for [hero.name] to be mine."
        claire.say "And I'm not going to share him with anyone else!"
        claire.say "Either he's mine alone, or I don't want him."
        show claire sad
        show kiara whining
        kiara.say "[hero.name] is an important part of my organisation, and my life."
        kiara.say "But in my world, there is no greater thing than loyalty."
        kiara.say "And if I do not have it from him, then there is no hope for us!"
        show kiara sad
        mike.say "No..."
        mike.say "Wait, Claire, Kiara..."
        mike.say "Can't we talk about this?"
        hide claire
        hide kiara
        with easeoutright
        "Without another word, Claire and Kiara stand up and walk out."
        play sound door_slam
        pause 0.3
        with hpunch
        "And I look over to Cherie as I hear the sound of the front-door closing behind them."
        show cherie a smile at center, traveling(1.5, 1.0, (640, 1040))
        "The only thing I can think to do is throw my arms around her."
        "She responds by doing the same thing, clinging onto me tightly."
        mike.say "I know all of that was pretty crazy."
        mike.say "But I think we can make it work..."
        mike.say "So long as we face whatever comes together."
        $ claire.set_gone_forever()
        $ kiara.set_gone_forever()
    elif kiara.love >= claire.love and kiara.love >= cherie.love and kiara.love >= 140:

        show kiara guilty
        kiara.say "[hero.name] is an important part of my organisation, and my life."
        kiara.say "And I will not give him up just because he has too much love to give."
        kiara.say "More than enough for all three of us to share."
        show kiara remorse
        "I turn to look at Claire and Cherie, who haven't spoken yet."
        show claire whining
        claire.say "I've waited years for [hero.name] to be mine."
        claire.say "And I'm not going to share him with anyone else!"
        claire.say "Either he's mine alone, or I don't want him."
        show claire sad
        show cherie a whining
        cherie.say "I could not have endured the things I have been though without him."
        cherie.say "But I need to know that I have his undivided attention and affection."
        cherie.say "I cannot do what needs to be done without that."
        show cherie a sad
        mike.say "No..."
        mike.say "Wait, Claire, Cherie..."
        mike.say "Can't we talk about this?"
        hide claire
        hide cherie
        with easeoutright
        "Without another word, Claire and Cherie stand up and walk out."
        play sound door_slam
        pause 0.3
        with hpunch
        "And I look over to Kiara as I hear the sound of the front-door closing behind them."
        show kiara flirt at center, traveling(1.5, 1.0, (640, 1040))
        "The only thing I can think to do is throw my arms around her."
        "She responds by doing the same thing, clinging onto me tightly."
        mike.say "I know all of that was pretty crazy."
        mike.say "But I think we can make it work..."
        mike.say "So long as we face whatever comes together."
        $ claire.set_gone_forever()
        $ cherie.set_gone_forever()
    else:
        show claire whining
        claire.say "I've waited years for [hero.name] to be mine."
        claire.say "And I'm not going to share him with anyone else!"
        claire.say "Either he's mine alone, or I don't want him."
        show claire sad
        show cherie a whining
        cherie.say "I could not have endured the things I have been though without him."
        cherie.say "But I need to know that I have his undivided attention and affection."
        cherie.say "I cannot do what needs to be done without that."
        show cherie a sad
        show kiara whining
        kiara.say "[hero.name] is an important part of my organisation, and my life."
        kiara.say "But in my world, there is no greater thing than loyalty."
        kiara.say "And if I do not have it from him, then there is no hope for us!"
        show kiara sad
        "I shake my head as I listen to what the girls have to say."
        "Knowing that it means my world is falling apart."
        mike.say "No..."
        mike.say "Wait..."
        mike.say "Can't we talk about this?"
        "I'm waving my hands in the air and trying to get their attention."
        "But the girls are already grabbing their things and standing up."
        hide claire
        hide cherie
        hide kiara
        with easeoutright
        "And then they troop back into the hallway and out of the front-door."
        "Leaving me to stand in the open doorway, helpless to do a thing about it."
        $ claire.set_gone_forever()
        $ cherie.set_gone_forever()
        $ kiara.set_gone_forever()
    scene bg black with dissolve
    pause 0.3
    return

label milf_harem_event_04:
    scene bg street with fade
    "Part of me is still reeling from the very idea that when Claire, Cherie and Kiara found out about each other, I didn't get bumped off."
    "And the fact that there was a tumultuous meeting at which we all decided that we'd 'pool our resources' on top of that..."
    "Well, let's just say that I haven't quite managed to come all the way down from the high that I've been on ever since."
    "So when Kiara invites the three of us to the VIP lounge of her private and very exclusive club, I jump at the offer."
    "Because I figure that it's a chance to spend some quality time with all of my girls, away from the troubles of the world at large."
    scene nightclub
    show layer master at lparty
    with fade
    "But when I walk into the club and the very well dressed goons on the door wave me through to the lounge, I realise that I must be early."
    "As Kiara's the only one already there, looking as stunning as ever and beckoning me over to join her."
    scene nightclubbar
    show kiara date talkative at center
    show layer master at lparty
    with dissolve
    kiara.say "[hero.name], welcome!"
    kiara.say "You're the first of my guests to arrive."
    kiara.say "So let's hurry up and get you a drink, shall we?"
    show kiara smile
    mike.say "Hi, Kiara..."
    mike.say "I tried to get here as soon as I could."
    mike.say "A drink sounds great - maybe a beer?"
    show kiara stare
    pause 0.7
    show kiara smile at startle(0.1, 5)
    "Kiara throws her head back and lets out a peal of laughter."
    show kiara talkative
    kiara.say "A beer?"
    kiara.say "How quaint!"
    kiara.say "But no, no beer for you."
    kiara.say "Tonight we are drinking cocktails."
    play sound "<from 1.4 to 2.6>sd/SFX/humans/finger_snap.ogg"
    show kiara remorse at startle(0.1, -5)
    pause 0.2
    show kiara normal
    "I watch as Kiara clicks her fingers and the bartender instantly leaps into action."
    "Glasses clatter and bottles clink as they deftly mix up a complex cocktails right in front of me."
    "And when it's done, Kiara picks up the glass and hands it to me, nodding eagerly."
    show kiara talkative
    kiara.say "Try it, [hero.name]…"
    kiara.say "This is a creation of my own."
    kiara.say "I call it an 'Ice-Pick'!"
    show kiara normal
    play sound drinking
    "I nod and take a sip of the drink, wanting to please Kiara."
    "And the moment I've swallowed a mouthful, I feel it hit me."
    mike.say "Whoa..."
    mike.say "That is very strong, and..."
    show bg nightclubbar at blur(20)
    show kiara at blur(10)
    with hpunch
    mike.say "Aargh!"
    scene bg nightclubbar
    show kiara date
    show layer master at lparty
    with dissolve
    "A sudden pain blossoms inside of my skull, and then just as quickly fades again."
    "Reminding me of the effects that come along with an ice-cream headache."
    "But Kiara doesn't seem to be in the least bit concerned by my cry of pain."
    show kiara talkative
    kiara.say "You see now where the name comes from?"
    kiara.say "Drinking it is like the ice-pick to the skull, no?"
    kiara.say "Like a good old-fashioned way of whacking your enemies!"
    show kiara normal
    mike.say "Ah..."
    mike.say "Yeah, Kiara..."
    mike.say "Very nice!"
    claire.say "Ooh!"
    claire.say "Erm..."
    claire.say "Hello?"
    claire.say "Am I in the right place?"
    scene nightclub
    show claire date haircut pout
    show layer master at lparty
    with fade
    "As one, Kiara and I turn around to see Claire standing in the doorway."
    "She's obviously made an effort to dress up as nicely as she can."
    "Also I notice that her hair and make-up are far more fancy than usual."
    "But she still looks more than a little out of place in Kiara's lounge."
    show claire embarrassed at startle(0.1, -5)
    mike.say "Over here, Claire!"
    kiara.say "Yes, Claire..."
    kiara.say "Welcome to my humble club."
    scene bg nightclubbar
    show kiara date dreaming
    show layer master at lparty
    with fade
    pause 0.3
    show claire a date haircut conceited at left with easeinleft
    "As soon as she sees us, Claire looks relieved and hurries over."
    "Glancing around the place as she closes the short distance between us."
    show claire talkative
    claire.say "If this is humble, Kiara..."
    claire.say "I'd have to see what you call fancy!"
    show claire happy
    play sound "<from 1.4 to 2.6>sd/SFX/humans/finger_snap.ogg"
    show kiara smile at startle(0.1, -5)
    "Kiara just laughs at the comment and clicks her fingers again."
    "Which soon results in another cocktail appearing on the bar."
    "The sight of which does seem to improve Claire's mood somewhat."
    show claire talkative
    claire.say "Oh my!"
    claire.say "That's pretty fancy too."
    show claire normal
    "I watch in amazement as Claire plucks the cocktail of the bar and takes a sip."
    "Becoming even more amazed as she drains off almost half of it in one go!"
    mike.say "Slow down, Claire!"
    mike.say "These things are bloody strong."
    mike.say "You don't want to get plastered, do you?"
    "Claire lets out a gasp and wipes her mouth on the back of her hand."
    show claire talkative
    claire.say "Urgh..."
    claire.say "Don't I?"
    claire.say "If you'd had the kind of day I have, you wouldn't be saying that!"
    show claire normal
    "Kiara and I exchange a worried glance, then turn our attention back to Claire."
    mike.say "What does that mean?"
    show kiara whining
    kiara.say "Yes, Claire..."
    kiara.say "If misfortune has befallen you, we need to know about it."
    show kiara sadsmile
    "Claire takes another sip of her cocktail before answering."
    "But I note that this one is considerably smaller than the first."
    show claire annoyed
    claire.say "Oh, it's that pig of an ex-husband of mine."
    claire.say "He might have had a stroke, but it's not improved his mood any."
    show claire angry
    claire.say "And now I have to deal with his bitch of a lawyer, trying to cheat me out of what's rightfully mine!"
    show claire bored
    "I'm about to ask Claire to tell us more, eager to see if we can help."
    "But that's the exact moment the sound of another voice distracts me."
    cherie.say "I know that tone of voice, {i}mes amis…{/i}"
    cherie.say "It is the way a woman speaks when she is dealing with shit from her former husband!"
    cherie.say "I should know, I have been uttering it myself all day long."
    show cherie date annoyed at right with easeinright
    "Where Claire crept into the lounge meekly, Cherie sweeps in as if she owns the place."
    show cherie normal
    "Indeed I can tell from the look on her face that she's impressed with Kiara's club."
    "And she seems to fit in perfectly too, dressed for the décor and confident of her right to be here."
    mike.say "Hi, Cherie."
    show claire talkative
    claire.say "Oh, hello, Cherie!"
    show claire normal
    show kiara remorse at startle(0.1, -5)
    play sound "<from 1.4 to 2.6>sd/SFX/humans/finger_snap.ogg"
    show kiara normal with dissolve
    "Rather than saying hello, Kiara clicks her fingers once more."
    scene drink_room_club
    show claire a date haircut at center, zoomAt(1.65,(280,1060))
    show kiara a date at center, zoomAt(1.65,(640,1050))
    show cherie a date at center, zoomAt(1.65,(1040,1060))
    show drink_table_club_nonpc
    show drink_drink_sasha as drink_cl at center, zoomAt(1.0,(480,730))
    show drink_drink_sasha as drink_ki at center, zoomAt(1.0,(640,720))
    show drink_drink_sasha as drink_ch at center, zoomAt(1.0,(960,720))
    show drink_room_fg_pub
    show layer master at lparty
    with fade
    "And then presents the resulting cocktail to Cherie as her own form of greeting."
    "Which she takes with a nod, and then sips delicately, closing her eyes as she does so."
    "But for all of Cherie's practised poise and composure, I can see that she's weary."
    "Keeping up her usual trick of holding it all together for the sake of appearances."
    mike.say "Claire was just telling us that Hector's been making a nuisance of himself."
    show cherie annoyed
    "At the mention of Claire's ex-husband, Cherie's face breaks into a scowl."
    "And for the first time she seems to lose a little of her normally iron self-control."
    show claire stuned
    show kiara mischievous
    show cherie angry at startle(0.1, -5)
    cherie.say "HA!"
    cherie.say "A curse on all ex-husbands..."
    cherie.say "They are still a burden on their former wives when they are dead!"
    show cherie annoyed
    pause 0.5
    show cherie sadsmile
    "Suddenly Cherie seems to realise that Claire and I are staring at her in amazement."
    "Kiara, in contrast, is smiling and looking on with genuine interest."
    show claire sadsmile
    show cherie talkative
    cherie.say "Of course I am a tumult of emotions at the moment."
    cherie.say "And I am not saying that my husband is dead, you understand?"
    cherie.say "He is merely missing - a fact which the police do not seem to appreciate!"
    show cherie sadsmile
    "Finally I can start to get a handle on what's bugging Cherie."
    "And her current mood is starting to make sense to me."
    mike.say "So..."
    mike.say "I'm guessing you had a run-in with the police?"
    show cherie closed
    "Cherie closes her eyes for a moment and takes a deep breath."
    "She seems to be using the opportunity to center herself."
    show cherie normal
    "And when she lets it out again and opens her eyes, it's with renewed focus and control."
    show cherie amused at startle(0.1, -5)
    cherie.say "Hmm..."
    show cherie talkative
    cherie.say "Yes, {i}mon ami…{/i}"
    cherie.say "This detective they have put on the case..."
    cherie.say "He is like a Blood Hound with a scent - he will not give up!"
    show cherie annoyed
    "I can't help frowning as I nod along to what Cherie's saying."
    "Claire doing the same as she sips on her own cocktail."
    show kiara talkative at startle(0.1, -5)
    kiara.say "Ah..."
    kiara.say "What problems we endure, my friends!"
    kiara.say "If only there were something that we could do about it."
    kiara.say "If only one of us was in charge of a network of underworld fixers."
    kiara.say "The kind of people who could take care of a pesky lawyer or a bothersome detective..."
    show kiara normal
    show cherie stuned
    show claire stuned
    "As one, Claire, Cherie and I turn to look at Kiara."
    show kiara smile
    pause 0.5
    show kiara dreaming
    "As we do so, she smiles and looks around at the room we're standing in."
    show kiara talkative
    kiara.say "Oh, how forgetful of me - one of us is all of those things!"
    show kiara smile
    show cherie normal
    show claire normal
    mike.say "Kiara's right, you guys..."
    mike.say "We can use her underworld connections to stick it to those assholes!"
    show kiara pout at startle(0.1, 5)
    kiara.say "Hmm..."
    show kiara talkative
    kiara.say "I prefer to use the term 'legitimate business associates'."
    show kiara normal
    show claire whining
    claire.say "Oh no..."
    claire.say "Nobody's going to get hurt, are they?"
    show claire sad
    show cherie talkative
    cherie.say "What exactly do you have in mind?"
    cherie.say "Remember that I have the law breathing down my neck already!"
    show cherie annoyed
    if kiara.sub <= 50:

        "Before I can say anything more, Kiara seems to step up and take control."
        "Waving her hand and setting her people into motion around us."
        show kiara angry
        kiara.say "This is a classic show of disrespect, to both of you!"
        kiara.say "When something like that happens, swift action is required."
        kiara.say "We will send men that we trust to...explain the situation."
        show kiara guilty
        kiara.say "They will talk to this Hector, for you, Claire."
        kiara.say "And the policemen involved in your case, Cherie."
        show kiara upset
        "By now all four of us are huddled together."
        "Listening closely as Kiara details her plan."
        show kiara talkative
        kiara.say "First they will warn."
        kiara.say "If that does not work, they will offer a small bribe."
        kiara.say "And finally, they will administer physical incentives."
        show kiara mischievous
        mike.say "I can help organise the goon squads!"
        show cherie talkative
        cherie.say "I can maximise your utilisation of resources."
        show cherie normal
        show claire startle
        claire.say "And I can..."
        claire.say "Well...I can whip us all up a homemade meal - to keep our strength up!"
        show claire sadsmile
    else:
        menu:
            "We could use Kiara's underworld contacts in a discreet manner":
                "I can see that Kiara's right that this is a way out for us."
                "But Claire and Cherie make valid points too."
                "So maybe there's a way to do this that will please everyone?"
                mike.say "Look, we don't have to do this in a violent way."
                mike.say "Kiara's people are good at being subtle too."
                mike.say "Like, if we offer Hector and the cops a little bribe to back off."
                mike.say "Carrot and stick, you see?"
                show claire normal
                show cherie normal
                show kiara mischievous
                "I can see that Claire and Cherie are listening to me with interest."
                "But Kiara's actually studying me in a much more intense manner."
                "Almost like she's interested in seeing how well I can pull this off."
                show kiara irritated
                kiara.say "But what is your back-up plan?"
                kiara.say "What if they hear your offer and still say you can go to hell?"
                show kiara mischievous
                mike.say "Well, we'll have tried the carrot..."
                mike.say "So then we resort to the stick instead."
                show kiara normal
                "Kiara nods, showing her approval."
                show kiara talkative
                kiara.say "Sounds like a plan to me."
                kiara.say "Come on, let's get the ball rolling."
                show kiara normal
            "We could use Kiara's underworld contacts to have goons intimidate Hector and the police" if kiara.sub >= 50 and claire.sub >= 50 and cherie.sub >= 50:
                "What Claire and Cherie need is someone to step in here and take control."
                "And it needs to be me, before Kiara gets the idea she's the one calling the shots."
                mike.say "Kiara..."
                mike.say "Get me a couple of your most reliable goons."
                mike.say "We're going to have them make calls on Hector and a few police officers."
                "It looks to me like Kiara was about to make a suggestion of her own."
                show kiara dreaming
                "But the authority with which I'm speaking seems to cow her into submission."
                "Because she nods, making a point of not looking me in the eye."
                show kiara talkative
                kiara.say "Yes, [hero.name]…"
                kiara.say "I know just the men for the job."
                kiara.say "And I will personally guarantee their success."
                show claire pout
                show cherie annoyed
                "Claire and Cherie, on the other hand, aren't as easily convinced."
                show claire whining
                claire.say "You're not going to hurt Hector, are you?"
                claire.say "He looked so frail the last time I saw him!"
                show claire sad
                show cherie angry
                cherie.say "This is the police, [hero.name]…"
                cherie.say "Not some silly little punks!"
                show cherie upset
                "I hold up a hand and give them both a stern look."
                "Which is enough to silence them and give me back the upper hand."
                mike.say "I know what I'm doing, and I don't need you questioning me either."
                mike.say "Trust me, this will put a stop to all of the trouble you've been having."
    with fade
    "Once all of the plans have been finalised, Kiara orders another round of cocktails."
    play sfx1 wine_cheers
    pause 0.1
    play sfx2 glass_wine
    "And the four of us raise our glasses in a toast to each other."
    "Celebrating the triumph of our teamwork against the challenges we're facing."
    "And looking forward to seeing any and all threats neutralised for good."
    scene bg black with dissolve
    return

label milf_harem_event_05:
    scene bg beach with fade
    pause 0.5
    show claire swimsuit a pained at right with easeinright
    claire.say "Are we nearly there yet?"
    show claire sad
    show cherie swimsuit a angry at center with easeinright
    cherie.say "I cannot believe you will not say where we are going!"
    show cherie a annoyed
    show kiara swimsuit cringe at left with easeinright
    kiara.say "The reveal had better be worth the mystery, [hero.name]!"
    show kiara blank
    "Oh man, if only this were the first time that Claire, Cherie and Kiara had spoken up like that."
    "If that were the case, I could have just brushed it off and laughed - you know, played it cool?"
    "But the truth is that they've been bugging me almost since we set off on he journey to get here."
    "Foolish me, I thought that bringing the three of them on a mystery trip would be a great idea."
    "Turns out that they're all in the habit of acting like kids being dragged somewhere with their parents!"
    mike.say "Okay, how many times do I have to say it?"
    mike.say "The place we're headed to is just around the corner!"
    show claire pained
    claire.say "But you said that the last time!"
    show claire sad
    show cherie a talkative
    cherie.say "She is right, mon ami, you did."
    show cherie a annoyed
    show kiara angry
    kiara.say "How many more corners must we go around?"
    show kiara annoyed
    "I'm about to lose my temper and probably say something I'll regret at way too loud of a volume."
    "But luckily for me, fate intervenes just in time to prove me right for once."
    scene bg masterhouse with fade
    "As we round the corner to the sight of a pretty much perfect beach spreading out before us."
    mike.say "Just the one, apparently!"
    mike.say "There, you see?"
    mike.say "Now wasn't that worth the wait?!?"
    show claire swimsuit embarrassed at left
    show cherie b swimsuit stuned
    show kiara swimsuit stare at right
    with easeinleft
    "I'm momentarily irked as all three of the girls seem to suddenly forget that I even exist."
    "As they begin to gasp and coo at the sight of the place where we're going to be spending some time."
    "But then I suppose that I should see it as a blessing in disguise, as all the complaining stops in an instant."
    "And they all grab their bags, making a bee-line for the cute little cabana that overlooks the sand."
    show claire talkative
    claire.say "Ooh..."
    claire.say "Have you ever seen anything so great as that?"
    show claire normal
    show cherie a happy
    cherie.say "Not since I was sunning myself on the sands back home!"
    show cherie a smile
    show kiara talkative
    kiara.say "And we've got it all to ourselves!"
    show kiara normal
    "I watch with a growing feeling of pride as the girls hurry into the cabana and get settled in."
    "Giving myself a mental pat on the back as I gather up all the things they've forgotten."
    "Then I follow on behind, already looking forward to all the fun and frolics that lie ahead of us."
    "In fact I'm only halfway through doing that when the girls come streaming out again."
    "And the fact that they've already changed into their swimsuits makes me drop what I'm carrying."
    mike.say "Whoa..."
    mike.say "Wait a second, you guys..."
    mike.say "I thought we could spend some time settling in, you know?"
    mike.say "Like, see what the place is like and check out the facilities?"
    "The only response I get for my trouble is a volleyball tossed in my direction."
    show beach_volleyball_ball_front_03 at center, zoomAt(1.0, (720,650))
    show beach_volleyball_ball_front_03 at center, traveling(3.5, 0.15, (1420,2250))
    play sound punch_hard
    pause 0.1
    with hpunch
    "Which, as I'm totally unprepared, bounces off the side of my head."
    hide beach_volleyball_ball_front_03 with easeoutbottom
    mike.say "OUCH!"
    show claire talkative
    claire.say "Come on, [hero.name]…"
    claire.say "You can be on my team!"
    show claire normal
    show cherie a happy
    cherie.say "You may have him, Claire."
    show cherie a smile
    show kiara talkative
    kiara.say "That way it will be easier for us to win!"
    show kiara smile
    if kiara.sub <= -50:

        "I go to pick up the ball, but Kiara beats me to it."
        "And I stumble a little as she scoops it up and tosses it straight to Cherie."
        kiara.say "[hero.name] and Claire, over there..."
        kiara.say "Cherie and I will take this side of the court."
        cherie.say "And do try to keep up, mon ami!"
        scene bg black
        show beach_volleyball_bg_04
        show beach_volleyball_back_mc_04_mikemc at center, flip
        show beach_volleyball_back_mc_04_normal_mikemc at center, flip
        show beach_volleyball_front_claire at center, zoomAt(0.9, (660, 720))
        show beach_volleyball_swimsuit_claire at center, zoomAt(0.9, (660, 720))
        show beach_volleyball_nohaircut_claire at center, zoomAt(0.9, (660, 720))
        show beach_volleyball_net_04 at center, flip
        show beach_volleyball_ball_front_03 at center, zoomAt(1.0, (720,650))
        show beach_volleyball_front_cherie at flip, center, zoomAt(1.0, (340,720))
        show beach_volleyball_swimsuit_cherie at flip, center, zoomAt(1.0, (340,720))
        show beach_volleyball_haircut_cherie at flip, center, zoomAt(1.0, (340,720))
        show beach_volleyball_front_kiara at flip, center, zoomAt(1.0, (540,820))
        show beach_volleyball_swimsuit_kiara at flip, center, zoomAt(1.0, (540,820))
        show beach_volleyball_haircut_kiara at flip, center, zoomAt(1.0, (540,820))
        with fade
        "With that, Cherie launches the ball over the net."
        "And Claire and I do the best we can to chase after it."
        "The only problem is that we're like two random individuals on a pitch."
        "Whereas the other two are already working like a well oiled machine."
        "Together, Cherie and Kiara teach us a lesson about how the game should be played."
        "Scoring point after point, while Claire and I struggle not to run into each other."
    menu:
        "Try to make the game fun for everyone":
            "I grab the ball and wave for Claire to follow me."
            mike.say "Come on, Claire..."
            mike.say "Let's show them how a real team plays!"
            claire.say "Oh..."
            claire.say "Okay, [hero.name] - I'll do my best!"
            scene bg black
            show beach_volleyball_bg_04
            show beach_volleyball_back_mc_04_mikemc at center, flip
            show beach_volleyball_back_mc_04_normal_mikemc at center, flip
            show beach_volleyball_front_claire at center, zoomAt(0.9, (660, 720))
            show beach_volleyball_swimsuit_claire at center, zoomAt(0.9, (660, 720))
            show beach_volleyball_nohaircut_claire at center, zoomAt(0.9, (660, 720))
            show beach_volleyball_net_04 at center, flip
            show beach_volleyball_ball_front_03 at center, zoomAt(1.0, (720,650))
            show beach_volleyball_front_cherie at flip, center, zoomAt(1.0, (340,720))
            show beach_volleyball_swimsuit_cherie at flip, center, zoomAt(1.0, (340,720))
            show beach_volleyball_haircut_cherie at flip, center, zoomAt(1.0, (340,720))
            show beach_volleyball_front_kiara at flip, center, zoomAt(1.0, (540,820))
            show beach_volleyball_swimsuit_kiara at flip, center, zoomAt(1.0, (540,820))
            show beach_volleyball_haircut_kiara at flip, center, zoomAt(1.0, (540,820))
            with fade
            "Claire runs after me onto the sand and we take up our positions."
            "Cherie and Kiara line up on the other side of the net."
            "And then I fire the ball over the net at them."
            "What follows is a pretty intense game of volleyball."
            "With both sides pulling ahead of the other at different points."
            "But in the end, it's Cherie and Kiara that start to pull ahead."
        "Dominate the game" if hero.fitness >= 75:
            "I grab the ball and stride onto the pitch."
            "Leaving the others to hurry after me."
            mike.say "Claire, you go here..."
            mike.say "Cherie and Kiara, there and there."
            "Left with no other choice, the girls scramble to obey."
            scene bg black
            show beach_volleyball_bg_04
            show beach_volleyball_back_mc_04_mikemc at center, flip
            show beach_volleyball_back_mc_04_normal_mikemc at center, flip
            show beach_volleyball_front_claire at center, zoomAt(0.9, (660, 720))
            show beach_volleyball_swimsuit_claire at center, zoomAt(0.9, (660, 720))
            show beach_volleyball_nohaircut_claire at center, zoomAt(0.9, (660, 720))
            show beach_volleyball_net_04 at center, flip
            show beach_volleyball_ball_front_03 at center, zoomAt(1.0, (720,650))
            show beach_volleyball_front_cherie at flip, center, zoomAt(1.0, (340,720))
            show beach_volleyball_swimsuit_cherie at flip, center, zoomAt(1.0, (340,720))
            show beach_volleyball_haircut_cherie at flip, center, zoomAt(1.0, (340,720))
            show beach_volleyball_front_kiara at flip, center, zoomAt(1.0, (540,820))
            show beach_volleyball_swimsuit_kiara at flip, center, zoomAt(1.0, (540,820))
            show beach_volleyball_haircut_kiara at flip, center, zoomAt(1.0, (540,820))
            with fade
            "And once I'm happy with the positions they're in, I get things started."
            "Launching the ball over the net with authority and making the others flinch."
            "What follows is an authoritative lesson in how the game should be played."
            "One in which I school Cherie and Kiara with blistering shots."
            "As well as making Claire work hard to keep up with me too."
            "And it's no great surprise for me to find out that they just can't keep up."
    claire.say "Oh no..."
    claire.say "I forgot to put on sun-screen..."
    claire.say "I'm going to burn to a crisp!"
    "Almost as soon as Claire says the words, the game comes to an abrupt end."
    scene bg masterhouse with fade
    pause 0.3
    show claire swimsuit sadsmile at center, zoomAt(1.0, (340, 720))
    show cherie a swimsuit sadsmile at center, zoomAt(1.0, (640, 720))
    show kiara swimsuit sadsmile at center, zoomAt(1.0, (940, 720))
    with easeinright
    "With all three of the girls dashing off the court and searching for their sun-screen."
    show cherie whining at startle(0.1, -5)
    cherie.say "Me too!"
    show cherie sadsmile
    show kiara talkative at startle(0.1, -5)
    kiara.say "How could we forget?"
    show kiara sadsmile
    "I get the pleasure of watching the show as the girls all begin squeezing out sun-screen."
    "And then struggling to get it into all of the hard to reach parts of their bodies."
    "I honestly think they could have managed it themselves without my involvement."
    "But they're so flustered and desperate to avoid getting burnt, they can't seem to concentrate."
    "And all it need is a little bit of gentle encouragement to plant the notion in their minds."
    mike.say "Whoops - you missed a bit!"
    show claire whining zorder 3 at center, traveling(1.25, 0.5, (340, 880))
    claire.say "Where...where?"
    show claire sadsmile
    mike.say "I'd give that a second going over, if I were you."
    show cherie whining zorder 1 at center, traveling(1.25, 0.5, (640, 880))
    cherie.say "Mon dieu!"
    show cherie sadsmile
    mike.say "Man, it's SO hard to reach the bottom of such long legs!"
    show kiara whining zorder 2 at center, traveling(1.25, 0.5, (940, 880))
    kiara.say "Especially with these short arms!"
    show kiara sadsmile
    "Within a very short time I have three tubes of sun-screen being shoved in my face."
    "And the three of them desperately pointing to the curves and lines of their almost naked bodies."
    "So what else is a guy supposed to do?"
    if cherie.sub <= -25 and kiara.sub <= -25:

        show cherie talkative at startle(0.1, -5)
        cherie.say "I will take this spot here."
        cherie.say "Kiara the one to my side."
        cherie.say "Claire, you will go here."
        show cherie normal
        show claire normal
        show kiara talkative at startle(0.1, -5)
        kiara.say "[hero.name], you will work in this precise order."
        kiara.say "And you will not move on to the next part until we are satisfied!"
        show kiara normal
        mike.say "Y...yes, sir..."
        mike.say "I mean...yes, madam!"
        scene bg black
        show beach_cream_bg_01
        show beach_cream_npc_claire at center, zoomAt(1.0, (460, 720))
        show beach_cream_top_claire_swimsuit at center, zoomAt(1.0, (460, 720))
        show beach_cream_haircuts_claire_nohaircut at center, zoomAt(1.0, (460, 720))
        show beach_cream_npc_cherie at center, zoomAt(1.0, (880, 720))
        show beach_cream_top_cherie_swimsuit at center, zoomAt(1.0, (880, 720))
        show beach_cream_haircuts_cherie_nohaircut at center, zoomAt(1.0, (880, 720))
        show beach_cream_npc_kiara at center, zoomAt(1.0, (1140, 720))
        show beach_cream_top_kiara_swimsuit at center, zoomAt(1.0, (1140, 720))
        show beach_cream_haircuts_kiara_nohaircut at center, zoomAt(1.0, (1140, 720))
        show beach_cream_mikemc_right_01 at center, zoomAt(1.0, (1160, 720))
        show beach_cream_mchands_right_01 at center, zoomAt(1.0, (1160, 720))
        with fade
        "The girls settle down on the sand in front of me, stretching out casually."
        "While I hurry to squeeze sun-screen onto the palms of my hands."
        "And then I set to work, systematically topping up their cover from head to toe."
        "But don't let the fact that Cherie and Kiara are calling the shots fool you."
        "I'm really having the time of my life doing this."
        "Claire, Cherie and Kiara all do the best they can to keep still and quiet too."
        "The one that's getting my attentions chuckling and giggling at my touch."
        "While the other two visibly pout and look on enviously, waiting for their turn."
        "By now I feel like I'm reaching a higher plane."
        "Rubbing myself into a slippery state of nirvana."
        $ claire.sub += 2
        $ cherie.sub -= 2
        $ kiara.sub -= 2
    menu:
        "Apply sun-screen to all the girls equally":
            "So with a resigned nod, I pluck the sun-screen out of their hands."
            "And then I gesture for them to lie down in front of me on the sand."
            scene bg black
            show beach_cream_bg_01
            show beach_cream_npc_claire at center, zoomAt(1.0, (460, 720))
            show beach_cream_top_claire_swimsuit at center, zoomAt(1.0, (460, 720))
            show beach_cream_haircuts_claire_nohaircut at center, zoomAt(1.0, (460, 720))
            show beach_cream_npc_cherie at center, zoomAt(1.0, (880, 720))
            show beach_cream_top_cherie_swimsuit at center, zoomAt(1.0, (880, 720))
            show beach_cream_haircuts_cherie_nohaircut at center, zoomAt(1.0, (880, 720))
            show beach_cream_npc_kiara at center, zoomAt(1.0, (1140, 720))
            show beach_cream_top_kiara_swimsuit at center, zoomAt(1.0, (1140, 720))
            show beach_cream_haircuts_kiara_nohaircut at center, zoomAt(1.0, (1140, 720))
            show beach_cream_mikemc_right_01 at center, zoomAt(1.0, (1160, 720))
            show beach_cream_mchands_right_01 at center, zoomAt(1.0, (1160, 720))
            with fade
            "Claire, Cherie and Kiara hurry to do as they're told."
            "So soon enough, I have three exquisite bodies spread out before me."
            claire.say "Do me first, [hero.name]!"
            cherie.say "Do not linger too long on her, mon ami!"
            kiara.say "If you do, we will all burn up in the sun!"
            "Oh, the terrible chores of being me!"
            "With their pleas still ringing in my ears, I set to work."
            "Doing all that I can to cover Claire in sun-screen."
            "But at the same time trying to make sure I enjoy the task too."
            "And just as I'm getting into it, I find that I've covered the last spot."
            claire.say "That feels so good!"
            cherie.say "Quickly, [hero.name] - me next!"
            "In a flash my hands are all over Cherie, stroking her body."
            "Rubbing the sun-screen into every last nook and cranny."
            "The pleasure of the task returning once more."
            "And yet it's just as quickly over this time too."
            cherie.say "All done, mon ami!"
            kiara.say "Hurry, [hero.name] - I can feel myself burning!"
            "Just like that I'm repeating the same routine on Kiara."
            "Fingers massaging and palms rubbing the sun-screen into her skin."
            "By now I feel like I'm reaching a higher plane."
            "Rubbing myself into a slippery state of nirvana."
            $ claire.love += 2
            $ cherie.love += 2
            $ kiara.love += 2
        "Order the girls to line up and doles out the sun-screen as you see fit" if claire.sub >= 25 and cherie.sub >= 25 and kiara.sub >= 25:
            mike.say "Okay..."
            mike.say "Sun-screen here."
            "I point to the sand at my side."
            mike.say "And your butts here, here and here!"
            "Then I point to three spots in front of me."
            "And I cross my arms over my chest, making it clear that's going to be my last instruction."
            scene bg black
            show beach_cream_bg_01
            show beach_cream_npc_claire at center, zoomAt(1.0, (460, 720))
            show beach_cream_top_claire_swimsuit at center, zoomAt(1.0, (460, 720))
            show beach_cream_haircuts_claire_nohaircut at center, zoomAt(1.0, (460, 720))
            show beach_cream_npc_cherie at center, zoomAt(1.0, (880, 720))
            show beach_cream_top_cherie_swimsuit at center, zoomAt(1.0, (880, 720))
            show beach_cream_haircuts_cherie_nohaircut at center, zoomAt(1.0, (880, 720))
            show beach_cream_npc_kiara at center, zoomAt(1.0, (1140, 720))
            show beach_cream_top_kiara_swimsuit at center, zoomAt(1.0, (1140, 720))
            show beach_cream_haircuts_kiara_nohaircut at center, zoomAt(1.0, (1140, 720))
            show beach_cream_mikemc_right_01 at center, zoomAt(1.0, (1160, 720))
            show beach_cream_mchands_right_01 at center, zoomAt(1.0, (1160, 720))
            with fade
            "Then I get to stand back and watch as the girls all hurry to do as they're told."
            "Hastily dropping their tubes of sunscreen next to me and then assuming their spots."
            "One delightful body spreading out on the sand beside the next."
            "All waiting for the sun-screen to be applied by my own two hands."
            "Okay, this might seem a little controlling to the casual observer."
            "But you have no idea how much fun it is to get that sun-screen on my hands."
            "And the to be able to choose exactly where I start and what gets rubbed in where!"
            "Claire, Cherie and Kiara all do the best they can to keep still and quiet too."
            "The one that's getting my attentions chuckling and giggling at my touch."
            "While the other two visibly pout and look on enviously, waiting for their turn."
            "By now I feel like I'm reaching a higher plane."
            "Rubbing myself into a slippery state of nirvana."
            $ claire.sub += 2
            $ cherie.sub += 2
            $ kiara.sub += 2
    "I'm just about done with working the last of the sun-screen into Kiara's shoulders."
    scene bg masterhouse with fade
    "And by now the sun is starting to sink towards the far line of the horizon."
    "Spreading it's light across the water of the sea and painting the view as it does so."
    "I can't really explain how it happens, I guess I must have become distracted."
    show kiara naked smile at center, zoomAt(1.5, (940, 1080)) with easeinbottom
    "But when I look down, one of the straps of Kiara's swimming costume has fallen down."
    "It's hooked around my fingers, leaving one of her breasts exposed for everyone to see."
    show kiara talkative
    kiara.say "[hero.name]…"
    kiara.say "You wicked beast of a man..."
    kiara.say "Look at what you've gone and done!"
    show kiara mischievous
    "I back off a little at first, thrown by Kiara's accusations."
    "But then I see the twinkle of mischief in her eyes."
    cherie.say "You think that is bad, mon ami?"
    cherie.say "Look at the state he has left me in!"
    show cherie naked smile at center, zoomAt(1.5, (640, 1080)) with easeinbottom
    "At the sound of Cherie's voice, I look around."
    "Only to be greeted with the sight of her own swimming costume pulled down to her waist!"
    claire.say "Well what about me?"
    claire.say "Mine just up and fell off of me!"
    show claire naked sadsmile at center, zoomAt(1.5, (340, 1080)) with easeinbottom
    "My head snaps around again, this time to look at Claire."
    "And I see her drop her swimming costume onto the sand."
    "As she lies there totally naked, yet trying to look completely innocent at the same time."
    show kiara talkative
    kiara.say "We should have our revenge on him, shouldn't we?"
    show kiara flirt
    show cherie happy
    cherie.say "Give him a taste of his own medicine, perhaps?"
    show cherie normal
    show claire talkative
    claire.say "Yeah, let's get him!"
    show claire happy
    "As one, the three of them pounce on me."
    with vpunch
    "Pinning me down as they pull down my own shorts then toss them away."
    "Not that I mind in the slightest, because by now the mood has definitely shifted."
    "And there's only one direction things are going to go from here!"

    "For a moment I'm faced with what seems like an unsolvable dilemma."
    "There are three of them getting naked with me on the beach right now."
    "So how in the hell am I supposed to please them all?"
    "After all, I only have one cock!"
    "But then it occurs to me that there are other ways of getting off."
    "And ways that can involve more than one pair of hands too."
    "So sitting up on the sand, I nod my head downwards."
    mike.say "You guys fancy a challenge?"
    show claire talkative
    claire.say "Oh..."
    claire.say "What do you mean by that?"
    show claire normal
    show cherie talkative
    cherie.say "Whatever it is, I think it involves his manhood!"
    show cherie normal
    show kiara talkative
    kiara.say "I know that we are equal to anything involving that!"
    show kiara normal
    mike.say "Is that so, Kiara?"
    mike.say "Well why don't we see if you can work together?"
    mike.say "If the three of you can use your mouths for something other than talk!"
    "I deliberately make the challenge a provocative one."
    "Knowing that Cherie and Kiara will be sure to rise to it."
    "That they will encourage Claire to join in too."
    scene bg black
    show milf 4some blowjob beach
    with fade
    "And it doesn't take long for me to be proven right."
    "As the three of them slither towards me like a trio of sexy serpents."
    "Quick as a flash, Kiara darts to my left, pinning down my leg on that side."
    "Claire mirrors her movements on the right, if a little slower on her part."
    "At the same time, Cherie crawls between my legs and straight towards my groin."
    "It looks to me like she's going to the one that takes the lead."
    "And my suspicions are confirmed when she lowers her head and parts her lips."
    "She takes the tip into her mouth, kissing it delicately to begin with."
    "Then teasing it with the tip of her tongue to intensify the sensation."
    show milf 4some blowjob claire_suck
    "Kiara and Claire add to the experience by going lower still."
    show milf 4some blowjob kiara_suck
    "And soon enough, each of them is sucking on one of my balls."
    "Somehow working in sympathy with Cherie above them too."
    play sexsfx1 bj_sucking loop
    show milf 4some blowjob cherie_suck at startle(0.05,-10)
    "As if sensing the effect they're having, Cherie takes me deeper."
    "Slowly inching the shaft of my cock into her mouth and the tip towards her throat."
    "All the while she keeps on working away, kissing and caressing."
    "My entire body tenses and relaxes according to her attentions."
    show milf 4some blowjob at startle(0.05,-10)
    "And I can't help sinking my hands into the sand, clenching handfuls of the stuff."
    "As if doing so will somehow help to release the tension building up inside of me."
    "It feels like a kind of torture, and yet I want it more than anything I can imagine."
    "I gasp, my head swimming as Kiara and Claire rise up from below."
    show milf 4some blowjob cherie_lick at startle(0.05,-10)
    "And Cherie smoothly releases me from her mouth, my cock sliding free."
    "Before I can let out a moan of disappointment, Kiara takes her place."
    "Now it's in her mouth, and she's making me feel more helpless than ever."
    "All I can do is watch as Claire takes her turn next, just as seamlessly."
    show milf 4some blowjob cherie_suck at startle(0.05,-10)
    "Without a word, the three of them pass me between their lips."
    "Each change pushing me further over the edge and making me ever more helpless."
    show milf 4some blowjob at startle(0.05,-10)
    "Soon enough there's nothing I can do to resist the pull of it."
    "And I just know that I'm going to shoot my load."
    menu:
        "Triple facial":
            "The girls seem to know exactly what's happening."
            play sexsfx1 slide_out
            show milf 4some blowjob cherie_lick claire_lick kiara_lick
            "As they resume their former positions, leaving my cock to bob in front of them."
            play sexsfx1 cum_outside
            show milf 4some blowjob cum with vpunch
            "And when it finally happens, none of them flinch or move as much as an inch."
            play sexsfx1 cum_outside
            show milf 4some blowjob facecum_cherie with vpunch
            "They just smile and close their eyes, keeping their mouths open."
            play sexsfx1 cum_outside
            show milf 4some blowjob facecum_kiara with vpunch
            "Letting me spatter them with strings of warm, white cum."
            show milf 4some blowjob -cum facecum_claire with vpunch
            "Enjoying the results of all the hard work they just put in to get here."
            $ cherie.love += 1
            $ claire.love += 1
            $ kiara.love += 1
            if hero.stamina:
                call milf_fuck from _call_milf_fuck
            else:
                call milf_after_beach_sex from _call_milf_after_beach_sex
        "Make Cherie swallow":







            "I could shoot it into the faces of all three of them."
            "But for some reason I can't explain, I want Cherie to swallow."
            show milf 4some blowjob at startle(0.05,-10)
            "And so at the last possible moment, I reach out and pull her forwards."
            play sexsfx1 bj_gulp
            show milf 4some blowjob cum with vpunch
            "She seems to know what I'm doing, leaning in and taking me into her mouth."
            show milf 4some blowjob claire_lick kiara_lick with vpunch
            "Claire and Kiara look on, unable to hide their envy."
            with vpunch
            "But I'm too wrapped up in the sensation of Cherie gulping down every last drop to do a thing about it."
            $ cherie.love += 2
            if hero.stamina:
                call milf_fuck from _call_milf_fuck_1
            else:
                call milf_after_beach_sex from _call_milf_after_beach_sex_1
        "Hold it in":







            "No, I don't want this thing to end just yet."
            "I think that if I...just concentrate hard enough..."
            play sexsfx1 slide_out
            "Somehow, through sheer force of will, I manage to make my body obey me."
            "Fighting down the need to cum and suppressing it so that we can keep on going."

label milf_fuck:
    mike.say "Okay, girls..."
    mike.say "What's next?"
    menu:
        "Fuck Claire":
            "How in the hell am I supposed to choose between the three of them?"
            "That feels like an impossible choice for me to be forced to make."
            "At least until my eyes meet Claire's, and it's all decided for me."
            "For some reason I can't help myself, I just know it's got to be her."
            "And she seems to realise it as soon as I reach out a hand in her direction."
            scene bg black
            show milf 4some fuckclaire beach
            with fade
            "Claire instantly takes it, sliding across my thighs with her back to me."
            "Cherie and Kiara look a little disappointed for a moment."
            "But then the same weird spell seems to settle over them too."
            "And instead of objecting, they help to support Claire as she gets into position."
            "Looking back over her shoulder, Claire reaches down between my legs."
            "And I let out a gasp as she takes hold of my cock."
            "Not because her touch is rough, but because I'm so tensed for what's about to happen."
            show milf 4some fuckclaire claire_happy
            claire.say "Oh, [hero.name]…"
            claire.say "What do you want?"
            claire.say "Where do you want me to put it?"
            show milf 4some fuckclaire claire_normal
            menu:
                "Fuck Claire's pussy":
                    mike.say "Ah..."
                    mike.say "Pussy, Claire..."
                    mike.say "Please, put it in your pussy!"
                    "I see desire and genuine need flash in Claire's eyes as I tell her what I want."
                    "And when she nods, turning her head back to face forwards, I almost hold my breath."
                    "Because the knowledge that she wants this as much as I do is an incredible turn-on."
                    "But everything else disappears from my mind the moment that Claire starts to move."
                    "In that moment I feel her pressing my cock hard against her pussy as she rises and falls."
                    "And I can tell instantly just how hot, wet and needy already is."
                    "So much so that it feels like the lips of her pussy are melting."
                    "I can't remember her ever being this aroused before now, this desperate."
                    "She's using both of her hands to hold the head of my cock against herself right now."
                    "Almost all of her weight pressing down on it as she forces her body to submit."
                    "And thanks to the fact that she's already so far gone, it doesn't take all that much."
                    show milf 4some fuckclaire claire_pleasure
                    claire.say "Oooh…"
                    claire.say "Oh fuck..."
                    show milf 4some fuckclaire claire_normal
                    "Claire slowly begins to sink downwards as her lips fully part."
                    play sexsfx1 slide_in
                    show milf 4some fuckclaire vaginal at startle(0.05,-10)
                    "Moving at an achingly gradual pace, she takes me inside of her."
                    "Hands shifting to my thighs, she controls her descent perfectly."
                    "Meaning that I feel every second of it with exquisite intensity."
                    show milf 4some fuckclaire claire_pleasure
                    claire.say "Oh, [hero.name]…"
                    claire.say "You're just so...so big!"
                    show milf 4some fuckclaire claire_normal
                    play sexsfx1 fuck_calm
                    "I hear Claire starting to chuckle with pleasure as she begins to ride me."
                    "And I can't possibly describe how much of a turn-on the sound is to my ears."
                    "Even with my cock buried as deep into her as it will go, it still adds to the sensation."
                    "Until now, Cherie and Kiara have been happy to sit on the side-lines and just watch."
                    "But I notice a hand creeping into view, sliding up Claire's left leg."
                    "I watch with genuine fascination as it arrives at the top and reaches her buttock."
                    "And then it starts to squeeze, making her buck and shiver, pushing down even harder."
                    "Somehow I manage to cast my eyes to the side, where I see the arm is attached to Kiara's arm."
                    "She and Cherie are locked together in a tight embrace, kissing and caressing each other."
                    "But still she's managing to get involved in what Claire and I are doing right now!"
                    play sexsfx1 fuck_speed
                    show milf 4some fuckclaire at startle(0.05,-10)
                    pause 0.2
                    show milf 4some fuckclaire at startle(0.05,-10)
                    "All this time I've been thrusting up as Claire's been pushing down."
                    "Yet the sudden upturn in intensity means that I've now picked up the pace."
                    show milf 4some fuckclaire at startle(0.05,-10)
                    pause 0.2
                    show milf 4some fuckclaire at startle(0.05,-10)
                    "Grabbing a firm hold of Claire myself, I thrust myself as deep into her as I possibly can."
                    "Each time I do so pushing the both of us ever closer to the edge of cuming."
                    play sexsfx1 fuck_sprint
                    show milf 4some fuckclaire at startle(0.05,-10)
                    pause 0.2
                    show milf 4some fuckclaire claire_pleasure at startle(0.05,-10)
                    "It's Claire that surrenders first, throwing her head back and wailing."
                    "But as she does so, I feel the muscles of her body squeeze me harder then ever."
                    show milf 4some fuckclaire at startle(0.05,-10)
                    pause 0.2
                    show milf 4some fuckclaire at startle(0.05,-10)
                    "And no more than a few seconds later, I'm following her lead."
                    menu:
                        "Cum inside of pussy":
                            "Unable to control myself any longer, I surrender to the inevitable."
                            play sexsfx1 cum_inside
                            show milf 4some fuckclaire cum with vpunch
                            "Shooting my load inside of Claire as feeling the sensation of relief that comes with it."
                            with vpunch
                            "Now we're both gasping, utterly wiped out by the release of all that energy."
                            with vpunch
                            "And more than ready to collapse into a helpless heap on the sand."
                        "Pull out of pussy":
                            "I use the last of my strength to pull backwards before it happens."
                            play sexsfx1 slide_out
                            show milf 4some fuckclaire out with vpunch
                            "Sliding all the way out of Claire the moment before I lose it."
                            play sexsfx1 cum_outside
                            show milf 4some fuckclaire cum with vpunch
                            "She moans softly as I shoot my load over her back and buttocks."
                            show milf 4some fuckclaire -cum bodycum with vpunch
                            "More than ready to collapse into a helpless heap on the sand."
                "Fuck Claire's ass":






                    mike.say "Ah..."
                    mike.say "Ass, Claire..."
                    mike.say "Please, put it in your ass!"
                    "I see desire and genuine need flash in Claire's eyes as I tell her what I want."
                    "And when she nods, turning her head back to face forwards, I almost hold my breath."
                    "Because the knowledge that she wants this as much as I do is an incredible turn-on."
                    "But everything else disappears from my mind the moment that Claire starts to move."
                    "In that moment I feel her pressing my cock hard between her cheeks as she rises and falls."
                    "And I can tell instantly just how hot, soft and needy already is."
                    "So much so that it feels like the muscles of her ass are melting."
                    "I can't remember her ever being this aroused before now, this desperate."
                    "She's using both of her hands to hold the head of my cock against herself right now."
                    "Almost all of her weight pressing down on it as she forces her body to submit."
                    "And thanks to the fact that she's already so far gone, it doesn't take all that much."
                    show milf 4some fuckclaire claire_pleasure
                    claire.say "Oooh…"
                    claire.say "Oh fuck..."
                    show milf 4some fuckclaire claire_normal
                    "Claire slowly begins to sink downwards as her muscles fully relax."
                    play sexsfx1 slide_in
                    show milf 4some fuckclaire anal at startle(0.05,-10)
                    "Moving at an achingly gradual pace, she takes me inside of her."
                    "Hands shifting to my thighs, she controls her descent perfectly."
                    "Meaning that I feel every second of it with exquisite intensity."
                    show milf 4some fuckclaire claire_pleasure
                    claire.say "Oh, [hero.name]…"
                    claire.say "You're just so...so big!"
                    show milf 4some fuckclaire claire_normal
                    play sexsfx1 fuck_calm
                    "I hear Claire starting to chuckle with pleasure as she begins to ride me."
                    "And I can't possibly describe how much of a turn-on the sound is to my ears."
                    "Even with my cock buried as deep into her as it will go, it still adds to the sensation."
                    "Until now, Cherie and Kiara have been happy to sit on the side-lines and just watch."
                    "But I notice a hand creeping into view, sliding up Claire's left leg."
                    "I watch with genuine fascination as it arrives at the top and reaches her buttock."
                    "And then it starts to squeeze, making her buck and shiver, pushing down even harder."
                    "Somehow I manage to cast my eyes to the side, where I see the arm is attached to Kiara's arm."
                    "She and Cherie are locked together in a tight embrace, kissing and caressing each other."
                    "But still she's managing to get involved in what Claire and I are doing right now!"
                    play sexsfx1 fuck_speed
                    show milf 4some fuckclaire at startle(0.05,-10)
                    pause 0.2
                    show milf 4some fuckclaire at startle(0.05,-10)
                    "All this time I've been thrusting up as Claire's been pushing down."
                    "Yet the sudden upturn in intensity means that I've now picked up the pace."
                    show milf 4some fuckclaire at startle(0.05,-10)
                    pause 0.2
                    show milf 4some fuckclaire at startle(0.05,-10)
                    "Grabbing a firm hold of Claire myself, I thrust myself as deep into her as I possibly can."
                    "Each time I do so pushing the both of us ever closer to the edge of cuming."
                    play sexsfx1 fuck_sprint
                    show milf 4some fuckclaire at startle(0.05,-10)
                    pause 0.2
                    show milf 4some fuckclaire claire_pleasure at startle(0.05,-10)
                    "It's Claire that surrenders first, throwing her head back and wailing."
                    "But as she does so, I feel the muscles of her body squeeze me harder then ever."
                    show milf 4some fuckclaire at startle(0.05,-10)
                    pause 0.2
                    show milf 4some fuckclaire at startle(0.05,-10)
                    "And no more than a few seconds later, I'm following her lead."
                    menu:
                        "Cum inside of ass":
                            "Unable to control myself any longer, I surrender to the inevitable."
                            play sexsfx1 cum_inside
                            show milf 4some fuckclaire cum with vpunch
                            "Shooting my load inside of Claire's ass as feeling the sensation of relief that comes with it."
                            with vpunch
                            "Now we're both gasping, utterly wiped out by the release of all that energy."
                            with vpunch
                            "And more than ready to collapse into a helpless heap on the sand."
                        "Pull out of ass":
                            "I use the last of my strength to pull backwards before it happens."
                            play sexsfx1 pop_out
                            show milf 4some fuckclaire out with vpunch
                            "Sliding all the way out of Claire's ass the moment before I lose it."
                            play sexsfx1 cum_outside
                            show milf 4some fuckclaire cum with vpunch
                            "She moans softly as I shoot my load over her back and buttocks."
                            show milf 4some fuckclaire -cum bodycum with vpunch
                            "More than ready to collapse into a helpless heap on the sand."
        "Fuck Cherie":






            "How in the hell am I supposed to choose between the three of them?"
            "That feels like an impossible choice for me to be forced to make."
            "At least until my eyes meet Cherie's, and it's all decided for me."
            "For some reason I can't help myself, I just know it's got to be her."
            "And she seems to realise it as soon as I reach out a hand in her direction."
            "Cherie instantly takes it, letting me guide her down and onto her back."
            "Claire and Kiara look a little disappointed for a moment."
            "But then the same weird spell seems to settle over them too."
            "And instead of objecting, they help to support Cherie as she gets into position."
            "Kiara placing herself behind Cherie and propping the other woman's shoulders up on her own knees."
            "Claire comes to my right side and Cherie's left, lifting her legs into the air."
            scene bg black
            show milf 4some fuckcherie beach
            with fade
            "All of which means I have complete access to Cherie as she lays before me."
            "A fact that must be all too apparent to her, as she looks up at me without a hint of resistance in her eyes."
            cherie.say "I am at your mercy, mon ami…"
            cherie.say "So I must ask, what is your pleasure?"
            cherie.say "How will you choose to use me?"
            menu:
                "Fuck Cherie's pussy":
                    "The position that Cherie's in right now means that I have two obvious choices."
                    "And the mood that the sight of her is getting me in means that it's going to be a simple one too."
                    "I can actually see the light of the sun, making Cherie's pussy glisten invitingly."
                    "So there's no chance of me choosing to put it anywhere else."
                    "But all the same, it's not like I make a point of telling her where it's going."
                    show milf 4some fuckcherie at stepback(speed=0.1, h=-10, v=0)
                    "Instead I simply lean in, aiming the head of my cock for those slick lips."
                    "And the first thing that Cherie knows about it is the sensation of it sliding along them."
                    cherie.say "Oh..."
                    cherie.say "Oh yes..."
                    cherie.say "Just like that!"
                    "Cherie nods eagerly, straining to look down and see what's happening between her thighs."
                    "Though I'm not in the mood to slow down and let her get a blow by blow view of it."
                    play sexsfx1 fuck_calm loop
                    show milf 4some fuckcherie at stepback(speed=0.1, h=-10, v=0)
                    "Already the head of my cock is going up and down with increasing speed."
                    "Sliding smoothly between the folds of Cherie's pussy and making her moan."
                    show milf 4some fuckcherie at stepback(speed=0.1, h=-10, v=0)
                    "Every pass makes it feel to me as if she's getting softer and more relaxed."
                    "Each one a small degree towards achieving my ultimate goal of getting inside of her."
                    cherie.say "Ah..."
                    cherie.say "That is right, mon ami…"
                    cherie.say "Make me yours!"
                    "For the first time since we started going at it, I find myself looking up at Cherie."
                    "Because her voice seems to be getting louder each and every time she speaks."
                    "And while we're on a pretty deserted stretch of beach, there's still a limit."
                    "The last thing I want is for someone to come wandering over after hearing her cries."
                    "A fear that gets even more pressing as things progress while my attention is elsewhere."
                    play sexsfx1 slide_in
                    show milf 4some fuckcherie vaginal at stepback(speed=0.1, h=-10, v=0)
                    "All of a sudden, Cherie's pussy stops resisting, and I feel myself slide all the way inside."
                    "And I can be sure that she feels it to, as she starts to gasp and cry out."
                    cherie.say "MON DIEU!"
                    cherie.say "MON DIEU!"
                    cherie.say "Mmmm...mmmph!"
                    "Cherie's exclamations suddenly become muffled mumbles instead."
                    "Because Kiara places a hand neatly over her mouth, effectively muting them."
                    "I don't need to be told to take advantage of the chance this gives me."
                    play sexsfx1 fuck_moderate loop
                    show milf 4some fuckcherie at stepback(speed=0.07, h=-10, v=0)
                    pause 0.2
                    show milf 4some fuckcherie at stepback(speed=0.07, h=-10, v=0)
                    "Instantly picking up the pace and starting to plough into Cherie."
                    "Which only makes her wriggle and writhe all the more as a result."
                    "Where before Kiara and Claire were just holding Cherie up, now they're holding her down."
                    play sexsfx1 fuck_speed loop
                    show milf 4some fuckcherie at stepback(speed=0.07, h=-10, v=0)
                    pause 0.2
                    show milf 4some fuckcherie at stepback(speed=0.07, h=-10, v=0)
                    "Gripping her tightly as I really get into my stride and begin to set the pace."
                    "Everything seems to speed up now, and to become more impactful too."
                    show milf 4some fuckcherie at stepback(speed=0.07, h=-10, v=0)
                    pause 0.2
                    show milf 4some fuckcherie at stepback(speed=0.07, h=-10, v=0)
                    "As if time and all the forces involved are becoming ever more concentrated."
                    "And so it comes as no surprise to me that I can feel myself on the verge of cuming."
                    menu:
                        "Cum inside of pussy":
                            "Unable to control myself any longer, I surrender to the inevitable."
                            play sexsfx1 cum_inside
                            show milf 4some fuckcherie cum with hpunch
                            "Shooting my load inside of Cherie as feeling the sensation of relief that comes with it."
                            with hpunch
                            "And the others release her from their grasp at the same time letting her flop backwards."
                            with hpunch
                            "And more than ready to collapse into a helpless heap on the sand."
                        "Pull out of pussy":
                            "I use the last of my strength to pull backwards before it happens."
                            play sexsfx1 slide_out
                            show milf 4some fuckcherie out with hpunch
                            "Sliding all the way out of Cherie the moment before I lose it."
                            play sexsfx1 cum_outside
                            show milf 4some fuckcherie cum with hpunch
                            "She moans softly as I shoot my load over her back and buttocks."
                            with hpunch
                            "And the others release her from their grasp at the same time letting her flop backwards."
                            with hpunch
                            "And more than ready to collapse into a helpless heap on the sand."
                "Fuck Cherie's ass":






                    "The position that Cherie's in right now means that I have two obvious choices."
                    "And the mood that the sight of her is getting me in means that it's going to be a simple one too."
                    "I can actually see the light of the sun, shining off the curve of Cherie's ass."
                    "So there's no chance of me choosing to put it anywhere else."
                    "But all the same, it's not like I make a point of telling her where it's going."
                    show milf 4some fuckcherie at stepback(speed=0.1, h=-10, v=0)
                    "Instead I simply lean in, aiming the head of my cock at the crack of her butt."
                    "And the first thing that Cherie knows about it is the sensation of it sliding between her buttocks."
                    cherie.say "Oh..."
                    cherie.say "Oh yes..."
                    cherie.say "Just like that!"
                    "Cherie nods eagerly, straining to look down and see what's happening between her thighs."
                    "Though I'm not in the mood to slow down and let her get a blow by blow view of it."
                    play sexsfx1 fuck_calm loop
                    show milf 4some fuckcherie at stepback(speed=0.1, h=-10, v=0)
                    "Already the head of my cock is going up and down with increasing speed."
                    "Sliding smoothly between the cheeks of Cherie's ass and making her moan."
                    show milf 4some fuckcherie at stepback(speed=0.1, h=-10, v=0)
                    "Every pass makes it feel to me as if she's getting softer and more relaxed."
                    "Each one a small degree towards achieving my ultimate goal of getting inside of her."
                    cherie.say "Ah..."
                    cherie.say "That is right, mon ami…"
                    cherie.say "Make me yours!"
                    "For the first time since we started going at it, I find myself looking up at Cherie."
                    "Because her voice seems to be getting louder each and every time she speaks."
                    "And while we're on a pretty deserted stretch of beach, there's still a limit."
                    "The last thing I want is for someone to come wandering over after hearing her cries."
                    "A fear that gets even more pressing as things progress while my attention is elsewhere."
                    play sexsfx1 slide_in
                    show milf 4some fuckcherie anal at stepback(speed=0.1, h=-10, v=0)
                    "All of a sudden, Cherie's muscles stop resisting, and I feel myself slide all the way inside."
                    "And I can be sure that she feels it to, as she starts to gasp and cry out."
                    cherie.say "MON DIEU!"
                    cherie.say "MON DIEU!"
                    cherie.say "Mmmm...mmmph!"
                    "Cherie's exclamations suddenly become muffled mumbles instead."
                    "Because Kiara places a hand neatly over her mouth, effectively muting them."
                    "I don't need to be told to take advantage of the chance this gives me."
                    play sexsfx1 fuck_moderate loop
                    show milf 4some fuckcherie at stepback(speed=0.07, h=-10, v=0)
                    pause 0.2
                    show milf 4some fuckcherie at stepback(speed=0.07, h=-10, v=0)
                    "Instantly picking up the pace and starting to plough into Cherie."
                    "Which only makes her wriggle and writhe all the more as a result."
                    "Where before Kiara and Claire were just holding Cherie up, now they're holding her down."
                    play sexsfx1 fuck_speed loop
                    show milf 4some fuckcherie at stepback(speed=0.07, h=-10, v=0)
                    pause 0.2
                    show milf 4some fuckcherie at stepback(speed=0.07, h=-10, v=0)
                    "Gripping her tightly as I really get into my stride and begin to set the pace."
                    "Everything seems to speed up now, and to become more impactful too."
                    show milf 4some fuckcherie at stepback(speed=0.07, h=-10, v=0)
                    pause 0.2
                    show milf 4some fuckcherie at stepback(speed=0.07, h=-10, v=0)
                    "As if time and all the forces involved are becoming ever more concentrated."
                    "And so it comes as no surprise to me that I can feel myself on the verge of cuming."
                    menu:
                        "Cum inside of ass":
                            "Unable to control myself any longer, I surrender to the inevitable."
                            play sexsfx1 cum_inside
                            show milf 4some fuckcherie cum with hpunch
                            "Shooting my load inside of Cherie's ass as feeling the sensation of relief that comes with it."
                            with hpunch
                            "And the others release her from their grasp at the same time letting her flop backwards."
                            with hpunch
                            "And more than ready to collapse into a helpless heap on the sand."
                        "Pull out of ass":
                            "I use the last of my strength to pull backwards before it happens."
                            play sexsfx1 pop_out
                            show milf 4some fuckcherie out with hpunch
                            "Sliding all the way out of Cherie's ass the moment before I lose it."
                            play sexsfx1 cum_outside
                            show milf 4some fuckcherie cum with hpunch
                            "She moans softly as I shoot my load over her back and buttocks."
                            with hpunch
                            "And the others release her from their grasp at the same time letting her flop backwards."
                            with hpunch
                            "And more than ready to collapse into a helpless heap on the sand."
        "Fuck Kiara":






            "How in the hell am I supposed to choose between the three of them?"
            "That feels like an impossible choice for me to be forced to make."
            "At least until my eyes meet Kiara's, and it's all decided for me."
            "For some reason I can't help myself, I just know it's got to be her."
            "And she seems to realise it as soon as I reach out a hand in her direction."
            "Kiara instantly takes it, letting me guide her down and onto my lap."
            "Claire and Cherie look a little disappointed for a moment."
            "But then the same weird spell seems to settle over them too."
            "And instead of objecting, they settle down to one side of me."
            "Wrapping their arms around each other as they watch what we're doing."
            scene bg black
            show milf 4some fuckkiara beach
            with fade
            "And that's about the same time that Kiara leans her head back."
            "Catching my eye at the very moment she reaches down and takes hold of my cock!"
            mike.say "Argh!"
            mike.say "Hey, Kiara..."
            mike.say "Be careful with that thing - it's the only one that I've got!"
            kiara.say "Then you must have had a lot of practice with it, no?"
            kiara.say "So hurry up and show me what you're going to do with it now!"
            menu:
                "Fuck Kiara's pussy":
                    "Chastened and more than a little affronted by Kiara's words, I leap into action."
                    "Determined to show her that I know what I'm doing and pay her back for squeezing my cock just now."
                    with vpunch
                    "So I slide my hands under her thighs and lift her into the air without warning."
                    "Which makes her squeal in alarm and cling onto me tighter than before."
                    kiara.say "Wha…"
                    kiara.say "What are you..."
                    kiara.say "What are you doing?!?"
                    "I don't bother to answer Kiara's question, because my plan is to show her."
                    "A process that begins as soon as I lower her down again into my lap."
                    "But the difference is that, this time, she's coming down straight onto my cock."
                    "It's already hard and standing to attention below her, more than ready to go."
                    "And so Kiara's pussy is soon pressed against the tip, her weight pushing down from above."
                    "She squeals again, wriggling and writhing in my arms, but there's nowhere for her to go."
                    "Well, nowhere except straight down, which means my cock goes in the opposite direction."
                    show milf 4some fuckkiara kiara_normal
                    kiara.say "Ah..."
                    kiara.say "[hero.name]…"
                    kiara.say "You...you beast...you magnificent beast!"
                    play sexsfx1 slide_in
                    show milf 4some fuckkiara vaginal kiara_pleasure at startle(0.1,-10)
                    "By now Kiara is already starting to sink down and onto my cock."
                    "The lips of her pussy parting to let it inch into her body."
                    "Which means that it can't just be gravity doing all the work."
                    "She's obviously surrendering to my physically at the same time."
                    "Not that I'm content to sit back and wait for nature to take it's course."
                    play sexsfx1 fuck_moderate loop
                    show milf 4some fuckkiara at startle(0.07,-10)
                    pause 0.2
                    show milf 4some fuckkiara at startle(0.07,-10)
                    "And that's why I tighten my grip on Kiara, pulling her downwards even faster."
                    "This means that in mere seconds, I'm as deep inside of her as I can go."
                    "Kiara's head falls backwards, landing on my shoulder as she reels from the sensation."
                    "But I don't give her any time to ride it out, instantly lifting her into the air again."
                    show milf 4some fuckkiara at startle(0.07,-10)
                    pause 0.2
                    show milf 4some fuckkiara at startle(0.07,-10)
                    "And by the time she comes down for a second time, I've settled into a rhythm."
                    "Soon enough I'm bouncing Kiara up and down on my lap, filling her every time."
                    show milf 4some fuckkiara at startle(0.07,-10)
                    pause 0.2
                    show milf 4some fuckkiara at startle(0.07,-10)
                    "I can't really be sure if she's riding me in any true sense of the word right now."
                    "But I can tell by the way that she's clinging onto me and gasping that she's overwhelmed."
                    "There doesn't seem to be any way that she can speak up like she did when we started."
                    "By now the pleasure that she's feeling seems to have totally overtaken her."
                    play sexsfx1 fuck_speed loop
                    show milf 4some fuckkiara at startle(0.06,-10)
                    pause 0.15
                    show milf 4some fuckkiara at startle(0.06,-10)
                    "And the only sounds that she's making are ones of helpless pleasure."
                    "Yet she's not the only one making sounds like that."
                    "As I see when I risk glancing to my side in the direction of Claire and Cherie."
                    "Which is when I see the latter going down on the former, mere inches away from me."
                    show milf 4some fuckkiara at startle(0.06,-10)
                    pause 0.15
                    show milf 4some fuckkiara at startle(0.06,-10)
                    "And the sight of it only serves to make me thrust into Kiara even harder than before."
                    "I have no idea if she can even see what the other two are doing like I can."
                    "Because her head is lolling around and her eyes seem to have almost glazed over."
                    play sexsfx1 fuck_sprint loop
                    show milf 4some fuckkiara at startle(0.05,-10)
                    pause 0.15
                    show milf 4some fuckkiara kiara_ahegao at startle(0.05,-10)
                    "All of which means there's no warning when I feel Kiara begin to cum in my arms."
                    "Her muscles contract, squeezing my cock as she reaches her climax."
                    show milf 4some fuckkiara at startle(0.05,-10)
                    pause 0.15
                    show milf 4some fuckkiara at startle(0.05,-10)
                    "And suddenly I lose all interest in what Claire and Cherie are doing."
                    "Because I know that I'm about to cum too!"
                    menu:
                        "Cum inside of pussy":
                            "Unable to control myself any longer, I surrender to the inevitable."
                            play sexsfx1 cum_inside
                            show milf 4some fuckkiara cum with vpunch
                            "Shooting my load inside of Kiara as feeling the sensation of relief that comes with it."
                            with vpunch
                            "She sags in my arms, like a puppet with suddenly severed strings."
                            with vpunch
                            "And more than ready to collapse into a helpless heap on the sand."
                        "Pull out of pussy":
                            "I use the last of my strength to pull backwards before it happens."
                            play sexsfx1 slide_out
                            show milf 4some fuckkiara out at startle(0.05,-10)
                            "Sliding all the way out of Kiara the moment before I lose it."
                            play sexsfx1 cum_outside
                            show milf 4some fuckkiara cum with vpunch
                            "She moans softly as I shoot my load over her back and buttocks."
                            with vpunch
                            "And she sags in my arms, like a puppet with suddenly severed strings."
                            with vpunch
                            "And more than ready to collapse into a helpless heap on the sand."
                "Fuck Kiara's ass":






                    "Chastened and more than a little affronted by Kiara's words, I leap into action."
                    "Determined to show her that I know what I'm doing and pay her back for squeezing my cock just now."
                    with vpunch
                    "So I slide my hands under her thighs and lift her into the air without warning."
                    "Which makes her squeal in alarm and cling onto me tighter than before."
                    kiara.say "Wha…"
                    kiara.say "What are you..."
                    kiara.say "What are you doing?!?"
                    "I don't bother to answer Kiara's question, because my plan is to show her."
                    "A process that begins as soon as I lower her down again into my lap."
                    "But the difference is that, this time, she's coming down straight onto my cock."
                    "It's already hard and standing to attention below her, more than ready to go."
                    "I position her so that it's between her buttocks."
                    "Her hold pressed against the tip, her weight pushing down from above."
                    "She squeals again, wriggling and writhing in my arms, but there's nowhere for her to go."
                    "Well, nowhere except straight down, which means my cock goes in the opposite direction."
                    show milf 4some fuckkiara kiara_normal
                    kiara.say "Ah..."
                    kiara.say "[hero.name]…"
                    kiara.say "You...you beast...you magnificent beast!"
                    play sexsfx1 slide_in
                    show milf 4some fuckkiara anal kiara_pleasure at startle(0.1,-10)
                    "By now Kiara is already starting to sink down and onto my cock."
                    "The muscles of her ass to let it inch into her body."
                    "Which means that it can't just be gravity doing all the work."
                    "She's obviously surrendering to my physically at the same time."
                    "Not that I'm content to sit back and wait for nature to take it's course."
                    play sexsfx1 fuck_moderate loop
                    show milf 4some fuckkiara at startle(0.07,-10)
                    pause 0.2
                    show milf 4some fuckkiara at startle(0.07,-10)
                    "And that's why I tighten my grip on Kiara, pulling her downwards even faster."
                    "This means that in mere seconds, I'm as deep inside of her as I can go."
                    "Kiara's head falls backwards, landing on my shoulder as she reels from the sensation."
                    "But I don't give her any time to ride it out, instantly lifting her into the air again."
                    show milf 4some fuckkiara at startle(0.07,-10)
                    pause 0.2
                    show milf 4some fuckkiara at startle(0.07,-10)
                    "And by the time she comes down for a second time, I've settled into a rhythm."
                    "Soon enough I'm bouncing Kiara up and down on my lap, filling her every time."
                    show milf 4some fuckkiara at startle(0.07,-10)
                    pause 0.2
                    show milf 4some fuckkiara at startle(0.07,-10)
                    "I can't really be sure if she's riding me in any true sense of the word right now."
                    "But I can tell by the way that she's clinging onto me and gasping that she's overwhelmed."
                    "There doesn't seem to be any way that she can speak up like she did when we started."
                    "By now the pleasure that she's feeling seems to have totally overtaken her."
                    play sexsfx1 fuck_speed loop
                    show milf 4some fuckkiara at startle(0.06,-10)
                    pause 0.15
                    show milf 4some fuckkiara at startle(0.06,-10)
                    "And the only sounds that she's making are ones of helpless pleasure."
                    "Yet she's not the only one making sounds like that."
                    "As I see when I risk glancing to my side in the direction of Claire and Cherie."
                    "Which is when I see the latter going down on the former, mere inches away from me."
                    show milf 4some fuckkiara at startle(0.06,-10)
                    pause 0.15
                    show milf 4some fuckkiara at startle(0.06,-10)
                    "And the sight of it only serves to make me thrust into Kiara even harder than before."
                    "I have no idea if she can even see what the other two are doing like I can."
                    "Because her head is lolling around and her eyes seem to have almost glazed over."
                    play sexsfx1 fuck_sprint loop
                    show milf 4some fuckkiara at startle(0.05,-10)
                    pause 0.15
                    show milf 4some fuckkiara kiara_ahegao at startle(0.05,-10)
                    "All of which means there's no warning when I feel Kiara begin to cum in my arms."
                    "Her muscles contract, squeezing my cock as she reaches her climax."
                    show milf 4some fuckkiara at startle(0.05,-10)
                    pause 0.15
                    show milf 4some fuckkiara at startle(0.05,-10)
                    "And suddenly I lose all interest in what Claire and Cherie are doing."
                    "Because I know that I'm about to cum too!"
                    menu:
                        "Cum inside of ass":
                            "Unable to control myself any longer, I surrender to the inevitable."
                            play sexsfx1 cum_inside
                            show milf 4some fuckkiara cum with vpunch
                            "Shooting my load inside of Kiara's ass as feeling the sensation of relief that comes with it."
                            with vpunch
                            "She sags in my arms, like a puppet with suddenly severed strings."
                            with vpunch
                            "And more than ready to collapse into a helpless heap on the sand."
                        "Pull out of ass":
                            "I use the last of my strength to pull backwards before it happens."
                            play sexsfx1 pop_out
                            show milf 4some fuckkiara out at startle(0.05,-10)
                            "Sliding all the way out of Kiara's ass the moment before I lose it."
                            play sexsfx1 cum_outside
                            show milf 4some fuckkiara cum with vpunch
                            "She moans softly as I shoot my load over her back and buttocks."
                            with vpunch
                            "And she sags in my arms, like a puppet with suddenly severed strings."
                            with vpunch
                            "And more than ready to collapse into a helpless heap on the sand."






    call stop_all_sfx from _call_stop_all_sfx_64
    scene bg black with dissolve

label milf_after_beach_sex:
    scene bg masterhouse night
    show claire swimsuit at dark, left
    show cherie a swimsuit at dark, center
    show kiara swimsuit at dark, right
    with fade
    "By the time it's all over, the sun is beginning to set, sinking below the horizon."
    "This paints the sky a brilliant pink, fading to crimson as the day comes to an end."
    "And once all of us have gotten back into our swimming costumes, night has truly fallen."
    "We wander the shoreline, picking up the driftwood we find there and then pile it up."
    "And soon enough we have a fire to sit by and enjoy the stars coming out above us."
    mike.say "You know..."
    mike.say "I don't think this could be any more perfect."
    mike.say "The sound of the sea, the stars overhead - and the three most beautiful women in the world."
    "I know that's a pretty cheesy line, and it earns me a round of groans and more than one shove on the shoulder."
    "But I can see that the girls are feeling a warmth that's coming from somewhere aside from the fire too."
    show claire talkative blush
    claire.say "Oh, [hero.name]…"
    claire.say "You really have freed my heart, you know?"
    show claire happy
    show cherie happy
    cherie.say "You've helped us all to build a future together too."
    cherie.say "One more secure than any business could ever be."
    show cherie smile
    show kiara talkative
    kiara.say "I used to think that my underworld empire was all I needed."
    kiara.say "But you...you're my forever empire!"
    show kiara normal
    show claire normal
    "I can see the light of the fire reflecting their eyes as they say all of this."
    "Telling me that they're all tearing up as the emotions begin to get the better of them."
    "And I'm feeling the same way too, my voice breaking as I struggle to reply."
    mike.say "I..."
    mike.say "I love you all..."
    mike.say "In fact, I love you eternally!"
    mike.say "Let's make a vow to stay together, forever."
    "As one we place hands atop hands, agreeing to the idea and sealing the deal."
    "Making a pledge to be together for as long as we're able."
    "To join our lives and share the rest of them with each other."
    "And it's a vow that I very much intend to honour."
    $ game.hour = 20
    scene bg black with dissolve
    return

label cherie_claire_kiara_male_ending:
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding
    with fade
    "I can hear the sounds of the waves crashing quietly on the beach below the chapel."
    "They're merging almost seamlessly with the low voices of all the guests filling the pews."
    "And everywhere I look today, I see reminders of the three women that I'm waiting for."
    "The location is pretty much perfect, the chapel suiting our needs down to the ground."
    "Which is thanks to the business skills and organisational acumen of Cherie."
    "The interior of the chapel is also decked out with flowers that set just the right tone."
    "A subtle touch of domestic flair, and one that could only have come from Claire."
    "And the place is running super smoothly, with discreet men in smart suits on security detail."
    "Every one of them answering to Kiara and ready to obey her without hesitation."
    "I keep telling myself that all of this is stuff that should be calming my nerves right now."
    "That there's been four heads involved in the organisation of this wedding, rather than two."
    "Which means that it's had literally twice the amount of thought put into it than usual."
    "And yet, as I stand there at the altar, I'm still feeling anxious as hell!"
    "Thankfully the moment that the music starts to play, all of that changes."
    "As one the entire sum of humanity in the room turns to look at the doors."
    show claire wedding zorder 2 at center, zoomAt( 1.0, (340, 720))
    show cherie wedding zorder 1 at center, zoomAt( 1.0, (640, 720))
    show kiara wedding zorder 3 at center, zoomAt( 1.0, (940, 730))
    with dissolve
    "Just in time for them to swing open and for my brides to step into the chapel."
    "Wearing magnificent dresses and walking arm in arm, they sweep down the aisle towards me."
    "And the effect is like being hit by a storm, or washed over by a powerful wave."
    "Each one of them reminds me instantly of why I love them and how I feel for their charms."
    "Claire radiates her comforting, almost maternal calm and serene beauty."
    show claire wedding at center, traveling( 1.25, 3.0, (340, 880))
    show cherie wedding at center, traveling( 1.25, 3.0, (640, 880))
    show kiara wedding at center, traveling( 1.25, 3.0, (940, 890))
    "Cherie walks with poise and confidence, a woman comfortable in her own authority."
    "Kiara radiates the control and charm that makes her so exotic, a knowing look in her eye."
    if claire.is_visibly_pregnant and cherie.is_visibly_pregnant and kiara.is_visibly_pregnant:
        "The exquisite cut of their dresses taking into account their being with child."
        "Not seeking to hide it, and yet not making it stand out in any kind of stark manner."
    elif claire.is_visibly_pregnant and cherie.is_visibly_pregnant:
        "The exquisite cut of Claire and Cherie's dresses taking into account their being with child."
        "Not seeking to hide it, and yet not making it stand out in any kind of stark manner."
    elif claire.is_visibly_pregnant and kiara.is_visibly_pregnant:
        "The exquisite cut of Claire and Kiara's dresses taking into account their being with child."
        "Not seeking to hide it, and yet not making it stand out in any kind of stark manner."
    elif cherie.is_visibly_pregnant and kiara.is_visibly_pregnant:
        "The exquisite cut of Cherie and Kiara's dresses taking into account their being with child."
        "Not seeking to hide it, and yet not making it stand out in any kind of stark manner."
    elif claire.is_visibly_pregnant:
        "The exquisite cut of Claire's dress taking into account her being with child."
        "Not seeking to hide it, and yet not making it stand out in any kind of stark manner."
    elif cherie.is_visibly_pregnant:
        "The exquisite cut of Cherie's dress taking into account her being with child."
        "Not seeking to hide it, and yet not making it stand out in any kind of stark manner."
    elif kiara.is_visibly_pregnant:
        "The exquisite cut of Kiara's dress taking into account her being with child."
        "Not seeking to hide it, and yet not making it stand out in any kind of stark manner."
    else:
        "All in all, they look like a dream come true, a fantasy incarnate."
    "And as they reach the altar, I can finally let all of my emotions come bursting out."
    mike.say "Oh man..."
    mike.say "You guys look SO beautiful."
    mike.say "I can't believe this is actually happening!"
    show claire talkative
    claire.say "I know, I know!"
    show claire happy
    show cherie talkative
    cherie.say "It is like a waking dream, mon ami!"
    show cherie smile
    show kiara talkative
    kiara.say "I keep having to pinch myself!"
    show kiara smile
    "Priest" "Ahem..."
    show claire normal
    show cherie normal
    show kiara normal
    "As one, the four of us turn around to see the priest giving us a serious look."
    "And as we hurry to take up our allotted positions, he shakes his head."
    "Priest" "This is going to be like herding cats!"
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these FOUR people in holy matrimony!"
    "The priest launches into the ceremony, giving it all of the usual fire and fervour."
    "But even with four of us standing at the altar, it doesn't really get interesting."
    "Not until we make it to the actual vows that are going to be exchanged."
    "Priest" "Do you, Claire..."
    "Priest" "Take these three to be your partners?"
    show claire talkative at startle (0.05, -10)
    claire.say "I do."
    show claire normal
    "Priest" "Do you, Cherie..."
    "Priest" "Take these three to be your partners?"
    show cherie happy at startle (0.05, -10)
    cherie.say "Oui...I do."
    show cherie smile
    "Priest" "Do you, Kiara..."
    "Priest" "Take these three to be your partners?"
    show kiara talkative at startle (0.05, -10)
    kiara.say "I do."
    show kiara smile
    "Priest" "And what about you, [hero.name]?"
    "Priest" "Do you take all three of these women to be your wives?"
    mike.say "You bet I do!"
    "The priest nods."
    "Priest" "And what about the three of you?"
    show claire talkative
    show cherie talkative
    show kiara talkative
    "Claire, Cherie & Kiara" "We share him, and he shares us!"
    show claire normal
    show cherie normal
    show kiara normal
    "Priest" "I'll take that as a yes."
    "The priest takes a moment to collect himself."
    "Then he turns to face the guests filling the pews."
    "Priest" "I call upon those here present..."
    "Priest" "Asking that if you know of any lawful reason these people may not be joined in holy matrimony..."
    "Priest" "Speak now, or forever hold your peace!"
    "Okay, this is one of those moments when being in a quartet really makes things different."
    "Normally the wedding guests get the chance to chuckle to themselves for a few awkward seconds."
    "But what's going through my head is a riot of all the issues that each of us adds to the mix."
    "I mean, is Claire's ex-husband Hector going to have recovered from his stroke and come storming in?"
    "Is Claire's ex-husband Dwayne going to somehow manage to come back from the dead and crash the wedding?"
    "Or will one of Kiara's underworld rivals burst through the doors, Tommy Guns blazing?"
    "Hell, the string of ex-girlfriends I have in my past doesn't even get a look in!"
    "And when the doors do swing open, I can only fear the worst."
    show inspector at center, zoomAt(1.0, (200, 740)) with easeinleft
    "But the slightly dishevelled-looking, middle-aged man that shuffles in doesn't fit the bill."
    show claire stuned
    show cherie stuned
    show kiara stuned
    "In fact, he looks as confused as everyone else right now."
    show inspector at startle(0.05,-10)
    "Michaels" "Erm..."
    "Michaels" "Is dis the place where the mafia broad's getting married?"
    "Michaels" "I just came to...pay my respects...for being paid off."
    "Michaels" "Oops...forget I said that!"
    hide inspector with easeoutleft
    show claire normal
    show cherie normal
    show kiara normal
    "With that, he finds a spot at the back of the chapel."
    "And the ceremony gets back underway."
    "Priest" "Alright..."
    "Priest" "By the powers vested in me..."
    "Priest" "I now pronounce you husband and wives."
    "Priest" "Unless someone else has anything to say on the subject?"
    "Priest" "No?"
    "Priest" "Then you may kiss your...erm...your herd of brides."
    show claire happy at center, traveling( 1.5, 0.3, (380, 1040))
    show cherie closed at center, traveling( 1.5, 0.3, (640, 1040))
    show kiara smile at center, traveling( 1.5, 0.3, (900, 1040))
    "Suddenly everyone is kissing everyone else in a mad scrum of mutual affection."
    "Three bouquets are being tossed into the crowd of guests, causing a chaotic scrum."
    "And then we're hurrying out of the chapel and into the waiting limousine."
    "Slamming the door on the scene and driving off into the first day of the rest of our lives."
    scene bg black with dissolve
    pause 0.5
    show milf ending with fade
    claire.say "Oh, I'd have to say that our life together is as close to perfect as it's possible to be!"
    claire.say "After the wedding it turned out that I was the one with the most space to offer."
    claire.say "And so everyone decided to come and move into my cosy little house in the suburbs."
    claire.say "Cherie with all of her power suits and spreadsheets taking over the home office."
    claire.say "Kiara bringing her sense of luxury and style - always wanting to redecorate!"
    claire.say "And [hero.name], becoming the new man of the house."
    claire.say "All of which means that I get to be den-mother to the lot of them."
    claire.say "Cooking them hearty meals and worrying about all of the things they get up to."
    claire.say "It's like having a whole new family to keep me busy and to care for."
    claire.say "The only thing is that [hero.name] swears he can sense Hector's ghost haunting the place."
    claire.say "We find empty beer cans around the place sometimes, and the toilet inexplicably clogged."
    claire.say "But part of me thinks [hero.name] might be using the haunting as an excuse for his own messiness!"
    cherie.say "Claire is right, she is the foundation on which all of our hopes and achievements are built."
    cherie.say "Without her behind me and [hero.name] at my side, I could not have reclaimed my business empire."
    cherie.say "And not only have I reclaimed it, but I have been ruthless in my expansion too."
    cherie.say "But it is always good to come home to my love and the other women in my life."
    cherie.say "They support me, give me the strength to fight and something to fight for!"
    kiara.say "While Claire has expanded her business, I have chosen to scale mine back somewhat."
    kiara.say "Using our new base of operations to discover a whole different range of possibilities."
    kiara.say "Book clubs to infiltrate, bake sales to be turned into a profitable racket."
    kiara.say "Who would have thought that the suburbs held so many things ready to be exploited?"
    kiara.say "Perhaps the future of the underworld lies here, rather than in the big city?"
    if (claire.is_visibly_pregnant or claire.flags.mikeBabies >= 1):
        claire.say "Oh, and little Mikey Junior is coming growing up so fast."
        claire.say "They say that he's a natural at little league baseball."
        claire.say "And not just because his dad's the head coach!"
    if (cherie.is_visibly_pregnant or cherie.flags.mikeBabies >= 1):
        cherie.say "My Francois is already saying that he wants to be like her mother."
        cherie.say "And he looks so beautiful in his suits that match my own."
        cherie.say "Already able to run rings around his father in negotiations!"
    if (kiara.is_visibly_pregnant or kiara.flags.mikeBabies >= 1):
        kiara.say "Sofia may have her father's looks and amiable nature."
        kiara.say "But she is already the secret don of the day-care."
        kiara.say "Cutting deals and dispensing favours like her mother!"
    if not any(npc.is_visibly_pregnant or npc.flags.mikeBabies >= 1 for npc in (claire, cherie, kiara)):
        claire.say "Something tells me it won't be long before we hear the pitter-patter of tiny feet too!"
        cherie.say "The only question is, will it be one, two or all of us that are in the family way?"
        kiara.say "I am sure we will soon find out that [hero.name] is man enough for the challenge that awaits him!"
    claire.say "So there you have it..."
    claire.say "Four people from such different places in life."
    cherie.say "All of us brought together by [hero.name]."
    cherie.say "And made more by the bonding of our souls in love."
    kiara.say "It is true to say that he was the one that took hold of our disparate threads."
    kiara.say "That he was the one that wove us all together into a rich tapestry."
    claire.say "Oh, it's so fun when all four of us are cuddled up together on the sofa!"
    cherie.say "It is a time when I feel the most contented that I can ever remember."
    kiara.say "A time when everything seems to be perfect and complete."
    "Claire, Cherie & Kiara" "Because we know..."
    "Claire, Cherie & Kiara" "He's ours forever!"
    scene bg black with dissolve
    pause 0.5
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
