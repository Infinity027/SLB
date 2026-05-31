init 1:
    layeredimage bree peeping:
        attribute_function MultiPickers([MCCGPicker, DayNightPicker, HaircutPicker, CollarPicker, PiercingsPicker, OutfitPicker], append_npc_from_attributes=True)

        attribute cum null
        attribute down null
        attribute npc_topless null
        attribute npc_bottomless null
        attribute mc_topless null
        attribute mc_bottomless null

        group bg auto variant "day" if_any ["day"]:
            attribute livingroom default
        group bg auto variant "night" if_any ["night"]:
            attribute livingroom default


        group npc auto
        group npc_top_outfit auto if_not ["npc_topless"]
        group npc_dick auto
        group npc_cum auto if_any ["cum"]
        group npc_bot_outfit auto if_not ["npc_bottomless"]


        attribute breemc
        attribute mc_haircut
        attribute mc_pubes
        always "bree_peeping_upperarms"
        group mc_exp auto:
            attribute surprised default
        group mc_bot auto if_not ["down", "mc_bottomless"]
        group mc_bot auto variant "down" if_any ["down"] if_not ["mc_bottomless"]
        group mc_top auto if_not ["mc_topless"]
        group mc_rightarm auto:
            attribute normal default
        group mc_rightarm auto variant "outfit" if_any ["mc_casual"] if_not ["mc_topless"]:
            attribute normal default
        always "bree_peeping_mc_leftarm"
        always "bree_peeping_mc_leftarm_outfit_casual" if_any ["mc_casual"] if_not ["mc_topless"]
        attribute mc_collar
        attribute mc_ears
        attribute mc_lips
        attribute mc_tongue
        attribute mc_nose
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
