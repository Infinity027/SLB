init python:
    class CGHauntedHousePicker(object):
        def __call__(self, attr):
            if attr & {"bree", "audrey", "angela", "anna", "amy", "alexis", "aletta", "danny", "scottie", "mike", "kiara"}:
                attr.add("01")
            elif attr & {"kleio", "kat", "harmony", "hanna", "emma", "cassidy", "camila", "jack", "shawn", "dwayne", "cherie"}:
                attr.add("02")
            elif attr & {"samantha", "sasha", "shiori", "reona", "palla", "morgan", "minami", "lexi", "lavish", "master", "ryan", "victor", "claire"}:
                attr.add("03")
            
            if enable_debug_picker:
                renpy.log(f"CGHauntedHousePicker results: {attr}")
            return attr

init 1:
    layeredimage haunted house:
        attribute_function MultiPickers([PregnancyPicker, PiercingsPicker, HaircutPicker, CollarPicker, OutfitPicker, MCCGPicker, CGHauntedHousePicker], append_npc_from_attributes=True, use_morgan_cg_outfits=True)

        group bg auto

        group mc_dicks auto:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null


        group mcbody auto variant "01" if_all "01" if_any ["mikemc", "breemc"]


        group mcbody auto variant "02" if_all ["mikemc", "02"]
        group mcbody auto variant "03" if_all ["mikemc", "03"]


        group mikemc_outfits auto variant "01" if_all ["mikemc", "01"]
        group mikemc_outfits auto variant "02" if_all ["mikemc", "02"]
        group mikemc_outfits auto variant "03" if_all ["mikemc", "03"]


        group breemc_outfits auto variant "01" if_all ["breemc", "01"]

        attribute mc_pregnant null
        group breemc_pregnant_outfits auto variant "01" if_all ["mc_pregnant", "breemc", "01"]
        group multiple auto variant mc_piercings_01 when breemc and 01
        group mc_haircuts auto variant "01" if_all ["breemc", "01"]

        attribute mc_nohaircut null

        group npc auto

        attribute morgan_makeup
        group glasses auto

        group multiple auto variant piercings

        group outfits auto
        group outfits auto variant "pregnant" if_any ["morgan_pregnant", "reona_pregnant"]

        attribute sasha_boobjob if_any "sasha"

        group haircuts auto:
            attribute morgan_nohaircut null

        group pregnancies auto

        group outfits_front auto

        group amy_necktie auto if_any "amy"

        group collars auto

        group outfits auto variant "collarcover" if_any "morgan"
        group outfits auto variant "collarcover_pregnant" if_any "morgan_pregnant"



        group mcbody auto variant "02" if_all ["breemc", "02"]
        group mcbody auto variant "03" if_all ["breemc", "03"]
        group breemc_outfits auto variant "02" if_all ["breemc", "02"]
        group breemc_outfits auto variant "03" if_all ["breemc", "03"]
        group breemc_pregnant_outfits auto variant "02" if_all ["mc_pregnant", "breemc", "02"]
        group breemc_pregnant_outfits auto variant "03" if_all ["mc_pregnant", "breemc", "03"]
        group multiple auto variant mc_piercings_02 when breemc and 02
        group multiple auto variant mc_piercings_03 when breemc and 03
        group mc_haircuts auto variant "02" if_all ["breemc", "02"]
        group mc_haircuts auto variant "03" if_all ["breemc", "03"]

        group fx auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
