init python:
    class CG_BeachIceCream_Picker(object):
        def __call__(self, attr):
            if "mikemc" in attr:
                if {"harmony"} & attr:
                    attr.discard("01")
                    attr.add("02")
                else:
                    attr.discard("02")
                    attr.add("01")
            elif "breemc" in attr:
                if {"angela", "lexi", "sasha"} & attr:
                    attr.discard("01")
                    attr.add("02")
                else:
                    attr.discard("02")
                    attr.add("01")
            if enable_debug_picker:
                renpy.log(f"CG_BeachIceCream_Picker results: {attr}")
            return attr

init 1:
    layeredimage beach icecream:
        attribute_function Pickers([PubesPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, CollarPicker, OutfitPicker, MCCGPicker, CG_BeachIceCream_Picker],clear_npc=True,piercings_prefix=True)

        attribute nomc null
        attribute naked null


        attribute waterpark "beach_icecream_bg_waterpark"
        always "beach_icecream_bg" if_not ["waterpark"]
        always "beach_icecream_seller" if_not ["waterpark"]
        always "beach_icecream_seller_outfit" if_not ["waterpark", "naked"]


        attribute mikemc null
        group mikemc auto if_any ["mikemc"] if_not ["nomc"]
        attribute breemc null
        group breemc auto if_any ["breemc"] if_not ["nomc"]


        attribute mc_naked null

        group outfit auto variant "mikemc_01" if_all ["mikemc", "01"] if_not ["mc_naked", "nomc"]
        group outfit auto variant "mikemc_02" if_all ["mikemc", "02"] if_not ["mc_naked", "nomc"]
        group outfit auto variant "mikemc_01_naked" if_all ["mikemc", "01", "mc_naked"] if_not ["nomc"]
        group outfit auto variant "mikemc_02_naked" if_all ["mikemc", "02", "mc_naked"] if_not ["nomc"]

        group outfit auto variant "breemc_01" if_all ["breemc", "01"] if_not ["mc_naked", "nomc"]
        group outfit auto variant "breemc_02" if_all ["breemc", "02"] if_not ["mc_naked", "nomc"]
        group outfit auto variant "breemc_01_naked" if_all ["breemc", "01", "mc_naked"] if_not ["nomc"]
        group outfit auto variant "breemc_02_naked" if_all ["breemc", "02", "mc_naked"] if_not ["nomc"]
        group outfit auto variant "breemc_01_pregnant" if_all ["breemc", "01", "mc_pregnant"] if_not ["mc_naked", "nomc"]
        group outfit auto variant "breemc_02_pregnant" if_all ["breemc", "02", "mc_pregnant"] if_not ["mc_naked", "nomc"]
        group mc_haircuts auto variant "breemc_01" if_all ["breemc", "01"] if_not ["nomc"]
        group mc_haircuts auto variant "breemc_02" if_all ["breemc", "02"] if_not ["nomc"]


        group girl auto

        attribute pubes null
        group pubes auto if_any "pubes"

        attribute armpits null
        group armpits auto if_any "armpits"


        attribute haircut null
        attribute nohaircut null
        group haircut auto when haircut
        group nohaircut auto when nohaircut and not (cherie and swimsuit)

        group hat_cherie auto when cherie and nohaircut


        attribute boobjob null
        group bb auto if_any ["boobjob"]


        attribute collar null
        group collar auto if_any ["collar"]
        group collar auto variant "breemc" if_all ["breemc", "mc_collar"] if_not ["nomc"]


        attribute swimsuit null default
        attribute sexyswimsuit null
        group swimsuit auto if_not ["sexyswimsuit", "naked", "pregnant", "boobjob"]
        group sexyswimsuit auto if_any ["sexyswimsuit"] if_not ["naked", "pregnant", "boobjob"]


        group swimsuit auto variant "pregnant" if_any ["pregnant"] if_not ["sexyswimsuit", "naked", "boobjob"]
        group sexyswimsuit auto variant "pregnant" if_all ["sexyswimsuit", "pregnant"] if_not ["naked", "boobjob"]


        group swimsuit auto variant "bb" if_any ["boobjob"] if_not ["pregnant", "sexyswimsuit", "naked"]
        group sexyswimsuit auto variant "bb" if_all ["sexyswimsuit", "boobjob"] if_not ["pregnant", "naked"]


        group swimsuit auto variant "pregnant_bb" if_all ["boobjob", "pregnant"] if_not ["sexyswimsuit", "naked"]
        group sexyswimsuit auto variant "pregnant_bb" if_all ["sexyswimsuit", "boobjob", "pregnant"] if_not ["naked"]


        attribute bluebikinitop null
        attribute redbluebikinitop null
        group outfit auto variant "morgan" if_any ["morgan"] if_not ["naked", "pregnant"]
        group outfit auto variant "morgan_pregnant" if_all ["morgan", "pregnant"] if_not "naked"


        group normal auto if_not ["naked"]
        group naked auto if_any ["naked"]
        group naked auto variant "big" if_all ["naked", "big"]
        group naked auto variant "medium" if_all ["naked", "medium"]
        group naked auto variant "small" if_all ["naked", "small"]


        group ice auto


        attribute pregnant null
        group pregnant auto if_all ["naked","pregnant"]
        group pregnant auto variant "breemc" if_all ["breemc", "naked","mc_pregnant"] if_not ["nomc"]


        group multiple auto variant piercings
        group multiple auto variant piercings_naked when naked
        group multiple auto variant piercings_notswimsuit when not swimsuit
        group multiple auto variant piercings_notsexyswimsuit when not sexyswimsuit
        group multiple auto variant piercings_notblueblackswimsuit when not blueblackswimsuit
        group multiple auto variant piercings_breemc when not nomc
        group multiple auto variant piercings_naked_breemc when breemc and naked and not nomc


        attribute glasses null
        group glasses auto if_any ["glasses"]


        attribute makeup null
        group makeup auto if_any ["makeup"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
