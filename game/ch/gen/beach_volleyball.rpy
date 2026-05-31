init python:
    class CG_BeachVolleyball_Picker(object):
        def __call__(self, attr):
            for a in attr:
                g = Person.find(a)
                if g is not None:
                    break
            if g:
                
                
                if g.id in ["cassidy", "aletta", "hanna", "ayesha", "kylie", "master", "scottie", "mike", "victor", "dwayne", "kat", "amy", "reona"]:
                    attr.update({"frontmc", "01"})
                    attr.discard("backmc")
                    attr.discard("02")
                    attr.discard("03")
                    attr.discard("04")
                elif g.id in ["sasha", "samantha", "shiori", "bree", "lavish", "shawn", "danny", "jack", "ryan"]:
                    attr.update({"frontmc", "02"})
                    attr.discard("backmc")
                    attr.discard("01")
                    attr.discard("03")
                    attr.discard("04")
                elif g.id in ["angela", "kleio", "lexi", "emma", "minami", "morgan", "camila"]:
                    attr.update({"backmc", "03"})
                    attr.discard("frontmc")
                    attr.discard("01")
                    attr.discard("02")
                    attr.discard("04")
                elif g.id in ["palla", "audrey", "alexis", "anna", "harmony", "cherie", "claire", "kiara"]:
                    attr.update({"backmc", "04"})
                    attr.discard("frontmc")
                    attr.discard("01")
                    attr.discard("02")
                    attr.discard("03")
            
            if enable_debug_picker:
                renpy.log(f"CG_BeachVolleyball_Picker results: {attr}")
            return attr

