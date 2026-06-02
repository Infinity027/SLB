init python:
    class CG_Swimming_Picker(object):
        def __call__(self, attr):
            for a in attr:
                g = Person.find(a)
                if g is not None:
                    break
            if g:
                if g.id in ["bree", "camila", "aletta", "anna", "hanna", "cassidy", "victor", "scottie", "reona"]:
                    attr.add("01")
                elif g.id in ["harmony", "angela", "alexis", "kleio", "shiori", "mike", "shawn", "cherie", "claire", "kiara"]:
                    attr.add("02")
                elif g.id in ["palla", "ayesha", "audrey", "minami", "lexi", "danny", "jack", "kat"]:
                    attr.add("03")
                elif g.id in ["morgan", "samantha", "lavish", "emma", "sasha", "ryan", "master", "dwayne", "amy"]:
                    attr.add("04")
            
            if enable_debug_picker:
                renpy.log(f"CG_Swimming_Picker results: {attr}")
            return attr

init 1:
    layeredimage swimmingrace:
        attribute_function Pickers([CG_Swimming_Picker, PregnancyPicker, CollarPicker, HaircutPicker, OutfitPicker, PiercingsPicker, PubesPicker, MCCGPicker], clear_npc=True, use_morgan_cg_outfits=True)


        group bg auto


        attribute nomc null
        group mikemc auto if_all ["mikemc"] if_not "nomc"
        group breemc auto if_all ["breemc"] if_not "nomc"


        attribute mc_naked null
        attribute mc_swimsuit null
        attribute mc_sexyswimsuit null
        group outfit auto variant "mikemc_naked_01" if_all ["mikemc", "01", "mc_naked"] if_not "nomc"
        group outfit auto variant "mikemc_normal" if_all ["mikemc", "mc_swimsuit"] if_not ["mc_naked", "nomc"]
        group outfit auto variant "breemc_normal" if_all ["breemc", "mc_swimsuit"] if_not ["mc_naked", "nomc"]
        group outfit auto variant "breemc_sexy" if_all ["breemc", "mc_sexyswimsuit"] if_not ["mc_naked", "nomc"]


        group water auto variant "mikemc" if_all ["mikemc"] if_not "nomc"
        group water auto variant "breemc" if_all ["breemc"] if_not "nomc"
        group water auto variant "fg_mikemc" if_all ["mikemc"] if_not "nomc"
        group water auto variant "fg_breemc" if_all ["breemc"] if_not "nomc"


        group girl auto


        attribute pubes null
        group pubes auto if_all ["pubes"]


        attribute pregnant null
        group pregnant auto if_all ["pregnant"]


        attribute makeup null
        group makeup auto if_any ["makeup"]


        attribute boobjob null
        group boobjob auto if_any ["boobjob"]


        attribute collar null
        group collar auto if_any ["collar"]



        attribute lips null
        group lips auto if_any ["lips"]

        attribute tongue null
        group tongue auto if_any ["tongue"]

        attribute nipples null
        group nipples auto if_any ["nipples"] if_not ["boobjob", "shiori"]
        group nipples_bb auto if_all ["nipples", "boobjob"]

        attribute nose null
        group nose auto if_any ["nose"]

        attribute ears null
        group ears auto if_any ["ears"]

        attribute clit null
        group clit auto if_any ["clit"]

        attribute navel null
        attribute pregnant_navel null
        group navel auto if_any ["navel"]
        group pregnant_navel auto if_any ["pregnant_navel"]

        attribute eyebrow null
        group eyebrow auto if_any ["eyebrow"]


        attribute swimsuit null
        attribute sexyswimsuit null
        group swimsuit auto if_all ["swimsuit"] if_not ["pregnant", "naked", "boobjob"]
        group swimsuit auto variant "pregnant" if_all ["swimsuit", "pregnant"] if_not ["naked", "boobjob"]
        group swimsuit auto variant "bb" if_all ["swimsuit", "boobjob"] if_not ["pregnant", "naked"]
        group swimsuit auto variant "bb_pregnant" if_all ["swimsuit", "boobjob", "pregnant"] if_not ["naked"]
        group sexyswimsuit auto if_all ["sexyswimsuit"] if_not ["pregnant", "naked", "boobjob"]
        group sexyswimsuit auto variant "pregnant" if_all ["sexyswimsuit", "pregnant"] if_not ["naked", "boobjob"]
        group sexyswimsuit auto variant "bb" if_all ["sexyswimsuit", "boobjob"] if_not ["pregnant", "naked"]
        group sexyswimsuit auto variant "bb_pregnant" if_all ["sexyswimsuit", "boobjob", "pregnant"] if_not ["naked"]


        group outfit auto if_not ["pregnant"]
        group outfit auto variant "pregnant" if_all ["pregnant"]


        attribute haircut null
        attribute nohaircut null
        group haircut auto if_all ["haircut"] if_not ["02"]
        group nohaircut auto if_all ["nohaircut"] if_not ["02"]


        group water auto
        group water_fg auto


        group haircut auto if_all ["haircut", "02"]
        group nohaircut auto if_all ["nohaircut", "02"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
