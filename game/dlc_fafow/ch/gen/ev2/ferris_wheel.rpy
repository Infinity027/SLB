init 1:
    layeredimage ferris wheel:
        attribute_function MultiPickers([ HaircutPicker, CollarPicker, OutfitPicker, MCCGPicker, DayNightPicker], append_npc_from_attributes=True, use_morgan_cg_outfits=True)

        group bg auto

        attribute mikemc
        group mc_dicks auto:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null

        group mc_outfits auto variant "mikemc" if_any "mikemc"

        group npc auto

        attribute morgan_makeup
        attribute aletta_glasses if_any "aletta"

        group outfits auto
        attribute sasha_boobjob if_any "sasha"

        group collars auto

        group haircuts auto:
            attribute morgan_nohaircut null

        group pregnancies auto

        group amy_necktie auto if_any "amy"


        group outfits auto variant "collarcover" if_any "morgan"
        attribute breemc
        group mc_haircuts auto variant "breemc" if_any "breemc":
            attribute mc_nohaircut null
        group mc_outfits auto variant "breemc" if_any "breemc"
        group mc_collars auto variant "breemc" if_any "breemc"