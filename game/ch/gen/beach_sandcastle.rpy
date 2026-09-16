init python:
    class CG_BeachSandCastle_Picker(object):
        def __call__(self, attr):
            if hero.is_male:
                if attr & {"angela", "anna", "bree", "emma", "hanna", "kleio", "lavish", "samantha", "shiori", "minami", "master", "dwayne", "victor", "danny", "ryan", "shawn", "jack", "scottie", "mike", "reona", "kat", "amy"}:
                    attr.add("01")
                    attr.discard("02")
                elif attr & {"aletta", "alexis", "audrey", "cassidy", "harmony", "lexi", "palla", "sasha", "morgan", "camila", "cherie", "claire", "kiara"}:
                    attr.add("02")
                    attr.discard("01")
                
                
                if 'kleio' in attr and 'pregnant' in attr:
                    attr.remove('kleio')
                    attr.add('kleiopreg')
            
            else:
                if attr & {"lexi", "sasha"}:
                    attr.add("02")
                    attr.discard("01")
                else:
                    attr.add("01")
                    attr.discard("02")
            
            if enable_debug_picker:
                renpy.log(f"CG_BeachSandCastle_Picker results: {attr}")
            return attr

init 1:
    layeredimage beach sandcastle:
        attribute_function MultiPickers([PubesPicker, CollarPicker, HaircutPicker, OutfitPicker,  MCCGPicker, CG_BeachSandCastle_Picker], add_simple_pregnant_attribute=True, add_simple_outfit_attribute=True, append_npc_from_attributes=True, use_morgan_cg_outfits=True)


        group bg auto

        attribute alonemc null
        group npc auto if_not ["alonemc"]
        group npc auto variant "nopregnant" if_not ["alonemc", "pregnant"]
        group npc auto variant "pregnant" if_all "pregnant" if_not ["alonemc"]

        group pubes auto if_any ["pubes"] if_not ["alonemc"]:
            attribute emma_pubes null

        attribute breemc null
        group breemc_position auto:
            attribute left null
            attribute right null
        group breemc auto variant "left" if_all ["breemc", "left"]
        group breemc auto variant "right" if_all ["breemc", "right"]

        group mchaircuts auto variant "breemc_left_01" if_all ["breemc", "01", "left"]:
            attribute mc_nohaircut null

        group mcoutfits auto variant "breemc_left_01" if_all ["breemc", "01", "left"] if_not ["mc_pregnant", "mc_naked"]
        group mcoutfits auto variant "breemc_left_01_pregnant" if_all ["breemc", "mc_pregnant", "01", "left"] if_not ["mc_naked"]
        group mccollars auto variant "breemc_left_01" if_all ["breemc", "mc_collar", "01", "left"]
  
        group mchaircuts auto variant "breemc_right_01" if_all ["breemc", "01", "right"]:
            attribute mc_nohaircut null
        group mcoutfits auto variant "breemc_right_01" if_all ["breemc", "01", "right"] if_not ["mc_pregnant", "mc_naked"]
        group mcoutfits auto variant "breemc_right_01_pregnant" if_all ["breemc", "mc_pregnant", "01", "right"] if_not ["mc_naked"]
        group mccollars auto variant "breemc_right_01" if_all ["breemc", "mc_collar", "01", "right"]

        group haircuts auto if_not ["alonemc"]:
            attribute emma_nohaircut null

        attribute pregnant null
        group pregnancies auto if_all ["pregnant", "naked"] if_not ["alonemc"]


        group boobjobs auto if_not ["alonemc"]:
            attribute sasha_noboobjob null

        group outfits auto if_not ["alonemc", "naked"]

        group outfits auto variant "pregnant" if_any "pregnant" if_not ["alonemc", "naked"]

        group outfits auto variant "nopregnant" if_not ["alonemc", "pregnant", "naked"]

        group outfits auto variant "noboobjob" if_any "sasha_noboobjob" if_not ["alonemc", "naked"]
        group outfits auto variant "boobjob" if_any "sasha_boobjob" if_not ["alonemc", "naked"]
        group outfits auto variant "pregnant_noboobjob" if_all ["sasha_noboobjob", "sasha_pregnant"] if_not ["alonemc", "naked"]
        group outfits auto variant "pregnant_boobjob" if_all ["sasha_boobjob", "sasha_pregnant"] if_not ["alonemc", "naked"]


        attribute swimsuit null
        attribute sexyswimsuit null

        group dicks auto

        group collars auto if_not ["alonemc"]

        attribute morgan_makeup

        group castle auto

        attribute mikemc null
        group mikemc auto if_any ["mikemc"]


        attribute mc_naked null
        group mcoutfits auto variant "mikemc_01" if_all ["mikemc", "01"]
        group mcoutfits auto variant "mikemc_01_mc_naked" if_all ["mikemc", "01", "mc_naked"]
        group mcoutfits auto variant "mikemc_02" if_all ["mikemc", "02"]


        group breemc auto if_any ["breemc"]
        group mchaircuts auto variant "breemc_02" if_all ["breemc", "02"]:
            attribute mc_nohaircut null
        group mcpregnant auto variant "breemc_02" if_all ["breemc", "mc_pregnant", "mc_naked", "02"]
        group mcoutfits auto variant "breemc_02" if_all ["breemc", "02"] if_not ["mc_pregnant", "mc_naked"]
        group mcoutfits auto variant "breemc_02_pregnant" if_all ["breemc", "mc_pregnant", "02"] if_not ["mc_naked"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
