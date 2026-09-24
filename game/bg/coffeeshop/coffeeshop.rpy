init python:
    Consumable("coffee", price=25, tooltip="A simple coffee", effects=[("energy", 1)], label="drink_coffee", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("cappuccino", price=50, tooltip="A frothy cappuccino", effects=[("energy", 2)], label="drink_coffee", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("moka", price=100, tooltip="A rich moka coffee", effects=[("energy", 3)], label="drink_coffee", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("pine_needle_tea", price=50, tooltip="A herbal tea, made from pine needles", effects=[("energy", 2)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("rose_hip_tea", price=150, tooltip="A tea that can be use as a painkiller, made from Rose Hips", effects=[("energy", 3)], label="drink_tea_cured", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("sage_tea", price=100, tooltip="A tea with a strong and unique flavor, made from sage", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("turmeric_tea", price=100, tooltip="A tea from Okinawa, made of the rhizomes of turmeric", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("white_peony_tea", price=100, tooltip="A white fruity tea, made from leaf shoot and young leaves of the Camellia sinensis", effects=[("energy", 2)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("willow_bark_tea", price=50, tooltip="A tea that can be used to relieve headaches, made from Willow bark", effects=[("energy", 2)], label="drink_tea_cured", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("peppermint_tea", price=50, tooltip="A tea made by infusing peppermint leaves", effects=[("energy", 2)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("parsley_tea", price=100, tooltip="A tea made by steeping fresh or dried parsley", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("nettle_tea", price=50, tooltip="A tea with a floral taste, made from fresh leaves of nettle", effects=[("energy", 2)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("mint_tea", price=100, tooltip="A tea made by infusing mint leaves", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("marigold_tea", price=150, tooltip="Delicious and healthy way to have a good cold glass of iced tea, made from French marigold", effects=[("energy", 4)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("liquorice_tea", price=50, tooltip="A tea with strong flavor not suitable for everyone, made from Liquorice", effects=[("energy", 2)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("jasmine_tea", price=100, tooltip="A black jasmine tea, subtly sweet and highly fragrant", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("honeysuckle_tea", price=100, tooltip="Made with Honeysuckle sun tea method, making it delicious", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("hibiscus_tea", price=150, tooltip="A herbal tea with reminiscent of cranberry juice, and similar to raw hibiscus flowers", effects=[("energy", 4)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("ginger_tea", price=200, tooltip="A herbal beverage that has many health benefits, made from ginger root", effects=[("energy", 3)], label="drink_tea_cured", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("fennel_tea", price=50, tooltip="A tea with a relaxing scent and slightly bitter aftertaste, taste a little like licorice", effects=[("energy", 2)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("cinnamon_tea", price=100, tooltip="A tea with distinctively sweet and aromatic notes, made by infusing cinnamon bark", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("chamomile_tea", price=100, tooltip="A tea that tastes silky but also fresh and floral, with a crisp apple flavour", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("buckwheat_tea", price=100, tooltip="A tea that has a toasty aroma and nutty sweet flavor, made of organic roasted buckwheat", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("english_breakfast_tea", price=100, tooltip="A tea that offers a bold flavor similar to coffee with roasted notes", effects=[("energy", 2)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("earl_grey_green_tea", price=50, tooltip="A tea with the finesse of green tea associated to the flavor of bergamot", effects=[("energy", 2)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("earl_grey_black_tea", price=50, tooltip="Smooth and balanced, with notes of citrus, spice, malt, and smoke", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("darjeeling_tea", price=100, tooltip="Musky-sweet tasting notes similar to muscat wine", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("assam_tea", price=100, tooltip="A tea with almost caramel sweetness", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("sencha_tea", price=100, tooltip="A green tea with a wide variety of flavors", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("russian_caravan_tea", price=100, tooltip="This tea has a distinct smoky, slightly sweet flavor.", effects=[("energy", 3)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("lady_grey_tea", price=150, tooltip="Contains lemon and orange peel that give it a softer, more subtle citrusy flavor", effects=[("energy", 4)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])
    Consumable("ceylon_tea", price=50, tooltip="A taste full bodied and rich, but not harsh or bitter", effects=[("energy", 2)], label="drink_tea", frequency_limit="day", conditions=[HeroTarget(IsFlag("coffee", False))])

    Room(**{
    "name": "coffeeshop",
    "exits": ["mall2","flowershop","electronic", "drugstore", "jewelrystore", "mallmap"],
    "display_name": "Coffee Shop",
    "hours": (7, 18),
    "conditions": [
        IsHour(7, 18),
        ],
    "music": "music/roa_music/chillaxing_waves.ogg",
    "outfit": "casual",
    "tags": ["mall_southside", "mall_northside"],
    "inventory": (
        "coffee",
        "cappuccino",
        "moka",
        {"id": "pine_needle_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "rose_hip_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "sage_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "turmeric_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "white_peony_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "willow_bark_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "peppermint_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "parsley_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "nettle_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "mint_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "marigold_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "liquorice_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "jasmine_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "honeysuckle_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "hibiscus_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "ginger_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "fennel_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "cinnamon_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "chamomile_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "buckwheat_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "english_breakfast_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "earl_grey_green_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "earl_grey_black_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "darjeeling_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "assam_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "sencha_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "russian_caravan_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "lady_grey_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        {"id": "ceylon_tea", "conditions": ("'gianna_coffeshop_tea' in DONE",)},
        ),
    })

    Activity(**{
    "name": "drink_a_coffee_coffeeshop",
    "label": "drink_coffee_coffeeshop",
    "duration": 0,
    "icon": "coffee",
    "rooms": "coffeeshop",
    "conditions": [
        Not(
            And(
                IsNotDone("gianna_coffeshop_tea"),
                HeroTarget(MinFlag("coffee_drank", 10)),
                ),
            ),
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            ),
        ],
    "display_name": "Buy a coffee",
    })

    Activity(**{
    "name": "work_coffeeshop",
    "label": "work_coffeeshop",
    "money_gain": {"attributes": ["charm", "knowledge"], "bonus": (1,)},
    "duration": 4,
    "rooms": "coffeeshop",
    "conditions": [
        HeroTarget(
            MinStat("energy", 4),
            MinStat("hunger", 4),
            MinStat("grooming", 4),
            MinStat("fun", 4),
            IsFlag("job_day", "coffeeshop"),
            ),
        ],
    "display_name": "Work",
    "icon": "work",
    })

    Activity(**{
    "name": "gianna_coffeshop_tea",
    "label": "gianna_coffeshop_tea",
    "duration": 0,
    "icon": "coffee",
    "rooms": "coffeeshop",
    "conditions": [
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            MinFlag("coffee_drank", 10),
            ),
        ],
    "do_once": True,
    "display_name": "Buy a coffee",
    })

label work_coffeeshop:
    show chibi coffeeshop
    "If I can sell a hundred coffee I get a one dollar bonus!"
    hide chibi
    $ game.flags.story_hasworked = True
    $ game.flags.hasworked = TemporaryFlag(True, "day")
    return

label drink_coffee_coffeeshop:
    if "gianna_coffeshop_tea" in DONE:
        $ Room.find("coffeeshop").shop("gianna teaser")
    else:
        $ Room.find("coffeeshop").shop(Transform("breedad", matrixcolor=TintMatrix("#000")))
    return

label drink_coffee:
    show chibi coffee
    play sound coffee
    "I drink some coffee..."
    if game.room == 'kitchen':
        $ game.flags.kitchencoffee = TemporaryFlag(True, "day")
    else:
        $ game.flags.coffee = TemporaryFlag(True, "day")
    hide chibi
    stop sound
    return

label drink_tea:
    show chibi coffee
    "I drink some tea..."
    $ game.flags.coffee = TemporaryFlag(True, "day")
    hide chibi
    return

label drink_tea_cured:
    show chibi coffee
    "I drink some tea..."
    $ game.flags.coffee = TemporaryFlag(True, "day")
    call cured from _call_cured
    hide chibi
    return

label gianna_coffeshop_tea:
    scene bg coffeeshop with fade
    "When you come to the same coffee shop every day, you stop thinking about it."
    "The barista knows your order, you tap your card, and you're out the door — minimum effort, minimum conversation."
    "But today I want something different. I'm either over-caffeinated or just desperate enough to try tea."
    "I've seen it on the menu plenty of times. How complicated could it really be?"
    show gianna teaser with easeinleft
    "Gianna" "Hey there..."
    "Gianna" "What can I get for you today?"
    "The voice is sweet and completely unfamiliar — which means this barista is new."
    "New enough not to know my usual order. Which means first impressions still count."
    mike.say "Hey there..."
    "I glance at her name-tag."
    mike.say "Gianna... I think I'd like to try a tea, please."
    "Long brown hair in bunches, pale green eyes, and an impressive figure behind her apron."
    "My choice of drink isn't the only interesting new thing in here today."
    show gianna teaser at startle
    "Gianna" "A tea?!?"
    "Gianna" "You're sure you don't mean a coffee?"
    "The barrage of questions catches me off guard. I actually glance around to check if this is a joke."
    "It isn't. I turn back and try to answer at least one of them."
    mike.say "No, I'm totally serious. I want a tea."
    show gianna teaser at startle
    "Gianna claps her hands together with glee."
    "Gianna" "You just made my day! I LOVE tea — but nobody ever orders it here."
    "Gianna" "So, what can I get you?"
    mike.say "Erm... didn't I just say? A tea."
    "Gianna" "What KIND of tea, silly!"
    "Gianna" "Black, green, chai, bubble, smoked?"
    mike.say "I... I don't know..."
    "Gianna" "Or a blend! We have English Breakfast, Earl Grey, Darjeeling, Assam, Sencha, Russian Caravan, Lady Grey and Ceylon!"
    mike.say "Whoa... are those drinks or place names?"
    "Gianna" "More of a flavour person? Then there's Willow Bark, White Peony, Turmeric, Sage, Rose Hip, Peppermint, Nettle, Mint, Jasmine, Hibiscus, Ginger, Chamomile, Cinnamon..."
    "Gianna" "Phew. I think that's most of them!"
    "I stand there, completely blank, brain fully offline."
    "The pressure of being expected to respond pushes it straight into meltdown."
    mike.say "I... I just wanted tea-flavoured tea!"
    "That has to be the dumbest thing anyone has ever said in a coffee shop."
    scene bg street with fade
    "I turn on my heel and walk straight out the door."
    "I don't stop until I'm two blocks away, slightly breathless and deeply embarrassed."
    "Eventually I'll have to go back — I'm far too hooked on their coffee to stay away forever."
    "I just have to hope that when I do, Gianna has forgotten every word of this."
    $ game.room = "street"
    $ game.flags.tea_drank = set()
    return
return