init 1:
    layeredimage victor kiss:
        attribute_function Pickers([OutfitPicker, MCCGPicker], npc=victor)

        attribute breemc null
        attribute mc_collar null
        attribute mc_pregnant null
        attribute mc_pubes null


        always "victor_kiss_bodies" if_not ["bowsette"]
        attribute bowsette "victor_kiss_bodies_bowsette"

        group multiple auto variant piercings
        group multiple:
            attribute mc_clit null
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_nipples null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_tongue null

        attribute mc_nohaircut null
        attribute mc_haircut if_not ["bowsette"]

        attribute naked null
        attribute topless null


        group outfits auto if_not ["naked", "topless"]:
            attribute sleep null
            attribute sport null
            attribute swimsuit null
            attribute towel null
            attribute underwear null
            attribute casual default
            attribute chinese "victor_kiss_outfits_casual"
            attribute bowsette "victor_kiss_outfits_casual"
            attribute invisible "victor_kiss_outfits_casual"


        group mcoutfits auto if_not ["naked", "topless"]


    layeredimage victor beats:
        attribute_function MultiPickers([MCCGPicker, OutfitPicker], npcs=[victor], append_npc_from_attributes=True)

        attribute nomc null
        attribute naked null


        attribute breemc if_not ["nomc"]
        attribute mc_haircut if_not ["nomc"]
        attribute mc_pregnant if_not ["nomc"]
        group multiple auto variant mc_piercings when not nomc
        group mc_outfit auto if_not ["nomc", "naked"]
        group mc_pregnant_outfit auto if_any ["mc_pregnant"] if_not ["nomc", "naked"]
        attribute mc_collar if_not ["nomc"]


        group foe auto
        group foe_naked auto if_any ["naked"]
        group foe_outfit auto if_not ["naked"]


        always "victor_beats_victor"
        group outfit auto if_not ["naked"]

        always "victor_beats_fx"

    layeredimage victor standing:
        attribute_function Pickers([MCCGPicker], npc=victor)
        attribute breemc null
        attribute mc_casual null

        group bg auto:
            attribute bedroom default

        always:
            "victor_standing_bodies"

        attribute mc_pubes
        attribute mc_pregnant
        attribute mc_collar

        group multiple auto variant piercings
        group multiple:
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_tongue null

        group piercings auto variant "out" if_not "vaginal"
        group dick auto:
            attribute out default

        group piercings auto variant "vaginal" if_any "vaginal"

        attribute condom null
        group condom auto if_any "condom"

        attribute creampie null
        group creampie auto if_any "creampie" if_not "condom"

        attribute cumshot if_any "out" if_not "condom"

        attribute cum null
        group cum auto if_any "cum" if_not "condom"

        group mouth auto:
            attribute normal default

        group eyes auto:
            attribute down default

        group haircuts auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
