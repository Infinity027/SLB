init python:
    class CG_EatSnacks_Picker(object):
        def __call__(self, attr):
            if attr & {"bree", "sasha", "minami", "aletta", "shiori", "audrey", "samantha", "lexi", "mike", "scottie"}:
                attr.add("01")
                attr.discard("02")
                attr.discard("03")
                attr.discard("04")
            elif attr & {"harmony", "angela", "kleio", "ayesha", "jack", "shawn", "reona"}:
                attr.add("02")
                attr.discard("01")
                attr.discard("03")
                attr.discard("04")
            elif attr & {"palla", "lavish", "morgan", "alexis", "camila", "cassidy", "dwayne", "victor", "danny", "amy"}:
                attr.add("03")
                attr.discard("01")
                attr.discard("02")
                attr.discard("04")
            elif attr & {"emma", "hanna", "anna", "master", "ryan", "kat", "cherie", "claire", "kiara" }:
                attr.add("04")
                attr.discard("01")
                attr.discard("02")
                attr.discard("03")
            
            if enable_debug_picker:
                renpy.log(f"CG_EatSnacks_Picker results: {attr}")
            return attr

init 1:
    layeredimage eat snacks:
        attribute_function MultiPickers([PregnancyPicker, PiercingsPicker, HaircutPicker, CollarPicker, OutfitPicker, MCCGPicker, CG_EatSnacks_Picker], add_simple_pregnant_attribute=True, append_npc_from_attributes=True)

        attribute pregnant null
        attribute mikemc null
        attribute breemc null

        attribute sasha_boobjob null
        attribute sasha_noboobjob null

        group bg auto


        group mc auto variant "01" if_any "01"
        group mc auto variant "02" if_any "02"
        group mc auto variant "04" if_any "04"

        group mcoutfits_01 auto variant "mikemc" if_all ["mikemc", "01"]
        group mcoutfits_01 auto variant "breemc" if_all ["breemc", "01"]

        group mcoutfits_02 auto variant "mikemc" if_all ["mikemc", "02"]
        group mcoutfits_02 auto variant "breemc" if_all ["breemc", "02"]

        group mcoutfits_04 auto variant "mikemc" if_all ["mikemc", "04"]
        group mcoutfits_04 auto variant "breemc" if_all ["breemc", "04"]


        group npc auto
        group collars auto
        group haircuts auto

        group outfits auto
        group outfits_boobjob auto if_all ["sasha_boobjob"]
        group outfits_noboobjob auto if_all ["sasha_noboobjob"]
        group outfits_pregnant auto if_all ["pregnant"]

        group pregnancies auto

        group multiple auto variant piercings

        group bot auto
        group bot_pregnant auto if_all "morgan_pregnant"
        group top auto
        group top_pregnant auto if_all "morgan_pregnant"
        attribute morgan_makeup


        group mc auto variant "03" if_any "03"
        group mcoutfits_03 auto variant "mikemc" if_all ["mikemc", "03"]
        group mcoutfits_03 auto variant "breemc" if_all ["breemc", "03"]

        group mc_fg_03 auto if_any "03"

        group npc_snack auto
        group mc_snack auto variant "01" if_all ["01"]
        group mc_snack auto variant "02" if_all ["02"]
        group mc_snack auto variant "03" if_all ["03"]
        group mc_snack auto variant "04" if_all ["04"]

        group glasses auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