init 1:
    layeredimage beach volleyball:
        attribute_function Pickers([PubesPicker, PregnancyPicker, CollarPicker, HaircutPicker, OutfitPicker, PiercingsPicker, MCCGPicker, CG_BeachVolleyball_Picker], clear_npc=True)

        attribute mc_naked null


        group bg auto


        attribute backmc null
        group back auto if_not ["backmc"]
        group back auto variant "haircut" if_not ["haircut", "backmc"]
        group back auto variant "nohaircut" if_any ["haircut"] if_not ["backmc"]


        group back auto variant "black" if_not ["haircut", "backmc"]
        group back auto variant "blonde" if_any ["haircut"] if_not ["backmc"]


        group back auto variant "mc_03" if_all ["backmc", "03"]
        group back auto variant "mc_04" if_all ["backmc", "04"]

        attribute mc_swimsuit null
        group back auto variant "mc_03_normal" if_all ["backmc", "03", "mc_swimsuit"] if_not ["mc_naked"]
        group back auto variant "mc_04_normal" if_all ["backmc", "04", "mc_swimsuit"] if_not ["mc_naked"]

        group back auto variant "mc_03_naked_mikemc" if_all ["backmc", "03", "mc_naked", "mikemc"]
        group back auto variant "mc_04_naked_mikemc" if_all ["backmc", "04", "mc_naked", "mikemc"]

        group front auto variant "mc_03_swimsuit" if_all ["backmc", "03", "mc_swimsuit"] if_not ["mc_naked"]
        group front auto variant "mc_04_swimsuit" if_all ["backmc", "04", "mc_swimsuit"] if_not ["mc_naked"]

        attribute mc_sexyswimsuit null
        group front auto variant "mc_03_sexyswimsuit" if_all ["backmc", "03", "mc_sexyswimsuit"] if_not ["mc_naked"]
        group front auto variant "mc_04_sexyswimsuit" if_all ["backmc", "04", "mc_sexyswimsuit"] if_not ["mc_naked"]


        attribute boobjob null
        group bb auto if_any ["boobjob"]



        attribute lips null
        group lips auto if_any ["lips"] if_not ["backmc"]

        attribute tongue null
        group tongue auto if_any ["tongue"] if_not ["backmc"]

        attribute nipples null
        group nipples auto if_any ["nipples"] if_not ["backmc", "boobjob"]
        group nipples_bb auto if_all ["nipples", "boobjob"] if_not ["backmc"]

        attribute nose null
        group nose auto if_any ["nose"] if_not ["backmc"]

        attribute ears null
        group ears auto if_any ["ears"] if_not ["backmc"]

        attribute clit null
        group clit auto if_any ["clit"] if_not ["backmc"]

        attribute navel null
        group navel auto if_any ["navel"] if_not ["backmc", "pregnant"]

        attribute eyebrow null
        group eyebrow auto if_any ["eyebrow"] if_not ["backmc"]

        attribute pubes null
        group pubes auto if_all ["pubes", "naked"]

        attribute armpits null
        group armpits auto if_all ["armpits"]


        attribute pregnant null
        group pregnant auto if_all ["pregnant", "naked"] if_not ["backmc"]


        attribute naked null

        attribute swimsuit null default
        group swimsuit auto if_any ["swimsuit"] if_not ["backmc", "pregnant", "boobjob", "naked"]
        group swimsuit auto variant "pregnant" if_all ["swimsuit", "pregnant"] if_not ["backmc", "boobjob", "naked"]
        group swimsuit auto variant "bb" if_all ["swimsuit", "boobjob"] if_not ["backmc", "pregnant", "naked"]
        group swimsuit auto variant "pregnant_bb" if_all ["swimsuit", "pregnant", "boobjob"] if_not ["backmc", "naked"]

        attribute sexyswimsuit null
        group sexyswimsuit auto if_any ["sexyswimsuit"] if_not ["backmc", "pregnant", "boobjob", "naked"]
        group sexyswimsuit auto variant "pregnant" if_all ["sexyswimsuit", "pregnant"] if_not ["backmc", "boobjob", "naked"]
        group sexyswimsuit auto variant "bb" if_all ["sexyswimsuit", "boobjob"] if_not ["backmc", "pregnant", "naked"]
        group sexyswimsuit auto variant "pregnant_bb" if_all ["sexyswimsuit", "pregnant", "boobjob"] if_not ["backmc", "naked"]


        group normal auto if_not ["naked", "backmc"]
        group naked auto if_any ["naked"] if_not ["backmc"]


        attribute pregnant_navel null
        group pregnant_navel auto if_all ["pregnant_navel"] if_not ["backmc"]
        group pregnant_navel auto variant "swim" if_all ["pregnant_navel"] if_any ["naked", "swimsuit"] if_not ["backmc"]
        group pregnant_navel auto variant "sexy" if_all ["pregnant_navel"] if_any ["naked", "sexyswimsuit"] if_not ["backmc"]


        attribute collar null
        group collar auto if_any ["collar"] if_not ["backmc"]


        attribute glasses null
        group glasses auto if_any ["glasses"] if_not ["backmc"]



        group ball auto variant "back" if_any ["01", "02", "04"]


        group net auto


        group ball auto variant "front" if_any ["03"]


        attribute frontmc null
        group front auto if_not ["frontmc"]


        group front auto variant "mc_01" if_all ["frontmc", "01"]
        group front auto variant "mc_02" if_all ["frontmc", "02"]

        group front auto variant "mc_01_normal" if_all ["frontmc", "01", "mc_swimsuit"] if_not ["mc_naked"]
        group front auto variant "mc_02_normal" if_all ["frontmc", "02", "mc_swimsuit"] if_not ["mc_naked"]

        group front auto variant "mc_01_naked_mikemc" if_all ["frontmc", "01", "mc_naked", "mikemc"]
        group front auto variant "mc_02_naked_mikemc" if_all ["frontmc", "02", "mc_naked", "mikemc"]

        group front auto variant "mc_01_swimsuit" if_all ["frontmc", "01", "mc_swimsuit"] if_not ["mc_naked"]
        group front auto variant "mc_02_swimsuit" if_all ["frontmc", "02", "mc_swimsuit"] if_not ["mc_naked"]

        group front auto variant "mc_01_sexyswimsuit" if_all ["frontmc", "01", "mc_sexyswimsuit"] if_not ["mc_naked"]
        group front auto variant "mc_02_sexyswimsuit" if_all ["frontmc", "02", "mc_sexyswimsuit"] if_not ["mc_naked"]



        group lips auto if_any ["lips"] if_not ["frontmc"]

        group tongue auto if_any ["tongue"] if_not ["frontmc"]

        group nipples auto if_any ["nipples"] if_not ["frontmc", "boobjob"]
        group nipples_bb auto if_all ["nipples", "boobjob"] if_not ["frontmc"]

        group nose auto if_any ["nose"] if_not ["frontmc"]

        group ears auto if_any ["ears"] if_not ["frontmc"]

        group clit auto if_any ["clit"] if_not ["frontmc"]

        group navel auto if_any ["navel"] if_not ["frontmc", "pregnant"]

        group eyebrow auto if_any ["eyebrow"] if_not ["frontmc"]


        group pregnant auto if_all ["naked", "pregnant"] if_not ["frontmc"]



        group swimsuit auto if_not ["sexyswimsuit", "frontmc", "pregnant", "boobjob", "naked"]
        group swimsuit auto variant "pregnant" if_any ["pregnant"] if_not ["sexyswimsuit", "frontmc", "boobjob", "naked"]

        group sexyswimsuit auto if_any ["sexyswimsuit"] if_not ["frontmc", "pregnant", "boobjob", "naked"]
        group sexyswimsuit auto variant "pregnant" if_all ["sexyswimsuit", "pregnant"] if_not ["frontmc", "boobjob", "naked"]


        group pregnant_navel auto if_any ["pregnant_navel"] if_not ["frontmc"]
        group pregnant_navel auto variant "swim" if_all ["pregnant_navel"] if_any ["naked", "swimsuit"] if_not ["frontmc"]
        group pregnant_navel auto variant "sexy" if_all ["pregnant_navel"] if_any ["naked", "sexyswimsuit"] if_not ["frontmc"]


        group normal auto if_not ["naked", "frontmc"]
        group naked auto if_any ["naked"] if_not ["frontmc"]
        group naked auto variant "big" if_all ["naked", "big"] if_not ["frontmc"]
        group naked auto variant "medium" if_all ["naked", "medium"] if_not ["frontmc"]
        group naked auto variant "small" if_all ["naked", "small"] if_not ["frontmc"]


        group collar auto if_any ["collar"] if_not ["frontmc"]


        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any ["haircut"] if_not ["frontmc"]
        group nohaircut auto if_any ["nohaircut"] if_not ["frontmc"]


        group frontexp auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
