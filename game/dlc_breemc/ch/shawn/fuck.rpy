init python:
    InteractActivity(**{
    "name": "fuck_shawn",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            HasStamina(),
            ),
        PersonTarget(shawn,
            IsActive(),
            MinStat("love", 100),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    Event(**{
    "name": "shawn_hottub_sex_female",
    "label": "shawn_hottub_sex_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(shawn,
            OnDate(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "priority": 500,
    "do_once": False,
    "once_day": True,
    "duration": 1,
    })

    Event(**{
    "name": "shawn_cinema_sex_female",
    "label": "shawn_cinema_sex_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("date_watch_a_movie"),
            IsRoom("date_cinemaroom"),
            ),
        PersonTarget(shawn,
            OnDate(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "priority": 500,
    "do_once": True,
    "duration": 1,
    })


label shawn_hottub_sex_female:
    scene bg pool
    $ renpy.show(f"hottub_bg_{'night' if game.calendar.get_time_of_day() in ['evening', 'night'] else game.calendar.season_name}_left")
    $ renpy.show("hottub_fg_valentine_left", tag="romantic")
    with fade
    "I've got to admit that I'm a little bit nervous as I wait for Shawn to turn up."


    "I asked him if he wanted to come over and use the hot-tub with me."
    "And that's exactly what we're going to be doing as soon as he gets here."
    "But I might have made it sound a little bit more casual than it's going to be."
    "At least that's if my plan comes off, and he doesn't smell a rat."
    "Because I'm pretty sure Shawn won't be expecting the subdued lighting."
    "Likewise the candles and rose petals scattered all over the place."
    "The wine I might have been able to get away with on its own."
    "But all together, things are looking pretty romantic around here!"
    "I just have to hope that he likes surprises."
    "And that he's thinking along the same lines as me too!"
    shawn.say "Hey, [hero.name]..."
    shawn.say "Are you back there?"
    scene bg pool with vpunch
    "I actually jump in surprise at the sound of Shawn's voice."
    "And I do the best I can to make myself act normal as he walks around the side of the house."
    bree.say "Yeah, Shawn..."
    bree.say "Just come right around the back."
    bree.say "I'm right by the hot-tub, okay?"
    "I'm already in my swimsuit, all ready for the big reveal."
    "And I make sure to grab the wine and two glasses as well."
    shawn.say "I'm coming, [hero.name]!"
    show shawn date nice noglasses at left with easeinleft
    shawn.say "Trust me, I need something like this to relax me."
    shawn.say "You wouldn't believe the day I've had at work!"
    show shawn normal at center with ease
    shawn.say "I...oh my...oh my goodness!"
    "Shawn stops dead in his tracks when he sees what I've prepared for him."
    show shawn surprised blush at startle
    "The words just peter off, forgotten as he struggles to take it all in."
    "And I'd like to think at least a little of that is on account of his seeing me too!"
    bree.say "Surprise, Shawn!"
    bree.say "You ready to take a dip with me?"
    "Shawn blinks and shakes his head."
    "He genuinely looks like he's stunned right now."
    "But the shock soon wears off to the point where he regains the power of speech."
    shawn.say "Wow, [hero.name]..."
    shawn.say "Just...wow!"
    bree.say "Okay, Shawn..."
    bree.say "Is that wow as in good?"
    bree.say "Or wow as in bad?"
    show shawn normal blush
    "This seems to be enough to snap Shawn out of it."
    "And he instantly becomes animated again."
    "In fact, where before he was stunned, he now becomes almost manic."
    show shawn happy
    shawn.say "Oh...OH..."
    shawn.say "Wow as in good, [hero.name]!"
    shawn.say "Definitely wow as in good!"
    shawn.say "You look amazing."
    shawn.say "And all of this looks amazing too."
    shawn.say "I thought I was just getting to unwind after a stressful day at work!"
    show shawn nice
    shawn.say "But this...this is...wow!"
    "I can't help shaking my head and giggling at Shawn's reaction."
    "He's so cute and bumbling when he's like this!"
    "Sure, it's a nerdy, geeky kind of thing he has going on."
    "But I guess I'm kind of a nerd too."
    "So it works for me."
    bree.say "You can still unwind, Shawn."
    bree.say "In fact, I guarantee this will help de-stress you!"
    show shawn smug
    "I close the distance between us, handing Shawn a glass of wine."
    "And as I do, I can see that his eyes are all over me!"
    "Yeah, yeah, yeah - I know what you're thinking."
    "Girls are always complaining when guys eye them up."
    "But it's different when the guy in question is someone who's attention you want on you."
    "And trust me, the specific guy it is matters a hell of a lot too."
    "Shawn's not some random weirdo staring at me in a crowded elevator."
    "Nor is he a jackass catcalling me from across the street."
    "I know that he's a sweet, sensitive guy that's worth my time."
    "And that makes all the difference too!"
    show shawn normal
    "Shawn drops his things on the ground in order to take the wine."
    "And at the same time he's already trying to get undressed too!"
    bree.say "Slow down, Shawn!"
    bree.say "We've got plenty of time."
    bree.say "Plus you don't want to fall and hurt yourself!"
    bree.say "You can go inside and change in my room, if you like?"
    "Shawn shakes his head, trying to dismiss my concerns."
    show shawn happy
    shawn.say "It's okay..."
    shawn.say "I put my trunks on..."
    shawn.say "Under my pants!"
    bree.say "Oh...I see..."
    bree.say "Aren't you the eager one!"
    show shawn normal
    "Shawn nods as he finally manages to kick off his shoes."
    "One of them flies into the bushes, the other hits the wall."
    "Then he's into struggling with his work-shirt and pants."
    bree.say "Erm..."
    bree.say "Let me help you out there..."
    "I put down my wine and hurry to help Shawn."
    "And at first it's awkward as hell."
    "He's trying to do everything on his own."
    "Probably to protect that fragile male ego most guys seem to have."
    "And I'm trying to help while not looking like I'm directing traffic."
    "But as he's almost stripped off, I accidentally step forwards."
    "Which means that his groin rubs against me."
    "And in that moment, I can feel just how excited Shawn is right now!"
    bree.say "Ooh..."
    bree.say "Well hello there!"
    show shawn nice
    "Shawn instantly starts to flush red with embarrassment."
    "And he tries to take a step backwards and away from me."
    shawn.say "S...sorry, [hero.name]!"
    shawn.say "I didn't mean to..."
    "I grab hold of his wrist with one hand, stopping him from stepping away."
    "And with the other, I cup his manhood."
    "I do it gently, but make sure he knows it's no accident on my part too."
    bree.say "It's okay, Shawn!"
    bree.say "I was hoping to get my hands on it anyway..."
    "I get the impression that Shawn's on the brink of getting flustered again."
    "So I decide to step things up in order to keep that from happening."
    show shawn kiss with fade
    $ shawn.flags.kiss += 1
    "I place my lips against Shawn and begin to kiss him."
    "Maybe if he's tongue-tied, he can use his mouth for something else?"
    "And it doesn't take long for the gamble to start paying off either."
    "Shawn soon begins to relax, returning the kiss and leaning into me."
    "It seems like his instincts are winning out over his conscious mind."
    "And that's all the better for what I have in mind."
    "Somehow, while he's kissing me, Shawn becomes more coordinated."
    $ game.active_date.clothes = "swimsuit"
    show shawn kiss swimsuit with dissolve
    "He manages to shed the last of his clothes and hold onto his wine."
    "All while I lead him over to the tub and we climb down into the water."
    scene bg black
    $ renpy.show(f"hottub_bg_{'night' if game.calendar.get_time_of_day() in ['evening', 'night'] else game.calendar.season_name}_left")
    $ renpy.show("hottub_fg_valentine_left", tag="romantic")
    show shawn kiss swimsuit
    with dissolve
    "Shawn ends up pressed against the side, with me leaning over him."
    "And it's only now that I break off the kiss."
    show hottub shawn valentine with fade
    "He looks up at me as I take the wine-glass from his hand."
    bree.say "You said you were stressed before, right?"
    shawn.say "Y...yeah, [hero.name]!"
    bree.say "Then sit back and let me handle it."
    bree.say "I think I know just the thing for that..."
    "Shawn nods at this, his eyes wide as he looks up at me."
    "Which I guess means that he's happy to just sit back."
    "Sit back and leave everything to me!"
    "I start out slow, peeling off my swimsuit and making a show of it."
    "I can feels Shawn's eyes on me the whole time, watching my every move."
    "I don't feel anything but powerful as I reveal myself to him."
    "Like I'm holding him in the palm of my hand."
    "That done, I reach down and take hold of his trunks."
    "I pull them down and the moment I do, his cock pops up."
    "He seems embarrassed by this, but I just raise my eyebrows."
    bree.say "Well, well..."
    bree.say "What do we have here?"
    bree.say "I think I know."
    bree.say "And I know what to do with it too..."
    "Parting my legs, I begin to stroke my pussy with one hand."
    "I need the other to keep myself upright while I do this."
    "But luckily for me, Shawn's not going anywhere soon."
    "This means I can lower myself onto him slowly but surely."
    "And the lack of speed here seems to be to both our liking too!"
    show hottub sex female shawn valentine with fade
    "Shawn lets out a gasp of pleasure as the head of his cock makes contact."
    "I feel the same way too, though I bite my lip to keep myself under control."
    "I want this, and I'm eager to have him inside of me."
    "But there's still a little resistance that needs to be overcome."
    "With this in mind, I work the head back and forth against my lips."
    "And it doesn't take long for nature to take its course."
    shawn.say "Oh..."
    shawn.say "Oh fuck..."
    "All I can do right now is nod."
    "Because I can feel my muscles surrendering."
    "I can feel my pussy beginning to open."
    "And I can feel Shawn starting to slide into me!"
    "I make sure this goes as slow as possible, enjoying every moment."
    "Shawn fills me a little at a time this way, every fraction of an inch counting."
    "And by the time all of him is inside, I'm quivering all over."
    "I have to start out slow, it's not like I have a choice in the matter."
    "Anything more and I think I'd be overwhelmed!"
    "So I begin to ease myself up and down on Shawn's cock."
    "But even then I can feel the pleasure start to build in me."
    "I don't know if I can do this, if I can hold on so long."
    "I'm worried that if I go just a little faster, I won't last very long."
    "But that's when Shawn seems to come alive for the first time."
    "To come alive and take all of the decisions out of my hands."
    "I feel him grab hold of me around the waist."
    "And then he thrusts up and into me from below."
    bree.say "Mmm..."
    bree.say "Shawn..."
    bree.say "Yes...just like that!"
    "Shawn doesn't say a word, doesn't even nod."
    "He just launches into it, like his life depends on pleasing me!"
    "And here I was thinking I'd have to do all the work."
    "Instead I have to just hang on in there while he fucks me."
    "And believe me, you can't call what he's doing making love."
    "No, Shawn's fucking me right now, and hard too."
    "And I gotta say - I'm loving it!"
    "Shawn thrust up and down, in and out of me."
    "There's water splashing all over the place, slapping against me."
    "It sloshes over the sides of the tub and onto the decking."
    "But I couldn't care less, not so long as this keeps up!"
    "Or until he..."
    shawn.say "Ah..."
    shawn.say "Oh no..."
    shawn.say "I'm gonna..."
    with vpunch
    "I don't need Shawn to finish what he's saying."
    "Because I can already feel it happening inside of me."
    $ shawn.impregnate()
    with vpunch
    "As I come down on top of him, Shawn shoots his load."
    "He takes me by surprise too, meaning I can't pace myself."
    with vpunch
    "And the sensation instantly makes me start to cum too."
    "All I can manage to do is cling on for dear life as my orgasm takes me."
    "Luckily, Shawn has the presence of mind to hold me up in the water."
    "Then he keeps me there until the moment passes and I recover."
    "And once I do, there's no hint of stress left in him."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ shawn.sexperience += 1
    $ game.active_date.clothes = None
    scene bg black with dissolve
    return

label shawn_fuck_date_female(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg street
    show shawn
    call shawn_fuck_date_female_intro from _call_shawn_fuck_date_female_intro
    menu:
        "foreplay":
            call shawn_fuck_date_female_foreplay from _call_shawn_fuck_date_female_foreplay
        "fuck me right now":
            pass
    menu:
        "Missionary":
            call shawn_fuck_date_female_missionary (0) from _call_shawn_fuck_date_female_missionary
        "Doggy" if hero.sexperience >= 5:
            call shawn_fuck_date_female_doggy (5) from _call_shawn_fuck_date_female_doggy
        "Cowgirl" if hero.sexperience >= 10:
            call shawn_fuck_date_female_cowgirl (10) from _call_shawn_fuck_date_female_cowgirl
        "Reverse Cowgirl" if hero.sexperience >= 15:
            call shawn_fuck_date_female_reverse_cowgirl (15) from _call_shawn_fuck_date_female_reverse_cowgirl
    $ shawn.sexperience += 1
    hide shawn
    call shawn_sleep_date_fuck_female (location) from _call_shawn_sleep_date_fuck_female
    return

label shawn_fuck_date_female_intro:
    $ game.room = "bedroom4"
    scene bg bedroom4 with fade
    "I feel like I'm really beginning to be able to read Shawn, to tell what he wants in a given situation."
    "Sometimes it takes a subtle understanding of the kind of guy he is and the complexities of his personality."
    "But then there are some times when it's a little bit more obvious than that, more easy to read."
    show shawn happy at center, zoomAt (1.5, (640, 1080)) with fade
    "Such as right now, when we're sitting on the bed in my bedroom and both of us are laughing like fools."
    "The date that we just got back from was a total success, and we had the best time imaginable together."
    "Plus it doesn't hurt that we both had more than a couple of drinks to take the edge off too!"
    "Though for all that I'm sitting here giggling, I keep catching Shawn's eyes wandering downwards."
    "Now I know that us girls are usually supposed to go crazy when we catch a guy staring at our cleavage."
    "But right now it's more flattering than anything else, like a real compliment in my mind."
    "And the thing is that it's also kind of turning me on more than a little!"
    "Like, I'm super curious about what Shawn's thinking as he's staring at my breasts."
    bree.say "You like the look of my boobies, huh?"
    show shawn stuned
    "Wow...way to go, [hero.name]."
    "That was like, the least smooth line ever!"
    "All the same, Shawn almost leaps out of his skin at the question."
    "And now his eyes are definitely focussed solely on mine."
    "In fact they look as wide as saucers!"
    show shawn surprised
    shawn.say "Wha..."
    shawn.say "I..."
    show shawn embarrassed
    shawn.say "Sorry, [hero.name]...I was just..."
    "I can't help giggling and shaking my head as Shawn desperately tries to explain himself."
    bree.say "Oh, Shawn!"
    bree.say "If you really wanted to see them..."
    bree.say "All you have to do is ask!"
    "I'm already pulling off my top as I'm saying all of this."
    "Which means that Shawn is in the perfect spot to get an eyeful."
    "Obviously I can't see his reaction as I have my top over my head."
    show sexinserts chest bree zorder 1 at center, zoomAt(1, (-80, 820)) with easeinleft
    show sexinserts chest bree at center, zoomAt(1, (-80, 820)), vshake
    "But once it's off and my breasts are bouncing free in front of him, I get the whole picture."
    show shawn stuned
    "And believe me, now his eyes are bigger than ever."
    "In fact they're almost sticking out on stalks!"
    show shawn surprised
    shawn.say "Urgh..."
    show shawn complain
    shawn.say "Hrngh..."
    show shawn surprised
    shawn.say "Grrngh..."
    show shawn stuned
    "I sit there, patiently listening to the sounds that Shawn's making."
    "And at first I just assume that he's really liking what he's seeing."
    "But it doesn't take me long to start getting a little concerned."
    "Because his face seems to be getting redder by the moment."
    "In fact, I'm beginning to worry that he's starting to have some kind of funny turn."
    bree.say "Erm..."
    bree.say "Shawn..."
    bree.say "Are you feeling okay?"
    "Shawn doesn't so much answer the question as simply leap into action."
    hide sexinserts
    return

label shawn_fuck_date_female_foreplay:
    $ game.room = "bedroom4"
    scene bg bedroom4 with fade
    pause 0.1
    show shawn naked at center, zoomAt(1.5, (640, 1080)) with dissolve
    "One moment he's totally still, sitting on the bed like a statue."
    show shawn at center, traveling(1.75, 0.5, (640, 1220))
    "And the next he's leaping straight towards me, hands outstretched."
    "I barely have the time to take breath before he pounces on me."
    show shawn at center, traveling(2.0, 0.5, (640, 1360))
    "Then I find myself pinned to the mattress, with Shawn staring down at me."
    "Because he's all but barrelled into me in an effort to get to my breasts!"
    "Before I can say another word, I feel his hands on them."
    "But don't get me wrong, Shawn isn't being rough or handling me without respect."
    "His touch is gentle and delicate as he begins to caress my chest."
    "Which is more than enough to make me start to melt within moments."
    bree.say "Mmm..."
    bree.say "Shawn..."
    bree.say "Please...keep going?"
    "I have no way of knowing if Shawn hears what I'm saying to him."
    show shawn at center, traveling(2.5, 0.3, (640, 1680))
    "But all the same he leans in closer than ever before."
    "And I watch in silent anticipation as he parts his lips."
    hide shawn
    show shawn foreplay
    with fade
    bree.say "Oh..."
    bree.say "Oh fuck!"
    "Yeah, not the most eloquent of things that I could have come out with under the circumstances."
    "But give me a break, as I'm feeling the sensation of Shawn beginning to kiss one of my nipples!"
    "I can also feel them stiffening in response to the attention, starting to respond in kind."
    "And it's not just my breasts that are doing so either."
    with vpunch
    "At the same time I can feel more and more of my body becoming aroused."
    "So much so that I can't help squeezing my legs together tightly."
    "Because the sensations coming from my pussy right now are almost too much to bear!"
    "I still have no idea if Shawn can even hear a word I'm saying."
    "For all I know, he could be in a world of his own and not paying any attention."
    "But it's not like I'm really concerned that my message might not be getting through."
    "Not when his touch is making me feel this good."
    "Or when it's turning me on to such an incredible degree."
    "Shawn switches between one breast and the other, just as I think I'm handling it all."
    "So the sensations of pleasure change from one breast to the other in a mere matter of seconds."
    "But that doesn't mean the one he leaves behind is bereft of pleasure either."
    "Because even as the sensations are fading, his fingers find it and begin to squeeze."
    "Which means that I'm being pleasured on both sides at once, unable to escape."
    "As much as I can't get through to Shawn, I soon can't form words of my own either."
    "Now I find myself reduced to merely making sounds of helpless delight."
    "I'm gasping, panting and moaning without the ability to stop myself."
    "All I know is that I'm getting ever closer to losing control."
    "And that's when I feel the desperate need from between my thighs again."
    with vpunch
    "Even as I start to cum, I know that I need more from Shawn tonight."
    "I know that this just won't be enough to satisfy me."
    "That I'm going to need to feel him inside of me to be sated."
    "Which is what forces me to at least try to speak again."
    bree.say "Sh...Shawn..."
    bree.say "Please..."
    bree.say "Please...fuck me?"
    "The question seems to be more than enough to stop Shawn in his tracks."
    hide shawn
    show shawn naked at center, zoomAt(1.5, (640, 1080))
    with fade
    "He raises his head and looks me straight in the eye."
    "And at first I'm surprised to see that he looks surprised, even a little shocked."
    "But then I realise that I'm not dealing with some swaggering alpha male here."
    "Shawn's the kind of guy to still be taken aback when a woman admits that she wants him."
    "Which, of course, makes me want him all the more!"
    show shawn talkative
    shawn.say "Y...yeah, [hero.name]..."
    show shawn nice
    shawn.say "Of course - whatever you want!"
    show shawn smile
    "I find that I'm biting my lip as Shawn agrees to give me what I want."
    "Because I feel like I'm going to explode if he doesn't hurry up and do it."
    "God, he's a total nerd."
    "And I want him so badly because of that!"
    return

label shawn_fuck_date_female_missionary(sexperience_min):
    $ game.room = "bedroom4"
    scene bg bedroom4
    show shawn naked smile at center, zoomAt(1.5, (640, 1080))
    with fade
    "I feel like the entire evening has been leading up to this moment."
    "The moment when I find myself laid on my back with Shawn looking down at me."
    "We're in my place and safely inside of my own room, so nobody can disturb us."
    "And I know that both of us are in the perfect mood for what's about to happen."
    "Because we're stripped down to our skins, and I can almost feel the electricity between us."
    "As Shawn begins to find his confidence, he lowers himself down further still."
    "And I make a point of parting my legs to welcome him as he does so."
    scene bg black
    show shawn missionary closed
    with fade
    shawn.say "[hero.name]..."
    shawn.say "Is..."
    shawn.say "Is this okay?"
    shawn.say "Is this what you want?"
    "By way of an answer, I reach up and wrap my hands around Shawn's neck."
    "Then I pull him down into a kiss that's motivated by pure hunger and desire."
    "Luckily for me, this seems to be the last little hint that he needs."
    "The final push from my side of things to inform him that I want him in control."
    "At least to the point where that's what he thinks is going on between us!"
    "But I'm also aware that there's soon going to be little room for me to think like that."
    "Soon enough this is going to turn into an affair of pure instinct and the pursuit of pleasure."
    "And when I feel the sensation of his manhood rubbing against the inside of my thigh..."
    "Well, let's just say that I know it's on!"
    "As we're starting to pick up momentum, I have Shawn looking down on me from above."
    "And it's about then that I start to get the strangest of urges building inside of me."
    "I start to wonder what it would feel like to have those hands of his around my neck."
    "Without thinking what I'm doing, I reach up and take hold of Shawn's wrists."
    "Then I guide his hands until they're resting on my neck."
    shawn.say "...[hero.name]?"
    shawn.say "What are you doing?"
    show shawn missionary pleasure opened
    bree.say "Just go with it, yeah?"
    bree.say "Squeeze, but don't suffocate, okay?"
    show shawn missionary closed
    "Shawn nods, beginning to look a little more confident."
    "And then he begins to do as I ask, gently squeezing with his hands."
    "The effect is immediate and more dramatic than I expected it to be."
    show shawn missionary normal
    "My eyes widen and I can feel myself gasping a little."
    "But at the same time the sensation is matched down below."
    "There's a genuine surge of feeling from between my legs."
    "And my desire to have Shawn inside of me rises too."
    "I think all of this must be plain to see."
    "Because at the same time, Shawn's confidence seems to grow."
    "He's squeezing in just the right way for me to be getting off on it."
    "But there's not enough force in his hands to make it too scary either."
    "And the longer this goes on, the more I feel like I want him."
    "Like I want him inside of me!"
    menu:
        "Guide him to my pussy":
            "And I know exactly where I want Shawn to put it too."
            "I just have to make him feel like it was his idea to go there!"

            if hero.morality >= 25:
                show shawn missionary back opened
                bree.say "Oh, Shawn..."
                bree.say "It's SO big!"
                bree.say "Please be gentle with me?"

            if hero.morality <= -25:
                show shawn missionary pleasure
                bree.say "Mmm..."
                show shawn missionary opened
                bree.say "I'm used to big ones, Shawn..."
                bree.say "You think that you can fill me up?"
            else:

                show shawn missionary pleasure opened
                bree.say "Wow, Shawn..."
                bree.say "I can't wait to see how you get that thing inside of me!"
            show shawn missionary normal closed
            "I can see the ego-rub starting to take effect as Shawn grins."
            "And that's when I know he's going to go straight for my pussy."
            shawn.say "Oh, you bet, [hero.name]..."
            shawn.say "I totally will!"
            "And just like that, he's ready to go."
            call check_condom_usage (shawn) from _call_check_condom_usage_146
            if _return == False:
                return "leave_without_gain"
            "The sensation of Shawn atop me just feels so right."
            "His weight pressing down on my body isn't oppressive in the slightest."
            "Instead it makes me feel safe and secure, like he's protecting me."
            "But it's the sensation of him between my legs that really makes the difference."
            "Let's just say that when people assume things about the stature of the average nerd..."
            "Well, I don't think any of them have seen Shawn naked before!"
            "I honestly find myself biting my lip as he comes ever closer."
            "Anticipating the moment that he'll touch me down there."
            "And when it finally happens, I feel a shiver through my entire body."
            "Luckily for me, I don't think Shawn notices a thing."
            "Because he just keeps right on going, stroking the head against my lips."
            "I can hear myself beginning to whimper as my pussy opens to him."
            if CONDOM:
                show shawn missionary vaginal pleasure condom at stepback(0.1, -10, 0)
            else:
                show shawn missionary vaginal pleasure at stepback(0.1, -10, 0)
            "All it takes is a couple of short passes, and that's it."
            "My body doesn't seem to be in the mood to play hard to get at all!"
            "But that's fine by me, as I feel him begin to inch his way inside."
            "I feel the urge to speed things up, to pull Shawn down and onto me."
            "It's only a feat of will that makes me simply wrap my arms and legs around him instead."
            "And so I force myself to wait and allow Shawn to set the pace."
            "My reward for that is the intense feeling of desire that it causes me."
            show shawn missionary at stepback(0.1, -10, 0)
            "That and the inevitable surge of relief as I feel him push inside."
            "Shawn goes in smoothly, but with a sense of purpose that see him through."
            "It also means that I get to savour every single moment as he fills me."
            show shawn missionary at stepback(0.1, -10, 0)
            "Each movement he makes leaves me thinking it can't possibly get better."
            "And yet the next proves me wrong as it does!"
            show shawn missionary at stepback(0.1, -10, 0)
            "Once he's as deep as he can go, Shawn begins to move again."
            "Which makes the pleasure I'm feeling become that much more intense."
            "Don't get me wrong, I'm a thoroughly modern kind of girl."
            "The type that's capable of taking control when I feel the need."
            "But I'm also sensible enough to know when to do the exact opposite too."
            "And right now, all I want to do is lie back and let Shawn fuck me."
            "So that's exactly what I do, and he doesn't disappoint for a second."
            "Left to set the pace, he treats me to a slow and through ploughing."
            show shawn missionary at stepback(0.1, -10, 0)
            "His body moves atop me at a steady pace that never seems to waver."
            show shawn missionary at stepback(0.1, -10, 0)
            "Which means that I feel the sensation of his cock inside me the same way."
            show shawn missionary at stepback(0.1, -10, 0)
            "Every inch of me is pleasured, every spot hit in perfect time."
            show shawn missionary at stepback(0.1, -10, 0)
            "And each pass builds on the last, pushing me closer to my limits."
            show shawn missionary wide at stepback(0.1, -10, 0)

            if hero.morality >= 25:
                bree.say "Oh..."
                bree.say "Oh, Shawn..."
                bree.say "I'm going to...going to explode!"

            if hero.morality <= -25:
                bree.say "F...fuck..."
                bree.say "Fuck me...fuck me harder!"
                bree.say "Make me cum!"
            else:

                bree.say "Ah..."
                bree.say "Shawn..."
                bree.say "I'm going to...to cum!"
            call cum_reaction (shawn, 'vaginal', sexperience_min) from _call_cum_reaction_276
            if _return == "vaginal_outside":

                bree.say "Pull out now, Shawn..."
                bree.say "Before it's too late!"
                "Luckily for me, Shawn does as he's told before the end."
                show shawn missionary -vaginal at stepback(0.1, -10, 0)
                "Pulling out of me at the very last moment."
                show shawn missionary squirt
                "And even then it doesn't stop, as I feel him shooting his load over me."
                with hpunch
                "Now I really do cling onto Shawn for all I'm worth, pulling him against me."
                with hpunch
                "Then I hold him there as we ride out our climaxes together."
            elif _return == "vaginal_condom":

                "It's times like these that I'm glad we remembered to use a condom."
                "Because it means there's no need for Shawn to slow down for a second."
                "Instead he keeps right on going, thrusting into me until the very last."
                with hpunch
                "And even then it doesn't stop, as I feel him shooting his load into me."
                with hpunch
                "Now I really do cling onto Shawn for all I'm worth, pulling him against me."
                with hpunch
                "Then I hold him there as we ride out our climaxes together."
            elif _return == "vaginal_inside_pill":

                bree.say "Keep going, Shawn..."
                bree.say "I'm on the pill, remember?"
                "It's times like these that I'm glad I chose to go on the pill."
                "Because it means there's no need for Shawn to slow down for a second."
                "Instead he keeps right on going, thrusting into me until the very last."
                show shawn missionary ahegao creampie with hpunch
                "And even then it doesn't stop, as I feel him shooting his load into me."
                with hpunch
                "Now I really do cling onto Shawn for all I'm worth, pulling him against me."
                with hpunch
                "Then I hold him there as we ride out our climaxes together."
            elif _return == "vaginal_inside_pregnant":

                bree.say "Keep going, Shawn..."
                bree.say "I'm pregnant, remember?"
                "It's times like these that I realise being pregnant has it's advantages."
                "Because it means there's no need for Shawn to slow down for a second."
                "Instead he keeps right on going, thrusting into me until the very last."
                show shawn missionary ahegao creampie with hpunch
                "And even then it doesn't stop, as I feel him shooting his load into me."
                with hpunch
                "Now I really do cling onto Shawn for all I'm worth, pulling him against me."
                with hpunch
                "Then I hold him there as we ride out our climaxes together."
            else:

                "It's times like these that I just think you have to go for it."
                "And this is definitely one of those times."
                "Because it means there's no need for Shawn to slow down for a second."
                "Instead he keeps right on going, thrusting into me until the very last."
                show shawn missionary ahegao creampie with hpunch
                "And even then it doesn't stop, as I feel him shooting his load into me."
                with hpunch
                "Now I really do cling onto Shawn for all I'm worth, pulling him against me."
                with hpunch
                "Then I hold him there as we ride out our climaxes together."
        "Guide him to my ass":
            "And I know exactly where I want Shawn to put it too."
            "I just have to make him feel like it was his idea to go there!"

            if hero.morality >= 25:
                show shawn missionary back opened
                bree.say "Oh, Shawn..."
                bree.say "It's SO big!"
                bree.say "Please see if you can put it in my butt?"

            if hero.morality <= -25:
                show shawn missionary pleasure
                bree.say "Mmm..."
                show shawn missionary opened
                bree.say "I'm used to big ones up the ass, Shawn..."
                bree.say "You think that you can fill me up?"
            else:

                show shawn missionary pleasure opened
                bree.say "Wow, Shawn..."
                bree.say "I can't wait to see how you get that thing inside of my ass!"
            show shawn missionary normal closed
            "I can see the ego-rub starting to take effect as Shawn grins."
            "And that's when I know he's going to go straight for my ass."
            shawn.say "Oh, you bet, [hero.name]..."
            shawn.say "I totally will!"
            "And just like that, he's ready to go."
            "The sensation of Shawn atop me just feels so right."
            "His weight pressing down on my body isn't oppressive in the slightest."
            "Instead it makes me feel safe and secure, like he's protecting me."
            "But it's the sensation of him between my legs that really makes the difference."
            "Let's just say that when people assume things about the stature of the average nerd..."
            "Well, I don't think any of them have seen Shawn naked before!"
            "I honestly find myself biting my lip as he comes ever closer."
            "Anticipating the moment that he'll touch me down there."
            "And when it finally happens, I feel a shiver through my entire body."
            "Luckily for me, I don't think Shawn notices a thing."
            "Because he just keeps right on going, stroking the head between my buttocks."
            "I can hear myself beginning to whimper as my ass opens to him."
            show shawn missionary anal pleasure wide at stepback(0.1, -10, 0)
            "All it takes is a couple of short passes, and that's it."
            "My body doesn't seem to be in the mood to play hard to get at all!"
            "But that's fine by me, as I feel him begin to inch his way inside."
            "I feel the urge to speed things up, to pull Shawn down and onto me."
            "It's only a feat of will that makes me simply wrap my arms and legs around him instead."
            "And so I force myself to wait and allow Shawn to set the pace."
            "My reward for that is the intense feeling of desire that it causes me."
            show shawn missionary at stepback(0.1, -10, 0)
            "That and the inevitable surge of relief as I feel him push inside."
            "Shawn goes in smoothly, but with a sense of purpose that see him through."
            "It also means that I get to savour every single moment as he fills me."
            show shawn missionary at stepback(0.1, -10, 0)
            "Each movement he makes leaves me thinking it can't possibly get better."
            "And yet the next proves me wrong as it does!"
            show shawn missionary at stepback(0.1, -10, 0)
            "Once he's as deep as he can go, Shawn begins to move again."
            "Which makes the pleasure I'm feeling become that much more intense."
            "Don't get me wrong, I'm a thoroughly modern kind of girl."
            "The type that's capable of taking control when I feel the need."
            "But I'm also sensible enough to know when to do the exact opposite too."
            "And right now, all I want to do is lie back and let Shawn fuck me."
            "So that's exactly what I do, and he doesn't disappoint for a second."
            "Left to set the pace, he treats me to a slow and through ploughing."
            show shawn missionary at stepback(0.1, -10, 0)
            "His body moves atop me at a steady pace that never seems to waver."
            show shawn missionary at stepback(0.1, -10, 0)
            "Which means that I feel the sensation of his cock inside me the same way."
            show shawn missionary at stepback(0.1, -10, 0)
            "Every inch of me is pleasured, every spot hit in perfect time."
            show shawn missionary at stepback(0.1, -10, 0)
            "And each pass builds on the last, pushing me closer to my limits."
            show shawn missionary wide at stepback(0.1, -10, 0)

            if hero.morality >= 25:
                bree.say "Oh..."
                bree.say "Oh, Shawn..."
                bree.say "I'm going to...going to explode!"

            if hero.morality <= -25:
                bree.say "F...fuck..."
                bree.say "Fuck me...fuck me harder!"
                bree.say "Make me cum!"
            else:

                bree.say "Ah..."
                bree.say "Shawn..."
                bree.say "I'm going to...to cum!"
            call cum_reaction (shawn, 'anal', sexperience_min) from _call_cum_reaction_277
            if _return == "anal_inside":

                "It's times like these that using the back door really pays off."
                "Because it means there's no need for Shawn to slow down for a second."
                "Instead he keeps right on going, thrusting into me until the very last."
                show shawn missionary anal ahegao with hpunch
                "And even then it doesn't stop, as I feel him shooting his load into me."
                with hpunch
                "Now I really do cling onto Shawn for all I'm worth, pulling him against me."
                with hpunch
                "Then I hold him there as we ride out our climaxes together."
            else:

                bree.say "Pull out now, Shawn..."
                bree.say "Before it's too late!"
                "Luckily for me, Shawn does as he's told before the end."
                show shawn missionary -anal at stepback(0.1, -10, 0)
                "Pulling out of me at the very last moment."
                show shawn missionary squirt with hpunch
                "And even then it doesn't stop, as I feel him shooting his load over me."
                with hpunch
                "Now I really do cling onto Shawn for all I'm worth, pulling him against me."
                with hpunch
                "Then I hold him there as we ride out our climaxes together."
    "Once we're both spent, Shawn collapses onto the bed."
    "But luckily he happens to fall mostly to one side of me."
    "This means that I can easily wriggle out from under him."
    "Then I cuddle up as close as I can, wrapping us up together."
    "And it won't be long until we fall asleep too."
    "Because I feel totally exhausted and deeply satisfied."
    "My eyes already starting to feel heavy as they close."
    return

label shawn_fuck_date_female_cowgirl:
    $ game.room = "bedroom4"
    scene bg bedroom4
    show shawn naked smile at center, zoomAt(1.5, (640, 1080))
    with fade
    "There's always part of me that kind of wishes Shawn would assert himself sometimes."
    "You know, like not become a total alpha male jerk, but just take the lead a little?"
    "But then I guess that's one of the quirks of his personality."
    "He's just one of those sweet, sort of shy guys that's a bit awkward."
    "And it means that I sometimes have to be the one that makes the first move."
    "Which is why I wait until the exact moment that we're both done getting undressed."
    show shawn stuned at center, traveling(2.0, 0.5, (640, 1380))
    "Then I make my move, putting my hands on Shawn's shoulders and shoving him hard."
    "There's no way he could have seen it coming, so he's totally unprepared."
    "He barely has time to say a word before he's falling backwards."
    show shawn surprised
    shawn.say "Wha..."
    shawn.say "[hero.name]..."
    shawn.say "What are you..."
    show shawn stuned
    "Shawn windmills his arms as he topples over and falls."
    "But the bed is there to break his fall."
    "Because of course it is - you think I'd push him over if it wasn't?!?"
    show shawn surprised with vpunch
    shawn.say "Oof..."
    show shawn smile
    "I don't let Shawn get too comfortable on the mattress."
    "Instead I make a point of leaping onto the bed and atop him."
    "I wanted to land astride his thighs, but my aim isn't perfect."
    "So I kind of end up spreads across him and have to scramble into place."
    "Sure, it's pretty undignified, but he's too confused to even notice."
    "And a moment later I'm in the position that I wanted, straddling his thighs."
    scene bg black
    show shawn cowgirl
    with fade
    "Placing my hands on Shawn's shoulders, I look down at him, a smile on my face."
    show shawn cowgirl opened

    if hero.morality >= 25:
        bree.say "Are you okay, Shawn?"
        bree.say "I...I don't know what came over me!"

    if hero.morality <= -25:
        bree.say "I hope you're ready for this, Shawn..."
        bree.say "I'm one hundred percent going to get what I want - because I'm gonna take it!"
    else:

        bree.say "Surprise, Shawn..."
        bree.say "I feel like taking charge today!"
    show shawn cowgirl closed
    "I'm more than a little worried that I might have been too forward with Shawn."
    "That pouncing on him like that could have scared the poor guy half to death."
    "But much to my relief, I see that he has a huge, dumb smile on his face."
    shawn.say "N...no, [hero.name]..."
    shawn.say "It's fine..."
    shawn.say "In fact, it's really great!"
    "I'd be concerned that Shawn was just trying to be nice to me, to spare my feelings."
    "But the smile on his face looks pretty genuine to me."
    "And even more telling is the fact that I can feel something moving down there."
    "The unmistakable sensation of his cock as it rapidly hardens against my thigh."
    "I can't honestly think of better proof that he's loving every moment!"
    "Nodding eagerly, I make a point of reaching down and taking hold of it."
    "Shawn's eyes bulge as I give his cock a playful squeeze."
    "But if anything, it only makes the thing get bigger and harder still."
    menu:
        "Choking" if hero.flags.collared == True:
            "I don't know where the idea comes from, but suddenly it pops into my head."
            "An unshakable feeling that I want something different from Shawn, something unusual."
            "I feel the need for a little more assertiveness from him, maybe even a little danger too."
            "Almost unconsciously, I reach under the bed and grab exactly what I need."
            "Then I hold it up to Shawn, a collar and leash."
            "Without even thinking about it, I put them into his hands."
            "And then I guide them to my neck, placing them gently around it."
            "Shawn blinks and then stares at me in surprise."
            shawn.say "[hero.name]..."
            shawn.say "Are you..."
            shawn.say "Are you asking what I think you're asking?"
            show shawn cowgirl opened

            if hero.morality >= 25:
                bree.say "Yeah, Shawn - I want you to choke me a little."
                bree.say "Sure, it's scary, but that's kind of the point!"

            if hero.morality <= -25:
                bree.say "Yeah, Shawn - just the thought of it makes me hot."
                bree.say "Choke me a little, and I'll go all night, I promise!"
            else:

                bree.say "Just a little gentle choking, Shawn."
                bree.say "And remember, you're not throttling a chicken!"
            show shawn cowgirl hand closed with fade
            "Shawn nods, and I feel him tighten the collar around my neck."
            "I can't keep myself from moving as he does so, especially below the waist."
            "The pressure starts to build as my pussy brushes against his cock."
            "And it mixes with the thrill of being gently choked in a crazy way."
            "The more Shawn does it, the hotter I feel myself getting."
            "I have my hands on his waist, my grip on him tightening."
            "But it's to keep them in place not to struggle against what he's doing."
            show shawn cowgirl pleasure ahegao
            "By now my breath is coming in quick, ragged gasps."
            "Every moment that it keeps going, I think I'm going to cum."
            "And that makes me long to have Shawn inside of me."
            "So that in the end I have to let go of his waist."
            "As soon as I do so, my hands go fumbling for his cock."
            "Like I'm desperate to push it into me by any means possible."
            "Luckily for me, Shawn seems to understand what's happening."
            show shawn cowgirl -hand normal closed with fade
            "Because he releases his grip, allowing me to let out a gasp of air."
        "Spanking":
            "I don't know where the idea comes from, but suddenly it pops into my head."
            "An unshakable feeling that I want something different from Shawn, something unusual."
            "I feel the need for a little more assertiveness from him, maybe even a little danger too."
            "Without even thinking about it, I put my hands on his wrists."
            "And then I guide them to my butt, encouraging him to squeeze them for all he's worth."
            "Shawn blinks and then stares at me in surprise."
            shawn.say "[hero.name]..."
            shawn.say "Are you..."
            shawn.say "Are you asking what I think you're asking?"
            show shawn cowgirl opened

            if hero.morality >= 25:
                bree.say "Yeah, Shawn - I want you to spank me a little."
                bree.say "Sure, it's scary, but that's kind of the point!"

            if hero.morality <= -25:
                bree.say "Yeah, Shawn - just the thought of it makes me hot."
                bree.say "Spank me a little, and I'll go all night, I promise!"
            else:

                bree.say "Just a little gentle spanking, Shawn."
                bree.say "And remember, you're slapping me into the middle of next week!"
            show shawn cowgirl closed
            "Shawn nods eagerly, and I feel one of his hands lift off of my buttock."
            play sound spank
            with hpunch
            "A moment later there's the sound of skin meeting skin at high speed."
            "It's like the cracking of a whip, and the sensation is just as instant."
            bree.say "Ah!"
            bree.say "Oh yeah..."
            bree.say "Do it again, please?"
            play sound spank
            with hpunch
            "Shawn slaps my ass for a second time, and harder too."
            "All of which just makes it feel that much better."
            play sound spank
            with hpunch
            pause 0.3
            play sound spank
            with hpunch
            "After that he seems to hit his stride, adding a third and then a fourth slap."
            "I soon begin to lose count as the spanking picks up pace."
            play sound spank
            with hpunch
            "All I know is that I'm starting to feel like I can't hold it in."
            "By now my breath is coming in quick, ragged gasps."
            play sound spank
            with hpunch
            "Every moment that it keeps going, I think I'm going to cum."
            "And that makes me long to have Shawn inside of me."
            "So that in the end I have to take hold of his wrists again."
            "Luckily for me, Shawn seems to understand what's happening."
            "Because he stops the spanking, allowing me to let out a gasp of air."
        "Fuck me right now":
            pass
    menu:
        "Guide him to my pussy":
            "It can't have been more than a couple of minutes since we got naked."
            "But somehow it feels like forever, like I've been waiting for so long."
            "And only because I'm so desperate to have Shawn inside of me!"
            "Which is why I reach down and take a hold of his cock."
            "And it must be a firm one too, judging by his instant reaction."
            shawn.say "Urgh..."
            shawn.say "Hey, [hero.name]..."
            shawn.say "Be careful with that thing - it's the only one I've got!"
            call check_condom_usage (shawn) from _call_check_condom_usage_147
            if _return == False:
                return "leave"
            if CONDOM:
                show shawn cowgirl condom with fade
            "Almost as soon as I'm in position, I make my move."
            "I feel like I've been waiting long enough, and now it's time."
            "Grabbing the base of Shawn's cock with one hand, I put the other on his chest."
            "And then I almost throw myself down and onto it, looking like I'm just going for it."
            "But the truth is that I've already taken careful aim."
            "So I know exactly where I'm going to land and what will be in position when I do."
            "There's just enough time for me to hear Shawn gasp in surprise."
            "And in the very next moment I feel it happening, I feel everything coming together."
            "The head of his cock slides against the lips of my pussy, making me gasp too."
            "I'm expecting to have to do this more than once, to work for it."
            "But to my surprise, I feel my pussy surrendering without a fight."
            "I can't explain why it happens, only that it does."
            "One moment Shawn's on the outside, and I'm doing all that I can to get him in."
            "The next he's on the inside and my body is swallowing all that he has to give."
            show shawn cowgirl vaginal with fade
            "I feel like I'm sinking down onto him in slow motion, as if time is slowing to a crawl."
            "Perhaps that's because of how intense the sensations are right now."
            "So much so that I can barely feel any other part of my body."
            "Only where I'm being touched by Shawn feels in any measure solid and real."
            "The further a part of me from that, the more faint and unreal it seems to me."
            show shawn cowgirl at stepback(0.1, 10, 5)
            "And when I've sunk down as far as I can go, I just stop and stare into space."
            "It sounds crazy to say so, but I have no idea what to do next."
            "My brain just can't cope with the concept of there being more than this."
            "So it seems to want to keep me here for as long as possible."
            "Well, maybe that would have worked if there were only one person involved."
            "But I'm suddenly reminded of the fact that Shawn's in on this one too."
            "Because all at once he comes alive, like he's waking up from sleep."
            "I feel his hands tighten on my haunches, his legs stiffen under me."
            "And then I realise that it doesn't matter if I stay still or not."
            "Shawn's going to do what he needs to do either way!"
            show shawn cowgirl at stepback(0.1, 10, 5)
            "Even now I can feel him beginning to move inside of me."
            "Slowly at first, but somehow with the promise of far more to come."
            "Kind of like when you see one of those huge engines beginning to work."
            show shawn cowgirl at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl at stepback(0.1, 10, 5)
            "Soon enough they've gone from a standing start to pounding away like crazy."
            "And ironically enough, that's exactly what Shawn's doing to me now!"
            show shawn cowgirl speed at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl -speed opened pleasure with hpunch
            "Within no time at all he's in motion, going faster and faster."
            "And as he picks up speed, what I'm feeling becomes more intense too."
            show shawn cowgirl speed at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl -speed at stepback(0.1, 10, 5)
            "I feel like I'm being dragged steadily higher all the time."
            "Like I'm sitting on a roller-coaster, ratcheting up towards a big drop."
            show shawn cowgirl speed at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl -speed at stepback(0.1, 10, 5)
            "The air is filled with the sound of Shawn's grunting at the effort of it all."
            "And almost as loud are the noises coming out of me at the same time."
            show shawn cowgirl speed at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl -speed at stepback(0.1, 10, 5)
            "Then it happens, we reach the top of the roller-coaster."
            "And there's only one direction that we can go in now."
            "We seem to teeter on the edge for a moment, and then gravity takes over."
            show shawn cowgirl speed at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl -speed at stepback(0.1, 10, 5)
            "I'm pushing down as Shawn pushes up, and between us we make it happen."
            "I can feel my orgasm taking hold."
            show shawn cowgirl speed at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl -speed at stepback(0.1, 10, 5)
            "And from the look on his face, Shawn's not far behind."
            call cum_reaction (shawn, 'vaginal', 1) from _call_cum_reaction_278

            if _return == "vaginal_condom":
                "I remember that we chose to use a condom, and feel a flood of relief."
                show shawn cowgirl speed with hpunch
                pause 0.2
                show shawn cowgirl -speed ahegao pleasure with hpunch
                "But it's only a blip in comparison to the wave that hits me as I cum."
                show shawn cowgirl speed with hpunch
                pause 0.2
                show shawn cowgirl -speed with hpunch
                "Shawn seems to lose it at the exact same moment, filling me up completely."
                with hpunch
                "It's all that I can do to hold myself up while it's happening."
                "And when the sensation passes, I sink down onto Shawn's chest."
                "Lying there without the strength to move a single muscle."

            elif _return == "vaginal_inside_pill":
                "I remember that I'm on the pill right now, and feel a flood of relief."
                show shawn cowgirl speed with hpunch
                pause 0.2
                show shawn cowgirl -speed ahegao pleasure with hpunch
                "But it's only a blip in comparison to the wave that hits me as I cum."
                show shawn cowgirl speed with hpunch
                pause 0.2
                show shawn cowgirl -speed creampie with hpunch
                "Shawn seems to lose it at the exact same moment, filling me up completely."
                with hpunch
                "It's all that I can do to hold myself up while it's happening."
                "And when the sensation passes, I sink down onto Shawn's chest."
                "Lying there without the strength to move a single muscle."

            elif _return == "vaginal_inside_pregnant":
                "I give a silent word of thanks for being pregnant, and it take physical from as a flood of relief."
                show shawn cowgirl speed with hpunch
                pause 0.2
                show shawn cowgirl -speed ahegao pleasure with hpunch
                "But it's only a blip in comparison to the wave that hits me as I cum."
                show shawn cowgirl speed with hpunch
                pause 0.2
                show shawn cowgirl -speed creampie with hpunch
                "Shawn seems to lose it at the exact same moment, filling me up completely."
                with hpunch
                "It's all that I can do to hold myself up while it's happening."
                "And when the sensation passes, I sink down onto Shawn's chest."
                "Lying there without the strength to move a single muscle."

            elif _return == "vaginal_outside":
                "At the last moment I realise that I want Shawn to pull out before the end."
                "But I know that I'm going to have to take matters into my own hands if I want it to actually happen."
                show shawn cowgirl -speed out ahegao cumshot with hpunch
                "This means hauling myself off of Shawn before he loses it."
                show shawn cowgirl cumshot with hpunch
                "Shawn seems to explode the exact same moment I do it, his cock firing off like a cannon."
                show shawn cowgirl -cumshot cum onbody with hpunch
                "It's all that I can do to hold myself up while it's happening, with him shooting his load over my chest."
                "And when the sensation passes, I sink down onto Shawn's chest."
                "Lying there without the strength to move a single muscle."
            else:

                "I feel almost overwhelmed by the wave that hits me as I cum."
                show shawn cowgirl speed with hpunch
                pause 0.2
                show shawn cowgirl -speed creampie with hpunch
                "Shawn seems to lose it at the exact same moment, filling me up completely."
                show shawn cowgirl speed with hpunch
                pause 0.2
                show shawn cowgirl -speed ahegao pleasure with hpunch
                "It's all that I can do to hold myself up while it's happening."
                with hpunch
                "And when the sensation passes, I sink down onto Shawn's chest."
                "Lying there without the strength to move a single muscle."
        "Guide him to my ass":
            "It can't have been more than a couple of minutes since we got naked."
            "But somehow it feels like forever, like I've been waiting for so long."
            "And only because I'm so desperate to have Shawn inside of me!"
            "Which is why I reach down and take a hold of his cock."
            "And it must be a firm one too, judging by his instant reaction."
            shawn.say "Urgh..."
            shawn.say "Hey, [hero.name]..."
            shawn.say "Be careful with that thing - it's the only one I've got!"
            "Almost as soon as I'm in position, I make my move."
            "I feel like I've been waiting long enough, and now it's time."
            "Grabbing the base of Shawn's cock with one hand, I put the other on his chest."
            "And then I almost throw myself down and onto it, looking like I'm just going for it."
            "But the truth is that I've already taken careful aim."
            "So I know exactly where I'm going to land and what will be in position when I do."
            "There's just enough time for me to hear Shawn gasp in surprise."
            "And in the very next moment I feel it happening, I feel everything coming together."
            "The head of his cock slides straight between my butt-cheeks, making me gasp too."
            "I'm expecting to have to do this more than once, to work for it."
            "But to my surprise, I feel my ass surrendering without a fight."
            "I can't explain why it happens, only that it does."
            "One moment Shawn's on the outside, and I'm doing all that I can to get him in."
            "The next he's on the inside and my body is swallowing all that he has to give."
            show shawn cowgirl anal with fade
            "I feel like I'm sinking down onto him in slow motion, as if time is slowing to a crawl."
            "Perhaps that's because of how intense the sensations are right now."
            "So much so that I can barely feel any other part of my body."
            "Only where I'm being touched by Shawn feels in any measure solid and real."
            "The further a part of me from that, the more faint and unreal it seems to me."
            show shawn cowgirl at stepback(0.1, 10, 5)
            "And when I've sunk down as far as I can go, I just stop and stare into space."
            "It sounds crazy to say so, but I have no idea what to do next."
            "My brain just can't cope with the concept of there being more than this."
            "So it seems to want to keep me here for as long as possible."
            "Well, maybe that would have worked if there were only one person involved."
            "But I'm suddenly reminded of the fact that Shawn's in on this one too."
            "Because all at once he comes alive, like he's waking up from sleep."
            "I feel his hands tighten on my haunches, his legs stiffen under me."
            "And then I realise that it doesn't matter if I stay still or not."
            "Shawn's going to do what he needs to do either way!"
            show shawn cowgirl at stepback(0.1, 10, 5)
            "Even now I can feel him beginning to move inside of me."
            "Slowly at first, but somehow with the promise of far more to come."
            "Kind of like when you see one of those huge engines beginning to work."
            show shawn cowgirl at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl at stepback(0.1, 10, 5)
            "Soon enough they've gone from a standing start to pounding away like crazy."
            "And ironically enough, that's exactly what Shawn's doing to me now!"
            show shawn cowgirl speed at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl -speed opened pleasure with hpunch
            "Within no time at all he's in motion, going faster and faster."
            "And as he picks up speed, what I'm feeling becomes more intense too."
            show shawn cowgirl speed at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl -speed at stepback(0.1, 10, 5)
            "I feel like I'm being dragged steadily higher all the time."
            "Like I'm sitting on a roller-coaster, ratcheting up towards a big drop."
            show shawn cowgirl speed at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl -speed at stepback(0.1, 10, 5)
            "The air is filled with the sound of Shawn's grunting at the effort of it all."
            "And almost as loud are the noises coming out of me at the same time."
            show shawn cowgirl speed at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl -speed at stepback(0.1, 10, 5)
            "Then it happens, we reach the top of the roller-coaster."
            "And there's only one direction that we can go in now."
            "We seem to teeter on the edge for a moment, and then gravity takes over."
            show shawn cowgirl speed at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl -speed at stepback(0.1, 10, 5)
            "I'm pushing down as Shawn pushes up, and between us we make it happen."
            show shawn cowgirl speed opened pleasure with vpunch
            "I can feel my orgasm taking hold."
            show shawn cowgirl speed at stepback(0.1, 10, 5)
            pause 0.2
            show shawn cowgirl -speed at stepback(0.1, 10, 5)
            "And from the look on his face, Shawn's not far behind."
            call cum_reaction (shawn, 'anal', 1) from _call_cum_reaction_279

            if _return == "anal_inside":
                "I feel almost overwhelmed by the wave that hits me as I cum."
                show shawn cowgirl speed with hpunch
                pause 0.2
                show shawn cowgirl -speed creampie with hpunch
                "Shawn seems to lose it at the exact same moment, filling me up completely."
                show shawn cowgirl speed with hpunch
                pause 0.2
                show shawn cowgirl -speed ahegao pleasure with hpunch
                "It's all that I can do to hold myself up while it's happening."
                with hpunch
                "And when the sensation passes, I sink down onto Shawn's chest."
                "Lying there without the strength to move a single muscle."
            else:

                "At the last moment I realise that I want Shawn to pull out before the end."
                "But I know that I'm going to have to take matters into my own hands if I want it to actually happen."
                show shawn cowgirl -speed out ahegao cumshot with hpunch
                "This means hauling myself off of Shawn before he loses it."
                show shawn cowgirl cumshot with hpunch
                "Shawn seems to explode the exact same moment I do it, his cock firing off like a cannon."
                show shawn cowgirl -cumshot cum onbody with hpunch
                "It's all that I can do to hold myself up while it's happening, with him shooting his load over my chest."
                "And when the sensation passes, I sink down onto Shawn's chest."
                "Lying there without the strength to move a single muscle."
    return

label shawn_fuck_date_female_reverse_cowgirl:
    $ game.room = "bedroom4"
    scene bg bedroom4
    show shawn naked smile at center, zoomAt(1.5, (640, 1080))
    with fade
    "There's no denying it, Shawn and I are about to get it on."
    "We're wrapped up in each other's arms and excited as hell."
    "But neither of us seems to be giving the details much thought."
    "Which makes sense, as right now I'm more concerned with kissing him."
    hide shawn
    show shawn kiss naked
    with fade
    "And he seems to be dead set on exploring every inch of me with his hands!"
    "All of this means that we're kind of walking towards the bed at the same time."
    "Or perhaps it'd be more truthful to say we're headed in that vague direction."
    "The truth is that we're both way too distracted to really know where we are."
    "So when we do make it to the edge of the bed, we walk straight into it!"
    show shawn naked stuned at center, zoomAt(1.5, (640, 1080))
    with hpunch
    bree.say "Wha..."
    bree.say "Whoa!"
    show shawn surprised
    shawn.say "Oops..."
    shawn.say "Oh shit!"
    with vpunch
    "As one we topple over, still held together in a tangle of limbs."
    "And I guess that probably helps matters from going south."
    "Because we fall straight onto the mattress, bouncing as we do so."
    "Plus our arms are wrapped around each other too."
    "So nobody crashes into anything else on the way down."
    show shawn sadsmile
    "Shawn's the one that lands on his back, and he seems more disoriented than me."
    "I say this because he stays right where he is as I begin to move atop him."
    "And it's only once I'm straddling his thighs that Shawn seems to snap out of it."
    "But by then it's kind of too late for him to be able to stop me doing what I wanted."
    show shawn surprised
    shawn.say "Huh?"
    shawn.say "What..."
    shawn.say "What just happened?"
    show shawn sadsmile
    "I have my back turned to Shawn as he asks the question."
    "Which means I have to look over my shoulder to make eye contact."

    if hero.morality >= 25:
        bree.say "Oh, sorry, Shawn..."
        bree.say "We kind of lost our balance back there."
        bree.say "Since then, I don't know what's come over me!"

    if hero.morality <= -25:
        bree.say "Lust on the brain, Shawn - that's what happened!"
        bree.say "But don't worry, I know just how to fix that."
        bree.say "So just lie back and leave it to me, okay?"
    else:

        bree.say "Don't worry, Shawn..."
        bree.say "We just took a tumble, that's all."
        bree.say "But I've got everything in hand."
    scene bg black
    show shawn reverse cowgirl smile
    with fade
    "Shawn's eyes go wide as he sees that I have him pinned down on the bed."
    "But he nods all the same, pretty much putting me in the driver's seat."
    "That's all the permission I need to do what I have in mind for next."
    "And so not wasting another second, I reach out and take hold of Shawn's cock."
    "By which I don't mean that I grab it as though it's going to escape me."
    "And by the same token I don't go for it gingerly either."
    "My hand moves slowly but with an assured confidence."
    "My fingers wrapping around the shaft in a firm, yet gentle manner."
    "And I know that I've done what I intended to do when I hear Shawn gasp."
    "The sound is just the right mixture of surprise and excitement."
    "Plus I can feel the sensation of him getting harder under my touch."
    "Letting me know that we're both on the same page here."
    "But now that I have what I want, I need to decide what I'm going to do with it."
    menu:
        "Spanking":
            "Just as I'm about to put my plan into action, I feel something behind me."
            "It's the unmistakable sensation of Shawn reaching up and putting his hands on my butt."
            "He does it gently, but for some unknown reason, I can't help jumping."
            show shawn reverse cowgirl normal
            bree.say "Oh man!"
            show shawn reverse cowgirl smile
            shawn.say "What's the matter, [hero.name]?"
            shawn.say "Are you okay?"
            show shawn reverse cowgirl normal
            bree.say "I'm...fine, totally fine."
            bree.say "But would you mind doing that again?"
            bree.say "Maybe like, harder and more often?"
            show shawn reverse cowgirl smile
            "There's a moment of silence as Shawn tries to process the request."
            "And I find myself biting my lip as he does so."
            shawn.say "Erm..."
            shawn.say "Just to be clear, [hero.name]..."
            shawn.say "To make sure we're on the same page, yeah?"
            shawn.say "Are you asking me to...to spank you?!?"
            show shawn reverse cowgirl normal

            if hero.morality >= 25:
                bree.say "Oh, I know it sounds weird, Shawn..."
                bree.say "But I just can't help it!"

            if hero.morality <= -25:
                bree.say "You bet I am, Shawn..."
                bree.say "I want you to pound my ass before you pound me!"
            else:

                bree.say "Ah..."
                bree.say "Yeah, I guess so!"
            show shawn reverse cowgirl smile
            "I wait for a little while longer."
            "And I'm starting to worry that I've freaked Shawn out."
            play sound spank
            show shawn reverse cowgirl normal closed slap at hshake
            pause 0.5
            show shawn reverse cowgirl wink -slap
            "But then there's the sudden sound of skin cracking against skin."
            "A second later I flinch and let out a yelp of surprise."
            "As soon as I do so, something seems to click in Shawn."
            play sound spank
            show shawn reverse cowgirl normal closed slap at hshake
            pause 0.5
            show shawn reverse cowgirl wink -slap
            "The second slap across my butt-cheeks comes fast on the heels of the first."
            "I don't yelp as loudly this time, but I do feel more of a thrill."
            play sound spank
            show shawn reverse cowgirl normal closed slap at hshake
            pause 0.5
            show shawn reverse cowgirl wink -slap
            "Pretty soon Shawn's spanking me like it's the most natural thing in the world."
            "And I can tell that we're both getting off on the experience too."
            play sound spank
            show shawn reverse cowgirl ahegao slap at hshake
            pause 0.5
            show shawn reverse cowgirl normal wink -slap
            "Because I can feel myself getting hotter and wetter with every slap."
            "Shawn's cock, on the other hand, never felt so big and hard as it does right now!"
            shawn.say "Oh man..."
            shawn.say "[hero.name], your ass is so red!"
            shawn.say "It's like the whole thing is glowing!"
            "I nod eagerly, knowing that it's time to move on to the next stage."
        "Fuck me right now":
            pass
    menu:
        "Guide him to my pussy":
            "Without hesitation, I begin to slide Shawn's cock between my thighs."
            "Or to be more specific, I slide my pussy against the head."
            "Only after a couple more passes do I let any more of it touch me."
            "Adding a little more of the shaft each time, just enough to make him gasp."
            call check_condom_usage (shawn) from _call_check_condom_usage_149
            if _return == False:
                return "leave"
            if CONDOM:
                show shawn reverse cowgirl condom with fade
            else:
                show shawn reverse cowgirl with fade
            shawn.say "[hero.name]..."
            shawn.say "Are you..."
            shawn.say "Are you going to, you know...do it?"

            if hero.morality >= 25:
                bree.say "Oh, sorry, Shawn..."
                bree.say "We're going to do it, I promise!"

            if hero.morality <= -25:
                bree.say "You're so desperate for pussy!"
                bree.say "Geez, Shawn..."
            else:

                bree.say "Don't worry, Shawn..."
                bree.say "We're almost there!"
            "It's ironic Shawn would choose that exact moment to ask such a question."
            "Because almost the same moment he does so, things start to move down there."
            "I'm still rubbing his cock hard against my pussy as I answer him."
            "And even before I'm finished, the lips begin to part and he slips inside."
            show shawn reverse cowgirl vaginal back at stepback(0.1, 10, 5)
            play sound slide_in
            "Looking back over my shoulder, I see Shawn almost co cross-eyed at the sensation."
            "Then he kind of collapses backwards onto the bed, which I take as a good sign."
            "Because as I turn my head back, I can feel the same sensations overtaking me too."
            "Soon any sense of me being the one in charge begins to fade away."
            "It's not that Shawn's the one taking over in any sense."
            "More that he's rising to meet me in the middle as he moves beneath me."
            show shawn reverse cowgirl down at stepback(1.5, 0, -20)
            play sound slide_in
            "That and the way that his cock is moving inside of me too."
            show shawn reverse cowgirl up
            play sound slide_out
            "I'm starting to feel like someone riding a mechanical bull."
            show shawn reverse cowgirl down at stepback(1.5, 0, -20)
            play sound slide_in
            "Like I'm holding on tight in those first few moments when it moves gently."
            show shawn reverse cowgirl up
            play sound slide_out
            "Then the feeling of pleasure begins to build rapidly as Shawn picks up speed."
            show shawn reverse cowgirl down at stepback(1.5, 0, -20)
            play sound slide_in
            pause 1.5
            show shawn reverse cowgirl up
            play sound slide_out
            "And so I feel like the bull's now twisting and turning making me hold on tightly."
            "I respond in the only way that seems to make sense."
            show shawn reverse cowgirl down at stepback(1.5, 0, -20)
            play sound slide_in
            pause 1.5
            show shawn reverse cowgirl up
            play sound slide_out
            "Which is to dig in with my knees and ride it out to the end."
            "Hell, part of me wishes that I really did have a cowboy hat on right now."
            show shawn reverse cowgirl down at stepback(1.5, 0, -20)
            play sound slide_in
            pause 1.5
            show shawn reverse cowgirl up
            play sound slide_out
            "Because I'd be using it to whip away at Shawn in the blink of an eye!"
            show shawn reverse cowgirl down at stepback(1, 0, -20)
            play sound slide_in
            pause 1
            show shawn reverse cowgirl up
            play sound slide_out
            "But as I don't, I'll just have to make do with holding onto Shawn's thighs."
            show shawn reverse cowgirl down at stepback(1, 0, -20)
            play sound slide_in
            pause 1
            show shawn reverse cowgirl up smile
            play sound slide_out
            "That and grinding myself down onto him like my life depends on it."
            show shawn reverse cowgirl down at stepback(1, 0, -15)
            play sound slide_in
            pause 1
            show shawn reverse cowgirl up
            play sound slide_out
            "By now Shawn's thrusting in and out of me like a piston."
            show shawn reverse cowgirl down at stepback(0.5, 0, -15)
            play sound slide_in
            pause 0.5
            show shawn reverse cowgirl up
            play sound slide_out
            "Going so fast that I can hardly sense where he is from one second to the next."
            show shawn reverse cowgirl down at stepback(0.5, 0, -15)
            play sound slide_in
            pause 0.5
            show shawn reverse cowgirl up
            play sound slide_out
            "At this rate I'm worried that I'm going to pass out before I cum."
            show shawn reverse cowgirl down at stepback(0.5, 0, -15)
            play sound slide_in
            pause 0.5
            show shawn reverse cowgirl up pleasure
            play sound slide_out
            "But there's no sense in asking Shawn to slow down or go easy on me."
            show shawn reverse cowgirl down at stepback(0.3, 0, -15)
            play sound slide_in
            pause 0.3
            show shawn reverse cowgirl up
            play sound slide_out
            "Because I'm sure that he wouldn't hear me if I spoke up right now."
            show shawn reverse cowgirl down at stepback(0.3, 0, -15)
            play sound slide_in
            pause 0.3
            show shawn reverse cowgirl up
            play sound slide_out
            "So I just tighten my grip and redouble my efforts to hold on."
            show shawn reverse cowgirl down at stepback(0.3, 0, -15)
            play sound slide_in
            pause 0.3
            show shawn reverse cowgirl up
            play sound slide_out
            "And even as I do so, I can feel the pressure building up inside of me."
            show shawn reverse cowgirl down at stepback(0.3, 0, -15)
            play sound slide_in
            pause 0.3
            show shawn reverse cowgirl up
            play sound slide_out
            "Oh man...maybe I was wrong."
            show shawn reverse cowgirl down at stepback(0.3, 0, -15)
            play sound slide_in
            pause 0.3
            show shawn reverse cowgirl up ahegao
            play sound slide_out
            "I feel like I'm about to lose it any second!"
            call cum_reaction (shawn, 'vaginal', 1) from _call_cum_reaction_283

            if _return == "vaginal_condom":
                "As soon as I start to cum, I remember that we used protection."
                "Which makes me instantly push down even harder than before."
                show shawn reverse cowgirl down at stepback(0.3, 0, -15)
                play sound slide_in
                "Confident that I'm safe to do so, I make sure Shawn's as deep as possible."
                "Then I hold tight as he shoots his load into me and I'm swept away."
                scene bg white with dissolve
                pause 0.1
                show shawn reverse cowgirl vaginal with vpunch
                "And in the moments that follow, it's all I can do to stay upright."

            elif _return == "vaginal_outside":
                "As soon as I start to cum, I can feel that Shawn's about to do the same thing."
                "Which makes me instantly pull myself up and off of him."
                "The result is that Shawn's cock pops out of me just as he shoots his load."
                if CONDOM:
                    show shawn reverse cowgirl out with vpunch
                else:
                    show shawn reverse cowgirl out cumshot with vpunch
                play sound slide_out
                "Then I hold tight as my orgasm takes me and I'm swept away."
                if CONDOM:
                    show shawn reverse cowgirl out with vpunch
                else:
                    show shawn reverse cowgirl out -cumshot cum body with vpunch
                "And in the moments that follow, it's all I can do to stay upright."
            else:



                "As soon as I start to cum, I push down even harder than before."
                show shawn reverse cowgirl down at stepback(0.3, 0, -15)
                play sound slide_in
                "I make sure Shawn's as deep as possible, even digging my fingers into his thighs."
                "Then I hold tight as he shoots his load into me and I'm swept away."
                scene bg white with dissolve
                pause 0.1
                show shawn reverse cowgirl vaginal creampie with vpunch
                "And in the moments that follow, it's all I can do to stay upright."
        "Guide him to my ass":
            "Without hesitation, I begin to slide Shawn's cock between my thighs."
            "Or to be more specific, I slide the head between my buttocks."
            "Only after a couple more passes do I let any more of it touch me."
            "Adding a little more of the shaft each time, just enough to make him gasp."
            shawn.say "[hero.name]..."
            shawn.say "Are you..."
            shawn.say "Are you going to, you know...do it?"

            if hero.morality >= 25:
                bree.say "Oh, sorry, Shawn..."
                bree.say "We're going to do it, I promise!"

            if hero.morality <= -25:
                bree.say "Geez, Shawn..."
                bree.say "You're so desperate for my ass!"
            else:

                bree.say "Don't worry, Shawn..."
                bree.say "We're almost there!"
            "It's ironic Shawn would choose that exact moment to ask such a question."
            "Because almost the same moment he does so, things start to move down there."
            "I'm still rubbing his cock hard against my hole as I answer him."
            "And even before I'm finished, the muscles begin to relax and he slips inside."
            show shawn reverse cowgirl anal back at stepback(0.1, 10, 5)
            play sound slide_in
            "Looking back over my shoulder, I see Shawn almost co cross-eyed at the sensation."
            "Then he kind of collapses backwards onto the bed, which I take as a good sign."
            "Because as I turn my head back, I can feel the same sensations overtaking me too."
            "Soon any sense of me being the one in charge begins to fade away."
            "It's not that Shawn's the one taking over in any sense."
            "More that he's rising to meet me in the middle as he moves beneath me."
            show shawn reverse cowgirl down at stepback(1.5, 0, -20)
            play sound slide_in
            "That and the way that his cock is moving inside of me too."
            show shawn reverse cowgirl up
            play sound slide_out
            "I'm starting to feel like someone riding a mechanical bull."
            show shawn reverse cowgirl down at stepback(1.5, 0, -20)
            play sound slide_in
            "Like I'm holding on tight in those first few moments when it moves gently."
            show shawn reverse cowgirl up
            play sound slide_out
            "Then the feeling of pleasure begins to build rapidly as Shawn picks up speed."
            show shawn reverse cowgirl down at stepback(1.5, 0, -20)
            play sound slide_in
            pause 1.5
            show shawn reverse cowgirl up
            play sound slide_out
            "And so I feel like the bull's now twisting and turning making me hold on tightly."
            "I respond in the only way that seems to make sense."
            show shawn reverse cowgirl down at stepback(1.5, 0, -20)
            play sound slide_in
            pause 1.5
            show shawn reverse cowgirl up
            play sound slide_out
            "Which is to dig in with my knees and ride it out to the end."
            "Hell, part of me wishes that I really did have a cowboy hat on right now."
            show shawn reverse cowgirl down at stepback(1.5, 0, -20)
            play sound slide_in
            pause 1.5
            show shawn reverse cowgirl up
            play sound slide_out
            "Because I'd be using it to whip away at Shawn in the blink of an eye!"
            show shawn reverse cowgirl down at stepback(1, 0, -20)
            play sound slide_in
            pause 1
            show shawn reverse cowgirl up
            play sound slide_out
            "But as I don't, I'll just have to make do with holding onto Shawn's thighs."
            show shawn reverse cowgirl down at stepback(1, 0, -20)
            play sound slide_in
            pause 1
            show shawn reverse cowgirl up smile
            play sound slide_out
            "That and grinding myself down onto him like my life depends on it."
            show shawn reverse cowgirl down at stepback(1, 0, -15)
            play sound slide_in
            pause 1
            show shawn reverse cowgirl up
            play sound slide_out
            "By now Shawn's thrusting in and out of my like a piston."
            show shawn reverse cowgirl down at stepback(0.5, 0, -15)
            play sound slide_in
            pause 0.5
            show shawn reverse cowgirl up
            play sound slide_out
            "Going so fast that I can hardly sense where he is from one second to the next."
            show shawn reverse cowgirl down at stepback(0.5, 0, -15)
            play sound slide_in
            pause 0.5
            show shawn reverse cowgirl up
            play sound slide_out
            "At this rate I'm worried that I'm going to pass out before I cum."
            show shawn reverse cowgirl down at stepback(0.5, 0, -15)
            play sound slide_in
            pause 0.5
            show shawn reverse cowgirl up pleasure
            play sound slide_out
            "But there's no sense in asking Shawn to slow down or go easy on me."
            show shawn reverse cowgirl down at stepback(0.3, 0, -15)
            play sound slide_in
            pause 0.3
            show shawn reverse cowgirl up
            play sound slide_out
            "Because I'm sure that he wouldn't hear me if I spoke up right now."
            show shawn reverse cowgirl down at stepback(0.3, 0, -15)
            play sound slide_in
            pause 0.3
            show shawn reverse cowgirl up
            play sound slide_out
            "So I just tighten my grip and redouble my efforts to hold on."
            show shawn reverse cowgirl down at stepback(0.3, 0, -15)
            play sound slide_in
            pause 0.3
            show shawn reverse cowgirl up
            play sound slide_out
            "And even as I do so, I can feel the pressure building up inside of me."
            show shawn reverse cowgirl down at stepback(0.3, 0, -15)
            play sound slide_in
            pause 0.3
            show shawn reverse cowgirl up
            play sound slide_out
            "Oh man...maybe I was wrong."
            show shawn reverse cowgirl down at stepback(0.3, 0, -15)
            play sound slide_in
            pause 0.3
            show shawn reverse cowgirl up ahegao
            play sound slide_out
            "I feel like I'm about to lose it any second!"
            call cum_reaction (shawn, 'anal', 1) from _call_cum_reaction_284

            if _return == "anal_inside":
                "As soon as I start to cum, I push down even harder than before."
                "I make sure Shawn's as deep as possible, even digging my fingers into his thighs."
                "Then I hold tight as he shoots his load into me and I'm swept away."
                scene bg white with dissolve
                pause 0.1
                show shawn reverse cowgirl anal creampie with vpunch
                "And in the moments that follow, it's all I can do to stay upright."
            else:

                "As soon as I start to cum, I can feel that Shawn's about to do the same thing."
                "Which makes me instantly pull myself up and off of him."
                "The result is that Shawn's cock pops out of my ass just as he shoots his load."
                if CONDOM:
                    show shawn reverse cowgirl out with vpunch
                else:
                    show shawn reverse cowgirl out cumshot with vpunch
                play sound slide_out
                "Then I hold tight as my orgasm takes me and I'm swept away."
                if CONDOM:
                    show shawn reverse cowgirl out with vpunch
                else:
                    show shawn reverse cowgirl out -cumshot cum body with vpunch
                "And in the moments that follow, it's all I can do to stay upright."
    "Once we're both spent, I finally let go of Shawn, letting my muscles go slack."
    "This means that I slide off him and flop sideways onto the bed, totally limp."
    "Luckily for me, Shawn seems to be in pretty much the same state."
    "So nobody complains as we just lie there, utterly spent but totally satisfied."
    return

label shawn_fuck_date_female_doggy:
    $ game.room = "bedroom4"
    scene bg bedroom4
    show shawn naked smile at center, zoomAt(1.5, (640, 1080))
    with fade
    "Sometimes it can be hard to make up my mind as to exactly what I want from a guy in the bedroom."
    "And then there's the additional problem of plucking up the courage to ask for it too."
    "But for some reason none of that seems to be affecting me right now."
    "Instead I feel like my mind is totally clear, that I know exactly what I want as well."
    "And I don't waste a moment thinking about how I'm going to ask for it either."
    "I just start stripping off my clothes as I walk over to the bed and climb onto it."
    show shawn surprised
    shawn.say "...[hero.name]..."
    shawn.say "What are you doing?"
    show shawn smile
    "By the time Shawn manages to get the words out of his mouth, I'm already on the bed."
    "And I can't help chuckling, because it's so blatantly obvious what's happening."
    "Shawn must be so into what he's seeing that his lust is interfering with his brain!"

    if hero.morality >= 25:
        bree.say "I...I don't know what's come over me, Shawn."
        bree.say "Just that...I really want you!"

    if hero.morality <= -25:
        bree.say "What does it look like, Shawn?"
        bree.say "That I'm wiping my ass with a brick?"
    else:

        bree.say "Isn't it bloody obvious, Shawn?"
        bree.say "Do you need me to actually rub my pussy in your face before you get it?!?"
    "I'm looking back over my shoulder as I say this to Shawn."
    "And at the same time I'm pulling down my panties too."
    "Which I make a point of balling up and throwing straight at him."
    "This seems to catch him off-guard, as he flinches and take a step backwards."
    "But he also manages to catch the panties before they hit him in the face."
    scene bg black
    show shawn doggy nonpc opened
    with fade

    if hero.morality >= 25:
        bree.say "I...I hope you like those, Shawn?"
        bree.say "You made me so excited that they're totally wet..."

    if hero.morality <= -25:
        bree.say "You feel how wet my panties are, Shawn?"
        bree.say "Just think what state my pussy's in by now!"
    else:

        bree.say "Now are you going to get over here and join me?"
        bree.say "Or do you need me to actually order you to fuck me?"
    show shawn doggy nonpc normal
    "Shawn's nodding as he starts toward the bed, finally stirred into action."
    "He doesn't manage to take off all of his clothes before he reaches me."
    "But this means that I get to watch him wresting his way out of his shorts as he does so."
    "And I can already see that the little show I've put on for him has had the desired effect."
    "Because I can see the head of his cock as it bobs this way and that, slowly rising to attention."
    shawn.say "Sure, [hero.name]..."
    shawn.say "I'll be right there..."
    shawn.say "Just let me...get onto the...the bed!"
    "As Shawn pulls off the last of his clothes, he seems to trip over his own feet."
    "This means that he stumbles as he climbs onto the bed, falling towards me."
    "Without thinking, he reaches out with his hands, trying to keep from toppling over."
    show shawn doggy -nonpc out far with hpunch
    "But in doing so, Shawn stumbles roughly into me, his groin slapping against my ass."
    show shawn doggy hand
    "At the same time he grabs hold of my haunches, gripping me tightly."
    "The effect is quite something, making my eyes bulge in their sockets."
    "That's because for a moment I feel like he's going to slide straight into me."
    "And in the moment, my growing desires become almost too much to control."
    "Before I know it, I'm leaning backward and into Shawn."
    "Rubbing my ass into his groin, like I'm some kind of horny animal."
    show shawn doggy opened

    if hero.morality >= 25:
        bree.say "Sorry, Shawn..."
        bree.say "I don't know what's come over me!"

    if hero.morality <= -25:
        bree.say "Ah..."
        bree.say "Guess I want it more than I thought!"
    else:

        bree.say "Of fuck..."
        bree.say "I need you inside of me, and quick!"
    show shawn doggy normal
    "Of course Shawn's nodding away, eager to do whatever I ask of him."
    "But I can still see that there's a little hesitation in his expression."
    "Like he's waiting for me to be more specific with what I want him to do to me."
    menu:
        "spank me !":
            "I know that I should be thinking about where I want it right now."
            "But for some reason my brain is still hung up on the sensation of Shawn's thighs against my ass."
            "The feeling of his skin slapping against mine just won't fade from my mind."
            "And in that moment I know that I need to feel more of it before we do anything else."
            "I know that I want him to take the time to slap my ass."
            "Not just to gently tap it either - I really want him to spank me hard!"
            "But now I have to figure out how best to actually ask Shawn to do it."
            "Though the only solution that comes to mind is the most obvious."
            show shawn doggy opened

            if hero.morality >= 25:
                bree.say "Oh, Shawn..."
                bree.say "Would you..."
                bree.say "Would you maybe...spank me a little?"

            if hero.morality <= -25:
                bree.say "Shawn..."
                bree.say "I've been such a naughty girl, so dirty too..."
                bree.say "And I need you to spank me!"
            else:

                bree.say "Ah, Shawn..."
                bree.say "This might sound a bit random..."
                bree.say "But I could really go for a spanking right now!"
            show shawn doggy normal
            "I make sure to look back over my shoulder at Shawn as I say this."
            "And it's plain to see that the request has stopped him dead in his tracks."
            "Shawn's staring at me, his mouth hanging open with what I take to be amazement."
            "Unsure as to how he's going to react, I make a point of wiggling my butt."
            "Which seems to be all the encouragement he needed."
            "Because no more than a second later, Shawn leaps into action."
            "Without a single word, he raises one hand."
            "And then he swings his open palm in an arc towards my waiting buttocks."
            show shawn doggy -hand
            pause 0.3
            show shawn doggy hand shake closed moan
            play sound spank
            with vpunch
            pause 0.3
            show shawn doggy -shake back normal
            "The sound that follows seems to totally fill my senses."
            "A huge crack, like the sound-effect they always use for a whip in the movies."
            "I instinctively leap forwards a little, gasping in surprise."
            show shawn doggy -hand
            pause 0.3
            show shawn doggy hand shake closed opened
            play sound spank
            with vpunch
            pause 0.3
            show shawn doggy -shake back normal
            "Shawn's delivering the second slap just as I feel the sensation of the first."
            "But it's not like the pain of being struck, at least not exactly."
            "This feels warmer and more intense."
            "A wave of sensation that spreads out to engulf me."
            "And as soon as I feel it dissipating, I know that I want more."
            "So I guess it's a good thing that Shawn's not holding back."
            "Because the second wave comes close on the heels of the first."
            show shawn doggy -hand
            pause 0.3
            show shawn doggy hand shake closed opened
            play sound spank
            with vpunch
            pause 0.3
            show shawn doggy -shake back moan
            "From then on I begin to lose the ability to tell one slap from the next."
            "All I can do is lean into the experience, loving every second that it lasts."
            show shawn doggy -hand
            pause 0.3
            show shawn doggy hand shake closed opened
            play sound spank
            with vpunch
            pause 0.1
            show shawn doggy -shake back moan
            "I can feel the cheeks on my face burning with the thrill of it all."
            show shawn doggy -hand
            pause 0.1
            show shawn doggy hand shake closed opened
            play sound spank
            with vpunch
            pause 0.1
            show shawn doggy -shake pleasure moan
            "And I can only imagine how red the cheeks on my ass must be by now!"
            show shawn doggy -hand
            pause 0.1
            show shawn doggy hand shake closed opened
            play sound spank
            with vpunch
            pause 0.1
            show shawn doggy -hand -shake pleasure moan
            shawn.say "Urgh..."
            shawn.say "Oh wow, [hero.name]..."
            shawn.say "I think that's enough spanking for now."
            shawn.say "Like, I can't actually feel my hand anymore!"
        "fuck me right now":
            pass
    menu:
        "Guide him to my pussy":
            "I can see that Shawn's already in position and prepared to go."
            "And the moment that I think about it, I know exactly what I want."
            "So I don't hesitate to press my ass backwards and against him."
            "Making sure that his manhood is trapped between my thighs too."
            call check_condom_usage (shawn) from _call_check_condom_usage_148
            if _return == False:
                return "leave"
            if CONDOM:
                show shawn doggy condom with fade
            "Almost the same moment I feel Shawn's hands on my haunches, I spring into action."
            "My body moves instinctively, lowering just a little so as to make sure he's on target."
            "And I can't help shuddering with pleasure as the head of his cock slides over the lips of my pussy."
            menu:
                "Use butt-plug":
                    "At what feels like the last possible moment, I remember what's under the bed."
                    "And so I reach down and feel around for it, searching for something to sweeten the deal."
                    "Shawn looks over my shoulder, puzzled as to what's going on."
                    "But then I shove my prize into his hand, motioning towards my ass."
                    shawn.say "...[hero.name]..."
                    shawn.say "This is..."
                    shawn.say "This is a butt-plug!"
                    show shawn doggy opened wink

                    if hero.morality >= 25:
                        bree.say "I..."
                        bree.say "I know it is, Shawn - please use it on me?"

                    if hero.morality <= -25:
                        bree.say "You bet it is!"
                        bree.say "Now what are you waiting for?"
                        bree.say "Shove it in my fucking ass already!"
                    else:

                        bree.say "It is?!?"
                        bree.say "I thought it was a paperweight!"
                        bree.say "Of course I know what it is, and I know where I want it too!"
                    show shawn doggy normal -wink
                    "Shawn nods as he grabs the butt-plug from my hand."
                    "Then he gets to work doing as I asked."
                    "I feel the sensation of the plug being worked between my butt-cheeks."
                    "And then I close my eyes, gasping as it's pushed into my hole."
                    show shawn doggy buttplug
                    "The feeling is incredible, making me feel instantly twice as horny as before."
                    "It's all I can do to keep my mind focussed on getting Shawn to fuck me."
                    $ hero.flags.buttplug = True
                "Do not use butt-plug":
                    "For a moment I think about spicing things up a little."
                    "About reaching for one of the toys under the bed."
                    "But then the head of Shawn's cock pressed hard against my pussy."
                    "It makes me gasp, and all thought of anything else vanishes instantly."
                    "In that moment, all I want is to get his cock inside of me as quickly as possible!"
            "Part of me is sure that I'm going to have to be the one to take the lead with Shawn."
            "That he'll need me to take him by the hand and show him what I want him to do to me."
            "So it comes as a surprise a moment later when I feel him begin to move without my saying a word."
            "The first thing I feel is the sensation of his grip tightening and being pulled backwards."
            "Then my lips part and I let out a moan of pure and unadulterated pleasure."
            show shawn doggy opened
            bree.say "Oh..."
            bree.say "Oh fuck..."
            show shawn doggy normal
            "And that's because of the way his cock is pressing against my pussy."
            "It's neither too hard, nor lacking in force - it's just right."
            "Then Shawn adds to the perfection that I'm feeling by beginning to move."
            "Just a little at first, moving the head of his cock back and forth."
            "But it's more than enough to do the trick, as I feel myself begin to melt."
            "Everything below my waist feels like it's softening, becoming loose."
            "And so it's no surprise when, a moment later, I feel myself starting to open."
            show shawn doggy moan
            "I'm gasping as Shawn begins to inch his way into me."
            show shawn doggy vaginal with fade
            "Nodding eagerly as he slowly fills my pussy with his manhood."
            "The muscles inside of me want to squeeze him hard."
            show shawn doggy near at stepback(0.05, -10, 0)
            "To grab hold of him and then never let go."
            "But that would stop the natural flow of what's happening here."
            show shawn doggy far
            "And it'd mean that things would stay right where they are too."
            "That's not going to cut it for me, not when what I really want is more!"
            show shawn doggy near at stepback(0.05, -10, 0)
            "So instead I force myself to relax, holding back and letting Shawn dictate the pace."
            "And it doesn't take me long to be rewarded for putting my trust in him."
            show shawn doggy far
            "At first Shawn seems to be overly eager to make it all the way inside."
            "Almost like he's hurrying for fear of his prize being taken away before he can claim it."
            show shawn doggy near at stepback(0.05, -10, 0)
            "But then I feel the subtle change in him that reassures me."
            show shawn doggy far
            "He slows his pace just a little, and seems to concentrate on what he's doing."
            show shawn doggy near at stepback(0.05, -10, 0)
            "And that's when I feel like the top of my head is going to blow off!"
            show shawn doggy far
            "Seriously, I can't put my finger on just what it is that Shawn does."
            show shawn doggy near at stepback(0.05, -10, 0)
            "But he does it so well that I feel like biting down on a pillow."
            show shawn doggy far
            "Before I was indulging him, letting him have his way for the sake of my own pleasure."
            show shawn doggy near at stepback(0.05, -10, 0)
            "Now the difference is that I couldn't assert myself even if I wanted to."
            show shawn doggy far
            "What Shawn's doing to me is so intense that I can only surrender myself to it."
            show shawn doggy near at stepback(0.05, -10, 0)
            pause 1
            show shawn doggy far
            "Without a conscious thought, I spread my legs and lower my body down."
            show shawn doggy near bodyheat at stepback(0.05, -10, 0)
            pause 1
            show shawn doggy far
            "Anything that I can manage to let him get deeper into me."
            show shawn doggy near at stepback(0.05, -10, 0)
            pause 1
            show shawn doggy far
            "Anything that will make his motion inside of me smoother still."
            show shawn doggy near heat at stepback(0.05, -10, 0)
            pause 1
            show shawn doggy far
            pause 1
            show shawn doggy near at stepback(0.05, -10, 0)
            pause 1
            show shawn doggy far
            "More than once I think that I'm going to cum in the next second."
            show shawn doggy near mc_sweat at stepback(0.05, -10, 0)
            pause 0.5
            show shawn doggy far
            pause 0.5
            show shawn doggy near at stepback(0.05, -10, 0)
            pause 0.5
            show shawn doggy far
            pause 0.5
            show shawn doggy near at stepback(0.05, -10, 0)
            pause 0.5
            show shawn doggy far
            pause 0.5
            "That I'll collapse into a pool of helpless flesh before Shawn's done with me."
            show shawn doggy near shake backsweat frontsweat with hpunch
            pause 0.1
            show shawn doggy -shake -backsweat -frontsweat
            show shawn doggy far
            pause 0.1
            show shawn doggy near shake backsweat frontsweat with hpunch
            pause 0.1
            show shawn doggy -shake -backsweat -frontsweat
            show shawn doggy far
            pause 0.1
            show shawn doggy near shake backsweat frontsweat with hpunch
            pause 0.1
            show shawn doggy -shake -backsweat -frontsweat
            show shawn doggy far
            pause 0.1
            show shawn doggy pleasure ahegao squirt with hpunch
            "And when my orgasm finally hits, it makes every muscle in my body quiver helplessly."
            if hero.flags.buttplug:
                "It's then that Shawn seems to remember something I've forgotten."
                "Because I feel a sudden sensation of pressure in my ass."
                "Then there's a loud popping sound, and I realise what it is."
                play sound pop_out
                show shawn doggy -buttplug with vpunch
                "He's pulling the butt-plug out of my ass - and it's making me lost it all over again!"
            call cum_reaction (shawn, 'vaginal', 1) from _call_cum_reaction_280

            if _return == "vaginal_condom":
                "Right now I'm so glad we remembered to use a condom."
                "Because it means that I can just sit back and enjoy the ride."
                "And that's exactly what I do, letting nature take it's course."
                show shawn doggy near shake backsweat frontsweat creampie with hpunch
                "Shawn shoots his load one moment, and the next I'm swept along with him."
                with hpunch
                "Grabbing onto the bedclothes for dear life as my orgasm takes hold."
                with hpunch
                "And afterwards, my arms and legs seem unable to support my weight."
                "So as they give way, I collapse into a heap on the bed."
            elif _return == "vaginal_inside_pill":

                "Right now I'm so glad I'm on the pill."
                "Because it means that I can just sit back and enjoy the ride."
                "And that's exactly what I do, letting nature take it's course."
                show shawn doggy near shake backsweat frontsweat creampie with hpunch
                "Shawn shoots his load one moment, and the next I'm swept along with him."
                with hpunch
                "Grabbing onto the bedclothes for dear life as my orgasm takes hold."
                "And afterwards, my arms and legs seem unable to support my weight."
                with hpunch
                "So as they give way, I collapse into a heap on the bed."

            elif _return == "vaginal_inside_pregnant":
                "Right now I'm so glad that I'm pregnant."
                "Because it means that I can just sit back and enjoy the ride."
                "And that's exactly what I do, letting nature take it's course."
                show shawn doggy near shake backsweat frontsweat creampie with hpunch
                "Shawn shoots his load one moment, and the next I'm swept along with him."
                with hpunch
                "Grabbing onto the bedclothes for dear life as my orgasm takes hold."
                "And afterwards, my arms and legs seem unable to support my weight."
                with hpunch
                "So as they give way, I collapse into a heap on the bed."

            elif _return == "vaginal_outside":
                "I know that I need Shawn to pull out of me before it's too late."
                "Because once he's done that I can just sit back and enjoy the ride."
                show shawn doggy out with hpunch
                "And that's exactly what I do, crawling forwards so that he slides out of me."
                show shawn doggy cumshot with hpunch
                "Shawn shoots his load the moment that his cock pops out of my pussy."
                show shawn doggy cum onbody with hpunch
                "But the sensation pushes me over the edge too, making me hold still as it seizes me."
                "Afterwards, my arms and legs seem unable to support my weight."
                "So as they give way, I collapse into a heap on the bed."
            else:

                "There's nothing I can do but sit back and enjoy the ride."
                "And that's exactly what I do, letting nature take it's course."
                show shawn doggy near shake backsweat frontsweat creampie with hpunch
                "Shawn shoots his load one moment, and the next I'm swept along with him."
                with hpunch
                "Grabbing onto the bedclothes for dear life as my orgasm takes hold."
                with hpunch
                "And afterwards, my arms and legs seem unable to support my weight."
                "So as they give way, I collapse into a heap on the bed."
        "Guide him to my ass":
            "I can see that Shawn's already in position and prepared to go."
            "And the moment that I think about it, I know exactly what I want."
            "So I don't hesitate to press my ass backwards and against him."
            "Making sure that his manhood is trapped between my butt-cheeks too."
            "Almost the same moment I feel Shawn's hands on my haunches, I spring into action."
            "My body moves instinctively, lowering just a little so as to make sure he's on target."
            "And I can't help shuddering with pleasure as the head of his cock presses against my hole."
            "Part of me is sure that I'm going to have to be the one to take the lead with Shawn."
            "That he'll need me to take him by the hand and show him what I want him to do to me."
            "So it comes as a surprise a moment later when I feel him begin to move without my saying a word."
            "The first thing I feel is the sensation of his grip tightening and being pulled backwards."
            "Then my lips part and I let out a moan of pure and unadulterated pleasure."
            show shawn doggy opened
            bree.say "Oh..."
            bree.say "Oh fuck..."
            show shawn doggy normal
            "And that's because of the way his cock is pushing into my ass."
            "It's neither too hard, nor lacking in force - it's just right."
            "Then Shawn adds to the perfection that I'm feeling by beginning to move."
            "Just a little at first, moving the head of his cock back and forth."
            "But it's more than enough to do the trick, as I feel myself begin to melt."
            "Everything below my waist feels like it's softening, becoming loose."
            "And so it's no surprise when, a moment later, I feel myself starting to open."
            show shawn doggy moan
            "I'm gasping as Shawn begins to inch his way into me."
            show shawn doggy anal with fade
            "Nodding eagerly as he slowly fills my ass with his manhood."
            "The muscles inside of me want to squeeze him hard."
            show shawn doggy near at stepback(0.05, -10, 0)
            "To grab hold of him and then never let go."
            "But that would stop the natural flow of what's happening here."
            show shawn doggy far
            "And it'd mean that things would stay right where they are too."
            "That's not going to cut it for me, not when what I really want is more!"
            show shawn doggy near at stepback(0.05, -10, 0)
            "So instead I force myself to relax, holding back and letting Shawn dictate the pace."
            "And it doesn't take me long to be rewarded for putting my trust in him."
            show shawn doggy far
            "At first Shawn seems to be overly eager to make it all the way inside."
            "Almost like he's hurrying for fear of his prize being taken away before he can claim it."
            show shawn doggy near at stepback(0.05, -10, 0)
            "But then I feel the subtle change in him that reassures me."
            show shawn doggy far
            "He slows his pace just a little, and seems to concentrate on what he's doing."
            show shawn doggy near at stepback(0.05, -10, 0)
            "And that's when I feel like the top of my head is going to blow off!"
            show shawn doggy far
            "Seriously, I can't put my finger on just what it is that Shawn does."
            show shawn doggy near at stepback(0.05, -10, 0)
            "But he does it so well that I feel like biting down on a pillow."
            show shawn doggy far
            "Before I was indulging him, letting him have his way for the sake of my own pleasure."
            show shawn doggy near at stepback(0.05, -10, 0)
            "Now the difference is that I couldn't assert myself even if I wanted to."
            show shawn doggy far
            "What Shawn's doing to me is so intense that I can only surrender myself to it."
            show shawn doggy near at stepback(0.05, -10, 0)
            pause 1
            show shawn doggy far
            "Without a conscious thought, I spread my legs and lower my body down."
            show shawn doggy near bodyheat at stepback(0.05, -10, 0)
            pause 1
            show shawn doggy far
            "Anything that I can manage to let him get deeper into me."
            show shawn doggy near at stepback(0.05, -10, 0)
            pause 1
            show shawn doggy far
            "Anything that will make his motion inside of me smoother still."
            show shawn doggy near heat at stepback(0.05, -10, 0)
            pause 1
            show shawn doggy far
            pause 1
            show shawn doggy near at stepback(0.05, -10, 0)
            pause 1
            show shawn doggy far
            "More than once I think that I'm going to cum in the next second."
            show shawn doggy near mc_sweat at stepback(0.05, -10, 0)
            pause 0.5
            show shawn doggy far
            pause 0.5
            show shawn doggy near at stepback(0.05, -10, 0)
            pause 0.5
            show shawn doggy far
            pause 0.5
            show shawn doggy near at stepback(0.05, -10, 0)
            pause 0.5
            show shawn doggy far
            pause 0.5
            "That I'll collapse into a pool of helpless flesh before Shawn's done with me."
            show shawn doggy near shake backsweat frontsweat with hpunch
            pause 0.1
            show shawn doggy -shake -backsweat -frontsweat
            show shawn doggy far
            pause 0.1
            show shawn doggy near shake backsweat frontsweat with hpunch
            pause 0.1
            show shawn doggy -shake -backsweat -frontsweat
            show shawn doggy far
            pause 0.1
            show shawn doggy near shake backsweat frontsweat with hpunch
            pause 0.1
            show shawn doggy -shake -backsweat -frontsweat
            show shawn doggy far
            pause 0.1
            show shawn doggy pleasure ahegao squirt with hpunch
            "And when my orgasm finally hits, it makes every muscle in my body quiver helplessly."
            call cum_reaction (shawn, 'anal', 1) from _call_cum_reaction_281

            if _return == "anal_inside":
                "There's nothing I can do but sit back and enjoy the ride."
                "And that's exactly what I do, letting nature take it's course."
                show shawn doggy near shake backsweat frontsweat creampie with hpunch
                "Shawn shoots his load one moment, and the next I'm swept along with him."
                with hpunch
                "Grabbing onto the bedclothes for dear life as my orgasm takes hold."
                with hpunch
                "And afterwards, my arms and legs seem unable to support my weight."
                "So as they give way, I collapse into a heap on the bed."
            else:

                "I know that I want Shawn to pull out of me before it's too late."
                "Because once he's done that I can just sit back and enjoy the ride."
                "And that's exactly what I do, crawling forwards so that he slides out of me."
                show shawn doggy out with hpunch
                play sound pop_out
                pause 0.1
                show shawn doggy cumshot with hpunch
                "Shawn shoots his load the moment that his cock pops out of my ass."
                show shawn doggy cum onbody with hpunch
                "But the sensation pushes me over the edge too, making me hold still as it seizes me."
                with hpunch
                "Afterwards, my arms and legs seem unable to support my weight."
                "So as they give way, I collapse into a heap on the bed."
    return


label shawn_sleep_date_fuck_female(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom4
        show shawn naked smile at center, zoomAt(1.5, (640, 1080))
        with fade
        menu:
            "You should leave":
                bree.say "I am done with you and I have to get up early tomorrow, you should leave."
                "The sex was beyond incredible."
                show shawn naked normal
                "Frowning a little, Shawn straightens and shrugs, then goes to collect his clothes from where he'd let it fall earlier."
                "He then heads up the stairs."
                $ shawn.love -= 1
                $ shawn.sub += 1
                call sleep from _call_sleep_115
            "You should sleep here":
                bree.say "You can stay and sleep here."
                "I say, my voice a little shaky."
                "We curl up spooning together in bed, drifting toward sleep."
                $ shawn.love += 1
                call sleep ("shawn") from _call_sleep_116
    return

label shawn_cinema_sex_female:
    scene bg cinema with fade
    "One of the great things about dating Shawn is that I never have to talk him into going to the movies."
    "You know how some guys are, right?"
    "They only ever want to go to a bar or a nightclub?"
    "And even when they're there with you, they're still trying to show off?"
    "Well that's the total opposite of Shawn, who's a film nerd of the very highest degree."
    "Plus the fact that he's also a nerd in general means that he's glad to even be on a date in the first place."
    "And so I can pretty much guarantee that all of his attention is going to be on me the whole time."
    scene buy_popcorn_bg_01 at center, zoomAt(1.25, (800, 900))
    show shawn nice at center, zoomAt(1.25, (640, 920))
    shawn.say "So..."
    shawn.say "What do you actually want to see, [hero.name]?"
    show shawn smile
    "Shawn and I are standing in the lobby of the multiplex as he asks me this."
    "And we're staring at all of the glossy, exciting posters of the movies showing right now."
    "Because we agreed to make the decision what to see when we got here."
    "You know, to be totally spontaneous and exciting?"
    bree.say "Hmmm..."
    bree.say "Normally I'd just choose a sci-fi film and go with that."
    bree.say "But there doesn't seem to be one of those showing."
    show shawn sad
    "Shawn nods, and I can see that he's feeling my pain."
    show shawn sadsmile
    shawn.say "Tell me about it, [hero.name]!"
    shawn.say "Nothing fantasy and no anime either."
    shawn.say "Just promise me we don't have to see a romcom, yeah?"
    show shawn normal
    "I can't help wrinkling my nose at the mere mention of the idea."
    "And to make sure the message is clear, I stick a finger in my mouth."
    "Then I mime throwing up in total disgust."
    bree.say "Bleurgh!"
    bree.say "No worries there, Shawn!"
    "It's as I look up from this gesture that I see something interesting."
    bree.say "Oh..."
    bree.say "What about this one?"
    "Shawn takes a closer look at the poster I'm pointing to."
    "And when he recognises it, I see his eyes almost pop out of his head."
    show shawn surprised
    shawn.say "'Fifty Shades of Beige'?!?"
    shawn.say "But, [hero.name]..."
    shawn.say "Isn't that the one with all the crazy bondage stuff in it?"
    show shawn stuned
    bree.say "That's the one."
    show shawn complain
    shawn.say "The same one that was like..."
    shawn.say "Like, based on a really awful piece of fan-fiction?"
    show shawn normal
    bree.say "The very same!"
    "Shawn looks like he's fast running out of things to object to."
    "And I can see that he's looking from me to the poster then back again."
    "Most likely he's weighing up how much he doesn't want to see that film."
    "But at the same time, he's also balancing that with the fact he'll be doing it with me."
    show shawn sadsmile
    shawn.say "It's..."
    shawn.say "It's not my kind of film, [hero.name]..."
    show shawn normal
    "I'm nodding, but not in the kind of way that would suggest I'm agreeing with Shawn."
    "More in the kind of way that's intended to gently push him along to the right conclusion."
    bree.say "But..."
    bree.say "As you're here with me?"
    "I cock my head on one side, waiting for Shawn to catch on."
    show shawn nice
    shawn.say "As I'm here with you..."
    shawn.say "I...I'm willing to..."
    shawn.say "Make an exception?"
    show shawn smile
    "I make a point of smiling sweetly and taking hold of Shawn's hand."
    bree.say "Oh, Shawn..."
    bree.say "That's so nice of you!"
    "Before Shawn can really think things through, I wall him towards the box office."
    "And to be honest, he still looks a little confused when we buy tickets for the movie."
    "Almost like his brain is only now starting to catch up and realise what he agreed to."
    "Of course this means that I have to usher him into the theatre quickly."
    scene cinemaroom with fade
    "And so I steer him to the very back row, where we'll have some privacy."
    "But just as I get Shawn sitting in his seat, he seems to snap back to reality."
    show shawn surprised at center, zoomAt(1.25, (640, 920))
    shawn.say "What the..."
    shawn.say "How did..."
    shawn.say "[hero.name], do you have psychic powers or something?!?"
    show shawn stuned
    bree.say "Shhh..."
    bree.say "The film's starting!"
    scene cinemaroom at dark with fade
    "Shawn looks suitably chastened by my warning."
    "And he slides down in his seat, trying to avoid being seen."
    "Which works out pretty well, as it means I can devote all of my attention to the film."
    "But I do have to say that it doesn't take me long to realise Shawn was kind of right."
    "There's no real plot to it, and the acting is pretty bloody awful too."
    "Though I can see why so many people want to see it."
    "Because despite how bad it is, there's a hell of a lot of sexy stuff going."
    "In fact, I can feel myself starting to squirm a little in my seat."
    "Because all of the sexiness on the screen is beginning to get me hot too!"
    "Feeling a little self-conscious, I steal a glance in Shawn's direction."
    "And I'm just in time to see him rubbing a hand on his groin!"
    "He jumps in his seat the second he realises I'm watching him."
    "His hands clamping down on the arms of the seat."
    bree.say "Shawn..."
    bree.say "Were you..."
    shawn.say "Erm..."
    shawn.say "No way, [hero.name]!"
    bree.say "Then what were you doing with your hand just now?"
    shawn.say "I was just..."
    shawn.say "Just adjusting things down there, you know?"
    shawn.say "I have a really tight pair of shorts on today!"

    if hero.morality <= -25:
        "I can't help letting out a pretty dirty laugh at Shawn's explanation."
        "Because it's totally obvious what's really going on here."
        "He was stroking himself on account of getting really turned-on."
        "And the thought of that is turning me on even more than I already am!"
        bree.say "Oh no, poor baby!"
        bree.say "Let me help to ease the pressure..."
        "Before Shawn can object, I lean over and unzip his flies."
        $ renpy.music.set_pan(-0.5, 0, channel='sound')
        play sexsfx1 pants_unzip
        "And I have a hand in there a few seconds later."
        "Shawn begins to react a moment too late, tyring to pull it out."
        "But then he realises that he's going to make a scene."
        "So he just shuts his mouth and leaves me to it."
    else:
        "I totally get where Shawn's coming from."
        "It's not the easiest of things to admit that you're getting turned-on in public."
        "But I'm feeling the same way too, and we're totally alone on the back row."
        "Plus the knowledge that he's feeling the same way as me is making things worse!"
        "So I lean over and gently place a hand where his was a few moments before."
        bree.say "It's okay, Shawn..."
        bree.say "I'm feeling pretty horny too!"
        "Shawn looks down at my hand, then back up at me."
        "And I can see a mixture of surprise and relief in his eyes."
        shawn.say "B...[hero.name]..."
        shawn.say "Do you think..."
        shawn.say "Maybe we could..."
        bree.say "Sure thing, Shawn..."
        bree.say "Leave it to me, okay?"
        $ renpy.music.set_pan(-0.5, 0, channel='sound')
        play sexsfx1 pants_unzip
        "I'm unzipping Shawn's flies and sliding a hand in there all the time I'm saying this."
    "Slipping out of my seat, I pull Shawn's cock out of his pants."
    "It pops up, already hard and standing to attention."
    "Looks like he was even more aroused than I thought!"
    "The sight of his manhood makes me all the more determined."
    "Before now I wanted it, but having seen it, I now feel like I need it."
    "I hold onto Shawn's cock with one hand and pull down my panties with the other."
    "And then I slowly lower myself into his lap and onto him."
    scene bg black
    show shawn cowgirl cinema at dark
    with fade
    "The need that I'm feeling for Shawn means there's no foreplay required."
    "That and the dangerous excitement of doing it in the movie theatre has already affected me."
    "Or to be more precise, it's made sure that I'm slick and supple down below."
    "I was sure that the dangers of doing it here were firmly on my mind."
    "That I was ready to keep the noise down and get on with the task at hand."
    "But the moment the head of Shawn's cock touches my lips, I gasp in sheer pleasure."
    "This earns me a round of annoyed grumbles and urges to be silent."
    "Though luckily it doesn't make anyone get out of their seat to investigate."
    "Biting my lip, I keep right on lowering myself onto Shawn."
    "And it's a relief when I feel his hands take hold of me too."
    "This means that I can relax and let him slide all the way into me."
    show shawn cowgirl opened vaginal
    "The sensation is incredible, bringing an instant feeling of relief."
    "I could stay right here, just enjoying him being all the way inside."
    "But it doesn't seem like that's enough for Shawn."
    "A moment later he begins to thrust upwards from below."
    "And that sense of satisfaction vanishes as he gives me more."
    "In it's place I feel a mounting need for my appetites to be met."
    "It's like the more he gives me the more I want."
    "Steadying myself on the seats around us, I push down as best I can."
    show shawn cowgirl speed with vpunch
    "Shawn responds by thrusting harder than ever, making me bite down on my lip."
    "All the time he's fucking me, I'm looking straight at the big screen."
    "It just so happens that the heroine of the film is getting the same treatment."
    "And I watch helplessly as the hero pumps her at the same time as Shawn fucks me."
    "The sounds of the sex scene in the movie help to cover for us."
    "I even feel like I can let a few low moans escape from my lips too."
    "I don't know if Shawn can even see what's happening in the movie."
    "But somehow he seems to be thrusting almost in time with it."
    "This means I have the odd sensation of being connected to the heroine."
    "And as her hands roam over her body, I swear I can feel it too."
    with hpunch
    "As she reaches her cinematic climax, I push down hard on Shawn."
    "My reward is to hear him groan and then begin to shudder beneath me."
    show shawn cowgirl creampie with hpunch
    "The next thing I know, he's shooting his load into my pussy."
    show shawn cowgirl pleasure ahegao -speed with hpunch
    "My orgasm comes moments after his, totally overwhelming my senses."
    "And it's lucky for me that Shawn has the presence of mind to react in time."
    "He catches me as I collapse like a rag-doll, slumping into his arms."
    "Then he holds onto me until the throes of my climax are past."
    "After that I can't really say that I recall much of the film."
    "And nothing that I see on the screen could hope to compare to my own experience."
    "The movie probably deserves no more than one out of five stars."
    "But the sex was good enough to get five out of five."
    $ hero.replace_activity()
    $ game.active_date.score += 40
    $ shawn.sexperience += 1
    return

label shawn_fuck_beach_female:
label shawn_fuck_date_nudistbeach_female:
label shawn_fuck_date_beach_female:
    scene bg beach
    show shawn swimsuit smile at center, zoomAt(1.25, (640, 920))
    with fade
    "I never really pictured Shawn as the kind of guy that would naturally gravitate towards the beach."
    "Because he's like, you know, kind of a nerd!"
    "But he's really surprised me, by firstly wanting to come along on a date that means spending whole the day there."
    "Secondly, and this really is a nice surprise, he's impressed me with how good he looks in his swimming trunks."
    "I mean sure, Shawn's not going to win any posing contests, not unless he hits the gym and sleeps on a tanning-bed!"
    "But there's more than enough on show there for my eyes to linger on him and my imagination to start working away."
    "And luckily for me, Shawn's also the kind of guy that's not going to even notice the interest I'm showing."
    "Mainly because he's far too busy thinking that he's going to get sunburnt or step on a marooned jelly-fish."
    "Which means that I can look all I want and formulate my plans to get some serious attention from him when the time comes."
    show shawn nice
    shawn.say "Hey, [hero.name]..."
    shawn.say "The sun's getting pretty high."
    shawn.say "You want to go grab an ice-cream or something?"
    shawn.say "You know, cool down a little?"
    show shawn smile
    "I look up as Shawn asks the question, seeing that we're pretty much alone on the beach right now."
    "And even before I open my mouth to speak, I know that there's something I want to do."
    "But let's just say that it's not going to grab an ice-cream!"

    if hero.morality >= 25:
        "I give Shawn my sweetest smile and pat the spot next to me."
        bree.say "Maybe later, Shawn..."
        bree.say "Right now I want you to come and sit with me, here in the shade."

    if hero.morality <= -25:
        "I spread myself out on the sand in full view of Shawn."
        bree.say "And I make damn sure to squeeze my breasts between my arms as I do so."
        bree.say "Who need ice-cream when you can lick these instead?"
    else:

        "I make a point of stretching myself out on the sand where Shawn can see."
        bree.say "That can wait, Shawn..."
        bree.say "Right now I just want to spend a little quality time with you!"
    "Luckily for me, Shawn seems to get the message straight away."
    "Or else his conscious brain is overruled by his animal instincts."
    show shawn at center, traveling(1.5, 0.3, (640, 1080))
    "Because he wastes no time in hurrying over to where I'm laid."
    show shawn at center, zoomAt(1.5, (640, 1180)) with ease
    "And then he almost throws himself down on the sand beside me."
    show shawn nice
    shawn.say "Oh yeah, [hero.name]..."
    shawn.say "That's a much better idea."
    shawn.say "All that other stuff can wait."
    show shawn smile
    "I only have to sneak a quick glance down at Shawn's shorts to know that we're on the same wavelength."
    "Because I can easily see that something is already growing and getting hard in there!"

    if hero.morality >= 25:
        "The mere thought of it is a little intimidating, for sure."
        "But I know that I really want this, that I want to be with him."

    if hero.morality <= -25:
        "I can already feel my own body responding in kind."
        "Nipples hardening and pussy getting wetter by the second."
        "In fact I don't know how much longer I can hold myself back!"
    else:

        "I'm getting ever more turned on by the thought of it."
        "But I still do the best I can to pace myself and stay in control."
    show shawn nice blush
    shawn.say "So, [hero.name]..."
    shawn.say "What did you have in..."
    shawn.say "Mmmph!"
    show shawn smile
    "I can sense that Shawn's still nervous around me, even now."
    "That he's not sure of the best way to get things started."
    "But as I know exactly what I want, I make the decision for him."
    hide shawn
    show shawn kiss swimsuit
    with fade
    "As soon as my lips are planted on his, it seems to do the trick."
    "It's like I can feel the trepidation draining out of his body."
    "And within moments his hands are moving over me, pulling me closer."
    "Of course one of the big advantages of sex at the beach is the dress code."
    "When all you're wearing is a tiny swimming costume, getting naked takes no time at all."
    "Even so, I'm expecting to have to tell Shawn to start peeling mine off of me."
    "But to my surprise, he takes the initiative, easing it down and then stripping it from me."
    "Not wanting to look like I'm playing catch-up, I grab the waist-band of his trunks."
    "Then I yank them down, accidentally pulling something else down with them."
    "Shawn's cock naturally bends and then pops back up again as soon as it's free."
    "Which means that it pretty much lands in the palm of my hand."
    hide shawn
    show shawn swimsuit smile blush at center, zoomAt(1.5, (640, 1180))
    with fade
    "This is what breaks the kiss, as I look down in surprise Shawn gasps at the sensation."

    if hero.morality >= 25:
        bree.say "Oh, Shawn..."
        bree.say "It's SO big!"

    if hero.morality <= -25:
        bree.say "Oh fuck yeah!"
        bree.say "Shawn, I want this thing inside of me!"
    else:

        bree.say "Oh, hello..."
        bree.say "Someone's eager to get in on the action!"
    "Shawn doesn't seem capable of responding with words."
    "Instead he just nods eagerly, reaching out to embrace me."
    "I return the gesture, and together we roll on the sand."
    "But I soon realise that I need to steer things in a certain direction."
    "Because I'm getting a clear mental image of where I want things to go next."
    menu:
        "Missionary":
            scene bg black
            show shawn missionary beach
            with fade
            "I know what I want, and that's to have Shawn on top of me right now."
            show shawn missionary beach back
            "So I make sure that as we roll around, I stay underneath him."
            "And by the time we end up in the lapping waves, he's in the perfect position."
            "I manage to throw out my arms and position my legs in just the right way."
            "This means Shawn doesn't roll over again, and finds himself atop me."
            show shawn missionary beach normal
            "And from the look on his face, he thinks he's the one that pulled it off too!"
            "I can already feel his cock as it rubs against the inside of my thigh."
            "The need it inspires in me is so strong I have to bite my lip."
            menu:
                "Guide him to my pussy":
                    "I know where I want Shawn too, so I make sure to let him know."
                    "Angling myself so the head slides over the lips of my pussy."
                    "And when it does, we both let out a moan of sheer pleasure."
                    "Which is more than enough to seal the deal."
                    call check_condom_usage (shawn) from _call_check_condom_usage_150
                    if _return == False:
                        return "leave_without_gain"
                    "Not wanting to waste another moment, I pull Shawn down and onto me."
                    "And the second that I do so, he seems to get the message, loud and clear."
                    "Because his actions are all focussed on the same thing that I want."
                    "Which is getting him inside of me as quickly as possible!"
                    "Shawn angles himself perfectly, positioning his cock in just the right way."
                    "This means that as soon as he begins to move, it travels the length of my pussy."
                    if CONDOM:
                        show shawn missionary vaginal pleasure condom at stepback(0.1, -10, 0)
                    else:
                        show shawn missionary vaginal pleasure at stepback(0.1, -10, 0)
                    "It's only the first pass, so there's almost no chance of me opening to him yet."
                    "But still the mere sensation of contact makes me moan and wriggle beneath him."
                    "Shawn takes this in the exact way it was intended, and he doubles down on it."
                    show shawn missionary opened at stepback(0.25, -10, 0)
                    play sound slide_in
                    pause 0.25
                    play sound slide_out
                    "I feel the same motion repeated again and again, each time building in intensity."
                    "Losing track of the number of times he's done it, I feel myself starting to zone out."
                    "Like I'm trapped on the edge of a precipice, waiting to be pushed over."
                    "But when that moment comes, it's like being jolted back into wakefulness."
                    show shawn missionary at stepback(0.25, -10, 0)
                    play sound slide_in
                    pause 0.25
                    play sound slide_out
                    "My eyes burst open as Shawn begins to sink into me, and I cling onto him tightly."
                    show shawn missionary at stepback(0.15, -10, 0)
                    play sound slide_in
                    pause 0.15
                    play sound slide_out
                    "The sudden nature of my movements seems to surprise him, making him move faster."
                    "Which in turn means that he's deep inside of me in the blink of an eye."
                    "I can't help whimpering at the sensation, nodding helplessly."
                    "There's no way of knowing if Shawn sees or hears any of this."
                    "But still he seems intent on the same course of action as me."
                    show shawn missionary at stepback(0.15, -10, 0)
                    play sound slide_in
                    pause 0.15
                    play sound slide_out
                    "That's why I feel him speeding up, beginning to thrust in and out."
                    "In turn this makes the whole feeling that much more intense."
                    "Which in turn means that all I can do is lie back and take it."
                    show shawn missionary at stepback(0.15, -10, 0)
                    play sound slide_in
                    pause 0.15
                    play sound slide_out
                    "Luckily for me, Shawn seems more than capable of taking the lead."
                    "So all I have to do is hold onto him and let it all wash over me."
                    "Though that doesn't mean that I lie there like a lump of wood."
                    show shawn missionary at stepback(0.15, -10, 0)
                    play sound slide_in
                    pause 0.15
                    play sound slide_out
                    "My heels are scraping in the sand, my hands digging in to squeeze it between my fingers."
                    "But all the same, that does nothing to release the need that's building up inside of me."
                    "The way that Shawn's filling me, I feel like satisfaction should be inevitable."
                    show shawn missionary normal at stepback(0.15, -10, 0)
                    play sound slide_in
                    pause 0.15
                    play sound slide_out
                    "Yet somehow the more he makes me feel, the more my body seems to crave."
                    "Either Shawn senses this, or else he's in the exact same position."
                    "Because he rises to meet the demand as soon as it arises."
                    show shawn missionary pleasure speed at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.1
                    show shawn missionary -speed
                    play sound slide_out
                    "Moving faster, thrusting harder and pushing deeper as much as he can."
                    "But I know that there has to be a limit, that we can only go so far like this."
                    "Soon enough we seem to reach that point, and I feel like I'm about to explode."
                    show shawn missionary pleasure wide speed at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.1
                    show shawn missionary -speed
                    play sound slide_out
                    "I open my mouth to say as much."
                    "But Shawn beats me to the punch."
                    show shawn missionary pleasure speed at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.1
                    show shawn missionary -speed
                    play sound slide_out
                    shawn.say "...[hero.name]..."
                    shawn.say "I'm...I'm going to..."
                    shawn.say "I'm going to cum!"
                    call cum_reaction (shawn, 'vaginal') from _call_cum_reaction_285
                    if _return == "vaginal_condom":

                        "I remember that we took the time to use a condom."
                        "So there's nothing at all to worry about."
                        "All I need to do is hold on and let nature take its course."
                        show shawn missionary vaginal ahegao squirt with hpunch
                        "A moment later, Shawn shoots his load deep inside of me."
                        with hpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        with hpunch
                        "Flowing over me in a wave of pleasure I never want to end."
                    elif _return == "vaginal_outside":

                        bree.say "Pull out, Shawn..."
                        bree.say "Before you lose it!"
                        "Shawn hurries to do as he's told, sliding out of me before the end."
                        show shawn missionary out
                        play sound pop_out
                        "That done, there's nothing at all to worry about."
                        "All I need to do is hold on and let nature take its course."
                        show shawn missionary ahegao squirt with hpunch
                        "A moment later, Shawn shoots his load over my belly."
                        with hpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        with hpunch
                        "Flowing over me in a wave of pleasure I never want to end."
                    elif _return == "vaginal_inside_pill":

                        bree.say "I'm on the...pill..."
                        bree.say "So just let go!"
                        "The medication means there's nothing at all to worry about."
                        "All I need to do is hold on and let nature take its course."
                        show shawn missionary ahegao creampie squirt with hpunch
                        "A moment later, Shawn shoots his load deep inside of me."
                        with hpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        with hpunch
                        "Flowing over me in a wave of pleasure I never want to end."
                    elif _return == "vaginal_inside_pregnant":

                        bree.say "I'm pregnant, remember?"
                        bree.say "So just let go!"
                        "I can't get any more pregnant, which means there's nothing at all to worry about."
                        "All I need to do is hold on and let nature take its course."
                        show shawn missionary ahegao creampie squirt with hpunch
                        "A moment later, Shawn shoots his load deep inside of me."
                        with hpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        with hpunch
                        "Flowing over me in a wave of pleasure I never want to end."
                    else:

                        "I have Shawn right where I want him, hitting the exact spot."
                        "All I need to do is hold on and let nature take its course."
                        show shawn missionary ahegao creampie squirt with hpunch
                        "A moment later, Shawn shoots his load deep inside of me."
                        with hpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        with hpunch
                        "Flowing over me in a wave of pleasure I never want to end."
                "Guide him to my ass":
                    "I know where I want Shawn too, so I make sure to let him know."
                    "Angling myself so the head slides between the cheeks of my butt."
                    "And when it does, we both let out a moan of sheer pleasure."
                    "Which is more than enough to seal the deal."
                    "Not wanting to waste another moment, I pull Shawn down and onto me."
                    "And the second that I do so, he seems to get the message, loud and clear."
                    "Because his actions are all focussed on the same thing that I want."
                    "Which is getting him inside of me as quickly as possible!"
                    "Shawn angles himself perfectly, positioning his cock in just the right way."
                    "This means that as soon as he begins to move, it presses hard against my hole."
                    show shawn missionary anal pleasure at stepback(0.1, -10, 0)
                    "It's only the first pass, so there's almost no chance of me opening to him yet."
                    "But still the mere sensation of contact makes me moan and wriggle beneath him."
                    "Shawn takes this in the exact way it was intended, and he doubles down on it."
                    show shawn missionary at stepback(0.25, -10, 0)
                    play sound slide_in
                    pause 0.25
                    play sound slide_out
                    "I feel the same motion repeated again and again, each time building in intensity."
                    "Losing track of the number of times he's done it, I feel myself starting to zone out."
                    "Like I'm trapped on the edge of a precipice, waiting to be pushed over."
                    "But when that moment comes, it's like being jolted back into wakefulness."
                    show shawn missionary normal at stepback(0.25, -10, 0)
                    play sound slide_in
                    pause 0.25
                    play sound slide_out
                    "My eyes burst open as Shawn begins to sink into me, and I cling onto him tightly."
                    show shawn missionary at stepback(0.15, -10, 0)
                    play sound slide_in
                    pause 0.15
                    play sound slide_out
                    "The sudden nature of my movements seems to surprise him, making him move faster."
                    "Which in turn means that he's deep inside of me in the blink of an eye."
                    "I can't help whimpering at the sensation, nodding helplessly."
                    "There's no way of knowing if Shawn sees or hears any of this."
                    "But still he seems intent on the same course of action as me."
                    show shawn missionary at stepback(0.15, -10, 0)
                    play sound slide_in
                    pause 0.15
                    play sound slide_out
                    "That's why I feel him speeding up, beginning to thrust in and out."
                    "In turn this makes the whole feeling that much more intense."
                    "Which in turn means that all I can do is lie back and take it."
                    show shawn missionary at stepback(0.15, -10, 0)
                    play sound slide_in
                    pause 0.15
                    play sound slide_out
                    "Luckily for me, Shawn seems more than capable of taking the lead."
                    "So all I have to do is hold onto him and let it all wash over me."
                    "Though that doesn't mean that I lie there like a lump of wood."
                    show shawn missionary at stepback(0.15, -10, 0)
                    play sound slide_in
                    pause 0.15
                    play sound slide_out
                    "My heels are scraping in the sand, my hands digging in to squeeze it between my fingers."
                    "But all the same, that does nothing to release the need that's building up inside of me."
                    "The way that Shawn's filling me, I feel like satisfaction should be inevitable."
                    show shawn missionary normal at stepback(0.15, -10, 0)
                    play sound slide_in
                    pause 0.15
                    play sound slide_out
                    "Yet somehow the more he makes me feel, the more my body seems to crave."
                    "Either Shawn senses this, or else he's in the exact same position."
                    "Because he rises to meet the demand as soon as it arises."
                    show shawn missionary pleasure speed at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.1
                    show shawn missionary -speed
                    play sound slide_out
                    "Moving faster, thrusting harder and pushing deeper as much as he can."
                    "But I know that there has to be a limit, that we can only go so far like this."
                    "Soon enough we seem to reach that point, and I feel like I'm about to explode."
                    show shawn missionary pleasure wide speed at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.1
                    show shawn missionary -speed
                    play sound slide_out
                    "I open my mouth to say as much."
                    "But Shawn beats me to the punch."
                    show shawn missionary pleasure speed at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.1
                    show shawn missionary -speed
                    play sound slide_out
                    shawn.say "B...[hero.name]..."
                    shawn.say "I'm...I'm going to..."
                    shawn.say "I'm going to cum!"
                    call cum_reaction (shawn, 'anal', 1) from _call_cum_reaction_286
                    if _return == "anal_inside":

                        "There are definite perks to choosing the back door."
                        "Such as not needing to worry about any little accidents."
                        "All I need to do is hold on and let nature take its course."
                        show shawn missionary ahegao creampie squirt with hpunch
                        "A moment later, Shawn shoots his load deep inside of me."
                        with hpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        with hpunch
                        "Flowing over me in a wave of pleasure I never want to end."
                    else:

                        bree.say "Pull out, Shawn..."
                        bree.say "I want you to rain down on me!"
                        "Shawn hurries to do as he's told, sliding out of me before the end."
                        show shawn missionary out with vpunch
                        play sound slide_out
                        "That done, there's nothing at all to worry about."
                        "All I need to do is hold on and let nature take its course."
                        show shawn missionary squirt with hpunch
                        "A moment later, Shawn shoots his load over my belly."
                        with hpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        with hpunch
                        "Flowing over me in a wave of pleasure I never want to end."
        "Doggy":
            scene bg black
            show shawn doggy beach floats
            with fade
            "Almost as soon as I'm rolling in the sand with Shawn, I make to get up again."
            "The feeling of the water lapping around my hands and knees just feels so good."
            "So much so that I feel like I want it to be part of the experience too."
            "That's why I make a point of crawling a little way from Shawn and into the shallows."
            "Of course he follows, hot on my heels and unaware of where I'm going."
            "But all it takes is a quick look back over my shoulder to tell him I'm not going far."
            "And maybe an inviting waggle of my butt to drive the point home!"
            "It seems to work too, as Shawn gets straight onto his knees behind me."
            "Then I feel him clap his hands on my haunches, confirming my suspicions."
            menu:
                "Guide him to my pussy":
                    "I can already feel the sensation of Shawn's cock brushing the back of my thighs."
                    "And it's sending shivers through the entire length of my body right now."
                    "But there's nowhere I'm feeling in more than between my thighs."
                    "So with my pussy positively tingling, I decide that's where I want it to go."
                    call check_condom_usage (shawn) from _call_check_condom_usage_151
                    if _return == False:
                        return "leave_without_gain"
                    if CONDOM:
                        show shawn doggy condom at stepback(0.1, -10, 0)
                    "Shawn seems to be able to read my mind, or at least my body language."
                    "As he instantly lines himself up so that his cock it pressing against my pussy."
                    "I don't think there's any need for me to speak up."
                    "But something keeps me from just staying silent."

                    if hero.morality >= 25:
                        bree.say "Oh, Shawn..."
                        bree.say "I can't believe I'm saying this..."
                        bree.say "But I want you in my pussy so badly!"

                    if hero.morality <= -25:
                        bree.say "What are you waiting for, Shawn?"
                        bree.say "Put it in my pussy already!"
                    else:

                        bree.say "Please, Shawn..."
                        bree.say "I want you in my pussy!"
                    "My pleas seem to hurry Shawn along, making him go faster."
                    "Almost as if he's afraid that I'm getting tired of waiting."
                    "And for me, the change is instant and pretty powerful."
                    "I gasp as Shawn thrusts himself hard against me, sliding along my pussy."
                    "He doesn't make it inside on the first attempt, but not for want of trying."
                    "If anything, his second pass is more forceful and intent than the first."
                    "And by the time he makes a third, I can already feel myself beginning to yield."
                    "On the next pass, Shawn's pushing more than hard enough to take advantage of this."
                    "Which means that the head of his cock suddenly sinks between the lips of my pussy."
                    "There's no way that I could speak a single word now, not even if I wanted to."
                    "Because as Shawn pushes deeper, the sensations spread out from between my legs."
                    "And the deeper he goes, the further they seem to reach."
                    if CONDOM:
                        show shawn doggy vaginal closed condom at stepback(0.1, -20, 0)
                    else:
                        show shawn doggy vaginal closed at stepback(0.1, -20, 0)
                    play sound slide_in
                    "This means that by the time he's as far in as he can go, my whole body is alive with pleasure."
                    "Part of me wants to beg Shawn to stop right there, maybe to just pause for a few short moments."
                    "The feeling is so intense and overwhelming, I want to let it sink in before we go further."
                    "But as I already mentioned, he's just managed to leave me without the power of speech."
                    "So all that comes out of my mouth is a desperate cry of ecstasy."
                    "Shawn seems to interpret this as me asking for more."
                    "Or else he's not aware of it in the slightest."
                    show shawn doggy near at stepback(0.1, -20, 0)
                    play sound slide_in
                    pause 1.5
                    show shawn doggy far
                    play sound slide_out
                    "Because the next thing that he does is begin to move inside of me."
                    "Not pausing to catch his breath, Shawm launches into the act of fucking me."
                    show shawn doggy near at stepback(0.1, -20, 0)
                    play sound slide_in
                    pause 1.5
                    show shawn doggy far
                    play sound slide_out
                    "And soon I feel that well of passion hidden beneath his nerdy exterior."
                    "It's like that guy that turns green and goes on the rampage when he gets angry."
                    show shawn doggy near at stepback(0.1, -20, 0)
                    play sound slide_in
                    pause 1.5
                    show shawn doggy far
                    play sound slide_out
                    "Normally I'd remember the name of the comic-book."
                    "But right now I'm getting pumped to within an inch of my life!"
                    show shawn doggy near at stepback(0.1, -15, 0)
                    play sound slide_in
                    pause 1
                    show shawn doggy far heat closed
                    play sound slide_out
                    "Anyway, Shawn's like that, but instead of getting mad, he gets horny."
                    "He's not just making love to me, or humping me like a desperate animal."
                    show shawn doggy near bodyheat at stepback(0.1, -15, 0)
                    play sound slide_in
                    pause 1
                    show shawn doggy far mc_sweat
                    play sound slide_out
                    "It's more like he's smashing me the whole time!"
                    shawn.say "Urgh..."
                    show shawn doggy near at stepback(0.1, -15, 0)
                    play sound slide_in
                    pause 1
                    show shawn doggy far moan
                    play sound slide_out
                    shawn.say "Shawn fuck!"
                    "I'm sure that in any other position I'd have been laughing out loud."
                    show shawn doggy near at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.5
                    show shawn doggy far
                    play sound slide_out
                    "But as Shawn pounds away at me, I find myself nodding eagerly."
                    "Almost like he's been able to turn the both of us into grunting savages."
                    show shawn doggy near at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.5
                    show shawn doggy far
                    play sound slide_out
                    "Or more appropriately, desperate and horny animals."
                    "Because the only thing on my mind right now is his cock."
                    show shawn doggy near at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.5
                    show shawn doggy far
                    play sound slide_out
                    "The sensation of it thrusting in and out of me."
                    "The pleasure that it's overwhelming my body with."
                    show shawn doggy near at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.3
                    show shawn doggy far
                    play sound slide_out
                    "And the desire for all of this to keep on going as long as possible."
                    "But the problem is that I'm only human, and I can only take so much of this."
                    show shawn doggy near backsweat frontsweat shake pleasure ahegao with hpunch
                    play sound slide_in
                    pause 0.3
                    show shawn doggy -shake -backsweat -frontsweat
                    bree.say "Aahhh..."
                    bree.say "Oh god..."
                    show shawn doggy far
                    play sound slide_out
                    bree.say "Shawn...I'm going to...to cum!"
                    shawn.say "Urgh..."
                    show shawn doggy near backsweat frontsweat shake with hpunch
                    play sound slide_in
                    pause 0.3
                    show shawn doggy -shake -backsweat -frontsweat
                    shawn.say "Shawn cum too!"
                    call cum_reaction (shawn, 'vaginal') from _call_cum_reaction_287
                    if _return == "vaginal_condom":

                        "I remember that we took the time to use a condom."
                        "So there's nothing at all to worry about."
                        show shawn doggy far -backsweat -frontsweat -shake
                        play sound slide_out
                        "All I need to do is hold on and let nature take its course."
                        show shawn doggy near squirt shake backsweat frontsweat with hpunch
                        play sound slide_in
                        pause 0.3
                        show shawn doggy -squirt -shake -backsweat -frontsweat
                        "A moment later, Shawn shoots his load deep inside of me."
                        "And I feel everything in slow-motion, including my own orgasm."
                        "Flowing over me in a wave of pleasure I never want to end."
                    elif _return == "vaginal_outside":

                        bree.say "Pull out, Shawn..."
                        bree.say "Before you lose it!"
                        "Shawn hurries to do as he's told, sliding out of me before the end."
                        show shawn doggy out far -backsweat -frontsweat with hpunch
                        play sound slide_out
                        "That done, there's nothing at all to worry about."
                        "All I need to do is hold on and let nature take its course."
                        if CONDOM:
                            show shawn with hpunch
                        else:
                            show shawn cumshot with hpunch
                        "A moment later, Shawn shoots his load over my back and buttocks."
                        if CONDOM:
                            show shawn squirt with hpunch
                        else:
                            show shawn -cumshot cum onbody squirt with hpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        "Flowing over me in a wave of pleasure I never want to end."
                    elif _return == "vaginal_inside_pill":

                        bree.say "I'm on the...pill..."
                        bree.say "So just let go!"
                        "The medication means there's nothing at all to worry about."
                        show shawn doggy far -backsweat -frontsweat
                        play sound slide_out
                        "All I need to do is hold on and let nature take its course."
                        show shawn doggy near creampie squirt shake backsweat frontsweat with hpunch
                        play sound slide_in
                        pause 0.3
                        show shawn doggy -squirt -shake -backsweat -frontsweat cum onpussy
                        "A moment later, Shawn shoots his load deep inside of me."
                        "And I feel everything in slow-motion, including my own orgasm."
                        "Flowing over me in a wave of pleasure I never want to end."
                    elif _return == "vaginal_inside_pregnant":

                        bree.say "I'm pregnant, remember?"
                        bree.say "So just let go!"
                        "I can't get any more pregnant, which means there's nothing at all to worry about."
                        show shawn doggy far -backsweat -frontsweat
                        play sound slide_out
                        "All I need to do is hold on and let nature take its course."
                        show shawn doggy near creampie squirt shake backsweat frontsweat with hpunch
                        play sound slide_in
                        pause 0.3
                        show shawn doggy -squirt -shake -backsweat -frontsweat cum onpussy
                        "A moment later, Shawn shoots his load deep inside of me."
                        "And I feel everything in slow-motion, including my own orgasm."
                        "Flowing over me in a wave of pleasure I never want to end."
                    else:

                        "I have Shawn right where I want him, hitting the exact spot."
                        show shawn doggy far -backsweat -frontsweat
                        play sound slide_out
                        "All I need to do is hold on and let nature take its course."
                        play sound slide_in
                        show shawn doggy near creampie squirt shake backsweat frontsweat with hpunch
                        pause 0.3
                        show shawn doggy -squirt -shake -backsweat -frontsweat cum onpussy
                        "A moment later, Shawn shoots his load deep inside of me."
                        "And I feel everything in slow-motion, including my own orgasm."
                        "Flowing over me in a wave of pleasure I never want to end."
                "Guide him to my ass":
                    "I can already feel the sensation of Shawn's cock brushing the back of my thighs."
                    "And it's sending shivers through the entire length of my body right now."
                    "But there's nowhere I'm feeling in more than between my buttocks."
                    "So with my ass positively tingling, I decide that's where I want it to go."
                    "Shawn seems to be able to read my mind, or at least my body language."
                    "As he instantly lines himself up so that his cock it pressing against my pussy."
                    "I don't think there's any need for me to speak up."
                    "But something keeps me from just staying silent."

                    if hero.morality >= 25:
                        bree.say "Oh, Shawn..."
                        bree.say "I can't believe I'm saying this..."
                        bree.say "But I want you in my ass so badly!"

                    if hero.morality <= -25:
                        bree.say "What are you waiting for, Shawn?"
                        show shawn doggy wink
                        bree.say "Put it in my ass already!"
                        show shawn doggy back
                    else:

                        bree.say "Please, Shawn..."
                        bree.say "I want you in my ass!"
                    "My pleas seem to hurry Shawn along, making him go faster."
                    "Almost as if he's afraid that I'm getting tired of waiting."
                    "And for me, the change is instant and pretty powerful."
                    "I gasp as Shawn thrusts himself hard against me, sliding around my hole."
                    "He doesn't make it inside on the first attempt, but not for want of trying."
                    "If anything, his second pass is more forceful and intent than the first."
                    "And by the time he makes a third, I can already feel myself beginning to yield."
                    "On the next pass, Shawn's pushing more than hard enough to take advantage of this."
                    "Which means that the head of his cock suddenly sinks into the hole."
                    "There's no way that I could speak a single word now, not even if I wanted to."
                    "Because as Shawn pushes deeper, the sensations spread out from between my legs."
                    "And the deeper he goes, the further they seem to reach."
                    show shawn doggy anal
                    play sound slide_in
                    "This means that by the time he's as far in as he can go, my whole body is alive with pleasure."
                    "Part of me wants to beg Shawn to stop right there, maybe to just pause for a few short moments."
                    "The feeling is so intense and overwhelming, I want to let it sink in before we go further."
                    "But as I already mentioned, he's just managed to leave me without the power of speech."
                    "So all that comes out of my mouth is a desperate cry of ecstasy."
                    "Shawn seems to interpret this as me asking for more."
                    "Or else he's not aware of it in the slightest."
                    show shawn doggy near at stepback(0.1, -20, 0)
                    play sound slide_in
                    pause 1.5
                    show shawn doggy far
                    play sound slide_out
                    "Because the next thing that he does is begin to move inside of me."
                    "Not pausing to catch his breath, Shawm launches into the act of fucking me."
                    show shawn doggy near at stepback(0.1, -20, 0)
                    play sound slide_in
                    pause 1.5
                    show shawn doggy far
                    play sound slide_out
                    "And soon I feel that well of passion hidden beneath his nerdy exterior."
                    "It's like that guy that turns green and goes on the rampage when he gets angry."
                    show shawn doggy near at stepback(0.1, -20, 0)
                    play sound slide_in
                    pause 1.5
                    show shawn doggy far
                    play sound slide_out
                    "Normally I'd remember the name of the comic-book."
                    "But right now I'm getting pumped to within an inch of my life!"
                    show shawn doggy near at stepback(0.1, -15, 0)
                    play sound slide_in
                    pause 1
                    show shawn doggy far heat closed
                    play sound slide_out
                    "Anyway, Shawn's like that, but instead of getting mad, he gets horny."
                    "He's not just making love to me, or humping me like a desperate animal."
                    show shawn doggy near bodyheat at stepback(0.1, -15, 0)
                    play sound slide_in
                    pause 1
                    show shawn doggy far mc_sweat
                    play sound slide_out
                    "It's more like he's smashing me the whole time!"
                    shawn.say "Urgh..."
                    show shawn doggy near at stepback(0.1, -15, 0)
                    play sound slide_in
                    pause 1
                    show shawn doggy far heat moan
                    shawn.say "Shawn fuck!"
                    "I'm sure that in any other position I'd have been laughing out loud."
                    show shawn doggy near at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.5
                    show shawn doggy far
                    "But as Shawn pounds away at me, I find myself nodding eagerly."
                    "Almost like he's been able to turn the both of us into grunting savages."
                    "Or more appropriately, desperate and horny animals."
                    show shawn doggy near at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.5
                    show shawn doggy far
                    play sound slide_out
                    "Because the only thing on my mind right now is his cock."
                    show shawn doggy near at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.5
                    show shawn doggy far
                    play sound slide_out
                    "The sensation of it thrusting in and out of me."
                    "The pleasure that it's overwhelming my body with."
                    show shawn doggy near at stepback(0.1, -10, 0)
                    play sound slide_in
                    pause 0.3
                    show shawn doggy far
                    play sound slide_out
                    "And the desire for all of this to keep on going as long as possible."
                    "But the problem is that I'm only human, and I can only take so much of this."
                    show shawn doggy near backsweat frontsweat shake pleasure ahegao with hpunch
                    play sound slide_in
                    pause 0.3
                    show shawn doggy -shake -backsweat -frontsweat
                    bree.say "Aahhh..."
                    bree.say "Oh god..."
                    show shawn doggy far
                    play sound slide_out
                    bree.say "Shawn...I'm going to...to cum!"
                    shawn.say "Urgh..."
                    show shawn doggy near backsweat frontsweat shake with hpunch
                    play sound slide_in
                    pause 0.3
                    show shawn doggy -shake -backsweat -frontsweat
                    shawn.say "Shawn cum too!"
                    call cum_reaction (shawn, 'anal', 1) from _call_cum_reaction_288
                    if _return == "anal_inside":

                        "I have Shawn right where I want him, hitting the exact spot."
                        show shawn doggy far -shake -backsweat -frontsweat
                        play sound slide_out
                        "All I need to do is hold on and let nature take its course."
                        show shawn doggy near creampie squirt shake backsweat frontsweat with hpunch
                        play sound slide_in
                        pause 0.3
                        show shawn doggy -squirt -shake -backsweat -frontsweat
                        "A moment later, Shawn shoots his load deep inside of me."
                        "And I feel everything in slow-motion, including my own orgasm."
                        "Flowing over me in a wave of pleasure I never want to end."
                    else:

                        bree.say "Pull out, Shawn..."
                        bree.say "Before you lose it!"
                        "Shawn hurries to do as he's told, sliding out of me before the end."
                        show shawn doggy out far -shake -backsweat -frontsweat with hpunch
                        play sound slide_out
                        "That done, there's nothing at all to worry about."
                        "All I need to do is hold on and let nature take its course."
                        if CONDOM:
                            show shawn doggy with hpunch
                        else:
                            show shawn doggy cumshot with hpunch
                        "A moment later, Shawn shoots his load over my back and buttocks."
                        if CONDOM:
                            show shawn doggy with hpunch
                        else:
                            show shawn doggy -cumshot cum onbody squirt with hpunch
                        "And I feel everything in slow-motion, including my own orgasm."
        "Reverse Cowgirl":
            scene bg black
            show shawn reverse cowgirl beach
            with fade
            "I feel like I'm the one making things happen here, the one calling the shots."
            "And so with that in mind, I decide that I want to be the one on top this time around."
            "Which is why I make sure that I sit up and take charge when I'm in that position."
            "With Shawn beneath me, I throw out my limbs and anchor myself on the sand."
            "And then I straddle his thighs, with my back turned to him as I do so."
            "As soon as my knees are digging into the sand, I feel like I have total control."
            "So I don't hesitate to reach down and grab hold of Shawn's cock."
            shawn.say "Oooh..."
            shawn.say "Please be gentle, [hero.name]!"
            shawn.say "That thing is attached to me, you know?"
            "I look back over my shoulder, letting Shawn read the expression on my face."

            if hero.morality >= 25:
                bree.say "Oh no, sorry, Shawn!"
                bree.say "I'll be gentle, I promise!"

            if hero.morality <= -25:
                bree.say "Ah, man up, Shawn..."
                bree.say "I'm gonna be riding you way harder than that!"
            else:

                bree.say "Oops!"
                bree.say "I guess I just got carried away for a second there."
                bree.say "I'll try not to do it again, but I can't make it a promise!"
            menu:
                "Guide him to my Pussy":
                    "Making good on my words, I press the head of Shawn's cock against my pussy."
                    "And I can't be sure where the moan of pleasure that follows comes from."
                    "Seriously, it could have been either Shawn or me that let it out in the moment."
                    "Or else we might have both let out moans that blended into one."
                    "Whatever the reason, I feel like I could just open up and let Shawn inside of me."
                    "My body feels that ready to welcome him."
                    call check_condom_usage (shawn) from _call_check_condom_usage_152
                    if _return == False:
                        return "leave_without_gain"
                    if CONDOM:
                        show shawn reverse cowgirl condom
                    "Beginning to move slowly, I rock myself back and forth atop Shawn."
                    "This means that I can gently start to tease my body into accepting him."
                    "I feel Shawn's hands taking hold of my waist, as if to steady me."
                    "And so I feel like he's giving me the permission to not to hold back."
                    "Choosing to take his actions that way, I kick up the speed significantly."
                    "At the same time I begin to push down with all of my weight."
                    "The angle we're at to each other means both of those things are significant."
                    "As the slightest alteration intensifies everything to a ridiculous degree."

                    if hero.morality >= 25:
                        bree.say "Oh..."
                        bree.say "Oh my goodness!"

                    if hero.morality <= -25:
                        bree.say "Oh..."
                        bree.say "Oh, I fucking need it..."
                        bree.say "I need it in me!"
                    else:

                        bree.say "Oh..."
                        bree.say "Oh fuck!"
                    "This time there's no doubt which one of us is making all of the noise."
                    "The sound of my voice is clear as crystal."
                    "While at the same time, Shawn's merely grunting and panting behind me."
                    "I don't know whether or not he's feeling the same rush of pleasure as I am right now."
                    "But there's no way that I'm going to stop and ask him about it either."
                    "Instead I push down harder still, almost trying to force things to get moving."
                    "And it doesn't take long for me to feel my efforts being rewarded either."
                    "Each pass I make seems to see the muscles down there surrender just a little more."
                    "Every time I rub myself along the length of Shawn's cock, my lips open another fraction of an inch."
                    "The process is so gradual and slow that I don't notice how close I must be coming to success."
                    show shawn reverse cowgirl vaginal at stepback(0.5, 0, -5)
                    play sound slide_in
                    "So when my pussy finally gives in, everything seems to happen at once."
                    "I sink down onto Shawn as he thrusts up and into me."
                    show shawn reverse cowgirl down at stepback(1.5, 0, -20)
                    play sound slide_in
                    pause 1.5
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "The fact we're both moving means it happens super fast too."
                    "All it feels like to me is that one moment Shawn's on the outside, and the next he's filling me!"
                    show shawn reverse cowgirl down at stepback(1.5, 0, -20)
                    play sound slide_in
                    pause 1.5
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "But the surprise and the sudden sensation of intense pleasure only seems to affect my conscious mind."
                    "Because while that is temporarily stunned, my body carries on regardless."
                    show shawn reverse cowgirl down at stepback(1.5, 0, -20)
                    play sound slide_in
                    pause 1.5
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "And that's not all, as it even seems to respond to the pleasure by stepping things up a notch."
                    "So the moment my head clears, it's to a whole new wave of sensations."
                    show shawn reverse cowgirl down at stepback(1, 0, -20)
                    play sound slide_in
                    pause 1
                    show shawn reverse cowgirl up smile
                    play sound slide_out
                    "I feel like I've woken up in the middle of what we're doing."
                    "As if I got here while I was sound asleep only a few seconds before."
                    show shawn reverse cowgirl down at stepback(0.5, 0, -15)
                    play sound slide_in
                    pause 1
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "And from what I can tell, my unconscious is a totally insatiable animal!"
                    "I find myself riding Shawn like he was a bull in the rodeo."
                    show shawn reverse cowgirl down at stepback(0.5, 0, -15)
                    play sound slide_in
                    pause 1
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "One hand waving in the air while the other holds on for dear life."
                    "But it's not like he's resisting, even in the slightest."
                    show shawn reverse cowgirl down at stepback(0.5, 0, -15)
                    play sound slide_in
                    pause 1
                    show shawn reverse cowgirl up closed
                    play sound slide_out
                    "I can feel Shawn bucking and twitching under me."
                    "And it seems like he's enjoying every second of it!"
                    show shawn reverse cowgirl down at stepback(0.5, 0, -10)
                    play sound slide_in
                    pause 0.5
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "Part of me is glad that we chose a deserted part of the beach to do this."
                    "But another part, the more wanton part, doesn't even care."
                    show shawn reverse cowgirl down at stepback(0.5, 0, -10)
                    play sound slide_in
                    pause 0.5
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "So what if someone else sees me like this."
                    "Red-faced and naked, riding Shawn with my breasts bouncing like footballs."
                    show shawn reverse cowgirl down at stepback(0.5, 0, -10)
                    play sound slide_in
                    pause 0.5
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "That would serve them right for snooping around!"
                    "The thought is followed by a deep and sudden feeling of something changing."
                    show shawn reverse cowgirl down at stepback(0.5, 0, -10)
                    play sound slide_in
                    pause 0.5
                    show shawn reverse cowgirl up pleasure
                    play sound slide_out
                    "I don't know if it's the excitement at the danger of being caught in the act."
                    show shawn reverse cowgirl down at stepback(0.5, 0, -10)
                    play sound slide_in
                    pause 0.3
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "Or if I'm just getting to the natural limits of what my body can handle."
                    show shawn reverse cowgirl down at stepback(0.3, 0, -10)
                    play sound slide_in
                    pause 0.3
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "Either way, I know that I'm going to cum."
                    show shawn reverse cowgirl down at stepback(0.3, 0, -10)
                    play sound slide_in
                    pause 0.3
                    show shawn reverse cowgirl up ahegao
                    play sound slide_out
                    "And within seconds too!"
                    call cum_reaction (shawn, 'vaginal') from _call_cum_reaction_289
                    if _return == "vaginal_condom":

                        "I remember that we took the time to use a condom."
                        show shawn reverse cowgirl down with vpunch
                        play sound slide_in
                        "So there's nothing at all to worry about."
                        show shawn reverse cowgirl up
                        play sound slide_out
                        "All I need to do is hold on and let nature take its course."
                        show shawn reverse cowgirl down with vpunch
                        play sound slide_in
                        "A moment later, Shawn shoots his load deep inside of me."
                        scene bg white with dissolve
                        pause 0.1
                        show shawn reverse cowgirl beach vaginal down ahegao with vpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        "Flowing over me in a wave of pleasure I never want to end."
                    elif _return == "vaginal_outside":

                        bree.say "Pull out, Shawn..."
                        bree.say "Before you lose it!"
                        "Shawn hurries to do as he's told, sliding out of me before the end."
                        show shawn reverse cowgirl ahegao out with vpunch
                        play sound slide_out
                        "That done, there's nothing at all to worry about."
                        "All I need to do is hold on and let nature take its course."
                        if CONDOM:
                            show shawn reverse cowgirl out with vpunch
                        else:
                            show shawn reverse cowgirl out cumshot with vpunch
                        "A moment later, Shawn shoots his load over my back and buttocks."
                        if CONDOM:
                            show shawn reverse cowgirl out with vpunch
                        else:
                            show shawn reverse cowgirl out -cumshot cum body with vpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        "Flowing over me in a wave of pleasure I never want to end."
                    elif _return == "vaginal_inside_pill":

                        bree.say "I'm on the...pill..."
                        bree.say "So just let go!"
                        show shawn reverse cowgirl down with vpunch
                        play sound slide_in
                        "The medication means there's nothing at all to worry about."
                        show shawn reverse cowgirl up
                        play sound slide_out
                        "All I need to do is hold on and let nature take its course."
                        show shawn reverse cowgirl down with vpunch
                        play sound slide_in
                        "A moment later, Shawn shoots his load deep inside of me."
                        scene bg white with dissolve
                        pause 0.1
                        show shawn reverse cowgirl beach vaginal down ahegao creampie with vpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        "Flowing over me in a wave of pleasure I never want to end."
                    elif _return == "vaginal_inside_pregnant":

                        bree.say "I'm pregnant, remember?"
                        bree.say "So just let go!"
                        show shawn reverse cowgirl down with vpunch
                        play sound slide_in
                        "I can't get any more pregnant, which means there's nothing at all to worry about."
                        show shawn reverse cowgirl up
                        play sound slide_out
                        "All I need to do is hold on and let nature take its course."
                        show shawn reverse cowgirl down with vpunch
                        play sound slide_in
                        "A moment later, Shawn shoots his load deep inside of me."
                        scene bg white with dissolve
                        pause 0.1
                        show shawn reverse cowgirl beach vaginal down ahegao creampie with vpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        "Flowing over me in a wave of pleasure I never want to end."
                    else:

                        show shawn reverse cowgirl down with vpunch
                        play sound slide_in
                        "I have Shawn right where I want him, hitting the exact spot."
                        show shawn reverse cowgirl up
                        play sound slide_out
                        "All I need to do is hold on and let nature take its course."
                        show shawn reverse cowgirl down with vpunch
                        play sound slide_in
                        "A moment later, Shawn shoots his load deep inside of me."
                        scene bg white with dissolve
                        pause 0.1
                        show shawn reverse cowgirl beach vaginal down ahegao creampie with vpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        "Flowing over me in a wave of pleasure I never want to end."
                "Guide him to my Ass":
                    "Making good on my words, I press the head of Shawn's cock between my buttocks."
                    "And I can't be sure where the moan of pleasure that follows comes from."
                    "Seriously, it could have been either Shawn or me that let it out in the moment."
                    "Or else we might have both let out moans that blended into one."
                    "Whatever the reason, I feel like I could just open up and let Shawn inside of me."
                    "My body feels that ready to welcome him."
                    "Beginning to move slowly, I rock myself back and forth atop Shawn."
                    "This means that I can gently start to tease my body into accepting him."
                    "I feel Shawn's hands taking hold of my waist, as if to steady me."
                    "And so I feel like he's giving me the permission to not to hold back."
                    "Choosing to take his actions that way, I kick up the speed significantly."
                    "At the same time I begin to push down with all of my weight."
                    "The angle we're at to each other means both of those things are significant."
                    "As the slightest alteration intensifies everything to a ridiculous degree."

                    if hero.morality >= 25:
                        bree.say "Oh..."
                        bree.say "Oh my goodness!"

                    if hero.morality <= -25:
                        bree.say "Oh..."
                        bree.say "Oh, I fucking need it..."
                        bree.say "I need it in me!"
                    else:

                        bree.say "Oh..."
                        bree.say "Oh fuck!"
                    "This time there's no doubt which one of us is making all of the noise."
                    "The sound of my voice is clear as crystal."
                    "While at the same time, Shawn's merely grunting and panting behind me."
                    "I don't know whether or not he's feeling the same rush of pleasure as I am right now."
                    "But there's no way that I'm going to stop and ask him about it either."
                    "Instead I push down harder still, almost trying to force things to get moving."
                    "And it doesn't take long for me to feel my efforts being rewarded either."
                    "Each pass I make seems to see the muscles down there surrender just a little more."
                    "Every time I rub myself along the length of Shawn's cock, my muscles relax a fraction of an inch."
                    "The process is so gradual and slow that I don't notice how close I must be coming to success."
                    show shawn reverse cowgirl anal at stepback(0.5, 0, -5)
                    play sound slide_in
                    "So when my ass finally gives in, everything seems to happen at once."
                    "I sink down onto Shawn as he thrusts up and into me."
                    show shawn reverse cowgirl down at stepback(1.5, 0, -20)
                    play sound slide_in
                    pause 1.5
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "The fact we're both moving means it happens super fast too."
                    "All it feels like to me is that one moment Shawn's on the outside, and the next he's filling me!"
                    show shawn reverse cowgirl down at stepback(1.5, 0, -20)
                    play sound slide_in
                    pause 1.5
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "But the surprise and the sudden sensation of intense pleasure only seems to affect my conscious mind."
                    "Because while that is temporarily stunned, my body carries on regardless."
                    show shawn reverse cowgirl down at stepback(1.5, 0, -20)
                    play sound slide_in
                    pause 1.5
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "And that's not all, as it even seems to respond to the pleasure by stepping things up a notch."
                    "So the moment my head clears, it's to a whole new wave of sensations."
                    show shawn reverse cowgirl down at stepback(1, 0, -20)
                    play sound slide_in
                    pause 1
                    show shawn reverse cowgirl up smile
                    play sound slide_out
                    "I feel like I've woken up in the middle of what we're doing."
                    "As if I got here while I was sound asleep only a few seconds before."
                    show shawn reverse cowgirl down at stepback(0.5, 0, -15)
                    play sound slide_in
                    pause 1
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "And from what I can tell, my unconscious is a totally insatiable animal!"
                    "I find myself riding Shawn like he was a bull in the rodeo."
                    show shawn reverse cowgirl down at stepback(0.5, 0, -15)
                    play sound slide_in
                    pause 1
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "One hand waving in the air while the other holds on for dear life."
                    "But it's not like he's resisting, even in the slightest."
                    show shawn reverse cowgirl down at stepback(0.5, 0, -10)
                    play sound slide_in
                    pause 0.5
                    show shawn reverse cowgirl up closed
                    play sound slide_out
                    "I can feel Shawn bucking and twitching under me."
                    "And it seems like he's enjoying every second of it!"
                    show shawn reverse cowgirl down at stepback(0.5, 0, -10)
                    play sound slide_in
                    pause 0.5
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "Part of me is glad that we chose a deserted part of the beach to do this."
                    "But another part, the more wanton part, doesn't even care."
                    show shawn reverse cowgirl down at stepback(0.5, 0, -10)
                    play sound slide_in
                    pause 0.5
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "So what if someone else sees me like this."
                    "Red-faced and naked, riding Shawn with my breasts bouncing like footballs."
                    show shawn reverse cowgirl anal down at stepback(0.5, 0, -10)
                    play sound slide_in
                    pause 0.5
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "That would serve them right for snooping around!"
                    "The thought is followed by a deep and sudden feeling of something changing."
                    show shawn reverse cowgirl down at stepback(0.5, 0, -10)
                    play sound slide_in
                    pause 0.5
                    show shawn reverse cowgirl up pleasure
                    play sound slide_out
                    "I don't know if it's the excitement at the danger of being caught in the act."
                    show shawn reverse cowgirl down at stepback(0.5, 0, -10)
                    play sound slide_in
                    pause 0.3
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "Or if I'm just getting to the natural limits of what my body can handle."
                    show shawn reverse cowgirl anal down at stepback(0.3, 0, -10)
                    play sound slide_in
                    pause 0.3
                    show shawn reverse cowgirl up
                    play sound slide_out
                    "Either way, I know that I'm going to cum."
                    show shawn reverse cowgirl down at stepback(0.3, 0, -10)
                    play sound slide_in
                    pause 0.3
                    show shawn reverse cowgirl up ahegao
                    play sound slide_out
                    "And within seconds too!"
                    call cum_reaction (shawn, 'anal', 1) from _call_cum_reaction_290
                    if _return == "anal_inside":

                        show shawn reverse cowgirl down with vpunch
                        play sound slide_in
                        "I have Shawn right where I want him, hitting the exact spot."
                        show shawn reverse cowgirl up
                        "All I need to do is hold on and let nature take its course."
                        show shawn reverse cowgirl down with vpunch
                        play sound slide_in
                        "A moment later, Shawn shoots his load deep inside of me."
                        scene bg white with dissolve
                        pause 0.1
                        show shawn reverse cowgirl beach anal down creampie ahegao with vpunch
                        "And I feel everything in slow-motion, including my own orgasm."
                        "Flowing over me in a wave of pleasure I never want to end."
                    else:

                        bree.say "Pull out, Shawn..."
                        bree.say "Before you lose it!"
                        "Shawn hurries to do as he's told, sliding out of me before the end."
                        show shawn reverse cowgirl ahegao out with vpunch
                        play sound slide_out
                        "That done, there's nothing at all to worry about."
                        "All I need to do is hold on and let nature take its course."
                        show shawn reverse cowgirl cumshot with vpunch
                        "A moment later, Shawn shoots his load over my back and buttocks."
                        show shawn reverse cowgirl -cumshot cum body with vpunch
                        "And I feel everything in slow-motion, including my own orgasm."
    "Totally spent and overwhelmed by the aftershocks of my orgasm, I roll away from Shawn."
    "This isn't from a desire to keep him from touching me, just to be able to feel release."
    "So when he rolls after me and throws an arm over my chest, I wrap my own around it too."
    "And then we just lie there, letting the water lap against us and wash our bodies clean."
    $ shawn.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
