init 1:
    layeredimage love boat:
        attribute_function MultiPickers([PregnancyPicker, PiercingsPicker, HaircutPicker, CollarPicker, OutfitPicker, MCCGPicker], append_npc_from_attributes=True, use_morgan_cg_outfits=True)

        always:
            "love_boat_bg"

        attribute mikemc
        group mc_dicks auto:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null

        group mc_outfits auto variant "mikemc" if_any "mikemc"

        attribute breemc
        group mc_haircuts auto variant "breemc" if_any "breemc":
            attribute mc_nohaircut null
        group mc_outfits auto variant "breemc" if_any "breemc"
        group multiple auto variant mc_piercings_breemc when breemc
        group mc_collars auto variant "breemc" if_any "breemc"

        group npc auto

        attribute morgan_makeup
        attribute aletta_glasses if_any "aletta"

        group outfits auto
        group outfits auto variant "pregnant" if_any "morgan_pregnant"

        attribute sasha_boobjob if_any "sasha"

        group collars auto

        group outfits auto variant "collarcover" if_any "morgan"
        group outfits auto variant "collarcover_pregnant" if_any "morgan_pregnant"

        group haircuts auto:
            attribute morgan_nohaircut null

        group pregnancies auto

        group amy_necktie auto if_any "amy"

        group multiple auto variant piercings

        group fx auto

        always:
            "love_boat_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
