init 1:
    layeredimage sasha female foreplay:
        attribute_function MultiPickers([HaircutPicker, OutfitPicker, PubesPicker], npcs=[bree, sasha], add_simple_outfit_attribute=True)


        group bg auto:
            attribute beach default


        attribute bree null
        attribute sasha null
        group bodies auto
        group sashabody auto variant "beach" if_any ["beach"]
        group sashabody auto variant "bedroom" if_any ["bedroom"]


        attribute bree_pubes
        attribute sasha_pubes null


        attribute naked null
        attribute casual null

        attribute bree_casual null
        group breeoutfit auto if_not ["naked"]

        attribute sasha_casual null
        attribute sasha_boobjob null
        group sashaoutfit auto variant "boobjob" if_any ["sasha_boobjob"]:
            attribute sasha_naked null
        attribute sasha_noboobjob null
        group sashaoutfit auto variant "noboobjob" if_not ["sasha_boobjob"]:
            attribute sasha_naked null


        attribute bree_haircut null
        attribute bree_nohaircut null
        attribute sasha_haircut null
        attribute sasha_nohaircut


        group fg auto

    layeredimage sasha female ending:
        attribute_function Pickers([MCCGPicker, HaircutPicker, EndingKidPicker], npc=sasha)

        attribute mc_nohaircut null
        attribute boobjob null
        attribute noboobjob null
        attribute mc_casual null
        attribute mc_pregnant null
        attribute mc_ears null

        always "sasha_female_ending_bg"

        always "sasha_female_ending_sasha_body"


        group hairs auto:
            attribute nohaircut default

        always "sasha_female_ending_sasha_face"

        attribute breemc
        attribute mc_haircut
        always "sasha_female_ending_bottle" if_not ["mc_pregnant", "black"]


        group kid auto if_any ["mc_pregnant"]:
            attribute white null default
            attribute black
            attribute redhead

        group kid auto variant "white" if_all ["mc_pregnant", "white"]:
            attribute blonde default
            attribute dark

        always "sasha_female_ending_fg_objects"
        always "sasha_female_ending_fg_shadow"

    layeredimage sasha fingering:
        attribute_function Pickers([HaircutPicker, OutfitPicker, PiercingsPicker, PregnancyPicker, MCCGPicker], npc=sasha)

        attribute breemc null
        attribute casual null
        attribute mc_casual null
        attribute mc_collar null

        group bg auto:
            attribute bedroom4 default

        always "sasha_fingering_bodies"

        attribute mc_pubes

        group mc_haircuts auto:
            attribute mc_nohaircut null

        group sasha_haircuts auto
        group wig auto

        group sasha_exp auto:
            attribute sashanormal default

        group mc_exp auto:
            attribute breenormal default

        attribute noboobjob null
        attribute boobjob

        attribute mc_pregnant
        attribute pregnant

        group multiple auto variant mc_piercings
        group multiple:
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_nose null
            attribute mc_navel null
            attribute mc_pregnant_navel null

        attribute sasha_arm
        group arm_outfit auto if_any "sasha_arm"

        group mc_bot auto
        group mc_top auto if_not "mc_pregnant"
        group mc_top auto if_any "mc_pregnant"
        group mc_hat auto

        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute nipples null

        group outfit auto
        group outfit auto variant "pregnant" if_any "pregnant"
        group outfit auto variant "boobjob" if_any "boobjob"

        attribute squirt

        always "sasha_fingering_fx"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
