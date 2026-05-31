init 1:
    layeredimage bg park:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        group season auto variant "day" if_any "day"
        group season auto variant "night" if_any "night"
        always:
            "snow"

init python:
    Consumable("4leaf_clover", display_name="4 Leaf Clover", conditions=[HeroTarget(Not(MaxStat("luck")))], label="use_clover", tooltip="+1 Luck", frequency_limit="day")

    Room(**{
    "name": "park",
    "exits": ["map", "pond"],
    "music": season_music(),
    "random_music": True,
    "ambience": "sd/SFX/ambiences/nature/park.ogg",
    "tags": ["park"],
    })

    Activity(**{
    "name": "takeanappark",
    "label": "takeanappark",
    "energy": 1.5,
    "conditions": [
        IsSeason(1),
        IsHour(8, 20),
        HeroTarget(
            HasRoomTag("park"),
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            ),
        ],
    "display_name": "Take a nap",
    "once_day": True,
    "icon": "sleep",
    })

    Activity(**{
    "name": "run_park",
    "fun": 1,
    "energy": -1,
    "grooming": -2,
    "duration": 2,
    "conditions": [
        HeroTarget(
            HasRoomTag("park"),
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("fun", 3),
            ),
        InInventory("sport_clothes"),
        ],
    "display_name": "Go for a run",
    "icon": "jog",
    "label": "run_activity",
    })

    Activity(**{
    "name": "think",
    "label": "thinkpark",
    "knowledge": 0.5,
    "conditions": [
        HeroTarget(
            HasRoomTag("park"),
            MinStat("energy", 5),
            MinStat("hunger", 5),
            MinStat("grooming", 5),
            MinStat("fun", 5),
            MaxStat("knowledge", 25),
            ),
        ],
    "icon": "study",
    "display_name": "Think",
    "once_day": True,
    "say": [
        "What harsh truths do you prefer to ignore?",
        "Is free will real or just an illusion?",
        "Is there a meaning to life? If so, what is it?",
        "Is the meaning of life the same for animals and humans?",
        "Where is the line between art and not art?",
        "Does fate exist? If so, do we have free will?",
        "What does it mean to live a good life?",
        "Why do we dream?",
        "Is it possible to live a normal life and never tell a lie?",
        "Does a person's name influence the person they become?",
        "What should be the goal of humanity?",
        "What awaits me at the end of it all?",
        ],
    })

    Activity(**{
    "name": "find_clover",
    "display_name": "Find 4 Leaf Clover",
    "conditions": [
        IsSeason(0, 1, 2),
        IsHour(2, 8),
        HeroTarget(
            HasRoomTag("park"),
            Not(MaxStat("luck")),
            ),
        ],
    "duration": 0,
    "icon": "investigate",
    "label": "find_clover",
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "thug_attack",
    "conditions": [
        IsHour(22, 4),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("park"),
            IsFlag("dannydead", False),
            ),
        ],
    "chances": 5,
    "label": "park_thug_attack",
    "do_once": False,
    "once_day": True,
    })

    DayTransitionEvent(**{
    "name": "expire_clover",
    "label": "expire_clover",
    })

label find_clover:
    show chibi clover
    "I look for a 4 leaf clover to improve my luck."
    if randint(1, 100) > 80:
        "Yes! I found one!"
        $ hero.gain_item("4leaf_clover")
    else:
        "None today, I should try again tomorrow."
    return

label thinkpark:
    show chibi parkthink
    "I take some time to think about life, the universe and the rest..."
    return

label takeanappark:
    show chibi parknap
    "I take a nap on a bench."
    return

label use_clover:
    $ hero.flags.clover = True
    $ hero.luck += 1
    return

label expire_clover:
    if hero.flags.clover:
        $ hero.luck -= 1
        $ hero.flags.clover = False
    return

label run_activity:
    show chibi run
    if hero.fitness <= 50:
        $ hero.fitness += 1
    python:
        run_say = [
    "I go for a run in the park...",
    "Running is good for what I have."
    ]
        successes = []
        for girl in Room.find(game.room).get_present_girls():
            if not girl.flags.knows_mike_runs:
                girl.flags.knows_mike_runs = True
            if hero.fitness * 2 > girl.love:
                successes.append(girl)
                girl.love += 1
    if successes:
        if len(successes) == 1:
            hide chibi run
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

label park_thug_attack:
    "The park at night sure is scary..."
    thug_say "Hey, you!"
    show danny
    if not game.flags.thugfight:
        thug_say "Yeah, you! Give me your money!"
        $ fight = False
        menu:
            "Give it to him":
                "I give the thug my money."
                thug_say "Good boy."
                $ hero.money.val = 0
                $ hero.fun -= 5
            "Refuse":
                mike.say "No way, go fuck yourself."
                thug_say "You'll regret this, faggot."
                menu:
                    "Attack him":
                        $ fight = True
                    "Intimidate him":
                        mike.say "You should leave, I do Macrame."
                        if hero.charm >= 20:
                            thug_say "Is that an uber Israeli martial art?"
                            thug_say "Alright, alright alright..."
                            "He turns and runs as if the devil was on his tail."
                            $ game.flags.thugfight = 1
                        else:
                            thug_say "We'll see about that."
                            $ fight = True
        if fight:
            python:
                d = 50
                if not hero.has_skill("martial_arts"):
                    d += 25
            if hero.fitness >= d:
                play sound punch_hard
                pause 0.2
                show danny fight lose at center, hshake
                pause 0.2
                with hpunch
                "I kick his ass, badly."
                thug_say "I'll have my revenge!"
                "He turns and runs as if the devil was on his tail."
                $ game.flags.thugfight = 1
            else:
                play sound punch_hard
                pause 0.2
                show danny fight win at center, hshake
                pause 0.2
                with hpunch
                "The thug kicks my ass, takes my money and leaves me lying on the ground."
                thug_say "Next time, hand it over nicely."
                if hero.money > 500:
                    $ hero.money -= 500
                else:
                    $ hero.money.val = 0
                $ hero.grooming -= 5
                $ hero.energy -= 5
                $ hero.fun -= 5
            call injured from _call_injured_2
    else:
        show danny scared
        thug_say "Oh, it's you..."
        thug_say "Sorry sir, I didn't recognize you."
    hide danny
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
