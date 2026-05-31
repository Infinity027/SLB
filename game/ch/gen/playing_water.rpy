init python:
    class CG_PlayingWater_Picker(object):
        def __call__(self, attr):
            for a in attr:
                g = Person.find(a)
                if g is not None:
                    break
            if g:
                if g.id in ["alexis", "harmony", "kleio", "lavish", "minami", "sasha", "dwayne", "master", "shawn"]:
                    attr.add("01")
                elif g.id in ["angela", "aletta", "bree", "cassidy", "camila", "emma", "lexi", "morgan", "palla", "danny", "mike", "victor", "jack", "ryan", "scottie", "kat", "reona", "amy", "cherie", "claire", "kiara"]:
                    attr.add("02")
                elif g.id in ["anna", "audrey", "ayesha", "hanna", "kylie", "samantha", "shiori"]:
                    attr.add("03")
                
                if game.room in ["pool", "date_livingroom"]:
                    attr.add("pool")
                    if g.id == 'morgan':
                        if g.flags.sexyswimsuit:
                            attr.add("sexyswimsuit_morgan")
                        else:
                            attr.add("swimsuit")
                    else:
                        if g.flags.sexyswimsuit:
                            attr.add("sexyswimsuit")
                        else:
                            attr.add("swimsuit")
            
            if enable_debug_picker:
                renpy.log(f"CG_PlayingWater_Picker results: {attr}")
            return attr

init 1:
    layeredimage playing water:
        attribute_function MultiPickers([CG_PlayingWater_Picker, PregnancyPicker, CollarPicker, HaircutPicker, OutfitPicker, PiercingsPicker, PubesPicker, MCCGPicker], use_morgan_cg_outfits=True, append_npc_from_attributes=True, add_simple_pregnant_attribute=True)


        group bg auto variant "01" if_any ["01"]:
            attribute beach default
        group bg auto variant "02" if_any ["02"]:
            attribute beach default
        group bg auto variant "03" if_any ["03"]:
            attribute beach default


        attribute noball null
        group ball auto if_all ["01", "master"] if_not ["noball"]


        attribute mikemc null
        group mikemc if_any ["mikemc"]:
            attribute 01
            attribute 02
        attribute breemc null
        group breemc if_any ["breemc"]:
            attribute 01
            attribute 02


        group mcoutfits:
            attribute mc_naked null
            attribute mc_swimsuit null default
            attribute mc_sexyswimsuit null

        group mc_dicks auto:
            attribute mc_small null
            attribute mc_medium null
            attribute mc_big null

        group outfit_mikemc auto variant "naked" if_all ["mikemc", "mc_naked"] if_any ["01", "02"]
        group outfit_mikemc auto variant "naked_small" if_all ["mikemc", "mc_naked", "mc_small"] if_any ["01", "02"]
        group outfit_mikemc auto variant "naked_medium" if_all ["mikemc", "mc_naked", "mc_medium"] if_any ["01", "02"]
        group outfit_mikemc auto variant "naked_big" if_all ["mikemc", "mc_naked", "mc_big"] if_any ["01", "02"]
        group outfit_mikemc auto variant "normal" if_all ["mikemc", "mc_swimsuit"] if_any ["01", "02"] if_not ["mc_naked"]
        group outfit_breemc auto variant "normal" if_all ["breemc", "mc_swimsuit"] if_any ["01", "02"] if_not ["mc_naked"]
        group outfit_breemc auto variant "sexy" if_all ["breemc", "mc_sexyswimsuit"] if_any ["01", "02"] if_not ["mc_naked"]


        group splash auto


        group npc auto

        group pubes auto


        group haircuts auto


        attribute sasha_boobjob


        group collars auto


        group multiple auto variant piercings
        group piercings auto variant noboobjob when sasha_noboobjob and (naked or sasha_naked)
        group piercings auto variant boobjob when sasha_boobjob and (naked or sasha_naked)


        group pregnancies auto when naked


        attribute naked null
        group outfit auto when not naked
        group outfit auto variant pregnant when pregnant and not naked


        group outfits auto when not naked
        group outfits auto variant pregnant when pregnant and not naked
        group outfits auto variant noboobjob when sasha_noboobjob and not naked
        group outfits auto variant boobjob when sasha_boobjob and not naked
        group outfits auto variant pregnant_noboobjob when sasha_noboobjob and sasha_pregnant and not naked
        group outfits auto variant pregnant_boobjob when sasha_boobjob and sasha_pregnant and not naked

        group normal auto when not naked
        group naked auto if_any ["naked"]
        group naked auto variant "big" if_all ["big", "naked"]
        group naked auto variant "medium" if_all ["medium", "naked"]
        group naked auto variant "small" if_all ["small", "naked"]


        group piercings_swim auto when naked or swimsuit
        group piercings_sexy auto when naked or sexyswimsuit
        group pregnant_navel auto variant "notblueblack" if_all ["pregnant_navel"] if_any ["naked", "redbluebikini_morgan", "bluebikini_morgan", "sexyswimsuit_morgan"]


        attribute morgan_makeup


        group acc auto


        group mikemc if_any ["mikemc"]:
            attribute 03
        group breemc if_any ["breemc"]:
            attribute 03


        group mikemc_exp auto if_all ["mikemc", "03"]
        group breemc_exp auto if_all ["breemc", "03"]


        group outfit_mikemc auto variant "naked" if_all ["mikemc", "03", "mc_naked"]
        group outfit_mikemc auto variant "normal" if_all ["mikemc", "03", "mc_swimsuit"] if_not ["mc_naked"]
        group outfit_breemc auto variant "normal" if_all ["breemc", "mc_swimsuit", "03"] if_not ["mc_naked"]
        group outfit_breemc auto variant "sexy" if_all ["breemc", "mc_sexyswimsuit", "03"] if_not ["mc_naked"]


        group arms auto variant "03" if_any ["03"]


        group nipples auto if_all ["nipples", "shiori"]


        group mikemcarms auto if_any ["mikemc"]
        group mikemcarmsb auto if_any ["mikemc"]
        group breemcarms auto if_any ["breemc"]
        group breemcarmsb auto if_any ["breemc"]


        group armsb auto variant "03" if_any ["03"]


        group top auto when not naked


        group ball auto if_any ["01"] if_not ["master", "noball"]


        group fx auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
