init python:
    Event(**{
    "name": "dog_attack_female",
    "label": "dog_attack_female",
    "conditions": [
        IsHour(6, 20),
        HeroTarget(
            IsGender("female"),
            Or(
                IsRoom("map"),
                HasRoomTag("street"),
                ),
            Or(
                HasSkill("animalhated"),
                MaxStat("energy", 3),
                ),
            ),
        ],
    "chances": 10,
    "once_week": True,
    })

label dog_attack_female:
    if game.room == "map":
        scene bg street
    else:
        scene expression f"bg {game.room}"
    "I'm just walking down the street when it happens, minding my own business as usual."
    "My mind on any number of things that pop in there as I go from one place to the next."
    play sound dog_small volume 0.3
    "At first I don't really notice the sound of a dog barking at all."
    "And when I do, it's just a part of the background noise around me."
    "The ever-present soundtrack to my life that I hardly know is even there."
    "It's only when I start to see people turning their heads to look behind me that it changes."
    "People are frowning at first, as if they see something they don't like the look of."
    "And then some of them begin to cross the road, trying to avoid it too."
    $ renpy.sound.set_pan(-0.75, 0, channel='sound')
    play sound dog_small volume 0.8
    "All the time the sound of the barking is getting louder, like it's coming closer to me."
    "Then finally I see a guy almost throw himself into the road."
    "His face a picture of surprise and growing fear."
    "That's when I get the feeling there's something wrong."
    "And so I turn to see whatever it could be."
    "I don't actually stop walking, just twist to see behind me."
    "But as soon as I do, I turn around and start walking backwards."
    "Because it's only now that I see the dog coming towards me."







    "For a moment I think that I'm worrying about nothing."
    "That the dog's just going to dodge to the left or right and run straight past me."
    "But as it gets closer, I see it's beady little eyes focussing in on my ankles."
    "And as soon as that happens, I know that I'm the centre of it's attention."
    "Right now it seems like I can just about keep out of it's reach."
    "But when I sneak a look back over my shoulder, I slow down a little."
    "And then the god darts forwards, almost making it to my ankles."
    "So I let out a little yelp and speed up again."
    play sound dog_small
    with hpunch
    bree.say "Argh!"
    bree.say "Erm..."
    bree.say "Hey there, doggy..."
    bree.say "You...you seem REALLY mean!"
    bree.say "But maybe that's just because you look mean, huh?"
    bree.say "Maybe people are judging you how your appearance, which wouldn't be fair."
    bree.say "Maybe you're actually a nice doggy...a sweet doggy?"
    "I reach out a tentative hand as I say all of this."
    "Hoping that the dog will prove me right and roll over onto it's back."
    "But the moment my hand is vaguely within reach, the dog lunges for it."
    $ renpy.sound.set_pan(0, 0, channel='sound')
    play sound dog_small
    "The thing snarls and slavers, teeth snapping within inches of my fingers!"
    bree.say "Oh no..."
    bree.say "You're every bit as mean and nasty as you look!"
    "There's nothing else for it, so I take a deep breath."
    "Then I turn around and run, as fast as I can down the street."
    if hero.fitness >= 50:
        "I feel like the dog must be right on my heels."
        "Like any moment I'll feel it's jaws clamping down on me."
        "But at the same time my body seems to go into automatic."
        "All of my time at the gym and the jogging sessions are paying off."
        "Because I can feel myself running faster, not tiring in the slightest."
        $ renpy.sound.set_pan(-0.5, 0, channel='sound')
        play sound dog_small volume 0.5
        "And at the same time, the sound of the dog's barking is getting quieter."
        "As soon as I can't hear it anymore, I risk a look over my shoulder."
        "And I'm just in time to see it barrelling off down another street."
        "It must have gotten tired of chasing me and spotted some easier-looking prey."
        "I know it sounds cruel, but in the moment I can't help wishing it'd run right under a semi-truck!"
        "But at least it's finally left me alone."
        $ renpy.sound.set_pan(0, 0, channel='sound')
        "So with my lungs burning and my breath coming in ragged gasps, I start walking again."
        "Hoping that I don't see that awful thing ever again."
        $ hero.energy -= 1
        $ hero.fitness += 1
    else:
        "I feel like the dog must be right on my heels."
        "Like any moment I'll feel it's jaws clamping down on me."
        "But even worse is the fact that I can already feel myself slowing down."
        "My body's betraying me, taking revenge for all the times I skipped the gym!"
        $ renpy.sound.set_pan(0, 0, channel='sound')
        play sound "<from 0 to 0.6>sd/SFX/animals/dog_small.ogg"
        show dog attack with hpunch
        "Before I know it, the damn mutt is chewing on my leg!"
        play sound "<from 0 to 0.6>sd/SFX/animals/dog_small.ogg"
        "Luckily the dog seems to have gotten more of my pants than my actual leg."







        "Dog owner" "Rupert!"
        "Dog owner" "Rupert, you naughty boy!"
        "Soon I see a man wrestling the dog onto a lead."
        "All the time he's smiling up at me, trying to ingratiate himself."
        "Dog owner" "I'm so sorry, miss..."
        "Dog owner" "He's a big softie really!"
        "I do the best I can to nod and smile."

        scene bg street with fade
        "But at least it's finally gone."
        "So with my head spinning and my legs feeling like jelly, I start walking again."
        "Hoping that I don't see that awful thing ever again."
        $ hero.fun -= 5
        $ hero.energy -= 5
        $ hero.fitness += 1
    $ persistent.dog_attack = True
    return

label found_money_female:
    menu:
        "Take it":
            $ hero.money += amount
            $ hero.morality -= 1
        "Leave it":
            $ hero.morality += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
