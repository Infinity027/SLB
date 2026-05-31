init python:
    Event(**{
    "name": "victor_hottub_sex_female",
    "label": "victor_hottub_sex_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(victor,
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

label victor_hottub_sex_female:
    scene bg pool
    $ renpy.show(f"hottub_bg_{'night' if game.calendar.get_time_of_day() in ['evening', 'night'] else game.calendar.season_name}_left")
    $ renpy.show("hottub_fg_valentine_left", tag="romantic")
    with fade
    "I've been bugging Victor to come over and take a dip in the hot-tub for ages."
    "But he always seems to come up with some excuse or other to make sure it doesn't happen."
    "Which is annoying on so many levels, because it shows how little I know about him."
    "That and the fact he's got so much stuff going on in his life that's a mystery to me."


    "I've got the whole place ready for him too."
    "Subdued lighting, wine for two, scented candles, even rose petals scattered around for good measure!"
    "Throw in the feminine charms of your's truly, and how could he ever hope to resist?"
    victor.say "Uh, [hero.name]..."
    victor.say "Are you back here?"
    "At the sound of Victor's voice, I turn around to meet him."
    "I'm already wearing my sexiest swimsuit and what I hope is a seductive smile."



    scene bg pool
    show victor casual surprised
    with fade
    "Victor flinches a little and takes a reflexive step backwards as he sees me."
    "I see his hand reach into his jacket, like he's going to whip something out."
    "But then he seems to realise it's just me, and he runs the hand through his hair instead."


    show victor annoyed
    victor.say "Sorry, I'm a little jumpy right now."
    victor.say "Work was like...murder today!"
    "I nod as I hurry over to meet Victor."
    show victor normal
    "He sure looks more than a little stressed."
    "So I feel the need to do what I can to help him wind down."
    bree.say "Well you can forget all about work for a while, Victor."
    bree.say "Tonight's just about chilling out and relaxing in the tub!"
    "Picking up the bottle of wine, I open it."
    "And then I proceed to pour us a couple of glasses."
    show victor annoyed
    "Victor takes the glass I offer him while he looks around."
    "Sure, he was scanning the place just now when he called for me."
    "But this time it's like he's actually noticing my efforts for the first time."
    show victor blush
    victor.say "Oh wow, [hero.name]..."
    victor.say "You really went to some serious trouble for me!"
    victor.say "This place looks real nice."
    show victor -blush shy
    victor.say "And you too..."
    victor.say "You look especially nice!"
    show victor normal blush
    "I can already feel myself blushing at the compliment."
    "I mean, what girl wouldn't with it coming from a guy as hot as Victor?"
    bree.say "Well..."
    bree.say "You want to take a dip in the tub?"
    bree.say "It's not getting any hotter!"
    bree.say "Or maybe it will when you get in it!"
    show victor normal -blush
    "I feel like kicking myself as soon as the corny line comes out of my mouth."
    "Victor raises an eyebrow, as if he's surprised to hear me talk like that."
    "But if he doesn't like the sound of it, he keeps that fact to himself."
    victor.say "Uh..."
    victor.say "Okay, [hero.name], okay..."
    victor.say "You got somewhere I can change?"
    hide victor with easeoutleft
    "I hurry to show Victor where he can change without being seen."
    "And then I hurry to the side of the pool, waiting for his return."
    "I'm still feeling ashamed of my terrible line earlier when he emerges."
    $ game.active_date.clothes = "swimsuit"
    show victor swimsuit at left with easeinleft
    "But the moment I see him, I forget all about it."
    victor.say "Ah, [hero.name]..."
    show victor shy at center with ease
    victor.say "Why are you looking at me like that?"
    bree.say "I..."
    bree.say "Whoa..."
    show victor surprised blush
    bree.say "Come to momma!"
    "I don't know if I've ever seen a guy with a body like Victor's."
    "Must be like zero percent body fat, and the rest of him sinewy muscle!"
    "Plus there are genuine scars on him too, like he's been in a literal war!"
    show victor normal blush
    victor.say "What was that?"
    victor.say "[hero.name], are you okay?"
    bree.say "Oh..."
    bree.say "Oh yeah, Victor, I'm fine."
    bree.say "I think the wine must have gone to my head!"
    show victor normal -blush
    "Victor nods as he walks over to me."
    "Which means I get to see that super hot bod in action."
    "And by the time he reaches me, I feel like I'm melting!"
    victor.say "So..."
    victor.say "Shall we?"
    show hottub victor valentine with fade
    "Victor gestures to the tub and I hurry to climb into the water."
    "He follows close on my heels, but as he gets in, I see him wince."
    victor.say "Agh..."
    bree.say "Are you okay, Victor?"
    victor.say "Yeah, I'm fine."
    victor.say "I just got a little banged up at work today."
    victor.say "It's nothing that won't work itself out."
    bree.say "I could take a look at it if you like?"
    bree.say "I give a pretty good massage!"
    "Okay, okay - my massages are basic at the best of times."
    "But you think I'm going to pass up the chance to get my hands on Victor?"
    victor.say "Huh..."
    victor.say "I guess it couldn't hurt."
    victor.say "It's kinda around my shoulders and back, yeah?"
    bree.say "Don't worry, Victor."
    bree.say "Just leave everything to me!"
    "Victor nods and he turns his back to me and leans on the edge of the tub."
    "He spreads his arms out on the decking and lays his head between them."
    "I glide over to his side of the tub, trying to contain my excitement."
    "Yeah, we're in the hot-tub together, wearing nothing but our swimsuits."
    "And yeah, this is probably going to go the way I hope it is in the end."
    "But I still have to make an effort to actually give Victor that massage."
    "And I want it to be a pretty good one too!"
    "So I reach out my hands and begin in earnest."
    "The first thing that I notice is that his muscles are like coiled steel!"
    "I don't know what kind of workout he does, but it's definitely working."
    "Normally I'd stroke and rub, but here I have to go in with my thumbs, and hard too."
    "But even as I start battling with the knots I find, Victor lets out a sigh of release."
    victor.say "That's the spot, [hero.name]..."
    victor.say "Right there!"
    victor.say "Whatever you're doing, don't stop - do it harder!"
    "I nod, even though I know Victor can't see me doing it."
    "And I redouble my efforts."
    "Little by little I feel the knots loosening."
    "And he sighs with relief as I ease his pain."
    "Once I'm done, I sink down beside Victor."
    victor.say "That feels great, [hero.name]."
    victor.say "I think you even eased some really old aches and pains too!"
    victor.say "Is there anything I can do to pay you back?"
    "I make a point of looking thoughtful for a moment."
    "Then I lean in really close to Victor."
    bree.say "Maybe there is..."
    hide hottub
    hide victor
    $ renpy.show(f"hottub_bg_{'night' if game.calendar.get_time_of_day() in ['evening', 'night'] else game.calendar.season_name}_left")
    $ renpy.show("hottub_fg_valentine_left", tag="romantic")
    show victor kiss swimsuit
    with dissolve
    $ victor.flags.kiss += 1
    "He doesn't resist as I kiss him on the lips."
    "In fact he rises to it, kissing me back with a passion."
    "I feel his arms wrap around me, a sensation that thrills me."
    "And now those sinewy muscles are pressed against my own body."
    "I don't resist for a moment as Victor slides around behind me."
    "Likewise I let him guide me down onto my knees ."
    "And then I wait for the sensation of him pulling side my swimsuit."
    show hottub sex female victor valentine with fade
    "I have to bite my lip as I feel his manhood between my thighs."
    "He's gentle and yet determined at the same time."
    "The natural resistance of my body heightening the anticipation."
    "The head of his cock slides against my lips."
    "And I can't help gasping as the inevitable happens."
    "Victor sinks into me as my lips part, going slow and straight."
    "He doesn't stop until he's as far inside as he can possibly go."
    "But once he is, the real experience can finally begin for me."
    "Victor starts slow, but picks up speed without me noticing."
    "I can feel the quality of his lithe muscles in the way that he makes love."
    "It's intense, deep and totally moving."
    "I feel like I'm completely in Victor's hands right now."
    "Like he's the one in charge of where this is going."
    "And I'm totally fine with that, happy to go where he leads."
    "Victor's hands hold me in place as he thrusts in and out."
    "The way he's totally losing himself to the task fascinates me."
    "It's like he's zoned out completely, cut himself off from the world."
    "That kind of single-minded dedication is really rare."
    "Like he's focused on one thing alone, and nothing can distract him."
    "I also like to think that I can feel some of his stress and angst leaving him."
    "That what we're doing is helping to bleed it off and lighten his load."
    "Because I know that it's making me feel amazing."
    "And keeping him inside of me for as long as possible is all I can think about!"
    victor.say "Unh..."
    with hpunch
    victor.say "Oh, [hero.name]..."
    victor.say "Oh man!"
    with hpunch
    "Victor cums without warning, shooting his load into me a moment later."
    "I feel his thrusts sending my own body into a helpless spasm too."
    $ victor.impregnate()
    with hpunch
    "Before I know it, I'm cumming at the same time."
    "And I'm holding onto the edge of the pool like my life depends on it!"
    "Afterwards we both lie back in the water, utterly spent."
    "And I can't help thinking that I don't know much more about Victor than I did before."
    "Save, of course, for what makes him tick when it comes to having fun of an intimate kind!"
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ victor.sexperience += 1
    $ game.active_date.clothes = None
    scene bg black with dissolve
    return


label victor_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom4
        show victor naked
        with fade
        menu:
            "You should leave":
                bree.say "I am done with you and I have to get up early tomorrow, you should leave."
                "The sex was beyond incredible."
                "Frowning a little, Victor straightens and shrugs, then goes to collect his clothes from where he'd let it fall earlier."
                "He then heads up the stairs."
                $ victor.love -= 1
                $ victor.sub += 1
                call sleep from _call_sleep_117
            "You should sleep here":
                bree.say "You can stay and sleep here."
                "I say, my voice a little shaky."
                "We curl up spooning together in bed, drifting toward sleep."
                $ victor.love += 1
                call sleep ("victor") from _call_sleep_118
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
