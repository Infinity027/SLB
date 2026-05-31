init python:
    Event(**{
    "name": "master_hottub_sex_female",
    "label": "master_hottub_sex_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(master,
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

label master_hottub_sex_female:
    $ CONDOM = False
    scene bg pool
    if game.calendar.get_time_of_day() == "evening":
        $ renpy.show(f"hottub_bg_night_left")
    else:
        $ renpy.show(f"hottub_bg_{game.calendar.season_name}_left")
    $ renpy.show("hottub_fg_valentine_left", tag="romantic")
    with fade
    "I've been fussing over getting the hot-tub ready for tonight for what feels like forever."
    "And now that I'm done, I can finally take a step back and admire all that I've achieved."
    "But the moment I do that, I can already feel the doubt setting in."
    "I've lowered the lights around the tub so that it's extra atmospheric."
    "I've dotted candles here and there to add to the effect too."
    "There's a really nice bottle of wine to hand with two glasses."
    "Hell, I've even gone to the trouble of scattering rose petals all over the place!"
    "But the problem is that the guy I've invited over..."
    "Well, let's just say that he isn't your average guy!"
    "It's my martial arts teacher, or the Master, as I tend to call him."
    "And now I'm starting to wonder if I should have gone in a totally different direction."
    "You know, like incense and music that you can meditate to?"
    "Someone like that is so spiritual and focussed on the world beyond the physical."
    "He's sure to be more interested in the chance to focus his energies in a hot-tub."
    "Far more so than getting intimate and swigging wine!"
    master.say "Ho, ho, ho!"
    master.say "This is all very nice, my dear."
    master.say "Very nice indeed!"
    "The sound of the Master's voice snaps me straight back to reality."
    "It also reminds me that he's not your typical kind of martial artist either."
    "So what in the hell was I worried about?"
    scene bg pool
    show master casual
    with fade
    "I turn and offer the old man a smile."
    "And then I gesture to the hot-tub."
    bree.say "Hello, Master..."
    bree.say "I take it that you approve?"
    bree.say "That all of this isn't too frivolous and distracting?"
    "I can see what his answer's going to be."
    show master happy
    "The huge grin on his face kind of gives it away."
    master.say "Oh no, my dear..."
    master.say "A true practitioner of the martial arts is not so easily distracted."
    master.say "He is able to extract benefits from the most decadent of pursuits!"
    master.say "And is that a bottle of wine I see over there?"
    show master normal
    "I take the extremely unsubtle hint and retrieve the bottle."
    "Then I pour us both a generous glass and had his to him."
    play sound woosh_punch
    show master at center, traveling(1.5, 0.2, (640, 1040))
    "The Master takes it from me eagerly and raises it to his lips."
    "I watch in surprise as he instantly drains almost half of it."
    "And then he lets out a deep sigh of satisfaction."
    master.say "Ah!"
    show master noglasses
    master.say "Now that's more like it!"
    show master naked with dissolve
    "Without asking for permission, he unbuttons his shirt."
    "And then he kicks off his shoes, before jumping into the tub."
    play sound water_splash
    hide master
    $ game.active_date.clothes = "swimsuit"
    show hottub master valentine nomc
    with fade
    "I guess the loud pair of shorts he has on are swimming trunks."
    "The old man leans back in the water, his arms on the sides of the tub."
    master.say "Well?"
    master.say "What are you waiting for?"
    master.say "I'm not going to be sitting in here alone all night, am I?"
    "His comment makes me jump to it and hurry over to the tub."
    play sound water_splash
    pause 0.1
    show hottub master valentine -nomc with vpunch
    "Part of me knows that it shouldn't have that kind of effect."
    "But I have been taking lessons from him for a little while now."
    "And I guess the habit of doing as he says is hard to break."
    bree.say "I have to say, Master..."
    bree.say "I was worried that you'd disapprove of this."
    bree.say "But you seem to be really enjoying yourself!"
    "The old man nods and smiles."
    master.say "The warmth is good for relaxing the muscles."
    master.say "The motion of the water helps to massage my joints, keeping them supple."
    master.say "And the bubbles..."
    master.say "Well, the bubbles are just delightful in their own right!"
    "I nod at everything he's saying, sipping my wine at the same time."
    "And I think I must be drinking it faster than I realised."
    "Because I can already feel it going to my head!"
    bree.say "Oh dear..."
    bree.say "I think I need to slow down a little!"
    "At this, the Master narrows his eyes."
    "And he looks at me with a keen interest."
    master.say "Hmm..."
    master.say "I would suggest the opposite, my dear."
    master.say "Speeding up your metabolism is the answer here."
    master.say "That would allow you to process the alcohol much more quickly."
    "Part of me is a little suspicious when he starts talking like this."
    "And it's telling me that I need to be more than a little wary."
    "But unfortunately, the larger part of me is pretty tipsy by now."
    "And it's eating up everything the old man is saying."
    bree.say "Really, Master?"
    bree.say "How do I even do that?"
    "As I fall for his pitch, the Master can't help chuckling with glee."
    "He also hurries to put down his glass and beckon me closer to him."
    master.say "He, he, he..."
    master.say "Come over here, my dear."
    master.say "Come over here and I'll show you!"
    "I can feel myself starting to grin as I follow his instructions."
    "And that's because he can't keep himself from starting to pull down his shorts."
    "So by the time I reach him on the other side of the tub, he's already naked!"
    "I shake my head and roll my eyes as he gestures for me to come closer still."
    bree.say "Oh, Master..."
    bree.say "I think I know where this is going!"
    "He doesn't bother to answer this time."
    "Either because he's confident of getting what he wants."
    "Or else he's too wrapped up in thinking about it to hear me."
    "Either way I decide that I'm just going to humour him."
    "After all, I did invite him over for a romantic dip in the tub."
    "And that body of his is in such good condition for a man of his age too."
    "So I guess I'll be putting his claims to the test."
    "I can already see his manhood rising out of the water."
    "And I don't hesitate to take hold of it as I reach him."
    "The Master lets out a yelp of surprise as I grab it firmly."
    "And his eyes bulge as I use the other hand to pull off my swimsuit."
    "But then he recovers his air of command, and nods at me."
    master.say "Very good, very good!"
    master.say "You seem to be able to read my mind."
    master.say "So I believe you know what you must do next?"
    bree.say "Maybe this, Master?"
    show hottub sex female master naked with fade
    "Lowering myself down and onto him, I straddle the old man's thighs."
    "Still holding onto his cock, I aim it between my own as I do this."
    "And it does seem like I know what he wants, as he nods eagerly."
    master.say "Yes, yes!"
    master.say "Just like that!"
    "I keep on nodding, making it look like I'm following his instructions to the letter."
    "But the reality is that I'm already tuning him out, letting his voice fade into the background."
    "And that's because I can feel myself taking control, asserting myself."
    "Maybe his teachings are paying off."
    "Maybe I'm finally becoming able to control my body to a ridiculous degree."
    "Because the moment I begin to urge my pussy to part and let him it, it starts to happen!"
    "It could be sheer coincidence, my head and heart being on the same page."
    "But in the moment, it really does feel like more than that."
    "As I feel myself sinking down onto him, I swear that I'm one hundred percent in control."
    "I can see that he's still talking, nodding and offering instruction."
    "Yet now his words mean nothing to me, as though I don't need them at all."
    "Is this how it feels to surpass your teacher?"
    "Or am I just a little drunk and high on the sensations of sex?"
    "There's no time to contemplate the philosophical aspects of my situation."
    "As now I'm brought back down to earth by the sensation of the Master grabbing my ass!"
    "In my state of bliss I'd almost forgotten he was involved."
    "But now I remember that the cock inside of me is actually attached to him."
    "He seems to be doing all he can to add to my state of bliss."
    "His steely muscles are tensed and his skinny limbs working very hard."
    "Thankfully he's more than up to the task at hand."
    "Which is why I feel confident to lean more of my weight onto him."
    show hottub sex female master naked at startle(0.05,-10)
    "I'm pushing down as he's thrusting up, so that we meet in the middle."
    "And that's the point where the magic happens."
    "Where we come together, there's nothing but pure pleasure."
    "The old man's head is moving the whole time."
    "I can't tell if he's nodding or swaying from delirium."
    "But when I see blood spurting from his nose, I realise something must be wrong."
    master.say "Urgh..."
    show hottub sex female master naked at startle(0.05,-10)
    master.say "Oh my..."
    show hottub sex female master naked at startle(0.05,-10)
    master.say "Oh my goodness!"
    bree.say "What is it, Master?"
    bree.say "What's wrong?"
    show hottub sex female master naked at startle(0.05,-10)
    bree.say "Oh..."
    show hottub sex female master naked at startle(0.05,-10)
    bree.say "Oh goodness!"
    show hottub sex female master naked at startle(0.05,-10)
    "What's wrong with the Master is that he can't hold on any longer."
    $ master.impregnate()
    with vpunch
    "And a moment later, I feel him lose it inside of me."
    "His hands tighten their grip on my buttocks, fingers digging into the soft flesh."
    with vpunch
    "And I cling to him more tightly than ever too, threatening to push him under the water."
    with vpunch
    "Now we're both cumming, splashing around desperately in the water."
    "But afterwards I can't say that the Master's remedy has worked."
    "Because if anything, I feel dizzier than I did before we started!"
    "The Master, on the other hand, seems to be perfectly fine."
    "Lying back against the edge of the tub, a blissful smile on his face."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ master.sexperience += 1
    $ game.active_date.clothes = None
    scene bg black with dissolve
    return


label master_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom4
        show master naked
        with fade
        menu:
            "You should leave":
                bree.say "I am done with you and I have to get up early tomorrow, you should leave."
                "The sex was beyond incredible."
                "Frowning a little, Master straightens and shrugs, then goes to collect his clothes from where he'd let it fall earlier."
                "He then heads up the stairs."
                $ master.love -= 1
                $ master.sub += 1
                call sleep from _call_sleep_111
            "You should sleep here":
                bree.say "You can stay and sleep here."
                "I say, my voice a little shaky."
                "We curl up spooning together in bed, drifting toward sleep."
                $ master.love += 1
                call sleep ("master") from _call_sleep_112
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
