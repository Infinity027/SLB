init 1:
    layeredimage photobooth:
        attribute_function MultiPickers([MCCGPicker, HaircutPicker, CollarPicker, PregnancyPicker, PiercingsPicker, OutfitPicker], add_simple_pregnant_attribute=True, append_npc_from_attributes=True)


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
        group breemc_piercings auto variant "ears" if_all ["breemc", "mc_ears"]
        group breemc_piercings auto variant "lips" if_all ["breemc", "mc_lips"]
        group breemc_piercings auto variant "nose" if_all ["breemc", "mc_nose"]


        attribute morgan_makeup


        group pregnancy auto
        group pregnancy_casual auto if_all ["reona_casual", "reona_pregnant"]
        group pregnancy_purecasual auto if_all ["reona_purecasual", "reona_pregnant"]


        group bot auto if_not ["pregnant"]
        group bot auto variant "pregnant" if_any ["pregnant"]
        group top auto if_not ["pregnant"]
        group top auto variant "pregnant" if_any ["pregnant"]


        group collars auto


        group glasses auto



        group bb auto


        group hair auto if_any ["sasha"]


        group multiple auto variant piercings
        group multiple auto variant piercings_hidden when not reona_purecasual
        group multiple auto variant piercings_nav when not (morgan_blackjacket or morgan_bluesweater or morgan_dotdress)


        group hair auto if_not ["sasha"]

        group hair_casual auto if_all ["reona_casual"]
        group hair_purecasual auto if_all ["reona_purecasual"]

        group glasses_casual auto if_all ["reona_casual"]
        group glasses_purecasual auto if_all ["reona_purecasual"]


        always:
            "photobooth_borders"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
