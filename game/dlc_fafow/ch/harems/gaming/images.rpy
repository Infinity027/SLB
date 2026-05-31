init 1:
    layeredimage kat cunnilingus bree:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, PubesPicker, HaircutPicker], npcs=[bree, kat])


        attribute bree null
        attribute bree_ears null
        attribute bree_lips null
        attribute bree_tongue null
        attribute kat null
        attribute kat_clit null
        attribute kat_collar null
        attribute kat_ears null
        attribute kat_navel null
        attribute kat_nipples null
        attribute kat_nohaircut null
        attribute kat_nose null
        attribute kat_pregnant_navel null
        attribute kat_tongue null


        group bg auto:
            attribute bedroom default


        attribute fx variant pleasure when pleasure


        group head auto:
            attribute normal default
            attribute orgasm null


        group bree_hair_orgasm auto when orgasm


        attribute fx variant orgasm when orgasm


        attribute bree_nose variant normal when normal
        attribute bree_nose variant pleasure when pleasure


        attribute bree_collar variant normal when normal
        attribute bree_collar variant pleasure when pleasure
        attribute bree_collar variant orgasm when orgasm


        group bree_hair_normal auto when normal
        group bree_hair_pleasure auto when pleasure


        always "kat_cunnilingus_bree_bodies"


        attribute tongue


        attribute blush


        group kat_eyes auto:
            attribute open default


        attribute bree_pregnant


        group multiple auto variant bree_piercings


        attribute kat_pregnant


        group multiple auto variant kat_piercings


        attribute kat_pubes
        attribute bree_pubes


        attribute squirt


        always "kat_cunnilingus_bree_fg"

    layeredimage bree cunnilingus kat:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, HaircutPicker], npcs=[bree, kat])


        attribute bree null
        attribute kat null
        attribute kat_nohaircut null
        attribute bree_nohaircut null
        attribute bree_collar null
        attribute bree_clit null
        attribute bree_ears null
        attribute bree_lips null
        attribute bree_navel null
        attribute bree_pregnant_navel null
        attribute bree_nipples null
        attribute bree_nose null
        attribute bree_tongue null
        attribute kat_clit null
        attribute kat_ears null
        attribute kat_nipples null
        attribute kat_navel null
        attribute kat_pregnant_navel null
        attribute kat_tongue null


        group bg auto:
            attribute bedroom default

        attribute closeup


        always "bree_cunnilingus_kat_bodies"


        attribute bree_haircut


        attribute squirt


        always "bree_cunnilingus_kat_breeeyes"


        group multiple auto variant pregnancies


        group katmouths auto:
            attribute normal default


        attribute blush


        group kateyes auto:
            attribute lookfront default


        attribute kat_collar


        group multiple auto variant piercings


        attribute breath

    layeredimage kat bree ending:
        attribute_function MultiPickers([HaircutPicker, EndingKidPicker], npcs=[bree, kat])


        always "kat_bree_ending_bg"


        attribute kat
        attribute kat_nohaircut null


        attribute bree
        attribute bree_nohaircut when bree
        attribute bree_haircut when bree


        group multiple auto variant kids


        always "kat_bree_ending_fx"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
