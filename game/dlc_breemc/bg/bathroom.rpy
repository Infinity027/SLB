init python:
    Activity(**{
    "name": "makeup",
    "charm": 0.5,
    "icon": "mirror",
    "rooms": "bathroom",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            MinStat("energy", 5),
            MinStat("hunger", 5),
            MinStat("grooming", 5),
            MinStat("fun", 5),
            MaxStat("charm", 25),
            ),
        ],
    "display_name": "Put some make-up on",
    "once_day": True,
    "say": [
        "Looking sexy!",
        ],
    })

    Activity(**{
    "name": "use_pregnancy_test",
    "display_name": "Use a pregnancy test",
    "max_girls": 0,
    "rooms": ["firstfloorbathroom", "bathroom"],
    "conditions": [
        HeroTarget(
            IsGender("female"),
            ),
        InInventory("pregnancy_test"),
        ],
    "label": "use_pregnancy_test",
    "icon": "pregtest",
    "once_day": True,
    })

    Activity(**{
    "name": "shave_pubes",
    "grooming": 8,
    "rooms": ["firstfloorbathroom", "bathroom"],
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsFlag("pubes", True),
            ),
        ],
    "display_name": "Shave pubes",
    "label": "shave_pubes",
    "icon": "shave",
    })

label shave_pubes:
    show chibi shave
    "I shaved my pubes."
    $ hero.flags.pubes = False
    $ hero.flags.last_shave = game.days_played
    hide chibi
    return

label use_pregnancy_test:
    if hero.flags.foundpreg:
        "I'm not sure why I would use this..."
        "I already know that I'm pregnant..."
        return
    show chibi pregnancy
    "Urgh..."
    "This is one of those positions that you always tell yourself you're never going to end up in."
    "I mean, it's such a fucking cliche!"
    "How many times have I seen a girl in a movie with one of these things in a bathroom?"
    "Someone using a pregnancy test and then waiting for the result while they hold their breath?"
    "Well one thing that I can tell you is the holding your breath part is bullshit."
    "The instructions say that this thing takes a good few minutes to give a result."
    "So I'd have passed out and smashed my head on the toilet by then!"
    "Okay, okay..."
    "Come on, [hero.name] - you can do this!"
    "With the test in one hand, I use the other to pull down my pants."
    "Because of course I have to pee on this thing."
    "No way they could fail to make it anything but undignified!"
    "Wait a minute..."
    "How am I supposed to aim at this thing?"
    "It's not like I can watch myself peeing!"
    "I guess I just have to hold it under my ass and hope for the best..."
    play sound "<from 0 to 4>sd/SFX/humans/peeing.ogg" fadeout 0.5
    "There..."
    "I think that hit the spot."
    stop sound fadeout 0.5
    "As I pull up my pants, I take a look at the test."
    "Yeah, definitely hit the spot."
    "So I suppose all I can do now is wait."
    "I sit down on the toilet, knowing that I locked the door before I came in here."
    "Bad luck for anyone needing to use the bathroom while I wait."
    "They're just going to have to suck it up!"
    "My mind wanders as I'm sitting still with nothing better to do."
    "I keep turning it over and over in my mind."
    "And I honestly can't decide which would be worse - a positive or a negative result."
    "Sure, you'd probably assume that I want it to be the latter."
    "But that's just the thing - I don't know what I want."
    "I haven't had the chance to really decide how I feel about being pregnant."
    "A negative result would make things easier."
    "But the thought makes me feel a little stab of panic too."
    "Is it possible that I want this?"
    "That I really want to have a baby?"
    "While I'm thinking about all of this, I must have lost track of time."
    "Because when I happen to look down at the test, I see something's changed."
    "At first I don't know what it means, so I scramble for the instructions."
    "And even then I have to check the result a couple of times before I'm convinced."
    "Well, that puts an end to all of the speculation."
    "Because the result is clear..."
    if hero.pregnant:
        "It's positive!"
        $ hero.flags.foundpreg = True
        menu:
            "Be happy":
                $ hero.flags.happypreg = True
                $ hero.fun += 5
                "Oh god, it's positive!"
                "I'm...I'm going to be a mom!"
                "The moment that realisation dawns on me, everything seems to change."
                "Before I was terrified of the whole thing, every single part of it."
                "But now the knowledge that I'm having a baby, growing a life inside me..."
                "Somehow it seems to make all the other bits fade into the background."
                "Sure, I'm still pretty scared of the responsibility."
                "And I have no idea how I'm going to tell the father."
                "But all of that seems to be things that can be sorted out later."
                "They're starting to feel like they can be handled when they come up."
                "And even if the father's not interested, that I can handle too."
                "I mean, women have been raising kids on their own since forever."
                "It's never easy and it won't be any different for me."
                "But the idea doesn't scare me as much as it used to."
                "In fact, I can feel a smile spreading over my face."
                "Because I think everything's going to be alright."
                "I think I can do this thing."
            "Be unhappy":
                $ hero.flags.happypreg = False
                $ hero.fun -= 5
                "Oh god, it's positive!"
                "Of course it's positive - it had to be!"
                "No way I was going to get lucky and it go the other way."
                "I guess this is what I deserve for being careless."
                "And it's only going to get harder from here on in."
                "Because now I have to decide what I'm actually going to do about it."
                "Do I keep the baby or have an abortion?"
                "Both of those things are terrifying to even think about."
                "Then there's the other person involved in all of this."
                "Well...maybe I should say the third person involved."
                "Because the baby's wrapped up in it too."
                "Do I tell the person that I think is the father?"
                "I suppose I really should."
                "But what if they want something different than I do?"
                "Why does life have to be so hard?"
    else:
        "It's negative!"
        "Oh god...it's negative!"
        "I feel a flood of relief pass through me."
        "It's a physical sensation, like a flush that makes me shiver."
        "I'm not pregnant, I got away with it!"
        "This time, I tell myself."
        "I got away with it this time."
        "What I need to do now is straighten up and get smart."
        "I need to learn the lesson and not get in this position again."
        "But at the same time I'm promising myself that, I'm feeling something else too."
        "It's weird, because I should be over the moon."
        "Yet a little piece of me is wondering what if..."
        "What if I had been pregnant and chosen to keep the baby?"
        "I shake my head, pushing the thought aside."
        "There's going to be plenty of time for that later."
        "I can be a mom when I'm good and ready."
        "Right now I should be thankful for having the choice."
    $ hero.lose_item("pregnancy_test")
    return


label generic_get_out_dialogues_1_female:
    bree.say "Sure."
    return

label generic_get_out_dialogues_2_female:
    bree.say "Sorry [name], I didn't know you would be in here."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
