init python:


    Equip("fancy_clothes", gender="male", price=200, tooltip="Elegant attire to impress with charm {b}even in the most swanky places{/b}", effects={"pacifist": 20, "princess": 20, "charm": 10})
    Equip("tweed_blazer", gender="male", price=100, tooltip="A sophisticated blazer for the presence", effects={"bookworm": 20, "family": 20, "knowledge": 5})
    Equip("military_fatigues", gender="male", price=100, tooltip="Rugged wear with pants and t-shirt", effects={"submissive": 20, "gourmand": 20, "charm": 5})
    Equip("luxury_watch", type="accessory", gender="male", price=200, tooltip="A stylish and shiny accessory well detail", effects={"pacifist": 20, "princess": 20, "charm": 10})


    Equip("leather_jacket", price=100, tooltip="A rebellious jacket with attitude", effects={"submissive": 20, "rebel": 20, "charm": 5})
    Equip("sweat_pants", price=100, tooltip="Comfortable pants for the sporty", effects={"sporty": 20, "dominant": 20, "fitness": 5})
    Equip("funny_shirt", price=100, tooltip="A playful shirt with geeky humor", effects={"geek": 20, "playful": 20, "charm": 5})
    Equip("sport_clothes", price=200, tooltip="Ideal outfit for {b}sports and fitness{/b}", effects={"sporty": 30, "fitness": 10})
    Equip("swimsuit", price=200, tooltip="Perfect swimwear for {b}watery activities{/b}", effects={"sporty": 30, "fitness": 10})
    Equip("cool_sunglasses", type="accessory", price=100, tooltip="Stylish sunglasses for a rebellious look", effects={"submissive": 20, "rebel": 20, "charm": 5})
    Equip("geeky_pen", type="accessory", price=100, tooltip="A pen for the knowledgeable bookworm", effects={"bookworm": 20, "family": 20, "knowledge": 5})
    Equip("sport_shoes", type="accessory", price=100, tooltip="Shoes designed for sporty individuals", effects={"sporty": 20, "dominant": 20, "fitness": 5})
    Equip("funny_badge", type="accessory", price=100, tooltip="A playful badge with geeky humor", effects={"geek": 20, "playful": 20, "charm": 5})
    Equip("military_boots", type="accessory", price=100, tooltip="Rugged and strong boots", effects={"submissive": 20, "gourmand": 20, "charm": 5})



    Gift("lingerie", price=150, tooltip="Seductive lingerie for a flirty appeal and to {b}amplify allure of specific people{/b}", tags=["underwear"], label="sexy_underwear", love_bonus=3, once=True, bonus_traits=["not_innocent", "flirty"])
    Gift("sexy_dress", price=200, tooltip="A provocative dress to {b}enhance allure{/b}", tags=["clothes"], label="sexy_dress", sub_bonus=5, once=True, bonus_traits=["not_innocent", "flirty"])
    Gift("slutty_dress", price=400, tooltip="A daring dress to {b}amplify allure{/b}", tags=["clothes"], label="slutty_dress", sub_bonus=10, once=True, bonus_traits=["not_innocent", "flirty", "slutty", "submissive"])
    Gift("cute_top", price=100, tooltip="A sweet charming top", tags=["clothes"], love_bonus=2, bonus_traits=["flirty", "innocent"])
    Gift("nice_scarf", price=50, tooltip="A stylish scarf with a touch of flirtiness", tags=["clothes"], love_bonus=1, bonus_traits=["flirty", "artsy"])
    Gift("sexy_swimsuit", price=100, tooltip="A revealing swimsuit to {b}enhance allure{/b}", tags=["swimsuit"], label="swimsuit", sub_bonus=5, once=True, bonus_traits=["flirty", "slutty"])
    Gift("cute_swimsuit", price=200, tooltip="A lovely swimsuit", tags=["swimsuit"], love_bonus=4, bonus_traits=["not_slutty"])
    Gift("purse", price=200, tooltip="A fashionable purse with appeal", tags=["purse"], love_bonus=4, bonus_traits=["flirty"])
    Gift("fancy_purse", price=400, tooltip="A luxurious purse fit for a princess", tags=["purse"], love_bonus=6, bonus_traits=["princess", "flirty", "slutty"])
    Gift("shoes", price=100, tooltip="Classical stylish shoes", tags=["shoes"], love_bonus=2, bonus_traits=["flirty"])
    Gift("fancy_shoes", price=200, tooltip="Elegant shoes fit for a princess", tags=["shoes"], love_bonus=4, bonus_traits=["princess", "flirty", "slutty"])




    Gift("sexy_underwear", price=150, tooltip="Seductive underwear for men", tags=["underwear"], love_bonus=3),
    Gift("tuxedo", price=200, tooltip="A classy tuxedo to impress", tags=["clothes"], love_bonus=4),
    Gift("tshirt", display_name="T-shirt", price=100, tooltip="A casual t-shirt", tags=["clothes"], love_bonus=2),
    Gift("leather_shoes", price=50, tooltip="Stylish leather shoes", tags=["clothes"], love_bonus=1),
    Gift("swimming_tback", display_name="Swimming t-back", price=100, tooltip="A bold swimwear choice", tags=["swimsuit"], love_bonus=2),
    Gift("swimming_trunk", price=200, tooltip="Stylish swimwear for men", tags=["swimsuit"], love_bonus=4),
    Gift("wallet", price=200, tooltip="A practical and stylish wallet", tags=["purse"], love_bonus=4),
    Gift("fancy_watch", price=400, tooltip="A luxurious watch to impress", tags=["purse"], love_bonus=6),
    Gift("sports_shoes", price=100, tooltip="Comfortable sports shoes", tags=["shoes"], love_bonus=2),

    Room(**{
    "name": "clothesshop",
    "exits": ["mall1", "bakery", "bookstore", "arcade", "tattooshop", "mallmap"],
    "display_name": "Clothes Shop",
    "hours": (9, 18),
    "conditions": [
        IsHour(9, 18),
        ],
    "music": "music/roa_music/wishes.ogg",
    "outfit": "casual",
    "tags": ["mall_southside"],
    "itm_class_choice": [("For me", Equip), ("For someone", Gift)],
    "inventory": {
        "Women section": (
            {  
                "conditions": ("hero.is_female", ),
                "items": (
                    "fancy_dress",
                    {"id": "sexy_date_equip", "conditions": ("hero.morality <= -20", "hero.has_item('fancy_dress')",)},
                    {"id": "slutty_date_equip", "conditions": ("hero.morality <= -80", "hero.has_item('sexy_date_equip')",)},
                    {"id": "innocent_date_equip", "conditions": ("hero.morality >= 20",)},
                    {"id": "pure_date_equip", "conditions": ("hero.morality >= 80", "hero.has_item('innocent_date_equip')",)},
                    "leather_jacket",
                    {"id": "innocent_casual_equip", "conditions": ("hero.morality >= 60",)},
                    "cardigan",
                    "sweat_pants",
                    "funny_shirt",
                    "leather_pants",
                    "sport_clothes",
                    "swimsuit",
                    {"id": "sexy_swimsuit_equip", "conditions": ("hero.morality <= -40", "hero.has_item('swimsuit')",)},
                    {"id": "innocent_swimsuit_equip", "conditions": ("hero.morality >= 40", "hero.has_item('swimsuit')",)},
                    "luxury_bracelet",
                    "cool_sunglasses",
                    "geeky_pen",
                    "sport_shoes",
                    "funny_badge",
                    "military_boots",
                ),
            },
            
            "lingerie",
            "sexy_dress",
            "slutty_dress",
            "cute_top",
            "nice_scarf",
            "sexy_swimsuit",
            "cute_swimsuit",
            "purse",
            "fancy_purse",
            "shoes",
            "fancy_shoes",
            
            
            ),
        "Men section": (
            {  
                "conditions": ("hero.is_male", ),
                "items": (
                    "fancy_clothes",
                    "leather_jacket",
                    "tweed_blazer",
                    "sweat_pants",
                    "funny_shirt",
                    "military_fatigues",
                    "sport_clothes",
                    "swimsuit",
                    "luxury_watch",
                    "cool_sunglasses",
                    "geeky_pen",
                    "sport_shoes",
                    "funny_badge",
                    "military_boots",
                ),
            },
            {  
                "conditions": ("hero.is_female", ),
                "items": (
                    "sexy_underwear",
                    "tuxedo",
                    "tshirt",
                    "leather_shoes",
                    "swimming_tback",
                    "swimming_trunk",
                    "wallet",
                    "fancy_watch",
                    "sports_shoes",
                ),
            },
            ),
        },
    })

    Activity(**{
    "name": "clothesshop_shop",
    "duration": 0,
    "display_name": "Shop",
    "icon": "shop",
    "rooms": "clothesshop",
    "label": "clothesshop_shop",
    })

label clothesshop_shop:
    $ Room.find("clothesshop").shop("sasha" if sasha.present else None)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
