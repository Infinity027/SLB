init python:
    InteractActivity(**{
    "name": "fuck_cherie",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            ),
        PersonTarget(cherie,
            IsActive(),
            MinStat("love", 100),
            MinStat("sub", 25),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    Event(**{
    "name": "cherie_hottub_sex_male",
    "label": "cherie_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            IsActivity("date_hot_tub_home")),
        PersonTarget(cherie,
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


label cherie_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    "I'm always kind of nervous about having Cherie over to my place."
    "I mean, who wouldn't be - she lives in an actual frickin mansion!"
    "But today there's an added layer of stress for me to deal with."
    "Because she's coming to take a dip in the hot-tub with me too."
    "And that's why I'm beavering about the house in my swimming-trunks."
    "Doing the best I can to tidy stuff up before she gets here."
    play sound door_knock
    "That is until I hear the sound of someone knocking at the door."
    "As soon as that happens, I drop everything and hurry into the hallway."
    "Yanking the door open as quickly as I possibly can."
    play sound door_open
    pause 0.7
    scene bg house
    show cherie stuned at center, zoomAt(1.4, (640, 920))
    "So quickly, in fact, that the person on the other side is taken by surprise."
    show cherie at center, traveling(1.2, 0.2, (640, 820))
    "Exclaiming and taking a small leap backwards on the front porch."
    show cherie b surprised
    cherie.say "{i}Mon Dieu!{/i}"
    show cherie stuned
    mike.say "Oh..."
    mike.say "Sorry, Cherie..."
    show cherie a
    mike.say "I didn't mean to make you jump like that!"
    show cherie at center, traveling(1.6, 1, (640, 1020))
    "Cherie still has one hand on her chest as she steps forwards again."
    "And I make a point of stepping to one side, then gesturing for her to come in."
    "Much to my relief she takes the hint, walking into the hallway so I can close the door behind her."
    show cherie talkative
    cherie.say "What were you doing, mon ami…"
    cherie.say "Waiting behind the door for me to arrive?"
    show cherie normal
    mike.say "Ah..."
    mike.say "No, not exactly."
    mike.say "But I have been kind of listening out for you."
    "Cherie seems to have recovered from the shock of a few moments before."
    "As she cracks a smile, realising that I've been anticipating her arrival."
    show cherie talkative
    cherie.say "I suppose that I should be flattered."
    cherie.say "It is nice to know that someone looks forward to my company so."
    show bg livingroom with dissolve
    "I keep on leading Cherie through the house and towards the back porch."
    "Doing all I can to prevent her from really paying much attention to the state of the place."
    "But all the same she keeps on glancing around, defeating my best efforts."
    mike.say "Yeah..."
    mike.say "Sorry about the mess, Cherie..."
    mike.say "My housemates are pretty messy!"
    "As we reach the patio doors, I see that Cherie's shaking her head."
    show cherie talkative
    cherie.say "Ah yes - Cassidy is just the same."
    cherie.say "I keep telling you, mon ami…"
    cherie.say "You do not need to apologise for your home."
    cherie.say "Sometimes I actually envy you living in this place."
    show cherie normal
    "I'm just about done sliding the doors open when I hear what Cherie just said."
    "And I turn around with a look of genuine disbelief on my face."
    scene bg pool at center, zoomAt(1.2, (640, 820)) with dissolve
    mike.say "Cherie, you live in one of the biggest houses I've ever seen!"
    mike.say "What could you possibly want with a place like this?"
    show cherie a talkative with easeinleft
    cherie.say "It can be lonely, living in such a huge, empty space."
    cherie.say "And as they say...size isn't everything."
    cherie.say "Well, at least in the case of houses!"
    show cherie normal
    "I see that Cherie's directing her gaze below my waist as she says this."
    "And that a knowing smile is creeping across her face at the same time."
    mike.say "I..."
    mike.say "Erm..."
    mike.say "I tried to make the place look nice!"
    "Unable to think of anything else to break the pregnant silence, I gesture around the hot-tub."
    "Pointing out the candles and the bottle of wine that surround it as the water bubbles away."
    show cherie talkative
    cherie.say "Oh, very nice, {i}mon ami…{/i}"
    cherie.say "You are really spoiling me!"
    show cherie happy
    cherie.say "Now, where may I go and change?"
    mike.say "Just back in the hallway, Cherie..."
    mike.say "There's a bathroom you can use down there."
    show cherie smile at startle(0.1, -5)
    pause 0.2
    hide cherie with easeoutleft
    "Cherie nods and turns on her heel, heading to the bathroom."
    "And I take the opportunity to let out a long sigh and pull myself together."
    "Something that I can really manage to do, as Cherie seems to be taking her time."
    "Though when I hear the sound of her voice again and turn around, I can see why."
    cherie.say "I am ready, mon ami…"
    cherie.say "Shall we test the waters together?"
    "I was about to say something in response to Cherie's question."
    "Probably something pretty flippant and silly."
    "But as soon as I lay eyes on her, I feel myself choking on the words."
    show cherie a smile sexyswimsuit at center, zoomAt(1.4, (640, 920)) with easeinleft
    mike.say "Urgh!"
    "And that's because Cherie looks way more stunning than I could have imagined."
    "Okay, I already know she's beautiful and she has a pretty perfect body."
    "Even a passing glance would be enough to prove that to anyone."
    show bg pool at center, traveling(1.2, 1, (640, 720))
    show cherie at center, traveling(1.4, 1, (640, 720))
    pause 2
    "But she has on what at first looks like a simple bikini, until I look closer."
    show bg pool at center, traveling(1.2, 1, (640, 820))
    show cherie at center, traveling(1.4, 1, (640, 920))
    pause 2
    "Because then I see that it's more like a series of strategically placed straps."
    "All bound together by delicate golden chains that crisscross her naked skin."
    show cherie happy at center, traveling(1.8, 0.7, (640, 1170))
    cherie.say "Oh come now, {i}mon ami…{/i}"
    cherie.say "You have seen a woman in a bathing-costume before, I know you have."
    cherie.say "So pick your jaw up off of the ground, and pour me a glass of wine!"
    "Cherie gracefully turns her back on me and walks over to the edge of the tub."
    "Then she lowers herself slowly into the water, making a show of every single movement."
    "And it's all I can do to fumble for the glasses and the bottle as I watch her."
    show hottub cherie sexyswimsuit with fade
    mike.say "Yeah, Cherie..."
    mike.say "I'm already on it, see?"
    "Cherie smiles and nods approvingly as I follow her into the tub."
    "She takes the glass and then allows herself a small sip as I get comfortable."
    cherie.say "Mmm…"
    mike.say "So...you like the wine?"
    cherie.say "Let's just say that if I were the one choosing the wine to sip in a hot-tub with a young man..."
    cherie.say "Then this is the kind of wine that I would choose."
    "Cherie seems to be doing that thing again where she makes a vague statement out of politeness."
    "And I get the distinct feeling that I'm not worldly or sophisticated enough to really get it."
    "That I can't tell if she's complimenting me or subtly putting me down."
    "So I choose to just nod and smile."
    mike.say "Well...okay then."
    "Cherie smiles and then makes a point of stretching out in the water."
    "She reaches out with her arms and lets her legs float out in front of her."
    "At the same time she rotates her head and exercises her neck."
    cherie.say "Oh..."
    cherie.say "This is something that I should do more often."
    cherie.say "It is like I can feel the stress and strain leaving my body."
    mike.say "Oh yeah, Cherie..."
    mike.say "It's almost like I can feel it too!"
    "Cherie lifts her head and opens her eyes, looking straight at me."
    cherie.say "Is that so, mon ami?"
    cherie.say "Then you must be very observant indeed."
    cherie.say "And be watching me very closely too!"
    "By now I've swallowed more than half my own glass of wine on account of my nerves."
    "And the fact that I haven't eaten much today means that I can feel it going to my head."
    "Not that I'm saying I can't handle my drink, just that it's already taking the edge off."
    "So rather than making me feel awkward, Cherie's subtle flirting is really hitting the spot."
    mike.say "It's not like I can help it, Cherie..."
    mike.say "When you're around, I can't look at anything else!"
    "Cherie's smile grows wider as she realises that I'm well and truly hooked."
    "And I can see that she's about to start trying to reel me in."
    cherie.say "I would always spend time in the spas back home."
    cherie.say "They are so much more sensitive than the ones you have here, so much more...liberated."
    cherie.say "I would engage a young man to massage me from head to toe, to leave no part of me untouched."
    cherie.say "And afterwards, if the mood took me...I would ask him to do more...to finish the job."
    "I'm nodding at everything Cherie's telling me right now."
    "Hanging on her every word and waiting to hear what's coming next."
    mike.say "Wow, Cherie..."
    mike.say "That sounds totally wild!"
    "Cherie does that weird thing with her head, where she turns it to the side with a subtle incline."
    "A gesture that's neither a nod or a shake of the head, but more like a subtle gesture that means 'maybe'."
    cherie.say "Perhaps it is, {i}mon ami{/i}..."
    cherie.say "But here we are, in your country and in your home."
    cherie.say "So perhaps you are the one that should be attended to?"
    "Before I can fully comprehend what she means, Cherie puts down her glass."
    "And then she pushes herself towards me through the water."
    "Instinctively I open my arms to her, guiding her to me."
    "Then, without the need for another word, she straddles my waist and puts her arms around my neck."
    "Cherie begins to kiss me passionately a moment later, almost instantly using her tongue."
    "And I don't resist her for a second, already feeling the passion that she's stoked inside of me."
    "By now there's no need for us to communicate with words, our actions doing the speaking for us."
    "Cherie's pretty much sitting astride me by now, firmly in place and staying there."
    "Which means that my hands are free to begin exploring her body, and they do so in earnest."
    "I feel her shiver and wriggle as I run them down her back, then caress her buttocks."
    "But as soon as they're below her waist, Cherie bears down on me."
    "Almost like she's trying to plant herself on top of my hands and trap them."
    "My brain's working on instinct alone, and so it easily interprets Cherie's intent."
    "Wrapping my fingers around the gusset of her bikini bottoms, I pull it aside."
    "And then I begin to stroke the lips of her pussy with the fingers of the other hand."
    "Cherie instantly breaks off the kiss, throwing her head back in dramatic fashion."
    "But I can see that she's nodding, telling me that she wants more of the same."
    "So I start to hastily tug at my trunks, pulling them down to release my cock."
    "Needless to say it's already hard, and pops up the moment it's freed."
    "And then I line Cherie up, getting ready to take things to the next stage."
    menu:
        "Fuck her ass":
            scene hottub sex male cherie sexyswimsuit with fade
            "And she does all that she can to help make it happen too."
            "Pushing herself straight down and onto me a moment later."
            "But I think she's expecting me to make a beeline for her pussy."
            "Which is a shame, because I have something a little different in mind."
            "Pulling Cherie towards me so that my manhood pokes between her buttocks."
            "This means that the head of my cock is pressed hard against her hole."
            "The tip skidding around the edge, which only seems to make her want it all the more."
            "Taking a more firm hold on Cherie, I make sure that I'm in the right spot."
            "Then I begin to move with a more controlled kind of motion than before."
            "The regular pattern of my movements seems to do the trick, making Cherie slow down."
            "Not only that, but I feel her yield to me as well, letting me set the pace."
            "Soon enough my strategy starts to get results, as I feel her muscles relax."
            "And then I half gasp as I feel the head slide perhaps half in inch inside."
            "But that's all I need to make it happen, instantly thrusting harder than before."
            "Cherie moans and puts her head on my shoulder as my cock pushes into her."
            "And I can feel the sensation of her sinking down and onto me too."
            "I slow down while it happens, almost coming to a complete stop."
            "Just letting gravity and Cherie's own weight do all of the work for me."
            "Soon enough I'm as far into her as it's physically possible for me to go."
            "And she's clinging on as if for dear life, quaking the whole time."
            "Part of me wants to stay like this for as long as possible, to savour the sensation."
            "But the part of me that wins is the one that desperately wants to grind away at Cherie."
            "So almost without a conscious thought, I start to move inside of her."
            "Pulling back and then thrusting forwards, I set the pace I intend to keep."
            "And before either of us know it, I'm pounding away at Cherie for all I'm worth."
            "She responds in kind, tightening her grip on me and pushing downwards."
            "Her actions letting me know that she's completely down with what I'm doing."
            "There's no way that Cherie could hope to tell me that using coherent words."
            "As my ear is already filled with the sound of her gasping for breath."
            "The ragged sound of her breathing telling the tale of her tumultuous passion."
            "And it's not just the sensation of my cock inside of Cherie that's doing it for me either."
            "I'm loving the way that her arms and legs are hugging me close right now."
            "That and the sensation of her flat belly against mine."
            "And obviously I couldn't fail to mention her breasts, right here in front of me."
            "Her bikini top is straining to keep them under control as I pound away at her."
            "Pushing Cherie's cleavage ever closer to my face and threatening to smother me!"
            "But then, to my surprise, Cherie does actually manage to string together a couple of words."
            cherie.say "Oh..."
            cherie.say "Oh, [hero.name]…"
            cherie.say "Here it comes...{i}la petite mort!{/i}"
            "For a moment I have no idea what Cherie's even talking about."
            "But then I feel the sensation of her muscles squeezing my cock."
            "And I realise that she's about to cum!"
            call cum_reaction (cherie, 'vaginal', 1) from _call_cum_reaction_322
            if _return == "vaginal_outside":
                show hottub sex male outside
                "I choose this as the moment to pull back and make sure that I slide out of Cherie's ass."
                show hottub cumshot ahegao with vpunch
                $ cherie.sub += 1
                "But the motion does nothing to lessen the impact of her orgasm when it hits."
                with vpunch
                "In fact it only seems to add to the intensity of the pleasure she's feeling."
                "Pushing her higher than ever and adding to the pleasure overwhelming her body."
            else:
                "Wanting the exact same thing as Cherie does, I push myself harder than ever."
                show hottub cumshot ahegao inside with vpunch
                $ cherie.love += 1
                "Meaning that I start to cum at the same time her orgasm really takes hold."
                with vpunch
                "And I make sure to let go when I'm as deep inside of her ass as I can get."
                with vpunch
                "Pushing her higher than ever and adding to the pleasure overwhelming her body."
        "Fuck her pussy":
            scene hottub sex male cherie sexyswimsuit with fade
            "And she does all that she can to help make it happen too."
            "Pushing herself straight down and onto me a moment later."
            "This means that the head of my cock is pressed hard against her pussy."
            "The tip skidding along her lips, which only seems to make her want it all the more."
            "Taking a more firm hold on Cherie, I make sure that I'm in the right spot."
            "Then I begin to move with a more controlled kind of motion than before."
            "The regular pattern of my movements seems to do the trick, making Cherie slow down."
            "Not only that, but I feel her yield to me as well, letting me set the pace."
            "Soon enough my strategy starts to get results, as I feel her pussy relax."
            "And then I half gasp as I feel the head slide perhaps half in inch inside."
            "But that's all I need to make it happen, instantly thrusting harder than before."
            "Cherie moans and puts her head on my shoulder as my cock pushes into her."
            "And I can feel the sensation of her sinking down and onto me too."
            "I slow down while it happens, almost coming to a complete stop."
            "Just letting gravity and Cherie's own weight do all of the work for me."
            "Soon enough I'm as far into her as it's physically possible for me to go."
            "And she's clinging on as if for dear life, quaking the whole time."
            "Part of me wants to stay like this for as long as possible, to savour the sensation."
            "But the part of me that wins is the one that desperately wants to grind away at Cherie."
            "So almost without a conscious thought, I start to move inside of her."
            "Pulling back and then thrusting forwards, I set the pace I intend to keep."
            "And before either of us know it, I'm pounding away at Cherie for all I'm worth."
            "She responds in kind, tightening her grip on me and pushing downwards."
            "Her actions letting me know that she's completely down with what I'm doing."
            "There's no way that Cherie could hope to tell me that using coherent words."
            "As my ear is already filled with the sound of her gasping for breath."
            "The ragged sound of her breathing telling the tale of her tumultuous passion."
            "And it's not just the sensation of my cock inside of Cherie that's doing it for me either."
            "I'm loving the way that her arms and legs are hugging me close right now."
            "That and the sensation of her flat belly against mine."
            "And obviously I couldn't fail to mention her breasts, right here in front of me."
            "Her bikini top is straining to keep them under control as I pound away at her."
            "Pushing Cherie's cleavage ever closer to my face and threatening to smother me!"
            "But then, to my surprise, Cherie does actually manage to string together a couple of words."
            cherie.say "Oh..."
            cherie.say "Oh, [hero.name]…"
            cherie.say "Here it comes...{i}la petite mort!{/i}"
            "For a moment I have no idea what Cherie's even talking about."
            "But then I feel the sensation of her muscles squeezing my cock."
            "And I realise that she's about to cum!"
            call cum_reaction (cherie, 'anal', 1) from _call_cum_reaction_323
            if _return == "anal_outside":
                show hottub sex male outside
                "I choose this as the moment to pull back and make sure that I slide out of Cherie."
                show hottub cumshot ahegao with vpunch
                $ cherie.sub += 1
                "But the motion does nothing to lessen the impact of her orgasm when it hits."
                with vpunch
                "In fact it only seems to add to the intensity of the pleasure she's feeling."
                "Pushing her higher than ever and adding to the pleasure overwhelming her body."
            else:
                "Wanting the exact same thing as Cherie does, I push myself harder than ever."
                show hottub cumshot ahegao with vpunch
                $ cherie.love += 1
                "Meaning that I start to cum at the same time her orgasm really takes hold."
                with vpunch
                "And I make sure to let go when I'm as deep inside of her as I can get."
                with vpunch
                "Pushing her higher than ever and adding to the pleasure overwhelming her body."
    "Once she's totally spent, I feel Cherie going limp in my arms."
    "And so I gently lower her into the water, keeping a hold of her."
    "Then I support her in the tub, waiting for the strength to return to her limbs."
    "When it does, she presses herself against me, nestling into my embrace."
    call stop_all_sfx from _call_stop_all_sfx_71
    show bg black with fade
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ cherie.sexperience += 1
    $ game.active_date.clothes = None
    return


label cherie_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg street
    show cherie


    call cherie_fuck_date_intro_male (location) from _call_cherie_fuck_date_intro


    call cherie_dick_reactions from _call_cherie_dick_reactions


    call cherie_fuck_date_foreplay_male from _call_cherie_fuck_date_foreplay_male


    call cherie_fuck_date_choices_male from _call_cherie_fuck_date_choices_male


    call handle_npc_leaving (cherie, _return) from _call_handle_npc_leaving_30
    if _return:
        return


    hide cherie
    call cherie_fuck_date_sleep (location="hero") from _call_cherie_fuck_date_sleep
    return

label cherie_fuck_date_intro_male(location="hero"):
    if cherie.sexperience == 0:
        scene bg house
        show cherie at center, zoomAt(1.25, (640, 880))
        with fade
        "I always feel kind of self-conscious when I bring a girl back to my place after a date."
        "So imagine how much worse that anxiety is when that girl happens to be someone like Cherie."
        "I mean, for one she's a mature woman that's seen the world and raised a daughter of her own."
        "And on top of that, she's used to living the high-life in an actual bloody mansion!"
        "So I'm almost visibly sweating as I lead her up to the front door of my humble little abode."
        mike.say "Now you remember me telling you not to get your hopes up, yeah?"
        mike.say "This is just the place that I'm renting at the moment."
        mike.say "It's not like I'm gonna be living here until I retire!"
        show cherie amused
        "Cherie's standing with her hands behind her back as I unlock the front-door."
        "And it's plain to see from the look on her face that she finds all of this very amusing."
        show cherie happy
        cherie.say "Of course, mon ami…"
        show cherie talkative
        cherie.say "I am not so shallow as to judge a man by the size of his house."
        cherie.say "Not when it is really the size of certain other things that really matters!"
        show cherie smile at center, traveling(1.35, 0.3, (640, 960))
        "Cherie underlines her point by leaning forwards and sneaking a hand under my line of sight."
        "Then I feel her playfully squeezing me just below the belt, caressing my manhood with her fingers."
        show cherie amused
        mike.say "Oh..."
        mike.say "Well okay then..."
        mike.say "So long as we understand each other."
        show cherie smile at startle
        "Cherie lets out a chuckle that only serves to make my predicament that much more awkward."
        hide cherie with dissolve
        "And then she slips past into the hallway, leaving me to hurriedly lock the door behind her."
        scene bg bedroom1
        show cherie at center, zoomAt(1.25, (640, 880))
        with fade
        "That done, I hastily lead her through the house and to my bedroom door."
        "Luckily for me, we don't bump into any of my housemates on the way there."
        "But I note that Cherie seems to be paying close attention to her surroundings."
        "As if she's taking it all in, despite my haste to deliver her to our ultimate destination."
        "And when I open the door and usher her inside, that interest seems to suddenly peak."
        show cherie happy
        cherie.say "Oh my goodness..."
        cherie.say "I did not know that you were so interested in space-men!"
        show cherie normal
        "Cherie smiles innocently as she points at the sci-fi movie posters covering my walls."
        "And I have to fight my natural urge to instantly argue that they're not what she might think."
        "Because there's nothing more likely to kill the mood than a nerd arguing minutiae with a girl!"
        mike.say "Oh those?"
        mike.say "Yeah, I kind of like science fiction, I guess."
        mike.say "But it's more for the stories than the special effects, you know?"
        show cherie smile
        "Cherie nods and smiles, not seeming put off in the least."
        "And I watch as she walks slowly towards the bed."
        show cherie happy
        cherie.say "So if you watch so many of these fantastical films..."
        cherie.say "Then you must also have a very active imagination..."
        cherie.say "Is that not so?"
        show cherie amused
        mike.say "Erm..."
        mike.say "I guess you could say that."
        show cherie happy
        cherie.say "Then why don't you show me just what wonders you an imagine for me?"
        show cherie amused topless with dissolve
        "As if it wasn't clear to me what Cherie's suggesting, I see that she's already pulling off her top."
        "And I begin to do the same without as much as a conscious thought."
        show cherie amused naked with dissolve
        "Feeling my natural instincts take over as my brain almost loses the ability to function."
        "My desire for Cherie pushing everything else to the side."
    else:
        scene bg house
        show cherie at center, zoomAt(1.25, (640, 880))
        with fade
        "Thankfully this isn't the first time that I've brought Cherie back to my place."
        "And so I don't feel the need to apologise for the humble nature of it to her."
        "Even though she's still more used to residing in a mansion many times its size."
        "In fact Cherie seems just take it all in her stride by now, not even passing comment."
        "She simply follows me up the path to the front-door and waits patiently as I open it."
        "Then we both hurry inside, making sure to close it behind us and ensure it's locked."
        scene bg bedroom1
        show cherie at center, zoomAt(1.25, (640, 880))
        with fade
        "From there it's just a case of a short dash to the door of my bedroom."
        "Luckily we don't bump into one of my housemates along the way."
        "Which means that we can close the door behind us and finally be alone."
        show cherie smile naked at center, zoomAt(1.35, (640, 960)) with fade
        "Though it's Cherie that almost pounces on me the moment that happens."
        "Almost tearing at my clothes like an animal that's intent on devouring its prey!"
    $ game.room = "bedroom1"
    return

label cherie_fuck_date_foreplay_male:
    menu:
        "Suggest a blowjob" if cherie.sub >= 10:
            call cherie_fuck_date_blowjob from _call_cherie_fuck_date_blowjob


        "Eat her pussy" if hero.sexperience >= 5:
            call cherie_fuck_date_cunnilingus from _call_cherie_fuck_date_cunnilingus
        "Fuck her right now":
            pass
    call stop_all_sfx from _call_stop_all_sfx_49

    return _return

label cherie_fuck_date_choices_male:
    menu:
        "Cowgirl":
            call cherie_fuck_date_cowgirl (0) from _call_cherie_fuck_date_cowgirl
        "Reverse cowgirl" if hero.sexperience >= 5:
            call cherie_fuck_date_reverse (5) from _call_cherie_fuck_date_reverse
        "Doggy" if hero.sexperience >= 10:
            call cherie_fuck_date_doggy (10) from _call_cherie_fuck_date_doggy
        "Standing" if hero.sexperience >= 15:
            call cherie_fuck_date_standing (15) from _call_cherie_fuck_date_standing
    call stop_all_sfx from _call_stop_all_sfx_50

    return _return

label cherie_fuck_date_sleep(location="hero"):
    scene bg bedroom1
    if game.hour > 19 or game.hour < 6:
        show cherie naked talkative at center, zoomAt(1.25, (640, 880))
        if cherie.is_sex_slave:
            cherie.say "May I share your bed tonight, Master?"
        else:
            cherie.say "Mmm...you cool with me spending the night here?"
        show cherie normal
        menu:
            "No":
                mike.say "No...I have to be up really early in the morning."
                "The sex was beyond incredible, but now I want to be alone."
                "Cherie frowns in disappointment, clearly trying to shrug off the sense of rejection."
                cherie.say "Okay...sleep well, I guess."
                "She shakes her head as she collects her things and leaves my bedroom."
                $ cherie.love -= 3
                call sleep from _call_sleep_125
            "Yes":
                mike.say "YES...I mean, yes...if you want to!"
                "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                show cuddle cherie
                "Cherie curling up against me beneath the covers is almost as good as the sex - almost..."
                if cherie.is_sex_slave:
                    cherie.say "Sweet dreams, Master..."
                else:
                    cherie.say "Sweet dreams, [hero.name]..."
                mike.say "You too, Cherie..."
                $ cherie.love += 3
                call sleep ("cherie") from _call_sleep_126
    return

label cherie_fuck_date_blowjob:
    "Now that we're both naked, I find that I can't keep my eyes off of Cherie's naked body."
    "I know that's not any kind of surprise, but there's just something exceptional about her."
    "Maybe it's the fact that I've had to wait so long to be able to see her like this?"
    "And I guess that the feeling must be mutual, because she's looking at me in the exact same way."
    "Or to be more precise, Cherie's looking at a certain part of my anatomy right now."
    "And it seems that she's already imagining just what she could do with it too."
    "Of course, that fact that she's staring straight at my cock doesn't go unnoticed."
    "The very knowledge of it soon begins to have a visible effect on me too."
    "Knowing that Cherie wants it makes me begin to stiffen and it slowly rises upwards."
    "Which only serves to make her all the more keen on getting hold of it."
    "And so we're kind of locked into an inevitable snowballing effect."
    "The more Cherie looks at it, the bigger it gets."
    "And the bigger it gets, the more Cherie looks at it."
    hide cherie
    show cherie bj
    with fade
    "I watch as she kneels down in front of me, eyes fixated on the head."
    "Finally it rises to the point where it's almost on a level with her eyes too."
    "And that's when I feel the momentum passes between us, from me to Cherie."
    "She nods, as though acknowledging that something big is about to happen."
    cherie.say "Do not worry, mon ami..."
    cherie.say "I think that I already know what you want."
    cherie.say "And it is the same thing that I want too!"
    "I'm about to say something in response, but then it turns into a soft gasp."
    "Because in the very same moment, Cherie parts her lips and leaps into action."
    show cherie bj suck pleasure
    "They close around the tip of my cock, and I feel the corresponding tip of her tongue."
    "And then slowly, almost achingly, she begins to take it into her mouth."
    "Nothing that Cherie does to me is sudden or surprising in nature."
    "Instead it's gradual and done with an infinite amount of care."
    "But all the same I still feel the sensations of it hitting me pretty hard."
    "And that combined with the care that she's taking seems to rattle me to the core."
    "In fact it feels so good that I can sense my legs beginning to tremble."
    show cherie bj closed
    "By now Cherie has me a few inches into her mouth, her eyes closed as she works away."
    "And the waves of pleasure that I can feel radiating outwards are really affecting me."
    "As another hits, I can't help swaying, as if my muscles are starting to turn weaken."
    "I reach out with both hands, bracing myself against the nearest solid object."
    "But luckily for me, Cherie doesn't seem to notice the effect she's having on me."
    "And it only seems to become that much more intense as she swallows me further."
    "Now she's starting to move her head back and forth, sucking as she does so."
    "I've lost the sense of just how deep she's taken my cock by now."
    "But there doesn't seem to be any sign of it hampering her."
    "Eyes firmly closed and focussed on the task at hand, she just presses onwards."
    "And part of me wishes that I could be as cool and professional as she's being."
    "But the truth is that every second this lasts feels like a miracle to me."
    "I'm sure that any moment I'm going to lose the ability to hold on."
    "And that fact must be reflected in the way my body is reacting too."
    show cherie bj heart
    "Because just before I slip over the edge, Cherie's eyes pop open."
    "She looks up at me, silently seeking confirmation of what to do next."
    menu:
        "Cum on her face" if cherie.sub >= 25:
            "As quickly as I can, I make a sweeping gesture with my hands in front of Cherie's face."
            show cherie bj outside with vpunch
            "And she seems to understand what I mean by it, because she instantly lets me slide out of her mouth."
            "All of this happens just in time, as almost the same moment my cock is free, I start to lose it."
            show cherie bj cum with vpunch
            "Cherie doesn't move in inch as I shoot my load either, simply closing her eyes and staying perfectly still."
            show cherie bj cum bodycum with vpunch
            "Which means that she takes the whole thing square in the face, sticky white lines painting her cheeks and nose."
            $ cherie.love += 1
            $ cherie.sub += 1
        "Cum in her mouth" if cherie.sub >= 50:
            "As quickly as I can, I point downwards, trying to let Cherie know I want her to swallow."
            "And she seems to understand what I mean by it, because she keeps right on going."
            show cherie bj cum with vpunch
            "Prepared for what's going to happen next, she also doesn't miss a beat as I shoot my load."
            "Instead she swallows down every last drop, not pausing once as she does so."
            "Whereas I find myself gasping and for air as release finally comes."
            $ cherie.love += 2
            $ cherie.sub += 2
        "Hold on":
            "As quickly as I can, I shake my head and make to pull backwards."
            "Cherie seems to understand that I want to keep myself from losing it."
            show cherie bj outside with vpunch
            "And so she allows my cock to slide smoothly out of her mouth."
            "Not protesting the decision, as she no doubt knows that she'll soon be rewarded for her patience."
    hide cherie bj
    show expression "bg [game.room]"
    show cherie naked
    return










































































label cherie_fuck_date_cunnilingus:
    "Now that we're both naked, I find that I can't keep my eyes off of Cherie's naked body."
    "I know that's not any kind of surprise, but there's just something exceptional about her."
    "Maybe it's the fact that I've had to wait so long to be able to see her like this?"
    "And I guess that the feeling must be mutual, because she's looking at me in the exact same way."
    "Or to be more precise, Cherie's looking at a certain part of my anatomy right now."
    "And it seems that she's already imagining just what she could do with it too."
    "Of course, that fact that she's staring straight at my cock doesn't go unnoticed."
    "The very knowledge of it soon begins to have a visible effect on me too."
    "Knowing that Cherie wants it makes me begin to stiffen and it slowly rises upwards."
    "Which only serves to make her all the more keen on getting hold of it."
    "And so we're kind of locked into an inevitable snowballing effect."
    "The more Cherie looks at it, the bigger it gets."
    show cherie normal blush
    "And the bigger it gets, the more Cherie looks at it."
    "That's when I feel the momentum passes between us, from me to Cherie."
    "She nods, as though acknowledging that something big is about to happen."
    show cherie happy
    cherie.say "Do not worry, mon ami..."
    cherie.say "I think that I already know what you want."
    cherie.say "And it is the same thing that I want too!"
    show cherie normal
    "But before she can take the head of my cock in her mouth, I put my hands on her shoulders."
    "The gesture seems to surprise Cherie, stopping her in her tracks."
    show cherie stuned
    "And it also means that she offers no resistance as I guide her to sit down."
    "Cherie gaze up at me as I lie her down and then turn myself around above her."
    mike.say "I think I know what you want too, Cherie..."
    scene bg black
    show cherie cunnilingus
    with fade
    "Seeking to demonstrate my point, I lower my head between Cherie's thighs."
    "And then I part my lips just before they touch the lips of her pussy."
    "My tongue darts out, beginning to trace the soft folds that surround it."
    "At first I can hear the sound of Cherie moaning with please at my efforts."
    "I'm doing the best I can to be delicate and go lightly."
    show cherie cunnilingus closed
    "Instantly I feel her tense and the sound of her gasping."
    "But she doesn't try to stop me, and I take that as a good sign."
    "Pushing my tongue deeper still, I start to probe and explore."
    "And pretty soon I'm diving deeper than ever into her pussy."
    "Pushing the tip of my tongue downwards as quickly as I can."
    show cherie cunnilingus pleasure
    "The more pleasure Cherie expresses, the more I feel compelled to give in return."
    "Just like before, when her desire for my manhood and my desire for her fed into each other, that's what happens now."
    show cherie cunnilingus closed
    "And those efforts are returned in what feels like and endless cycle of escalation."
    "And part of me wishes that we could go on like this forever."
    "But the truth is that every second this lasts feels like a miracle to me."
    "I'm sure that any moment Cherie is going to lose the ability to hold on."
    "And Cherie proves me right just a second later."
    show cherie cunnilingus pleasure
    cherie.say "Oh...Oh..."
    cherie.say "I'm going to..."
    cherie.say "I'm going to cum!"
    with vpunch
    "Every muscle in her body seems to clench at the exact same second."
    show cherie cunnilingus closed with vpunch
    "It's like she's pulling all of her energy into the very centre of her being."
    show cherie cunnilingus pleasure with vpunch
    "And then it's all released with the next breath that leaves her body."
    "Those same muscles are suddenly limp as she melts into the afterglow."
    "Turning my head to gaze back over my shoulder, I see her waiting for instruction."
    "She practically glows as her orgasm is slowly fading."
    "Silently seeking confirmation of what to do next."
    hide cherie bj
    show expression "bg [game.room]"
    show cherie naked
    return


label cherie_fuck_date_doggy(sexperience_min):
    hide cherie
    show cherie doggy
    with fade
    "There's just something about seeing Cherie from behind, appreciating the lines and curves of her body."
    "So much so that I find myself reaching out and putting my hands on her waist, holding onto her haunches."
    "For her own part, Cherie seems to be eager to put herself firmly into my grasp."
    "As she makes no effort to pull away as I take hold of her and begin to move her body according to my desires."
    "And when I start to guide her downwards towards the floor, she goes along with it too."
    "Soon enough, Cherie is down on all fours in front of me, looking back over her shoulder."
    "She's right there for the taking, the mere sight of her making me painfully hard."
    menu:
        "Fuck her pussy":
            "I can't resist the temptation to take full advantage of Cherie's position."
            "And so I slide one hand from her waist over her stomach and between her thighs."
            "Cherie lets out a gasp of surprise and arousal as my fingers find the edge of her pussy."
            "At the same time she makes no effort to pull away, instead pushing herself downwards."
            "Which means that the tips of my fingers are pressed against those warm, wet lips."
            if cherie.sub >= 25:
                cherie.say "Oh, [hero.name] - please...please use me?"
            elif cherie.sub < -25:
                cherie.say "[hero.name] - you must do all that you can to pleasure me!"
            else:
                cherie.say "Oh, [hero.name] - I want to feel you inside of me!"
            "Oh man - like I needed any encouragement to want to do that!"
            "The only thing that I can think of right now is getting inside of Cherie."
            call check_condom_usage (cherie) from _call_check_condom_usage_160
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show cherie doggy condom
            show cherie doggy
            with fade
            "I'm about to begin lining myself up to take advantage of the position that Cherie's in."
            "Working out the best way to maximise my angle and make sure that I hit the target on the first attempt."
            "But the few seconds that should take seems to be far too long of a time for Cherie to be able to wait."
            "Because all of a sudden, I feel her reach back and take a firm hold of the shaft of my cock!"
            mike.say "Wha..."
            mike.say "Whoa..."
            mike.say "Settle down, Cherie!"
            cherie.say "I cannot, mon ami…"
            cherie.say "Not until I have this magnificent thing inside of me!"
            cherie.say "So then - where is it to go?"
            with hpunch
            "Cherie underlines her point by giving my cock a hard tug."
            "And that's more than enough to make me leap to attention."
            mike.say "Urgh..."
            mike.say "Pussy..."
            mike.say "It's going in the pussy!"
            "Cherie nods as she turns her head back to face the front."
            "And at the same time she also presses the head of my cock hard against the lips of her pussy."
            show cherie doggy vaginal at startle(0.07, -15)
            "I can already feel just how hot and wet it feels as the tip slides all over those soft folds."
            "The feeling beginning to explain to me just how desperate Cherie must be for it right now."
            "But there's no need for her to fear not getting what she wants."
            "Because I can feel a similar need rising inside of me."
            "And it's getting harder to hold back with each second that passes."
            show cherie doggy at startle(0.07, -15)
            pause 0.25
            show cherie doggy at startle(0.07, -15)
            "Cherie begins to moan and nod her head as I start to move behind her."
            "Every pass that I make sees her push herself backwards against me."
            "And we're both applying more pressure each time it happens too."
            "From my position it feels like we're the gears in a human machine."
            show cherie doggy at startle(0.07, -15)
            pause 0.25
            show cherie doggy at startle(0.07, -15)
            "Desperately moving against each other while trying to mesh correctly."
            "And thankfully that's just what our bodies are designed to do in this situation."
            "So when I finally feel the inevitable sensation of Cherie opening up to me, I go for it."
            show cherie doggy at startle(0.07, -15)
            pause 0.2
            show cherie doggy at startle(0.07, -15)
            "There's no sense of relaxing or slowing down as I feel myself sinking into her."
            "Instead it's quite the opposite, as I instantly begin to pick up speed."
            "Before I was just moving back and forth, trying to get in there."
            show cherie doggy at startle(0.07, -15)
            pause 0.2
            show cherie doggy at startle(0.07, -15)
            "But now I'm aiming myself downwards as I thrust, burying myself in Cherie."
            "It's like I want to get as deep as I possibly can as quickly as I can manage."
            show cherie doggy at startle(0.07, -15)
            pause 0.2
            show cherie doggy at startle(0.05, -10)
            "This means that she's almost pinned to the floor by my efforts."
            "Her legs splaying out beneath her as her body struggles to handle the force of it all."
            "But there's no sign whatsoever of Cherie wanting me to slow down, not for an instant."
            "Because I can see her doing all she can to brace herself, to absorb what I'm giving her."
            "And all the time I can see that her head is still nodding, telling me that she wants it."
            show cherie doggy at startle(0.07, -15)
            pause 0.2
            show cherie doggy at startle(0.05, -10)
            "So I channel all of my efforts into ploughing Cherie, going as deep and hard as I can."
            "By now my desire for her is so intense that I can't see the sophisticated woman I've come to desire."
            "Instead I feel like I'm staring down at the most irresistible and sexual creature imaginable."
            "The Cherie before me is a carnal animal, the mate that my most primitive self could imagine."













            "And that's the only thing on my mind, the singular need to make Cherie mine and mine alone."
            show cherie doggy at startle(0.05, -10)
            pause 0.15
            show cherie doggy at startle(0.05, -10)
            "Cherie begins to pant now, and I feel like she's perfectly matching my speed and force."
            show cherie doggy at startle(0.05, -10)
            pause 0.15
            show cherie doggy at startle(0.05, -10)
            "Our bodies seem to be moving in perfect synchronicity, complimenting each other to an insane degree."
            "Part of me wishes that we could just keep on going like this forever."
            show cherie doggy at startle(0.05, -10)
            pause 0.15
            show cherie doggy at startle(0.05, -10)
            "But I can already feel the sensation of my legs beginning to quiver."
            "And I know that I'm not going to be able to hold on for much longer."



            show cherie doggy at startle(0.05, -10)
            pause 0.15
            show cherie doggy at startle(0.05, -10)
            "So I make one final effort, pushing myself and Cherie in turn, over the edge."
            call cum_reaction (cherie, 'vaginal', sexperience_min) from _call_cum_reaction_294
            if _return == "vaginal_condom":
                show cherie doggy at startle(0.05, -10)
                "One final push is all it takes for me to reach my climax."
                "And as I do so, I silently thank my past self for using a condom."
                show cherie doggy pleasure with vpunch
                "Because it means that I can just let go and explode inside of Cherie."
                with vpunch
                "She seems to appreciate that foresight too, wriggling and writhing under me as she cums."





            elif _return == "vaginal_inside_pregnant":
                cherie.say "Don't...stop..."
                cherie.say "Remember...I am...pregnant!"
                "One final push is all it takes for me to reach my climax."
                "And as I do so, I silently thank Cherie for that timely reminder."
                $ cherie.love += 3
                show cherie doggy cum pleasure with vpunch
                "Because it means that I can just let go and explode inside of her."
                with vpunch
                "She seems to appreciate that foresight too, wriggling and writhing under me as she cums."
            elif _return == "vaginal_inside_pill":
                cherie.say "Don't...stop..."
                cherie.say "Remember...I am...on the pill!"
                show cherie doggy at startle(0.05, -10)
                "One final push is all it takes for me to reach my climax."
                "And as I do so, I silently thank Cherie for that timely reminder."
                $ cherie.love += 2
                show cherie doggy cum pleasure with vpunch
                "Because it means that I can just let go and explode inside of her."
                "She seems to appreciate that foresight too, wriggling and writhing under me as she cums."
            elif _return == "vaginal_inside_mad":
                cherie.say "Stop...pull out"
                cherie.say "Before it is...too late!"
                "I hear the words and they seem to make sense to me."
                "But the problem is that there's no time to act on them."
                $ cherie.impregnate()
                show cherie doggy cum pleasure with vpunch
                "Cherie moans as I shoot my load deep inside of her."
                with vpunch
                "And then she hurriedly shuffles forwards, pulling herself off me."
                "Even though it's too late for that to be of any use."
                hide cherie
                show cherie naked upset at center, zoomAt(1.5, (640, 1040))
                with fade
                $ cherie.love -= 5
                "Then we end up just staring at each other as the reality of what just happened finally starts to sink in."
            elif _return == "vaginal_inside_happy":
                mike.say "Oh shit..."
                mike.say "I need to pull out!"
                "I make to do just that, beginning to pull myself backwards."
                "But the moment I do so, Cherie surprises me by moving in the same direction."
                "This means that I remain buried inside of her until it's too late."
                $ cherie.love += 5
                $ cherie.impregnate()
                show cherie doggy cum pleasure with vpunch
                "A second later I lose it, shooting my load into Cherie."
                with vpunch
                "She almost purrs with pleasure as it happens, seeming to be delighted with what just happened."
                "But I'm left slack-jawed and speechless, unable to process what just happened."
            elif _return == "vaginal_outside":
                menu:
                    "Cum on her body":
                        "Somehow I manage to keep my mind clear enough to remember the need to pull out."
                        if CONDOM:
                            "With a quick movement, I remove the condom."
                        show cherie doggy outside cum pleasure with vpunch
                        "And that's just what I do, mere moments before I lose it and shoot my load."
                        show cherie doggy oncherie with vpunch
                        "But the act of pulling out doesn't seem to do anything to lessen Cherie's pleasure."
                        show cherie doggy onmike with vpunch
                        "In fact it looks like that's what finally pushes her over the edge too."
                        "As she writhes and wriggles in front of me as I shower her buttocks a moment later."
                        $ cherie.love += 1
                    "Cum on her face" if cherie.sub >= 25:
                        "As quickly as I can, I make a sweeping gesture with my hands in front of Cherie's face."
                        "And she seems to understand what I mean by it, because she instantly lets me slide out of her."
                        if CONDOM:
                            "With a quick movement, I remove the condom."
                        hide cherie
                        show cherie bj heart
                        with hpunch
                        "All of this happens just in time, as almost the same moment my cock is free, I start to lose it."
                        show cherie bj closed cum with vpunch
                        "Cherie quickly turns around and sits up, then closes her eyes and staying perfectly still."
                        with vpunch
                        "Which means that she takes the whole thing square in the face, sticky white lines painting her cheeks and nose."
                        $ cherie.love += 1
                        $ cherie.sub += 1
                    "Cum in her mouth" if cherie.sub >= 50:
                        "As quickly as I can, I point downwards, trying to let Cherie know I want her to swallow."
                        "And she seems to understand what I mean by it, because she lets me slide out of her."
                        if CONDOM:
                            "With a quick movement, I remove the condom."
                        hide cherie
                        show cherie bj heart pleasure suck
                        with hpunch
                        "Then she turns around and quickly opens her mouth, letting my cock fill it to capacity."
                        show cherie bj cum with vpunch
                        "Prepared for what's going to happen next, she also doesn't miss a beat as I shoot my load."
                        show cherie bj closed with vpunch
                        "Instead she swallows down every last drop, not pausing once as she does so."
                        "Whereas I find myself gasping and for air as release finally comes."
                        $ cherie.love += 2
                        $ cherie.sub += 2
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "I can't resist the temptation to take full advantage of Cherie's position."
            "And so I slide one hand from her waist over her stomach and between her thighs."
            "Cherie lets out a gasp of surprise and arousal as my fingers find the edge of her hole."
            "At the same time she makes no effort to pull away, instead pushing herself downwards."
            "Which means that the tips of my fingers are pressed against that tight little hole."
            if cherie.sub >= 25:
                cherie.say "Oh, [hero.name] - please...please use me?"
            elif cherie.sub <= -25:
                cherie.say "[hero.name] - you must do all that you can to pleasure me!"
            else:
                cherie.say "Oh, [hero.name] - I want to feel you inside of me!"
            "Oh man - like I needed any encouragement to want to do that!"
            "The only thing that I can think of right now is getting inside of Cherie."
            scene bg black
            show cherie doggy
            with fade
            "I'm about to begin lining myself up to take advantage of the position that Cherie's in."
            "Working out the best way to maximise my angle and make sure that I hit the target on the first attempt."
            "But the few seconds that should take seems to be far too long of a time for Cherie to be able to wait."
            "Because all of a sudden, I feel her reach back and take a firm hold of the shaft of my cock!"
            mike.say "Wha..."
            mike.say "Whoa..."
            mike.say "Settle down, Cherie!"
            cherie.say "I cannot, mon ami…"
            cherie.say "Not until I have this magnificent thing inside of me!"
            cherie.say "So then - where is it to go?"
            with hpunch
            "Cherie underlines her point by giving my cock a hard tug."
            "And that's more than enough to make me leap to attention."
            mike.say "Urgh..."
            mike.say "Ass..."
            mike.say "It's going in the ass!"
            "Cherie nods as she turns her head back to face the front."
            "And at the same time she also presses the head of my cock hard against the edge of her hole."
            show cherie doggy anal at startle(0.07, -15)
            "I can already feel just how hot and wet it feels as the tip slides around back there."
            "The feeling beginning to explain to me just how desperate Cherie must be for it right now."
            "But there's no need for her to fear not getting what she wants."
            "Because I can feel a similar need rising inside of me."
            "And it's getting harder to hold back with each second that passes."
            show cherie doggy at startle(0.07, -15)
            pause 0.25
            show cherie doggy at startle(0.07, -15)
            "Cherie begins to moan and nod her head as I start to move behind her."
            "Every pass that I make sees her push herself backwards against me."
            "And we're both applying more pressure each time it happens too."
            "From my position it feels like we're the gears in a human machine."
            show cherie doggy at startle(0.07, -15)
            pause 0.25
            show cherie doggy at startle(0.07, -15)
            "Desperately moving against each other while trying to mesh correctly."
            "And thankfully that's just what our bodies are designed to do in this situation."
            "So when I finally feel the inevitable sensation of Cherie opening up to me, I go for it."
            show cherie doggy at startle(0.07, -15)
            pause 0.2
            show cherie doggy at startle(0.07, -15)
            "There's no sense of relaxing or slowing down as I feel myself sinking into her."
            "Instead it's quite the opposite, as I instantly begin to pick up speed."
            "Before I was just moving back and forth, trying to get in there."
            show cherie doggy at startle(0.07, -15)
            pause 0.2
            show cherie doggy at startle(0.07, -15)
            "But now I'm aiming myself downwards as I thrust, burying myself in Cherie."
            "It's like I want to get as deep as I possibly can as quickly as I can manage."
            show cherie doggy at startle(0.07, -15)
            pause 0.2
            show cherie doggy at startle(0.05, -10)
            "This means that she's almost pinned to the floor by my efforts."
            "Her legs splaying out beneath her as her body struggles to handle the force of it all."
            "But there's no sign whatsoever of Cherie wanting me to slow down, not for an instant."
            "Because I can see her doing all she can to brace herself, to absorb what I'm giving her."
            "And all the time I can see that her head is still nodding, telling me that she wants it."
            show cherie doggy at startle(0.07, -15)
            pause 0.2
            show cherie doggy at startle(0.05, -10)
            "So I channel all of my efforts into ploughing Cherie, going as deep and hard as I can."
            "By now my desire for her is so intense that I can't see the sophisticated woman I've come to desire."
            "Instead I feel like I'm staring down at the most irresistible and sexual creature imaginable."
            "The Cherie before me is a carnal animal, the mate that my most primitive self could imagine."













            "And that's the only thing on my mind, the singular need to make Cherie mine and mine alone."

            "Cherie begins to pant now, and I feel like she's perfectly matching my speed and force."
            show cherie doggy at startle(0.05, -10)
            pause 0.15
            show cherie doggy at startle(0.05, -10)
            "Our bodies seem to be moving in perfect synchronicity, complimenting each other to an insane degree."
            "Part of me wishes that we could just keep on going like this forever."
            show cherie doggy at startle(0.05, -10)
            pause 0.15
            show cherie doggy at startle(0.05, -10)
            "But I can already feel the sensation of my legs beginning to quiver."
            "And I know that I'm not going to be able to hold on for much longer."



            show cherie doggy at startle(0.05, -10)
            pause 0.15
            show cherie doggy at startle(0.05, -10)
            "So I make one final effort, pushing myself and Cherie in turn, over the edge."
            call cum_reaction (cherie, 'anal', sexperience_min) from _call_cum_reaction_315
            if _return == "anal_inside":
                "One final push is all it takes for me to reach my climax."
                "And I make a point of holding onto those haunches even tighter, just to be sure."
                $ cherie.love += 2
                show cherie doggy cum pleasure with vpunch
                "Which means that I can just let go and explode inside of Cherie's ass."
                with vpunch
                "She seems to appreciate the effort too, wriggling and writhing under me as she cums."
            elif _return == "anal_outside":
                menu:
                    "Cum on her body":
                        "Somehow I manage to keep my mind clear enough to remember the need to pull out of her ass."
                        show cherie doggy outside cum pleasure with vpunch
                        "And that's just what I do, mere moments before I lose it and shoot my load."
                        show cherie doggy oncherie with vpunch
                        "But the act of pulling out doesn't seem to do anything to lessen Cherie's pleasure."
                        show cherie doggy onmike with vpunch
                        "In fact it looks like that's what finally pushes her over the edge too."
                        "As she writhes and wriggles in front of me as I shower her buttocks a moment later."
                        $ cherie.love += 1
                    "Cum on her face" if cherie.sub >= 25:
                        "As quickly as I can, I make a sweeping gesture with my hands in front of Cherie's face."
                        "And she seems to understand what I mean by it, because she instantly lets me slide out of her ass."
                        hide cherie
                        show cherie bj heart
                        with hpunch
                        "All of this happens just in time, as almost the same moment my cock is free, I start to lose it."
                        show cherie bj closed cum with vpunch
                        "Cherie quickly turns around and sits up, then closes her eyes and staying perfectly still."
                        with vpunch
                        "Which means that she takes the whole thing square in the face, sticky white lines painting her cheeks and nose."
                        $ cherie.love += 1
                        $ cherie.sub += 1
                    "Cum in her mouth" if cherie.sub >= 50:
                        "As quickly as I can, I point downwards, trying to let Cherie know I want her to swallow."
                        "And she seems to understand what I mean by it, because she lets me slide out of her ass."
                        hide cherie
                        show cherie bj heart pleasure suck
                        with hpunch
                        "Then she turns around and quickly opens her mouth, letting my cock fill it to capacity."
                        show cherie bj cum with vpunch
                        "Prepared for what's going to happen next, she also doesn't miss a beat as I shoot my load."
                        show cherie bj closed with vpunch
                        "Instead she swallows down every last drop, not pausing once as she does so."
                        "Whereas I find myself gasping and for air as release finally comes."
                        $ cherie.love += 2
                        $ cherie.sub += 2
    return

label cherie_fuck_date_cowgirl(sexperience_min):
    hide cherie
    show cherie flirt naked at center, zoomAt(1.25, (640, 880))
    with fade
    "Now that we're both naked, there's obviously only one thing on my mind."
    "And that's getting Cherie over to the bed as soon as humanly possible."
    "But luckily for me it seems that we're both totally on the same page."
    "As she holds out her hand to me, letting me take it and lead her straight there."
    show cherie at center, traveling(1.5, 0.3, (640, 1040))
    "In fact Cherie almost seems to be hurrying me along as we cover the few feet to the bed."
    "Like she's trying her best to hold back and let me take the lead."
    "But part of her is almost unable to keep from wanting to speed things up."
    "This means that by the time we make it over there, I kind of trying to slow her down."
    "And we end up doing a weird little two-step at the side of the bed."
    mike.say "Cherie..."
    mike.say "Do you want to come this way..."
    mike.say "And then I can..."
    show cherie happy blush
    if cherie.sub >= 25:
        cherie.say "Where do you want me, mon ami?"
        cherie.say "Just...just tell me where to go!"
    elif cherie.sub <= -25:
        cherie.say "Will you make up your mind, mon ami?"
        cherie.say "Because if not, then I will have to make it up for you!"
    else:
        cherie.say "Where should I be going, mon ami?"
        cherie.say "I do not know if I am supposed to be coming or going!"
    show cherie normal
    "In the end it's neither of us that gets the chance to decide where this is going."
    "As gravity soon steps in and makes the decision itself."
    show cherie stuned with hpunch
    "First I twist one way and then Cherie bends in another."
    hide cherie with easeoutbottom
    "All of which means that I lose my balance and fall onto the bed."
    "And as she's kind of tied herself up with me, Cherie's dragged down at the same time."
    scene bg black
    show cherie cowgirl
    with vpunch
    "Falling first, I land on my back arms and legs spread out on the mattress."
    "Luckily, Cherie manages to get her hands down before she lands on top of me."
    "Which leaves her staring down at me from above."
    if cherie.sub >= 25:
        cherie.say "How about this, mon ami?"
        cherie.say "Do you approve of this position?"
    elif cherie.sub <= -25:
        cherie.say "Mmm...I like the feeling of this position, mon ami."
        cherie.say "So I think that we will be staying right where we are!"
    else:
        cherie.say "It seems that we have fallen into place, does it not?"
        cherie.say "So what do you say we accept the hand fate has dealt us?"
    "I find myself nodding without the need for a single conscious thought."
    "Because the view from where I'm laid is simply magnificent."
    "And so by way of an answer, I reach up and begin to run my hands over Cherie's body."
    "At the same time she straddles me, lowering herself even more than before."
    "Which in turn means that I can reach even more of her with my hands."
    "And I could just keep on doing that for a good while longer too."
    "But I can already see that Cherie wants more from me as she lowers herself even more."
    "Allof which means that I'm going to have too make an important decision pretty soon."
    menu:
        "Fuck her pussy":
            "I'm way too invested in what we're doing to even think about parts of Cherie hidden from view right now."
            "So to me, the only possible goal that I could be working towards is getting inside of her pussy."
            "And luckily for me, the position that she's adopted means that it's no more than an inch away from my cock."
            call check_condom_usage (cherie) from _call_check_condom_usage_161
            if _return == False:
                return "leave_without_gain"
            show cherie cowgirl at startle(0.05,-10)
            with fade
            "Putting my hands on the top of Cherie's thighs, I begin to pull her downwards."
            "At the same time I'm also making sure that my cock is in just the right position too."
            "She seems to be able to read my intentions without the need to exchange a single word."
            "Because the next thing I know, Cherie reaches down with one hand."
            "I gasp at the sensation of her gently grasping the shaft and beginning to stroke it."
            "But of course that's not all she's doing, as she also helps to direct traffic down there."
            "All of this means that we come together slowly and smoothly, as well as in almost perfect harmony."
            show cherie cowgirl at startle(0.05,-10)
            "As soon as everything is in place, I begin to move in a subtle, controlled manner."
            "Making sure that the head of my cock slides along the entire length of Cherie's lips."
            "The range of movement is small in the extreme, but the effect is instantly visible."
            show cherie cowgirl at startle(0.05,-10)
            "Cherie doesn't seem to have any choice but to start moving in sympathy to me."
            "It seems that she's trying to maximise the potential of each pass I make."
            "Almost doubling the effect it's having on her by doing so and thus speeding things up too."
            "And it seems to be working as well, because I can feel things getting warmer and more slippery by the second."
            "Suddenly there's a change in the motion happening down below, only a subtle shift."
            "But it's more than enough to totally kick things into a higher gear."
            show cherie cowgirl closed with vpunch
            "Cherie's lips part, just enough for the head of my cock to sink into her."
            "And once that happens, there's no turning back."
            "Cherie let's go of me and instead reaches out with her hands."
            "She places them on my arms, using them to brace herself."
            show cherie cowgirl pleasure at startle(0.07,-15)
            pause 0.25
            show cherie cowgirl at startle(0.07,-15)
            "And then she pushes down with all of her weight, making sure things only go in one direction."
            "Or to be more specific, she makes sure that one thing goes straight up and into her!"
            "I'm pushing upwards as all of this is happening, feeling it with genuine intensity."
            show cherie cowgirl at startle(0.07,-15)
            pause 0.25
            show cherie cowgirl at startle(0.07,-15)
            "Slowly, Cherie slides down and onto me, letting my cock fill her completely."
            "At first that's the only movement that the two of us make."
            show cherie cowgirl at startle(0.07,-15)
            pause 0.25
            show cherie cowgirl at startle(0.07,-15)
            "Her pressing down from above as I push up from below."
            "And for a moment that seems to be all either of us is going to do."
            "As if we've been building towards this and neither of us knows what to do next."
            show cherie cowgirl at startle(0.05,-10)
            pause 0.15
            show cherie cowgirl closed at startle(0.05,-10)
            "So it comes as a genuine relief when I feel Cherie begin to pull herself upwards."
            "All the while she has a look on her face of pure, helpless pleasure."
            "And it doesn't take long for me to start moving in sympathy again."
            show cherie cowgirl at startle(0.05,-10)
            pause 0.15
            show cherie cowgirl pleasure at startle(0.05,-10)
            "With that movement comes a sense of growing urgency, which in turn leads to more speed."
            "All I have to do is hold on and keep thrusting up from below."
            "Which is something that I'm more than happy to do."
            show cherie cowgirl at startle(0.05,-10)
            pause 0.15
            show cherie cowgirl at startle(0.05,-10)














            "By now I'm totally focussed on giving Cherie as much pleasure as I possibly can."
            "Pacing myself so that my reserves of energy will last until the very end."
            "And it seems as though my efforts are paying off too, as I watch her reactions."
            show cherie cowgirl closed at startle(0.05,-10)
            pause 0.15
            show cherie cowgirl at startle(0.05,-10)
            "Cherie closes her eyes as her lips part and she lets out a helpless moan."
            "And as beautiful and subtle as the sight may be, it definitely affects me."
            show cherie cowgirl at startle(0.05,-10)
            pause 0.15
            show cherie cowgirl at startle(0.05,-10)
            "Because suddenly I can feel the limits of my stamina being reached."
            "And I know that I'm not going to be able to hang on much longer."



            "So I make one final effort, pushing myself and Cherie in turn, over the edge."
            show cherie cowgirl at startle(0.05,-10)
            pause 0.15
            show cherie cowgirl at startle(0.05,-10)
            call cum_reaction (cherie, 'vaginal', sexperience_min) from _call_cum_reaction_295
            if _return == "vaginal_condom":
                show cherie cowgirl at startle(0.05, -10)
                "One final push is all it takes for me to reach my climax."
                "And as I do so, I silently thank my past self for using a condom."
                show cherie cowgirl pleasure with vpunch
                "Because it means that I can just let go and explode inside of Cherie."
                with vpunch
                "She seems to appreciate that foresight too, wriggling and writhing under me as she cums."





            elif _return == "vaginal_inside_pregnant":
                cherie.say "Don't...stop..."
                cherie.say "Remember...I am...pregnant!"
                "One final push is all it takes for me to reach my climax."
                "And as I do so, I silently thank Cherie for that timely reminder."
                $ cherie.love += 3
                show cherie cowgirl cum pleasure with vpunch
                "Because it means that I can just let go and explode inside of her."
                with vpunch
                "She seems to appreciate that foresight too, wriggling and writhing under me as she cums."
            elif _return == "vaginal_inside_pill":
                cherie.say "Don't...stop..."
                cherie.say "Remember...I am...on the pill!"
                show cherie cowgirl at startle(0.05, -10)
                "One final push is all it takes for me to reach my climax."
                "And as I do so, I silently thank Cherie for that timely reminder."
                $ cherie.love += 2
                show cherie cowgirl cum pleasure with vpunch
                "Because it means that I can just let go and explode inside of her."
                "She seems to appreciate that foresight too, wriggling and writhing under me as she cums."
            elif _return == "vaginal_inside_mad":
                cherie.say "Stop...pull out"
                cherie.say "Before it is...too late!"
                "I hear the words and they seem to make sense to me."
                "But the problem is that there's no time to act on them."
                $ cherie.impregnate()
                show cherie cowgirl cum pleasure with vpunch
                "Cherie moans as I shoot my load deep inside of her."
                with vpunch
                "And then she hurriedly shuffles forwards, pulling herself off me."
                "Even though it's too late for that to be of any use."
                hide cherie
                show cherie naked upset at center, zoomAt(1.5, (640, 1040))
                with fade
                $ cherie.love -= 5
                "Then we end up just staring at each other as the reality of what just happened finally starts to sink in."
            elif _return == "vaginal_inside_happy":
                mike.say "Oh shit..."
                mike.say "I need to pull out!"
                "I make to do just that, beginning to pull myself backwards."
                "But the moment I do so, Cherie surprises me by moving in the same direction."
                "This means that I remain buried inside of her until it's too late."
                $ cherie.love += 5
                $ cherie.impregnate()
                show cherie cowgirl cum pleasure with vpunch
                "A second later I lose it, shooting my load into Cherie."
                "She almost purrs with pleasure as it happens, seeming to be delighted with what just happened."
                "But I'm left slack-jawed and speechless, unable to process what just happened."
            elif _return == "vaginal_outside":
                menu:
                    "Cum on her body":
                        "Somehow I manage to keep my mind clear enough to remember the need to pull out."
                        if CONDOM:
                            "With a quick movement, I remove the condom."
                        show cherie cowgirl cum pleasure with vpunch
                        "And that's just what I do, mere moments before I lose it and shoot my load."
                        show cherie cowgirl with vpunch
                        "But the act of pulling out doesn't seem to do anything to lessen Cherie's pleasure."
                        show cherie cowgirl bodycum with vpunch
                        "In fact it looks like that's what finally pushes her over the edge too."
                        "As she writhes and wriggles in front of me as I shower her buttocks a moment later."
                        $ cherie.love += 1
                    "Cum on her face" if cherie.sub >= 25:
                        "As quickly as I can, I make a sweeping gesture with my hands in front of Cherie's face."
                        "And she seems to understand what I mean by it, because she instantly lets me slide out of her."
                        if CONDOM:
                            "With a quick movement, I remove the condom."
                        hide cherie
                        show cherie bj heart
                        with hpunch
                        "All of this happens just in time, as almost the same moment my cock is free, I start to lose it."
                        show cherie bj closed cum with vpunch
                        "Cherie quickly turns around and sits up, then closes her eyes and staying perfectly still."
                        with vpunch
                        "Which means that she takes the whole thing square in the face, sticky white lines painting her cheeks and nose."
                        $ cherie.love += 1
                        $ cherie.sub += 1
                    "Cum in her mouth" if cherie.sub >= 50:
                        "As quickly as I can, I point downwards, trying to let Cherie know I want her to swallow."
                        "And she seems to understand what I mean by it, because she lets me slide out of her."
                        if CONDOM:
                            "With a quick movement, I remove the condom."
                        hide cherie
                        show cherie bj heart pleasure suck
                        with hpunch
                        "Then she turns around and quickly opens her mouth, letting my cock fill it to capacity."
                        show cherie bj cum with vpunch
                        "Prepared for what's going to happen next, she also doesn't miss a beat as I shoot my load."
                        show cherie bj closed with vpunch
                        "Instead she swallows down every last drop, not pausing once as she does so."
                        "Whereas I find myself gasping and for air as release finally comes."
                        $ cherie.love += 2
                        $ cherie.sub += 2
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "I'm kind of one of those guys that can never just take what's right there in front of him."
            "I mean anyone else would be fixated on Cherie's pussy, right?"
            "So to me, the only possible goal that I could be working towards is getting inside of her ass."
            "And luckily for me, the position that she's adopted means that it's no more than an inch away from my cock."
            "Putting my hands on the top of Cherie's thighs, I begin to pull her downwards."
            "At the same time I'm also making sure that my cock is in just the right position too."
            "She seems to be able to read my intentions without the need to exchange a single word."
            "Because the next thing I know, Cherie reaches down with one hand."
            "I gasp at the sensation of her gently grasping the shaft and beginning to stroke it."
            "But of course that's not all she's doing, as she also helps to direct traffic down there."
            "All of this means that we come together slowly and smoothly, as well as in almost perfect harmony."
            show cherie cowgirl at startle(0.05,-10)
            "As soon as everything is in place, I begin to move in a subtle, controlled manner."
            "Making sure that the head of my cock slides between Cherie's cheeks."
            "The range of movement is small in the extreme, but the effect is instantly visible."
            show cherie cowgirl at startle(0.05,-10)
            "Cherie doesn't seem to have any choice but to start moving in sympathy to me."
            "It seems that she's trying to maximise the potential of each pass I make."
            "Almost doubling the effect it's having on her by doing so and thus speeding things up too."
            "And it seems to be working as well, because I can feel things getting warmer and more slippery by the second."
            "Suddenly there's a change in the motion happening down below, only a subtle shift."
            "But it's more than enough to totally kick things into a higher gear."
            show cherie cowgirl closed with vpunch
            "Cherie's lips part, just enough for the head of my cock to sink into her."
            "And once that happens, there's no turning back."
            "Cherie let's go of me and instead reaches out with her hands."
            "She places them on my arms, using them to brace herself."
            show cherie cowgirl pleasure at startle(0.07,-15)
            pause 0.25
            show cherie cowgirl at startle(0.07,-15)
            "And then she pushes down with all of her weight, making sure things only go in one direction."
            "Or to be more specific, she makes sure that one thing goes straight up and into her!"
            "I'm pushing upwards as all of this is happening, feeling it with genuine intensity."
            show cherie cowgirl at startle(0.07,-15)
            pause 0.25
            show cherie cowgirl at startle(0.07,-15)
            "Slowly, Cherie slides down and onto me, letting my cock fill her completely."
            "At first that's the only movement that the two of us make."
            show cherie cowgirl at startle(0.07,-15)
            pause 0.25
            show cherie cowgirl at startle(0.07,-15)
            "Her pressing down from above as I push up from below."
            "And for a moment that seems to be all either of us is going to do."
            "As if we've been building towards this and neither of us knows what to do next."
            show cherie cowgirl at startle(0.05,-10)
            pause 0.15
            show cherie cowgirl closed at startle(0.05,-10)
            "So it comes as a genuine relief when I feel Cherie begin to pull herself upwards."
            "All the while she has a look on her face of pure, helpless pleasure."
            "And it doesn't take long for me to start moving in sympathy again."
            show cherie cowgirl at startle(0.05,-10)
            pause 0.15
            show cherie cowgirl pleasure at startle(0.05,-10)
            "With that movement comes a sense of growing urgency, which in turn leads to more speed."
            "All I have to do is hold on and keep thrusting up from below."
            "Which is something that I'm more than happy to do."















            "Pacing myself so that my reserves of energy will last until the very end."
            "And it seems as though my efforts are paying off too, as I watch her reactions."
            show cherie cowgirl closed at startle(0.05,-10)
            pause 0.15
            show cherie cowgirl at startle(0.05,-10)
            "Cherie closes her eyes as her lips part and she lets out a helpless moan."
            "And as beautiful and subtle as the sight may be, it definitely affects me."
            show cherie cowgirl at startle(0.05,-10)
            pause 0.15
            show cherie cowgirl at startle(0.05,-10)
            "Because suddenly I can feel the limits of my stamina being reached."
            "And I know that I'm not going to be able to hang on much longer."



            "So I make one final effort, pushing myself and Cherie in turn, over the edge."
            call cum_reaction (cherie, 'anal', sexperience_min) from _call_cum_reaction_316
            if _return == "anal_inside":
                "One final push is all it takes for me to reach my climax."
                "And I make a point of holding onto those haunches even tighter, just to be sure."
                $ cherie.love += 2
                show cherie cowgirl cum pleasure with vpunch
                "Which means that I can just let go and explode inside of Cherie's ass."
                with vpunch
                "She seems to appreciate the effort too, wriggling and writhing atop me as she cums."
            elif _return == "anal_outside":
                menu:
                    "Cum on her body":
                        "Somehow I manage to keep my mind clear enough to remember the need to pull out of her ass."
                        show cherie cowgirl pleasure with vpunch
                        "And that's just what I do, mere moments before I lose it and shoot my load."
                        show cherie cowgirl with vpunch
                        "But the act of pulling out doesn't seem to do anything to lessen Cherie's pleasure."
                        show cherie cowgirl bodycum with vpunch
                        "In fact it looks like that's what finally pushes her over the edge too."
                        "As she writhes and wriggles in front of me as I shower her buttocks a moment later."
                        $ cherie.love += 1
                    "Cum on her face" if cherie.sub >= 25:
                        "As quickly as I can, I make a sweeping gesture with my hands in front of Cherie's face."
                        "And she seems to understand what I mean by it, because she instantly lets me slide out of her ass."
                        hide cherie
                        show cherie bj heart
                        with hpunch
                        "All of this happens just in time, as almost the same moment my cock is free, I start to lose it."
                        show cherie bj closed cum with vpunch
                        "Cherie quickly turns around and sits up, then closes her eyes and staying perfectly still."
                        with vpunch
                        "Which means that she takes the whole thing square in the face, sticky white lines painting her cheeks and nose."
                        $ cherie.love += 1
                        $ cherie.sub += 1
                    "Cum in her mouth" if cherie.sub >= 50:
                        "As quickly as I can, I point downwards, trying to let Cherie know I want her to swallow."
                        "And she seems to understand what I mean by it, because she lets me slide out of her ass."
                        hide cherie
                        show cherie bj heart pleasure suck
                        with hpunch
                        "Then she turns around and quickly opens her mouth, letting my cock fill it to capacity."
                        show cherie bj cum with vpunch
                        "Prepared for what's going to happen next, she also doesn't miss a beat as I shoot my load."
                        show cherie bj closed with vpunch
                        "Instead she swallows down every last drop, not pausing once as she does so."
                        "Whereas I find myself gasping and for air as release finally comes."
                        $ cherie.love += 2
                        $ cherie.sub += 2
    return

label cherie_fuck_date_standing(sexperience_min):
    hide cherie
    show cherie flirt naked at center, zoomAt(1.25, (640, 880))
    with fade
    "You might have thought that a mature, sophisticated and absolutely stunning woman like Cherie would have technique for seduction."
    "That by now she'd be luring me into her web of wanton pleasure, controlling my every move with the slightest twitch of a finger."
    "But the truth of the matter is that she's simply standing in front of me, stripped naked and regarding me with an innocent smile."
    "And that's having pretty much the same kind of effect as all of the other crazy stuff that I just described."
    "Because it's not like Cherie actually has to do anything to be able to bend me to her will and command my complete devotion."
    "Oh no, the simple chance to gaze at her naked bottom is more than enough to make me hers to command!"
    show cherie happy blush
    if cherie.sub >= 25:
        cherie.say "Mon ami…"
        cherie.say "Why are you looking at me like that?"
    if cherie.sub <= -25:
        cherie.say "Oh, mon ami…"
        cherie.say "I cannot allow you just to stare at me all day!"
        cherie.say "Come now, do something to please me, if you truly can."
    else:
        cherie.say "I feel your eyes on me, mon ami…"
        cherie.say "And I think that you like what you see, no?"
    show cherie normal
    "The sound of Cherie's voice is more than enough to break me out of the trance-like state that I've been trapped in."
    "And I almost leap into the air as I begin moving again, wanting to do all that I can to please her."
    show cherie at center, traveling(1.5, 0.3, (640, 1040))
    "But as I hurry towards Cherie, reaching out with both hands, she surprises me by moving too."
    "I can't be sure if she's trying to slip out of my grasp or just to make sure that I catch her from a certain angle."
    "But whatever the reason, it means that she's almost turned her back on me by the time I actually get my hands on her."
    show cherie smile
    "Cherie reassures me that I'm doing what she wants by giggling and pressing her back against my chest."
    "Which has the very welcome advantage of her shapely butt grinding into my groin too!"
    show cherie normal
    cherie.say "Mmm..."
    show cherie happy
    cherie.say "I think that someone is ready for me down there."
    cherie.say "Please, mon ami - do not keep me waiting too much longer?"
    cherie.say "Mmm..."
    "Oh man, as if I'd do anything to keep from giving Cherie exactly what she wants!"
    scene bg black
    show cherie standing
    with fade
    "So it looks like we're going to be getting in on right here and now."
    "Doing it while we're both on our feet, without even making it to the bed."
    menu:
        "Fuck her pussy":
            "I make a point of taking a couple of steps forwards before really getting down to it."
            "A move that forces Cherie to keep shuffling ahead of me until she's almost up against the wall."
            "She reaches out with both hands, using them to keep herself from being pressed into it."
            "And at the same time she looks back over her shoulder, eyes filled with anticipation."
            "Obviously wondering with great interest what's going to happen next."
            "But all it takes is one brief glimpse of her pussy for me to know the answer to that question."
            call check_condom_usage (cherie) from _call_check_condom_usage_162
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show cherie standing condom
            show cherie standing
            with fade
            "Forced to stoop a little in order to be able to aim my cock between Cherie's thighs, I make to get things started."
            "But as soon as I do so, she seems to notice the trouble I'm having on account of the difference in our respective heights."
            "Without saying a word, Cherie raises one of her legs and plants her foot on my bedside table in an effort to help."
            "This means that she's suddenly spread wide open in front of me, the object of my desires laid bare to my eyes."
            "I have no idea if she means to do the same with the other leg, but even if she did, there's no time for it to happen."
            "Because I instantly step forwards, rising up from the stoop and closing the short distance between Cherie and me."
            "She turns her head, getting no more than the chance to see what's happening for a fraction of a second before I'm in place."
            "My hands take a firm hold of Cherie, ensuring that she's held at the perfect height for what I have in mind."
            "And then I feel the sensation of my rising cock as it slides into the tight space between her thighs."
            "Now the position that Cherie's gotten herself into really pays off, at least from my perspective."
            "Because the higher she goes, the better the angle that I have on her."
            show cherie standing at stepback(speed=0.1, h=10, v=5)
            "And if she falls back even a fraction of an inch, then she lowers herself onto me."
            "Not that escape seems to be something on Cherie's mind right now."
            "Instead she keeps sneaking a look back over her shoulder every few seconds."
            "The look in her eyes telling me that she's waiting for me to make my next move."
            "That comes when my hands reach out and grab her around the waist."
            "And I pull her backwards, down and straight onto my waiting cock below."
            "I'd been expecting to have to put in a good deal of work at this stage."
            "That Cherie would need to be coaxed and teased in order to open up to me."
            "But I must have underestimated just how turned-on she is right now."
            "Because almost as soon as the tip of my cock touches the lips of her pussy, it starts to happen."
            show cherie standing vaginal closed at stepback(speed=0.1, h=10, v=5)
            "There's no more than a second of resistance before they begin to part, letting it slip inside."
            "As soon as that happens, all of the playful resistance in Cherie seems to melt away."
            "And instead I feel her weight gently settling against me as I fill her up."
            show cherie standing happy
            cherie.say "Oh..."
            cherie.say "Oh, mon ami…"
            cherie.say "You are so very...very big!"
            show cherie standing closed
            "Somehow the sound of Cherie's sophisticated accent makes her words seem poetic."
            "Another girl saying that might have sounded like she was just trying to win me over."
            "But coming from Cherie, it makes me all the more determined to wow her even more."
            show cherie standing at stepback(speed=0.1, h=10, v=5)
            "Using my arms to steer her and my core to support her weight, I begin to move inside her."
            "Almost instantly, Cherie seems to adjust to the rhythm of my movements."
            "Instinctively knowing where and when to compliment them with her own."
            show cherie standing at stepback(speed=0.1, h=10, v=5)
            pause 0.25
            show cherie standing at stepback(speed=0.1, h=10, v=5)
            "This means that we're moving in what feels like perfect harmony."
            "The back and forth motion of our union pleasuring us both all the more."
















            "And that's the only thing on my mind, the singular need to take Cherie to the moon and back."
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            pause 0.15
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            "Eventually we're going at it do hard and fast that I start to worry about the décor."
            "That all of Cherie's weight might come down on the bedside table and smash it."
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            pause 0.15
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            "Or else she could actually end up clawing at the wallpaper and gouging the plaster beneath."
            "So that's why it comes as a genuine relief when I begin to feel myself reaching the end."
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            pause 0.15
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            "Knowing that I won't be able to go on much longer only serves to make me push harder."
            "To make the last few moments of this even more memorable for Cherie."



            "So I make one final effort, pushing myself and Cherie in turn, over the edge."
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            pause 0.15
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            call cum_reaction (cherie, 'vaginal', sexperience_min) from _call_cum_reaction_296
            if _return == "vaginal_condom":
                show cherie standing at stepback(speed=0.1, h=10, v=5)
                "One final push is all it takes for me to reach my climax."
                "And as I do so, I silently thank my past self for using a condom."
                show cherie standing pleasure with vpunch
                "Because it means that I can just let go and explode inside of Cherie."
                with vpunch
                "She seems to appreciate that foresight too, wriggling and writhing under me as she cums."





            elif _return == "vaginal_inside_pregnant":
                cherie.say "Don't...stop..."
                cherie.say "Remember...I am...pregnant!"
                "One final push is all it takes for me to reach my climax."
                "And as I do so, I silently thank Cherie for that timely reminder."
                $ cherie.love += 3
                show cherie standing cum pleasure with vpunch
                "Because it means that I can just let go and explode inside of her."
                with vpunch
                "She seems to appreciate that foresight too, pushing all of her weight against me as she cums."
            elif _return == "vaginal_inside_pill":
                cherie.say "Don't...stop..."
                cherie.say "Remember...I am...on the pill!"
                show cherie standing at stepback(speed=0.5, h=10, v=5)
                "One final push is all it takes for me to reach my climax."
                "And as I do so, I silently thank Cherie for that timely reminder."
                $ cherie.love += 2
                show cherie standing cum pleasure with hpunch
                "Because it means that I can just let go and explode inside of her."
                "She seems to appreciate that foresight too, pushing all of her weight against me as she cums."
            elif _return == "vaginal_inside_mad":
                cherie.say "Stop...pull out"
                cherie.say "Before it is...too late!"
                "I hear the words and they seem to make sense to me."
                "But the problem is that there's no time to act on them."
                $ cherie.impregnate()
                show cherie standing cum pleasure with hpunch
                "Cherie moans as I shoot my load deep inside of her."
                with hpunch
                "And then she hurriedly shuffles forwards, pulling herself off me."
                "Even though it's too late for that to be of any use."
                hide cherie
                show cherie naked upset at center, zoomAt(1.5, (640, 1040))
                with fade
                $ cherie.love -= 5
                "Then we end up just staring at each other as the reality of what just happened finally starts to sink in."
            elif _return == "vaginal_inside_happy":
                mike.say "Oh shit..."
                mike.say "I need to pull out!"
                "I make to do just that, beginning to pull myself backwards."
                "But the moment I do so, Cherie surprises me by moving in the same direction."
                "This means that I remain buried inside of her until it's too late."
                $ cherie.love += 5
                $ cherie.impregnate()
                show cherie standing cum pleasure with hpunch
                "A second later I lose it, shooting my load into Cherie."
                with vpunch
                "She almost purrs with pleasure as it happens, seeming to be delighted with what just happened."
                "But I'm left slack-jawed and speechless, unable to process what just happened."
            elif _return == "vaginal_outside":
                menu:
                    "Cum on her body":
                        "Somehow I manage to keep my mind clear enough to remember the need to pull out."
                        if CONDOM:
                            "With a quick movement, I remove the condom."
                        show cherie standing outside cum pleasure with hpunch
                        "And that's just what I do, mere moments before I lose it and shoot my load."
                        show cherie standing with hpunch
                        "But the act of pulling out doesn't seem to do anything to lessen Cherie's pleasure."
                        show cherie standing onsex with hpunch
                        "In fact it looks like that's what finally pushes her over the edge too."
                        "As she writhes and wriggles in front of me as I shower her buttocks a moment later."
                        $ cherie.love += 1
                    "Cum on her face" if cherie.sub >= 25:
                        "As quickly as I can, I make a sweeping gesture with my hands in front of Cherie's face."
                        "And she seems to understand what I mean by it, because she instantly lets me slide out of her."
                        if CONDOM:
                            "With a quick movement, I remove the condom."
                        hide cherie
                        show cherie bj heart
                        with hpunch
                        "All of this happens just in time, as almost the same moment my cock is free, I start to lose it."
                        show cherie bj closed cum with vpunch
                        "Cherie quickly turns around and sits up, then closes her eyes and staying perfectly still."
                        with vpunch
                        "Which means that she takes the whole thing square in the face, sticky white lines painting her cheeks and nose."
                        $ cherie.love += 1
                        $ cherie.sub += 1
                    "Cum in her mouth" if cherie.sub >= 50:
                        "As quickly as I can, I point downwards, trying to let Cherie know I want her to swallow."
                        "And she seems to understand what I mean by it, because she lets me slide out of her."
                        if CONDOM:
                            "With a quick movement, I remove the condom."
                        hide cherie
                        show cherie bj heart pleasure suck
                        with hpunch
                        "Then she turns around and quickly opens her mouth, letting my cock fill it to capacity."
                        show cherie bj cum with vpunch
                        "Prepared for what's going to happen next, she also doesn't miss a beat as I shoot my load."
                        show cherie bj closed with vpunch
                        "Instead she swallows down every last drop, not pausing once as she does so."
                        "Whereas I find myself gasping and for air as release finally comes."
                        $ cherie.love += 2
                        $ cherie.sub += 2
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "I make a point of taking a couple of steps forwards before really getting down to it."
            "A move that forces Cherie to keep shuffling ahead of me until she's almost up against the wall."
            "She reaches out with both hands, using them to keep herself from being pressed into it."
            "And at the same time she looks back over her shoulder, eyes filled with anticipation."
            "Obviously wondering with great interest what's going to happen next."
            "But all it takes is one brief glimpse of her perfect little ass for me to know the answer to that question."
            "Forced to stoop a little in order to be able to aim my cock between Cherie's thighs, I make to get things started."
            "But as soon as I do so, she seems to notice the trouble I'm having on account of the difference in our respective heights."
            "Without saying a word, Cherie raises one of her legs and plants her foot on my bedside table in an effort to help."
            "This means that she's suddenly spread wide open in front of me, the object of my desires laid bare to my eyes."
            "I have no idea if she means to do the same with the other leg, but even if she did, there's no time for it to happen."
            "Because I instantly step forwards, rising up from the stoop and closing the short distance between Cherie and me."
            "She turns her head, getting no more than the chance to see what's happening for a fraction of a second before I'm in place."
            "My hands take a firm hold of Cherie, ensuring that she's held at the perfect height for what I have in mind."
            "And then I feel the sensation of my rising cock as it slides into the tight space between her buttocks."
            "Now the position that Cherie's gotten herself into really pays off, at least from my perspective."
            "Because the higher she goes, the better the angle that I have on her."
            show cherie standing at stepback(speed=0.1, h=10, v=5)
            "And if she falls back even a fraction of an inch, then she lowers herself onto me."
            "Not that escape seems to be something on Cherie's mind right now."
            "Instead she keeps sneaking a look back over her shoulder every few seconds."
            "The look in her eyes telling me that she's waiting for me to make my next move."
            "That comes when my hands reach out and grab her around the waist."
            "And I pull her backwards, down and straight onto my waiting cock below."
            "I'd been expecting to have to put in a good deal of work at this stage."
            "That Cherie would need to be coaxed and teased in order to open up to me."
            "But I must have underestimated just how turned-on she is right now."
            "Because almost as soon as the tip of my cock touched the edge of her hole, it starts to happen."
            show cherie standing anal closed at stepback(speed=0.1, h=10, v=5)
            "There's no more than a second of resistance before her muscles start to relax, letting it slip inside."
            "As soon as that happens, all of the playful resistance in Cherie seems to melt away."
            "And instead I feel her weight gently settling against me as I fill her up."
            show cherie standing happy
            cherie.say "Oh..."
            cherie.say "Oh, mon ami…"
            cherie.say "You are so very...very big!"
            show cherie standing closed
            "Somehow the sound of Cherie's sophisticated accent makes her words seem poetic."
            "Another girl saying that might have sounded like she was just trying to win me over."
            "But coming from Cherie, it makes me all the more determined to wow her even more."
            show cherie standing at stepback(speed=0.1, h=10, v=5)
            "Using my arms to steer her and my core to support her weight, I begin to move inside her."
            "Almost instantly, Cherie seems to adjust to the rhythm of my movements."
            "Instinctively knowing where and when to compliment them with her own."
            show cherie standing at stepback(speed=0.1, h=10, v=5)
            pause 0.25
            show cherie standing at stepback(speed=0.1, h=10, v=5)
            "This means that we're moving in what feels like perfect harmony."
            "The back and forth motion of our union pleasuring us both all the more."
















            "And that's the only thing on my mind, the singular need to take Cherie to the moon and back."
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            pause 0.15
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            "Eventually we're going at it do hard and fast that I start to worry about the décor."
            "That all of Cherie's weight might come down on the bedside table and smash it."
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            pause 0.15
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            "Or else she could actually end up clawing at the wallpaper and gouging the plaster beneath."
            "So that's why it comes as a genuine relief when I begin to feel myself reaching the end."
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            pause 0.15
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            "Knowing that I won't be able to go on much longer only serves to make me push harder."
            "To make the last few moments of this even more memorable for Cherie."



            "So I make one final effort, pushing myself and Cherie in turn, over the edge."
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            pause 0.15
            show cherie standing at stepback(speed=0.05, h=10, v=5)
            call cum_reaction (cherie, 'anal', sexperience_min) from _call_cum_reaction_317
            if _return == "anal_inside":
                "One final push is all it takes for me to reach my climax."
                "And I make a point of holding onto those haunches even tighter, just to be sure."
                $ cherie.love += 2
                show cherie standing cum pleasure with hpunch
                "Which means that I can just let go and explode inside of Cherie."
                with hpunch
                "She seems to appreciate the effort too, pushing all of her weight against me as she cums."
            elif _return == "anal_outside":
                menu:
                    "Cum on her body":
                        "Somehow I manage to keep my mind clear enough to remember the need to pull out."
                        show cherie standing outside cum pleasure with hpunch
                        "And that's just what I do, mere moments before I lose it and shoot my load."
                        show cherie standing with hpunch
                        "But the act of pulling out doesn't seem to do anything to lessen Cherie's pleasure."
                        show cherie standing onsex with hpunch
                        "In fact it looks like that's what finally pushes her over the edge too."
                        "As she writhes and wriggles in front of me as I shower her buttocks a moment later."
                        $ cherie.love += 1
                    "Cum on her face" if cherie.sub >= 25:
                        "As quickly as I can, I make a sweeping gesture with my hands in front of Cherie's face."
                        "And she seems to understand what I mean by it, because she instantly lets me slide out of her."
                        hide cherie
                        show cherie bj heart
                        with hpunch
                        "All of this happens just in time, as almost the same moment my cock is free, I start to lose it."
                        show cherie bj closed cum with vpunch
                        "Cherie quickly turns around and sits up, then closes her eyes and staying perfectly still."
                        with vpunch
                        "Which means that she takes the whole thing square in the face, sticky white lines painting her cheeks and nose."
                        $ cherie.love += 1
                        $ cherie.sub += 1
                    "Cum in her mouth" if cherie.sub >= 50:
                        "As quickly as I can, I point downwards, trying to let Cherie know I want her to swallow."
                        "And she seems to understand what I mean by it, because she lets me slide out of her."
                        hide cherie
                        show cherie bj heart pleasure suck
                        with hpunch
                        "Then she turns around and quickly opens her mouth, letting my cock fill it to capacity."
                        show cherie bj cum with vpunch
                        "Prepared for what's going to happen next, she also doesn't miss a beat as I shoot my load."
                        show cherie bj closed with vpunch
                        "Instead she swallows down every last drop, not pausing once as she does so."
                        "Whereas I find myself gasping and for air as release finally comes."
                        $ cherie.love += 2
                        $ cherie.sub += 2
    return


label cherie_fuck_date_reverse(sexperience_min):
    hide cherie
    show cherie flirt naked at center, zoomAt(1.25, (640, 880))
    with fade
    "It's hard for me not to come over all poetic when I find myself in the company of Cherie."
    "Her accent and the refined mannerisms that she possesses are more than enough to do it."
    "But when you add into the mix the fact that she's currently naked..."
    "Well, she pretty much becomes a walking work of art to me."
    "And I can imagine her posing for a great master to paint a portrait or carve a statue."
    "But the fact is that I'm neither a painter nor a sculptor."
    "So I guess she's going to have to settle for me just straight up making love to her!"
    "Not that the prospect of that seems to be in any way a disappointment for Cherie."
    "As she takes a gentle hold of my hand, and begins to lead me the short distance to the bed."
    show cherie happy blush
    if cherie.sub >= 25:
        cherie.say "Will you come where I lead, mon ami…"
        cherie.say "And then show me what you have in mind to do to me?"
    elif cherie.sub <= -25:
        cherie.say "Come with me now, mon ami…"
        cherie.say "There are so many things that I want you to do for me!"
    else:
        cherie.say "Come over here with me, mon ami…"
        cherie.say "And together we can make our dreams a reality!"
    show cherie normal
    "As if the prospect of getting it on with Cherie wasn't enough to motivate me."
    "The sound of her voice seems almost to become like that of an enchanted siren."
    "And I don't know that I could resist the urge to do as she says, even if I wanted to."
    scene bg black
    show cherie reverse
    with vpunch
    "Letting her guide me to the bed, I lie down as she pushes me gently in that direction."
    "My head lands softly on the pillow, while my eyes remain looking upwards."
    "And that's because they're fixated on Cherie as she lowers herself onto the bed too."
    "Looking down at me with a smile on her face, Cherie begins to straddle my thighs."
    "But she does so with her back to me, gazing over her shoulder the whole time."
    mike.say "Whoa..."
    mike.say "I didn't know they had the reverse cowgirl where you're from, Cherie!"
    "Cherie chuckles and shakes her head at me."
    cherie.say "Oh, [hero.name]…"
    cherie.say "But of course we do."
    cherie.say "Only I believe that we call it something else entirely."
    cherie.say "Now then..."
    "Cherie's tone changes to become a little more serious than before."
    "And I feel her reach down, wrapping her fingers around my stiffening cock."
    cherie.say "What are we going to do with this?"
    cherie.say "Where is it going to go?"
    menu:
        "Fuck her pussy":
            "The sensation of Cherie's fine, dextrous fingers upon my cock is instantly intense and totally impossible to ignore."
            "In that moment she has all of my attention focussed on the question that she just posed."
            "But all the same, it doesn't take me long to be able to come up with an answer."
            mike.say "P...pussy..."
            mike.say "I want to put it...in the pussy!"
            "A slow, knowing smile spreads across Cherie's face."
            "And she nods her head in a similarly languid manner."
            cherie.say "Very well, mon ami..."
            cherie.say "Then that is where it will go."
            call check_condom_usage (cherie) from _call_check_condom_usage_163
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show cherie reverse condom
            show cherie reverse
            with fade
            "Almost as soon as we're even vaguely in the right position to get it on, Cherie makes her move."
            "I suspected that she was almost champing at the bit to get things going between us."
            "And now she proves me right by tightening her grip on the shaft of my cock."
            "At the same time I can also see that she's not laid her legs down to either side of me."
            "Instead she's using them to put herself almost into a squatting position as she straddles my thighs."
            "Cherie uses this to be able to lower herself slowly into place, closing the distance between my cock and her pussy."
            "All the time this is going on, I'm almost reduced to the status of a mere observer."
            "Because I'm keeping as still as possible, not wanting to screw up what she's doing."
            "And I'm also straining to see what's happening around the front as well."
            cherie.say "Be still, mon ami..."
            cherie.say "Because you are in good hands."
            "As Cherie speaks the words, she presses the head of my cock against the lips of her pussy."
            "And that's all it takes for me to simply fall back onto the bed, totally under her control."
            "Still almost crouching, she uses her legs to begin moving up and down."
            "The motion sliding the folds between the lips up and down the tip."
            "Again I'm made aware of just how aroused she already is, as things soon start to happen."
            "And it feels like every movement causes her to relax and open up to me just a little more."
            "Soon enough it's not just rubbing against her, it's literally sinking in."
            show cherie reverse vaginal closed
            "Cherie's lips part, almost like a flower opening at the touch of the light."
            "And inch by inch, the motion of her body and the effects of gravity take hold."
            "To me it feels like I've been holding my breath the entire time."
            "Like if I moved or spoke a word the spell would break and it would be over."
            "But once I can feel that I'm all the way inside, there's a natural change in the dynamic."
            "Neither of us says anything, or even makes a gesture with head or hand."
            "Cherie simply slows down without actually coming to a total stop."
            "And at the same time I reach up and place my hands on her haunches."
            show cherie reverse at startle(0.1,-15)
            "Then I start to move beneath her, slowly at first."
            "Pulling myself almost out of her, but not quite, and then pushing back inside."
            show cherie reverse at startle(0.8,-15)
            pause 0.2
            show cherie reverse at startle(0.7,-15)
            "By the second and third thrusts, I'm already beginning to pick up speed."
            "Feeling like I'm gaining momentum with each passing second that's impossible to resist."
            show cherie reverse pleasure at startle(0.7,-15)
            pause 0.2
            show cherie reverse at startle(0.7,-15)
            "For her part, Cherie seems to be more than happy to place herself in my hands."
            "I feel the movements that she's making begin to align with my own."
            show cherie reverse pleasure at startle(0.7,-15)
            pause 0.2
            show cherie reverse at startle(0.7,-15)
            "Soon I'm the one setting the pace, guiding her motions."
            "And believe me when I say that it feels beyond amazing."
            "Every moment that I'm inside Cherie, pleasure pulses through my body."
            show cherie reverse pleasure at startle(0.5,-10)
            pause 0.15
            show cherie reverse at startle(0.5,-10)
            "Urging me to go ever faster and harder in order to generate more of it."













            "And that's the only thing on my mind, the singular need to make us both experience more pleasure."
            show cherie reverse pleasure at startle(0.5,-10)
            pause 0.15
            show cherie reverse at startle(0.5,-10)
            "By now I can see that Cherie's hands are travelling all over her naked body."
            "They caress and gently squeeze the parts of her that I can't see from where I'm laid."
            "All of which makes me wish that I could feel what Cherie's fingers are touching right now."
            show cherie reverse pleasure at startle(0.5,-10)
            pause 0.15
            show cherie reverse at startle(0.5,-10)
            "It must be quite something too, as I can already feel her picking up speed as she strokes herself."
            "Where before she was letting me lead, now she reasserts herself with a vengeance."
            "And it's not long before I find myself struggling to keep up."
            show cherie reverse pleasure at startle(0.5,-10)
            pause 0.15
            show cherie reverse at startle(0.5,-10)
            "Cherie's going at a pace that I just don't have the stamina to sustain."
            "And I can already feel the end approaching, the inevitable climax rushing towards me."



            show cherie reverse pleasure at startle(0.5,-10)
            pause 0.15
            show cherie reverse at startle(0.5,-10)
            "So I make one final effort, pushing myself and Cherie in turn, over the edge."
            call cum_reaction (cherie, 'vaginal', sexperience_min) from _call_cum_reaction_297
            if _return == "vaginal_condom":
                show cherie reverse at startle(0.05, -10)
                "One final push is all it takes for me to reach my climax."
                "And as I do so, I silently thank my past self for using a condom."
                show cherie reverse pleasure with vpunch
                "Because it means that I can just let go and explode inside of Cherie."
                with vpunch
                "She seems to appreciate that foresight too, wriggling and writhing under me as she cums."





            elif _return == "vaginal_inside_pregnant":
                cherie.say "Don't...stop..."
                cherie.say "Remember...I am...pregnant!"
                "One final push is all it takes for me to reach my climax."
                "And as I do so, I silently thank Cherie for that timely reminder."
                $ cherie.love += 3
                show cherie reverse cum pleasure with vpunch
                "Because it means that I can just let go and explode inside of her."
                with vpunch
                "She seems to appreciate that foresight too, wriggling and writhing under me as she cums."
            elif _return == "vaginal_inside_pill":
                cherie.say "Don't...stop..."
                cherie.say "Remember...I am...on the pill!"
                show cherie reverse at startle(0.05, -10)
                "One final push is all it takes for me to reach my climax."
                "And as I do so, I silently thank Cherie for that timely reminder."
                $ cherie.love += 2
                show cherie reverse cum pleasure with vpunch
                "Because it means that I can just let go and explode inside of her."
                "She seems to appreciate that foresight too, wriggling and writhing under me as she cums."
            elif _return == "vaginal_inside_mad":
                cherie.say "Stop...pull out"
                cherie.say "Before it is...too late!"
                "I hear the words and they seem to make sense to me."
                "But the problem is that there's no time to act on them."
                $ cherie.impregnate()
                show cherie reverse cum pleasure with vpunch
                "Cherie moans as I shoot my load deep inside of her."
                with vpunch
                "And then she hurriedly shuffles forwards, pulling herself off me."
                "Even though it's too late for that to be of any use."
                hide cherie
                show cherie naked upset at center, zoomAt(1.5, (640, 1040))
                with fade
                $ cherie.love -= 5
                "Then we end up just staring at each other as the reality of what just happened finally starts to sink in."
            elif _return == "vaginal_inside_happy":
                mike.say "Oh shit..."
                mike.say "I need to pull out!"
                "I make to do just that, beginning to pull myself backwards."
                "But the moment I do so, Cherie surprises me by moving in the same direction."
                "This means that I remain buried inside of her until it's too late."
                $ cherie.love += 5
                $ cherie.impregnate()
                show cherie reverse cum pleasure with vpunch
                "A second later I lose it, shooting my load into Cherie."
                "She almost purrs with pleasure as it happens, seeming to be delighted with what just happened."
                "But I'm left slack-jawed and speechless, unable to process what just happened."
            elif _return == "vaginal_outside":
                menu:
                    "Cum on her body":
                        "Somehow I manage to keep my mind clear enough to remember the need to pull out."
                        if CONDOM:
                            "With a quick movement, I remove the condom."
                        show cherie reverse outside cum pleasure with vpunch
                        "And that's just what I do, mere moments before I lose it and shoot my load."
                        show cherie reverse with vpunch
                        "But the act of pulling out doesn't seem to do anything to lessen Cherie's pleasure."
                        show cherie reverse bodycum with vpunch
                        "In fact it looks like that's what finally pushes her over the edge too."
                        "As she writhes and wriggles in front of me as I shower her buttocks a moment later."
                        $ cherie.love += 1
                    "Cum on her face" if cherie.sub >= 25:
                        "As quickly as I can, I make a sweeping gesture with my hands in front of Cherie's face."
                        "And she seems to understand what I mean by it, because she instantly lets me slide out of her."
                        if CONDOM:
                            "With a quick movement, I remove the condom."
                        hide cherie
                        show cherie bj heart
                        with hpunch
                        "All of this happens just in time, as almost the same moment my cock is free, I start to lose it."
                        show cherie bj closed cum with vpunch
                        "Cherie quickly turns around and sits up, then closes her eyes and staying perfectly still."
                        with vpunch
                        "Which means that she takes the whole thing square in the face, sticky white lines painting her cheeks and nose."
                        $ cherie.love += 1
                        $ cherie.sub += 1
                    "Cum in her mouth" if cherie.sub >= 50:
                        "As quickly as I can, I point downwards, trying to let Cherie know I want her to swallow."
                        "And she seems to understand what I mean by it, because she lets me slide out of her."
                        if CONDOM:
                            "With a quick movement, I remove the condom."
                        hide cherie
                        show cherie bj heart pleasure suck
                        with hpunch
                        "Then she turns around and quickly opens her mouth, letting my cock fill it to capacity."
                        show cherie bj cum with vpunch
                        "Prepared for what's going to happen next, she also doesn't miss a beat as I shoot my load."
                        show cherie bj closed with vpunch
                        "Instead she swallows down every last drop, not pausing once as she does so."
                        "Whereas I find myself gasping and for air as release finally comes."
                        $ cherie.love += 2
                        $ cherie.sub += 2
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "The sensation of Cherie's fine, dextrous fingers upon my cock is instantly intense and totally impossible to ignore."
            "In that moment she has all of my attention focussed on the question that she just posed."
            "But all the same, it doesn't take me long to be able to come up with an answer."
            mike.say "A...ass..."
            mike.say "I want to put it...in the ass!"
            "A slow, knowing smile spreads across Cherie's face."
            "And she nods her head in a similarly languid manner."
            cherie.say "Very well, mon ami..."
            cherie.say "Then that is where it will go."
            "Almost as soon as we're even vaguely in the right position to get it on, Cherie makes her move."
            "I suspected that she was almost champing at the bit to get things going between us."
            "And now she proves me right by tightening her grip on the shaft of my cock."
            "At the same time I can also see that she's not laid her legs down to either side of me."
            "Instead she's using them to put herself almost into a squatting position as she straddles my thighs."
            "Cherie uses this to be able to lower herself slowly into place, closing the distance between my cock and her ass."
            "All the time this is going on, I'm almost reduced to the status of a mere observer."
            "Because I'm keeping as still as possible, not wanting to screw up what she's doing."
            "And I'm also straining to see what's happening around the front as well."
            cherie.say "Be still, mon ami..."
            cherie.say "Because you are in good hands."
            "As Cherie speaks the words, she presses the head of my cock between the cheeks of her ass."
            "And that's all it takes for me to simply fall back onto the bed, totally under her control."
            "Still almost crouching, she uses her legs to begin moving up and down."
            "The motion sliding the tip around the very edge of her hole."
            "Again I'm made aware of just how aroused she already is, as things soon start to happen."
            "And it feels like every movement causes her to relax and open up to me just a little more."
            "Soon enough it's not just rubbing against her, it's literally sinking in."
            show cherie reverse anal closed
            "Cherie's muscles relax, almost like a flower opening at the touch of the light."
            "And inch by inch, the motion of her body and the effects of gravity take hold."
            "To me it feels like I've been holding my breath the entire time."
            "Like if I moved or spoke a word the spell would break and it would be over."
            "But once I can feel that I'm all the way inside, there's a natural change in the dynamic."
            "Neither of us says anything, or even makes a gesture with head or hand."
            "Cherie simply slows down without actually coming to a total stop."
            "And at the same time I reach up and place my hands on her haunches."
            show cherie reverse at startle(0.1,-15)
            "Then I start to move beneath her, slowly at first."
            "Pulling myself almost out of her, but not quite, and then pushing back inside."
            show cherie reverse at startle(0.8,-15)
            pause 0.2
            show cherie reverse at startle(0.7,-15)
            "By the second and third thrusts, I'm already beginning to pick up speed."
            "Feeling like I'm gaining momentum with each passing second that's impossible to resist."
            show cherie reverse pleasure at startle(0.7,-15)
            pause 0.2
            show cherie reverse at startle(0.7,-15)
            "For her part, Cherie seems to be more than happy to place herself in my hands."
            "I feel the movements that she's making begin to align with my own."
            show cherie reverse pleasure at startle(0.7,-15)
            pause 0.2
            show cherie reverse at startle(0.7,-15)
            "Soon I'm the one setting the pace, guiding her motions."
            "And believe me when I say that it feels beyond amazing."
            "Every moment that I'm inside Cherie, pleasure pulses through my body."
            show cherie reverse pleasure at startle(0.5,-10)
            pause 0.15
            show cherie reverse at startle(0.5,-10)
            "Urging me to go ever faster and harder in order to generate more of it."













            "And that's the only thing on my mind, the singular need to make us both experience more pleasure."
            "By now I can see that Cherie's hands are travelling all over her naked body."
            "They caress and gently squeeze the parts of her that I can't see from where I'm laid."
            "All of which makes me wish that I could feel what Cherie's fingers are touching right now."
            show cherie reverse pleasure at startle(0.5,-10)
            pause 0.15
            show cherie reverse at startle(0.5,-10)
            "It must be quite something too, as I can already feel her picking up speed as she strokes herself."
            "Where before she was letting me lead, now she reasserts herself with a vengeance."
            "And it's not long before I find myself struggling to keep up."
            show cherie reverse pleasure at startle(0.5,-10)
            pause 0.15
            show cherie reverse at startle(0.5,-10)
            "Cherie's going at a pace that I just don't have the stamina to sustain."
            "And I can already feel the end approaching, the inevitable climax rushing towards me."



            "So I make one final effort, pushing myself and Cherie in turn, over the edge."
            call cum_reaction (cherie, 'anal', sexperience_min) from _call_cum_reaction_318
            if _return == "anal_inside":
                "One final push is all it takes for me to reach my climax."
                "And I make a point of holding onto those haunches even tighter, just to be sure."
                $ cherie.love += 2
                show cherie reverse cum pleasure with vpunch
                "Which means that I can just let go and explode inside of Cherie's ass."
                with vpunch
                "She seems to appreciate the effort too, wriggling and writhing atop me as she cums."
            elif _return == "anal_outside":
                menu:
                    "Cum on her body":
                        "Somehow I manage to keep my mind clear enough to remember the need to pull out of her ass."
                        show cherie reverse outside cum pleasure with vpunch
                        "And that's just what I do, mere moments before I lose it and shoot my load."
                        show cherie reverse with vpunch
                        "But the act of pulling out doesn't seem to do anything to lessen Cherie's pleasure."
                        show cherie reverse bodycum with vpunch
                        "In fact it looks like that's what finally pushes her over the edge too."
                        "As she writhes and wriggles in front of me as I shower her buttocks a moment later."
                        $ cherie.love += 1
                    "Cum on her face" if cherie.sub >= 25:
                        "As quickly as I can, I make a sweeping gesture with my hands in front of Cherie's face."
                        "And she seems to understand what I mean by it, because she instantly lets me slide out of her ass."
                        hide cherie
                        show cherie bj heart
                        with hpunch
                        "All of this happens just in time, as almost the same moment my cock is free, I start to lose it."
                        show cherie bj closed cum with vpunch
                        "Cherie quickly turns around and sits up, then closes her eyes and staying perfectly still."
                        with vpunch
                        "Which means that she takes the whole thing square in the face, sticky white lines painting her cheeks and nose."
                        $ cherie.love += 1
                        $ cherie.sub += 1
                    "Cum in her mouth" if cherie.sub >= 50:
                        "As quickly as I can, I point downwards, trying to let Cherie know I want her to swallow."
                        "And she seems to understand what I mean by it, because she lets me slide out of her ass."
                        hide cherie
                        show cherie bj heart pleasure suck
                        with hpunch
                        "Then she turns around and quickly opens her mouth, letting my cock fill it to capacity."
                        show cherie bj cum with vpunch
                        "Prepared for what's going to happen next, she also doesn't miss a beat as I shoot my load."
                        show cherie bj closed with vpunch
                        "Instead she swallows down every last drop, not pausing once as she does so."
                        "Whereas I find myself gasping and for air as release finally comes."
                        $ cherie.love += 2
                        $ cherie.sub += 2
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
