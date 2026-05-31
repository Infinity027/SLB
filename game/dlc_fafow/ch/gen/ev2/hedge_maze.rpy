init 1:
    layeredimage hedge maze:
        attribute_function MultiPickers([PregnancyPicker, PiercingsPicker, HaircutPicker, CollarPicker, OutfitPicker, MCCGPicker, DayNightPicker], append_npc_from_attributes=True, use_morgan_cg_outfits=True)

        always:
            "hedge_maze_bg"


        group mc_dicks auto:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null
        attribute day null
        attribute morgan_clit null
        attribute morgan_nipples null
        attribute morgan_tongue null
        attribute morgan_pregnant null


        group mcbody auto


        group mc_haircuts auto variant "breemc" if_any "breemc"
        group mc_outfits auto variant "mikemc" if_any "mikemc"
        group mc_outfits auto variant "breemc" if_any "breemc"

        attribute mc_pregnant null
        group mc_outfits auto variant "mc_pregnant" if_all ["breemc", "mc_pregnant"]

        group multiple auto variant mc_piercings_breemc when breemc
        group mc_collars auto variant "breemc" if_any "breemc"


        group npc auto

        attribute morgan_makeup
        attribute aletta_glasses if_any "aletta"

        group outfits auto variant "nakedbelly" if_any ["morgan", "aletta", "amy", "audrey", "cassidy", "kleio", "lexi", "reona", "samantha"]
        group outfits auto variant "nakedbelly_pregnant" if_any ["morgan_pregnant", "aletta_pregnant", "amy_pregnant", "audrey_pregnant", "cassidy_pregnant", "kleio_pregnant", "lexi_pregnant", "reona_pregnant", "samantha_pregnant"]

        group multiple auto variant piercings

        group outfits auto
        group outfits auto variant "pregnant" if_any "morgan_pregnant"

        attribute sasha_boobjob if_any "sasha"

        always:
            "hedge_maze_npc_bree_fx" if_any "bree"

        group collars auto

        group haircuts auto:
            attribute morgan_nohaircut null

        group pregnancies auto

        group amy_necktie auto if_any "amy"


        group outfits auto variant "collarcover" if_any "morgan"
        group outfits auto variant "collarcover_pregnant" if_any "morgan_pregnant"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
