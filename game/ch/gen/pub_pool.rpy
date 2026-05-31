init 1:
    layeredimage pool:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, OutfitPicker, PregnancyPicker, HaircutPicker, MCCGPicker], use_morgan_cg_outfits=True, append_npc_from_attributes=True)

        attribute shiori null
        attribute makeup null

        always:
            "pool_bg"

        group npc auto:
            attribute none default null
        group npc auto variant "breemc" if_any "breemc":
            attribute none default null
        group npc auto variant "mikemc" if_any "mikemc":
            attribute none default null

        attribute sasha_boobjob

        group haircuts auto

        group multiple auto variant piercings

        group pregnancies auto

        attribute morgan_makeup

        group outfit auto
        group outfit auto variant "pregnant" if_any "morgan_pregnant"

        group collars auto if_not ["bluesweater_morgan"]
        group queue auto
        group gun auto

        group mc auto if_not "shiori"

        group glasses auto

        always:
            "pool_balls"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
