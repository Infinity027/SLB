init python:
    class RestaurantMealPositionPicker(object):
        def __call__(self, attr):
            g = attr & set(p.id for p in Person.all())
            g = list(g)[0] if g else None
            if g in ["aletta", "angela", "audrey", "camila", "hanna", "jack", "master", "minami", "samantha", "victor", "amy", "kat", "reona", "cherie", "claire", "kiara"]:
                attr.add("pose01")
            elif g in ["alexis", "cassidy", "harmony", "lavish", "morgan", "sasha", "scottie", "shawn", "danny"]:
                attr.add("pose02")
            elif g in ["anna", "bree", "emma", "kleio", "lexi", "palla", "shiori", "ryan", "dwayne", "mike"]:
                attr.add("pose03")
            exp = attr & {"bored", "blush", "happy"}
            if exp:
                attr.add(g + list(exp)[0])
            else:
                attr.add(g + "normal")
            if enable_debug_picker:
                renpy.log(f"RestaurantMealPositionPicker results: {attr}")
            return attr
init 1:
    layeredimage restaurant meal:
        attribute_function MultiPickers([PregnancyPicker, PiercingsPicker, HaircutPicker, CollarPicker, OutfitPicker, MCGenderPicker, RestaurantMealPositionPicker], add_simple_pregnant_attribute=True, append_npc_from_attributes=True)

        attribute hold null
        attribute waiter null
        attribute nonpc null
        attribute nomc null
        attribute nomeals null
        attribute happy null
        attribute bored null
        attribute blush null
        attribute closed null
        attribute date null
        attribute sexydate null

        group bg auto

        group npc auto if_not "nonpc"
        group npc auto variant "pregnant" if_any "pregnant" if_not "nonpc"

        group multiple auto variant exp when not nonpc

        attribute morgan_makeup null
        group makeup auto if_any "morgan_makeup" if_not "nonpc"

        group collars auto if_not "nonpc"

        group multiple auto variant piercings when not nonpc

        group arms auto variant "normal" if_not ["hold", "askbill", "nonpc"]
        group arms auto variant "under" if_any "hold" if_not "nonpc"
        group arms auto variant "askbill" if_any "askbill" if_not "nonpc"

        group outfits auto if_not "nonpc"
        group outfits auto variant "pregnant" if_any "pregnant" if_not "nonpc"

        group bot_outfits auto if_not "nonpc"
        group bot_outfits auto variant "pregnant" if_any "pregnant" if_not "nonpc"

        group top_outfits auto if_not "nonpc"
        group top_outfits auto variant "pregnant" if_any "pregnant" if_not "nonpc"

        group haircuts auto if_not ["camila", "nonpc"]
        group haircuts auto if_any ["camila"] if_not ["camila_sluttydate", "nonpc"]


        group table auto

        group meals auto if_not ["nomeals"]
        group table_bottom auto
        group outfits auto variant "boobjob" if_any "sasha_boobjob" if_not "nonpc"
        group arms_outfits auto variant "normal" if_not ["hold", "askbill", "nonpc"]
        group arms_outfits auto variant "under" if_any "hold" if_not "nonpc"
        group arms_outfits auto variant "askbill" if_any "askbill" if_not "nonpc"

        group table_outfit auto variant "pregnant" if_any "pregnant" if_not "nonpc"


        group mc auto variant "pose01" if_any "pose01" if_not "nomc"
        group meals auto variant "pose01" if_any "pose01" if_not ["nomc", "nomeals"]
        group hands auto variant "mikemc_pose01" if_all ["mikemc", "pose01"] if_not "nomc":
            attribute normal default
        group hands auto variant "breemc_pose01" if_all ["breemc", "pose01"] if_not "nomc":
            attribute normal default
        group exp_pose01 auto variant "bored" if_all ["bored", "pose01"] if_not "nomc"
        group exp_pose01 auto variant "eat" if_all ["eat", "pose01"] if_not "nomc"


        group mc auto variant "pose02" if_any "pose02" if_not "nomc"
        group table auto variant "pose02" if_any "pose02" if_not "nomc"
        group lefthand auto variant "breemc_pose02" if_all ["breemc", "pose02"] if_not "nomc":
            attribute normal default
        group lefthand auto variant "mikemc_pose02" if_all ["mikemc", "pose02"] if_not "nomc":
            attribute normal default
        group meals auto variant "pose02" if_any "pose02" if_not ["nomeals"]
        group righthand auto variant "mikemc_pose02" if_all ["mikemc", "pose02"] if_not "nomc":
            attribute normal default

        group righthand auto variant "breemc_pose02" if_all ["breemc", "pose02"] if_not "nomc":
            attribute normal default
        group exp_pose02 auto variant "bored" if_all ["bored", "pose02"] if_not "nomc"
        group exp_pose02 auto variant "eat" if_all ["eat", "pose02"] if_not "nomc"


        group mc auto variant "pose03" if_any "pose03" if_not "nomc"
        group meals auto variant "pose03" if_any "pose03" if_not ["nomc", "nomeals"]
        group hands auto variant "mikemc_pose03" if_all ["mikemc", "pose03"] if_not "nomc":
            attribute normal default
        group hands auto variant "breemc_pose03" if_all ["breemc", "pose03"] if_not "nomc":
            attribute normal default
        group exp_pose03 auto variant "bored" if_all ["bored", "pose03"] if_not "nomc"
        group exp_pose03 auto variant "eat" if_all ["eat", "pose03"] if_not "nomc"

        group fg auto
        group acc auto

        group waiter auto if_any ["waiter"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
