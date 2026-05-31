init 1:
    layeredimage tattooparlor:
        attribute_function MultiPickers([HaircutPicker, CollarPicker, PregnancyPicker, PiercingsPicker, OutfitPicker, PubesPicker], add_simple_pregnant_attribute=True, append_npc_from_attributes=True)

        attribute pregnant null
        attribute collar null

        attribute notop null
        attribute topless null
        attribute bottomless null

        attribute focused null
        attribute head null
        attribute sasha_lips null

        attribute makeup null

        always:
            "tattooparlor_bg"

        always:
            if_not "kleio"
            "tattooparlor_chair"

        always:
            if_any "kleio"
            "tattooparlor_bed"

        group npc auto

        group tattoo auto

        group pubic auto

        group bot auto

        group bot_opened auto if_any ["bottomless"]
        group bot_closed auto if_not ["bottomless"]

        group pregnancy auto if_any ["pregnant"]

        group bot_opened variant "pregnant" auto if_all ["pregnant", "bottomless"]
        group bot_closed variant "pregnant" auto if_any ["pregnant"] if_not ["bottomless"]
        group bot variant "pregnant" auto if_any ["pregnant"]

        group multiple auto variant piercings

        group top auto

        group top_opened auto if_any ["topless"] if_not ["notop"]
        group top_opened auto variant "boobjob" if_all ["topless", "sasha_boobjob"] if_not ["notop"]
        group top_opened auto variant "pregnant" if_all ["topless", "pregnant"] if_not ["notop"]

        group piercings_opened auto if_any ["topless"] if_not ["notop"]

        group top_closed auto if_not ["topless", "notop"]
        group top_closed auto variant "boobjob" if_not ["topless", "notop"] if_all ["sasha_boobjob"]
        group top_closed auto variant "pregnant" if_not ["topless", "notop"] if_any ["pregnant"]

        group top auto variant "pregnant" if_any ["pregnant"] if_not ["notop"]
        group piercings_preg auto if_any ["pregnant"] if_not ["notop"]

        attribute sasha_boobjob if_all "sasha_boobjob" if_any ["topless", "notop"]
        group multiple auto variant piercings_noboobjob when (topless or notop) and not sasha_boobjob
        group multiple auto variant piercings_boobjob when (topless or notop) and sasha_boobjob

        group haircuts auto
        group glasses auto

        attribute morgan_makeup null
        group makeup auto if_any "morgan_makeup"
        group focused auto variant "head" if_all ["focused", "head"]
        group makeup_focused auto if_all ["focused", "head", "morgan_makeup"]
        group add_piercing auto if_all ["focused", "head"]

        always:
            "tattooparlor_fg"

        group insert auto variant "belly" if_all ["focused", "belly", "notop"]
        group insert auto variant "bottom" if_all ["focused", "bottomless"]
        group insert auto variant "chest" if_all ["focused", "topless"]
        group insert auto variant "chest_boobjob" if_all ["focused", "topless", "sasha_boobjob"]
        group insert auto variant "chest_noboobjob" if_all ["focused", "topless", "sasha"] if_not ["sasha_boobjob"]
        group insert auto variant "head" if_all ["focused", "head"]
        group haircuts_insert auto variant "bg" if_any "head"

        group insert_pubes auto if_all ["focused", "bottomless"]

        group multiple auto variant add_piercing_insert_belly when focused and belly and notop
        group multiple auto variant add_piercing_insert_navel when focused and belly and notop
        group multiple auto variant add_piercing_insert_bottom when focused and bottomless
        group multiple auto variant add_piercing_insert_chest when focused and topless
        group multiple auto variant add_piercing_insert_chest_boobjob when focused and sasha_boobjob and topless
        group multiple auto variant add_piercing_insert_chest_noboobjob when focused and sasha and topless and not sasha_boobjob
        group multiple auto variant add_piercing_insert_head when focused and head

        group haircuts_insert auto if_any "head"
        group haircuts_insert auto variant "fg" if_any "head"

        group collars auto

        group armchair auto

        group makeup_insert auto if_all ["focused", "makeup", "head"]




    layeredimage tattooparlormc:
        attribute_function MultiPickers([MCCGPicker], npcs=[hero])

        attribute notop null
        attribute topless null
        attribute bottomless null

        attribute focused null
        attribute head null

        always:
            "tattooparlormc_bg"

        always:
            "tattooparlormc_chair"

        group npc auto


        group bot auto variant "breemc" if_any "breemc" if_not ["bottomless"]

        group pregnancy auto variant "breemc" if_all ["mc_pregnant", "breemc"]

        group bot_opened variant "pregnant_breemc" auto if_all ["mc_pregnant", "bottomless", "breemc"]
        group bot_closed variant "pregnant_breemc" auto if_all ["mc_pregnant", "breemc"] if_not ["bottomless"]
        group bot variant "pregnant_breemc" auto if_all ["mc_pregnant", "breemc"] if_not ["bottomless"]

        group multiple auto variant piercings_breemc when breemc

        group top auto

        group top_opened auto variant "breemc" if_all ["topless", "breemc"] if_not ["notop"]
        group top_opened auto variant "pregnant_breemc" if_all ["topless", "mc_pregnant", "breemc"] if_not ["notop"]

        group piercings_opened auto variant "breemc" if_all ["topless", "breemc"] if_not ["notop"]

        group top_closed auto variant "breemc" if_any "breemc" if_not ["topless", "notop"]
        group top_closed auto variant "pregnant_breemc" if_not ["topless", "notop"] if_all ["mc_pregnant", "breemc"]

        group top auto variant "pregnant" if_any ["pregnant"] if_not ["notop"]
        group piercings_preg auto if_any ["mc_pregnant"] if_not ["notop"]

        group focused auto variant "head" if_all ["focused", "head"]
        group add_piercing auto if_all ["focused", "head"]

        group insert auto variant "belly" if_all ["focused", "belly", "notop"]
        group insert auto variant "bottom" if_all ["focused", "bottomless"]
        group insert auto variant "chest" if_all ["focused", "topless"]
        group insert auto variant "head" if_all ["focused", "head"]

        group insert_pubes auto variant "breemc" if_all ["focused", "bottomless", "breemc"]

        group multiple auto variant add_piercing_insert_belly_breemc when focused and belly and notop and breemc
        group multiple auto variant add_piercing_insert_navel_breemc when focused and belly and notop and breemc
        group multiple auto variant add_piercing_insert_bottom_breemc when focused and bottomless and breemc
        group multiple auto variant add_piercing_insert_chest_breemc when focused and topless and breemc
        group multiple auto variant add_piercing_insert_head_breemc when focused and head and breemc

        group collars auto variant "breemc" if_any "breemc"

        group armchair auto

        always:
            "tattooparlormc_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
