init python:
    Event(**{
    "name": "bird_attack_female",
    "label": "bird_attack_female",
    "conditions": [
        IsHour(6, 20),
        HeroTarget(
            IsGender("female"),
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

    Event(**{
    "name": "shark_attack_female",
    "label": "shark_attack_female",
    "conditions": [
        IsHour(22, 6),
        HeroTarget(
            IsGender("female"),
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

label bird_attack_female:
    scene bg beach
    "I'm not usually one for eating on the move, I like to sit down and enjoy my food."
    "Even when I'm at the beach, I always want to take a moment to relax when I eat."
    "So as soon as I grab something tasty from one of the food stalls on the sand, that's what I do."
    "Of course I make sure that it's something that tastes totally amazing."
    "And I start to munch on it the moment that I sit down with my prize."
    "Soon I'm feeling pretty pleased with myself."
    "Because in my mind, I'm being hyper efficient and using my time wisely."
    "And the pleasant taste of my convenient snack only helps to add to the feeling."
    "So yeah, I'm thinking that I have this whole thing nailed down."
    "Like I could write a book on being a modern woman that's totally in control."
    $ renpy.sound.set_pan(1, 0, channel='sound')
    $ renpy.sound.set_pan(-1, 2.0, channel='sound')
    play sound seagull fadein 0.5
    "That is until I hear the sudden sound of something screeching."
    "At first I think it sounds like some kind of hell-spawned demon."
    $ renpy.sound.set_pan(-1, 0, channel='sound')
    $ renpy.sound.set_pan(1, 2.0, channel='sound')
    play sound doves fadein 0.5
    with hpunch
    "But then a streak of dirty feathers shoots past my face."
    "I realise that it must be a bird of some kind."
    "And when it comes back a second later, swooping in from the opposite direction, I realise something else too."
    $ renpy.sound.set_pan(1, 0, channel='sound')
    $ renpy.sound.set_pan(0, 2.0, channel='sound')
    play sound seagull
    $ renpy.sound.set_pan(1, 0, channel='audio')
    $ renpy.sound.set_pan(0, 2.0, channel='audio')
    play sound dove
    show bird attack with hpunch
    "The damn thing is attacking me!"
    bree.say "AARGH!"
    bree.say "Help me!"
    bree.say "Get it away!"
    "I leap up and narrowly avoid having the thing swoop straight into me."
    "I'm running in a circle, waving my hands in the air as I try to shoo the bird away."
    "But for some reason this seems to have the exact opposite effect."
    play sound seagull
    with hpunch
    "Instead of leaving me alone, the bird starts to go for me all the more."
    "And I swear that I can feel it's vicious talons clawing at my fingers!"
    "It's so scary that I almost drop the food I was just eating."
    "That's when it hits me - the food!"
    play sound seagull
    with hpunch
    "The damn bird has to be after my food!"
    bree.say "Oh no you don't..."
    bree.say "I paid good money for this..."
    bree.say "Go get your own, you...you feathered freeloader!"
    "With that I decide to make a run for it."
    "And so still waving my hands in the air, I take off down the beach."
    "I was hoping that the bird might have a territory or something."
    "At least that it wouldn't follow me too far."
    "But no matter how fast I run, it seems to keep pace with ease."
    "So I find myself ducking and dodging as I run."
    "I'm almost stepping on bathers laid out on their towels."
    "All of my attention is on trying to spot the bird before it can swoop down on me again."
    "But after nearly colliding with people walking on the sand, I decide to give up."
    "Which basically entails tossing the damn food aside and keeping on running."
    "Luckily for me, this seems to work."
    $ renpy.sound.set_pan(0, 0, channel='sound')
    $ renpy.sound.set_pan(-1, 2.0, channel='sound')
    play sound seagull
    scene bg beach
    "The bird follows the food and leaves me alone."
    "But all the same, I still keep watching the sky for a good while."
    "Afraid that the damn thing might come back once it's eaten my food."
    "And all the while I'm telling myself that this is why I don't usually eat when I'm at the beach."
    $ hero.fun -= 3
    $ hero.energy -= 3
    $ hero.money -= 10
    $ hero.fitness += 1
    $ persistent.bird_attack = True
    return

label shark_attack_female:
    scene bg beach
    "It's on days like this that I wonder why I don't spend more time at the beach."
    "I mean, the sun is high in the sky and beating down on beautiful, golden sand."
    "And it's shimmering off the waves as they lap their way onto the sand too."
    "Plus the beach is totally full of gorgeous people, lounging around in their swimming costumes."
    "Of course, it doesn't hurt that a lot of them are looking in my direction right now."
    "But then who can blame them for checking me out?"
    "I'm in great shape and my own swimming costume is like the stuff of legends."
    "All in all, I'm really working it today, and I totally deserve all the attention I'm getting."
    "Even when I stop and pause for a moment, I can still feel that there are eyes on me."
    "Hmmm..."
    "I wonder what I should do next?"
    "Perhaps I should walk out into the water and take a swim?"
    "Not because I want to keep on showing off and getting admiring looks, obviously."
    "Taking a swim would be a great idea because it's such great exercise, you know?"
    "And that's the enough to make up my mind."
    "Turning towards the water, I saunter into the waves and begin to wade out."
    "The water quickly covers my feet, and then my ankles to."
    "Within a few more steps it's rising up my claves and towards the knee."
    "And by the time it's halfway up my thighs, I'm far enough out to begin swimming."
    show swimmingrace_bg_02 at flip
    show swimmingrace_breemc_02 at flip
    show swimmingrace_outfit_breemc_normal_02 at flip
    show swimmingrace_water_breemc_02 at flip
    show swimmingrace_water_fg_breemc_02 at flip
    with fade
    "So I lean forwards into the water, reaching out my arms to begin using them to propel myself."
    "After that, all it takes is a couple of kicks from my legs, and I'm off."
    "And I have to say that, from here, the water feels even better than it looked from the beach."
    "Before I know it, I'm happily ploughing my way through it."
    "Which means that I'm getting a great workout."
    "And no doubt looking damn good at the same time."
    "I can hear the usual hubbub coming from the beach."
    "All the sounds you'd expect from a load of people doing whatever it is they're doing."
    "And when they start to become louder, it's not really something that gets my attention."
    "It's only when I actually pick out the first of the screams that everything changes."
    "Because it's not just the sound of someone finding out the water's too cold."
    "Those are genuine screams of alarm, and they're starting to get me worried."
    "Bather" "SHARK!"
    "Bather" "There's a shark out there!"
    "Wait a minute..."
    "I have to be hearing things, right?"
    "There can't actually be a shark in the water?"
    "Like the kind with the fin on the back and the huge, razor-sharp teeth?"
    "Risking a look back over my shoulder, I instantly see a fin."
    show shark_attack_bg at center, zoomAt(1.0, (640, 720))
    show shark_attack_shark at center, zoomAt(1.0, (340, 720))
    show shark_attack_shark at center, traveling(1.2, 5.0, (680, 800))
    show shark_attack_water at center, zoomAt(1.0, (640, 720))
    show shark_attack_breemc
    show shark_attack_fg at center, zoomAt(1.0, (640, 720))
    with fade
    "And there are the razor-sharp teeth too!"
    "Instantly my brain goes into a state of panic, and my limbs thrash in the water."
    "Every muscle in my body is trying to push me faster through the waves."
    "But all the time the shark is getting closer, coming straight for me!"


















    "Even working as hard as I am right now, I don't seem to be moving much."
    "Maybe the panic is making me flounder in the water, rather than swim."
    "Which is kind of a shame, because the shark is having no such problems."
    "Perhaps the one mercy I get is that everything happens so damn fast."
    show shark_attack_bg at center, traveling(1.2, 5.0, (680, 800))
    show shark_attack_shark at center, traveling(1.2, 5.0, (680, 800))
    show shark_attack_water at center, traveling(1.2, 5.0, (680, 800))
    show shark_attack_fg at center, traveling(1.2, 5.0, (680, 800))
    show shark_attack_breemc at hshake
    pause 0.3
    hide shark_attack_breemc with easeoutbottom
    if not game.flags.cheat and renpy.has_label("shark_achievement_1"):
        call shark_achievement_1 from _call_shark_achievement_1_1
    "Before I can even feel the pain, it's jaws clamp down on me."
    show shark_attack_water at blood
    show shark_attack_fg at blood
    with dissolve
    "And after that I'm no longer swimming at all, just being dragged through the water."
    "The sounds of the other bathers on the beach are getting fainter with every passing moment."
    "And all of my senses are being overwhelmed at once, making everything a blur."
    scene bg black with dissolve
    "So when it all goes black, at first that seems to be just another aspect of the confusion."
    "It's only when none of my senses return that I even have an inkling something is wrong."
    "And by that time it's too late, as I'm already sinking into an ocean of blankness."
    "One from which there's no chance of returning."
    pause 1.0
    $ renpy.mark_image_seen("shark attack")
    $ renpy.full_restart()
    $ persistent.shark_attack = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
