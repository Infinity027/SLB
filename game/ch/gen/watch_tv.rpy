init python:
    class CG_WatchDateTV_Picker(object):
        def __call__(self, attr):
            for a in attr:
                g = Person.find(a)
                if g is not None:
                    break
            if g:
                if g.id in ["bree", "sasha", "aletta", "audrey", "samantha", "minami", "shiori", "lexi", "mike", "jack", "kat", "claire"]:
                    attr.add("01")
                elif g.id in ["emma", "anna", "hanna", "scottie", "danny", "reona", "cherie"]:
                    attr.add("02")
                elif g.id in ["palla", "lavish", "morgan", "alexis", "camila", "cassidy", "shawn", "victor", "kiara"]:
                    attr.add("03")
                elif g.id in ["harmony", "angela", "kleio", "master", "ryan", "dwayne", "amy"]:
                    attr.add("04")
            
            if enable_debug_picker:
                renpy.log(f"CG_WatchDateTV_Picker results: {attr}")
            return attr

init 1:
    layeredimage watch tv:
        attribute_function MultiPickers([DayNightPicker, CollarPicker, PiercingsPicker, OutfitPicker, PregnancyPicker, HaircutPicker, MCCGPicker], append_npc_from_attributes=True)

        attribute naked null
        attribute nopopcorn null


        always "watch_tv_out"
        group period auto
        always "watch_tv_in"


        attribute breemc

        attribute mc_pregnant if_all ["mc_naked"] if_any ["breemc"]

        attribute mc_collar if_any ["breemc"]

        group multiple auto variant breemc_piercings when breemc
        group multiple:
            attribute mc_clit null
            attribute mc_ears null

        attribute mc_nohaircut null

        attribute mc_naked null
        group breemc_outfit auto if_any ["breemc"] if_not ["mc_naked"]
        group breemc_outfit auto variant "preg" if_all ["mc_pregnant", "breemc"] if_not ["mc_naked"]



        attribute bree
        always "watch_tv_bree" if_any ["bree"]

        attribute bree_pregnant if_all ["bree_naked"] if_any ["bree"]

        attribute bree_collar if_any ["bree"]

        group multiple auto variant bree_piercings when bree
        group multiple:
            attribute bree_clit null
            attribute bree_ears null

        attribute bree_nohaircut null

        attribute bree_naked null
        group bree_outfit auto if_any ["bree"] if_not ["bree_naked"]
        group bree_outfit auto variant "preg" if_all ["bree_pregnant"] if_any ["bree"] if_not ["bree_naked"]




        group multiple:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null

        attribute mikemc
        always "watch_tv_mikemc_popcorn" if_any ["mikemc"] if_not ["nopopcorn"]


        attribute mike
        always "watch_tv_mike_popcorn" if_any ["mike"] if_not ["nopopcorn"]


        attribute sasha

        attribute sasha_haircut if_any ["sasha"]
        attribute sasha_nohaircut if_any ["sasha"]

        always "watch_tv_sasha_lineart" if_any ["sasha"]

        attribute sasha_pregnant if_all ["sasha", "sasha_naked"]

        attribute sasha_boobjob
        attribute sasha_noboobjob null
        always "watch_tv_sasha_boobjob" if_all ["sasha", "sasha_boobjob", "sasha_naked"]

        attribute sasha_collar if_any ["sasha"]

        group multiple auto variant sasha_piercings when sasha
        group multiple:
            attribute sasha_lips null
            attribute sasha_tongue null
        group multiple auto variant sasha_piercings_bb when sasha and sasha_boobjob
        group multiple auto variant sasha_piercings_notbb when sasha and not sasha_boobjob

        attribute sasha_naked null
        group sasha_outfit auto if_any ["sasha"] if_not ["sasha_naked"]
        group sasha_outfit auto variant "preg" if_all ["sasha", "sasha_pregnant"] if_not ["sasha_naked"]
        group sasha_outfit auto variant "bb" if_all ["sasha", "sasha_boobjob"] if_not ["sasha_naked"]


        attribute samantha

        attribute samantha_pregnant if_all ["samantha", "samantha_naked"]

        attribute samantha_collar if_any ["samantha"]

        group multiple auto variant samantha_piercings when samantha
        group multiple:
            attribute samantha_clit null
            attribute samantha_ears null
            attribute samantha_tongue null

        attribute samantha_nohaircut null

        attribute samantha_naked null
        group samantha_outfit auto if_any ["samantha"] if_not ["samantha_naked"]
        group samantha_outfit auto variant "preg" if_all ["samantha", "samantha_pregnant"] if_not ["samantha_naked"]


        attribute minami

        attribute minami_pregnant if_all ["minami", "minami_naked"]

        attribute minami_haircut if_any ["minami"]
        attribute minami_nohaircut if_any ["minami"]

        attribute minami_collar if_any ["minami"]

        group multiple auto variant minami_piercings when minami
        group multiple:
            attribute minami_ears null
            attribute minami_navel null
            attribute minami_pregnant_navel null

        attribute minami_naked null
        group minami_outfit auto if_any ["minami"] if_not ["minami_naked"]
        group minami_outfit auto variant "preg" if_all ["minami", "minami_pregnant"] if_not ["minami_naked"]


        attribute lexi

        attribute lexi_pregnant if_any ["lexi"]

        attribute lexi_collar if_any ["lexi"]

        group multiple auto variant lexi_piercings when lexi
        group multiple:
            attribute lexi_clit null
            attribute lexi_tongue null

        attribute lexi_nohaircut null

        attribute lexi_naked null
        group lexi_outfit auto if_any ["lexi"] if_not ["lexi_naked"]
        group lexi_outfit auto variant "preg" if_all ["lexi", "lexi_pregnant"] if_not ["lexi_naked"]


        always "watch_tv_bottom_popcorn" if_any ["minami", "samantha", "lexi"]








    layeredimage watch date tv:
        attribute_function Pickers([CG_WatchDateTV_Picker, PregnancyPicker, CollarPicker, HaircutPicker, OutfitPicker, PiercingsPicker, MCCGPicker], clear_npc=True)

        attribute mikemc null
        attribute breemc null

        group bg auto


        attribute mc_haircut null
        attribute mc_nohaircut null
        group mikemc auto variant "haircut" if_all ["mikemc", "mc_haircut"]
        group mikemc auto variant "nohaircut" if_all ["mikemc"] if_not "mc_haircut"
        group breemc auto variant "haircut" if_all ["breemc", "mc_haircut"]
        group breemc auto variant "nohaircut" if_all ["breemc"] if_not "mc_haircut"


        group npc auto


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute boobjob null
        group boobjob auto if_any ["boobjob"]


        attribute makeup null
        group makeup auto if_any ["makeup"]


        attribute haircut null
        attribute nohaircut null
        group haircut auto if_all ["haircut"] if_any ["camila", "morgan", "sasha", "bree"]
        group nohaircut auto if_all ["nohaircut"] if_any ["camila", "morgan", "sasha"]


        attribute naked null
        group outfit auto if_not ["naked"]
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["naked"]
        group outfit auto variant "boobjob" if_any ["boobjob"] if_not ["naked"]


        attribute collar null
        group collar auto if_any ["collar"]



        attribute lips null
        group lips auto if_any ["lips"]

        attribute tongue null
        group tongue auto if_any ["tongue"]

        attribute nipples null
        group nipples auto if_all ["nipples", "naked"]
        group nipples auto variant "bb" if_all ["nipples", "naked", "boobjob"]
        group nipples auto variant "notbb" if_all ["nipples", "naked"] if_not ["boobjob"]

        attribute nose null
        group nose auto if_any ["nose"]

        attribute ears null
        group ears auto if_any ["ears"]

        attribute clit null
        group clit auto if_all ["clit", "naked"]

        attribute navel null
        attribute pregnant_navel null
        group navel auto if_any ["navel"]
        group navel auto variant "naked" if_all ["navel", "naked"]
        group pregnant_navel auto if_any ["pregnant_navel"]
        group pregnant_navel auto variant "naked" if_all ["pregnant_navel", "naked"]

        attribute eyebrow null
        group eyebrow auto if_any ["eyebrow"]


        group haircut auto if_any ["haircut"] if_not ["camila", "morgan", "sasha"]
        group nohaircut auto if_any ["nohaircut"] if_not ["camila", "morgan", "sasha"]


        group outfits auto if_any ["reona"] if_not "pregnant"
        group outfits auto variant "pregnant" if_all ["reona", "pregnant"]


        group bot auto if_any ["morgan"]
        group bot auto variant "pregnant" if_all ["morgan", "pregnant"]


        group top auto if_any ["morgan"]
        group top auto variant "pregnant" if_all ["morgan", "pregnant"]

        group glasses auto


        group popcorn auto


        group fg auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
