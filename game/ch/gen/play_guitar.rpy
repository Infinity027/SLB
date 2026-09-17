init python:
    class CG_PlayGuitar_Picker(object):
        def __call__(self, attr):
            if attr & {"bree", "sasha", "aletta", "audrey", "lexi"}:
                attr.add("01")
            elif attr & {"palla", "minami", "harmony", "camila", "kleio", "cherie", "claire", "kiara"}:
                attr.add("02")
            elif attr & {"anna", "hanna", "angela", "shiori", "lavish", "emma", "kat", "amy", "reona"}:
                attr.add("03")
            elif attr & {"morgan", "alexis", "cassidy", "samantha"}:
                attr.add("04")
            
            if enable_debug_picker:
                renpy.log(f"CG_PlayGuitar_Picker results: {attr}")
            return attr

init 1:
    layeredimage play guitar:
        attribute_function Pickers([CG_PlayGuitar_Picker, CollarPicker, HaircutPicker, OutfitPicker,  MCGenderPicker], clear_npc=True)

        group bg auto

        attribute mikemc null
        group mikemc auto if_any ["mikemc"] if_not ["03"]

        group npc auto

        attribute boobjob null
        group boobjob auto if_any ["boobjob"]

        attribute naked null
        attribute casual null
        group outfit auto if_not ["naked"]
        group outfit auto variant "boobjob" if_any ["boobjob"] if_not ["naked"]

        group outfit_reona auto if_all "reona" if_not ["naked"]

        group bot auto if_all "morgan" if_not ["naked"]
        group top auto if_all "morgan" if_not ["naked"]

        attribute collar null
        group collar auto if_any ["collar"]

        attribute makeup null
        group makeup auto if_any ["makeup"]

        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any ["haircut"]
        group nohaircut auto if_any ["nohaircut"]

        attribute lips null
        group lips auto if_any ["lips"]

        attribute tongue null
        group tongue auto if_any ["tongue"]

        attribute nose null
        group nose auto if_any ["nose"]

        attribute ears null
        group ears auto if_any ["ears"]

        attribute navel null
        group navel auto variant "naked" if_all ["navel", "naked"]
 
        attribute eyebrow null
        group eyebrow auto if_any ["eyebrow"]

        attribute nipples null
        group nipples auto if_all ["nipples", "naked"]
        group nipples auto variant "bb" if_all ["nipples", "naked", "boobjob"]
        group nipples auto variant "notbb" if_all ["nipples", "naked"] if_not ["boobjob"]

        group glasses auto

        group mikemc auto if_all ["mikemc", "03"]
