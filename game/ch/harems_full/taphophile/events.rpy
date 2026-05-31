init python:
    Event(**{
    "name": "cemetery_threesome",
    "label": "cemetery_threesome",
    "conditions": [
        IsDone("ayesha_event_03b"),
        GameTarget(IsFlag("waitCemetery3some", False)),
        HeroTarget(
            IsGender("male"),
            IsRoom("cemetery"),
            HasStamina(),
            ),
        ],
    "music": "music/roa_music/2am.ogg",
    "do_once": True,
    "quit": False,
    }
    )

label cemetery_threesome:
    scene bg cemetery with fade
    "I'm in a hurry to get where I'm going, already worried that I'm not going to make it on time."
    "Which is why I make the decision to take a short-cut that I know is just up ahead."
    "The only problem is that it takes me somewhere that I'm not keen on exploring in the dark."
    "And that's a cemetery which always has its gates open no matter the hour of day or night."
    "Now let's just get something straight here - I'm not scared of anything supernatural, okay?"
    "What I find far more terrifying is the prospect of getting mugged or assaulted in there."
    "It's not well lit and the place is full of gravestones and tombs, all great to hide behind."
    "Even as I walk through the gates it's flesh and blood human beings that I'm afraid of meeting."
    "Not ghouls and ghosts popping up from open graves!"
    "With all that in mind, I quicken my pace until I'm almost but not quite running."
    "That way I should make it through the cemetery pretty quickly and be on my way."
    "I make it most of the way without incident."
    "All I see are shadows and all I hear is the sound of the wind in the trees."
    "But just as I'm starting to think that I was wrong to be worried, everything changes."
    "I can see and hear something that makes may hair stand on end."
    "A little way off the main path through the cemetery is a small rise."
    "Atop it there's a bunch of pretty elaborate tombs, complete with crosses and statues."
    "I swear that I can see something white moving amongst them."
    "And I hear what sounds like ghostly voices too!"
    violaine.say "Oh yes..."
    violaine.say "Oh yes, Lord of the night!"
    "Vincent" "Do I amaze you?"
    "My first thought is to just take to my heels and run."
    "It's not far to the other side of the cemetery from here."
    "And I'm sure that I could reach it before whoever's up there could catch up to me."
    "But there's something oddly familiar about the voices that I can hear too."
    "It's almost like I've heard them before, but I just can't place them from down here."
    "I'm probably going to regret this decision, sooner rather than later."
    "But something makes me turn and begin to walk up the rise."
    "The closer I get to the source of the voices, the clearer they become."
    "At first I think it must be some sort of chanting, even a ritual."
    "Then I get a better look at the owners of the voices."
    show violaine vincent 3some with fade
    "I see two pale bodies on top of a flat tomb, one atop the other."
    "They look almost radiant in the moonlight, white as snow."
    "Suddenly my foot lands on something that makes a sound."
    "The heads turn around to regard me, and I see two pale visages."
    "Those faces look like something straight out of a horror film!"
    "I almost let out a cry of alarm, but they beat me to it."
    "Though I am surprised when they smile and nod at me!"
    violaine.say "Oh..."
    violaine.say "[hero.name], it's you!"
    "Vincent" "Greetings, friend!"
    "Vincent" "Fancy seeing you here!"
    "I can't help breathing a sigh of relief as I recognise Violaine and Vincent."
    "It's not a pair of cadaverous ghouls, just a couple of goths that I happen to know!"
    "But that still doesn't explain what they're doing out here in the cemetery."
    "Though now I'm up close, the situation is starting to make more sense."
    "I mean, they're naked in a compromising position on top of a tomb."
    "What's the most likely explanation?"
    mike.say "Erm..."
    mike.say "Hey guys..."
    mike.say "I was just cutting through here as a short-cut."
    mike.say "I heard a noise and came to investigate."
    mike.say "I didn't mean to disturb you!"
    "Most people would be annoyed and offended if you caught them having sex in a public place."
    "But Violaine and Vincent seem to take it in their stride, all nods and smiles."
    violaine.say "Don't worry about it, [hero.name]."
    violaine.say "At least you said sorry."
    violaine.say "Most people are less understanding, you know?"
    "Vincent" "They're SO closed-minded!"
    "Vincent" "Very disappointing when that happens."
    "I'm really not sure how to handle the situation that I've found myself in."
    "But as Violaine and Vincent seem cool with it, I just follow their example."
    mike.say "So..."
    mike.say "Are you out here for some magical ritual or something?"
    mike.say "Making love on the grave of an infamous witch or wizard?"
    mike.say "Using sexual energy to summon a demon perhaps?"
    violaine.say "Oh no, [hero.name]!"
    violaine.say "Our neighbours are having work done on their house."
    "Vincent" "Yes, we came out here to get some peace and quiet."
    "Vincent" "The noise was driving me out of my tiny little mind!"
    violaine.say "We just chose this grave because it's the most comfortable."
    "Vincent" "I think it belongs to somebody that sold used cars for a living!"
    "I chuckle and shake my head."
    mike.say "Well..."
    mike.say "I really should get going, you know?"
    mike.say "Sorry to interrupt you!"
    "Violaine and Vincent exchange a meaningful glance at this."
    "Neither of them says a word at first."
    "But I get the feeling an idea just passed between them."
    violaine.say "No need to hurry off, [hero.name]."
    violaine.say "In fact, why don't you join us?"
    "Vincent" "Yes, plenty of room up here."
    "Vincent" "We could make the beast with THREE backs!"
    menu:
        "Accept":
            "Suddenly the need to get to where I was going doesn't seem so urgent."
            "Instead I find myself staring intently at the shape of Violaine's naked body."
            "Sure, she's so pale that she looks anaemic, but she'd undeniably hot as well."
            "And from the look in her striking blue eyes, she's deadly serious too!"
            "I turn my gaze towards Vincent, and he nods to let me know he's not kidding."
            "Maybe I'm not as crazy about getting naked with him."
            "But he's not moving from underneath Violaine."
            "So at least I won't have to look him in the face!"
            mike.say "Okay, if you guys insist!"
            mike.say "There are some things worth being late for!"
            "Violaine and Vincent nod and share a dry chuckle at this."
            "At the same time I'm already stripping off beside them."
            violaine.say "Hurry up and climb on, [hero.name]."
            violaine.say "Vincent is already in the front entrance to my batcave."
            violaine.say "So you'll have to use the back-door!"
            show violaine vincent 3some mike
            if renpy.has_label("violaine_achievement_1") and not game.flags.cheat:
                call violaine_achievement_1 from _call_violaine_achievement_1
            "I nod eagerly, clambering onto the tomb and then onto Violaine in turn."
            "She nods too as I take hold of her and part her buttocks."
            "My cock's hard and so I waste no time in pushing it forwards."
            show violaine vincent 3some pleasure inside
            "Violaine moans at the sensation of it pushing into her ass."
            "She looks back over her shoulder, biting her blood-red lip."
            "And I hold her eye as I sink slowly into her."
            "Vincent" "Sir, Madam..."
            "Vincent" "Shall we proceed?"
            "He begins to thrust up from below as he says this."
            "And a moment later I do the same from above."
            "Instinctively we time our movements so that they don't clash."
            "This means that pretty soon Violaine is riding two cocks at once."
            "As one pushes into her, the other is pulling out."
            "The effect is pretty impressive to watch."
            "She goes up and down, her movements dictated by our own."
            "And all the time she's feeling ever more pleasure too!"
            violaine.say "Oh yes..."
            violaine.say "Give it to me..."
            violaine.say "Violate my mortal flesh!"
            violaine.say "Carry me to hell on a wave of exquisite pleasure!"
            "When she's not uttering florid lines, Violaine moans with delight."
            "She caresses her own body with both hands, tracing every line and curve."
            "Then she begins to squeeze at her own breasts with what looks like desperation."
            "Like she's trying to release some of the pressure that's building inside of her."
            "All three of us are getting to that point."
            "We're moving together and pushing each other on to greater heights."
            "Any worry that I might have had about doing it here is long gone."
            "Now all I can think about is thrusting into Violaine."
            "All I want is to hear the sound of her cumming."
            show violaine vincent 3some ahegao
            "To feel the muscles of her ass squeezing my cock as it happens."
            violaine.say "The time has come!"
            violaine.say "My tumult is fast approaching!"
            violaine.say "Behold, it is upon me!"
            with hpunch
            "I feel myself losing it as Violaine cums beneath me."
            show violaine vincent 3some cum vincentcum with hpunch
            "I let out an almost bestial groan as I shoot my load into her."
            with hpunch
            "Vincent" "Oh wow..."
            "Vincent" "Do I amaze you?"
            "All three of us peak pretty much at once."
            show violaine vincent 3some pleasure
            "Bodies quiver and breath comes in ragged pants."
            "Once it's over, I climb gingerly off of Violaine and start to get dressed."
            "Violaine and Vincent do the same, but at a more leisurely pace."
            "Which is fine for them, as they don't have to be somewhere else like I do!"
            scene bg cemetery
            show vincent teaser at left5
            show violaine at right5
            with fade
            violaine.say "That was fun, [hero.name]."
            violaine.say "We'll have to do it again some time soon!"
            "Vincent" "You'd be more than welcome next time around."
            "Vincent" "We like to have sex in some very unusual places!"
            mike.say "Thanks, guys."
            mike.say "Maybe we can make that happen."
            "I wave to them as I hurry back down the rise."
            hide vincent teaser
            hide violaine
            with dissolve
            "This was fun, but part of me is reluctant to seem too enthusiastic for more."
            "Because I have no idea what other crazy places those guys like to fuck!"
            "And no matter how hard I try, my head is full of the possibilities for hours to come."
        "Refuse":
            "I can't help taking an instinctive step backwards at the offer."
            "In fact, I'm already shaking my head and turning to leave."
            mike.say "Ah..."
            mike.say "No, guys..."
            mike.say "That's a really kind offer, though."
            mike.say "And if I had the time, I'd be well up for it!"
            mike.say "But like I said, I have to be somewhere else right now."
            "Violaine and Vincent exchange a glance and a casual shrug of the shoulders."
            violaine.say "That's a shame."
            violaine.say "Maybe next time, okay?"
            "Vincent" "Indeed, we'll have to let you know."
            "Vincent" "Then you can make sure your diary's clear, yes?"
            "I nod and smile, already walking away."
            hide violaine vincent 3some with fade
            "And as I walk back down the rise the sounds resume behind me."
            "Though I make sure to hurry the rest of the way across the cemetery."
            "Because of all the scary things I could imagine seeing in a graveyard - that tops the list!"
    $ Room.find("cemetery").hide()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
