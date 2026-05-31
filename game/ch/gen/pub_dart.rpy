init 1:
    layeredimage date pub dart:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, OutfitPicker, PregnancyPicker, HaircutPicker, MCCGPicker], use_morgan_cg_outfits=True, append_npc_from_attributes=True)

        attribute makeup null

        always:
            "date_pub_dart_bg"

        group npc auto:
            attribute none default null

        group pregnancies auto

        group outfit auto
        group outfit auto variant "pregnant" if_any ["morgan_pregnant", "reona_pregnant", "kiara_pregnant", "claire_pregnant", "cherie_pregnant"]

        group haircuts auto

        group line auto
        attribute sasha_boobjob

        group collars auto if_not ["bluesweater_morgan"]
        attribute morgan_makeup
        group gun auto

        group multiple auto variant piercings

        group glasses auto

        group darts auto

        group fx auto:
            attribute nodart null

        group mc auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
