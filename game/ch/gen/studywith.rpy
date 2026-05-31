init 1:
    layeredimage studywith:
        attribute_function MultiPickers([PregnancyPicker, HaircutPicker, CollarPicker, OutfitPicker, MCCGPicker], append_npc_from_attributes=True)


        always:
            "studywith_bg"


        always:
            if_any ["minami", "kylie", "emma", "bree", "lexi", "reona"] if_not "nonpc"
            "studywith_book"


        group mc auto


        always:
            "studywith_pen"


        attribute nonpc null
        group npc auto if_not "nonpc"


        group collars auto if_not "nonpc"


        group haircuts auto if_not "nonpc"


        group pregnant auto if_any ["pregnant"] if_not "nonpc"


        group multiple auto variant piercings when not nonpc


        group outfits auto if_not "nonpc"


        group breemc_collars auto if_any "breemc"

        group breemc_haircuts auto if_any "breemc"

        group multiple auto variant breemc_piercings when breemc
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
