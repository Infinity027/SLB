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
            IsGender("male"),
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
    "When you frequent the same coffee shop day in and day out, you kind of go in there on autopilot."
    "Like, sometimes you don't even have to look up from your phone all the while that you're in there."
    "It's just like, the barista recognises you, they make your usual, then you swipe your card or phone."
    "Then you're out of there, coffee in hand, having had the least social interaction possible."
    "But today is different, as I have a craving for something different."
    "I don't know if I'm over-caffeinated right now."
    "Or just dreaming of a different beverage to keep me from falling asleep at my desk."
    "Whatever the reason for my sudden decision to betray coffee - I want to try some tea."
    "I know that the coffee shop has a lot of them on the menu, because I've seen it."
    "I just don't know that much about the stuff."
    "But how hard can it be?"
    "You just put it in a cup, like coffee, right?"
    show gianna teaser with easeinleft
    "Gianna" "Hey there..."
    "Gianna" "What can I get for you today?"
    "The voice is sweet and clear as a bell."
    "Plus it's also totally unfamiliar to my ear."
    "Either one of those things would normally be enough to make me look up and pay attention."
    "But perhaps the most important thing here is the fact that the person speaking doesn't know my usual order."
    "Which means that they're new here - so it's time to make a good first impression!"
    if hero.is_male:
        mike.say "Hey there..."
    else:
        bree.say "Hey there..."
    "I take a moment to read the girl's name-tag."
    if hero.is_male:
        mike.say "Gianna..."
        mike.say "I think I'd like to try a tea, please."
    else:
        bree.say "Gianna..."
        bree.say "I think I'd like to try a tea, please."
    "Of course I'm studying the new barista all the time I'm saying this."
    "And I have to admit that I'm more than a little impressed with what I'm seeing."
    "Long brown hair in bunches, pale green eyes and an impressive figure behind her apron."
    "Looks like my choice of drink isn't the only exciting new thing in here today!"
    show gianna teaser at startle
    "Gianna" "A tea?!?"
    "Gianna" "You really want a tea?"
    "Gianna" "You're sure you don't really mean a coffee?"
    "Having so many intense questions fired at me one after another is pretty confusing."
    "So much so that I take a step backwards and look around me to see if this is some kind of joke."
    "But when nobody jumps out and says as much, I shake it off and try to answer."
    "Or at least I try to answer one of them."
    if hero.is_male:
        mike.say "No, I'm totally serious..."
        mike.say "I want a tea."
    else:
        bree.say "No, I'm totally serious..."
        bree.say "I want a tea."
    show gianna teaser at startle
    "Gianna claps her hands together with glee."
    "Gianna" "Yes!"
    "Gianna" "You just made my day!"
    "Gianna" "I LOVE tea - but all anybody orders is coffee."
    "Gianna" "Well, until you came along!"
    "Gianna" "So...what can I get you?"
    if hero.is_male:
        mike.say "Erm..."
        mike.say "Didn't I already say I wanted a tea?"
    else:
        bree.say "Erm..."
        bree.say "Didn't I already say I wanted a tea?"
    "Gianna" "What KIND of tea, silly!"
    "Gianna" "Like...do you want black or green?"
    "Gianna" "Maybe you want chai or bubble?"
    "Gianna" "Or even smoked?"
    if hero.is_male:
        mike.say "I..."
        mike.say "I don't know..."
    else:
        bree.say "I..."
        bree.say "I don't know..."
    "Gianna" "Or how about a blend, yeah?"
    "Gianna" "We have English Breakfast, Earl Grey, Darjeeling, Assam, Sencha, Russian Caravan, Lady Grey and Ceylon!"
    if hero.is_male:
        mike.say "Whoa..."
        mike.say "Are those drinks or place names?"
    else:
        bree.say "Whoa..."
        bree.say "Are those drinks or place names?"
    "Gianna" "Hmm..."
    "Gianna" "Perhaps you're more a flavour guy?"
    "Gianna" "In which case you can choose from Willow Bark, White Peony, Turmeric, Sage, Rose Hip, Pine Needle, Peppermint, Parsley, Nettle, Mint, Marigold, Liquorice, Jasmine, Honeysuckle, Hibiscus, Ginger, Fennel, Cinnamon, Chamomile or Buckwheat..."
    "Gianna" "Phew..."
    "Gianna" "I think that's all of them!"
    "All I can do is stand and stare at Gianna in amazement."
    "But I know that she's expecting me to say something."
    "And the pressure that puts on me seems to make my brain go into meltdown."
    if hero.is_male:
        mike.say "I..."
        mike.say "I..."
        mike.say "I just wanted tea flavoured tea!"
    else:
        bree.say "I..."
        bree.say "I..."
        bree.say "I just wanted tea flavoured tea!"
    "After all the varieties and flavours that Gianna just reeled off, that must sound so dumb."
    "She must think I'm the stupidest guy that ever lived right now!"
    scene bg street with fade
    "The only thing that I can think to do is turn on my heel and run straight out of the door."
    "I don't stop or look back until I'm at least a couple of blocks away from the coffee shop."
    "And it's only then that I realise I'll probably have to go back there sooner or later."
    "Maybe not as soon as tomorrow, but eventually as I have a serious addiction to decent coffee."
    "I guess I just have to hope that when I finally do, nobody that just witnessed all of that is in there too."
    $ game.room = "street"
    $ game.flags.tea_drank = set()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
