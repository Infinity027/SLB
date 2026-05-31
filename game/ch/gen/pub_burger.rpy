init 1:
    layeredimage date pub burger:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, OutfitPicker, PregnancyPicker, HaircutPicker, MCCGPicker], use_morgan_cg_outfits=True, append_npc_from_attributes=True)

        attribute makeup null

        always:
            "date_pub_burger_bg"
        always:
            "date_pub_burger_bar"
        always:
            "date_pub_burger_stools_shadows"

        group leg auto

        always:
            "date_pub_burger_stools"

        group npc auto:
            attribute none default null

        group multiple auto variant piercings

        group pregnancies auto

        group outfit auto
        group outfit auto variant "pregnant" if_any ["morgan_pregnant", "reona_pregnant"]

        attribute sasha_boobjob

        group collars auto

        group haircuts auto

        group jacket auto
        group gun auto

        attribute morgan_makeup

        group mc auto

        group glasses auto

        always:
            "date_pub_burger_light"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
