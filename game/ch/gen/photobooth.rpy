init 1:
    layeredimage photobooth:
        attribute_function MultiPickers([MCCGPicker, HaircutPicker, CollarPicker,  OutfitPicker], add_simple_pregnant_attribute=True, append_npc_from_attributes=True)

        always:
            "photobooth_bg"

        group npc auto variant "mikemc" if_any ["mikemc"]
        group npc auto variant "breemc" if_any ["breemc"]


        attribute mc_casual null
        attribute mc_innocentcasual null
        group breemc_outfit auto variant "casual" if_all ["breemc", "mc_casual"]
        group breemc_outfit auto variant "innocentcasual" if_all ["breemc", "mc_innocentcasual"]


        attribute mc_haircut null
        attribute mc_nohaircut null
        group breemc_haircut auto if_all ["breemc", "mc_haircut"]

        attribute mc_ears null
        attribute mc_lips null
        attribute mc_nose null
        attribute morgan_makeup

        group collars auto

        group glasses auto

        group bb auto

        group hair auto if_any ["sasha"]

        group hair auto if_not ["sasha"]

        group hair_casual auto if_all ["reona_casual"]
        group hair_purecasual auto if_all ["reona_purecasual"]

        group glasses_casual auto if_all ["reona_casual"]
        group glasses_purecasual auto if_all ["reona_purecasual"]


        always:
            "photobooth_borders"
