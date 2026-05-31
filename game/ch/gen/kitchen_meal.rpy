init python:
    class KitchenMealPicker(object):
        def __call__(self, attr):
            if not {"breakfast", "salad", "meat"} & attr:
                if game.calendar.get_time_of_day() == "morning":
                    attr.add("breakfast")
                else:
                    attr.add(randchoice(["salad", "meat"]))
            if enable_debug_picker:
                renpy.log(f"KitchenMealPicker results: {attr}")
            return attr
init 1:
    layeredimage kitchen meal multi:
        attribute_function MultiPickers([MCCGPicker, PregnancyPicker, CollarPicker, OutfitPicker, PiercingsPicker, HaircutPicker, KitchenMealPicker], append_npc_from_attributes=True)

        group mc_dicks auto:
            attribute mc_small null
            attribute mc_medium null
            attribute mc_big null

        attribute breakfast null
        attribute salad null
        attribute meat null
        attribute mike null
        attribute mikemc null
        attribute breemc null

        always "kitchen_meal_multi_bg"

        group multiple auto variant person

        group multiple auto variant collars

        attribute mc_pregnant if_any ["mc_naked"]
        attribute bree_pregnant if_any ["bree_naked", "bree_topless"]
        attribute lexi_pregnant if_any ["lexi_naked", "lexi_topless"]
        attribute minami_pregnant if_any ["minami_naked", "minami_topless"]
        attribute samantha_pregnant if_any ["samantha_naked", "samantha_topless"]
        attribute sasha_pregnant if_any ["sasha_naked", "sasha_topless"]

        group multiple auto variant piercings 

        attribute mc_naked null
        group breemcoutfit auto variant "notpregnant" if_any ["breemc"] if_not ["mc_pregnant", "mc_naked"]
        group breemcoutfit auto variant "pregnant" if_all ["breemc", "mc_pregnant"] if_not ["mc_naked"]

        attribute bree_naked null
        attribute bree_topless null
        group breeoutfit auto variant "notpregnant" if_any ["bree"] if_not ["bree_pregnant", "bree_naked", "bree_topless"]
        group breeoutfit auto variant "pregnant" if_all ["bree", "bree_pregnant"] if_not ["bree_naked", "bree_topless"]

        attribute lexi_naked null
        attribute lexi_topless null
        group lexioutfit auto variant "notpregnant" if_any ["lexi"] if_not ["lexi_pregnant", "lexi_naked", "lexi_topless"]
        group lexioutfit auto variant "pregnant" if_all ["lexi", "lexi_pregnant"] if_not ["lexi_naked", "lexi_topless"]

        attribute minami_naked null
        attribute minami_topless null
        group minamioutfit auto variant "notpregnant" if_any ["minami"] if_not ["minami_pregnant", "minami_naked", "minami_topless"]
        group minamioutfit auto variant "pregnant" if_all ["minami", "minami_pregnant"] if_not ["minami_naked", "minami_topless"]

        attribute samantha_naked null
        attribute samantha_topless null
        group samanthaoutfit auto variant "notpregnant" if_any ["samantha"] if_not ["samantha_pregnant", "samantha_naked", "samantha_topless"]
        group samanthaoutfit auto variant "pregnant" if_all ["samantha", "samantha_pregnant"] if_not ["samantha_naked", "samantha_topless"]

        attribute sasha_naked null
        attribute sasha_topless null
        group sashaoutfit auto variant "notpregnant" if_any ["sasha"] if_not ["sasha_pregnant", "sasha_naked", "sasha_topless"]
        group sashaoutfit auto variant "pregnant" if_all ["sasha", "sasha_pregnant"] if_not ["sasha_naked", "sasha_topless"]

        attribute sasha_noboobjob null
        attribute sasha_boobjob if_any ["sasha_naked", "sasha_topless"]
        group boobs auto if_all ["sasha_boobjob"] if_not ["sasha_naked", "sasha_topless"]

        group multiple auto variant piercings_bb when sasha_boobjob and (sasha_naked or sasha_topless)
        group multiple auto variant piercings_notbb when (sasha_naked or sasha_topless) and not sasha_boobjob


        always "kitchen_meal_multi_counter"


        group multiple auto variant plate


        group multiple auto variant food_salad when salad
        group multiple auto variant food_breakfast when breakfast
        group multiple auto variant food_meat when meat


        group multiple auto variant arms
        group breemcarms_outfit auto if_any ["breemc"] if_not ["mc_naked"]
        group breearms_outfit auto if_any ["bree"] if_not ["bree_naked", "bree_topless"]
        group sashaarms_outfit auto if_any ["sasha"] if_not ["sasha_naked", "sasha_topless"]

        always "kitchen_meal_multi_tap"


        always "kitchen_meal_multi_mike" if_any ["mike", "mikemc"] if_not ["lexi"]
        always "kitchen_meal_multi_mike_notsam" if_any ["mike", "mikemc"] if_all ["lexi"] if_not ["samantha"]
        always "kitchen_meal_multi_mike_lexi" if_any ["mike", "mikemc"] if_all ["lexi", "samantha"]

        always "kitchen_meal_multi_bottle"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
