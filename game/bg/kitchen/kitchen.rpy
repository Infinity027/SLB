init python:
    meal_say = [
    [ 
        "You aren't a bad cook...",
        "You'll make a fine bride some day.",
        "I can't eat one more bit.",
        "That soup was pretty good.",
        "Are you trying to make me fat?"
        ],
    [ 
        "This is amazing!",
        "So true!",
        "It's pretty good!"
        ],
    [ 
        "Can I have seconds?",
        "You need to send me this recipe.",
        "And you made fancy drinks too?",
        "You make this dish better than Mom did.",
        "Did you make this from scratch?"
        ],
    [ 
        "I love pasta...\nMaybe that's why I have so much weight to lose...",
        "I make myself a sandwich.",
        "I cook some chicken.",
        "I was never a fish lover, I fancy myself a carnivore.",
        "Why bother with vegetables, meat is life!"
        ]
]

    Room(**{
    "name": "kitchen",
    "exits": ["livingroom","housemap"],
    "music": house_music(),
    "outfit": "casual",
    "tags": ["home"],
    })

    Activity(**{
    "name": "drink_a_coffee",
    "energy": 2,
    "duration": 0,
    "icon": "coffee",
    "label": "drink_coffee",
    "rooms": "kitchen",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            IsFlag("kitchencoffee", False),
            Not(OnDate()),
            ),
        ],
    "display_name": "Drink coffee",
    "once_day": True,
    })

    Activity(**{
    "name": "generic_meal",
    "hunger": 10,
    "icon": "eat",
    "rooms": "kitchen",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            Not(MaxStat("hunger")),
            Not(OnDate()),
            ),
        ],
    "display_name": "Have a meal",
    "label": "generic_meal",
    })

    Activity(**{
    "name": "do_the_dishes",
    "duration": 0,
    "fun": -0.5,
    "rooms": "kitchen",
    "conditions": [
        HeroTarget(
            MinStat("energy", 2),
            MinStat("hunger", 2),
            MinStat("grooming", 2),
            MinStat("fun", 2),
            IsFlag("cleaningservices", False),
            Not(OnDate()),
            ),
        ],
    "display_name": "Do the dishes",
    "icon": "dishes",
    "label": "do_the_dishes",
    "once_day": True,
    })

    Event(**{
    "name": "sasha_kitchen_bree",
    "label": "sasha_kitchen_bree",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("kitchen")
            ),
        "not Harem.find_by_name('home')",
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "chances": 5,
    "do_once": False,
    "once_week": True,
    })

label generic_meal:
    $ present_people = Room.find(game.room).get_present_girls_ids(valid=True)
    $ fun_bonus = len(present_people)
    if 'sasha' in present_people and sasha.flags.cheated:
        $ present_people.remove("sasha")


    if not present_people:
        show chibi eat
        $ narrator(randchoice(meal_say[3]))
        $ hero.flags.alone_meal = True
    else:
        $ meal_label = "_".join(["meal"] + present_people)
        $ hero.flags[meal_label] = True
        $ hero.fun += fun_bonus


        $ renpy.random.shuffle(present_people)
        $ i = 0
        while i < len(present_people):
            if renpy.has_label(present_people[i] + "_greet"):
                call expression present_people[i] + "_greet" from _call_expression_161

            $ meal_love = 1
            if hero.has_skill("cooking"):
                $ meal_love += 1
            if hero.charm >= 40:
                $ meal_love += 1
            $ Person.find(present_people[i]).love += meal_love
            $ i += 1
        show expression f"kitchen meal multi {' '.join(present_people)}"
        "We have a nice meal together."
        python:
            for idx, p in enumerate(present_people):
                renpy.say(p, randchoice(meal_say[idx if idx <= 2 else 2]))
    return

label sasha_kitchen_bree:
    show bree at left
    show sasha at right
    "Sasha and [bree.name] are chatting in the kitchen."
    if game.days_played <= 7:
        sasha.say "It's great to have found this place."
        bree.say "Yeah, it's cheap and nice."
        sasha.say "And the roommate is kinda cute."
        bree.say "Yeah, I wouldn't mind having a piece of him."
        sasha.say "Be careful of your diet."
        $ bree.love += 1
        $ sasha.love += 1
    elif sasha.love + hero.charm > 100 and bree.love + hero.charm > 100 and sasha.lesbian > MIN_LES_GIRL_SEX and bree.lesbian > MIN_LES_GIRL_SEX:
        bree.say "I've seen the way you look at [hero.name]."
        sasha.say "I wouldn't mind sharing him..."
        $ bree.love += 1
        $ sasha.love += 1
        bree.say "Me neither."
    elif sasha.love + hero.charm > 100 and bree.love + hero.charm > 100 and sasha.lesbian > MIN_LES_GIRL_SEX:
        bree.say "I've seen the way you look at [hero.name]."
        sasha.say "I wouldn't mind sharing him..."
        $ bree.love += 1
        $ sasha.love += 1
        bree.say "Over my dead body."
    elif sasha.love + hero.charm > 100 and bree.love + hero.charm > 100 and bree.lesbian > MIN_LES_GIRL_SEX:
        bree.say "I've seen the way you look at [hero.name]."
        sasha.say "You're no better."
        bree.say "Where there's room for one, there's room for two..."
        sasha.say "Where there's room for me, there's none for anyone else."
        $ bree.love += 1
        $ sasha.love += 1
        bree.say "We'll see..."
    elif sasha.love + hero.charm > 100 and bree.love + hero.charm > 100:
        bree.say "I've seen the way you look at [hero.name]."
        sasha.say "You're no better."
        bree.say "I guess that makes us rivals."
        sasha.say "Don't be a sore loser when you find me in bed with him..."
        $ bree.love += 1
        $ sasha.love += 1
        bree.say "I guess we'll find out then what happens."
    elif bree.love + hero.charm > 100:
        bree.say "I'm thinking on making a move on [hero.name]."
        sasha.say "Good luck with that."
        $ sasha.love += 1
    elif sasha.love + hero.charm > 100:
        sasha.say "I'm thinking of making [hero.name] my personal sextoy."
        bree.say "You should totally go for it."
        $ bree.love += 1
    else:
        "They just talk about girly stuff."
        $ bree.love += 1
        $ sasha.love += 1
    return

label do_the_dishes:
    show chibi dishes
    play sound dishes
    $ game.set_flag("chores", 5, "week", "+")
    "I do the dishes."
    stop sound
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
