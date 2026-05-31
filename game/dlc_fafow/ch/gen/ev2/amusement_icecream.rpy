init python:
    class CGAmusementIceCreamPicker(object):
        def __call__(self, attr):
            
            if "mikemc" in attr and not {"01", "02"} & attr:
                for a in attr:
                    g = Person.find(a)
                    if g is not None:
                        break
                if g:
                    if g.id in ["harmony"]:
                        attr.add("02")
                    else:
                        attr.add("01")
            elif "breemc" in attr:
                if {"angela", "ayesha", "kylie", "lexi", "sasha"} & attr:
                    attr.discard("01")
                    attr.add("02")
                else:
                    attr.discard("02")
                    attr.add("01")
            if enable_debug_picker:
                renpy.log(f"CG_AmusementIceCream_Picker results: {attr}")
            return attr

init 1:
    layeredimage amusement icecream:
        attribute_function MultiPickers([PregnancyPicker, PiercingsPicker, HaircutPicker, CollarPicker, OutfitPicker, MCCGPicker, DayNightPicker, SeasonPicker, CGAmusementIceCreamPicker], append_npc_from_attributes=True, use_morgan_cg_outfits=True)

        attribute nomc null

        group mc_dicks auto:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null

        attribute day null
        attribute night null
        group bg auto variant "day" if_any "day"
        group bg auto variant "night" if_any "night"


        group npc auto

        attribute morgan_makeup
        attribute aletta_glasses if_any "aletta"

        group collars_back auto

        group outfits auto

        attribute sasha_boobjob if_any "sasha"

        group haircuts auto:
            attribute morgan_nohaircut null

        group pregnancies auto

        group multiple auto variant piercings

        group outfits auto variant "pregnant" if_any ["morgan_pregnant", "reona_pregnant"]

        group amy_necktie auto if_any "amy"

        group collars_fore auto

        group piercings auto variant "morgan_navel" if_any "morgan_navel"
        group piercings auto variant "morgan_pregnant_navel" if_any "morgan_pregnant_navel"

        group ice auto

        attribute mikemc null
        group mikemc auto if_any ["mikemc"] if_not ["nomc"]

        group mc_outfits auto variant "mikemc_01" if_all ["mikemc", "01"] if_not ["nomc"]
        group mc_outfits auto variant "mikemc_02" if_all ["mikemc", "02"] if_not ["nomc"]

        attribute breemc null
        group breemc auto if_any ["breemc"] if_not ["nomc"]

        group mc_haircuts auto variant "breemc_01" if_all ["breemc", "01"] if_not ["nomc"]:
            attribute mc_nohaircut null
        group mc_outfits auto variant "breemc_01" if_all ["breemc", "01"] if_not ["nomc"]
        group multiple auto variant mc_piercings_breemc_01 when breemc and 01 and not nomc
        group mc_collars auto variant "breemc_01" if_all ["breemc", "01"] if_not ["nomc"]

        group mc_haircuts auto variant "breemc_02" if_all ["breemc", "02"] if_not ["nomc"]:
            attribute mc_nohaircut null
        group mc_outfits auto variant "breemc_02" if_all ["breemc", "02"] if_not ["nomc"]
        group multiple auto variant mc_piercings_breemc_02 when breemc and 02 and not nomc
        group mc_collars auto variant "breemc_02" if_all ["breemc", "02"] if_not ["nomc"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
