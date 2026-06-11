init python:
    class CG_PlayConsole_Picker(object):
        def __call__(self, attr):
            if attr & {"bree", "camila", "aletta", "anna", "hanna", "cassidy", "mike", "scottie", "dwayne"}:
                attr.add("01")
            elif attr & {"harmony", "angela", "alexis", "kleio", "shiori", "master", "ryan"}:
                attr.add("02")
            elif attr & {"palla", "audrey", "minami", "lexi", "victor", "shawn", "amy", "kat", "reona", "cherie", "claire", "kiara"}:
                attr.add("03")
            elif attr & {"morgan", "samantha", "lavish", "emma", "sasha", "danny", "jack"}:
                attr.add("04")
            
            if enable_debug_picker:
                renpy.log(f"CG_PlayConsole_Picker results: {attr}")
            return attr

init 1:
    layeredimage play console:
        attribute_function Pickers([CG_PlayConsole_Picker, PregnancyPicker, CollarPicker, HaircutPicker, OutfitPicker, PiercingsPicker, MCGenderPicker], clear_npc=True)

        attribute mcalone null
        attribute nomike null
        attribute nobree null


        group bg auto


        attribute mikemc null
        attribute breemc null
        group mikemc auto if_any ["mikemc"] if_not "nomike"
        group breemc auto if_any ["breemc"] if_not "nobree"


        group npc auto if_not "mcalone"


        group haircut auto if_all ["haircut", "sasha"] if_not "mcalone"


        attribute pregnant null
        group pregnant auto if_all ["pregnant"] if_not "mcalone"


        attribute boobjob null
        group boobjob auto if_all ["boobjob", "naked"] if_not "mcalone"


        attribute makeup null
        group makeup auto if_any ["makeup"] if_not "mcalone"



        attribute lips null
        group lips auto if_any ["lips"] if_not "mcalone"

        attribute tongue null
        group tongue auto if_any ["tongue"] if_not "mcalone"

        attribute nose null
        group nose auto if_any ["nose"] if_not "mcalone"

        attribute ears null
        group ears auto if_any ["ears"] if_not "mcalone"

        attribute navel null
        attribute pregnant_navel null
        group navel auto if_any ["navel"] if_not "mcalone"
        group pregnant_navel auto if_any ["pregnant_navel"] if_not "mcalone"

        attribute eyebrow null
        group eyebrow auto if_any ["eyebrow"] if_not "mcalone"

        attribute nipples null
        group nipples auto if_any ["nipples"] if_not "mcalone"
        group nipples auto variant "bb" if_all ["nipples", "boobjob"] if_not "mcalone"
        group nipples auto variant "notbb" if_any ["nipples"] if_not ["boobjob", "mcalone"]

        attribute clit null
        group clit auto if_any ["clit"] if_not "mcalone"


        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any ["haircut"] if_not "mcalone"
        group nohaircut auto if_any ["nohaircut"] if_not "mcalone"


        attribute naked null
        attribute casual null
        group outfit auto if_not ["naked", "mcalone"]
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["naked", "mcalone"]


        group outfit_reona auto if_all "reona" if_not ["naked", "mcalone"]
        group outfit_reona auto variant "pregnant" if_all ["reona", "pregnant"] if_not ["naked", "mcalone"]


        group outfit auto variant "boobjob" if_any ["boobjob"] if_not ["naked", "mcalone"]


        group top auto if_all "morgan" if_not ["naked", "mcalone"]
        group top auto variant "pregnant" if_all ["morgan", "pregnant"] if_not ["naked", "mcalone"]
        group bot auto if_all ["morgan"] if_not ["naked", "mcalone"]


        attribute necklace null
        attribute collar null
        group collar auto if_any ["collar"] if_not "mcalone"

        group glasses auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
