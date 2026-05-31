init 1:
    layeredimage bg forest:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"

init python:
    Room(**{
    "name": "forest",
    "display_name": "Forest",
    "exits": ["map"],
    "conditions": [
        HasVehicle(),
        ],
    "travel_time": 2,
    "music": "music/darren_curtis/into_oblivion.ogg",
    "ambience": "sd/SFX/ambiences/nature/forest.ogg",
    "outfit": "casual",
    })

    Activity(**{
    "name": "run_forest",
    "fun": 1,
    "energy": -1,
    "grooming": -2,
    "duration": 2,
    "rooms": "forest",
    "conditions": [
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("fun", 3),
            ),
        InInventory("sport_clothes"),
        ],
    "display_name": "Go for a run",
    "icon": "jog",
    "label": "run_forest",
    })

    Activity(**{
    "name": "hike_forest",
    "fun": 2,
    "energy": -1,
    "grooming": -2,
    "duration": 4,
    "rooms": "forest",
    "conditions": [
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("fun", 3),
            ),
        ],
    "display_name": "Go on a hike",
    "icon": "hike",
    "label": "hike_forest",
    })

    Event(**{
    "name": "bear_attack_male",
    "label": "bear_attack_male",
    "conditions": [
        IsSeason(0, 1, 2),
        IsHour(20, 6),
        HeroTarget(
            IsGender("male"),
            IsRoom("forest"),
            Not(InInventory("bear_bell")),
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
    "name": "bear_chan_pet",
    "label": "bear_chan_pet",
    "conditions": [
        IsSeason(0, 1, 2),
        IsHour(20, 6),
        HeroTarget(
            IsGender("male"),
            IsRoom("forest"),
            InInventory("bear_bell"),
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

label bear_chan_pet:
    scene bg forest with fade
    "The forest isn't normally somewhere I'd ever have thought to come after dark."
    "But it's been one of those days, you know?"
    "The kind where you just need to find a way to unwind?"
    "And as I pondered what to do, the thought popped right in there."
    "Why not drive to the forest and take a long stroll there?"
    "It's not like it's too far from my house, and it's bound to be quiet at this time of night."
    "So that's how I find myself walking down a deserted woodland path after the sun's set."
    "At first, I feel like patting myself on the back for having thought of this."
    "All the usual bothersome hikers and dog-walkers have long since gone home."
    "Which means that I have the place to myself to enjoy at my leisure."
    "It's so quiet and peaceful out here in the forest."
    "I honestly believe that I could be the only human being for miles around."
    play sound hitting_bushes
    "But all it takes is the sound of one snapping branch to change my mood completely."
    "My head turns to look in the direction of the sound."
    "And just like that, the whole atmosphere of the woods seems to transform."
    "Before everything was still, giving me a pleasant sense of solitude."
    "But now that same silence and emptiness is starting to make me uneasy."
    "Ah, who the hell am I trying to kid?"
    "It's practically making me shit my pants!"
    "Stopping on the path, I cast my eyes around the trees and undergrowth."
    "Why in the hell didn't I bring a flash-light?"
    "Why in the hell can't I get a signal on my phone?"
    "Why in the hell did I come here in the first place?!?"
    mike.say "Who...who's there?"
    "There's no answer to my question."
    "Just more rustling amongst the bushes."
    "And more snapping twigs, lots more."
    mike.say "I...I'm armed..."
    mike.say "You want to get shot out here?"
    "I'm not armed, obviously."
    "If I was too dumb to think of bringing a flash-light, you think I'd have thought to bring an actual gun?"
    "My only hope is that whoever's out there might think twice about the possibility."
    "Or maybe not - as I can hear them coming ever closer."
    show bear at blacker, center, zoomAt(1.0, (-250, 600))
    pause 0.1
    play sound hitting_bushes
    show bear at blacker, center, zoomAt(1.0, (1800, 600)) with MoveTransition(0.3)
    "In fact, they're moving faster by the second."
    "The moment before I turn to run, I see why my threats had no effect whatsoever."
    "At first it just looks like a portion of the darkness is coming towards me."
    play sound woosh_punch
    hide bear
    show bear at center, blacker, zoomAt(1.0, (640, 600))
    with dissolve
    pause 0.2
    hide bear
    show bear at center, zoomAt(1.0, (640, 600)) with dissolve
    "But then it resolves itself into the shape of a huge, hulking animal."
    "And it can only be a bear!"
    "This is it - I'm going to die out here in the woods."
    "All because I wanted to take an evening stroll."
    "The bear comes to a halt perhaps a dozen feet from me."
    "It stares blankly, as if seeing me for the first time."
    "Which seems kind of odd, because I would have assumed it could already smell me."
    "I always seem to see nature shows where they go on about how sharp animals senses are."
    "But this thing is looking at me like I surprised it taking a dump or something!"
    mike.say "Ah..."
    mike.say "N...nice bear..."
    mike.say "Good bear..."
    "At the sound of my voice, the bear begins to move forwards."
    "And I'm sure that I just blew any chance I had to escape this encounter alive."
    hide bear
    show bg forest at blur(16), dark, dark
    with wipedown
    "I squeeze my eyes shut, tensing every muscle in my body as I prepare for death."
    play sound bear_groan
    "But then I hear a grunting, chuffing noise."
    "At the same time, something cold and wet brushes against my face."
    scene bg forest
    show bear at center, zoomAt(1.5, (640, 750))
    with wipeup
    "Opening one eye, I see the bear pushing it's snout into me."
    "It's snuffling away like a dog looking for a treat."
    "With both eyes open now, I stand still and let it do as it pleases."
    show bear at center, zoomAt(1.0, (640, 600))
    "That is until it backs up a little and returns to staring at me."
    "The bear seems to be waiting for something now."
    "What is the thing expecting me to do?"
    $ renpy.show("sasha_arm_pat", at_list=[zoomAt(1.0, (300, -10))])
    with dissolve
    "Bereft of any better ideas, I reach out a hand."
    $ renpy.show("sasha_arm_pat", at_list=[zoomAt(1.0, (150, -60)), rotation(-10), slide(30, 2.0)])
    "And I pat it as gently as I can on top of the head."
    mike.say "Yeah..."
    mike.say "Like I said, good bear..."
    mike.say "Thanks for not eating me!"
    $ renpy.hide("sasha_arm_pat")
    with dissolve
    play sound bear_groan
    "The bear makes another chuffing sound, then turns around."
    hide bear with dissolve
    "I keep on standing still as it shuffles off back into the trees."
    "And once I'm sure it's gone, I dash back in the direction I came."
    "All I want now is to make it to the safety of my car."
    "Then I can drive home and never come here again."
    "Oh, and I can change my pants too..."
    return

label bear_attack_male:
    scene bg black
    show bear attack
    $ persistent.bear_attack = True
    if not game.flags.cheat:
        if renpy.has_label("mike_achievement_0") and (game.days_played == 0 or (game.days_played == 1 and game.hour <= 10)):
            call mike_achievement_0 from _call_mike_achievement_0_3
        if renpy.has_label("bear_achievement_1"):
            call bear_achievement_1 from _call_bear_achievement_1
    "I glance back over my shoulder, ready to give myself up and claim ignorance."
    "And it's then that I see something that instantly makes me pollute the pure fresh air of the forest I'm currently in."
    "It's a bear. Huge, ugly and like something out of cinematic nightmare."
    "And it's bearing down on me with its mouth wide open."
    "Red shining eyes stare at me behind the two razor-sharp claws that are dashing towards my face."
    "I'm not frozen in place by the fear, but it does make me panic and reduce my legs to limp noodles."
    "I try with all of my might to push myself faster through the forest, but everything happens so fast."
    "The shape of the bear looms over me, it's jaws closing faster than I ever thought it was possible for something that large to move."
    "There's no pain, but only because there isn't time for me to make sense of what's happening."
    show bear attack at blood, hshake
    "Everything is churning, green grass and a red that isn't the bear's gaping mouth."
    show bear attack at blur(8), dark, red, hshake
    "And then there's nothing but black..."
    scene bg black with dissolve
    pause 1.0
    $ renpy.full_restart()
    return

label hike_forest:
    show chibi hike
    if hero.fitness <= 50:
        $ hero.fitness += 1
        $ hero.fun += 1
    python:
        run_say = [
    "I go for a hike in the forest...",
    "Hiking is so relaxing."
    ]
    $ renpy.say("", randchoice(run_say))
    return

label run_forest:
    show chibi run
    if hero.fitness <= 50:
        $ hero.fitness += 1
    python:
        run_say = [
    "I go for a run in the forest...",
    "Running is good for what I have."
    ]
        successes = []
        for girl in Room.find(game.room).get_present_girls():
            if hero.fitness * 2 > girl.love:
                successes.append(girl)
                girl.love += 1
    if successes:
        if len(successes) == 1:
            $ renpy.show(f"{successes[0].id}")
            if isinstance(successes[0], Guy):
                "[successes[0].name] can't take his eyes off me while I run."
            else:
                "[successes[0].name] can't take her eyes off me while I run."
            $ renpy.hide(f"{successes[0].id}")
        else:
            if all([isinstance(i, Girl) for i in successes]):
                "The girls can't take their eyes off me while I run."
            else:
                "They can't take their eyes off me while I run."
    else:
        $ renpy.say("", randchoice(run_say))
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
