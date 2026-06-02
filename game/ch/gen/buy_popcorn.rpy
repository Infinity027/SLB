init python:
    class CG_BuyPopcorn_Picker(object):
        def __call__(self, attr):
            for a in attr:
                g = Person.find(a)
                if g is not None:
                    break
            if g:
                if g.id in ["bree", "camila", "aletta", "anna", "hanna", "cassidy", "mike", "scottie"]:
                    attr.add("01")
                elif g.id in ["harmony", "angela", "alexis", "kleio", "shiori", "victor", "shawn", "amy", "kat", "reona", "claire", "cherie", "kiara"]:
                    attr.add("02")
                elif g.id in ["palla", "ayesha", "audrey", "minami", "lexi", "danny", "jack"]:
                    attr.add("03")
                elif g.id in ["morgan", "sasha", "samantha", "lavish", "emma", "ryan", "master", "dwayne"]:
                    attr.add("04")
            
            if enable_debug_picker:
                renpy.log(f"CG_BuyPopcorn_Picker results: {attr}")
            return attr

init 1:
    layeredimage buy popcorn:
        attribute_function Pickers([CG_BuyPopcorn_Picker, PregnancyPicker, CollarPicker, HaircutPicker, OutfitPicker, PiercingsPicker, MCGenderPicker], clear_npc=True)


        group bg auto


        group vendor auto


        group fg auto if_any ["04"]


        group mikemc auto if_any ["mikemc"]
        group breemc auto if_any ["breemc"]


        group outfit auto variant "mikemc" if_any ["mikemc"]
        group outfit auto variant "breemc" if_any ["breemc"]


        attribute nogirl null
        group girl auto if_not ["nogirl"]


        attribute pregnant null
        group pregnant auto if_any ["pregnant"] if_not ["nogirl"]


        group outfit auto if_not ["nogirl"]
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["nogirl"]
        group outfit auto variant "boobjob" if_any ["boobjob"] if_not ["nogirl"]


        group outfits_reona auto if_all "reona"
        group outfits_reona auto variant "pregnant" if_all ["pregnant", "reona"]



        group top_morgan auto if_all ["morgan"] if_not ["pregnant", "nogirl"]
        group bot_morgan auto if_all ["morgan"] if_not ["pregnant", "nogirl"]
        group top_morgan auto variant "pregnant" if_all ["morgan", "pregnant"] if_not ["nogirl"]
        group bot_morgan auto variant "pregnant" if_all ["morgan", "pregnant"] if_not ["nogirl"]


        attribute collar null
        group collar auto if_any ["collar"] if_not ["nogirl"]


        attribute makeup null
        group makeup auto if_any ["makeup"] if_not ["nogirl"]


        attribute haircut null
        attribute nohaircut null
        group haircut auto if_all ["haircut"] if_not ["camila", "minami", "morgan", "nogirl"]
        group nohaircut auto if_all ["nohaircut"] if_not ["camila", "minami", "morgan", "nogirl"]



        attribute lips null
        group lips auto if_any ["lips"] if_not ["nogirl"]

        attribute tongue null
        group tongue auto if_any ["tongue"] if_not ["nogirl"]

        attribute nipples null
        group nipples auto if_any ["nipples"] if_not ["boobjob", "shiori", "nogirl"]
        group nipples_bb auto if_all ["nipples", "boobjob"] if_not ["nogirl"]

        attribute nose null
        group nose auto if_any ["nose"] if_not ["nogirl"]

        attribute ears null
        group ears auto if_any ["ears"] if_not ["nogirl"]

        attribute clit null
        group clit auto if_any ["clit"] if_not ["nogirl"]

        attribute navel null
        attribute pregnant_navel null
        group navel auto if_any ["navel"] if_not ["nogirl", "purecasual"]
        group pregnant_navel auto if_any ["pregnant_navel"] if_not ["nogirl", "purecasual"]

        attribute eyebrow null
        group eyebrow auto if_any ["eyebrow"] if_not ["nogirl"]


        group nohaircut auto if_all ["nohaircut"] if_any ["camila", "minami", "morgan", "reona"] if_not ["nogirl"]
        group haircut auto if_all ["haircut"] if_any ["camila", "minami", "morgan", "reona"] if_not ["nogirl"]

        group acc auto


        group fg auto if_not ["04"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
