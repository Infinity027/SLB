init python:
    Event(**{
    "name": "bear_attack_female",
    "label": "bear_attack_female",
    "conditions": [
        IsSeason(0, 1, 2),
        IsHour(20, 6),
        HeroTarget(
            IsGender("female"),
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

label bear_attack_female:
    scene bg forest
    "The forest is so peaceful and serene at this time in the evening, I can't believe I never thought of this before."
    "I've not seen another human being since I got here, and I could be the only person for literally miles around here."
    "Normally when I go out for a walk in the evening, I end up at the local park, which is always full of people."
    "People walking their yapping dogs, people running into you as they jog and worst of all, people taking a walk at the same time as me!"
    "But out here, on this forest path, there's just me and the silent, welcoming bosom of nature."
    "I really should do this more often, because I can actually feel myself starting to relax and unwind."
    "Before I was going over all the petty little stresses of my day, probably shortening my lifespan as a result."
    "And now all of that is just melting away, the things I was hung up on looking small and unimportant."
    "Aaah...yeah, this really is the best idea that I've had in a bloody long time."
    $ renpy.sound.set_pan(-1, 0, channel='sound')
    play sound bear_groan
    "Bear" "Uuurgh…"
    "The sound comes out of nowhere, long and low, like a deep grumble."
    "I can't help jumping and turning in a circle when I hear it."
    "My head spinning as I try to figure out where it's coming from."
    bree.say "Erm..."
    bree.say "Hello?"
    bree.say "Is there anyone out there?"
    "I wait for what feels like forever."
    "Listening to my own words and they echo through the trees and then fade into silence."
    "But no more than a few seconds later, the sound comes again, louder than before."
    $ renpy.sound.set_pan(0.25, 0, channel='sound')
    play sound bear_roar
    "Bear" "Uuurgghuurgah!"
    "I've already begun to walk backwards, even before I realise my legs are moving at all."
    "Part of me wants to turn and just run, as fast as I can back down the path in the direction from which I came."
    "But the more rational part keeps telling me that would be a bad idea."
    "That it'd mean showing my back to what's making that terrible sound."
    "So for the moment I try to move as fast as I can without turning at all."
    "This means that I keep on stumbling, almost falling over backwards."
    "But by now I've begun to hear noises coming from amongst the trees off the path."
    play sound hitting_bushes
    "The sound of breaking limbs and fallen branches snapping under the tread of something heavy."
    "I can't have made it more than a few dozen metres when I see a shape moving out there too."
    "Huge and round, it perfectly matches all of the sounds that I've heard so far."
    "And the more I see of it, the more my hair stands on end."
    "I honestly think I know what the thing is before I get a good look at it."
    "And when the hulking shape finally emerges onto the path, it can only be a bear."
    "I have no fucking clue what kind it is, just that it's the biggest thing I've ever seen."
    "And that it's looking right at me, in the least friendly way imaginable!"
    "Somehow I manage to keep my whole body from freezing up at the sight of the bear."
    "I manage perhaps another half a dozen steps before the bear really begins to advance on me."
    "But when it does, the thing moves with enough speed to make me piss myself!"
    "I have one chance to act and one chance only."
    "It's really that serious."
















    "The only thing that I can think to do is turn and run."
    "To run as fast as I possibly can and hope it's fast enough."
    "It might seem a hopeless, even crazy thing to do."
    "But just standing there and letting the bear have it's way with me seems even crazier."
    play sound body_fall
    with hpunch
    "I have non idea how far I've made it when the first blow lands."
    "It's not like being hit by another human being, not in the slightest."
    "This is more like being sideswiped by a speeding car."
    play sound bear_growl
    "One moment I'm upright and running, the next I'm face down on the ground."
    if renpy.has_label("bear_achievement_1"):
        call bear_achievement_1 from _call_bear_achievement_1_1
    $ renpy.sound.set_pan(0, 0, channel='sound')
    play sound bear_roar
    show bear attack
    "There's no sense of falling, just the sudden, shocking change of position."
    "I don't feel any pain either, thanks to how fast everything is happening."
    "Before I can even think of crawling, some part of the bear hammers down onto me."
    show bear attack at blood, hshake
    "Something breaks, but I don't know what it is."
    "I just know that I couldn't move if I tried."
    show bear attack at blur(8), dark, red, hshake
    "My awareness doesn't las much longer than that."
    "Not even long enough for me to realise what's happening."
    "It fades quickly, which I suppose is something to be thankful for."
    "And then there's nothing."
    scene bg black with dissolve
    pause 1.0
    $ renpy.full_restart()
    $ persistent.bear_attack = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
