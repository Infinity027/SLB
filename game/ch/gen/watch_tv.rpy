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
    layeredimage watch date tv:
        attribute_function Pickers([CG_WatchDateTV_Picker, CollarPicker, HaircutPicker, OutfitPicker,  MCCGPicker], clear_npc=True)

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

        group navel auto if_any ["navel"]
        group navel auto variant "naked" if_all ["navel", "naked"]

        attribute eyebrow null
        group eyebrow auto if_any ["eyebrow"]

        group haircut auto if_any ["haircut"] if_not ["camila", "morgan", "sasha"]
        group nohaircut auto if_any ["nohaircut"] if_not ["camila", "morgan", "sasha"]

        group outfits auto if_any ["reona"]

        group bot auto if_any ["morgan"]

        group top auto if_any ["morgan"]
  
        group glasses auto

        group popcorn auto

        group fg auto
